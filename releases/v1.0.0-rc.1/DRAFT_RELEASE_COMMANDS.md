# Draft GitHub prerelease commands — v1.0.0-rc.1

**Authorization:** Edmund re-approved RC1 and authorized normal merge of portal PR #39 plus creation of **draft** `v1.0.0-rc.1` prereleases. RC1 publication is still a separate decision. Final `v1.0.0` is not authorized.

Run from the portal checkout that contains `release_staging/` and `release_staging_large/`.

## Umbrella portal

After PR #39 merges, set the exact accepted-main SHA:

```bash
POST_PR39_ACCEPTED_MAIN_SHA="$(git -C gunnchos-research-portal rev-parse origin/main)"

gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/gunnchos-research-portal \
  --draft --prerelease \
  --target "$POST_PR39_ACCEPTED_MAIN_SHA" \
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
  releases/v1.0.0-rc.1/APP_VERSION_MAPPING.md \
  releases/v1.0.0-rc.1/V1_RC1_GATES.json
```

## Device OS

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/gunnchos-device-os \
  --draft --prerelease \
  --target 2218ead0efa0e4b8a622717a0a9bf623ee95ddb0 \
  --title "gunnchOS Capsule / Device OS v1.0.0-rc.1" \
  --notes "Post-feedback accepted main. Production npm audit critical=0 high=0. Feedback hub live on portal main." \
  release_staging/v1.0.0-rc.1/device-os/gunnchOS-Capsule-Pixel6a-post-feedback-debug.apk \
  release_staging/v1.0.0-rc.1/device-os/gunnchOS-Capsule-Pixel6a-post-feedback-debug.apk.sha256 \
  release_staging/v1.0.0-rc.1/device-os/BUILD_MANIFEST.json \
  release_staging/v1.0.0-rc.1/device-os/RC1_REBUILD_MANIFEST.json \
  release_staging/v1.0.0-rc.1/device-os/RC1_STAGING_PROVENANCE.json \
  release_staging/v1.0.0-rc.1/device-os/INSTALL_UNINSTALL.md
```

## WAIKE Learning Platform

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/gunnchos-waike-learning-platform \
  --draft --prerelease \
  --target a4daa1d07a3ef8f6c00cf2b4a1692053bf99f518 \
  --title "WAIKE Learning Platform v1.0.0-rc.1" \
  --notes "Post-feedback accepted main. Web/PWA RC1 bundle." \
  release_staging/v1.0.0-rc.1/waike/waike-web-pwa-v1.0.0-rc.1.zip
```

## WAIKE Curriculum

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/waike-research-ops \
  --draft --prerelease \
  --target 34ae043abbd38c89bd30f7ae1ae7cf8cc06645a0 \
  --title "WAIKE Curriculum v1.0.0-rc.1" \
  --notes "18-track curriculum/research bundle from accepted main." \
  release_staging/v1.0.0-rc.1/curriculum/waike-curriculum-v1.0.0-rc.1.zip
```

## gunnchAI

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/gunnchAI3k \
  --draft --prerelease \
  --target 04eef2d891a8dda58455acc58a8e93e7865379b8 \
  --title "gunnchAI3k Runtime v1.0.0-rc.1" \
  --notes "Post-feedback accepted main. Runtime bundle only; no unauthorized model weights. Nearby Edge remains honestly unavailable." \
  release_staging/v1.0.0-rc.1/gunnchai/gunnchai-runtime-v1.0.0-rc.1.zip
```

## Games

