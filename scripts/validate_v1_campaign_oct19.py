#!/usr/bin/env python3
"""Validate prospective release evidence without changing the frozen baseline."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs/release'
EVIDENCE = DOCS / 'rolling/evidence/v0002'
CAMPAIGN = DOCS / 'campaigns/2026-10-19'


def read(path):
    return json.loads(path.read_text())


original = read(DOCS / 'rolling/board-v0001.json')
board = read(DOCS / 'rolling/board-v0002.json')
assert board['revision'] == 2 and board['previous_revision'] == 1
assert board['baseline_commit'] == original['baseline_commit']
assert board['baseline_ledger_sha256'] == original['baseline_ledger_sha256']
assert board['gate_state'] == original['gate_state'], 'No new release/human approvals in this campaign'
assert board['scope_changes'] == [] and board['new_human_approvals'] == []
assert board['status'] == 'NOT_READY'
assert board['operational_overrides'] == original['operational_overrides']
for key in ['product_deployments_performed', 'RC2_PUBLISHED', 'V1_PUBLISHED']:
    assert board[key] is False
canonical = read(ROOT / 'releases/v1.0.0-rc.1/FINAL_ACCEPTED_MAIN_MANIFEST.json')
names = {c['repo'].split('/')[-1] for c in canonical['components'] if c['in_v1_rc1']}
matrix = read(CAMPAIGN / 'RELEASE_MATRIX.json')
assert len(matrix) == len(names) == 16
assert {r['repo'] for r in matrix} == names, 'Canonical membership changed'
remote = read(EVIDENCE / 'github-state.json')
for row in matrix:
    repo = remote['repos'][row['repo']]
    assert row['main_sha'] == repo['main']['sha']
    assert row['rc1_source_sha'] == repo['rc1']['source_sha']
    assert repo['rc1']['prerelease'] and not repo['rc1']['draft']
    assert row['classification'] in {'RED', 'YELLOW'}, 'Full acceptance is not granted here'
assets = read(EVIDENCE / 'RC1_ASSET_VERIFICATION.json')
assert len(assets) == 33 and all(a['verified'] for a in assets)
assert all(a['digest'] == 'sha256:' + a['computed_sha256'] for a in assets)
publication = read(EVIDENCE / 'PUBLICATION_VERIFICATION.json')
assert len(publication['editions']) == 8
assert all(e['current_bytes_match'] and e['report_status'] == 'PASS' for e in publication['editions'])
for key in ['rights_clearance', 'editorial_approval', 'release_approval']:
    assert publication[key] is False
assert all(not r['official_v1_present'] and not r['rc2_present'] for r in read(EVIDENCE / 'PUBLISHED_RELEASE_STATE.json'))
rc2 = read(CAMPAIGN / 'RC2_PREPARATION_MANIFEST.json')
for key in ['RC2_READY', 'RC2_OWNER_AUTHORIZED', 'V1_0_0_RELEASE_AUTHORIZED', 'published']:
    assert rc2[key] is False
assert rc2['tags_created'] == [] and len(rc2['components']) == 16
assert all(not r['artifact_verified_for_rc2'] and not r['integration_accepted'] and not r['owner_accepted'] for r in rc2['components'])
journeys = read(EVIDENCE / 'JOURNEY_RESULTS.json')['journeys']
assert {j['id'] for j in journeys} == set('ABCDEF')
assert all(j['not_proven'] for j in journeys)
manifest = read(EVIDENCE / 'MANIFEST.json')
actual = {p.name for p in EVIDENCE.iterdir() if p.is_file() and p.name != 'MANIFEST.json'}
assert actual == set(manifest['files'])
for name, expected in manifest['files'].items():
    assert hashlib.sha256((EVIDENCE / name).read_bytes()).hexdigest() == expected, 'Evidence hash mismatch: ' + name
print('PASS: canonical 16, RC1 assets, eight EPUB bindings, six scoped journeys, revision 2 and unchanged approval boundaries')
