# RQ → evidence matrix — 2026-08-27 freeze (post-A2 refresh 2026-08-28)

Machine-readable: [`artifacts/oulu_readiness_2026_08_27/RQ_EVIDENCE_MATRIX.json`](../../artifacts/oulu_readiness_2026_08_27/RQ_EVIDENCE_MATRIX.json)

Audited **accepted `origin/main` only**. Evidence class is digital/`SYNTHETIC_SIM` unless stated. Independent reproduction is **EXTERNAL_PENDING** for every repo. Dissertation is **not** complete.

Working title (V3): *Resilience-Aware Service Continuity in Heterogeneous 6G Networks: Cross-Layer Orchestration for Resource-Constrained Devices*

Truth boundary: 5G-Advanced / NTN-capable research architecture, IMT-2030 aligned — **not** standardized/commercial 6G.

Live SHAs: 7GC `dc43a56` · SpectrumX `9060655` (PR #102 / `b44357f` on main) · ReadyGary `5698752` · Edge I/O `af57fbd` · NTN `c4215fc` · WAIKE `8eb2827` · portal `f4155bc`.  
Historical pre-A2: 7GC `4cd7016` · SpectrumX `cef3900` · NTN `9165209`.

## RQ rollup

Canonical V3 wording is below. Short labels are evidence-audit interpretations only.

### RQ1 / Paper I

**Canonical RQ (V3).** How can representative workloads and the constraints of four resource-constrained device classes be translated into measurable service-continuity profiles, metrics, and benchmark scenarios?

**Evidence-audit interpretation.** Service-continuity profiles, metrics, and benchmarks.

| Status | Strongest accepted-main evidence | Biggest gap |
|---|---|---|
| DIGITAL_REPRODUCIBLE_STRONG_CORE | 7GC `dc43a56` (#31): profiles + seeded bench seeds 1..30; `task_completion_ratio` + `time_above_minimum_useful`; correct 95% t-CI; paired \(d_z\); `SYNTHETIC_SIM` | Not scientifically complete / field validated; independent `EXTERNAL_PENDING` |

### RQ2 / Paper II

**Canonical RQ (V3).** To what extent can joint access selection, computation placement, fidelity/model adaptation, caching/checkpointing, and recovery control - informed by radio-aware digital-twin state and uncertainty - improve service-continuity utility under mobility, blockage, congestion, edge-resource variation, and energy constraints?

**Evidence-audit interpretation.** Cross-layer controller (access, placement, fidelity, checkpoint/recover).

| Status | Strongest accepted-main evidence | Biggest gap |
|---|---|---|
| DIGITAL_REPRODUCIBLE_STRONG_CORE | SpectrumX `9060655` (#102): fidelity action; causal checkpoint/recover; fixed-fidelity / checkpoint-disabled baselines; runtime info-equivalence; Paper II held-out/ablation/domain-shift + Student-t; ReadyGary FR2 beam JSON. `SYNTHETIC_SIM` | Do **not** claim app persistence / production RAN / physical RF / trained RL / standardized 6G |

### RQ3 / Paper III

**Canonical RQ (V3).** Under which disruption conditions do terrestrial, local-edge, peer/device-to-device, offline, and NTN fallback modes preserve minimum useful service, and what performance, energy, privacy, and recovery tradeoffs arise in simulation, emulation, and device-level measurements?

**Evidence-audit interpretation.** TN/NTN disruption, fallback, and transfer toward measurement.

| Status | Strongest accepted-main evidence | Biggest gap |
|---|---|---|
| DIGITAL_REPRODUCIBLE_STRONG_CORE_WITH_TRANSFER_PENDING | NTN `c4215fc` (#28): TN/NTN seeds 1..30; CIs; paired defs; decision regions; `ntn_always_better=false`; negative regions. `SYNTHETIC_SIM` | sim→measurement; operator attach; RF/spatial; local-edge/peer **not** in seeded Paper-III engine |

## Capability cells (primary instruments)

Status vocabulary is the required enum. Portal/WAIKE are supporting.

| Capability | 7GC | SpectrumX | ReadyGary | NTN | Edge I/O |
|---|---|---|---|---|---|
| Model variables | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | PARTIAL |
| System assumptions | PARTIAL | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | DOCUMENTED_ONLY |
| Service profiles | IMPLEMENTED_AND_REPRODUCIBLE | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| State/action space | PARTIAL | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | PARTIAL |
| Controller | PARTIAL | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | PARTIAL |
| Baselines | PARTIAL | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | NOT_APPLICABLE |
| Metrics | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE |
| Scenario generator | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | PARTIAL |
| TN/NTN disruption | PARTIAL | PARTIAL | NOT_APPLICABLE | IMPLEMENTED_AND_REPRODUCIBLE | MISSING_DIGITAL |
| Compute placement | PARTIAL | IMPLEMENTED_AND_REPRODUCIBLE | NOT_APPLICABLE | MISSING_DIGITAL | NOT_APPLICABLE |
| Fidelity adaptation | MISSING_DIGITAL | **IMPLEMENTED_AND_REPRODUCIBLE** | PARTIAL | MISSING_DIGITAL | MISSING_DIGITAL |
| Checkpoint/recovery | PARTIAL | **IMPLEMENTED_AND_REPRODUCIBLE** | MISSING_DIGITAL | PARTIAL | PARTIAL |
| Offline/degraded | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | PARTIAL | IMPLEMENTED_AND_REPRODUCIBLE | PARTIAL |
| Reproducibility (digital) | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE |
| Seeds/configs | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | PARTIAL |
| Experiment scripts | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE |
| Output schemas | PARTIAL | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | PARTIAL | IMPLEMENTED_AND_REPRODUCIBLE |
| Statistical reporting | **IMPLEMENTED_AND_REPRODUCIBLE** | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | **IMPLEMENTED_AND_REPRODUCIBLE** | MISSING_DIGITAL |
| Ablations | MISSING_DIGITAL | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | PARTIAL | MISSING_DIGITAL |
| Domain shift | PARTIAL | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | PARTIAL | MISSING_DIGITAL |
| Measurement hooks | PARTIAL | PARTIAL | EXTERNAL_PENDING | PARTIAL | PHYSICAL_PENDING |
| Ethics boundaries | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE |
| Claim–evidence map | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE | IMPLEMENTED_AND_REPRODUCIBLE |
| Sim→measurement transfer | MISSING_DIGITAL | MISSING_DIGITAL | EXTERNAL_PENDING | MISSING_DIGITAL | PHYSICAL_PENDING |

Exact SHA/path/command/artifact tuples are in the JSON.

WAIKE: **NOT_APPLICABLE** for radio cells; **IMPLEMENTED_AND_REPRODUCIBLE** for curriculum schema tests; partner classroom **EXTERNAL_PENDING**.
