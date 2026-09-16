# Offline / Low-Bandwidth Requirements

## Normative

- Core learning, docs viewing, media already-on-device, and identity session resume must work offline.  
- Sync conflicts must be explainable; no silent data loss.  
- Community hub mode: local content distribution without cloud dependency.  
- Low-bandwidth: adaptive sync, deferred media, text-first fallbacks.

## Current state

OfflineSyncEngine / offline_mode_manager / network_decision — **PARTIAL**. WAIKE offline reconnect GUI skipped on Device Lab guest.

## Gaps (P0)

1. Product Files offline UX  
2. WAIKE offline reconnect earned on Device Lab (coordinate; do not hijack #134)  
3. Community hub profile implementation  
