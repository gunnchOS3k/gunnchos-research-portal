from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_cx2h_control_doc_exists():
    p = ROOT / "docs/complete-experience/CX2H_JOURNEY_DIGITAL_PASS_CONTROL.md"
    assert p.is_file()
    text = p.read_text()
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=false" in text
    assert "CX2H_XDG_PORTAL_SESSION_PASS" in text
    assert "J3_CLASS" in text
    assert "BLOCKED" in text
    assert "#14" in text and "#15" in text
    assert "CX2H2_DOCUMENT_PRINT_RECOVERY_J1_J7" in text
    assert "eng/cx2h-journey-digital-pass-closure" in text


def test_readme_mentions_cx2h():
    assert "CX2H" in (ROOT / "docs/complete-experience/README.md").read_text()
