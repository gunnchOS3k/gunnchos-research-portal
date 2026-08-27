# V3 research-plan ↔ live evidence alignment

**Date:** 2026-08-27  
**Canonical narrative:** V3 research plan (DOCX/PDF) — **not modified**.  
**Freeze reuse:** Stream A `artifacts/oulu_readiness_2026_08_27/` + `docs/oulu/*`.  
**No physical evidence invented.** Pixel = install/launch smoke only.

### Accepted-main SHAs (reverified 2026-08-27)

| Repo | Freeze SHA | `origin/main` match |
|---|---|---|
| 7gc-digital-twin | `4cd70169b35a67937eac076caaa7905ffd47adeb` | yes |
| spectrumx-ai-ran-gary | `cef3900af100c0526e8f75efd238303fd6a268bd` | yes |
| readygary-6g-beam-selection | `569875224db7812890ec6abc48dfe43a608094f3` | yes |
| edge-io-measurement-node | `af57fbdac857ae386b23b5b747fdc05797621f92` | yes |
| ntn-resilience-sim | `916520919bea4d9957970d824045c32929bb80e5` | yes |
| waike-research-ops | `8eb2827dc58ffa391842da1bfb1ee665c25a31a7` | yes |
| gunnchos-research-portal (Stream A freeze) | `2a3303d56a71c1f78bfbbf165ed75f1d368fa98f` | ancestor of current `origin/main` `f4155bc…` (PR #12 merged) |

Evidence classes: `DIGITAL_REPRODUCIBLE` | `DIGITAL_PARTIAL` | `DOCUMENTED_ONLY` | `PHYSICAL_PENDING` | `HUMAN_PENDING` | `EXTERNAL_PENDING` | `SUPERVISOR_DESIGN_DECISION` | `NOT_YET_EVIDENCE`

---

## RQ1 — profiles, metrics, benchmarks

| V3 claim | Required evidence | Repo @ SHA | Path | Command | Class | Status | Gap / next automatable |
|---|---|---|---|---|---|---|---|
| Four device classes → continuity profiles | Profile schema + states | 7gc `4cd7016` | `fixtures/device_os/SERVICE_CONTINUITY_PROFILES.json` | `PYTHONPATH=src python scripts/reproduce.py` | DIGITAL_REPRODUCIBLE | PASS (synthetic) | Unify fidelity+checkpoint fields into one frozen action model |
| Benchmark scenarios | Scenario/experiment JSON | 7gc `4cd7016` | `results/experiments/rq1_gary_flagship_profiles.json`; `paper/artifacts/rq1_experiment_summary.json` | same | DIGITAL_REPRODUCIBLE | PASS (synthetic) | Stronger stats pack (CIs) still lighter than Paper II |
| Workload translation | Human/service workload model | waike `8eb2827` | `artifacts/COURSE_COUNTS.json` | `PYTHONPATH=src python3.11 scripts/emit_digital_rc.py` | DIGITAL_PARTIAL | Supporting only | Partner classroom EXTERNAL_PENDING |
| Independent reproduction | External clean-room | — | — | — | EXTERNAL_PENDING | OPEN | Human/external action |

## RQ2 — joint access / placement / fidelity / checkpoint / recovery

| V3 claim | Required evidence | Repo @ SHA | Path | Command | Class | Status | Gap / next automatable |
|---|---|---|---|---|---|---|---|
| Access + compute placement control vs baselines | Rule-based controller + baselines | spectrumx `cef3900` | `results/e2e/airan_policy_metrics.json`; Paper II `results/experiments/rq2_*` | `python scripts/demo_airan_policy.py --toy`; pytest Paper II suite | DIGITAL_REPRODUCIBLE | PASS (synthetic / toy path) | Not RL; fidelity+checkpoint MISSING_DIGITAL |
| Held-out / ablation / domain-shift / CIs | Paper II packs | spectrumx `cef3900` | `results/experiments/rq2_*` | pytest `tests/test_paper_ii_digital.py` | DIGITAL_REPRODUCIBLE | PASS | Independent EXTERNAL_PENDING |
| Beam/band radio instrument | Beam baselines | readygary `5698752` | `results/e2e/benchmark_summary.md`; FR2 experiment JSON | `PYTHONPATH=. python scripts/run_benchmark_table.py --toy` | DIGITAL_REPRODUCIBLE | PASS (`SYNTHETIC_SIM`) | Sub-ms edge inference **not** proven |
| Fidelity/model adaptation in joint action | Named RQ2 action | spectrumx / readygary | — | — | DIGITAL_PARTIAL / NOT_YET_EVIDENCE | GAP | ReadyGary dual-band/CSI only partial analogue |
| Caching/checkpointing + recovery control | Named RQ2 action | spectrumx / readygary | — | — | NOT_YET_EVIDENCE | GAP | SUPERVISOR_DESIGN_DECISION on scope order |
| Radio-aware digital-twin state | Twin coupling | 7gc + spectrumx | twin fixtures / policy inputs | reproduce scripts above | DIGITAL_PARTIAL | PARTIAL | Full frozen Paper II twin coupling campaign |

## RQ3 — TN / local-edge / peer / offline / NTN fallback + measurements

| V3 claim | Required evidence | Repo @ SHA | Path | Command | Class | Status | Gap / next automatable |
|---|---|---|---|---|---|---|---|
| Disruption decision regions | TN/NTN/offline sweeps | ntn `9165209` | `results/experiments/rq3_gary_failover_sweeps.json`; `paper/artifacts/rq3_experiment_summary.json` | `PYTHONPATH=src python scripts/reproduce.py` | DIGITAL_REPRODUCIBLE | PASS (synthetic; rejects “NTN always better” under documented assumptions) | Compound radio+compute+privacy cost still deepen-able |
| Device-level measurements | Measurement export | edge-io `af57fbd` | `results/research_export/gary_research_export.json` | `PYTHONPATH=src python3.11 scripts/reproduce.py` | DIGITAL_PARTIAL | Schema/export PASS | Absolute spatial/RF/QoS PHYSICAL_PENDING |
| Pixel device smoke | Install/launch only | edge-io / portal packets | Pixel acceptance packet | — | PHYSICAL_PENDING | Smoke only | Not RF evidence |
| Sim→measurement transfer | Transfer test | — | — | — | PHYSICAL_PENDING / NOT_YET_EVIDENCE | OPEN | Needs lab/test-network design with supervisor |
| Privacy / energy tradeoffs at device | Measurement + energy | edge-io / device constraints | — | — | DOCUMENTED_ONLY / PHYSICAL_PENDING | OPEN | Do not invent |

## Cross-cutting V3 claims

| Claim | Class | Status |
|---|---|---|
| Reproducible digital instruments exist | DIGITAL_REPRODUCIBLE | PASS on six instruments (Stream A) |
| Physical / test-network validation | PHYSICAL_PENDING | Honest in V3 feasibility |
| Independent third-party reproduction | EXTERNAL_PENDING | OPEN |
| Human classroom / playtest | HUMAN_PENDING / EXTERNAL_PENDING | OPEN |
| Oulu affiliation / supervisor commitment | NOT_YET_EVIDENCE | Explicitly **not claimed** |
| Novelty already established | SUPERVISOR_DESIGN_DECISION | Hypothesis only |

## Rollup

| RQ | Live alignment | Strongest class | Honest gap |
|---|---|---|---|
| RQ1 | DIGITAL_PARTIAL→strong digital core | DIGITAL_REPRODUCIBLE profiles/scenarios | Joint action model + stronger stats |
| RQ2 | DIGITAL_PARTIAL | DIGITAL_REPRODUCIBLE Paper II packs | Fidelity + checkpoint actions |
| RQ3 | DIGITAL_PARTIAL | DIGITAL_REPRODUCIBLE NTN sweeps | Measurement transfer; physical RF |

Repository existence alone is not paper evidence. Dirty local ReadyGary tables are **not** accepted-main truth.
