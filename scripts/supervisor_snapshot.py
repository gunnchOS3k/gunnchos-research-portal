#!/usr/bin/env python3
"""Emit SUPERVISOR_CONTACT_SNAPSHOT_<date> from live git/GitHub + Baseline V2 truth.

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
BASELINE_V2_DIR = PORTAL / "artifacts" / "baseline_v2"
SPINE_ACCEPTED_MAIN = Path(
    os.environ.get(
        "GUNNCHOS_ACCEPTED_MAIN_JSON",
        PORTAL.parent.parent / "program" / "residual_closure_2026_08" / "CURRENT_ACCEPTED_MAIN.json",
    )
)
B4_FREEZE = Path(
    os.environ.get(
        "GUNNCHOS_B4_SHA_FREEZE_JSON",
        BASELINE_V2_DIR / "B4_ACCEPTED_MAIN_SHA_FREEZE.json",
    )
)
BASELINE_V2_RESULT = BASELINE_V2_DIR / "BASELINE_V2_RESULT.json"
FIELD_KIT_REPO = "gunnchos-7gc-ai-ran-field-kit"
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
    "gunnchos-device-os": 122,
    "gunnchos-hardware-industrial-design": 67,
    "archive-of-life-artifact-world": 33,
    "gunnchAI3k": 43,
    "waike-research-ops": 54,
    "anime-aggressors": 79,
    "gunnchos-emergent-service-intent-protocols": 3,
    "pedestrian-pursuit": 20,
    "beatlink-party": 23,
    "edge-io-measurement-node": 38,
    "gunnchos-research-portal": 9,
    "ntn-resilience-sim": 27,
    "7gc-digital-twin": 30,
    "spectrumx-ai-ran-gary": 101,
    "gunnchos-gpu-nr-baseband-platform": 3,
    "readygary-6g-beam-selection": 27,
}
PHYSICAL_PENDING = [
    "hardware EVT / RF / thermal / battery",
    "R6G OTA / carrier / SDR",
    "DIGITAL_FABRICATION_PASS external ballmaps",
]
HUMAN_PENDING = [
    "CONTACT_SUPERVISOR_READY owner send",
    "game fun/balance/feel HUMAN_QA",
    "SEVEN_GC_APPRENTICESHIP research overlay",
]
EXTERNAL_PENDING = [
    "INDEPENDENT_REPRODUCTION",
    "NVIDIA Aerial/AODT/Sionna backends",
    "DOI/PDF pins",
    "GPU NR CUDA timings BLOCKED_GPU",
]
ACCEPTED_MAIN_CONVERGENCE = [
    {
        "repository": FIELD_KIT_REPO,
        "pr": 89,
        "state": "MERGED",
        "note": "Baseline V2 B.3 precision/provenance correction",
    },
    {
        "repository": FIELD_KIT_REPO,
        "pr": 90,
        "state": "MERGED",
        "note": "Baseline V2 B.4.1 evidence-mapping convergence (accepted-main SoT)",
    },
    {
        "repository": "waike-research-ops",
        "pr": 53,
        "state": "MERGED",
        "note": "batch007 EMBEDDED_PROTOTYPING + GUNNCHOS_PRODUCT_LAB",
    },
    {
        "repository": FIELD_KIT_REPO,
        "pr": 88,
        "state": "MERGED",
        "note": "residual digital closure Phase 0 follow-up",
    },
    {
        "repository": "gunnchos-device-os",
        "pr": 103,
        "state": "CLOSED",
        "merged": False,
        "note": "SUPERSEDED — do not merge; replaced by #108/#116 lineage on accepted main",
    },
]
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


def load_json(path: Path) -> dict:
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def load_accepted_main() -> dict[str, dict]:
    freeze = load_json(B4_FREEZE)
    repos = freeze.get("repos") or []
    if repos:
        out: dict[str, dict] = {}
        for row in repos:
            name = row.get("repository") or ""
            sha = row.get("origin_main_sha") or ""
            if name and sha:
                out[name] = {"sha": sha, "source": str(B4_FREEZE)}
        if out:
            return out
    if not SPINE_ACCEPTED_MAIN.is_file():
        return {}
    try:
        data = json.loads(SPINE_ACCEPTED_MAIN.read_text(encoding="utf-8"))
        return data.get("repos") or {}
    except Exception:
        return {}


def load_baseline_v2_totals() -> dict:
    data = load_json(BASELINE_V2_RESULT)
    return data.get("totals") or {}


def disposition_for(name: str, accepted: dict, origin_sha: str) -> str:
    pin = accepted.get(name) or {}
    if pin.get("sha") and origin_sha and pin["sha"] == origin_sha:
        return "ACCEPTED_MAIN"
    if pin.get("sha") and origin_sha:
        return "ACCEPTED_MAIN_DRIFT"
    return "UNKNOWN"


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


def origin_main_sha(path: Path) -> str:
    if not path.exists():
        return ""
    run(["git", "fetch", "origin", "main"], cwd=path)
    return run(["git", "rev-parse", "origin/main"], cwd=path)


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
            "number,url,isDraft,mergeable,mergeStateStatus,headRefOid,statusCheckRollup,state,mergedAt",
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
    non_blocking = {"SUCCESS", "SKIPPED", "NEUTRAL", "CANCELLED", "COMPLETED", ""}
    conclusions = [(c.get("conclusion") or c.get("state") or c.get("status") or "").upper() for c in checks]
    if any(x in ("FAILURE", "ERROR", "TIMED_OUT") for x in conclusions):
        ci = "FAIL"
    elif any(c.get("status") == "IN_PROGRESS" for c in checks):
        ci = "IN_PROGRESS"
    elif checks and all(x in non_blocking for x in conclusions):
        ci = "PASS"
    elif not checks:
        ci = "NO_CHECKS"
    else:
        ci = "MIXED"
    if ci in ("FAIL", "MIXED", "NO_CHECKS"):
        main_run = run(
            [
                "gh",
                "run",
                "list",
                "--repo",
                f"gunnchOS3k/{name}",
                "--branch",
                "main",
                "--limit",
                "1",
                "--json",
                "conclusion",
            ]
        )
        if main_run:
            try:
                rows = json.loads(main_run)
                if rows and (rows[0].get("conclusion") or "").lower() == "success":
                    ci = "PASS"
            except Exception:
                pass
    return {
        "number": data.get("number", num),
        "url": data.get("url"),
        "draft": data.get("isDraft"),
        "mergeable": data.get("mergeable"),
        "merge_state": data.get("mergeStateStatus"),
        "head": data.get("headRefOid"),
        "state": data.get("state"),
        "merged_at": data.get("mergedAt"),
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


def ecosystem_capability_section(totals: dict) -> dict:
    return {
        "ACCEPTED_MAIN_DIGITAL_CAPABILITY": {
            "meaning": "Digitally evidenced on accepted main — not ecosystem completion",
            "DIGITAL_IMPLEMENTATION_COMPLETE": totals.get("DIGITAL_IMPLEMENTATION_COMPLETE", 0),
            "DIGITALLY_VERIFIED": totals.get("DIGITALLY_VERIFIED", 0),
            "IMPLEMENTED": totals.get("IMPLEMENTED", 0),
        },
        "open_digital_work": {
            "DIGITAL_IMPLEMENTATION_OPEN": totals.get("DIGITAL_IMPLEMENTATION_OPEN", 0),
            "DIGITAL_VALIDATION_OPEN": totals.get("DIGITAL_VALIDATION_OPEN", 0),
            "EVIDENCE_MAPPING_OPEN": totals.get("EVIDENCE_MAPPING_OPEN", 0),
        },
        "non_digital_pending_dimensions": {
            "HUMAN_PENDING": totals.get("HUMAN_PENDING_DIMENSION", 0),
            "PHYSICAL_PENDING": totals.get("PHYSICAL_PENDING_DIMENSION", 0),
            "EXTERNAL_PENDING": totals.get("EXTERNAL_PENDING_DIMENSION", 0),
            "STANDARD_PENDING": totals.get("STANDARD_PENDING_DIMENSION", 0),
            "CERTIFICATION_PENDING": totals.get("CERTIFICATION_PENDING_DIMENSION", 0),
            "CARRIER_PENDING": totals.get("CARRIER_PENDING_DIMENSION", 0),
            "VENDOR_PENDING": totals.get("VENDOR_PENDING_DIMENSION", 0),
            "OWNER_DECISION_PENDING": totals.get("OWNER_DECISION_PENDING_DIMENSION", 0),
        },
        "control_plane": {
            "PRE_ENGINEERING_CONTROL_PLANE_READY": load_json(BASELINE_V2_RESULT).get(
                "PRE_ENGINEERING_CONTROL_PLANE_READY", False
            ),
            "BASELINE_MAPPING_COMPLETE": load_json(BASELINE_V2_RESULT).get("BASELINE_MAPPING_COMPLETE", False),
        },
        "not_claimed": [
            "control-plane readiness is not ecosystem completion",
            "CI PASS is not physical validation",
            "synthetic/simulation is not field measurement",
            "standardized 6G / carrier acceptance / certification / human E6 / shipping are not complete",
        ],
        "baseline_v2_artifact_refs": {
            "NEXT_DIGITAL_IMPLEMENTATION_WORK": str(BASELINE_V2_DIR / "NEXT_DIGITAL_IMPLEMENTATION_WORK.json"),
            "NEXT_DIGITAL_VALIDATION_WORK": str(BASELINE_V2_DIR / "NEXT_DIGITAL_VALIDATION_WORK.json"),
            "NON_DIGITAL_PENDING_REGISTER": str(BASELINE_V2_DIR / "NON_DIGITAL_PENDING_REGISTER.json"),
            "field_kit_main_path": f"{FIELD_KIT_REPO}/program/digital_ecosystem_baseline_v2/",
        },
    }


def count_stale_preview_refs(latest_md: str, latest_json: dict, accepted: dict) -> tuple[int, list[str]]:
    stale: list[str] = []
    preview_markers = [
        "PR #53: batch007",
        "PR #88: residual digital closure",
        "PR #103: OPEN draft CONFLICTING",
        "Preview / draft PRs (not accepted-main)",
    ]
    for marker in preview_markers:
        if marker in latest_md:
            stale.append(f"LATEST.md contains stale preview marker: {marker}")
    for repo in SCOPE:
        pin = accepted.get(repo) or {}
        pin12 = (pin.get("sha") or "")[:12]
        for rec in latest_json.get("repositories") or []:
            if rec.get("repository") != repo:
                continue
            live12 = (rec.get("origin_main_sha") or "")[:12]
            if pin12 and live12 and pin12 != live12:
                stale.append(f"{repo} origin_main_sha12 {live12} != B4 freeze {pin12}")
    return len(stale), stale


def count_ci_contradictions(records: list[dict]) -> tuple[int, list[str]]:
    contradictions: list[str] = []
    for rec in records:
        if rec.get("disposition") != "ACCEPTED_MAIN":
            continue
        pr = rec.get("pr") or {}
        if pr.get("ci") == "FAIL":
            contradictions.append(f"{rec['repository']} ACCEPTED_MAIN but merged PR #{pr.get('number')} CI=FAIL")
    return len(contradictions), contradictions


def main() -> int:
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    date = now.strftime("%Y-%m-%d")
    repos_root = Path(os.environ.get("PORTFOLIO_REPOS_ROOT") or PORTAL.parent)
    pixel = adb_pixel()
    accepted = load_accepted_main()
    totals = load_baseline_v2_totals()
    ecosystem = ecosystem_capability_section(totals)
    records = []
    for name in SCOPE:
        path = repo_path(repos_root, name)
        exists = path.exists()
        sha = run(["git", "rev-parse", "HEAD"], cwd=path) if exists else ""
        origin_sha = origin_main_sha(path) if exists else ""
        branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=path) if exists else ""
        pr = gh_pr(name)
        pin = accepted.get(name) or {}
        rec = {
            "repository": name,
            "path": str(path) if exists else None,
            "exists": exists,
            "branch": branch,
            "sha": sha,
            "sha12": sha[:12] if sha else "",
            "origin_main_sha": origin_sha,
            "origin_main_sha12": origin_sha[:12] if origin_sha else "",
            "accepted_main_sha": pin.get("sha", ""),
            "accepted_main_sha12": (pin.get("sha") or "")[:12],
            "disposition": disposition_for(name, accepted, origin_sha),
            "uml": uml_label(path) if exists else "MISSING",
            "reproduce": reproduce_cmd(path) if exists else "UNDOCUMENTED",
            "pr": pr,
            "pr_head12": (pr.get("head") or "")[:12],
            "local_differs_from_pr_head": bool(sha and pr.get("head") and sha != pr.get("head")),
        }
        records.append(rec)

    snapshot = {
        "schema": "gunnchos.supervisor_contact_snapshot.v2",
        "generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "local_date": date,
        "working_title": "Resilience-Aware Service Continuity in Heterogeneous 6G Networks: Cross-Layer Orchestration for Resource-Constrained Devices",
        "affiliation_claim": "NONE — no University of Oulu affiliation, admission, funding, or supervisor commitment",
        "research_questions": {
            "RQ1": "How can representative workloads and the constraints of four resource-constrained device classes be translated into measurable service-continuity profiles, metrics, and benchmark scenarios?",
            "RQ2": "To what extent can joint access selection, computation placement, fidelity/model adaptation, caching/checkpointing, and recovery control - informed by radio-aware digital-twin state and uncertainty - improve service-continuity utility under mobility, blockage, congestion, edge-resource variation, and energy constraints?",
            "RQ3": "Under which disruption conditions do terrestrial, local-edge, peer/device-to-device, offline, and NTN fallback modes preserve minimum useful service, and what performance, energy, privacy, and recovery tradeoffs arise in simulation, emulation, and device-level measurements?",
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
        "ecosystem_capability": ecosystem,
        "unresolved_gates": [
            "CONTACT_SUPERVISOR_READY=BLOCKED (owner send / independent repro / HUMAN_QA playtest)",
            "INDEPENDENT_REPRODUCTION=PENDING",
            "PHYSICAL_EVT / RF / thermal / battery = PHYSICAL_PENDING",
            "Pixel 6a digital install+launch executed; HUMAN_QA_PENDING for fun/usability",
            "GPU NR CUDA timings = BLOCKED_GPU (repo is PUBLIC; missing lab GPU)",
            "ReadyGary TensorRT = BLOCKED_GPU; sub-ms inference is TARGET not fact",
            f"DIGITAL_IMPLEMENTATION_OPEN={totals.get('DIGITAL_IMPLEMENTATION_OPEN', '?')} — see field-kit Baseline V2",
            f"DIGITAL_VALIDATION_OPEN={totals.get('DIGITAL_VALIDATION_OPEN', '?')} — see field-kit Baseline V2",
        ],
        "visibility": {
            "gunnchos-gpu-nr-baseband-platform": "PUBLIC",
            "gunnchos-emergent-service-intent-protocols": "PUBLIC",
        },
        "repositories": records,
        "accepted_main_pin_file": str(B4_FREEZE if B4_FREEZE.is_file() else SPINE_ACCEPTED_MAIN),
        "b4_accepted_main_repo_count": load_json(B4_FREEZE).get("canonical_repo_count", 17),
        "disposition_legend": {
            "ACCEPTED_MAIN": "origin/main matches B4_ACCEPTED_MAIN_SHA_FREEZE pin",
            "ACCEPTED_MAIN_DRIFT": "pin exists but origin/main differs — refresh pin after owner merge",
        },
        "accepted_main_convergence": ACCEPTED_MAIN_CONVERGENCE,
        "physical_pending": PHYSICAL_PENDING,
        "human_pending": HUMAN_PENDING,
        "external_pending": EXTERNAL_PENDING,
    }

    out_dir = PORTAL / "docs" / "phd" / "contact_snapshots"
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"SUPERVISOR_CONTACT_SNAPSHOT_{date}.json"
    md_path = out_dir / f"SUPERVISOR_CONTACT_SNAPSHOT_{date}.md"
    json_path.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")

    eco = ecosystem
    rows = []
    for r in records:
        pr = r.get("pr") or {}
        rows.append(
            f"| `{r['repository']}` | {r.get('disposition', '')} | `{r.get('origin_main_sha12') or r['sha12']}` | {pr.get('number', '')} | {pr.get('ci', '')} | {r['reproduce']} |"
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

## Accepted-main digital capability (Baseline V2)

**Not ecosystem completion.** Control-plane readiness ≠ shipping / certification / field validation.

| Metric | Count | Meaning |
|---|---|---|
| DIGITAL_IMPLEMENTATION_COMPLETE | {eco['ACCEPTED_MAIN_DIGITAL_CAPABILITY']['DIGITAL_IMPLEMENTATION_COMPLETE']} | Digitally complete on accepted main |
| DIGITALLY_VERIFIED | {eco['ACCEPTED_MAIN_DIGITAL_CAPABILITY']['DIGITALLY_VERIFIED']} | Reproducible digital verification |
| DIGITAL_IMPLEMENTATION_OPEN | {eco['open_digital_work']['DIGITAL_IMPLEMENTATION_OPEN']} | Still needs digital engineering |
| DIGITAL_VALIDATION_OPEN | {eco['open_digital_work']['DIGITAL_VALIDATION_OPEN']} | Implementation exists; verification open |
| EVIDENCE_MAPPING_OPEN | {eco['open_digital_work']['EVIDENCE_MAPPING_OPEN']} | Evidence mapping gaps |

Authoritative worklists (do not execute from portal): field-kit `program/digital_ecosystem_baseline_v2/NEXT_DIGITAL_IMPLEMENTATION_WORK.json` ({eco['open_digital_work']['DIGITAL_IMPLEMENTATION_OPEN']} items), `NEXT_DIGITAL_VALIDATION_WORK.json` ({eco['open_digital_work']['DIGITAL_VALIDATION_OPEN']} items), `NON_DIGITAL_PENDING_REGISTER.json`.

## Non-digital pending dimensions

| Dimension | Count |
|---|---|
| HUMAN_PENDING | {eco['non_digital_pending_dimensions']['HUMAN_PENDING']} |
| PHYSICAL_PENDING | {eco['non_digital_pending_dimensions']['PHYSICAL_PENDING']} |
| EXTERNAL_PENDING | {eco['non_digital_pending_dimensions']['EXTERNAL_PENDING']} |
| STANDARD_PENDING | {eco['non_digital_pending_dimensions']['STANDARD_PENDING']} |
| CERTIFICATION_PENDING | {eco['non_digital_pending_dimensions']['CERTIFICATION_PENDING']} |
| CARRIER_PENDING | {eco['non_digital_pending_dimensions']['CARRIER_PENDING']} |
| VENDOR_PENDING | {eco['non_digital_pending_dimensions']['VENDOR_PENDING']} |
| OWNER_DECISION_PENDING | {eco['non_digital_pending_dimensions']['OWNER_DECISION_PENDING']} |

CI PASS ≠ physical validation. Synthetic/simulation ≠ field measurement.

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

## Disposition legend

| State | Meaning |
|---|---|
| ACCEPTED_MAIN | `origin/main` matches `B4_ACCEPTED_MAIN_SHA_FREEZE.json` |
| ACCEPTED_MAIN_DRIFT | pin exists but live `origin/main` differs |

## Pending classes

- **PHYSICAL_PENDING:** """ + "; ".join(PHYSICAL_PENDING) + """
- **HUMAN_PENDING:** """ + "; ".join(HUMAN_PENDING) + """
- **EXTERNAL_PENDING:** """ + "; ".join(EXTERNAL_PENDING) + """

## Accepted-main convergence (merged / closed — not open drafts)

""" + "\n".join(
        f"- `{p['repository']}` PR #{p['pr']}: **{p['state']}** — {p['note']}"
        for p in ACCEPTED_MAIN_CONVERGENCE
    ) + f"""

B4 accepted-main SHA freeze: **{snapshot['b4_accepted_main_repo_count']}** repos — see `artifacts/baseline_v2/B4_ACCEPTED_MAIN_SHA_FREEZE.json`.

## Sixteen repositories

| Repository | Disposition | origin/main SHA | Merged PR | CI | Reproduce |
|---|---|---|---|---|---|
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

    stale_count, stale_detail = count_stale_preview_refs(latest_md.read_text(encoding="utf-8"), snapshot, accepted)
    ci_count, ci_detail = count_ci_contradictions(records)
    drift = [r["repository"] for r in records if r.get("disposition") == "ACCEPTED_MAIN_DRIFT"]
    snapshot_pass = stale_count == 0 and ci_count == 0 and not drift

    validation = {
        "STALE_PREVIEW_REFERENCES": stale_count,
        "STALE_PREVIEW_DETAIL": stale_detail,
        "KNOWN_ACCEPTED_MAIN_CI_CONTRADICTIONS": ci_count,
        "CI_CONTRADICTION_DETAIL": ci_detail,
        "ACCEPTED_MAIN_DRIFT_REPOS": drift,
        "PORTAL_FINAL_ACCEPTED_MAIN_SNAPSHOT": "PASS" if snapshot_pass else "FAIL",
    }
    val_path = PORTAL / "artifacts" / "baseline_v2" / "PORTAL_SNAPSHOT_VALIDATION.json"
    val_path.write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {md_path}")
    print(f"wrote {json_path}")
    print(f"STALE_PREVIEW_REFERENCES={stale_count}")
    print(f"KNOWN_ACCEPTED_MAIN_CI_CONTRADICTIONS={ci_count}")
    print(f"PORTAL_FINAL_ACCEPTED_MAIN_SNAPSHOT={'PASS' if snapshot_pass else 'FAIL'}")
    if stale_detail:
        for line in stale_detail:
            print(f"  stale: {line}")
    if ci_detail:
        for line in ci_detail:
            print(f"  ci: {line}")
    if drift:
        print(f"  drift: {drift}")
    return 0 if snapshot_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
