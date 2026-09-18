# CX4.1 Control — Validation Center (Human/Field Task, Rating, Evidence, Submission UI)

Stacked on Portal CX4.0 (`docs/cx4-human-physical-external-readiness-control`).
Does **not** touch Portal #14/#15. Does **not** modify WAIKE release/main. No Device Lab. No merges.

The Validation Center is a **human-evidence collection system**. Software existence must **not** be converted into human/physical PASS.

## Device OS DRAFT

| PR | Branch | Base |
|----|--------|------|
| CX4.0 | `eng/cx4-human-physical-external-readiness` | CX3.3 |
| CX4.1 (this wave) | `eng/cx4-validation-center-human-field-ui` | CX4.0 |

## Portal DRAFT

| PR | Branch | Base |
|----|--------|------|
| CX4.0 | `docs/cx4-human-physical-external-readiness-control` | CX3.3 |
| CX4.1 (this wave) | `docs/cx4-validation-center-control` | CX4.0 |

## Implementation state (software)

| Token | Value |
|-------|-------|
| `CX4_VALIDATION_CENTER_GUI_PASS` | **true** |
| `CX4_VALIDATION_TASK_LIBRARY_PASS` | **true** |
| `CX4_VALIDATION_RATING_UI_PASS` | **true** |
| `CX4_VALIDATION_EVIDENCE_CAPTURE_PASS` | **true** |
| `CX4_VALIDATION_CENTER_OFFLINE_AUTOSAVE_PASS` | **true** |
| `CX4_VALIDATION_SUBMISSION_BUNDLE_PASS` | **true** |
| `CX4_VALIDATION_REVIEWER_SIGNOFF_ENFORCED` | **true** |
| `CX4_EDMUND_ACTION_PACKET_UI_MAPPED` | **true** |
| `CX4_VALIDATION_CENTER_AUTOMATED_A11Y_PASS` | **true** |
| `CX4_VALIDATION_CENTER_SECURITY_PASS` | **true** |
| `MINORS_MODE_DISABLED_BY_DEFAULT` | **true** |

## Session truth (no fabricated human sessions)

| Metric | Value |
|--------|-------|
| Real human sessions submitted | **0** |
| Reviewer-signed real sessions | **0** |

## Available packs (not all active by default)

- `validation_center_smoke` (active by default for software drills only)
- `human_a11y`
- `physical_printer`
- `camera_mic_av`
- `physical_peripherals`
- `device_quartet_evt` / `device_quartet_dvt` / `device_quartet_pvt`
- `firmware_lifecycle`
- `support_repair_rma`
- `external_chat_meeting` (pending external)
- `institutional_issuer` (pending external)
- `privacy_review` / `rights_review` (pending external)
- `certification` / `manufacturing` (pending external)

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
| `certified` | **false** |
| `legal_approval` | **false** |
| `manufacturing_pass` | **false** |

## Retained CX4.0 / CX3.3

| Token | Value |
|-------|-------|
| `CX4_ALL_AUTOMATABLE_NON_DIGITAL_PREWORK_PASS` | **true** |
| `CX3_EDUCATION_CAREER_DIGITAL_CLOSURE_PASS` | **true** |
| `CX3_WAIKE_EARNED_CREDENTIAL_INTEGRATION_PASS` | **false** |
| `WAIKE_REAL_EARNED_EVIDENCE_AVAILABLE` | **false** |

## Evidence paths (Device OS)

- UI: `apps/validation_center/`
- Package: `gunnchos_device_os/cx4_validation_center/`
- Artifacts: `artifacts/complete_experience/cx4_1/`
- Docs: `docs/complete-experience/cx4_validation_center/`
- Tests: `tests/cx4_validation_center/`

## Concurrency

No QEMU by default for this campaign. Prefer host-side tests. If guest ever required: wait for `/tmp/gunnchos-cx-qemu.lock`; never kill foreign QEMU.

## Next action

`NEXT_CX_ACTION=BEGIN_REAL_HUMAN_VALIDATION_SESSIONS_IN_VALIDATION_CENTER`

Do **not** start real human sessions from this control plane alone.
Do **not** fabricate human sessions.
