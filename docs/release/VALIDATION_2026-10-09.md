# Reconciliation validation

- `python3 scripts/validate_v1_release_ledger.py`: PASS — 108 retained/expanded feature rows, 38 gates, 43 exact-base implementation tickets; acyclic dependencies, preserved evidence hashes, full-scope overrides and owner/release firewalls verified.
- `make test` using an isolated temporary pytest environment: PASS — supervisor control-plane validator and seven portfolio tests.
- `git diff --check`: PASS.
- Read-only portfolio audit: `AUTOMATABLE_SUPERVISOR_READY=FAIL`, `CONTACT_SUPERVISOR_READY=BLOCKED`, 16 repositories present. This remains a separate diagnostic; the reconciliation does not rewrite it as ready.

System and bundled Python lacked pytest. Tests were run with pytest installed only in a temporary virtual environment; no product dependency files changed.

GitHub evidence was read at accepted main and named checkpoints. All 77 WAIKE PR-head check results were retrieved; site/Pursuit/Anime-checkpoint/Passport check scopes are recorded separately. Public game manifests were read and saved; this did not replay gameplay. Website and WAIKE deployment reports retain their original dates and scopes. No product tests, human sessions, physical installs, merges, deployments, tags or release publications were performed by this reconciliation.

The ledger validator is wired into portal CI. A green control-plane check never grants product completion, human acceptance or release authorization.
