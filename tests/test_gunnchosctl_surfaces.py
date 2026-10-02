"""Surface control plane tests. No network."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

PORTAL = Path(__file__).resolve().parents[1]
SCRIPT = PORTAL / "tools" / "surfaces" / "gunnchosctl_surfaces.py"
KIT = PORTAL / "tools" / "surfaces" / "surfacekit_v2.py"


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_catalog_has_the_staging_set():
    cli = _load(SCRIPT, "gunnchosctl_surfaces")
    rows = cli.catalog()
    assert len(rows) == 33
    names = {row["worker_name"] for row in rows}
    assert "gunnchos-ntn-resilience" in names
    assert "anime-aggressors-web" in names
    assert "finds-worker" not in names
    assert all(row["worker_url"].startswith("https://") for row in rows)


def test_inventory_offline(tmp_path: Path):
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "surfaces", "inventory", "--offline", "--out", str(tmp_path)],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "inventory=33" in proc.stdout
    rows = json.loads((tmp_path / "SURFACE_INVENTORY.json").read_text(encoding="utf-8"))
    assert rows[0]["merge_authorized"] is False
    assert rows[0]["dns_changed"] is False


def test_surfacekit_keeps_truth_firewall_and_adds_explore(tmp_path: Path):
    kit = _load(KIT, "surfacekit_v2")
    repo = tmp_path / "sample"
    public = repo / "web-surface" / "public"
    public.mkdir(parents=True)
    (repo / "configs" / "scenarios").mkdir(parents=True)
    (repo / "README.md").write_text(
        "# Sample\n\n## What problem does this solve?\n\nA documented local problem.\n\n## What exists today\n\nCLI and configs.\n",
        encoding="utf-8",
    )
    (repo / "REPRODUCIBILITY.md").write_text("Run make smoke locally.\n", encoding="utf-8")
    (repo / "configs" / "scenarios" / "gary_emergency.yaml").write_text(
        "scenario_id: gary_emergency\nsite_id: gary\nterrestrial_status: degraded\nntn_available: true\nfallback_policy: ntn_when_terrestrial_down\nethical_framing: simulation_only\n",
        encoding="utf-8",
    )
    meta = {
        "repo": "sample",
        "productName": "Sample",
        "family": "7GC",
        "classification": "STATIC_RESEARCH_SURFACE_WORKER",
        "acceptedSha": "abc123",
        "status": "STAGING_WORKER",
        "summary": "A sample research surface.",
        "limitations": ["Not a live network"],
        "sourceUrl": "https://github.com/gunnchOS3k/sample",
        "returnUrl": "https://example.test",
    }
    (public / "project-surface.json").write_text(json.dumps(meta), encoding="utf-8")
    result = kit.write_surface(repo)
    html = (public / "index.html").read_text(encoding="utf-8")
    css = (public / "styles.css").read_text(encoding="utf-8")
    js = (public / "app.js").read_text(encoding="utf-8")
    assert result["measured_topology"] is True
    assert 'data-surfacekit="v2"' in html
    assert 'id="primary-action"' in html
    assert "What is this?" in html
    assert "What is not finished?" in html
    assert "STAGING_WORKER" in html
    assert "@media (max-width: 800px)" in css
    assert "a:focus-visible" in css
    for blob in (html, css, js):
        assert "workers.dev" not in blob
        assert "gunnchos-finds" not in blob
        assert "official oulu" not in blob.lower()
    explore = json.loads((public / "explore.json").read_text(encoding="utf-8"))
    assert explore["rows"][0]["scenario_id"] == "gary_emergency"
    judged = _load(SCRIPT, "gunnchosctl_surfaces")._judge(
        {"repo": "sample", "pr": 1, "classification": meta["classification"], "worker_name": "x", "worker_url": "https://example.test", "source_ref": "surface/staging-worker"},
        200,
        html,
    )
    assert judged["generic_status_only"] is False
    assert judged["primary_action_status"] == "present"
