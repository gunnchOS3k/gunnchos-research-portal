from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_cx2g_control_doc_exists():
    p = ROOT / "docs/complete-experience/CX2G_CHROMIUM_SHELL_RENDER_CONTROL.md"
    assert p.is_file()
    text = p.read_text()
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=false" in text
    assert "pkill -f chromium" in text
    assert "cx2g-gunnch-shell.service" in text
    assert "#14" in text and "#15" in text
    assert "CX2H_" in text
    assert "CX2G_CHROMIUM_RUNTIME_PASS" in text


def test_readme_mentions_cx2g():
    assert "CX2G" in (ROOT / "docs/complete-experience/README.md").read_text()
