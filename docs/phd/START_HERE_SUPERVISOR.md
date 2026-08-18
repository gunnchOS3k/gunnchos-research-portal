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

| Paper | Question |
|---|---|
| **RQ1 / Paper I** | How can representative workloads and four device classes be translated into measurable service-continuity profiles, metrics, and benchmark scenarios? |
| **RQ2 / Paper II** | To what extent can joint access, placement, fidelity, caching/checkpointing, and recovery control — informed by radio-aware digital-twin state and uncertainty — improve continuity versus transparent baselines? |
| **RQ3 / Paper III** | Under which disruption conditions do terrestrial, local-edge, peer, offline, and NTN fallback modes preserve minimum useful service, and what tradeoffs appear? |

**Research status (honest).**  
The experimental computing/communications **infrastructure is implemented and digitally exercisable**. Independently reproduced results, physical RF/lab measurements, and supervisor-visible access to two private repos remain **pending**. See [PORTFOLIO_READINESS_DASHBOARD.md](PORTFOLIO_READINESS_DASHBOARD.md).

**Research plan (canonical).** [THESIS_AT_A_GLANCE.md](THESIS_AT_A_GLANCE.md) · [RESEARCH_SCOPE_AND_BOUNDARIES.md](RESEARCH_SCOPE_AND_BOUNDARIES.md)

**Core evidence map.** [RQ_TO_REPO_EVIDENCE_MAP.md](RQ_TO_REPO_EVIDENCE_MAP.md)

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

1. Thesis and constrained-control formulation  
2. RQ1 evidence (`gunnchos-device-os`, `7gc-digital-twin`)  
3. RQ2 evidence (`spectrumx-ai-ran-gary`, `readygary-6g-beam-selection`)  
4. RQ3 evidence (`ntn-resilience-sim`, `edge-io-measurement-node`)  
5. Reproducibility commands  
6. Evidence boundaries (what is simulated vs measured)  
7. Supporting device/application ecosystem  
8. Oulu / 6G Flagship **fit without affiliation**  
9. Open doctoral questions that require CWC / test-network resources  

---

## What a laboratory would add

This portfolio is offered as **working research infrastructure**. Independent validation, RF/test-network measurement, and scientific narrowing of the hypothesis are the work of a doctoral environment — not something this software pass can truthfully complete.

Contact/release gates: [CONTACT_SUPERVISOR_RELEASE_GATE.md](CONTACT_SUPERVISOR_RELEASE_GATE.md)
