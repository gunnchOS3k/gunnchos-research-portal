import importlib.util
from pathlib import Path


def _validate():
    path = Path(__file__).resolve().parents[1] / "scripts" / "validate_control_plane.py"
    spec = importlib.util.spec_from_file_location("validate_control_plane", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.validate()


def test_control_plane_import_keeps_gates_false():
    dashboard = _validate()
    assert dashboard["v1_release_authorized"] is False
    assert dashboard["rc1_immutable"] is True
    assert dashboard["errors"] == []
    assert dashboard["scope_count"] > 0
    assert "IN_V1_REQUIRED" in dashboard["disposition_counts"]
