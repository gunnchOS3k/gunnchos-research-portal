# Codex Task — Archive of Life V1: All Time Periods + All Known Life Coverage Architecture

Work only in `gunnchOS3k/archive-of-life-artifact-world`.

Expected accepted main at task start:
`23ce4dafc2711449cab43a5bb6f42698c61ed2a1`

## Owner V1 scope decision

Archive of Life V1 is no longer allowed to stop at sample taxa or sample time coverage.

The V1 intent is:

**the full temporal backbone and all known life represented through authoritative, versioned scientific sources, with searchable/browsable access, provenance, uncertainty, and honest completeness metrics.**

This is a data-backed atlas requirement, not a requirement to hand-author millions of species pages.

Do not claim science is literally complete. "All known life" means all records covered by the pinned authoritative source snapshots used by V1, with explicit source-version coverage metrics and known gaps.

## Required source architecture

Use source adapters with pinned versions/licensing/provenance.

At minimum evaluate and integrate the appropriate combination of:

### Geological time
- International Commission on Stratigraphy (ICS) International Chronostratigraphic Chart
- every applicable eon / era / period / epoch / age in the pinned V1 chart

### Extant / taxonomic coverage
- Catalogue of Life as the primary authoritative species checklist snapshot
- GBIF taxonomic/species services where useful
- Open Tree of Life for broad tree/taxonomy relationships
- Encyclopedia of Life for trusted species/trait context where licensing permits

### Fossil/extinct coverage
- Paleobiology Database or another authoritative fossil-occurrence source
- source IDs, age ranges, uncertainty, and provenance

Do not copy external content whose license does not permit it. Prefer source IDs, licensed fields, API-backed metadata, citations, and attribution.

If the owner means cosmic time before Earth as well, implement that as a separately sourced "cosmic prelude" rather than mislabeling it as ICS geological time.

## Completion model

V1 completion must be measurable.

Create an evidence model such as:

- `ICS_TIME_UNITS_INDEXED / ICS_TIME_UNITS_IN_PINNED_RELEASE`
- `COL_ACCEPTED_TAXA_INDEXED / COL_ACCEPTED_TAXA_IN_PINNED_RELEASE`
- `COL_SYNONYMS_INDEXED`
- `EXTINCT_TAXA/FOSSIL_OCCURRENCES_INDEXED`
- source snapshot IDs / dates / DOIs
- unresolved records
- failed imports
- license/provenance status
- stale-source age

Do not use a hand-picked sample as the denominator.

## Product UX

Archive of Life should remain playable/explorable, but the knowledge layer must support:

- timeline browse from earliest covered period to present;
- taxonomic/tree browse;
- search by common/scientific name;
- extinct/extant filters;
- time filters;
- geography filters where source evidence exists;
- provenance/source panel;
- uncertainty labels;
- related taxa / lineage navigation;
- artifact/expedition links back into the game;
- mobile-safe progressive loading.

Do not attempt to render millions of records at once. Use indexes, pagination, lazy loading, caching, and progressive disclosure.

## Existing game

Preserve the existing:
- museum hub
- expedition regions
- quests/minigames
- Lifeling
- ArchiveDex
- Time Atlas
- coverage dashboard
- ingestion pipeline

Expand the data layer without destroying the game.

## Full-Earth temporal maps

The repo currently has explicit map/source gates. Close what is automatable with authoritative sources and keep unavailable measurements unavailable.

Do not fabricate NASA/regional measurements or temporal Earth maps.

## Validation

Run all current audits and add full-source coverage audits:
- typecheck
- data
- coverage
- ArchiveDex
- maps
- implementation
- release
- source validation
- source audit
- build
- pipeline
- production scientific readiness

Create deterministic fixtures for CI, but distinguish fixtures from real source snapshots.

## Human/external gates

External dataset acquisition/licensing/download availability may remain blockers.

Human playtest remains separate.

## Final report

Return:
- pinned source releases
- coverage counts/percentages
- complete time-unit coverage status
- known-life coverage status
- extinct/fossil coverage status
- import failures
- provenance/license matrix
- product UX changes
- remaining external blockers
- exact V1 readiness state

Do not call Archive "complete" while it is still sample-only.
