# gunnchOS Ecosystem v1.0.0 — Final Push Control Pack

**Snapshot date:** 2026-09-30

This pack is the release-control layer for the last push from the already-published `v1.0.0-rc.1` to final `v1.0.0`.

The operating goal is simple:

> **Nothing gets lost, but not everything gets into v1.**

The pack is designed to prevent scope creep from disappearing, prevent old evidence from being reused accidentally, and keep digital, human, physical, rights, institutional, scientific, and vendor gates separate.

## Canonical documents

1. `01_V1_RELEASE_CHARTER_AND_SCOPE_AUTHORITY.md` — what v1 is and is not.
2. `02_V1_MASTER_SCOPE_CREEP_LEDGER.csv` — every tracked scope item and disposition.
3. `03_V1_COMPONENT_STATUS_MATRIX.md` — current product/repo state.
4. `04_V1_BLOCKER_AND_DEPENDENCY_REGISTER.md` — final-push blockers.
5. `05_V1_HUMAN_PHYSICAL_EXTERNAL_GATE_REGISTER.md` — gates automation must not fake.
6. `06_V1_ACCEPTANCE_EVIDENCE_INDEX.md` — final proof requirements.
7. `07_V1_CHANGE_CONTROL_AND_SCOPE_FREEZE_PROTOCOL.md` — how scope freezes.
8. `08_V1_FINAL_FREEZE_RC2_AND_FINAL_RUNBOOK.md` — last-push sequence.
9. `09_V1_PUBLIC_DEPLOYMENT_AND_DOMAIN_MAP.md` — `gunnchos.com` hosting map.
10. `10_V1_POST_V1_BACKLOG.md` — preserved scope that does not belong in v1.
11. `11_V1_OWNER_ACCEPTANCE_CHECKLIST.md` — owner-only review checklist.
12. `12_V1_DECISION_LOG.md` — release-impacting decisions.
13. `13_V1_LAST_PUSH_BOARD.md` — WIP-limited execution board.
14. `14_V1_DEFINITION_OF_DONE.md` — final release definition.
15. `15_V1_REQUIREMENT_TRACEABILITY_MATRIX.md` — requirement→repo→gate→evidence.
16. `16_SCOPE_CREEP_INTAKE_TEMPLATE.md` — intake for anything newly discovered.
17. `CURRENT_STATUS_SNAPSHOT.json` — current machine-readable snapshot.
18. `V1_MASTER_CONTROL.json` — current machine-readable release policy.

## Current release state

- `v1.0.0-rc.1`: **published historical prerelease**
- final `v1.0.0`: **not authorized**
- the September 21 final-freeze manifest is **stale for final release**
- major current candidate drafts:
  - Anime Aggressors PR #118
  - Pedestrian Pursuit PR #39
  - 3k MLV PR #6
  - Research Portal PR #48
- public Cloudflare hosting is being prepared but is not yet the production source of truth.

## Disposition vocabulary

Every new scope item must receive one of these:
- `IN_V1_REQUIRED`
- `IN_V1_CANDIDATE_PENDING_OWNER`
- `IN_V1_HUMAN_GATE`
- `IN_V1_CLAIM_BOUNDARY`
- `POST_V1`
- `POST_V1_PHYSICAL`
- `POST_V1_REGULATORY`
- `POST_V1_RIGHTS_BLOCKED`
- `POST_V1_VENDOR`
- `HISTORICAL_RELEASE`

If an item has no disposition, it is uncontrolled.
