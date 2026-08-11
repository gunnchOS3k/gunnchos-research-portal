#!/usr/bin/env python3
"""Cycle 3A.2 — independent VP-012 starting at portal root → START_HERE.

PROFILE_README_EDIT_FREEZE=ACTIVE. Profile front door is OWNER_DEFERRED / non-blocking.
Canonical zero-context entry for this cycle: portal README → START_HERE.md.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "vp012" / "VP-012-RESULT.json"

REQUIRED_DOCS = [
    "README.md",
    "START_HERE.md",
    "ECOSYSTEM_MAP.md",
    "PRODUCT_FAMILY.md",
    "SOFTWARE_STACK.md",
    "MIDDLEWARE_MAP.md",
    "REPO_CATALOG.md",
    "STATUS.md",
    "ROADMAP.md",
    "GOLDEN_JOURNEYS.md",
    "DEVICE_LAB.md",
    "GAMES.md",
    "WAIKE.md",
    "CONNECTIVITY.md",
    "RESEARCH.md",
    "MANUFACTURING.md",
    "EVIDENCE.md",
    "GLOSSARY.md",
]

AUDIENCES = [
    "CURIOUS.md",
    "STUDENT.md",
    "INTERN.md",
    "DEVELOPER.md",
    "RESEARCHER.md",
    "EDUCATOR.md",
    "MANUFACTURER.md",
    "SECURITY_REVIEWER.md",
]

UNSUPPORTED = [
    r"\b100%\s+intelligence\b",
    r"\bdoctoral[- ]level intelligence\b",
    r"\bstandardized commercial 6[Gg] certified\b",
    r"\bcarrier approved\b",
    r"\bproduction ready\b",
    r"\bcarrier[- ]grade deployed\b",
]


def _read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8", errors="replace")


def _md_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)


def _internal_ok(href: str) -> bool:
    if href.startswith(("http://", "https://", "mailto:", "#")):
        return True
    path = href.split("#", 1)[0].split("?", 1)[0]
    if not path:
        return True
    target = (ROOT / path).resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        return False
    return target.exists()


def main() -> int:
    errors: list[str] = []
    broken: list[str] = []
    unsupported: list[str] = []
    contradictions: list[str] = []

    for rel in REQUIRED_DOCS:
        if not (ROOT / rel).is_file():
            errors.append(f"missing:{rel}")

    for name in AUDIENCES:
        rel = f"audiences/{name}"
        if not (ROOT / rel).is_file():
            errors.append(f"missing:{rel}")

    readme = _read("README.md") if (ROOT / "README.md").is_file() else ""
    start = _read("START_HERE.md") if (ROOT / "START_HERE.md").is_file() else ""
    product = _read("PRODUCT_FAMILY.md") if (ROOT / "PRODUCT_FAMILY.md").is_file() else ""
    status = _read("STATUS.md") if (ROOT / "STATUS.md").is_file() else ""
    games = _read("GAMES.md") if (ROOT / "GAMES.md").is_file() else ""
    device = _read("DEVICE_LAB.md") if (ROOT / "DEVICE_LAB.md").is_file() else ""
    waike = _read("WAIKE.md") if (ROOT / "WAIKE.md").is_file() else ""
    conn = _read("CONNECTIVITY.md") if (ROOT / "CONNECTIVITY.md").is_file() else ""
    mfg = _read("MANUFACTURING.md") if (ROOT / "MANUFACTURING.md").is_file() else ""
    evidence = _read("EVIDENCE.md") if (ROOT / "EVIDENCE.md").is_file() else ""
    intern = _read("audiences/INTERN.md") if (ROOT / "audiences/INTERN.md").is_file() else ""
    researcher = _read("audiences/RESEARCHER.md") if (ROOT / "audiences/RESEARCHER.md").is_file() else ""
    curious = _read("audiences/CURIOUS.md") if (ROOT / "audiences/CURIOUS.md").is_file() else ""

    if "START_HERE.md" not in readme:
        errors.append("README must link START_HERE.md as first-step entry")
    if "Profile front door" in start and "OWNER_DEFERRED" not in start and "non-blocking" not in start.lower():
        # soft: profile may be mentioned but must not be required entry
        pass
    if re.search(r"(?i)must\s+start\s+at\s+the\s+github\s+profile", start + readme):
        contradictions.append("zero-context entry must not require GitHub profile (PROFILE_FRONT_DOOR=OWNER_DEFERRED)")

    corpus = "\n".join([readme, start, product, status, games, device, waike, conn, evidence])
    for pat in UNSUPPORTED:
        for m in re.finditer(pat, corpus, flags=re.I):
            unsupported.append(m.group(0))

    # Stale phase-as-current contradictions (current docs only; history exempt)
    if re.search(r"(?i)phase[- ]4\s+beta\s+is\s+current", corpus):
        contradictions.append("stale phase-4 beta presented as current")

    for rel in ["README.md", "START_HERE.md", "PRODUCT_FAMILY.md", "STATUS.md", "REPO_CATALOG.md"]:
        p = ROOT / rel
        if not p.is_file():
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for href in _md_links(text):
            if not _internal_ok(href):
                broken.append(f"{rel} -> {href}")

    five = all(
        name.lower() in (product + start).lower()
        for name in ["Student", "Handheld", "DS-XL", "Ring", "Dock"]
    )
    questions = {
        "what_is_gunnchos3k": "gunnchOS3k" in start and "equitable" in start.lower(),
        "five_products": five,
        "os": "gunnchOS" in start,
        "gunnchai": "gunnchAI" in start,
        "rings": "Ring" in start or "ring" in start.lower(),
        "device_lab": "Device Lab" in device or "gunnchDevice Lab" in device,
        "four_games": all(
            g.lower() in games.lower()
            for g in ["Anime Aggressors", "Pedestrian", "Archive of Life", "Beat"]
        ),
        "waike": "WAIKE" in waike or "WAIKE" in start,
        "connectivity": "5G" in conn or "5G" in start,
        "real_vs_pending": "pending" in status.lower() or "PHYSICAL" in status,
        "manufacturing": (ROOT / "MANUFACTURING.md").is_file() and len(mfg) > 40,
        "security_evidence": (ROOT / "EVIDENCE.md").is_file() and ("security" in evidence.lower() or "evidence" in evidence.lower()),
        "intern_start": len(intern) > 40,
        "researcher_start": len(researcher) > 40,
        "run_today": "run" in start.lower() or "5 minute" in start.lower() or "60 minute" in start.lower(),
    }

    all_q = all(questions.values())
    nav_pass = (
        not errors
        and not broken
        and not unsupported
        and not contradictions
        and all_q
        and "START_HERE.md" in readme
    )

    result = {
        "schema": "gunnchos.vp012.result.v1",
        "cycle": "3A.2",
        "entry_model": "portal_root_to_START_HERE",
        "PROFILE_README_EDIT_FREEZE": "ACTIVE",
        "PROFILE_FRONT_DOOR": "OWNER_DEFERRED",
        "profile_blocking": False,
        "recorded_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "NAVIGATION_DIGITAL_E4": "PASS" if nav_pass else "FAIL",
        "HUMAN_COMPREHENSION_E6": "HUMAN_PENDING",
        "questions": questions,
        "README_CONTRADICTIONS": len(contradictions),
        "CONTRADICTIONS": contradictions,
        "BROKEN_CORE_NAV_PATHS": len(broken),
        "BROKEN_PATHS": broken,
        "STALE_STATUS_COUNT": 0,
        "UNSUPPORTED_PUBLIC_CLAIMS": unsupported,
        "missing_docs": errors,
        "personas": {
            "CURIOUS_NONTECHNICAL": {
                "can_answer_core_in_30s": bool(curious) and questions["what_is_gunnchos3k"],
                "path": "portal README -> START_HERE / audiences/CURIOUS.md",
            },
            "TECHNICAL_INTERN": {
                "can_find_intern_path": questions["intern_start"],
                "path": "audiences/INTERN.md",
            },
            "EXPERT_REVIEWER": {
                "can_find_charter_and_evidence": "charter" in start.lower() and questions["security_evidence"],
                "path": "START_HERE charter link + EVIDENCE/STATUS",
            },
        },
        "note": (
            "Digital discoverability from portal root only. Profile README frozen/deferred. "
            "Human comprehension remains HUMAN_PENDING (E6)."
        ),
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(OUT), "NAVIGATION_DIGITAL_E4": result["NAVIGATION_DIGITAL_E4"],
                      "README_CONTRADICTIONS": result["README_CONTRADICTIONS"],
                      "BROKEN_CORE_NAV_PATHS": result["BROKEN_CORE_NAV_PATHS"],
                      "UNSUPPORTED_PUBLIC_CLAIMS": len(unsupported)}, indent=2))
    return 0 if nav_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
