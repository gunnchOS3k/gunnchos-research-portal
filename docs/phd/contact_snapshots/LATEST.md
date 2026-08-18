# Supervisor contact snapshot — 2026-08-18

Generated: 2026-08-18T21:41:01Z  
Generator: `make supervisor-snapshot` (`scripts/supervisor_snapshot.py`)  
**Do not send.** This is a package for owner review.

## Thesis

**Title.** Resilience-Aware Service Continuity in Heterogeneous 6G Networks: Cross-Layer Orchestration for Resource-Constrained Devices

**Affiliation.** NONE — no University of Oulu affiliation, admission, funding, or supervisor commitment

## Research questions

| ID | Question |
|---|---|
| RQ1 | How can representative workloads and four device classes be translated into measurable service-continuity profiles, metrics, and benchmark scenarios? |
| RQ2 | To what extent can joint access, placement, fidelity, caching/checkpointing, and recovery control — informed by radio-aware digital-twin state and uncertainty — improve continuity versus transparent baselines? |
| RQ3 | Under which disruption conditions do terrestrial, local-edge, peer, offline, and NTN fallback modes preserve minimum useful service, and what tradeoffs appear? |

## Conference-paper status

not SUBMITTED; not ACCEPTED; venue-neutral

| Paper | Status | Source of truth |
|---|---|---|
| I / RQ1 | DIGITAL_RESULTS_VALIDATED | 7gc-digital-twin/paper + gunnchos-device-os profiles |
| II / RQ2 | DIGITAL_RESULTS_VALIDATED | spectrumx-ai-ran-gary/paper + readygary-6g-beam-selection |
| III / RQ3 | DIGITAL_RESULTS_VALIDATED | ntn-resilience-sim/paper + edge-io-measurement-node |

Never SUBMITTED / ACCEPTED from this generator.

## Digital manufacturing

DIGITAL packet prepared; DIGITAL_FABRICATION_PASS=FALSE; PHYSICAL_PENDING

## Programme gates

| Gate | Status |
|---|---|
| SUPERVISOR_CONTACT_DIGITAL_READY | **PASS** |
| FULL_RESEARCH_VALIDATION_READY | **PASS** |
| PHYSICAL_REALIZATION_BOUNDARY_READY | **PASS** |
| PIXEL_6A_READY | **PASS** |
| CONTACT_SUPERVISOR_READY | **BLOCKED** |

GPU NR and emergent-protocol repos are **public**. CUDA timings remain `BLOCKED_GPU` without a lab GPU.

## Pixel 6a

- serial `27211JEGR06194`
- adb: `27211JEGR06194         device usb:17825792X product:bluejay model:Pixel_6a device:bluejay transport_id:5`
- adb_authorized: **True**
- PIXEL_6A_READY: **PASS**
- PIXEL_6A_READY=PASS when artifacts show install+launch. Fun/usability stays HUMAN_QA_PENDING. Live adb is recorded separately.

## Unresolved gates

- CONTACT_SUPERVISOR_READY=BLOCKED (owner send / independent repro / HUMAN_QA playtest)
- INDEPENDENT_REPRODUCTION=PENDING
- PHYSICAL_EVT / RF / thermal / battery = PHYSICAL_PENDING
- Pixel 6a digital install+launch executed; HUMAN_QA_PENDING for fun/usability
- GPU NR CUDA timings = BLOCKED_GPU (repo is PUBLIC; missing lab GPU)
- ReadyGary TensorRT = BLOCKED_GPU; sub-ms inference is TARGET not fact
- ReadyGary additive commit add0e47 is AHEAD of already-merged PR #24; this agent did not merge and will not merge

## Sixteen repositories

| Repository | PR | SHA | CI | Mergeable | Reproduce | UML | Local vs PR |
|---|---|---|---|---|---|---|---|
| `gunnchos-device-os` | 121 | `65c33a03fdfc` | PASS | UNKNOWN | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY |  |
| `gunnchos-hardware-industrial-design` | 67 | `5a93e261fdd8` | PASS | UNKNOWN | see REPRODUCIBILITY.md | STRUCTURED_CURRENT_FUTURE_LEGACY |  |
| `archive-of-life-artifact-world` | 32 | `02192669e61d` | PASS | UNKNOWN | see REPRODUCIBILITY.md | STRUCTURED_CURRENT_FUTURE_LEGACY | AHEAD_OF_MERGED_PR |
| `gunnchAI3k` | 42 | `9a659a6400cc` | PASS | UNKNOWN | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY |  |
| `waike-research-ops` | 52 | `554c364aa0ec` | PASS | UNKNOWN | see REPRODUCIBILITY.md | STRUCTURED_CURRENT_FUTURE_LEGACY |  |
| `anime-aggressors` | 78 | `6d3f1fa3617e` | PASS | UNKNOWN | see REPRODUCIBILITY.md | STRUCTURED_CURRENT_FUTURE_LEGACY | AHEAD_OF_MERGED_PR |
| `gunnchos-emergent-service-intent-protocols` | 3 | `7381de141836` | PASS | UNKNOWN | see REPRODUCIBILITY.md | STRUCTURED_CURRENT_FUTURE_LEGACY |  |
| `pedestrian-pursuit` | 19 | `409566d66e5d` | PASS | UNKNOWN | see REPRODUCIBILITY.md | STRUCTURED_CURRENT_FUTURE_LEGACY | AHEAD_OF_MERGED_PR |
| `beatlink-party` | 22 | `dcb5a916a92c` | PASS | UNKNOWN | see REPRODUCIBILITY.md | STRUCTURED_CURRENT_FUTURE_LEGACY | AHEAD_OF_MERGED_PR |
| `edge-io-measurement-node` | 37 | `3c5606751be4` | PASS | UNKNOWN | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY | AHEAD_OF_MERGED_PR |
| `gunnchos-research-portal` | 7 | `f64fd24a96b9` | PASS | UNKNOWN | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY | AHEAD_OF_MERGED_PR |
| `ntn-resilience-sim` | 27 | `f2b48a826a42` | PASS | UNKNOWN | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY |  |
| `7gc-digital-twin` | 30 | `376b6d673ff6` | PASS | UNKNOWN | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY |  |
| `spectrumx-ai-ran-gary` | 100 | `20f40f15753a` | PASS | UNKNOWN | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY | AHEAD_OF_MERGED_PR |
| `gunnchos-gpu-nr-baseband-platform` | 3 | `2a5c483fdeb6` | IN_PROGRESS | UNKNOWN | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY |  |
| `readygary-6g-beam-selection` | 24 | `add0e474b0f2` | PASS | UNKNOWN | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY | AHEAD_OF_MERGED_PR |

## How to regenerate

```bash
make supervisor-snapshot
```
