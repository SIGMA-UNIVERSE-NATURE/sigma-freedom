# SIGMA V09 -> VKM R5A3 Trainer + Curriculum Provenance Body Audit — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Mode: READ_ONLY_TARGETED_SOURCE_BODY_AUDIT

## Trigger

R5A2 proved:
- current native SEM68 candidate source exists;
- Σ.MAIN calls AL68_train / AL68_eval_saved_dev / AL_native_eval / G3_train / N_train;
- current curriculum contains 192 records;
- the curriculum schema includes GOLD_CHANGE_MASK, GOLD_INVARIANT_MASK and GOLD_SOURCE_SPAN;
- current gap classification is DATA_INSUFFICIENT;
- CANDIDATE_ADMITTED=NO;
- NEXT_REQUIRED_ACTION=AUTONOMOUS_ACQUIRE_FRESH_NONFROZEN_DATA.

Before any training, exact source evidence is required to determine whether GOLD fields are produced by native SIGMA or by host semantic supervision.

## R5A3 scope

Read-only extraction of exact source bodies for:
AL68_train
AL68S_train_batch
AL68_eval_saved_dev
AL68S_eval_batch
AL_native_eval
N_train
G3_train
N_model
G3_model_generation
N_features
AL68_RAW_FEATURES
AL68_RAW_ENCODE
AL68_RAW_PAIR
AL68_RAW_G3_SCORE

Also:
- trace source references to GOLD_CHANGE_MASK / GOLD_INVARIANT_MASK / GOLD_SOURCE_SPAN;
- mechanically classify source files as native Sigma source, host code, data JSONL, or metadata;
- locate head-store/train/eval write paths;
- do not dump gold row values;
- do not execute any discovered trainer/evaluator/source.

## Boundaries

CANONICAL_MUTATION_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
GIA_ADMISSION_ALLOWED=NO
DNA15_ALLOWED=NO
TRAINING_ALLOWED=NO
SEMANTIC_EXECUTION_ALLOWED=NO

R4E_HOLD_PRESERVED=YES

## Release

BUNDLE=
SIGMA_V09_TO_VKM_R5A3_TRAINER_CURRICULUM_PROVENANCE_BODY_AUDIT_BUNDLE.zip

BUNDLE_SHA256=
f5f973a1ea1d16ad814bc72a0bf80fb2d3946cfe57ea287bb4f59ae27bcfd932

R5A3_RELEASE_VERIFY=PASS

NEXT=RUN_R5A3
