# gunnchOS Ecosystem Constitution, Product Doctrine, and Design Bible
**Living doctrine — current state + intended future state**

## Purpose

This document is the philosophical and product authority for the gunnchOS ecosystem.

It exists to preserve:
- the reason each product exists;
- the user experience it is supposed to create;
- the boundaries between the products;
- the things that are allowed to evolve;
- the things that must never be lost;
- the difference between current implementation and future vision;
- the meaning behind scope that has accumulated over time.

The release-control pack answers:

> What must be finished, validated, deferred, or accepted for v1.0.0?

This doctrine answers:

> What is gunnchOS supposed to be, and how should every future decision preserve that identity?

---

# I. The North Star

gunnchOS is not intended to be a collection of unrelated apps.

It is a **coherent personal, educational, creative, research, social, and recreational computing world** that can follow a person across devices, operating systems, learning environments, workspaces, and shared experiences.

The ecosystem should make advanced technology feel understandable, useful, and personal whether the user is:
- a child;
- a student;
- a teacher;
- a non-technical adult;
- a technical professional;
- a researcher;
- a developer;
- a gamer;
- a creator;
- an institution;
- a community.

The long-term idea is that the user should not need to understand the implementation boundaries to understand the product.

A visitor should experience:

```text
gunnchOS
   ↓
3k MLV
   ↓
Home · Campus · Gallery
   ↓
Learning · Work · Creation · Games · Research · Community
```

not:

```text
repository A
repository B
website C
APK D
research demo E
```

Implementation may be modular.

The experience should feel unified.

---

# II. Canonical Architecture Principle

The canonical architecture is:

```text
USER
  ↓
3k MLV WORLD SHELL
(Home · Campus · Gallery)
  ↓
WAIKE · Games · gunnchAI · Research · Media · Workbench
  ↓
HOST CAPABILITY ADAPTER
  ↓
HOST OS
(gunnchOS / Windows / Linux / Android / macOS / validated future hosts)
  ↓
HARDWARE
```

The governing principle is:

> **3k MLV is the portable world. gunnchOS is the deepest first-party host. The Hardware Quartet is the first-party physical expression of that world. Third-party operating systems and hardware may enter through validated compatibility layers.**

No future architecture change should casually collapse these layers.

---

# III. The Three Places

## Home

Home is the user's private/personal space.

It represents:
- identity;
- private work;
- media;
- rest/logoff;
- personal games;
- personal creation;
- unfinished work;
- personal devices;
- approved sharing.

Canonical spaces include:
- bedroom / logoff;
- office / desk / workbench;
- media room;
- personal files and creations;
- friends/visitors.

**Privacy doctrine:** granting someone access to Home does not grant access to all private files. A visitor sees only content the owner explicitly makes shareable.

The user's Home is not a social-media profile pretending to be private.

It is a private computing space that can expose selected surfaces.

## Campus

Campus is the learning, research, collaboration, and institutional space.

Campus connects:
- WAIKE;
- courses;
- assessments;
- labs;
- groups;
- instructors;
- portfolios;
- research environments;
- 7GC campuses;
- institutional tools.

Campus should make learning feel like a place the user enters, not merely a list of assignments.

## Gallery

Gallery is the public/shared creative space.

It is where approved work becomes discoverable.

Gallery can hold:
- projects;
- games;
- art;
- technical demos;
- portfolios;
- research;
- educational creations;
- public artifacts.

Gallery is not allowed to expose private Home content without explicit user action.

---

# IV. Product Philosophy

## 1. One ecosystem, many surfaces

Separate repositories, services, and domains may exist.

They are implementation boundaries, not user-facing fragmentation.

## 2. Complexity should be underneath, not in front

Advanced systems may be sophisticated internally.

The user's experience should stay comprehensible.

## 3. The ecosystem should teach itself

A user should be able to move from curiosity to understanding.

Interfaces, docs, labs, diagrams, walkthroughs, and contextual help should reveal how the system works.

## 4. Learning, work, and play are not enemies

The same environment can support:
- school;
- technical creation;
- research;
- employment;
- games;
- media;
- social use.

The user should not have to buy into separate computing identities for each part of life.

## 5. Continuity matters

A user should be able to move between:
- desk;
- handheld;
- mobile;
- dual-screen;
- wearable;
- third-party host;
- public display;

without losing identity or unnecessarily relearning the interface.

## 6. Personal computing should remain personal

Private work stays private by default.

Sharing is explicit.

Identity should travel without exposing everything.

## 7. Digital equity is a product requirement

Affordability, accessibility, offline operation, understandable interfaces, and lower barriers to technical knowledge are not marketing themes.

They are design requirements.

## 8. Evidence must match claims

Digital success does not imply physical certification.

Automation does not imply human enjoyment.

Simulation does not imply field validation.

Ingestion does not imply scientific completeness.

A build does not imply final art.

## 9. Human judgment remains part of quality

Some things cannot be reduced to CI:
- fun;
- feel;
- readability;
- final art;
- teaching quality;
- scientific review;
- accessibility lived experience;
- ergonomic comfort.

## 10. Scope may expand, identity should not drift

New features are welcome when they deepen the ecosystem's purpose.

New features should not turn it into an incoherent collection of demos.

---

# V. Ecosystem Components

## 3k MLV
**Role:** the portable world and user-facing shell.

**Now:** Home/Campus/Gallery architecture, shared world, social and application surfaces, host-neutral direction, 7GC environments, public deployment work.

**Future:** the persistent world through which the user reaches most of the ecosystem regardless of host device.

## WAIKE
**Role:** the native learning system.

