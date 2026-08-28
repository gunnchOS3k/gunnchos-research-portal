# V3 research-plan ↔ live evidence alignment

**Date:** 2026-08-28 (post-A2 refresh; Stream A freeze dated 2026-08-27)  
**Canonical narrative:** V3 research plan (DOCX/PDF) — **not modified**.  
**Freeze reuse:** Stream A `artifacts/oulu_readiness_2026_08_27/` + `docs/oulu/*` (SHAs/status refreshed).  
**No physical evidence invented.** Pixel = install/launch smoke only.  
**Dissertation is not complete.** Frame: digitally implemented now vs doctoral research still open.

### Accepted-main SHAs (reverified 2026-08-28)

| Repo | Live SHA | Notes |
|---|---|---|
| 7gc-digital-twin | `dc43a567e3f2e81a5b59fea6dd67c7054cfdde56` | merged #31; historical pre-A2 `4cd7016…` |
| spectrumx-ai-ran-gary | `9060655e724374f60cbbb86832816c9c2d332ca4` | merged #102; feature `b44357f…` on main; historical `cef3900…` |
| readygary-6g-beam-selection | `569875224db7812890ec6abc48dfe43a608094f3` | unchanged tip |
| edge-io-measurement-node | `af57fbdac857ae386b23b5b747fdc05797621f92` | unchanged tip |
| ntn-resilience-sim | `c4215fc1039f5452917b9b2034b42e03fdc13689` | merged #28; historical `9165209…` |
| waike-research-ops | `8eb2827dc58ffa391842da1bfb1ee665c25a31a7` | unchanged tip |
| gunnchos-research-portal | `f4155bc79831a6ed0d9e7881a3037cc4bf012d6a` | origin/main tip (PR #12 lineage) |

Evidence classes: `DIGITAL_REPRODUCIBLE` | `DIGITAL_PARTIAL` | `DOCUMENTED_ONLY` | `PHYSICAL_PENDING` | `HUMAN_PENDING` | `EXTERNAL_PENDING` | `SUPERVISOR_DESIGN_DECISION` | `NOT_YET_EVIDENCE`

---

## RQ1 — profiles, metrics, benchmarks

| V3 claim | Required evidence | Repo @ SHA | Path | Command | Class | Status | Gap / next |
|---|---|---|---|---|---|---|---|
| Four device classes → continuity profiles | Profile schema + states | 7gc `dc43a56` | `fixtures/device_os/SERVICE_CONTINUITY_PROFILES.json` | `make reproduce` / faculty pytest | DIGITAL_REPRODUCIBLE | PASS (`SYNTHETIC_SIM`) | Independent EXTERNAL_PENDING |
| Seeded stats (task completion + time above min-useful) | n=30, 95% t-CI, paired \(d_z\) | 7gc `dc43a56` | `paper/artifacts/rq1_statistical_*.json` | `PYTHONPATH=src python -m pytest -q tests/test_rq1_statistical_parity.py` | DIGITAL_REPRODUCIBLE | **STRONG_CORE** | Not field validated |
| Workload translation | Human/service workload model | waike `8eb2827` | `artifacts/COURSE_COUNTS.json` | `PYTHONPATH=src python3.11 scripts/emit_digital_rc.py` | DIGITAL_PARTIAL | Supporting only | Partner classroom EXTERNAL_PENDING |

## RQ2 — joint access / placement / fidelity / checkpoint / recovery

| V3 claim | Required evidence | Repo @ SHA | Path | Command | Class | Status | Gap / next |
|---|---|---|---|---|---|---|---|
| Access + compute placement vs baselines | Rule-based controller + baselines | spectrumx `9060655` | Paper II `results/experiments/rq2_*` | Paper II pytest | DIGITAL_REPRODUCIBLE | PASS | Not RL |
| Fidelity + checkpoint/recover actions | Named RQ2 actions + baselines | spectrumx `9060655` | `rq2_fidelity_checkpoint_tiny.json`; artifact index | `pytest tests/test_rq2_fidelity_checkpoint.py` | DIGITAL_REPRODUCIBLE | **STRONG_CORE** (post-A2) | Not app persistence / production RAN |
| Runtime information-equivalence | Declared obs + action-space; oracle no future peek | spectrumx `9060655` | `rq2_information_equivalence_audit.json` | same pytest suite | DIGITAL_REPRODUCIBLE | PASS (`information_equivalence_pass=true`) | — |
| Beam/band radio instrument | Beam baselines | readygary `5698752` | FR2/beam tables | toy benchmark | DIGITAL_REPRODUCIBLE | PASS (`SYNTHETIC_SIM`) | Sub-ms edge **not** proven |

## RQ3 — TN / local-edge / peer / offline / NTN fallback + measurements

| V3 claim | Required evidence | Repo @ SHA | Path | Command | Class | Status | Gap / next |
|---|---|---|---|---|---|---|---|
| Disruption decision regions + stats | TN/NTN seeds 1..30, CIs, paired defs | ntn `c4215fc` | `rq3_statistical_summary.json`; sweeps JSON | `pytest tests/test_rq3_statistical_parity.py`; `scripts/reproduce.py` | DIGITAL_REPRODUCIBLE | **STRONG_CORE** (`ntn_always_better=false`) | Transfer still open |
| Local-edge / peer in seeded engine | Seeded Paper-III modes | ntn | experiment flag `local_peer_not_in_paper_iii_engine` | — | DIGITAL_PARTIAL / NOT_YET_EVIDENCE | **PENDING** in seeded engine | Gate2 stubs only |
| Device-level measurements | Measurement export | edge-io `af57fbd` | research export | reproduce script | DIGITAL_PARTIAL | Schema PASS | RF/spatial PHYSICAL_PENDING |
| Sim→measurement transfer | Transfer test | — | — | — | PHYSICAL_PENDING | OPEN | Needs lab/test-network with supervisor |

## Cross-cutting V3 claims

| Claim | Class | Status |
|---|---|---|
| Reproducible digital instruments exist | DIGITAL_REPRODUCIBLE | PASS — strong cores RQ1–RQ3 (post-A2) |
| Physical / test-network validation | PHYSICAL_PENDING | Honest in V3 feasibility |
| Independent third-party reproduction | EXTERNAL_PENDING | OPEN |
| Dissertation scientifically complete | NOT_YET_EVIDENCE | Explicitly **not claimed** |
| Oulu affiliation / supervisor commitment | NOT_YET_EVIDENCE | Explicitly **not claimed** |
| Novelty already established | SUPERVISOR_DESIGN_DECISION | Hypothesis only |

## Rollup

| RQ | Live alignment | Strongest class | Honest gap |
|---|---|---|---|
| RQ1 | DIGITAL_REPRODUCIBLE_STRONG_CORE | SYNTHETIC_SIM profiles + n=30 CIs | Field validation; independent repro |
| RQ2 | DIGITAL_REPRODUCIBLE_STRONG_CORE | SYNTHETIC_SIM fidelity/checkpoint + info-equivalence | Not production RAN / RF / RL |
| RQ3 | DIGITAL_REPRODUCIBLE_STRONG_CORE_WITH_TRANSFER_PENDING | SYNTHETIC_SIM TN/NTN decision regions | Measurement transfer; local-edge/peer in seeded engine |

Repository existence alone is not paper evidence. Dirty local ReadyGary tables are **not** accepted-main truth.
