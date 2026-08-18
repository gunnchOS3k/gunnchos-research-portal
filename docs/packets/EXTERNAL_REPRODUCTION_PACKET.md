# External / independent reproduction packet

**Status:** `INDEPENDENT_REPRODUCTION_PENDING`

Cursor cannot sign this on another person’s behalf.

## Why blocked

No returned evidence record from an independent researcher exists in the audited trees.

## Prerequisite

A person who is not Edmund, with a clean machine, reproduces a **frozen commit** of each core RQ repo.

## Command (core pattern)

```bash
git clone <url>
git checkout <frozen-sha>
# then that repo's canonical reproduce command
```

## Expected evidence form

```text
system:
commit:
command:
start:
end:
result:
output_hashes:
deviations:
PASS_FAIL:
notes:
```

Store as `artifacts/independent_reproduction/<person-or-lab-id>.md` in the repo (no PII beyond what the reproducer consents to).

## Status transition

At least one independent PASS on each of the six core RQ repos → `INDEPENDENT_REPRODUCTION` may move from PENDING. Still not `FIELD_VALIDATED`.
