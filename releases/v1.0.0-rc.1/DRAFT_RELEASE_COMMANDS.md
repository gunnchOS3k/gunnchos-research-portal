# Draft GitHub prerelease commands — v1.0.0-rc.1

Do NOT publish final `v1.0.0`. Do NOT publish RC1 until Edmund explicitly authorizes.  
Create **draft + prerelease** only. Paths are relative to the portal repo root unless noted.

Attachment inventory: [`RELEASE_ATTACHMENT_PLAN.json`](RELEASE_ATTACHMENT_PLAN.json).

## gunnchos-research-portal (umbrella)

> Target is **not** stale pre-RC1 portal main `ff1325a1…`.  
> After owner-authorized merge of PR #39, fetch the new portal `main` SHA and substitute `<POST_PR39_ACCEPTED_MAIN_SHA>`.

```bash
POST_PR39_ACCEPTED_MAIN_SHA="<POST_PR39_ACCEPTED_MAIN_SHA>"

gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/gunnchos-research-portal \
  --draft --prerelease \
  --target "${POST_PR39_ACCEPTED_MAIN_SHA}" \
  --title "gunnchOS Ecosystem v1.0.0-rc.1" \
  --notes-file RELEASE_NOTES_v1.0.0-rc.1.md \
  releases/v1.0.0-rc.1/FINAL_ACCEPTED_MAIN_MANIFEST.json \
  releases/v1.0.0-rc.1/COMPONENT_VERSION_MATRIX.md \
  release_staging/v1.0.0-rc.1/RELEASE_ASSET_MANIFEST.json \
  release_staging/v1.0.0-rc.1/SHA256SUMS.txt \
  releases/v1.0.0-rc.1/RELEASE_HASH_VERIFICATION.json \
  RELEASE_NOTES_v1.0.0-rc.1.md \
  release_staging/v1.0.0-rc.1/hardware/gunnchOS-Hardware-Design-v1.0.0-rc.1.zip \
  release_staging/v1.0.0-rc.1/research/research-systems-v1.0.0-rc.1.zip \
  releases/v1.0.0-rc.1/qr/FRONT_DOOR.png \
  releases/v1.0.0-rc.1/qr/FRONT_DOOR.svg \
  releases/v1.0.0-rc.1/qr/FRONT_DOOR_URL.txt \
  releases/v1.0.0-rc.1/OWNER_RC1_REVIEW.md \
  releases/v1.0.0-rc.1/APP_VERSION_MAPPING.md \
  releases/v1.0.0-rc.1/V1_RC1_GATES.json
```

## gunnchos-device-os

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/gunnchos-device-os \
  --draft --prerelease \
  --target bf109e704ac28b38b9fe1d9ce39954158f061793 \
  --title "gunnchOS Capsule / Device OS v1.0.0-rc.1" \
  --notes "Accepted main: bf109e704ac28b38b9fe1d9ce39954158f061793. Umbrella: gunnchos-research-portal RC1." \
  release_staging/v1.0.0-rc.1/device-os/gunnchOS-Capsule-Pixel6a-rc1-rebuilt-debug.apk \
  release_staging/v1.0.0-rc.1/device-os/gunnchOS-Capsule-Pixel6a-rc1-rebuilt-debug.apk.sha256 \
  release_staging/v1.0.0-rc.1/device-os/BUILD_MANIFEST.json \
  release_staging/v1.0.0-rc.1/device-os/RC1_REBUILD_MANIFEST.json \
  release_staging/v1.0.0-rc.1/device-os/RC1_STAGING_PROVENANCE.json \
  release_staging/v1.0.0-rc.1/device-os/INSTALL_UNINSTALL.md
```

*(Run from portal checkout that holds `release_staging/`, or copy assets into the device-os tree before attach.)*

## gunnchos-waike-learning-platform

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/gunnchos-waike-learning-platform \
  --draft --prerelease \
  --target c306543ccc89fb0304734d0ebbaa94f8a0b19c1d \
  --title "WAIKE Learning Platform v1.0.0-rc.1" \
  --notes "Accepted main: c306543ccc89fb0304734d0ebbaa94f8a0b19c1d. Web/PWA RC1 zip." \
  release_staging/v1.0.0-rc.1/waike/waike-web-pwa-v1.0.0-rc.1.zip
```

## waike-research-ops

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/waike-research-ops \
  --draft --prerelease \
  --target e919976237cb67e26582b1da7caf975d6f35d883 \
  --title "WAIKE Curriculum v1.0.0-rc.1" \
  --notes "Accepted main: e919976237cb67e26582b1da7caf975d6f35d883. Curriculum bundle." \
  release_staging/v1.0.0-rc.1/curriculum/waike-curriculum-v1.0.0-rc.1.zip
