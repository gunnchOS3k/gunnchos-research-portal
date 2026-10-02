"""Validate a research source manifest. This module does not set measured_topology."""

from __future__ import annotations

import json
import re
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parents[2] / "contracts" / "schemas" / "research_source_manifest.v1.json"
SHA = re.compile(r"^[0-9a-f]{40}$")
EVIDENCE = {
    "SIMULATED",
    "SYNTHETIC_SIM",
    "MEASURED",
    "REFERENCE_IMPLEMENTATION",
    "LIVE_EXTERNAL_APP",
    "DOCUMENTED_ONLY",
}
REQUIRED = (
    "title",
    "evidenceClass",
    "sourceRepo",
    "sourceSha",
    "license",
    "citation",
    "papers",
    "reports",
    "reproducibility",
    "data",
    "configs",
    "results",
    "figures",
    "limitations",
    "downloadBundle",
)
LINK_LISTS = (
    "papers",
    "reports",
    "reproducibility",
    "data",
    "configs",
    "results",
    "figures",
)
RAIL_LABELS = (
    "Demo / Explore",
    "Paper / Report",
    "Source code",
    "Reproduce",
    "Data / Results",
    "Cite",
    "Download research bundle",
)


def schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text())


def validate_manifest(payload: dict) -> list[str]:
    errors: list[str] = []
    if "measured_topology" in payload:
        errors.append("measured_topology is not part of the research source manifest")
    for key in REQUIRED:
        if key not in payload:
            errors.append(f"missing {key}")
    if any(key not in payload for key in REQUIRED):
        return errors
    if not isinstance(payload["title"], str) or not payload["title"].strip():
        errors.append("title must be non-empty")
    if payload["evidenceClass"] not in EVIDENCE:
        errors.append("evidenceClass is not a known class")
    if not isinstance(payload["sourceRepo"], str) or not payload["sourceRepo"].startswith("gunnchOS3k/"):
        errors.append("sourceRepo must be a gunnchOS3k repository")
    if not isinstance(payload["sourceSha"], str) or not SHA.fullmatch(payload["sourceSha"]):
        errors.append("sourceSha must be a 40-character hex SHA")
    if not isinstance(payload["license"], str) or not payload["license"].strip():
        errors.append("license must be non-empty")
    citation = payload["citation"]
    if not isinstance(citation, dict) or not citation.get("cff") or not citation.get("bibtex"):
        errors.append("citation needs cff and bibtex")
    for key in LINK_LISTS:
        rows = payload[key]
        if not isinstance(rows, list):
            errors.append(f"{key} must be a list")
            continue
        for index, row in enumerate(rows):
            if not isinstance(row, dict) or not row.get("label") or not row.get("href"):
                errors.append(f"{key}[{index}] needs label and href")
    limitations = payload["limitations"]
    if not isinstance(limitations, list) or not limitations or not all(isinstance(item, str) and item.strip() for item in limitations):
        errors.append("limitations must be a non-empty list of strings")
    if not isinstance(payload["downloadBundle"], str) or not payload["downloadBundle"].strip():
        errors.append("downloadBundle must be non-empty")
    return errors
