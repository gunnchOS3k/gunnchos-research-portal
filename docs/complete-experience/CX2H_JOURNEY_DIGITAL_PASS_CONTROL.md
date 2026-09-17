# CX2H Control — Journey Digital Pass Closure (CX2H.1)

Stacked on Portal CX2G (`docs/cx2g-chromium-shell-render-control`).  
Does **not** touch Portal #14/#15.

## Device OS DRAFT stack

| PR | Branch | Base |
|----|--------|------|
| CX2G #143 | `eng/cx2g-chromium-shell-render-repair` | CX2F |
| CX2H (this wave) | `eng/cx2h-journey-digital-pass-closure` | CX2G #143 |

## CX2H.1 scope

1. Real XDG portal session on the graphical DBus (`CX2H_XDG_PORTAL_SESSION_PASS`)
2. J3 App Center real-user Flatpak lifecycle (`J3_CLASS=REAL_USER_JOURNEY_DIGITAL_PASS`)
3. Stop — do not attempt J1/J2/J5/J7; do not start CX3

## Separated truth lanes

| Lane | Token |
|------|-------|
| Shell prereq (re-prove CX2G) | `CX2H_SHELL_PREREQ_PASS` |
| Portals | `CX2H_XDG_PORTAL_SESSION_PASS` |
| App Center provider | `CX2H_REAL_APP_CENTER_PROVIDER_PASS` |
| Install / launch / update / rollback / uninstall | `CX2H_REAL_APP_*_GUI_PASS` |
| Persistence read-back | `CX2H_J3_PERSISTENCE_PASS` |
| J3 | `J3_CLASS` |
| J1/J2/J5/J7 | `BLOCKED` |
| J6 | `HUMAN_VALIDATION_PENDING` |

## Evidence

Device OS: `artifacts/complete_experience/cx2h/` only.  
Lab: `os_build/cx2h_linux_lab/` (CX2G overlay clone).

## Concurrency

`/tmp/gunnchos-cx-qemu.lock` — one CX guest; never kill foreign QEMU.

`FULL_COMPLETE_EXPERIENCE_COMPLETE=false`

## Results (CX2H.1 earned 2026-09-17T00:50:33Z)

| Token | Value |
|-------|-------|
| `CX2H_SHELL_PREREQ_PASS` | true |
| `CX2H_CHROMIUM_RUNTIME_PASS` | true |
| `CX2H_WAYLAND_SURFACE_PASS` | true |
| `CX2H_GUNNCH_SHELL_RENDER_PASS` | true |
| `CX2H_QEMU_FRAMEBUFFER_CAPTURE_PASS` | true |
| `CX2H_REAL_INPUT_TO_SHELL_MUTATION_PASS` | true |
| `CX2H_REAL_APP_CENTER_WINDOW` | true |
| `CX2H_XDG_PORTAL_SESSION_PASS` | **true** |
| `CX2H_REAL_APP_CENTER_PROVIDER_PASS` | true |
| `CX2H_REAL_APP_INSTALL_GUI_PASS` | true |
| `CX2H_REAL_APP_LAUNCH_GUI_PASS` | true |
| `CX2H_REAL_APP_UPDATE_GUI_PASS` | true |
| `CX2H_REAL_APP_ROLLBACK_GUI_PASS` | true |
| `CX2H_REAL_APP_UNINSTALL_GUI_PASS` | true |
| `CX2H_J3_PERSISTENCE_PASS` | true |
| `J3_CLASS` | **REAL_USER_JOURNEY_DIGITAL_PASS** |
| `J1_CLASS` / `J2_CLASS` / `J5_CLASS` / `J7_CLASS` | BLOCKED |
| `J6_CLASS` | HUMAN_VALIDATION_PENDING |
| `FULL_COMPLETE_EXPERIENCE_COMPLETE` | false |

### Portal root cause (repaired)

Wedged/root-owned session bus at `/run/cx2g-wayland/bus` left `org.freedesktop.portal.Desktop` absent. Repair: gunnchos-owned session bus at `/run/user/1000/bus`, gtk.portal `UseIn` widened, `xdg-desktop-portal` + gtk backend on the same bus as Chromium. Exercised Settings / Notification / OpenURI / FileChooser (Screenshot → QEMU FB fallback).

### J3 Flatpak lifecycle

Local repo `cx2h-local` with installable `org.gunnchos.CX2HTestApp` v1.0.0 / v2.0.0 (visually distinct HTML). App Center GUI drove install → launch → update → rollback → uninstall → persistence reinstall + shell restart; CLI verified provider truth only.

## Next gate

`NEXT_CX_GATE=CX2H2_DOCUMENT_PRINT_RECOVERY_J1_J7`

Do **not** start CX2H.2 from this control doc alone — await explicit owner prompt. Future CX2H.2/.3/.4 continue this same branch/PR.
