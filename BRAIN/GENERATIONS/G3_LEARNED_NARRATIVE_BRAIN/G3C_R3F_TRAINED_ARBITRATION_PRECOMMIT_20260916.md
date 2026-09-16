# G3C R3F TRAIN-Learned Arbitration Precommit — 2026-09-16

```text
HANDOFF_ID=G3C_R3F_TRAINED_ARBITRATION_PRECOMMIT_20260916
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
BRAIN/GENERATIONS/G3_LEARNED_NARRATIVE_BRAIN/G3C_R3E_SEED104729_GATE_HOLD_20260916.md
COMMIT=e9c9db295b6ab23b5d94d7d51f649d9b7e5112ff
```

R3E tied fixed-sum because its frozen hand threshold produced zero gate fires. R3F removes hand threshold selection entirely. The arbitration function itself is learned only from public TRAIN behavior before DEV is evaluated.

## Exact artifact identity before first DEV result

```text
ARTIFACT=SIGMA_G3C_TRAINED_ARBITRATION_R3F_CANDIDATE
BUNDLE_SHA256=b9ac624d1b83c51184599fb34aa2ac9c6161e367228c3782c188794a01e01b18
SOURCE_SHA256=45786bf50d32b8f3c5d3fd9209c0f379cd31dc0c355f660ab9e76ab964cf7c56
RUNNER_SHA256=48da0f0ff96b1651e733e90e48e2cabd60c3a539968bf71651894e458ebcbf0d
MANIFEST_SHA256=6314e9f83e07c085ce0dd311b98385a11796c5b1bcf3f38c278081cbdec5f06b
NATIVE_COMPILE=NOT_YET_PROVEN_ON_OPPO
```

## Frozen substrate

R3F keeps the R3A evidence channels and R3D learned residual path. The R2 base model is read-only.

```text
READOUT_FEATURES=FINAL_MEMORY;STRONGEST_LOCAL;LATEST;MEMORY_X_LOCAL;MEMORY_X_LATEST;LOCAL_X_LATEST
READOUT_OBJECTIVE=IN_CONTEXT_COUNTERFACTUAL_PAIRWISE_MARGIN
READOUT_TRAIN_SOURCE=PUBLIC_TRAIN_160_ONLY
READOUT_EPOCHS=4
READOUT_NATIVE_TICKS=640
```

## TRAIN-only arbitration learner

After the readout is locked, a separate 3-parameter native gate is trained only on public TRAIN stories.

```text
GATE_FEATURES=SOFT_FIXED_TOP_MARGIN;SOFT_LEARNED_ADVANTAGE_OVER_FIXED_CHOICE;BIAS
GATE_INITIAL_WEIGHTS=0;0;-0.05
GATE_OBJECTIVE=PAIRWISE_MARGIN_CLASSIFICATION
GATE_MARGIN=0.08
GATE_EPOCHS=4
GATE_MAX_NATIVE_TICKS=640
```

For each TRAIN story, native SIGMA forms the same-story candidate pool from the observed final answer and generic counterfactual surface substitutions. An arbitration example is informative only when fixed-sum and raw learned differ in TRAIN correctness on that candidate pool:

```text
LABEL_OVERRIDE=1  iff RAW_LEARNED_IS_CORRECT and FIXED_SUM_IS_WRONG
LABEL_OVERRIDE=0  iff FIXED_SUM_IS_CORRECT and RAW_LEARNED_IS_WRONG
OTHER_CASES=NO_GATE_UPDATE
```

No DEV label, blind label, sealed R4 content, story-specific rule, phrase-specific rule, semantic role label, or host cognition enters gate training.

## Frozen inference

```text
BASE_DECISION=FIXED_SUM_TOP
RAW_LEARNED_DECISION=R3D_STYLE_LEARNED_TOP
IF RAW_LEARNED_TOP_DIFFERS_FROM_FIXED_TOP AND TRAIN_LEARNED_GATE_SCORE_GT_0:
    FINAL=RAW_LEARNED_TOP
ELSE:
    FINAL=FIXED_SUM_TOP
```

There is no DEV-derived threshold.

## Frozen evaluation protocol

```text
SOURCE_MODELS=SIGMA_CURRICULUM_WITH_REPLAY
SEEDS=104729;130363;155921
EVALUATION=DEV_ONLY
DEV_KEY_SCOPE=HOST_EVALUATOR_ONLY_AFTER_NATIVE_INFERENCE
BLIND_USED=NO
SEALED_R4_USED=NO
```

## Precommitted stop gate

Seed 104729 is the first stop gate.

```text
FIXED_SUM_SEED_104729_REFERENCE=14/40
GATED_GT_FIXED_SUM_SEED_104729=PASS_REQUIRED
EQUALITY_IS_PASS=NO
GATE_INFORMATIVE_TRAIN_EXAMPLES_GT_0=REQUIRED
GATED_PREDICTION_CHANGES_VS_FIXED_GT_0=REQUIRED
NO_NEW_ABSOLUTE_POSITIONAL_COLLAPSE=PASS_REQUIRED
BASE_MODEL_UNCHANGED=PASS_REQUIRED
CANONICAL_UNCHANGED=PASS_REQUIRED
BLIND_USED=NO_REQUIRED
SEALED_R4_USED=NO_REQUIRED
HOST_COGNITION=NO_REQUIRED
```

If seed 104729 is not strictly above 14/40, stop and checkpoint HOLD. If it passes, run seeds 130363 and 155921 under the identical frozen protocol; final R3F success requires gated > fixed-sum on each seed and aggregate.

## Claim boundary

Even a R3F DEV pass proves only that TRAIN-supervised arbitration improves candidate ranking over fixed-sum on the existing DEV partition under the frozen protocol. It does not prove semantic understanding, revision reasoning, role-swap reasoning, causality, final causal synthesis, whole-story understanding, or G3 promotion.

NEXT_ACTION=INSTALL_HASH_VERIFY_COMPILE_AND_RUN_SEED_104729_DEV_ONLY
