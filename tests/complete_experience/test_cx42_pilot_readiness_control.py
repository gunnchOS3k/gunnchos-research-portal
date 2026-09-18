"""Portal CX4.2 Validation Center pilot-readiness control-plane fail-closed checks."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "docs" / "complete-experience" / "CX4_VALIDATION_CENTER_PILOT_READINESS_CONTROL.md"


def test_cx42_control_doc_exists():
    assert DOC.is_file()
    text = DOC.read_text()
    assert "eng/cx4-validation-center-pilot-readiness" in text
    assert "docs/cx4-validation-center-pilot-readiness-control" in text
    assert "CX4_VALIDATION_CENTER_ONE_CLICK_LAUNCH_PASS" in text
    assert "CX4_FINAL_HUMAN_VALIDATION_ELIGIBLE" in text
    assert "**false**" in text
    assert "WAIT_FOR_FINAL_ACCEPTED_BUILD_THEN_RUN_HUMAN_VALIDATION" in text
    assert "rehearsal" in text.lower() or "REHEARSAL" in text


def test_cx42_keeps_pending_and_zero_real_sessions():
    text = DOC.read_text()
    assert "| `J6_CLASS` | **HUMAN_VALIDATION_PENDING** |" in text
    assert "| `PHYSICAL_PRINTER_PENDING` | **true** |" in text
    assert "| `EVT_PENDING` | **true** |" in text
    assert "| `DVT_PENDING` | **true** |" in text
    assert "| `PVT_PENDING` | **true** |" in text
    assert "| `FULL_COMPLETE_EXPERIENCE_COMPLETE` | **false** |" in text
    assert "| `CX4_FINAL_HUMAN_VALIDATION_ELIGIBLE` | **false** |" in text
    assert "| Real human sessions submitted | **0** |" in text


def test_cx42_retains_cx41_control():
    assert (ROOT / "docs" / "complete-experience" / "CX4_VALIDATION_CENTER_CONTROL.md").is_file()
