# RQ → repository → evidence map

Evidence classes follow [EVIDENCE_TAXONOMY.md](EVIDENCE_TAXONOMY.md). A repository’s existence is not Paper I/II/III evidence.

**Live freeze (post-A2, 2026-08-28).** Accepted `origin/main` SHAs and digital reproduction: [../oulu/FACULTY_EVIDENCE_FREEZE.md](../oulu/FACULTY_EVIDENCE_FREEZE.md), [../oulu/RQ_EVIDENCE_MATRIX.md](../oulu/RQ_EVIDENCE_MATRIX.md), [../oulu/ACCEPTED_MAIN_REPRODUCTION.md](../oulu/ACCEPTED_MAIN_REPRODUCTION.md).

The 2026-08-18 baseline and 2026-08-27 pre-A2 Stream A blocks below are **historical**. They are not live GitHub truth.

## RQ1 / Paper I — live post-A2

**Canonical RQ (V3).** How can representative workloads and the constraints of four resource-constrained device classes be translated into measurable service-continuity profiles, metrics, and benchmark scenarios?

**Status:** `DIGITAL_REPRODUCIBLE_STRONG_CORE` (not scientifically complete / field validated).

| Item | Status on accepted main |
|---|---|
| Primary repos | `7gc-digital-twin` `dc43a567e3f2e81a5b59fea6dd67c7054cfdde56` (merged #31; historical pre-A2 `4cd7016…`) |
| Service-continuity profiles | `IMPLEMENTED_AND_REPRODUCIBLE` — `fixtures/device_os/SERVICE_CONTINUITY_PROFILES.json`; states target/degraded/min_useful/failed |
| Seeded bench + stats | `IMPLEMENTED_AND_REPRODUCIBLE` — seeds 1..30 (n=30); `task_completion_ratio` + `time_above_minimum_useful`; correct 95% Student-t CIs; paired \(d_z\) where applicable |
| Artifacts | `paper/artifacts/rq1_statistical_summary.json`, `rq1_statistical_report.*` |
| Faculty command | `PYTHONPATH=src python -m pytest -q tests/test_rq1_statistical_parity.py --tb=line` |
| Evidence class | `SYNTHETIC_SIM` |
| Remaining | Independent reproduction `EXTERNAL_PENDING`; physical RF pending |

Supporting workloads (games, WAIKE, gunnchAI) may supply traces **if** a frozen RQ1 experiment imports them.

## RQ2 / Paper II — live post-A2

**Canonical RQ (V3).** To what extent can joint access selection, computation placement, fidelity/model adaptation, caching/checkpointing, and recovery control - informed by radio-aware digital-twin state and uncertainty - improve service-continuity utility under mobility, blockage, congestion, edge-resource variation, and energy constraints?

**Status:** `DIGITAL_REPRODUCIBLE_STRONG_CORE`.

| Item | Status on accepted main |
|---|---|
| Primary repos | `spectrumx-ai-ran-gary` `9060655e724374f60cbbb86832816c9c2d332ca4` (merged #102; feature `b44357f…` on main; historical pre-A2 `cef3900…`); `readygary-6g-beam-selection` `5698752…` |
| Controller | Rule-based access×placement **plus** `fidelity_level` and checkpoint/recover actions. **Not RL.** |
| Baselines | no-adaptation / static / placement-only; **fixed_target_fidelity** / **checkpoint_disabled**; ReadyGary exhaustive / hierarchical / oracle |
| Info-equivalence | Runtime enforced: non-oracle policies see declared observation fields + action-space only; oracle explicit **no future peek**; `information_equivalence_pass=true` |
| Held-out, ablations, domain shift, CIs | `IMPLEMENTED_AND_REPRODUCIBLE` on Paper II JSON packs |
| Fidelity adaptation | `IMPLEMENTED_AND_REPRODUCIBLE` on SpectrumX (post-A2) |
| Checkpoint/recover | `IMPLEMENTED_AND_REPRODUCIBLE` — causal checkpoint state; rolling thrash |
| Evidence class | Policy extension + ReadyGary: `SYNTHETIC_SIM`. Do **not** claim app persistence / production RAN / physical RF / trained RL / standardized 6G |
| Remaining | Independent reproduction `EXTERNAL_PENDING` |

Dirty local ReadyGary tables are **not** accepted-main truth.

## RQ3 / Paper III — live post-A2

**Canonical RQ (V3).** Under which disruption conditions do terrestrial, local-edge, peer/device-to-device, offline, and NTN fallback modes preserve minimum useful service, and what performance, energy, privacy, and recovery tradeoffs arise in simulation, emulation, and device-level measurements?

**Status:** `DIGITAL_REPRODUCIBLE_STRONG_CORE_WITH_TRANSFER_PENDING`.

| Item | Status on accepted main |
|---|---|
| Primary repos | `ntn-resilience-sim` `c4215fc1039f5452917b9b2034b42e03fdc13689` (merged #28; historical pre-A2 `9165209…`); `edge-io-measurement-node` `af57fbd…` |
| Disruption families | TN/NTN/offline seeded sweeps seeds 1..30; correct CIs; paired defs; decision regions; `ntn_always_better=false` with negative regions |
| Local-edge / peer | Gate2 mode stubs exist; **not** exercised in seeded Paper-III engine (`local_peer_not_in_paper_iii_engine`) |
| Measurement | Edge I/O digital schema/export `IMPLEMENTED_AND_REPRODUCIBLE`; absolute spatial / RF / QoS **`PHYSICAL_PENDING`** |
| Sim→measurement transfer | Still open |
| Evidence class | NTN: `SYNTHETIC_SIM`. Edge I/O: `EMULATED` (not `DEVICE_MEASURED`) |
| Remaining | Transfer test; operator attach; RF/spatial; independent reproduction |

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

---

## Historical — pre-A2 Stream A (2026-08-27) — not live status

Kept so the Stream A freeze is not silently rewritten. **Do not cite as current evidence.**

| RQ | Pre-A2 SHA | Pre-A2 status note |
|---|---|---|
| RQ1 | 7GC `4cd7016` | Profiles + reproduce PASS; stats lighter than Paper II |
| RQ2 | SpectrumX `cef3900` | Paper II packs PASS; fidelity + checkpoint **MISSING_DIGITAL** |
| RQ3 | NTN `9165209` | Sweeps PASS; stats lighter; transfer pending |

---

## Historical baseline (2026-08-18) — not live status

Kept so the 2026-08-18 supervisor snapshot is not silently rewritten. **Do not cite this block as current evidence.**

### RQ1 (2026-08-18)

| Item | Status at baseline audit (2026-08-18) |
|---|---|
| Primary repos | `gunnchos-device-os`, `7gc-digital-twin` |
| Service-Continuity Profile Model | Partial — device states, campus modes, twin site schemas exist; not yet a frozen Paper-I profile package |
| Benchmark scenarios | Partial — 7GC synthetic/site fixtures; not held-out Paper-I campaign |
| Current evidence class | `SYNTHETIC_SIM` / `EMULATED` |
| Remaining | Unify profile schema; generate tables from code; independent reproduction |

### RQ2 (2026-08-18)

| Item | Status at baseline audit |
|---|---|
| Primary repos | `spectrumx-ai-ran-gary`, `readygary-6g-beam-selection` |
| Known defect | ReadyGary README labelled **28 GHz as “Sub-6 GHz”** — corrected on later accepted main |
| Current evidence class | SpectrumX judged core: `OPEN_DATA_BACKED` (competition IQ). Extension/policy: `SYNTHETIC_SIM`. ReadyGary: `SYNTHETIC_SIM` |

### RQ3 (2026-08-18)

| Item | Status at baseline audit |
|---|---|
| Primary repos | `ntn-resilience-sim`, `edge-io-measurement-node` |
| Measurement calibration | Edge I/O: simulated device / schema path; **absolute spatial accuracy `PHYSICAL_PENDING`** |
| Current evidence class | NTN: `SYNTHETIC_SIM`. Edge I/O: `EMULATED` (not `DEVICE_MEASURED`) |
