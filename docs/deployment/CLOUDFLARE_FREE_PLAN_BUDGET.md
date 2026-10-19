# Cloudflare Free plan budget

Queried from the public limits page on 2026-09-30: https://developers.cloudflare.com/workers/platform/limits/ (page updated 2026-09-05).

The live account plan and usage were **not** queried. `wrangler whoami` is unauthenticated, and the Cloudflare plugin MCP is not installed. Do not treat the table below as proof this account is on Free, and do not treat it as a promise of zero cost forever.

| Limit | Workers Free (published) |
|---|---|
| Requests | 100,000 / day |
| CPU time | 10 ms / request |
| Workers | 100 |
| Static asset files / version | 20,000 |
| Individual asset size | 25 MiB |
| Worker size | 64 MiB uncompressed |
| Memory | 128 MB |

Rules followed this session:

- No paid Workers upgrade.
- No paid subscription enabled.
- Static pages are preferred. The gateway `next build` prerenders the public routes. Dynamic routes are `/api/health` and `/api/vitals` only.
- A Next.js server render that spends more than 10 ms of CPU will not fit the published Free CPU limit. Measure that before production.
- Supabase, model providers, and multiplayer backends are separate quotas.

Account usage remains unknown until the owner runs `wrangler login` or `/add-plugin cloudflare`.
