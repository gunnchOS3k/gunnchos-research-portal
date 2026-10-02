#!/usr/bin/env python3
"""Live SurfaceKit shell and depth audit. Does not deploy."""

from __future__ import annotations

import csv
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = Path(__file__).resolve().parent / "catalog.json"
GENERIC_LABELS = {
    "overview",
    "what this is",
    "what is this",
    "beginner mental model",
    "what problem does this solve",
    "what exists today",
    "how this repo addresses the problem",
    "evidence status",
    "limitations",
    "methods",
    "source",
    "artifacts",
}
DOMAIN_KEYS = {
    "terrestrial_status",
    "ntn_available",
    "fallback_policy",
    "location_type",
    "site_id",
    "outage_duration_minutes",
    "ethical_framing",
}
GAME = {"HEAVY_ASSET_EXTERNAL_RUNTIME_SURFACE", "GAME_LANDING_WORKER"}
DEVELOPMENT_RUNTIME = "LIVE_DEVELOPMENT_RUNTIME"
EVIDENCE_CLASSES = (
    "MEASURED",
    "SIMULATED",
    "SYNTHETIC_SIM",
    "REFERENCE_ARCHITECTURE",
    "REFERENCE_IMPLEMENTATION",
    "LIVE_EXTERNAL_APP",
    "STATIC_PRODUCT_ARTIFACT",
    "DIRECTORY",
)


def get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "gunnchosctl-depth"})
    try:
        with urllib.request.urlopen(req, timeout=25) as res:
            return int(res.status), res.read(500_000).decode("utf-8", "replace")
    except Exception as exc:
        code = getattr(exc, "code", 0) or 0
        return int(code), str(exc)


def shell(html: str, status: int) -> dict:
    low = html.lower()
    v2 = 'data-surfacekit="v2"' in html
    primary = 'id="primary-action"' in html
    ret = 'aria-label="Return to gunnchOS"' in html and "← gunnchOS" in html
    theme = 'id="theme-toggle"' in html
    mobile = 'name="viewport"' in html
    provenance = "<code>" in html and "source repository" in low
    truth = "staging_worker" in low or "not executing here" in low or "research surface" in low
    generic = (not v2) and ("what is this?" in low)
    passed = status == 200 and v2 and primary and ret and theme and mobile and provenance and truth and not generic
    return {
        "http_status": status,
        "surfacekit_v2": v2,
        "generic_status_only": generic,
        "primary_action": primary,
        "return_nav": ret,
        "theme_control": theme,
        "mobile_viewport": mobile,
        "provenance": provenance,
        "truth_boundary": truth and "official oulu" not in low,
        "shell_pass": passed,
    }


def development_runtime(html: str, status: int, manifest: dict | None, runtime_status: int, runtime_html: str) -> dict:
    """Development boot with an exact manifest. This is not final approval."""
    manifest = manifest or {}
    files = manifest.get("files") or {}
    hrefs = re.findall(r'href="(/runtime/([0-9a-f]{40})/index\.html)"', html)
    sha = hrefs[0][1] if hrefs else ""
    exact_files = bool(files) and all(
        isinstance(item, dict) and "sha256" in item and "bytes" in item for item in files.values()
    )
    labeled = 'id="dev-label">DEVELOPMENT BUILD' in html and "STAGING_WORKER" in html
    approval_claim = "approval is true" in html.lower() or "accepted main." in html.lower() and "not accepted main" not in html.lower()
    shell_pass = (
        status == 200
        and labeled
        and 'id="primary-action"' in html
        and 'aria-label="Return to gunnchOS"' in html
        and 'name="viewport"' in html
        and "source repository" in html.lower()
        and bool(sha)
        and not approval_claim
    )
    boot = runtime_status == 200 and "DEVELOPMENT BUILD" in runtime_html
    depth_pass = (
        shell_pass
        and manifest.get("sha") == sha
        and manifest.get("label") == "DEVELOPMENT_BUILD"
        and manifest.get("channel") == "DEVELOPMENT"
        and manifest.get("acceptedMain") is False
        and exact_files
        and boot
    )
    return {
        "http_status": status,
        "surfacekit_v2": 'data-surfacekit="v2"' in html,
        "generic_status_only": False,
        "primary_action": 'id="primary-action"' in html,
        "return_nav": 'aria-label="Return to gunnchOS"' in html,
        "theme_control": 'id="theme-toggle"' in html,
        "mobile_viewport": 'name="viewport"' in html,
        "provenance": "source repository" in html.lower(),
        "truth_boundary": labeled and manifest.get("acceptedMain") is False,
        "shell_pass": shell_pass,
        "depth_pass": depth_pass,
        "depth_note": "Development runtime boots from the exact manifest. Not final approval.",
        "runtime_sha": sha,
        "runtime_boot": boot,
        "methods_nonempty": False,
        "source_list_nonempty": "source repository" in html.lower(),
        "repo_authentic_artifact_count": len(files),
        "domain_specific_interaction": depth_pass,
        "domain_specific_diagram_or_data": exact_files,
        "generic_readme_headings_only": False,
        "measured_topology": False,
        "evidence_class": "",
        "limitations_shown": "not accepted main" in html.lower() or "not a release" in html.lower(),
        "node_labels": [],
        "row_count": 0,
        "card_count": 0,
    }