**Now:** LMS capabilities, assessments, labs, offline/sync, identity/security, curriculum integration, standards work.

**Future:** a learning operating environment where curriculum, mastery, labs, portfolios, AI support, collaboration, and devices work together without feeling like disconnected institutional software.

## gunnchAI
**Role:** intelligence layer for students, instructors, creators, operators, and the ecosystem itself.

**Now:** tutoring/instructor workflows, digital evaluation, WAIKE integration.

**Future:** a contextual assistant that can participate deeply in learning and creation while respecting privacy, user agency, educational rules, and evidence boundaries.

## Device OS
**Role:** first-party operating system/service layer and capability host.

**Now:** Android Capsule, host adapters, cross-app continuity, security/update/recovery systems.

**Future:** the deepest integration path for the world shell, devices, AI, learning, games, networking, and first-party hardware.

## Hardware Quartet
**Role:** the first-party physical forms of the ecosystem.

- Student 14.5 — desk/shared-learning computer
- Handheld Hybrid — portable/docked personal computing and games
- DS-XL Coder — dual-screen creation/research system
- Edge I/O Rings — embodied/spatial input layer

**Now:** digital engineering and prototypes/concepts.

**Future:** validated physical products.

## Games
Games are not isolated entertainment side-projects.

They are:
- product-quality experiences;
- testing grounds for interaction systems;
- social systems;
- animation/game-feel labs;
- data/AI/security learning surfaces;
- expressions of the ecosystem.

## 7GC / Research
**Role:** global validation and research fabric.

**Now:** digital twins, AI-RAN, NTN, beam selection, resilience, measurement, field-kit architecture.

**Future:** a validated experimental network spanning simulation, digital twins, devices, edge systems, and real-world measurements.

---

# VI. The Product Should Feel Like One World

The user should be able to understand the ecosystem as:

```text
HOME
personal life
private work
media
personal games
creation

CAMPUS
learning
labs
research
collaboration

GALLERY
public work
community
shared creations
discoverability
```

Games, WAIKE, research, AI, and devices should appear within this model rather than fighting it.

---

# VII. Privacy Constitution

1. Private by default.
2. Sharing must be intentional.
3. Home access is not file-system access.
4. Friend access reveals only owner-approved content.
5. Shared/lab devices must preserve user separation.
6. Institutional roles do not automatically imply unrestricted personal access.
7. AI should not silently cross privacy boundaries.
8. Public Gallery publishing is a deliberate transition from private to shared.
9. Logs/telemetry must have purpose and bounded access.
10. Physical/biometric/spatial input demands stronger privacy discipline, not weaker discipline.

---

# VIII. Compatibility Constitution

The ecosystem should seek broad compatibility without making dishonest universal claims.

The correct language is:

```text
SUPPORTED
PARTIALLY SUPPORTED
VALIDATED
EXPERIMENTAL
NOT YET VALIDATED
```

not:

```text
works on everything
```

Host compatibility is measured, published, and improved.

---

# IX. Learning Constitution

Learning should:
- work offline where practical;
- connect theory to real artifacts;
- allow beginners to understand what experts are doing;
- support mastery rather than only submission;
- preserve portfolios and evidence of work;
- connect curriculum to devices, software, games, networking, and research;
- let the learner inspect systems instead of treating technology as magic.

WAIKE should not become a prettier clone of Canvas/Brightspace/Blackboard.

It should learn from those systems while remaining native to the world.

---

# X. Game Constitution

Every game must:
- feel like a real game, not a technical demo;
- have a recognizable identity;
- make important state readable;
- preserve consistent input and feedback;
- support human validation;
- avoid hiding weak interaction under visual effects;
- respect rights;
- support the ecosystem's social and device philosophy.

PartyLink principle:

> **Controllers are personal. The match is shared.**

---

# XI. Research Constitution

Research artifacts must distinguish:
- simulation;
- synthetic evaluation;
- digital twin;
- emulation;
- prototype;
- field measurement;
- operator deployment;
- carrier certification.

No level may silently stand in for another.

Digital equity remains part of the research mission, not merely a deployment afterthought.

---

# XII. Public Web Constitution

`gunnchos.com` should make the ecosystem legible to a person who has never seen the GitHub organization.

Subdomains are implementation boundaries.

The user experience should still feel coherent.

The public web should provide:
- a front door;
- a way to play;
- a way to learn;
- a way to understand the devices;
- a way to explore research;
- a way to view public work;
- a way to give feedback;
- a way to understand what is real now and what is future work.

---

# XIII. Release Constitution

A feature is not complete because:
- code exists;
- a PR merged;
- a test passed;
- a screenshot exists;
- AI said it is complete.

Completion depends on the evidence class.

Examples:
- build → digital build evidence;
- Pixel → physical-device evidence;
- gameplay feel → human evidence;
- final art → owner/art review;
- scientific truth → qualified review;
- certification → external authority.

Owner controls final merge/release authorization.

---

# XIV. Future State

The long-term ecosystem should allow a user to:

1. create an identity;
2. enter 3k MLV;
3. maintain a private Home;
4. learn through Campus/WAIKE;
5. use gunnchAI contextually;
6. create games, software, research, art, and technical work;
7. publish selected work into Gallery;
8. play locally or socially;
9. move across first-party and validated third-party devices;
10. participate in research and community systems;
11. understand how the systems beneath the experience work.

The product should grow without requiring the user to abandon their world.

---

# XV. Final Decision Principle

When future contributors disagree, ask:

> Does this make the world more coherent, more understandable, more useful, more personal, more accessible, more truthful, and easier to move through?

If not, the feature may be technically impressive but philosophically wrong for gunnchOS.
