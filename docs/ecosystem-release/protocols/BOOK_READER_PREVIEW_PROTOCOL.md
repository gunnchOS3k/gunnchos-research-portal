# Technology Landscape — Reader-Preview Human Validation Protocol

**Repo:** `gunnchos-technology-landscape` (GitHub-only; not in local multi-repo workspace by default)  
**Evidence class:** `HUMAN_VALIDATION_PENDING` until sessions filed.  
**Digital baseline:** `origin/main` `8d56d214fa6490ba6f99058babea834b5d3bb4ab` (refresh before session).  
**CI note:** `reader-preview` + `ci` workflows success on that tip — digital CI ≠ human approval.

## Participant criteria
- Adults (≥18), STEM-curious or staff readers.
- Can complete a 30–45 minute guided reading session in the reader-preview surface.

## Consent / privacy
- Session notes may record chapter IDs and subjective scores only.
- No requirement to collect identity beyond a pseudonymous evaluator ID.

## Tasks
1. Open reader-preview for current main.
2. Read one foundational chapter end-to-end.
3. Follow one WAIKE-lab / evidence-backed example cross-link (if present).
4. Note clarity, trust, and “would recommend” scores 1–5.
5. Log defects (broken links, overclaims, accessibility friction).

## Metrics
- Clarity, trust, usefulness (1–5); binary `no_overclaim_detected`; defect list.
- **Internal pass bar:** median ≥3 and no S0 overclaim presenting physical/cert PASS falsely.

## Stop conditions
- Treating PhD `PUBLICATION_PIPELINE` manuscripts as this consumer guidebook SKU.
- Claiming `FIELD_VALIDATED` without recorded human sessions.
- Under-18 participants without approved consent path.

## Result schema (minimal)
```json
{
  "schema": "gunnchos.books.reader_preview_result.v1",
  "evidence_class": "HUMAN_VALIDATION_PENDING",
  "sha": "<12+ hex>",
  "evaluator_id": "reader-001",
  "scores": {"clarity": 0, "trust": 0, "usefulness": 0},
  "no_overclaim_detected": false,
  "defects": [],
  "HUMAN_READER_VALIDATION": false
}
```
