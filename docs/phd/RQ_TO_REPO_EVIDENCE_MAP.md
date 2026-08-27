# RQ → repository → evidence map

Evidence classes follow [EVIDENCE_TAXONOMY.md](EVIDENCE_TAXONOMY.md). A repository’s existence is not Paper I/II/III evidence.

**Live freeze (2026-08-27).** Accepted `origin/main` SHAs and digital reproduction: [../oulu/FACULTY_EVIDENCE_FREEZE.md](../oulu/FACULTY_EVIDENCE_FREEZE.md), [../oulu/RQ_EVIDENCE_MATRIX.md](../oulu/RQ_EVIDENCE_MATRIX.md), [../oulu/ACCEPTED_MAIN_REPRODUCTION.md](../oulu/ACCEPTED_MAIN_REPRODUCTION.md).

The 2026-08-18 baseline table is kept below as **historical**. It is not live GitHub truth.

## RQ1 / Paper I — live 2026-08-27

**Question.** How should minimum useful service be represented for resource-constrained devices when communication, compute, fidelity, and recovery choices are jointly variable?

| Item | Status on accepted main |
|---|---|
| Primary repos | `7gc-digital-twin` `4cd70169b35a67937eac076caaa7905ffd47adeb` (device-OS profiles consumed as fixtures) |
| Service-continuity profiles | `IMPLEMENTED_AND_REPRODUCIBLE` — `fixtures/device_os/SERVICE_CONTINUITY_PROFILES.json`; states target/degraded/min_useful/failed |
| Benchmark scenarios | `IMPLEMENTED_AND_REPRODUCIBLE` (synthetic) — `make reproduce` wrote `results/experiments/rq1_gary_flagship_profiles.json` on 2026-08-27 |
| Baselines | `PARTIAL` — proportional-fair stub, weaker than Paper II |
| Metrics + stats | `PARTIAL` — seed sensitivity tables exist; not a full 95% t-CI pack |
| Evidence class | `SYNTHETIC_SIM` / `EMULATED` |
| Remaining | Joint fidelity+checkpoint in the profile; independent reproduction `EXTERNAL_PENDING` |

Supporting workloads (games, WAIKE, gunnchAI) may supply traces **if** a frozen RQ1 experiment imports them.

## RQ2 / Paper II — live 2026-08-27

**Question.** When should a system switch access, move computation, reduce fidelity, use local/peer compute, checkpoint/recover, or enter a degraded/offline mode?

| Item | Status on accepted main |
|---|---|
| Primary repos | `spectrumx-ai-ran-gary` `cef3900af100c0526e8f75efd238303fd6a268bd`; `readygary-6g-beam-selection` `569875224db7812890ec6abc48dfe43a608094f3` |
| Controller | SpectrumX: detector-conditioned **rule-based** network×placement controller (`offline_continuation` included). ReadyGary: adaptive beam/band + dual-band controller. **Not RL.** |
| Baselines | SpectrumX: no-adaptation / static / placement-only. ReadyGary: exhaustive / hierarchical / oracle |
| Held-out, ablations, domain shift, CIs | `IMPLEMENTED_AND_REPRODUCIBLE` on both Paper II JSON packs committed on main (`results/experiments/rq2_*`) |
| Fidelity adaptation | `MISSING_DIGITAL` on SpectrumX Action; ReadyGary dual-band/CSI is only a partial analogue |
| Checkpoint/recover | `MISSING_DIGITAL` on both PHY/policy repos |
| Known defect (closed on ReadyGary main) | FR2 (28 GHz) vs Sub-6 is **distinguished** on `5698752`. Do not repeat the 2026-08-18 “README labels 28 GHz as Sub-6” defect as live. |
| Evidence class | SpectrumX competition IQ core: `OPEN_DATA_BACKED` (private IQ not re-run here). Policy extension + ReadyGary: `SYNTHETIC_SIM`. Host timing: `HOST_PROCESS_TIMING`. Sub-ms edge: **not proven**. |
| Remaining | Add fidelity + checkpoint to the action space; independent reproduction `EXTERNAL_PENDING` |

Dirty local ReadyGary tables (2026-08-27 working tree) are **not** accepted-main truth.

## RQ3 / Paper III — live 2026-08-27

**Question.** Under terrestrial/NTN/backhaul disruption, what decision regions and policies preserve useful service, and how well do digital-twin/simulation conclusions transfer toward test-network or measurement evidence?

