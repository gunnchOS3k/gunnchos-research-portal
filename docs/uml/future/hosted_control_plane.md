# Future — hosted control plane

Not implemented.

```mermaid
flowchart LR
  GH[GitHub source of truth] --> SITE[Optional static site]
  SITE --> DASH[Live gate dashboard]
  PRIV[Private repo mirrors] --> ACL[Supervisor-only ACL]
```

Would require owner hosting, identity, and visibility decisions. Must not be drawn as current.
