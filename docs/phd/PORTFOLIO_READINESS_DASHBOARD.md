# Portfolio readiness dashboard

Generated: 2026-08-19T20:53:05Z
Generator: `scripts/audit_portfolio.py`
Branch context: live checkouts under `/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos`

This dashboard is **descriptive of the audited trees**. A passing test is not physical readiness.
A simulation is not RF performance. A generated RFQ packet is not a sent RFQ.

## Gates

```text
AUTOMATABLE_SUPERVISOR_READY = FAIL
CONTACT_SUPERVISOR_READY = BLOCKED
DIGITAL_MANUFACTURING_READY = FAIL
PIXEL_6A_READY = PASS
CORE_RESEARCH_REPRODUCIBLE = BLOCKED
INDEPENDENT_REPRODUCTION = PENDING
```

## Repositories

| Repository | RQ | Class | Branch | Commit | UML | Digital | Physical | External | Human QA | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `gunnchos-device-os` | RQ1 | `core` | `cursor/supervisor-ready-portfolio-release-001` | `65c33a03fdfc` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `PHYSICAL_PENDING` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `gunnchos-hardware-industrial-design` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `5a93e261fdd8` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `PHYSICAL_PENDING` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `archive-of-life-artifact-world` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `02192669e61d` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `EMULATED` |
| `gunnchAI3k` | — | `supporting` | `cursor/gunnchai-digital-product-completion-001` | `85d55568207f` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `SYNTHETIC_SIM` |
| `waike-research-ops` | — | `supporting` | `cursor/waike-post53-ci-hygiene-001` | `0c627ab700cf` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `SYNTHETIC_SIM` |
| `anime-aggressors` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `6d3f1fa3617e` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `EMULATED` |
| `gunnchos-emergent-service-intent-protocols` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `7381de141836` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `pedestrian-pursuit` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `409566d66e5d` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `EMULATED` |
| `beatlink-party` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `dcb5a916a92c` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `HUMAN_QA_PENDING` | `EMULATED` |
| `edge-io-measurement-node` | RQ3 | `core` | `cursor/supervisor-ready-portfolio-release-001` | `3c5606751be4` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `PHYSICAL_PENDING` | `EXTERNAL_PENDING` | `HUMAN_QA_PENDING` | `EMULATED` |
| `gunnchos-research-portal` | — | `public` | `cursor/final-accepted-main-portal-hygiene` | `e60705b8b3cd` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `ntn-resilience-sim` | RQ3 | `core` | `cursor/supervisor-ready-portfolio-release-001` | `f2b48a826a42` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `7gc-digital-twin` | RQ1 | `core` | `cursor/supervisor-ready-portfolio-release-001` | `376b6d673ff6` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `spectrumx-ai-ran-gary` | RQ2 | `core` | `cursor/supervisor-ready-portfolio-release-001` | `20f40f15753a` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `NOT_APPLICABLE` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `OPEN_DATA_BACKED` |
| `gunnchos-gpu-nr-baseband-platform` | — | `supporting` | `cursor/supervisor-ready-portfolio-release-001` | `2a5c483fdeb6` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `DIGITAL_PASS` | `BLOCKED_GPU` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |
| `readygary-6g-beam-selection` | RQ2 | `core` | `cursor/readygary-accepted-main-ci-hygiene-001` | `7150384f73f4` | `STRUCTURED_CURRENT_FUTURE_LEGACY` | `FAIL_DIGITAL` | `NOT_APPLICABLE` | `EXTERNAL_PENDING` | `NOT_APPLICABLE` | `SYNTHETIC_SIM` |

## How to regenerate

```bash
make audit
```
