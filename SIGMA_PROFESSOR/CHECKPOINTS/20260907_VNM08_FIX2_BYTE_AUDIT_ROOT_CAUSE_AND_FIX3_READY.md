# VNM-08 FIX2 — Byte Audit Root Cause + FIX3 Ready

Date: 2026-09-07 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane: `TEACHER_GPT_VNM`
Status: `FIX2_FAILURE_ROOT_CAUSE_PROVEN / FIX3_SOURCE_READY / VNM08_NOT_ADMITTED`

## Governance

```text
FAILURE_IS_EVIDENCE=YES
WEAKEN_GATE_TO_FORCE_PASS=FORBIDDEN
FAIL_LOCAL_FIX_MINIMAL=YES
RERUN_FULL_REQUIRED_SUITE_AFTER_FIX=YES
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PRODUCTION_STATE_MUTATED=NO
```

## Preserved history

1. Original VNM-08 attempt HOLDed before VM due incorrect pinned VNM-07 runner SHA256 metadata.
2. Exact local/origin/effective byte audit corrected the canonical VNM-07 runner SHA256 to `53fe674e377439146078994c4ba6af3215c96bd966f470d9bbac74bc383e1921` without changing VNM-07 bytes or cognition.
3. VNM-08 FIX1 then reached the declared negative support-mismatch case but its original awk fault injection corrupted the candidate protocol.
4. FIX2 attempted to replace that fault construction with suffix-only `||SUPPORT||2 -> ||SUPPORT||3` framing, but runtime still produced `CANDIDATE_VALID=0`.
5. FIX2 failure was preserved at `SIGMA_PROFESSOR/CHECKPOINTS/20260907_VNM08_FIX2_REPEATED_NEGATIVE_CANDIDATE_INVALID_FAIL.md`.

## Operator byte audit after FIX2

The failed sandbox artifacts were read without rerunning the VM.

Observed base candidate:

```text
BASE_BYTES=161
BASE_SHA256=5d9fff1ed5802999c640573fa84f7409b1eb6bdf2708cfc26687942dc8bc8da5
BASE_VISIBLE=<CANDIDATE||PAIR_CANDIDATE_INDUCED||FORM_A||điện-12825431208757412~mạch-12825431208757412||FORM_B||học-30111999370163179~sâu-30111999370163179||SUPPORT||2>
```

Observed negative fault candidate:

```text
FAULT_BYTES=176
FAULT_SHA256=ae28de4a123ad6043be3a389da9e52c6f7c83393c3b79cf35e7544bd733d9310
FAULT_VISIBLE=<CANDIDATE||PAIR_CANDIDATE_INDUCED||FORM_A||điện-12825431208757412~mạch-12825431208757412||FORM_B||học-30111999370163179~sâu-30111999370163179||SUPPORT||2||||||||||||||3>
```

The fault file therefore contains the untouched original `||SUPPORT||2` followed by additional delimiter bytes and `3`; it is not a one-byte support mutation.

The failed FIX2 materialized runner identity was:

```text
MATERIALIZED_RUNNER_SHA256=94e5dc68ed83b804143caf8298b2adfc5ad3db635b5a4e9e119c7c8e76dcbb19
```

## Exact materialization root cause

Inspection of the materialized negative block showed both:

1. the newly inserted FIX2 block at lines 143-168; and
2. the original legacy negative-fault command line still present immediately after it at line 169.

The relevant structure was:

```text
CASE_NAME=NEGATIVE_SUPPORT_MISMATCH
<new FIX2 suffix-only fault block>
...
NEG=$((NEG+1))
BN="$CASES/neg04"; XN=...; awk -F ... "$CAND" > "$XN/input/candidate.memory"; ...
```

FIX2 materialization matched and replaced only the standalone line:

```text
CASE_NAME=NEGATIVE_SUPPORT_MISMATCH
```

but the legacy fault implementation actually occupied the **next separate line**, beginning with:

```text
BN="$CASES/neg04"; XN="$BN/.sigma_exec/SIGMA_VNM_04_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_V1"; ... awk -F ...
```

That old line therefore executed after the new block and overwrote the correctly faulted candidate with the historical corrupted awk reconstruction.

## Failure classification

```text
FAILURE_CLASS=B_RUNNER_HARNESS_DEFECT
DEFECT_SUBCLASS=FIX2_MATERIALIZATION_REPLACED_CASE_NAME_LINE_BUT_LEFT_NEXT_LEGACY_AWK_FAULT_LINE_EXECUTABLE
VNM04_NATIVE_SOURCE_DEFECT=NO_BY_EVIDENCE
VNM08_COGNITIVE_POLICY_DEFECT=NO
ORACLE_WEAKENING_ALLOWED=NO
EXPECTED_SUPPORT_PAIR_COUNT_2_REMAINS=YES
EXPECTED_SUPPORT_MATCH_0_REMAINS=YES
EXPECTED_BRIDGE_STATUS_REFUSED_CANDIDATE_SUPPORT_MISMATCH_REMAINS=YES
PRODUCTION_STATE_MUTATED=NO
ADMISSION=FAIL_NOT_ADMITTED
```

