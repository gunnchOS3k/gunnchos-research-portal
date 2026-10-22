# Field Kit #123 — fresh Standards Watch dispatch plan (NOT EXECUTED)

Review-only plan, October19. **Do not run the dispatch command under this task's authorization.** A separate explicit workflow-execution instruction is required. No new run ID or successful source fetch is asserted.

## Fixed source and review

- Repository: `gunnchOS3k/gunnchos-7gc-ai-ran-field-kit`.
- Draft [PR #123](https://github.com/gunnchOS3k/gunnchos-7gc-ai-ran-field-kit/pull/123), branch `release/standards-watch-dependencies-2026-10-19`, exact remote/local head `ddf90ab0c4e4b29e765be73093d0ba91c59249d0`.
- Accepted main remains `9dfc326647880c244904dd50a47ea80c3d46748e`; repair **pending on accepted main**. PR open/draft/mergeable; 21 returned checks successful, with distinct check IDs retained in REMOTE_SOURCE_CHECK.json. Standards Watch is scheduled/manual and is not proved by these PR checks.
- Only change from parent/main: two added workflow lines install existing `pyyaml>=6.0` before unchanged validators. Python3.12 setup, claim firewall, standards mapping, watcher, artifact path and compliance policy are unchanged. No scientific claims or manuscript changes.
- Fresh local read-only validators: STANDARDS_VALIDATE_PASS and CLAIM_FIREWALL_PASS in Python3.14.7/PyYAML6.0.3. This differs from the workflow's Python3.12 environment and does not prove a dispatched run.
- Known failed scheduled run36904310777 used accepted-main9dfc326. Rerunning that old run retains its original source and will not pick up ddf90ab. Request a new workflow_dispatch against the fixed branch instead.

## Future execution sequence

1. Re-read the branch ref and abort if it differs from ddf90ab. Inspect the workflow at that ref; preserve compliance_claim NONE. Record UTC dispatch window, workflow ID and expected source before any action. If the branch moves, stop and obtain a new source-specific plan.
2. Only following separate authorization, create a **fresh** dispatch:
```sh
gh workflow run standards-watch.yml \
  --repo gunnchOS3k/gunnchos-7gc-ai-ran-field-kit \
  --ref release/standards-watch-dependencies-2026-10-19
```
3. Select the new run by event `workflow_dispatch`, branch, dispatch timestamp and `headSha == ddf90ab0c4e4b29e765be73093d0ba91c59249d0`. Do not select an old run by “latest” alone. Record run ID, attempt (fresh attempt1), URL, workflow path/ID, head SHA, event, branch and created/completed times. Inspect checkout identity plus dependency-install, mapping, firewall, fetch and upload steps.
4. Require successful conclusion **and** download the `standards-watch` artifact from that exact run. Record artifact ID, run/source binding and available GitHub digest; calculate the downloaded ZIP and report SHA256, retain them locally. Reject expired/missing artifacts or a report timestamp outside the new run.
5. Inspect the new `watch_report_<UTC>.json`, not just last_hashes.json or stdout. The report must have exactly these three source keys, each with its exact URL, `status == "ok"` and a nonempty 64-character lowercase SHA256:

   | Key | URL |
   |---|---|
   | ITU-IMT-2030 | https://www.itu.int/en/ITU-R/study-groups/rsg5/rwp5d/imt-2030/pages/default.aspx |
   | ITU-IMT-FAMILY | https://www.itu.int/en/ITU-R/study-groups/rsg5/rwp5d/pages/imt.aspx |
   | 3GPP-REL20 | https://www.3gpp.org/specifications-technologies/releases/release-20 |

   Require exact `compliance_claim == "NONE — do not auto-claim compliance after source change"`; last_hashes.json must agree with the report. Manually inspect deltas and provenance; page hashes alone establish retrieval/change detection, not compliance, scientific completeness or standards conformance.
6. Any fetch error, null/missing/malformed hash, wrong source/ref/time, incomplete artifact or changed claim means **NOT VERIFIED**, even if the job prints WATCH_OK and is green. Preserve the actual failure; no invented replacement hashes, old artifact substitution or unapproved rerun. A result on this unmerged branch leaves accepted-main repair pending.
7. Return exact run/artifact evidence for review only. Do not merge, publish or modify gate states.

## Reproduced reason for strict artifact inspection

The watcher at this source catches exceptions for each URL, emits error/null entries, then unconditionally prints WATCH_OK and returns0. A fresh isolated probe redirected STD to `/private/tmp/v1-standards-offline-probe-qzqc8pq1/standards` and replaced only its fetch function in memory with an explicit fictional URLError. All3 statuses were errors, all3 hashes null, exit0, WATCH_OK, compliance_claim unchanged; no source network fetch or repository mutation occurred. This is a demonstrated false-green risk, not a claimed failure of a newly dispatched run.

Future bounded hardening, if separately assigned: add a strict post-fetch artifact verification step while retaining all three sources and the NONE claim. That implementation is outside this plan; PR #123 remains the narrow dependency fix.
