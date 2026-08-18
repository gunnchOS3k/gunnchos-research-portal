# Supervisor contact — owner action only

**Status:** `CONTACT_SUPERVISOR_READY = BLOCKED` at baseline; remains owner-gated even after automatable PASS.

This agent must not email, submit applications, or contact a supervisor.

## Smallest sequence for Edmund

1. Wait until `AUTOMATABLE_SUPERVISOR_READY = PASS` on the portal dashboard **or** consciously accept residual digital gaps.  
2. Resolve private-repo access ([REPOSITORY_VISIBILITY_PACKET.md](REPOSITORY_VISIBILITY_PACKET.md)).  
3. Send **only** the public 10-minute path:  
   `docs/phd/START_HERE_SUPERVISOR.md` in `gunnchos-research-portal`.  
4. Do not claim University of Oulu affiliation or 6G Flagship membership.  
5. Optional: attach independent reproduction records if they exist.

## Expected evidence

Owner-kept record of what was sent (not committed if it contains personal emails).

## Status transition

Contacting a supervisor does **not** set `CONTACT_SUPERVISOR_READY = PASS`. That gate is about inspectability and honesty of the public portfolio, not about a reply.
