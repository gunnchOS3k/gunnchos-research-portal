# Pixel Latest-and-Greatest — Owner Test Menu

Physical baseline: **Pixel 6a (bluejay) / Android 17**  
Evidence root: `artifacts/pixel_full_matrix/`

Human/fun/feel/8P/release/final-art gates stay **FALSE** until you enter them.

## Native apps

### gunnchOS Capsule
- Package: `com.gunnchos.capsule.debug`
- Exact main SHA: `2ae070fd8b050c3520ed8dac211e0d607bf9f63f`
- 3–8 min smoke: launch → shell home → App Center → WAIKE/Games/MLV routes if shown → Back continuity → no crash
- Ask: Does home feel like gunnchOS? Any dead ends?

### Anime Aggressors
- Package: `com.gunnchos.animeaggressors`
- Exact main SHA: `72e5dada4e557b42b6abb8c85f218f0a5b3d2e35` (post-#117 merge)
- Version: 0.3.7 / 219
- 3–8 min smoke: launch → fighter select → battle → Party Mode create/lobby/Arena View/QR → reduced motion → no crash
- Ask: Does Party Mode invite feel fun? Would you show a friend?

### Pedestrian Pursuit
- Package: `com.gunnchos.pedestrianpursuit`
- Exact main SHA: `77a5413c15e0d25524fe5381e117678aa2d42edf`
- Version: 0.4.3-race-experience-v3 / 18
- 3–8 min smoke: launch → race → course select → Party Race lobby / Race Director → phone controller route → no crash
- Ask: Does racing feel good enough to continue?

### Archive of Life
- Package: `com.gunnchos.archiveoflife`
- Exact main SHA: `23ce4dafc2711449cab43a5bb6f42698c61ed2a1`
- Version: 1.1.1 / 3
- 3–8 min smoke: splash → museum/home → Begin → map/fossil → observation → ArchiveDex search → Sources & Evidence → no crash
- Ask: Is ArchiveDex usable at large list sizes? Keep GLOBAL_DATA_COMPLETE=false.

### BeatLink Party
- Package: `com.gunnchos.beatlinkparty`
- Exact main SHA: `e1a5d9998f93d707440f68673c0da844617dc10e`
- Version: 1.1.2 / 4
- 3–8 min smoke: launch → create room → join → same-LAN → reconnect → host/player → no stuck room
- Ask: Does room flow feel party-ready without claiming Spotify rights?

## Chrome / PWA

### 3k MLV (+ seven 7GC campuses + Network Twin)
- URL (USB reverse): `http://127.0.0.1:4174/3k-mlv/`
- Exact main SHA: `94cba498f7b6b4b78825af16d9ed403bdb617eaf`
- Commands: `adb reverse tcp:4174 tcp:4174` then open the URL in Chrome
- Use **Enter local test identity** if hosted Supabase is unset
- 3–8 min smoke: Home → Campus → 7GC Atlas → Gary/Ghana/Guyana/Geelong/Germany/Gaza/Graham Land → Network Twin Lab → Gallery privacy → portrait/landscape → Android Back
- Ask: Do campuses feel distinct? Any privacy leaks in Gallery?

### WAIKE (+ gunnchAI surface)
- Hub `8000` / client `1420` via `tools/pixel_pilot/run_pixel_pilot.py`
- Exact main SHA target: `9966e95b84a8b008ea50ffebd3f851950c1136be`
- Status this pass: **exact-main web client PASS** (`9966e95…`); offline reconnect PASS; 18 tracks loaded; Ask gunnchAI surface NOT earned (`PIXEL_WAIKE_AI_SURFACE_PASS=false`); learner physical visibility journey false on short soak
- When green: learner Today → Continue Learning → lesson → Study/Listen/Ask gunnchAI → submit/receipt → Grades → Calendar → offline/reconnect → 18-track visibility
- Ask: Is Ask gunnchAI honest about local vs live provider?
- Keep `GUNNCHAI_LIVE_PROVIDER_QUALIFICATION_PASS=false` unless live credentials used
- Native Android Phase B remains **DEFER**

## Not on this Pixel as standalone products
7GC backends, AI-RAN field kit, SpectrumX, Edge-IO node, Hardware Quartet EVT, Edge IO Rings.

## After walkthrough
Enter human gates only after real owner play. Then friend/async acceptance.
