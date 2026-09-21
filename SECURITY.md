# Security Policy — gunnchOS Ecosystem (portal)

## Supported versions

| Version | Supported |
|---------|-----------|
| `v1.0.0-rc.1` (when published) | Best effort during RC |
| `main` / freeze branches | Best effort |
| Final `v1.0.0` | Only after owner authorization |

## Reporting a vulnerability (private only)

**Do not open public GitHub issues for security vulnerabilities.**

1. Prefer [GitHub Private Security Advisories](https://github.com/gunnchOS3k/gunnchos-research-portal/security/advisories/new) on this repository.
2. If you cannot use advisories, contact the repository owner (Edmund Gunn Jr. / gunnchOS3k) through a private channel referenced in the org security settings.
3. Include: affected component, version/SHA, impact, reproduction **without** secrets or private datasets.

We will acknowledge privately and coordinate disclosure. Public issues that disclose exploitable details may be locked and converted to a private advisory.

## Scope

- No secrets, tokens, PII, or private competition / field datasets in issues or PRs.
- Privacy-preserving, opt-in telemetry only where a research repo explicitly documents it.
- Hardware artifacts in RC1 are **digital engineering** — not certified consumer products.

## Dependency / supply-chain notes

Device OS launcher tooling audits for RC1 live under:

`releases/v1.0.0-rc.1/security/device_os_launcher_mock/`
