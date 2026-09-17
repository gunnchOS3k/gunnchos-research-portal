# Complete Experience Platform Contracts v1

Additive JSON Schema-style contracts. Presence ≠ implementation ≠ certification.

Files:
- `UserProfile_v1.json`
- `IdentitySession_v1.json`
- `FileProvider_v1.json`
- `SyncProvider_v1.json`
- `BackupProvider_v1.json`
- `AppPackage_v1.json`
- `AppProvider_v1.json`
- `PermissionGrant_v1.json`
- `AccessibilityCapability_v1.json`
- `PeripheralCapability_v1.json`
- `ContinuityState_v1.json`
- `CredentialRecord_v1.json`
- `CreatorProject_v1.json`
- `RemoteExecutionProvider_v1.json`
- `SupportBundle_v1.json`

Consumers must version bumps additively (v2+) and never remove intended fields without deprecation windows.
