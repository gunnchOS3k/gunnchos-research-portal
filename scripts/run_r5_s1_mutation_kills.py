#!/usr/bin/env python3
"""Disposable mutation kill harness for portal R5-S1 (mutated files never committed)."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = Path("scripts/audit_portfolio.py")
ART = ROOT / "artifacts" / "code_health_r5_s1" / "portal"


def flip_return_zero(text: str) -> str:
    return re.sub(r"return\s+0\b", "return 1", text, count=1)


def copy_repo(dst: Path) -> None:
    ignore = shutil.ignore_patterns(
        ".git",
        ".tmp_*",
        "artifacts",
        "node_modules",
        ".pytest_cache",
        "__pycache__",
        ".worktrees",
        "*.pyc",
    )
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(ROOT, dst, symlinks=True, ignore=ignore)


def run_make_test(cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["make", "test"],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        timeout=420,
    )


def main() -> int:
    ART.mkdir(parents=True, exist_ok=True)
    base = Path(tempfile.mkdtemp(prefix="portal_r5s1_mut_"))
    try:
        clean = base / "clean"
        copy_repo(clean)
        base_run = run_make_test(clean)
        if base_run.returncode != 0:
            print("baseline make test failed", file=sys.stderr)
            print(base_run.stdout[-1000:], file=sys.stderr)
            print(base_run.stderr[-1000:], file=sys.stderr)
            return 2

        mutated = base / "mutated"
        copy_repo(mutated)
        path = mutated / TARGET
        original = path.read_text(encoding="utf-8")
        flipped = flip_return_zero(original)
        if flipped == original:
            print("mutation did not apply", file=sys.stderr)
            return 3
        path.write_text(flipped, encoding="utf-8")
        mut_run = run_make_test(mutated)
        killed = mut_run.returncode != 0
        result = {
            "repository": "gunnchos-research-portal",
            "path": str(TARGET),
            "kind": "flip_return_zero",
            "baseline_pass": True,
            "mutated_pass": mut_run.returncode == 0,
            "mutated_returncode": mut_run.returncode,
            "mutation_outcome": "MUTATION_KILLED" if killed else "MUTATION_SURVIVED",
            "MUTATED_FILES_COMMITTED": False,
            "worktree": str(mutated),
        }
        (ART / "MUTATION_REGRESSION_RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps(result, indent=2))
        return 0 if killed else 1
    finally:
        shutil.rmtree(base, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
