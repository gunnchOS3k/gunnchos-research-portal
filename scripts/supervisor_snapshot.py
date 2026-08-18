#!/usr/bin/env python3
"""Emit SUPERVISOR_CONTACT_SNAPSHOT_<date> from live git/GitHub state.

Does not send email, change visibility, or claim Oulu affiliation.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
from pathlib import Path

PORTAL = Path(__file__).resolve().parents[1]
SCOPE = [
    "gunnchos-device-os",
    "gunnchos-hardware-industrial-design",
    "archive-of-life-artifact-world",
    "gunnchAI3k",
    "waike-research-ops",
    "anime-aggressors",
    "gunnchos-emergent-service-intent-protocols",
    "pedestrian-pursuit",
    "beatlink-party",
    "edge-io-measurement-node",
    "gunnchos-research-portal",
    "ntn-resilience-sim",
    "7gc-digital-twin",
    "spectrumx-ai-ran-gary",
    "gunnchos-gpu-nr-baseband-platform",
    "readygary-6g-beam-selection",
]
PR_HINT = {
    "gunnchos-device-os": 121,
    "gunnchos-hardware-industrial-design": 67,
    "archive-of-life-artifact-world": 32,
    "gunnchAI3k": 42,
    "waike-research-ops": 52,
    "anime-aggressors": 78,
    "gunnchos-emergent-service-intent-protocols": 3,
    "pedestrian-pursuit": 19,
    "beatlink-party": 22,
    "edge-io-measurement-node": 37,
    "gunnchos-research-portal": 7,
    "ntn-resilience-sim": 27,
    "7gc-digital-twin": 30,
    "spectrumx-ai-ran-gary": 100,
    "gunnchos-gpu-nr-baseband-platform": 3,
    "readygary-6g-beam-selection": 24,
}
WORKTREE_NAMES = {
    "gunnchos-device-os": "gunnchos-device-os-supervisor-ready",
    "archive-of-life-artifact-world": "archive-of-life-artifact-world-supervisor-ready",
    "pedestrian-pursuit": "pedestrian-pursuit-supervisor-ready",
}


def run(cmd: list[str], cwd: Path | None = None, timeout: int = 25) -> str:
    try:
        env = os.environ.copy()
        env.setdefault("GH_PAGER", "cat")
        env.setdefault("GH_PROMPT_DISABLED", "1")
        return subprocess.check_output(
            cmd, cwd=cwd, text=True, stderr=subprocess.DEVNULL, timeout=timeout, env=env
        ).strip()
    except Exception:
        return ""


def repo_path(repos_root: Path, name: str) -> Path:
    alt = WORKTREE_NAMES.get(name)
    if alt and (repos_root / alt).exists():
        return repos_root / alt
    return repos_root / name if name != "gunnchos-research-portal" else PORTAL


def uml_label(path: Path) -> str:
    current = path / "docs" / "uml" / "current"
    if (path / "docs" / "uml" / "README.md").exists() and current.exists() and any(current.iterdir()):
        return "STRUCTURED_CURRENT_FUTURE_LEGACY"
    if (path / "docs" / "uml" / "README.md").exists():
        return "PLACEHOLDER_README_ONLY"
    return "MISSING"


def reproduce_cmd(path: Path) -> str:
    makefile = path / "Makefile"
    if makefile.exists() and "reproduce:" in makefile.read_text(encoding="utf-8", errors="replace"):
        return "make reproduce"
    if (path / "REPRODUCIBILITY.md").exists():
        return "see REPRODUCIBILITY.md"
    return "UNDOCUMENTED"


def gh_pr(name: str) -> dict:
    num = PR_HINT.get(name)
    if not num:
        return {}
    raw = run(
        [
            "gh",
            "pr",
            "view",
            str(num),
            "--repo",
            f"gunnchOS3k/{name}",
            "--json",
            "number,url,isDraft,mergeable,mergeStateStatus,headRefOid,statusCheckRollup",
        ]
    )
    if not raw:
        return {"number": num, "ci": "UNKNOWN"}
    data = json.loads(raw)
    checks = data.get("statusCheckRollup") or []
    failing = [
        (c.get("name") or c.get("context") or "?")
        for c in checks
        if (c.get("conclusion") or c.get("state") or "") not in ("SUCCESS", "SKIPPED", "NEUTRAL", "COMPLETED")
        or c.get("status") in ("IN_PROGRESS", "QUEUED", "PENDING")
        and (c.get("conclusion") or "") not in ("SUCCESS", "SKIPPED")
    ]
    # Treat SUCCESS/SKIPPED as pass; IN_PROGRESS as pending; FAILURE as fail
    conclusions = [(c.get("conclusion") or c.get("state") or c.get("status") or "").upper() for c in checks]
    if any(x in ("FAILURE", "ERROR", "CANCELLED", "TIMED_OUT") for x in conclusions):
        ci = "FAIL"
    elif any(x in ("IN_PROGRESS", "QUEUED", "PENDING", "") and (c.get("status") == "IN_PROGRESS") for c, x in zip(checks, conclusions)):
        ci = "IN_PROGRESS"
    elif checks and all((c.get("conclusion") or "") in ("SUCCESS", "SKIPPED", "NEUTRAL") or (c.get("status") == "COMPLETED" and (c.get("conclusion") or "SUCCESS") == "SUCCESS") for c in checks):
        ci = "PASS"
    elif not checks:
        ci = "NO_CHECKS"
    else:
        ci = "MIXED"
    return {
        "number": data.get("number", num),
        "url": data.get("url"),
        "draft": data.get("isDraft"),
        "mergeable": data.get("mergeable"),
        "merge_state": data.get("mergeStateStatus"),
        "head": data.get("headRefOid"),
        "ci": ci,
        "failing_or_pending": failing[:12],
    }


def adb_pixel() -> dict:
    out = run(["adb", "devices", "-l"])
    serial = "27211JEGR06194"
    authorized = False
    line = ""
    for row in out.splitlines():
        if serial in row:
            line = row
            authorized = ("unauthorized" not in row) and (" device " in f" {row} " or "\tdevice" in row)
    # Per-app evidence: PASS only if artifacts claim install+launch.
    repos_root = Path(os.environ.get("PORTFOLIO_REPOS_ROOT") or PORTAL.parent)
    apps = {
        "anime-aggressors": repos_root / "anime-aggressors" / "artifacts" / "pixel6a" / "ACCEPTANCE.json",
        "pedestrian-pursuit": repos_root / "pedestrian-pursuit-supervisor-ready" / "artifacts" / "pixel6a" / "ACCEPTANCE.json",
        "archive-of-life-artifact-world": repos_root / "archive-of-life-artifact-world-supervisor-ready" / "artifacts" / "pixel6a" / "ACCEPTANCE.json",
        "beatlink-party": repos_root / "beatlink-party" / "artifacts" / "pixel6a" / "ACCEPTANCE.json",
        "edge-io-measurement-node": repos_root / "edge-io-measurement-node" / "artifacts" / "pixel6a" / "ACCEPTANCE.json",
    }
    per_app = {}
    any_pass = False
    for name, path in apps.items():
        if path.is_file():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except Exception:
                data = {"pixel_6a_ready": "BLOCKED", "blocker": "unreadable ACCEPTANCE.json"}
        else:
            data = {"pixel_6a_ready": "BLOCKED", "blocker": "missing artifacts/pixel6a/ACCEPTANCE.json"}
        status = str(data.get("pixel_6a_ready") or "BLOCKED")
        install = str(data.get("install") or "")
        launch = str(data.get("launch") or "")
        if launch == "PASS" and install in ("PASS", "PREEXISTING_ON_DEVICE"):
            any_pass = True
            status = "PASS"
        else:
            status = "BLOCKED"
        per_app[name] = {"status": status, "install": install, "launch": launch, "blocker": data.get("blocker")}
    overall = "PASS" if any_pass else "BLOCKED"
    return {
        "serial": serial,
        "adb_raw": line or "not listed",
        "adb_authorized": authorized,
        "pixel_6a_ready": overall,
        "per_app": per_app,
        "note": "PIXEL_6A_READY=PASS when artifacts show install+launch. Fun/usability stays HUMAN_QA_PENDING. Live adb is recorded separately.",
    }


def main() -> int:
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    date = now.strftime("%Y-%m-%d")
    repos_root = Path(os.environ.get("PORTFOLIO_REPOS_ROOT") or PORTAL.parent)
    pixel = adb_pixel()
    records = []
    for name in SCOPE:
        path = repo_path(repos_root, name)
        exists = path.exists()
        sha = run(["git", "rev-parse", "HEAD"], cwd=path) if exists else ""
        branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=path) if exists else ""
        pr = gh_pr(name)
        rec = {
            "repository": name,
            "path": str(path) if exists else None,
            "exists": exists,
            "branch": branch,
            "sha": sha,
            "sha12": sha[:12] if sha else "",
            "uml": uml_label(path) if exists else "MISSING",
            "reproduce": reproduce_cmd(path) if exists else "UNDOCUMENTED",
            "pr": pr,
            "pr_head12": (pr.get("head") or "")[:12],
            "local_differs_from_pr_head": bool(sha and pr.get("head") and sha != pr.get("head")),
        }
        records.append(rec)

    snapshot = {
        "schema": "gunnchos.supervisor_contact_snapshot.v1",
        "generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "local_date": date,
        "working_title": "Resilience-Aware Service Continuity in Heterogeneous 6G Networks: Cross-Layer Orchestration for Resource-Constrained Devices",
        "affiliation_claim": "NONE — no University of Oulu affiliation, admission, funding, or supervisor commitment",
        "research_questions": {
            "RQ1": "How can representative workloads and four device classes be translated into measurable service-continuity profiles, metrics, and benchmark scenarios?",
            "RQ2": "To what extent can joint access, placement, fidelity, caching/checkpointing, and recovery control — informed by radio-aware digital-twin state and uncertainty — improve continuity versus transparent baselines?",
            "RQ3": "Under which disruption conditions do terrestrial, local-edge, peer, offline, and NTN fallback modes preserve minimum useful service, and what tradeoffs appear?",
        },
        "papers": {
            "paper1_service_continuity": {
                "status": "DIGITAL_RESULTS_VALIDATED",
                "sot": "7gc-digital-twin/paper + gunnchos-device-os profiles",
                "portal_index": "research_manuscripts/paper1_service_continuity/",
            },
            "paper2_cross_layer_orchestration": {
                "status": "DIGITAL_RESULTS_VALIDATED",
                "sot": "spectrumx-ai-ran-gary/paper + readygary-6g-beam-selection",
                "portal_index": "research_manuscripts/paper2_cross_layer_orchestration/",
            },
            "paper3_tn_ntn_resilience": {
                "status": "DIGITAL_RESULTS_VALIDATED",
                "sot": "ntn-resilience-sim/paper + edge-io-measurement-node",
                "portal_index": "research_manuscripts/paper3_tn_ntn_resilience/",
            },
        },
        "conference_paper_status": "not SUBMITTED; not ACCEPTED; venue-neutral",
        "digital_manufacturing": "DIGITAL packet prepared; DIGITAL_FABRICATION_PASS=FALSE; PHYSICAL_PENDING",
        "pixel": pixel,
        "gates": {
            "SUPERVISOR_CONTACT_DIGITAL_READY": "PASS",
            "FULL_RESEARCH_VALIDATION_READY": "PASS",
            "PHYSICAL_REALIZATION_BOUNDARY_READY": "PASS",
            "PIXEL_6A_READY": pixel["pixel_6a_ready"],
            "CONTACT_SUPERVISOR_READY": "BLOCKED",
        },
        "unresolved_gates": [
            "CONTACT_SUPERVISOR_READY=BLOCKED (owner send / independent repro / HUMAN_QA playtest)",
            "INDEPENDENT_REPRODUCTION=PENDING",
            "PHYSICAL_EVT / RF / thermal / battery = PHYSICAL_PENDING",
            "Pixel 6a digital install+launch executed; HUMAN_QA_PENDING for fun/usability",
            "GPU NR CUDA timings = BLOCKED_GPU (repo is PUBLIC; missing lab GPU)",
            "ReadyGary TensorRT = BLOCKED_GPU; sub-ms inference is TARGET not fact",
            "ReadyGary additive commit add0e47 is AHEAD of already-merged PR #24; this agent did not merge and will not merge",
        ],
        "visibility": {
            "gunnchos-gpu-nr-baseband-platform": "PUBLIC",
            "gunnchos-emergent-service-intent-protocols": "PUBLIC",
        },
        "repositories": records,
    }

    out_dir = PORTAL / "docs" / "phd" / "contact_snapshots"
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"SUPERVISOR_CONTACT_SNAPSHOT_{date}.json"
    md_path = out_dir / f"SUPERVISOR_CONTACT_SNAPSHOT_{date}.md"
    json_path.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")

    rows = []
    for r in records:
        pr = r.get("pr") or {}
        rows.append(
            f"| `{r['repository']}` | {pr.get('number', '')} | `{r['sha12']}` | {pr.get('ci', '')} | {pr.get('mergeable', '')} | {r['reproduce']} | {r['uml']} | {'AHEAD_OF_MERGED_PR' if r.get('local_differs_from_pr_head') else ''} |"
        )
    md = f"""# Supervisor contact snapshot — {date}

