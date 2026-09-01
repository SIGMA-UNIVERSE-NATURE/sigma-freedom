# SIGMA — AUTO INTERNET LESSON CURRENT CHECKPOINT

STATUS_DATE=2026-09-01
BRANCH=SIGMA_LIFE
CANONICAL_FOR_NEXT_WINDOWS=YES

## CURRENT GOAL

The proof target is NOT a Bash-orchestrated one-start wrapper.
The proof target is:

```text
USER RUNS SIGMA VM CONTROLLER ONCE
→ SIGMA controller receives RAW_TOPIC
→ SIGMA decides/requests query generation
→ SIGMA requests Internet search capability
→ SIGMA receives discovered URLs
→ SIGMA requests technical network membrane/fetch
→ SIGMA requests/uses lesson reader
→ SIGMA requests lesson persistence/provenance
→ SIGMA STOP
```

Required:

```text
MAIN_CONTROLLER_LANGUAGE=SIGMA
MAIN_ENTRYPOINT=SIGMA_VM
HOST_ORCHESTRATES_LEARNING_FLOW=NO
HUMAN_INTERVENTION_BETWEEN_STAGES=0
```

Host/C/Python/Bash may provide only generic mechanical capabilities: network transport, DNS/TLS, RSS/XML transport parsing, file lifecycle, hash, resource limits, and exact child-Sigma execution if required. They may not choose query, URL, lesson, semantic winner, relevance, truth, or next cognitive stage.

## PRESERVE LOCK

QUERY_ENGINE_SHA256=db199f572a9415dc812fb3936387541a3b1e648f3836387541a3b1e648f383d5e1da6487f11e97c4b6a
LESSON_READER_SHA256=ba2faf7bddb81789b3fbccff96bdf8f3c2021d0db252d7e8ef38dc92b182994c
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
HTTP_BRIDGE_SHA256=d7dcc121dbd4611ea5f2cf677f5ec08567b8a03ba11ae57ba4c1624b3f638d1e

QUERY_ENGINE_REWRITE=FORBIDDEN
LESSON_READER_REWRITE=FORBIDDEN
ZERO_ANSWER_INJECTION=LOCKED

NOTE: verify the query-engine hash from the actual preserved bytecode before use. If it does not match the known machine evidence, STOP rather than rewriting/rebuilding silently.

## PROVEN TESTED SCOPE ALREADY AVAILABLE

SIGMA_QUERY_GENERATION=PASS_TESTED_SCOPE
LIVE_INTERNET_SEARCH_TRANSPORT=PASS_TESTED_SCOPE
OPEN_WEB_URL_DISCOVERY=PASS_TESTED_SCOPE
NETWORK_SAFETY_MEMBRANE=PASS_TESTED_SCOPE
SIGMA_HUMAN_WEB_TEXT_EXTRACTION=PASS_TESTED_SCOPE
BYTE_EXACT_EXPERIENCE_READBACK=PASS_TESTED_SCOPE

## LAST REAL OPPO AUTO ATTEMPT

RUN_DIR=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_exec/HH_AUTO_INTERNET_LESSONS/runs/20260901T120406Z_6891_26254
SIGMA_QUERY_RC=0
SIGMA_QUERY_CANDIDATES=9
QUERY_READBACK_CMP_RC=0
SEARCH_REQUESTS=3
SEARCH_HTTP_200=3
SEARCH_TRANSPORT_COMPLETE=3
RSS_RESULTS_PRESENT=YES
DISCOVERED_URLS=0
SOURCE_REQUESTS=0
LESSON_ACQUIRED=0

CANONICAL_FAILURE=FAIL_HARNESS_DISCOVERY_DRIVER
NOT_SIGMA_FAILURE=YES
NOT_NO_LESSON_FOUND=YES

ROOT_CAUSE_1=BASH_ARITHMETIC_USED_COMMAND_SUBSTITUTION_INSTEAD_OF_ARITHMETIC_EXPANSION
ROOT_CAUSE_2=PYTHON_WAS_INVOKED_WITH_RSS_BODY_AS_SOURCE_CODE_INSTEAD_OF_DATA_ARGUMENT

## DEPRECATED HOST-ORCHESTRATED QA CANDIDATE

The previously prepared five-script host wrapper:

