# C01-W02-B1.1-MATH-FAMILY-C01 — Durable Status Report

Status: `PASS`  
Stage: `CURRICULUM`  
Scope: `B1.1-C01 — Logic, tập hợp và chứng minh`  
Execution branch: `hka-tree/c01-w02-math-c01`

## Repaired child result

The Director-reopened C01 repair is complete at the child-window level. Academic repair commit: `24f26793d923dd55e87839331994c45489109d88`. Pre-PASS checkpoint: `CP06-REPAIR-PRE-PASS-AUDIT` at `a62420f15499a60cdab78c176a5c6b4a5510e0e7`.

Repaired counts: **8 nodes / 38 claims / 8 sources / 32 learning objectives / 32 claim-to-objective closure rows / 10 cross-links / 8 sequence intents**.

## Director correction order — completed

1. **Propositional foundation:** explicit sourced claims now cover recursive well-formed-formula construction and the syntax/semantics distinction.
2. **Set existence:** explicit sourced claims now cover restricted Separation from an existing set and distinguish it from unrestricted comprehension; the full audit also closed the required `∈` versus `⊆` distinction.
3. **Decidability:** explicit sourced claims define decidability at the metatheory level and distinguish it from consistency/completeness, while detailed computability, formal languages, automata, complexity and limits of computation remain owned by `B1.5-C02`.
4. **Immutable Open Logic source:** active Open Logic provenance is `HKA-SRC-73f520eedb8e`, pinned to exact `OpenLogicProject/OpenLogic@1e960beff9ed7835bf3e3f1335e21af3439cd107`. The former moving landing/build sources are historical only and have zero active claim/node references.
5. **32/32 objective support:** `CLAIM_TO_LEARNING_OBJECTIVE_CLOSURE.jsonl` contains exactly one row per Learning Objective. All 32 rows are `SUPPORTED_BY_CLAIMS=true`; none requires claims from an unlocked scope. B1.5 references are boundary references only.

The full closure audit also added the minimum claims needed for first-order term/formula syntax, equivalence/function property definitions, and the proof-logic versus program-verification boundary. No new Learning Objective or scope was created.

## Audits

`CP06-REPAIR-PRE-PASS-AUDIT` records PASS for 8/8 topic coverage, stable IDs, node fields, claim epistemics/certainty/scope/source traceability, D1–D4, immutable-source pin, 32/32 claim-objective closure, R04, semantic duplicate scan, prerequisites/sequence, stage boundary, and durable recovery state.

The control-plane was re-read immediately before pre-PASS and remained at `262cbe8f63cb6bfda2f017313883dd15bc9ed7dc`: C01 is still `REVIEW_REQUIRED` there and C02 remains locked. This child window does not alter that control-plane state.

## Boundary / next action

No B1.1-C02, Lesson Registry, image prompt/image, R2, delivery, website, or `ACADEMIC_LOCKED` artifact was authored.

The child repair result is now `PASS`, but **independent Director acceptance is still pending**. `C01-W02-B1.1-MATH-FAMILY-C02` must remain locked until that acceptance is recorded in the control-plane.
