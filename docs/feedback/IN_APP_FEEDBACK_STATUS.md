# In-app Feedback status

| Class | Meaning | RC1 | Final v1.0.0 |
|---|---|---|---|
| `RC1_DESIRED` | Capsule / WAIKE / games expose Feedback → portal | Not required if front door works | Superseded by V1_REQUIRED |
| `V1_REQUIRED` | Stable in-product entry points | Tracked | **Required** (or owner waiver) |

## Canonical in-app target

All product deep-links MUST use accepted-main placeholder URL (never freeze-branch):

`https://github.com/gunnchOS3k/gunnchos-research-portal/blob/main/FEEDBACK.md`

Optional query markers (public only): `?component=Device%20OS` (no secrets).

## Surfaces

| Product | Entry | Status this pass |
|---|---|---|
| Device OS Capsule | Settings → About | Draft PR prepared locally |
| WAIKE | Help/footer + role-aware routes | Draft PR prepared locally |
| gunnchAI | Hub / assist feedback links | Draft PR prepared locally |
| Anime Aggressors | Settings + Results | Draft PR prepared locally |
| Pedestrian Pursuit | Settings/About/Results | Draft PR prepared locally |
| Archive of Life | Settings | Draft PR prepared locally |
| BeatLink Party | Host + Player help | Draft PR prepared locally |

RC1 may ship without every in-app gate. Final `v1.0.0` may not.
