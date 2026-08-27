# Claim-honesty scan — 2026-08-27

Machine-readable: [`artifacts/oulu_readiness_2026_08_27/CLAIM_AUDIT.json`](../../artifacts/oulu_readiness_2026_08_27/CLAIM_AUDIT.json)

Hits were classified. Only noncontroversial control-plane wording was repaired on this branch. Historical files were not erased.

## Repaired on this branch

| File | Before | After intent |
|---|---|---|
| `START_HERE.md` | “carrier-grade-targeted” without a same-sentence denial | Still product-target language, plus explicit **not certified / not carrier-grade today** |
| `docs/phd/RQ_TO_REPO_EVIDENCE_MAP.md` | 2026-08-18 baseline presented as live status | Dated freeze; Paper II packs and ReadyGary FR2≠Sub-6 now match accepted main |

## Left in research repos (WIP cap)

| Repo | Quote | Class | Why not edited here |
|---|---|---|---|
| spectrumx-ai-ran-gary `README.md` | “Production-ready detection pipeline…” | unsupported / overclaim vs Limits row | Needs a **separate** scoped research-repo PR |
| 7gc `README.md` | “digital twins with validated metrics” | ambiguous | Aspirational; smoke is synthetic |

## Accurate / correctly scoped (keep)

- All six research README Limits rows: not operational 6G; not Oulu affiliation; not carrier-grade.
- ReadyGary **VALIDATED TODAY** row is labeled `SYNTHETIC_SIM` + independent reproduction pending.
- ReadyGary explicitly denies sub-ms edge inference and production-ready deployment.
- NTN README denies validated operator NTN performance.
- WAIKE README: partner execution `EXTERNAL_PENDING`.
- Edge I/O Pixel `PASS` is install/launch smoke; `HUMAN_QA_PENDING` is explicit.

## Absent as positive claims on accepted-main READMEs

`6G ready`, `field proven`, `pilot complete`, Nokia partnership, satellite attach, human tested, student tested, FCC/CE certified, manufacture ready.

Do not convert Pixel install smoke or synthetic CIs into physical or carrier evidence.
