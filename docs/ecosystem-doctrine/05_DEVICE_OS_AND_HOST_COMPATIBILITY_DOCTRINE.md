# Device OS and Host Compatibility Doctrine

## Role

gunnchOS Device OS is the deepest first-party host and service layer.

3k MLV should not be trapped inside it.

## Canonical stack

```text
3k MLV
→ Host Capability Adapter
→ Host OS
→ Hardware
```

## First-party path

gunnchOS should offer:
- deepest system integration;
- consistent permissions;
- optimized lifecycle;
- device-aware features;
- offline/local behavior;
- update/recovery/security integration.

## Third-party path

Windows, Linux, Android, macOS, and future hosts may participate through validated adapters.

## Compatibility language

Use:
- validated;
- supported;
- partially supported;
- experimental;
- not yet validated.

Never use “any OS” without evidence.

## Continuity requirements
- identity should carry;
- app state should carry where designed;
- input models should adapt;
- learning should remain available;
- games should preserve core quality;
- unsupported capabilities should fail honestly.

## Current state
Android Capsule, host adapters, continuity, security/update work exist.

## Future state
A host-neutral world with best-in-class first-party depth and honest third-party support.
