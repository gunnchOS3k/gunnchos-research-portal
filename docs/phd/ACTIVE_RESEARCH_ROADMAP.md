# Active research roadmap

Working title remains: *Resilience-Aware Service Continuity in Heterogeneous 6G Networks: Cross-Layer Orchestration for Resource-Constrained Devices*.

No University of Oulu affiliation is claimed.

## Now (digital, automatable)

- Keep 16 draft PRs mergeable; do not merge to `main`.
- RQ1 synthetic profiles + twin experiment `rq1_gary_flagship_profiles`.
- RQ2 rule-based SpectrumX path + ReadyGary `SYNTHETIC_SIM` beam tables (28 GHz = FR2 mmWave).
- RQ3 seeded NTN policies; NTN is not always better.
- Hardware digital packet + `DIGITAL_TO_PHYSICAL_HANDOFF.md`; ERC/DRC 0 errors with warnings.
- Supervisor snapshot via `make supervisor-snapshot`.

## Next (requires owner / lab / independent human)

| Item | Gate |
|---|---|
| Independent reproduction of RQ1–RQ3 digital packets | `INDEPENDENT_REPRODUCTION_PENDING` |
| Pixel 6a human playtest (fun/usability) | `HUMAN_QA_PENDING` (digital install+launch smoke already PASS) |
| EVT bring-up, measured rails, RF, thermal, battery | `PHYSICAL_PENDING` |
| COM-HPC / dock NDA pin maps | `EXTERNAL_PENDING` |
| GPU NR CUDA / Nsight timings | `BLOCKED_GPU` |
| Human playtests (games) | `HUMAN_QA_PENDING` — not dissertation papers |
| Venue CFP verification + owner submission | never auto-`SUBMITTED` |

## Not current scope

- Extra dissertation papers for games / WAIKE / gunnchAI.
- Claiming standardized commercial 6G or IMT-2030 compliance.
- Inferring NTN from RM520N-GL SKU.
- Inventing electrical values to close ERC warnings.
