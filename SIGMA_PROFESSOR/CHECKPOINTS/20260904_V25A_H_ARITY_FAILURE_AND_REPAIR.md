# V2.5A DOCUMENT SURVEY — H ARITY FAILURE + V2.5A.1 REPAIR

Date: 2026-09-04 (Asia/Ho_Chi_Minh)

## Failure evidence

V2.5A source identity matched expected SHA and compiled successfully on the locked compiler.

Observed device output:

- `SIGMAC_RC=0`
- bytecode SHA-256: `af044e6ee39ac3b18a7f8e1983f27ed279800ba475b01b988c9db154b734666b`
- first VM run: `VM_RC=8`
- VM error: `SIGMA C VM: arg mismatch for H`
- persisted survey remained empty
- surveyed-document state remained empty
- production namespace was not mutated

## Root cause

The V2.5A source defined:

`DEF H(op, a, b, c)`

but the `str_replace` call supplied five total arguments:

`H("str_replace", SELECTED_FILE, ".document", "", NULL)`

The host ABI uses `op + a + b + c`; `str_replace` already consumes all three value arguments as input string, old substring, and replacement substring. The trailing `NULL` was therefore invalid.

## Repair

V2.5A.1 changes the call to:

`H("str_replace", SELECTED_FILE, ".document", "")`

No survey policy or production-memory behavior changed.

A static arity audit was added during artifact preparation and verified that every `H(...)` invocation in V2.5A.1 has exactly four total arguments.

## Repaired artifacts

Native source:

`SIGMA_PROFESSOR/artifacts/SIGMA_DOCUMENT_SURVEY_V2_5A_1.sigma`

SHA-256:

`210b1227f2805ddd460f95db89dd71258f84ba5a892aa5b50787cea84cf3eb85`

Runner:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V25A_1_DOCUMENT_SURVEY_PREFLIGHT.sh`

SHA-256:

`7ab3f2b157aa21d2effc3eeff7b6ae816e5ae88d27f32a15ffaaf1d840796ed3`

## Boundaries

- `HOST_LEARNING=NO`
- `HOST_DOCUMENT_SELECTION=NO`
- `PRODUCTION_LEARNER_MUTATION=NO_BY_NAMESPACE_ISOLATION`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`

## Next action

Run V2.5A.1 on the same three-document isolated QA corpus.

PASS requires:

- four VM invocations all `RC=0`;
- three distinct documents marked surveyed;
- three persisted survey records;
- fourth run reports `SURVEY_COMPLETE YES`;
- no production learner namespace mutation.

Do not promote to full-corpus survey until this admission test passes.
