# V3.1 Pre-Human Closure — Post-Salvage Addendum

**Playbook:** `CURSOR_V3_1_POST_SALVAGE_PIXEL_PREHUMAN_CLOSURE`  
**Control branch:** `acceptance/v3-1-post-salvage-pixel-prehuman`  
**Historical V3 preserved at:** `artifacts/acceptance/v3/` and `docs/acceptance/v3/` (not overwritten)

## What changed since V3

| Stale V3 fact | V3.1 live truth |
|---|---|
| Anime #115 draft-only | **MERGED** `1dcbf7af` |
| Anime main pre-#115 | Tip `4b54b2c4` includes **#115 + #116** |
| PR106 salvage open | **#116 MERGED**; legacy **#106 CLOSED** superseded |
| Portal V3 packet draft #47 | **MERGED** `e1d349d` |
| Pixel connected=false | Still **false** this pass → `REQUIRES_PHYSICAL` |
| FIXABLE Anime web CI | Closed by #115; **new** Pedestrian Gate1 failure open |

## Preconditions

- `V3_1_POST_SALVAGE_PRECONDITIONS_PASS=true` (digital salvage path)
- Pixel USB authorize still required for exact-head installs

## Digital status

- `UNKNOWN_GATE_COUNT=0`
- `FIXABLE_DIGITAL_FAILURE_COUNT=1` — Pedestrian `godot-headless-no-false-green` / `BetaProductStateTest` online-arch private scope after PartyLink #37
  - Draft fix branch: `fix/v3-1-beta-online-arch-scope` (`private_same_room_lan_v1`)
  - Local revalidation: PASS on Godot 4.7.1
- Anime tip CI after #116: in progress / queued at report time (taste-gate already success)

## Pixel status

- `adb devices` empty → no installs, no signer checks, no logcat
- `PIXEL_CONNECTED_PASS=false`
- `PIXEL_EXACT_HEAD_MATRIX_COMPLETE=false`
- Owner test script + topology prepared under `docs/acceptance/v3_1/` and `artifacts/acceptance/v3_1/pixel/`

## Required-false (unchanged)

```text
ANIME_8_HUMAN_PHYSICAL_SESSION_PASS=false
PEDESTRIAN_8_HUMAN_PHYSICAL_SESSION_PASS=false
HARDWARE_QUARTET_EVT_PASS=false
RINGS_PHYSICAL_PASS=false
GLOBAL_DATA_COMPLETE=false
RIGHTS_PROVENANCE_RELEASE_PASS=false
REAL_RIC_FIELD_PASS=false
DIGITAL_ECOSYSTEM_V1_RELEASE_AUTHORIZED=false
```

Human fun / feel / authored-animation originality / final-art gates remain false.

## NEXT

```text
NEXT_MASTER_ACTION=OWNER_MERGE_PEDESTRIAN_GATE1_FIX_THEN_CONNECT_PIXEL_FOR_V3_1_EXACT_HEAD
```

After Pedestrian Gate1 fix is on main **and** Pixel is connected with signer-safe exact-head installs complete with no new fixable digital failures:

```text
NEXT_MASTER_ACTION=RUN_OWNER_FRIEND_AND_ASYNC_HUMAN_ACCEPTANCE
```

Nothing merged automatically by this pass.


## Pixel reconnect update (post owner claim)

Owner reported Pixel connected. Automation host still observes:

- `adb devices -l` → empty
- USB enumerator → no Android/Pixel gadget
- mDNS `_adb._tcp` → none

Exact-head APKs prepared (not installed):

- Anime `4b54b2c4` sha256 `a6f7545e245c963109dcf1f196a50c222f66639f496bc8ba9c9003fa51a8501a`
- Pedestrian `77a5413` sha256 `a006f7c80efd0b7da36f2ba9976f40a8682373934939c46e1504d4fd88cbcdfd` (post-#38)

```text
NEXT_MASTER_ACTION=AUTHORIZE_PIXEL_ADB_ON_THIS_HOST_THEN_INSTALL_EXACT_HEAD_APKS
```
