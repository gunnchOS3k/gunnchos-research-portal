# October 19 release recovery and acceptance

**Official V1.0.0 is not eligible. RC2 is not ready or authorized.** October 23 remains the fourth-anniversary target. Required scope and outstanding gates have not been reduced or passed.

## Recovered authority

Accepted portal main is `1cd5819b446a8ba0e0e4d0c24a0305dee4a86e2c`. PR #54 adopted the immutable October 9 baseline: 108 features, 38 gate definitions and 43 tickets. This campaign adds rolling revision 2, leaving the dated documents, evidence and both baseline validators unchanged. The October 4 board is historical.

The canonical RC1 manifest at `releases/v1.0.0-rc.1/FINAL_ACCEPTED_MAIN_MANIFEST.json` defines exactly 16 components. The website, 3k MLV and Technology Landscape are additional integration surfaces under existing contracts, not invented RC1 members. The eight-edition library is preserved and inspected; its original optional-but-tracked disposition is unchanged. Any claim to release that library requires all eight editions and their own approval gates.

Recovery found 395 registered worktree entries, including 147 with dirty or untracked work. Missing/prunable entries were recorded, not removed. The newer separate publication clone was also inspected. Complete local paths/status and working-diff hashes are preserved under workspace `artifacts/v1-integration-2026-10-19/`. This inventory does not claim to discover arbitrary unregistered folders. Chat-history tools were unavailable; actual Git/source/report outputs were recovered instead. No specialized agent checkout was reset or cleaned.

## Canonical 16-component release matrix

GREEN requires required technical evidence and applicable owner approvals. No component receives GREEN solely from CI. YELLOW means meaningful functionality with a defined remaining requirement; RED identifies a required failure or gap. Physical manufacturing exclusions do not become hidden software waivers.

| Repository | State | Accepted main | Actual RC1 tag source | Commits since RC1 | CI success/failure | Remaining acceptance |
|---|---|---|---|---|---|---|
| gunnchos-research-portal | YELLOW | `1cd5819b446a8ba0e0e4d0c24a0305dee4a86e2c` | `bfb211ecfbdd486eed2602c32a5636eb419d4740` | 19 | 1/0 | owner/release gates; exact RC2 freeze absent |
| gunnchos-device-os | YELLOW | `2ae070fd8b050c3520ed8dac211e0d607bf9f63f` | `438aaf2b54d3365d681dd6eeeb73f6ac58663acc` | 44 | 42/0 | no connected physical Android target; final current-pin candidate matrix and RC1 source discrepancy |
| gunnchos-waike-learning-platform | RED | `2641042936f3b965daccb11091c80cbc6fa64f91` | `a4daa1d07a3ef8f6c00cf2b4a1692053bf99f518` | 8 | 77/0 | deployed Lessons returns Home; full 18-track practical/assessment/offline/native and educational gates open |
| gunnchAI3k | YELLOW | `e08b68bdbc26715a903bca51a9740f621a3b2dd6` | `04eef2d891a8dda58455acc58a8e93e7865379b8` | 2 | 29/0 | supported real provider/workflow and human evaluation remain required; no universal AI claim |
| anime-aggressors | RED | `887e100114c9741ebc7a449b46116bcb6eef5072` | `6cd1b3100a7e467c2c991394576891660deb1162` | 80 | 27/0 | full ordinary seven-route/roster/forms/acting/OVA/export/device/human gates open; public runtime older0188ea4 |
| pedestrian-pursuit | YELLOW | `957ff95b89d0516855ea61ddba19224a0583c3f8` | `3e98106939786c69a64657f4cc2b9a652a3b5fec` | 30 | 5/0 | no full lap/all-eight-course/mode/item/invite matrix or human/Pixel approval in this campaign |
| archive-of-life-artifact-world | RED | `23ce4dafc2711449cab43a5bb6f42698c61ed2a1` | `03d734453f040e3081e763277e2c15aa62ef095e` | 4 | 4/0 | full authoritative known-life/ICS coverage and maps still unproven; external sources/licenses/scientific review open |
| beatlink-party | RED | `e15bc30856c67c508ab0c56b401e05eb34a58595` | `e1a5d9998f93d707440f68673c0da844617dc10e` | 2 | 4/0 | public site states room server unavailable and party creation disabled; rights-safe full party/invites and human session not accepted |
| gunnchos-hardware-industrial-design | YELLOW | `af5af66a28e36351b3929ef15756b6df6381ff6a` | `af5af66a28e36351b3929ef15756b6df6381ff6a` | 0 | 4/0 | all-four digital design acceptance and Student mesh follow-up; no EVT/DVT/PVT/manufacturing claims |
| 7gc-digital-twin | YELLOW | `1a5491bf9261f77a75cc0fa7edbb5f25b425c7aa` | `9654ac82a722e800193e771556036dbb0df263db` | 2 | 1/0 | final public/reproduce/integration review; no measured radio topology claim |
| spectrumx-ai-ran-gary | YELLOW | `48eeacb7440af3a72966f3c4d5288d15c7de9617` | `2dc41c73fa0b16cb5703b8876e7e199f9a1b2b0a` | 9 | 1/0 | final reproducibility/links and owner review; exploratory/synthetic remains synthetic |
| readygary-6g-beam-selection | YELLOW | `e04b38b48cd2ebd87243153ca8fad9e914f16b21` | `e04b38b48cd2ebd87243153ca8fad9e914f16b21` | 0 | 2/0 | final integrated evidence review; simulation not carrier/physical acceptance |
| ntn-resilience-sim | YELLOW | `05aaa9aec16882f58bac6ce4ff47618d9812f69f` | `05aaa9aec16882f58bac6ce4ff47618d9812f69f` | 0 | 1/0 | final integrated evidence review; no real carrier/RF claim |
| edge-io-measurement-node | YELLOW | `f357b4c0fcfa77ea74d88e3263467dc60ec8cb2a` | `758b14a2c06b70a6678fc761d5360bde5e7cb235` | 2 | 2/0 | privacy/export/current integration review; physical sensing/EVT separate |
| waike-research-ops | RED | `34ae043abbd38c89bd30f7ae1ae7cf8cc06645a0` | `34ae043abbd38c89bd30f7ae1ae7cf8cc06645a0` | 0 | 4/0 | all18 program remains incomplete; current content privately developed and not accepted/pushed |
| gunnchos-7gc-ai-ran-field-kit | RED | `9dfc326647880c244904dd50a47ea80c3d46748e` | `4f3095e349f522d6db9901b99101f3fe5dff9f6c` | 8 | 25/1 | missing PyYAML reproduced; isolated repair ddf90ab draft PR123; accepted-main watch not repaired yet |

