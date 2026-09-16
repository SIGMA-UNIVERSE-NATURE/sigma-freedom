# G3C R3H Evidence-Profile Readout Precommit — 2026-09-16

```text
HANDOFF_ID=G3C_R3H_EVIDENCE_PROFILE_READOUT_PRECOMMIT_20260916
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

Parent HOLD checkpoint:

```text
BRAIN/GENERATIONS/G3_LEARNED_NARRATIVE_BRAIN/G3C_R3G_SEED104729_GATE_HOLD_20260916.md
COMMIT=b5beb4aa6e2b5edc0c35dbe6cac8111b0558b973
BLOB=8c27f9c2e91178ac2f586c7e6ebc288ab52ad860
```

R3G showed that TRAIN-only arbitration over only two scalar branch-level features did not generalize: fixed-sum 14/40, raw learned 13/40, gated 12/40. R3H therefore stops branch arbitration and changes the candidate-conditioned evidence representation/readout itself.

## Exact artifact identity before first R3H DEV result

```text
ARTIFACT=SIGMA_G3C_EVIDENCE_PROFILE_R3H_CANDIDATE
BUNDLE_SHA256=3f0c53fd57b74ff52704de521fad55ff4bcfaafb9e3770c0350b201e551d8b51
SOURCE_SHA256=f00d09b2eeb96adfeb9f2db300806a6355c120baab9da434e84129ed3b9ef451
RUNNER_SHA256=fff2987e9a2144bbf2755de366df5bf71ae8d0d3af8aaad88d0552b118b6fee3
MANIFEST_SHA256=b731bf8a15c361e26d935f64d2b50d5f5f2fb9c5239c032853d591245501c17c
NATIVE_COMPILE=NOT_YET_PROVEN_ON_OPPO
```

## Frozen candidate-conditioned evidence profile

R3H preserves the locked R2 base model and extends the R3A candidate-conditioned evidence trace with generic structural summaries only:

```text
1=FINAL_RECURRENT_MEMORY_COMPATIBILITY
2=STRONGEST_LOCAL_SUPPORT
3=LATEST_LINE_SUPPORT
4=MEAN_LOCAL_SUPPORT
5=PEAK_GAP_BEST_MINUS_SECOND_BEST
6=BEST_EVIDENCE_NORMALIZED_POSITION
7=LATE_MINUS_EARLY_MEAN_SUPPORT_SHIFT
8=RECENCY_WEIGHTED_SUPPORT
9=LOCAL_SUPPORT_DISPERSION
```

The fixed-sum control remains exactly channels `1+2+3`. The learned ranker begins at weights `1,1,1,0,0,0,0,0,0`, so its initial ranking is identical to R3A fixed-sum before learning.

These features encode no story word, role label, answer string, semantic opcode, or phrase rule.

## Frozen TRAIN-only direct ranking objective

```text
TRAIN_SOURCE=R2_PUBLIC_TRAIN_160_ONLY
DEV_LABEL_TRAINING=NO
EPOCHS=4
STORY_TICKS=640
POSITIVE=OBSERVED_FINAL_ANSWER_LINE_FROM_PUBLIC_TRAIN_STORY
NEGATIVE_CONSTRUCTION=NATIVE_UNIQUE_SAME_STORY_SURFACE_COUNTERFACTUAL
NEGATIVE_SELECTION=TOP_4_HARDEST_UNIQUE_COUNTERFACTUALS_UNDER_PRE_UPDATE_READOUT
PAIRWISE_MARGIN=0.08
NORMALIZED_GRADIENT=YES
BASE_MODEL_LEARNING=NO
HOST_STORY_SELECTION=NO
HOST_COGNITION=NO
```

R3H trains the candidate ranker directly and has no fixed-vs-learned arbitration gate.

## Frozen evaluation protocol

```text
SOURCE_MODELS=SIGMA_CURRICULUM_WITH_REPLAY
SEEDS=104729;130363;155921
EVALUATION=DEV_ONLY
FIXED_SUM_CONTROL=R3A_MEMORY_PLUS_BEST_LOCAL_PLUS_LATEST
DEV_KEY_SCOPE=HOST_EVALUATOR_ONLY_AFTER_NATIVE_INFERENCE
BLIND_USED=NO
SEALED_R4_USED=NO
```

## Precommitted stop gate

Seed 104729 is the first stop gate.

```text
FIXED_SUM_SEED_104729_REFERENCE=14/40
LEARNED_GT_FIXED_SUM_SEED_104729=PASS_REQUIRED
EQUALITY_IS_PASS=NO
PREDICTION_CHANGES_VS_FIXED_GT_0=REQUIRED
NO_NEW_ABSOLUTE_POSITIONAL_COLLAPSE=PASS_REQUIRED
BASE_MODEL_UNCHANGED=PASS_REQUIRED
CANONICAL_UNCHANGED=PASS_REQUIRED
BLIND_USED=NO_REQUIRED
SEALED_R4_USED=NO_REQUIRED
HOST_COGNITION=NO_REQUIRED
```

If seed 104729 does not strictly exceed 14/40, stop and checkpoint HOLD. If it passes, run seeds 130363 and 155921 under the identical frozen protocol; final R3H success requires learned > fixed-sum on every seed and aggregate.

## Forbidden

```text
STORY_SPECIFIC_RULES=FORBIDDEN
PHRASE_SPECIFIC_RULES=FORBIDDEN
EXPECTED_ANSWER_LEAKAGE=FORBIDDEN
SEMANTIC_VM_OPCODE=FORBIDDEN
DEV_LABEL_TRAINING=FORBIDDEN
DEV_THRESHOLD_TUNING=FORBIDDEN
BLIND_TUNING=FORBIDDEN
SEALED_R4_ACCESS=FORBIDDEN
```

## Claim boundary

Even an R3H DEV gate pass proves only that the richer candidate-conditioned evidence profile and direct TRAIN-only ranker improve DEV candidate ranking over the R3A fixed-sum control under this exact protocol. It does not prove semantic understanding, late-evidence revision, role-swap reasoning, chronology-versus-causality, unresolved-state retention, final causal synthesis, whole-story understanding, or G3 promotion.

NEXT_ACTION=INSTALL_HASH_VERIFY_COMPILE_AND_RUN_SEED_104729_DEV_ONLY
