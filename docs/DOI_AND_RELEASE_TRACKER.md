# DOI and Release Tracker

| Repo | GitHub release | Zenodo DOI | CITATION.cff | Priority |
|------|----------------|------------|--------------|----------|
| gunnchos-7gc-ai-ran-field-kit | planned | planned | present | P0 umbrella |
| spectrumx-ai-ran-gary | planned | planned | present | P1 |
| edge-io-measurement-node | planned | planned | present | P1 |
| 7gc-digital-twin | planned | planned | present | P2 |
| ntn-resilience-sim | planned | planned | present | P2 |
| readygary-6g-beam-selection | planned | planned | present | P2 |
| gunnchos-7gc-verticals-6g-use-case-lab | planned | planned | present | P2 |
| gunnchos-research-portal | planned | planned | present | P1 meta |
| scaly-wings | planned | planned | present | P2 console software |
| waike-research-ops | planned | planned | present | P2 education |

## Release checklist (per repo)

- [ ] `scripts/check_required_files.py` passes
- [ ] CI green on default branch
- [ ] CLAIMS_TO_EVIDENCE.md reviewed for overclaims
- [ ] Tag `v0.1.0-artifact` (or similar)
- [ ] Zenodo upload from GitHub integration
- [ ] Update CITATION.cff with `doi:`

## Umbrella-first strategy

Release **gunnchos-7gc-ai-ran-field-kit** as citation hub linking component DOIs.
