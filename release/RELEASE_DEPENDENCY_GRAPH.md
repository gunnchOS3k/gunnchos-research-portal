# RELEASE_DEPENDENCY_GRAPH — STREAM P1 (Post–Gate D)

Generated: `2026-09-07T20:59:22Z`

```text
[gunnchos-research-portal PR #14]  control-plane freeze / release registers
        |
        +--> accepted-main pins for all product repos
        |
[gunnchos-device-os 4f02a48780d3] ---- digital guest/lab ----+
        |                                                    |
        +--> device-lab integration (NEEDS current-pin revalidation)
        v
[anime] [pedestrian] [archive] [beatlink] + [WAIKE LP ef73dc1804b9 Gate D] + [gunnchAI]
        |
        v
RC-SOFTWARE-PILOT (DIGITAL)  --blocked-by-->  Windows READY_PACKET + Device Lab revalidation + soaks
        |
        v (requires TARGET_HARDWARE)
[hardware-industrial-design] + [edge-io]  --EVT ranking--> Rings conditional first
        |
        v
RC-HARDWARE-EVT
        |
        v (EXTERNAL + REGULATORY + CARRIER + MANUFACTURING + RIGHTS + HUMAN)
PRODUCTION-RELEASE
```

## Critical dependency notes
- **WAIKE Learning Platform** accepted main (`ef73dc1804b9`) includes merged Gates B/C/D; Gate D is the digital baseline for staff-alpha prep.
- **Device OS** tip advanced with WAIKE learning integration; device-lab tokens must be re-earned on this tip.
- **Windows** is REQUIRED_NOW for Pilot 0 readiness and currently READY_PACKET only.
- **BeatLink** Pilot 0 uses rights-safe catalog only; commercial DSP/stream rights remain EXTERNAL/RIGHTS.
- **Archive** must not claim all-species complete.
- **gunnchAI** digital ≠ HUMAN eval PASS.
- **Physical gunnchOS** is not a Software Pilot prerequisite (EVT path).
