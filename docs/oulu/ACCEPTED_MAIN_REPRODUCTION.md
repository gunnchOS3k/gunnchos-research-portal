# Accepted-main reproduction — 2026-08-27

Machine-readable: [`artifacts/oulu_readiness_2026_08_27/ACCEPTED_MAIN_REPRODUCTION.json`](../../artifacts/oulu_readiness_2026_08_27/ACCEPTED_MAIN_REPRODUCTION.json)

Worktrees: `/tmp/oulu_audit_20260827/<repo>` at detached `origin/main`. Owner dirty trees were not reset.

## Environment

| Item | Value |
|---|---|
| Host | darwin 25.6.0 arm64 |
| Homebrew Python | 3.14.7 — `pip install pytest` blocked by PEP 668 (`BLOCKED_DEPENDENCY` for that interpreter only) |
| Framework Python | 3.11.2, pytest 9.0.3 |
| Repo `.venv` pytest | 9.1.1 (7gc, spectrumx, readygary, ntn) |
| GitHub identity | `gunnchOS3k` / Edmund Gunn, Jr. (token redacted) |

No accepted-main test was silently fixed. Homebrew 3.14 lack of pytest was recorded, then existing venvs / Python 3.11 were used as the documented interpreter class.

## Results

| Repo | main SHA | Digital result | Tests | Scientific script | Strongest output |
|---|---|---|---|---|---|
| 7gc-digital-twin | `4cd7016` | **PASS** | 55 passed / 3s | `scripts/reproduce.py` EXIT 0 / 2s | `rq1_gary_flagship_profiles.json` (`synthetic-fixture`) |
| spectrumx-ai-ran-gary | `cef3900` | **PASS** | 10 passed / 2s | `scripts/demo_airan_policy.py --toy` EXIT 0 | `results/e2e/airan_policy_metrics.json` seed 42 |
| readygary-6g-beam-selection | `5698752` | **PASS** | 31 passed / 2s | `scripts/run_benchmark_table.py --toy` EXIT 0 | `SYNTHETIC_SIM`; `sub_ms_inference_proven: false` |
| edge-io-measurement-node | `af57fbd` | **PASS** | 26 passed / 1s | `scripts/reproduce.py` EXIT 0 | export `spatial_accuracy: PHYSICAL_PENDING` |
| ntn-resilience-sim | `9165209` | **PASS** | 29 passed / 1s | `scripts/reproduce.py` EXIT 0 | `rq3_gary_failover_sweeps.json` |
| waike-research-ops | `8eb2827` | **PASS** | 19 passed / 2s | `scripts/emit_digital_rc.py` EXIT 0 | `artifacts/COURSE_COUNTS.json` |
| gunnchos-research-portal | `2a3303d` | **PASS** | 7 passed / 1s | control-plane pytest | not a wireless experiment |

Exact commands are in the JSON. Independent third-party reproduction remains **EXTERNAL_PENDING**. Pixel RF/QoS remains **PHYSICAL_PENDING**. Partner classroom remains **EXTERNAL_PENDING**.
