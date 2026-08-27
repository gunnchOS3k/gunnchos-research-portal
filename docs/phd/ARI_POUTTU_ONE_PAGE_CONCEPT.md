# One-page concept — for discussion with Prof. Ari Pouttu

**Applicant:** Edmund Gunn Jr.  
**Proposed major:** Communications Engineering (ITEE-DP)  
**Working title (V3):** Resilience-Aware Service Continuity in Heterogeneous 6G Networks: Cross-Layer Orchestration for Resource-Constrained Devices  

**Boundary:** No University of Oulu affiliation, funding entitlement, or supervisor commitment is claimed. This page is a fit/scope discussion aid only.

---

## Scientific problem

In heterogeneous 6G-era systems, **connectivity ≠ usable service**. Latency, blockage, congestion, compute placement, energy, privacy, recovery delay, and intermittent terrestrial/NTN access can push a task below its minimum useful operating point even when a link metric looks acceptable.

## Proposed doctoral object

A **resilience-aware service-continuity** framework for four resource-constrained device classes (desk; mobile/docked; local creation/deployment; wearable/body-area). The object is communications-and-computing behaviour under disruption — not product shipping.

**Hypothesis.** A cross-layer controller informed by device state, radio-aware digital-twin context, compute availability, and uncertainty can preserve useful service better than transparent static/local/cloud/fixed-fallback baselines, subject to energy, privacy, and switching-cost constraints. Negative results are accepted when complexity is not justified.

## Three papers

1. **Profiles & benchmark** — translate workloads/device constraints into measurable continuity metrics and scenarios.  
2. **Cross-layer control** — joint access, placement, fidelity/adaptation, caching/checkpointing, and recovery under mobility, blockage, congestion, edge-resource variation, and energy limits.  
3. **Fallback decision regions** — when terrestrial, local-edge, peer/D2D, offline, and NTN modes preserve minimum useful service; performance/energy/privacy/recovery tradeoffs in simulation, emulation, and device-level measurement.

## Why this is Communications Engineering

Dependable heterogeneous wireless systems; experimental/test-network validation; terrestrial/NTN fallback; radio-aware digital twins; reproducible cross-layer evaluation. Vendor tools (e.g. Sionna / optional AI Aerial) are enhancement paths, not theoretical dependencies.

## What already exists (honest)

Accepted-main **digital** instruments and reproduce scripts for twin/profiles, AI-RAN policy comparison, beam/band tables, and TN/NTN disruption sweeps (2026-08-27 freeze). Physical RF, operator NTN, and independent third-party reproduction remain pending. Pixel work is install/launch smoke only.

## Ask (not a company pitch)

Is this a strong Communications Engineering doctoral problem, and how would you **narrow** the radio / test-network / NTN scope into the strongest three-paper dissertation under CWC supervision?

Portfolio entry: `docs/phd/START_HERE_SUPERVISOR.md` in `gunnchos-research-portal` · V3 plan available on request.
