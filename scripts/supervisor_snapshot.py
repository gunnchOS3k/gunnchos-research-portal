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


def run(cmd: list[str], cwd: Path | None = None) -> str:
    try:
        return subprocess.check_output(cmd, cwd=cwd, text=True, stderr=subprocess.DEVNULL).strip()
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
            authorized = "unauthorized" not in row and "device" in row
    return {
        "serial": serial,
        "adb_raw": line or "not listed",
        "adb_authorized": authorized,
        "pixel_6a_ready": "BLOCKED",
        "note": "adb authorized is not PIXEL_6A_READY; signed acceptance session still PHYSICAL_PENDING",
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
                "status": "DIGITAL_RESULTS_AVAILABLE",
                "sot": "7gc-digital-twin/paper + gunnchos-device-os profiles",
                "portal_index": "research_manuscripts/paper1_service_continuity/",
            },
            "paper2_cross_layer_orchestration": {
                "status": "EXPERIMENT_IMPLEMENTATION",
                "sot": "spectrumx-ai-ran-gary/paper + readygary-6g-beam-selection",
                "portal_index": "research_manuscripts/paper2_cross_layer_orchestration/",
            },
            "paper3_tn_ntn_resilience": {
                "status": "DIGITAL_RESULTS_AVAILABLE",
                "sot": "ntn-resilience-sim/paper + edge-io-measurement-node",
                "portal_index": "research_manuscripts/paper3_tn_ntn_resilience/",
            },
        },
        "conference_paper_status": "not SUBMITTED; not ACCEPTED; venue-neutral",
        "digital_manufacturing": "DIGITAL packet prepared; DIGITAL_FABRICATION_PASS=FALSE; PHYSICAL_PENDING",
        "pixel": pixel,
        "unresolved_gates": [
            "CONTACT_SUPERVISOR_READY=BLOCKED",
            "INDEPENDENT_REPRODUCTION=PENDING",
            "PHYSICAL_EVT / RF / thermal / battery = PHYSICAL_PENDING",
            "two private repos visibility = EXTERNAL_PENDING",
            "Pixel 6a signed acceptance = PHYSICAL_PENDING",
            "GPU NR CUDA timings = BLOCKED_GPU",
        ],
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
            f"| `{r['repository']}` | {pr.get('number', '')} | `{r['sha12']}` | {pr.get('ci', '')} | {pr.get('mergeable', '')} | {r['reproduce']} | {r['uml']} |"
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

## Pixel 6a

- serial `{pixel['serial']}`
- adb: `{pixel['adb_raw']}`
- adb_authorized: **{pixel['adb_authorized']}**
- PIXEL_6A_READY: **{pixel['pixel_6a_ready']}**
- {pixel['note']}

## Unresolved gates

""" + "\n".join(f"- {g}" for g in snapshot["unresolved_gates"]) + """

## Sixteen repositories

| Repository | PR | SHA | CI | Mergeable | Reproduce | UML |
|---|---|---|---|---|---|---|
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
