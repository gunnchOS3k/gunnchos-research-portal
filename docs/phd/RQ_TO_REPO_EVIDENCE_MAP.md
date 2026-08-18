# RQ → repository → evidence map

Evidence classes follow [EVIDENCE_TAXONOMY.md](EVIDENCE_TAXONOMY.md). A repository’s existence is not Paper I/II/III evidence.

## RQ1 / Paper I

**Question.** How can representative workloads and the constraints of four resource-constrained device classes be translated into measurable service-continuity profiles, metrics, and benchmark scenarios?

| Item | Status at baseline audit (2026-08-18) |
|---|---|
| Primary repos | `gunnchos-device-os`, `7gc-digital-twin` |
| Service-Continuity Profile Model | Partial — device states, campus modes, twin site schemas exist; not yet a frozen Paper-I profile package |
| Benchmark scenarios | Partial — 7GC synthetic/site fixtures; not held-out Paper-I campaign |
| Device/service/network state schemas | Partial — launcher contracts, twin state JSON, Edge I/O schemas (supporting) |
| Minimum-useful / degraded / target / failed states | Partial — mode/state machines in device OS; not unified continuity metrics |
| Transparent static/reference/oracle baselines | Incomplete for RQ1 as a named experiment |
| Metrics + reproducibility package | Device OS and 7GC have `make test` / smoke paths; Paper-I frozen artifact **not** signed |
| Current evidence class | `SYNTHETIC_SIM` / `EMULATED` |
| Remaining | Unify profile schema; generate tables from code; independent reproduction |

Supporting workloads (games, WAIKE, gunnchAI) may supply traces **if** a frozen RQ1 experiment imports them.

## RQ2 / Paper II

**Question.** To what extent can joint access selection, computation placement, fidelity/model adaptation, caching/checkpointing, and recovery control informed by radio-aware digital-twin state and uncertainty improve service continuity under mobility, blockage, congestion, edge-resource variation, compute contention, and energy constraints?

| Item | Status at baseline audit |
|---|---|
| Primary repos | `spectrumx-ai-ran-gary`, `readygary-6g-beam-selection` |
| Simple baselines first | SpectrumX: detector-conditioned **rule-based** controller is the shipped path (not RL). ReadyGary: exhaustive/hierarchical baselines exist in code; README table must not be treated as measured RF |
| Digital-twin context | SpectrumX extension + 7GC twin manifests; coupling not a frozen Paper-II campaign |
| Held-out families, seeds, ablations, domain shift, uncertainty, CIs, compute cost, switching cost | Partial scripts (`make ablation`, toy benchmarks); **not** a complete Paper-II evidence pack |
| Known defect | ReadyGary README labelled **28 GHz as “Sub-6 GHz”** — technically false (FR2 mmWave). Must be corrected in-repo |
| Current evidence class | SpectrumX judged core: `OPEN_DATA_BACKED` (competition IQ). Extension/policy: `SYNTHETIC_SIM`. ReadyGary: `SYNTHETIC_SIM` |
| Remaining | Information-equivalent comparisons; reject unsupported latency claims (sub-ms unproven); independent reproduction |

## RQ3 / Paper III

**Question.** Under which disruption conditions do terrestrial, local-edge, peer/device-to-device, offline, and NTN fallback modes preserve minimum useful service, and what performance, energy, privacy, and recovery tradeoffs arise in simulation, emulation, and device-level measurements?

| Item | Status at baseline audit |
|---|---|
| Primary repos | `ntn-resilience-sim`, `edge-io-measurement-node` |
| Disruption families | NTN sim has demo/sensitivity targets; compound radio+compute+backhaul not yet a frozen Paper-III matrix |
| Measurement calibration | Edge I/O: simulated device / schema path; **absolute spatial accuracy `PHYSICAL_PENDING`** |
| Current evidence class | NTN: `SYNTHETIC_SIM`. Edge I/O: `EMULATED` (not `DEVICE_MEASURED`) |
| Remaining | Thresholded minimum-service metrics aligned with RQ1 profiles; physical calibration packet; no operator-performance claims |

## Supporting repositories (not automatic papers)

| Repository | Allowed scientific use |
|---|---|
| `gunnchos-hardware-industrial-design` | Form-factor / power / antenna integration **constraints** for RQ1/RQ3 |
| `gunnchAI3k` | Local intelligence **workload** and placement/fidelity actions |
| `waike-research-ops` | Education service workload |
| Games + BeatLink + Archive of Life | Latency/QoE/content workloads if imported into a frozen experiment |
| `gunnchos-gpu-nr-baseband-platform` | Optional PHY validation extension (`BLOCKED_GPU` on CPU-only hosts) |
| `gunnchos-emergent-service-intent-protocols` | Optional distributed-intelligence extension (public; not a fourth paper) |
| `gunnchos-research-portal` | Navigation only |

See [RESEARCH_PLAN_ALIGNMENT_REPORT.md](RESEARCH_PLAN_ALIGNMENT_REPORT.md) for gaps versus the canonical narrative.
