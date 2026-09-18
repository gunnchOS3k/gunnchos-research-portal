# CX2D Control — Linux Production-Shell + Real User Journey Closure

Stacked on Portal CX2 (#18 `docs/cx2-real-surface-productization-control`).  
Does **not** touch Portal #14/#15.

## Device OS DRAFT stack

| PR | Branch | Base |
|----|--------|------|
| #135 CX0 | `eng/cx0-complete-experience-foundations` | main |
| #136 CX1 | `eng/cx1-ordinary-user-foundations` | CX0 |
| #137 CX2A | `eng/cx2a-real-experience-surfaces` | CX1 |
| #138 CX2B | `eng/cx2b-real-provider-integrations` | CX2A |
| #139 CX2C | `eng/cx2c-authentic-user-journeys` | CX2B |
| CX2D (this wave) | `eng/cx2d-linux-real-user-journey-closure` | CX2C |

## Production shell authority

**Path B** — `apps/gunnch_shell` is sole production GUI authority.  
`launcher_mock` is a deprecated adapter.  
Token: `CX2D_SINGLE_PRODUCTION_SHELL_AUTHORITY=true`

## Evidence classes (separated)

| Class | Meaning |
|-------|---------|
| CONTRACT_PASS | API/schema |
| HARNESS_PASS | Deterministic harness without real Linux GUI |
| REAL_PROVIDER_CLI_PASS | Real binary/protocol, no rendered shell |
| REAL_PROVIDER_GUI_PASS | Real provider + window |
| REAL_USER_JOURNEY_DIGITAL_PASS | Shell UI + provider + input + read-back + persistence |
| HUMAN_VALIDATION_PENDING | Human packet |
| PHYSICAL_VALIDATION_PENDING | Physical SI |
| EXTERNAL_PROVIDER_PENDING | External dependency |
| BLOCKED | Missing required condition |

Device OS evidence path: `artifacts/complete_experience/cx2d/` only.  
Do not inherit macOS CX2 provider PASS as Linux PASS.

## Pending (honest)

- Linux graphical session journey proof (Weston/Wayland guest)
- All `CX2D_REAL_*_WINDOW` / GUI domain PASSes until guest proof
- `HUMAN_A11Y_PENDING` / physical printer / AV / camera-mic

`FULL_COMPLETE_EXPERIENCE_COMPLETE=false`

## Next gate

If J1/J2/J3/J5/J7 are not `REAL_USER_JOURNEY_DIGITAL_PASS`:

`NEXT_CX_GATE=CX2E_LINUX_GRAPHICAL_SESSION_JOURNEY_PROOF`