```

## gunnchAI3k

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/gunnchAI3k \
  --draft --prerelease \
  --target ef665648aecb06230ecf7017065861b148e19c35 \
  --title "gunnchAI3k Runtime v1.0.0-rc.1" \
  --notes "Accepted main: ef665648aecb06230ecf7017065861b148e19c35. Runtime zip only — no unauthorized model weights." \
  release_staging/v1.0.0-rc.1/gunnchai/gunnchai-runtime-v1.0.0-rc.1.zip
```

## anime-aggressors

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/anime-aggressors \
  --draft --prerelease \
  --target 649b20f422b31bba2af9bf0c5c1b2b555c9a4a40 \
  --title "Anime Aggressors v1.0.0-rc.1" \
  --notes "Accepted main: 649b20f422b31bba2af9bf0c5c1b2b555c9a4a40. Debug APK + provenance." \
  release_staging/v1.0.0-rc.1/anime/anime-aggressors-debug-v1.0.0-rc.1.apk \
  release_staging/v1.0.0-rc.1/anime/anime-aggressors-debug-v1.0.0-rc.1.apk.sha256 \
  release_staging/v1.0.0-rc.1/anime/PROVENANCE.json
```

## pedestrian-pursuit

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/pedestrian-pursuit \
  --draft --prerelease \
  --target d91f102f251ef67d536d2f95188de7d627701902 \
  --title "Pedestrian Pursuit v1.0.0-rc.1" \
  --notes "Accepted main: d91f102f251ef67d536d2f95188de7d627701902. APK exceeds git 100MB — attach from release_staging_large." \
  release_staging_large/v1.0.0-rc.1/pedestrian/pedestrian-pursuit-debug-v1.0.0-rc.1.apk \
  release_staging/v1.0.0-rc.1/pedestrian/pedestrian-pursuit-debug-v1.0.0-rc.1.apk.sha256 \
  release_staging/v1.0.0-rc.1/pedestrian/PROVENANCE.json
```

## archive-of-life-artifact-world

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/archive-of-life-artifact-world \
  --draft --prerelease \
  --target 7b3e2e51782541a1a2d2896fc317a5e41e9db8f8 \
  --title "Archive of Life v1.0.0-rc.1" \
  --notes "Accepted main: 7b3e2e51782541a1a2d2896fc317a5e41e9db8f8. Debug APK + provenance." \
  release_staging/v1.0.0-rc.1/archive/archive-of-life-debug-v1.0.0-rc.1.apk \
  release_staging/v1.0.0-rc.1/archive/archive-of-life-debug-v1.0.0-rc.1.apk.sha256 \
  release_staging/v1.0.0-rc.1/archive/PROVENANCE.json
```

## beatlink-party

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/beatlink-party \
  --draft --prerelease \
  --target acdeb77bdf01c40a0e78f4adae6c119752ca5cca \
  --title "BeatLink Party v1.0.0-rc.1 (web)" \
  --notes "Accepted main: acdeb77bdf01c40a0e78f4adae6c119752ca5cca. RC1 artifact is web zip only — no BeatLink APK." \
  release_staging/v1.0.0-rc.1/beatlink/beatlink-web-v1.0.0-rc.1.zip
```

## gunnchos-hardware-industrial-design

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/gunnchos-hardware-industrial-design \
  --draft --prerelease \
  --target 56125d1738a437f413ee4418c51c2f3a82bcbac8 \
  --title "gunnchOS Hardware Digital Engineering v1.0.0-rc.1" \
  --notes "Accepted main: 56125d1738a437f413ee4418c51c2f3a82bcbac8. DIGITAL_HARDWARE_ENGINEERING_RELEASE only — no fab/EVT/DVT/PVT/cert claims." \
  release_staging/v1.0.0-rc.1/hardware/gunnchOS-Hardware-Design-v1.0.0-rc.1.zip
```

## Research components (shared bundle + per-repo tags)

Attach `release_staging/v1.0.0-rc.1/research/research-systems-v1.0.0-rc.1.zip` on the umbrella release.  
Optional per-repo draft tags (no extra binaries required for RC1):

| Repo | `--target` |
|---|---|
| `7gc-digital-twin` | `dc43a567e3f2e81a5b59fea6dd67c7054cfdde56` |
| `spectrumx-ai-ran-gary` | `9060655e724374f60cbbb86832816c9c2d332ca4` |
| `readygary-6g-beam-selection` | `569875224db7812890ec6abc48dfe43a608094f3` |
| `ntn-resilience-sim` | `c4215fc1039f5452917b9b2034b42e03fdc13689` |
| `edge-io-measurement-node` | `af57fbdac857ae386b23b5b747fdc05797621f92` |
| `gunnchos-7gc-ai-ran-field-kit` | `9e93e41a3b16b009c9cc5163b775360d4d2ef693` |

Example:

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/7gc-digital-twin \
  --draft --prerelease \
  --target dc43a567e3f2e81a5b59fea6dd67c7054cfdde56 \
  --title "7GC Digital Twin v1.0.0-rc.1" \
  --notes "Pinned accepted main for gunnchOS Ecosystem v1.0.0-rc.1. Bundle on portal umbrella release."
```
