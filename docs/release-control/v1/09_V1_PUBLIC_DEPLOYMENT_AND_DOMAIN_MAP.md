# v1.0.0 Public Deployment and Domain Map

## Service ownership

```text
Squarespace → domain registrar
Google Workspace → email / MX / SPF / DKIM
Cloudflare → Workers, previews, CDN/TLS, future DNS
GitHub → source, CI, release provenance
```

## Target surfaces

| Hostname | Product | v1 |
|---|---|---|
| `gunnchos.com` | ecosystem front door | Required |
| `mlv.gunnchos.com` | 3k MLV | Required |
| `campus.gunnchos.com` | WAIKE / Campus | Required |
| `anime.gunnchos.com` | Anime Aggressors | Required |
| `pursuit.gunnchos.com` | Pedestrian Pursuit | Required |
| `archive.gunnchos.com` | Archive of Life | Required |
| `beatlink.gunnchos.com` | BeatLink Party | Required |
| `research.gunnchos.com` | Research / 7GC | Required |
| `ai.gunnchos.com` | gunnchAI | Optional |
| `devices.gunnchos.com` | Device/Hardware | Optional |
| `docs.gunnchos.com` | Documentation | Optional |

## Production rules
Every hosted product must have:
- pinned source SHA
- preview before production
- deployment identity
- deep-link routing
- mobile smoke
- 404/fallback behavior
- feedback path
- valid TLS
- no embedded secret
- documented public build variables

## DNS migration rule
Do not change authoritative nameservers until:
1. Squarespace DNS is inventoried;
2. Google Workspace records are copied;
3. records are reviewed;
4. rollback is documented.
