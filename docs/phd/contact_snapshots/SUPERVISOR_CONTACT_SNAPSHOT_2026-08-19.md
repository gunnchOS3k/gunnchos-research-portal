# Supervisor contact snapshot — 2026-08-19

Generated: 2026-08-19T03:27:48Z  
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

## Disposition legend

| State | Meaning |
|---|---|
| ACCEPTED_MAIN | `origin/main` matches `CURRENT_ACCEPTED_MAIN.json` |
| ACCEPTED_MAIN_DRIFT | pin exists but live `origin/main` differs |
| PREVIEW_DRAFT | open draft PR — not accepted-main |

## Pending classes

- **PHYSICAL_PENDING:** hardware EVT / RF / thermal / battery; R6G OTA / carrier / SDR; DIGITAL_FABRICATION_PASS external ballmaps
- **HUMAN_PENDING:** CONTACT_SUPERVISOR_READY owner send; game fun/balance/feel HUMAN_QA; SEVEN_GC_APPRENTICESHIP research overlay; device-os #103 owner supersession/close
- **EXTERNAL_PENDING:** INDEPENDENT_REPRODUCTION; NVIDIA Aerial/AODT/Sionna backends; DOI/PDF pins; GPU NR CUDA timings BLOCKED_GPU

## Preview / draft PRs (not accepted-main)

- `waike-research-ops` PR #53: batch007 EMBEDDED_PROTOTYPING + GUNNCHOS_PRODUCT_LAB
- `gunnchos-7gc-ai-ran-field-kit` PR #88: residual digital closure Phase 0 follow-up
- `gunnchos-device-os` PR #103: OPEN draft CONFLICTING — do not merge; superseded

## Sixteen repositories

| Repository | Disposition | Accepted/main SHA | Merged PR | CI | Reproduce |
|---|---|---|---|---|---|
| `gunnchos-device-os` | ACCEPTED_MAIN | `d5c2d179ae21` | 121 | PASS | make reproduce |
| `gunnchos-hardware-industrial-design` | ACCEPTED_MAIN | `9ee0ef2f688b` | 67 | PASS | see REPRODUCIBILITY.md |
| `archive-of-life-artifact-world` | ACCEPTED_MAIN | `bf479085cee9` | 33 | PASS | see REPRODUCIBILITY.md |
| `gunnchAI3k` | ACCEPTED_MAIN | `d357846810b9` | 43 | PASS | make reproduce |
| `waike-research-ops` | ACCEPTED_MAIN | `491744328596` | 52 | PASS | see REPRODUCIBILITY.md |
| `anime-aggressors` | ACCEPTED_MAIN | `a7d11537625b` | 79 | PASS | see REPRODUCIBILITY.md |
| `gunnchos-emergent-service-intent-protocols` | ACCEPTED_MAIN | `088c5e88e155` | 3 | PASS | see REPRODUCIBILITY.md |
| `pedestrian-pursuit` | ACCEPTED_MAIN | `8f513c2b3cc3` | 20 | PASS | see REPRODUCIBILITY.md |
| `beatlink-party` | ACCEPTED_MAIN | `6e8d1a0461e9` | 23 | PASS | see REPRODUCIBILITY.md |
| `edge-io-measurement-node` | ACCEPTED_MAIN | `af57fbdac857` | 38 | PASS | make reproduce |
| `gunnchos-research-portal` | ACCEPTED_MAIN | `7842ff2e0d1d` | 8 | PASS | make reproduce |
| `ntn-resilience-sim` | ACCEPTED_MAIN | `916520919bea` | 27 | PASS | make reproduce |
| `7gc-digital-twin` | ACCEPTED_MAIN | `4cd70169b35a` | 30 | PASS | make reproduce |
| `spectrumx-ai-ran-gary` | ACCEPTED_MAIN | `cef3900af100` | 101 | PASS | make reproduce |
| `gunnchos-gpu-nr-baseband-platform` | ACCEPTED_MAIN | `3931f51d43b7` | 3 | FAIL | make reproduce |
| `readygary-6g-beam-selection` | ACCEPTED_MAIN | `0e2a79177222` | 26 | FAIL | make reproduce |

## How to regenerate

```bash
make supervisor-snapshot
```
