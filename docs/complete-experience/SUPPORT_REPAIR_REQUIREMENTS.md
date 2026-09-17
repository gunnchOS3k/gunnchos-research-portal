# Support / Repair / Ownership Requirements

## Normative

- SupportBundle v1 with mandatory redaction.  
- User can export diagnostics without root shell expertise.  
- Ownership transfer / warranty / repair status must be representable.  
- Self-service recovery journeys for backup restore and factory-safe reset.

## Current state

`export_diagnostic_bundle` + `redact_text` digital — PARTIAL. Product UX and ownership transfer ABSENT.

## Gaps (P0)

1. SupportBundle schema adoption + UI  
2. Redaction coverage tests for PII classes  
3. Ownership/repair record model  
