# Additive Architecture Doctrine

**Status:** Binding doctrine for Complete Experience implementation  
**Companion to:** `GUNNCHOS3K_COMPLETE_USER_EXPERIENCE_REQUIREMENTS_V1.md`

## Principles

1. **Never remove intended capability** to “simplify.” Degrade via tiers, adapters, or declared remote paths.  
2. **Adapters and contracts** front unstable providers. Version contracts (`contracts/*_v1.json`).  
3. **One production authority per concern** — declare it; coexist with legacy adapters until migrated.  
4. **Tiers:** digital foundation → qualified provider → physical/human evidence. Do not promote tiers without evidence.  
5. **Pin safety:** Complete Experience work must not rewrite Device Lab accepted-main pins or #134/#14 sequences.  
6. **Additive drafts:** Prefer new modules/docs/schemas over mutating frozen release evidence.  
7. **Honesty:** Status values COMPLETE / PARTIAL / ABSENT / EXTERNAL_PENDING / PHYSICAL_PENDING / HUMAN_PENDING only.

## Authority separation

| Concern | Authority |
|---------|-----------|
| Complete Experience coverage & ownership | Portal `docs/complete-experience/CAPABILITY_REGISTRY.json` |
| Device Lab gate / pin freeze | Portal release-control (PR #14 lineage); Device OS #134 evidence |
| Learning curriculum SoT | `waike-research-ops` |
| Learning runtime | `gunnchos-waike-learning-platform` |
| Assistance broker (target) | `gunnchAI3k` Capability Broker contract |

## Anti-patterns

- Claiming COMPLETE from README or digital lock alone  
- Standardizing FOSS providers before compatibility matrix PASS  
- Certification claims from schema presence  
- Merging CX drafts into frozen Device Lab branches without owner decision  
