# CX4.0 Control — Guest Rebind + Human/Physical/External Gate Readiness

Stacked on Portal CX3.3 (`docs/cx3-education-career-digital-closure-control`).
Does **not** touch Portal #14/#15. Does **not** modify WAIKE release/main. No Device Lab. No merges.

Preparation only: readiness packets and harnesses must **not** be converted into human/physical/external PASS.

## Device OS DRAFT

| PR | Branch | Base |
|----|--------|------|
| CX3.3 | `eng/cx3-education-career-digital-closure` | CX3.2 |
| CX4.0 (this wave) | `eng/cx4-human-physical-external-readiness` | CX3.3 |

## Portal DRAFT

| PR | Branch | Base |
|----|--------|------|
| CX3.3 | `docs/cx3-education-career-digital-closure-control` | CX3.2 |
| CX4.0 (this wave) | `docs/cx4-human-physical-external-readiness-control` | CX3.3 |

## Scope

1. Repair/re-prove current-tip CX guest overlay (canonical base + campaign overlay)
2. Compact current-tip guest smoke against CX3.3 stack
3. Human a11y validation packet (`J6_CLASS=HUMAN_VALIDATION_PENDING`)
4. Physical printer / camera / mic / AV / peripheral packets + collectors
5. Device Quartet EVT/DVT/PVT packets
6. Firmware lifecycle harness (simulation ≠ physical PASS)
7. Support/Care/repair/RMA readiness
8. Chat/meeting provider contracts (external pending)
9. Institutional issuer onboarding packet (`certification_claimed=false`)
10. Privacy/rights registers (no legal conclusions)
11. Certification + manufacturing matrices (no certified/mfg PASS)
12. Master non-digital blocker register + Edmund action packet
13. Fail-closed tests proving readiness ≠ PASS

Keep `FULL_COMPLETE_EXPERIENCE_COMPLETE=false`.

## Separated truth lanes

| Lane | Token |
|------|-------|
| Current-tip guest overlay | `CX4_CURRENT_TIP_GUEST_OVERLAY_PASS` |
| Current-tip guest smoke | `CX4_CURRENT_TIP_GUEST_SMOKE_PASS` |
| Human a11y packet ready | `CX4_HUMAN_A11Y_PACKET_READY` |
| Physical printer packet ready | `CX4_PHYSICAL_PRINTER_PACKET_READY` |
| Camera/mic/AV packet ready | `CX4_CAMERA_MIC_AV_PACKET_READY` |
| Peripheral packet ready | `CX4_PHYSICAL_PERIPHERAL_PACKET_READY` |
| EVT/DVT/PVT packets ready | `CX4_EVT_PACKET_READY` / `CX4_DVT_PACKET_READY` / `CX4_PVT_PACKET_READY` |
| Firmware lifecycle packet | `CX4_FIRMWARE_LIFECYCLE_PACKET_READY` |
| Support bundle / repair RMA | `CX4_SUPPORT_BUNDLE_READY` / `CX4_REPAIR_RMA_PACKET_READY` |
| Chat/meeting readiness | `CX4_CHAT_MEETING_PROVIDER_READINESS_PASS` |
| External issuer packet | `CX4_EXTERNAL_ISSUER_PACKET_READY` |
| Privacy / rights | `CX4_PRIVACY_REVIEW_PACKET_READY` / `CX4_RIGHTS_REGISTER_READY` |
| Certification / manufacturing | `CX4_CERTIFICATION_MATRIX_READY` / `CX4_MANUFACTURING_PACKET_READY` |
| Owner action packet | `CX4_OWNER_ACTION_PACKET_READY` |
| All automatable non-digital prework | `CX4_ALL_AUTOMATABLE_NON_DIGITAL_PREWORK_PASS` |

## Retained CX3.3

| Token | Value |
|-------|-------|
| `CX3_EDUCATION_CAREER_DIGITAL_CLOSURE_PASS` | **true** |
| `WAIKE_REAL_EARNED_EVIDENCE_AVAILABLE` | **false** |
| `CX3_WAIKE_EARNED_CREDENTIAL_INTEGRATION_PASS` | **false** |
| `J6_CLASS` | **HUMAN_VALIDATION_PENDING** |

## Kept pending (never flipped by preparation)

| Token | Value |
|-------|-------|
| `PHYSICAL_PRINTER_PENDING` | **true** |
| `PHYSICAL_CAMERA_MIC_AV_PENDING` | **true** |
| `EVT_PENDING` | **true** |
| `DVT_PENDING` | **true** |
| `PVT_PENDING` | **true** |
| `FULL_COMPLETE_EXPERIENCE_COMPLETE` | **false** |
| `certification_claimed` | **false** |
| `certified` | **false** |
| `legal_approval` | **false** |
| `manufacturing_pass` | **false** |
| `human_a11y_pass` | **false** |
| `external_provider_integration_pass` | **false** |

## Evidence

Device OS: `artifacts/complete_experience/cx4_0/`
Packets: `docs/complete-experience/cx4_readiness/`
Lab: `os_build/cx4_linux_lab/`
Canonical overlays: `os_build/cx_canonical/` (durable, worktree-independent)

## Concurrency

`/tmp/gunnchos-cx-qemu.lock` — one CX guest; never kill foreign QEMU.

## Results (filled after campaign run)

| Token | Value |
|-------|-------|
| `CX4_CURRENT_TIP_GUEST_OVERLAY_PASS` | **true** |
| `CX4_CURRENT_TIP_GUEST_SMOKE_PASS` | **true** |
| `CX4_HUMAN_A11Y_PACKET_READY` | **true** |
| `CX4_PHYSICAL_PRINTER_PACKET_READY` | **true** |
| `CX4_CAMERA_MIC_AV_PACKET_READY` | **true** |
| `CX4_PHYSICAL_PERIPHERAL_PACKET_READY` | **true** |
| `CX4_EVT_PACKET_READY` | **true** |
| `CX4_DVT_PACKET_READY` | **true** |
| `CX4_PVT_PACKET_READY` | **true** |
| `CX4_FIRMWARE_LIFECYCLE_PACKET_READY` | **true** |
| `CX4_SUPPORT_BUNDLE_READY` | **true** |
| `CX4_REPAIR_RMA_PACKET_READY` | **true** |
| `CX4_CHAT_MEETING_PROVIDER_READINESS_PASS` | **true** |
| `CX4_EXTERNAL_ISSUER_PACKET_READY` | **true** |
| `CX4_PRIVACY_REVIEW_PACKET_READY` | **true** |
| `CX4_RIGHTS_REGISTER_READY` | **true** |
| `CX4_CERTIFICATION_MATRIX_READY` | **true** |
| `CX4_MANUFACTURING_PACKET_READY` | **true** |
| `CX4_OWNER_ACTION_PACKET_READY` | **true** |
| `CX4_ALL_AUTOMATABLE_NON_DIGITAL_PREWORK_PASS` | **true** |
| `FULL_COMPLETE_EXPERIENCE_COMPLETE` | **false** |

## Next gate

`NEXT_CX_GATE=CX4_OWNER_HUMAN_PHYSICAL_EXECUTION`

When an automatable blocker remains: `NEXT_CX_GATE=CX4_0B_<EXACT_BLOCKER>`

Do **not** start the next gate from this control plane.
