# WAIKE Staff Alpha Protocol

**Evidence class:** `HUMAN_VALIDATION_PENDING`  
**Digital baseline:** `gunnchos-waike-learning-platform@8610018a62e0` (+ curriculum pin `waike-research-ops@fbf7685bc568`).  
**Adults only.** No K-12 classroom claim.

## Participant criteria
- Staff / instructors / internal operators ≥18.
- Access to staff-alpha build on accepted main (or labeled candidate SHA).

## Tasks
1. Staff login / course browse across ≥3 tracks.
2. Assign or preview one assessment without claiming LMS cert.
3. Confirm gunnchAI assist stays within integrity + privacy boundaries.
4. Export / report smoke if available; note failures honestly.

## Metrics
- Task completion (Y/N), severity of defects (S0–S3), time-to-first-success, privacy incidents (must be 0).

## Consent / privacy
- Staff-alpha data only; no student PII from real classrooms.
- Retention per WAIKE / gunnchAI policies.

## Scoring rubric
- **PASS_INTERNAL:** all critical tasks complete, no S0/S1 privacy/security defects.
- Does not equal FERPA/OneRoster/QTI/LTI certification (`REGULATORY_PENDING`).

## Stop conditions
- Under-18 learner enrolled.
- Real classroom PII ingested.
- Claiming Device Lab WAIKE runtime PASS without current-pin evidence.

## Result schema (minimal)
```json
{
  "schema": "gunnchos.waike.staff_alpha_result.v1",
  "evidence_class": "HUMAN_VALIDATION_PENDING",
  "sha": "<12+ hex>",
  "HUMAN_CLASSROOM_VALIDATION": false,
  "tasks": [],
  "defects": [],
  "pass_internal": false
}
```
