# SIGMA — NEW CODER MANDATORY HANDOFF ORDER

Date: 2026-10-02
Status: ACTIVE COORDINATION ORDER

## 0. Absolute rule

DO NOT RESTART SIGMA.
DO NOT REBUILD THE ROADMAP FROM ZERO.
DO NOT CREATE A PARALLEL SIGMA.
DO NOT REPLACE CURRENT AUTHORITY WITH A NEW DESIGN.
DO NOT MUTATE LIVE VKM/RUNTIME/HEAD/MODEL.
DO NOT CALL CANDIDATE STATE "LIVE".
DO NOT CALL LOCAL PASS "ADMISSION".

Continue from the existing ONE SIGMA state only.

ONE_SIGMA_NATIVE_IDENTITY_REQUIRED=
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

GitHub is archive/continuity only.
Oppo live measurement is current-state authority.

## 1. Read these files first, in this order

1. Sigma-VKM.Sigma_OS/MASTER_HANDOFF_ONE_SIGMA_2026-09-23_V4.md

Purpose:
master ONE SIGMA invariants, ownership boundaries, anti-fake contract.

2. Sigma-VKM.Sigma_OS/SIGMA_FINAL_CUTOVER_FINGERPRINT_MATRIX_2026-10-02.md

Purpose:
exact final admission/cutover fingerprint requirements and fail-closed matrix.

3. Sigma-VKM.Sigma_OS/SIGMA_REALBRAIN_B5_TO_ADMISSION_CUTOVER_ROADMAP_2026-10-01.md

Purpose:
major-gate roadmap from tokenizer/RealBrain work to admission and cutover.

4. Sigma-VKM.Sigma_OS/SIGMA_VM_YIELD_AUTOSUPERVISOR_V2_INSTALL_PASS_2026-10-02.md

Purpose:
current VM yield/autosupervisor contract:
AUTO_RESUME_REQUIRED=YES
UNATTENDED_DEAD_END=FORBIDDEN
INFINITE_RETRY=FORBIDDEN
SIGMA_MAX_STEPS=10000000

5. Sigma-VKM.Sigma_OS/SIGMA_RB_PRODUCTION_SEED_PLAN_PASS_2026-10-02.md

Purpose:
exact 32B/70B production seed plan and unresolved production weight payload boundary.

6. Sigma-VKM.Sigma_OS/SIGMA_RB_PRODUCTION_SEED_EXECUTOR_INSTALL_PASS_2026-10-02.md

Purpose:
seed executor, Tiny conformance, exact replay, server materialization boundary.

7. Sigma-VKM.Sigma_OS/SIGMA_OPPO_BEHAVIORAL_SEMANTIC_EVAL_INSTALL_PASS_2026-10-02.md

Purpose:
LATEST behavioral semantic gate boundary and next required work.

## 2. Latest active boundary

Latest proven behavioral boundary:

OPPO_BEHAVIORAL_SEMANTIC_EVAL_INSTALL=PASS
TRANSFORMER_DOES_SEMANTIC_EXAM=YES
GROUNDING_ANSWERS_FOR_MODEL=NO
SIX_BEHAVIORAL_CAPABILITIES_REQUIRED=YES
MODULE97_ACCEPT_REQUIRES_BEHAVIOR_GATE=YES
ARCHITECTURE_REDUCED=NO

OPPO_REAL_LEARNING_PROOF=PENDING_SOURCE_BOUND_EXAM

NEXT=
BUILD_SOURCE_BOUND_TRAIN_DEV_CORE_BEHAVIOR_WORKSETS

READY_FOR_6_AUTOLEARN_CORPORA=NO

SHADOW_POINTER_INITIALIZED=NO
PRODUCTION_ADMISSION_PERFORMED=NO
CUTOVER_PERFORMED=NO

This is the immediate coding boundary.

## 3. Work to do next

Build source-bound TRAIN / DEV / CORE behavioral worksets from the already-imported corpus.

Required pipeline:

existing corpus records
-> native deterministic traversal
-> source/source-cluster aware split
-> TRAIN / DEV / CORE
-> zero leakage
-> R21 provenance binding
-> R57 TRAIN-only learning
-> candidate checkpoint
-> DEV generalization
-> CORE retention
-> six transformer behavioral exams
-> Module97 behavioral ACCEPT/REJECT
-> R22 native policy
-> accepted SHADOW generation only

Do NOT treat Module97 ACCEPT as final admission.

## 4. Six mandatory behavioral capabilities

The transformer itself must be tested for:

1. referent_identity
2. relation_support
3. contradiction
4. scope_compatibility
5. evidence_support
6. cross_document_support

GROUNDING_ANSWERS_FOR_MODEL must remain NO.

Grounding may provide evidence structures/mechanics but must not answer the behavioral exam for the transformer.

## 5. Split requirements

