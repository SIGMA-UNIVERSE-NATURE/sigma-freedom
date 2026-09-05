# SIGMA I5A Wikipedia discovery — mechanical jq decoder HOLD

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: HOLD / MECHANICAL_JSON_DECODER_SYNTAX / NATIVE_I5A_PREPARE_PASS_OBSERVED

## User machine evidence

```text
C01_CANONICAL_PREPARE
VM_RC=0
I5A_STATUS=DISCOVERY_REQUEST_READY
QUERY_WRITE_READBACK_MATCH=1
REQUEST_EVENT_EMITTED=1
POST_VM_ALIGNMENT=PASS
NATIVE_QUERY_TO_CANONICAL_RAW_TOPIC_BYTE_BINDING=PASS
CANONICAL_QUERY_BYTES=37
CANONICAL_WIKIPEDIA_HTTP_RC=0
jq: error: syntax error, unexpected INVALID_CHARACTER
CANONICAL_WIKIPEDIA_JSON_DECODE_RC=3
HOLD=CANONICAL_WIKIPEDIA_JSON_DECODE_FAILED
```

The failure occurs after the native I5A PREPARE VM invocation and successful live HTTP transport, before native I5A VERIFY consumes the candidate-set protocol.

## Exact root cause

The canonical runner contained this jq interpolation:

```jq
\(.value.timestamp // \"\")
```

This jq expression is syntactically invalid. The empty-string fallback belongs inside the interpolation expression without backslash-escaped quotes:

```jq
\((.value.timestamp // ""))
```

The failure was independently reproduced with jq 1.7:

```text
OLD_EXPRESSION_JQ_COMPILE_RC=3
REPAIRED_EXPRESSION_JQ_COMPILE_RC=0
```

No other `\\"` occurrence exists in the runner's jq code.

## Classification

```text
FAILURE_CLASS=MECHANICAL_HOST_JSON_DECODER_SYNTAX
NATIVE_I5A_COGNITIVE_FAILURE=NOT_ESTABLISHED
I5A_PREPARE_NATIVE_RUNTIME=PASS_OBSERVED_IN_CANONICAL_CASE
LIVE_WIKIPEDIA_HTTP_TRANSPORT=PASS_OBSERVED_FOR_THIS_RUN
HOST_JSON_DECODE_EXECUTED_SUCCESSFULLY=NO
NATIVE_I5A_VERIFY_EXECUTED_FOR_CANONICAL_LIVE_RESPONSE=NO
I5A_ADMISSION=NOT_PROVEN
```

## Smallest repair

Fix1 is runner-only:

1. keep exact I3C source unchanged;
2. keep exact admitted I4 Fix3 source/catalog unchanged;
3. keep I5A native source unchanged;
4. replace only the invalid jq timestamp fallback expression;
5. add a static jq compile/projection QA using a synthetic JSON object;
6. rerun the same admission gate from clean isolated state.

Do not rank/filter/select any candidate in jq. Preserve complete bounded result-set projection and remote order as provenance only.

```text
HOST_QUERY_GENERATION=NO
HOST_RESULT_RANKING=NO
HOST_CANDIDATE_SELECTION=NO
HOST_RESOURCE_SELECTION=NO
REMOTE_API_ORDER=PROVENANCE_ONLY
RESOURCE_SELECTION=NOT_EXECUTED
```
