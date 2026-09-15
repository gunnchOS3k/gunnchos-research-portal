# ECOSYSTEM_SKU_RELEASE_MATRIX

Generated: `2026-09-15T04:52:44Z`  
JSON: [`ECOSYSTEM_SKU_RELEASE_MATRIX.json`](./ECOSYSTEM_SKU_RELEASE_MATRIX.json)

## Policy
- Physical hardware EVT must **not** falsely block commodity Windows software pilots.
- Digital PASS ≠ production readiness.
- Simulation ≠ physical PASS; build ≠ UX; coverage ≠ human approval.

| Surface | SKU | Version | Platform | Market | Evidence class | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Windows Software Pilot | software_pilot_windows | Pilot-0 | Windows | internal_adult | ACCEPTED_MAIN_DIGITAL_PASS | WINDOWS_PILOT0_ACCEPTED_MAIN_PASS=true; not RC Software Pilot ready |
| gunnchOS Interactive Guest | gunnchos_interactive_guest | current-pin-candidate | gunnchOS_emulation | internal | DRAFT_DIGITAL_CANDIDATE | LIVE/DSXL/Ring PASS on device-os #134 draft; DIGITAL_DEVICE_LAB_CURRENT_PIN_PASS=false |
| Student pre-EVT | student_14_5 | pre-EVT | target_hardware | education | PHYSICAL_VALIDATION_PENDING | Digital EVT packet ready; firmware digital FAIL; NDA |
| Handheld pre-EVT | handheld_hybrid | pre-EVT | target_hardware | consumer | PHYSICAL_VALIDATION_PENDING | Digital packet ready; firmware digital FAIL |
| DS-XL pre-EVT | ds_xl_coder | pre-EVT | target_hardware | creator | PHYSICAL_VALIDATION_PENDING | DSXL compositor UX digital PASS in lab candidate ≠ physical EVT |
| Ring functional EVT | edge_io_rings | EVT | target_hardware | input | PHYSICAL_VALIDATION_PENDING | FIRMWARE_DIGITAL_BUILD_PASS=true; EVT_PHYSICAL_PASS=false |
| WAIKE staff alpha | waike_staff_alpha | alpha | desktop/web | education_staff | HUMAN_VALIDATION_PENDING | Digital baseline Gate D on main; human pending |
| WAIKE learner/instructor alpha | waike_learner_instructor_alpha | alpha | desktop/web | education | HUMAN_VALIDATION_PENDING | No K-12 classroom claim |
| gunnchAI internal alpha | gunnchai_internal_alpha | alpha | desktop/cli | internal | HUMAN_VALIDATION_PENDING | Digital green; HUMAN_E6 false |
| game desktop/Windows RC | games_windows_rc | RC-candidate | Windows | internal | DRAFT_DIGITAL_CANDIDATE | Pilot0 digital candidates; Device Lab Four-Game still open |
| game Android/Pixel candidate | games_android_pixel | candidate | Android_Pixel | internal | PHYSICAL_VALIDATION_PENDING | Anime PENDING_DEVICE; BeatLink smoke retained |
| book reader-preview candidate | technology_landscape_reader_preview | main@8d56d214fa64 | web_reader_preview | education_general | HUMAN_VALIDATION_PENDING | Repo gunnchos-technology-landscape; reader-preview CI green; human validation pending |
| creation/developer workflow alpha | creation_dev_workflow | alpha | gunnchOS_emulation/desktop | creator | DIGITAL_BLOCKED | Creator journeys exist; current-pin E2E not closed |
