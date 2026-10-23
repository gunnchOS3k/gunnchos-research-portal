# H. PR compatibility and proposed integration sequence

This is a plan. **No rebase, cherry-pick, or merge was performed.** Codex's branch and the Cursor engineering branches were not checked out for writing.

## #127 and #128

They are independent drafts. Both parents are `7c25c299`. They are not stacked.

Shared path: `packages/partylink/src/lanHost.ts` only. `git diff --name-only` intersection against the common parent is that one file.

#127 changes the host frame inside `tick()` from `grab: false` to `grab: Boolean(i.semantic.grab)` and adds a Grab button in `browserController.ts`. The diff does not include a combat `stepState` change.

#128 replaces that `tick()` body. It drains posted inputs through `consumePostedPartyFrames` and copies the resulting batch onto `pub.world.inputs`. `partySimInputsFromControllerInputs` in `postedPartyFrames.ts` still sets `grab: false`. Its comment says the release tip forces grab false and that unmerged #127 owns `semantic.grab`. The #128 diff does not contain `Boolean(i.semantic.grab)`.

If #128 lands on top of #127 without an edit, the Boolean grab line disappears with the old `tick()` mapping, and the posted-frame mapper reintroduces `grab: false`.

Required sequence, for the engineering owner to execute later:

1. Review #127's grab mapping and Grab button first.
2. Rebase or manually reconcile #128 onto that result so `partySimInputsFromControllerInputs` copies the posted grab bit instead of forcing false.
3. Keep `stepState` left/right-only unless a separate combat change is authorized. #127 does not authorize that.

## #129 and #130

No shared paths. #129 touches `game-godot/scripts/core/GameState.gd` and a save probe. #130 touches `game-godot/scripts/net/replay_store.gd`, `game-godot/scripts/net/private_netplay_stack.gd`, and a replay probe. They can be reviewed in parallel with each other. They still wait on CI and owner review, and they do not close B02.

`ensure_save_loaded` on #129 reads `rules.stocks` (default 3), `rules.cpu_level` (default 2), and `rules.timer` into `match_timer_seconds` (default 180).

#130 `simulate_match_frames` calls `ReplayStore.write_json`. `read_json` is new. Default path: `user://aa_private_match_replay.json`.

## #125 and #126 against the Codex tip

Codex tip is still `7c25c299`. It has not moved past the last check.

| PR | Merge-base with `7c25c299` | Commits on the tip that the PR lacks | Shared paths with those commits |
|---|---|---|---|
| #125 | `3ab7667c` | 7 (`3ab7667c..7c25c299`) | none |
| #126 | `bda5b5a5` | 2 (`2d762eef`, `7c25c299`) | none |

No shared path means a textual merge may be possible, and GitHub currently reports both MERGEABLE. The branches are still behind the art tip. Later art commits change hand and control sources, `fighter_model_3d.gd`, and `source_controls_8d.gd`. Review them only after the engineering owner rebases onto the then-current Codex tip. This pass did not rebase them. CI for both is unstable: #125 has cancelled wave jobs, and #126 has sixteen cancelled jobs and only the two `web` successes.

## #124

Parent `9516770d` is 10 commits behind `7c25c299`. GitHub's recorded `base.sha` (`3ab7667c`) is also behind the live tip. The change is a finding: delayed AudioServer cleanup, with no production audio change. Do not merge it as a product fix. B02 and the sound-direction gate stay open.

## Order to propose, not to execute here

1. Leave #124 unmerged as a finding.
2. Engineering rebases #125 and #126 onto the current Codex tip, then reviews them. Packaging sidecars and three joypad actions do not close export or feel gates.
3. Review #127.
4. Reconcile #128 so the posted grab bit survives.
5. Review #129 and #130 independently of that conflict.
6. Leave Pedestrian #42 unmerged. It is a validator finding, not a portal ledger id.
7. Do not merge #122, #123, #55, or this coordination branch as part of that sequence.
