# Repository visibility packet

**Status:** `EXTERNAL_PENDING`

## Why blocked

These GitHub repositories are **private** (org listing 2026-08-18):

- `gunnchOS3k/gunnchos-gpu-nr-baseband-platform`  
- `gunnchOS3k/gunnchos-emergent-service-intent-protocols`  

This agent must not change visibility.

## Prerequisite

Owner decides public vs collaborator access vs GitHub release of a sanitized snapshot.

## Owner action (examples — you run them)

```bash
# inspect only
gh repo view gunnchOS3k/gunnchos-gpu-nr-baseband-platform --json isPrivate,visibility
gh repo view gunnchOS3k/gunnchos-emergent-service-intent-protocols --json isPrivate,visibility
```

If a supervisor must see them: add collaborator **or** publish after secret scan. Do not send 404 links.

## Expected evidence

Public URL or confirmed collaborator access recorded in the portal dashboard (owner edit).

## Status transition

Public or confirmed shared access → drop `repository_visibility_owner_action` for that repo. Secret scan must be clean first.
