"""Portal CX2H.4 control-plane fail-closed checks."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "docs" / "complete-experience" / "CX2H4_P0_DIGITAL_CLOSURE_CONTROL.md"


def test_cx2h4_control_doc_exists():
    assert DOC.is_file()
    text = DOC.read_text()
    assert "CX2H4_JOURNEY_REBIND_PASS" in text
    assert "CX2H4_J4_P0_DIGITAL_BLOCKER" in text
    assert "CX2H4_SPREADSHEET_P0_PASS" in text
    assert "CX2H4_PRESENTATION_P0_PASS" in text
    assert "CX2H4_NO_SECOND_COMPUTER_P0_PASS" in text
    assert "CX2H4_SECURITY_REGRESSION_FREE" in text
    assert "CX2H4_P0_DIGITAL_CLOSURE_PASS" in text
    assert "HUMAN_VALIDATION_PENDING" in text
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=false" in text or "FULL_COMPLETE_EXPERIENCE_COMPLETE` | **false**" in text
    assert "eng/cx2h4-p0-digital-closure-audit" in text
    assert "CX3_EDUCATION_CREDENTIALS_PORTFOLIO" in text
    # Must keep full complete experience false
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=false" in text or "| **false**" in text
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=true`" in text  # forbidden claim mentioned as "do not set"
    assert "do **not** set" in text.lower()


def test_cx2h4_cannot_claim_closure_if_blocker_register_nonempty_language():
    text = DOC.read_text()
    assert "Blocks CX3 count" in text
    assert "**0**" in text


def test_cx2h3_control_still_points_next_gate():
    prior = ROOT / "docs" / "complete-experience" / "CX2H3_BROWSER_MAIL_OFFLINE_CONTROL.md"
    assert prior.is_file()
    text = prior.read_text()
    assert "CX2H4_P0_DIGITAL_CLOSURE_AUDIT" in text
