# ECOSYSTEM_ACCEPTED_MAIN_REGISTRY

> **17G.7 current-state (live):** Device OS accepted-main = `1c20c264d27bc8daf3a7d5b3280256f871ae1a06` (PR #155 merge; PR head `d20fe17422f1092b240ec5ecf985c71d9bc14e3f` is NOT accepted main). Portal #14 = `7ad4ce84ab61037d140f2185de14b191ecf7ec28`. WAIKE #17 = `7ccb64459df088d41655af51c959a7bbbac849a3`. gunnchAI = `65b799e21dc1c4979d52b9c8b328f7aa47059bde`. Pin/freeze = `271e52938b19f66d79a652d050a8be039cf942bd67ced3cc8cd16babd1db27ea` / `9115f7b60ea2e362e6399cfcdfefe21fd28ed53cc2a4ebdd2f448aecba65258c`. Digital accepted-main candidate PASS. Next owner action: `MERGE_PORTAL_15_WITH_MERGE_COMMIT`. Human/physical/CX remain pending. Historical Prompt 18 discovery body retained below.

Generated current overlay: `2026-09-18T01:41:55Z`  
Prompt: **17G.7** — #155 Accepted-Main Rebind + Portal #15 Final Release-Control Sync  
Machine-readable: [`ECOSYSTEM_ACCEPTED_MAIN_REGISTRY.json`](./ECOSYSTEM_ACCEPTED_MAIN_REGISTRY.json) (`current_state_17g7`)

---

## Historical Prompt 18 discovery snapshot (retained)

Generated: `2026-09-15T05:17:53Z`  
Prompt: **18** — gunnchOS3k Ecosystem Release Control Tower  
Org: `gunnchOS3k`  
Control plane: `gunnchos-research-portal`  
Machine-readable: [`ECOSYSTEM_ACCEPTED_MAIN_REGISTRY.json`](./ECOSYSTEM_ACCEPTED_MAIN_REGISTRY.json)

## Discovery notes
- Built from **local workspace remotes** + per-repo `gh pr list` + existing `REPO_CATALOG.yaml` / `release/` pins.
- `gh` org-wide repo list returned **404/Forbidden** this session initially; follow-up per-repo `gh` confirmed additional GH-only assets (notably books).
- Native learning platform repo: **`gunnchos-waike-learning-platform`**.
- Books guidebook: **`gunnchos-technology-landscape`** (GH-only).

## Device Lab pin firewall
- Manifest: `release/DEVICE_LAB_CURRENT_PIN_MANIFEST.json`
- Master: `release/DEVICE_LAB_CURRENT_PIN_MASTER.json` (as of 2026-09-10): `FOUR_GAME_REAL_RUNTIME_DEVICE_LAB_PASS=false`
- Prompt 18 **does not** edit Four-Game / Device Lab current-pin runtime paths (Prompt 17F separation).
- Portal draft **#15** is Prompt 18 control-tower docs only — not a Device Lab pin rewrite of freeze PR **#14**.

## Registry

| Repo | Purpose | origin/main | Open PRs | Evidence class | Pinned | Product area |
| --- | --- | --- | --- | --- | --- | --- |
| `gunnchos-research-portal` | Canonical ecosystem IA + release control plane | `eef765bdb615` | 0 | DRAFT_DIGITAL_CANDIDATE | yes | Research/7GC control |
| `gunnchos-7gc-ai-ran-field-kit` | Program charter + evidence aggregation | `9e93e41a3b16` | 0 | ACCEPTED_MAIN_DIGITAL_PASS | yes | Research/7GC |
| `gunnchos-device-os` | gunnchOS + Device Lab + middleware host | `898e44cfa8b7` | 0 | DIGITAL_BLOCKED | yes | OS/middleware |
| `gunnchos-hardware-industrial-design` | Device Quartet industrial/electrical SoT | `9ee0ef2f688b` | 0 | PHYSICAL_VALIDATION_PENDING | yes | Hardware |
| `edge-io-measurement-node` | Ring sensing/measurement + privacy export | `af57fbdac857` | 0 | PHYSICAL_VALIDATION_PENDING | yes | Edge IO/Rings |
| `gunnchAI3k` | Local-first AI tutor / assist | `65b799e21dc1` | 0 | HUMAN_VALIDATION_PENDING | yes | AI |
| `waike-research-ops` | WAIKE curriculum/research ops | `fbf7685bc568` | 0 | HUMAN_VALIDATION_PENDING | yes | WAIKE curriculum |
| `gunnchos-waike-learning-platform` | Native WAIKE learning platform | `8610018a62e0` | 0 | HUMAN_VALIDATION_PENDING | yes | Native learning platform |
| `anime-aggressors` | Anime Aggressors game | `258cc0c45991` | 0 | PHYSICAL_VALIDATION_PENDING | yes | Games |
| `pedestrian-pursuit` | Pedestrian Pursuit game | `ba698e929b57` | 0 | HUMAN_VALIDATION_PENDING | yes | Games |
| `archive-of-life-artifact-world` | Archive of Life game | `8611d2e30315` | 0 | HUMAN_VALIDATION_PENDING | yes | Games |
| `beatlink-party` | BeatLink Party game | `06b4a6f74159` | 0 | RIGHTS_PENDING | yes | Games |
| `7gc-digital-twin` | 7GC campus digital twin research | `dc43a567e3f2` | 0 | ACCEPTED_MAIN_DIGITAL_PASS | no | Research/7GC |
| `spectrumx-ai-ran-gary` | AI-RAN equitable spectrum research | `9060655e7243` | 0 | ACCEPTED_MAIN_DIGITAL_PASS | no | Research/7GC |
| `readygary-6g-beam-selection` | 6G beam selection research | `569875224db7` | 0 | ACCEPTED_MAIN_DIGITAL_PASS | no | Research/7GC |
| `ntn-resilience-sim` | NTN resilience simulation | `c4215fc1039f` | 0 | ACCEPTED_MAIN_DIGITAL_PASS | no | Research/7GC |
| `gunnchos-gpu-nr-baseband-platform` | GPU NR baseband research platform | `3931f51d43b7` | 0 | DRAFT_DIGITAL_CANDIDATE | no | Research/7GC |
| `gunnchos-emergent-service-intent-protocols` | Emergent service-intent protocol research | `088c5e88e155` | 0 | DRAFT_DIGITAL_CANDIDATE | no | Middleware/research |
| `oulu-6g-security-trust-privacy-lab` | 6G security/trust/privacy lab (Oulu) | `d276579333a8` | 0 | DRAFT_DIGITAL_CANDIDATE | no | Security/privacy research |
| `oulu-wce-readiness-dashboard` | WCE readiness dashboard | `eb09ebeb955f` | 0 | DRAFT_DIGITAL_CANDIDATE | no | Research tooling |
| `oulu-open-ran-testbed-lab` | Open RAN testbed lab | `c86f3e497506` | 0 | DRAFT_DIGITAL_CANDIDATE | no | Research/7GC |
| `gunnchos-technology-landscape` | Accessible systems guidebook + reader-preview (Technology Landscape) | `8d56d214fa64` | 0 | HUMAN_VALIDATION_PENDING | no | Books/publications |

## Books discovery
- Dedicated guidebook / reader-preview repo: **`gunnchos-technology-landscape`** @ `8d56d214fa64` (https://github.com/gunnchOS3k/gunnchos-technology-landscape)
- Local checkout: **False**
- Evidence class: `HUMAN_VALIDATION_PENDING`
- CI: main ci + reader-preview success @ 8d56d214 (human-validation launch prep #10 merged)
- Related only (not this SKU): PhD `docs/phd/PUBLICATION_PIPELINE.md`
- Prompt 18 initial pass marked books NOT_APPLICABLE (not in local workspace). Follow-up discovery confirmed GH-only repo gunnchos-technology-landscape.

## Non-claims
- Never equate simulation with physical PASS.
- Never print `FULL_ECOSYSTEM_COMPLETE=true` from this registry alone.
