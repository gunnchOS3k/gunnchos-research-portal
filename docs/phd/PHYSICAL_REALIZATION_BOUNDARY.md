# Physical realization boundary

Desired digital/physical split:

> Everything that can be completed digitally before procurement/fabrication is complete; remaining work requires actual components, fabrication, assembly, bring-up, physical measurement, certification, or external manufacturer activity.

## Digitally in-scope (software/CAD/docs)

- Requirements, ICD, BOM, schematics/PCB projects, ERC/DRC **if files and tools exist**  
- Mechanical CAD, stack-up notes, harness definitions, factory/bring-up checklists  
- Firmware manifests, flashing *procedures*, simulated Device Lab  
- RFQ **packets** (not sending)  
- OS/hardware traceability documents  

## Must remain pending without hardware/lab

| Item | Status word |
|---|---|
| EVT assembly / bring-up | `PHYSICAL_PENDING` |
| RF antenna validation | `PHYSICAL_PENDING` |
| Thermal chamber / skin-temp | `PHYSICAL_PENDING` |
| Battery runtime on metal | `PHYSICAL_PENDING` |
| Edge I/O absolute spatial accuracy | `PHYSICAL_PENDING` |
| Pixel 6a | USB-C connected 2026-08-18 ~21:15Z; serial `27211JEGR06194` listed as **unauthorized**. PIXEL_6A_READY = **BLOCKED**. Owner must accept the USB debugging prompt. |
| CUDA NR timings | `BLOCKED_GPU` on CPU-only hosts |
| FCC / CE / USB-IF / carrier | `EXTERNAL_PENDING` |
| RFQ send / fab PO | `EXTERNAL_PENDING` |

Do not invent electrical values to close a gate. Unverified component specs stay unresolved.

Owner packets: [PHYSICAL_EVT_BRINGUP_PACKET.md](../packets/PHYSICAL_EVT_BRINGUP_PACKET.md), [RF_LAB_VALIDATION_PACKET.md](../packets/RF_LAB_VALIDATION_PACKET.md), [MANUFACTURER_RFQ_SEND_PACKET.md](../packets/MANUFACTURER_RFQ_SEND_PACKET.md).
