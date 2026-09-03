---
title: "HKA W01 Director Layer — Change Requests"
version: "1.1"
status: "OPEN ITEMS RECORDED"
---

# DIRECTOR CHANGE REQUESTS

## HKA-CR-W01-DIR-001 — Optional R2 staging plane

### Observation

Current canonical Cloudflare pipeline defines `hka-c4k-vault`, `hka-c4k-audit`, `hka-c4k-delivery` and does not authorize Production Window to upload canonical R2 objects before Independent QA.

### Director decision

```text
STAGING CONCEPT: APPROVED IN PRINCIPLE BY ARCHITECT REVIEW 01
CANONICAL STATUS: NOT ACTIVE
DO NOT SILENTLY ADD STAGING IN W01
SEPARATE CANONICAL AMENDMENT REQUIRED BEFORE AUTOMATED IMAGE PRODUCTION USE
```

### Requirements for future amendment

- staging remains non-canonical;
- least-privilege/short-lived credentials;
- immutable package SHA before QA;
- staging receipt distinct from Vault receipt;
- lifecycle/retention explicit;
- state/schema changes versioned;
- no Vault release authority for production;
- Amendment 1.1 release order preserved.

### Status

```text
OPEN — NONBLOCKING FOR W02 ACADEMIC AUTHORING
BLOCKS AUTOMATED STAGING-BASED IMAGE PRODUCTION UNTIL APPROVED
```

---

## HKA-CR-W01-DIR-002 — IMG Unit production sub-unit model

### Source conflict

Canonical pipeline currently defines one Image Production Window per batch. Director anti-drift design proposes multiple IMG Units within a batch, each max two Asset IDs.

### Architect Review 01 direction

```text
CONCEPT: ACCEPTED IN PRINCIPLE
CANONICAL STATUS: NOT ACTIVE
REQUIRED: FORMAL CANONICAL AMENDMENT BEFORE ACTIVATION
```

### Proposal

See:

```text
IMG_UNIT_CANONICAL_AMENDMENT_PROPOSAL.md
```

Proposed semantics:

```text
BATCH = manifest / complete snapshot / batch self-QA / Independent QA / release unit
IMG UNIT = generation sub-unit, max 2 assets
BATCH PRODUCTION ORCHESTRATOR = assembles all units into one complete snapshot
NO PARTIAL BATCH TO INDEPENDENT QA
```

B00 remains exactly two assets and one IMG Unit by default under the proposed model.

### Status

```text
OPEN — IMG UNIT DOCUMENTS ARE DESIGN SPECIFICATIONS ONLY
ACTIVE CANONICAL PRODUCTION REMAINS ONE PRODUCTION WINDOW PER BATCH
```

### Required decision

```text
APPROVE CANONICAL AMENDMENT / REQUEST REVISION / REJECT
```