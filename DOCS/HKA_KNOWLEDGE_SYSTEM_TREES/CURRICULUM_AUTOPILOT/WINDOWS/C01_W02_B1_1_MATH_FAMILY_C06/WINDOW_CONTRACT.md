# WINDOW CONTRACT — C01-W02-B1.1-MATH-FAMILY-C06

STATUS: READY_AFTER_DIRECTOR_C04_ACCEPTANCE
STAGE: CURRICULUM
SCOPE: B1.1-C06 — Phương trình vi phân và hệ động lực
EXECUTION_BRANCH: `hka-tree/c01-w02-math-c06`
INPUT_COMMIT_SHA: `76077695c07b853ac37f058477177e211f740f17`

## Canonical topics — exact stable order

- `B1.1-C06-T01` — Phương trình vi phân thường
- `B1.1-C06-T02` — Phương trình đạo hàm riêng
- `B1.1-C06-T03` — Hệ động lực
- `B1.1-C06-T04` — Ổn định
- `B1.1-C06-T05` — Dao động
- `B1.1-C06-T06` — Phân nhánh
- `B1.1-C06-T07` — Hỗn loạn
- `B1.1-C06-T08` — Mô hình biến đổi theo thời gian

Stable topic IDs and primary ownership are fixed. Do not renumber or rename silently.

## Accepted prerequisites

- C01: logic/proof foundations.
- C02: real/complex number and arithmetic foundations.
- C03: algebra, linear algebra, eigenvalue/eigenvector and structural primitives.
- C05: limits, continuity, derivatives, integration, multivariable calculus, real/functional analysis.
- C04 is accepted and may be referenced for geometric phase portraits only where academically relevant; geometry must not become a substitute for dynamics claims.

## Required output artifacts

Under:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C06/`

- `NODES.jsonl`
- `CLAIMS.jsonl`
- `SOURCES.jsonl`
- `LEARNING_OBJECTIVES.jsonl`
- `CLAIM_TO_LEARNING_OBJECTIVE_CLOSURE.jsonl`
- `CROSS_LINKS.jsonl`
- `CURRICULUM_SEQUENCE_INTENT.jsonl`
- `RESULT.json`
- `HANDOFF.md`

Mandatory durable status folder:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/C01-W02-B1.1-MATH-FAMILY-C06/`

## Academic gates

1. Complete knowledge, minimum redundancy. Do not target a claim count.
2. Every claim must be atomic, sourced, scope-limited, epistemically classified and certainty-labelled.
3. Exactly one D1–D4 objective per node per depth; D1–D4 remain independent of age.
4. Every objective must have one effective closure row and direct support Claim IDs.
5. `future_or_locked_scope_claim_ids` must be empty for every closure row.
6. All source IDs must follow deterministic HKA SHA-256 source-ID normalization and use stable edition/DOI/ISBN identities where practicable.
7. Prerequisite graph must be acyclic and must not require locked scopes.
8. Worker PASS is candidate only. Only Director acceptance may unlock a successor.

## Mandatory ownership boundaries

- T01 owns ODE definitions, initial-value problems, existence/uniqueness conditions, solution structure and elementary qualitative behavior; C05 retains derivative/integral primitives.
- T02 owns PDE definitions/classification, boundary/initial conditions and core solution principles within a mathematically bounded scope; C05 retains multivariable/functional-analysis primitives.
- T03 owns dynamical-system state evolution, flows/maps, phase-space/orbit language and invariant-set meanings; do not duplicate generic functions/maps from C01/C03.
- T04 owns stability concepts and mathematically stated stability criteria; it consumes T03 dynamics and C03 linearization/eigen primitives.
- T05 owns mathematical oscillation/periodic-orbit structure; physical oscillators/waves in B1.2 remain boundary examples, never support claims.
- T06 owns bifurcation and parameter-driven qualitative change; it consumes T03/T04 and may use accepted C05 local analysis.
- T07 owns deterministic chaos concepts such as sensitive dependence, invariant structures and Lyapunov-style indicators in a bounded mathematical scope; probability/statistics C07 remains locked and cannot provide support.
- T08 owns mathematical modeling of time-evolving systems and explicit model-assumption/state-equation discipline; numerical simulation/optimization C10 and physical domain models remain boundary-only until opened.

## Locked boundaries

- `B1.1-C07` probability/statistics: LOCKED, no support claims.
- `B1.1-C08` discrete/combinatorics: LOCKED, no support claims.
- `B1.1-C09` topology/modern geometry: LOCKED, no support claims.
- `B1.1-C10` applied/computational mathematics: LOCKED, no support claims.
- B1.2 physics and later subbranches: boundary examples only unless already Director-accepted.
- No `ACADEMIC_LOCKED`, Lesson Registry, prompt, image, R2, delivery or website artifact.

## Terminal rule

If committed read-back and all gates PASS:

`STATUS: PASS — WORKER_PASS_CANDIDATE`

`NEXT_ACTION: successor remains GATED pending Director acceptance`

If any semantic or source uncertainty remains, return `REVIEW_REQUIRED` rather than forcing PASS.
