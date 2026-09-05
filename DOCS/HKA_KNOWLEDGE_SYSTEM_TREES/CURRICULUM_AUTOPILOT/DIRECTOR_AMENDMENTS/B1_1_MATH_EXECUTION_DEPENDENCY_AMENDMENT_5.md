# B1.1 Math Execution / Ownership Amendment 5 — C10 Applied Mathematics Boundary

Status: ACTIVE  
Stage: CURRICULUM  
Scope affected: `B1.1-C10 — Toán ứng dụng và tính toán`

## 1. Purpose

This amendment does not change any frozen scope/topic ID, name, or primary owner. It clarifies the final B1.1 authoring boundary before C10 execution so applied mathematics does not silently duplicate accepted mathematical foundations or future B1.5/domain-science curricula.

## 2. Frozen C10 topics

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

## 3. Academic prerequisites

Frozen architecture prerequisites remain exactly:

- `B1.1-C03 — Đại số và cấu trúc`
- `B1.1-C05 — Giải tích và biến đổi liên tục`
- `B1.1-C06 — Phương trình vi phân và hệ động lực`
- `B1.1-C07 — Xác suất, thống kê và suy luận`
- `B1.1-C08 — Toán rời rạc và tổ hợp`

C09 is the accepted continuity predecessor because of execution order, but **is not added as a mandatory academic prerequisite**.

## 4. Mandatory ownership boundaries

### T01 mathematical modeling

C10 owns model formulation, assumptions, parameterization, dimensional/structural interpretation, sensitivity and model-validation logic as mathematics. C06 retains differential-equation/dynamical-system theorem ownership. Domain-science facts remain with their future canonical branches.

### T02 numerical analysis

C10 owns numerical approximation, discretization, conditioning, numerical stability, consistency/convergence and error propagation of computational methods. C05 retains analytic limit/calculus theorems; C02 retains arithmetic/number foundations; future B1.5 retains implementation and computational-system engineering.

### T03/T04 optimization

C10 owns general continuous, linear/nonlinear and convex optimization mathematics, optimality conditions and duality within stated hypotheses. C08 retains combinatorial/discrete optimization structures. Future B1.5-C03 retains algorithm implementation and complexity engineering.

### T05 operations research

C10 owns mathematical operations-research formulations and analytic optimization/decision structures. Reuse C07 probability and C08 discrete structures by reference. Do not turn this into software/algorithm-system implementation.

### T06 decision theory

C10 owns general mathematical decision theory: actions, states, loss/utility/risk, decision criteria and optimization under uncertainty. C07 retains probability/statistical inference, posterior semantics and its already accepted Bayesian-decision specialization. Shared Bayes-action mathematics must be referenced rather than independently reauthored.

### T07 financial mathematics

C10 owns mathematical structures used in finance (discounting, stochastic/portfolio/pricing mathematics under explicit model assumptions). Do not author financial advice, institutional/economic policy claims, or treat model assumptions as empirical truths.

### T08 biological mathematics

C10 owns mathematical model structures applied to biological systems. Future biology/health branches retain biological mechanisms and empirical claims. No future biology Claim ID may support C10.

### T09 mathematical physics

C10 owns mathematical formulations/structures used in physics. Future B1.2 retains physical-law, measurement and empirical-physics ownership. No locked B1.2 Claim ID may support C10.

### T10 simulation

C10 owns mathematical simulation methodology, approximation/sampling logic and validation/error reasoning. Future B1.5 owns software implementation, systems, performance engineering and computational infrastructure.

## 5. Mandatory risk controls

- `R06` mathematics-vs-data/AI: mathematical/statistical/applied foundations remain B1.1; future B1.5 owns computational pipelines, ML/AI engineering and implementation.
- `R13` AI shared node: `X02` is secondary only; `B1.5-C10` remains primary B1 AI-computation owner.
- `X07` justice/fairness linkage is secondary only. Normative, legal, political and ethical claims remain outside C10 primary ownership.

## 6. Hard gates

- Complete knowledge, minimum redundancy; no target claim count.
- Every claim must be atomic, sourced, epistemically classified and scope-limited.
- Every D1–D4 objective must be semantically closed by actual Claim IDs.
- Future/locked support Claim IDs = 0.
- No B1.2+, B1.5, B2+ claim may be used as support.
- No ACADEMIC_LOCKED, Lesson Registry, prompts, images, R2 or later-stage artifact.
- Worker PASS remains candidate only; no successor/subbranch unlock by worker.

## 7. Effect on execution order

Execution order remains:

`C06 → C08 → C07 → C09 → C10`

After Director-accepted C10, B1.1 authoring is complete, but B1 is **not** complete and no global academic lock is authorized.
