#!/usr/bin/env python3
"""Validate supervisor-ready control-plane files in gunnchos-research-portal.

Checks presence, vocabulary, claim-boundary phrases, and UML lane structure.
Does not claim CONTACT_SUPERVISOR_READY PASS.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PORTAL = Path(__file__).resolve().parents[1]

REQUIRED_PHD = [
    "docs/phd/START_HERE_SUPERVISOR.md",
    "docs/phd/BASELINE_PORTFOLIO_AUDIT.md",
    "docs/phd/THESIS_AT_A_GLANCE.md",
    "docs/phd/RESEARCH_SCOPE_AND_BOUNDARIES.md",
    "docs/phd/RQ_TO_REPO_EVIDENCE_MAP.md",
    "docs/phd/EXPERIMENTAL_SYSTEM_MAP.md",
    "docs/phd/OULU_FIT.md",
    "docs/phd/CONTACT_SUPERVISOR_RELEASE_GATE.md",
    "docs/phd/SUPERVISOR_10_MINUTE_PATH.md",
    "docs/phd/PORTFOLIO_READINESS_DASHBOARD.md",
    "docs/phd/REPRODUCIBILITY_INDEX.md",
    "docs/phd/UML_INDEX.md",
    "docs/phd/PHYSICAL_REALIZATION_BOUNDARY.md",
    "docs/phd/RESEARCH_PLAN_ALIGNMENT_REPORT.md",
    "docs/phd/EVIDENCE_TAXONOMY.md",
]

REQUIRED_PACKETS = [
    "docs/packets/PIXEL_6A_ACCEPTANCE_PACKET.md",
    "docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md",
    "docs/packets/EXTERNAL_REPRODUCTION_PACKET.md",
    "docs/packets/HUMAN_PLAYTEST_PACKET.md",
    "docs/packets/REPOSITORY_VISIBILITY_PACKET.md",
    "docs/packets/RF_LAB_VALIDATION_PACKET.md",
    "docs/packets/MANUFACTURER_RFQ_SEND_PACKET.md",
    "docs/packets/SUPERVISOR_CONTACT_USER_ACTION.md",
]

REQUIRED_UML = [
    "docs/uml/README.md",
    "docs/uml/current/index.md",
    "docs/uml/future/index.md",
    "docs/uml/legacy/index.md",
    "docs/uml/traceability_matrix.md",
    "docs/uml/current/use_case.md",
    "docs/uml/current/component.md",
    "docs/uml/current/package_repository.md",
    "docs/uml/current/activity_audience_navigation.md",
    "docs/uml/current/deployment.md",
]

FORBIDDEN_CLAIM_PATTERNS = [
    r"Oulu affiliation (is|has been) confirmed",
    r"supervisor has (accepted|committed|agreed)",
    r"we are members of 6G Flagship",
    r"FCC certified",
    r"CE certified",
]

ALLOWED_STATUSES = {
    "DIGITAL_PASS",
    "FAIL_DIGITAL",
    "PHYSICAL_PENDING",
    "EXTERNAL_PENDING",
    "HUMAN_QA_PENDING",
    "INDEPENDENT_REPRODUCTION_PENDING",
    "BLOCKED_HARDWARE",
    "BLOCKED_GPU",
    "BLOCKED_DATA",
    "NOT_APPLICABLE",
    "PASS",
    "FAIL",
    "BLOCKED",
    "PENDING",
}


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_PHD + REQUIRED_PACKETS + REQUIRED_UML:
        path = PORTAL / rel
        if not path.exists():
            errors.append(f"missing {rel}")
        elif path.stat().st_size < 80:
            errors.append(f"too_short {rel}")

    manifest = PORTAL / "portfolio" / "supervisor_ready_manifest.yaml"
    roles = PORTAL / "portfolio" / "repo_roles.yaml"
    if not manifest.exists():
        errors.append("missing portfolio/supervisor_ready_manifest.yaml — run make audit")
    if not roles.exists():
        errors.append("missing portfolio/repo_roles.yaml")

    for rel in REQUIRED_PHD + ["README.md", "docs/phd/OULU_FIT.md"]:
        path = PORTAL / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pat in FORBIDDEN_CLAIM_PATTERNS:
            if re.search(pat, text, re.I):
                errors.append(f"forbidden_claim {rel}: {pat}")

    oulu = PORTAL / "docs/phd/OULU_FIT.md"
    if oulu.exists():
        text = oulu.read_text(encoding="utf-8")
        if "no affiliation" not in text.lower() and "does not claim affiliation" not in text.lower():
            errors.append("OULU_FIT.md must explicitly deny affiliation claims")
        if "6gflagship.com" not in text.lower():
            errors.append("OULU_FIT.md must cite official 6G Flagship source")

    start = PORTAL / "docs/phd/START_HERE_SUPERVISOR.md"
    if start.exists():
        text = start.read_text(encoding="utf-8")
        for needle in [
            "Resilience-Aware Service Continuity",
            "RQ1",
            "RQ2",
            "RQ3",
            "30-second",
            "10-minute",
        ]:
            if needle not in text:
                errors.append(f"START_HERE_SUPERVISOR.md missing {needle}")

    if errors:
        print("FAIL")
        for e in errors:
            print(f" - {e}")
        return 1
    print("PASS digital control-plane files present and claim-boundary checks clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
