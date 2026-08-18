# Thesis at a glance

**Working title.** Resilience-Aware Service Continuity in Heterogeneous 6G Networks: Cross-Layer Orchestration for Resource-Constrained Devices

**Programme positioning.** Proposed major: Communications Engineering. Intended environment: University of Oulu / Centre for Wireless Communications (CWC) / 6G Flagship research. Article-based dissertation. Simulation-first and measurement-grounded. Vendor tools may enhance validation; they are not required for the theoretical core.

This document does **not** claim admission, affiliation, funding, or supervisor commitment.

## Scientific problem

A radio connection being available does not guarantee that a human-facing service remains usable.

A service can fall below its minimum useful operating point because of latency, jitter, packet loss, congestion, handover interruption, blockage, backhaul failure, compute placement, compute contention, battery/energy limits, thermal limits, privacy/data-locality constraints, model/runtime cost, recovery time, or intermittent terrestrial/NTN availability.

The research asks how heterogeneous network and compute resources can preserve **minimum useful service**, rather than optimizing only best-case throughput.

## Four research device classes

These are research form factors, not commercial SKUs:

1. sustained desk compute  
2. mobile/docked compute  
3. local creation/deployment compute  
4. wearable/body-area sensing  

They correspond naturally to the existing device ecosystem. The PhD concerns their communications/computing behaviour.

## Central hypothesis

A service-aware cross-layer controller informed by service requirements, device capabilities, network/radio state, radio-aware digital-twin state, compute availability, and uncertainty can increase successful task completion and time above the minimum-useful-service threshold, subject to reliability, energy, privacy/data-locality, fairness, compute, switching, and recovery constraints, relative to transparent static/reference baselines.

The implementation must retain the scientific possibility that this hypothesis is **not supported**. If apparent gains disappear under held-out conditions, information-equivalent comparisons, realistic switching cost, realistic computation cost, uncertainty, domain shift, or stronger simple baselines, the corresponding claim must be rejected or narrowed. Negative results are legitimate research results.

## Formal research formulation

Constrained stochastic control. At time `t`, the controller observes state approximately represented by:

```text
state = service + device + network + compute context
```

and may choose actions including access/bearer selection, compute placement, fidelity/model-size adaptation, caching, checkpointing, delayed synchronization, peer/local-edge use, safe offline operation, recovery, NTN fallback, and beam/resource action when the experiment supports it.

Transparent rule-based, optimization, MPC-style, static, and oracle/reference approaches must precede or accompany learning-based methods. **AI is never automatically the contribution.**

## Primary outcomes

- successful task-completion ratio  
- time above minimum-useful-service threshold  

Secondary outcomes may include outage duration, recovery time, QoE violations, latency, jitter, packet loss, throughput, reliability, handover interruption, compute completion time, edge response time, energy, thermal state where measured, privacy/policy violations, and switching cost.

If a composite continuity-utility metric is used, weights, normalization, raw components, and sensitivity to weights must remain visible.

## Three papers only

| Paper | Primary repositories |
|---|---|
| RQ1 / Paper I — profiles, metrics, benchmarks | `gunnchos-device-os`, `7gc-digital-twin` |
| RQ2 / Paper II — joint control with twin state | `spectrumx-ai-ran-gary`, `readygary-6g-beam-selection` |
| RQ3 / Paper III — disruption/fallback tradeoffs | `ntn-resilience-sim`, `edge-io-measurement-node` |

Supporting products (hardware, games, WAIKE, gunnchAI, GPU NR, emergent protocols) demonstrate experimental capability. They become dissertation evidence **only** when a frozen experiment uses them to answer RQ1–RQ3.

See [RESEARCH_SCOPE_AND_BOUNDARIES.md](RESEARCH_SCOPE_AND_BOUNDARIES.md) and [RQ_TO_REPO_EVIDENCE_MAP.md](RQ_TO_REPO_EVIDENCE_MAP.md).
