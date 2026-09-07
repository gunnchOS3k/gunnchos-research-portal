## STREAM P1 RC0 — Windows Pilot 0 remote CI verification

**Owner merge authority:** Edmund Gunn Jr. — Cursor merges nothing.  
**PR:** #14 only (`release/stream-p1-rc0-digital-freeze`). Do not open a competing RC0 PR / do not create portal PR #15.

### Snapshot (`2026-09-07T22:49:22Z`)
- `gh` auth: **broken** (invalid keyring token). Observation via public GitHub API + Actions HTML.
- Exact-head remote Windows CI: **partial** — Archive + BeatLink **OBSERVED_GREEN** (soak ≥1800s); Device OS **NOT_APPLICABLE** green; WAIKE / gunnchAI / Anime / Pedestrian **BLOCKED** (harness fixes pushed; re-runs pending).
- Device Lab current-pin: **NOT started** this gate.
- Anime Pixel: **PENDING_DEVICE** unchanged.
- BeatLink: rights-safe software candidate only; commercial rights + multiplayer PASS remain false.
- gunnchAI: `HUMAN_EVALUATION=PENDING_HUMANS` unchanged.
- Hardware EVT / manufacturing / human studies: **not started**.

### Windows candidate PRs (draft; Cursor merges nothing)
| Product | Class | Verdict | PR | Candidate head | Observed CI |
|---|---|---|---|---|---|
| WAIKE Learning Platform | WINDOWS_NATIVE_DESKTOP | **BLOCKED** | [#8](https://github.com/gunnchOS3k/gunnchos-waike-learning-platform/pull/8) | `36e83dd1b75c` | Tauri NSIS build still failing after bootstrap fix; re-run after split vite/tauri steps |
| gunnchAI3k | WINDOWS_CLI_SERVICE | **BLOCKED** | [#46](https://github.com/gunnchOS3k/gunnchAI3k/pull/46) | `453c2b700ff1` | Prior head `770f11bf3755` failed: BUILD_FAILED / NO_DIST (`cmd /c` argv bug); fix pushed |
| Anime Aggressors | WINDOWS_WEB_PWA | **BLOCKED** | [#98](https://github.com/gunnchOS3k/anime-aggressors/pull/98) | `ef9b87fbe273` | Prior head hung on Godot export; 900s timeout pushed |
| Pedestrian Pursuit | WINDOWS_NATIVE_DESKTOP | **BLOCKED** | [#23](https://github.com/gunnchOS3k/pedestrian-pursuit/pull/23) | `e3c5f0bcf667` | Prior head evidence step age >4000s (export hang); 900s timeout pushed |
| Archive of Life | WINDOWS_WEB_PWA | **PASS** | [#36](https://github.com/gunnchOS3k/archive-of-life-artifact-world/pull/36) | `89f0bb447c27` | windows-2025 **success**; evidence step **1819s**; artifact `archive-windows-pilot0-*` |
| BeatLink Party | WINDOWS_WEB_PWA | **PASS** | [#26](https://github.com/gunnchOS3k/beatlink-party/pull/26) | `b20a570a8173` | windows-2025 **success**; evidence step **1836s**; artifact `beatlink-windows-pilot0-*` |
| Device OS | WINDOWS_NOT_APPLICABLE | **NOT_APPLICABLE** | [#133](https://github.com/gunnchOS3k/gunnchos-device-os/pull/133) | `4ab2a29e233f` | Classification job **success** ([run 34163332433](https://github.com/gunnchOS3k/gunnchos-device-os/actions/runs/34163332433)) |

### Verdicts
| Verdict | Value |
|---|---|
| `WINDOWS_PILOT0_ACCEPTED_MAIN_PASS` | **false** |
| `WINDOWS_PILOT0_CANDIDATES_READY_FOR_OWNER` | **false** |
| `WINDOWS_CEASED_TO_BE_DIGITAL_BLOCKER` | **false** |
| `RC_SOFTWARE_PILOT_READY_FOR_OWNER` | **false** |
| `HARDWARE_EVT_READY_TO_EXECUTE` | **false** |
| `PRODUCTION_RELEASE_READY_FOR_OWNER` | **false** |

### Why Windows is still a digital blocker
1. Required set not all PASS on exact heads (WAIKE / gunnchAI / Anime / Pedestrian still BLOCKED or re-running).
2. Accepted mains still lack Windows Pilot 0 evidence until Edmund merges candidates + revalidates.
3. Prefer honest PARTIAL/BLOCKED over false PASS. Artifact private download blocked without auth (ImageOS/ImageVersion recorded as present-in-artifact where green).

### Next gate (recommendation only — not started)
`DEVICE_LAB_CURRENT_PIN_REVALIDATION`

### Non-claims
No physical quartet, classroom, WCAG, FERPA, carrier, cert, commercial music rights, signing/production, or manufacturing PASS inferred from Windows candidate CI.
