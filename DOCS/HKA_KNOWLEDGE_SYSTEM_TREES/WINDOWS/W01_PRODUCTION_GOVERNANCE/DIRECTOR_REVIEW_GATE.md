---
title: "HKA Director Review Gate"
version: "1.1"
status: "PROPOSED REVIEW STANDARD — ARCHITECT REVIEW REQUIRED"
language: "vi"
date: "2026-09-03"
---

# HKA DIRECTOR REVIEW GATE

Director review has two primary authoring gates and a production-consistency review. It does not replace Independent Image QA.

## GATE A — Academic Program

Apply only to Window Types with academic-authoring scope.

PASS only when:

```text
[ ] exact Window Contract read
[ ] Window Type declared and applicability profile correct
[ ] mandatory branches 100% mapped
[ ] TREE/NODE/RELATION/SOURCE artifacts complete as contracted
[ ] canonical minimum node anatomy complete
[ ] Academic Coverage Audit exists and PASS
[ ] Academic QA Report exists and PASS
[ ] semantic duplicate-node count unresolved = 0
[ ] orphan/unreachable required nodes = 0 or justified
[ ] prerequisite targets exist
[ ] prerequisite-cycle check PASS or documented co-requisite exception
[ ] entry-point reachability PASS
[ ] material claim-to-source mapping adequate
[ ] unsupported high-risk claims = 0
[ ] high-risk cross-checks complete
[ ] certainty and content class classified independently
[ ] model/normative/context status not conflated with certainty
[ ] D1-D4 progression substantive
[ ] high-risk misconceptions addressed
[ ] open/debated/settled separation correct
[ ] external curriculum/classification mapping complete when contracted
[ ] unresolved material expert-review items = 0 or explicitly deferred by contract
[ ] cross-window ownership conflicts unresolved = 0
[ ] Compression Test PASS
[ ] Expansion Test PASS
```

Director may direct-fix only bounded nonmaterial defects using `DIRECTOR_FIX_PROVENANCE_TEMPLATE.md`. Material academic changes return to owner Window.

Result:

```text
DIRECTOR ACADEMIC GATE: PASS / RETURN / BLOCKED
```

## GATE B — Visual & Prompt Package

PASS only when:

```text
[ ] Academic QA PASS
[ ] every VCU traces to locked Node IDs
[ ] every material VCU/asset traces Node → Claim → Source
[ ] Academic Content Commit SHA locked
[ ] Academic Truth Pack complete per asset/candidate
[ ] certainty/content class preserved into visual handoff
[ ] misconception to prevent explicit
[ ] WHAT MUST BE SEEN explicit
[ ] WHAT MUST NOT BE IMPLIED explicit
[ ] representation disclosure explicit
[ ] required expert review cleared
[ ] every asset has one primary learning objective
[ ] unique visual job per asset
[ ] final duplicate visual-job count = 0
[ ] package is smallest sufficient canonical package
[ ] no decorative-only asset
[ ] continuity/spiral logic documented
[ ] prompt records complete
[ ] official brand references exact
[ ] manifest mapping exact
[ ] prompt hashes reproducible
[ ] batch map valid
```

IMG Unit plan is **not** a Gate B activation requirement until a canonical IMG Unit amendment is accepted.

Result:

```text
DIRECTOR VISUAL GATE: PASS / RETURN / BLOCKED
```

## GATE C — Production Consistency Review

Director checks returned production before batch submission to Independent Image QA:

```text
[ ] correct Asset IDs
[ ] complete batch snapshot
[ ] academic truth locks preserved
[ ] character identity consistent
[ ] no repeated unresolved production defect
[ ] clean/branded distinction correct
[ ] file names and hashes present
[ ] per-asset provenance complete when carry-forward applies
[ ] correction records applied
```

Director may reject production before formal QA to save time. Director review status is never `QA_APPROVED`.

## B00 mass-production gate — P0 lock

No B01+ mass production may open until:

```text
B00 DIRECTOR CONSISTENCY REVIEW = PASS
AND
B00 INDEPENDENT IMAGE QA = QA_APPROVED
```

`QA_REJECTED` or `QA_BLOCKED` keeps every B01+ production path closed. Director review alone is insufficient.

## Error handling

```text
SMALL NONMATERIAL METADATA / OBJECTIVE DEFECT
→ Director direct-fix only with provenance + new commit SHA

MATERIAL ACADEMIC DEFECT
→ owner Window correction
→ new Academic Content Commit
→ rerun affected coverage/QA
→ invalidate affected truth/visual/prompt/manifest locks

GENERATION DEFECT
→ canonical rework path / new run

PROMPT DEFECT
→ prompt correction + new prompt hash/commit

CANONICAL CONFLICT
→ BLOCK + change request/amendment
```

## Direct-fix invalidation check

For every post-lock Director edit:

```text
DIRECTOR FIX COMMIT SHA PRESENT: YES/NO
SUPERSEDES ACADEMIC CONTENT COMMIT SHA PRESENT: YES/NO
AFFECTED NODE/CLAIM/RELATION IDS PRESENT: YES/NO
SOURCE IMPACT CLASSIFIED: YES/NO
DOWNSTREAM PROMPT INVALIDATION DECIDED: YES/NO
```

## Partial rework provenance check

When a later complete Batch Run carries forward prior bytes:

```text
BATCH_ASSET_PROVENANCE RECORD COUNT = MANIFEST ASSET COUNT
ORIGIN RUN/UNIT/HASH PRESENT PER ASSET
CARRIED_FORWARD FLAG PRESENT
REVALIDATED_IN_FINAL_BATCH = YES FOR FINAL SNAPSHOT
```

Independent QA still reviews the complete final snapshot.

## W02 opening rule

W02 academic authoring may not open as an operating inheritance until:

```text
Director Layer Architect Review Round 2 = PASS
W02 exact Window Contract / Window Type = ISSUED
```

W02 image production additionally requires the applicable academic/visual gates and current canonical production authorization. Proposed IMG Unit semantics cannot activate without canonical amendment.