---
title: "HKA W01 — Director Layer Execution Register"
window_id: "W01"
version: "2.0"
status: "ARCHITECT_ACCEPTED_FOR_AUTHORING"
language: "vi"
date: "2026-09-03"
---

# HKA W01 — DIRECTOR LAYER EXECUTION REGISTER

## 1. Purpose

Director Layer nối Knowledge Tree contract với academic authoring, visual direction và production handoff. Mục tiêu là để các Window làm đúng phần tri thức của mình với ít vòng lặp nhất.

## 2. Provenance

```text
REPOSITORY: SIGMA-UNIVERSE-NATURE/sigma-freedom
ARCHITECT-ACCEPTED BASELINE:
5ed62129b8eae603d9d9917ca57a46a03361c909

W01 DIRECTOR CORRECTION COMMIT:
447ce385385dea7aad20a80ad1db7bcde6428d4c

ARCHITECT FINALIZATION HEAD:
a53eead2b7a15108c1417def33f55e9305675bb9

DIRECTOR BRANCH:
hka-tree/w01-director-layer

CANONICAL BASE:
b2c6b8dacfb425c5e6d260176ed879fb75da6dae

BRAND ASSET COMMIT:
2d3aa9d8418acccd39a3d263e917d4157e029e17
```

## 3. Architect Review Round 2 decision

```text
HKA-ADR-W01-001 ... HKA-ADR-W01-011: CLOSED
CANONICAL HKA COMPASS ALIGNMENT: FIXED BY ARCHITECT
PROCESS DUPLICATION: REDUCED BY ARCHITECT
DIRECTOR LAYER AUTHORING STATUS: ACCEPTED
UNRESOLVED P0/P1 FOR W02 AUTHORING: 0
```

One reporting discrepancy was corrected at review: W01 correction diff contained 24 changed files rather than the reported 21. The three extra reference files are retained but are not mandatory per-Window steps.

## 4. Lean operating model

For a W02-like content Window, default critical path is:

```text
WINDOW CONTRACT
→ TREE / NODE / RELATION / SOURCE
→ ONE ACADEMIC QA REPORT
→ PROGRAM-TO-VISUAL BRIEF
→ PROMPTS + MANIFEST
```

Coverage matrices, separate Truth Packs, dedup registries, global ledgers and correction/provenance templates are used only when complexity or an actual defect requires them.

## 5. Active production semantics

```text
CONTENT WINDOW GENERATES IMAGES: NO
ACTIVE PRODUCTION RULE: ONE IMAGE PRODUCTION WINDOW PER BATCH
PROPOSED IMG UNIT <=2 ASSETS MODEL: NOT ACTIVE
INDEPENDENT IMAGE QA: MANDATORY
B00 DIRECTOR PASS + B00 QA_APPROVED BEFORE B01+: MANDATORY
R2 STAGING: NOT ACTIVE
```

IMG Unit and R2 staging amendments are deferred until image production is actually approaching. They do not block W02 academic/visual authoring.

## 6. W02 authorization

```text
W01 DIRECTOR LAYER: ACCEPTED FOR AUTHORING
W02 EXACT CONTRACT: AUTHORIZED TO ISSUE
W02 ACADEMIC AUTHORING: MAY OPEN AFTER CONTRACT SHA EXISTS
W02 IMAGE PRODUCTION: NOT YET AUTHORIZED
R2: NOT YET AUTHORIZED
MERGE: SEPARATE DECISION
WEBSITE: HOLD
```

## 7. Final principle

```text
WRITE THE KNOWLEDGE FIRST.
VERIFY THE KNOWLEDGE ONCE.
DESIGN ONLY THE VISUALS THAT ADD LEARNING VALUE.
DO NOT BUILD PROCEDURE FOR ITS OWN SAKE.
```