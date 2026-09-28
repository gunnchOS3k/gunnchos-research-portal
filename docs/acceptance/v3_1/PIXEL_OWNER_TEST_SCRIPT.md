# Pixel Owner Test Script — V3.1

**Device expected:** Pixel 6a / `bluejay` (trust live `adb` output)  
**This pass:** Pixel **not connected** — script is readiness-only until USB debugging is authorized.

## Safety

- Prefer `adb install -r <apk>` only after signer compatibility is confirmed.
- Never `adb uninstall` / `pm clear` / factory reset / wipe / downgrade without explicit owner approval.
- Record serial only in local evidence; redact if published.
- Exact-head APKs only; SHA must match reviewed build.

## PartyLink physical topology (not one-Pixel 8P)

```text
DISPLAY HOST:  Mac/PC/TV browser
PLAYER 1:      Pixel 6a
PLAYERS 2–8:   other phones/tablets/laptops/browsers
SPECTATORS:    separate browsers/screens
```

Minimum before calling PartyLink human session complete:

- 2 real humans/devices
- one shared display
- one spectator join
- disconnect/reconnect
- results/rematch

Desired extended: 4 real players, then 8 if available. Automation 8P ≠ human validation.

## Session sections (refresh from V3 where main changed)

1. **gunnchOS / device-os Pixel** — install/upgrade, launch, MLV route, WAIKE route, return continuity, Home/Campus/Gallery, no crash, build identity  
2. **3k MLV mobile web** — Home, Campus, Gallery, Network Twin, degraded-host behavior (Chrome; no native APK)  
3. **Anime core** — launch, battle, fighter select, reduced-motion, no crash, exact SHA  
4. **Anime PartyLink / Arena** — Party Mode entry, create-room, LAN controller URL/QR, Arena View; Pixel as **one** controller only  
5. **Pedestrian core** — launch, race, no crash, exact build identity  
6. **Pedestrian Party Race / Race Director** — Party Race entry, Race Director display, phone/browser controller  
7. **Archive of Life** — museum/start, map/expedition, ArchiveDex, search/pagination, Sources & Evidence, offline/degraded; no global-completeness claims  
8. **BeatLink** — create/join, reconnect, multi-client; no Spotify/commercial-music claim  
9. **WAIKE supported surface** — mobile-web if usable; do not claim native Android unless proven  

## Separate blockers (do not flip)

- Hardware Quartet physical EVT  
- Edge IO Rings physical validation  
- Rights  
- Scientific source snapshots  
- Live gunnchAI provider  
- Real AI-RAN field/RIC/carrier  
- Institutional WAIKE pilot  

## Ask every tester

- What confused you?  
- What felt unfinished / amateur / slow?  
- What did you expect?  
- Would you use/play this again?  

Owner must not rescue immediately; record hesitation and wrong turns first.
