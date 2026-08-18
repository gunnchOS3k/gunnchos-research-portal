# Research-plan alignment report

Compares the **canonical narrative in the supervisor-ready prompt** to what the 16 repositories actually contain at the 2026-08-18 baseline audit. Application PDFs were not edited.

## Implemented support for RQ1

- Device OS: modes, launcher contract, Device Lab, golden-journey hooks, `make test`.  
- 7GC twin: site/scenario scaffold, synthetic scenes, `make test` / `make smoke`.  
- Gap: no frozen **Service-Continuity Profile Model** artifact that a paper could cite with regenerable tables; UML placeholder-only in both repos.

## Implemented support for RQ2

- SpectrumX: judged occupancy core + documented rule-based extension controller; mature UML.  
- ReadyGary: toy channel benchmarks, exhaustive/hierarchical baselines in scripts.  
- Gaps: 28 GHz documented as Sub-6 (false); README benchmark table risk of being read as measured; sub-ms inference unproven; joint placement/fidelity/caching/recovery not a single frozen Paper-II harness; SpectrumX has no `.github/workflows` and no `LICENSE` file in the audited tree.

## Implemented support for RQ3

- NTN sim: setup/test/sensitivity/demo Makefile targets; template-like `REPRODUCIBILITY.md`.  
- Edge I/O: schemas, simulated paths, Android make targets, consent language.  
- Gaps: compound failure matrix not frozen; no `DEVICE_MEASURED` evidence; IMU must not be sold as absolute pose.

## Plan claims not yet backed by repo evidence

- Held-out scenario families with repeated seeds, domain-shift tests, effect sizes, and confidence intervals as a **Paper-II package**.  
- Oracle/reference baselines that are information-equivalent to the proposed controller.  
- Independent external reproduction records.  
- Physical calibration of Edge I/O and hardware EVT.  

## Repo capabilities not needed by the dissertation

- Full commercial launcher polish, four complete games, WAIKE curriculum ops, Discord/music integrations in gunnchAI.  
These should remain **workloads / engineering depth**, not extra RQs.

## Wording that risks scope creep

- Portal `README.md` still leads with equitable **product** ecosystem (Cycle 3A WP-012). Fine for public product IA; dangerous if a supervisor never reaches `docs/phd/`.  
- 7GC README still says “Spine repo” for a digital-twin program — historical; twin is RQ1 validation, not the product charter.  
- Emergent-intent README mentions “Oulu GENOME research track” — must stay **theme alignment**, not appointment.

## Opportunities for stronger digital evidence (automatable)

- Correct ReadyGary frequency taxonomy.  
- Generate ReadyGary/NTN/SpectrumX tables from scripts into `results/` and cite those files.  
- Replace placeholder `docs/uml/README.md` files with current/future/legacy packs.  
- Add SpectrumX LICENSE + CI.  
- Portal supervisor front door (this directory).  
- Contract tests for twin-state JSON across 7GC ↔ SpectrumX ↔ NTN.

Keep the dissertation focused on three papers.
