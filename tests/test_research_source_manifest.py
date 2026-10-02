"""Research source manifest stays separate from surface depth claims."""

from __future__ import annotations

import importlib.util
from pathlib import Path

PORTAL = Path(__file__).resolve().parents[1]
MODULE = PORTAL / "tools" / "surfaces" / "research_source.py"


def _load():
    spec = importlib.util.spec_from_file_location("research_source", MODULE)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _sample() -> dict:
    link = {"label": "Record", "href": "https://github.com/gunnchOS3k/spectrumx-ai-ran-gary"}
    return {
        "title": "AI-RAN Gary",
        "evidenceClass": "LIVE_EXTERNAL_APP",
        "sourceRepo": "gunnchOS3k/spectrumx-ai-ran-gary",
        "sourceSha": "a62ce3e224c7247eb1cda2969464d599b1c0870d",
        "license": "MIT",
        "citation": {"cff": "CITATION.cff", "bibtex": "paper/citation.bib"},
        "papers": [link],
        "reports": [link],
        "reproducibility": [link],
        "data": [link],
        "configs": [link],
        "results": [link],
        "figures": [],
        "limitations": ["Not a live RAN."],
        "downloadBundle": "https://github.com/gunnchOS3k/spectrumx-ai-ran-gary/archive/a62ce3e224c7247eb1cda2969464d599b1c0870d.zip",
    }


def test_schema_does_not_define_measured_topology():
    mod = _load()
    encoded = mod.SCHEMA_PATH.read_text()
    assert "measured_topology" not in encoded


def test_sample_manifest_passes():
    mod = _load()
    assert mod.validate_manifest(_sample()) == []


def test_missing_sha_and_topology_flag_fail():
    mod = _load()
    payload = _sample()
    payload["sourceSha"] = "main"
    payload["measured_topology"] = True
    errors = mod.validate_manifest(payload)
    assert any("sourceSha" in item for item in errors)
    assert any("measured_topology" in item for item in errors)
