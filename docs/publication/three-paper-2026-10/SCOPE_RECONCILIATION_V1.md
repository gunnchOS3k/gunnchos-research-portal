# July roadmap and Oulu V3.1 reconciliation

Version 1.0; 13 October 2026. This is a provenance analysis and proposed publication mapping. It does not amend either historical plan, a frozen experiment, or the field-kit's Gate 1 authority.

## Preserved sources

The July authority is `gunnchos-7gc-ai-ran-field-kit/GATE1_LOCKED_RESEARCH_THESIS.md`, locked 23 July 2026, with `contracts/gate1_locked_thesis.v1.json`. It is inspected at source commit `9dfc326647880c244904dd50a47ea80c3d46748e`; its historical lock and change-control rules remain intact.

The later source is the owner's nine-page `Oulu_Research_Plan_V3_1_Source.pdf` in the attached `oulu_6g_three_paper_publication_program/sources/`. Pages 1–5 describe the research questions and studies; pages 6–7 give ethics, AI, feasibility and implementation boundaries. The PDF was read and the complete study pages 3–5 rendered and inspected. The source hash is recorded in `SOURCE_PROVENANCE.json`. The attached prospective two-page papers are useful context, not replacements for the canonical repository manuscripts or empirical evidence.

The owner-authorized production briefs of 12–13 October retain the three canonical paper repositories and confirm the later benchmark/control/resilience mapping. Drafting authorization does not make the July Gate 1's text or version change retrospectively.

## Research-question comparison

| Study | July locked emphasis | V3.1 proposed emphasis | Scientific continuity | Material difference |
|---|---|---|---|---|
| I | Privacy-preserving physical measurements, device/workload observations and trustworthy twin-state construction | Minimum-useful service profiles, workload/device thresholds, continuity metrics and benchmark scenarios | Both need traceable observations and explicit service/device context | A synthetic benchmark does not demonstrate physical measurement accuracy, consent execution or calibrated twin fidelity |
| II | Twin-informed AI-RAN control, fairness and worst-user performance against transparent baselines | Joint access, placement, fidelity, checkpointing and recovery with uncertainty | Both test the incremental value and cost of context-aware control | The implemented historical controller is a simplified rule/optimization instrument; joint uncertainty-aware deployment and equal compute budgets are not established |
| III | Terrestrial/local-edge/offline/NTN resilience and failure boundaries | TN, local-edge, peer, offline and NTN tradeoffs plus measurement-grounded calibration | Both seek conditions in which fallback helps or harms service | The seeded simulator validates a narrower TN/NTN policy set; local/peer execution and measured transfer cannot be inferred from other software paths |

## Evidence available for the publication drafts

Paper I's existing profile classifier and 30-seed timeline study support reproducible metric definitions, synthetic fixture behavior and the consequences of configured priors. Device-class mappings and repeated/proxy endpoints must be disclosed. A benchmark artifact is a defensible methodological object; transferable physical validity has not been demonstrated.

Paper II's historical and revised digital engines support reproducible policy comparisons, a failed superiority hypothesis, and a source-level diagnosis of switching costs and comparison semantics. The historical baseline labels, observation declarations, greedy oracle and ablations require qualifications. The revised fidelity/checkpoint results have their own provenance and must not replace the failed original result. Fixed-trace switching-cost algebra is retrospective analysis, not a new preregistered experiment.

Paper III's 30-seed simulator supports conditional, configured TN/NTN service outcomes, favorable and unfavorable fallback cases and analytical boundaries within the engine. It does not validate commercial NTN, RF links, local/peer fallback or satellite-terminal power measurements. Closely related current simulators constrain novelty; the draft must justify its narrower, auditable service-level contribution.

Supporting repositories contribute instruments rather than extra papers. ReadyGary supplies synthetic FR2 beam-selection context and host-process timing; those are not measured RF performance or proven sub-millisecond edge inference. Edge I/O and the field kit supply telemetry contracts, privacy/provenance mechanisms and controlled-evidence infrastructure. Any later genuine device record has to be identified by its own source and protocol before it can support a particular paper claim; its presence alone does not calibrate the three frozen simulations.

## Extensions requiring new studies

| Extension | Evidence required | Relationship to present drafts |
|---|---|---|
| Service-threshold validity and benchmark transfer | Independently defined workloads, calibrated device/network traces, external scenario families and threshold sensitivity | Future validation of Paper I; no retroactive claim that configured priors were measured |
| Fair controller superiority | Prospective equal-information/equal-action/feasibility protocol, equalized compute accounting and held-out cost-sensitive evaluation | Follow-up to Paper II's negative result; historical results remain visible |
| Fidelity/checkpoint persistence | Real state-size, loss/recovery, overhead and continuity measurements | Goes beyond abstract action labels and synthetic scoring |
| Local/peer/offline fallback | Implemented modes and recovery/synchronization costs in a newly frozen engine | Cannot be claimed validated by Paper III's present seeded TN/NTN experiment |
| NTN measurement transfer | Source-backed link ranges, terminal-power measurements or approved emulation, and a documented calibration/transfer test | Future extension rather than a completed result |
| Independent research reproduction | Separate human or institution executes the preserved source and reports results | AI-assisted author-side re-execution does not satisfy this external gate |

## Three distinct contribution boundaries

The proposed separation is (I) a metric/profile and benchmark-method artifact, (II) a cost-sensitive control comparison and negative-result analysis, and (III) conditional fallback decision regions and failure ceilings. Shared service terminology, software provenance and elementary statistical definitions may be restated for standalone review. The papers must use different primary questions and evidence, disclose related drafts, cite genuine public companion outputs when appropriate and avoid repeating the same results as separate contributions. Technical separation does not establish scientific originality; the paper-specific novelty matrices and author/external review remain necessary.

## Future dissertation compatibility

The drafts align with the later plan's central theme of service continuity under heterogeneous communications and computing constraints. Their current synthetic scope is narrower than its proposed measurement-grounded dissertation. Admission, supervision, research-unit approval, funding and University of Oulu affiliation remain unclaimed.

The current [Oulu thesis requirements](https://www.oulu.fi/en/research/graduate-school/thesis-requirements-and-doctoral-studies/thesis-requirements), inspected 13 October 2026, list at least three papers for Information Technology and Electrical Engineering, including Communications Engineering; at least two must be published or accepted, and one may be submitted at pre-examination. Significant individual contribution is required in each. A compilation thesis also needs an independent synthesis, scientific quality review, AI-use disclosure and attention to publisher rights. These drafts satisfy no publication or acceptance gate.

## Change-control disposition

Keep the July lock and V3.1 source unchanged. Treat this document and the three publication branches as a reviewable reconciliation. If the owner later wants the field-kit's authoritative thesis/RQ map changed, prepare a separate versioned Gate 1 change, JSON/schema/validator agreement and reviewed PR. No such authority amendment or merge is performed here.
