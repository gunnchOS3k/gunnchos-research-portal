# Supervisor contact snapshot — 2026-08-19

Generated: 2026-08-19T20:52:44Z  
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

## Accepted-main digital capability (Baseline V2)

**Not ecosystem completion.** Control-plane readiness ≠ shipping / certification / field validation.

| Metric | Count | Meaning |
|---|---|---|
| DIGITAL_IMPLEMENTATION_COMPLETE | 7 | Digitally complete on accepted main |
| DIGITALLY_VERIFIED | 32 | Reproducible digital verification |
| DIGITAL_IMPLEMENTATION_OPEN | 136 | Still needs digital engineering |
| DIGITAL_VALIDATION_OPEN | 19 | Implementation exists; verification open |
| EVIDENCE_MAPPING_OPEN | 0 | Evidence mapping gaps |

Authoritative worklists (do not execute from portal): field-kit `program/digital_ecosystem_baseline_v2/NEXT_DIGITAL_IMPLEMENTATION_WORK.json` (136 items), `NEXT_DIGITAL_VALIDATION_WORK.json` (19 items), `NON_DIGITAL_PENDING_REGISTER.json`.

## Non-digital pending dimensions

| Dimension | Count |
|---|---|
| HUMAN_PENDING | 88 |
| PHYSICAL_PENDING | 308 |
| EXTERNAL_PENDING | 55 |
| STANDARD_PENDING | 7 |
| CERTIFICATION_PENDING | 15 |
| CARRIER_PENDING | 102 |
| VENDOR_PENDING | 18 |
| OWNER_DECISION_PENDING | 4 |

CI PASS ≠ physical validation. Synthetic/simulation ≠ field measurement.

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
- adb: `27211JEGR06194         unauthorized usb:17825792X transport_id:10`
- adb_authorized: **False**
- PIXEL_6A_READY: **PASS**
- PIXEL_6A_READY=PASS when artifacts show install+launch. Fun/usability stays HUMAN_QA_PENDING. Live adb is recorded separately.

## Unresolved gates

- CONTACT_SUPERVISOR_READY=BLOCKED (owner send / independent repro / HUMAN_QA playtest)
- INDEPENDENT_REPRODUCTION=PENDING
- PHYSICAL_EVT / RF / thermal / battery = PHYSICAL_PENDING
- Pixel 6a digital install+launch executed; HUMAN_QA_PENDING for fun/usability
- GPU NR CUDA timings = BLOCKED_GPU (repo is PUBLIC; missing lab GPU)
- ReadyGary TensorRT = BLOCKED_GPU; sub-ms inference is TARGET not fact
- DIGITAL_IMPLEMENTATION_OPEN=136 — see field-kit Baseline V2
- DIGITAL_VALIDATION_OPEN=19 — see field-kit Baseline V2

## Disposition legend

| State | Meaning |
|---|---|
| ACCEPTED_MAIN | `origin/main` matches `B4_ACCEPTED_MAIN_SHA_FREEZE.json` |
| ACCEPTED_MAIN_DRIFT | pin exists but live `origin/main` differs |

## Pending classes

- **PHYSICAL_PENDING:** hardware EVT / RF / thermal / battery; R6G OTA / carrier / SDR; DIGITAL_FABRICATION_PASS external ballmaps
- **HUMAN_PENDING:** CONTACT_SUPERVISOR_READY owner send; game fun/balance/feel HUMAN_QA; SEVEN_GC_APPRENTICESHIP research overlay
- **EXTERNAL_PENDING:** INDEPENDENT_REPRODUCTION; NVIDIA Aerial/AODT/Sionna backends; DOI/PDF pins; GPU NR CUDA timings BLOCKED_GPU

## Accepted-main convergence (merged / closed — not open drafts)

- `gunnchos-7gc-ai-ran-field-kit` PR #89: **MERGED** — Baseline V2 B.3 precision/provenance correction
- `gunnchos-7gc-ai-ran-field-kit` PR #90: **MERGED** — Baseline V2 B.4.1 evidence-mapping convergence (accepted-main SoT)
- `waike-research-ops` PR #53: **MERGED** — batch007 EMBEDDED_PROTOTYPING + GUNNCHOS_PRODUCT_LAB
- `gunnchos-7gc-ai-ran-field-kit` PR #88: **MERGED** — residual digital closure Phase 0 follow-up
- `gunnchos-device-os` PR #103: **CLOSED** — SUPERSEDED — do not merge; replaced by #108/#116 lineage on accepted main

B4 accepted-main SHA freeze: **17** repos — see `artifacts/baseline_v2/B4_ACCEPTED_MAIN_SHA_FREEZE.json`.

## Sixteen repositories

| Repository | Disposition | origin/main SHA | Merged PR | CI | Reproduce |
|---|---|---|---|---|---|
| `gunnchos-device-os` | ACCEPTED_MAIN | `b0b087681085` | 122 | PASS | make reproduce |
| `gunnchos-hardware-industrial-design` | ACCEPTED_MAIN | `9ee0ef2f688b` | 67 | PASS | see REPRODUCIBILITY.md |
| `archive-of-life-artifact-world` | ACCEPTED_MAIN | `bf479085cee9` | 33 | PASS | see REPRODUCIBILITY.md |
| `gunnchAI3k` | ACCEPTED_MAIN | `d357846810b9` | 43 | PASS | make reproduce |
| `waike-research-ops` | ACCEPTED_MAIN | `5d416c09164c` | 54 | PASS | see REPRODUCIBILITY.md |
| `anime-aggressors` | ACCEPTED_MAIN | `a7d11537625b` | 79 | PASS | see REPRODUCIBILITY.md |
| `gunnchos-emergent-service-intent-protocols` | ACCEPTED_MAIN | `088c5e88e155` | 3 | PASS | see REPRODUCIBILITY.md |
| `pedestrian-pursuit` | ACCEPTED_MAIN | `8f513c2b3cc3` | 20 | PASS | see REPRODUCIBILITY.md |
| `beatlink-party` | ACCEPTED_MAIN | `6e8d1a0461e9` | 23 | PASS | see REPRODUCIBILITY.md |
| `edge-io-measurement-node` | ACCEPTED_MAIN | `af57fbdac857` | 38 | PASS | make reproduce |
| `gunnchos-research-portal` | ACCEPTED_MAIN | `e60705b8b3cd` | 9 | PASS | make reproduce |
| `ntn-resilience-sim` | ACCEPTED_MAIN | `916520919bea` | 27 | PASS | make reproduce |
| `7gc-digital-twin` | ACCEPTED_MAIN | `4cd70169b35a` | 30 | PASS | make reproduce |
| `spectrumx-ai-ran-gary` | ACCEPTED_MAIN | `cef3900af100` | 101 | PASS | make reproduce |
| `gunnchos-gpu-nr-baseband-platform` | ACCEPTED_MAIN | `3931f51d43b7` | 3 | PASS | make reproduce |
| `readygary-6g-beam-selection` | ACCEPTED_MAIN | `569875224db7` | 27 | PASS | make reproduce |

## How to regenerate

```bash
make supervisor-snapshot
```
