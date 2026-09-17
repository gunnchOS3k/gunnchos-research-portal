# STREAM P1: RC0 digital freeze — Device Lab (#134)

## 17G.5F status (WAIKE #15 accepted-main; white-WebView product defect)

- WAIKE LP accepted-main: `5037df0c2dd1a966fcb07422a27366b14fe56b2f` (merge commit of Platform PR #15)
- Device OS tip: `e26e4caec753d09ad8bfd79fadb9bbfb865659ae`
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


## 17G.5J status (Device OS #134 accepted-main bind + Portal final sync)

- Device OS #134 **MERGED**: `c3b7a5183aba0c0567cdc3483bbce2c43dd12ebe` (PR head `819f5a839cad9442d7850a203a9f59db37b08c70`)
- WAIKE LP accepted-main: `7ccb64459df088d41655af51c959a7bbbac849a3`
- Artifact: `071cce1383561e14cf957cdcd5e932e04884a2d2a5bba35cdbbce08e137e58f8`
- Manifest: `8da7a6f9688e88b8fa31ad61c6f0f4229a8cbf83cbc0ad0711a81557643df36b`
- `DEVICE_OS_134_ACCEPTED_MAIN_MERGE_SHA=c3b7a5183aba0c0567cdc3483bbce2c43dd12ebe` (replaced PENDING_OWNER_MERGE)
- Post-merge main validation PASS; compact release rebind PASS; LIVE/DSXL/RING/FOUR_GAME/WAIKE true
- Portal #14 remains OPEN/DRAFT — owner merge next
- `GUNNCHAI_GATE_BLOCKED_ON_PORTAL_14_OWNER_MERGE=true`
- Intended next gate after Portal merge: `GUNNCHAI_DEVICE_LAB_INTEGRATION`
- Do **not** start gunnchAI; Cursor does **not** merge
- NEXT_OWNER_ACTION: `MERGE_PORTAL_14_WITH_MERGE_COMMIT`
