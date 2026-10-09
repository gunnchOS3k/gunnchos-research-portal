# V1 readiness — 2026-10-04

Historical snapshot, superseded for current V1 decisions by the [October 9 full-scope ledger](V1_0_0_READINESS_2026-10-09.md). Preserve this evidence; its gold-slice criteria, older source pins and open-PR notes are not current release authority.

This board records what was checked in the convergence pass after gunnchOS site PR #10. It is not a release authorization. `v1.0.0-rc.1` remains the published release candidate. RC2 was not cut. `V1_0_0_RELEASE_AUTHORIZED=false`.

No domain below is a substitute for another domain.

| Domain | Accepted main SHA | Live / deployed SHA | Automated | Human | Blocking issue | Next action | V1 required |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PUBLIC_SITE | `4ce91d3fdded63db315b694c5988ae78c738d0c2` | Worker `gunnchos-site` version `238da4d3-e5cf-4d65-ae60-13f9ba57f034`, message `Deploy_exact_main_4ce91d3` | Lint, unit, secret scan, Next build, OpenNext build, public Playwright (55 passed, 9 skipped), and the closed-production harness passed on that SHA before deploy. Live smoke: home, labs, week 1 = 200; submit has no file input; preview route 404; POST submissions 403 `submissions_disabled`; gallery empty. | Not a human visual sign-off. | Live homepage title is still `gunnchOS · gunnchOS`. Contact still has the old Workspace sentence until PR #15 lands. | Owner reviews https://github.com/gunnchOS3k/gunnchos-site/pull/15 after site-ci. Do not treat that PR as merged. | yes |
| OPEN_LAB | same site SHA `4ce91d3fdded63db315b694c5988ae78c738d0c2` | same production worker | Week 1 YouTube order on the live page: `HXBNt8JJAb0`, `3aoVQ8h7FUc`, `hAbFGw2Dk20`, `eF1nR85cEzs`, playlist `PLULQocxqXUns`. Twitch VOD `2889378579` remains. Chrome and Safari click-to-load used `autoplay=false` and a direct Twitch link. Instagram and Facebook in-app browsers showed the fallback, a direct link, copy, and browser help, and no Twitch iframe. | Legal review is not complete. | Public uploads stay off. `PUBLIC_SUBMISSIONS_ENABLED=false`. `PRODUCTION_UPLOAD_FORM_VISIBLE=false`. `SHOWCASE_PUBLICATION_ENABLED=false`. `LEGAL_REVIEW_COMPLETE=false`. `CLOUDFLARE_ACCESS_CONFIGURED=false`. | Owner decides later whether submissions should ever open. This pass does not enable them. | yes |
| 3K_MLV | `a10cfe7535cde6508699735930378a2801fa31f4` | `https://mlv.gunnchos.com/` returned HTTP 200. The deployed git SHA was not read from the page. This pass did not deploy MLV. | PR #9 head `47cdb5b3902a9e3004228a30b17a44090c6c3370` is still an open draft and `CONFLICTING`. It was not merged and was not reconciled. | `HUMAN_7GC_SPATIAL_FIDELITY_PASS=false`. `HUMAN_LOCAL_IDENTITY_PASS=false`. `HUMAN_CAMPUS_USABILITY_PASS=false`. `PIXEL_7GC_CAMPUS_PASS=false`. | Gold slice for Commons, Home, Gallery, and Gary is not done on current main. | A later pass reconciles PR #9 onto `a10cfe75` without a second movement runtime, then the owner reviews the walk. | yes |
| WAIKE | `gunnchos-waike-learning-platform` `90fb9c5ceab51d99dfff7b5e6d1775fd1dca85d6` | `https://learn.gunnchos.com/` returned HTTP 200. Live SHA was not proven equal to that main. | Host responded. A course walk was not run. | `V1_WAIKE_HUMAN_PASS=false`. | No human campus sign-off in this pass. | Owner smoke of the public campus when a human review is scheduled. | yes |
| ANIME_AGGRESSORS | `887e100114c9741ebc7a449b46116bcb6eef5072` (merge of PR #121) | Live `https://anime.gunnchos.com/runtime-manifest` pins runtime `0188ea458dce77ba322e7e1fede841f216c004f0`. | Manifest: `release_channel=DEVELOPMENT`, `acceptedMain=true`, `FINAL_CHARACTER_ART_PASS=false`, `HUMAN_ART_APPROVAL=false`. | `ANIME_FINAL_ART_V1_PASS=false`. `V1_ANIME_HUMAN_PASS=false`. | Final character art is not approved. | Owner art approval is a separate gate. Do not install a placeholder on a Pixel as final art. | yes |
| PEDESTRIAN_PURSUIT | `f1c1a4cec80e2708baf5e3367f952eb9dae26b26` (merge of PR #40) | Live development runtime `8eeb5051d70fab7fc9339a1fef6272e943df1be1` at `https://pursuit.gunnchos.com/runtime/8eeb5051d70fab7fc9339a1fef6272e943df1be1/index.html`. | The page returned 200 and showed `DEVELOPMENT BUILD 8eeb5051d70f`. No page error in that short load. Race Now, countdown, driving, checkpoints, and lap 1 were not observed. | `HUMAN_COURSE_APPROVAL=false`. `HUMAN_FUN_APPROVAL=false`. `V1_PURSUIT_HUMAN_PASS=false`. | Exact-main race acceptance did not pass in this pass. | Owner or a later browser session completes one lap on this runtime before any fun approval. | yes |
| DEVICE_OS | `2ae070fd8b050c3520ed8dac211e0d607bf9f63f` | Not deployed by this pass. | Not re-run here. | No new human device sign-off. | Older device-lab notes in `release/RELEASE_BLOCKERS.md` are not rewritten by this file. | Do not treat this board as a device-lab pass. | yes |
| HARDWARE_DIGITAL | `af5af66a28e36351b3929ef15756b6df6381ff6a` | Public site shows four concept models. Labels stay digital concept model, placeholder geometry, physical validation pending. | Public viewer shipped inside site `4ce91d3f`. | Physical validation is not claimed. | Student 14.5 still has a disconnected fragment in the source mesh. Site PR #15 records the follow-up and does not repair the STL. | Repair the mesh in `gunnchos-hardware-industrial-design`, not in the site repo. | yes |
| RESEARCH | Portal `3f3d07b9996fab50a538a96035b96f2d40154a80` (PR #52 merged). SpectrumX `48eeacb7440af3a72966f3c4d5288d15c7de9617` (PR #106 merged). | `https://gunnchos.com/research/ai-ran` includes Demo, Architecture/UML, Source, Reproduce, and Citation where that repo has them, and states `measured_topology=false`. | Those two PRs were already merged. They were not reopened. | No new measured-topology claim. | Missing diagrams stay missing. Draft UML stays draft. | Keep evidence links only where the artifact exists. | yes |
| 7GC | `1a5491bf9261f77a75cc0fa7edbb5f25b425c7aa` | Not a separate production deploy in this pass. | Not re-measured. | `measured_topology` stays false unless a repo already records a real topology. | No physical or RF validation. | Do not describe the twin as a measured network. | yes |
| PIXEL_DEVICE | none accepted as a V1 device candidate in this pass | not installed | not run | `V1_PIXEL_ACCEPTANCE_PASS=false` | No Pixel install was performed. | Owner device acceptance when a candidate build exists. | yes |
| HUMAN_ACCEPTANCE | n/a | n/a | n/a | MLV, Anime, Pursuit, and WAIKE human gates are false. | Human review is still open on the world, the games, and the campus. | Owner visual, fun, and usability review. CI does not grant it. | yes |
| RELEASE | Portal main `3f3d07b9996fab50a538a96035b96f2d40154a80`. Published candidate remains `releases/v1.0.0-rc.1`. | Production site worker above. No RC2 tag. | `RC2_READY=false`. `RC2_PUBLISHED=false`. | `V1_0_0_RELEASE_AUTHORIZED=false`. | MLV gold slice, Pursuit lap, Pixel acceptance, and the public-copy PR are not done. | Owner authorizes any later RC or V1 explicitly. | yes |

## Gates from this pass

```text
V1_AUTOMATED_PIPELINE_PASS=false
V1_PUBLIC_SITE_PASS=false
V1_MLV_HUMAN_PASS=false
V1_ANIME_HUMAN_PASS=false
V1_PURSUIT_HUMAN_PASS=false
V1_WAIKE_HUMAN_PASS=false
V1_PIXEL_ACCEPTANCE_PASS=false
RC2_READY=false
RC2_PUBLISHED=false
V1_0_0_RELEASE_AUTHORIZED=false
```

`V1_PUBLIC_SITE_PASS` stays false because the live site still shows the duplicate homepage title and the stale contact sentence. The closed-upload deploy itself succeeded.

`V1_AUTOMATED_PIPELINE_PASS` stays false because MLV PR #9 is conflicting, Pursuit lap acceptance was not observed, and site PR #15 CI was still running when this note was written.
