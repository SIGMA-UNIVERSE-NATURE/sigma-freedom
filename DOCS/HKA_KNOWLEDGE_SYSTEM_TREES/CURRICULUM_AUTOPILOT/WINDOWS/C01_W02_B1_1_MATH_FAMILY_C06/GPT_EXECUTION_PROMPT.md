# GPT EXECUTION PROMPT — C01-W02-B1.1-MATH-FAMILY-C06

You are the bounded academic worker for HKA World Tree `B1.1-C06 — Phương trình vi phân và hệ động lực`.

## Bootstrap

Treat GitHub durable state as authoritative. Chat history is non-authoritative.

Read in order:

1. `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/HKA_CURRICULUM_STATE.json` on `hka-tree/curriculum-master`.
2. Active Director amendments.
3. This window's `DIRECTOR_OPEN_ORDER.md`.
4. This `WINDOW_CONTRACT.md`.
5. Current C06 `STATUS.json`, `REPORT.md`, latest checkpoint.
6. Accepted predecessor artifacts at exact commit `76077695c07b853ac37f058477177e211f740f17` and accepted C01/C02/C03/C05 academic records as needed.

Abort with durable `REVIEW_REQUIRED` if control-plane does not authorize C06 or the branch ancestry does not contain the accepted predecessor.

## Scope

Author exactly these eight canonical topics and nothing beyond them:

1. `B1.1-C06-T01` — Phương trình vi phân thường
2. `B1.1-C06-T02` — Phương trình đạo hàm riêng
3. `B1.1-C06-T03` — Hệ động lực
4. `B1.1-C06-T04` — Ổn định
5. `B1.1-C06-T05` — Dao động
6. `B1.1-C06-T06` — Phân nhánh
7. `B1.1-C06-T07` — Hỗn loạn
8. `B1.1-C06-T08` — Mô hình biến đổi theo thời gian

Do not author C07/C08/C09/C10 or any later pipeline stage.

## Authoring standard

For each topic create one canonical knowledge node with all required HKA node fields, atomic Claim IDs, D1–D4 objectives, sources, duplicate fingerprints, cross-links and sequence intent.

Claims must be academically conservative and theorem hypotheses must be explicit. In particular:

- Do not state ODE existence/uniqueness without conditions on the vector field.
- Distinguish local from global solutions and existence from uniqueness.
- PDE classification and solution principles must state domain/regularity/boundary hypotheses and avoid pretending every PDE has classical solutions.
- Stability must distinguish Lyapunov/asymptotic/exponential notions when used.
- Linearization conclusions must state hyperbolicity or other required conditions; do not infer nonlinear stability unconditionally from eigenvalues.
- Oscillation/periodicity must distinguish periodic solutions from transient oscillatory behavior.
- Bifurcation claims must state parameter and nondegeneracy/transversality assumptions where theorem-level conclusions require them.
- Chaos claims must not equate a single positive numerical diagnostic with universal chaos, nor import probabilistic randomness.
- Modeling claims must separate mathematical model assumptions from empirical validation in future domain sciences.

## Ownership discipline

Reuse accepted C01/C02/C03/C05 definitions and theorem primitives by ID rather than re-authoring them.

C04 geometry may be used only for phase-space/trajectory representation where useful. Do not duplicate geometry learning meaning.

Locked-scope references are boundary metadata only and cannot appear as supporting Claim IDs.

## Closure discipline

Before worker PASS:

- Read every committed Learning Objective and Claim.
- For every objective, verify that the exact concepts/actions required by the objective are directly supported by the listed Claim IDs — not merely by the node description.
- Create exactly one effective closure row per objective.
- `SUPPORTED_BY_CLAIMS=true` for all objectives.
- `requires_unlocked_scope_claims=false` for all objectives.
- Future/locked support Claim ID count must be zero.

Do not repeat the C04 defect where mechanically present closure rows omitted concepts explicitly demanded by an objective.

## Durable work

Commit substantive authoring in bounded checkpoints. Do not keep the only copy of work in chat memory.

Required terminal audit from committed files:

- exact 8/8 topic coverage;
- ID/referential integrity;
- source identity and deterministic source hashes;
- 100% semantic Claim→Learning-Objective closure;
- duplicate/ownership boundaries;
- acyclic prerequisite/sequence graph;
- zero locked-scope prerequisites/support claims;
- stage boundary and control-plane non-mutation.

Only after those audits PASS may worker publish:

`STATUS: PASS — WORKER_PASS_CANDIDATE`

The worker must not unlock any successor.
