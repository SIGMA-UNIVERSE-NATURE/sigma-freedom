---
title: "HKA Director Review Gate"
version: "1.0"
status: "PROPOSED REVIEW STANDARD"
language: "vi"
date: "2026-09-03"
---

# HKA DIRECTOR REVIEW GATE

Director review có hai cổng chính và một review production nhanh. Không thay Independent Image QA release gate.

## GATE A — Academic Program

PASS chỉ khi:

```text
[ ] exact Window Contract read
[ ] mandatory branches 100% mapped
[ ] excluded scope respected
[ ] TREE.md complete
[ ] NODE_CATALOG.md complete
[ ] RELATION_CATALOG.md complete
[ ] SOURCE_REGISTER.md complete
[ ] core prerequisites connected
[ ] D1-D4 progression substantive
[ ] high-risk misconceptions addressed
[ ] controversies/open questions separated from settled claims
[ ] ownership/cross-tree links explicit
[ ] unsupported high-risk claims = 0
```

Director được sửa trực tiếp lỗi nhỏ, khách quan. Material academic rewrite trả đúng section về owner Window.

Result:

```text
DIRECTOR ACADEMIC GATE: PASS / RETURN / BLOCKED
```

## GATE B — Visual & Prompt Package

PASS chỉ khi:

```text
[ ] every VCU traces to locked nodes
[ ] every asset has one primary learning objective
[ ] package count justified
[ ] no decorative-only asset
[ ] continuity/spiral logic documented
[ ] prompt records complete
[ ] official brand references exact
[ ] manifest mapping exact
[ ] prompt hashes reproducible
[ ] batch map valid
[ ] IMG unit assignments max 2 assets
[ ] B00 assignment exactly 2 assets
```

Result:

```text
DIRECTOR VISUAL GATE: PASS / RETURN / BLOCKED
```

## GATE C — Production Consistency Review

Director checks each returned IMG Unit before batch is submitted to Independent Image QA:

```text
[ ] correct Asset IDs
[ ] character identity consistent
[ ] no repeated production defect
[ ] academic scene requirement met
[ ] clean/branded distinction correct
[ ] file names and hashes present
[ ] correction register applied
```

Director may reject a generation before formal QA to save time.

Director review status is not `QA_APPROVED`.

## Error handling

```text
SMALL METADATA / CONTROLLED POST-PRODUCTION DEFECT
→ Director fixes directly if authorized and rehashes affected package.

GENERATION DEFECT
→ fresh IMG Unit / new run path.

PROMPT DEFECT
→ Window prompt correction + new prompt hash/commit.

CANONICAL CONFLICT
→ BLOCK + change request.
```

## W02 opening rule

No W02 production until:

```text
Director Layer Architect Review = PASS
W02 Director Academic Gate = PASS
W02 Director Visual Gate = PASS
B00 execution pack = LOCKED
```