# Role-Specific Resume Bullets (Draft)

Honest wording: **prototype**, **mock**, **portfolio lab**, **designed**, **documented**, **implemented smoke tests**. Do not imply paid production SOC / PRISM / silicon tape-out experience unless true elsewhere.

## Agentic SecOps

- Designed and documented a **mock AI-assisted SOC triage workflow** in the gunnchAI3k Agentic SecOps Lab, converting unstructured synthetic threat reports into structured IOC JSON using an **offline defensive extractor** (no external APIs).
- Implemented **portfolio-safe smoke tests** validating IOC schema, mock labeling, and absence of secret-like fields in generated artifacts.
- Authored **YARA-L- and Sigma-style mock detection skeletons** and playbooks emphasizing **analyst validation** before any operational use.
- Documented **GenAI security risks** (prompt injection, hallucinated indicators, data leakage, model over-trust) and **human-in-the-loop** controls for agentic security operations.

## Access Risk

- Built a **mock IAM access graph** for the gunnchOS console ecosystem, modeling student, educator, service, research, and guest identities against console and data resources.
- Implemented an **attack-path modeling prototype** that flags risky privilege paths (guest→telemetry, impersonation, over-export, unapproved model config changes) from synthetic bindings.
- Developed a **least-privilege recommender** producing markdown tables with risk rationale for portfolio review.
- Documented **security invariants** and a **zero-trust device access model** for offline-first student consoles (prototype stage).

## RTL Verification

- Designed **console-relevant SystemVerilog examples**: parameterized SRAM/BIST educational module and framebuffer register block for the gunnchOS hardware roadmap.
- Wrote **directed smoke testbenches** and **SVA property stubs** with a documented verification and coverage plan (sample logs — not fabricated tool coverage %).
- Produced a **UVM roadmap** describing future agents, scoreboard, and coverage collector — directed+SVA pass only today.
- Connected memory/display subsystem verification concepts to [gunnchos-hardware-industrial-design](https://github.com/gunnchOS3k/gunnchos-hardware-industrial-design) and [gunnchos-device-os](https://github.com/gunnchOS3k/gunnchos-device-os) architecture docs.
