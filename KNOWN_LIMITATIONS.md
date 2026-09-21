# Known limitations — gunnchOS Ecosystem v1.0.0-rc.1

## Explicitly false / pending (do not greenwash)

- Physical EVT / DVT / PVT PASS
- READY_FOR_FAB
- RF, carrier, regulatory, or battery-transport certification
- Mass manufacturing / production yield
- Warranty / RMA readiness
- Institutional / school-wide deployment
- Disabled-user accessibility validation (unless separately performed and evidenced)
- Final public release `v1.0.0` (unauthorized until owner approval)

## Software honesty

- Nearby Mac is not on-device gunnchAI
- No fake-gunnchAI product inference
- Open PRs outside freeze remain OUTSIDE_RC1 / STALE / EXPERIMENTAL / FUTURE
- Hardware PR #84 and experimental #69–#79 are outside V1 mainline
- Device OS launcher_mock **dev/test** toolchain still carries deferred vite/vitest advisories (not production-reachable); major bumps planned post-RC1
- In-app Feedback entry points are `RC1_DESIRED` / `V1_REQUIRED` — public portal front door is the RC1 channel

## Demo device

- Pixel demo requires exclusive authorized ADB device
- Raw device serials must not appear in commits

## Security reporting

- Vulnerabilities must use **private** GitHub Security Advisories — never public issues
