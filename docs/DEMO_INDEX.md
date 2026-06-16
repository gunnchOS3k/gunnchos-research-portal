# Demo Index

| Demo | Repo | Role lane | Status | How to run | Evidence |
|------|------|-----------|--------|------------|----------|
| Agentic SecOps mock triage | [gunnchAI3k](https://github.com/gunnchOS3k/gunnchAI3k) | Agentic SecOps | prototype | `python3 scripts/secops_mock_ioc_extractor.py` + pytest | [AGENTIC_SECOPS_ALIGNMENT](https://github.com/gunnchOS3k/gunnchAI3k/blob/main/docs/AGENTIC_SECOPS_ALIGNMENT.md) |
| Access risk graph | [gunnchos-device-os](https://github.com/gunnchOS3k/gunnchos-device-os) | Access Risk | prototype | `python3 security/access-risk/attack_path_model.py` | [risk_report_example.md](https://github.com/gunnchOS3k/gunnchos-device-os/blob/main/security/access-risk/risk_report_example.md) |
| RTL smoke verification lab | [eg3573-ece-6443-sram-bist-project](https://github.com/gunnchOS3k/eg3573-ece-6443-sram-bist-project) | RTL / UVM | prototype | `console_rtl_verification_lab/scripts/check_required_files.py` | [VERIFICATION_PLAN](https://github.com/gunnchOS3k/eg3573-ece-6443-sram-bist-project/blob/main/console_rtl_verification_lab/docs/VERIFICATION_PLAN.md) |
| Field-kit umbrella | [gunnchos-7gc-ai-ran-field-kit](https://github.com/gunnchOS3k/gunnchos-7gc-ai-ran-field-kit) | 6G / research | prototype | `python3 scripts/check_required_files.py` | [CLAIMS_TO_EVIDENCE](https://github.com/gunnchOS3k/gunnchos-7gc-ai-ran-field-kit/blob/main/CLAIMS_TO_EVIDENCE.md) |
| Scaly Wings multilingual console | [scaly-wings](https://github.com/gunnchOS3k/scaly-wings) | Device / education | real software | `npm run i18n:check` | [CONSOLE_SOFTWARE_ALIGNMENT](https://github.com/gunnchOS3k/scaly-wings/blob/main/docs/CONSOLE_SOFTWARE_ALIGNMENT.md) |
| Device OS architecture | [gunnchos-device-os](https://github.com/gunnchOS3k/gunnchos-device-os) | Device | prototype | `pytest -q` + launcher mock | [DEVICE_ARCHITECTURE](https://github.com/gunnchOS3k/gunnchos-device-os/blob/main/docs/DEVICE_ARCHITECTURE.md) |

All security demos use **mock/synthetic data only**.
