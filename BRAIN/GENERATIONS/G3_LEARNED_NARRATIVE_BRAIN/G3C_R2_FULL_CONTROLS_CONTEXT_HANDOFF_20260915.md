# G3C R2 Full-Controls Context Handoff — 2026-09-15

```text
HANDOFF_ID=G3C_R2_FULL_CONTROLS_CONTEXT_HANDOFF_20260915
SYSTEM_IDENTITY=SIGMA.AIL
LANE=G3C_STATE_TRACKING_PILOT
SESSION_CODE=SF07900DEB302
CURRENT_PROGRAM_GENERATION=G2_ONE_SIGMA_AIL
G3_STATUS=CANDIDATE_TRACK_ACTIVE_NOT_PROMOTED
TARGET_HEAD=700d5c1b4845322d7c14800029c629b0
TARGET_MODEL_GENERATION=1
TARGET_MODEL=25f78a8a17d8ec8957545f2f747170c0
G3_PROMOTION=NO
CANONICAL_BRAIN_MODEL_MUTATION_FOR_PILOT=NO
FROZEN20_TRAINING_USE=FORBIDDEN
EXTERNAL_R3_TRAINING_USE=FORBIDDEN_AFTER_RESULTS
HOST_COGNITION=NO
HOST_TEST_ORACLE=NO
```

## Why this handoff exists

The active chat/context reached its practical limit while G3C had just entered the R2 full-controls pilot. This file is the continuation checkpoint. It records only observed machine outputs, hash-bound artifacts, and already-published diagnostic checkpoints. It is not a G3 promotion artifact.

## G3B diagnosis that defines the teaching target

Frozen-20 generation-1 mechanical evaluation reached 20/20 summary artifacts at 10,000 words each while keeping the target HEAD/model/model-generation bound and the canonical HEAD unchanged. That result was explicitly mechanical only; semantic correctness and G3 promotion were not proven.

The subsequent Frozen-20 semantic diagnostic found strong extractive source fidelity but semantic prioritization was not demonstrated, final causal synthesis was absent, and whole-story understanding was not proven. The observed selection was close to stratified positional sampling.

A second independent external diagnostic R3 sharpened the same error profile:

```text
EXTERNAL_R3_MECHANICAL_12_OF_12=YES
TRACE_REGION_DECISIONS=72
TRACE_ANCHOR_EQUALS_REGION_START=72_OF_72
TRACE_ANCHOR_SCORE_UNIQUE_VALUE=0.05
POSITION_DOMINANCE=STRONGLY_OBSERVED
SEMANTIC_SELECTIVITY=NOT_DEMONSTRATED
LATE_EVIDENCE_RETENTION=WEAK
REVISION_RETENTION=WEAK
FINAL_CAUSAL_SYNTHESIS=FAIL
WHOLE_STORY_UNDERSTANDING=NOT_PROVEN
G3_PROMOTION=NO
TRAIN_ON_R3_AFTER_RESULTS=FORBIDDEN
```

R3 commit:

```text
3db72abc7192078fe5476651eb33d972ec480a94
```

R3 path:

```text
BRAIN/GENERATIONS/G3_LEARNED_NARRATIVE_BRAIN/G3B_EXTERNAL_SEMANTIC_DIAGNOSTIC_R3_RESULT_20260915.md
```

Therefore G3C teaching remains focused on separate-corpus learned state tracking, semantic selectivity, late evidence/revision, role binding, chronology-versus-causality, unresolved-state retention, semantic planning, and only later 10k→1k compression. Frozen-20 and external R3 are evaluation material, not training data.

## Locked G3C pilot contract

The pilot corpus is separate from Frozen-20 and remains fixed:

```text
TRAIN=160
DEV=40
BLIND=80
BLIND_GROUPS=4x20
FAMILY_PARTITION_OVERLAP=NO
CORPUS_MANIFEST_SHA256=347e2d36f68366ed98bf79576dbf23e06a4a6e4033909a5b9e16d16384adf183
```

Blind groups are: new names/surface phrasing; role swaps; longer chains plus distractors; late evidence including revise / do-not-revise / insufficient-evidence cases.

The learner path must remain native `.sigma`: order-preserving learned encoder, learned per-segment memory updater, next-segment compatibility scorer, contrastive observed-next learning, replay, and native curriculum/item selection. Host may transport bytes, launch VM, hash, checkpoint, rollback mechanical partial transactions, and persist receipts. Host may not inject semantic labels, semantic graphs, blind answers, story selection, or semantic verdicts.

