# Engineer path — gunnchOS Ecosystem v1.0.0-rc.1

## Freeze rule

RC1 is accepted-main only. Open PRs are classified and **not** merged into the freeze. No branch tip substitutes for `origin/main`.

## Start here

1. Read [releases/v1.0.0-rc.1/FINAL_ACCEPTED_MAIN_MANIFEST.json](releases/v1.0.0-rc.1/FINAL_ACCEPTED_MAIN_MANIFEST.json)
2. Match SHAs in [COMPONENT_VERSION_MATRIX.md](releases/v1.0.0-rc.1/COMPONENT_VERSION_MATRIX.md)
3. Build from clean worktrees at those SHAs
4. Stage under `release_staging/v1.0.0-rc.1/`
5. Verify `SHA256SUMS.txt` + `RELEASE_ASSET_MANIFEST.json`
6. Pixel path: [PIXEL_DEMO.md](PIXEL_DEMO.md)

## Preferred artifacts

| Component | Strongest truthful artifact |
|---|---|
| Device OS | Android Capsule APK + build metadata + checksums |
| WAIKE | Web/PWA client bundle (+ desktop if CI-validated) |
| Curriculum | 18-track registry/manifest bundle + hashes |
| gunnchAI | Service/runtime bundle + instructions (no unauthorized weights) |
| Games | APK / Capacitor / host-player as each repo supports |
| Hardware | Digital-engineering zip only |
| Research | Source pin + reproduce README + evidence boundary |

## Do not

- Publish `v1.0.0`
- Merge portal RC1 PR without owner approval
- Claim fab/EVT/DVT/PVT/cert
- Fabricate Pixel serials or personal data in commits

## Feedback

- Public feedback: [FEEDBACK.md](FEEDBACK.md) · Security (private): [SECURITY.md](SECURITY.md)
