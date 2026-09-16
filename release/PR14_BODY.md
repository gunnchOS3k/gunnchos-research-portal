# STREAM P1 — Device Lab current-pin (Prompt 17G.5C1 network proof)

## Snapshot
- Device OS PR: #134 @ `5ce7cb3e857b5b90cc19c939fb2d21831641a47b` (continue only; Cursor merges nothing)
- Portal PR: #14 (this PR; #15 consumes)
- WAIKE accepted-main: `232fc8dc3aa10d3dd644ef48d1d8c63da50d4d3c` (PR #12 merge-commit; glibc236 artifact `3df1e42e…`)
- Pin manifest: `47fe0c86856c4eec795a7b28c582532d612175475a83f91ad315720326a5ce15`
- WAIKE product PR #12: **MERGED** (owner merge-commit)

## Gate tokens
- LIVE/DSXL/RING/FOUR_GAME = **true** (retained)
- WAIKE_REAL_RUNTIME_DEVICE_LAB_PASS = **false**
- RUNTIME_TARGET_PREFLIGHT_PASS = **true**
- glibc_gap_closed = **true**
- QEMU_SCOPED_GUESTFWD_PASS = **true**
- QEMU_GUEST_ISOLATION_RETAINED = **true**
- WAIKE_GUEST_HUB_REACHABILITY_PASS = **true**
- WAIKE_REAL_HUB_CLIENT_BIND_PASS = **true** (minimal bind; no full GUI journey)

## Network result (17G.5C1)
- restrict=on retained; scoped guestfwd `10.0.2.100 → 127.0.0.1`
- Guest Hub URL: `http://10.0.2.100:8787`
- Evidence: `gunnchos-device-os#134 artifacts/device_lab_current_pin/waike/network_only/`

## Next gate
`NEXT_GATE=17G5D_FULL_WAIKE_GUI_JOURNEY_REEARN` (not started)

## Firewall
- Do not start gunnchAI / lifecycle / ECO010 / independent verify / master closure
- Do not start full 17G.5D in this portal refresh
- CX expansion firewall: no Device OS #135 / Portal #16 / WAIKE #13 / gunnchAI #48 work in this stream
