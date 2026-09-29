# SIGMA R22E — Provenance Finalize FIX2

Date: 2026-09-29
Source: user-supplied Termux runtime output.

R22E_PROVENANCE_FINALIZE_FIX2=PASS

FIX_REASON=
FINAL_REPLAY_OVERWROTE_TRANSIENT_CYCLE_RESULT_FILE

FIRST_RUN_RESULT_AUTHORITY=
R22E_RECEIPT_PLUS_NATIVE_DURABLE_VERIFIER

REPLAY_RESULT_AUTHORITY=
EXACTLY_ONCE_RECONCILIATION_ONLY

LEARNING_RERUN=NO
MODEL_RETRAINED=NO
STATE_MUTATION=NO

SELECTED_OBJECTIVE_SPEC_HASH=
47506c317a1f2aef24d8aab176273b88

SELECTED_OBJECTIVE_NAME=
masked_representation

PAIR_BEFORE_CURRICULUM=
604c740b63a9dc270cacc9445233f205

ACTUAL_TRAINING_PAIR=
6715aabd590535ff392ede4f3b7a8002

CURRICULUM_REORDERED_PAIR=YES

LEARNING_RESULT=MODEL_ACCEPTED

PRIVATE_MODEL=
466e9fcd423836d533d1d21c765e7e53

FIX2_RECEIPT_SHA256=
63da46ba172f8eaab2b1c289b7a4938cf63d33383ab9cab36a53a43ebe85f018

PRODUCTION_ADMISSION_ENABLED=NO
ADMISSION=NO

NEXT=
R22F_NATIVE_RESERVE_FIRST_CANDIDATE_EVALUATION

MANUAL_REBOOT_REQUIRED=NO

## Interpretation boundary

This FIX2 repairs provenance/result authority only.

It establishes:
- the final replay overwrote a transient cycle-result file;
- first-run learning authority is the R22E receipt plus native durable verifier;
- replay output is authoritative only for exactly-once reconciliation;
- no learning rerun occurred;
- the model was not retrained;
- state was not mutated;
- the selected objective spec hash maps to masked_representation;
- curriculum reordered the initially referenced pair before the actual training pair was used;
- the accepted private model remains 466e9fcd423836d533d1d21c765e7e53.

Production admission remains disabled and ADMISSION remains NO.
