# RELEASE_DEPENDENCY_GRAPH — STREAM P1

Generated: `2026-09-06T19:08:26Z`

```text
[gunnchos-research-portal]  control-plane freeze / release registers
        |
        +--> accepted-main pins for all product repos
        |
[gunnchos-device-os] ---- digital guest/lab ----+
        |                                       |
        +--> device-lab integration             |
        |      (games + gunnchAI + WAIKE)       |
        v                                       v
[anime-aggressors]  [pedestrian-pursuit]  [archive-of-life]  [beatlink-party]
        |                  |                     |                  |
        +------------------+---------------------+------------------+
                           |
                           v
                 RC-SOFTWARE-PILOT (DIGITAL only)
                           |
                           v (requires TARGET_HARDWARE)
[gunnchos-hardware-industrial-design] + [edge-io-measurement-node]
                           |
                           v
                   RC-HARDWARE-EVT
                           |
                           v (requires EXTERNAL + REGULATORY + CARRIER + MANUFACTURING + RIGHTS + HUMAN)
                   PRODUCTION-RELEASE
```

## Critical dependency notes
- **WAIKE Learning Platform** accepted main (`43e770772b97`) includes merged PR #3/#4; open PR #5 does **not** unlock pilot readiness until owner merge + digital gates.
- **Device OS** digital lock ≠ physical OS ship; dock continuity and physical Ring remain blockers for EVT.
- **BeatLink** product loop depends on rights-safe catalog; commercial DSP/stream providers are EXTERNAL/RIGHTS and cannot be assumed.
- **Archive** campaign can ship sample/authored tiers only while `ALL_SPECIES_INGESTED=false`.
- **gunnchAI** digital capability on main does not imply HUMAN eval PASS or frontier parity.
- **Field kit / portal** are orchestration/evidence planes; they do not clear hardware or carrier gates.
