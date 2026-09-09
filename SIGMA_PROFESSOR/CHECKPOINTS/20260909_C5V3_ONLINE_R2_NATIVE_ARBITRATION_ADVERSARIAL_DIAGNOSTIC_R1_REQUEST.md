# 2026-09-09 — C5V3 ONLINE R2 NATIVE ARBITRATION ADVERSARIAL DIAGNOSTIC R1 REQUEST

Status: **ACTIVE INDEPENDENT DIAGNOSTIC / R2 IS NOT FINAL ADMISSION TARGET / PRODUCTION UNTOUCHED**
Branch: `c5v3-online-capability-utilization-test-20260909`
Owner role: **ONLINE VERIFICATION WINDOW**

## Purpose

Use the already-frozen same-identity R2 prototype only as an adversarial diagnostic target before R3. Do not admit R2 as the final C5V3 runtime.

The diagnostic is deliberately capable of falsifying the desired native-utilization claim. It must not convert source self-report fields into proof.

Frozen target:

```text
R2_SOURCE_SHA256=d7d1153fd6979dff7d119bb5e8187f045b9f8af62e51065cccf95265478fc3a0
R2_BYTECODE_SHA256=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
R2_RUNTIME_ADMISSION_TARGET=NO
```

Harness:

`C5_M5/RUN_C5V3_ONLINE_R2_NATIVE_ARBITRATION_ADVERSARIAL_DIAGNOSTIC_R1.sh`

Harness commit:

`a9faf3d7745a655fc3d040f02192f65274e3be02`

Harness Git blob:

`4008fbdef6c3b0223e09726aa6a5c081efa77b55`

## Exact questions

1. With task input and relevant prestate held fixed, does changing capability family availability alone change native action from `WAIT_CAPABILITY` to `EXECUTE_CAPABILITY` for T1/T2/T3/T4?
2. With raw task payload and full registry held byte-identical, does changing only host-supplied `TASK_KIND` control the selected family?
3. Does R2 provide a valid `CAPABILITY_NOT_NEEDED` task path, or only mapped families plus invalid-kind refusal?
4. Does capability-result handling reject wrong IDs and non-OK status?
5. With result ID/status/kind/provenance/prestate held fixed, do materially different result payload bytes causally change the next native decision, or are they merely copied to `task_result.txt`?

## Anti-hardcode / host boundary

The harness generates unseen runtime tokens only after source/bytecode hash freeze. It does not execute T1/T2/T3/T4 tools and contains no semantic expected answer. Expected values are only mechanical source-contract observables checked after VM execution.

```text
HOST_CAPABILITY_EXECUTION=NO
HOST_SEMANTIC_ORACLE=NO
HOST_LEARNING=NO
NETWORK=NO
PRODUCTION_STATE_WRITE=NO
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

The harness explicitly records:

`HOST_TASK_KIND_FIXTURE_PROVIDED=YES`

because the purpose is to determine whether R2's claimed need detection actually depends on that host-provided classification.

## Claim boundary

Even a clean diagnostic mechanics PASS cannot admit:

```text
C5V3_NATIVE_CAPABILITY_UTILIZATION
NATIVE_CAPABILITY_NEED_DETECTION_FROM_RAW_PROBLEM
NATIVE_CAPABILITY_EXECUTION
NATIVE_CAPABILITY_RESULT_CONTENT_EVALUATION
NATIVE_LEARNING_UPDATE
FRESH_RESTART_LEARNED_STATE_REUSE
```

unless the corresponding machine evidence actually exists.

If `TASK_KIND` causally controls family selection for byte-identical raw problem bytes, report that fact directly and keep final native need detection NOT_PROVEN for R2.

If materially different result payload bytes produce an identical next native action/status/target in the generic TASK path, keep content-sensitive native result evaluation NOT_PROVEN.

`CLAIM <= MACHINE EVIDENCE`