def depth(classification: str, html: str, explore: dict | None) -> dict:
    explore = explore or {}
    methods = str(explore.get("methods") or "")
    artifacts = explore.get("artifacts") or []
    rows = explore.get("rows") or []
    nodes = explore.get("nodes") or []
    cards = explore.get("cards") or []
    measured = bool(explore.get("measured_topology"))
    labels = [str(n.get("label") or "").strip().lower() for n in nodes]
    generic_nodes = bool(labels) and all(label in GENERIC_LABELS or len(label) < 3 for label in labels)
    domain_keys = set()
    for row in rows:
        domain_keys.update(k for k in row if k not in {"source", "scenario_id"})
    readme_only = all(str(r.get("source") or "") == "README.md" for r in rows) if rows else True
    domain_data = bool(domain_keys & DOMAIN_KEYS) or (not generic_nodes and bool(labels)) or bool(rows and not readme_only)
    declared = re.findall(r"Evidence class:\s*([A-Z_]+)", html)
    evidence_class = next((name for name in declared if name in EVIDENCE_CLASSES), "")
    live_embed = 'id="spectrumx-streamlit-app"' in html and "embed=true" in html
    out = {
        "methods_nonempty": len(methods.strip()) > 40,
        "source_list_nonempty": "source repository" in html.lower() or bool(explore.get("sources")),
        "repo_authentic_artifact_count": len(artifacts),
        "domain_specific_interaction": ('id="row-select"' in html and bool(rows) and not readme_only) or live_embed,
        "domain_specific_diagram_or_data": (domain_data and not generic_nodes) or live_embed,
        "generic_readme_headings_only": readme_only or generic_nodes,
        "measured_topology": measured,
        "evidence_class": evidence_class,
        "limitations_shown": "limitation" in html.lower(),
        "node_labels": [n.get("label") for n in nodes],
        "row_count": len(rows),
        "card_count": len(cards),
    }
    if classification == "STATIC_RESEARCH_SURFACE_WORKER":
        class_ok = evidence_class in EVIDENCE_CLASSES and (evidence_class != "MEASURED" or measured)
        legacy_measured = (not evidence_class) and measured and not readme_only
        out["depth_pass"] = (
            out["methods_nonempty"]
            and out["source_list_nonempty"]
            and out["repo_authentic_artifact_count"] >= 1
            and out["domain_specific_interaction"]
            and out["domain_specific_diagram_or_data"]
            and out["limitations_shown"]
            and not out["generic_readme_headings_only"]
            and (class_ok or legacy_measured)
        )
    elif classification == "META_DIRECTORY_WORKER":
        entries = len(cards) or len(rows)
        out["real_directory_entries"] = entries
        out["search_control"] = 'id="row-filter"' in html
        out["filter_control"] = 'id="row-select"' in html
        out["depth_pass"] = entries > 0 and out["search_control"] and out["filter_control"]
        out["depth_note"] = "Search and filter controls are present. Entry links are repository records, not a separate crawled directory."
    elif classification == "STATIC_PRODUCT_SURFACE_WORKER":
        out["depth_pass"] = out["repo_authentic_artifact_count"] >= 1 or bool(rows)
        out["depth_note"] = "Pass requires a repo-listed artifact or record. A GLB viewer is not claimed unless that file is in the artifact list."
    elif classification == "BACKEND_CONTROL_SURFACE_WORKER":
        out["depth_pass"] = explore.get("runtime_mode") == "LOCAL/DEMO" and bool(rows)
        out["depth_note"] = "LOCAL/DEMO label with at least one repository record. No remote model call."
    elif classification in GAME:
        out["depth_pass"] = False
        out["depth_note"] = "Runtime-pending game surface. Shell upgrade is not a playable boot."
    else:
        out["depth_pass"] = False
    return out


