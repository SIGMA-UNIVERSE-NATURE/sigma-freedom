# V2.5A.1 runtime failure and V2.5A.2 repair

Date: 2026-09-04 (Asia/Ho_Chi_Minh)

## Failure evidence

V2.5A.1 compiled successfully on the locked compiler but failed immediately on the locked VM:

SIGMAC_RC=0
BYTECODE_SHA256=2d5bb4ea2e0428d6c3bbc3b574364f63be0e06341f5b6b068f1a1f5fa76ef1f3
VM_RC=8
SIGMA C VM: undefined function str

No survey state was written:

V25A_SURVEYED_COUNT=0
V25A_RECORD_COUNT=0
V25A_COMPLETE_SENTINEL=0
V25A_WRITES_PRODUCTION_NAMESPACE=NO

This proves that compiler acceptance does not imply runtime capability availability.

## Root cause

V2.5A.1 used direct `str(value)` calls to stringify native integer metrics for persistent text records. The locked VM does not expose `str` as a runtime function in this tested binary.

## Repair

V2.5A.2 removes every direct `str(...)` dependency.

Native integer metrics remain native and are printed directly. Persistent survey records contain only textual fields that can be assembled without numeric string conversion:

DOC=<sha> || SURVEY_STATUS=COMPLETE || BEST_LOCAL_RELATION=<relation>

No survey-selection policy changed.

## V2.5A.2 identities

SOURCE_SHA256=153431aa3f78e282ddf0b2ddd73be993440abd9ce4118d4e717aa5ce83f14eb8
RUNNER_SHA256=c3bbed189661275fda1eb5394965c87b605108a0a316aa1466a7fe3c782ecca5

Static checks:

H_CALL_ARITY_AUDIT=PASS
DIRECT_STR_DEPENDENCY=NONE
BASH_N_RC=0

## Boundaries

HOST_LEARNING=NO
HOST_DOCUMENT_SELECTION=NO
PRODUCTION_LEARNER_MUTATION=NO_BY_NAMESPACE_ISOLATION
SEMANTIC_UNDERSTANDING=NOT_PROVEN

## Next action

Run V2.5A.2 on device. Promote only if all four QA invocations return VM_RC=0, three documents are persistently surveyed, and the fourth invocation reports SURVEY_COMPLETE=YES.
