# Private WAIKE delivery assessment — October 19, 2026

**PARTIAL REPRODUCTION / TRUSTED-TLS REPLAY BLOCKED. Official V1: NOT READY / NOT AUTHORIZED. RC2: UNFROZEN / NOT READY / NOT AUTHORIZED.** No gate or scope changed. This is a local continuation from portal draft PR #55 at `052f1723df5644156305a5cad99408ef8d8cc61e`; it is not an accepted-main update or publication.

## Exact identities

| Layer | Source / artifact actually inspected | Meaning |
|---|---|---|
| Accepted portal main | `1cd5819b446a8ba0e0e4d0c24a0305dee4a86e2c` | Unchanged; #55 remains draft/open at the requested checkpoint; two checks successful |
| Built gateway | Site `a6f4cd620123c1d12ac704346fb4a7fe5b51b05e`, branch `delivery/full-learning-2026-10-15`; Next build ID `5ZovRgVg-ApL0-J7YMJI1` | Existing build reused, never rebuilt; source checkout has preserved dirty continuations |
| Retained reader release | Platform `c7d1aefd9a641e99c8cf1746c9d6eef841a3096f`, curriculum `33a101852f4fefb0eb239bcffa60a65d71102e2c` | Both tree hashes freshly match `.release/candidates/c7d1aef/runtime-release.json`; reader not started |
| Later platform HEAD | `6bdfa0b416ea95b0abb36669faa8059095962281` | Clean checkout; Hub/client/PIN bytes have no Git diff from c7d1aef. Later HEAD is not the retained build identity |
| Workshop package / later curriculum HEAD | `18efa764e4db066fb17d597284557195499f93ea` | Clean checkout; gateway displays this workshop source separately from 33a1018 canonical course evidence |
| Public sources | Site `f4f4c85cd5bb924a6bc5ca2d196f159da32c81b9`; platform `2641042936f3b965daccb11091c80cbc6fa64f91`; curriculum main `34ae043abbd38c89bd30f7ae1ae7cf8cc06645a0` | Relevant accepted mains freshly read, unchanged. Campaign's public deployment/source bindings remain distinct from local builds |
| Public reader curriculum pin | `63ba9f25ac6b8d8d1b6dd118923566fd51c57b62` | Existing campaign deployment binding; no new deployment or live rollout verification in this continuation |

Full hashes, dirty paths, dependency versions and read-only checks are in [EVIDENCE.json](EVIDENCE.json). Source fingerprint and built-page hashes bind the gateway observation; a Git HEAD alone does not prove that an unrebuilt build contains later dirty documentation.

## What executed

| Step | Fresh result | Limit |
|---|---|---|
| Port / database guards | 4194 and 4197 initially free; no process held the named rehearsal database; schema/migration read used SQLite `mode=ro` | No database migration, seed, learner account or reader process |
| Retained artifacts | Manifest, reader and curriculum hashes match; exact source comparison passes for Hub/client/PIN | No source repin, new build or reader fix |
| Buyer gateway | Existing Next 15.5.28 build ran on loopback 4197, Node 24.9.0 / npm 11.6.0; workshop rendered with pending-review boundaries | HTTP gateway check, not a trusted-HTTPS reader pass |
| Instructor link / return | Instructor packet route opens; browser Back returns to workshop | No instructor rehearsal, observation or private answer payload exported |
| Empty evidence export | Clicking “Download unsubmitted evidence note” with no file/explanation produces the explicit input guard | Negative check only; no valid export or course record created |
| Client regressions | Two existing files, five tests pass: bounded deep links, ungraded evaluation, failure honesty, opt-in draft save/restore, delayed-file-read answer preservation | jsdom/mocked fetch, not live TLS/API, authentic learners or all 18 tracks; React act warning remains |
| Field Kit | Standards mapping and unchanged claim firewall both PASS in existing isolated Python environment; offline false-green reproduction confirmed | No external fetch, workflow dispatch/rerun or accepted-main repair |

Gateway process: execution session94594, PID13835, loopback only; stopped after these checks. The first sandboxed bind returned EPERM; the authorized loopback retry succeeded. No service was substituted for the missing reader.

## Reproducible blockers and limits

**WAIKE-REPLAY-01 — expired rehearsal certificate.** Retained certificate CN/SAN localhost, SHA256 fingerprint `5CC4CEF6B03288A177349C6562727ED6D7E4ED7087ECF2E39AA92D57CB0F5F18`, valid October 15 20:32:20 UTC through October 17 20:32:20 UTC. On October 19 it fails:
```sh
openssl verify -CAfile deploy/production/private/local-acceptance/tls.crt \
  -attime 1792433100 deploy/production/private/local-acceptance/tls.crt
```
Result: error10, certificate has expired. The explicit evaluation time is October 19 18:05 UTC. macOS `security verify-cert` printed “No error”; that does not override the expired validity interval or establish successful browser TLS. No trust store, certificate, DNS or global verification setting changed; no warning bypass, `-k` or allow-self-signed harness was used.

