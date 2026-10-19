#!/usr/bin/env python3
"""Validate imported doctrine and v1 control packs. Does not flip gates."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCTRINE = ROOT / "docs" / "ecosystem-doctrine"
CONTROL = ROOT / "docs" / "release-control" / "v1"
RC1 = ROOT / "releases" / "v1.0.0-rc.1"
DASHBOARD = ROOT / "artifacts" / "release-control" / "V1_CONTROL_PLANE_DASHBOARD.json"
RC1_SHA256 = "1e8763413e279ab73eb7ccdceedcbeb886d43af24ae660090b84414355296b2e"
RC1_FILES = 125
REQUIRED_COLUMNS = ["id", "area", "item", "disposition", "status", "repo", "gate", "next_action"]
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def rc1_digest() -> tuple[int, str]:
    digest = hashlib.sha256()
    count = 0
    for path in sorted(p for p in RC1.rglob("*") if p.is_file()):
        rel = path.relative_to(RC1).as_posix()
        digest.update(rel.encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        count += 1
    return count, digest.hexdigest()


def broken_links(folder: Path) -> list[str]:
    broken: list[str] = []
    for path in folder.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for match in LINK.finditer(text):
            target = match.group(1).split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            candidate = (path.parent / target).resolve()
            if not candidate.exists():
                broken.append(f"{path.relative_to(ROOT)} -> {target}")
    return broken


def load_scope() -> list[dict[str, str]]:
    path = CONTROL / "02_V1_MASTER_SCOPE_CREEP_LEDGER.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []
        missing = [name for name in REQUIRED_COLUMNS if name not in columns]
        if missing:
            raise SystemExit(f"scope ledger missing columns: {missing}")
        return list(reader)


def validate() -> dict:
    errors: list[str] = []
    manifest = json.loads((DOCTRINE / "ECOSYSTEM_DOCTRINE_MANIFEST.json").read_text())
    for key in ("schema", "north_star", "non_negotiables", "places"):
        if key not in manifest:
            errors.append(f"doctrine manifest missing {key}")
    control = json.loads((CONTROL / "V1_MASTER_CONTROL.json").read_text())
    for key in ("schema", "v1_release_authorized", "claim_boundary", "current_wip"):
        if key not in control:
            errors.append(f"master control missing {key}")
    if control.get("v1_release_authorized") is not False:
        errors.append("refusing to validate a pack that authorizes final v1")
    boundary = control.get("claim_boundary") or {}
    for flag in ("physical_evt", "dvt", "pvt", "rf_certification", "carrier_certification", "mass_manufacturing"):
        if boundary.get(flag) is not False:
            errors.append(f"claim boundary {flag} is not false")
    rows = load_scope()
    ids = [row.get("id", "") for row in rows]
    duplicates = sorted({item for item in ids if item and ids.count(item) > 1})
    if duplicates:
        errors.append(f"duplicate scope ids: {duplicates}")
    DASHBOARD.parent.mkdir(parents=True, exist_ok=True)
    DASHBOARD.write_text(json.dumps({"placeholder": True}) + "\n", encoding="utf-8")
    links = broken_links(DOCTRINE) + broken_links(CONTROL)
    # START_HERE is a file; broken_links expects a folder. Handle file separately.
    start = ROOT / "docs" / "START_HERE_ECOSYSTEM.md"
    if start.exists():
        for match in LINK.finditer(start.read_text(encoding="utf-8")):
            target = match.group(1).split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (start.parent / target).resolve().exists():
                links.append(f"docs/START_HERE_ECOSYSTEM.md -> {target}")
    if links:
        errors.append("broken internal links: " + "; ".join(links))
    count, digest = rc1_digest()
    if count != RC1_FILES or digest != RC1_SHA256:
        errors.append("historical releases/v1.0.0-rc.1 digest changed")
    dispositions = Counter(row.get("disposition") or "UNSET" for row in rows)
    owner_gates = [
        row["id"]
        for row in rows
        if "HUMAN" in (row.get("disposition") or "") or "owner" in (row.get("gate") or "").lower() or "human" in (row.get("gate") or "").lower()
    ]
    physical = [
        row["id"]
        for row in rows
        if "PHYSICAL" in (row.get("disposition") or "") or "physical" in (row.get("gate") or "").lower()
    ]
    external = [
        row["id"]
        for row in rows
        if any(word in (row.get("disposition") or "") for word in ("REGULATORY", "RIGHTS", "VENDOR"))
        or any(word in (row.get("gate") or "").lower() for word in ("rights", "vendor", "regulatory", "external"))
    ]
    dashboard = {
        "schema": "gunnchos.v1.control_plane_dashboard.v1",
        "source": "docs/release-control/v1",
        "doctrine": "docs/ecosystem-doctrine",
        "scope_count": len(rows),
        "disposition_counts": dict(sorted(dispositions.items())),
        "unresolved_owner_gates": owner_gates,
        "physical_gates": physical,
        "external_gates": external,
        "active_v1_lanes": control.get("current_wip"),
        "v1_release_authorized": False,
        "historical_rc": control.get("historical_rc"),
        "rc1_immutable": count == RC1_FILES and digest == RC1_SHA256,
        "import_is_not_evidence": True,
        "errors": errors,
    }
    DASHBOARD.parent.mkdir(parents=True, exist_ok=True)
    DASHBOARD.write_text(json.dumps(dashboard, indent=2) + "\n", encoding="utf-8")
    if errors:
        raise SystemExit("\n".join(errors))
    return dashboard


if __name__ == "__main__":
    result = validate()
    json.dump({k: result[k] for k in ("scope_count", "v1_release_authorized", "rc1_immutable")}, sys.stdout)
    sys.stdout.write("\n")