def main() -> None:
    dest = ROOT / "artifacts" / "surfaces" / "latest"
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "screenshots").mkdir(exist_ok=True)
    (dest / "console").mkdir(exist_ok=True)
    (dest / "network").mkdir(exist_ok=True)
    catalog = json.loads(CATALOG.read_text())
    rows = []
    for item in catalog:
        url = f"https://{item['worker_name']}.gunnchos-finds.workers.dev/"
        status, html = get(url)
        exp_status, exp_body = get(url + "explore.json")
        explore = None
        if exp_status == 200:
            try:
                explore = json.loads(exp_body)
            except json.JSONDecodeError:
                explore = None
        if item["classification"] == DEVELOPMENT_RUNTIME:
            man_status, man_body = get(url + "runtime-manifest")
            manifest = None
            if man_status == 200:
                try:
                    manifest = json.loads(man_body)
                except json.JSONDecodeError:
                    manifest = None
            runtime_href = ""
            found = re.search(r'href="(/runtime/[0-9a-f]{40}/index\.html)"', html)
            if found:
                runtime_href = found.group(1)
            runtime_status, runtime_html = get(url.rstrip("/") + runtime_href) if runtime_href else (0, "")
            judged = development_runtime(html, status, manifest, runtime_status, runtime_html)
            judged_shell = judged
            judged_depth = judged
        else:
            judged_shell = shell(html, status)
            judged_depth = depth(item["classification"], html, explore)
        row = {
            "repo": item["repo"],
            "pr": item["pr"],
            "classification": item["classification"],
            "worker_name": item["worker_name"],
            "worker_url": url,
            "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "explore_http": exp_status,
            **{k: v for k, v in judged_shell.items() if k not in judged_depth or k in {
                "http_status", "surfacekit_v2", "generic_status_only", "primary_action",
                "return_nav", "theme_control", "mobile_viewport", "provenance",
                "truth_boundary", "shell_pass",
            }},
            **{k: v for k, v in judged_depth.items() if k != "node_labels"},
            "node_labels": judged_depth.get("node_labels"),
            "runtime_pending": item["classification"] in GAME,
            "redeployed_this_audit": False,
        }
        rows.append(row)
        (dest / "network" / f"{item['worker_name']}.depth.txt").write_text(
            f"status={status}\nexplore={exp_status}\nshell={judged_shell['shell_pass']}\ndepth={judged_depth['depth_pass']}\n",
            encoding="utf-8",
        )
        print(item["worker_name"], "shell", judged_shell["shell_pass"], "depth", judged_depth["depth_pass"], "generic", judged_shell["generic_status_only"])
    (dest / "SURFACE_ACCEPTANCE.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    fields = [
        "repo", "pr", "classification", "worker_url", "http_status", "shell_pass", "depth_pass",
        "generic_status_only", "methods_nonempty", "repo_authentic_artifact_count",
        "domain_specific_interaction", "domain_specific_diagram_or_data",         "generic_readme_headings_only", "evidence_class",
        "row_count", "runtime_pending",
    ]
    with (dest / "SURFACE_DEPTH_MATRIX.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    shell_n = sum(1 for r in rows if r["shell_pass"])
    depth_n = sum(1 for r in rows if r["depth_pass"])
    generic_n = sum(1 for r in rows if r["generic_status_only"])
    summary = {
        "TOTAL_STAGING_SURFACES": len(rows),
        "SURFACEKIT_SHELL_PASS": shell_n,
        "SURFACE_DEPTH_PASS": depth_n,
        "GENERIC_STATUS_ONLY": generic_n,
        "RUNTIME_PENDING": sum(1 for r in rows if r["runtime_pending"]),
        "axe": "not_in_current_surface_test_stack",
        "redeployed": False,
    }
    (dest / "DEPTH_SUMMARY.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
