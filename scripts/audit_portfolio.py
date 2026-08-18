#!/usr/bin/env python3
"""Read-only portfolio audit for the 16-repo supervisor-ready programme.

Merges curated dissertation roles (portfolio/repo_roles.yaml) with live git/file
state from sibling checkouts. Never invents measurements, affiliations, or results.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None


SCOPE = [
    "gunnchos-device-os",
    "gunnchos-hardware-industrial-design",
    "archive-of-life-artifact-world",
    "gunnchAI3k",
    "waike-research-ops",
    "anime-aggressors",
    "gunnchos-emergent-service-intent-protocols",
    "pedestrian-pursuit",
    "beatlink-party",
    "edge-io-measurement-node",
    "gunnchos-research-portal",
    "ntn-resilience-sim",
    "7gc-digital-twin",
    "spectrumx-ai-ran-gary",
    "gunnchos-gpu-nr-baseband-platform",
    "readygary-6g-beam-selection",
]

ALLOWED_STATUSES = {
    "DIGITAL_PASS",
    "FAIL_DIGITAL",
    "PHYSICAL_PENDING",
    "EXTERNAL_PENDING",
    "HUMAN_QA_PENDING",
    "INDEPENDENT_REPRODUCTION_PENDING",
    "BLOCKED_HARDWARE",
    "BLOCKED_GPU",
    "BLOCKED_DATA",
    "NOT_APPLICABLE",
}


def run_git(repo: Path, *args: str) -> str:
    try:
        return subprocess.check_output(
            ["git", *args],
            cwd=repo,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return ""


def exists(path: Path) -> bool:
    return path.exists()


def uml_status(repo: Path) -> dict[str, Any]:
    uml = repo / "docs" / "uml"
    current = uml / "current"
    future = uml / "future"
    legacy = uml / "legacy"
    rendered = uml / "rendered"
    readme = uml / "README.md"
    trace = uml / "traceability_matrix.md"
    current_files = list(current.glob("*")) if current.exists() else []
    mature = (
        readme.exists()
        and current.exists()
        and future.exists()
        and legacy.exists()
        and bool(current_files)
    )
    placeholder_only = readme.exists() and not current.exists()
    if mature:
        label = "STRUCTURED_CURRENT_FUTURE_LEGACY"
    elif placeholder_only:
        label = "PLACEHOLDER_README_ONLY"
    elif uml.exists():
        label = "PARTIAL"
    else:
        label = "MISSING"
    return {
        "label": label,
        "docs_uml": uml.exists(),
        "readme": readme.exists(),
        "current": current.exists() and bool(current_files),
        "future": future.exists(),
        "legacy": legacy.exists(),
        "rendered": rendered.exists(),
        "traceability": trace.exists(),
    }


def classify_uml_gate(uml: dict[str, Any]) -> str:
    if uml["label"] == "STRUCTURED_CURRENT_FUTURE_LEGACY":
        return "DIGITAL_PASS"
    return "FAIL_DIGITAL"


def _parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the curated repo_roles.yaml subset without PyYAML.

    Supports nested mappings, lists of scalars, and lists of mappings.
    """
    lines = text.splitlines()
    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, root)]

    def current(indent: int):
        while stack and stack[-1][0] >= indent:
            stack.pop()
        return stack[-1][1]

    i = 0
    while i < len(lines):
        raw = lines[i]
        i += 1
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        stripped = raw.strip()
        container = current(indent)
        if stripped.startswith("- "):
            item = stripped[2:]
            if isinstance(container, list):
                pass
            else:
                raise ValueError(f"list item without list parent: {raw}")
            if ":" in item and not item.startswith("{") and not (item.startswith('"') and item.endswith('"')):
                key, _, val = item.partition(":")
                d: dict[str, Any] = {key.strip(): _scalar(val.strip())}
                container.append(d)
                stack.append((indent + 2, d))
            else:
                container.append(_scalar(item))
            continue
        key, _, rest = stripped.partition(":")
        key = key.strip()
        rest = rest.strip()
        if rest == "":
            # peek next non-empty
            j = i
            nxt = ""
            while j < len(lines):
                if lines[j].strip() and not lines[j].lstrip().startswith("#"):
                    nxt = lines[j]
                    break
                j += 1
            nindent = len(nxt) - len(nxt.lstrip(" ")) if nxt else indent + 2
            child: Any = [] if (nxt.strip().startswith("- ")) else {}
            if isinstance(container, dict):
                container[key] = child
            else:
                raise ValueError(f"mapping key in non-dict: {raw}")
            stack.append((indent, container))
            stack.append((nindent - 1, child) if False else (indent, container))
            # push child as current level
            stack.append((indent + 1, child) if nindent > indent else (indent + 2, child))
        else:
            if isinstance(container, dict):
                container[key] = _scalar(rest)
            else:
                raise ValueError(f"scalar in non-dict: {raw}")
    return root


