from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_cx2f_control_doc_exists():
    p = ROOT / "docs/complete-experience/CX2F_DRM_SHELL_RENDER_CAPTURE_CONTROL.md"
    assert p.is_file()
    text = p.read_text()
    assert "FULL_COMPLETE_EXPERIENCE_COMPLETE=false" in text
    assert "drm-backend.so" in text
    assert "#14" in text and "#15" in text
    assert "CX2G_" in text


def test_readme_mentions_cx2f():
    assert "CX2F" in (ROOT / "docs/complete-experience/README.md").read_text()
