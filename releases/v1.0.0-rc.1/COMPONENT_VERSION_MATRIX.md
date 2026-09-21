# Component Version Matrix — gunnchOS Ecosystem v1.0.0-rc.1

Generated: `2026-09-21T15:16:58Z`

Authority: live `origin/main` only. No branch tip substitutes for accepted main.

| Lane | Component | Accepted main SHA | Recovered child(ren) | Open PRs (class) |
|---|---|---|---|---|
| Core | `gunnchos-research-portal` | `ff1325a1a65ebfae5aab5532dcd05876fa643240` | — | #38:STALE, #37:STALE |
| Core | `gunnchos-device-os` | `c6fd04aced44b0d3eec6f07c3b0b3fdbe50ad7a4` | — | none |
| Core | `gunnchos-waike-learning-platform` | `c306543ccc89fb0304734d0ebbaa94f8a0b19c1d` | `efe21df092c7…` | none |
| Core | `waike-research-ops` | `e919976237cb67e26582b1da7caf975d6f35d883` | `63ba9f25ac6b…` | none |
| Core | `gunnchAI3k` | `ef665648aecb06230ecf7017065861b148e19c35` | `d4a5c6d857c3…`, `e2d1adcb5847…` | none |
| Hardware | `gunnchos-hardware-industrial-design` | `56125d1738a437f413ee4418c51c2f3a82bcbac8` | — | #84:OUTSIDE_RC1, #79:EXPERIMENTAL, #78:EXPERIMENTAL, #77:EXPERIMENTAL, #76:EXPERIMENTAL, #75:EXPERIMENTAL (+6) |
| Research | `edge-io-measurement-node` | `af57fbdac857ae386b23b5b747fdc05797621f92` | — | #39:OUTSIDE_RC1, #18:OUTSIDE_RC1, #17:OUTSIDE_RC1, #16:OUTSIDE_RC1, #8:OUTSIDE_RC1 |
| Research | `gunnchos-7gc-ai-ran-field-kit` | `9e93e41a3b16b009c9cc5163b775360d4d2ef693` | — | #75:OUTSIDE_RC1, #71:OUTSIDE_RC1, #1:OUTSIDE_RC1 |
| Research | `7gc-digital-twin` | `dc43a567e3f2e81a5b59fea6dd67c7054cfdde56` | — | #29:OUTSIDE_RC1, #23:OUTSIDE_RC1 |
| Research | `spectrumx-ai-ran-gary` | `9060655e724374f60cbbb86832816c9c2d332ca4` | — | #99:OUTSIDE_RC1, #93:OUTSIDE_RC1, #92:OUTSIDE_RC1, #91:OUTSIDE_RC1, #83:OUTSIDE_RC1 |
| Research | `readygary-6g-beam-selection` | `569875224db7812890ec6abc48dfe43a608094f3` | — | #22:OUTSIDE_RC1, #21:OUTSIDE_RC1, #20:OUTSIDE_RC1, #12:OUTSIDE_RC1 |
| Research | `ntn-resilience-sim` | `c4215fc1039f5452917b9b2034b42e03fdc13689` | — | #26:OUTSIDE_RC1, #20:OUTSIDE_RC1, #10:OUTSIDE_RC1 |
| Experiences | `anime-aggressors` | `649b20f422b31bba2af9bf0c5c1b2b555c9a4a40` | `106e92e31bae…` | none |
| Experiences | `pedestrian-pursuit` | `d91f102f251ef67d536d2f95188de7d627701902` | `622ed74d2dfc…` | none |
| Experiences | `archive-of-life-artifact-world` | `7b3e2e51782541a1a2d2896fc317a5e41e9db8f8` | `a095d90aa339…` | none |
| Experiences | `beatlink-party` | `acdeb77bdf01c40a0e78f4adae6c119752ca5cca` | `3fd2a2acf1af…` | none |

## Ancestry

**RECOVERED_CHILD_ANCESTRY_PASS** = `True`

## Hardware classification

- V1 class: `DIGITAL_HARDWARE_ENGINEERING_RELEASE`
- PR #84: OUTSIDE V1
- PRs #69–#79: EXPERIMENTAL / OUTSIDE V1 mainline
- No READY_FOR_FAB / EVT / DVT / PVT / certification claims

## Freeze rule

No new features enter RC1 after gates pass. Only release-blocking, packaging, claim, privacy/security, and install/demo fixes.
