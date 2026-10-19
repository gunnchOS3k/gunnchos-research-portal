# v1.0.0 Final Freeze, RC2, and Final Runbook

## Phase 1 — Close active candidates
- Anime: signer-safe Pixel → G7 → G6/G8/G9 → merge decision.
- Pedestrian: exact-head → eight-course review → merge decision.
- 3k MLV: Cloudflare hardening; decide PR #6 v1 vs v1.1.
- WAIKE/gunnchAI: targeted human review + honest limitations.

## Phase 2 — Public deployment
Recommended order:
1. `mlv.gunnchos.com`
2. `campus.gunnchos.com`
3. `anime.gunnchos.com`
4. `pursuit.gunnchos.com`
5. `archive.gunnchos.com`
6. `beatlink.gunnchos.com`
7. `research.gunnchos.com`
8. canonical `gunnchos.com`

For each deployment capture:
- exact source SHA
- preview smoke
- production deploy identity
- TLS/custom domain
- deep-link test
- mobile smoke
- feedback link
- deployment manifest

## Phase 3 — Scope freeze
Set:

```text
V1_SCOPE_FROZEN=true
```

## Phase 4 — Rebuild current-main authority
- pin every selected accepted-main SHA
- confirm selected PRs are merged or explicitly deferred
- rebuild dependency graph
- rebuild blocker register

## Phase 5 — Build candidate artifacts
- APKs
- web builds/zips
- SBOMs where available
- hashes
- provenance
- release notes
- known limitations
- rights boundary
- public deployment manifest

## Phase 6 — Publish `v1.0.0-rc.2`
RC2 is recommended because the ecosystem changed materially after RC1.

RC2 publication still requires owner authorization.

## Phase 7 — Candidate acceptance
- clean install/update
- public web smoke
- MLV Home/Campus/Gallery
- WAIKE learner journey
- gunnchAI supported journey
- each game
- research portal
- feedback/security links
- no stale-SHA evidence

## Phase 8 — Final authorization
Only the owner sets:

```text
V1_0_0_RELEASE_AUTHORIZED=true
```

Then publish final tags/releases and preserve RC1/RC2 history.

## Stop rule
If a post-freeze issue does not break a v1 promise, move it to v1.0.1/v1.1.
