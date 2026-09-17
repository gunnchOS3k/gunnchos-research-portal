# CX2H Control — Journey Digital Pass Closure (CX2H.1 / CX2H.1B)

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

## CX2H.1B scope (this update)

Close Flatpak **launch / window / version-visible** evidence so J3 can honestly earn `REAL_USER_JOURNEY_DIGITAL_PASS`.

- Reclassified premature CX2H.1 J3 PASS → `REAL_PROVIDER_GUI_PARTIAL` (PID/`$!` and App Center FB churn were not window proof).
- Provider launch must return structured `{ok, instance_id, pid, application, version, branch, alive_after_5s, launch_log, error}` — `$!` alone is insufficient; requires `flatpak ps` + `CX2H_WINDOW_MAPPED` and fails on Gtk Bail out.
- Test app: undecorated GTK3 DrawingArea (host GI); v1 green `#0B3D2E` vs v2 orange `#C45C26` + yellow band; pixbuf loaders cache rewritten to `/run/host`.
- Window proof requires two channels (FB diff vs after-install + AT-SPI/color); thresholds not lowered (earned ~64% / ~49%).

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

CX2H.1B artifacts:
- `CX2H1B_J3_EVIDENCE_REVIEW.json`
- `CX2H1B_FLATPAK_LAUNCH_ROOT_CAUSE.json`
- `CX2H1B_WINDOW_PROOF_V1.json` / `CX2H1B_WINDOW_PROOF_V2.json`
- `CX2H1B_PROVIDER_LAUNCH_RESULT.json`

## Concurrency

`/tmp/gunnchos-cx-qemu.lock` — one CX guest; never kill foreign QEMU.

`FULL_COMPLETE_EXPERIENCE_COMPLETE=false`

## Results (CX2H.1B closed — fail-closed honest PASS)

| Token | Value |
|-------|-------|
| `CX2H_SHELL_PREREQ_PASS` | **true** |
| `CX2H_XDG_PORTAL_SESSION_PASS` | **true** |
| `CX2H_REAL_APP_CENTER_PROVIDER_PASS` | **true** |
| `CX2H_REAL_APP_INSTALL_GUI_PASS` | **true** |
| `CX2H_REAL_APP_LAUNCH_GUI_PASS` | **true** (flatpak ps + WINDOW_MAPPED + dual-channel FB) |
| `CX2H_REAL_APP_UPDATE_GUI_PASS` | **true** (provider 1.0.0→2.0.0 + FB/color distinction) |
| `CX2H_REAL_APP_ROLLBACK_GUI_PASS` | **true** |
| `CX2H_REAL_APP_UNINSTALL_GUI_PASS` | **true** |
| `CX2H_J3_PERSISTENCE_PASS` | **true** |
| `J3_CLASS` | **REAL_USER_JOURNEY_DIGITAL_PASS** |
| `J1_CLASS` / `J2_CLASS` / `J5_CLASS` / `J7_CLASS` | BLOCKED |
| `J6_CLASS` | HUMAN_VALIDATION_PENDING |
| `FULL_COMPLETE_EXPERIENCE_COMPLETE` | false |

### Portal root cause (repaired; preserve)

Wedged/root-owned session bus at `/run/cx2g-wayland/bus` left `org.freedesktop.portal.Desktop` absent. Repair: gunnchos-owned session bus at `/run/user/1000/bus`, gtk.portal `UseIn` widened, `xdg-desktop-portal` + gtk backend on the same bus as Chromium.

### J3 Flatpak launch (CX2H.1B closed)

Root cause class `HOST_GTK_WAYLAND_GEOMETRY_OVERFLOW` / pixbuf icon abort closed by: undecorated DrawingArea, host pixbuf loader cache via `/run/host`, provider requires `flatpak ps` + `CX2H_WINDOW_MAPPED` (not shell `$!`). Window proofs: v1 ~64% FB / green, v2 ~49% FB / orange.

## Next gate

`NEXT_CX_GATE=CX2H2_DOCUMENT_PRINT_RECOVERY_J1_J7`

Do **not** start CX2H.2 from this control doc alone — await explicit owner prompt. Future CX2H.2/.3/.4 continue this same branch/PR.
