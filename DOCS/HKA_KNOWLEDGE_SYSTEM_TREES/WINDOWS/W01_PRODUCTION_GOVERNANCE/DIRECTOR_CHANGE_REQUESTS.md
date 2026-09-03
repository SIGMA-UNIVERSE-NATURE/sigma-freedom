---
title: "HKA W01 Director Layer — Change Requests"
version: "1.0"
status: "OPEN ITEMS RECORDED"
---

# DIRECTOR CHANGE REQUESTS

## HKA-CR-W01-DIR-001 — Optional R2 staging plane

### Observation

Current canonical Cloudflare pipeline defines:

```text
hka-c4k-vault
hka-c4k-audit
hka-c4k-delivery
```

and does not authorize Production Window to upload canonical R2 objects before Independent QA.

A separate `hka-c4k-staging` bucket could reduce manual file handling and support scalable full-resolution QA, but adding it changes canonical R2 architecture, state transitions, credentials, receipts and likely schema.

### Director decision

```text
DO NOT SILENTLY ADD STAGING IN W01.
KEEP CURRENT CANONICAL RELEASE FLOW.
PROPOSE A SEPARATE CANONICAL AMENDMENT IF ARCHITECT WANTS STAGING.
```

### Requirements for any future staging amendment

- staging is non-canonical;
- credentials least-privilege and short-lived;
- immutable package SHA before QA;
- no Vault release authority for IMG Unit;
- lifecycle retention explicitly defined;
- staging receipt distinct from canonical Vault upload receipt;
- state/schema changes versioned;
- Vault release order in Amendment 1.1 preserved.

### Status

```text
NONBLOCKING FOR DIRECTOR LAYER.
BLOCKS ONLY AUTOMATED R2-STAGING WORKFLOW UNTIL CANONICALIZED.
```