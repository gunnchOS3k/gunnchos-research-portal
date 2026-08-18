# Reproducibility index

Commands below are **canonical intent** from `portfolio/repo_roles.yaml`. They are not a claim that a clean clone was executed on this host for every repo during the baseline audit (`clean_clone_status: UNVERIFIED_THIS_AUDIT` until `make reproduce` is run in that repo).

Core research target shape:

```bash
make bootstrap
make test
make reproduce
make verify
```

Native commands are kept where they are cleaner. Each core repo should still expose one obvious path.

## Core RQ repositories

| Repo | Test | Reproduce intent | Evidence class |
|---|---|---|---|
| `gunnchos-device-os` | `make test` | `make bootstrap && make test` | `EMULATED` |
| `7gc-digital-twin` | `make test` | `make setup && make test && make smoke` | `SYNTHETIC_SIM` |
| `spectrumx-ai-ran-gary` | `make test` | `make setup && make test && make smoke` | judged: `OPEN_DATA_BACKED`; extension: `SYNTHETIC_SIM` |
| `readygary-6g-beam-selection` | `make test` | `make test && make benchmark-toy` | `SYNTHETIC_SIM` |
| `ntn-resilience-sim` | `make test` | `make setup && make test && make sensitivity` | `SYNTHETIC_SIM` |
| `edge-io-measurement-node` | `make test` | `make setup && make test && make smoke` | `EMULATED` |

A research reproduction record should capture: source commit SHA, runtime version, dependency versions, seeds, dataset/version/hash, configuration, environment, command, outputs, tolerances, evidence class, elapsed time, failure diagnostics.

## Portal

```bash
make bootstrap
make audit
make test
make reproduce
```

## Independent reproduction

Cursor cannot sign for another person. Until an external packet is returned, every core repo remains `INDEPENDENT_REPRODUCTION_PENDING`. Packet: [EXTERNAL_REPRODUCTION_PACKET.md](../packets/EXTERNAL_REPRODUCTION_PACKET.md).
