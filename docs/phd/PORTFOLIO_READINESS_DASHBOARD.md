# Portfolio readiness dashboard

Generated: 2026-08-18T17:06:42Z
Generator: `scripts/audit_portfolio.py`
Branch context: live checkouts under `/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos`

This dashboard is **descriptive of the audited trees**. A passing test is not physical readiness.
A simulation is not RF performance. A generated RFQ packet is not a sent RFQ.

## Gates

```text
AUTOMATABLE_SUPERVISOR_READY = FAIL
CONTACT_SUPERVISOR_READY = BLOCKED
DIGITAL_MANUFACTURING_READY = FAIL
PIXEL_6A_READY = BLOCKED
CORE_RESEARCH_REPRODUCIBLE = BLOCKED
INDEPENDENT_REPRODUCTION = PENDING
```

## Repositories

| Repository | RQ | Class | Branch | Commit | UML | Digital | Physical | External | Human QA | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `gunnchos-device-os` | RQ1 | `core` | `tmp-image-fit` | `a1e11efcb502` | `PLACEHOLDER_README_ONLY` | `FAIL_DIGITAL` | `PHYSICAL_PENDING` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `gunnchos-hardware-industrial-design` | — | `supporting` | `stream/c-pkt-003-evt-firmware` | `39cf58ebf412` | `PLACEHOLDER_README_ONLY` | `FAIL_DIGITAL` | `PHYSICAL_PENDING` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `archive-of-life-artifact-world` | — | `supporting` | `stream/b-pkt-003-scientific-lifeling-expedition` | `6d55f6bbc535` | `MISSING` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `EMULATED` |
| `gunnchAI3k` | — | `supporting` | `stream/b-pkt-003-data-dashboards-mastery` | `1875d32ea5f9` | `MISSING` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `SYNTHETIC_SIM` |
| `waike-research-ops` | — | `supporting` | `stream/b-pkt-003-data-dashboards-digital-rc` | `ecf43ac5030b` | `PLACEHOLDER_README_ONLY` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `SYNTHETIC_SIM` |
| `anime-aggressors` | — | `supporting` | `stream/b-pkt-002-playtest-polish` | `36e7f0257496` | `MISSING` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `EMULATED` |
| `gunnchos-emergent-service-intent-protocols` | — | `supporting` | `cursor/oulu-publication-grade-science` | `785d35d3973d` | `MISSING` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `pedestrian-pursuit` | — | `supporting` | `stream/b-pkt-001-playtest-polish` | `c34f7d960422` | `MISSING` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `EMULATED` |
| `beatlink-party` | — | `supporting` | `main` | `4fc8fe017634` | `MISSING` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `EMULATED` |
| `edge-io-measurement-node` | RQ3 | `core` | `main` | `a1cd2e95c62e` | `PLACEHOLDER_README_ONLY` | `FAIL_DIGITAL` | `PHYSICAL_PENDING` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `EMULATED` |
| `gunnchos-research-portal` | — | `public` | `cursor/supervisor-ready-portfolio-release-001` | `88a6e7251bbd` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `ntn-resilience-sim` | RQ3 | `core` | `cursor/corrective-depth-gates-4-6` | `7ec94c219237` | `PLACEHOLDER_README_ONLY` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `7gc-digital-twin` | RQ1 | `core` | `cursor/corrective-depth-gates-4-6` | `62126f700db4` | `PLACEHOLDER_README_ONLY` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `spectrumx-ai-ran-gary` | RQ2 | `core` | `cursor/corrective-depth-gates-4-6` | `c7e2905f4bc4` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `OPEN_DATA_BACKED` |
| `gunnchos-gpu-nr-baseband-platform` | — | `supporting` | `cursor/nvidia-real-nr-aerial-depth` | `3730f236c7d4` | `MISSING` | `FAIL_DIGITAL` | `BLOCKED_GPU` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `readygary-6g-beam-selection` | RQ2 | `core` | `cursor/corrective-depth-gates-4-6` | `525405cb19d7` | `PLACEHOLDER_README_ONLY` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |

## How to regenerate

```bash
make audit
```
