---
title: "HKA Director Review Gate"
version: "1.2"
status: "ARCHITECT FINALIZED REFERENCE"
language: "vi"
date: "2026-09-03"
---

# HKA DIRECTOR REVIEW GATE

Director review có hai authoring gates và một production-consistency review. Không thay Independent Image QA.

## GATE A — Academic Program

Apply only to Window Types with academic-authoring scope.

PASS only when:

```text
[ ] exact Window Contract read
[ ] Window Type correct
[ ] mandatory branches 100% mapped
[ ] TREE/NODE/RELATION/SOURCE artifacts complete as contracted
[ ] canonical minimum node anatomy complete
[ ] Academic QA Report exists and PASS
[ ] Academic QA contains or links adequate coverage/graph/source evidence
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
[ ] program economy / redundancy check PASS
```

A separate `ACADEMIC_COVERAGE_AUDIT` file is optional if the same durable evidence is already in Academic QA.

Director may direct-fix only bounded nonmaterial defects with provenance. Material academic changes return to owner Window.

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
[ ] truth metadata complete per asset/candidate
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

Truth metadata and dedup evidence may be embedded in `PROGRAM_TO_VISUAL_DIRECTOR_BRIEF.md`; separate files are not required unless useful.

IMG Unit plan is not a Gate B activation requirement until a canonical IMG Unit amendment is accepted.

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
[ ] correction records applied when applicable
```

Director may reject production before formal QA to save time. Director review status is never `QA_APPROVED`.

## B00 mass-production gate

No B01+ mass production may open until:

```text
B00 DIRECTOR CONSISTENCY REVIEW = PASS
AND
B00 INDEPENDENT IMAGE QA = QA_APPROVED
```

`QA_REJECTED` or `QA_BLOCKED` keeps every B01+ production path closed.

## Error handling

```text
SMALL NONMATERIAL DEFECT
→ bounded direct-fix with provenance

MATERIAL ACADEMIC DEFECT
→ owner Window correction
→ new Academic Content Commit
→ rerun only affected QA/downstream locks

GENERATION DEFECT
→ canonical rework path / new run

PROMPT DEFECT
→ prompt correction + new prompt hash/commit

CANONICAL CONFLICT
→ BLOCK + change request/amendment
```

Do not rerun unaffected gates or rewrite unaffected files.

## W02 opening rule

W02 academic authoring may open when:

```text
Director Layer Architect Review Round 2 = PASS
W02 exact Window Contract / Window Type = ISSUED
```

W02 authoring does not wait for IMG Unit or R2 staging amendments. Image production remains separately gated.