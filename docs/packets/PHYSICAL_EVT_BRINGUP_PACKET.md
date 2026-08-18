# Physical EVT bring-up packet

**Status:** `PHYSICAL_PENDING`

## Why blocked

Hardware industrial design and device OS digital paths cannot substitute for assembled EVT hardware.

## Prerequisite

Fabricated/assembled EVT unit matching the hardware repo revision; lab ESD/power setup; firmware image from the matching OS/hardware SHAs.

## Owner action

Follow the hardware repo bring-up checklist (do not invent voltages). Record:

- board ID / serial  
- firmware hash  
- boot log  
- failed/passed test points  

## Expected evidence

`artifacts/evt/` in hardware and device-os repos with photos optional, logs required.

## Status transition

Successful bring-up → still not certification. Enables `DEVICE_MEASURED` for boot/power rails only after recorded procedures pass.
