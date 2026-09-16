# CX2 Control — Real Surface Productization

Stacked on Portal CX1 (#17). Does not touch Portal #14/#15.

## Device OS DRAFT stack

| PR | Branch | Base |
|----|--------|------|
| #137 CX2A | `eng/cx2a-real-experience-surfaces` | CX1 #136 |
| #138 CX2B | `eng/cx2b-real-provider-integrations` | CX2A |
| #139 CX2C | `eng/cx2c-authentic-user-journeys` | CX2B |

## Evidence taxonomy (revised)

CONTRACT_PASS, HARNESS_PASS, REAL_PROVIDER_CLI_PASS, REAL_PROVIDER_GUI_PASS,
REAL_USER_JOURNEY_DIGITAL_PASS, HUMAN_VALIDATION_PENDING, PHYSICAL_VALIDATION_PENDING,
EXTERNAL_PROVIDER_PENDING, NOT_APPLICABLE

CX1 fixture/marker DIGITAL_PASS claims → HARNESS_PASS (history retained under `artifacts/complete_experience/cx1/`).

## Pending (honest)

- HUMAN_A11Y_PENDING / HUMAN_VALIDATION_PENDING
- PHYSICAL_PRINTER_VALIDATION_PENDING
- Chat/video HUMAN_AV_QUALITY_PENDING + PHYSICAL_CAMERA_MIC_PENDING
- Browser GUI download/chooser
- Flatpak on hosts without Flatpak
- xdg-desktop-portal outside Linux session

`FULL_COMPLETE_EXPERIENCE_COMPLETE=false`
