# DIRECTOR-W01 — Status Report

## Current stage

`CURRICULUM`

No later pipeline stage is unlocked.

## Director-accepted B1.1 scopes

- `B1.1-C01 — Logic, tập hợp và chứng minh` @ `5659288da80a239e2ded408da87348670c1410c2`
- `B1.1-C02 — Số học và lý thuyết số` @ `cfd9746e2296280705e2e2e67b2c5980d440f02d`
- `B1.1-C03 — Đại số và cấu trúc` @ `7546ad74fb0e71ad2120c7091947993690bef82d`
- `B1.1-C05 — Giải tích và biến đổi liên tục` @ `9c743ab4d5b5ad2ed18000af6a3b80bdace81e16`
- `B1.1-C04 — Hình học và đo lường` @ `76077695c07b853ac37f058477177e211f740f17`

## C04 Director audit and repair

Worker candidate:
`add8e0732da7d69ea5e641654acb8f948ff8b265`

Director independently reviewed:

- 9/9 canonical topics and 9 nodes;
- 83/83 atomic claims;
- 6/6 versioned/persistent sources and deterministic SOURCE_ID hashes;
- 36/36 D1–D4 Learning Objectives;
- all 36 base Claim → Learning Objective closure rows;
- 18 ownership/cross-link records;
- 9 prerequisite/sequence records;
- T08 differential-geometry boundary against locked C09;
- T09 algebraic-geometry boundary against accepted C03 and locked C09;
- stage boundary and worker control-plane non-mutation.

No theorem-level academic correction was required.

Director did find four semantic closure-map omissions despite the worker's mechanical `36/36 PASS`:

1. `N001-D1`: diameter objective omitted support claim `N001-C006`.
2. `N002-D1`: perimeter/surface-area/volume recognition omitted the committed claims supplying those meanings.
3. `N005-D1`: distance/midpoint objective omitted `N005-C002` and `N005-C003`.
4. `N007-D2`: point-at-infinity objective omitted `N007-C004`.

Director repaired only those mappings, without changing stable IDs or theorem claims:

`CLAIM_TO_LEARNING_OBJECTIVE_CLOSURE_DIRECTOR_AMENDMENT_1.jsonl`

Amendment commit:
`3b3f15c778a0ea33ba58a405007ea1311f877cef`

Effective rule: for a matching `learning_objective_id`, the Director amendment row supersedes the base closure row.

After repair:

- effective Claim → Learning Objective closure: `36/36 PASS`;
- future/locked support Claim IDs: `0`;
- T08 support from C09: `0`;
- T09 support from C09: `0`;
- semantic duplicate/ownership audit: PASS;
- prerequisite DAG: PASS / acyclic;
- stage boundary: PASS.

Canonical Director-accepted C04 head:

`76077695c07b853ac37f058477177e211f740f17`

C04 is `DIRECTOR_ACCEPTED_PASS`.

## Active work

Only active child:

`C01-W02-B1.1-MATH-FAMILY-C06`

Scope:

`B1.1-C06 — Phương trình vi phân và hệ động lực`

Execution branch:

`hka-tree/c01-w02-math-c06`

Pinned accepted predecessor:

`76077695c07b853ac37f058477177e211f740f17`

Canonical topics:

1. Phương trình vi phân thường
2. Phương trình đạo hàm riêng
3. Hệ động lực
4. Ổn định
5. Dao động
6. Phân nhánh
7. Hỗn loạn
8. Mô hình biến đổi theo thời gian

## C06 mandatory academic controls

- ODE existence/uniqueness must state real hypotheses and distinguish local from global conclusions.
- PDE claims must state domain/regularity/initial or boundary hypotheses and must not imply universal classical solvability.
- Stability and linearization must preserve their exact hypotheses; eigenvalues alone do not justify unconditional nonlinear conclusions.
- Periodicity, bifurcation and deterministic chaos must remain distinct concepts.
- Chaos must not be equated with probabilistic randomness; C07 remains locked.
- Numerical simulation/optimization belongs to locked C10 and cannot support C06 claims.
- Physical-domain models in B1.2 remain boundary examples only.
- Every objective must be semantically closed by its exact supporting Claim IDs; mechanical closure-row presence is insufficient.
- Future/locked support Claim IDs must be zero.

## Durable C06 activation

- C06 contract: `888ede187b631211e2f32cad3d3088ef660883c8`
- C06 execution prompt: `71ef87c77b704bdbde7ae1ae835302e678705c9c`
- C06 Director open order: `82e055c6d54eacc31625f95f8485071fb70316d6`
- C06 bootstrap checkpoint: `6eb206014bb06b5f524b2854a50fd7e4b1ec63ef`
- C06 READY status: `cb783e71758c4165372b05cbbb03580cc97cebc0`
- C06 READY report: `e481601256b112b56ab30ef30aadb5b67cc477ea`
- Control-plane state: `e45d9aa4ec9552bfc9d7868c5efa0d25c0c4c174`
- Window registry: `3524072e1063a39ae37abbc90edd15b1921bf788`
- Director checkpoint: `b50bf59eddd59bb9d3b216f6288272401c69345a`

## Stage lock

C07/C08/C09/C10 and all B1.2+ scopes remain locked until later Director decisions.

`ACADEMIC_LOCKED`, Lesson Registry, prompts, images, R2, delivery and website stages remain gated.

## Next action

Run only `C01-W02-B1.1-MATH-FAMILY-C06` from `DIRECTOR_OPEN_ORDER.md` and `GPT_EXECUTION_PROMPT.md` on `hka-tree/c01-w02-math-c06`.
