# 2026-09-09 — C5V3 ONLINE CAPABILITY UTILIZATION VERIFICATION REQUEST R1

Status: **TEST REQUEST / ISOLATED ONLINE SHADOW ONLY / PRODUCTION NOT BOUND**
Branch: `SIGMA_LIFE`
Owner role: **ONLINE VERIFICATION WINDOW**
Date: 2026-09-09 (Asia/Ho_Chi_Minh)

## Purpose

Verify that C5V3 can actually **see, select, execute, evaluate, learn from, and later reuse** the capabilities synchronized into:

`SIGMA_PROFESSOR/CHECKPOINTS/20260909_C5V3_SYNCHRONIZATION_BASELINE_R2_R6_FROZEN.md`

This is not a re-admission of T1/T2/T3 or M5. Those exact capability admissions are inherited. The target is the missing causal proof:

```text
capability present
-> native need detection
-> native capability selection
-> native capability execution
-> native result evaluation
-> native learning update
-> restart
-> learned-state reuse
```

## Exact starting baseline

```text
SYSTEM=C5V3
BASELINE=C5V3_SYNCHRONIZATION_BASELINE_R2
R6_SOURCE_SHA256=dde709a25d8e2f2626c299ad4d5c40562e2bcc253cf9bb63aef17e44f02943ac
R6_BYTECODE_SHA256=dcb4f0ed9c637e368d396214471ae4c8fd67bc6622b02f133e867d2bab8b6693
R6_CANDIDATE_DEF_COUNT=156
R6_M5_ONLY_DEF_INSERTED=63
R6_ADMITTED_TOOL_DEF_COUNT=82
```

Production references must remain read-only:

