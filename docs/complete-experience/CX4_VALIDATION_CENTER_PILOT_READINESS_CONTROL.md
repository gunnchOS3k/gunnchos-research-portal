# CX4.2 Control — Validation Center Pilot Readiness + Final Human Validation Freeze Prep

Stacked on Portal CX4.1 (`docs/cx4-validation-center-control`).
Does **not** touch Portal #14/#15. Does **not** modify WAIKE release/main. No Device Lab. No QEMU. No merges.

## Device OS DRAFT

| PR | Branch | Base |
|----|--------|------|
| CX4.1 | `eng/cx4-validation-center-human-field-ui` | CX4.0 |
| CX4.2 (this wave) | `eng/cx4-validation-center-pilot-readiness` | CX4.1 |

## Portal DRAFT

| PR | Branch | Base |
|----|--------|------|
| CX4.1 | `docs/cx4-validation-center-control` | CX4.0 |
| CX4.2 (this wave) | `docs/cx4-validation-center-pilot-readiness-control` | CX4.1 |

## Pilot readiness (software)

| Token | Value |
|-------|-------|
| `CX4_VALIDATION_CENTER_ONE_CLICK_LAUNCH_PASS` | **true** |
| `CX4_PARTICIPANT_ENTRY_FLOW_PASS` | **true** |
| `CX4_MODERATOR_SESSION_WIZARD_PASS` | **true** |
| `CX4_PARTICIPANT_ACCESSIBILITY_RENDERED_PASS` | **true** |
| `CX4_PARTICIPANT_RATING_FLOW_PASS` | **true** |
| `CX4_HUMAN_EVIDENCE_CAPTURE_UX_PASS` | **true** |
| `CX4_REVIEWER_WORKFLOW_PASS` | **true** |
| `CX4_HUMAN_VALIDATION_FREEZE_CHECK_PASS` | **true** |
| `CX4_VALIDATION_MATERIALITY_ENGINE_PASS` | **true** |
| `CX4_VALIDATION_REHEARSAL_FLOW_PASS` | **true** |
| `CX4_HUMAN_VALIDATION_DAY_PACKET_READY` | **true** |
| `CX4_VALIDATION_EXPORT_RECOVERY_PASS` | **true** |
| `CX4_VALIDATION_UI_COMPATIBILITY_PASS` | **true** |
| `CX4_VALIDATION_PILOT_SECURITY_PASS` | **true** |
| `CX4_FINAL_HUMAN_VALIDATION_ELIGIBLE` | **false** |

## Session truth

| Metric | Value |
|--------|-------|
| Real human sessions submitted | **0** |
| Rehearsal sessions (excluded from real count) | software rehearsal only |
| Reviewer-signed real sessions | **0** |

## Kept pending (never flipped by Validation Center software)

| Token | Value |
|-------|-------|
| `J6_CLASS` | **HUMAN_VALIDATION_PENDING** |
| `PHYSICAL_PRINTER_PENDING` | **true** |
| `PHYSICAL_CAMERA_MIC_AV_PENDING` | **true** |
| `EVT_PENDING` | **true** |
| `DVT_PENDING` | **true** |
| `PVT_PENDING` | **true** |
| `FULL_COMPLETE_EXPERIENCE_COMPLETE` | **false** |
| `human_a11y_pass` | **false** |
| `physical_printer_pass` | **false** |
| `physical_camera_mic_av_pass` | **false** |
| `evt_pass` | **false** |
| `dvt_pass` | **false** |
| `pvt_pass` | **false** |

## Evidence paths (Device OS)

- Launcher: `scripts/start-validation-center`
- Package: `gunnchos_device_os/cx4_validation_center/`
- Artifacts: `artifacts/complete_experience/cx4_2/`
- Docs: `docs/complete-experience/cx4_validation_center/`
- Tests: `tests/cx4_validation_center/test_cx42_pilot_readiness.py`

## Concurrency

No QEMU. Prefer host-side. Parallel-safe with release. If a test would contend with release resources: `DEFERRED_RELEASE_RESOURCE_CONTENTION`.

## Next action

`NEXT_CX_ACTION=WAIT_FOR_FINAL_ACCEPTED_BUILD_THEN_RUN_HUMAN_VALIDATION`

Do **not** start final human sessions from this control plane alone.
Do **not** fabricate human sessions.
Do **not** convert rehearsal/pilot into gating evidence.
