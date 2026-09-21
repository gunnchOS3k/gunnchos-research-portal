# Device OS #161 provenance for RC1 demo

| Role | SHA / ref |
|------|-----------|
| **Device OS accepted main (current)** | `c6fd04aced44b0d3eec6f07c3b0b3fdbe50ad7a4` |
| Merge | Normal merge commit of owner-merged PR [#161](https://github.com/gunnchOS3k/gunnchos-device-os/pull/161) |
| Prior accepted main (superseded) | `bf109e704ac28b38b9fe1d9ce39954158f061793` — **do not use for RC1 tag** |
| Pixel demo production head (pre-merge) | `563271f8d02a74fc61be5e6893a5ab524767083f` |
| Green CI head merged via #161 | `5e88313e42b0a5ce42d7c2e2a990f3ac43a6f5eb` (ancestor of accepted main: **yes**) |

## Purpose
WAIKE Capsule loopback Hub URL handoff + Continue lesson path for the RC1 career-fair Pixel demo.

## Ancestry checks (post-merge)
```text
git merge-base --is-ancestor 5e88313e42b0a5ce42d7c2e2a990f3ac43a6f5eb origin/main  # OK
git rev-parse origin/main  # c6fd04aced44b0d3eec6f07c3b0b3fdbe50ad7a4
```

## Pixel proof inherit
`5e88313…` changes only `apps/launcher_mock` vitest setup (`window.matchMedia` polyfill) and CX2 adapter assertions relative to the production handoff head. Post-merge lockfile-only dependency remediation does not change production/runtime deps → Pixel re-demo **not** required for the vuln-closure pass.

## Nearby Edge
Live Nearby Edge gunnchAI unavailable; do not claim `gunnchai_live_response=true`.
