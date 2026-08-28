# Faculty evidence freeze — 2026-08-27 (post-A2 refresh 2026-08-28)

Machine-readable: [`artifacts/oulu_readiness_2026_08_27/FACULTY_EVIDENCE_FREEZE.json`](../../artifacts/oulu_readiness_2026_08_27/FACULTY_EVIDENCE_FREEZE.json)

This freeze is for a **Communications Engineering / CWC / 6G Flagship conversation**. It does not require the product ecosystem to be finished. The dissertation is **not** complete.

**Working title (V3).** Resilience-Aware Service Continuity in Heterogeneous 6G Networks: Cross-Layer Orchestration for Resource-Constrained Devices

**No University of Oulu affiliation, supervisor commitment, or standardized/commercial 6G product is claimed.**

Live SHA freeze (accepted `origin/main`, post-A2): 7GC `dc43a56` (#31) · SpectrumX `9060655` (#102; feature `b44357f` on main) · ReadyGary `5698752` · Edge I/O `af57fbd` · NTN `c4215fc` (#28) · WAIKE `8eb2827` · portal `f4155bc`.

Historical pre-A2 freeze (2026-08-27 Stream A): 7GC `4cd7016` · SpectrumX `cef3900` · NTN `9165209` · portal `2a3303d` — retained as historical digital PASS, not live faculty status.

---

## 1. What is the scientific problem?

How should **minimum useful service** be represented and preserved for resource-constrained devices when communication, compute placement, fidelity, and recovery are jointly variable under terrestrial / NTN / backhaul disruption?

## 2. Why is it Communications Engineering?

The object is **wireless service continuity** under heterogeneous access (blockage, outage, TN/NTN fallback, radio-aware control), not an operating-system or game dissertation. Public fit is 6G Flagship Wireless Connectivity and CWC Radio / Networks themes. Official sources are listed in [docs/phd/OULU_FIT.md](../phd/OULU_FIT.md). Personnel names are not proposed as supervisors here.

## 3. What is the proposed contribution?

**Proposed contribution / novelty hypothesis:** a service-continuity formulation that treats minimum useful service as a cross-layer objective and evaluates access, compute placement, fidelity/recovery actions, and TN/NTN fallback through a reproducible instrumented stack. The novelty claim remains to be tested against the focused literature review and supervisor/peer-review feedback.

It is **not** a claim of established novelty, a new standardized PHY, operator NTN performance, or a trained RL policy.

## 4. What is measurable?

- Continuity states: target / degraded / min-useful / failed  
- RQ1: `task_completion_ratio`, `time_above_minimum_useful`, seeds 1..30 (n=30), correct 95% Student-t CIs, paired \(d_z\) where applicable  
- RQ2: service-continuity utility, fidelity/checkpoint costs, thrash, switch/compute cost; Paper II held-out/ablation/domain-shift CIs  
- RQ3: NTN vs terrestrial uptime, min-service, recovery steps; decision regions; `ntn_always_better=false`  
- Host process timing (not proven sub-millisecond edge inference)

## 5. What are the baselines?

| Instrument | Baselines on accepted main |
|---|---|
| SpectrumX | no-adaptation, static, placement-only; **fixed-target-fidelity**, **checkpoint-disabled** |
| ReadyGary | exhaustive / hierarchical / oracle |
| NTN | terrestrial-only, static NTN, fallback, adaptive |
| 7GC | proportional-fair stub + seeded profile bench (n=30) |

## 6. What can be completed fully in simulation / digital twin?

RQ1 seeded profiles and statistical bench; RQ2 Paper II packs **plus** fidelity/checkpoint actions with runtime information-equivalence; RQ3 TN/NTN seeded decision regions with CIs. Post-A2 faculty paths **PASS** on detached accepted main (2026-08-28). Evidence class: `SYNTHETIC_SIM`. That is not physical, independent, or operator validation.

## 7. What physical / test-network work is optional vs later validation?

| Optional for a simulation-first thesis | Validation that would materially strengthen Papers II–III | Product, not thesis |
|---|---|---|
| Shipping EVT silicon | A test-network or measurement transfer campaign for RQ3 (high-value later validation, not a stated CWC defence requirement) | Manufacture, carrier attach, certification, games as products |
| Full Device Quartet | Independent reproduction of the digital packs | |

The V3 plan is structured as a four-year, simulation-first and measurement-grounded programme. Later measurement/test-network access strengthens Papers II–III but does not gate the theoretical core. Final gunnchOS hardware is not the doctoral object. This is the V3 schedule, not a proven completion date.

## 8. Which repositories are research instruments?

| Repo | Role |
|---|---|
| `7gc-digital-twin` | Scenario / digital-twin framework + RQ1 statistical parity |
| `spectrumx-ai-ran-gary` | AI-RAN / cross-layer policy instrument (incl. fidelity + checkpoint) |
| `readygary-6g-beam-selection` | PHY beam / band instrument |
| `ntn-resilience-sim` | TN/NTN disruption instrument + RQ3 statistical parity |
| `edge-io-measurement-node` | Measurement / consent instrument |
| `waike-research-ops` | Human/service workload model |

Narrow product roles: Device Quartet = research form factors; WAIKE = workload model; 7GC = twin; gunnchOS = service-aware middleware; games = optional interactive workloads.

## 9. What evidence exists now?

**Digital (post-A2):** RQ1 / RQ2 = `DIGITAL_REPRODUCIBLE_STRONG_CORE`; RQ3 = `DIGITAL_REPRODUCIBLE_STRONG_CORE_WITH_TRANSFER_PENDING`. Faculty paths re-verified on detached accepted main 2026-08-28. See [ACCEPTED_MAIN_REPRODUCTION.md](ACCEPTED_MAIN_REPRODUCTION.md).

**Physical:** Pixel 6a **install/launch smoke only** — not RF, not spatial accuracy.

## 10. What evidence does not exist?

Calibrated mmWave OTA; NTN operator attach; sim→field transfer test; independent third-party reproduction; student/partner classroom execution; certification; carrier-grade operation; Oulu affiliation; scientifically complete / field-validated dissertation.

## 11. What could Oulu / relevant CWC test-network resources strengthen?

Witnessed test-network interruption, RF/QoS calibration, terrestrial/NTN-capable fallback on real bearers, external reproduction culture, and supervisor narrowing of doctoral scope. This is a resource-fit statement, not a uniqueness or affiliation claim.

## 12. Why can this dissertation finish without shipping hardware?

Because the **scientific claims are about decision regions and continuity policies under stated models**, which are already digitally exercisable. Hardware shipping would strengthen RQ3 transfer; it is not required to pose and bound the three papers if limitations stay honest. The V3 plan remains a four-year staged programme, not a guarantee.

**Digitally implemented now vs doctoral research still open.** Strong synthetic digital cores exist for all three RQs; measurement transfer, independent reproduction, and physical RF remain open doctoral work.

**Faculty outreach recommendation:** `YES_WITH_EXPLICIT_LIMITATIONS`.
