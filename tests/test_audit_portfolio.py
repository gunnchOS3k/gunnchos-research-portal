"""Canonical behavior tests for scripts/audit_portfolio.py (R5-S1)."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

PORTAL = Path(__file__).resolve().parents[1]
SCRIPT = PORTAL / "scripts" / "audit_portfolio.py"


def _load_audit():
    spec = importlib.util.spec_from_file_location("audit_portfolio", SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_load_roles_from_real_portfolio_catalog():
    audit = _load_audit()
    roles = audit.load_roles(PORTAL)
    assert "repositories" in roles
    names = {r["repository"] for r in roles["repositories"]}
    assert "gunnchos-research-portal" in names
    assert len(names) >= 16


def test_uml_status_and_gate_on_structured_fixture(tmp_path: Path):
    audit = _load_audit()
    uml = tmp_path / "docs" / "uml"
    for lane in ("current", "future", "legacy"):
        (uml / lane).mkdir(parents=True)
    (uml / "current" / "component.md").write_text("# component\n", encoding="utf-8")
    (uml / "README.md").write_text("# uml\n", encoding="utf-8")
    status = audit.uml_status(tmp_path)
    assert status["label"] == "STRUCTURED_CURRENT_FUTURE_LEGACY"
    assert audit.classify_uml_gate(status) == "DIGITAL_PASS"


def test_uml_gate_fails_when_uml_missing(tmp_path: Path):
    audit = _load_audit()
    status = audit.uml_status(tmp_path)
    assert status["label"] == "MISSING"
    assert audit.classify_uml_gate(status) == "FAIL_DIGITAL"


def test_main_allow_missing_siblings_exits_zero(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """Isolated CI contract: missing spine + allow flag must exit 0 (not 1)."""
    audit = _load_audit()
    portal = tmp_path / "portal"
    (portal / "portfolio").mkdir(parents=True)
    roles = json.loads((PORTAL / "portfolio" / "repo_roles.json").read_text(encoding="utf-8"))
    (portal / "portfolio" / "repo_roles.json").write_text(json.dumps(roles), encoding="utf-8")
    empty_spine = tmp_path / "empty_spine"
    empty_spine.mkdir()

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "audit_portfolio.py",
            "--portal-root",
            str(portal),
            "--repos-root",
            str(empty_spine),
            "--no-write",
            "--allow-missing-siblings",
        ],
    )
    rc = audit.main()
    assert rc == 0


def test_main_missing_siblings_without_allow_exits_nonzero(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    audit = _load_audit()
    portal = tmp_path / "portal"
    (portal / "portfolio").mkdir(parents=True)
    roles = json.loads((PORTAL / "portfolio" / "repo_roles.json").read_text(encoding="utf-8"))
    (portal / "portfolio" / "repo_roles.json").write_text(json.dumps(roles), encoding="utf-8")
    empty_spine = tmp_path / "empty_spine"
    empty_spine.mkdir()

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "audit_portfolio.py",
            "--portal-root",
            str(portal),
            "--repos-root",
            str(empty_spine),
            "--no-write",
        ],
    )
    rc = audit.main()
    assert rc == 1


def test_missing_roles_catalog_raises(tmp_path: Path):
    audit = _load_audit()
    with pytest.raises(SystemExit):
        audit.load_roles(tmp_path)


def test_cli_subprocess_allow_missing_siblings_exit_zero(tmp_path: Path):
    portal = tmp_path / "portal"
    (portal / "portfolio").mkdir(parents=True)
    roles = json.loads((PORTAL / "portfolio" / "repo_roles.json").read_text(encoding="utf-8"))
    (portal / "portfolio" / "repo_roles.json").write_text(json.dumps(roles), encoding="utf-8")
    empty_spine = tmp_path / "empty_spine"
    empty_spine.mkdir()

    proc = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--portal-root",
            str(portal),
            "--repos-root",
            str(empty_spine),
            "--no-write",
            "--allow-missing-siblings",
        ],
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert proc.returncode == 0
    assert "missing=" in (proc.stdout or "")
    assert "isolated_portal_ci" in (proc.stdout or "")