```bash
gh release create v1.0.0-rc.1 --repo gunnchOS3k/anime-aggressors --draft --prerelease \
  --target 6cd1b3100a7e467c2c991394576891660deb1162 \
  --title "Anime Aggressors v1.0.0-rc.1" \
  --notes "Post-feedback accepted main. Debug APK + provenance." \
  release_staging/v1.0.0-rc.1/anime/anime-aggressors-debug-v1.0.0-rc.1.apk \
  release_staging/v1.0.0-rc.1/anime/anime-aggressors-debug-v1.0.0-rc.1.apk.sha256 \
  release_staging/v1.0.0-rc.1/anime/PROVENANCE.json

gh release create v1.0.0-rc.1 --repo gunnchOS3k/pedestrian-pursuit --draft --prerelease \
  --target 3e98106939786c69a64657f4cc2b9a652a3b5fec \
  --title "Pedestrian Pursuit v1.0.0-rc.1" \
  --notes "Post-feedback accepted main. APK attached externally because it exceeds the git blob limit." \
  release_staging_large/v1.0.0-rc.1/pedestrian/pedestrian-pursuit-debug-v1.0.0-rc.1.apk \
  release_staging/v1.0.0-rc.1/pedestrian/pedestrian-pursuit-debug-v1.0.0-rc.1.apk.sha256 \
  release_staging/v1.0.0-rc.1/pedestrian/PROVENANCE.json

gh release create v1.0.0-rc.1 --repo gunnchOS3k/archive-of-life-artifact-world --draft --prerelease \
  --target 03d734453f040e3081e763277e2c15aa62ef095e \
  --title "Archive of Life v1.0.0-rc.1" \
  --notes "Post-feedback accepted main. Debug APK + provenance." \
  release_staging/v1.0.0-rc.1/archive/archive-of-life-debug-v1.0.0-rc.1.apk \
  release_staging/v1.0.0-rc.1/archive/archive-of-life-debug-v1.0.0-rc.1.apk.sha256 \
  release_staging/v1.0.0-rc.1/archive/PROVENANCE.json

gh release create v1.0.0-rc.1 --repo gunnchOS3k/beatlink-party --draft --prerelease \
  --target e1a5d9998f93d707440f68673c0da844617dc10e \
  --title "BeatLink Party v1.0.0-rc.1 (web)" \
  --notes "Post-feedback accepted main. Web-only RC1; no APK." \
  release_staging/v1.0.0-rc.1/beatlink/beatlink-web-v1.0.0-rc.1.zip
```

## Hardware

```bash
gh release create v1.0.0-rc.1 \
  --repo gunnchOS3k/gunnchos-hardware-industrial-design \
  --draft --prerelease \
  --target af5af66a28e36351b3929ef15756b6df6381ff6a \
  --title "gunnchOS Hardware Digital Engineering v1.0.0-rc.1" \
  --notes "DIGITAL_HARDWARE_ENGINEERING_RELEASE only — no READY_FOR_FAB / EVT / DVT / PVT / certification claims." \
  release_staging/v1.0.0-rc.1/hardware/gunnchOS-Hardware-Design-v1.0.0-rc.1.zip
```

## Research component draft prereleases

The shared research bundle is attached to the umbrella release. Component draft prereleases pin accepted main and point users to the umbrella bundle.

```bash
gh release create v1.0.0-rc.1 --repo gunnchOS3k/7gc-digital-twin --draft --prerelease --target 9654ac82a722e800193e771556036dbb0df263db --title "7GC Digital Twin v1.0.0-rc.1" --notes "Accepted-main research component; shared research bundle is on the umbrella RC1."
gh release create v1.0.0-rc.1 --repo gunnchOS3k/spectrumx-ai-ran-gary --draft --prerelease --target 2dc41c73fa0b16cb5703b8876e7e199f9a1b2b0a --title "SpectrumX AI-RAN Gary v1.0.0-rc.1" --notes "Accepted-main research component; shared research bundle is on the umbrella RC1."
gh release create v1.0.0-rc.1 --repo gunnchOS3k/readygary-6g-beam-selection --draft --prerelease --target e04b38b48cd2ebd87243153ca8fad9e914f16b21 --title "ReadyGary 6G Beam Selection v1.0.0-rc.1" --notes "Accepted-main research component; shared research bundle is on the umbrella RC1."
gh release create v1.0.0-rc.1 --repo gunnchOS3k/ntn-resilience-sim --draft --prerelease --target 05aaa9aec16882f58bac6ce4ff47618d9812f69f --title "NTN Resilience Sim v1.0.0-rc.1" --notes "Accepted-main research component; shared research bundle is on the umbrella RC1."
gh release create v1.0.0-rc.1 --repo gunnchOS3k/edge-io-measurement-node --draft --prerelease --target 758b14a2c06b70a6678fc761d5360bde5e7cb235 --title "Edge IO Measurement Node v1.0.0-rc.1" --notes "Accepted-main research component; physical calibration claims remain pending where documented."
gh release create v1.0.0-rc.1 --repo gunnchOS3k/gunnchos-7gc-ai-ran-field-kit --draft --prerelease --target 4f3095e349f522d6db9901b99101f3fe5dff9f6c --title "7GC AI-RAN Field Kit v1.0.0-rc.1" --notes "Accepted-main research field-kit component; shared research bundle is on the umbrella RC1."
```

## Publication boundary

These commands create **draft prereleases**. Do not publish them and do not create final `v1.0.0` without a later explicit owner authorization.