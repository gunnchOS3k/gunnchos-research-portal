# Faculty evidence map (V3) — strongest evidence only

**Freeze date:** 2026-08-27 · **post-A2 refresh:** 2026-08-28  
**Detail:** `docs/oulu/FACULTY_EVIDENCE_FREEZE.md`, `V3_RESEARCH_PLAN_EVIDENCE_ALIGNMENT_REPORT.md`  
**No affiliation / commitment / standardized-6G-product claims.** Dissertation **not** complete.

Working title: *Resilience-Aware Service Continuity in Heterogeneous 6G Networks: Cross-Layer Orchestration for Resource-Constrained Devices*

---

## RQ1 / Paper I — profiles & benchmark

| | |
|---|---|
| **Status** | `DIGITAL_REPRODUCIBLE_STRONG_CORE` |
| **Contribution** | Measurable service-continuity profiles and seeded synthetic benchmarks for four device classes |
| **Primary instrument** | `7gc-digital-twin` @ `dc43a567e3f2e81a5b59fea6dd67c7054cfdde56` (merged #31; historical `4cd7016…`) |
| **Strongest evidence** | Profiles + seeds 1..30; `task_completion_ratio` / `time_above_minimum_useful` with 95% Student-t CIs; `paper/artifacts/rq1_statistical_*` |
| **Reproduce** | `PYTHONPATH=src python -m pytest -q tests/test_rq1_statistical_parity.py --tb=line` |
| **Limitation** | `SYNTHETIC_SIM`; not scientifically complete / field validated; independent `EXTERNAL_PENDING` |
| **Oulu strengthen** | Supervisor narrowing of profile metrics; optional witnessed scenario review |

## RQ2 / Paper II — cross-layer control

| | |
|---|---|
| **Status** | `DIGITAL_REPRODUCIBLE_STRONG_CORE` |
| **Contribution** | Transparent baselines vs rule-based access×placement×fidelity×checkpoint control; beam/band instrument under synthetic channel models |
| **Primary instruments** | `spectrumx-ai-ran-gary` @ `9060655…` (#102 / `b44357f` on main); `readygary-6g-beam-selection` @ `5698752…` |
| **Strongest evidence** | Fidelity + causal checkpoint/recover; fixed-fidelity / checkpoint-disabled baselines; runtime info-equivalence; Paper II held-out/ablation/domain-shift + CIs; ReadyGary FR2 tables |
| **Reproduce** | `PYTHONPATH=src python -m pytest -q tests/test_rq2_fidelity_checkpoint.py tests/test_paper_ii_digital.py --tb=line` |
| **Limitation** | `SYNTHETIC_SIM`; do **not** claim app persistence / production RAN / physical RF / trained RL / standardized 6G; sub-ms edge not proven |
| **Oulu strengthen** | Information-equivalent radio comparisons at lab scale; lab timing discipline |

## RQ3 / Paper III — fallback & measurement

| | |
|---|---|
| **Status** | `DIGITAL_REPRODUCIBLE_STRONG_CORE_WITH_TRANSFER_PENDING` |
| **Contribution** | TN/NTN/offline decision regions under documented assumptions; measurement schema toward device-level evidence |
| **Primary instruments** | `ntn-resilience-sim` @ `c4215fc…` (#28); `edge-io-measurement-node` @ `af57fbd…` |
| **Strongest evidence** | Seeds 1..30; CIs; paired defs; `ntn_always_better=false` with negative regions; Edge I/O research export schema |
| **Reproduce** | NTN: `PYTHONPATH=src python -m pytest -q tests/test_rq3_statistical_parity.py --tb=line` |
| **Limitation** | No sim→field transfer; RF/spatial **PHYSICAL_PENDING**; local-edge/peer not in seeded Paper-III engine; Pixel = install/launch smoke only |
| **Oulu strengthen** | Test-network interruption campaign; witnessed RF/QoS; ethics/permits path if human/field data enter |

## Supporting (not automatic papers)

WAIKE (`8eb2827`) = education workload model (digital RC PASS; classroom EXTERNAL_PENDING). Portal = navigation/control plane only.
