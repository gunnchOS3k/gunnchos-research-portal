# v1.0.0 Blocker and Dependency Register

## P0 — Release-control blockers

### B-001 Fresh final freeze cannot be authoritative yet
Active final-v1 candidate work is still open and current mains advanced after the September 21 freeze.

**Depends on:**
- Anime #118 disposition
- Pedestrian #39 disposition
- 3k MLV #6 decision
- public hosting state
- WAIKE/gunnchAI human truth

**Closure:** regenerate accepted-main pins only after those settle.

### B-002 Public ecosystem not live
Cloudflare GitHub integration is configured, but production Worker/custom-domain deployment is incomplete.

**Closure order:**
1. harden `3k-mlv` for Workers;
2. preview;
3. production deploy;
4. attach `mlv.gunnchos.com`;
5. replicate pattern to required apps;
6. decide canonical `gunnchos.com` front door.

## P1 — Product blockers

### B-010 Anime signer mismatch
Exact-head APK exists; connected Pixel has a different signer; destructive uninstall is not authorized.

### B-011 Anime human acceptance
- G6 visual readability
- G8 human feel
- G9 final art
- merge authorization

### B-012 Pedestrian V4 physical/human review
- exact-head CI
- all eight courses
- power-up readability
- fun/feel

### B-013 WAIKE human/content truth
Automation must not fabricate missing academic content to force a pass.

### B-014 gunnchAI human/provider truth
Live-provider qualification is external; human evaluation remains.

## P2 — Claim-boundary blockers, not software-release blockers

- Archive scientific source completeness
- Archive scientific review
- BeatLink commercial rights
- human accessibility certification
- hardware EVT/DVT/PVT
- RF/carrier certification
- manufacturing
- warranty/RMA staffing
- institutional K-12 pilot

## Dependency graph

```text
Anime #118 ─┐
Pedestrian #39 ─┤
3k MLV #6 decision ─┤
Cloudflare deployment ─┤
WAIKE/gunnchAI human boundary ─┤
                         ↓
              FINAL SCOPE FREEZE
                         ↓
            CURRENT-MAIN PIN MANIFEST
                         ↓
                 FINAL BUILD SET
                         ↓
                   v1.0.0-rc.2
                         ↓
                OWNER FINAL REVIEW
                         ↓
                v1.0.0 AUTHORIZATION
```
