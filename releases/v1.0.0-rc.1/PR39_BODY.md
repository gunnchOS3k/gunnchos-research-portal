## Summary
Draft freeze for **gunnchOS Ecosystem v1.0.0-rc.1** (First Public Engineering & Demonstration Release Candidate).

- Accepted-main freeze + recovered-child ancestry for V1 components
- **Device OS accepted main refreshed** to post-#161 merge `c6fd04aced44b0d3eec6f07c3b0b3fdbe50ad7a4` (supersedes `bf109e7…`)
- Release packaging under `release_staging/v1.0.0-rc.1/` with corrected non-self-referential checksums + `RELEASE_HASH_VERIFICATION.json`
- Games: rebuilt Anime / Pedestrian / Archive APKs; BeatLink **web zip only** (`GAMES_RELEASE_PASS=true`)
- Pedestrian APK external `release_staging_large/` (>100MB) — attach on GitHub Release
- Front door / QR encode tagged `v1.0.0-rc.1` START_HERE (branch URL is preview only)
- Demo bootstrap: `releases/v1.0.0-rc.1/demo/start_demo_services.sh`
- Owner review packet: `releases/v1.0.0-rc.1/OWNER_RC1_REVIEW.md` (unchecked — **do not invent owner approval**)
- **Public feedback front door:** `FEEDBACK.md` + issue forms + `docs/feedback/*` + ROADMAP/CHANGELOG discipline
- **Security path:** private advisories only (`SECURITY.md`); Device OS `launcher_mock` vuln classification under `releases/v1.0.0-rc.1/security/device_os_launcher_mock/`

## Gates (authoritative: `releases/v1.0.0-rc.1/V1_RC1_GATES.json`)
- `GAMES_RELEASE_PASS=true`
- `RELEASE_ASSET_HASH_PASS=true`
- `PIXEL_V1_RC1_DEMO_PASS=true` (Capsule → WAIKE Continue/adapter → loopback client; CDP Sign-in → 18 tracks → lesson)
- `PUBLIC_FEEDBACK_FRONT_DOOR_PASS=true`
- `SECURITY_PRIVATE_REPORTING_PASS=true`
- `DEPENDENCY_PRODUCTION_CRITICAL_ZERO_PASS=true` (prod npm audit critical=0 / high=0)
- `RC1_OWNER_APPROVAL=false`
- `V1_0_0_RELEASE_AUTHORIZED=false`

## Device OS provenance
- **Accepted main (current):** `c6fd04aced44b0d3eec6f07c3b0b3fdbe50ad7a4` — owner-merged PR [#161](https://github.com/gunnchOS3k/gunnchos-device-os/pull/161) (normal merge)
- **Merged head included:** `5e88313e42b0a5ce42d7c2e2a990f3ac43a6f5eb` (ancestor of `origin/main`: yes)
- **Superseded:** `bf109e704ac28b38b9fe1d9ce39954158f061793` — do not tag RC1 at old main
- **Purpose of #161:** Capsule WAIKE loopback Hub URL + Continue lesson handoff for RC1 career-fair demo
- **Vuln closure:** safe `npm audit fix` (no `--force`) on `apps/launcher_mock`; remaining vite/vitest advisories classified `DEV_ONLY_ACCEPTED` + `DEFERRED_MAJOR_BUMP`; regression 77/77; Pixel re-demo not required (no prod/runtime dep change)

## Feedback architecture
- Portal `FEEDBACK.md` + forms: bug, feature, experience, research, hardware, accessibility, documentation
- Triage: `docs/feedback/FEEDBACK_TRIAGE.md` · Release promotion: `docs/feedback/FEEDBACK_TO_RELEASE.md`
- In-app Feedback links: `RC1_DESIRED` / `V1_REQUIRED` — public front door is sufficient for RC1; do not delay RC1 solely for in-app

## Nearby Edge / gunnchAI
- Nearby Edge live AI honestly **unavailable**
- `gunnchai_live_response=false` — no fake live AI claimed

## Policy
DO NOT MERGE until owner review. DO NOT publish RC1 or final `v1.0.0` without explicit authorization. Do **not** invent `RC1_OWNER_APPROVAL`.
