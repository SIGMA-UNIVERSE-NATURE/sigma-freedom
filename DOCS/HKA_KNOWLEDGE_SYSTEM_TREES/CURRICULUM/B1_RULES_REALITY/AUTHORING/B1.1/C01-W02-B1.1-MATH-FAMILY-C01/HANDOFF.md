# HANDOFF — C01-W02-B1.1-MATH-FAMILY-C01 repaired child PASS

## Scope

`B1.1-C01 — Logic, tập hợp và chứng minh` only.

## Authoritative repaired commits

- Director-reopened repair input: `3c0906772ae6a356a4671d372180a0d38933fbca`
- Control-plane recheck: `262cbe8f63cb6bfda2f017313883dd15bc9ed7dc`
- Academic repair records: `24f26793d923dd55e87839331994c45489109d88`
- Academic closure checkpoint CP05: `40023f836059a7ae5a9edefa2806ffdb04edbb72`
- Pre-PASS checkpoint CP06: `a62420f15499a60cdab78c176a5c6b4a5510e0e7`

The terminal commit containing this HANDOFF/RESULT/STATUS/REPORT is the branch HEAD returned by the worker after this file is committed.

## Repair summary for independent Director audit

### 1. Propositional syntax closure

Verify N001 appended claims `C004` and `C005`: well-formed propositional formulas are constructed recursively by formation rules, and syntactic well-formedness is distinguished from semantic valuation.

### 2. Set-existence / Separation closure

Verify N003 `C004`: Separation forms a subset from an already-given set and formula; it is not unrestricted comprehension. N003 `C005` records foundational scope limits and N003 `C006` closes `∈` versus `⊆`.

### 3. Decidability boundary

Verify N008 `C005` and `C006`: decidability is defined only at the metatheory level needed by C01 and distinguished from consistency/completeness. Detailed computability, formal languages, automata, complexity and computation limits remain `B1.5-C02`.

### 4. Immutable Open Logic source

Active source: `HKA-SRC-73f520eedb8e`.

It is deterministically derived from:

`open_textbook|https://github.com/OpenLogicProject/OpenLogic/tree/1e960beff9ed7835bf3e3f1335e21af3439cd107|commit-1e960beff9ed7835bf3e3f1335e21af3439cd107`

Expected SHA-256 prefix: `73f520eedb8e`.

The old source IDs `HKA-SRC-cf3f2232b1bf` and `HKA-SRC-7ff0e7a8abe8` are retained only as `SUPERSEDED_HISTORICAL`. There must be no active claim/node reference to them.

### 5. 32/32 objective support closure

Audit artifact:

`CLAIM_TO_LEARNING_OBJECTIVE_CLOSURE.jsonl`

Expected:
- exactly 32 rows;
- exactly one row for each `LEARNING_OBJECTIVES.jsonl` record;
- all `SUPPORTED_BY_CLAIMS=true`;
- all `requires_unlocked_scope_claims=false`;
- every `supporting_claim_ids` value resolves to a committed C01 Claim ID;
- `B1.5-C02` / `B1.5-C04` may appear only in `boundary_references_not_support_claims`.

The full audit also appended minimum closure claims for FOL term/formula syntax, equivalence/function-property definitions, and proof logic versus program-verification ownership. These do not create new Learning Objectives or expand scope.

## R04

The original two `OVERLAP_REVIEW` cross-links remain authoritative:
- C01 → `B1.5-C02` for computability/formal-language/automata boundary;
- C01 → `B1.5-C04` for program verification/formal methods boundary.

`primary_ownership_transferred=false` for both.

## Expected counts

- nodes: 8
- claims: 38
- sources: 8
- learning objectives: 32
- claim-to-learning-objective closure rows: 32
- cross-links: 10
- sequence intents: 8

## Stage boundary

No B1.1-C02 content, Lesson Registry, image prompt/image, R2, delivery, website or `ACADEMIC_LOCKED` artifacts were authored.

## Acceptance gate

This child branch now reports `PASS`, but it does **not** unlock C02. The control-plane must be independently updated by the Director after verifying the repaired terminal commit. Only then may `C01-W02-B1.1-MATH-FAMILY-C02` execute.
