# STREAM P1: RC0 digital freeze — Device Lab (#134)

## 17G.5F status (WAIKE #15 accepted-main)

- WAIKE LP accepted-main: `5037df0c2dd1a966fcb07422a27366b14fe56b2f` (merge commit of Platform PR #15)
- Device OS tip: `df325461842f80cf00f89ee77e60a522b38bb443`
- `WAIKE_EFFECTIVE_WEBVIEW_CSP_PASS=true` (DirectiveMap + HTML meta + authorized Hub origin in connect-src)
- `WAIKE_GUEST_HUB_REACHABILITY_PASS=true` (restrict=on + scoped guestfwd)
- `WAIKE_REAL_HUB_CLIENT_BIND_PASS=false` (Hub healthz-only; no client HTTP beyond healthz)
- `WAIKE_REAL_RUNTIME_DEVICE_LAB_PASS=false` — honest FAIL
- LIVE/DSXL/RING/FOUR_GAME retained via materiality rebind
- **Do not merge** Device OS #134 or Portal #14 yet
- NEXT_GATE: `DEVICE_OS_134_WAIKE_CLIENT_HTTP_BIND_REEARN`
- Do **not** start gunnchAI; do **not** advance to `GUNNCHAI_DEVICE_LAB_INTEGRATION`
