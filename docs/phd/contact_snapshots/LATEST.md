# Supervisor contact snapshot — 2026-08-18

Generated: 2026-08-18T18:13:28Z  
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
| I / RQ1 | DIGITAL_RESULTS_AVAILABLE | 7gc-digital-twin/paper + gunnchos-device-os profiles |
| II / RQ2 | EXPERIMENT_IMPLEMENTATION | spectrumx-ai-ran-gary/paper + readygary-6g-beam-selection |
| III / RQ3 | DIGITAL_RESULTS_AVAILABLE | ntn-resilience-sim/paper + edge-io-measurement-node |

Never SUBMITTED / ACCEPTED from this generator.

## Digital manufacturing

DIGITAL packet prepared; DIGITAL_FABRICATION_PASS=FALSE; PHYSICAL_PENDING

## Pixel 6a

- serial `27211JEGR06194`
- adb: `27211JEGR06194         device usb:17825792X product:bluejay model:Pixel_6a device:bluejay transport_id:1`
- adb_authorized: **True**
- PIXEL_6A_READY: **BLOCKED**
- adb authorized is not PIXEL_6A_READY; signed acceptance session still PHYSICAL_PENDING

## Unresolved gates

- CONTACT_SUPERVISOR_READY=BLOCKED
- INDEPENDENT_REPRODUCTION=PENDING
- PHYSICAL_EVT / RF / thermal / battery = PHYSICAL_PENDING
- two private repos visibility = EXTERNAL_PENDING
- Pixel 6a signed acceptance = PHYSICAL_PENDING
- GPU NR CUDA timings = BLOCKED_GPU

## Sixteen repositories

| Repository | PR | SHA | CI | Mergeable | Reproduce | UML |
|---|---|---|---|---|---|---|
| `gunnchos-device-os` | 121 | `65c33a03fdfc` | PASS | MERGEABLE | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `gunnchos-hardware-industrial-design` | 67 | `68630a04c6d3` | PASS | MERGEABLE | see REPRODUCIBILITY.md | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `archive-of-life-artifact-world` | 32 | `6419a35d1341` | PASS | MERGEABLE | UNDOCUMENTED | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `gunnchAI3k` | 42 | `9a659a6400cc` | PASS | MERGEABLE | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `waike-research-ops` | 52 | `554c364aa0ec` | PASS | MERGEABLE | see REPRODUCIBILITY.md | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `anime-aggressors` | 78 | `050878b5e317` | PASS | MERGEABLE | UNDOCUMENTED | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `gunnchos-emergent-service-intent-protocols` | 3 | `b703408121c3` | PASS | MERGEABLE | see REPRODUCIBILITY.md | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `pedestrian-pursuit` | 19 | `86d981c0e975` | PASS | MERGEABLE | UNDOCUMENTED | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `beatlink-party` | 22 | `206cb8501180` | PASS | MERGEABLE | UNDOCUMENTED | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `edge-io-measurement-node` | 37 | `009f227d3257` | PASS | MERGEABLE | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `gunnchos-research-portal` | 7 | `9ea2fd69e950` | PASS | MERGEABLE | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `ntn-resilience-sim` | 27 | `e7ed8504e1e5` | PASS | MERGEABLE | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `7gc-digital-twin` | 30 | `86996b82e778` | PASS | MERGEABLE | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `spectrumx-ai-ran-gary` | 100 | `4ac16c4a1e8f` | PASS | MERGEABLE | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `gunnchos-gpu-nr-baseband-platform` | 3 | `60c6ea5f29de` | IN_PROGRESS | MERGEABLE | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY |
| `readygary-6g-beam-selection` | 24 | `5ef9a4a65b3c` | PASS | MERGEABLE | make reproduce | STRUCTURED_CURRENT_FUTURE_LEGACY |

## How to regenerate

```bash
make supervisor-snapshot
```