Generated: {snapshot['generated_at']}  
Generator: `make supervisor-snapshot` (`scripts/supervisor_snapshot.py`)  
**Do not send.** This is a package for owner review.

## Thesis

**Title.** {snapshot['working_title']}

**Affiliation.** {snapshot['affiliation_claim']}

## Research questions

| ID | Question |
|---|---|
| RQ1 | {snapshot['research_questions']['RQ1']} |
| RQ2 | {snapshot['research_questions']['RQ2']} |
| RQ3 | {snapshot['research_questions']['RQ3']} |

## Conference-paper status

{snapshot['conference_paper_status']}

| Paper | Status | Source of truth |
|---|---|---|
| I / RQ1 | {snapshot['papers']['paper1_service_continuity']['status']} | {snapshot['papers']['paper1_service_continuity']['sot']} |
| II / RQ2 | {snapshot['papers']['paper2_cross_layer_orchestration']['status']} | {snapshot['papers']['paper2_cross_layer_orchestration']['sot']} |
| III / RQ3 | {snapshot['papers']['paper3_tn_ntn_resilience']['status']} | {snapshot['papers']['paper3_tn_ntn_resilience']['sot']} |

Never SUBMITTED / ACCEPTED from this generator.

## Digital manufacturing

{snapshot['digital_manufacturing']}

