# DNA-15 V2 H-FREE STATE-DERIVED-K — RUNTIME FAIL

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Machine evidence

```text
SOURCE_SHA256=94f4684115d03116bff19348ce840457f5c066d2399c7f83dd3f5b9ecfd24f26
BYTECODE_SHA256=c44a85358c4ab0fd7ca5fd71f328575859bf16b7dfdffca516f15620eeb26f76
TOTAL_VM_INVOCATIONS=50
POST_VM_ALIGNMENT_PASS_COUNT=45
POST_VM_ALIGNMENT_FAIL_COUNT=5
POST_VM_NUMERIC_ALIGNMENT_PASS_COUNT=48
POST_VM_NUMERIC_ALIGNMENT_FAIL_COUNT=2
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
SENTINEL_FAIL_COUNT=0
REPLAY_IDENTICAL_INPUT_DECISION=YES
STALE_H_AND_CALLER_K_INDEPENDENCE_PASS_COUNT=1
STALE_H_AND_CALLER_K_INDEPENDENCE_FAIL_COUNT=0
ADMISSION=FAIL
RESULT=FAIL_IN_TESTED_SCOPE
```

No DNA-15 capability admission follows from this run.

## Static source/runner diagnosis after failure

Two independent defects were found by exact inspection of the tested V2 source and runner:

1. The native source emitted `MEASUREMENT_COMPLETE=INPUT_BINDING_VALID`. The runner defines measurement completeness from presence of the five measurement fields independently of dependency validity. Therefore the three directed dependency-invalid cases (bad state schema, bad persistence schema, DNA14 output absent) can disagree on `MEASUREMENT_COMPLETE` even when all measurement fields are present.

2. The post-VM numeric oracle set expected `TIME_OFFSET=0` whenever the k-derivation domain was invalid. The native source instead computes `TIME_OFFSET=t-t0` whenever the complete dependency-bound numeric input is parsed, even when k derivation is later blocked by `A0<=0` or `A_t<=0`. This accounts for the two directed numeric-domain cases `A0_ZERO_DOMAIN_INVALID` and `OBS_ZERO_DOMAIN_INVALID` as a static oracle mismatch candidate.

These diagnoses explain the observed 5 semantic / 2 numeric failure pattern, but causal repair is not promoted until a FIX1 full rerun passes.

## FIX1 scope

- Keep H removed from active calculation.
- Keep caller-k removed from active calculation.
- Keep `k=ln(A_t/A0)/(t-t0)^2` unchanged.
- Native source: change only `MEASUREMENT_COMPLETE` emission from dependency-bound input validity to required-field completeness.
- Runner oracle: preserve parsed `TIME_OFFSET` for complete dependency-bound input even when the positive-A k-derivation domain is invalid.
- Rerun all 50 cases.

Boundaries remain:

```text
STATE_DERIVED_K=NOT_ADMITTED
MATH_LOG_ABI=NOT_ADMITTED
K_TEMPORAL_CONSTANCY=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
```