## FIX3 repair

FIX3 starts from the exact preserved parent VNM-08 runner and applies only mechanical materialization repairs:

1. retain the proven VNM-07 runner SHA256 metadata correction;
2. detect exactly one standalone `CASE_NAME=NEGATIVE_SUPPORT_MISMATCH` line;
3. detect exactly one following legacy `BN=...awk...` negative-fault line;
4. emit the suffix-only support fault block;
5. **skip/remove the legacy line** rather than leaving it executable;
6. verify after materialization:
   - corrected metadata count = 1;
   - case-name exact count = 1;
   - legacy negative-fault line count = 0;
   - negative fault precondition marker count = 1;
7. run `bash -n`;
8. rerun the unchanged full VNM-08 29-VM gate.

FIX3 artifact:

```text
FIX3_WRAPPER_PATH=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_08_HIERARCHICAL_SPAN_FORM_WEIGHTING_INTEGRATION_PREFLIGHT_FIX3.sh
FIX3_WRAPPER_COMMIT=cb22bae1e645bb43fe419250eab882959357e6fc
FIX3_WRAPPER_GIT_BLOB=a0cdb5c506e23b37de8ee8bd46dab8bc102144ac
FIX3_WRAPPER_SHA256=UNKNOWN_UNTIL_TERMUX_VERIFY
```

Identity gates inside FIX3:

```text
PARENT_VNM08_GIT_BLOB=ebb17737ce9119e609ef9d83e29db4039f0ac6eb
FIX2_WRAPPER_GIT_BLOB=ef064e3b3e57d759dd177506d252c19f5f418a7b
VNM07_RUNNER_GIT_BLOB=840d6d86e11b7bc8fc8e881ee7dc5cb26e9c5ee3
VNM07_RUNNER_SHA256=53fe674e377439146078994c4ba6af3215c96bd966f470d9bbac74bc383e1921
```

Repair locks:

```text
REPAIR_CLASS=RUNNER_ONLY_MECHANICAL_MATERIALIZATION_BOUNDARY_REPAIR
NATIVE_SOURCE_CHANGED=NO
VNM07_RUNNER_BYTES_CHANGED=NO
VNM08_PARENT_RUNNER_CHANGED=NO
COGNITIVE_POLICY_CHANGED=NO
CASE_MATRIX_CHANGED=NO
PASS_DEFINITION_WEAKENED=NO
FULL_REQUIRED_SUITE_RERUN=YES
```

## Full gate remains unchanged

```text
TOTAL_VM_INVOCATIONS=29
VNM07_SUBSUITE_VM_INVOCATIONS=21
VNM08_ADDITIONAL_VM_INVOCATIONS=8
VNM04_VM_INVOCATIONS=4
VNM01_VM_INVOCATIONS=4
POST_VM_ALIGNMENT_PASS_COUNT=24
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
NEGATIVE_PASS_COUNT=11
HIERARCHICAL_WEIGHTING_INTEGRATION_PASS_COUNT=4
PERSISTENCE_PASS_COUNT=2
REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES
INITIAL_HIERARCHICAL_WEIGHT=2
SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
PRODUCTION_STATE_MUTATED=NO
VNM_08_PREFLIGHT=PASS
ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
FIX3_FULL_GATE_RC=0
```

## Current proof state

```text
VNM_01_TO_07_ADMITTED=YES_IN_EXACT_TESTED_SCOPES
VNM_08_FIRST_ATTEMPT=HOLD_BEFORE_VM
VNM_08_FIX1=FAIL_NEGATIVE_SUPPORT_FAULT_FRAMING
VNM_08_FIX2=FAIL_LEGACY_AWK_LINE_REMAINED_EXECUTABLE
VNM_08_FIX3_SOURCE_READY=YES
VNM_08_FIX3_RUNTIME=NOT_RUN
VNM_08_ADMISSION=FAIL_UNTIL_FULL_FIX3_GATE_PASSES
PRODUCTION_BINDING=NO
```

Explicit non-claims remain unchanged:

```text
NATURAL_LANGUAGE_TOKENIZATION=NOT_PROVEN
WORD_BOUNDARY_DETECTION=NOT_PROVEN
PHRASE_BOUNDARY_DETECTION=NOT_PROVEN
PHRASE_SEMANTICS=NOT_PROVEN
SEMANTIC_EQUIVALENCE=NOT_PROVEN
WORD_MEANING=NOT_PROVEN
VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN
```

```text
NEXT_ACTION=PULL_FIX3_VERIFY_GIT_BLOB_AND_TERMUX_SHA256_THEN_RUN_FULL_29_VM_GATE
```
