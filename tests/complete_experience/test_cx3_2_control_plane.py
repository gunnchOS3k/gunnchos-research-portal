"""Portal CX3.2 control-plane fail-closed checks."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "docs" / "complete-experience" / "CX3_2_WAIKE_CAREER_SHARING_VERIFIER_CONTROL.md"


def test_cx32_control_doc_exists():
    assert DOC.is_file()
    text = DOC.read_text()
    assert "CX3_1_WALLET_PORTFOLIO_FOUNDATION_PASS" in text
    assert "WAIKE_REAL_EARNED_EVIDENCE_AVAILABLE" in text
    assert "CX3_WAIKE_READ_ONLY_PROVIDER_PASS" in text
    assert "CX3_WAIKE_EARNED_CREDENTIAL_INTEGRATION_PASS" in text
    assert "CX3_REAL_CAREER_PROFILE_GUI_PASS" in text
    assert "CX3_RESUME_EXPORT_PASS" in text
    assert "CX3_PORTFOLIO_SHARE_PACKAGE_PASS" in text
    assert "CX3_INDEPENDENT_VERIFIER_PASS" in text
    assert "CX3_REAL_VERIFIER_GUI_PASS" in text
    assert "CX3_SELECTIVE_DISCLOSURE_PASS" in text
    assert "CX3_VERIFIER_REVOCATION_PROPAGATION_PASS" in text
    assert "CX3_OFFLINE_CAREER_VERIFIER_PASS" in text
    assert "CX3_NO_SECOND_COMPUTER_CAREER_PASS" in text
    assert "CX3_2_SECURITY_REGRESSION_FREE" in text
    assert "eng/cx3-waike-career-sharing-verifier-campaign" in text
    assert "docs/cx3-waike-career-sharing-verifier-control" in text or "CX3_2B_WAIKE_RELEASE_DEPENDENCY_RETRY" in text
    assert "certification_claimed=false" in text or "certification_claimed` | **false**" in text
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=false" in text
    assert "do **not** set" in text.lower()
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=true" in text


def test_cx32_keeps_waike_earned_false_unless_proven():
    text = DOC.read_text()
    assert "| `CX3_WAIKE_EARNED_CREDENTIAL_INTEGRATION_PASS` | **false** |" in text
    assert "| `WAIKE_REAL_EARNED_EVIDENCE_AVAILABLE` | **false** |" in text


def test_cx31_control_still_present():
    prior = ROOT / "docs" / "complete-experience" / "CX3_CREDENTIAL_WALLET_PORTFOLIO_CONTROL.md"
    assert prior.is_file()
    assert "CX3_1_WALLET_PORTFOLIO_FOUNDATION_PASS" in prior.read_text()
