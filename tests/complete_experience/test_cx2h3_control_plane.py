"""Portal CX2H.3 control-plane fail-closed checks."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "docs" / "complete-experience" / "CX2H3_BROWSER_MAIL_OFFLINE_CONTROL.md"


def test_cx2h3_control_doc_exists():
    assert DOC.is_file()
    text = DOC.read_text()
    assert "CX2H3_REAL_HTTPS_PROVIDER_PASS" in text
    assert "CX2H3_REAL_BROWSER_GUI_PASS" in text
    assert "CX2H3_EXACTLY_ONCE_RECONCILIATION_PASS" in text
    assert "HUMAN_VALIDATION_PENDING" in text
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=false" in text or "FULL_COMPLETE_EXPERIENCE_COMPLETE` | false" in text
    assert "eng/cx2h3-browser-mail-offline-j2-j5" in text
    assert "CX2H4_P0_DIGITAL_CLOSURE_AUDIT" in text


def test_cx2h2_control_still_points_next_gate():
    prior = ROOT / "docs" / "complete-experience" / "CX2H2_DOCUMENT_PRINT_RECOVERY_CONTROL.md"
    assert prior.is_file()
    text = prior.read_text()
    assert "CX2H3_BROWSER_MAIL_OFFLINE_J2_J5" in text
