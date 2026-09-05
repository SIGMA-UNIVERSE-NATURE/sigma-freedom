# DNA-15 NATIVE ADMISSION V1 — RUNTIME FAIL 46/50 + H-FREE DERIVED-K DIRECTIVE

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## V1 machine evidence

SOURCE_SHA256=2f8c58101ee2a543fed7a8ecab2e2b4cbeeff6b1beefd89ae461b4e557433f51
BYTECODE_SHA256=4240280f7b352e22e18ea2c81ddc8f1135b77088124d15b4dfa8ee3bee33dca5
TOTAL_VM_INVOCATIONS=50
POST_VM_ALIGNMENT_PASS_COUNT=46
POST_VM_ALIGNMENT_FAIL_COUNT=4
POST_VM_NUMERIC_ALIGNMENT_PASS_COUNT=50
POST_VM_NUMERIC_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
SENTINEL_FAIL_COUNT=0
REPLAY_IDENTICAL_INPUT_DECISION=YES
SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0
ADMISSION=FAIL
RESULT=FAIL_IN_TESTED_SCOPE

V1 is not admitted. Numeric F174 calculations aligned in all 50 invocations, but four semantic/post-VM alignment checks failed.

## User directive after V1 failure

The user explicitly directed:
- remove H as an active ceiling/input from the F174 operational calculation;
- derive `k` from the measured A state rather than require a caller-supplied `k`;
- keep the chain continuous.

This directive authorizes a new native operational-extension candidate. It does not retroactively make V1 pass and does not by itself prove the new capability.

## New candidate design boundary

Active calculation candidate:

`k = ln(A_t / A0) / (t - t0)^2`

for positive `A0`, positive observed `A_t`, and nonzero time offset.

Expected state binding in the new candidate:
- `A_t > A0` -> `A_INCREASING` and derived `k > 0`;
- `A_t = A0` -> `A_STABLE` and derived `k = 0`;
- `A_t < A0` -> `A_DECREASING` and derived `k < 0`.

The active source will not read `H_t` or caller `k` files. Stale H/k files will be changed dynamically in a dedicated independence test; identical VM output is required.

`math_log` is present in the host ABI source inventory but is not yet locked-VM runtime proof. The new admission must exercise it directly; no shell/host semantic fallback is allowed.

## Claim boundaries

```text
DNA15_V1_ADMISSION=FAIL
DNA15_V2_SOURCE=IN_PREPARATION
MATH_LOG_LOCKED_VM_RUNTIME=NOT_PROVEN
H_FREE_ACTIVE_CALCULATION=NOT_PROVEN_UNTIL_V2_RUNTIME
STATE_DERIVED_K=NOT_PROVEN_UNTIL_V2_RUNTIME
K_TEMPORAL_CONSTANCY=NOT_PROVEN
DERIVATIVE_FROM_DERIVED_K=NOT_EXECUTED
PARAMETER_OPTIMIZATION=NOT_EXECUTED
F174_EXPERIMENT=NOT_EXECUTED
CAPABILITY_GROWTH=NOT_EXECUTED
MODEL_REPLACEMENT=NOT_EXECUTED
SEMANTIC_UNDERSTANDING=NOT_PROVEN
```
