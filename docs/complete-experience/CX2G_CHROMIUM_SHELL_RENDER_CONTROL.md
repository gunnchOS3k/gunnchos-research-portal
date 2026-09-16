# CX2G Control — Chromium Shell Launch Repair + Render/Capture Proof

Stacked on Portal CX2F (`docs/cx2f-drm-shell-render-capture-control`).  
Does **not** touch Portal #14/#15.

## Device OS DRAFT stack

| PR | Branch | Base |
|----|--------|------|
| CX2F #142 | `eng/cx2f-drm-shell-render-capture-journey-reearn` | CX2E |
| CX2G (this wave) | `eng/cx2g-chromium-shell-render-repair` | CX2F #142 |

## Root cause (CX2F Chromium fail)

`launch_chromium_shell` embedded plaintext `chromium` in the SSH remote argv and ran `pkill -f chromium`, self-killing the remote shell before systemd restart completed.

## CX2G remediation

- Forbidden: `pkill -f chromium`
- `stop_owned_shell_runtime()` — `systemctl stop` owned unit → wait cgroup empty → terminate only owned PIDs
- Authoritative unit: `cx2g-gunnch-shell.service` (User=gunnchos, coherent Wayland/DBus env, loopback URL, isolated profile, remote-debug loopback, Restart=no during diagnosis)

## Separated truth lanes

| Lane | Token |
|------|-------|
| Non-cloud kernel | `CX2G_NON_CLOUD_KERNEL_BOOT_PASS` |
| DRM | `CX2G_DRM_CARD_PASS` |
| Weston DRM | `CX2G_WESTON_DRM_PASS` (headless ≠ success) |
| Chromium runtime | `CX2G_CHROMIUM_RUNTIME_PASS` |
| Wayland surface | `CX2G_WAYLAND_SURFACE_PASS` |
| Shell render | `CX2G_GUNNCH_SHELL_RENDER_PASS` |
| Framebuffer capture | `CX2G_QEMU_FRAMEBUFFER_CAPTURE_PASS` |
| Input mutation | `CX2G_REAL_INPUT_TO_SHELL_MUTATION_PASS` |
| Portals | `CX2G_XDG_PORTAL_SESSION_PASS` |
| Digital a11y | `CX2G_DIGITAL_RENDERED_A11Y_PASS` (`HUMAN_A11Y_PENDING=true` always) |
| J1–J7 | Re-earn only after shell gate green + real UI/provider/read-back |

## Evidence

Device OS: `artifacts/complete_experience/cx2g/` only.  
Lab: `os_build/cx2g_linux_lab/`.  
CX2F overlay cloned as backing when present; CX2F evidence immutable.

## Concurrency

`/tmp/gunnchos-cx-qemu.lock` — one CX guest; never kill foreign QEMU.

`FULL_COMPLETE_EXPERIENCE_COMPLETE=false`

## Next gate

Only if shell gate + J1/J2/J3/J5/J7 `REAL_USER_JOURNEY_DIGITAL_PASS` → `NEXT_CX_GATE=CX3_EDUCATION_CREDENTIALS_PORTFOLIO`  

Else → `NEXT_CX_GATE=CX2H_<BLOCKER>` (do not start next wave from this PR alone)
