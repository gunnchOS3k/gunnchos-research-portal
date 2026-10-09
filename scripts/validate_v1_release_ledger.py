#!/usr/bin/env python3
"""Validate release-control integrity without granting product or human acceptance."""
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs/release'
EVIDENCE = DOCS / 'evidence/2026-10-09'
ledger = json.loads((DOCS / 'V1_0_0_LEDGER_2026-10-09.json').read_text())
features = ledger['features']
tickets = {t['id']: t for t in ledger['tickets']}
gates = ledger['gates']
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


check(len(tickets) == len(ledger['tickets']), 'Duplicate ticket ID')
check(len({f['id'] for f in features}) == len(features), 'Duplicate feature ID')
check(ledger['as_of'] == '2026-10-09', 'Snapshot date changed')
check(ledger['target'] == '2026-10-23', 'Owner target changed')
check(ledger['portal_base_commit'] == '947138fcec929f7f21f1738fb6e2fad11f32661a', 'Portal base changed')
check(not ledger['merged_or_published_by_this_task'], 'Reconciliation must not merge/publish')
for t in tickets.values():
    check(bool(re.fullmatch('[0-9a-f]{40}', t['base_commit'])), f"Invalid ticket base: {t['id']}")
    check(t['repo'] in ledger['repo_bases'], f"Unknown ticket repo: {t['id']}")
    check(bool(t['base_branch']) and bool(t['acceptance']), f"Missing base/acceptance: {t['id']}")
    for d in t['depends_on']:
        check(d in tickets, f"Unknown dependency {d} for {t['id']}")
visiting, visited = set(), set()


def visit(id):
    if id in visiting:
        errors.append('Dependency cycle at ' + id)
        return
    if id in visited or id not in tickets:
        return
    visiting.add(id)
    for dep in tickets[id]['depends_on']:
        visit(dep)
    visiting.remove(id)
    visited.add(id)


for id in tickets:
    visit(id)
historical = list(csv.DictReader((EVIDENCE / 'historical-scope-ledger.csv').open()))
by_id = {f['id']: f for f in features}
for h in historical:
    check(h['id'] in by_id, 'Historical scope omitted: ' + h['id'])
    if h['disposition'].startswith('IN_V1') and 'OPTIONAL' not in h['disposition']:
        check(by_id.get(h['id'], {}).get('required_for_v1'), 'Required scope silently reduced: ' + h['id'])
for id in ['ARCH-003', 'ARCH-004', 'MLV-006', 'PP-001', 'PP-002', 'ARC-ICS', 'ARC-LIFE', 'ARC-MAPS', 'PASSPORT']:
    check(by_id.get(id, {}).get('required_for_v1'), 'Missing owner-required override: ' + id)
check(sum(f['id'].startswith('WORLD-') for f in features) == 20, 'Full world spaces omitted')
check(sum(f['id'].startswith('INVITE-') for f in features) == 8, 'Invite domains omitted')
for f in features:
    for t in f['tickets']:
        check(t in tickets, f"Unknown ticket {t} for feature {f['id']}")
    check(bool(re.fullmatch('[0-9a-f]{40}', f['base_commit'])), 'Feature base invalid: ' + f['id'])
    for name in f['evidence']:
        check((EVIDENCE / name).is_file(), 'Missing evidence: ' + name)
    if f['complete']:
        check(f['id'] == 'SITE-TASTE' and f['owner_approved'] == 'APPROVED_RECORDED', 'Unearned complete feature: ' + f['id'])
for name, g in gates.items():
    if g['passed']:
        check(name in {'V1_PUBLIC_SITE_PASS', 'V1_SITE_HUMAN_TASTE_PASS'}, 'Unearned approval/pass: ' + name)
        check(bool(g['evidence']), 'Pass lacks evidence: ' + name)
    if g['kind'] == 'AUTOMATED_AGGREGATE' and g['passed']:
        check(all(gates[d]['passed'] for d in g['depends_on']), 'Aggregate without dependencies: ' + name)
check(len(gates['V1_INVITES_FULL_PASS']['depends_on']) == 8, 'Invite aggregate omits required gate')
check(not gates['V1_INVITES_HUMAN_PASS']['passed'], 'Invite human approval must remain open')
check(not gates['V1_0_0_RELEASE_AUTHORIZED']['passed'], 'Release authorization must remain false')
check(not gates['RC2_OWNER_AUTHORIZED']['passed'], 'RC2 authorization must remain false')
for entry in json.loads((EVIDENCE / 'source-index.json').read_text()):
    check(hashlib.sha256((EVIDENCE / entry['file']).read_bytes()).hexdigest() == entry['sha256'], 'Evidence hash mismatch: ' + entry['file'])
for title in ['pursuit', 'anime']:
    manifest = json.loads((EVIDENCE / (title + '-live-manifest.json')).read_text())
    check(manifest['release_channel'] == 'DEVELOPMENT', 'Game release channel falsely promoted')
check(json.loads((EVIDENCE / 'pursuit-live-manifest.json').read_text())['source_sha'] == ledger['repo_bases']['pedestrian-pursuit']['sha'], 'Pursuit deployment mismatch')
checks = json.loads((EVIDENCE / 'github-snapshot.json').read_text())['checks']
waike = next(v for k, v in checks.items() if k.startswith('gunnchos-waike-learning-platform@'))
check(waike['total'] == waike['returned'] == 77, 'WAIKE check result was truncated')
check(all(c['conclusion'] == 'success' for c in waike['checks']), 'WAIKE check conclusion changed')
view = (DOCS / 'V1_0_0_READINESS_2026-10-09.md').read_text()
execution = (DOCS / 'V1_0_0_EXECUTION_2026-10-09.md').read_text()
for f in features:
    check('| ' + f['id'] + ' |' in view, 'Feature missing from view: ' + f['id'])
for name, g in gates.items():
    check('| `' + name + '` | ' + g['kind'] + ' | ' + str(g['passed']).lower() + ' |' in view, 'Gate view drift: ' + name)
for t in tickets.values():
    check('### ' + t['id'] + ' ·' in execution and t['base_commit'] in execution, 'Ticket view missing base: ' + t['id'])
if errors:
    raise SystemExit('\n'.join(errors))
print(f"PASS: {len(features)} features, {len(gates)} gates, {len(tickets)} tickets; scope, SHA bases, DAG, evidence hashes and owner firewalls intact")
