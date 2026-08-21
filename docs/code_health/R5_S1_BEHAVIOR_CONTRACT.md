# R5-S1 behavior contract — gunnchos-research-portal

## Symbol
`scripts/audit_portfolio.py` → `main()` (CLI entry) and helpers `load_roles`, `audit_repo`, `uml_status`, `compute_gates`.

## Callers
- CI: `python3 scripts/audit_portfolio.py --portal-root . --no-write --allow-missing-siblings`
- Make: `make audit` / `make verify`
- Local regeneration of `portfolio/supervisor_ready_manifest.yaml` and the PhD dashboard

## Inputs
- `--portal-root`: portal checkout containing `portfolio/repo_roles.json` (or `.yaml`)
- `--repos-root` / `PORTFOLIO_REPOS_ROOT`: sibling spine root (default: parent of portal)
- `--no-write`: do not write manifest/dashboard artifacts
- `--allow-missing-siblings`: isolated portal CI mode when spine checkouts are absent

## Expected outputs / exit semantics
- Loads curated roles; audits each in-scope checkout that exists.
- Prints gate lines including `AUTOMATABLE_SUPERVISOR_READY=...` and `repos_audited=N missing=[...]`.
- Exit `0` when:
  - all in-scope siblings exist, or
  - siblings are missing **and** `--allow-missing-siblings` is set (missing list is still recorded; automatable gate forced FAIL).
- Exit `1` when siblings are missing and `--allow-missing-siblings` is **not** set.
- Missing `portfolio/repo_roles.json` (and no YAML fallback) → `SystemExit` / hard failure.

## Failure conditions
- Missing role catalog
- Incomplete spine without allow-missing flag (non-zero exit)
- Invalid/absent portal root content required by helpers under test

## Why the audited mutation matters
Audit mutation `flip_return_zero` rewrites the first `return 0` (the `--allow-missing-siblings` success path) to `return 1`.
If the suite never exercises that exit path (historically `make test` only ran `validate_supervisor_ready.py`), a broken CI exit contract survives.

## Coverage gap closed by R5-S1
Canonical tests call `main()` / CLI for valid portfolio, missing catalog, missing-siblings exit codes, and subprocess CLI — then a disposable mutation harness confirms `flip_return_zero` fails the suite.