def _scalar(val: str) -> Any:
    if val in ("null", "~", ""):
        return None
    if val in ("true", "false"):
        return val == "true"
    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
        return val[1:-1]
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        if not inner:
            return []
        return [_scalar(p.strip()) for p in inner.split(",")]
    return val


def load_roles(portal_root: Path) -> dict[str, Any]:
    json_path = portal_root / "portfolio" / "repo_roles.json"
    yaml_path = portal_root / "portfolio" / "repo_roles.yaml"
    if json_path.exists():
        return json.loads(json_path.read_text(encoding="utf-8"))
    if yaml is not None and yaml_path.exists():
        return yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    raise SystemExit("missing portfolio/repo_roles.json")


def audit_repo(repo: Path, role: dict[str, Any]) -> dict[str, Any]:
    uml = uml_status(repo)
    dirty = run_git(repo, "status", "--porcelain")
    dirty_count = len([ln for ln in dirty.splitlines() if ln.strip()])
    branch = run_git(repo, "rev-parse", "--abbrev-ref", "HEAD")
    head = run_git(repo, "rev-parse", "HEAD")
    remote = run_git(repo, "remote", "get-url", "origin")
    ci = (repo / ".github" / "workflows").exists()
    license_ok = any((repo / n).exists() for n in ("LICENSE", "LICENSE.md", "LICENSE.txt"))
    pixel_doc = (repo / "docs" / "PIXEL_6A_ACCEPTANCE.md").exists()
    android = (repo / "android").exists() or (repo / "export_presets.cfg").exists()
    repro = (repo / "REPRODUCIBILITY.md").exists()
    citation = (repo / "CITATION.cff").exists()
    env_committed = (repo / ".env").exists()
    env_example = (repo / ".env.example").exists()
    makefile = (repo / "Makefile").exists()
    reproduce_target = False
    if makefile:
        mk = (repo / "Makefile").read_text(encoding="utf-8", errors="replace")
        reproduce_target = "\nreproduce:" in mk or mk.startswith("reproduce:") or "\nreproduce :" in mk

    digital_blockers: list[str] = []
    if uml["label"] != "STRUCTURED_CURRENT_FUTURE_LEGACY":
        digital_blockers.append("uml_current_future_legacy_incomplete")
    if not license_ok:
        digital_blockers.append("license_missing")
    if not ci:
        digital_blockers.append("ci_missing")
    if not repro and role.get("classification") == "core":
        digital_blockers.append("reproducibility_md_missing")
    if env_committed:
        digital_blockers.append("dotenv_committed")
    if dirty_count:
        digital_blockers.append(f"dirty_working_tree:{dirty_count}")

    physical_blockers: list[str] = []
    external_blockers: list[str] = []
    human_qa_blockers: list[str] = []

    name = role["repository"]
    if name in {
        "gunnchos-hardware-industrial-design",
        "gunnchos-device-os",
        "edge-io-measurement-node",
    }:
        physical_blockers.append("physical_device_or_lab_measurement_required")
    if name == "gunnchos-gpu-nr-baseband-platform":
        physical_blockers.append("BLOCKED_GPU unless CUDA runner present")
    if name in {
        "anime-aggressors",
        "pedestrian-pursuit",
        "archive-of-life-artifact-world",
        "beatlink-party",
        "gunnchAI3k",
        "waike-research-ops",
    }:
        human_qa_blockers.append("HUMAN_QA_PENDING human playtest_or_usability")
    if android or pixel_doc:
        human_qa_blockers.append("PIXEL_6A_ACCEPTANCE requires authorized device")
    if role.get("visibility_note") == "private":
        external_blockers.append("repository_visibility_owner_action")
    if role.get("classification") == "core":
        external_blockers.append("INDEPENDENT_REPRODUCTION_PENDING")

    digital_status = "FAIL_DIGITAL" if digital_blockers else "DIGITAL_PASS"
    physical_status = "PHYSICAL_PENDING" if physical_blockers else "NOT_APPLICABLE"
    if name == "gunnchos-gpu-nr-baseband-platform":
        physical_status = "BLOCKED_GPU"
    external_status = "EXTERNAL_PENDING" if external_blockers else "NOT_APPLICABLE"
    human_status = "HUMAN_QA_PENDING" if human_qa_blockers else "NOT_APPLICABLE"

    evidence_level = "SYNTHETIC_SIM"
    if name == "spectrumx-ai-ran-gary":
        evidence_level = "OPEN_DATA_BACKED"  # competition IQ path exists; still not field-validated
    if name == "edge-io-measurement-node":
        evidence_level = "EMULATED"
    if name in {"anime-aggressors", "pedestrian-pursuit", "beatlink-party", "archive-of-life-artifact-world"}:
        evidence_level = "EMULATED"

    user_facing = name in {
        "gunnchos-research-portal",
        "gunnchAI3k",
        "waike-research-ops",
        "anime-aggressors",
        "pedestrian-pursuit",
        "archive-of-life-artifact-world",
        "beatlink-party",
        "gunnchos-device-os",
    }

    return {
        "repository": name,
        "layer": role.get("layer"),
        "dissertation_role": role.get("dissertation_role"),
        "rq": role.get("rq"),
        "classification": role.get("classification"),
        "public_supporting_core": role.get("public_supporting_core"),
        "visibility_note": role.get("visibility_note", "public"),
        "current_branch": branch or "UNKNOWN",
        "current_commit": head or "UNKNOWN",
        "remote": remote,
        "dirty_count": dirty_count,
        "primary_language_runtime": role.get("primary_language"),
        "canonical_run_command": role.get("canonical_run_command"),
        "canonical_test_command": role.get("canonical_test_command"),
        "canonical_reproduce_command": role.get("canonical_reproduce_command"),
        "uml_status": uml["label"],
        "uml": uml,
        "uml_gate": classify_uml_gate(uml),
        "clean_clone_status": "UNVERIFIED_THIS_AUDIT",
        "android_status": (
            "PIXEL_6A_DOC_MISSING" if android and not pixel_doc else
            ("DOCUMENTED_NOT_DEVICE_TESTED" if pixel_doc else "NOT_APPLICABLE")
        ),
        "current_evidence_level": evidence_level,
        "user_facing_status": "USER_FACING" if user_facing else "RESEARCH_OR_INFRA",
        "digital_status": digital_status,
        "physical_status": physical_status,
        "external_status": external_status,
        "human_qa_status": human_status,
        "digital_blockers": digital_blockers,
        "physical_blockers": physical_blockers,
        "external_blockers": external_blockers,
        "human_qa_blockers": human_qa_blockers,
        "files": {
            "readme": (repo / "README.md").exists(),
            "makefile": makefile,
            "reproduce_make_target": reproduce_target,
            "license": license_ok,
            "citation": citation,
            "reproducibility": repro,
            "ci": ci,
            "env_example": env_example,
            "env_committed": env_committed,
            "pixel_6a_doc": pixel_doc,
            "android_tree": android,
        },
        "oulu_framing": role.get("oulu_framing", "none"),
    }


