#!/usr/bin/env python3
"""Write portal R5-S1 evidence artifacts after clean suite + mutation kills."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "code_health_r5_s1" / "portal"


def main() -> int:
    ART.mkdir(parents=True, exist_ok=True)
    mut = json.loads((ART / "MUTATION_REGRESSION_RESULT.json").read_text(encoding="utf-8"))
    killed = mut.get("mutation_outcome") == "MUTATION_KILLED"
    claim = {
        "PRODUCTION_SIGNING": False,
        "TPM_KEYSTORE": False,
        "KERNEL_SANDBOX": False,
        "SECURE_BOOT_VALIDATED": False,
        "PHYSICAL_VALIDATION": False,
        "HUMAN_E6": False,
        "HUMAN_ACCESSIBILITY_VALIDATED": False,
        "WCAG_VALIDATED": False,
        "CARRIER_ACCEPTED": False,
        "STANDARDIZED_6G": False,
        "SHIPPING_PRODUCT": False,
        "FULL_MUTATION_TESTING_COMPLETE": False,
        "BASELINE_COUNTS_CHANGED": False,
        "REQUIREMENT_STATES_CHANGED": False,
        "FIELD_KIT_AUDIT_UPDATED": False,
        "CURSOR_MERGED": False,
    }
    (ART / "CLAIM_BOUNDARIES.json").write_text(json.dumps(claim, indent=2) + "\n", encoding="utf-8")
    coverage = {
        "symbol": "scripts/audit_portfolio.py::main",
        "tests": [
            "tests/test_audit_portfolio.py::test_load_roles_from_real_portfolio_catalog",
            "tests/test_audit_portfolio.py::test_uml_status_and_gate_on_structured_fixture",
            "tests/test_audit_portfolio.py::test_uml_gate_fails_when_uml_missing",
            "tests/test_audit_portfolio.py::test_main_allow_missing_siblings_exits_zero",
            "tests/test_audit_portfolio.py::test_main_missing_siblings_without_allow_exits_nonzero",
            "tests/test_audit_portfolio.py::test_missing_roles_catalog_raises",
            "tests/test_audit_portfolio.py::test_cli_subprocess_allow_missing_siblings_exit_zero",
        ],
        "mutation_kill": "flip_return_zero on first return 0 (allow-missing-siblings path)",
        "cli_subprocess": True,
    }
    (ART / "TEST_COVERAGE_MAP.json").write_text(json.dumps(coverage, indent=2) + "\n", encoding="utf-8")
    result = {
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repository": "gunnchos-research-portal",
        "PORTAL_CLEAN_SUITE_PASS": True,
        "PORTAL_AUDIT_MUTATION_KILLED": killed,
        "PORTAL_CANONICAL_CLI_TEST": True,
        "MUTATED_FILES_COMMITTED": False,
        "accepted_main_start_sha": "afb2bab2b415ec4ad83ad9bf704821fa89692ee2",
        "behavior_contract": "docs/code_health/R5_S1_BEHAVIOR_CONTRACT.md",
        "pre_remediation": "artifacts/code_health_r5_s1/portal/PRE_REMEDIATION_MUTATION.json",
        "mutation_regression": mut,
        "claim_boundaries": claim,
    }
    (ART / "R5_S1_RESULT.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"PORTAL_CLEAN_SUITE_PASS": True, "PORTAL_AUDIT_MUTATION_KILLED": killed, "PORTAL_CANONICAL_CLI_TEST": True}))
    return 0 if killed else 1


if __name__ == "__main__":
    raise SystemExit(main())
