# Hardening Review Status

Review of portfolio-spine / console / mission / research hardening draft PRs. **Do not merge automatically** — Edmund review required.

| Repo | PR | Branch | Tier | CI status | Ready to merge | Blocker | Next action |
|------|-----|--------|------|-----------|----------------|---------|-------------|
| gunnchos-7gc-ai-ran-field-kit | [#1](https://github.com/gunnchOS3k/gunnchos-7gc-ai-ran-field-kit/pull/1) | `portfolio-spine-hardening` | L1 | SUCCESS | yes | none | Merge after spot-check umbrella README |
| gunnchos-research-portal | [#4](https://github.com/gunnchOS3k/gunnchos-research-portal/pull/4) | `portfolio-spine-hardening` | L3 | SUCCESS | yes* | role landing pages on separate PR | Merge #4 or supersede with role-proof PR |
| scaly-wings | [#1](https://github.com/gunnchOS3k/scaly-wings/pull/1) | `console-device-hardening` | L2 | SUCCESS | yes | none | Verify i18n unchanged; merge |
| gunnchos-device-os | [#20](https://github.com/gunnchOS3k/gunnchos-device-os/pull/20) | `console-device-hardening` | L2 | FAILURE | no | existing `test` job fails | Fix pytest/CI before merge; access-risk on new branch |
| gunnchos-hardware-industrial-design | [#25](https://github.com/gunnchOS3k/gunnchos-hardware-industrial-design/pull/25) | `console-device-hardening` | L2 | SUCCESS | yes | none | Merge after BOM doc review |
| spectrumx-ai-ran-gary | [#92](https://github.com/gunnchOS3k/spectrumx-ai-ran-gary/pull/92) | `research-artifact-hardening` | L1 | FAILURE | no | pytest/benchmark in CI | Fix test deps or scope CI to smoke |
| edge-io-measurement-node | [#17](https://github.com/gunnchOS3k/edge-io-measurement-node/pull/17) | `research-artifact-hardening` | L1 | FAILURE | no | `test` job fails | Diagnose pytest on branch |
| waike-research-ops | [#39](https://github.com/gunnchOS3k/waike-research-ops/pull/39) | `mission-community-hardening` | L3 | SUCCESS | yes | none | Merge after curriculum spot-check |
| gunnchAI3k | [#4](https://github.com/gunnchOS3k/gunnchAI3k/pull/4) | `mission-community-hardening` | L3 | SUCCESS | yes* | SecOps proof on new branch | Merge mission docs; open role-proof PR |
| ntn-resilience-sim | [#18](https://github.com/gunnchOS3k/ntn-resilience-sim/pull/18) | `research-artifact-hardening` | L1 | FAILURE | no | CI test failure | Fix tests |
| readygary-6g-beam-selection | [#21](https://github.com/gunnchOS3k/readygary-6g-beam-selection/pull/21) | `research-artifact-hardening` | L1 | SUCCESS | yes | none | Merge |
| 7gc-digital-twin | [#21](https://github.com/gunnchOS3k/7gc-digital-twin/pull/21) | `research-artifact-hardening` | L1 | FAILURE | no | CI test failure | Fix tests |
| 7gc-verticals-6g-use-case-lab | [#1](https://github.com/gunnchOS3k/7gc-verticals-6g-use-case-lab/pull/1) | `research-artifact-hardening` | L1 | SUCCESS | yes | none | Merge |
| gunnchOS3k-MLV-Hackathons | [#1](https://github.com/gunnchOS3k/gunnchOS3k-MLV-Hackathons/pull/1) | `mission-community-hardening` | L3 | SUCCESS | yes | none | Merge |
| gunnchOS3k-MLV-GameJam | [#1](https://github.com/gunnchOS3k/gunnchOS3k-MLV-GameJam/pull/1) | `mission-community-hardening` | L3 | SUCCESS | yes | none | Merge |
| EdgeGesture | [#1](https://github.com/gunnchOS3k/EdgeGesture-Fall-2025-Edge-AI-Qualcomm-Hackathon/pull/1) | `console-device-hardening` | L2 | — | review | not re-checked this pass | Spot-check |
| gunnchOS3k-MLV-open-Roles | [#1](https://github.com/gunnchOS3k/gunnchOS3k-MLV-open-Roles-and-Opportunities/pull/1) | `mission-community-hardening` | L3 | — | review | iCloud local path | Merge from GitHub branch |

## Required-file checker (local)

All 18 hardened repos passed `scripts/check_required_files.py` locally during the first hardening pass.

## Role-proof PRs (second pass)

See [ROLE_PROOF_COMPLETION_REPORT.md](ROLE_PROOF_COMPLETION_REPORT.md).
