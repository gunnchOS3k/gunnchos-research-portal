#!/usr/bin/env python3
"""gunnchosctl surfaces — inventory, audit, build, and acceptance for staging Workers.

Reads the checked-in catalog. Live HTTP and GitHub lookups are best-effort.
This tool does not change DNS, attach custom domains, or merge pull requests.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = Path(__file__).resolve().parent / "catalog.json"
OWNER = "gunnchOS3k"
FIELDS = [
    "repo",
    "pr",
    "classification",
    "worker_name",
    "worker_url",
    "source_ref",
    "source_sha",
    "deployment_sha_or_id",
    "http_status",
    "primary_action",
    "primary_action_status",
    "return_nav",
    "mobile_smoke",
    "console_error_count",
    "broken_link_count",
    "accessibility_serious_critical_count",
    "generic_status_only",
    "truth_boundary_pass",
    "source_provenance_present",
    "runtime_kind",
    "runtime_boot_pass",
    "large_asset_backend",
    "custom_domain_attached",
    "dns_changed",
    "paid_plan_changed",
]

ACCEPTED_DO_NOT_REDEPLOY = {
    "gunnchos-site",
    "3k-mlv",
    "waike-campus",
    "archive-of-life",
    "beatlink-party",
    "finds-worker",
    "finds-web",
}


def catalog() -> list[dict[str, Any]]:
    rows = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    for row in rows:
        row["worker_url"] = f"https://{row['worker_name']}.gunnchos-finds.workers.dev"
        row["source_ref"] = "surface/staging-worker"
        row.setdefault("pr", None)
    return rows


def out_dir(path: str | None) -> Path:
    dest = Path(path) if path else ROOT / "artifacts" / "surfaces" / "latest"
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "screenshots").mkdir(exist_ok=True)
    (dest / "console").mkdir(exist_ok=True)
    (dest / "network").mkdir(exist_ok=True)
    (dest / "accessibility").mkdir(exist_ok=True)
    return dest


def _http_get(url: str, timeout: float = 20) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "gunnchosctl-surfaces"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            body = res.read(400_000).decode("utf-8", errors="replace")
            return int(res.status), body
    except urllib.error.HTTPError as exc:
        body = exc.read(80_000).decode("utf-8", errors="replace")
        return int(exc.code), body
    except Exception as exc:
        return 0, str(exc)


def _gh_pr(repo: str, number: int) -> dict[str, Any]:
    try:
        raw = subprocess.check_output(
            [
                "gh",
                "pr",
                "view",
                str(number),
                "--repo",
                f"{OWNER}/{repo}",
                "--json",
                "headRefOid,isDraft,state,url",
            ],
            text=True,
            stderr=subprocess.DEVNULL,
            timeout=30,
        )
        return json.loads(raw)
    except Exception:
        return {}


def inventory(dest: Path, live: bool) -> list[dict[str, Any]]:
    rows = []
    for item in catalog():
        pr = _gh_pr(item["repo"], int(item["pr"])) if live else {}
        rows.append(
            {
                "repo": item["repo"],
                "pr": item["pr"],
                "pr_url": pr.get("url") or f"https://github.com/{OWNER}/{item['repo']}/pull/{item['pr']}",
                "classification": item["classification"],
                "worker_name": item["worker_name"],
                "worker_url": item["worker_url"],
                "source_ref": item["source_ref"],
                "source_sha": pr.get("headRefOid"),
                "pr_state": pr.get("state"),
                "is_draft": pr.get("isDraft"),
                "merge_authorized": False,
                "custom_domain_attached": False,
                "dns_changed": False,
                "paid_plan_changed": False,
                "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            }
        )
    (dest / "SURFACE_INVENTORY.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    return rows


def _judge(item: dict[str, Any], status: int, html: str) -> dict[str, Any]:
    lowered = html.lower()
    v2 = 'data-surfacekit="v2"' in html
    generic = (not v2) and ("what is this?" in lowered)
    primary_present = 'id="primary-action"' in html
    return_nav = 'aria-label="Return to gunnchOS"' in html and "← gunnchOS" in html
    provenance = "<code>" in html and "source repository" in lowered
    mobile = "@media (max-width: 800px)" in html or "viewport" in lowered
    truth = "not executing here" in lowered or "research surface" in lowered or "staging_worker" in lowered
    if item["classification"].startswith("GAME") or item["classification"].startswith("HEAVY"):
        truth = "play now" not in lowered
    runtime_boot = "ANIME_WEB_RUNTIME_BOOT" in html or 'data-runtime-boot="true"' in html
    broken = 0 if status == 200 and primary_present else 1
    primary_status = "present" if primary_present and status == 200 else "missing"
    if generic:
        primary_status = "generic_status_page"
    return {
        "repo": item["repo"],
        "pr": item["pr"],
        "classification": item["classification"],
        "worker_name": item["worker_name"],
        "worker_url": item["worker_url"],
        "source_ref": item["source_ref"],
        "source_sha": None,
        "deployment_sha_or_id": None,
        "http_status": status,
        "primary_action": "primary-action" if primary_present else None,
        "primary_action_status": primary_status,
        "return_nav": return_nav,
        "mobile_smoke": "viewport" in lowered,
        "console_error_count": None,
        "broken_link_count": broken,
        "accessibility_serious_critical_count": None,
        "generic_status_only": generic,
        "truth_boundary_pass": truth and "official oulu" not in lowered,
        "source_provenance_present": provenance,
        "runtime_kind": item["classification"],
        "runtime_boot_pass": runtime_boot,
        "large_asset_backend": "r2" if "r2" in lowered else "none_observed",
        "custom_domain_attached": False,
        "dns_changed": False,
        "paid_plan_changed": False,
        "surfacekit_v2": v2,
        "mobile_css_hint": mobile,
    }


def audit(dest: Path) -> list[dict[str, Any]]:
    rows = []
    for item in catalog():
        status, html = _http_get(item["worker_url"])
        judged = _judge(item, status, html)
        (dest / "network" / f"{item['worker_name']}.http.txt").write_text(
            f"status={status}\nbytes={len(html)}\n",
            encoding="utf-8",
        )
        rows.append(judged)
    return rows


def _write_acceptance(dest: Path, rows: list[dict[str, Any]]) -> None:
    (dest / "SURFACE_ACCEPTANCE.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    with (dest / "SURFACE_MATRIX.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    generic = sum(1 for row in rows if row.get("generic_status_only"))
    broken = sum(int(row.get("broken_link_count") or 0) for row in rows)
    v2 = sum(1 for row in rows if row.get("surfacekit_v2"))
    http200 = sum(1 for row in rows if row.get("http_status") == 200)
    lines = [
        "# Surface acceptance",
        "",
        f"Recorded: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "",
        f"- Surfaces in catalog: {len(rows)}",
        f"- HTTP 200: {http200}",
        f"- SurfaceKit V2 observed: {v2}",
        f"- GENERIC_STATUS_ONLY: {generic}",
        f"- Broken primary CTA count: {broken}",
        "- Custom domains attached by this tool: false",
        "- DNS changed by this tool: false",
        "- Paid plan changed by this tool: false",
        "- Merge authorized: false",
        "",
        "A row is not complete because HTTP 200 passed. `console_error_count` and serious accessibility counts stay empty until a browser capture fills them.",
        "",
    ]
    (dest / "SURFACE_ACCEPTANCE.md").write_text("\n".join(lines), encoding="utf-8")


def find_checkout(repo: str) -> Path | None:
    roots = [
        Path("/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos"),
        Path("/Users/gunnchos/Downloads"),
        Path("/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos/_v1_continuation_worktrees"),
    ]
    for root in roots:
        candidate = root / repo
        if (candidate / ".git").exists() or (candidate / "web-surface" / "public" / "project-surface.json").exists():
            return candidate
    return None


def build_repo(repo_name: str) -> dict[str, Any]:
    checkout = find_checkout(repo_name)
    if checkout is None:
        return {"repo": repo_name, "status": "checkout_missing"}
    surface = checkout / "web-surface" / "public" / "project-surface.json"
    if not surface.exists():
        return {"repo": repo_name, "status": "web_surface_missing", "checkout": str(checkout)}
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import surfacekit_v2

    result = surfacekit_v2.write_surface(checkout)
    test = checkout / "web-surface" / "surface.test.mjs"
    if test.exists():
        proc = subprocess.run(
            ["node", "--test", str(test)],
            cwd=checkout / "web-surface",
            text=True,
            capture_output=True,
        )
        result["test_exit"] = proc.returncode
        result["test_tail"] = (proc.stdout + proc.stderr)[-500:]
    result["status"] = "built"
    result["checkout"] = str(checkout)
    return result


def smoke_urls(repos: list[str] | None, dest: Path) -> list[dict[str, Any]]:
    wanted = set(repos or [])
    rows = []
    for item in catalog():
        if wanted and item["repo"] not in wanted:
            continue
        status, html = _http_get(item["worker_url"])
        rows.append(_judge(item, status, html))
    _write_acceptance(dest, rows)
    return rows


def capture(dest: Path) -> dict[str, Any]:
    chrome = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
    note = {
        "chrome": chrome.exists(),
        "captured": [],
        "skipped": "Browser capture records HTTP-backed screenshots only. It does not mark human art or live production.",
    }
    if not chrome.exists():
        note["error"] = "chrome_missing"
        (dest / "screenshots" / "CAPTURE.json").write_text(json.dumps(note, indent=2) + "\n", encoding="utf-8")
        return note
    for item in catalog():
        png = dest / "screenshots" / f"{item['worker_name']}.png"
        proc = subprocess.run(
            [
                str(chrome),
                "--headless=new",
                "--disable-gpu",
                "--window-size=1280,900",
                f"--screenshot={png}",
                item["worker_url"],
            ],
            capture_output=True,
            text=True,
            timeout=45,
        )
        note["captured"].append({"repo": item["repo"], "exit": proc.returncode, "png": png.exists()})
        (dest / "console" / f"{item['worker_name']}.txt").write_text(
            "Headless Chrome screenshot does not export page console errors. console_error_count stays null.\n",
            encoding="utf-8",
        )
    (dest / "screenshots" / "CAPTURE.json").write_text(json.dumps(note, indent=2) + "\n", encoding="utf-8")
    return note


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="gunnchosctl surfaces")
    parser.add_argument("group", choices=["surfaces"])
    parser.add_argument("command", choices=["inventory", "audit", "build", "smoke", "capture", "acceptance"])
    parser.add_argument("--repo")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--out")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args(argv)
    dest = out_dir(args.out)
    if args.command == "inventory":
        rows = inventory(dest, live=not args.offline)
        print(f"inventory={len(rows)} out={dest}")
        return 0
    if args.command == "audit":
        rows = audit(dest)
        _write_acceptance(dest, rows)
        print(f"audit={len(rows)} generic={sum(1 for row in rows if row['generic_status_only'])} out={dest}")
        return 0
    if args.command == "build":
        if not args.repo:
            print("build requires --repo", file=sys.stderr)
            return 2
        if args.repo in ACCEPTED_DO_NOT_REDEPLOY:
            print("refusing to build an accepted worker from this command", file=sys.stderr)
            return 2
        result = build_repo(args.repo)
        print(json.dumps(result))
        return 0 if result.get("status") == "built" and result.get("test_exit", 0) == 0 else 1
    if args.command in {"smoke", "acceptance"}:
        repos = [args.repo] if args.repo else None
        if args.repo is None and not args.all and args.command == "smoke":
            print("smoke requires --repo or --all", file=sys.stderr)
            return 2
        rows = smoke_urls(repos, dest)
        print(f"{args.command}={len(rows)} out={dest}")
        return 0
    if args.command == "capture":
        if not args.all:
            print("capture requires --all", file=sys.stderr)
            return 2
        note = capture(dest)
        print(json.dumps({"captured": len(note.get("captured") or [])}))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
