# Feedback triage

**Owner:** Edmund Gunn Jr. / release operators  
**Scope:** Public issues filed against `gunnchos-research-portal` (and forwarded component issues)

## Labels

| Label | Use |
|---|---|
| `needs-triage` | New inbound |
| `feedback:bug` / `feature` / `experience` / `research` / `hardware` / `accessibility` / `documentation` | Kind |
| `lane:core` / `lane:hardware` / `lane:research` / `lane:experiences` / `lane:portal` | Routing |
| `priority:p0` … `p3` | Severity / urgency |
| `security` | **Never** on public vulns — use private advisories only |
| `roadmap:candidate` | Accepted for roadmap consideration |
| `release:rc1` / `release:v1` / `release:later` | Target window |

## SLA (best effort for RC1)

| Class | First response target |
|---|---|
| Accessibility blocker / data-loss bug | 2 business days |
| Other bugs | 5 business days |
| Features / research commentary | Weekly batch |
| Security (private advisory) | Acknowledge ASAP; no public disclosure |

## Routing

1. Confirm not a security disclosure in a public issue → convert to private advisory + close public with pointer.
2. Assign lane + component repo if known.
3. For research ethics / dataset concerns → `ethics_privacy_review` style handling; quarantine attachments.
4. Hardware feedback stays inside **digital engineering** claim boundary (no accidental EVT/fab promises).

## Outcomes

- `roadmap:candidate` → appears on [ROADMAP.md](../../ROADMAP.md)
- Fix in component → link PR; note in [CHANGELOG.md](../../CHANGELOG.md) when released
- Duplicate → close with pointer
- Out of scope / experimental → label `release:later` with short rationale
