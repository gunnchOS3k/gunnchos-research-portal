# Owner RC1 Review Packet — gunnchOS Ecosystem v1.0.0-rc.1

**Audience:** Edmund (owner)  
**Policy:** Do not merge PR #39, publish RC1, or publish final `v1.0.0` until this review is complete and explicitly authorized.  
**Flags:** Keep `RC1_OWNER_APPROVAL=false` and `V1_0_0_RELEASE_AUTHORIZED=false` until you flip them.

No boxes below are pre-checked.

## Front door & docs

- [ ] START_HERE clarity (paths for recruiter / PhD / engineer / educator / Pixel demo)
- [ ] Recruiter page (`RECRUITER.md`)
- [ ] PhD advisor page (`PHD_ADVISOR.md`)
- [ ] Hardware page (`HARDWARE_V1.md`) — digital-engineering boundary only
- [ ] Research page (`RESEARCH_V1.md`)
- [ ] Experiences page (`EXPERIENCES_V1.md`)
- [ ] QR behavior (encodes tagged `v1.0.0-rc.1` START_HERE; branch URL is preview only)

## Pixel career-fair path

- [ ] Pixel cold launch of Capsule home
- [ ] WAIKE actual learner content (demo login → track list → real lesson/activity)
- [ ] gunnchAI actual response **or** honest unavailable + truthful provenance
- [ ] One accepted-main rebuilt game launch
- [ ] Return-to-home / Capsule
- [ ] Privacy / no notification leakage
- [ ] Readable UI on Pixel

## Decision

- [ ] Overall: would I hand this to a recruiter / faculty member as RC1?

## Authorization (owner only)

- [ ] Authorize merge of portal PR #39 to `main` (creates post-merge accepted-main SHA)
- [ ] Authorize draft GitHub prereleases (`v1.0.0-rc.1`) with attached validated assets
- [ ] Flip `RC1_OWNER_APPROVAL=true` only after the above
- [ ] Do **not** flip `V1_0_0_RELEASE_AUTHORIZED` until final `v1.0.0` acceptance

## Pointers

- Gates: `releases/v1.0.0-rc.1/V1_RC1_GATES.json`
- Pixel acceptance: `releases/v1.0.0-rc.1/pixel/PIXEL_RC1_DEMO_ACCEPTANCE.json`
- Draft release commands: `releases/v1.0.0-rc.1/DRAFT_RELEASE_COMMANDS.md`
- Attachment plan: `releases/v1.0.0-rc.1/RELEASE_ATTACHMENT_PLAN.json`
- Hash verification: `releases/v1.0.0-rc.1/RELEASE_HASH_VERIFICATION.json`
- Demo bootstrap: `releases/v1.0.0-rc.1/demo/start_demo_services.sh`