**WAIKE-REPLAY-02 — temporary environment absent.** `/private/tmp/waike-recovery-platform-env/bin/uvicorn` no longer exists. The retained release, key paths and database still exist. Recreate only the documented temporary environment from the existing requirements lock plus pytest/httpx/jsonschema/pynacl when the TLS prerequisite is available; do not rebuild the reader. The historical environment list is not an active running-version claim.

**FIELD-WATCH-01 — success output does not establish successful source retrieval.** At ddf90ab the unchanged watcher catches each fetch exception, writes null hashes/error statuses, then returns 0 and prints WATCH_OK. An isolated, explicitly fictional offline probe reproduced all three failures with zero network requests and no repository output writes. [Dispatch plan](FIELD_KIT_DISPATCH_PLAN.md) therefore requires inspecting the new run's artifact, not its green badge.

The lesson → fresh practical → wrong-input correction/feedback → browser opt-in save/restore → positive unsubmitted export sequence **was not executed end to end**. Do not label its unexecuted steps PASS. No fictional practical results were fabricated to fill the missing reader segment. Existing October15 allow-self-signed evidence remains historical engineering evidence, and the already-fixed reader/file-read behavior was not reimplemented.

## Remaining prerequisites and next bounded task

1. Owner/environment action: make a current localhost certificate available through an already authorized trust path, with a valid chain/SAN/date in the actual browser. No system trust installation or new credential/account action is authorized here.
2. Codex can then recreate the small documented Python environment, verify dependency versions, manifest/PIN/tree hashes, schema and process guards, and start exactly one worker on4194 against the named rehearsal DB. Serve only the reader directory; never the whole private release.
3. Reuse this gateway build. With exclusively fictional files, replay unit1 fresh case → intentionally missing/wrong evidence → correction → criterion feedback; opt in, save and reload a draft; export and inspect the unsubmitted practical/note. Record sources, network destination, bytes/hash, restore behavior and pending-review/no-completion flags. Opt-in browser storage is separate from bytes transmitted to the local evaluator. Stop only owned processes.
4. Manual keyboard/screen-reader/zoom/mobile/low-bandwidth review and instructor rehearsal remain owner-only acceptance. Automated tests cannot pass these gates.

**Next engineering task:** restore only the retained rehearsal prerequisites and complete that one source-bound workshop journey; stop at private evidence and defect reporting. No product implementation or production rollout is needed to resolve this reproduction blocker. Any subsequent PR set must preserve curriculum33a1018 → platform c7d1aef behavior → workshop18efa764/site integration, with target-main reconciliation and review still pending.

Free space at preflight: approximately **2.2 GiB**, falling to approximately **1.0 GiB** at close; both are below the **18 GiB heavy-export guard**. No heavy export/build, cleanup, pruning or source/backup deletion occurred. Capacity provisioning remains an owner action before heavy builds.

## October 23 assessment and control-plane continuity

Full V1 is not supportable as ready from current evidence: the 16-component acceptance gaps in the existing campaign remain open, including full scientific Archive coverage, complete WAIKE18-track delivery, physical devices, real games/parties/privacy, rights/accessibility and explicit owner acceptance. Four days is a target window, not evidence that these gates can be met. RC2 stays unfrozen.

Path B remains a separately scoped, **unapproved** engineering demonstration option. The gateway and historical bounded workshop results do not authorize a public or commercial workshop, full LMS acceptance, new outcomes or V1/RC2 publication. Use only separately authorized demonstration scope and truthful limitations.

This addendum and the missing owner worksheet row are local review work. Rolling revision2, its hashed evidence, the canonical16 manifest and all23 locked October9 files are untouched. Subsequent accepted progress belongs in a new board revision/evidence directory (v0003), linked to these source-bound observations; never rewrite v0002 or the dated October9 snapshot. No pending gate becomes true. Existing inherited site passes remain historical. RC1 history, private editions and Anime #122 → #123 dependencies are preserved.

Validation: unchanged ledger, snapshot-adoption and October19 campaign validators PASS; seven portfolio tests and supervisor validator PASS; diff checks PASS. See the adjacent evidence and checksums. No push, merge, deploy, publish, tag, approval or workflow execution was performed.
