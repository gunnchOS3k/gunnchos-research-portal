# Charter traceability matrix

**Charter source:** `gunnchos-7gc-ai-ran-field-kit` `program/charter/gunnchOS3k_PRODUCT_CHARTER.md` (and YAML twin). That repo is the product-charter SoT; this portal **indexes** it.

**Status words used here (no ambiguous PASS):**

`TARGET` · `IMPLEMENTED_DIGITAL` · `DIGITAL_VALIDATED` · `PHYSICAL_PENDING` · `EXTERNAL_PENDING` · `CERTIFICATION_PENDING` · `NOT_CURRENT_SCOPE`

“Carrier-grade-targeted” means reliability/evidence posture, not a conferred carrier certificate.

## First-party products

| Charter product | Role (must not regress) | Hardware / OS evidence | Status |
|---|---|---|---|
| Student 14.5 | Sustained learning/work | hardware `device_designs/student_14_5` + device-os desktop-class profiles | `IMPLEMENTED_DIGITAL` / `PHYSICAL_PENDING` |
| Handheld Hybrid | Mobile/docked compute | hardware digital release package earned; continuity SI unproven | `IMPLEMENTED_DIGITAL` / `PHYSICAL_PENDING` |
| DS-XL Coder | Local create/build/deploy | dual-eDP AVL `EXTERNAL_PENDING`; compositor contract digital | `IMPLEMENTED_DIGITAL` / `EXTERNAL_PENDING` / `PHYSICAL_PENDING` |
| Edge I/O Rings | Embodied spatial input | nRF52840 public path; absolute pose `PHYSICAL_PENDING` | `IMPLEMENTED_DIGITAL` / `PHYSICAL_PENDING` |
| First-party Dock | Continuity expansion | JHL topology; NDA balls `EXTERNAL_PENDING` | `TARGET` / `EXTERNAL_PENDING` / `PHYSICAL_PENDING` |

No first-party SKU is entertainment-only. Games are workloads, not the device identity.

## Sixteen charter layers → repos

| # | Layer | Primary repo(s) | Status |
|---|---|---|---|
| 1 | Industrial design | `gunnchos-hardware-industrial-design` | `IMPLEMENTED_DIGITAL` / `PHYSICAL_PENDING` |
| 2 | Electrical hardware | hardware (KiCad; 0 ERC/DRC errors, warnings remain) | `IMPLEMENTED_DIGITAL` / `PHYSICAL_PENDING` |
| 3 | Firmware | hardware + device-os | `IMPLEMENTED_DIGITAL` / `PHYSICAL_PENDING` |
| 4 | gunnchOS | `gunnchos-device-os` | `DIGITAL_VALIDATED` (CI) / `PHYSICAL_PENDING` boot |
| 5 | gunnchAI3k | `gunnchAI3k` | `IMPLEMENTED_DIGITAL` (no frontier-parity claim) |
| 6 | Connectivity | device-os, NTN sim, SpectrumX, 7GC twin | `IMPLEMENTED_DIGITAL` (`SYNTHETIC_SIM` / `OPEN_DATA_BACKED`) |
| 7 | Input ecosystem | device-os + Edge I/O | `IMPLEMENTED_DIGITAL` / `PHYSICAL_PENDING` |
| 8 | Applications | device-os app layer | `IMPLEMENTED_DIGITAL` |
| 9 | Games | anime, pedestrian, archive, beatlink | `IMPLEMENTED_DIGITAL` / `HUMAN_QA_PENDING` — `NOT_CURRENT_SCOPE` for dissertation papers |
| 10 | Cloud/edge | device-os + ops | `TARGET` / `IMPLEMENTED_DIGITAL` (partial) |
| 11 | Security operations | device-os + field-kit | `IMPLEMENTED_DIGITAL` / `EXTERNAL_PENDING` pentest |
| 12 | Manufacturing | hardware RFQ packets | `IMPLEMENTED_DIGITAL` packet; RFQ_SENT false; `EXTERNAL_PENDING` |
| 13 | Certification | hardware compliance track | `CERTIFICATION_PENDING` |
| 14 | Deployment | WAIKE + 7GC | `EXTERNAL_PENDING` |
| 15 | Support | portal + docs | `IMPLEMENTED_DIGITAL` |
| 16 | Evidence | portal + field-kit | `IMPLEMENTED_DIGITAL` (claim ≤ evidence) |

## Dissertation mapping

Charter layers 4–7 plus radio/twin/NTN research repos are the experimental stack for RQ1–RQ3. Charter games/education/AI products may supply **workload profiles** to RQ1; they are not Papers IV–N.

## Forbidden conversions

- Digital ERC/DRC 0 errors ≠ fabricated board.  
- `DIGITAL_VALIDATED` CI ≠ physical boot.  
- Charter “carrier-grade-targeted” ≠ certified.  
- No Oulu affiliation row.
