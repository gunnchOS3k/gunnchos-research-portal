# Install / Uninstall — gunnchOS Capsule v1.0.0-rc.1

## Safety

- Install with `adb install -r` **only**
- Never factory reset, unlock the bootloader, or wipe `/data`
- Never run `adb reboot bootloader` as part of Capsule installation
- Do not commit or publish the device serial

## RC1 artifact

`gunnchOS-Capsule-Pixel6a-post-feedback-debug.apk`

Accepted Device OS main:

`2218ead0efa0e4b8a622717a0a9bf623ee95ddb0`

SHA-256:

`a0c55be39c407ffd24868a715c9c86bb2da07efbff16dc2ddb90aecebef45826`

## Install

From the directory containing the release asset:

```bash
adb install -r gunnchOS-Capsule-Pixel6a-post-feedback-debug.apk
```

## Uninstall (optional)

```bash
adb uninstall com.gunnchos.capsule
# debug builds, when applicable:
adb uninstall com.gunnchos.capsule.debug
```

## USB debugging approval

If `adb devices -l` reports the device as unauthorized:

1. Unlock the Pixel and keep the screen on.
2. Approve the Android USB debugging prompt.
3. Re-check that ADB reports an authorized device.
4. Continue without recording the raw serial in release evidence.