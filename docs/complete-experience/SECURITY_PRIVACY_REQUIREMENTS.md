# Security / Privacy Requirements

## Normative

- PermissionGrant v1 for mic/camera/files/location/notifications.  
- Consent before outbound telemetry; redaction in SupportBundle.  
- Sandbox + portal for untrusted apps.  
- Guardian/school policies composable with user privacy.

## Current state

Privacy controller, permissions_manager, sandbox_executor — **PARTIAL** digital. Portal-mediated UX and production IdP/TPM ABSENT.

## Gaps (P0)

1. Portal permission UX  
2. PermissionGrant contract wiring  
3. SupportBundle redaction end-to-end product path  
