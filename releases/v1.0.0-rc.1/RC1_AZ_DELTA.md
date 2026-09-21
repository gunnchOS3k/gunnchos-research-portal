# A–Z delta — RC1 release-blocker closure

A — live PR #39 head: `5831c8a533ee72d6d5ac7b7c7514149eb3d9bfbc` (branch `release/v1.0.0-rc1-ecosystem-freeze`)
B — PR body: draft at `releases/v1.0.0-rc.1/PR39_BODY.md` (apply with `gh pr edit 39 --body-file ...` when auth available); GAMES=true; owner flags false; no serials
C — checksum model: SHA256SUMS does not hash itself; manifest has no self-hash; see checksum_model in RELEASE_ASSET_MANIFEST.json
D — checksum recompute: RELEASE_ASSET_HASH_PASS=True (25 entries; pedestrian EXTERNAL included)
E — umbrella release target: `<POST_PR39_ACCEPTED_MAIN_SHA>` (stale ff1325a1 removed)
F — component targets: unchanged accepted-main SHAs in DRAFT_RELEASE_COMMANDS.md
G — attachment plan: `releases/v1.0.0-rc.1/RELEASE_ATTACHMENT_PLAN.json` + commands attach assets
H — owner review packet: `releases/v1.0.0-rc.1/OWNER_RC1_REVIEW.md` (unchecked)
I — demo bootstrap: `releases/v1.0.0-rc.1/demo/start_demo_services.sh`
J — WAIKE Pixel: Hub API 18-track + Sign-in UI proven; on-device lesson UI pending manual IME login
K — gunnchAI Pixel: Nearby Edge unavailable (honest)
L — AI provenance: truthful unavailable / no fake live AI
M — game launch: Anime GodotApp focus proven; return-to-Capsule captured
N — BeatLink: preexisting_non_rc1_demo_app on device; RC1 artifact web zip only
O — app version mapping: `releases/v1.0.0-rc.1/APP_VERSION_MAPPING.md`
P — front-door strategy: tag URL `.../blob/v1.0.0-rc.1/START_HERE.md`; branch URL preview-only
Q — QR: regenerated SVG/PNG for tag URL; FRONT_DOOR_URL.txt updated
R — release notes: `RELEASE_NOTES_v1.0.0-rc.1.md` present
S — draft release commands: updated with attachments + placeholder target
T — technical gates: see V1_RC1_GATES.json (owner flags false)
U — PIXEL_V1_RC1_DEMO_PASS=False
V — RELEASE_ASSET_HASH_PASS=True
W — RC1_DRAFT_RELEASES_READY=True
X — RC1_OWNER_APPROVAL=false
Y — V1_0_0_RELEASE_AUTHORIZED=false
Z — remaining owner action: complete OWNER_RC1_REVIEW.md; run bootstrap + manual WAIKE Sign-in → tracks → lesson; then authorize merge of PR #39 and draft prereleases — do not publish final v1.0.0
