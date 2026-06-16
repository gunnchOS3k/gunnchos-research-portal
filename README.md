# gunnchos Research Portal

**Public front door** for the [gunnchOS3k](https://github.com/gunnchOS3k) portfolio — a research + product + education ecosystem for digital-equity wireless learning, phone-first field consoles, and builder empowerment.

> Markdown-first portal. Optional Next.js site later. **Not** a commercial product catalog or carrier deployment platform.

---

## Start here

| Doc | Purpose |
|-----|---------|
| [docs/PORTFOLIO_MAP.md](docs/PORTFOLIO_MAP.md) | Full repo index by tier and spine |
| [docs/RESEARCH_SPINE.md](docs/RESEARCH_SPINE.md) | IMT-2030-aligned research chain |
| [docs/DEVICE_SPINE.md](docs/DEVICE_SPINE.md) | Console / device software chain |
| [docs/EDUCATION_SPINE.md](docs/EDUCATION_SPINE.md) | WAIKE + tutor + community chain |
| [MISSION_ALIGNMENT.md](MISSION_ALIGNMENT.md) | Mission pillars and safe language |
| [CLAIMS_TO_EVIDENCE.md](CLAIMS_TO_EVIDENCE.md) | Portfolio-level evidence matrix |
| [REPRODUCIBILITY.md](REPRODUCIBILITY.md) | How to verify docs and CI across repos |
| [docs/ROLE_FIT_OVERVIEW.md](docs/ROLE_FIT_OVERVIEW.md) | **Role-specific proof paths** (SecOps, Access Risk, RTL) |
| [docs/DEMO_INDEX.md](docs/DEMO_INDEX.md) | Runnable mock demos index |
| [docs/HARDENING_REVIEW_STATUS.md](docs/HARDENING_REVIEW_STATUS.md) | Draft PR / CI review tracker |

---

## Portfolio spines

### Research spine (Level 1)

```text
gunnchos-7gc-ai-ran-field-kit  (umbrella)
  → spectrumx-ai-ran-gary
  → edge-io-measurement-node
  → 7gc-digital-twin
  → ntn-resilience-sim
  → readygary-6g-beam-selection
  → gunnchos-7gc-verticals-6g-use-case-lab
```

Umbrella: [gunnchos-7gc-ai-ran-field-kit](https://github.com/gunnchOS3k/gunnchos-7gc-ai-ran-field-kit)

### Device spine (Level 2)

```text
gunnchos-device-os
  → gunnchos-hardware-industrial-design
  → gunnchOS3k-MLV-Arcade
  → scaly-wings
  → EdgeGesture-Fall-2025-Edge-AI-Qualcomm-Hackathon
```

### Education spine (Level 3)

```text
waike-research-ops
  → gunnchAI3k
  → gunnchOS3k-MLV-Hackathons
  → gunnchOS3k-MLV-GameJam
  → gunnchOS3k-MLV-open-Roles-and-Opportunities
```

### Public portal spine

```text
gunnchos-research-portal (this repo)
  → edmundgunnjr.github.io
  → GitHub profile / org
```

---

## What is real today

- Open GitHub repos with documented scope (real vs synthetic vs planned)
- CI smoke validation and `scripts/check_required_files.py` on hardened repos
- Synthetic benchmarks and schema-validated telemetry examples (research spine)
- Multilingual console software in [scaly-wings](https://github.com/gunnchOS3k/scaly-wings) (en/ar/fr/es/fi)
- Education ops scaffolding in [waike-research-ops](https://github.com/gunnchOS3k/waike-research-ops)

## What is synthetic / prototype-only

- AI-RAN ablation tables, emulator telemetry, digital-twin demo scenes
- Device OS launcher mock — not a shipping OS image
- Tutor demo sessions — not credentialed instruction replacement
- Publication / DOI tracker placeholders

## What is planned

- Opt-in field campaigns with ethics review
- Zenodo DOI releases (umbrella + components)
- Community partner pilots (digital-equity deployment pathway)
- Console hardware prototype fabrication gate

## What is not claimed

- Commercial 6G or carrier-grade AI-RAN infrastructure
- Certified hardware or finished gunnchOS3k console product
- Citywide deployment or proven educational impact at scale
- Unauthorized RF transmission or private payload collection

---

## Evidence discipline

- [docs/EVIDENCE_STANDARD.md](docs/EVIDENCE_STANDARD.md)
- [docs/PUBLICATION_TRACKER.md](docs/PUBLICATION_TRACKER.md)
- [docs/DOI_AND_RELEASE_TRACKER.md](docs/DOI_AND_RELEASE_TRACKER.md)
- [docs/CONTRIBUTOR_ONBOARDING.md](docs/CONTRIBUTOR_ONBOARDING.md)

---

## Citation

See [CITATION.cff](CITATION.cff). Zenodo DOI: **planned**.

## License

MIT — see [LICENSE](LICENSE).
