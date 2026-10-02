# Surface control plane

`./gunnchosctl surfaces` inventories the 33 staging Worker pull requests and audits the public workers.dev pages.

```bash
./gunnchosctl surfaces inventory
./gunnchosctl surfaces audit
./gunnchosctl surfaces build --repo <repo>
./gunnchosctl surfaces smoke --repo <repo>
./gunnchosctl surfaces smoke --all
./gunnchosctl surfaces capture --all
./gunnchosctl surfaces acceptance --all
```

Outputs land in `artifacts/surfaces/latest/`.

This tool does not attach `gunnchos.com`, change nameservers, enable Email Routing, or mark a surface live. HTTP 200 is not acceptance. Game workers stay "Review build status" until a real runtime boots.

Accepted workers that this tool must not redeploy: `gunnchos-site`, `3k-mlv`, `waike-campus`, `archive-of-life`, `beatlink-party`. `finds-worker` and `finds-web` are out of scope.

DNS cutover preflight lives in `gunnchos-site` as `scripts/dns_cutover_preflight.sh`. It reads proven public records and does not write DNS.

## Research source standard

`contracts/schemas/research_source_manifest.v1.json` is the machine-readable source and reproduce record. `tools/surfaces/research_source.py` validates it. A passing manifest does not change surface depth and does not set `measured_topology`.

A public research surface should show these actions without making the visitor search the repository: Demo / Explore, Paper / Report, Source code, Reproduce, Data / Results, Cite, and Download research bundle. Evidence class stays the class the repository can actually support. Open research Worker pulls stay open until that manifest, its links, and a browser smoke pass.