| Item | Status on accepted main |
|---|---|
| Primary repos | `ntn-resilience-sim` `916520919bea4d9957970d824045c32929bb80e5`; `edge-io-measurement-node` `af57fbdac857ae386b23b5b747fdc05797621f92` |
| Disruption families | NTN: `IMPLEMENTED_AND_REPRODUCIBLE` synthetic TN/NTN/offline + `make reproduce` → `rq3_gary_failover_sweeps.json`. Summary rejects “NTN always better” under documented assumptions. |
| Measurement | Edge I/O digital schema/export `IMPLEMENTED_AND_REPRODUCIBLE`; absolute spatial / RF / QoS **`PHYSICAL_PENDING`**. Pixel 6a artifact is **install/launch smoke**, not RF. |
| Sim→measurement transfer | `MISSING_DIGITAL` / `PHYSICAL_PENDING` |
| Evidence class | NTN: `SYNTHETIC_SIM`. Edge I/O: `EMULATED` (not `DEVICE_MEASURED`) |
| Remaining | Transfer test; physical calibration packet; no operator-performance claims |

## Supporting repositories (not automatic papers)

| Repository | Allowed scientific use |
|---|---|
| `gunnchos-hardware-industrial-design` | Form-factor / power / antenna integration **constraints** for RQ1/RQ3 |
| `gunnchAI3k` | Local intelligence **workload** and placement/fidelity actions |
| `waike-research-ops` | Education service workload (`8eb2827`; digital RC tests PASS; partner classroom `EXTERNAL_PENDING`) |
| Games + BeatLink + Archive of Life | Latency/QoE/content workloads if imported into a frozen experiment |
| `gunnchos-gpu-nr-baseband-platform` | Optional PHY validation extension (`BLOCKED_GPU` on CPU-only hosts) |
| `gunnchos-emergent-service-intent-protocols` | Optional distributed-intelligence extension (public; not a fourth paper) |
| `gunnchos-research-portal` | Navigation / evidence map only |

See [RESEARCH_PLAN_ALIGNMENT_REPORT.md](RESEARCH_PLAN_ALIGNMENT_REPORT.md) for gaps versus the canonical narrative.

---

## Historical baseline (2026-08-18) — not live status

Kept so the 2026-08-18 supervisor snapshot is not silently rewritten. **Do not cite this block as current evidence.**

### RQ1 (2026-08-18)

| Item | Status at baseline audit (2026-08-18) |
|---|---|
| Primary repos | `gunnchos-device-os`, `7gc-digital-twin` |
| Service-Continuity Profile Model | Partial — device states, campus modes, twin site schemas exist; not yet a frozen Paper-I profile package |
| Benchmark scenarios | Partial — 7GC synthetic/site fixtures; not held-out Paper-I campaign |
| Device/service/network state schemas | Partial — launcher contracts, twin state JSON, Edge I/O schemas (supporting) |
| Minimum-useful / degraded / target / failed states | Partial — mode/state machines in device OS; not unified continuity metrics |
| Transparent static/reference/oracle baselines | Incomplete for RQ1 as a named experiment |
| Metrics + reproducibility package | Device OS and 7GC have `make test` / smoke paths; Paper-I frozen artifact **not** signed |
| Current evidence class | `SYNTHETIC_SIM` / `EMULATED` |
| Remaining | Unify profile schema; generate tables from code; independent reproduction |

### RQ2 (2026-08-18)

| Item | Status at baseline audit |
|---|---|
| Primary repos | `spectrumx-ai-ran-gary`, `readygary-6g-beam-selection` |
| Simple baselines first | SpectrumX: detector-conditioned **rule-based** controller is the shipped path (not RL). ReadyGary: exhaustive/hierarchical baselines exist in code; README table must not be treated as measured RF |
| Digital-twin context | SpectrumX extension + 7GC twin manifests; coupling not a frozen Paper-II campaign |
| Held-out families, seeds, ablations, domain shift, uncertainty, CIs, compute cost, switching cost | Partial scripts (`make ablation`, toy benchmarks); **not** a complete Paper-II evidence pack |
| Known defect | ReadyGary README labelled **28 GHz as “Sub-6 GHz”** — technically false (FR2 mmWave). Must be corrected in-repo |
| Current evidence class | SpectrumX judged core: `OPEN_DATA_BACKED` (competition IQ). Extension/policy: `SYNTHETIC_SIM`. ReadyGary: `SYNTHETIC_SIM` |
| Remaining | Information-equivalent comparisons; reject unsupported latency claims (sub-ms unproven); independent reproduction |

### RQ3 (2026-08-18)

| Item | Status at baseline audit |
|---|---|
| Primary repos | `ntn-resilience-sim`, `edge-io-measurement-node` |
| Disruption families | NTN sim has demo/sensitivity targets; compound radio+compute+backhaul not yet a frozen Paper-III matrix |
| Measurement calibration | Edge I/O: simulated device / schema path; **absolute spatial accuracy `PHYSICAL_PENDING`** |
| Current evidence class | NTN: `SYNTHETIC_SIM`. Edge I/O: `EMULATED` (not `DEVICE_MEASURED`) |
| Remaining | Thresholded minimum-service metrics aligned with RQ1 profiles; physical calibration packet; no operator-performance claims |
