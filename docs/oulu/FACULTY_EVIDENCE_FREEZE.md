# Faculty evidence freeze — 2026-08-27

Machine-readable: [`artifacts/oulu_readiness_2026_08_27/FACULTY_EVIDENCE_FREEZE.json`](../../artifacts/oulu_readiness_2026_08_27/FACULTY_EVIDENCE_FREEZE.json)

This freeze is for a **Communications Engineering / CWC / 6G Flagship conversation**. It does not require the product ecosystem to be finished.

**No University of Oulu affiliation, supervisor commitment, or standardized/commercial 6G product is claimed.**

Live SHA freeze: 7GC `4cd7016` · SpectrumX `cef3900` · ReadyGary `5698752` · Edge I/O `af57fbd` · NTN `9165209` · WAIKE `8eb2827` · portal `2a3303d`.

---

## 1. What is the scientific problem?

How should **minimum useful service** be represented and preserved for resource-constrained devices when communication, compute placement, fidelity, and recovery are jointly variable under terrestrial / NTN / backhaul disruption?

## 2. Why is it Communications Engineering?

The object is **wireless service continuity** under heterogeneous access (blockage, outage, TN/NTN fallback, radio-aware control), not an operating-system or game dissertation. Public fit is 6G Flagship Wireless Connectivity and CWC Radio / Networks themes. Official sources are listed in [docs/phd/OULU_FIT.md](../phd/OULU_FIT.md). Personnel names are not proposed as supervisors here.

## 3. What is novel?

A **cross-layer continuity** formulation (access × placement × degraded/offline modes) instrumented across a site-aware digital twin, an AI-RAN policy harness, a beam-selection benchmark, and a TN/NTN disruption simulator, with explicit evidence-class labels. Novelty is the problem + instrumented stack. It is **not** a claim of a new standardized PHY, operator NTN performance, or trained RL policy.

## 4. What is measurable?

- Continuity states: target / degraded / min-useful / failed  
- Policy utility, fairness, energy proxies, switch cost, `compute_time_ms`  
- Beam top-k and dB-vs-oracle (`SYNTHETIC_SIM`)  
- NTN vs terrestrial uptime, min-service, recovery steps  
- Paper II seed means and 95% t-CIs  
- Host process timing (not proven sub-millisecond edge inference)

## 5. What are the baselines?

| Instrument | Baselines on accepted main |
|---|---|
| SpectrumX | no-adaptation, static, placement-only (rule-based controller vs these) |
| ReadyGary | exhaustive / hierarchical / oracle |
| NTN | terrestrial-only, static NTN, fallback, adaptive |
| 7GC | proportional-fair stub (weaker than Paper II) |

## 6. What can be completed fully in simulation / digital twin?

RQ1 scenario and profile generation; RQ2 synthetic policy comparison and FR2/Sub-6/dual-band beam tables; RQ3 decision regions under documented assumptions; Paper II ablations and domain shift. All of this was **re-run PASS** on 2026-08-27 from `origin/main`.

## 7. What physical / test-network work is optional vs thesis-critical?

| Optional for a simulation-first thesis | Strongly expected for a CWC-style defence | Product, not thesis |
|---|---|---|
| Shipping EVT silicon | At least one honest transfer or test-network/measurement campaign for RQ3 | Manufacture, carrier attach, certification, games as products |
| Full Device Quartet | Independent reproduction of the digital packs | |

A dissertation can finish in **~3–4 years** if Papers I–III stay scoped to `SYNTHETIC_SIM` / `EMULATED` plus one measurement or 5GTN-style campaign **if available**. Final gunnchOS hardware is not the doctoral object.

## 8. Which repositories are research instruments?

| Repo | Role |
|---|---|
| `7gc-digital-twin` | Scenario / digital-twin framework |
| `spectrumx-ai-ran-gary` | AI-RAN / cross-layer policy instrument |
| `readygary-6g-beam-selection` | PHY beam / band instrument |
| `ntn-resilience-sim` | TN/NTN disruption instrument |
| `edge-io-measurement-node` | Measurement / consent instrument |
| `waike-research-ops` | Human/service workload model |

Narrow product roles: Device Quartet = research form factors; WAIKE = workload model; 7GC = twin; gunnchOS = service-aware middleware; games = optional interactive workloads.

## 9. What evidence exists now?

**Digital:** pytest + smallest scientific scripts PASS on all six instruments and this portal (see [ACCEPTED_MAIN_REPRODUCTION.md](ACCEPTED_MAIN_REPRODUCTION.md)). Paper II has held-out / ablation / domain-shift / CIs. Paper I and III have synthetic summaries and reproduce scripts.

**Physical:** Pixel 6a **install/launch smoke only** — not RF, not spatial accuracy.

## 10. What evidence does not exist?

Calibrated mmWave OTA; NTN operator attach; sim→field transfer test; independent third-party reproduction; student/partner classroom execution; certification; carrier-grade operation; Oulu affiliation.

## 11. What would Oulu / 5GTN / 6G Flagship uniquely strengthen?

Witnessed test-network interruption, RF/QoS calibration, terrestrial/NTN-capable fallback on real bearers, external reproduction culture, and supervisor narrowing of the missing fidelity + checkpoint action design.

## 12. Why can this dissertation finish without shipping hardware?

Because the **scientific claims are about decision regions and continuity policies under stated models**, which are already digitally exercisable. Hardware shipping would strengthen RQ3 transfer; it is not required to pose, bound, and publish the three papers if limitations stay honest.

**Faculty outreach recommendation:** `YES_WITH_EXPLICIT_LIMITATIONS`.
