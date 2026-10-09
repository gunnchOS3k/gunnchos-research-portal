# gunnchOS V1 Readiness Addendum — Cross-Platform Invites & Shared Sessions

**Status:** V1 REQUIRED  
**Applies to:** Anime Aggressors, Pedestrian Pursuit, BeatLink Party, Archive of Life, 3k MLV, Device OS  
**Release policy:** Full real-time online multiplayer for every game is **not** required for V1. The cross-platform invitation/session foundation and each title's declared V1 social action are required.

---

## 1. V1 requirement

Official gunnchOS V1 must include a shared invitation/session layer that lets a user invite another person into a game or shared experience through a normal shareable HTTPS link.

Canonical user concept:

> **gunnchOS Invites — one link to play, race, party, or explore together.**

The invitation transport may be:
- iMessage
- SMS
- RCS / Google Messages
- WhatsApp
- Discord
- Signal
- email
- QR code
- 3k MLV friends/invitations
- Device OS notifications/share surfaces

The messaging app is the invitation transport, not the multiplayer transport.

---

## 2. Shared V1 protocol

V1 must provide a common invitation contract with:

- opaque/signed invite token
- invite ID
- experience/game ID
- invite type/mode
- host identity reference
- game/content version
- rules/context payload
- created time
- expiry
- state
- max participants where applicable
- accept / decline / expired handling
- safe validation of incoming invite parameters
- no phone numbers, private messages, credentials, or raw sensitive state in the URL

Canonical link shape:

`https://play.gunnchos.com/i/<opaque-token>`

V1 must support graceful fallback:

- installed native app -> deep/app link when supported
- supported web runtime -> browser
- unavailable target -> clear install/open/help path
- expired/invalid invite -> safe error state

---

## 3. Per-title V1 social requirement

### Anime Aggressors — Challenge to Fight

V1 REQUIRED:
- create challenge
- choose or defer rules/fighter/stage context
- share invitation link
- recipient can accept/decline
- accepted invite lands at the correct Anime Aggressors challenge/lobby handoff
- rematch/share-result contract can exist where already supported
- invitation provenance/version is validated

V1 DOES NOT REQUIRE:
- production-grade global rollback matchmaking
- ranked online service
- anti-cheat service
- full cross-platform live 1v1 networking

Those may ship in V1.x after dedicated netcode validation.

### Pedestrian Pursuit — Race Me

V1 REQUIRED:
- create race challenge
- share invite
- recipient can accept
- asynchronous ghost/time challenge path is supported where technically practical
- invite carries track/rules/version/ghost reference/expiry as appropriate
- result/rematch sharing contract
- tutorial/onboarding cannot block acceptance of an invite

V1 DOES NOT REQUIRE:
- full live network racing across all platforms

Live racing may be V1.x unless already validated.

### BeatLink Party — Join My Party

V1 REQUIRED:
- create/share party invitation
- recipient can join the BeatLink room/session shell
- ready/react/vote/party-intent contract where already supported
- permitted-content boundaries remain truthful
- no claim that commercial-music rights are cleared
- no claim of live multiplayer if the room server is unavailable

V1 DOES NOT REQUIRE:
- head-to-head competition
- redistribution of unlicensed commercial music

### Archive of Life — Join My Expedition

V1 REQUIRED:
- create/share an expedition, collection, artifact, museum-tour, or discovery-challenge invitation
- recipient can open the intended Archive context
- invitation can encode a safe reference to:
  - time interval
  - taxon
  - region
  - expedition
  - collection
  - artifact
  - challenge
- provenance/source context remains intact
- no false multiplayer or scientific-completeness claim

V1 DOES NOT REQUIRE:
- PvP
- real-time synchronized multiplayer expedition

---

## 4. Ecosystem integration

### 3k MLV

V1 REQUIRED:
A visible social/invitation surface conceptually supporting:

- Fight
- Race
- Party
- Expedition

Where friends/presence are not production-ready, the UI must remain truthful and may use direct share links without pretending persistent social presence exists.

### Device OS

V1 REQUIRED:
- receive/open a valid gunnchOS invite
- route to the correct installed/browser experience
- safe fallback when the target is unavailable
- no fabricated native notification service if it is not actually connected

### iOS / Android

V1 REQUIRED:
- HTTPS invite works on both platforms
- deep-link/app-link contract exists where native packaging supports it
- browser fallback works

V1 OPTIONAL:
- dedicated iMessage extension

The iMessage extension is an enhancement over the universal invite system, not the foundation.

---

## 5. Automated acceptance gates

A V1 automated pass requires:

1. shared invite schema validates;
2. opaque/signed token path works;
3. invalid/expired/tampered invite fails safely;
4. invite does not expose sensitive data in URL;
5. each of the four experiences can generate/resolve its V1 invite type;
6. invite routing is version-aware;
7. browser fallback resolves correctly;
8. mobile deep-link/app-link manifest/config validates where applicable;
9. 3k MLV/Device OS handoff contracts validate;
10. title-specific tests pass;
11. no unsupported real-time/network capability is claimed;
12. evidence records exact source SHA and deployment/build version.

Recommended central gate names:

- `V1_INVITES_PROTOCOL_PASS`
- `V1_INVITES_ANIME_PASS`
- `V1_INVITES_PURSUIT_PASS`
- `V1_INVITES_BEATLINK_PASS`
- `V1_INVITES_ARCHIVE_PASS`
- `V1_INVITES_MLV_HANDOFF_PASS`
- `V1_INVITES_DEVICE_HANDOFF_PASS`
- `V1_INVITES_BROWSER_FALLBACK_PASS`

`V1_INVITES_FULL_PASS` may be true only when every required V1 invite gate above is true.

---

## 6. Human acceptance

Human acceptance remains separate from automation.

Owner must verify:

- invite creation is understandable;
- share action feels natural;
- received link communicates what is being invited;
- accept/decline behavior is obvious;
- the user lands in the intended game/context;
- failure states are understandable;
- the experience feels like one gunnchOS platform rather than four disconnected share links.

Owner statement:

> **V1_INVITES_HUMAN_PASS:** “I can invite someone to fight, race, party, or explore, and the experience feels coherent across gunnchOS.”

This gate must remain false until explicit owner approval.

---

## 7. Release boundary

Required for official V1:
- universal invite protocol
- text/share-sheet compatible invite links
- Anime challenge handoff
- Pursuit race/ghost challenge handoff
- BeatLink party invite
- Archive expedition/collection/challenge invite
- 3k MLV/Device OS integration contract
- browser/mobile fallback
- truthful evidence

Not required for official V1:
- full cross-platform real-time Anime netcode
- full live Pursuit multiplayer
- ranked matchmaking
- anti-cheat infrastructure
- dedicated iMessage extension
- full native social network/friends backend
- synchronous Archive multiplayer
- music-rights expansion

Those are V1.x unless separately completed and accepted before freeze.

---

## 8. Readiness-board integration

The central V1 readiness board must now include an **Invites & Shared Sessions** domain.

Official V1 cannot be authorized until:
- all required automated invite gates are green;
- invite deployment/build provenance is recorded;
- the owner completes the invite usability acceptance;
- no title overclaims unavailable networking/services.

This addendum is authoritative for V1 scope unless superseded by an explicit owner scope decision.