00_VERIFY_AUTO_LESSON_RUNTIME.sh
10_RSS_ITEM_LINK_EXTRACT.py
20_AUTO_INTERNET_LESSON_V1_R1.sh
30_VERIFY_AUTO_INTERNET_LESSON_V1_R1.sh
99_RUN_AUTO_INTERNET_LESSON_V1_R1.sh

was syntax/mock QA'd, but it is now:

```text
DEPRECATED_FOR_SIGMA_AUTONOMY_PROOF=YES
```

It may be retained only as a host-integration test/reference. It MUST NOT be used to claim that Sigma itself orchestrates automatic lesson acquisition, because Bash controls the stage order.

## CURRENT FRONTIER

CURRENT_FRONTIER=BUILD_VM_CALLABLE_GENERIC_CAPABILITY_SUBSTRATE_FOR_SIGMA_CONTROLLER

Do NOT jump directly to a fake SIGMA controller calling invented host operations.
Current online evidence does not establish an existing VM host-op such as http_get/eval/shell that can drive the Internet pipeline directly.

The next implementation must therefore proceed in this order:

1. Determine the exact existing VM-to-host extension point using known runtime source/evidence; no broad local knowledge scan and no guessed host-op names.
2. Build/verify a VM-callable GENERIC capability adapter at the substrate layer. It may expose only mechanical operations needed by a Sigma controller, such as safe network fetch, RSS item-link extraction, file/hash/resource operations, and exact child-Sigma execution if required.
3. Independently machine-test each adapter operation with non-semantic fixtures.
4. Build `SIGMA_AUTO_LESSON_CONTROLLER_V1.sigma` as the MAIN controller in SIGMA Language.
5. The controller, not Bash/Python, must choose/request stage progression based on returned machine facts.
6. Compile controller and run with the direct entrypoint:

```bash
./native/sigma-vm.v09_candidate "$CONTROLLER_BC" <"$REQUEST_INPUT" >"$CONTROLLER_OUT"
```

7. Only direct-VM execution may be used for the final autonomy proof.

## GENERIC CAPABILITY BOUNDARY

Allowed substrate capabilities:

- SAFE_HTTP_FETCH(url, resource bounds) → technical response facts/body artifact
- RSS_ITEM_LINKS(rss artifact) → ordered exact item links
- FILE_READ/WRITE/EXISTS/SIZE
- SHA256
- resource accounting
- exact RUN_SIGMA(child bytecode, input, outputs) if needed to preserve the existing query generator and lesson reader

These names are capability-contract descriptions, NOT assumed existing host-op names. Implement only through the actual proven VM extension mechanism.

Forbidden in host/substrate:

- semantic query generation
- semantic URL/source ranking
- relevance decisions
- truth decisions
- lesson quality decisions
- reasoning/conclusion
- cognitive next-stage policy

## FINAL ACCEPTANCE GATE

Required before promotion:

MAIN_CONTROLLER_LANGUAGE=SIGMA
MAIN_ENTRYPOINT=SIGMA_VM
HOST_ORCHESTRATES_LEARNING_FLOW=NO
HUMAN_INTERVENTION_BETWEEN_STAGES=0
SIGMA_CONTROLLER_RC=0
SIGMA_QUERY_GENERATION_USED=YES
LIVE_SEARCH_REQUESTS>0
DISCOVERED_URLS>0
TECHNICAL_SOURCE_FETCH_REQUESTS>0
RESOURCE_BUDGET_OVERRUN=0
BRIDGE_CEILING_VIOLATION=0
LESSON_ACQUIRED=1
SIGMA_LESSON_READER_USED=YES
LESSON_PARAGRAPHS>0
LESSON_BYTES>0
LESSON_READBACK_CMP_RC=0
LESSON_SHA256=<real hash>
PROVENANCE_SHA256=<real hash>
RAW_WEB_BODIES_RETAINED=0
WEB_CONTENT_EXECUTED=0
INDEPENDENT_VERIFY_RC=0

Only then may the verifier emit:

ONE_START_AUTOMATIC_INTERNET_LESSON_ACQUISITION=PASS_TESTED_SCOPE

Still NOT proven after that:

FULL_AUTONOMOUS_LEARNING
SEMANTIC_UNDERSTANDING
TOPIC_RELEVANCE
SOURCE_TRUST
LESSON_TRUTH
SELF_DIRECTED_CURRICULUM

NEXT_COMMAND=BUILD_VM_CALLABLE_GENERIC_CAPABILITY_SUBSTRATE_V1
