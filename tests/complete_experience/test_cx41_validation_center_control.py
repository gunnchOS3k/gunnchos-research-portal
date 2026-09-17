"""Portal CX4.1 Validation Center control-plane fail-closed checks."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "docs" / "complete-experience" / "CX4_VALIDATION_CENTER_CONTROL.md"


def test_cx41_control_doc_exists():
    assert DOC.is_file()
    text = DOC.read_text()
    assert "eng/cx4-validation-center-human-field-ui" in text
    assert "docs/cx4-validation-center-control" in text
    assert "CX4_VALIDATION_CENTER_GUI_PASS" in text
    assert "CX4_VALIDATION_REVIEWER_SIGNOFF_ENFORCED" in text
    assert "MINORS_MODE_DISABLED_BY_DEFAULT" in text
    assert "BEGIN_REAL_HUMAN_VALIDATION_SESSIONS_IN_VALIDATION_CENTER" in text
    assert "must **not** be converted into human/physical PASS" in text or "must **not** be converted" in text.lower()


def test_cx41_keeps_pending_and_zero_real_sessions():
    text = DOC.read_text()
    assert "| `J6_CLASS` | **HUMAN_VALIDATION_PENDING** |" in text
    assert "| `PHYSICAL_PRINTER_PENDING` | **true** |" in text
    assert "| `EVT_PENDING` | **true** |" in text
    assert "| `DVT_PENDING` | **true** |" in text
    assert "| `PVT_PENDING` | **true** |" in text
    assert "| `FULL_COMPLETE_EXPERIENCE_COMPLETE` | **false** |" in text
    assert "| Real human sessions submitted | **0** |" in text
    assert "| Reviewer-signed real sessions | **0** |" in text


def test_cx41_retains_cx40_control():
    assert (ROOT / "docs" / "complete-experience" / "CX4_HUMAN_PHYSICAL_EXTERNAL_READINESS_CONTROL.md").is_file()
