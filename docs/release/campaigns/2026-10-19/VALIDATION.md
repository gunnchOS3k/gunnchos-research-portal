# Campaign validation

- Original ledger validator: PASS — 108 features, 38 gates, 43 tickets retained.
- Snapshot-adoption validator: PASS — all 23 locked historical files and the original validator unchanged.
- New campaign validator: PASS — exact canonical 16 membership, remote source bindings, 33 verified asset hashes, eight EPUB/report bindings, six limited journeys, preserved gate states, evidence checksums and blocked RC2 flags.
- Negative integrity check in a temporary copy: baseline validates; changing `RC2_READY` to true fails. The real board was not mutated.
- `make test` in an isolated temporary pytest environment: supervisor validator PASS; all seven portfolio tests PASS.
- `git diff --check`: PASS.
- Field Kit repair: clean-interpreter missing-yaml failure reproduced; installing the existing PyYAML requirement yields `STANDARDS_VALIDATE_PASS` and `CLAIM_FIREWALL_PASS`. The scheduled/manual job has not been rerun or repaired on accepted main by this draft.
- Published RC1 assets: 33/33 streamed bytes match size and GitHub SHA-256 digests. Nothing saved/executed.
- Repaired review EPUBs: all eight actual local files match successful official EPUBCheck reports; no editorial/rights/human publication acceptance is inferred.

No full product builds or historical acceptance suites were repeated merely for continuity. Fresh UI probes and read-only source/asset/device checks are separately scoped in the report. The two owned loopback preview processes were stopped. No manuscript, private database, key, instructor-answer payload, new deployment or release is included in the control-plane changes.

Portal CI runs this campaign check additively alongside the unchanged baseline validators and existing checks. A passing control-plane CI run is not a product or release approval.
