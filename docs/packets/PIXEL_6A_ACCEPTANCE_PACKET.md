# Pixel 6a acceptance packet

**Status:** `HUMAN_QA_PENDING` / `PIXEL_6A_READY = BLOCKED`

## Why blocked (re-check 2026-08-18 ~21:15Z)

USB-C was connected. `adb devices -l` showed:

```text
27211JEGR06194         unauthorized usb:17825792X transport_id:1
```

An unauthorized session is not a device. Install, launch, logcat, orientation, and uninstall/reinstall were **not** executed. Evidence: each Android-capable repo `artifacts/pixel6a/ACCEPTANCE.json`.

## Prerequisite

Unlock the Pixel 6a, accept the USB debugging prompt, then:

```bash
adb devices -l
# expected: 27211JEGR06194    device usb:... product:bluejay model:Pixel_6a
```

## Commands (after authorized)

Per Android-capable repo, follow that repo’s `docs/PIXEL_6A_ACCEPTANCE.md` (build APK, hash, install, package ID, label, icon, launch, logcat, first-launch, smoke, back, pause/resume, orientation, touch, reconnect, uninstall/reinstall).

`PIXEL_6A_READY = PASS` only for apps that actually installed and launched. Fun/usability stays `HUMAN_QA_PENDING`.
