# PR #19 production verification

PR #19 was marked ready, passed CI on `42ced4bc427cdbddead7b3e67aa8ef6c67b23574`, and merged normally at `3a46b0eb74eab7e41a4960fd5f6621c9d1c7170e`. The exact merged main was built and deployed from this clean detached checkout. The existing `gunnchos-site` Worker is active at 100% on version `d6da71fd-ee12-45c7-a8db-d4f4364312ca`.

[Production](https://gunnchos.com) · [Contact](https://gunnchos.com/contact) · [noindex version preview](https://d6da71fd-gunnchos-site.gunnchos-finds.workers.dev) · [PR #19](https://github.com/gunnchOS3k/gunnchos-site/pull/19)

[Production verification record](production-verification.json) and [web audit](web-verification.json) record 15 landing pages and six 390px/320px checks. Homepage, My Home, Research, Devices, Play, Campus/WAIKE, Gallery, Status, and all other requested major landings passed. Search identity is unique; production canonicals/social URLs, JSON-LD, sitemap, robots, icon/social assets, production indexability, and fallback/version-preview noindex passed. Contact shows the active public `hello@gunnchos.com` mailto channel with all requested inquiry categories and no obsolete disclaimer. Mailbox delivery was confirmed by the owner; this verification did not send email.

The canonical JPEG is byte-identical to the supplied 278×252 RGB source. Its full artwork is shown at 34px width in the header, the opaque icons only downscale, and the social canvas places the JPEG at its native size. A higher-resolution transparent canonical logo is a non-blocking future asset-quality improvement. No upscaling, cropping, reconstruction, AI redraw, or fabricated transparency was performed.

[Homepage](homepage-desktop.png) · [My Home](home-desktop.png) · [Contact](contact-desktop.png) · [Contact at 390px](contact-390.png) · [Contact at 320px](contact-320.png) · [Social card](social.png). Desktop screenshots for each audited landing and mobile/narrow screenshots for homepage, My Home, and Contact are saved alongside this report.

Typecheck, lint (two existing warnings), focused SEO unit tests, secret scan, Cloudflare configuration, and Next/OpenNext builds passed. CI: 74 unit passes / one opt-in remote skip; 70 browser passes / 12 intentional skips. Focused local browsers: 15 passes / three intentional skips. Production unchanged Passport suite: eight passes, including QR decoding, direct lenses/event card, share fallback, closed Wallet, private-data exclusion, vCard privacy, keyboard focus, safe-area layout, and accessibility. [Passport result](passport-results.json); screenshots are in `passport/`. All five [closed-surface checks](closed-surfaces.json) passed.

`V1_SITE_HUMAN_TASTE_PASS=true` is recorded after successful production verification, based on the owner's explicit approval. Historical pre-approval artifacts retain their original false values. No other gate is inferred. DNS was unchanged; RC2/V1 remains unpublished; paused product engineering remains paused. This report is local post-deployment evidence, not a new source commit or release publication.

[Owner-only search-engine handoff](../../docs/SEO_LAUNCH_CHECKLIST.md). Search Console ownership, sitemap submission, indexing requests, and external validator checks remain owner-only manual steps; no account action is claimed.
