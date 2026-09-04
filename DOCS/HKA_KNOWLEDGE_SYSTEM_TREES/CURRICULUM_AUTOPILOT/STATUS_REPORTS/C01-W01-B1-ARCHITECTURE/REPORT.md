# C01-W01-B1-ARCHITECTURE — Durable Status Report

Status: `PASS`  
Stage: `CURRICULUM`  
Execution branch: `hka-tree/c01-w01-b1-architecture`  
Input baseline: `02ff47d64fd3b3b03d1fa2ae70d773afb071995e`  
Canonical tree: `fc799bf1104ab6352710e1801777a971b5179995`

## Assigned job

Build the restartable Branch 1 curriculum-authoring architecture only: preserve all canonical B1 coverage, assign stable primary ownership, define stable curriculum IDs/records, create prerequisite-aware bounded child windows, and control semantic duplication/cross-domain reuse. Do not author any later pipeline-stage artifact.

## Definitely finished

- Canonical B1 scope is reconciled into 5 subbranches, 68 stable primary scopes and 348 canonical topic leaves.
- All 348 leaves have exactly one primary authoring owner; orphan count and multi-primary count are zero.
- 52 independently resumable child windows are defined; the largest child has 10 canonical topics and all 348 topics are assigned exactly once across the child partition.
- The 68-scope prerequisite graph is acyclic and contains no unknown prerequisite scope ID.
- Stable rules are defined for Node, Claim, Source, Learning Objective and non-registry future lesson-slot references.
- Semantic duplicate control covers three exact repeated labels (`Dao động`, `Mã sửa lỗi`, `Entropy`) and 15 registered semantic/cross-domain risk cases; uncontrolled architecture duplicate-risk count is zero.
- All eight mandatory cross-domain nodes are treated as graph intersections/secondary links without transferring B1 primary ownership.
- Durable status/report/checkpoint requirements are integrated into family/controller/child recovery and acceptance.
- `HANDOFF.md` is synchronized with durable-status recovery.
- `CP02-PRE-PASS-AUDIT` passed coverage, ownership, partition, prerequisite-DAG, duplicate, governance and stage-boundary checks.
- `RESULT.json` is committed with `status=PASS` and deterministic `next_action=C01-W02-B1.1-MATH-FAMILY`.
- Durable `STATUS.json` is committed with `status=PASS`, zero remaining work and the same successor.

## Not finished

None inside `C01-W01-B1-ARCHITECTURE`. This window must not be reopened or extended into successor authoring unless a future canonical contradiction invalidates its accepted artifacts.

## Authoritative files and commits

- `B1_SCOPE_MAP.json` — blob `bedef47958a728e3f0d56d412f7bdea3ec465856`.
- `B1_COVERAGE_MATRIX.md` — blob `34f6a7ae5fc882ef9d3e217c7601103af573fba3`.
- `B1_DUPLICATE_CONTROL.md` — blob `04d3720d6061e74ff20c39c6edf7d517558105b9`.
- `B1_ID_AND_RECORD_STANDARD.md` — blob `ae6829c04a6eb870dbcf12a6622c29431f4da75f`.
- `B1_AUTHORING_SEQUENCE.md` — blob `e04f71a68dafa9c4196da813ad376912a062500a`; accepted-predecessor selector requires terminal durable PASS.
- `HANDOFF.md` — blob `b08a66750eee162a7c41ffcec1d8fbebfd79d243`, synchronized at commit `21330650608373f46b9d1ac05bf6b36fcbc9fafd`.
- `CP01-ARCHITECTURE-DRAFT.json` — commit `7a98aa5d52f29a08e17fc0760465186426cf9aaf`.
- `CP02-PRE-PASS-AUDIT.json` — commit `2b3ba51abeb5cf7f08be6a727b4aa441351fae6d`.
- `RESULT.json` — PASS commit `2ec918cb4dca4a851b917dc420e488042c07d240`.
- `STATUS.json` — terminal PASS commit `ff6e218e68a28a33ec969af8c1f726824d9b9647`.
- Governance inputs currently read on the execution branch: prompt blob `09080507c4d03ad08c2352681868e2b21468b81d`; contract blob `f3c70aee8211d5f8b679eb28b06b2c1739d052ef`.

The execution branch terminal commit containing this current PASS report is the immutable predecessor candidate selected by `B1_AUTHORING_SEQUENCE.md`; the successor must resolve and pin it from Git history rather than relying on a floating branch name.

## Locked decisions

- Preserve the canonical five B1 subbranches and canonical topic coverage; do not replace them with another subject taxonomy.
- Stable scope IDs are `B1.x-Cnn`; stable canonical topic IDs are `B1.x-Cnn-Tnn`.
- Every canonical topic has one primary owner. Cross-links are secondary and never silently transfer ownership.
- D1–D4 is epistemic depth and remains independent of age/presentation.
- Semantic duplicate identity at `CURRICULUM` is `NODE MEANING + CLAIM SET + LEARNING OBJECTIVE + CONTEXT`.
- Family windows are controllers over bounded child windows, not whole-discipline single-chat jobs.
- Accepted stable IDs are append-only and must never be silently renumbered after a crash/replacement.
- A family/child is accepted only when durable status and result both say PASS with required report/checkpoint present.
- `LESSON_REGISTRY`, prompts, image production, R2, delivery and website work remain forbidden until their pipeline gates open.

## Known risks / errors

No blocker remains in this architecture window. `R01`–`R15` remain mandatory successor review controls against actual future claims/objectives; this architecture PASS does not pre-approve future academic content.

Two concurrent governance changes were observed during execution: `7ee6efa385909139fb4718bca5eb72ecd8f73732` and `f52ddcb7fd7c6c821fede8af452c80efcc8ddead`. They were read and adopted as GitHub source-of-truth controls. They added durable-status requirements and did not unlock any later pipeline stage.

## What the successor must do next

Open only registered family controller `C01-W02-B1.1-MATH-FAMILY`. Before any authoring, resolve and pin the accepted architecture predecessor commit using the deterministic selector in `B1_AUTHORING_SEQUENCE.md`; then begin only bounded child `C01-W02-B1.1-MATH-FAMILY-C01` and maintain its own mandatory durable status folder.

## Do not redo

Do not reassign or renumber the 68 stable B1 scopes, do not duplicate the 348 ownership assignments under different wording/scenery, do not collapse the three repeated labels without their registered claim-boundary controls, do not author any later-stage artifact, and do not redo `C01-W01-B1-ARCHITECTURE` after terminal PASS.
