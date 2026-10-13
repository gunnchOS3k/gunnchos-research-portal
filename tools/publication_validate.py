#!/usr/bin/env python3
"""Check actual three-paper submission files; do not infer scientific approval."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

PAPERS = {
    "I": ("7gc-digital-twin", "ieeeaccess", (150, 250)),
    "II": ("spectrumx-ai-ran-gary", "IEEEtran", (75, 200)),
    "III": ("ntn-resilience-sim", "IEEEoj", (150, 250)),
}
GATES = ["MANUSCRIPT_COMPILES", "CITATIONS_VERIFIED", "EXPERIMENT_REPRODUCED",
         "STATISTICS_VERIFIED", "CLAIMS_EVIDENCE_ALIGNED", "VENUE_FORMAT_VERIFIED",
         "AI_DISCLOSURE_PREPARED", "AUTHOR_METADATA_VERIFIED", "OWNER_REVIEW_READY",
         "OWNER_APPROVED", "SUBMISSION_AUTHORIZED"]


def clean_tex(text: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def flatten_tex(path: Path, errors: list[str], seen: set[Path] | None = None, tex_root: Path | None = None) -> str:
    seen = set() if seen is None else seen
    tex_root = path.parent if tex_root is None else tex_root
    if path in seen:
        return ""
    seen.add(path)
    if not path.is_file():
        errors.append(f"Missing TeX source: {path}")
        return ""
    text = clean_tex(path.read_text()).replace(r"\ArtifactRoot ", "")
    for kind, target in re.findall(r"\\(input|include)\{([^}]+)\}", text):
        target = target.replace(r"\ArtifactRoot ", "")
        linked = tex_root / target
        if not linked.suffix:
            linked = linked.with_suffix(".tex")
        child = flatten_tex(linked, errors, seen, tex_root)
        text = text.replace(f"\\{kind}{{{target}}}", child)
    return text


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def check_paper(base: Path, number: str) -> dict:
    repo, expected_class, abstract_range = PAPERS[number]
    root = base / repo
    package = root / "paper/submission"
    errors: list[str] = []
    warnings: list[str] = []
    entry = package / "manuscript.tex"
    pdf = package / "manuscript.pdf"
    bib = package / ("bibliography.bib" if number == "I" else "references.bib")
    text = flatten_tex(entry, errors)
    bibtext = bib.read_text() if bib.is_file() else ""
    if not bib.is_file():
        errors.append(f"Missing {bib.name}")
    classes = re.findall(r"\\documentclass(?:\[[^]]*\])?\{([^}]+)\}", text)
    if classes != [expected_class]:
        errors.append(f"Expected venue class {expected_class}; found {classes}")

    bibkeys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bibtext)
    duplicate_keys = sorted({k for k in bibkeys if bibkeys.count(k) > 1})
    if duplicate_keys:
        errors.append(f"Duplicate bibliography keys: {duplicate_keys}")
    citekeys = set()
    for group in re.findall(r"\\cite\w*\*?(?:\[[^]]*\]){0,2}\{([^}]+)\}", text):
        citekeys.update(k.strip() for k in group.split(","))
    undefined = sorted(citekeys - set(bibkeys))
    if undefined:
        errors.append(f"Undefined citation keys: {undefined}")
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    refs = re.findall(r"\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}", text)
    missing_refs = sorted(set(refs) - set(labels))
    if missing_refs:
        errors.append(f"Undefined cross-reference labels: {missing_refs}")
    if len(labels) != len(set(labels)):
        errors.append("Duplicate cross-reference labels")

    graphics = re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}", text)
    for target in graphics:
        if "\\" in target:
            warnings.append(f"Graphic path uses a macro; manual check: {target}")
            continue
        p = package / target
        if not p.is_file() and not any(p.with_suffix(ext).is_file() for ext in [".pdf", ".png", ".jpg", ".eps"]):
            errors.append(f"Missing included graphic: {target}")

    abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", text, re.S)
    abstract_words = None
    if not abstract:
        errors.append("Missing abstract")
    else:
        prose = re.sub(r"\\[A-Za-z]+", " ", abstract.group(1))
        abstract_words = len(re.findall(r"\b[\w]+(?:[-'][\w]+)*\b", prose))
        if not abstract_range[0] <= abstract_words <= abstract_range[1]:
            warnings.append(f"Approximate abstract word count {abstract_words} outside {abstract_range}; verify venue-specific count")

    sections = list(re.finditer(r"\\(?:section|subsection)\*?(?:\[[^]]*\])?\{([^}]+)\}", text))
    empty = []
    for i, section in enumerate(sections):
        body = text[section.end():sections[i + 1].start() if i + 1 < len(sections) else len(text)]
        if not body.strip() and not (i + 1 < len(sections) and "subsection" in sections[i + 1].group(0)):
            empty.append(section.group(1))
    if empty:
        errors.append(f"Empty sections: {empty}")
    for token in ["0000-0000-0000", "10.1109/ACCESS.2017.DOI", "10.1109/OJCOMS.2024.DOI"]:
        if token in text:
            errors.append(f"Publisher/identity placeholder remains: {token}")
    for token in ["Edmund Gunn", "gunnchOS", "egunnjr@gunnchos.com", "0009-0004-6546-2609"]:
        if token not in text:
            errors.append(f"Confirmed author metadata absent from source: {token}")
    if re.search(r"\b(?:TODO|TBD|INSERT HERE|Lorem ipsum)\b", text):
        warnings.append("Draft placeholder tokens require contextual review")

    log = package / "manuscript.log"
    if log.is_file():
        logtext = log.read_text(errors="replace")
        if re.search(r"(^!|undefined references|Citation .* undefined|Reference .* undefined|not found)", logtext, re.M | re.I):
            errors.append("Compilation log contains errors, unresolved references or missing files")
        if "Overfull \\hbox" in logtext:
            warnings.append("Overfull boxes in log require visual inspection")
    else:
        errors.append("Missing compiler log")

    pdf_pages = None
    pdf_text = ""
    if not pdf.is_file():
        errors.append("Missing compiled manuscript.pdf")
    else:
        try:
            from pypdf import PdfReader
            reader = PdfReader(pdf)
            pdf_pages = len(reader.pages)
            pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
            if any(not (page.extract_text() or "").strip() for page in reader.pages):
                errors.append("Empty PDF page")
            if "[?]" in pdf_text or "??" in pdf_text:
                errors.append("Unresolved citation/cross-reference markers in PDF text")
        except Exception as exc:
            errors.append(f"PDF inspection failed: {type(exc).__name__}: {exc}")

    gatefile = package / "QUALITY_GATES.json"
    declared_gates = json.loads(gatefile.read_text()) if gatefile.is_file() else None
    if declared_gates is None:
        warnings.append("Paper-specific QUALITY_GATES.json absent")

    files = sorted(p.relative_to(package).as_posix() for p in package.rglob("*") if p.is_file()) if package.exists() else []
    return {
        "paper": number, "repository": repo, "branch": git(root, "branch", "--show-current"),
        "local_head": git(root, "rev-parse", "HEAD"), "source_main": git(root, "rev-parse", "origin/main"),
        "package": str(package), "structural_checks_pass": not errors, "errors": errors,
        "warnings": warnings, "venue_class": classes, "abstract_words_approx": abstract_words,
        "section_titles": [x.group(1) for x in sections], "citation_keys": sorted(citekeys),
        "bibliography_entries": len(bibkeys), "included_graphics": graphics, "pdf_pages": pdf_pages,
        "manuscript_pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest() if pdf.is_file() else None,
        "files": files, "declared_scientific_gates": declared_gates,
        "scope_of_check": "Structural/file validation only. DOI truth, numerical claims, novelty, visual layout and human approval need their recorded substantive audits.",
        "external_links": sorted(set(re.findall(r"https?://[^\s{}<>]+", text))),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repos-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records = [check_paper(args.repos_root, number) for number in PAPERS]
    result = {"schema": "gunnchos.publication.file_validation.v1", "papers": records,
              "all_structural_checks_pass": all(x["structural_checks_pass"] for x in records)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    for item in records:
        print(f"Paper {item['paper']}: {len(item['errors'])} errors; {len(item['warnings'])} review warnings; pages={item['pdf_pages']}")
    raise SystemExit(0 if result["all_structural_checks_pass"] else 1)


if __name__ == "__main__":
    main()
