# STREAM P1 — Device Lab current-pin (Prompt 17G.5D WAIKE GUI/Hub re-earn)

## Snapshot
- Device OS PR: #134 @ `a03dc5d02d55b5f2c4855ff784b9239f78888e6d` (continue only; Cursor merges nothing)
- Portal PR: #14 (this PR; #15 consumes)
- WAIKE accepted-main: `232fc8dc3aa10d3dd644ef48d1d8c63da50d4d3c` (PR #12 merge-commit; glibc236 artifact `3df1e42e…`)
- Pin manifest: `47fe0c86856c4eec795a7b28c582532d612175475a83f91ad315720326a5ce15`
- WAIKE product PR #12: **MERGED** (owner merge-commit)

## Gate tokens
- LIVE/DSXL/RING/FOUR_GAME = **true** (retained)
- RUNTIME_TARGET_PREFLIGHT_PASS = **true**
- QEMU_SCOPED_GUESTFWD_PASS = **true**
- QEMU_GUEST_ISOLATION_RETAINED = **true**
- WAIKE_GUEST_HUB_REACHABILITY_PASS = **true** (guestfwd HTTP/1.0 healthz 200)
- WAIKE_REAL_HUB_CLIENT_BIND_PASS = **false** (full client bind not earned)
- WAIKE_ATSPI_WINDOW_PASS = **false**
- WAIKE_REAL_RUNTIME_DEVICE_LAB_PASS = **false** (honest FAIL)

## 17G.5D result
- Hub bind `127.0.0.1:8787`; guest URL `http://10.0.2.100:8787`
- guestfwd `guestfwd=tcp:10.0.2.100:8787-tcp:127.0.0.1:8787`; restrict=on; mockHub off
- Guest Hub HTTP health PASS under isolation
- Weston compositor seen; owner-bundle 9p fetch failed when virtio-serial channel dropped
- Blocker: `guest_fetch_owner_bundle_failed`
- Evidence: `gunnchos-device-os#134 artifacts/device_lab_current_pin/waike/`

## Next gate
`NEXT_GATE=DEVICE_OS_134_WAIKE_9P_BUNDLE_FETCH_OVER_VIRTIO_SERIAL`

Do not start gunnchAI.

## Firewall
- Do not start gunnchAI / lifecycle / ECO010 / independent verify / master closure
- CX expansion firewall: no Device OS #135 / Portal #16 / WAIKE #13 / gunnchAI #48 work in this stream
- #134 / #14 remain OPEN / DRAFT / unmerged
