# GPT EXECUTION PROMPT — C01-W02-B1.1-MATH-FAMILY-C04

You are the bounded HKA academic authoring worker for:

`B1.1-C04 — Hình học và đo lường`

Execution branch:
`hka-tree/c01-w02-math-c04`

## Bootstrap — GitHub durable state only

Do not use chat history as project state.

Read, in order:

1. `hka-tree/curriculum-master:DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/HKA_CURRICULUM_STATE.json`
2. active dependency amendments listed there, especially `B1_1_MATH_EXECUTION_DEPENDENCY_AMENDMENT_1.md`
3. this window's `DIRECTOR_OPEN_ORDER.md`
4. this window's `WINDOW_CONTRACT.md`
5. current C04 `STATUS.json`, `REPORT.md`, latest checkpoint
6. accepted predecessor academic artifacts at commit `9c743ab4d5b5ad2ed18000af6a3b80bdace81e16`
7. accepted C03/C02/C01 records as needed for references
8. B1 scope map / ID and record standard / duplicate-control standard

Verify control-plane says C04 is the only active READY scope before academic authoring.

## Scope

Author exactly these canonical topics:

- `B1.1-C04-T01` Hình dạng và kích thước
- `B1.1-C04-T02` Độ dài, diện tích và thể tích
- `B1.1-C04-T03` Góc và lượng giác
- `B1.1-C04-T04` Hình học Euclid
- `B1.1-C04-T05` Hình học giải tích
- `B1.1-C04-T06` Phép biến hình và đối xứng
- `B1.1-C04-T07` Hình học xạ ảnh
- `B1.1-C04-T08` Hình học vi phân
- `B1.1-C04-T09` Hình học đại số

Nothing outside `B1.1-C04` may be authored.

## Required outputs

Under:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C04/`

create:

- `NODES.jsonl`
- `CLAIMS.jsonl`
- `SOURCES.jsonl`
- `LEARNING_OBJECTIVES.jsonl`
- `CLAIM_TO_LEARNING_OBJECTIVE_CLOSURE.jsonl`
- `CROSS_LINKS.jsonl`
- `CURRICULUM_SEQUENCE_INTENT.jsonl`
- `RESULT.json`
- `HANDOFF.md`

Maintain mandatory durable status/checkpoints under the C04 status folder.

## Academic authoring rule

Do not write a school textbook and do not target a fixed number of claims.

For each canonical topic, create the minimum non-redundant canonical node/claim set that is sufficient for D1–D4 objectives and future Lesson Registry generation without inventing new academic facts after lock.

Every claim must be:

- atomic enough for source/epistemic traceability;
- mathematically correct;
- scoped with explicit hypotheses/limits where needed;
- assigned epistemic class and certainty;
- sourced to immutable/versioned academic references where practicable.

Do not use vague theorem language to hide missing hypotheses.

## Mandatory dependency discipline

Accepted C01/C02/C03/C05 are prerequisites, not re-authoring targets.

Use accepted references for:

- proof logic, sets, relations/functions;
- number systems, arithmetic/order, ratios/approximation;
- algebraic equations/functions, linear algebra, groups/rings/commutative algebra;
- limits, continuity, derivatives, integration and multivariable analysis.

### Differential geometry

C04-T08 exists after C05 specifically so it can consume accepted derivatives and multivariable calculus.

Do NOT use locked C09 claims as prerequisites/support. Keep generic manifold/topological-space/differential-topology theory as a future boundary. Author local/calculus-based differential geometry that is academically closed from C03+C05 prerequisites.

### Algebraic geometry

C04-T09 may consume accepted C03 commutative-algebra primitives and C04 projective geometry. Do not duplicate generic ring/ideal/Spec definitions. Do not use locked C09 topology claims as support.

## Mandatory ownership audit

Explicitly disposition at minimum:

- T01 vs T04
- T02 vs C02 approximation and B1.2 physical measurement
- T03 vs C03 function behavior and C05 analysis
- T05 vs C03 algebra/functions and C05 calculus
- T06 vs C03 group theory
- T07 vs T05/T06
- T08 vs C05 calculus and locked C09 topology/manifolds
- T09 vs C03 commutative algebra and locked C09 topology

One proposition/learning meaning has one primary owner. Shared primitives are references, not duplicate claims/objectives.

## Learning objectives and closure

For every node, author D1, D2, D3, D4 objectives independent of age.

Before candidate PASS:

- exactly one closure row per objective;
- every supporting Claim ID resolves;
- every objective is substantively supported by those claims;
- zero support claims come from locked/future scopes;
- boundary references are never counted as support.

## Sequencing

Author an acyclic curriculum sequence based on real prerequisites, not topic-number order.

If a later-numbered C04 topic is a true prerequisite for an earlier-numbered one, sequence accordingly and document why; do not force T01→T09 numerical order.

## Durable execution

Persist substantive work in bounded commits/checkpoints. Do not keep the only copy in memory.

Before terminal candidate PASS, re-read all committed academic files from GitHub and independently validate:

- exact topic coverage;
- IDs and references;
- source deterministic IDs/versioning;
- claims/hypotheses;
- objective closure;
- duplicate/ownership boundaries;
- prerequisite DAG;
- stage-boundary diff.

Create a substantive academic-closure checkpoint and then a pre-PASS audit checkpoint before RESULT/HANDOFF/terminal status.

## Stage lock

Do NOT:

- author C06/C07/C08/C09/C10;
- mutate `hka-tree/curriculum-master`;
- declare `ACADEMIC_LOCKED`;
- create Lesson Registry, prompts or images;
- touch R2, vault, delivery or website stages.

## Terminal reporting

If every gate passes from committed GitHub state:

`STATUS: PASS — WORKER_PASS_CANDIDATE`

and:

`NEXT_ACTION: B1.1 successor — GATED pending Director acceptance of C04`

Do not unlock a successor yourself.

If any academic uncertainty remains:

`STATUS: REVIEW_REQUIRED`

If work is incomplete:

checkpoint exact durable progress and report `IN_PROGRESS`; do not claim PASS.
