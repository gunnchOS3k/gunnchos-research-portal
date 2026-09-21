# Device OS #161 provenance for RC1 demo

| Role | SHA / ref |
|------|-----------|
| Device OS accepted main (base) | `bf109e704ac28b38b9fe1d9ce39954158f061793` |
| Draft PR | https://github.com/gunnchOS3k/gunnchos-device-os/pull/161 (draft; **not** accepted-main yet) |
| Pixel demo production head | `563271f8d02a74fc61be5e6893a5ab524767083f` |
| Green CI head (test-only follow-up) | `5e88313e42b0a5ce42d7c2e2a990f3ac43a6f5eb` |

## Purpose
WAIKE Capsule loopback Hub URL handoff + Continue lesson path for the RC1 career-fair Pixel demo.

## Pixel proof inherit
`5e88313…` changes only `apps/launcher_mock` vitest setup (`window.matchMedia` polyfill) and CX2 adapter assertions. No production Capsule/shell code change → inherit Pixel demo evidence earned on `563271f…`.

## Freeze / tag rule
Merge #161 into Device OS accepted main **before** final accepted-main RC1 freeze or Device OS `v1.0.0-rc.1` release tag. Do **not** tag Device OS RC1 at old main `bf109e7…` if #161 is required for the demo path.

## Nearby Edge
Live Nearby Edge gunnchAI unavailable; do not claim `gunnchai_live_response=true`.
