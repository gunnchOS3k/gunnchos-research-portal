# In-app Feedback status (RC1)

| Class | Meaning | RC1 status |
|---|---|---|
| `RC1_DESIRED` | Capsule / WAIKE / games expose a Feedback link to the portal front door | **Not required to ship RC1** if public front door works |
| `V1_REQUIRED` | Stable in-product entry points before final `v1.0.0` | Tracked for post-RC1 / pre-v1.0.0 |

## Decision for this pass
Public front door (`FEEDBACK.md` + issue forms) is live on the portal freeze branch. No product-code draft PRs opened solely for in-app links in this pass — do not delay RC1.

## If adding in-app later
Open **narrow** draft PRs per surface (Device OS shell, WAIKE client, each game) linking to the portal FEEDBACK URL. Keep unrelated feature work out.
