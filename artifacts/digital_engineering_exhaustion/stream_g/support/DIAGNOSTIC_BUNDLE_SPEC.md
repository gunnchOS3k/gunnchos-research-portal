# Diagnostic bundle specification (digital prep)

**Status:** DIGITAL_PREPARATION · not human-validated support UX  
**Primary implementation:** `gunnchos-device-os` (`cx0/support_bundle.py`, `phase_xv/support_lifecycle`, Cont-IX self-service)

## Bundle contents (required fields)

| Artifact | Purpose | Redaction |
|----------|---------|-----------|
| `system_info.json` | OS version, device class, build SHA, locale | strip PII emails/tokens |
| `self_tests.json` | network/storage/update/ring/dock self-test results | no credentials |
| `journal_snippet.txt` | recent boot/update events | redact emails/tokens |
| `policy.json` | privacy/AI/offline policy snapshot | no secrets |
| `fault_codes.json` | active/recent fault codes | codes only |
| `MANIFEST.json` | bundle_id, created_at, sha256 of members | — |

## Collection path (product intent)

Settings → Support → Generate diagnostic bundle → share with school IT / manufacturer support.

## Claim boundary

Scaffold and digital schemas exist. Field-pilot exercise and human support-ops validation remain `HUMAN_VALIDATION_REQUIRED`.
