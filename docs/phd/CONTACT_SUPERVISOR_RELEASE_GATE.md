# Contact-supervisor release gates

Two gates. They must not be collapsed.

## `AUTOMATABLE_SUPERVISOR_READY`

**Meaning.** Everything that can reasonably be completed in software, simulation, documentation, tests, UML, CI, packaging, and local emulation — without physical manufacturing, RF/lab measurements, independent human reproduction, playtests that require a person, certifications, purchases, emails, visibility changes, or supervisor contact — is complete.

**PASS only if** all 16 in-scope repositories on branch `cursor/supervisor-ready-portfolio-release-001` (or documented continuation) satisfy:

- current UML is not a placeholder and is separated from future/legacy  
- canonical run/test/reproduce commands exist and are not contradictory  
- core RQ repos capture seeds/config/SHA in a reproduce path  
- READMEs match evidence labels  
- no committed secrets  
- licenses present  
- portal dashboard regenerates from live audit  
- known technical errors (for example 28 GHz labelled Sub-6) are corrected  
- Android/PWA apps have Pixel 6a **packets** even if the phone is unauthorized  

**Baseline (this audit):** `FAIL` — see [PORTFOLIO_READINESS_DASHBOARD.md](PORTFOLIO_READINESS_DASHBOARD.md).

## `CONTACT_SUPERVISOR_READY`

**Meaning.** A prospective supervisor can be sent public links without embarrassment, can access every cited private artifact, and the remaining blockers are only those a laboratory should own.

May remain **BLOCKED** after the automatable gate passes when any of these remain:

- independent reproduction  
- physical-device / RF validation  
- human usability/playtest evidence  
- owner review / merge  

GPU NR and emergent-protocol repositories are **public** (verified 2026-08-18). Visibility is no longer a faculty 404. CUDA timings remain `BLOCKED_GPU` without a lab GPU.

Pixel 6a digital install+launch smoke is **PASS**; playtest quality stays `HUMAN_QA_PENDING`.  

**Baseline:** `BLOCKED`.

### Smallest owner actions after automatable PASS

Exact packets (do not execute from this agent):

1. [SUPERVISOR_CONTACT_USER_ACTION.md](../packets/SUPERVISOR_CONTACT_USER_ACTION.md)  
2. [REPOSITORY_VISIBILITY_PACKET.md](../packets/REPOSITORY_VISIBILITY_PACKET.md)  
3. [EXTERNAL_REPRODUCTION_PACKET.md](../packets/EXTERNAL_REPRODUCTION_PACKET.md)  
4. [PIXEL_6A_ACCEPTANCE_PACKET.md](../packets/PIXEL_6A_ACCEPTANCE_PACKET.md)  

## Forbidden conversions

- A test passing does not prove physical readiness.  
- A smoke test does not prove research validity.  
- A simulation does not prove real RF performance.  
- A generated RFQ package does not mean an RFQ was sent.  
- An Android build does not mean Pixel 6a acceptance.  
- A mock service is not a production service.
