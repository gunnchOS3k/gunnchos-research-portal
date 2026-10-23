# Ancestry reconciliation — 2026-10-23

This note is additive. It does not edit `V1_0_0_LEDGER_2026-10-09.json`, `CURRENT.json`, `board-v0002.json`, `board-v0003.json`, `BLOCKERS.json`, or the October 19 campaign reports. Those files still describe the earlier unmerged state. That older text is historical. It is not the ancestry check below.

Denominators stay 16 components, 108 features, 38 gates, and 43 tickets. No feature `complete` flag changes. No gate is set to true. `RC2_READY` stays false. `V1_0_0_RELEASE_AUTHORIZED` stays false. A merged pull request is not a release authorization.

Rechecked with `gh` on 2026-10-23. `compare` status `ahead` with `behind_by` 0 means the pull-request head is an ancestor of `main`.

| Repo | PR | Head | GitHub merge commit | Base | On `main` now |
| --- | --- | --- | --- | --- | --- |
| gunnchos-7gc-ai-ran-field-kit | #123 | `ddf90ab0c4e4b29e765be73093d0ba91c59249d0` | `78d9b641474c430c3ab64eefc29641e2388c1d9f` | `main` | Yes. `main` is that merge commit. |
| ntn-resilience-sim | #31 | `8cda07f4e73ac5e5ada09f778e7d29ad1ef4ee75` | `8f779886abacc22349fb2d80231a1bc003443245` | `main` | Yes. `main` is that merge commit. |
| readygary-6g-beam-selection | #30 | `81e8318c0853aa17acd1e9465f292e3218bf5858` | `cb71ff9523cf520ac1e346f6e4caa381f38e15f8` | `main` | Yes. `main` is that merge commit. |
| edge-io-measurement-node | #43 | `dd51b903222040e19e0f3efe0bd70c5d9951a240` | `c339a5e98228bb955079f5dc158e081caca361ff` | `main` | Yes. `main` is that merge commit. |
| gunnchos-hardware-industrial-design | #87 | `9524ef5388448506650abedc0aa65d775cd59f57` | `1b837119eb232b841a8c210a64af8d259385cb1e` | `main` | Yes. `main` is that merge commit. |
| spectrumx-ai-ran-gary | #107 | `245b56243105f04ae5deb9e75622f2ec00912039` | `7baf08f988b75c0bd2016ed8799e3b2a1375d0e3` | `main` | Yes. `main` is that merge commit. |
| spectrumx-ai-ran-gary | #108 | `2becf04fda1dcf8906328cc4af3e6723c5dcc05e` | `7bcd14251e17f655370aba8b52ba80a2da9a588c` | `lane-e/spectrumx-heldout-seed-split` | No. Compare of the head to `main` is diverged (`ahead_by` 12, `behind_by` 3). The merge commit is also diverged (`behind_by` 4). |

Sentences that still say Field Kit #123, NTN #31, ReadyGary #30, Edge IO #43, Hardware #87, or SpectrumX #107 are unmerged are stale for ancestry only. Features `R-002`, `R-003`, `R-004`, `R-005`, `R-006`, and `HW-001` through `HW-004` stay `complete: false`. Blockers stay open. SpectrumX #108 stays a side-branch merge until a later check shows its commits on `main`.
