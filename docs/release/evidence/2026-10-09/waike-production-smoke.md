# Exact-main production deployment and smoke

Accepted PR #27 is contained in main `2641042936f3b965daccb11091c80cbc6fa64f91`, including ancestor `c73fae5945338d28c9915024c468fc0925027e93`. Deployment used a clean detached exact-main worktree; no source changes or dirty historical worktree changes.

The existing Cloudflare assets-only Worker `waike-campus` now serves version `14883cdd-d66d-4019-a2f2-ff27ac39577c` (version 2, 100% traffic), deployed 2026-10-06 12:36:45.676 UTC at https://learn.gunnchos.com. Existing custom-domain binding, SPA behavior, compatibility date and empty bindings were preserved. No DNS, routes, auth architecture, school Hub configuration or unrelated services were changed.

Locked offline dependency install and Vite production build passed using Node 24.9.0, pnpm 9.15.9 and Vite 6.4.3. Existing return-link configuration points to https://gunnchos.com; Hub is unset, mock Hub and Pixel pilot disabled. Public HTML and JavaScript SHA-256 values match the exact-main build. Detailed hashes and provenance are in `production-smoke.json`.

All ten requested live-browser smoke checks passed: public loading; 18 discoverable tracks; authored Digital Confidence lesson; real assignment and lab instructions; truthful unavailable Grades; truthful Today/Calendar/Messages; complete Digital Confidence packaged-content surface; Grades at 390-pixel width; return navigation through gunnchOS to MLV; no WAIKE console errors. Ask gunnchAI also preserves the explicit unavailable-Hub boundary.

No obvious new production runtime defect was observed. An already-open session required a second reload after its service-worker update; fresh public HTTP artifacts matched immediately. Vite emitted its large-bundle advisory. MLV showed an existing Supabase-unconfigured banner, outside this task's change scope. Browser-width checks are not Pixel/device acceptance, and sampled lesson/lab checks are not an exhaustive human curriculum review.

Still false/open: `V1_WAIKE_HUMAN_PASS`, production school-Hub acceptance, production AI acceptance, Pixel/device acceptance, external OneRoster/QTI/LTI certification, independent security/accessibility/privacy certification, production signing/notarization.

No RC2 or V1 release was published.
