# Canonical feedback URLs

**Policy:** No feature-branch URLs in final `v1.0.0` product binaries or published release notes.

| Constant | Value | Status |
|---|---|---|
| `FEEDBACK_HUB_ACCEPTED_MAIN` | `https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md` | **Placeholder until portal #39 merges to accepted main** — then live |
| `SECURITY_MD_ACCEPTED_MAIN` | `https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/SECURITY.md` | Same |
| `SECURITY_ADVISORY_NEW` | `https://github.com/gunnchOS3k/gunnchos-research-portal/security/advisories/new` | Live if private vulnerability reporting is enabled on the repo |
| `FEEDBACK_HUB_INTERIM_PR39` | `https://github.com/gunnchOS3k/gunnchos-research-portal/blob/release/v1.0.0-rc1-ecosystem-freeze/FEEDBACK.md` | Owner-preview / RC1 freeze only — **must not** remain in final V1 product links |

After #39 lands, optionally pin release notes to tag URLs:

- `https://github.com/gunnchOS3k/gunnchos-research-portal/blob/v1.0.0-rc.1/FEEDBACK.md`
- `https://github.com/gunnchOS3k/gunnchos-research-portal/blob/v1.0.0/FEEDBACK.md`
