# A–Z — Feedback Everywhere + Final Public Community Loop

**Generated:** 2026-09-21  
**Policy:** Do not publish final `v1.0.0` until final-V1 feedback gates PASS or owner waives. Draft PRs only; no auto-merge. No new feedback backend — GitHub is system of record.

## A — Canonical feedback URL
`https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md`  
**Status:** `PLACEHOLDER_UNTIL_PORTAL_39_ACCEPTED_MAIN` (documented in `docs/feedback/CANONICAL_FEEDBACK_URLS.md`). Product code uses this URL now so final V1 never ships freeze-branch links.

## B — Portal forms
bug / feature / experience / research / hardware / accessibility / documentation + `config.yml` contact links (security private + public guide → accepted-main URL).

## C — Device OS in-app feedback
Settings → About (`gunnch_shell` SettingsSurface) + Settings → System/Help (`launcher_mock` SettingsPanel). Links open accepted-main FEEDBACK with optional `component=Device OS`. Draft branch work on vuln-closure / local trees — **push blocked** (`gh` token invalid).

## D — WAIKE feedback
Implementation prepared: `FeedbackSuggestions` footer + role-aware form routes.  
**Blocked writing primary repo** (outside agent workspace). Applied to writable copy: `gunnchAI3k/.worktrees/waike-lp-stream-b`. Patch kit: agent store `v1_feedback_everywhere_patches/waike/`.

## E — gunnchAI feedback
`public/index.html` Feedback & Suggestions section: quality / provenance / runtime / security private.

## F — Anime feedback
Settings + Results: `Feedback & Suggestions` → OS.shell_open accepted-main hub. Combat not interrupted.

## G — Pedestrian feedback
MainMenu + ResultsScreen feedback buttons → accepted-main hub.

## H — Archive feedback
Settings UI Help/About section with hub + security links.

## I — BeatLink feedback
Host/Player AccessibilityPanel Help/About feedback links (web; no APK requirement).

## J — Hardware repos
`gunnchos-hardware-industrial-design` (+ Edge IO): FEEDBACK.md / CONTRIBUTING / SECURITY / README Feedback section (accepted-main).  
**Field-kit:** write blocked (outside workspace) — patch in agent store `v1_feedback_everywhere_patches/field-kit/`.

## K — Research repos
Digital Twin, SpectrumX, ReadyGary, NTN, Edge IO, waike-research-ops: FEEDBACK.md refreshed to accepted-main; README Feedback sections added where missing.

## L — Curriculum
Via WAIKE FEEDBACK + portal documentation/research forms; waike-research-ops FEEDBACK.md present.

## M — README links
Added **Feedback & Suggestions** to component READMEs where missing (writable repos).

## N — Release-note links
Portal `RELEASE_NOTES_v1.0.0-rc.1.md` uses template Feedback & Suggestions block (accepted-main). Template: `docs/feedback/templates/RELEASE_NOTES_FEEDBACK_BLOCK.md`. Component GitHub Releases still need owner to paste block when publishing.

## O — Accessibility route
Portal accessibility issue form kept public; optional AT disclosure; no certification claim; security warning present.

## P — Private security path verified?
**Documented:** PASS (SECURITY.md + advisory URL present). **Live Private Vulnerability Reporting:** DISABLED on portal and Device OS (`gh api .../private-vulnerability-reporting` → `enabled=false`).
→ `SECURITY_PRIVATE_PATH_VERIFIED=false`, `PRIVATE_SECURITY_REPORTING_SETUP_REQUIRED=true`. Owner must enable GitHub Private Vulnerability Reporting before final V1 claims this gate PASS.


## Q — Discussions status
`GITHUB_DISCUSSIONS_OPTIONAL_NOT_ENABLED` — see `docs/feedback/GITHUB_DISCUSSIONS_STATUS.md`. Issues remain guaranteed V1 mechanism. No claim Discussions is live.

## R — Triage labels/process
`docs/feedback/FEEDBACK_TRIAGE.md` + `FEEDBACK_TAXONOMY.md` (kind, workflow, P0–P4). Labels creation on GitHub still owner/ops when auth works.

## S — Feedback-to-release traceability
`docs/feedback/FEEDBACK_TO_RELEASE.md` + credit loop notes in triage. ROADMAP/CHANGELOG remain intake surfaces.

## T — Public feedback matrix
`docs/feedback/PUBLIC_FEEDBACK_SURFACE_MATRIX.md` — several rows IN_PROGRESS until draft PRs merge + field-kit/WAIKE primary apply.

## U — CI/tests
- `scripts/validate_feedback_urls.py` (portal)
- `feedbackUrls.test.ts` (Device OS shell + launcher_mock)
- Full product suite: run per-repo before merge; not all executed this pass (auth/time)

## V — URLs checked
Product deep-links use `/blob/main/FEEDBACK.md` only. Interim freeze URL documented for owner preview, not baked into product code.

