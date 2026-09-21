# App Version Mapping — gunnchOS Ecosystem v1.0.0-rc.1

**Ecosystem release version:** `v1.0.0-rc.1`  
**Meaning:** First Public Engineering & Demonstration Release Candidate for the umbrella ecosystem — not a claim that every installed package already uses internal `versionName` `1.0.0-rc.1`.

| Surface | Package / artifact | RC1 distribution | Observed internal `versionName` | `versionCode` | Alignment required before final `v1.0.0`? |
|---|---|---|---|---|---|
| Capsule (Pixel) | `com.gunnchos.capsule.debug` | RC1 rebuilt debug APK staged | `1.0.0-capsule-pilot-debug` | `1` | Yes — ship non-debug / aligned marketing version for final |
| Anime Aggressors | `com.gunnchos.animeaggressors` | RC1 rebuilt debug APK staged | `0.3.7` | `218` | Optional for RC1; recommend align or document for final |
| Pedestrian Pursuit | `com.gunnchos.pedestrianpursuit` | RC1 rebuilt debug APK (external >100MB) | `0.3.10` | `14` | Optional for RC1; recommend align or document for final |
| Archive of Life | `com.gunnchos.archiveoflife` | RC1 rebuilt debug APK staged | `1.1.1` | `3` | Optional for RC1; recommend align or document for final |
| BeatLink Party | `com.gunnchos.beatlinkparty` | **Not an RC1 APK** — RC1 is web zip only | Device may show preexisting `1.1.2` | `4` | N/A for RC1 APK; web bundle is the RC1 artifact |
| WAIKE | web/PWA zip | `waike/waike-web-pwa-v1.0.0-rc.1.zip` | (bundle) | — | Document client/hub versions at final |
| gunnchAI | runtime zip | `gunnchai/gunnchai-runtime-v1.0.0-rc.1.zip` | (bundle) | — | Document runtime label at final |
| Curriculum | zip | `curriculum/waike-curriculum-v1.0.0-rc.1.zip` | (bundle) | — | Track IDs over marketing version |
| Hardware | design zip | `hardware/gunnchOS-Hardware-Design-v1.0.0-rc.1.zip` | (bundle) | — | Claim digital-engineering class only |
| Research | systems zip | `research/research-systems-v1.0.0-rc.1.zip` | (bundle) | — | Pin accepted-main SHAs |

## BeatLink note

RC1 packaging is **web-only**. Any Android BeatLink package on the demo Pixel that was last updated before the RC1 rebuild window is `preexisting_non_rc1_demo_app` — see Pixel install manifest.

## Rule

Do not imply every package already has internal `versionName` `1.0.0-rc.1`. The ecosystem tag is the release identity; per-app strings may lag until final `v1.0.0`.
