# Research scope and boundaries

This portfolio is larger than a dissertation. That is intentional engineering breadth, not sixteen research objectives.

## In scope for the dissertation

- Service-continuity profiles for four resource-constrained device classes (RQ1).  
- Radio-aware digital-twin scenarios and schemas that make those profiles experimentally usable (RQ1).  
- Joint access / placement / fidelity / cache / recovery control versus transparent baselines, with uncertainty and twin context (RQ2).  
- Terrestrial / local-edge / peer / offline / NTN fallback under disruption, including energy, privacy, and recovery tradeoffs (RQ3).  
- Honest evidence labels: synthetic simulation, open-data-backed, emulated, device-measured, lab-measured, externally reproduced, field-validated.

## Out of scope as dissertation papers

- Commercial product launch of handheld computers.  
- Game design as a telecommunications contribution.  
- WAIKE as a standalone education PhD.  
- gunnchAI as a standalone AI PhD.  
- GPU NR as 3GPP conformance.  
- Emergent service-intent protocols as a mandatory fourth paper.  
- Manufacturer RFQ execution, certification (FCC/CE/USB-IF/carrier), or field deployment.

Those items may still appear as **workloads, form-factor constraints, optional extensions, or engineering evidence**.

## Claim boundaries (always)

| Claim type | Allowed today only if |
|---|---|
| Simulation result | Seed, config, code SHA, and regenerable artifacts exist |
| Open-data result | Dataset source/version/license/hash recorded |
| Device measurement | Hardware + procedure + calibration evidence exist |
| Lab / RF result | Instrumented measurement package exists |
| Independent reproduction | Named external reproducer evidence exists |
| Oulu / 6G Flagship fit | Mapping to public research themes; **no affiliation** |
| Product “finished” | User-journey evidence, not a vertical slice |
| Android “Pixel 6a PASS” | Authorized device session evidence |

## Hypothesis can fail

Controllers, twins, and fallback policies are implemented so that **null results remain representable**. The portfolio must not be read as a claim that cross-layer control already outperforms strong baselines in the field.

## Product language vs research language

The public ecosystem portal still describes first-party devices, education, and games for non-research audiences. Those pages are not dissertation claims. Research readers should stay on `docs/phd/` and the six core RQ repositories.
