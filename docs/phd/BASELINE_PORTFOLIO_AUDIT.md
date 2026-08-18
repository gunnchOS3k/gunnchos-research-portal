# Baseline portfolio audit (read-only)

Audit date: 2026-08-18. Host: local spine checkouts under  
`/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos`.

This document records **failures as well as strengths**. It is the factual baseline before the supervisor-ready implementation pass. Live SHAs refresh via `make audit` into [PORTFOLIO_READINESS_DASHBOARD.md](PORTFOLIO_READINESS_DASHBOARD.md) and `portfolio/supervisor_ready_manifest.yaml`.

## Method

For each of the 16 in-scope repositories: current branch, HEAD, dirty/untracked count, remote, presence of README/Makefile/CI/UML/LICENSE/CITATION/REPRODUCIBILITY, Android trees, and placeholder UML. No history rewrite. No merge to `main`. Pixel 6a: `adb devices` observed device `27211JEGR06194` **unauthorized** → not PASS.

Target branch `cursor/supervisor-ready-portfolio-release-001` did **not** exist on any repo at audit start. Portal created it from `operating-cycle-3a/wp-012-ecosystem-portal` @ `88a6e7251bbdcfceee91431f89208f79914deefb`.

## Dirty / do-not-touch working trees

| Repo | Dirty count | Action |
|---|---|---|
| `gunnchos-device-os` | 64 (artifacts, Device Lab session files) | **Do not discard.** Continue via worktree. |
| `archive-of-life-artifact-world` | 4 (stream_b JSON + untracked VP result) | Preserve; worktree or commit only new supervisor files separately |
| `pedestrian-pursuit` | 6 untracked `.uid` / VP JSON | Preserve |

All other in-scope repos were clean at audit.

## Per-repository snapshot

| Repository | Branch | HEAD (12) | UML | CI | License | Repro.md | Digital note |
|---|---|---|---|---|---|---|---|
| gunnchos-device-os | tmp-image-fit (tracks origin/main) | a1e11efcb502 | PLACEHOLDER | yes | yes | yes | Dirty; launcher_mock; not a shipping OS |
| gunnchos-hardware-industrial-design | stream/c-pkt-003-evt-firmware | 39cf58ebf412 | PLACEHOLDER | yes | yes | yes | Digital design present; PHYSICAL_PENDING |
| archive-of-life-artifact-world | stream/b-pkt-003-scientific-lifeling-expedition | 6d55f6bbc535 | MISSING | yes | **no** | no | Dirty; Android/Capacitor |
| gunnchAI3k | stream/b-pkt-003-data-dashboards-mastery | 1875d32ea5f9 | MISSING | yes | yes | no | Front door cleaned of SSJ claims at top; leftover “powers” marketing below; lecture PDFs in tree |
| waike-research-ops | stream/b-pkt-003-data-dashboards-digital-rc | ecf43ac5030b | PLACEHOLDER | yes | yes | yes | Curriculum/ops present |
| anime-aggressors | stream/b-pkt-002-playtest-polish | 36e7f0257496 | MISSING | yes | yes | no | Godot + legacy web; playtest polish branch |
| gunnchos-emergent-service-intent-protocols | cursor/oulu-publication-grade-science | 785d35d3973d | MISSING | yes | yes | no | **Private** |
| pedestrian-pursuit | stream/b-pkt-001-playtest-polish | c34f7d960422 | MISSING | yes | yes | no | Dirty untracked; Godot Android |
| beatlink-party | main | 4fc8fe017634 | MISSING | yes | **no** | no | README still has demo GIF/screenshot **placeholders**; `.env.example` referenced |
| edge-io-measurement-node | main | a1cd2e95c62e | PLACEHOLDER | yes | yes | no | Simulated measurement; Android make targets |
| gunnchos-research-portal | operating-cycle-3a/wp-012-ecosystem-portal → new branch | 88a6e7251bbd | MISSING at baseline | yes (weak: only `content/projects.ts`) | yes | no | Product IA, not supervisor PhD front door |
| ntn-resilience-sim | cursor/corrective-depth-gates-4-6 | 7ec94c219237 | PLACEHOLDER | yes | yes | yes (template) | No upstream tracking |
| 7gc-digital-twin | cursor/corrective-depth-gates-4-6 | 62126f700db4 | PLACEHOLDER | yes | yes | yes | No upstream tracking |
| spectrumx-ai-ran-gary | cursor/corrective-depth-gates-4-6 | c7e2905f4bc4 | **STRUCTURED** | **no** | **no** | no file (reproducibility/ dir exists) | UML benchmark; no LICENSE in tree |
| gunnchos-gpu-nr-baseband-platform | cursor/nvidia-real-nr-aerial-depth | 3730f236c7d4 | MISSING | yes | yes | no | **Private**; honest BLOCKED_GPU language |
| readygary-6g-beam-selection | cursor/corrective-depth-gates-4-6 | 525405cb19d7 | PLACEHOLDER | yes | yes | no | **28 GHz labelled Sub-6 GHz** in README |

## Cross-cutting defects

1. UML: 15/16 repos lack current/future/legacy packs; several `docs/uml/README.md` files only say “see SpectrumX”.  
2. Duplicated “End-to-End Research Artifact” README chrome on twin/NTN/Edge I/O/SpectrumX — supervisor cannot distinguish them in ten seconds.  
3. Two private repos: GPU NR, emergent-intent — supervisor links would 404 without owner visibility action.  
4. `gh pr list` GraphQL forbidden in sandbox at audit; draft PRs still required when auth permits.  
5. Pixel 6a attached but unauthorized.  
6. Independent reproduction: none.  
7. Portal CI does not validate PhD docs or UML.

## Strengths already present

- SpectrumX UML governance is real (current/future/legacy, traceability, render script).  
- Many core repos already have Makefile test/smoke targets and claim-boundary language (“not Oulu affiliation”, “smoke ≠ readiness”).  
- gunnchAI top-of-README already retires SSJ/doctoral-marketing claims (history file exists).  
- Hardware, device OS, WAIKE have CITATION/SECURITY/REPRO files.  
- BeatLink compliance note (no audio ripping) is correct and must be preserved.

## Baseline gates

```text
AUTOMATABLE_SUPERVISOR_READY = FAIL
CONTACT_SUPERVISOR_READY = BLOCKED
DIGITAL_MANUFACTURING_READY = FAIL
PIXEL_6A_READY = BLOCKED
CORE_RESEARCH_REPRODUCIBLE = BLOCKED
INDEPENDENT_REPRODUCTION = PENDING
```
