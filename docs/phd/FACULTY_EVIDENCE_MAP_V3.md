# Faculty evidence map (V3) — strongest evidence only

**Freeze date:** 2026-08-27  
**Detail:** `docs/oulu/FACULTY_EVIDENCE_FREEZE.md`, `V3_RESEARCH_PLAN_EVIDENCE_ALIGNMENT_REPORT.md`  
**No affiliation / commitment / standardized-6G-product claims.**

Working title: *Resilience-Aware Service Continuity in Heterogeneous 6G Networks: Cross-Layer Orchestration for Resource-Constrained Devices*

---

## RQ1 / Paper I — profiles & benchmark

| | |
|---|---|
| **Contribution** | Measurable service-continuity profiles and synthetic benchmark scenarios for four device classes |
| **Primary instrument** | `7gc-digital-twin` @ `4cd70169b35a67937eac076caaa7905ffd47adeb` |
| **Strongest evidence** | `fixtures/device_os/SERVICE_CONTINUITY_PROFILES.json`; `results/experiments/rq1_gary_flagship_profiles.json` |
| **Reproduce** | `PYTHONPATH=src python scripts/reproduce.py` (tests: `PYTHONPATH=src python -m pytest -q tests/ --tb=line`) |
| **Limitation** | Synthetic; joint fidelity+checkpoint not one frozen action model; stats lighter than Paper II |
| **Oulu strengthen** | Supervisor narrowing of profile metrics; optional witnessed scenario review |

## RQ2 / Paper II — cross-layer control

| | |
|---|---|
| **Contribution** | Transparent baselines vs rule-based access×placement control; beam/band instrument under synthetic channel models |
| **Primary instruments** | `spectrumx-ai-ran-gary` @ `cef3900…`; `readygary-6g-beam-selection` @ `5698752…` |
| **Strongest evidence** | SpectrumX Paper II held-out/ablation/domain-shift JSON + CIs; ReadyGary FR2/beam tables (`SYNTHETIC_SIM`) |
| **Reproduce** | SpectrumX: `python scripts/demo_airan_policy.py --toy` + Paper II pytest; ReadyGary: `PYTHONPATH=. python scripts/run_benchmark_table.py --toy` |
| **Limitation** | Fidelity + checkpoint/recover **MISSING_DIGITAL**; not RL; sub-ms edge inference not proven |
| **Oulu strengthen** | Design order for missing actions; information-equivalent radio comparisons; lab timing discipline |

## RQ3 / Paper III — fallback & measurement

| | |
|---|---|
| **Contribution** | TN/NTN/offline decision regions under documented assumptions; measurement schema toward device-level evidence |
| **Primary instruments** | `ntn-resilience-sim` @ `9165209…`; `edge-io-measurement-node` @ `af57fbd…` |
| **Strongest evidence** | `results/experiments/rq3_gary_failover_sweeps.json` (rejects “NTN always better” under stated assumptions); Edge I/O research export schema |
| **Reproduce** | NTN: `PYTHONPATH=src python scripts/reproduce.py`; Edge I/O: `PYTHONPATH=src python3.11 scripts/reproduce.py` |
| **Limitation** | No sim→field transfer; RF/spatial **PHYSICAL_PENDING**; Pixel = install/launch smoke only |
| **Oulu strengthen** | Test-network interruption campaign; witnessed RF/QoS; ethics/permits path if human/field data enter |

## Supporting (not automatic papers)

WAIKE (`8eb2827`) = education workload model (digital RC PASS; classroom EXTERNAL_PENDING). Portal = navigation/control plane only.
