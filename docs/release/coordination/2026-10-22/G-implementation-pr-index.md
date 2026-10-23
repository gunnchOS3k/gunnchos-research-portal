# G. Exact implementation PR index

Queried with `gh pr view` / `gh pr list` on 2026-10-22 after #130 existed (`createdAt` 2026-10-22T22:21:57Z). No newer open Anime pull request than #130 was returned. No product pull request was merged.

Live art-branch tip, local and `origin/release/anime-v1-dialogue-and-elemental-performance`: `7c25c2996f8adcee97ec2187a14bfc578d8681bf` (draft #123). GitHub `base.sha` on older Cursor drafts lags that tip. The parent column is the parent of the branch's unique commit and is the merge-base with `7c25c299` for every row below.

| Repo | PR | Branch | Head SHA | Parent / merge-base vs `7c25c299` | GitHub `base.sha` | Draft | Merge state |
|---|---|---|---|---|---|---|---|
| anime-aggressors | #124 | `eng/cursor-v1-audio-shutdown` | `b74cf3c6956bce4bda9c44d913707c3e3547c57e` | `9516770df92530564cb9beb04d144db00f978b24` (10 commits behind) | `3ab7667c` | yes | MERGEABLE, UNSTABLE |
| anime-aggressors | #125 | `eng/cursor-v1-glb-package` | `d12fba82ad8d5301721f852a9075941130fc3c0f` | `3ab7667ca0b22e50bb7acfe0b509ff6b4513daf5` (7 behind) | `bda5b5a5` | yes | MERGEABLE, UNSTABLE |
| anime-aggressors | #126 | `eng/cursor-v1-p1-joypad` | `46cf7ffeecd4950eb16d6cb731b41ab99dd66976` | `bda5b5a57fec99fc2d0821ae8819248c1baf7f74` (2 behind) | `bda5b5a5` | yes | MERGEABLE, UNSTABLE |
| anime-aggressors | #127 | `eng/cursor-v1-partylink-grab` | `9dd5e3e8be8fe82f98c9d5e00c660952d7cbc4de` | `7c25c2996f8adcee97ec2187a14bfc578d8681bf` | `7c25c299` | yes | MERGEABLE, UNSTABLE |
| anime-aggressors | #128 | `eng/cursor-v1-two-client-input` | `efd26b2394febf78bc2ce287c73ed5e774a7812e` | `7c25c2996f8adcee97ec2187a14bfc578d8681bf` | `7c25c299` | yes | MERGEABLE, UNSTABLE |
| anime-aggressors | #129 | `eng/cursor-v1-save-rules` | `b8eecbc5d7c63f26fd78e47210aef4229a43abd0` | `7c25c2996f8adcee97ec2187a14bfc578d8681bf` | `7c25c299` | yes | MERGEABLE, UNSTABLE |
| anime-aggressors | #130 | `eng/cursor-v1-replay-persist` | `cfd6e71de9007f010e24c68bbbc8834d96b738cd` | `7c25c2996f8adcee97ec2187a14bfc578d8681bf` | `7c25c299` | yes | MERGEABLE, UNSTABLE |
| pedestrian-pursuit | #42 | `eng/cursor-v1-pedestrian-achievements` | `bc327c8c3b2c1735441284e86122bd5a5a26d818` | base `origin/main` `957ff95b89d0516855ea61ddba19224a0583c3f8` | `957ff95` | yes | checks mixed; Windows pending |

Context, not Cursor implementation fixes: Anime #123 head `7c25c299` on #122. Portal #55 head `1f4ca20190c99dde5712e9e490ec81e05f1122dd`.

## Files

#124, 72 files from parent `9516770d`. Product behavior is unchanged. Notable paths: `docs/handoff/2026-10-22/CURSOR_AUDIO_SHUTDOWN_FINDING.md`, `game-godot/tests/v1_closure/AudioShutdownProbe.gd`, and baseline logs under `artifacts/v1_closure/cursor_audio_shutdown/baseline/`.

#125, 40 files from parent `3ab7667c`. 36 are `game-godot/assets/characters/form_acting_8c/**/*.glb.import`. Also `.github/workflows/glb-package-probe.yml`, `tools/packaging/probe_glb_package.py`, `docs/handoff/2026-10-22/CURSOR_GLB_PACKAGE_FINDING.md`, and `docs/handoff/2026-10-22/glb_package_probe_key_rows.json`. No path in that diff is also changed by `3ab7667c..7c25c299`.

#126: `game-godot/project.godot`, `tools/input/check_p1_joypad_parity.py`, `docs/handoff/2026-10-22/CURSOR_P1_JOYPAD_FINDING.md`. `bda5b5a5..7c25c299` does not touch `project.godot`.

#127: `packages/partylink/src/lanHost.ts`, `packages/partylink/src/browserController.ts`, `packages/partylink/test/partylinkGrab.test.ts`, `docs/handoff/2026-10-22/CURSOR_PARTYLINK_GRAB_FINDING.md`.

#128: `packages/partylink/src/lanHost.ts`, `packages/partylink/src/postedPartyFrames.ts`, `packages/partylink/src/partyRoom.ts`, `packages/partylink/src/index.ts`, `apps/web/src/screens/PartyLobbyScreen.ts`, `packages/partylink/test/twoClientPostedInput.test.ts`.

#129: `game-godot/scripts/core/GameState.gd`, `game-godot/tests/save_rules_roundtrip.gd`, `tools/save_rules/run_isolated_probe.sh`, plus `docs/handoff/2026-10-22/SAVE_RULES_ROUNDTRIP.md` and the before/after logs.

#130: `game-godot/scripts/net/replay_store.gd`, `game-godot/scripts/net/private_netplay_stack.gd`, `game-godot/tests/replay_persist_roundtrip.gd`, `tools/replay_persist/run_isolated_probe.sh`, plus `docs/handoff/2026-10-22/REPLAY_PERSIST_ROUNDTRIP.md` and the before/after logs.

Pedestrian #42: `docs/handoff/2026-10-22/CURSOR_PEDESTRIAN_ACHIEVEMENTS_FINDING.md` only.

## CI rollup at query time

Conclusions are GitHub check rollups, not a local re-run. Details and commands are in I.

| PR | Rollup |
|---|---|
| #124 | 12 success, 6 failure (`wave011`, `wave013b`, `wave014`, `wave015`, `wave016`, `wave017`), 3 skipped |
| #125 | 6 success, 12 cancelled, 4 skipped |
| #126 | 2 success (both named `web`), 16 cancelled, 4 skipped |
| #127 | 12 success, 6 failure (same wave names as #124), 5 skipped |
| #128 | 12 success, 6 failure (same wave names), 5 skipped |
| #129 | 12 success, 6 failure (same wave names), 5 skipped |
| #130 | 11 success, 5 failure (`wave011`, `wave014`–`wave017`), `wave013b` and `windows-pilot0-windows-2025` still pending, 5 skipped |
| Pedestrian #42 | `gate1-core-loop`, `godot-headless-no-false-green`, `wp014-actual-production-runtime`, and `wave010` passed. `windows-pilot0-windows-2025` still pending |
| Anime #123 | CLEAN: 7 success, 5 skipped. Wave011–020 are absent from that rollup |
| Portal #55 | two `check` successes on `1f4ca20` |
