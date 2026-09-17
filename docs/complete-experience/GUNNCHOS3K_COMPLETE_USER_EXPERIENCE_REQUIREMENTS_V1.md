# gunnchOS3k Complete User Experience Requirements v1.0

**Status:** Normative requirements for Complete Experience program (CX0+)  
**Authority:** Portfolio Complete Experience control plane (`docs/complete-experience/`)  
**Non-authority:** Does **not** override Device Lab gate authority (Portal #14 / stream-p1), Device OS #134, or accepted-main pin manifests.

## 1. Purpose

gunnchOS3k must be a **complete primary computing experience**: a user can discover, learn, create, communicate, play, administer, and recover without requiring a second primary computer. High-end workloads may use **declared remote/cloud paths**; those paths must not delete local intended capability.

## 2. No-second-computer test

A capability domain is not COMPLETE until a named persona can:

1. Discover and onboard without external primary device dependency for the core path  
2. Complete an authentic workflow on a supported device profile  
3. Persist state across reboot / offline / reconnect  
4. Recover from common failure  
5. Export or share results  
6. Meet accessibility requirements for that persona  
7. Meet security/privacy requirements for that persona  

**Truth rules:** Build ≠ journey success; package install ≠ complete; schema ≠ certification; lint ≠ accessibility PASS.

## 3. Personas

learner, educator, creator, developer, hardware builder, office worker, gamer, family user, accessibility user, offline user.

See `PERSONA_JOURNEY_MATRIX.md` and `personas/*_ACCEPTANCE.md`.

## 4. Planes

| Plane | Role |
|-------|------|
| Device OS | Local runtime, sandbox/portal, peripherals, continuity, offline, support |
| WAIKE | Learning/teaching runtime + education interop |
| gunnchAI | System assistance via Capability Broker |
| Creative / games / maker | First-party + qualified FOSS providers |
| Portal | Complete Experience ownership registry + Device Lab release-control (separate authority) |
| Research / sim | Backing science; not substitute for product journeys |

## 5. Twenty-one capability domains

1. Onboarding / identity  
2. Files / sync / backup / recovery  
3. App discovery / install / update / rollback  
4. Browser / web / PWA  
5. Everyday productivity  
6. Email / calendar / chat / video / screen sharing  
7. Printers / scanners / peripherals  
8. Accessibility  
9. WAIKE learning / teaching  
10. Portfolio / credentials  
11. Creative studio  
12. Developer / data / AI / cyber / maker workstation  
13. gunnchAI  
14. Games / media / leisure  
15. Compatibility / remote execution  
16. Continuity  
17. Offline / low-bandwidth / community hub  
18. Security / privacy  
19. Firmware / driver / hardware lifecycle  
20. School / family / work administration  
21. Support / repair / ownership  

Machine-readable coverage: `CAPABILITY_REGISTRY.json`.

## 6. Ordinary-user mandatory baseline (P0 review)

Ordinary users must not be blocked on: identity/onboarding, files+backup+recovery, app install/update, browser, everyday docs/PDF, basic email/calendar path, printing path, accessibility inventory + AT path, offline basics, security/privacy consent, support diagnostics.

## 7. Device profiles

handheld_student, ds_xl, office_dock, fleet_admin, community_hub (and future profiles). Eligibility is profile-gated; absence on a profile must be explicit, not silent.

## 8. Completeness claim boundary

`FULL_COMPLETE_EXPERIENCE_COMPLETE=true` is forbidden until all persona acceptance plans have evidence-backed PASS. CX0 establishes the control plane only.
