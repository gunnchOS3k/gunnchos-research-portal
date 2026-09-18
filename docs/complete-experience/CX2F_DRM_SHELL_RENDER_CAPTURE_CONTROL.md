# CX2F Control — DRM Weston + Shell Render/Capture + Journey Re-Earn

Stacked on Portal CX2E (#20 `docs/cx2e-linux-graphical-session-control`).  
Does **not** touch Portal #14/#15.

## Device OS DRAFT stack

| PR | Branch | Base |
|----|--------|------|
| #135–#141 | CX0–CX2E | stacked |
| CX2F (this wave) | `eng/cx2f-drm-shell-render-capture-journey-reearn` | CX2E #141 |

## Separated truth lanes

| Lane | Meaning |
|------|---------|
| Guest foundation | Debian aarch64 QEMU guest boot (from CX2E) |
| Non-cloud kernel | Newest `*-arm64` not `*-cloud-arm64`; GRUB + reboot + `uname` |
| DRM | `/dev/dri` + virtio_gpu bind |
| Weston DRM | `drm-backend.so` only; headless is not a success path |
| Shell asset delivery | Immutable `gunnch_shell` via loopback static HTTP |
| Shell render | Chromium Wayland + framebuffer diff + second channel |
| Framebuffer capture | QEMU HMP screendump PPM primary |
| Input-to-shell mutation | Visible + authoritative shell state change |
| Portal interfaces | xdg-desktop-portal matrix (Screenshot optional) |
| GUI providers | Browser / App Center / productivity / mail / calendar / IPP / offline |
| J1–J7 | Re-earn only with complete real UI/provider/read-back |
| Human/physical pending | A11y, printer, AV, camera/mic |

## Production shell authority

**Path B** — `apps/gunnch_shell`. Vite absolute `/assets/` requires loopback HTTP (not `file://`).

## Evidence

Device OS: `artifacts/complete_experience/cx2f/` only.  
CX2E overlay cloned as backing file; CX2E evidence immutable.

## Concurrency

`/tmp/gunnchos-cx-qemu.lock` — never kill foreign QEMU.

`FULL_COMPLETE_EXPERIENCE_COMPLETE=false`

## Next gate

Only if non-cloud kernel + DRM + Weston DRM + shell render + framebuffer + input-to-shell + J1/J2/J3/J5/J7 DIGITAL_PASS → `NEXT_CX_GATE=CX3_EDUCATION_CREDENTIALS_PORTFOLIO`  

Else → `NEXT_CX_GATE=CX2G_<BLOCKER>` (do not start next wave from this PR alone)
