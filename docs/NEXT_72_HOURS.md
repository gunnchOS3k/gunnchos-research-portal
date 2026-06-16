# Next 72 Hours

## Day 1 — Portfolio spine review

- Review [field-kit PR #1](https://github.com/gunnchOS3k/gunnchos-7gc-ai-ran-field-kit/pull/1)
- Review [portal hardening PR #4](https://github.com/gunnchOS3k/gunnchos-research-portal/pull/4)
- Check CI — see [HARDENING_REVIEW_STATUS.md](HARDENING_REVIEW_STATUS.md)
- Merge only if clean
- Update profile README via `role-proof-profile-readme` PR

## Day 2 — Agentic SecOps proof

- Validate IOC extraction demo on `gunnchAI3k` branch `role-proof-agentic-secops`
- Validate mock detection generation
- Walk through [FOR_AGENTIC_SECOPS_ROLES.md](FOR_AGENTIC_SECOPS_ROLES.md)
- Add screenshots to `gunnchAI3k/demo/screenshots/` (optional)
- Open / review draft PR

## Day 3 — Access Risk proof

- Validate access graph on `gunnchos-device-os` branch `role-proof-access-risk-intelligence`
- Validate least-privilege recommender
- Walk through [FOR_ACCESS_RISK_SECURITY_ROLES.md](FOR_ACCESS_RISK_SECURITY_ROLES.md)
- Open / review draft PR

## Day 4+ — RTL verification sprint

- Review `console_rtl_verification_lab/` on `eg3573-ece-6443-sram-bist-project`
- Run `check_required_files.py` and optional `iverilog` smoke
- Walk through [FOR_RTL_VERIFICATION_ROLES.md](FOR_RTL_VERIFICATION_ROLES.md)
- Open / review draft PR

## Ongoing

- Fix failing hardening CI on device-os, spectrumx, edge-io, ntn, 7gc-digital-twin
- Update [ROLE_PROOF_COMPLETION_REPORT.md](ROLE_PROOF_COMPLETION_REPORT.md) after each merge
