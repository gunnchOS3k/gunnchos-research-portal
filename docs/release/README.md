# Current release authority

Baseline adoption: [immutable snapshot and rolling-board policy](BASELINE_ADOPTION.md). Subsequent progress is recorded in [separately versioned rolling revisions](rolling/CURRENT.json); the October 9 ledger and evidence remain unchanged. The immediate INV-01 implementation origin is `https://gunnchos.com` with a proposed `/i/<opaque-token>` route, pending implementation and verification. No configured `play.gunnchos.com` host is assumed.

The canonical V1.0.0 release-control source is [the October 9 full feature-and-gate ledger](V1_0_0_LEDGER_2026-10-09.json), rendered as the [release matrix](V1_0_0_READINESS_2026-10-09.md) and [implementation tickets/dependency path](V1_0_0_EXECUTION_2026-10-09.md).

Verdict: **NOT READY**. Target: **October 23, 2026**, fourth anniversary. Every owner-required feature remains in scope. Only the previously recorded website taste approval is retained; all other human/device/release gates remain open.

The October 4 board, September registers and RC1 packages are historical evidence. They cannot override this ledger's full-completion, full scientific-coverage or four-experience invite requirements. They remain preserved for traceability. Do not interpret their old open-PR notes or pin-specific passes as current acceptance.

Run `python3 scripts/validate_v1_release_ledger.py` to check scope retention, exact bases, dependency integrity, source hashes, rendered views and the human/release approval firewall. This validates release-control consistency, not product readiness.

Updates must name the feature/gate, exact source/artifact/deployed version, test scope/date and approval reference. Changed implementation pins invalidate affected acceptance. Human gates require an explicit owner approval record; CI never supplies one. This draft changes release controls only and authorizes no merge, deploy, tag or publication.
