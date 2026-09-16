# STREAM P1 — Device Lab current-pin (Prompt 17G.5)

## Snapshot
- Device OS PR: #134 @ `471855907cb33a67d4a4cf0260816db0029943d7` (continue only; Cursor merges nothing)
- Portal PR: #14 (this PR; #15 consumes)
- WAIKE accepted-main: `b1c3ab5d4faa4d2613569e474013ccf0976d346e` (glibc236 artifact unchanged)
- Pin manifest: `a5a252ad7790c7f45eb1838a8dc26a2b407c1d75d830961d6dd62813bfadcb3b`
- DRAFT WAIKE product PR: #12 @ `9c4f4c25c5a85d6e2af2694cda4dfc882d09be15` (unmerged; owner merge + re-freeze required)

## Gate tokens
- LIVE/DSXL/RING/FOUR_GAME = **true** (retained)
- WAIKE_REAL_RUNTIME_DEVICE_LAB_PASS = **false**
- RUNTIME_TARGET_PREFLIGHT_PASS = **true**
- glibc_gap_closed = **true**
- GUI window alive on Interactive Guest weston = **true**
- Real Hub sidecar = **true**; client Hub bind = **false**

## Blocker
`accepted_main_no_runtime_hub_url_override;real_hub_sidecar_ok_but_client_cannot_bind;need_owner_merge_waike_pr12_then_refreeze_glibc236`

## Firewall
- Do not start gunnchAI / lifecycle / ECO010 / independent verify / master closure
- Next gate only when WAIKE=true with no unresolved product PR: `GUNNCHAI_DEVICE_LAB_INTEGRATION` (not started)
