from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_cx2e_control_doc_exists():
    p = ROOT / "docs/complete-experience/CX2E_LINUX_GRAPHICAL_SESSION_CONTROL.md"
    assert p.is_file()
    text = p.read_text()
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=false" in text
    assert "guest_booted" in text
    assert "#14" in text and "#15" in text


def test_readme_mentions_cx2e():
    assert "CX2E" in (ROOT / "docs/complete-experience/README.md").read_text()
