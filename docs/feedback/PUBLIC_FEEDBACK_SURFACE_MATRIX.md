# Public feedback surface matrix

Generated: 2026-09-21T21:12:46Z

Post-feedback accepted-main revalidation. Canonical hub live via portal #40: `https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md`.

All V1 components must reach **PASS** before final `v1.0.0` (or owner waiver).

| Component | Public-facing surface | Feedback link present | Link target | Security path present | Release-note link present | README link present | V1 status | Evidence |
|---|---|---|---|---|---|---|---|---|
| Portal | FEEDBACK.md + issue forms | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | yes | yes | PASS | portal #40 @ 5e4141db + freeze merge |
| Portal front doors | START_HERE / audiences | yes | FEEDBACK.md | yes | n/a | yes | PASS | secondary CTA |
| Device OS | Settings → About | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #164 @ 2218ead0 |
| WAIKE LP | Footer + Help/About | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #24 @ a4daa1d0 |
| gunnchAI | Hub feedback links | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #57 @ 04eef2d8 |
| Anime | Settings / Results | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #105 @ 6cd1b310 |
| Pedestrian | Results / Settings | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #31 @ 3e981069 |
| Archive | Settings | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #41 @ 03d73445 |
| BeatLink | Host + Player | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #31 @ e1a5d999 |
| Hardware industrial | FEEDBACK.md + README | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #85 @ af5af66a |
| Edge IO | FEEDBACK.md + README | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #40 @ 758b14a2 |
| Field kit | FEEDBACK.md | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #119 @ 4f3095e3 (origin/main) |
| Digital Twin | FEEDBACK.md + README | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #32 @ 9654ac82 |
| SpectrumX | FEEDBACK.md + README | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #103 @ 2dc41c73 |
| ReadyGary | FEEDBACK.md + README | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #28 @ e04b38b4 |
| NTN | FEEDBACK.md + README | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #29 @ 05aaa9ae |
| waike-research-ops | FEEDBACK.md + README | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | #62 @ 34ae043a |
| Curriculum (WAIKE packs) | WAIKE FEEDBACK + portal | yes | https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md | yes | pending | yes | PASS | via WAIKE + ops |

## Final V1 rule

RC1: public front door PASS is sufficient. Final v1.0.0: every row PASS or explicitly waived.

## Audit notes

- No freeze-branch FEEDBACK URLs in product code (validate_feedback_urls PASS on freeze tree).
- Live PVR: portal enabled=true; Device OS enabled=true.
