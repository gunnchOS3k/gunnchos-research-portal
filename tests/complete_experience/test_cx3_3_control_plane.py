"""Portal CX3.3 control-plane fail-closed checks."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "docs" / "complete-experience" / "CX3_3_EDUCATION_CAREER_DIGITAL_CLOSURE_CONTROL.md"


def test_cx33_control_doc_exists():
    assert DOC.is_file()
    text = DOC.read_text()
    assert "CX3_3_REBIND_PASS" in text
    assert "WAIKE_REAL_EARNED_EVIDENCE_AVAILABLE" in text
    assert "CX3_WAIKE_EARNED_CREDENTIAL_INTEGRATION_PASS" in text
    assert "CX3_EDUCATION_TIMELINE_PASS" in text
    assert "CX3_SKILL_EVIDENCE_GRAPH_PASS" in text
    assert "CX3_CAREER_PACKAGE_PASS" in text
    assert "CX3_CAREER_PACKAGE_RECOVERY_PASS" in text
    assert "CX3_VERIFIER_MATRIX_PASS" in text
    assert "CX3_AUTOMATED_A11Y_PASS" in text
    assert "CX3_NO_SECOND_COMPUTER_FINAL_PASS" in text
    assert "CX3_3_SECURITY_REGRESSION_FREE" in text
    assert "CX3_EDUCATION_CAREER_DIGITAL_CLOSURE_PASS" in text
    assert "eng/cx3-education-career-digital-closure" in text
    assert "docs/cx3-education-career-digital-closure-control" in text
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=false" in text
    assert "do **not** set" in text.lower()
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=true" in text
    assert "CX3_WAIKE_RELEASE_DEPENDENCY_WAIT" in text
    assert "certification_claimed=false" in text or "certification_claimed` | **false**" in text


def test_cx33_keeps_waike_earned_false_unless_proven():
    text = DOC.read_text()
    assert "| `CX3_WAIKE_EARNED_CREDENTIAL_INTEGRATION_PASS` | **false** |" in text
    assert "| `WAIKE_REAL_EARNED_EVIDENCE_AVAILABLE` | **false** |" in text
    assert "| `FULL_COMPLETE_EXPERIENCE_COMPLETE` | **false** |" in text


def test_prior_cx_controls_still_present():
    assert (ROOT / "docs" / "complete-experience" / "CX3_CREDENTIAL_WALLET_PORTFOLIO_CONTROL.md").is_file()
    assert (ROOT / "docs" / "complete-experience" / "CX3_2_WAIKE_CAREER_SHARING_VERIFIER_CONTROL.md").is_file()
