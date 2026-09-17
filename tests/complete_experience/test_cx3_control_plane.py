"""Portal CX3.1 control-plane fail-closed checks."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "docs" / "complete-experience" / "CX3_CREDENTIAL_WALLET_PORTFOLIO_CONTROL.md"


def test_cx3_control_doc_exists():
    assert DOC.is_file()
    text = DOC.read_text()
    assert "CX3_CONTRACTS_V1_PASS" in text
    assert "CX3_LAB_ISSUER_ED25519_PASS" in text
    assert "CX3_EVIDENCE_BOUND_ISSUANCE_PASS" in text
    assert "CX3_WALLET_GUI_PASS" in text
    assert "CX3_SIGNED_CREDENTIAL_JOURNEY_PASS" in text
    assert "CX3_PORTFOLIO_PRIVACY_EXPORT_PASS" in text
    assert "WAIKE_INTEGRATION_SEAM_PASS" in text
    assert "WAIKE_EARNED_CREDENTIAL_INTEGRATION_PASS" in text
    assert "CX3_1_WALLET_PORTFOLIO_FOUNDATION_PASS" in text
    assert "HUMAN_VALIDATION_PENDING" in text
    assert "eng/cx3-credential-wallet-portfolio-foundation" in text
    assert "CX3_2_WAIKE_REAL_EARNED_CREDENTIAL_INTEGRATION" in text
    assert "certification_claimed=false" in text or "certification_claimed` | **false**" in text
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=false" in text
    assert "do **not** set" in text.lower()
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=true" in text  # forbidden claim mentioned as do not set


def test_cx3_does_not_claim_waike_earned_pass_as_true_in_results():
    text = DOC.read_text()
    # Results table must keep earned integration false unless genuinely proven
    assert "| `WAIKE_EARNED_CREDENTIAL_INTEGRATION_PASS` | **false** |" in text


def test_cx2h4_control_still_points_next_gate():
    prior = ROOT / "docs" / "complete-experience" / "CX2H4_P0_DIGITAL_CLOSURE_CONTROL.md"
    assert prior.is_file()
    text = prior.read_text()
    assert "CX3_EDUCATION_CREDENTIALS_PORTFOLIO" in text


def test_credential_record_contract_keeps_claim_false():
    contract = ROOT / "docs" / "complete-experience" / "contracts" / "CredentialRecord_v1.json"
    text = contract.read_text()
    assert '"certification_claimed"' in text
    assert '"const": false' in text
