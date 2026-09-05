# SIGMA I5A Fix2 — Wikipedia discovery runner fixture isolation source ready

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: SOURCE_READY / RUNNER_ONLY_REPAIR / RUNTIME_ADMISSION_NOT_RUN_AFTER_FIX2

## Dependency and failure history

I4 remains admitted PASS in exact tested scope with canonical native source-family selection `WIKIPEDIA` / family id `10`.

I5A V1 native PREPARE previously passed; Fix1 repaired the mechanical jq decoder and then machine evidence established:

```text
C02_CANONICAL_VERIFY VM_RC=0
CANDIDATE_SET_VALID=1
CANDIDATE_COUNT=10
I5A_STATUS=DISCOVERY_RESULT_READY
POST_VM_ALIGNMENT=PASS
```

The subsequent D03 wrong-family fixture natively emitted:

```text
I5A_STATUS=HOLD_NOT_WIKIPEDIA
REQUEST_EVENT_EMITTED=0
POST_VM_ALIGNMENT=PASS
```

but the runner observed stale canonical bytes in `state/i5a_request_event.txt` and emitted:

```text
HOLD=WRONG_FAMILY_REQUEST_EVENT_EMITTED
```

Failure checkpoint:

`DOCS/GPT_REFERENCE/CHECKPOINTS/20260905_I5A_FIX1_D03_STALE_REQUEST_EVENT_FIXTURE_CONTAMINATION.md`

## Fix2 repair

Fix2 is runner-only.

A mechanical helper now truncates I5A output-state files before independent fixtures:

```text
request.query.txt
i5a_request_event.txt
i5a_result_event.txt
```

D03 oracle is unchanged. Wrong-family PREPARE must still produce no request event.

```text
FAILURE_CLASS=MECHANICAL_HARNESS_FIXTURE_CONTAMINATION
NATIVE_I5A_SOURCE_CHANGED=NO
ORACLE_WEAKENED=NO
RUNNER_ONLY_REPAIR=YES
```

## Exact identities

```text
FIX2_BUNDLE_SHA256=9791dbe1276a63af79c46e096f8a2dccfecce9ee97e9e6603dc68510ca5f5616
FIX2_RUNNER_SHA256=24de72c4cb299a65c3d8d8969f84c3550a8ac466c9d5bb5f766b21af10429097
I5A_SOURCE_SHA256=0d49e744c1d0395ca18dc87f40ea706da29d94474c42ac948ff2071980addd11
I4_FIX3_SOURCE_SHA256=a13417668f1dc85e42d7f529306cdc09928ab45655d771d95c89d383b6fc7784
I3C_SOURCE_SHA256=daa01d60e11afd64b763c6623bc14d0aa2d868cc03f686b26ad3026d6951284f
I4_CATALOG_SHA256=7d650b53bae8b22fb6ab7613127e0a116bbe32d3bc032a31cdb44ad69ae7c224
```

Static QA:

```text
BASH_SYNTAX_QA=PASS
D03_PRECASE_OUTPUT_RESET_QA=PASS
INDEPENDENT_FIXTURE_OUTPUT_ISOLATION_QA=PASS
NATIVE_I5A_SOURCE_CHANGED=NO
ORACLE_WEAKENED=NO
```

## Claim boundaries

Until the full Fix2 admission gate passes:

```text
I5A_RUNTIME_ADMISSION=NOT_PROVEN
NATIVE_SOURCE_DISCOVERY_REQUEST=NOT_PROVEN_UNTIL_FULL_GATE_PASS
WIKIPEDIA_DISCOVERY_TRANSPORT=NOT_ADMITTED_UNTIL_FULL_GATE_PASS
HOST_QUERY_GENERATION=NO
HOST_RESULT_RANKING=NO
HOST_CANDIDATE_SELECTION=NO
HOST_RESOURCE_SELECTION=NO
RESOURCE_SELECTION=NOT_EXECUTED
NATIVE_RESOURCE_SELECTION=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
CLOSED_AUTONOMOUS_NATURAL_LANGUAGE_WEB_LEARNING_LOOP=NOT_PROVEN
```

Next action: rerun the same I5A admission gate from a clean Fix2 bundle and preserve the first new HOLD/FAIL or the final admission summary exactly.
