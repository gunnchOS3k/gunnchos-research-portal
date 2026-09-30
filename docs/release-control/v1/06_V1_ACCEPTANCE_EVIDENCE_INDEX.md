# v1.0.0 Acceptance Evidence Index

## Every in-v1 repository needs
- accepted main SHA
- tag/version
- build manifest
- build hash
- CI status
- dependency/security status
- rights/provenance status
- release notes
- feedback link
- known limitations
- exact artifact names

## Core evidence

### 3k MLV
- accepted-main SHA
- Cloudflare production URL
- Worker deployment identity
- Home/Campus/Gallery smoke
- supported-host matrix
- PWA/service-worker validation

### WAIKE
- accepted-main SHA
- web/PWA build
- offline sync
- identity/security
- assessment flow
- track/content readiness matrix
- human learner/instructor notes

### Device OS
- accepted-main SHA
- Android Capsule artifact/hash
- exact-head identity
- lifecycle matrix
- host matrix
- update/recovery/security evidence

### gunnchAI
- accepted-main SHA
- runtime build
- digital evaluation
- human-eval result
- live-provider status

## Game evidence

### Anime
- final merge SHA if included
- exact-head Android artifact/hash
- installed Pixel SHA
- signer strategy
- match smoke
- Story smoke
- G6/G8/G9 owner result
- PartyLink status

### Pedestrian
- final V4 merge SHA if included
- exact-head build
- eight-course Pixel checklist
- power-up readability
- Party Race status

### Archive
- accepted-main SHA
- ingestion engineering gate
- human gameplay acceptance
- explicit science-completeness boundary

### BeatLink
- accepted-main SHA
- multi-client smoke
- human live-party result
- rights-safe catalog manifest
- commercial-rights boundary

## Release-control artifacts to regenerate
- `FINAL_ACCEPTED_MAIN_MANIFEST.json`
- `V1_FINAL_GATES.json`
- `RELEASE_ASSET_MANIFEST.json`
- `SHA256SUMS.txt`
- `RIGHTS_PROVENANCE_MANIFEST.json`
- `SUPPORTED_HOST_MATRIX.json`
- `HUMAN_ACCEPTANCE_SUMMARY.json`
- `PHYSICAL_EXTERNAL_GATE_SUMMARY.json`
- `PUBLIC_DEPLOYMENT_MANIFEST.json`
- `FINAL_RELEASE_NOTES.md`

## Freshness rule

Final-v1 evidence must be tied to the final accepted SHA, or to a documented ancestor whose behavior is proven unchanged.

Do not silently use stale PR-head evidence as final-main proof.
