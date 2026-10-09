# October 9 baseline adoption and rolling progress

PR #54's original head is `f74521603b039ea40d491f4658dbf09668b38a07`. The 108-feature reconciliation is adopted unchanged. Its dated JSON ledger, matrix, execution tickets, validation report, evidence directory and original integrity validator are immutable historical records, including statements about what that reconciliation did or did not merge.

[Snapshot lock](snapshots/2026-10-09.lock.json) records SHA256 for every dated document/evidence file and the original validator, computed from that Git commit's bytes. The additive snapshot validator pins the lock itself and rejects changed, removed or appended files in the dated evidence directory. Neither validator is weakened. New progress never rewrites the October 9 counts, source pins, test results, deployment reports, owner records or evidence hashes. A correction to history is documented prospectively, with the original preserved.

## Rolling release board

[CURRENT](rolling/CURRENT.json) points to [board revision 1](rolling/board-v0001.json). The rolling board inherits the full feature/ticket/gate set from the immutable ledger; absence of an update means the original value, not completion or removal. Revision 1 records no product progress, no scope changes, no new human approvals, no deployments and no publication. All previously outstanding gates remain false. The two existing site passes remain historical recorded passes only.

Subsequent progress uses a new `board-vNNNN.json` with monotonic revision, date and `previous_revision`, plus a new evidence folder `rolling/evidence/vNNNN/`. Older revisions/evidence are retained byte-for-byte. Only `CURRENT.json` moves to the reviewed revision. Every update must identify baseline feature/ticket IDs, repo and branch, source SHA, artifact SHA256, deployment identity if relevant, test command/run/date/coverage, limitations and evidence references. Evidence manifests record checksums. Source code, merge state, builds, deployments, automated acceptance and owner acceptance stay separate.

Use reviewable control-plane PRs to accept each rolling revision. A changed product pin invalidates affected acceptance until re-earned; it never changes the original snapshot. Required rows and dependencies remain inherited. Scope changes require explicit owner authority and a prospective decision record; pending work cannot be reclassified as post-V1 by an agent. A passing gate requires exact evidence. Human/physical gates require explicit build-bound owner approval, and release authorization requires a separate explicit owner decision. Completion aggregates require every declared dependency; green CI alone never authorizes V1. Future validation of rolling revisions is additive to the unchanged snapshot validator.

## Prospective invite-origin correction

INV-01's dated ticket and copied owner addendum contain the proposed `play.gunnchos.com` URL. Those historical bytes remain intact. The operational origin for immediate implementation is **`https://gunnchos.com`**, using a proposed **`/i/<opaque-token>`** route. This is a route to implement and test on the existing site, not a claim that an invite service already exists. No separate `play.gunnchos.com` DNS/domain/Worker binding is assumed, created or authorized by this adoption.

Any alternative origin needs explicit authorization and verified DNS/TLS/route/runtime and fallback evidence before the rolling board can select it. Token URLs carry no phone numbers, contact lists, private messages, credentials or sensitive game state. The four experiences, MLV/Device OS routing and mobile/browser fallback requirements are unchanged.

## Adoption verification and handoff boundary

At the pinned original head, GitHub reports PR #54 mergeable with a clean merge state and two successful `check` jobs. Main is unprotected with no configured required status contexts; the legacy combined-status endpoint has zero statuses and says pending, which is not a failed check. The final adoption head must also have all workflow checks green before the normal merge with an expected-head guard.

The allowed diff is control-plane documents, evidence/line-ending preservation, historical-register annotations and additive integrity validation/CI wiring. No product runtime, dataset, build or deployment configuration is edited. After merging, record the merge SHA and current main SHA in the local implementation handoff artifact; hand off ARC-01, ANI-02, ANI-01 and INV-01 at their ledger bases without launching product work. The control-plane merge is not any product owner approval or V1/RC2 authorization.
