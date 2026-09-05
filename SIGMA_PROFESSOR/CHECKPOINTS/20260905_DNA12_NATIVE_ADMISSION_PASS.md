# DNA-12 NATIVE ADMISSION PASS

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Identity

DNA_ID=DNA-12
NAME=Tool Intelligence
CANON_REFERENCE_BLOB_SHA1=eda8a57900cd9ee88970120bc8b89eec5fd4aad3
SOURCE_SHA256=336152fca9e1112e9646249b5109c54835d52d9d0b5948d6bbf6703bf328920c
BYTECODE_SHA256=7dc7cceab5442938a0846c811e98e8c367ab6beedfdefc7c281355f305f7fe70
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

## Runtime evidence

TOTAL_VM_INVOCATIONS=56
POST_VM_ALIGNMENT_PASS_COUNT=56
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
SENTINEL_FAIL_COUNT=0
REPLAY_IDENTICAL_INPUT_DECISION=YES
SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0
DYNAMIC_INPUT=YES
PERSISTENT_STATE=NA
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
HOST_POST_VM_TEST_ORACLE_ONLY=YES
PYTHON_USED=NO
VM_RC=0_IN_ALL_BOUNDED_INVOCATIONS
ADMISSION=PASS
RESULT=PASS_IN_EXACT_TESTED_SCOPE

## Proven in exact tested scope

- four Canon decision modes: `THINK_ONLY`, `TOOL_ASSISTED_REASONING`, `THINK_AND_DECLARE_TOOL_GAP`, `THINK_AND_IDENTIFY_EVIDENCE_GAP`;
- dynamic tool-use signal handling;
- explicit tool/evidence gap handling;
- supplied tool output classified as `UNVERIFIED_TOOL_OUTPUT` even when caller truth claim is `VERIFIED`;
- dynamic candidate-tool name binding;
- tool-output provenance preservation;
- knowledge-graph node token/count non-mutation in tested scope;
- reasoning remains required for all modes.

## Phase locks / boundaries

TOOL_OUTPUT_AUTOMATICALLY_TRUE=NO
TOOL_OUTPUT_DEFAULT_TRUTH_STATUS=UNVERIFIED_TOOL_OUTPUT
AUTOMATIC_KNOWLEDGE_PROMOTION=NO
TOOL_EXECUTION_AUTHORITY=NO
EXTERNAL_TOOL_EXECUTION=NOT_EXECUTED
MODEL_CALL_RUNTIME=NOT_EXECUTED
LEARNING_RUNTIME=NOT_EXECUTED
WORLD_RUNTIME=NOT_EXECUTED
KNOWLEDGE_GRAPH_WRITE_AUTHORITY=NO
SEMANTIC_UNDERSTANDING=NOT_PROVEN

CLAIM_SCOPE=Native bounded Tool Intelligence evaluation over dynamic DNA11-compatible knowledge-graph state and tool-use signals: four Canon decision modes, explicit tool/evidence gap handling, tool-output classification as unverified evidence regardless of caller truth claim, dynamic tool-name binding, provenance preservation, and knowledge-graph non-mutation. Tool execution, model calls, automatic knowledge promotion, Learning/World runtime execution, and semantic understanding are not claimed.
