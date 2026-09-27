# SIGMA V09 -> VKM R3 FIX2 Exact API410 Integrated Contract

Date: 2026-09-27
Source: user-supplied Termux source extraction from current SIGMA_VKM.sigma
Branch: SIGMA_LIFE
Rule: CLAIM <= EVIDENCE

## Exact current source identity

VKM_SOURCE_SHA256=
af918fe8794791d70dcf6fb1b62e1b2fdd075f4ec237a7f3b72b9054e39876c7

## API410 result constructor

DEF:
api410_result(status,final_state,final_task,stage_trace,final_verification,reason)

ROLE=RESULT_CONSTRUCTOR

Returned fields:
STATUS
FINAL_STATE
FINAL_TASK
STAGE_TRACE
FINAL_VERIFICATION
REASON

## API410 integrated root

DEF:
api410_integrate(
t1,t2,t3,t4,
i1,i2,i3,i4,
context_task,obs,
spec401,policy401,
spec402,policy402,
spec404,policy404,
spec406,spec407,spec408,spec409,
policy,context,caps
)

Observed source-level calls:
- api401_understand
- api402_resolve_task
- api408_discourse
- api409_resolve
- api404_plan
- api405_validate
- api406_execute
- api407_verify
- api410_result

Observed success path:
401 UNDERSTOOD
-> 402 RESOLVED
-> 408 VERIFIED
-> 409 RESOLVED
-> 403 causal dependency through 404
-> 404 PLAN_READY
-> 405 VALIDATED / PASS
-> 406 EXECUTED
-> 407 VERIFIED / PASS
-> api410_result(PASS,...,VERIFIED,INTEGRATION_VERIFIED)

Observed fail-closed branches return BLOCKED with stage-specific reasons.

## Transfer interpretation

API410 is strong source evidence for the current integrated VKM language/task pipeline.

However, its parameter list and body contain no direct R13-R6 frozen semantic head input and no direct donor encoder invocation.

Therefore:

API410_INTEGRATE=VKM_CURRENT_LANGUAGE_REGRESSION_BASELINE
API410_INTEGRATE_AS_R13R6_DONOR_EXECUTOR=NO

The R13-R6 donor capability must first port its own inference computation into an admitted native VKM mechanism before its anti-shortcut behavior can be revalidated as a transferred capability.

R13-R6 donor semantic-critical inference path from the frozen donor experiment:
TEXT
-> feat(text)
-> frozen head encode(features, weights)
-> distance(state_a,state_b)
-> anti-shortcut same-world vs altered-world comparison

NEXT=R4A_NATIVE_DONOR_INFERENCE_PORTABILITY_GAP_AUDIT
