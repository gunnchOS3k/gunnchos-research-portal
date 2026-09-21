## Summary
Draft freeze for **gunnchOS Ecosystem v1.0.0-rc.1** (First Public Engineering & Demonstration Release Candidate).

- Accepted-main freeze + recovered-child ancestry for V1 components
- Release packaging under `release_staging/v1.0.0-rc.1/` with corrected non-self-referential checksums + `RELEASE_HASH_VERIFICATION.json`
- Games: rebuilt Anime / Pedestrian / Archive APKs; BeatLink **web zip only** (`GAMES_RELEASE_PASS=true`)
- Pedestrian APK external `release_staging_large/` (>100MB) — attach on GitHub Release
- Front door / QR encode tagged `v1.0.0-rc.1` START_HERE (branch URL is preview only)
- Demo bootstrap: `releases/v1.0.0-rc.1/demo/start_demo_services.sh`
- Owner review packet: `releases/v1.0.0-rc.1/OWNER_RC1_REVIEW.md` (unchecked)

## Gates (authoritative: `releases/v1.0.0-rc.1/V1_RC1_GATES.json`)
- `GAMES_RELEASE_PASS=true`
- `RELEASE_ASSET_HASH_PASS=true` (after recompute)
- `PIXEL_V1_RC1_DEMO_PASS=false` until owner completes on-device Sign-in → tracks → lesson after bootstrap
- `RC1_OWNER_APPROVAL=false`
- `V1_0_0_RELEASE_AUTHORIZED=false`

## Policy
DO NOT MERGE until owner review. DO NOT publish RC1 or final `v1.0.0` without explicit authorization.