## RC1 source, tags and asset verification

All 16 canonical repositories have published `v1.0.0-rc.1` prereleases. Current release-list reads found no `v1.0.0` or `v1.0.0-rc.2` release in those repositories. Every recorded RC1 tag source is an ancestor of or identical to its current main. Exact source objects, annotated-tag peeling, release target strings, uploaded assets, post-RC1 commit histories and open PR states are preserved in `github-state.json`.

All 33 uploaded release assets were streamed through SHA-256 and byte-size verification: **33/33 matched the published GitHub digests**. No binary was saved or executed. Component releases with zero uploaded assets remain source-only release records, not executable acceptance proof. Checksums do not prove software quality or production signing. Device OS APK signing remains `debug_rc1`.

**Device OS provenance exception:** its annotated RC1 tag resolves to `438aaf2b54d3365d681dd6eeeb73f6ac58663acc`, but the release target and released APK build manifest identify `2218ead0efa0e4b8a622717a0a9bf623ee95ddb0`. The APK SHA-256 is `a0c55be39c407ffd24868a715c9c86bb2da07efbff16dc2ddb90aecebef45826`. Preserve RC1 history; do not move its tag. RC2 must consistently bind source, build and artifacts. Files under the historical `releases/v1.0.0` directory do not constitute publication or authorization.

## Changes since RC1 and October 9

The matrix records exact post-RC1 commit counts. Portal accepted main remains PR #54. Site main advanced to `f4f4c85cd5bb924a6bc5ca2d196f159da32c81b9`, including Thursday Lab Week 2. Other substantial work is still unmerged or local. Each candidate below has a precise branch, commit and dirty-state record in CURRENT_SOURCE_STATE.json; none is called accepted merely because a report says complete.

