# Application Readiness Checklist

## Portfolio spine (hardening pass 1)

- [ ] Merge [field-kit PR #1](https://github.com/gunnchOS3k/gunnchos-7gc-ai-ran-field-kit/pull/1)
- [ ] Merge [portal PR #4](https://github.com/gunnchOS3k/gunnchos-research-portal/pull/4) or role-proof supersede
- [ ] Fix CI on device-os #20, spectrumx #92, edge-io #17 before merge

## Role proof (pass 2)

- [ ] Merge or mark ready Agentic SecOps proof PR (`role-proof-agentic-secops`)
- [ ] Merge or mark ready Access Risk proof PR (`role-proof-access-risk-intelligence`)
- [ ] Merge or mark ready RTL verification proof PR (`role-proof-rtl-verification-lab`)
- [ ] Merge portal role landing PR (`role-proof-portfolio-landing-pages`)
- [ ] Merge profile README PR (`role-proof-profile-readme`)

## Public surfaces

- [ ] Update [gunnchOS3k](https://github.com/gunnchOS3k/gunnchOS3k) profile README (draft PR)
- [ ] Add demo screenshots to `demo/screenshots/` folders
- [ ] Add 2-minute walkthrough videos (optional)
- [ ] Tag releases per [DOI_AND_RELEASE_TRACKER.md](DOI_AND_RELEASE_TRACKER.md)
- [ ] Prepare Zenodo DOI for umbrella repo **after** evidence review
- [ ] Prepare role-specific resume bullets — [ROLE_SPECIFIC_RESUME_BULLETS.md](ROLE_SPECIFIC_RESUME_BULLETS.md)

## Safety

- [ ] Confirm no secrets in any role-proof branch
- [ ] Confirm mock-only security data
- [ ] Confirm claim boundary language on all landing pages
