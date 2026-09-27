# SIGMA V09 -> VKM Native Language Call-Graph Discovery R3 FIX2 — Runtime Result

Date: 2026-09-27
Source: user-supplied Termux runtime output.
Branch: SIGMA_LIFE
Rule: CLAIM <= EVIDENCE

## Runtime preflight

SCHEMA=SIGMA_V09_TO_VKM_NATIVE_LANGUAGE_CALLGRAPH_DISCOVERY_R3_FIX2
MODE=READ_ONLY_DISCOVERY
TARGET_OWNER_FINGERPRINT=c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222
CANONICAL_MUTATION_ALLOWED=NO

OWNER_STATE_SHA256=e73a8bba0f631b9ab90d98a04211a2c025a777734e68ec15bb4561a38da66661
NATIVE_BINDING_SHA256=99e25dd665bffda45315c0720e58c527529cc5a0b8f35d2a4d566f04a41f85f5
VKM_SOURCE_SHA256=af918fe8794791d70dcf6fb1b62e1b2fdd075f4ec237a7f3b72b9054e39876c7
SIGMAC_VKM_SHA256=60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98
SIGMA_VKM_VM_SHA256=c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95

R2_SOURCE_CONTINUITY=PASS
PINNED_SIGMAC_VKM_SHA256=PASS
PINNED_SIGMA_VKM_VM_SHA256=PASS

## Discovery counts

API401_410_DEF_COUNT=63
STRUCTURALLY_ELIGIBLE_COUNT=37
DIRECT_SEMANTIC_CANDIDATE_COUNT=0

R3_FIX2_CALLGRAPH_DISCOVERY_STATUS=NO_DIRECTLY_BOUND_SEMANTIC_CANDIDATE

This status means no semantic DEF name was directly referenced by exact text in Owner state / Native Binding / top-level source. It does not mean the native semantic pipeline is absent.

## Important call-graph structure

Observed source-level chain includes:

api410_integrate -> api401_understand
api410_integrate -> api402_resolve_task
api410_integrate -> api404_plan
api410_integrate -> api405_validate
api410_integrate -> api406_execute
api410_integrate -> api407_verify
api410_integrate -> api408_discourse
api410_integrate -> api409_resolve

Lower-level structure also includes:

api402_finish -> api401_understand
api403_decompose -> api402_resolve_task
api403_r11_decompose -> api403_decompose
api404_plan -> api403_r11_decompose
api405_validate -> api404_plan
api406_execute -> api405_validate
api407_verify -> api406_execute
api408_discourse -> api407_verify
api409_resolve -> api407_verify + api408_discourse

The earlier R3 heuristic candidate:
api405_expected_primary_constraint_from_language(task)

was correctly classified in FIX2 as:
ROLE=EXPECTED_OR_EVALUATOR_HELPER
ELIGIBLE=NO

Therefore it must not be used as a production semantic entry point.

## Key boundary

No exact Owner/Native-Binding source-function-name reference was observed for the candidate DEFs.

This is expected to remain separate from capability-level Owner binding, which may bind capability proof/state rather than source DEF names.

R3 FIX2 did not execute semantic behavior and did not mutate Owner state or Native Binding.

SEMANTIC_EXECUTION_PERFORMED=NO
CANONICAL_MUTATION=NO
OWNER_STATE_MUTATION=NO
NATIVE_BINDING_MUTATION=NO
OWNERSHIP_PROMOTION_PERFORMED=NO

## Next exact information required

Before R4 behavior execution, extract the exact source DEF record for the apparent integrated root:
api410_integrate

Required fields:
- line
- parameter list
- outbound callees
- role/classification
- any wrapper/result helper paired with API410

Do not invent the parameter contract.

NEXT=EXTRACT_API410_INTEGRATE_EXACT_DEF_THEN_BUILD_R4_NATIVE_SEMANTIC_BEHAVIOR_REVALIDATION
