# Portfolio readiness dashboard

Generated: 2026-08-18T18:16:56Z
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
| `gunnchos-device-os` | RQ1 | `core` | `cursor/supervisor-ready-portfolio-release-001` | `65c33a03fdfc` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `PHYSICAL_PENDING` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `gunnchos-hardware-industrial-design` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `68630a04c6d3` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `PHYSICAL_PENDING` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `archive-of-life-artifact-world` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `6419a35d1341` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `EMULATED` |
| `gunnchAI3k` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `9a659a6400cc` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `SYNTHETIC_SIM` |
| `waike-research-ops` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `554c364aa0ec` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `SYNTHETIC_SIM` |
| `anime-aggressors` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `050878b5e317` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `EMULATED` |
| `gunnchos-emergent-service-intent-protocols` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `7381de141836` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `pedestrian-pursuit` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `86d981c0e975` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `EMULATED` |
| `beatlink-party` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `206cb8501180` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `EMULATED` |
| `edge-io-measurement-node` | RQ3 | `core` | `cursor/supervisor-ready-portfolio-release-001` | `009f227d3257` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `PHYSICAL_PENDING` | `EXTERNAL_PENDING` | `HUMAN_QA_PENDING` | `EMULATED` |
| `gunnchos-research-portal` | — | `public` | `cursor/supervisor-ready-portfolio-release-001` | `9ca8635a89a4` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `ntn-resilience-sim` | RQ3 | `core` | `cursor/supervisor-ready-portfolio-release-001` | `e7ed8504e1e5` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `7gc-digital-twin` | RQ1 | `core` | `cursor/supervisor-ready-portfolio-release-001` | `86996b82e778` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `spectrumx-ai-ran-gary` | RQ2 | `core` | `cursor/supervisor-ready-portfolio-release-001` | `4ac16c4a1e8f` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `OPEN_DATA_BACKED` |
| `gunnchos-gpu-nr-baseband-platform` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `2a5c483fdeb6` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `BLOCKED_GPU` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `readygary-6g-beam-selection` | RQ2 | `core` | `cursor/supervisor-ready-portfolio-release-001` | `5ef9a4a65b3c` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |

## How to regenerate

```bash
make audit
```
