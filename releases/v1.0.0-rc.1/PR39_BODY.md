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
- `RELEASE_ASSET_HASH_PASS=true`
- `PIXEL_V1_RC1_DEMO_PASS=true` (Capsule → WAIKE Continue/adapter → loopback client; CDP Sign-in → 18 tracks → lesson)
- `RC1_OWNER_APPROVAL=false`
- `V1_0_0_RELEASE_AUTHORIZED=false`

## Device OS provenance (RC1 demo child)
- **Accepted main (base):** `bf109e704ac28b38b9fe1d9ce39954158f061793`
- **RC1 demo child:** Device OS draft PR [#161](https://github.com/gunnchOS3k/gunnchos-device-os/pull/161) — **not accepted-main yet**
- **Green #161 head (CI closed):** `5e88313e42b0a5ce42d7c2e2a990f3ac43a6f5eb` (WAIKE loopback Hub URL handoff + jsdom `matchMedia` test polyfill)
- **Pixel demo proof inherit:** production Capsule handoff proven at prior #161 head `563271f8d02a74fc61be5e6893a5ab524767083f`; follow-up `5e88313…` touches **test setup / CX2 adapter assertions only** — no production code change → full Pixel demo not re-run
- **Purpose of #161:** Capsule WAIKE loopback Hub URL + Continue lesson handoff for RC1 career-fair demo
- **Freeze rule:** merge #161 into Device OS accepted main **before** final accepted-main RC1 freeze / Device OS `v1.0.0-rc.1` release tag. **Do not tag Device OS RC1 at old main `bf109e7…` if #161 is required for the demo path.**

## Nearby Edge / gunnchAI
- Nearby Edge live AI honestly **unavailable**
- `gunnchai_live_response=false` — no fake live AI claimed

## Policy
DO NOT MERGE until owner review. DO NOT publish RC1 or final `v1.0.0` without explicit authorization.
