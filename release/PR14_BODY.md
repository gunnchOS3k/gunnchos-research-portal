# STREAM P1: RC0 digital freeze — Device Lab (#134)

## 17G.5F status (WAIKE #15 accepted-main; white-WebView product defect)

- WAIKE LP accepted-main: `5037df0c2dd1a966fcb07422a27366b14fe56b2f` (merge commit of Platform PR #15)
- Device OS tip: `74478acffbd2a85c8d19d8d9bc9acf87f024e064`
- Artifact: `6442824be7f27355b7189d307cc45da69be31c7ddd30a96134a80c820fb2333a`
- Manifest: `456cd0277f777076bfaa001a7e0b97a5c35313627f142d57b989355847f81e42`
- `WAIKE_EFFECTIVE_WEBVIEW_CSP_PASS=true` (DirectiveMap + HTML meta + authorized Hub origin in connect-src)
- `WAIKE_GUEST_HUB_REACHABILITY_PASS=true` (restrict=on + scoped guestfwd)
- `WAIKE_REAL_HUB_CLIENT_BIND_PASS=false` — white WebView loads `localhost:1420` (Tauri `devUrl`) instead of embedded `frontendDist`; no login form; Hub healthz-only; no `hub_login_fetch_*`
- `WAIKE_REAL_RUNTIME_DEVICE_LAB_PASS=false` — honest FAIL
- LIVE/DSXL/RING/FOUR_GAME retained
- Draft WAIKE product PR #16 (custom-protocol embed for Device Lab aarch64/glibc236 builds): https://github.com/gunnchOS3k/gunnchos-waike-learning-platform/pull/16
- **Do not merge** Device OS #134 or Portal #14 yet; keep WAIKE=false until owner merges #16 + new glibc236 artifact + bind re-earn
- NEXT_GATE: `WAIKE_PR16_CUSTOM_PROTOCOL_EMBED_OWNER_MERGE_REFREEZE`
- Do **not** start gunnchAI; do **not** advance to `GUNNCHAI_DEVICE_LAB_INTEGRATION`
