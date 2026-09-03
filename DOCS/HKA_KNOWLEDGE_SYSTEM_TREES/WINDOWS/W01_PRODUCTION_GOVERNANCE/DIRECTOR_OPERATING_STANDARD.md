---
title: "HKA Director Operating Standard"
version: "1.1"
status: "PROPOSED REFERENCE — ARCHITECT REVIEW REQUIRED"
language: "vi"
date: "2026-09-03"
applies_by_window_type: true
---

# HKA DIRECTOR OPERATING STANDARD

## 1. Mission

Director Layer exists to make later Windows complete assigned work with minimum rework while preserving canonical academic, visual and release controls.

For content-authoring Window Types:

```text
WINDOW CONTRACT
→ EXACT KNOWLEDGE SCOPE
→ COMPLETE ACADEMIC PROGRAM
→ ACADEMIC COVERAGE AUDIT
→ ACADEMIC QA REPORT
→ DIRECTOR ACADEMIC GATE
→ PROGRAM-TO-VISUAL BRIEF + TRUTH PACKS
→ PROMPT PACKAGE / MANIFEST LOCK
→ CANONICAL PRODUCTION MODEL
→ DIRECTOR CONSISTENCY REVIEW
→ INDEPENDENT IMAGE QA
→ CANONICAL RELEASE PIPELINE
```

Window applicability is defined by `WINDOW_TYPE_APPLICABILITY_STANDARD.md`, not by numeric range alone.

## 2. Window Types

Every Window Contract must state one profile:

```text
FOUNDATION / ROOT / METHOD WINDOW
DOMAIN / DISCIPLINE CONTENT WINDOW
CROSS-DOMAIN HUB WINDOW
SYSTEM QA / INTEGRATION WINDOW
```

Full academic-authoring workflow is expected mainly for applicable W02–W60 content windows. W61–W64 are not presumed curriculum-authoring windows; their exact system QA/integration contracts control.

## 3. Ownership

### Applicable Content Window

Owns the complete program within assigned scope:

- reads exact contract;
- authors required TREE/NODE/RELATION/SOURCE artifacts according to Window Type;
- creates durable Academic Coverage Audit and Academic QA evidence;
- authors visual coverage and prompts only if visuals are in scope;
- never generates images.

### W01 Director

Owns cross-window consistency and gates:

- scope/ownership completeness;
- node/graph integrity;
- claim/source fitness and epistemic boundaries;
- D1–D4 progression;
- Program→Visual truth transfer;
- visual deduplication/package economy;
- prompt executability;
- production consistency review;
- bounded direct fixes with provenance.

Director does not silently change canonical architecture.

### Production

Until canonical amendment approval, active semantics remain **one Image Production Window per batch**.

The proposed anti-drift IMG Unit design is documented separately and is not active solely because Director Layer exists.

### Independent Image QA

Remains a mandatory independent batch release gate. Director review never substitutes for `QA_APPROVED`.

## 4. Director review philosophy

```text
SMALL / OBJECTIVE DEFECT
→ DIRECTOR FIX ONLY WITH DIRECTOR_FIX_PROVENANCE RECORD

MATERIAL ACADEMIC DEFECT
→ RETURN EXACT AFFECTED SECTION TO OWNER WINDOW
→ NEW ACADEMIC CONTENT COMMIT
→ RE-RUN AFFECTED COVERAGE/QA/DOWNSTREAM LOCKS

SYSTEMIC / CANONICAL CONFLICT
→ BLOCK / CHANGE REQUEST
```

## 5. Content Window Definition of Done

Applicable content window may enter Program-to-Visual only when:

- mandatory branch coverage = 100%;
- durable Academic Coverage Audit = PASS;
- Academic QA Report = PASS;
- node anatomy meets canonical minimum;
- semantic duplicate-node issues resolved;
- prerequisite graph valid/reachable;
- material claims have stable claim-to-source mappings;
- certainty and content class remain separate;
- unsupported high-risk claims = 0;
- D1–D4 progression substantive;
- ownership conflicts = 0;
- unresolved material expert-review items = 0 or explicitly handled by contract.

## 6. Visual package Definition of Done

Before prompt lock:

- every VCU traces to node→claim→source;
- Academic Truth Pack exists per asset/candidate as required;
- truth locks, forbidden implications and representation disclosure are explicit;
- duplicate visual jobs are removed/reused;
- package is the smallest sufficient canonical package;
- prompt is sufficient for Production without academic inference.

## 7. Production sequencing

B00 is the calibration gate.

No B01+ mass production opens until:

```text
B00 DIRECTOR CONSISTENCY REVIEW = PASS
AND
B00 INDEPENDENT IMAGE QA = QA_APPROVED
```

`QA_REJECTED` or `QA_BLOCKED` keeps later production closed.

## 8. Proposed IMG Unit model

The design:

```text
IMG UNIT = generation sub-unit, proposed max 2 assets
BATCH = complete snapshot / self-QA / Independent QA / release unit
```

is **PROPOSED ONLY** pending canonical amendment. See `IMG_UNIT_CANONICAL_AMENDMENT_PROPOSAL.md`.

Until amendment acceptance, Window Contracts must not authorize multiple IMG Units as active canonical production semantics.

## 9. Director direct-fix provenance

Any post-lock Director edit must record:

```text
DIRECTOR FIX COMMIT SHA
SUPERSEDES ACADEMIC CONTENT COMMIT SHA
AFFECTED NODE/CLAIM/RELATION IDS
SOURCE IMPACT
DOWNSTREAM INVALIDATION
```

If material claim, prerequisite, source, learning objective, scope/ownership or visual learning job changes, Director must return the affected section to owner Window and downstream locks are invalidated as required.

## 10. Partial rework provenance

When accepted bytes are carried into a later complete Batch Run snapshot, every Asset ID records origin run/unit/hash and carry-forward/revalidation fields according to `BATCH_ASSET_PROVENANCE_TEMPLATE.md`.

Independent QA reviews the complete final snapshot, including carried-forward bytes.

## 11. Director master principle

```text
EXACT CONTRACT DEFINES WINDOW TYPE.
ONE OWNER WINDOW OWNS EACH CONTENT SCOPE.
ONE DIRECTOR OWNS CROSS-WINDOW CONSISTENCY.
INDEPENDENT IMAGE QA OWNS FINAL IMAGE APPROVAL.
CANONICAL CHANGES REQUIRE CANONICAL AMENDMENT.
```

Throughput is achieved by clear ownership and bounded correction, not by bypassing gates.