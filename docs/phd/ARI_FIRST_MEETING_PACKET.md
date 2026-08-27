# First meeting packet — Prof. Ari Pouttu

**Use with:** `ARI_POUTTU_ONE_PAGE_CONCEPT.md`, `THESIS_AT_A_GLANCE_V3.md`, `FACULTY_EVIDENCE_MAP_V3.md`  
**Boundary:** no affiliation, funding, or commitment claims.

---

## 60-second verbal pitch

I study how heterogeneous 6G-era networks and compute can preserve **minimum useful service** for resource-constrained devices when a radio link being up is not enough. The dissertation is three papers: continuity profiles and benchmarks; joint access/placement/fidelity/checkpoint/recovery control informed by radio-aware digital-twin state; and TN/local-edge/peer/offline/NTN fallback decision regions with measurement grounding. I already have reproducible digital instruments and honest gaps on physical RF and missing fidelity/checkpoint actions. I am asking how you would narrow the radio and test-network scope into the strongest CWC dissertation — not for a company pitch or assumed funding.

## 5-minute explanation

1. **Problem.** Connectivity metrics can look fine while tasks fail on latency, blockage, compute placement, energy, privacy, or recovery delay.  
2. **Gap.** Edge offloading, QoE, slicing, twin, and NTN literatures are often evaluated separately from a task’s minimum useful operating point under device constraints.  
3. **Model.** Constrained stochastic control over service/device/network/compute state; actions span access, placement, fidelity, checkpoint/sync, recovery.  
4. **Three papers.** RQ1 profiles/benchmark → RQ2 controller vs baselines → RQ3 fallback decision regions + measurements.  
5. **Instruments.** 7GC twin; SpectrumX policy; ReadyGary beam; NTN sim; Edge I/O schema — accepted-main digital PASS 2026-08-27.  
6. **Feasibility.** Simulation-first Year 1; measurement/test-network strengthens II–III; vendor tools optional.

## Questions for Ari

1. Where would you narrow the radio / test-network / NTN scope?
2. Is minimum useful service sufficiently Communications Engineering–centred?
3. Which validation path makes Paper III strongest?
4. Which part needs deeper PHY / RRM theory?
5. Which co-supervision expertise would you add (if any)?

## Questions Ari may ask — prepared answers

| Question | Honest answer |
|---|---|
| Novelty? | Hypothesis: minimum useful service as first-class cross-layer objective with joint device/radio/compute/fallback evaluation. Not claimed as established novelty. |
| Why not just QoE? | QoE is related; the object is **continuity under disruption and device constraints**, including offline/NTN fallback and recovery cost. |
| Why not just slicing? | Slicing allocates network resources; this problem jointly decides access, placement, fidelity, and recovery for constrained devices. |
| Why not just MEC offloading? | Placement is one action among access, fidelity, checkpoint, and fallback modes. |
| Why digital twin? | Radio-aware state and uncertainty for control — not twin-as-product; gains must beat information-equivalent baselines. |
| Why NTN? | One fallback family among terrestrial/edge/peer/offline; V3 rejects “NTN always better” without decision regions. |
| Why four device classes? | Repeatable constraint envelopes for Communications Engineering evaluation — not four product dissertations. |
| State / action / objective? | \(s_t=(q,d,n,c)\); actions access/placement/fidelity/checkpoint/recovery; maximize continuity under constraints. |
| Baselines? | No-adaptation / static / placement-only; exhaustive/hierarchical/oracle beams; terrestrial-only / static NTN / fixed fallback. |
| If AI loses to rules? | Negative result; keep simpler policy; document cost. Current Paper II path is rule-based, not RL. |
| Without Oulu infrastructure? | Theoretical model, open benchmark, synthetic/emulation studies. |
| What needs ethics approval? | Initial public/synthetic path; human/field/restricted data require supervisor-guided permits. |
| What is already implemented? | Digital reproduce PASS on twin, AI-RAN, beam, NTN, Edge I/O schema (2026-08-27). Physical RF pending. |
