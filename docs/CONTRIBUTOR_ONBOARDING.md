# Contributor Onboarding

Welcome to the gunnchOS3k portfolio. Builders are expected to **surpass the founder** through evidence-backed contributions.

## 1. Read mission + safe language

- [MISSION_ALIGNMENT.md](../MISSION_ALIGNMENT.md)
- [CLAIMS_TO_EVIDENCE.md](../CLAIMS_TO_EVIDENCE.md)
- [docs/EVIDENCE_STANDARD.md](EVIDENCE_STANDARD.md)

**Use:** research prototype, IMT-2030-aligned, phone-first field console, digital-equity deployment pathway.

**Do not claim:** commercial 6G, carrier-grade, certified hardware, finished console, citywide impact.

## 2. Pick a spine

| Interest | Start repo |
|----------|------------|
| Wireless research | [gunnchos-7gc-ai-ran-field-kit](https://github.com/gunnchOS3k/gunnchos-7gc-ai-ran-field-kit) |
| Console software | [gunnchos-device-os](https://github.com/gunnchOS3k/gunnchos-device-os) or [scaly-wings](https://github.com/gunnchOS3k/scaly-wings) |
| Education / tutoring | [waike-research-ops](https://github.com/gunnchOS3k/waike-research-ops) |
| Portal / docs | this repo |

## 3. Local setup

```bash
git clone https://github.com/gunnchOS3k/<repo>.git
cd <repo>
# Follow REPRODUCIBILITY.md
python3 scripts/check_required_files.py
```

## 4. Branch + draft PR

- Branch: `feature/short-description` or coordinated `portfolio-spine-hardening`
- Open **draft** PR until Edmund reviews
- Use PR template from portfolio hardening pass

## 5. Youth + privacy

- No minors without guardian/program approval
- No private payload traffic; no unauthorized RF transmission
- See `docs/PRIVACY_AND_YOUTH_SAFETY.md` in education repos

## 6. Teaching pathway

Instructors: [waike INSTRUCTOR_GUIDE](https://github.com/gunnchOS3k/waike-research-ops/blob/main/docs/INSTRUCTOR_GUIDE.md)

Learners: [waike LEARNER_PATHWAY](https://github.com/gunnchOS3k/waike-research-ops/blob/main/docs/LEARNER_PATHWAY.md)
