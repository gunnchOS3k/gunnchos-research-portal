# v1 Requirement Traceability Matrix

| Requirement | Primary repo(s) | Acceptance | Final evidence |
|---|---|---|---|
| Home/Campus/Gallery | `3k-mlv` | hosted journey + owner UX | deployment manifest + smoke |
| Host shell | `3k-mlv`, `device-os` | host matrix + CI | supported-host matrix |
| WAIKE LMS | WAIKE | build/offline/assessment + human | WAIKE final gate report |
| Curriculum | `waike-research-ops` | authored-content audit | readiness matrix |
| gunnchAI | `gunnchAI3k` | digital + human | human-eval + provider status |
| Device OS | `gunnchos-device-os` | exact build + lifecycle | build manifest + device/host evidence |
| Anime | `anime-aggressors` | CI + G7 + G6/G8/G9 | animectl + owner packet |
| Pedestrian | `pedestrian-pursuit` | exact-head + 8-course review | Pixel/owner packet |
| Archive | Archive repo | engineering + boundary | ingestion gate + limitation |
| BeatLink | BeatLink repo | multi-client + rights-safe | party packet + rights manifest |
| Hardware digital | hardware repo | digital evidence only | hardware digital manifest |
| Edge I/O | edge-io repo | synthetic/privacy | measurement/privacy packet |
| 7GC research | research repos | simulation/digital | research release matrix |
| Public hosting | Cloudflare + repos | preview/prod/domain smoke | public deployment manifest |
| Security/privacy | ecosystem | scans + config | security summary |
| Accessibility | ecosystem | automation + human boundary | a11y summary/checklist |
| Feedback | portal/components | live links | feedback traceability |
| Rights/provenance | ecosystem | inventory + owner review | rights manifest |
| Final release | portal control plane | fresh freeze + owner auth | final manifest + tags |

## Rule
Every `IN_V1_REQUIRED` row in the scope ledger must map to:
1. a repo/system;
2. an acceptance gate;
3. canonical evidence;
4. a final disposition.
