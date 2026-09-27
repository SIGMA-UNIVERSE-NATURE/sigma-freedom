# SIGMA V09 -> VKM Native Language Call-Graph Discovery R3 FIX2 Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Mode: READ_ONLY_DISCOVERY

## Repair

Correct Owner fingerprint:

c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

R3 FIX2 removes the bad FIX1 constant and adds:
OWNER_FINGERPRINT_EXACT_64HEX_STATIC=PASS

It also statically rejects the stale incorrect fingerprint from runtime scripts/docs.

## Preserved boundaries

CANONICAL_MUTATION_ALLOWED=NO
OWNER_REBIND_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
SEMANTIC_EXECUTION_PERFORMED=NO

The call-graph analysis remains unchanged in purpose:
- inventory API401-410 / owner401-410 definitions;
- build inbound/outbound call graph;
- identify Owner/Native-Binding/top-level references;
- disqualify expected/result/ablate/probe/test helpers from automatic entry-point selection;
- refuse name-score-only selection.

## Release

BUNDLE=
SIGMA_V09_TO_VKM_NATIVE_LANGUAGE_CALLGRAPH_DISCOVERY_R3_FIX2_BUNDLE.zip

BUNDLE_SHA256=
c0002ca6c7086cefd0c8004091dc388664bbc1388e24dbc6b33524d5719c7dad

Release verification:
- MANIFEST.sha256=PASS
- PYTHON_SYNTAX=PASS
- BASH_SYNTAX=PASS
- CALLGRAPH_DISCOVERY_STATIC=PASS
- EXPECTED_HELPER_DISQUALIFICATION_STATIC=PASS
- OWNER_BINDING_REFERENCE_ANALYSIS_STATIC=PASS
- OWNER_FINGERPRINT_EXACT_64HEX_STATIC=PASS
- SELFTEST=PASS

Runtime status:
NOT_YET_RUN

NEXT=RUN_R3_FIX2
