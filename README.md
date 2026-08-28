# gunnchOS3k research portal

Canonical **public entry** for the gunnchOS3k experimental computing and communications portfolio.

**Prospective doctoral supervisor (Communications Engineering / 6G Flagship fit, no affiliation claimed):** start at **[docs/phd/START_HERE_SUPERVISOR.md](docs/phd/START_HERE_SUPERVISOR.md)** (≈10 minutes).

This repository is a navigation and evidence-map control plane. It is not a RAN, not hardware proof, and not a University of Oulu appointment.

Working thesis: **Resilience-Aware Service Continuity in Heterogeneous 6G Networks: Cross-Layer Orchestration for Resource-Constrained Devices.**

| Audience | Start |
|---|---|
| Faculty / supervisor | [docs/phd/START_HERE_SUPERVISOR.md](docs/phd/START_HERE_SUPERVISOR.md) · [docs/phd/SUPERVISOR_10_MINUTE_PATH.md](docs/phd/SUPERVISOR_10_MINUTE_PATH.md) · [docs/phd/ARI_POUTTU_ONE_PAGE_CONCEPT.md](docs/phd/ARI_POUTTU_ONE_PAGE_CONCEPT.md) · [docs/oulu/FACULTY_EVIDENCE_FREEZE.md](docs/oulu/FACULTY_EVIDENCE_FREEZE.md) (2026-08-27) |
| Researcher | [audiences/RESEARCHER.md](audiences/RESEARCHER.md) · [docs/phd/RQ_TO_REPO_EVIDENCE_MAP.md](docs/phd/RQ_TO_REPO_EVIDENCE_MAP.md) |
| Curious / student / intern | [START_HERE.md](START_HERE.md) (product ecosystem path) |
| Developer | [audiences/DEVELOPER.md](audiences/DEVELOPER.md) |
| Manufacturer | [MANUFACTURING.md](MANUFACTURING.md) |

## What is real today

- Sixteen-repo map with dissertation roles (`portfolio/repo_roles.yaml`)
- Regenerable audit (`make audit`) and claim-boundary validator (`make test`)
- Honest gates: physical EVT/RF, independent reproduction, and human playtest remain pending where listed

## What is not proven

Simulations are not RF. Device Lab is not EVT silicon. Games are workloads unless a frozen RQ experiment uses them.

Dashboard: [docs/phd/PORTFOLIO_READINESS_DASHBOARD.md](docs/phd/PORTFOLIO_READINESS_DASHBOARD.md)  
UML: [docs/uml/README.md](docs/uml/README.md)  
Reproduce: [REPRODUCIBILITY.md](REPRODUCIBILITY.md)

```bash
make bootstrap
make reproduce
```

## Product ecosystem (supporting, not sixteen dissertations)

The Cycle 3A product information architecture remains for non-research readers: [START_HERE.md](START_HERE.md), [PRODUCT_FAMILY.md](PRODUCT_FAMILY.md), [STATUS.md](STATUS.md), [REPO_CATALOG.md](REPO_CATALOG.md). Product charter lives in [`gunnchos-7gc-ai-ran-field-kit`](https://github.com/gunnchOS3k/gunnchos-7gc-ai-ran-field-kit) `program/charter/` — **out of the 16-repo dissertation scope** except as charter reference.

Connectivity language: 5G-Advanced / NTN-capable architecture, IMT-2030-aligned — **not** standardized commercial 6G.

## History

Prior “research spine / 7gc as program hub” and product-only front door notes: [docs/history/](docs/history/), [docs/uml/legacy/](docs/uml/legacy/).
