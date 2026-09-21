# Feedback → release

How public feedback becomes RC patches and eventually `v1.0.0`.

## Pipeline

```text
Public issue / private advisory
        │
        ▼
   Triage (labels, lane)
        │
        ├─ Security → private advisory workflow → coordinated disclosure
        │
        ├─ RC1 hotfix candidate → component PR → RC1 notes / changelog
        │
        ├─ v1.0.0 candidate → ROADMAP Now/Next → CHANGELOG Unreleased
        │
        └─ Later / experimental → ROADMAP Later (no false readiness claims)
```

## RC1 rules

- Do **not** merge unrelated feature work into the RC1 freeze solely because an issue exists.
- Prefer honest limitations in `KNOWN_LIMITATIONS.md` over silent scope creep.
- Production-reachable security blockers must close before final `v1.0.0` (see Device OS `artifacts/security/v1_rc1/`).

## Evidence expected for “fixed in release”

| Change type | Minimum evidence |
|---|---|
| Docs-only | PR link + path list |
| Software fix | PR + tests / smoke note |
| Capsule / Pixel path | Note whether Pixel re-demo required |
| Dependency CVE | Classification disposition + audit JSON |

## Changelog discipline

- User-visible changes → `[Unreleased]` in root `CHANGELOG.md`
- Promote to version section only when a release tag is authorized
- Never claim final `v1.0.0` until `V1_0_0_RELEASE_AUTHORIZED=true`
