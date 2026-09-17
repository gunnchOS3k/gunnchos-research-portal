# Device OS #134 Hub bind PASS + CSP/GUI Hub next gate

- Device OS tip: `aff29a9bb708b9103adb2d6465aa78cb0f05f66a` on `cursor/device-lab-current-pin-revalidation` (PR #134 OPEN/DRAFT)
- Additive fix: QEMU `guestfwd=…-cmd:hub_guestfwd_cmd_relay_8787.sh` + preserve `cmd` in `parse_guestfwd_env` + CORS proxy ACCEPT/HTTP matrix
- `WAIKE_REAL_HUB_CLIENT_BIND_PASS=true` — guest OPTIONS+POST hit Hub via cmd relay (unsandboxed HVF)
- `WAIKE_REAL_RUNTIME_DEVICE_LAB_PASS=false` — journey A+B learner depth still incomplete after bind
- LIVE/DSXL/RING/FOUR_GAME retention unchanged (true)
- NEXT_GATE=`DEVICE_OS_134_WAIKE_EFFECTIVE_CSP_GUI_HUB_REEARN`
- WAIKE #17 DRAFT remains open for durable Hub CORS (`b2c2f23`)
- Do not merge #134/#14/#17; CX untouched; gunnchAI not started
