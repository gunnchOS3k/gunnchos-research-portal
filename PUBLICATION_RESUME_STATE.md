# Publication resume state

Checkpoint: 13 October 2026 (America/Chicago). Continuation of work begun 12 October; branch names retain the original start date. Owner confirmed Edmund Gunn, Jr.; gunnchOS Research; egunnjr@gunnchos.com; ORCID 0009-0004-6546-2609.

Recovery complete before new manuscript work. The three previous agents stopped with usage-limit errors. Their useful generated files, reproduction evidence, reference metadata and helper scripts are now committed separately. Their reported scientific findings are retained in each `paper/submission/RECOVERY_NOTES.md`; these reports still require coordinating verification. No accepted-main checkout or frozen protocol was discarded.

| Paper | Repository | Branch | Recovery HEAD | Manuscript status |
|---|---|---|---|---|
| I | `7gc-digital-twin` | `publication/paper-i-owner-review-2026-10-12` | `1d83c6782ea7fdb1852c452ed6a8d7d78e33cec3` | Reproduction/figures/statistics recovered; manuscript writing pending |
| II | `spectrumx-ai-ran-gary` | `publication/paper-ii-owner-review-2026-10-12` | `4e5cc1ede31ca02cd485cc0cfd9086b1c64c1ca9` | Original + revised SLSQP runs recovered; manuscript writing pending |
| III | `ntn-resilience-sim` | `publication/paper-iii-owner-review-2026-10-12` | `4608fc7860a69eaef604d274ff57de9c12822e3e` | Partial LaTeX manuscript + figures/statistics recovered; bibliography/package pending |

## Exact local checkouts

All seven isolated checkouts are under `/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos/_publication_worktrees/`. Canonical authoring roots remain `<paper-repository>/paper/`. Dedicated author-review packages are `<paper-repository>/paper/submission/`. Original dirty checkouts under `repos/` remain untouched.

## Reproduction and citation state

- Paper I: agent reported 17 paper-reproduce tests and 27 focused tests pass; 30-seed completion/time-above-minimum report, independent statistical audit and three exported plots recovered. Citation audit and full manuscript unfinished.
- Paper II: exact original/revised non-timing SLSQP outputs recovered; agent reported original 5 and revised 31 tests pass. Both protocols, source code, legacy manuscript/bibliography, reproduced JSON, paired statistics, four plots and Crossref metadata recovered. Full prose/citation claim mapping unfinished.
- Paper III: 30-seed experiment/results, statistical audit, five plots including graphical abstract and partial manuscript recovered. Agent reported full 37 tests pass after restoring clean sibling field-kit fixtures. Bibliography metadata for five sources recovered; reference verification and full package unfinished.
- No complete manuscript PDF existed at this recovery checkpoint. Recovered PDFs are figures, not manuscripts. Legacy PDFs in the attached Oulu package are prospective previews and do not replace canonical papers.

## Scientific issues preserved

Paper I: configured synthetic priors; class mappings differ between fixtures and timeline engine; duplicate/proxy endpoints; stored recovery count represents outage entries; generalizability unproven.

Paper II: twin failed its historical superiority comparison; information access differs from consumed features; equal computational budget unproven; static feasibility and oracle/global-optimality labels overstate implementation; some ablations alter metric truth. Switching-cost break-even is post-hoc algebra. Historical and revised results must remain distinct.

Paper III: NTN favorable and harmful cases; parameters configured rather than calibrated; abstract recovery steps; common power failure; seeded local/peer modes absent; close 2026 competing simulator limits novelty. Simulation-to-measurement transfer unresolved.

## Tools and temporary assets recovered

Tectonic 0.17.0 `/private/tmp/publication-tools/tectonic` compiles standard IEEEtran. Cache `/private/tmp/publication-tools/cache`.

Official current IEEE Access template: `/private/tmp/publication-tools/ieee-access-official/ACCESS_latex_template_20260513/`.

Exact OJ-COMS selector download: `/private/tmp/publication-tools/ojcoms-official/IEEE_OJCOMS-template-LaTex_202401/` (`IEEEoj.cls`). Official selector titleId209/articleId2/fileId476. TNSM selector retrieval is at titleId82/article type.

Paper-II reproduction environments `/private/tmp/paper-ii-original`, `/private/tmp/paper-ii-revised`, `/private/tmp/paper-ii-venv`; Paper-III environment `/private/tmp/paper-iii-reproduction-env`. Useful temporary helper scripts copied to committed submission scripts. Temporary virtual environments are rebuildable and are not research evidence.

## Exact next actions

1. Recovery branches pushed normally after exact owner approval: I1d83c67, II4e5cc1e, III4608fc7, portal986a520. Continue local milestones; never force-push.
2. Resume each paper with one authoring agent, first reading recovery notes and committed evidence. Finish full substantive prose, verified bibliography, correct venue class and supporting declarations.
3. Finish official TNSM template selector download (Original research and Brief -> LaTeX -> Download).
4. Complete July-lock versus Oulu V3.1 scope reconciliation in this portal.
5. Compile with `TECTONIC_CACHE_DIR=/private/tmp/publication-tools/cache /private/tmp/publication-tools/tectonic --untrusted --keep-logs --keep-intermediates manuscript.tex` from each `paper/submission/`, then render and inspect every page.
6. Run evidence/citation/file validation, commit completed milestones, update this state and prepare draft PRs.

No active shell process is known: recorded download/compile/clone sessions completed. General OS process enumeration was denied by sandbox, so no stronger claim is made. Child agent status was inspected and all three were errored.

Owner scientific review, additional coauthors/funding/conflict/rights declarations and explicit submission authorization remain pending. No journal submission, public preprint, ORCID write or merge is authorized.

## Post-recovery checkpoint

Four approved recovery SHAs are remote. Source provenance, version1 scope reconciliation, and rights/AI/ORCID review are now saved under `docs/publication/three-paper-2026-10/`. New paper agents own one manuscript each; they read the recovered assets before writing. Exact TNSM template downloaded from selector titleId82/articleId3/fileId264 at `/private/tmp/publication-tools/tnsm-official/`. Citation discrepancies are being resolved from publisher/fulltext sources.
