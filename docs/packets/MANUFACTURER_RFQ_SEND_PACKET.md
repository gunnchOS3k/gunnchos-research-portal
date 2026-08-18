# Manufacturer RFQ send packet

**Status:** `EXTERNAL_PENDING`

## Why blocked

RFQ **documents** may exist in the hardware repo. Sending an RFQ, purchasing parts, or placing a fab PO is an owner/external action. This agent must not send email or RFQs.

## Prerequisite

Owner-reviewed digital manufacturing packet; no invented electrical values.

## Owner action

Send via the owner’s procurement channel. Record vendor, date, and document hash **outside** or in a non-secret tracker.

## Expected evidence

Vendor acknowledgement (not to be fabricated).

## Status transition

Send ≠ manufacturing release ≠ FCC. Digital packet completeness is a separate gate (`DIGITAL_MANUFACTURING_READY`).
