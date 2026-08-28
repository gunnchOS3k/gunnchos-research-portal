# Thesis at a glance (V3)

**Audience:** prospective Communications Engineering / CWC faculty (≈2 minutes).  
**No University of Oulu affiliation, funding, or supervisor commitment is claimed.**  
**Dissertation is not complete.**

## 1. Problem

A radio link can be “up” while a human-facing service falls below its **minimum useful operating point** because of latency, loss, blockage, congestion, compute placement, energy, privacy, recovery delay, or intermittent terrestrial/NTN availability.

## 2. Central hypothesis

A service-aware cross-layer controller informed by device capabilities, radio-aware digital-twin state, compute availability, and calibrated uncertainty can improve time above minimum-useful service and task completion versus transparent static/reference baselines — subject to reliability, energy, privacy, and fairness constraints. Claims are rejected when gains vanish under held-out conditions or realistic switching/compute cost.

## 3. Formulation (short)

Constrained stochastic control: observe \(s_t=(q_t,d_t,n_t,c_t)\); choose action \(a_t\) over access, placement, fidelity, caching/checkpointing, sync, or recovery; maximize continuity subject to constraints.

## 4. Research questions (exact V3 wording)

1. **RQ1.** How can representative workloads and the constraints of four resource-constrained device classes be translated into measurable service-continuity profiles, metrics, and benchmark scenarios?
2. **RQ2.** To what extent can joint access selection, computation placement, fidelity/model adaptation, caching/checkpointing, and recovery control - informed by radio-aware digital-twin state and uncertainty - improve service-continuity utility under mobility, blockage, congestion, edge-resource variation, and energy constraints?
3. **RQ3.** Under which disruption conditions do terrestrial, local-edge, peer/device-to-device, offline, and NTN fallback modes preserve minimum useful service, and what performance, energy, privacy, and recovery tradeoffs arise in simulation, emulation, and device-level measurements?

## 5. Three-paper structure

| Paper | Focus |
|---|---|
| I / RQ1 | Continuity profiles + open benchmark |
| II / RQ2 | Digital-twin-informed cross-layer control vs baselines |
| III / RQ3 | TN/NTN/edge/offline fallback decision regions + measurement grounding |

## 6. Primary metrics

Task-completion ratio; time above minimum-useful threshold; outage/recovery time; QoE/continuity violations; energy/privacy proxies; switching/compute cost; fairness where applicable.

## 7. Baseline philosophy

Transparent rule-based, optimization, and oracle/reference policies first. Learning methods only if justified. Negative results are scientific outcomes.

## 8. Feasibility stance

**Simulation-first and measurement-grounded.** Year-1 theoretical/benchmark core does not require vendor GPU tools or field access. Later lab/test-network work strengthens Papers II–III.

## 9. Already implemented (accepted-main digital, post-A2 2026-08-28)

| RQ | Digital status | What exists |
|---|---|---|
| RQ1 | STRONG_CORE | Profiles + n=30 seeded stats with correct 95% t-CIs (`SYNTHETIC_SIM`) |
| RQ2 | STRONG_CORE | Paper II packs + fidelity/checkpoint actions + runtime info-equivalence (`SYNTHETIC_SIM`) |
| RQ3 | STRONG_CORE + transfer pending | TN/NTN decision regions + n=30 CIs; `ntn_always_better=false` (`SYNTHETIC_SIM`) |

See `FACULTY_EVIDENCE_MAP_V3.md`.

## 10. Remaining doctoral validation work

Sim→measurement transfer; physical RF/QoS; local-edge/peer in seeded Paper-III engine; independent reproduction; supervisor narrowing of scope. Pixel evidence = install/launch smoke only. Do not claim app persistence, production RAN, trained RL, or standardized 6G.
