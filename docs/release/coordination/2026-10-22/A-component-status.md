# A. Current 16-component V1 status matrix

Official V1.0.0 is **NOT READY** and **NOT AUTHORIZED**. RC2 is **NOT READY** and **NOT AUTHORIZED**.

This table does not replace `docs/release/campaigns/2026-10-19/RELEASE_MATRIX.json`. Classifications, accepted-main SHAs, RC1 pins, and post-RC1 counts are copied from that accepted matrix. October 22 notes are additive. No component is GREEN. Count: **16**.

| Repository | Accepted classification | Accepted main | RC1 source | Post-RC1 commits | October 22 additive note |
|---|---|---|---|---|---|
| gunnchos-research-portal | YELLOW | `1cd5819b446a` | `bfb211ecfbdd` | 19 | Control-plane tip is draft PR #55 at 1f4ca20, not accepted main. This coordination branch does not merge it. |
| gunnchos-device-os | YELLOW | `2ae070fd8b05` | `438aaf2b54d3` | 44 | Still YELLOW. No physical target in this pass. RC1 source/APK discrepancy remains. |
| gunnchos-waike-learning-platform | RED | `2641042936f3` | `a4daa1d07a3e` | 8 | Still RED. No new trusted-live evidence. |
| gunnchAI3k | YELLOW | `e08b68bdbc26` | `04eef2d891a8` | 2 | No new source audit in this pass. October 19 remaining acceptance still applies. |
| anime-aggressors | RED | `887e100114c9` | `6cd1b3100a7e` | 80 | Still RED. Codex tip 7c25c299 is unmerged PR #123. Cursor drafts #124–#130 are unmerged and do not close B02. |
| pedestrian-pursuit | YELLOW | `957ff95b89d0` | `3e9810693978` | 30 | Still YELLOW. Draft #42 is a finding only and stays unmerged. |
| archive-of-life-artifact-world | RED | `23ce4dafc271` | `03d734453f04` | 4 | Still RED. No approved acquisition. |
| beatlink-party | RED | `e15bc30856c6` | `e1a5d9998f93` | 2 | Still RED. Public party server remains a recorded failure. No new two-client proof. |
| gunnchos-hardware-industrial-design | YELLOW | `af5af66a28e3` | `af5af66a28e3` | 0 | No new source audit in this pass. October 19 remaining acceptance still applies. |
| 7gc-digital-twin | YELLOW | `1a5491bf9261` | `9654ac82a722` | 2 | No new source audit in this pass. October 19 remaining acceptance still applies. |
| spectrumx-ai-ran-gary | YELLOW | `48eeacb7440a` | `2dc41c73fa0b` | 9 | No new source audit in this pass. October 19 remaining acceptance still applies. |
| readygary-6g-beam-selection | YELLOW | `e04b38b48cd2` | `e04b38b48cd2` | 0 | No new source audit in this pass. October 19 remaining acceptance still applies. |
| ntn-resilience-sim | YELLOW | `05aaa9aec168` | `05aaa9aec168` | 0 | No new source audit in this pass. October 19 remaining acceptance still applies. |
| edge-io-measurement-node | YELLOW | `f357b4c0fcfa` | `758b14a2c06b` | 2 | No new source audit in this pass. October 19 remaining acceptance still applies. |
| waike-research-ops | RED | `34ae043abbd3` | `34ae043abbd3` | 0 | Still RED. 18-track program remains incomplete. |
| gunnchos-7gc-ai-ran-field-kit | RED | `9dfc32664788` | `4f3095e349f5` | 8 | Still RED. Candidate 92d0864 stays undispatched. Accepted-main watch is not repaired. |

YELLOW count in the accepted matrix: 10. RED count: 6. GREEN count: 0. Website, 3k MLV, and Technology Landscape remain integration surfaces under existing contracts. They are not added as RC1 members.

Canonical RC1 membership is `releases/v1.0.0-rc.1/FINAL_ACCEPTED_MAIN_MANIFEST.json`.
