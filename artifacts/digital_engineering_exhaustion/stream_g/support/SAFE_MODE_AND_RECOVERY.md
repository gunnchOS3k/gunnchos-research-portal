# Safe mode and recovery (digital prep)

## Safe mode

- Boot with minimal services: compositor fallback, Settings, Support, recovery helpers
- Disable third-party apps and experimental modules
- Preserve user data by default
- Collect diagnostic bundle automatically on entry

## Recovery image

- Signed recovery environment (schema in device-os release docs)
- Actions: rollback last update, factory reset (with data-preservation warning), reinstall OS package, export diagnostic bundle
- Interrupted upgrade → resume or rollback matrix (Stream A ownership for install matrices)

## Data preservation

| Action | User data | Credentials | Offline cache |
|--------|-----------|-------------|---------------|
| Safe mode | kept | kept | kept |
| Rollback update | kept | kept | may invalidate versioned cache |
| Factory reset | wiped after confirmation | wiped | wiped |
| RMA wipe | wiped per RMA schema | wiped | wiped |

## Claim boundary

Digital procedures and schemas only. Physical media sanitize and depot logistics remain `PHYSICAL_HARDWARE_REQUIRED` / `EXTERNAL_PARTY_REQUIRED`.