The full pilot comparison remains three conditions across three pre-locked seeds:

```text
NO_WEIGHT_UPDATE
RANDOM_ORDER_PLUS_REPLAY
SIGMA_SELECTED_CURRICULUM_PLUS_REPLAY
SEEDS=3
```

Blind is one-shot after model lock. Proposed success threshold remains at least 18/20 correct stories in each blind group and better than the no-learning condition. Curriculum efficiency may be claimed only by higher score at equal cost or same score at lower cost. Restart continuity and replay retention are mandatory. A changed hash or lower loss alone is not story understanding.

## R1 learning-path evidence — completed

R1 first encountered a native VM step-limit failure. FIX1 split learning into native checkpointed single-pair ticks without weakening the curriculum. A later tick was killed by SIGKILL (`-9`) at tick 328. Machine inspection showed a clean checkpoint:

```text
MODEL_UPDATES=258
STATE_UPDATES=258
STATE_ACCEPTED=258
MODEL_STATE_UPDATE_DELTA=0
```

A single infrastructure retry of the same checkpoint advanced consistently to 259/259 with delta 0. FIX2 then resumed the same existing run with host-side pre-tick byte snapshots / rollback mechanics while leaving native cognition unchanged. The completed machine result was:

```text
RESULT=G3C_TRAIN16_LEARNING_PATH_ACTIVE
LOSS_BEFORE=0.562498342187
LOSS_AFTER=0.562476117902
ENCODER_DELTA=0.003136641855
MEMORY_DELTA=0.018100966468
UPDATES_ATTEMPTED=621
UPDATES_ACCEPTED=621
LEARNING_PATH_ACTIVE=1
FROZEN20_USED=0
HOST_COGNITION=NO
HOST_STORY_SELECTION=NO
EXECUTION_PROTOCOL=NATIVE_CHECKPOINTED_SINGLE_PAIR_TICKS
VM_TICK_COUNT_THIS_INVOCATION=431
VM_RETRY_ATTEMPTS_THIS_INVOCATION=0
VM_ROLLBACKS_VERIFIED_THIS_INVOCATION=0
CANONICAL_HEAD_UNCHANGED=PASS
CANONICAL_MODEL_GENERATION_UNCHANGED=PASS
PILOT_MODEL_SHA256=2eefc7f8c8a63a05f96a7d411b596feef1c36ff55374575643a7a216d41c09c1
RECEIPT_SHA256=232577a2b183751606ee74b7d51543220b86e9c964786336bffe23715d1e100d
```

R1 final receipt path on the OPPO machine:

```text
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/WORKSPACES/SF07900DEB302/artifacts/SIGMA_G3C_STATE_TRACKING_PILOT_R1_FIX1_CANDIDATE/runs/train16_20260915_165146_4752/TRAIN16_RESUME_MACHINE_RECEIPT.json
```

R1 source/bytecode identities used for the successful path:

```text
SOURCE_SHA256=58acc3c204ae3c480bb271c31ccd92cf178373e6a709eeebceb5d27a54162d6b
BYTECODE_SHA256=67d2f785558233e0012d70b2bb9f1fe4caea78f06d69b4dbf41264d2e78020a7
```

Interpretation boundary: this proves a real active learning path in both encoder and memory-updater parameter blocks with a small loss decrease. It does not yet prove unseen generalization, role-swap understanding, late-evidence revision, semantic selectivity, or story understanding.

## R2 full-controls candidate — current active work

The original R2 candidate failed compiler parsing at line 473 (`unsupported statement (token=:)`). R2 FIX1 corrected only the malformed source statements; corpus, conditions, seeds, evaluator, control contract, and R1 gate binding were unchanged.

R2 FIX1 artifact identities:

```text
BUNDLE_SHA256=9a327f2f93abb976d28e6242b3aac31abe6d82cd3bfdcf2003dda5de512c0949
SOURCE_SHA256=850c969671421d4b95f2152d5935a856e3dac4fc697ab2dc97f11cba2f09c960
RUNNER_SHA256=b748ad29b74e1eab07f1630ff4978c22cc349754c1e9eee6e66e9f2cc1a9c082
CORPUS_MANIFEST_SHA256=347e2d36f68366ed98bf79576dbf23e06a4a6e4033909a5b9e16d16384adf183
```

R2 FIX1 preflight passed on the actual OPPO runtime:

