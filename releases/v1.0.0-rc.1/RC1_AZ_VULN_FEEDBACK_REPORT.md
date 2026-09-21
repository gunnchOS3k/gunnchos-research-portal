# RC1 A–Z report — Vulnerability closure + public feedback loop

**Release:** gunnchOS Ecosystem `v1.0.0-rc.1`  
**Generated:** 2026-09-21  
**Policy:** DO NOT PUBLISH final `v1.0.0`. DO NOT MERGE portal #39 without owner authorization. `RC1_OWNER_APPROVAL=false`. `V1_0_0_RELEASE_AUTHORIZED=false`.

## A — Accepted Device OS main (post-#161)
- **SHA:** `c6fd04aced44b0d3eec6f07c3b0b3fdbe50ad7a4`
- **Merge:** normal merge of PR #161
- **Ancestor check:** `5e88313…` is ancestor of `origin/main` — OK
- **Superseded:** `bf109e7…` must not be used for RC1 tags

## B — Baseline audits (`apps/launcher_mock`)
- `npm ci` clean install
- Full audit pre-fix: 9 vulns (4 moderate, 4 high, 1 critical)
- Production audit (`--omit=dev`): **0** before and after

## C — Classification dispositions used
`FIXED_IN_LOCKFILE`, `DEV_ONLY_ACCEPTED`, `DEFERRED_MAJOR_BUMP`, `PRODUCTION_REACHABLE_BLOCKER` (none present), `NOT_APPLICABLE`

## D — Dependency remediation executed
- Safe `npm audit fix` (no `--force`) cleared browserslist / nanoid / postcss / baseline-browser-mapping
- Remaining: vitest (critical), vite (high), + moderate toolchain transitive — require Vite 8 / Vitest 5 majors → deferred

## E — Evidence paths
- Device OS: `artifacts/security/v1_rc1/`
- Portal mirror: `releases/v1.0.0-rc.1/security/device_os_launcher_mock/`

## F — Feedback front door (portal)
- `FEEDBACK.md`
- Issue forms: bug, feature, experience, research, hardware, accessibility, documentation
- `config.yml`: blank issues off; private security contact link

## G — Gates added/updated
- `PUBLIC_FEEDBACK_FRONT_DOOR_PASS=true`
- `SECURITY_PRIVATE_REPORTING_PASS=true`
- `DEPENDENCY_PRODUCTION_CRITICAL_ZERO_PASS=true`
- Owner flags remain **false**

## H — Hardware claim boundary
Unchanged: digital engineering only; no fab/EVT/DVT/PVT/cert claims

## I — In-app feedback
- `RC1_DESIRED` / `V1_REQUIRED` documented in `docs/feedback/IN_APP_FEEDBACK_STATUS.md`
- No product-code draft PRs in this pass; RC1 not delayed

## J — Justification for deferred critical
Vitest/Vite are **dev/test** only; Capsule production bundle does not ship them; production audit critical=0

## K — Known limitations updates
Portal `KNOWN_LIMITATIONS.md` notes deferred toolchain advisories + in-app feedback status

## L — Lockfile-only change impact
`package.json` unchanged → Pixel re-demo **not required**

## M — Manifest refresh
`FINAL_ACCEPTED_MAIN_MANIFEST.json` Device OS SHA → `c6fd04a…`

## N — No force audit fix
Explicitly rejected mid-freeze; plan in `DEPENDENCY_REMEDIATION_PLAN.md`

## O — Owner approval
**Not invented.** `RC1_OWNER_APPROVAL=false`. Owner review packet remains unchecked.

## P — Portal PR #39
Draft branch `release/v1.0.0-rc1-ecosystem-freeze` updated with SHA, vuln evidence, feedback front door, security path, triage, roadmap, gates, limitations. Prefer push; **do not merge**.

## Q — Quality / regression
`npm test` in launcher_mock: **14 files / 77 tests passed**

## R — ROADMAP / CHANGELOG discipline
Portal `ROADMAP.md` + `CHANGELOG.md` refreshed; component stubs created where missing (preserve stronger existing ROADMAPs)

## S — SECURITY.md
Private-reporting language on portal + release-bearing component worktrees/roots; existing stronger templates preserved (e.g., Archive issue templates, research templates, gunnchAI long SECURITY doc + private reporting footer)

## T — Triage docs
`docs/feedback/FEEDBACK_TRIAGE.md`, `FEEDBACK_TO_RELEASE.md`

## U — Unrelated feature work
Not merged

## V — Vuln production gate
Production-reachable critical = **0** (RC1 requirement met)

## W — Worktree / branch artifacts
- Device OS: `.worktrees/v1-rc1-vuln-closure` branch `release/v1-rc1-vuln-closure` @ `fe67f84…`
- Portal: `.worktrees/v1-rc1-ecosystem-freeze` branch `release/v1.0.0-rc1-ecosystem-freeze`
- Component FEEDBACK/SECURITY scaffolding applied under `_rc1_release_worktrees/*` and research local roots (docs only; stronger templates preserved)

## X — Explicit non-publish
No GitHub Release publish; no final `v1.0.0`

## Y — Yet-to-land owner actions
1. Review PR #39 + owner packet
2. Optionally merge Device OS vuln-closure draft PR after review
3. Flip `RC1_OWNER_APPROVAL` only after personal review
4. Authorize publish separately

## Z — Zero surprises summary
RC1 can proceed with honest deferred **dev-toolchain** advisories, green **production** audit, live **public feedback** front door, private **security** path, and refreshed Device OS accepted-main SHA post-#161 — without inventing owner approval or publishing `v1.0.0`.