## W — Privacy scan
Feedback URL builders strip unsafe chars; no serial/IP/token/path in query params. Forms warn to redact logs.

## X — Final V1 feedback gates
`releases/v1.0.0/V1_FINAL_FEEDBACK_GATES.json` added; RC1 gates note that in-app gates are final-V1 only. `V1_0_0_RELEASE_AUTHORIZED=false`.

## Y — Blockers
1. `gh auth` token invalid — cannot push/update portal #39 or open component draft PRs
2. WAIKE LP + field-kit outside workspace — patches staged; need parent re-root or owner apply
3. `SECURITY_PRIVATE_PATH_VERIFIED` needs live advisory check after auth
4. In-app gates remain false until draft PRs land + smoke
5. Component GitHub Release pages need feedback block when releases are cut

## Z — Exact owner action
1. `gh auth login -h github.com` (restore `gunnchOS3k` token)
2. Review/push portal freeze commits onto PR **#39** (or approve new commit)
3. Merge #39 to accepted main → canonical `main/FEEDBACK.md` becomes live
4. Apply WAIKE + field-kit patch kits; open **narrow draft PRs** per product (Device OS, WAIKE, gunnchAI, 4 games)
5. Enable/verify private vulnerability reporting → flip `SECURITY_PRIVATE_PATH_VERIFIED=true`
6. Paste release-note feedback block on each V1 GitHub Release
7. Optionally enable Discussions (non-blocking)
8. When matrix all PASS (or waive), set final V1 feedback gates + only then authorize `v1.0.0`

**Do not publish final v1.0.0 in this pass.**


## Draft branches pushed (open draft PRs — API create blocked)

| Component | Branch | Open draft PR |
|---|---|---|
| Portal (#39 updated) | `release/v1.0.0-rc1-ecosystem-freeze` @ `e65dc6d` | https://github.com/gunnchOS3k/gunnchos-research-portal/pull/39 |
| Device OS | `release/v1-in-app-feedback` | https://github.com/gunnchOS3k/gunnchos-device-os/pull/new/release/v1-in-app-feedback |
| Anime | `release/v1-in-app-feedback` | https://github.com/gunnchOS3k/anime-aggressors/pull/new/release/v1-in-app-feedback |
| Pedestrian | `release/v1-in-app-feedback` | https://github.com/gunnchOS3k/pedestrian-pursuit/pull/new/release/v1-in-app-feedback |
| Archive | `release/v1-in-app-feedback` | https://github.com/gunnchOS3k/archive-of-life-artifact-world/pull/new/release/v1-in-app-feedback |
| BeatLink | `release/v1-in-app-feedback` | https://github.com/gunnchOS3k/beatlink-party/pull/new/release/v1-in-app-feedback |
| gunnchAI | `release/v1-in-app-feedback` | https://github.com/gunnchOS3k/gunnchAI3k/pull/new/release/v1-in-app-feedback |
| Digital Twin | `docs/v1-feedback-hub` | https://github.com/gunnchOS3k/7gc-digital-twin/pull/new/docs/v1-feedback-hub |
| SpectrumX | `docs/v1-feedback-hub` | https://github.com/gunnchOS3k/spectrumx-ai-ran-gary/pull/new/docs/v1-feedback-hub |
| ReadyGary | `docs/v1-feedback-hub` | https://github.com/gunnchOS3k/readygary-6g-beam-selection/pull/new/docs/v1-feedback-hub |
| NTN | `docs/v1-feedback-hub` | https://github.com/gunnchOS3k/ntn-resilience-sim/pull/new/docs/v1-feedback-hub |
| Edge IO | `docs/v1-feedback-hub` | https://github.com/gunnchOS3k/edge-io-measurement-node/pull/new/docs/v1-feedback-hub |
| Hardware industrial | `docs/v1-feedback-hub` | https://github.com/gunnchOS3k/gunnchos-hardware-industrial-design/pull/new/docs/v1-feedback-hub |
| waike-research-ops | `docs/v1-feedback-hub` | https://github.com/gunnchOS3k/waike-research-ops/pull/new/docs/v1-feedback-hub |
| WAIKE LP (primary) | patch kit only (see note) | Agent store `v1_feedback_everywhere_patches/waike/` + worktree `gunnchAI3k/.worktrees/waike-lp-stream-b` |
| Field kit | patch kit only | Agent store `v1_feedback_everywhere_patches/field-kit/` |

### WAIKE LP note
Primary repo `gunnchos-waike-learning-platform` was **outside the agent workspace** (writes blocked). Feedback UI was applied to a nested copy under `gunnchAI3k/.worktrees/waike-lp-stream-b` and committed into the **gunnchAI3k** `release/v1-in-app-feedback` branch as `.worktrees/waike-lp-stream-b/...` paths — **not** a proper WAIKE LP PR. Owner must copy the patch kit into the real WAIKE LP repo and open a narrow draft there.

