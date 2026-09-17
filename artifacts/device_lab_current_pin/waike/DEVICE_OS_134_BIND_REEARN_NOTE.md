# Device OS #134 WAIKE client HTTP bind re-earn (additive)

- Device OS tip: `a42f9aa` on `cursor/device-lab-current-pin-revalidation` (PR #134 OPEN/DRAFT)
- Leading root cause: Hub missing CORS for Tauri `http://ipc.localhost` Origin (OPTIONS preflight) while WebKit showed ESTAB TCP and `hub_login_fetch_start`
- Additive Device OS fix: guestfwd CORS proxy + WebKit-mimic probe + retry fix
- WAIKE durable CORS branch pushed: `cursor/waike-hub-device-lab-cors` @ `b2c2f23` (DRAFT PR create blocked by gh auth; open via compare URL)
- `WAIKE_REAL_HUB_CLIENT_BIND_PASS=false` — guest QEMU re-earn blocked in agent sandbox (HVF sysctl); do not claim WAIKE=true
- LIVE/DSXL/RING/FOUR_GAME retention unchanged
- NEXT_GATE=`DEVICE_OS_134_WAIKE_CLIENT_HTTP_BIND_REEARN`
- Do not merge #134/#14; CX untouched; gunnchAI not started
