# Reproducibility — research portal

This repository is documentation + audit scripts. It does not produce RF results.

```bash
git clone https://github.com/gunnchOS3k/gunnchos-research-portal.git
cd gunnchos-research-portal
python3 -m pip install pyyaml
make audit
make test
make reproduce
```

Expected: `scripts/validate_supervisor_ready.py` prints PASS; `portfolio/supervisor_ready_manifest.yaml` is regenerated.

Sibling checkouts: set `PORTFOLIO_REPOS_ROOT` to the directory that contains the other 15 repos if they are not `../<name>`.

Record the portal commit SHA in any supervisor packet. This is not independent reproduction of RQ1–RQ3 experiments.
