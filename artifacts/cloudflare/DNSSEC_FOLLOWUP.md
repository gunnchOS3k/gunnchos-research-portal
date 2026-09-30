# DNSSEC follow-up

Parent DS is already published for `gunnchos.com`. This session did not change it.

After Cloudflare DNS is stable and the owner has accepted a nameserver cutover:

1. Enable DNSSEC on the Cloudflare zone.
2. Copy the DS record Cloudflare shows.
3. Add that DS at Squarespace, which remains the registrar.
4. Verify the chain from a public resolver.

Do not upload a DS automatically.
