# Repair trees (digital)

| Tree ID | First actions | Escalate when |
|---------|---------------|---------------|
| RT-BOOT | Safe mode → rollback → recovery image | Persistent after reinstall |
| RT-STORAGE | Free space → clear caches → expand | Hardware storage fail |
| RT-UPDATE | Retry → rollback → recovery | Provenance mismatch |
| RT-NETWORK | Offline continue → reconnect | Persistent after known-good AP |
| RT-THERMAL | Cool-down → policy check | Repeated under light load (physical) |
| RT-BATTERY | Power cycle → charge path check | Health below FRU threshold (physical) |
| RT-DISPLAY | Safe mode compositor | Panel/cable FRU |
| RT-RING | Software re-pair | Hardware Ring FRU |
| RT-DOCK | Reseat / PD reset | Dock FRU |
| RT-AI | Restart local runtime → fallback | Model package corrupt |
| RT-WAIKE | Flush outbox / export | Persistent sync corruption |
| RT-SECURITY | Recovery image only | Suspected compromise → manufacturer |

FRU mapping lives in hardware repo Stream G pack.