"Zero overlap" does NOT mean record IDs only.

Require zero leakage across TRAIN / DEV / CORE for:

- exact content SHA256;
- document identity;
- source cluster;
- near-duplicate cluster;
- mirrors/syndication;
- derived paraphrase/translation family where applicable.

DEV generalization must not be TRAIN memorization under another record ID.

CORE must remain retention evidence, not training input.

## 6. Ownership chain

Keep this hierarchy:

R22 cognitive/autolearn policy
-> CORE SIGMA / RealBrain learning graph
-> VKM neutral mechanics
-> R21 storage/recovery

Module97 is a behavioral gate.
Module97 is NOT final admission authority.

Final production chain remains:

RealBrain gates
-> R22 READY
-> fresh-final
-> DNA15 Step6
-> atomic promotion
-> direct Oppo live re-measurement

Only then:
ADMISSION=COMPLETE
CUTOVER=COMPLETE

## 7. Production weight boundary

Do not forget:

PRODUCTION_WEIGHT_PAYLOAD_MATERIALIZED=NO
MODEL_V3_PRODUCTION_BINDING=PENDING_PRODUCTION_WEIGHT_PAYLOAD

The production seed executor exists and Tiny conformance passed, but 32B/70B production payload materialization remains unresolved.

Do not fake production readiness from seed-plan metadata.

## 8. Runtime/recovery contract

Preserve:

SIGMA_MAX_STEPS=10000000
VM_YIELD_STEP_BUDGET=PASS
VM_PROCESS_HARD_EXIT_ON_STEP_BUDGET=NO
AUTO_RESUME_REQUIRED=YES
UNATTENDED_DEAD_END=FORBIDDEN
INFINITE_RETRY=FORBIDDEN
BLOCKED_SAFE available
ROLLBACK_AVAILABLE=YES

Do not solve scale problems by permanently increasing production step limit.

## 9. Storage / anti-dup contract

Knowledge growth may create new unique immutable objects.

Replay must not create duplicates.

Preserve:
- content addressing;
- exact replay append=0;
- no second storage silo;
- no file-per-piece;
- no file-per-token;
- anti-dup;
- exactly-once effects.

## 10. What must NOT be redone

Do NOT redo from zero:

- tokenizer byte ABI;
- tokenizer persistence V2;
- pair statistics;
- Sigma piece policy;
- B7 generic two-phase growth engine;
- tokenizer accelerator architecture;
- production numerics contract;
- stochastic BF16 writeback;
- full AdamW checkpoint/replay;
- production seed plan;
- seed executor Tiny conformance;
- VM yield/autosupervisor;
- behavioral semantic gate infrastructure.

These are established checkpoints. Extend them; do not replace them.

## 11. First deliverable required from new coder

Produce one contained checkpoint proving:

SOURCE_BOUND_WORKSETS_V1

with at minimum:

SOURCE_RECORD_COUNT=<n>
TRAIN_COUNT=<n>
DEV_COUNT=<n>
CORE_COUNT=<n>

EXACT_CONTENT_OVERLAP=0
DOCUMENT_OVERLAP=0
SOURCE_CLUSTER_OVERLAP=0
NEAR_DUP_CLUSTER_OVERLAP=0

R21_PROVENANCE_BOUND=YES
HOST_SEMANTIC_SELECTION=NO
TRANSFORMER_BEHAVIOR_GATE_BOUND=YES

TRAIN_USED_FOR_LEARNING=YES
DEV_USED_FOR_TRAINING=NO
CORE_USED_FOR_TRAINING=NO

SIX_CAPABILITY_COVERAGE=<COUNTS>

FRESH_PROCESS_RESTORE=PASS
REPLAY_APPEND=0

LIVE_MUTATION=NO
ADMISSION=NO
CUTOVER=NO

## 12. After that checkpoint

Then run:

R57 source-bound TRAIN learning
-> candidate checkpoint
-> DEV generalization
-> CORE retention
-> six neural behavioral exams
-> Module97 decision

If ACCEPT:
candidate may continue as SHADOW generation.

It still must NOT become live production authority.

## 13. Fail-closed warnings

Stop and report BLOCKED_SAFE if any of these occur:

- native identity mismatch;
- source leakage across TRAIN/DEV/CORE;
- host performs semantic selection;
- grounding supplies behavioral answers;
- replay creates durable duplicates;
- candidate mutates live state;
- Module97 is used as final admission authority;
- production payload/model binding is claimed without materialization proof;
- old/external VM or parallel Sigma is introduced.

## Final instruction

Continue exactly from:
NEXT=BUILD_SOURCE_BOUND_TRAIN_DEV_CORE_BEHAVIOR_WORKSETS

Do not restart.
Do not redesign the architecture.
Do not replay completed historical milestones.
Do not mutate live authority.

ONE_SIGMA=YES
