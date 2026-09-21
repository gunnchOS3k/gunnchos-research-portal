# Research V1 — gunnchOS Ecosystem v1.0.0-rc.1

All pins are live accepted `origin/main` SHAs.

## 7GC Digital Twin

| | |
|---|---|
| Question | How do campus operational scenarios behave under load, disruption, and policy? |
| Method | Scenario engine + site profiles + integration adapters |
| Inputs | Synthetic campus profiles; optional adapter feeds |
| Outputs | Metrics/reports; operational demo artifacts |
| Real vs synthetic | Primarily synthetic/scenario; integrations may ingest external summaries |
| Reproduce | Clone `7gc-digital-twin` @ `dc43a567e3f2e81a5b59fea6dd67c7054cfdde56`; follow README/Makefile demos |
| SHA | `dc43a567e3f2e81a5b59fea6dd67c7054cfdde56` |

## SpectrumX AI-RAN Gary

| | |
|---|---|
| Question | Can AI-RAN policies improve fairness/energy under campus radio conditions? |
| Method | Baselines + policy interface + synthetic campus data |
| Inputs | Synthetic radio/campus profiles |
| Outputs | Metrics, reports, campus run scripts |
| Real vs synthetic | Synthetic research data unless otherwise labeled |
| Reproduce | `spectrumx-ai-ran-gary` @ `9060655e724374f60cbbb86832816c9c2d332ca4` |
| SHA | `9060655e724374f60cbbb86832816c9c2d332ca4` |

## ReadyGary (beam selection)

| | |
|---|---|
| Question | Which beam-selection policies hold under FR2 / domain shift? |
| Method | Benchmark tables, heldout policies, timing harness |
| Inputs | Experiment configs + synthetic/benchmark sets |
| Outputs | `results/` metrics tables; research cards |
| Real vs synthetic | Benchmark/synthetic unless measurement-labeled |
| Reproduce | `readygary-6g-beam-selection` @ `569875224db7812890ec6abc48dfe43a608094f3` |
| SHA | `569875224db7812890ec6abc48dfe43a608094f3` |

## NTN resilience

| | |
|---|---|
| Question | How does service continuity behave under NTN/disruption campus scenarios? |
| Method | Campus scenarios + CLI reports |
| Inputs | Scenario definitions |
| Outputs | Resilience reports |
| Real vs synthetic | Simulated |
| Reproduce | `ntn-resilience-sim` @ `c4215fc1039f5452917b9b2034b42e03fdc13689` |
| SHA | `c4215fc1039f5452917b9b2034b42e03fdc13689` |

## Edge IO

| | |
|---|---|
| Question | How do privacy-preserving edge measurements export into 7GC research flows? |
| Method | Measurement plans, privacy transforms, campus export |
| Inputs | Planned/demo measurements |
| Outputs | Export packages; privacy reports |
| Real vs synthetic | Demo/synthetic unless device-measured and labeled |
| Reproduce | `edge-io-measurement-node` @ `af57fbdac857ae386b23b5b747fdc05797621f92` |
| SHA | `af57fbdac857ae386b23b5b747fdc05797621f92` |

## 7GC AI-RAN Field Kit

| | |
|---|---|
| Question | What is the program charter / field kit for campus AI-RAN demonstration? |
| Method | Program docs + kit artifacts on accepted main |
| Inputs | Charter and kit materials |
| Outputs | Field-kit documentation/evidence tree |
| Real vs synthetic | Program/engineering artifacts |
| Reproduce | `gunnchos-7gc-ai-ran-field-kit` @ `9e93e41a3b16b009c9cc5163b775360d4d2ef693` |
| SHA | `9e93e41a3b16b009c9cc5163b775360d4d2ef693` |

## WAIKE workloads

| | |
|---|---|
| Question | Can realistic learning workloads drive device/edge/research coupling? |
| Method | 18-track curriculum ops + LP client |
| Inputs | Curriculum imports/registry |
| Outputs | Track packs; learner sessions |
| Real vs synthetic | Authored curriculum; demo identities |
| Reproduce | LP `c306543ccc89…` (child `efe21df…`); ops `e919976237cb…` (child `63ba9f25…`) |

## gunnchAI edge intelligence

| | |
|---|---|
| Question | How does local-first tutoring/assist behave with truthful provenance? |
| Method | Service/runtime + WAIKE consumer integration |
| Inputs | Prompts/context; optional Nearby Mac host |
| Outputs | Tutor responses with availability honesty |
| Real vs synthetic | Model/runtime dependent; never fake product inference |
| Reproduce | `gunnchAI3k` @ `ef665648aecb…` (children `d4a5c6d…`, `e2d1adc…`) |

## Feedback & Suggestions

Public feedback hub: [FEEDBACK.md](FEEDBACK.md)  
Security (private only): [SECURITY.md](SECURITY.md)  
Do not post exploitable security details publicly.

