# WINDOW CONTRACT — C01-W02-B1.1-MATH-FAMILY-C10

Status: READY_CONTRACT  
Stage: `CURRICULUM`  
Scope: `B1.1-C10 — Toán ứng dụng và tính toán`  
Execution branch: `hka-tree/c01-w02-math-c10`  
Continuity predecessor: `B1.1-C09@9f17cee504c51830f0f4fbfbe429ffa8759ea793`

## 1. Exact canonical topics

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

Stable IDs, names and order are immutable.

## 2. Frozen academic prerequisites

Exactly the architecture prerequisites:

- `B1.1-C03 — Đại số và cấu trúc`
- `B1.1-C05 — Giải tích và biến đổi liên tục`
- `B1.1-C06 — Phương trình vi phân và hệ động lực`
- `B1.1-C07 — Xác suất, thống kê và suy luận`
- `B1.1-C08 — Toán rời rạc và tổ hợp`

C09 is the continuity predecessor only; it is not silently added as a mandatory academic prerequisite.

## 3. Active Director controls

Read and obey all active dependency amendments, especially:

`B1_1_MATH_EXECUTION_DEPENDENCY_AMENDMENT_5.md`

Mandatory risks:

- `R06 — mathematics-vs-data/AI`
- `R13 — AI secondary cross-domain node`

Shared-node links allowed only as secondary:

- `X02 — TRÍ TUỆ NHÂN TẠO`
- `X07 — CÔNG BẰNG`

They do not transfer primary ownership.

## 4. Academic authoring standard

For each of 10 nodes author complete knowledge with minimum redundancy:

- atomic academically scoped claims;
- epistemic class + certainty + stable source IDs;
- explicit theorem/model assumptions and scope limits;
- exactly one D1, D2, D3 and D4 Learning Objective per node unless a later Director amendment explicitly changes this rule;
- direct Claim→Learning Objective semantic closure;
- typed cross-links and ownership dispositions;
- prerequisite/sequence intent with an acyclic graph.

No target claim count exists. Correct coverage determines count.

## 5. Non-negotiable ownership boundaries

### T01 — Mô hình toán

Own mathematical model formulation, assumptions, parameterization, sensitivity and mathematical validation logic. C06 retains differential-equation/dynamical-system theorem ownership. Domain facts stay with their future branches.

### T02 — Phân tích số

Own numerical approximation/discretization, conditioning, stability, consistency/convergence and numerical error. C05 retains analytic theorems; future B1.5 retains implementation/system engineering.

### T03/T04 — Optimization

Own continuous/general linear/nonlinear/convex optimization mathematics, duality and optimality conditions under exact hypotheses. C08 retains combinatorial optimization structures. B1.5 retains implementation and complexity.

### T05 — Vận trù học

Own mathematical operations-research formulations and optimization/decision structures. Probability/discrete foundations are references to C07/C08, not reauthored.

### T06 — Lý thuyết quyết định

Own general mathematical decision theory: actions, states, utility/loss/risk, criteria and optimization under uncertainty. C07 retains statistical/Bayesian inference and its accepted posterior/Bayes-action specialization. Reuse that specialization by reference; do not duplicate it.

### T07 — Toán tài chính

Own mathematical finance structures under explicit model assumptions. No financial advice, economic-policy ownership or empirical-truth overclaim.

### T08 — Toán sinh học

Own mathematical model structures applied to biological systems. Future biology/health branches retain biological mechanism and empirical claims. Future support Claim IDs = 0.

### T09 — Toán vật lý

Own mathematical structures/formulations used in physics. Future B1.2 retains physical-law, measurement and empirical-physics ownership. Future support Claim IDs = 0.

### T10 — Mô phỏng

Own mathematical simulation methodology, approximation/sampling logic and validation/error reasoning. Future B1.5 retains software, HPC and systems implementation.

## 6. Closure and prerequisite gates

- Every objective must be semantically supported by its listed Claim IDs, not merely have a closure row.
- `future_or_locked_scope_claim_ids = 0` in every closure record.
- No B1.2+, B1.5 or B2+ Claim ID may support C10.
- Accepted prerequisite references must preserve their primary ownership.
- Internal prerequisite graph must be acyclic.

## 7. Stage lock

C10 is the final B1.1 authoring scope, but completion of C10 does **not** complete B1 or CURRICULUM globally.

Forbidden:

- `ACADEMIC_LOCKED`
- Lesson Registry / Lesson Registry Locked
- prompts / Prompt Locked
- image production
- R2 / QA / Vault / Web Optimize / Delivery / Website Update
- B1.2+ authoring
- control-plane mutation by worker

## 8. Terminal rule

Worker may produce only:

`PASS — WORKER_PASS_CANDIDATE`

or

`REVIEW_REQUIRED`

Worker may not Director-accept C10 and may not unlock B1.2 or any later stage.
