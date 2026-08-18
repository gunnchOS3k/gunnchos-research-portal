# Pixel 6a acceptance packet

**Status:** `PIXEL_6A_READY = PASS` for digital install+launch smoke. Fun/usability remains `HUMAN_QA_PENDING`.

## Authorized session (2026-08-18)

USB-C Pixel 6a serial `27211JEGR06194` (`product:bluejay`, Android 17) listed as **device** (authorized). Install/launch smoke executed:

| App | Package | Install | Launch | PIXEL_6A_READY |
|---|---|---|---|---|
| Edge I/O | `org.gunnchos.edgeio.debug` | PASS (this-session APK) | PASS | PASS |
| BeatLink | `com.gunnchos.beatlinkparty` | PASS (uninstall + reinstall after signature mismatch) | PASS | PASS |
| Archive of Life | `com.gunnchos.archiveoflife` | PREEXISTING_ON_DEVICE | PASS | PASS |
| Anime Aggressors | `com.gunnchos.animeaggressors` | PASS (this-session APK) | PASS | PASS |
| Pedestrian Pursuit | `com.gunnchos.pedestrianpursuit` | PREEXISTING_ON_DEVICE | PASS | PASS |

Per-app evidence: each Android-capable repo `artifacts/pixel6a/ACCEPTANCE.json`.

This is **not** RF proof, not playtest quality, and not a signed store release. Archive/Pedestrian this-session APK rebuild remains a separate export (preexisting packages launched).

## Prerequisite (if the prompt returns)

Unlock the Pixel 6a, accept USB debugging, then:

```bash
adb devices -l
# expected: 27211JEGR06194    device usb:... product:bluejay model:Pixel_6a
```
