#!/usr/bin/env python3
"""Additive immutable-snapshot and initial rolling-board checks."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs/release'
lock_path = DOCS / 'snapshots/2026-10-09.lock.json'
assert hashlib.sha256(lock_path.read_bytes()).hexdigest() == '7662580e513fcdbaf962762a5b5be1bd4feb420e1d333aded4fef8ff4bff7883', 'Snapshot lock changed'
lock = json.loads(lock_path.read_text())
assert lock['snapshot_commit'] == 'f74521603b039ea40d491f4658dbf09668b38a07'
for name, checksum in lock['files'].items():
    path = ROOT / name
    assert path.is_file(), 'Snapshot file removed: ' + name
    assert hashlib.sha256(path.read_bytes()).hexdigest() == checksum, 'Snapshot bytes changed: ' + name
evidence = 'docs/release/evidence/2026-10-09/'
actual = {str(p.relative_to(ROOT)) for p in (ROOT / evidence).rglob('*') if p.is_file()}
expected = {p for p in lock['files'] if p.startswith(evidence)}
assert actual == expected, 'Dated evidence set changed'
baseline = json.loads((DOCS / 'V1_0_0_LEDGER_2026-10-09.json').read_text())
# Revision 1 remains a separate immutable adoption record even when CURRENT moves later.
board = json.loads((DOCS / 'rolling/board-v0001.json').read_text())
assert board['revision'] == 1 and board['previous_revision'] is None
assert board['baseline_commit'] == lock['snapshot_commit']
assert board['baseline_ledger_sha256'] == lock['files'][board['baseline_ledger']]
assert board['gate_state'] == {n: g['passed'] for n, g in baseline['gates'].items()}, 'Adoption granted/removed gate pass'
for key in ['events', 'scope_changes', 'feature_updates', 'new_human_approvals']:
    assert board[key] == [], 'Revision 1 must not acquire later product progress'
for key in ['product_deployments_performed', 'RC2_PUBLISHED', 'V1_PUBLISHED']:
    assert board[key] is False
assert board['status'] == 'NOT_READY'
invite = board['operational_overrides']['INV-01']
assert invite['invite_origin'] == 'https://gunnchos.com'
assert invite['proposed_path'] == '/i/<opaque-token>'
assert not invite['route_implemented'] and not invite['route_verified']
assert not invite['alternative_origin_authorized']
current = json.loads((DOCS / 'rolling/CURRENT.json').read_text())
assert current['board'] == f"board-v{current['revision']:04d}.json"
assert (DOCS / 'rolling' / current['board']).is_file()
print(f"PASS: {len(lock['files'])} snapshot files unchanged; initial rolling revision preserves gates and existing-origin invite plan")
