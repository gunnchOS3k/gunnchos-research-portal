# Publication pipeline (owner-controlled)

**Do not send, submit, or contact venues from this repository.** This file is a map.

Canonical thesis: *Resilience-Aware Service Continuity in Heterogeneous 6G Networks: Cross-Layer Orchestration for Resource-Constrained Devices*.

Exactly **three** conference manuscripts (article-based dissertation). Games, WAIKE, gunnchAI, GPU NR, and hardware EVT are experimental capability — not extra papers — unless a frozen experiment imports them into RQ1–RQ3.

## Status vocabulary (manuscripts)

`MANUSCRIPT_SCAFFOLD` → `EXPERIMENT_IMPLEMENTATION` → `DIGITAL_RESULTS_AVAILABLE` → `DIGITAL_RESULTS_VALIDATED` → `INDEPENDENT_REPRODUCTION_PENDING` → `MEASUREMENT_PENDING` → `CONFERENCE_RC` → `SUBMISSION_READY` → `SUBMITTED` → `ACCEPTED`

This programme **never** sets `SUBMITTED` or `ACCEPTED`. A PDF that looks camera-ready while results are pending must carry an explicit `RESULT_PENDING` banner.

## Three papers

| Paper | Working title | SoT (do not duplicate) | Portal index | Status now |
|---|---|---|---|---|
| I / RQ1 | Minimum-Useful-Service Continuity Benchmarking for Resource-Constrained Edge Devices in Heterogeneous Networks | `7gc-digital-twin/paper/` + device-os profiles | [paper1_service_continuity](../research_manuscripts/paper1_service_continuity/README.md) | `DIGITAL_RESULTS_VALIDATED` (`SYNTHETIC_SIM`) |
| II / RQ2 | Radio-Aware Digital-Twin-Informed Cross-Layer Orchestration for Service Continuity | `spectrumx-ai-ran-gary/paper/` + ReadyGary | [paper2_cross_layer_orchestration](../research_manuscripts/paper2_cross_layer_orchestration/README.md) | `DIGITAL_RESULTS_VALIDATED` |
| III / RQ3 | Decision Boundaries for Terrestrial, Edge, Peer, Offline, and NTN Fallback Under Compound Service Disruptions | `ntn-resilience-sim/paper/` + Edge I/O | [paper3_tn_ntn_resilience](../research_manuscripts/paper3_tn_ntn_resilience/README.md) | `DIGITAL_RESULTS_VALIDATED` (`SYNTHETIC_SIM`) |

Venue matrix (deadlines **not** claimed unless verified): [VENUE_READINESS_MATRIX.md](../research_manuscripts/VENUE_READINESS_MATRIX.md).

## Pipeline steps (owner)

1. Freeze pre-registration YAML in the SoT repo.  
2. Run digital experiments (`make paper-reproduce` in SoT).  
3. Generate figures/tables from code only.  
4. Citation audit (no placeholder `@misc{...todo}`).  
5. Independent reproduction packet (external human).  
6. Measurement / lab if the claim requires it.  
7. Owner picks venue from the matrix after CFP verification.  
8. Owner submits. Cursor does not.

## Cross-repo scientific pipeline

```text
workload profile → device constraints → radio → compute → twin → orchestrator → fallback → min-useful outcome
```

Implemented as repo layers, not a single binary: device-os profiles, 7GC twin scenarios, SpectrumX/ReadyGary radio policy, NTN fallback, Edge I/O measurement contracts.
