# gunnchOS Hardware Design v1.0.0-rc.1 — Digital Engineering Release

**Classification:** `DIGITAL_HARDWARE_ENGINEERING_RELEASE`  
**Accepted main:** `56125d1738a437f413ee4418c51c2f3a82bcbac8` (`gunnchos-hardware-industrial-design`)  
**Outside V1:** PR #84; experimental PRs #69–#79

This release presents architecture, EDA/export packages, BOM/AVL state, mechanical/industrial docs, firmware/interface docs, and validation **plans**. It does **not** claim READY_FOR_FAB, EVT/DVT/PVT PASS, RF/carrier/regulatory/battery-transport certification, manufacturing yield, or warranty/RMA readiness.

## Device Quartet

### Student 14.5"

| Field | V1 statement |
|---|---|
| Research/product role | Primary portable learning/work laptop form factor |
| Intended UX | All-day coursework, WAIKE, local AI assist, browser/productivity |
| Major architecture | AMD Platform Core class mainline (see repo architecture docs) |
| Design evidence | Device design docs, BOM/AVL, EDA packages on accepted main |
| Software relationship | Targets gunnchOS Device OS + Capsule parity journeys |
| Validation state | Digital engineering complete for RC1; physical gates pending |
| Remaining physical gates | EVT → DVT → PVT; certification suite |

### Handheld Hybrid

| Field | V1 statement |
|---|---|
| Research/product role | Portable hybrid compute + interactive experience device |
| Intended UX | Games/experiences + learning bursts + field demos |
| Major architecture | Handheld hybrid platform docs on accepted main |
| Design evidence | Industrial/mechanical + electrical packages |
| Software relationship | Capsule/experiences demo path on Pixel stands in for UX until HW |
| Validation state | Digital engineering |
| Remaining physical gates | EVT/DVT/PVT + handheld RF/thermal |

### DS-XL Coder

| Field | V1 statement |
|---|---|
| Research/product role | High-display coder / creator workstation form factor |
| Intended UX | Dual-display coding, research tooling, local model hosts |
| Major architecture | DS-XL mainline docs (experimental SoC variants OUTSIDE V1) |
| Design evidence | Architecture + BOM + EDA on main |
| Software relationship | Host for gunnchAI Nearby Mac / local services when available |
| Validation state | Digital engineering |
| Remaining physical gates | EVT/DVT/PVT |

### Edge IO Wearables

| Field | V1 statement |
|---|---|
| Research/product role | Wearable sensing / ring-class I/O for measurement + HCI |
| Intended UX | Privacy-preserving measurement; spatial input research |
| Major architecture | Edge IO + ring/dock supporting hardware docs |
| Design evidence | Wearable electrical/mechanical packages; Edge IO software repo |
| Software relationship | `edge-io-measurement-node` measurement + export path |
| Validation state | Digital engineering + software measurement demos |
| Remaining physical gates | Wearable EVT; battery transport; body-worn safety |

### Dock / supporting hardware

Where documented on accepted main: first-party dock / charge / I/O expansion — digital packages only; same physical-gate boundary.

## Artifact

`release_staging/v1.0.0-rc.1/hardware/gunnchOS-Hardware-Design-v1.0.0-rc.1.zip`

## Feedback & Suggestions

Public feedback hub: [FEEDBACK.md](FEEDBACK.md)  
Security (private only): [SECURITY.md](SECURITY.md)  
Do not post exploitable security details publicly.