```text
RESULT=G3C_R2_PREFLIGHT_PASS
R1_LEARNING_PATH_GATE=BOUND_AND_VERIFIED
NATIVE_RESULT=G3C_R2_PREFLIGHT_READY
TRAIN=160
DEV=40
BLIND=80
CONDITIONS=3
SEEDS=3
PAIR_BUDGET_MIN=1664
FROZEN20_TRAINING_USE=NO
HIDDEN_KEYS_EXPOSED_TO_NATIVE=NO
HOST_COGNITION=NO
CURRICULUM_SELECTION_NATIVE=YES
CANONICAL_HEAD_UNCHANGED=PASS
CANONICAL_MODEL_GENERATION_UNCHANGED=PASS
SOURCE_SHA256=850c969671421d4b95f2152d5935a856e3dac4fc697ab2dc97f11cba2f09c960
BYTECODE_SHA256=b9095c02244ce8290d7919b71161add261600f978b76dbdcce81c5e9fef4744b
CORPUS_MANIFEST_SHA256=347e2d36f68366ed98bf79576dbf23e06a4a6e4033909a5b9e16d16384adf183
RECEIPT_SHA256=eaea6545f09882f90cc425ab5ba34df4481f87fb4e11d1598f3542cbc7baed0b
```

Preflight receipt path:

```text
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/WORKSPACES/SF07900DEB302/artifacts/SIGMA_G3C_STATE_TRACKING_PILOT_R2_FIX1_FULL_CONTROLS_CANDIDATE/runs/preflight_20260915_180730_17333/PREFLIGHT_R2_MACHINE_RECEIPT.json
```

## Latest machine state at handoff

R2 has just initialized the first control run:

```text
RESULT=G3C_R2_RUN_INITIALIZED
CONDITION=NO_WEIGHT_UPDATE
SEED=104729
INITIAL_MODEL_SHA256=70da3e9e719ae0e72e88add59d6b7752fe732319b8fc7590170a050ef860005e
CANONICAL_HEAD_UNCHANGED=PASS
CANONICAL_MODEL_GENERATION_UNCHANGED=PASS
RUN_DIRECTORY=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/WORKSPACES/SF07900DEB302/artifacts/SIGMA_G3C_STATE_TRACKING_PILOT_R2_FIX1_FULL_CONTROLS_CANDIDATE/runs/no_weight_update_seed104729_20260915_181535_24405
```

No R2 training/control result beyond this initialization is claimed in this handoff.

## Continuation rules

Continue from the already-initialized `NO_WEIGHT_UPDATE / seed 104729` run using the R2 FIX1 bundle's own README/runner interface; do not invent commands or restart the run from a fresh model unless the runner contract requires it. Preserve identical architecture/data source and comparable budgets across all three conditions and all three seeds. Do not access blind gold from the learner path. Do not train on Frozen-20 or external R3. Do not claim semantic understanding from loss reduction or parameter movement.

Before any later claim of pilot success, require direct machine evidence for all applicable gates: per-group blind scores, comparison against no-learning control, 3-seed results, restart equivalence including provenance, replay-retention regression <=5 percentage points under the pilot proposal, VM-step/time cost, model pre/post hashes, source/bytecode/corpus/evaluator hashes, and unchanged canonical HEAD/model-generation unless separately admitted.

If any run fails mechanically, preserve the exact checkpoint and receipts, inspect first, and do not silently rerun or weaken a gate.

## Current claim boundary

```text
R1_REAL_LEARNING_PATH=PASS
R1_ENCODER_PARAMETER_MOVEMENT=YES
R1_MEMORY_UPDATER_PARAMETER_MOVEMENT=YES
R1_LOSS_DECREASE=YES
R2_PREFLIGHT=PASS
R2_FIRST_CONTROL_INITIALIZED=YES
R2_FULL_3x3_CONTROLS=NOT_YET_RUN
UNSEEN_GENERALIZATION=NOT_YET_PROVEN
ROLE_SWAP=NOT_YET_PROVEN
LATE_EVIDENCE_REVISION=NOT_YET_PROVEN
RESTART_RETENTION=NOT_YET_PROVEN
BEATS_NO_LEARNING=NOT_YET_PROVEN
BEATS_POSITIONAL_BASELINE=NOT_YET_PROVEN
SEMANTIC_PRIORITIZATION=NOT_YET_PROVEN
FINAL_CAUSAL_SYNTHESIS=NOT_YET_PROVEN
WHOLE_STORY_UNDERSTANDING=NOT_PROVEN
G3_PROMOTION=NO
```
