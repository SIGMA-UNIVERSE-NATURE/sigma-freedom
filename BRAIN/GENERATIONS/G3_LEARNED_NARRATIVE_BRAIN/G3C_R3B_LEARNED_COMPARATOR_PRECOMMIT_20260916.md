# G3C R3B Learned Comparator Precommit — 2026-09-16

```text
HANDOFF_ID=G3C_R3B_LEARNED_COMPARATOR_PRECOMMIT_20260916
SYSTEM_IDENTITY=SIGMA.AIL
LANE=G3C_LEARNED_NARRATIVE_CORE
CURRENT_PROGRAM_GENERATION=G2_ONE_SIGMA_AIL
TARGET_GENERATION=G3_LEARNED_NARRATIVE_BRAIN
G3_PROMOTION=NO
CANONICAL_MODEL_MUTATION=NO
HOST_COGNITION=NO
HOST_TEST_ORACLE=NO
BLIND_ACCESS=FORBIDDEN
SEALED_G3B_R4_ACCESS=FORBIDDEN
FROZEN20_TRAINING_USE=FORBIDDEN
EXTERNAL_R3_TRAINING_USE=FORBIDDEN
```

Parent checkpoint:

```text
BRAIN/GENERATIONS/G3_LEARNED_NARRATIVE_BRAIN/G3C_R3A_EVIDENCE_TOOL_DEV_DIAGNOSTIC_CHECKPOINT_20260916.md
COMMIT=a3305183247da4dbafba1bec3344be053342cdc4
BLOB=97042b463cf6869705583a7f374d9017cdb49f16
```

R3A established a useful but non-final evidence substrate: R2 DEV total 28/120 -> R3A 38/120, with WRONG_TO_RIGHT=25 and RIGHT_TO_WRONG=15. The original absolute region-start pathology was mechanically broken (22/120 region-start, 56/120 middle, 42/120 latest), but semantic correctness remains unproven.

## R3B exact candidate identity before first DEV result

```text
ARTIFACT=SIGMA_G3C_LEARNED_COMPARATOR_R3B_CANDIDATE
BUNDLE_SHA256=171264655168ac6d029f9997b33d587cfb7eca492822c027aee390e3bee09afd
SOURCE_SHA256=bfac9a884f9703e3cb270087aabab548093b2bc39865f40c485349d34b4e2f4a
RUNNER_SHA256=c66b2b59d2a88050016d9f0b559768d934bba2ba2cdc6f91c8edda8f84b6baf9
MANIFEST_SHA256=f56a8483e6179701db1f777d39d8b474518e523f5a734b969397f0568d9f2af5
NATIVE_COMPILE=NOT_YET_PROVEN_ON_OPPO
```

R3B preserves the R3A evidence substrate and replaces only the fixed equal-weight sum with an isolated learned readout over:

```text
1=FINAL_RECURRENT_MEMORY
2=STRONGEST_CONTEXT_LINE_SUPPORT
3=LATEST_CONTEXT_LINE_SUPPORT
4=BIAS
```

The base R2 model is read-only and must remain byte-identical. The readout begins at `1,1,1,0`, which preserves the fixed-sum ranking before learning.

## Frozen training protocol

The protocol is fixed before observing any R3B DEV result:

```text
TRAIN_SOURCE=R2_PUBLIC_TRAIN_160_ONLY
DEV_LABEL_TRAINING=NO
EPOCHS=3
STORIES_PER_EPOCH=160
NATIVE_TICKS=480
NEGATIVE_SELECTION=NATIVE_HARDEST_OF_4_DETERMINISTIC_CROSS_STORY_FINAL_ANSWER_CANDIDATES
READOUT_LEARNING=NATIVE_SIGMA
BASE_MODEL_LEARNING=NO
HOST_STORY_SELECTION=NO
HOST_COGNITION=NO
```

For each training story, the observed final answer line is the positive training candidate. Four deterministic answer lines from other training stories are compared against the current story context; native SIGMA chooses the currently hardest negative. No DEV or blind label participates in this learning path.

## Frozen evaluation protocol

```text
SOURCE_MODELS=SIGMA_CURRICULUM_WITH_REPLAY
SEEDS=104729;130363;155921
EVALUATION=DEV_ONLY
FRESH_VM_PROCESS_PER_DEV_QUERY=YES
FIXED_SUM_CONTROL_EMITTED_FROM_SAME_EVIDENCE_CHANNELS=YES
DEV_KEY_SCOPE=HOST_EVALUATOR_ONLY_AFTER_NATIVE_INFERENCE
BLIND_USED=NO
SEALED_R4_USED=NO
```

## Precommitted R3B gate

R3B may be called a successful learned-readout remediation candidate only if all are machine-proven:

```text
ALL_THREE_SEEDS_REPORTED=YES
LEARNED_GT_FIXED_SUM_SEED_104729=PASS
LEARNED_GT_FIXED_SUM_SEED_130363=PASS
LEARNED_GT_FIXED_SUM_SEED_155921=PASS
AGGREGATE_LEARNED_GT_FIXED_SUM=PASS
NO_NEW_ABSOLUTE_POSITIONAL_COLLAPSE=PASS
BASE_MODEL_UNCHANGED=PASS
CANONICAL_UNCHANGED=PASS
BLIND_USED=NO
SEALED_R4_USED=NO
HOST_COGNITION=NO
```

A changed readout hash, lower pair loss, or improvement on only a subset of seeds is not enough to pass this gate.

## Forbidden

```text
STORY_SPECIFIC_RULES=FORBIDDEN
PHRASE_SPECIFIC_RULES=FORBIDDEN
EXPECTED_ANSWER_LEAKAGE=FORBIDDEN
SEMANTIC_VM_OPCODE=FORBIDDEN
DEV_LABEL_TRAINING=FORBIDDEN
BLIND_TUNING=FORBIDDEN
SEALED_R4_ACCESS=FORBIDDEN
```

## Claim boundary

Even if the R3B DEV gate passes, it proves only that a small learned comparator improves candidate ranking over the R3A fixed-sum diagnostic on the pre-existing DEV partition under this exact protocol. It does not prove late-evidence revision, role-swap generalization, chronology-versus-causality, final causal synthesis, whole-story understanding, or G3 promotion.

NEXT_ACTION=INSTALL_HASH_VERIFY_COMPILE_AND_RUN_SEED_104729_DEV_ONLY
