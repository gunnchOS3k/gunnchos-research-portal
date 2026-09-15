# STREAM P1 — Device Lab current-pin (Prompt 17G.4)

## Snapshot
- Device OS PR: #134 (continue only; Cursor merges nothing)
- Portal PR: #14 (this PR; #15 consumes)
- WAIKE accepted-main: `b1c3ab5d4faa4d2613569e474013ccf0976d346e` (#11 glibc236)
- Pin manifest: `a5a252ad7790c7f45eb1838a8dc26a2b407c1d75d830961d6dd62813bfadcb3b`
- Drift: `WAIKE_GLIBC236_CI_FIX_ACCEPTED_MAIN` (workflow/docs/build support only)

## Gate tokens
- LIVE/DSXL/RING/FOUR_GAME = **true** (compact rebind)
- WAIKE_REAL_RUNTIME_DEVICE_LAB_PASS = **false**
- RUNTIME_TARGET_PREFLIGHT_PASS = **true**
- glibc_gap_closed = **true** (measured max 2.34 ≤ guest 2.36)
- authentic IPC ack earned; learner course/assessment/offline/recovery depth **not** earned (headless)

## Blocker
`native_aarch64_glibc236_headless_launch_ack_only_learner_journey_depth_not_earned;need_gui_or_product_journey_surface_for_course_assessment_offline_recovery`

## Firewall
- Do not start gunnchAI / lifecycle / ECO010 / independent verify / master closure
- Next gate only when WAIKE=true: `GUNNCHAI_DEVICE_LAB_INTEGRATION` (not started)
