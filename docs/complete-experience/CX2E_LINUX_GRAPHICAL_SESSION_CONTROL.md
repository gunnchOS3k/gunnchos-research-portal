# CX2E Control — Linux Graphical Session + Real User Journey Proof

Stacked on Portal CX2D (#19 `docs/cx2d-linux-real-user-journey-control`).  
Does **not** touch Portal #14/#15.

## Device OS DRAFT stack

| PR | Branch | Base |
|----|--------|------|
| #135–#140 | CX0–CX2D | stacked |
| CX2E (this wave) | `eng/cx2e-linux-graphical-session-journey-proof` | CX2D |

## Production shell authority

**Path B** — `apps/gunnch_shell` + `ShellRuntimeTarget v1`.  
Vite dev server is not production. Chromium app-mode allowed only as declared provider for local built assets.

## Truth gate

Guest facts only:

`guest_booted && guest_is_linux && compositor_running && wayland_socket_alive && shell_window_rendered`

No macOS provider fallback. No fixtures/static screenshots as PASS.

## Evidence

Device OS: `artifacts/complete_experience/cx2e/` only.

## Pending

- HUMAN_A11Y / physical printer / AV / camera-mic
- Any journey not earning `REAL_USER_JOURNEY_DIGITAL_PASS` records exact missing condition

`FULL_COMPLETE_EXPERIENCE_COMPLETE=false`

## Next gate

If J1/J2/J3/J5/J7 earn digital pass → `NEXT_CX_GATE=CX3`  
Else → `NEXT_CX_GATE=CX2F_<BLOCKER>` (do not start next wave from this PR alone)
