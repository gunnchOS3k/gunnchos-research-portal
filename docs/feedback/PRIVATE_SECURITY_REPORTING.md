# Private security reporting verification

**Do not post exploitable security details publicly.** Guide: [SECURITY.md](../../SECURITY.md) · Form: https://github.com/gunnchOS3k/gunnchos-research-portal/security/advisories/new

## Verification checklist (before final v1.0.0)

| Check | Result |
|---|---|
| SECURITY.md documents private path | PASS (documented) |
| Issue config routes security privately | PASS (contact_links) |
| Live advisory form reachable for reporters | **UNVERIFIED this pass** — `gh` auth token invalid (`PRIVATE_SECURITY_REPORTING_SETUP_REQUIRED` until owner verifies) |

## If private reporting is not enabled

Set gate:

```text
PRIVATE_SECURITY_REPORTING_SETUP_REQUIRED=true
SECURITY_PRIVATE_PATH_VERIFIED=false
```

Do **not** claim operational private reporting. Owner enablement:

1. Repo → Settings → Security → Code security → enable Private vulnerability reporting
2. Confirm `https://github.com/gunnchOS3k/gunnchos-research-portal/security/advisories/new` loads for an unprivileged test account
3. Flip `SECURITY_PRIVATE_PATH_VERIFIED=true` in final V1 gates