| Candidate | Exact branch | HEAD | Disposition |
|---|---|---|---|
| waike-site | `delivery/full-learning-2026-10-15` | `a6f4cd620123c1d12ac704346fb4a7fe5b51b05e` | Dirty continuation preserved; not accepted main |
| waike-platform | `delivery/full-learning-2026-10-15` | `6bdfa0b416ea95b0abb36669faa8059095962281` | Committed local candidate; not accepted main |
| waike-curriculum | `delivery/full-learning-2026-10-15` | `18efa764e4db066fb17d597284557195499f93ea` | Committed local candidate; not accepted main |
| publication | `cursor/publication-family-parallel-production-001` | `5adb3fd93792e3102e8a0915ac267b053e49e770` | Committed local candidate; not accepted main |
| anime | `release/anime-v1-dialogue-and-elemental-performance` | `30c6f2c87024eda9a283fe47121c8ce4abc4fa69` | Dirty continuation preserved; not accepted main |
| fieldkit-ci-repair | `release/standards-watch-dependencies-2026-10-19` | `ddf90ab0c4e4b29e765be73093d0ba91c59249d0` | Committed local candidate; not accepted main |

All original open PRs, branch heads, draft/conflict states and CI scopes are in the evidence snapshot. Unknown mergeability remains unknown. Experimental hardware PRs #69–79, unrelated PhD documents and IEEE work are not promoted into V1. Anime #123 stacks on #122; preserve that dependency. No product PR was merged by this campaign.

## WAIKE learning and workshop acceptance

All 18 tracks remain required. The live catalog and Courses → Digital Confidence → module → lesson path work. The top-level Lessons button returned Home in the fresh browser probe. Lab instructions are readable, but the public build explicitly lacks a school Hub: attempts, grading, feedback and institutional submissions are unavailable rather than fabricated. The entire public learn/practice/feedback/export journey therefore remains incomplete.

The existing local continuation already fixes the reader path; do not implement it again. It contains 180 weekly presentations from 170 unique sources, substantive Digital Confidence practicals and a narrow instructor-led workshop. Its canonical matrix still marks every whole course incomplete. Practical/independent assessment gaps, full 18-track offline/native acceptance and authentic educational/accessibility review remain required. No workshop success substitutes for the full LMS or 18-track program.

Recovered dated evidence includes four development buyer checks, six built-site buyer/privacy checks and 15 local HTTPS reader checks. Client 106, targeted Hub 33 and broader Hub 42 results have overlapping scopes—31 Hub checks overlap—and are not summed into invented independent totals. Local immutable runtime `c7d1aefd9a641e99c8cf1746c9d6eef841a3096f` consumes curriculum `33a101852f4fefb0eb239bcffa60a65d71102e2c`; current local HEADs are later evidence/workshop checkpoints. The public deployment still consumes the older `63ba9f25…` curriculum pin.

The built buyer page was freshly opened and correctly disclosed limitations, participant/instructor materials and unsubmitted evidence. Its retained HTTPS reader was not running, so the full buyer/practical flow was not re-certified today. No certificate warning was bypassed, no real student accounts were created and no instructor answer keys were exposed. Selected file bytes can reach the local evaluator; optional local saving does not imply no transmission. Free-to-learner, institutional, hosting and commercial-delivery gates remain explicit.

## Technology Landscape: eight private review editions

Publication checkpoint is `5adb3fd93792e3102e8a0915ac267b053e49e770`. All eight current review EPUB hashes match final successful official EPUBCheck 5.2.1 reports: adult, seniors and six children's editions. The earlier classpath execution failure and initial invalid adult/seniors EPUBs remain preserved; successful packaging repairs supersede only their affected outputs. The final passing summary was checked against actual bytes, not inferred from zero default error counts.

The private web reader is pinned separately to `81b7725ad65ddf64bb6cc2706c01168630dc156f`. Do not imply that it contains all later EPUB repairs. A fresh local UI probe opened its real contents and adult chapter, inspected figure alternative text, selected 32 px reading, tested opt-in bookmark/save/resume and searched “bottleneck” with five matching chapters. Public-mode local build kept the library pending; private chapter and ignored catalog paths returned 404.

Editorial/audience validation, illustration rights, manual accessibility and edition release decisions remain open. No manuscript text, EPUB/PDF content, instructor compiler data or private databases are included in this control-plane packet. Books are not part of an already approved commercial workshop entitlement.

## Anime combat, visual and Story evidence

ANI-02 progressed: a later explicit owner task in the candidate source approves seven unique working First Loss identities, and source validation confirms them. This is recovered authority, not a new Story/art/feel approval. Kaia → Rook remains canon; the remaining six choices are now recorded, so do not ask the owner to choose them again.

