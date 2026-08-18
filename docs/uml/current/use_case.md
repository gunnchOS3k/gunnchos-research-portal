# Use case — current

Actors: prospective supervisor, researcher, developer, curious reader, Edmund (owner). This portal does not execute RAN control.

```mermaid
flowchart LR
  subgraph actors
    S[Prospective supervisor]
    R[Researcher]
    D[Developer]
    C[Curious reader]
    O[Owner]
  end
  subgraph portal [gunnchos-research-portal]
    UC1[Read 10-minute thesis path]
    UC2[Inspect RQ-to-repo map]
    UC3[Regenerate readiness dashboard]
    UC4[Follow product/audience path]
    UC5[Open blocker packets]
  end
  S --> UC1
  S --> UC2
  R --> UC2
  R --> UC3
  D --> UC4
  C --> UC4
  O --> UC5
  O --> UC3
```

Code/docs: `docs/phd/*`, `audiences/*`, `scripts/audit_portfolio.py`.