def dump_yaml(data: Any, indent: int = 0) -> str:
    """Small YAML dumper so the audit does not require PyYAML to *write*."""
    sp = "  " * indent
    if isinstance(data, dict):
        lines = []
        for k, v in data.items():
            if v is None:
                lines.append(f"{sp}{k}: null")
            elif isinstance(v, (dict, list)):
                if not v:
                    lines.append(f"{sp}{k}: {'[]' if isinstance(v, list) else '{}'}")
                else:
                    lines.append(f"{sp}{k}:")
                    lines.append(dump_yaml(v, indent + 1))
            elif isinstance(v, bool):
                lines.append(f"{sp}{k}: {'true' if v else 'false'}")
            elif isinstance(v, (int, float)):
                lines.append(f"{sp}{k}: {v}")
            else:
                s = str(v).replace('"', '\\"')
                lines.append(f'{sp}{k}: "{s}"' if (":" in s or s == "" or "\n" in s) else f"{sp}{k}: {s}")
        return "\n".join(lines)
    if isinstance(data, list):
        lines = []
        for item in data:
            if isinstance(item, (dict, list)):
                lines.append(f"{sp}-")
                dumped = dump_yaml(item, indent + 1)
                lines.append(dumped)
            else:
                if isinstance(item, bool):
                    lines.append(f"{sp}- {'true' if item else 'false'}")
                else:
                    s = str(item)
                    lines.append(f'{sp}- "{s}"' if (":" in s or " " in s) else f"{sp}- {s}")
        return "\n".join(lines)
    return f"{sp}{data}"


