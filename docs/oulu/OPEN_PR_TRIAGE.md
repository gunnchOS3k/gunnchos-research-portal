# Open PR triage — 2026-08-27

Machine-readable: [`artifacts/oulu_readiness_2026_08_27/OPEN_PR_TRIAGE.json`](../../artifacts/oulu_readiness_2026_08_27/OPEN_PR_TRIAGE.json)

**Owner merges. Cursor did not merge, close, or enable auto-merge.** Equivalence was judged from unique commits / `git cherry` / blob compare against `origin/main`, not from PR titles.

Census: **23 open PRs** across six research repos + this control plane.

| Classification | Count |
|---|---|
| SUPERSEDED | 3 |
| PARTIALLY SUPERSEDED | 5 |
| STALE BUT CONTAINS UNIQUE COMMITS | 7 |
| CONFLICTING | 8 |
| CURRENT / UNIQUE | 0 |

| Recommended owner action | Count | Automate? |
|---|---|---|
| CLOSE_AS_SUPERSEDED | 9 | No |
| EXTRACT_UNIQUE_COMMIT | 9 | No |
| MANUAL_CONFLICT_REVIEW | 5 | No |
| REVIEW_FOR_MERGE | 0 | — |
| LEAVE_OPEN | 0 | — |
| REBASE_AND_REVIEW | 0 | — |

## PRs that need Edmund decisions

Do **not** close solely because they look old. These still have unique paths or conflicts that a human should skim.

### Extract unique commit (pedagogy / history / wearable notes)

| Repo | PR | Why |
|---|---|---|
| 7gc-digital-twin | [#29](https://github.com/gunnchOS3k/7gc-digital-twin/pull/29) | History archives `docs/history/*` after WP-012 README was superseded |
| spectrumx-ai-ran-gary | [#99](https://github.com/gunnchOS3k/spectrumx-ai-ran-gary/pull/99) | Same README-history leftover |
| spectrumx-ai-ran-gary | [#83](https://github.com/gunnchOS3k/spectrumx-ai-ran-gary/pull/83) | `docs/WAIKE_INTEGRATION.md` is richer than main's one-line `docs/14_WAIKE_INTEGRATION.md` |
| readygary-6g-beam-selection | [#12](https://github.com/gunnchOS3k/readygary-6g-beam-selection/pull/12) | Same WAIKE unique text vs numbered stub |
| edge-io-measurement-node | [#18](https://github.com/gunnchOS3k/edge-io-measurement-node/pull/18) | Unique wearable/privacy filenames; later PR #38 superseded most PhD pack |
| edge-io-measurement-node | [#8](https://github.com/gunnchOS3k/edge-io-measurement-node/pull/8) | WAIKE unique text; conflicting |
| ntn-resilience-sim | [#26](https://github.com/gunnchOS3k/ntn-resilience-sim/pull/26) | README history archive |
| ntn-resilience-sim | [#10](https://github.com/gunnchOS3k/ntn-resilience-sim/pull/10) | WAIKE unique text; conflicting |
| gunnchos-research-portal | [#1](https://github.com/gunnchOS3k/gunnchos-research-portal/pull/1) | Unique `content/waike.ts` / instructor pathway files |

### Manual conflict review (hardening / landing)

| Repo | PR | Why |
|---|---|---|
| spectrumx-ai-ran-gary | [#92](https://github.com/gunnchOS3k/spectrumx-ai-ran-gary/pull/92) | Draft hardening; CI FAIL; unique CLAIMS/MISSION vs later `quality/` matrix |
| readygary-6g-beam-selection | [#21](https://github.com/gunnchOS3k/readygary-6g-beam-selection/pull/21) | Draft hardening; DIRTY |
| edge-io-measurement-node | [#17](https://github.com/gunnchOS3k/edge-io-measurement-node/pull/17) | Draft hardening; unique field-test protocol; CI FAIL |
| gunnchos-research-portal | [#5](https://github.com/gunnchOS3k/gunnchos-research-portal/pull/5) | Draft public landing pages vs later `docs/phd/` |
| gunnchos-research-portal | [#4](https://github.com/gunnchOS3k/gunnchos-research-portal/pull/4) | Draft Tier-3 hardening vs merged supervisor-ready |

### Recommended close as superseded (after a 60-second glance)

| Repo | PR | Why close is still an owner action |
|---|---|---|
| 7gc-digital-twin | [#23](https://github.com/gunnchOS3k/7gc-digital-twin/pull/23) | PhD pack says experiments are prototype-pending; `make reproduce` now PASSes on main |
| spectrumx-ai-ran-gary | [#93](https://github.com/gunnchOS3k/spectrumx-ai-ran-gary/pull/93) | Later Paper II JSON + `OULU_CWC_ALIGNMENT.md` |
| spectrumx-ai-ran-gary | [#91](https://github.com/gunnchOS3k/spectrumx-ai-ran-gary/pull/91) | `OULU_WCE_ALIGNMENT.md` subset of `OULU_CWC_ALIGNMENT.md` |
| readygary-6g-beam-selection | [#22](https://github.com/gunnchOS3k/readygary-6g-beam-selection/pull/22) | Later FR2/Sub-6/dual-band Paper II pack |
| readygary-6g-beam-selection | [#20](https://github.com/gunnchOS3k/readygary-6g-beam-selection/pull/20) | WCE doc superseded by CWC doc |
| edge-io-measurement-node | [#16](https://github.com/gunnchOS3k/edge-io-measurement-node/pull/16) | Same WCE vs CWC |
| ntn-resilience-sim | [#20](https://github.com/gunnchOS3k/ntn-resilience-sim/pull/20) | Later assumption registry + Paper III summary |
| waike-research-ops | [#41](https://github.com/gunnchOS3k/waike-research-ops/pull/41) | Stale PhD docs **and** `__pycache__/*.pyc` must not merge |
| gunnchos-research-portal | [#3](https://github.com/gunnchOS3k/gunnchos-research-portal/pull/3) | `content/supervisor_landing.md` vs `docs/phd/START_HERE_SUPERVISOR.md` |

No open PR is `REVIEW_FOR_MERGE` as-is.

## Dirty trees recorded (not used as main truth)

- `readygary-6g-beam-selection`: 24 uncommitted result/table files on `cursor/readygary-accepted-main-ci-hygiene-001`. Audit used detached `origin/main` `5698752`.
- `waike-research-ops` / this portal: untracked `.worktrees/` only.
