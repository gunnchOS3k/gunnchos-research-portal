# Public Web, Community, and Gallery Doctrine

## Role

The public web makes the ecosystem legible without requiring GitHub knowledge.

## Principle

Subdomains are implementation boundaries.

They should not feel like unrelated companies.

## Intended structure

```text
gunnchos.com            → ecosystem gateway
mlv.gunnchos.com        → 3k MLV
campus.gunnchos.com     → WAIKE
anime.gunnchos.com      → Anime Aggressors
pursuit.gunnchos.com    → Pedestrian Pursuit
archive.gunnchos.com    → Archive of Life
beatlink.gunnchos.com   → BeatLink
research.gunnchos.com   → research / 7GC
```

Optional future:
- `ai.gunnchos.com`
- `devices.gunnchos.com`
- `docs.gunnchos.com`

## Public-site requirements
- clear entry point;
- consistent identity;
- responsive/mobile;
- accessible;
- deep-link safe;
- TLS;
- feedback path;
- known limitation transparency;
- no secrets in frontend builds;
- deployment maps to source SHA.

## Gallery relationship
Public web and Gallery should eventually reinforce each other:
- public projects;
- user creations;
- research artifacts;
- games;
- portfolios.

## Current state
Domain, Google Workspace, Cloudflare account, and repository access are being configured.

## Future state
One public gateway into the ecosystem.