PR #122 contains ordinary Kaia 20-node / 16 real BattleScene receipt evidence, losses/retries, process save/resume, Essence progression, Gray, ending and Next Route. The 145-node / 115-receipt sweep and Convergence prerequisites are staged engineering evidence. They do not prove seven fully earned ordinary-input campaigns or all-Gray unlocks. PR #122 has nine successful latest-head checks; PR #123 has eight.

PR #123 adds persistent aura, projectile ownership, direct-throw/policy, VFX intensity and bounded active-CPU contact evidence. Runtime `0e33ee436b78ebf67079ef044cd73845df9070d3` differs from evidence HEAD `30c6f2c87024eda9a283fe47121c8ce4abc4fa69`. Its PR body still mentions an earlier source; Git/source and retained capture bindings are used instead. Dirty later probe/tool reports were preserved separately. The recorded 103/108 contact cells are scope-limited; missing cells are unverified, not automatically defects.

Full form lifecycles, ordinary counterplay/KO/training reproduction, authored acting/defense/aerials/throws, screenplay/OVA/voices/mix, exported platform proof and owner quality acceptance remain open. No old training hit/KO report was treated as a current failure without reproduction, and no roster metadata or mannequin asset was treated as final art. All human taste/Story and release gates remain false. Low disk prevents heavy exports under the established guard.

## Pursuit, Archive, BeatLink and invitations

Pursuit's deployed `957ff95…` runtime loaded into Time Trial. Countdown/GO, directional input and movement, speed-lane feedback, Escape pause and return to Main Menu were observed. No completed lap, results/save recovery, all-eight-course/mode/item/Party Race matrix or physical FPS acceptance was earned. Clipped menu layout and washed-out framing are review concerns, not a visual approval.

Archive has accepted ingestion/index engineering, not full scientific completeness. The owner-required full pinned-source known-life/ICS/fossil/occurrence coverage and full-Earth maps remain in V1. Fixtures, a million-row scale test and sample taxa do not satisfy that requirement. Approved external datasets/licenses and qualified scientific review remain blockers.

BeatLink's public door responds, but its own gateway states that the room server is unavailable and party creation is disabled. Source Socket.IO tests cannot establish a current public party session. Rights-safe content and full party/invite acceptance remain required; new commercial music rights do not become a V1 requirement.

Invites remain planned on `https://gunnchos.com/i/<opaque-token>`. A 404 invalid-probe response is not a working resolver. No `play.gunnchos.com` configuration is assumed. Shared protocol, all four title actions, MLV/Device OS, supported native links and browser fallback remain required. No global rollback, live racing, synchronous Archive multiplayer, iMessage extension or full social backend is added to scope.

## MLV, Device OS and hardware

The public MLV local test identity loaded Commons, Home Yard, Gallery Lobby and Campus Transit. Production GitHub OAuth remains unconfigured. No friend/private-file cross-account denial, complete interior/seven-campus traversal, production persistence/conflict resolution or encrypted sync acceptance was earned. Reachability is not full world completion.

Read-only `adb devices -l` returned no devices. No installation, wipe or uninstall was attempted. Windows/Linux/macOS/Android source CI and historical runtime evidence retain their original scope; no new physical Windows or Pixel acceptance is inferred. Device OS still needs the final current-pin Capsule/continuity/update/recovery/security/host matrix.

Student 14.5, Handheld Hybrid, DS-XL Coder and Rings require digital design/provenance acceptance. EVT/DVT/PVT, RF/FCC/CE/carrier, battery transport, factory/manufacturing and warranty/RMA remain excluded from software V1 and unclaimed.

## Research, security and privacy

Current research CI is generally green except Field Kit's scheduled Standards Watch. Job 110510893665 failed before claim validation because `yaml` was missing. A clean temporary interpreter reproduced the exception. An isolated two-line workflow fix installs its existing `pyyaml>=6.0` requirement; the unchanged standards mapping and claim firewall then passed locally. Candidate `ddf90ab0c4e4b29e765be73093d0ba91c59249d0` is [draft Field Kit PR #123](https://github.com/gunnchOS3k/gunnchos-7gc-ai-ran-field-kit/pull/123). It is unmerged; the accepted-main failure is not called repaired. The scheduled/manual workflow must still be exercised after authorization.

No scientific data, research manuscript, separate three-paper checkout or truth validator was modified. Digital/synthetic/twin evidence does not establish measured RF, live RIC, carrier acceptance or commercial 6G performance.

