"""Portal CX4.0 control-plane fail-closed checks."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "docs" / "complete-experience" / "CX4_HUMAN_PHYSICAL_EXTERNAL_READINESS_CONTROL.md"


def test_cx4_control_doc_exists():
    assert DOC.is_file()
    text = DOC.read_text()
    assert "CX4_CURRENT_TIP_GUEST_OVERLAY_PASS" in text
    assert "CX4_CURRENT_TIP_GUEST_SMOKE_PASS" in text
    assert "CX4_HUMAN_A11Y_PACKET_READY" in text
    assert "CX4_ALL_AUTOMATABLE_NON_DIGITAL_PREWORK_PASS" in text
    assert "eng/cx4-human-physical-external-readiness" in text
    assert "docs/cx4-human-physical-external-readiness-control" in text
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=false" in text or "| `FULL_COMPLETE_EXPERIENCE_COMPLETE` | **false** |" in text
    assert "HUMAN_VALIDATION_PENDING" in text
    assert "CX4_OWNER_HUMAN_PHYSICAL_EXECUTION" in text
    assert "do **not** be converted into human/physical/external PASS" in text.lower() or "must **not** be converted" in text


def test_cx4_keeps_pending_gates():
    text = DOC.read_text()
    assert "| `PHYSICAL_PRINTER_PENDING` | **true** |" in text
    assert "| `PHYSICAL_CAMERA_MIC_AV_PENDING` | **true** |" in text
    assert "| `EVT_PENDING` | **true** |" in text
    assert "| `DVT_PENDING` | **true** |" in text
    assert "| `PVT_PENDING` | **true** |" in text
    assert "| `FULL_COMPLETE_EXPERIENCE_COMPLETE` | **false** |" in text
    assert "| `human_a11y_pass` | **false** |" in text
    assert "| `certified` | **false** |" in text


def test_cx4_retains_cx33_and_waike_pending():
    text = DOC.read_text()
    assert "| `CX3_EDUCATION_CAREER_DIGITAL_CLOSURE_PASS` | **true** |" in text
    assert "| `CX3_WAIKE_EARNED_CREDENTIAL_INTEGRATION_PASS` | **false** |" in text
    assert (ROOT / "docs" / "complete-experience" / "CX3_3_EDUCATION_CAREER_DIGITAL_CLOSURE_CONTROL.md").is_file()
