# Start here — prospective supervisor

This is the **canonical ten-minute front door** for a Communications Engineering / 6G Flagship doctoral conversation.

It is **not** an application, a request for a meeting, or a claim of University of Oulu affiliation, funding, or supervisor interest.

Portfolio control plane: this repository (`gunnchos-research-portal`).  
Product/ecosystem navigation for non-research audiences remains in [START_HERE.md](../../START_HERE.md).

---

## 30-second view

**Working title.** Resilience-Aware Service Continuity in Heterogeneous 6G Networks: Cross-Layer Orchestration for Resource-Constrained Devices

**Thesis (one sentence).**  
Edmund Gunn Jr. studies how heterogeneous 6G-era network and compute resources can preserve **minimum useful service** for resource-constrained devices when a radio link being “up” is not enough.

**Why it matters.**  
Latency, jitter, blockage, handover, backhaul failure, compute placement, energy, and NTN intermittency can each drop a human-facing service below its useful operating point even while connectivity metrics look acceptable.

**Three primary research questions (article-based dissertation).**

| Paper | Canonical RQ (V3) |
|---|---|
| **RQ1 / Paper I** | How can representative workloads and the constraints of four resource-constrained device classes be translated into measurable service-continuity profiles, metrics, and benchmark scenarios? |
| **RQ2 / Paper II** | To what extent can joint access selection, computation placement, fidelity/model adaptation, caching/checkpointing, and recovery control - informed by radio-aware digital-twin state and uncertainty - improve service-continuity utility under mobility, blockage, congestion, edge-resource variation, and energy constraints? |
| **RQ3 / Paper III** | Under which disruption conditions do terrestrial, local-edge, peer/device-to-device, offline, and NTN fallback modes preserve minimum useful service, and what performance, energy, privacy, and recovery tradeoffs arise in simulation, emulation, and device-level measurements? |

**Research status (honest).**  
The experimental computing/communications **infrastructure is implemented and digitally exercisable**. Independently reproduced results and physical RF/lab measurements remain **pending**. GPU NR and emergent-intent repos are **public**; CUDA timings stay `BLOCKED_GPU` without a lab GPU. See [PORTFOLIO_READINESS_DASHBOARD.md](PORTFOLIO_READINESS_DASHBOARD.md).

**Research plan (canonical V3).** [THESIS_AT_A_GLANCE_V3.md](THESIS_AT_A_GLANCE_V3.md) · [THESIS_AT_A_GLANCE.md](THESIS_AT_A_GLANCE.md) · [RESEARCH_SCOPE_AND_BOUNDARIES.md](RESEARCH_SCOPE_AND_BOUNDARIES.md) · [PUBLICATION_PIPELINE.md](PUBLICATION_PIPELINE.md) · [contact_package/](contact_package/)

**Ari Pouttu outreach package (draft; no commitment claimed).** [ARI_POUTTU_ONE_PAGE_CONCEPT.md](ARI_POUTTU_ONE_PAGE_CONCEPT.md) · [ARI_POUTTU_FIT_CURRENT.md](ARI_POUTTU_FIT_CURRENT.md) · [ARI_FIRST_MEETING_PACKET.md](ARI_FIRST_MEETING_PACKET.md) · [ARI_POUTTU_OUTREACH_EMAIL.md](ARI_POUTTU_OUTREACH_EMAIL.md) (do not send) · [OULU_APPLICATION_PACKAGE_STATUS_V3.md](OULU_APPLICATION_PACKAGE_STATUS_V3.md)

**Snapshot.** [contact_snapshots/LATEST.md](contact_snapshots/LATEST.md) (regenerate with `make supervisor-snapshot`)

**Core evidence map.** [FACULTY_EVIDENCE_MAP_V3.md](FACULTY_EVIDENCE_MAP_V3.md) · [RQ_TO_REPO_EVIDENCE_MAP.md](RQ_TO_REPO_EVIDENCE_MAP.md) · **2026-08-27 faculty freeze:** [../oulu/FACULTY_EVIDENCE_FREEZE.md](../oulu/FACULTY_EVIDENCE_FREEZE.md)

---

## 2-minute view — experimental stack

The doctoral object is **one** communications/computing control problem. The sixteen repositories are **layers of an experimental system**, not sixteen dissertation topics.

```text
PHY / baseband capability          gunnchos-gpu-nr-baseband-platform
        ↓
AI-RAN / beam policy               spectrumx-ai-ran-gary · readygary-6g-beam-selection
        ↓
Radio-aware digital twin           7gc-digital-twin
        ↓
TN / NTN resilience                ntn-resilience-sim
        ↓
Device / edge state                gunnchos-device-os · edge-io-measurement-node
        ↓
Minimum-useful service             Service-Continuity Profile Model (RQ1)
        ↓
Human / application workloads      WAIKE · gunnchAI · games · Archive of Life · BeatLink
```

Full map: [EXPERIMENTAL_SYSTEM_MAP.md](EXPERIMENTAL_SYSTEM_MAP.md)

---

## 10-minute view

Follow [SUPERVISOR_10_MINUTE_PATH.md](SUPERVISOR_10_MINUTE_PATH.md) in order:

```text
30 seconds  → thesis + problem + 3 RQs
2 minutes   → three-paper architecture + evidence map
5 minutes   → reproducibility / experiment entrypoints
10 minutes  → selected results, limitations, Oulu fit, open questions
```

Supporting products appear only after the dissertation core is clear.  

---

## What a laboratory would add

This portfolio is offered as **working research infrastructure**. Independent validation, RF/test-network measurement, and scientific narrowing of the hypothesis are the work of a doctoral environment — not something this software pass can truthfully complete.

Contact/release gates: [CONTACT_SUPERVISOR_RELEASE_GATE.md](CONTACT_SUPERVISOR_RELEASE_GATE.md)
