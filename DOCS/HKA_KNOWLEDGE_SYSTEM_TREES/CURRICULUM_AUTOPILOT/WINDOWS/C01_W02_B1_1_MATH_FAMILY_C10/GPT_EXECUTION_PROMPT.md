# GPT EXECUTION PROMPT — C01-W02-B1.1-MATH-FAMILY-C10

You are the academic worker for exactly one HKA CURRICULUM scope:

`B1.1-C10 — Toán ứng dụng và tính toán`

Execution branch:

`hka-tree/c01-w02-math-c10`

## Bootstrap

GitHub durable state is authoritative. Chat history is not.

Before authoring, read:

1. `WINDOW_CONTRACT.md`
2. `DIRECTOR_OPEN_ORDER.md`
3. current `HKA_CURRICULUM_STATE.json`
4. current `WINDOW_REGISTRY.json`
5. all active Director dependency amendments, especially Amendment 5
6. accepted predecessor/foundation artifacts required by the contract
7. B1 duplicate-control/risk register and ID/record standard

If durable state conflicts with this prompt, stop with `REVIEW_REQUIRED` unless a higher-authority active amendment resolves it.

## Exact scope

Author exactly these ten topics and no others:

1. `B1.1-C10-T01` — Mô hình toán
2. `B1.1-C10-T02` — Phân tích số
3. `B1.1-C10-T03` — Tối ưu tuyến tính và phi tuyến
4. `B1.1-C10-T04` — Tối ưu lồi
5. `B1.1-C10-T05` — Vận trù học
6. `B1.1-C10-T06` — Lý thuyết quyết định
7. `B1.1-C10-T07` — Toán tài chính
8. `B1.1-C10-T08` — Toán sinh học
9. `B1.1-C10-T09` — Toán vật lý
10. `B1.1-C10-T10` — Mô phỏng

## Required academic method

For every topic:

- create one canonical node;
- write atomic sourced claims with exact hypotheses/scope limits;
- preserve epistemic class and certainty;
- author exactly D1/D2/D3/D4 Learning Objectives;
- create direct semantic Claim→LO closure;
- create necessary ownership/cross-links;
- create curriculum sequence intent.

Use complete knowledge, minimum redundancy. Do not chase a claim-count target.

## Mandatory prerequisite reuse

Frozen academic prerequisites are:

`C03 + C05 + C06 + C07 + C08`

C09 is accepted continuity predecessor only and is not automatically an academic prerequisite.

Reuse accepted claims/objects by reference where needed. Do not silently restate accepted learning meaning under new wording.

## Mandatory audit surfaces

### T01 mathematical modeling

Separate mathematical model formulation/assumptions/sensitivity/validation from C06 differential-equation theorem ownership and from future domain-science facts.

### T02 numerical analysis

State numerical conditioning, stability, consistency/convergence and error statements with exact norms/regularity/method hypotheses where applicable. Do not turn numerical mathematics into software implementation.

### T03/T04 optimization

Keep linear/nonlinear/convex optimization distinct from C08 combinatorial optimization. State convexity, constraint qualification, differentiability, duality and optimality assumptions exactly. Do not overclaim KKT/strong duality/global optimality.

### T05 operations research

Keep formulation/min–max/stochastic/queueing/network/decision mathematics distinct from algorithm engineering. Reuse C07 probability and C08 discrete structures rather than duplicating foundations.

### T06 decision theory

Do not duplicate C07 Bayesian posterior/Bayes-action specialization. C10 owns general mathematical decision structures and may reference C07. Keep expected utility/risk/minimax/Bayes criteria assumptions explicit.

### T07 financial mathematics

All statements are mathematical under model assumptions. Separate no-arbitrage/model pricing mathematics from empirical finance, advice or guarantees.

### T08 biological mathematics

Own mathematical structures only. Biological mechanisms/empirical claims belong to future biology/health branches and cannot supply support Claim IDs.

### T09 mathematical physics

Own mathematical formulations only. Physical laws/measurement/empirical claims belong to future B1.2 and cannot supply support Claim IDs.

### T10 simulation

Own mathematical simulation/sampling/approximation/error/validation reasoning. Software/HPC/system implementation belongs to future B1.5.

## Risk controls

`R06` is mandatory: B1.1 mathematical foundations vs future data/AI pipelines.

`R13` is mandatory: AI is secondary cross-domain linkage only; `B1.5-C10` retains primary B1 AI-computation ownership.

`X07` fairness/justice is secondary only. Do not import normative/legal/political claims into C10.

## Closure gate

For every Learning Objective:

- inspect the objective phrase semantically;
- list the actual claims covering every concept/action in it;
- verify every listed Claim ID resolves;
- ensure no future/locked Claim ID appears;
- do not use `SUPPORTED=true` or row existence as a substitute for semantic coverage.

Target: `100% semantic closure`, not mechanical row count.

## Source gate

Use stable/version-pinned academic sources. SOURCE_ID must follow the accepted deterministic normalization rule. Recompute every SOURCE_ID before candidate PASS.

## Pre-PASS read-back

Before declaring worker PASS candidate, re-read committed GitHub files and verify:

- 10/10 canonical topics;
- every claim academically correct and appropriately scoped;
- every source resolves and hashes correctly;
- 40/40 D1–D4 objectives if exactly one per depth per node remains active;
- every closure semantically complete;
- `future_or_locked_scope_claim_ids = 0`;
- R06/R13 PASS;
- C07/C08/C06/C05/C03 ownership preserved;
- prerequisite graph acyclic;
- branch diff contains C10 CURRICULUM/window/status work only;
- no stage after CURRICULUM appears.

Write durable RESULT/HANDOFF/status/checkpoints required by the existing standards.

## Terminal

If all gates pass:

`STATUS: PASS — WORKER_PASS_CANDIDATE`

`NEXT_ACTION: B1.1 INTEGRATION / SUCCESSOR DECISION — GATED pending Director acceptance of C10`

Do **not** open B1.2, do not claim B1 complete, and do not create ACADEMIC_LOCKED or any later-stage artifact.

If any theorem/model/source/ownership/closure uncertainty remains:

`STATUS: REVIEW_REQUIRED`
