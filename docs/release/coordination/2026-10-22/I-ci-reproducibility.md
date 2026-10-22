# I. Current CI and reproducibility evidence

Disk before any portal command: `df -h /` reported Avail **15Gi** on `/dev/disk3s1s1`. That is under the 18 GiB reserve. No Godot export, asset import, npm install, or other heavy build was started.

## Commands that were run

```sh
df -h /
git worktree list   # portal, anime-aggressors, pedestrian-pursuit
git diff --name-only <parent> <head>   # read-only, for #124–#130 and Pedestrian #42
git merge-base <head> 7c25c299
gh pr view / gh pr list / gh pr checks
python3 scripts/validate_v1_release_ledger.py
python3 scripts/validate_v1_snapshot_adoption.py
python3 scripts/validate_v1_campaign_oct19.py
```

The campaign validator now also requires `CURRENT.json` to stay revision 2, `board-v0003.json` to stay `LOCAL_REVIEW_ONLY_NOT_ACCEPTED_MAIN`, and `docs/handoff/2026-10-22/LEDGER_HASHES.json` to match the six accepted files. Those hashes matched.

Local results in this worktree:

- `python3 scripts/validate_v1_release_ledger.py` — `PASS: 108 features, 38 gates, 43 tickets; scope, SHA bases, DAG, evidence hashes and owner firewalls intact`
- `python3 scripts/validate_v1_snapshot_adoption.py` — `PASS: 23 snapshot files unchanged; initial rolling revision preserves gates and existing-origin invite plan`
- `python3 scripts/validate_v1_campaign_oct19.py` — `PASS: canonical 16, RC1 assets, eight EPUB bindings, six scoped journeys, revision 2 CURRENT pointer, ledger hashes and unchanged approval boundaries`

`make test` pieces run locally without a repo copy:

- `python3 scripts/validate_supervisor_ready.py` — `PASS digital control-plane files present and claim-boundary checks clean`
- `pytest -q tests/test_audit_portfolio.py` in a temporary virtualenv — `7 passed`

`.github/workflows/ci.yml` also runs `make code-health-r5-s1` on `ubuntu-latest`. That target copies the tree into a temp directory. The copy was not run on this machine because Avail is already under the 18 GiB reserve. The GitHub `ubuntu-latest` job does not use this disk. Do not inherit #55's green checks.

This branch's own `check` jobs on `f7a1d2bef4bd7ee12819664eb40bdc7e65ab2b0f` passed:

- https://github.com/gunnchOS3k/gunnchos-research-portal/actions/runs/39868698058/job/120137358081 (14s)
- https://github.com/gunnchOS3k/gunnchos-research-portal/actions/runs/39868702941/job/120137375376 (18s)

A later documentation-only commit that records these URLs needs its own requery. It does not change the ledger.

## Commands that were not run

- Godot exports, GLB import, and Anime wave harnesses, including the failing `wave011` job.
- `adb devices`.
- Public-site, WAIKE, BeatLink, invite-route, and FieldKit scheduled-workflow reproductions.
- `python3 tools/validate_game_rc_contracts.py` in Pedestrian. The engineering note says it already exited 0 with achievements=12. This pass did not repeat it.
- Any merge, tag, deploy, or publish.

## Remote evidence

Portal #55 on `1f4ca20`, both `check` jobs passed:

- https://github.com/gunnchOS3k/gunnchos-research-portal/actions/runs/39836107630/job/120024761726
- https://github.com/gunnchOS3k/gunnchos-research-portal/actions/runs/39836113939/job/120024785049

Those conclusions bind `1f4ca20` only. This branch needs its own run.

Anime #123 on `7c25c299` is MERGEABLE and CLEAN: `authority`, `full-roster`, `infra`, both `web`, and both Windows pilot jobs succeeded. `grab-acting-8b`, `form-acting-8c`, `controls-8d`, `hands-8d2`, and `controls-8d-engine-review` were skipped. Wave011–020 do not appear on that rollup.

Cursor Anime drafts are UNSTABLE. The repeated failure sample is #127 `wave011`, job https://github.com/gunnchOS3k/anime-aggressors/actions/runs/39859911059/job/120107619790. The log ends with `"pass": false` and `INVALID_MUTATION:clean_baseline_not_pass`, exit code 2. The same wave names fail on #124 and #127–#129. #130 still had `wave013b` and `windows-pilot0-windows-2025` pending when queried, with `wave011` and `wave014`–`wave017` already failed. #125 and #126 mostly show CANCELLED jobs, so they are not green either.

This pass does not claim the one-line product diffs caused that mutation failure, and it does not treat the failure as acceptable. The harness was not re-run locally.

Pedestrian #42 run https://github.com/gunnchOS3k/pedestrian-pursuit/actions/runs/39865178208 passed `gate1-core-loop`, `godot-headless-no-false-green`, and `wp014-actual-production-runtime`. `wave010` passed on https://github.com/gunnchOS3k/pedestrian-pursuit/actions/runs/39865178146 and on https://github.com/gunnchOS3k/pedestrian-pursuit/actions/runs/39865096222. `windows-pilot0-windows-2025` was still pending.

## Reproducibility limit

October 19 asset verification (33/33 streamed hashes) was not repeated. The campaign validator still checks the stored evidence hashes. That is a ledger lock, not a new download of release binaries.
