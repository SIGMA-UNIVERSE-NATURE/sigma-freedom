# DNA-15 NATIVE ADMISSION V2 — H-FREE STATE-DERIVED K — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Status

This is source/static evidence only.

```text
DNA15_V2_SOURCE=SOURCE_ONLY
DNA15_V2_COMPILE=NOT_RUN
DNA15_V2_VM=NOT_RUN
DNA15_V2_ADMISSION=NOT_RUN
```

## Prior V1 evidence

V1 remains FAIL and is retained in:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_DNA15_NATIVE_ADMISSION_V1_FAIL_46_OF_50_AND_HFREE_DERIVED_K_DIRECTIVE.md`

V1 machine summary:
- 50 VM invocations;
- VM RC=0 in all invocations;
- numeric alignment 50/50;
- semantic/post-VM alignment 46/50;
- ADMISSION=FAIL.

## User-directed operational extension candidate

Active profile:
`H_FREE_STATE_DERIVED_K_V2`

Active source does not read `H_t.txt` and does not read caller `k.txt`.

For positive `A0`, positive measured `A_t`, and nonzero `t-t0`, SIGMA derives:

`k = ln(A_t/A0)/(t-t0)^2`

State binding:
- `A_t>A0` -> `A_INCREASING`, positive derived k required;
- `A_t=A0` -> `A_STABLE`, zero derived k required;
- `A_t<A0` -> `A_DECREASING`, negative derived k required.

The Canon base equation remains the reconstruction equation:
`A(t)=A0*exp(k*(t-t0)^2)`.

Temporal constancy of the derived interval-k is not claimed, therefore the constant-k derivative is not executed by this candidate.

## Native artifact

SOURCE_PATH=DNA15_F174_HFREE_STATE_DERIVED_K_NATIVE_V2.sigma
SOURCE_SHA256=94f4684115d03116bff19348ce840457f5c066d2399c7f83dd3f5b9ecfd24f26
RUNNER_PATH=run_DNA15_NATIVE_ADMISSION_V2.sh
RUNNER_SHA256=decb39240bd0cac6f8a851a03a2a0da3424efee09cc3d8dd7ea35fda3395dd18
CANON_REFERENCE_SHA256=ca365009b8c9780fb0278479f9dd553365f86c7d23f5f141b88a3ff9147354dd
README_SHA256=730f042a322b0a53d7c2de1f77fad8a7d816007eb2579a9bc4f55929f46a486e
MANIFEST_SHA256=60a9cdd66bcb14d43f92b306e0670b5d8c65f91bd83cf6d3c96ce8e74157637e
BUNDLE_SHA256=4c4c6d08f0017231153eceb24726cd5c52ccba91155cb0e28604aea372585086
CANON_REFERENCE_BLOB_SHA1=50ec4940f554d594c385a96ef986fc88dca7f53c

## Static audit

```text
SOURCE_HASH_COMMENTS=1
MIDFILE_HASH_COMMENT_COUNT=0
TOP_LEVEL_COMMAND_COUNT=1
BARE_TOP_LEVEL_BLOCK_COUNT=0
SOURCE_PYTHON_TOKEN_COUNT=0
RUNNER_PYTHON_COMMAND_COUNT=0
TO_FLOAT_CALL_COUNT=1
MATH_LOG_CALL_COUNT=1
MATH_EXP_CALL_COUNT=1
H_INPUT_PATH_READ_COUNT=0
CALLER_K_INPUT_PATH_READ_COUNT=0
BASH_SYNTAX=PASS
MANIFEST=PASS
ZIP_INTEGRITY=PASS
```

## Admission plan

Exact dependencies: admitted DNA-01 through DNA-14.

Dynamic after compile/freeze:
- 16 directed cases;
- 32 randomized valid measured-state cases;
- 2 byte-identical replay cases;
- total 50 VM invocations.

Dedicated stale-input independence pair:
- read inputs remain identical;
- only stale `H_t.txt` and stale `k.txt` change;
- shell input-record SHA must change;
- VM stdout SHA must remain identical.

This tests H/caller-k output-inertness in the exact scope because V2 source does not read those files.

Mechanical ABI under runtime test:
`read_text`, `to_float`, `math_log`, `math_exp`, `map_new`, `map_set`, `map_get`, `list_new`, `list_push`, `list_len`.

`math_log` is source-inventory evidence only before this run. No fallback is allowed.

## Claim boundaries

```text
ACTIVE_H_INPUT=REMOVED_CANDIDATE_NOT_RUNTIME_PROVEN
CALLER_K_INPUT=REMOVED_CANDIDATE_NOT_RUNTIME_PROVEN
STATE_DERIVED_K=NOT_PROVEN_UNTIL_RUNTIME_PASS
MATH_LOG_ABI=NOT_PROVEN_UNTIL_RUNTIME_PASS
K_TEMPORAL_CONSTANCY=NOT_PROVEN
DERIVATIVE_FROM_DERIVED_K=NOT_EXECUTED
NUMERIC_TEXT_VALIDATION=NOT_PROVEN
GLOBAL_F174_CANON_FILE_READ_NATIVE=NOT_PROVEN
PARAMETER_OPTIMIZATION=NOT_EXECUTED
F174_EXPERIMENT=NOT_EXECUTED
CAPABILITY_GROWTH=NOT_EXECUTED
MODEL_REPLACEMENT=NOT_EXECUTED
LEARNING_RUNTIME=NOT_EXECUTED
WORLD_RUNTIME=NOT_EXECUTED
EXTERNAL_ACTION_RUNTIME=NOT_EXECUTED
SEMANTIC_UNDERSTANDING=NOT_PROVEN
```
