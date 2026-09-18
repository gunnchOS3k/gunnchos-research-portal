"""Portal CX2H.2 control-plane fail-closed checks."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "docs" / "complete-experience" / "CX2H2_DOCUMENT_PRINT_RECOVERY_CONTROL.md"


def test_cx2h2_control_doc_exists():
    assert DOC.is_file()
    text = DOC.read_text()
    assert "CX2H2_REAL_WRITER_GUI_PASS" in text
    assert "CX2H2_PHYSICAL_PRINTER_PENDING" in text
    assert "J2" in text and "BLOCKED" in text
    assert "J5" in text and "BLOCKED" in text
    assert "HUMAN_VALIDATION_PENDING" in text
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=false" in text or "FULL_COMPLETE_EXPERIENCE_COMPLETE` | false" in text
    assert "CX2H3_BROWSER_MAIL_OFFLINE_J2_J5" in text
    assert "eng/cx2h2-document-print-recovery-j1-j7" in text


def test_cx2h1b_control_still_points_next_gate():
    prior = ROOT / "docs" / "complete-experience" / "CX2H_JOURNEY_DIGITAL_PASS_CONTROL.md"
    assert prior.is_file()
    text = prior.read_text()
    assert "CX2H2_DOCUMENT_PRINT_RECOVERY_J1_J7" in text
