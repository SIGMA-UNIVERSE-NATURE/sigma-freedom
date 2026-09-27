# SIGMA V09 -> VKM R5A4 Exact Native Supervision Chain Audit — Result

Date: 2026-09-27
Source: user-supplied Termux runtime output.
Branch: SIGMA_LIFE
Rule: CLAIM <= EVIDENCE

## Locked identities

R5A4_LOCKED_INPUT_IDENTITIES=PASS

SEM68 candidate source:
008d62f8120a112b0f4cfa27676e5d6f80f5b686c5aa76a080c568f04d0bee6b

Training curriculum:
ce02e548381fe25cfaf1b5890cb9cfad250f9f1bfb7eb601b9099282424c9414

Head registry:
7ee9bc9e9bc007490c0deed94463058a786b82d3952f039648bdce9fa6b33bf5

## Decision packet

ACTIVE_BUILDER_STATUS=UNBOUND
ACTIVE_BUILDER_CANDIDATES=NONE
GOLD_PRODUCER_COUNT=8
HOST_SEMANTIC_HIT_COUNT=0
TRAIN_CLOSURE_FUNCTION_COUNT=111
GAIN_HIT_COUNT=69
STORE_HIT_COUNT=163
R5B_TRAINING_AUTHORIZED=NO

## Important correction of interpretation

The eight items counted by the R5A4 harness as GOLD_PRODUCER_COUNT are not all proven semantic-value producers.

Observed repeated functions across the four builder variants include:

v927p_gold_clone_wrong_change_mask
- deliberately clones a probe with GOLD_CHANGE_MASK="WRONG_FIELD";
- this is a negative-control mutation function, not the producer of correct semantic gold.

v927p_sha256_lookup
- receives invariant_mask, change_mask, gold_source_span and mutation_operator as arguments;
- writes those supplied values into the record;
- therefore this is proven as a native field materializer/writer, but the upstream origin of the semantic values remains unresolved.

Accordingly:
GOLD_FIELD_WRITER_PATH_PROVEN=YES
GOLD_SEMANTIC_VALUE_ORIGIN_PROVEN=NO

## Native training computation

The exact current candidate contains a native training chain including:

AL68_train
 -> AL68_train_epoch
 -> AL68_train_one
 -> AL68_target
 -> AL68_head_dot / AL68_view_features / N_features / N_encode

and evaluation/loss paths including:

AL68_loss_one
 -> AL68_target
 -> AL68_view_features
 -> N_features
 -> N_encode
 -> AL68_head_dot

The current candidate also contains native state persistence calls through I_vsave/U_store and the underlying storage machinery.

This proves a substantial native train/loss/update mechanism exists, but does not yet establish the provenance of the semantic supervision values fed to that mechanism.

## Gain evidence

The current native candidate source emits TRAIN_BEFORE, TRAIN_AFTER, DEV_BEFORE and DEV_AFTER.

This is positive evidence that metric computation occurs in native source.

However R5A4 output provided here does not yet establish the exact native conditional that decides NATIVE_GAIN_GATE, so:
NATIVE_GAIN_DECISION_PROVEN=NOT_YET_FROM_R5A4_OUTPUT

## Host evidence

HOST_SEMANTIC_HIT_COUNT=0 within the exact targeted R5A4 scan scope.

This is useful negative evidence but is not a universal proof that no external layer ever supplied semantic values upstream.

## Boundary

ACTIVE_BUILDER_BOUND=NO
GOLD_FIELD_WRITER_NATIVE=YES
GOLD_SEMANTIC_VALUE_ORIGIN_PROVEN=NO
NATIVE_TRAINING_MECHANISM_EXISTS=YES
NATIVE_GAIN_DECISION_PROVEN=NOT_YET
HOST_SEMANTIC_SUBSTITUTION_ABSENT=NOT_YET_FULLY_PROVEN
R5B_TRAINING_AUTHORIZED=NO
GIA_ADMISSION_PERFORMED=NO
DNA15_ALLOWED=NO

NEXT=R5A5_ACTIVE_BUILDER_REVERSE_SEMANTIC_ORIGIN_AND_GAIN_AUTHORITY_AUDIT