Public entry points and local manuscript denial checks are recorded separately from functionality. No DNS/email, account permission, secret, real enrollment, payment or production deployment changed. This was not a penetration test. Preserved security/secret-scan/accessibility results retain their source and sampling limits; manual assistive-technology, multi-actor privacy, rights and full final-head security acceptance remain open.

## Integration journeys

The exact executed steps and limits are in [JOURNEY_RESULTS.json](../../rolling/evidence/v0002/JOURNEY_RESULTS.json). A: public lesson/instructions/return worked; complete feedback/export blocked. B: private reader controls worked; full eight-edition human review open. C: local-test MLV transitions worked; real-auth/private sharing open. D: bounded Pursuit gameplay worked; complete session and full matrix open. E: physical acceptance blocked by no device. F: buyer page and dated engineering tests verified; full fresh HTTPS practical/rehearsal not accepted.

## Blockers and next action

[BLOCKERS.json](BLOCKERS.json) contains 14 prioritized blockers, owning repositories, reproductions, next actions, acceptance evidence and effort limitations. No responsible full-release four-day forecast is supported. The principal constraints are Archive science, complete Anime/WAIKE/MLV/game/invite scope, private candidate integration, owner review, physical device access and low storage. Recovery saw about 2.6 GiB free; a later reading was about 1.3 GiB. Owned preview processes were stopped. No source/backups/caches were deleted to hide the constraint.

First review the narrow Field Kit repair and run its scheduled path on the authorized candidate. The next product integration task is a **private, source-bound review** of the existing WAIKE site/platform/curriculum payload and retained runtime, not reimplementation: confirm content-disclosure authority, preserve pins, reproduce the already-fixed reader defect and replay the buyer/practical flow with trusted TLS. Continue Anime from its current stacked branch and dirty checkpoint, not from October 6. Keep publication review private.

## RC2, owner review and anniversary paths

[RC2_PREPARATION_MANIFEST.json](RC2_PREPARATION_MANIFEST.json) is explicitly **UNFROZEN / NOT READY**, not a releasable consistent candidate. It lists exact accepted and provisional sources with every new artifact/integration/owner acceptance flag false. Dependency compatibility, required hashes/signatures, complete technical matrix, physical acceptance and explicit RC2 authorization must precede a genuine freeze. October 21 readiness is not established.

[OWNER_REVIEW_AND_DELIVERY.md](OWNER_REVIEW_AND_DELIVERY.md) is an October 19 preparation packet for October 22. It contains direct local instructions, a pending approval worksheet, permitted demonstration boundaries, two truthful anniversary paths and rollback/recovery instructions. Path A official V1 is currently NO-GO. Path B is a prepared engineering milestone only; public demonstrations/materials/announcements still need their applicable approvals. Nothing is published or mislabeled as finished V1.

## Requested deliverable index

| Requested output | Record |
|---|---|
| 1. October 19 source recovery | CURRENT_SOURCE_STATE.json and this report |
| 2. Canonical 16-component matrix | RELEASE_MATRIX.json / RELEASE_MATRIX.csv |
| 3. Exact SHA/branch manifest | CURRENT_SOURCE_STATE.json and github-state.json |
| 4. RC1-to-current comparison | RELEASE_BASELINE_STATE.json and GitHub comparisons |
| 5. Product acceptance | Source-bound evidence and product sections above |
| 6. Integration results | JOURNEY_RESULTS.json |
| 7. Security/privacy | HTTP_BOUNDARY_CHECKS.json and stated test limitations |
| 8. Gameplay/visual acceptance | Bounded game probe and candidate evidence; gates open |
| 9. WAIKE learning | CANDIDATE_TEST_PROVENANCE.json and canonical matrix references |
| 10. Publishing status | PUBLICATION_VERIFICATION.json; rights/release pending |
| 11. Device/runtime | Empty ADB enumeration; historical CI separated |
| 12. Scientific boundaries | Research and Archive sections; no measured promotion |
| 13. Hardware exclusions | Software/digital-only boundaries above |
| 14. Blockers/owners | BLOCKERS.json |
| 15. RC2 decision | RC2_PREPARATION_MANIFEST.json — NOT READY |
| 16. Owner worksheet | OWNER_REVIEW_AND_DELIVERY.md — all pending |
| 17. October 23 eligibility | Official V1 NO-GO; no scope waiver |
| 18. Anniversary demo package | Owner packet and draft Path B copy; not published |
| 19. Rollback/recovery | Owner packet; no current production change to roll back |
| 20. Exact next engineering task | Narrow CI repair review, then private WAIKE integration task above |
