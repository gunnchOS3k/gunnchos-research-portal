# J. Engineering work ready for owner and Codex review

All of the following stay **draft and unmerged**. Review is not acceptance, and acceptance is not authorization.

| Draft | What a reviewer can accept or reject | Recommendation |
|---|---|---|
| Anime #124 `b74cf3c6` | The written finding that form-audio exit warnings are delayed playback cleanup, on parent `9516770d`. | Reject as a product fix. The finding can stay on the draft. Do not merge it onto the art tip as behavior. |
| Anime #125 `d12fba82` | 36 `importer=keep` sidecars for `form_acting_8c`, plus a pack probe. Export filters and GLB bytes are unchanged on that branch. Parent `3ab7667c`, 7 art commits behind. | Hold. Rebase onto the current Codex tip before review. Do not treat sidecars as full Web/Android proof. |
| Anime #126 `46cf7ffe` | Three device-0 events in `project.godot`: `p1_up`, `p1_down`, `p1_grab`. Keyboard unchanged on that diff. Parent `bda5b5a5`, 2 art commits behind. CI mostly cancelled. | Hold for rebase and a completed CI rollup. Codex still owns whether grab-on-device-0 matches final feel. |
| Anime #127 `9dd5e3e8` | Host frame uses `Boolean(i.semantic.grab)` and the browser controller has a Grab button. Combat `stepState` is outside the diff. | Review this grab mapping first. CI waves are red. A code review can proceed; a merge cannot. |
| Anime #128 `efd26b23` | Posted second-client input is queued and served on `world.inputs`. `partySimInputsFromControllerInputs` forces `grab: false`. | Reject a naive merge after #127. Reconcile the grab bit first. See H. |
| Anime #129 `b8eecbc5` | Save load maps stocks, cpu level, and match timer from `rules.stocks`, `rules.cpu_level`, and `rules.timer`. | Eligible for engineering review as a narrow save fix. It does not close B02, balance, or human feel. |
| Anime #130 `cfd6e71d` | Private-match replay write and read at `user://aa_private_match_replay.json`. | Eligible for engineering review beside #129. Different files. CI was still incomplete when queried. It does not close B02. |
| Pedestrian #42 `bc327c8c` | Documents that the achievement catalog already has 12 entries and the RC contract validator already passed. No game change. | Leave unmerged. It is not a portal ledger id and it does not need a product merge to preserve the finding. |
| FieldKit `92d0864` | Not a pull request opened by this pass. | Do not dispatch. |

Codex review is required before any Anime draft that touches presentation, packaging of form-acting assets, controller feel, or audio interpretation is treated as final. #125 and #124 are in that set. #126's grab binding is controller runtime, with feel still owned by Codex.

No draft above is recommended for merge in this packet.
