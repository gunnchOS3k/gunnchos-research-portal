# HUMAN_VALIDATION_HANDOFF

- **Status:** READY (digital prerequisites verified by Stream H)
- **Generated (UTC):** 2026-09-18T19:12:00Z
- **`READY_TO_BEGIN_FULL_HUMAN_VALIDATION`:** **true**
- **`DIGITAL_ENGINEERING_EXHAUSTED`:** **true**

## Purpose

Turnkey packet to begin **authentic** human validation. Do not fabricate participants or results.

## Prerequisites (verified TRUE by Stream H)

| Prerequisite | Gate | Status |
|---|---|---|
| Software v1 pre-human engineering exhausted | `SOFTWARE_V1_PRE_HUMAN_ENGINEERING_EXHAUSTED` | TRUE |
| Automatable user journeys pass | `ALL_AUTOMATABLE_USER_JOURNEYS_PASS` | TRUE |
| Human validation infrastructure ready | `HUMAN_VALIDATION_INFRASTRUCTURE_READY` | TRUE |
| Defect/refinement loop ready | `HUMAN_REFINEMENT_LOOP_READY` | TRUE |
| WAIKE digital engineering exhausted | `WAIKE_DIGITAL_ENGINEERING_EXHAUSTED` | TRUE |
| gunnchAI pre-human engineering exhausted | `GUNNCHAI_PRE_HUMAN_ENGINEERING_EXHAUSTED` | TRUE |
| Games pre-playtest engineering exhausted | `GAMES_PRE_HUMAN_PLAYTEST_ENGINEERING_EXHAUSTED` | TRUE |
| Support diagnostic/KB digital prep | `SUPPORT_ENGINEERING_PREP_EXHAUSTED` | TRUE |

## How to run sessions (device-os)

```bash
# From gunnchos-device-os at accepted-main 438aaf2b… (or Stream A draft head after review)
PYTHONPATH=.:src python3 -m gunnchos_device_os.cx4_validation_center qualify-pilot
PYTHONPATH=.:src python3 -m gunnchos_device_os.cx4_validation_center freeze-check
./scripts/start-validation-center   # if present on branch
PYTHONPATH=.:src python3 -m gunnchos_device_os.cx4_validation_center validate-session <session.json>
PYTHONPATH=.:src python3 -m gunnchos_device_os.cx4_validation_center refinement-loop <sessions...>
```

Docs:

- `docs/complete-experience/cx4_validation_center/QUICK_START_HUMAN_VALIDATION.md`
- `docs/complete-experience/cx4_validation_center/HUMAN_VALIDATION_DAY_RUNBOOK.md`
- `docs/complete-experience/cx4_validation_center/PARTICIPANT_GUIDE.md`
- Forms UI: `apps/validation_center`

## Domain packets

| Domain | Focus | Notes |
|---|---|---|
| Complete Experience (J1–J7) | Office/paper, research, apps, care, vault, a11y, recovery | Physical printer/AV still pending in lab |
| WAIKE | Learner/instructor workflows | Curriculum authorship gaps remain content work |
| gunnchAI | Live tutoring quality | Synthetic eval ≠ human outcome |
| Games | Fun/balance/feel + a11y | Rights quarantine: do not ship uncleared assets |

## Explicitly forbidden

- Fabricating consent, participants, or PASS evidence
- Auto-promoting `CX4_FINAL_HUMAN_VALIDATION_ELIGIBLE` or physical/cert gates
- Treating SYNTHETIC / SIMULATION results as human/physical truth

## Remaining blocker class for outcomes

`HUMAN_VALIDATION_REQUIRED` — until real sessions + reviewer signoff land.
