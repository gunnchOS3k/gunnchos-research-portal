# Quality, Acceptance, Release, and Truth Doctrine

## Core principle

> **A claim must be no stronger than its evidence.**

## Evidence classes
- digital/unit;
- integration;
- end-to-end;
- device;
- human;
- physical;
- scientific;
- legal/rights;
- regulatory;
- vendor/manufacturing.

## Non-equivalences
- merged ≠ validated
- CI green ≠ fun
- model loads ≠ final art
- APK builds ≠ Pixel passes
- simulation ≠ field
- digital hardware ≠ EVT
- data ingestion ≠ scientific completeness
- API integration ≠ rights clearance

## Exact-head principle
Release evidence should name the exact source SHA whenever possible.

## Owner authority
Automation may recommend.

Owner controls:
- final art;
- final feel;
- scope freeze;
- merge authorization;
- final release authorization.

## Scope-creep principle
Nothing gets lost.

New ideas must receive a disposition rather than silently expanding the current release.

## WIP principle
Final pushes benefit from bounded parallelism.

Too many active lanes reduce truth and increase stale evidence.
