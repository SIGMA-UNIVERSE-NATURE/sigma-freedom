# SIGMA V09 -> VKM Native Language Call-Graph Discovery R3 FIX1 Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Status: SOURCE_READY / READ_ONLY_DISCOVERY

## Why FIX1 exists

R3 original output reported:

NATIVE_LANGUAGE_CALLABLE_DISCOVERY_STATUS=UNIQUE_CANDIDATE
UNIQUE_CALLABLE_NAME=api405_expected_primary_constraint_from_language
UNIQUE_CALLABLE_PARAMS=task

This conclusion was produced by a name-scoring heuristic only.

That is not sufficient evidence that the selected function is the production native semantic entry point.

The selected name contains "expected", while the same source contains other plausible semantic-path functions such as:
- api401_understand(task,spec,policy,obs,caps)
- api402_resolve_task(task,spec,policy,context,caps)
- api403_decompose(task,spec,policy,context,caps)
- owner403_gate(task,spec,policy,context,caps)

Therefore R3's "unique" result is not promoted into R4 behavior execution.

## R3 FIX1 design

R3 FIX1 is read-only and performs:
- API401-410 / owner401-410 DEF inventory;
- lexical call graph;
- inbound/outbound API-call mapping;
- top-level/dispatch references;
- exact function-name references in current Owner state;
- exact function-name references in current Native Binding;
- helper classification for expected/result/ablate/probe/test-like definitions;
- no name-score-only selection.

## Locked current identities

TARGET_OWNER_FINGERPRINT=
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

EXPECTED_VKM_SOURCE_SHA256=
af918fe8794791d70dcf6fb1b62e1b2fdd075f4ec237a7f3b72b9054e39876c7

PINNED_SIGMAC_VKM_SHA256=
60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98

PINNED_SIGMA_VKM_VM_SHA256=
c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95

## Safety

MODE=READ_ONLY_DISCOVERY
CANONICAL_MUTATION_ALLOWED=NO
OWNER_REBIND_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
SEMANTIC_EXECUTION_PERFORMED=NO

## Release

BUNDLE=
SIGMA_V09_TO_VKM_NATIVE_LANGUAGE_CALLGRAPH_DISCOVERY_R3_FIX1_BUNDLE.zip

BUNDLE_SHA256=
503f8a85d5be70d7928867f2598fde62c07d4142fecc5fc1c816cea313d56c35

RELEASE_VERIFY=PASS

NEXT=
RUN_R3_FIX1_AND_BUILD_R4_ONLY_FROM_CALLGRAPH_PLUS_OWNER_BINDING_EVIDENCE
