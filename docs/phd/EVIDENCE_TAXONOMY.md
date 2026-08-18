# Evidence taxonomy

Lower tiers must never be described as higher tiers.

| Class | Meaning | Typical in this portfolio |
|---|---|---|
| `SYNTHETIC_SIM` | Generated channels, mobility, or failures inside code | NTN sim; ReadyGary toy channel; 7GC synthetic sites |
| `OPEN_DATA_BACKED` | Public/competition dataset with recorded source | SpectrumX judged IQ path |
| `EMULATED` | Device Lab, browser, container, simulated sensors | Device OS lab; Edge I/O simulated device; games |
| `DEVICE_MEASURED` | Physical device, timestamps, calibration | **Not claimed** at baseline |
| `LAB_MEASURED` | Instrumented RF/compute lab | **Not claimed** |
| `EXTERNAL_REPRODUCED` | Independent researcher packet returned | **Not claimed** |
| `FIELD_VALIDATED` | Operational/field campaign | **Not claimed** |

## Composite metrics

If a continuity-utility scalar is published, the README/paper artifact must also expose weights, normalization, raw components, and weight sensitivity. Hiding components behind a score is a documentation defect.

## Regeneration rule

No result number may be typed into a README table unless a command regenerates it from raw/derived outputs. Toy or demo numbers must be labelled `SYNTHETIC_SIM` and must not be presented as measured RF latency.