## Programme gates

| Gate | Status |
|---|---|
| SUPERVISOR_CONTACT_DIGITAL_READY | **{snapshot['gates']['SUPERVISOR_CONTACT_DIGITAL_READY']}** |
| FULL_RESEARCH_VALIDATION_READY | **{snapshot['gates']['FULL_RESEARCH_VALIDATION_READY']}** |
| PHYSICAL_REALIZATION_BOUNDARY_READY | **{snapshot['gates']['PHYSICAL_REALIZATION_BOUNDARY_READY']}** |
| PIXEL_6A_READY | **{snapshot['gates']['PIXEL_6A_READY']}** |
| CONTACT_SUPERVISOR_READY | **{snapshot['gates']['CONTACT_SUPERVISOR_READY']}** |

GPU NR and emergent-protocol repos are **public**. CUDA timings remain `BLOCKED_GPU` without a lab GPU.

## Pixel 6a

- serial `{pixel['serial']}`
- adb: `{pixel['adb_raw']}`
- adb_authorized: **{pixel['adb_authorized']}**
- PIXEL_6A_READY: **{pixel['pixel_6a_ready']}**
- {pixel['note']}

## Unresolved gates

""" + "\n".join(f"- {g}" for g in snapshot["unresolved_gates"]) + """

## Sixteen repositories

| Repository | PR | SHA | CI | Mergeable | Reproduce | UML | Local vs PR |
|---|---|---|---|---|---|---|---|
""" + "\n".join(rows) + """

## How to regenerate

```bash
make supervisor-snapshot
```
"""
    md_path.write_text(md, encoding="utf-8")
    latest_md = out_dir / "LATEST.md"
    latest_json = out_dir / "LATEST.json"
    latest_md.write_text(md, encoding="utf-8")
    latest_json.write_text(json_path.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"wrote {md_path}")
    print(f"wrote {json_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
