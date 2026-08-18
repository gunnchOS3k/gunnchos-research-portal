# Pixel 6a acceptance packet

**Status:** `HUMAN_QA_PENDING` / `PIXEL_6A_READY = BLOCKED`

## Why blocked

`adb devices` on 2026-08-18 showed `27211JEGR06194	unauthorized`. Cursor cannot complete install, launch, or touch-flow evidence without an authorized session.

## Prerequisite

Edmund unlocks the Pixel 6a, accepts the USB debugging prompt, and confirms:

```bash
adb devices
# expected: <serial>    device
```

## Commands (after authorized)

Per Android-capable repo (BeatLink PWA / Archive Capacitor / Pedestrian Godot / Anime Godot export / Edge I/O Android target):

```bash
# example — replace with that repo's docs/PIXEL_6A_ACCEPTANCE.md
adb install -r <debug-apk>
adb logcat -c
# launch, smoke, pause/resume, back button
adb logcat -d > artifacts/pixel6a/logcat.txt
adb shell getprop ro.product.model
adb shell dumpsys package <package> | head
```

## Expected evidence

Store under each repo `artifacts/pixel6a/`:

- device model/build  
- package name  
- install success  
- smoke flow notes  
- logcat excerpt  

## Status transition

Authorized device + passing smoke → that repo’s Android line may move from `HUMAN_QA_PENDING` toward `DEVICE_MEASURED` **for install/launch only** — not RF, not playtest quality, not dissertation proof.
