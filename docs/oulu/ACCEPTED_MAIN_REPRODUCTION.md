# Accepted-main reproduction — 2026-08-27 / post-A2 refresh 2026-08-28

Machine-readable: [`artifacts/oulu_readiness_2026_08_27/ACCEPTED_MAIN_REPRODUCTION.json`](../../artifacts/oulu_readiness_2026_08_27/ACCEPTED_MAIN_REPRODUCTION.json)

**Post-A2 faculty paths** used detached worktrees `/tmp/oulu_post_a2_20260828/<repo>` at accepted `origin/main`. Owner dirty trees were not used as evidence.

Historical Stream A (2026-08-27) PASS on pre-A2 SHAs (7GC `4cd7016`, SpectrumX `cef3900`, NTN `9165209`) remains on record; live freeze uses post-A2 tips below.

## Environment

| Item | Value |
|---|---|
| Host | darwin 25.6.0 arm64 |
| Interpreter class | Existing repo `.venv` / Framework Python 3.11 |
| Repo `.venv` pytest | 9.x (7gc, spectrumx, ntn) |
| GitHub identity | `gunnchOS3k` / Edmund Gunn, Jr. (token redacted) |

## Post-A2 faculty results (primary instruments)

| Repo | main SHA | Faculty command | Result | Artifact | Class | Limitations |
|---|---|---|---|---|---|---|
| 7gc-digital-twin | `dc43a56` (#31) | `PYTHONPATH=src python -m pytest -q tests/test_rq1_statistical_parity.py --tb=line` (+ `make reproduce`) | **PASS** (10 passed / ~2s; reproduce EXIT 0) | `paper/artifacts/rq1_statistical_summary.json` | `SYNTHETIC_SIM` | Not RF / OTA; not scientifically complete |
| spectrumx-ai-ran-gary | `9060655` (#102; `b44357f` on main) | `PYTHONPATH=src python -m pytest -q tests/test_rq2_fidelity_checkpoint.py tests/test_paper_ii_digital.py --tb=line` | **PASS** (31 passed / ~1s) | `rq2_fidelity_checkpoint_tiny.json`; `rq2_information_equivalence_audit.json` (`information_equivalence_pass=true`) | `SYNTHETIC_SIM` | Not app persistence / production RAN / physical RF / RL / standardized 6G |
| ntn-resilience-sim | `c4215fc` (#28) | `PYTHONPATH=src python -m pytest -q tests/test_rq3_statistical_parity.py --tb=line` (+ `scripts/reproduce.py`) | **PASS** (8 passed; reproduce EXIT 0) | `paper/artifacts/rq3_statistical_summary.json`; `rq3_gary_failover_sweeps.json` | `SYNTHETIC_SIM` | No sim→measurement; no operator attach; local-edge/peer not in seeded Paper-III engine |

## Supporting instruments (unchanged tips; Stream A digital PASS retained)

| Repo | main SHA | Digital result | Notes |
|---|---|---|---|
| readygary-6g-beam-selection | `5698752` | **PASS** (Stream A) | Dirty local tables **not** evidence; `SYNTHETIC_SIM`; sub-ms edge not proven |
| edge-io-measurement-node | `af57fbd` | **PASS** (Stream A) | RF/spatial `PHYSICAL_PENDING` |
| waike-research-ops | `8eb2827` | **PASS** (Stream A) | Partner classroom `EXTERNAL_PENDING` |
| gunnchos-research-portal | `f4155bc` | control-plane | Not a wireless experiment |

Independent third-party reproduction remains **EXTERNAL_PENDING**. Pixel RF/QoS remains **PHYSICAL_PENDING**.
