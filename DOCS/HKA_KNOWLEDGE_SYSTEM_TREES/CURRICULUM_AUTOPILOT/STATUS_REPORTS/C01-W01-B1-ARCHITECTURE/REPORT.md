# C01-W01-B1-ARCHITECTURE — Durable Status Report

Status: `CHECKPOINTED`  
Stage: `CURRICULUM`  
Execution branch: `hka-tree/c01-w01-b1-architecture`  
Input baseline: `02ff47d64fd3b3b03d1fa2ae70d773afb071995e`  
Canonical tree: `fc799bf1104ab6352710e1801777a971b5179995`

## Assigned job

Build the restartable Branch 1 curriculum-authoring architecture only: preserve all canonical B1 coverage, assign stable primary ownership, define stable curriculum IDs/records, create prerequisite-aware bounded child windows, and control semantic duplication/cross-domain reuse. Do not author any later pipeline-stage artifact.

## Definitely finished

- Canonical B1 scope is reconciled into 5 subbranches, 68 stable primary scopes and 348 canonical topic leaves.
- All 348 leaves have exactly one primary authoring owner; orphan count and multi-primary count are zero.
- 52 independently resumable child windows are defined; the largest child has 10 canonical topics.
- A stable prerequisite graph is defined for all 68 scopes and has been checked acyclic during architecture construction.
- Stable rules are defined for Node, Claim, Source, Learning Objective and non-registry future lesson-slot references.
- Semantic duplicate control covers three exact repeated labels and 15 registered semantic/cross-domain risk cases.
- Mandatory cross-domain nodes are represented only as secondary links; they do not transfer B1 primary ownership.
- Governance updates `7ee6efa385909139fb4718bca5eb72ecd8f73732` and `f52ddcb7fd7c6c821fede8af452c80efcc8ddead` were detected on this execution branch, read, and adopted. They require the durable status folder and do not authorize work outside `CURRICULUM`.
- `CP01-ARCHITECTURE-DRAFT` and working `STATUS.json` are committed.

## Not finished yet

- Full post-commit audit of the current execution branch.
- Append-only pre-PASS audit checkpoint.
- `RESULT.json` terminal checkpoint.
- Final synchronization of `HANDOFF.md`, `STATUS.json` and this report to `PASS` if and only if every gate succeeds.

## Authoritative files and commits so far

- `B1_SCOPE_MAP.json` — introduced at `a2f35fdfb88b14538f3d036ed997475ec0756b62`.
- `B1_COVERAGE_MATRIX.md` — introduced at `9c2bd3e13758dbe2acf4f7a480efab23f424dbae`.
- `B1_DUPLICATE_CONTROL.md` — current duplicate enum normalized at `e0a43589dfb1d1078dece6dcfaa0e8f128afd55b`.
- `B1_AUTHORING_SEQUENCE.md` — durable-status integration at `e57bd70a02026cfeee0aa18282a4eb1ff7c12e69`.
- `B1_ID_AND_RECORD_STANDARD.md` — durable recovery integration at `a76d539da1d348c7d69ea4776b98bf912bcf0cc6`.
- `HANDOFF.md` — current recovery note introduced at `56108da75e551e2a8b59edd24f86efd044448f9e`; it will be synchronized with the new status standard before PASS.
- `CHECKPOINTS/CP01-ARCHITECTURE-DRAFT.json` — `7a98aa5d52f29a08e17fc0760465186426cf9aaf`.
- Working `STATUS.json` — `befa80718c5704565e043d0108998f49d59192ba`.

The execution branch itself is the current GitHub source of truth; later commits may supersede the file-level commits listed above without changing accepted stable IDs.

## Locked decisions

- Preserve the canonical five B1 subbranches and canonical topic coverage; do not replace them with another subject taxonomy.
- Stable scope IDs are `B1.x-Cnn`; stable canonical topic IDs are `B1.x-Cnn-Tnn`.
- Every canonical topic has one primary owner. Cross-links are secondary and never silently transfer ownership.
- D1–D4 is epistemic depth and remains independent of age/presentation.
- Semantic duplicate identity at `CURRICULUM` is `NODE MEANING + CLAIM SET + LEARNING OBJECTIVE + CONTEXT`.
- Family windows are controllers over bounded child windows, not whole-discipline single-chat jobs.
- Accepted stable IDs are append-only and must never be silently renumbered after a crash/replacement.
- `LESSON_REGISTRY`, prompts, image production, R2, delivery and website work remain forbidden.

## Known risks / errors

No current blocker is recorded. The known overlap zones are deliberately not treated as automatically resolved future content: successor children must disposition `R01`–`R15` against actual claims/objectives and repeat semantic duplicate checks. The architecture itself does not pre-approve future academic authoring.

A concurrent governance change occurred during this window. It was not ignored or reverted; GitHub source-of-truth controls were re-read and incorporated. The branch must be checked again before final PASS for any further governance drift.

## What happens next

Run the post-commit audit against the current branch: coverage/ownership counts, prerequisite DAG, duplicate controls, required status artifacts, pipeline-stage boundary, current state/contract/prompt, and changed-file paths. If every gate passes, commit a pre-PASS checkpoint, then `RESULT.json`, then synchronize durable status/report to PASS.

## Do not redo

Do not reassign or renumber the 68 stable B1 scopes, do not duplicate the 348 ownership assignments under different wording/scenery, do not collapse the three repeated labels without their registered claim-boundary controls, and do not start `C01-W02-B1.1-MATH-FAMILY` until this window has an accepted PASS checkpoint.
