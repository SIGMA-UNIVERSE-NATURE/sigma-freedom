# DNA-14 Native Admission V1 — POST-VM ALIGNMENT FAILURE

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Evidence state

DNA_ID=DNA-14
SOURCE_PATH=DNA14_PERSISTENCE_ENGINE_NATIVE_V1.sigma
SOURCE_SHA256=a18d240fd9b786b63babb01ee19fa687caaa860c43913f7fdbad6dcf41944b16
BYTECODE_SHA256=96781abf75bddaa01322ccc33ad0a1372b59392e33f3c0f2fee0fdd86c1c8d86
TOTAL_VM_INVOCATIONS=50
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
SENTINEL_FAIL_COUNT=0
POST_VM_ALIGNMENT_PASS_COUNT=28
POST_VM_ALIGNMENT_FAIL_COUNT=22
REPLAY_IDENTICAL_INPUT_DECISION=YES
DYNAMIC_INPUT=YES
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PYTHON_USED=NO
ADMISSION=FAIL
RESULT=FAIL_IN_TESTED_SCOPE

## Exact observed mismatch from replay cases 049/050

VM output preserved new-information slots by original AFTER position:

- A1 matched an existing BEFORE token, therefore `NEW_INFORMATION_1=NONE`.
- A2 was genuinely new, therefore `NEW_INFORMATION_2=<dynamic A2 token>`.
- `NEW_INFORMATION_COUNT=1`.

The V1 shell oracle compacted all new tokens into a left-packed array and therefore expected the A2 token in `NEW_INFORMATION_1` and `NONE` in `NEW_INFORMATION_2`.

This is an oracle expectation mismatch. The raw VM behavior is consistent with the native source implementation:

- N1 corresponds to A1 when G1 is true, else NONE.
- N2 corresponds to A2 when G2 is true, else NONE.
- N3 corresponds to A3 when G3 is true, else NONE.
- N4 corresponds to A4 when G4 is true, else NONE.
- a separate list compacts only non-NONE tokens for `NEW_INFORMATION_COUNT`.

Therefore:

POSITIONAL_NEW_INFORMATION_OUTPUT=SOURCE_ALIGNED_IN_OBSERVED_REPLAY
V1_SHELL_COMPACT_SLOT_ORACLE=INCORRECT_IN_OBSERVED_REPLAY
ROOT_CAUSE_SCOPE=POST_VM_ORACLE_POSITIONAL_EXPECTATION
SOURCE_SEMANTIC_FIX_REQUIRED=NO_EVIDENCE
RUNNER_ORACLE_FIX_REQUIRED=YES

## Claim boundary

This failure does not admit DNA-14. Although all 50 VM invocations returned RC0, 22 post-VM alignments failed, therefore runtime behavior is not admitted until a corrected runner is rerun across the complete 50-case suite.

DNA14_ADMISSION=FAIL
DNA14_VM_EXECUTED=YES
DNA14_PROVEN_CAPABILITY=NOT_ADMITTED

No change to DNA-15/F174 defer.