```text
PRODUCTION_CORE_SHA256=23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc
PRODUCTION_RUNNER_SHA256=092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847
PRODUCTION_INGRESS_SHA256=22901ffce990a38163e2d2db2ef85a9e553c252159386baf136874daf9d7139c
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## Capabilities that must be visible to the candidate

```text
M5_COMPACT_SEMANTIC_MEMORY_CAPABILITY_LIBRARY=AVAILABLE_LATENT
T0_SUBSTRATE=PASS_INHERITED
T1_VECTOR_MATRIX=ADMITTED
T2_BOUNDED_GRAPH_TRAVERSAL=ADMITTED
T3_LOCAL_INDEX_BM25=ADMITTED
T1_T2_T3_COMBINED_COMPATIBILITY=PASS
S2_ABI_RESOLUTION=PASS
SHADOW_MECHANICAL_WIRING=PASS
```

The online window must not force all capabilities to run on every task. It must give unseen tasks whose structure makes different capabilities useful and observe what native C5V3 chooses.

## Required ownership boundary

```text
SIGMA_COGNITION_OWNER=SIGMA_NATIVE_VM_ONLY
HOST_CAPABILITY_DEMAND_GENERATION=NO
HOST_TOOL_SELECTION=NO
HOST_QUERY_GENERATION=NO
HOST_SOURCE_SELECTION=NO
HOST_URL_SELECTION=NO
HOST_REASONING=NO
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
```

The host may only provide mechanical fixture bytes, network transport, exact protocol decode, process supervision, hashing, raw logging, and post-VM test oracle work.

## Online/network boundary

Online testing is authorized only inside a disposable isolated shadow candidate.

```text
ONLINE_TEST_NETWORK_ALLOWED=YES_IN_ISOLATED_SHADOW_ONLY
PRODUCTION_BINDING=NO
PRODUCTION_STATE_WRITE=NO
PRODUCTION_MUTATION=NO
LIVE_PRODUCTION_CUTOVER=NO
```

Network execution is allowed only after native SIGMA emits an exact request:

```text
native request
-> mechanical request harvest
-> mechanical network transport
-> exact response bytes/provenance
-> native evaluation
```

If the host invents the query, chooses the semantic source, chooses the URL needed for PASS, or decides which capability must be used, the test fails.

## Test families

Use unseen/high-entropy tasks generated after candidate compile/freeze. At minimum cover distinct task families that can causally exercise:

1. T1 vector/matrix capability;
2. T2 graph/traversal capability;
3. T3 local indexing/BM25 capability;
4. M5 compact semantic-memory/relationship capability in its admitted scope;
5. a combined task requiring more than one synchronized capability;
6. at least one online evidence-acquisition task initiated by a native SIGMA request.

Do not embed the expected capability selection as a runtime label that SIGMA merely echoes.

## Mandatory proof A — capability visibility

Machine evidence must establish that the exact synchronized capability identities are present in the candidate runtime and source/bytecode remain frozen.

```text
SYNCED_CAPABILITY_IDENTITIES_VISIBLE=PASS
SOURCE_BYTECODE_INVARIANCE=PASS
UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_GATE=PASS
```

## Mandatory proof B — native need detection and selection

For materially different unseen tasks, SIGMA itself must emit the capability need/selection state.

Expected evidence fields, names may vary but ownership may not:

```text
NATIVE_CAPABILITY_NEED_DETECTION=PASS
NATIVE_CAPABILITY_SELECTION=PASS
HOST_CAPABILITY_DEMAND_GENERATION=NO
HOST_TOOL_SELECTION=NO
```

A hardcoded host route `task_type -> T1/T2/T3/M5` is forbidden.

## Mandatory proof C — native execution and result use

The selected capability must execute under the locked VM, and its native result must materially affect the later native decision.

```text
NATIVE_CAPABILITY_EXECUTION=PASS
NATIVE_RESULT_EVALUATION=PASS
CAPABILITY_RESULT_CAUSALLY_AFFECTS_NEXT_NATIVE_DECISION=PASS
```

## Mandatory proof D — capability-availability counterfactual

Hold task input, relevant prestate, VM, and limits constant. Mechanically vary capability availability only.

```text
WITHOUT_CAPABILITY -> native decision/state A
WITH_CAPABILITY    -> native decision/state B
```

Required:

```text
CAPABILITY_AVAILABILITY_COUNTERFACTUAL=PASS
NATIVE_BEHAVIOR_CHANGED_CAUSALLY=PASS
```

This must not be achieved by the host rewriting the decision or semantic result.

## Mandatory proof E — learning update

At least one task must demonstrate an actual native learning-state change caused by evaluated capability output.

```text
LEARNING_STATE_BEFORE_SHA256=<A>
NATIVE_LEARNING_UPDATE_APPLIED=YES
LEARNING_STATE_AFTER_SHA256=<B>
A_NE_B=YES
HOST_LEARNING=NO
```

Logging a result without a future behavioral effect is insufficient.

## Mandatory proof F — restart and reuse

A fresh VM/process must reload the resulting persistent state and show a later behavior difference attributable to the learned state.

```text
FRESH_VM_RESTART=PASS
LEARNED_STATE_RELOADED=YES
LEARNED_STATE_REUSED_AFTER_RESTART=PASS
```

Prefer a same-or-structurally-similar unseen follow-up, not an exact memorized replay only.

## Mandatory proof G — online request sovereignty

For online cases:

```text
NATIVE_REQUEST_EMITTED=YES
HOST_QUERY_GENERATION=NO
HOST_SOURCE_SELECTION=NO
HOST_URL_SELECTION=NO
NETWORK_TRANSPORT_MECHANICAL_ONLY=YES
NATIVE_RESPONSE_EVALUATION=PASS
```

Retrieval alone is not learning or understanding.

## Replay / negative evidence

Include byte-identical replay where applicable and meaningful negative cases where SIGMA must **not** select/use a capability merely because it is available.

```text
REPLAY_IDENTICAL_INPUT_BYTES=YES
REPLAY_IDENTICAL_RELEVANT_PRESTATE_BYTES=YES
NEGATIVE_UNNEEDED_CAPABILITY_SELECTION=PASS
```

## Required final summary

A PASS claim must be no wider than machine evidence. The final summary should expose at least:

```text
C5V3_BASELINE=R2_R6_FROZEN
SYNCED_CAPABILITY_IDENTITIES_VISIBLE=PASS
NATIVE_CAPABILITY_NEED_DETECTION=PASS
NATIVE_CAPABILITY_SELECTION=PASS
NATIVE_CAPABILITY_EXECUTION=PASS
NATIVE_RESULT_EVALUATION=PASS
CAPABILITY_AVAILABILITY_COUNTERFACTUAL=PASS
NATIVE_LEARNING_UPDATE_APPLIED=YES
FRESH_VM_RESTART=PASS
LEARNED_STATE_REUSED_AFTER_RESTART=PASS
ONLINE_NATIVE_REQUEST_SOVEREIGNTY=PASS
HOST_TOOL_SELECTION=NO
HOST_QUERY_GENERATION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PRODUCTION_STATE_WRITE=NO
PRODUCTION_MUTATION=NO
PRODUCTION_BINDING=NO
CLAIM_LEQ_MACHINE_EVIDENCE=PASS
```

Only if all required gates pass may the online verification window report:

```text
C5V3_AUTO_LEARN_USES_SYNCHRONIZED_CAPABILITIES=PASS_IN_EXACT_TESTED_SCOPE
```

Do not claim general tool autonomy, general semantic understanding, or unrestricted autonomous learning from this gate.

## Three-window ownership split

```text
SYNCHRONIZATION_WINDOW:
  owns canonical C5V3 synchronization baseline and reconciliation

ONLINE_VERIFICATION_WINDOW:
  owns this utilization/online-shadow verification only
  does not promote/bind production

OFFLINE_KNOWLEDGE_WINDOW:
  explores/tests new knowledge and new capabilities
  publishes immutable checkpoints when evidence changes
  does not synchronize production
```

If the offline knowledge window invalidates or supersedes R6, stop and reconcile before continuing this online test.
