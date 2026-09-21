# Feedback — gunnchOS Ecosystem

**Canonical public front door** for the entire ecosystem. Do not fork competing feedback systems.

**Do not post exploitable security details publicly.** Use the private path in [SECURITY.md](SECURITY.md).

## Canonical URLs (V1)

| Role | URL |
|---|---|
| **Accepted-main / final V1 target** | `https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md` |
| Security guide (accepted-main target) | `https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/SECURITY.md` |
| Private advisory form | https://github.com/gunnchOS3k/gunnchos-research-portal/security/advisories/new |

**URL strategy until portal PR #39 lands:** product code and final V1 docs must reference the **accepted-main** URLs above (placeholder until merge). Interim owner-preview only: `https://github.com/gunnchOS3k/gunnchos-research-portal/blob/release/v1.0.0-rc1-ecosystem-freeze/FEEDBACK.md`. **Feature-branch URLs must not remain in final `v1.0.0` product links.** After #39 merges (and optionally after `v1.0.0-rc.1` / `v1.0.0` tags), prefer tag URLs when publishing release notes.

Relative issue-form links below resolve on GitHub; from a clone, use **Issues → New issue**.

## Quick links

| Kind | Open |
|---|---|
| Bug | [Bug report](../../issues/new?template=bug.yml) |
| Feature | [Feature request](../../issues/new?template=feature.yml) |
| Experience / games | [Experience feedback](../../issues/new?template=experience.yml) |
| Research | [Research feedback](../../issues/new?template=research.yml) |
| Hardware (digital eng.) | [Hardware feedback](../../issues/new?template=hardware.yml) |
| Accessibility | [Accessibility](../../issues/new?template=accessibility.yml) |
| Documentation | [Documentation](../../issues/new?template=documentation.yml) |
| Security (private) | [Security advisory](https://github.com/gunnchOS3k/gunnchos-research-portal/security/advisories/new) |

## What to include

- Component or lane (Portal, Device OS, WAIKE, gunnchAI, Hardware, Research, Experiences / game name)
- Public version / tag / commit SHA when known (`v1.0.0-rc.1`, Pixel, browser) — **no secrets**
- Steps, expected vs actual (bugs)
- Optional: assistive tech used (accessibility) — disability/medical disclosure is **optional**; describe the barrier without medical information

## What never to include in issues or deep-link query params

- Android serial, IP/MAC, account IDs, emails, auth tokens
- Local filesystem paths, private network details, personal logs with PII
- Exploitable vulnerability details (use private advisory)

Automated feedback deep-links may include **only**: component name, public version/tag, public commit SHA. Redact logs before attaching.

## How feedback becomes releases

1. Triage — [docs/feedback/FEEDBACK_TRIAGE.md](docs/feedback/FEEDBACK_TRIAGE.md)
2. Taxonomy / labels — [docs/feedback/FEEDBACK_TAXONOMY.md](docs/feedback/FEEDBACK_TAXONOMY.md)
3. Roadmap intake — [ROADMAP.md](ROADMAP.md)
4. Release candidacy — [docs/feedback/FEEDBACK_TO_RELEASE.md](docs/feedback/FEEDBACK_TO_RELEASE.md)
5. Changelog — [CHANGELOG.md](CHANGELOG.md) (credit contributors when appropriate; never expose private security reporter identity without consent)

## Component repos

File portal issues for cross-cutting / unsure routing. Component repos may keep specialized local templates; always prefer this portal for first public contact.

Surface matrix: [docs/feedback/PUBLIC_FEEDBACK_SURFACE_MATRIX.md](docs/feedback/PUBLIC_FEEDBACK_SURFACE_MATRIX.md)

## In-app feedback

| Class | Meaning |
|---|---|
| `RC1_DESIRED` | In-product Feedback links — **not** required to ship RC1 if this front door works |
| `V1_REQUIRED` | Stable in-product entry points **required** before final `v1.0.0` (or owner waiver) |

Status: [docs/feedback/IN_APP_FEEDBACK_STATUS.md](docs/feedback/IN_APP_FEEDBACK_STATUS.md)

## Accessibility

Public accessibility form stays easy to find. This is **not** a claim of formal accessibility certification.

## Optional Discussions

Issues remain the guaranteed V1 mechanism. See [docs/feedback/GITHUB_DISCUSSIONS_STATUS.md](docs/feedback/GITHUB_DISCUSSIONS_STATUS.md).