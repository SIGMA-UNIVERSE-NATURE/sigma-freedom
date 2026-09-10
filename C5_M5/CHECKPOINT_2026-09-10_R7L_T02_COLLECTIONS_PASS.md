# SIGMA C5 M5 — R7L-T02 Collections PASS

Date: 2026-09-10

## Result

Genuine OPPO offline admission PASS for R7L-T02 Collections FIX1.

- `R7L_T02_COLLECTIONS_ADMISSION=PASS`
- `RESULT=R7L_T02_PASS`
- `NEXT=R7L_T03_UNICODE_SPANS`

The original T02 bundle remained HOLD because top-k with `K=0` emitted a non-canonical empty `ITEMS=` value. It was not published. FIX1 closes the contract to require `-` for empty collection/list/state outputs and adds `TOP_K_EMPTY_CANONICAL=PASS`.

## Frozen OPPO tool identity

- ABI version `R7L-T02/1`
- source SHA256 `8558da916bf494ce7bc45d6aba19a0946c23ab15e2ea9cbd58c36eb4e867de86`
- binary SHA256 `bd03a456ff3a8604bf04cd4dc67794887d6514e2ffb1996197c9ec60dba2578a`
- compiler `/data/data/com.termux/files/usr/bin/clang++`
- ABI SHA256 `1a5ac3adb3ad9bfdb5704d74093ddb385328bd7c9e192bef21c2aa8618100a53`
- input schema SHA256 `f5508dba3da788330d685f88c48ed7940657b68455b6eb09799b5db6fb5c3fba`
- output schema SHA256 `f3ca67425c500075a81be281d92c5eb378581ed126340a9449b0d85ad794ca93`
- resource profile SHA256 `1e376c7d318891ad0c75454e74d7cde41523618c78670e353148f1ea1db311f0`
- prior admitted artifact lock SHA256 `d509746771f44d60e57fe1020aa2471496f9f46c7c74b71443db4707576a91bb`
- contract root SHA256 `c31dfd9ef963a75431808388c916327ea9f4cb604e413b598ee96771265ea7a7`
- admission root SHA256 `7d17afd07e5a236b7160b2fec02e9e4cdcf9b77ced12ded9ddd27372a61f74ed`

## Admission evidence

- deterministic compile PASS
- source/binary/ABI/schema/resource freeze PASS
- high-entropy literal leak audit PASS
- dynamic fixtures after freeze PASS
- 16 directed + 32 randomized-after-freeze + 2 replay = 50 admission cases
- 65 native process invocations
- post-tool mechanical oracle PASS
- map/set/multimap/ordered-map mechanics PASS
- deque and caller-priority queue PASS
- stable sort and caller-score top-k PASS
- exact-byte first-occurrence dedupe PASS
- bounded LRU-like candidate cache PASS
- explicit cache eviction receipt PASS
- `TOP_K_EMPTY_CANONICAL=PASS`
- exact iterator PASS
- malformed/adversarial matrix PASS
- resource-bound matrix PASS
- counterfactual behavior change PASS
- prior R7L-T01 and T1-T10 identity-lock regression PASS
- forbidden semantic API audit PASS

## Semantic / authority boundary

- `CACHE_EVICTION_IS_MEMORY_IMPORTANCE=NO`
- `TOP_K_IS_SEMANTIC_RELEVANCE=NO`
- `RETRIEVED_IS_RELEVANT=NO`
- `CANONICAL_EPISTEMIC_MEMORY_SILENT_EVICTION=NO`
- `PERSISTENT_STATE=NO`
- `STATE_OUTPUT_ROLE=CANDIDATE_COLLECTION_STATE_ONLY`
- `HOST_TOOL_SELECTION=NO`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `HOST_LEARNING=NO`
- `CORE_TEST_ORACLE_CONTAMINATION=NO`
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`

## SIGMA baseline reference — not re-verified by this admission

For audit separation only, the production baseline previously recorded is:

- SIGMA core `23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc`
- runner `092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847`
- sigmac `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- ingress `22901ffce990a38163e2d2db2ef85a9e553c252159386baf136874daf9d7139c`

T02 did not hash these live files before/after execution. Therefore:

- `SIGMA_BASELINE_REFERENCE=RECORDED`
- `SIGMA_BASELINE_IDENTITY_LOCK=NOT_TESTED_BY_T02`
- `SIGMA_BASELINE_NO_MUTATION=NOT_TESTED_BY_T02`

This distinction prevents tool identity from being misreported as SIGMA identity.

## Production boundary

- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

## Claim ceiling

`TOOL_AVAILABLE != TOOL_LEARNED`.

This checkpoint establishes availability of the R7L-T02 mechanical tool family only. It does not prove SIGMA selected, invoked, interpreted, learned from, or committed state from T02.
