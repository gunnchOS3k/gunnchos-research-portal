# RF / lab validation packet

**Status:** `PHYSICAL_PENDING` / `LAB_MEASURED` not claimed

## Why blocked

No instrumented RF campaign (OTA, chamber, base-station, NTN emulator) is in the audited evidence.

## Prerequisite

Access to a wireless lab / test network (for example CWC-class resources). This packet does not request that access.

## Owner/lab action

Freeze software SHAs; run the repo’s RF procedure; store IQ/logs **without** dumping secrets or licensed traces into public git unless license allows.

## Expected evidence

`LAB_MEASURED` artifacts with instrument IDs, calibration dates, and scripts that regenerate tables.

## Status transition

Only after recorded measurements. Simulations stay `SYNTHETIC_SIM`.