def dashboard_md(manifest: dict[str, Any]) -> str:
    rows = []
    for rec in manifest["repositories"]:
        rows.append(
            f"| `{rec['repository']}` | {rec['rq'] or '—'} | `{rec['classification']}` | "
            f"`{rec['current_branch']}` | `{rec['current_commit'][:12]}` | `{rec['uml_status']}` | "
            f"`{rec['digital_status']}` | `{rec['physical_status']}` | `{rec['external_status']}` | "
            f"`{rec['human_qa_status']}` | `{rec['current_evidence_level']}` |"
        )
    table = "\n".join(rows)
    gates = manifest["gates"]
    return f"""# Portfolio readiness dashboard

Generated: {manifest['generated_at']}
Generator: `scripts/audit_portfolio.py`
Branch context: live checkouts under `{manifest['repos_root']}`

This dashboard is **descriptive of the audited trees**. A passing test is not physical readiness.
A simulation is not RF performance. A generated RFQ packet is not a sent RFQ.

## Gates

```text
AUTOMATABLE_SUPERVISOR_READY = {gates['AUTOMATABLE_SUPERVISOR_READY']}
CONTACT_SUPERVISOR_READY = {gates['CONTACT_SUPERVISOR_READY']}
DIGITAL_MANUFACTURING_READY = {gates['DIGITAL_MANUFACTURING_READY']}
PIXEL_6A_READY = {gates['PIXEL_6A_READY']}
CORE_RESEARCH_REPRODUCIBLE = {gates['CORE_RESEARCH_REPRODUCIBLE']}
INDEPENDENT_REPRODUCTION = {gates['INDEPENDENT_REPRODUCTION']}
```

## Repositories

| Repository | RQ | Class | Branch | Commit | UML | Digital | Physical | External | Human QA | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
{table}

## How to regenerate

```bash
make audit
```
"""


def compute_gates(records: list[dict[str, Any]], pixel_authorized: bool) -> dict[str, str]:
    digital_fail = any(r["digital_status"] == "FAIL_DIGITAL" for r in records)
    dirty_core = any(r["dirty_count"] and r["classification"] == "core" for r in records)
    automatable = "FAIL" if digital_fail or dirty_core else "PASS"
    contact = "BLOCKED"
    manufacturing = "FAIL"
    pixel = "PASS" if pixel_authorized else "BLOCKED"
    core_repro = "BLOCKED"
    independent = "PENDING"
    return {
        "AUTOMATABLE_SUPERVISOR_READY": automatable,
        "CONTACT_SUPERVISOR_READY": contact,
        "DIGITAL_MANUFACTURING_READY": manufacturing,
        "PIXEL_6A_READY": pixel,
        "CORE_RESEARCH_REPRODUCIBLE": core_repro,
        "INDEPENDENT_REPRODUCTION": independent,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--portal-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--repos-root",
        type=Path,
        default=Path(os.environ.get("PORTFOLIO_REPOS_ROOT", "")).resolve()
        if os.environ.get("PORTFOLIO_REPOS_ROOT")
        else None,
    )
    parser.add_argument("--write", action="store_true", default=True)
    parser.add_argument("--no-write", action="store_true")
    parser.add_argument("--pixel-authorized", action="store_true")
    args = parser.parse_args()
    portal = args.portal_root
    repos_root = args.repos_root or portal.parent
    roles_doc = load_roles(portal)
    role_by_name = {r["repository"]: r for r in roles_doc["repositories"]}

    records = []
    missing = []
    for name in SCOPE:
        path = portal if name == "gunnchos-research-portal" else repos_root / name
        if name == "gunnchos-research-portal":
            path = portal
        if not path.exists():
            missing.append(name)
            continue
        role = role_by_name[name]
        records.append(audit_repo(path, role))

    pixel_authorized = args.pixel_authorized
    gates = compute_gates(records, pixel_authorized)
    manifest = {
        "schema": "gunnchos.supervisor_ready_manifest.v1",
        "generated_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "working_title": roles_doc["canonical_narrative"]["working_title"],
        "repos_root": str(repos_root),
        "missing_checkouts": missing,
        "gates": gates,
        "pixel_adb_note": "authorized device required; unauthorized attachment is BLOCKED",
        "repositories": records,
        "status_vocabulary": roles_doc["status_vocabulary"],
        "evidence_taxonomy": roles_doc["evidence_taxonomy"],
    }

    if not args.no_write:
        out = portal / "portfolio" / "supervisor_ready_manifest.yaml"
        out.parent.mkdir(parents=True, exist_ok=True)
        header = (
            "# Generated by scripts/audit_portfolio.py — do not hand-edit SHAs.\n"
            "# Curated roles live in portfolio/repo_roles.yaml.\n"
        )
        out.write_text(header + dump_yaml(manifest) + "\n", encoding="utf-8")
        dash = portal / "docs" / "phd" / "PORTFOLIO_READINESS_DASHBOARD.md"
        dash.parent.mkdir(parents=True, exist_ok=True)
        dash.write_text(dashboard_md(manifest), encoding="utf-8")
        json_out = portal / "portfolio" / "supervisor_ready_manifest.json"
        json_out.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {out}")
        print(f"wrote {dash}")
        print(f"wrote {json_out}")

    print(f"AUTOMATABLE_SUPERVISOR_READY={gates['AUTOMATABLE_SUPERVISOR_READY']}")
    print(f"CONTACT_SUPERVISOR_READY={gates['CONTACT_SUPERVISOR_READY']}")
    print(f"repos_audited={len(records)} missing={missing}")
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
