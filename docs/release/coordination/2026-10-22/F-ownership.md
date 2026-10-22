# F. Cursor and Codex work ownership

## Codex

Codex owns Anime character models, rigging, transformed appearances, animation, ultimate cinematics, visual art direction, sound direction, and final game feel.

Read-only observation on 2026-10-22: worktree `/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos/_anime_v1_closure` is branch `release/anime-v1-dialogue-and-elemental-performance` at `7c25c2996f8adcee97ec2187a14bfc578d8681bf`. That SHA matches `origin` and draft PR #123. The worktree has untracked art-pipeline files. They were not opened and not edited. This coordination pass did not commit, reset, or clean that checkout.

Codex stack that Cursor drafts sit against, when they are current: draft #123 at `7c25c299`, stacked on draft #122. Neither is merged.

## Cursor Engineering

The separate Cursor Engineering Continuation session owns Anime runtime, networking, controller, save and replay, CI, packaging, security, and integration corrections. That session already opened drafts #124–#130. This coordination pass does not launch, rewrite, or rebase those branches.

Their worktrees under `anime-aggressors/.worktrees/cursor-v1-*` were inspected with `git diff` and `git status` was not used to modify them.

## This coordination session

This session owns assignment tracking, cross-repo dependencies, branch and pull-request integration planning, provenance, release-gate evidence, blocker reconciliation, and the V1/RC2 readiness recommendation.

Writable checkout, created for this pass only:

- Path: `gunnchos-research-portal/.worktrees/cursor-v1-release-coord`
- Branch: `eng/cursor-v1-release-coord`
- Base: `1f4ca20190c99dde5712e9e490ec81e05f1122dd`

Portal worktree `repos/_v1_integration_2026_10_19` already owns `release/v1-integration-2026-10-19`. No commit was made there. Anime main checkout `repos/anime-aggressors` was not edited. Pedestrian worktrees were listed and not edited.

## Lane allocation

| Lane | State | Independent of Anime art? |
|---|---|---|
| Universal controllers, PartyLink, invites | Started. Drafts #126, #127, and #128 exist and are unmerged. Invite contract INV-01 is not started. | PartyLink drafts must follow Codex tip `7c25c299` before integration. Invites can be designed separately and still need every product adapter. Do not open another Anime controller branch from this session. |
| WAIKE, 3k MLV, gunnchAI | Unassigned here. Existing private WAIKE and MLV candidates stay where they are. | Yes for reading those candidates. No for trusted live replay, real auth, or human education acceptance. |
| Website, Passport, publications | Unassigned here. Historical website taste pass stays at its original scope. | Yes. Passport and eight-edition release still need their owners. |
| Pedestrian Pursuit | Started as finding-only draft #42. Leave it unmerged. | Yes. No further Pursuit engineering was started. |
| Archive of Life | Unassigned. | No. ARC-01 needs the external data and license owner before ingestion can count. |
| Device OS and hardware-software | Unassigned. | Metadata reconciliation can be discussed without Anime. Physical install and manufacturing claims cannot proceed. |
| 6G and research infrastructure | Unassigned. FieldKit `92d0864` stays undispatched. | Yes for evidence binding. No FieldKit dispatch and no measured-radio claim. |
| Final cross-product integration | Started as this packet only. | No. B14 waits on the other lanes. |

Human, rights, security, physical-device, scientific, and external approvals stay ungranted.
