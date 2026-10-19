# DNS missing-record checklist

Nameserver cutover was not prepared as `READY_TO_CHANGE_NAMESERVERS`. Cursor did not change Squarespace or Cloudflare DNS.

Still required before any owner nameserver change:

1. Export the full Squarespace / Google Domains zone, not only the records found by public query.
2. Retain the complete `google._domainkey.gunnchos.com` TXT value and confirm there is no second DKIM selector.
3. Confirm whether any Google verification TXT, CAA, SRV, or forwarding record exists outside the queried names.
4. Plan the existing DNSSEC DS (`41024 8 2 A06E615E40B22ADB1DF32E45E164C68E85D461262AFD65C41313B82951DFAE6E`) with the registrar. Do not cut nameservers while DNSSEC is active unless Squarespace's own flow disables it first.
5. Create the Cloudflare Free zone only after `wrangler login` or the official Cloudflare plugin OAuth. Do not paste an API token into chat.
6. Copy MX and SPF exactly. Do not enable Cloudflare Email Routing. Do not invent DMARC.

Observed and accounted for: Google MX, apex SPF, DKIM name presence, no apex A, no www, no DMARC.
