# Compatibility / Provider Matrix (candidates)

**Do not standardize** until compatibility demonstrated on target profiles.

See also `PROVIDER_QUALIFICATION_MATRIX.json`.

| Lane | Examples | Arch | Notes |
|------|----------|------|-------|
| GUNNCH_NATIVE | Device OS first-party | ARM64/x86_64 | Primary |
| LINUX_NATIVE | distro packages | both | Profile gated |
| FLATPAK | LibreOffice, browsers, creatives | both | Sandbox preferred |
| WEB_PWA | email/calendar fallback | both | Cont IX uses PWA fallback today |
| OCI_DEV | Podman workstation | ds_xl | Not productized |
| STEAM_PROTON_USER | games | EXTERNAL | User-managed |
| ANDROID_EXPERIMENTAL | — | unevaluated | Disabled |
| REMOTE_EXEC | RDP/VNC/cloud | ABSENT product | Required for high-end tier |

Device Lab guest uses qemu-user for arch escape — do not disturb #134 paths when adding Bridge work.
