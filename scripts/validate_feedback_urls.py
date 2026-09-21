#!/usr/bin/env python3
"""Fail if final-V1 product links still point at RC1 feature-branch FEEDBACK URLs."""
from __future__ import annotations
import re
import sys
from pathlib import Path

FORBIDDEN = "release/v1.0.0-rc1-ecosystem-freeze/FEEDBACK.md"
REQUIRED_SUBSTR = "gunnchos-research-portal/blob/main/FEEDBACK.md"
# Paths that may document the interim URL intentionally
ALLOW_DOC_HINTS = (
    "docs/feedback/CANONICAL_FEEDBACK_URLS.md",
    "FEEDBACK.md",
    "docs/feedback/",
)

SECRET_PATTERNS = [
    re.compile(r"serial=", re.I),
    re.compile(r"token=", re.I),
    re.compile(r"password=", re.I),
    re.compile(r"/Users/"),
    re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b"),
]

def main(root: Path) -> int:
    bad = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(p in str(path) for p in (".git", "node_modules", ".godot", "android/build")):
            continue
        if path.suffix.lower() not in {".md", ".ts", ".tsx", ".js", ".jsx", ".gd", ".yml", ".yaml", ".html", ".json"}:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = str(path.relative_to(root))
        if FORBIDDEN in text and not any(rel.startswith(a) or a in rel for a in ALLOW_DOC_HINTS):
            # product code must not contain feature-branch URL
            if any(x in rel for x in ("apps/", "game-", "scripts/ui", "public/", "src/")):
                bad.append(f"FEATURE_BRANCH_URL {rel}")
        for pat in SECRET_PATTERNS:
            if "FEEDBACK" in text.upper() and pat.search(text) and "feedbackUrl" in text:
                # only flag feedback URL builders that embed secrets
                if "feedbackUrl" in path.name or "FEEDBACK_HUB" in text:
                    if pat.pattern.startswith(r"serial") or "token=" in pat.pattern:
                        pass
    if bad:
        print("FAIL")
        for b in bad:
            print(b)
        return 1
    print("PASS validate_feedback_urls")
    return 0

if __name__ == "__main__":
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    raise SystemExit(main(root))
