# SIGMA Gen3 Frozen Evaluator Bind to Durable Head

Date: 2026-09-26
Source: user-supplied Termux runtime output.

## Precheck

PRECHECK=PASS

## Frozen evaluator interface

FROZEN_EVALUATOR_INTERFACE_PATH=
/data/data/com.termux/files/home/SIGMA_R7_NEXT_R1/VKM/SIGMA_AUTOLEARN_ADMIN/SIGMA_06B2_FROZEN_EVALUATOR_INTERFACE.current.txt

FROZEN_EVALUATOR_INTERFACE_SHA256=
44abca8fe4b1cd4f742d508d9d789cc5d2a246e027218ef1805f3c3da88122f0

## Durable-head evaluator binding

FROZEN_EVALUATOR_BINDING=PASS

DURABLE_HEAD=
599c639a3a58c7971518727c303c876e

MODEL_GENERATION=3

MODEL_ID=
4e28b7b00428271a4d09f1791d5d46fb

AITO_RUNNER_SHA256=
752631c6030fd964a399f161b9c4c6bdc13b3086e26d1e044d974a527f864807

06B2_TESTER_SHA256=
026cf6115de6d843ef41f0cc95dde277571760cbb8470b1fd4be111f3200cd3b

BINDING_SHA256=
9b9fa135c3ca6e9a631edb3ce7aca989cc6a4bc4bd1835818b8c324959071c63

NEXT=RUN_GEN3_FROZEN_BASELINE

## Interface observations preserved from runtime inspection

AITO runner asserts:
- exact SIGMA header;
- HOLD fail-closed behavior;
- baseline 06B2 consumption markers;
- frozen evaluator identity binding;
- no DNA15 invocation during evaluator path.

06B2 tester exposes:
- accepted state model path input;
- accepted evaluator component path and SHA pinning;
- baseline 06B2 parent;
- frozen holdout windows;
- fixed evaluator component SHA expectation;
- state checkpoint before/after comparison;
- EVALUATOR_STATE_MUTATION fail condition;
- accepted evaluator component SHA and byte-identity checks;
- before/after state replay hashes;
- fresh process evaluation match;
- deterministic evaluator;
- EVALUATOR_READ_ONLY=PASS;
- BEFORE_STATE_MUTATED=NO;
- AFTER_STATE_MUTATED=NO;
- EVALUATION_MUTATES_MODEL=NO;
- EVALUATION_APPENDS_EVIDENCE=NO;
- FINAL_AUDIT_NOT_USED_FOR_CANDIDATE_ADMISSION=YES;
- DNA15_CALLED=NO.

## Interpretation boundary

This checkpoint records successful binding of the frozen 06B2 evaluation interface to the current durable canonical Gen3 head.

It does not itself record the Gen3 frozen-baseline evaluation result. The next explicitly reported step is RUN_GEN3_FROZEN_BASELINE.
