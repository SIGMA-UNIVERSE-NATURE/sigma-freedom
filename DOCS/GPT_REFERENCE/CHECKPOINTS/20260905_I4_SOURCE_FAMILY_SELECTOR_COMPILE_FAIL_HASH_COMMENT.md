# SIGMA I4 source-family selector — compile failure checkpoint

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: COMPILE_FAIL / SYNTAX_ONLY_SOURCE_DEFECT / I4_RUNTIME_NOT_RUN

## User machine evidence

```text
COMPILED <I3C source> -> <I3C bytecode.partial>
sigmac: line 107 col 13: expected '}' (token=#)
I4_COMPILE_RC=4
HOLD=I4_COMPILE_FAILED
```

The failure occurred while compiling the new I4 native source before any I4 VM runtime execution.

## Root cause

Exact source inspection localized line 107 to:

```text
# Duplicate family id/name refusal.
```

The only valid `#` token in this source form is the `#SIGMAUNIVERSE_LANGUAGE[...]` header. A mid-source `#` comment is rejected by the locked SIGMAC lexer/parser.

```text
FAILURE_CLASS=SIGMA_SOURCE_SYNTAX_ONLY
ROOT_CAUSE=MID_SOURCE_HASH_COMMENT_UNSUPPORTED
I4_RUNTIME_EXECUTED=NO
I4_COGNITIVE_FAILURE=NOT_ESTABLISHED
I3C_SOURCE_CHANGED=NO
CATALOG_CHANGED=NO
I4_POLICY_CHANGE_REQUIRED=NO
SMALLEST_REPAIR=REMOVE_UNSUPPORTED_COMMENT_ONLY
```

## Repair discipline

Fix1 must remove only the unsupported comment line, preserve the entire I4 native policy and runner semantics, then rerun the same admission gate from clean isolated state.

Do not weaken anti-hardcode gates or prewrite the canonical selected source family.

```text
CANONICAL_EXPECTED_SOURCE_FAMILY_PREWRITTEN_IN_RUNNER=NO
HOST_SOURCE_SELECTION=NO
HOST_CATALOG_RANKING=NO
HOST_RESOURCE_SELECTION=NO
I4_ADMISSION=NOT_PROVEN
```
