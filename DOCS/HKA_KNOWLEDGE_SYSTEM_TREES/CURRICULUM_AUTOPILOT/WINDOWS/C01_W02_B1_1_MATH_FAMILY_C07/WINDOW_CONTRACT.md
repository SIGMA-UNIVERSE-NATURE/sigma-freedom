# WINDOW CONTRACT — C01-W02-B1.1-MATH-FAMILY-C07

STATUS: READY_AFTER_DIRECTOR_C08_ACCEPTANCE
STAGE: CURRICULUM
SCOPE: B1.1-C07 — Xác suất, thống kê và suy luận
EXECUTION_BRANCH: `hka-tree/c01-w02-math-c07`
INPUT_COMMIT_SHA: `14729ce490289b057d5dca25767c3b5ea357e1ec`

## Canonical topics — exact stable order

- `B1.1-C07-T01` — Không gian xác suất
- `B1.1-C07-T02` — Biến ngẫu nhiên
- `B1.1-C07-T03` — Phân phối xác suất
- `B1.1-C07-T04` — Quá trình ngẫu nhiên
- `B1.1-C07-T05` — Thống kê mô tả
- `B1.1-C07-T06` — Ước lượng
- `B1.1-C07-T07` — Kiểm định giả thuyết
- `B1.1-C07-T08` — Thống kê Bayes
- `B1.1-C07-T09` — Thiết kế thí nghiệm
- `B1.1-C07-T10` — Suy luận nhân quả

Stable topic IDs and primary ownership are fixed. Do not renumber or rename silently.

## Accepted prerequisites

Base frozen prerequisites:
- C01 logic/set/proof foundations.
- C02 arithmetic/number foundations.
- C03 algebra/linear-algebra/function primitives.

Dependency Amendment 3 supplemental prerequisites:
- C05 measure/integration/function-space analysis where probability/statistics needs rigorous measure-theoretic support.
- C08 DAG/topological-order/reachability graph mathematics for causal representation.

C06 is accepted project ancestry but is not a required support scope for C07 unless a specific stochastic-process cross-link is academically necessary. Do not convert deterministic-dynamics claims into probability claims.

## Required output artifacts

Under:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C07/`

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
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/C01-W02-B1.1-MATH-FAMILY-C07/`

## Academic gates

1. Complete knowledge, minimum redundancy. Do not target a claim count.
2. Every claim must be atomic, sourced, scope-limited, epistemically classified and certainty-labelled.
3. D1–D4 are academic depth, independent of age.
4. Every objective must have one effective closure row and direct semantic support Claim IDs.
5. `future_or_locked_scope_claim_ids` must be empty for every closure row.
6. Use immutable/versioned sources where practicable: DOI/ISBN/edition/versioned institutional standard.
7. Prerequisite graph must be acyclic and academically necessary.
8. Worker PASS is candidate only. Only Director acceptance may unlock a successor.
9. Do not force HKA Compass into technical claims.
10. No post-CURRICULUM artifact is allowed.

## Mandatory theorem/interpretation discipline

- Probability axioms and measure-theoretic constructions must state domain/sigma-algebra/integrability hypotheses when relevant; generic measure theory remains C05 ownership.
- Independence, conditional probability and conditional expectation must not be conflated.
- Distributional convergence, convergence in probability, almost-sure convergence and convergence in mean must remain distinct when used.
- LLN/CLT statements must state the actual independence/identical-distribution/moment or other theorem-specific assumptions for the selected form.
- Descriptive statistics must not be presented as inferential evidence without a sampling/identification argument.
- Estimator properties such as unbiasedness, consistency, efficiency and sufficiency must remain distinct.
- Confidence intervals are procedures with coverage under repeated sampling; they are not automatically posterior probability intervals.
- p-values are not posterior probabilities, effect sizes, or probabilities that the null is true.
- Bayesian posterior claims must state prior, likelihood/model and conditioning assumptions; Bayes factors/posterior probabilities are not frequentist p-values.
- Randomization, replication, blocking and control in experimental design must be separated from observational adjustment.
- Causal conclusions require identification assumptions or randomized design; association alone is not causation.
- A DAG alone does not establish causal meaning. C08 supplies graph mathematics only; C07 owns causal semantics/assumptions.

## Mandatory ownership boundaries

### R06 — mathematics vs data/AI
C07 owns mathematical probability/statistics/inference foundations. Future B1.5 data/AI scopes own data pipelines, machine-learning implementation/model engineering and AI-system objectives. No future B1.5 claim may support C07.

### R13 — AI mandatory cross-domain node
C07 may be a mathematical dependency of AI and may carry a secondary AI cross-link. B1.5-C10 remains primary B1 owner of AI computation. Do not author AI cognition, system engineering, ethics, policy or application content here.

### T10 causal inference
C08 owns graph/DAG/topological-order/reachability mathematics. C07-T10 owns causal models, causal assumptions, interventions, confounding, graphical/conditional-independence reasoning, identification and design-based causal inference. Do not re-author generic graph theory.

## Locked boundaries

- `B1.1-C09`: LOCKED, no support claims.
- `B1.1-C10`: LOCKED, no support claims.
- `B1.5+`: future ownership boundaries only, no support claims.
- B2+ domain sciences: examples/boundaries only, no support claims unless later accepted and explicitly authorized.
- No `ACADEMIC_LOCKED`, Lesson Registry, prompt, image, R2, delivery or website artifact.

## Terminal rule

If committed read-back and all gates PASS:

`STATUS: PASS — WORKER_PASS_CANDIDATE`

`NEXT_ACTION: C01-W02-B1.1-MATH-FAMILY-C09 — GATED pending Director acceptance of C07`

If any semantic/source/identification uncertainty remains, return `REVIEW_REQUIRED` rather than forcing PASS.
