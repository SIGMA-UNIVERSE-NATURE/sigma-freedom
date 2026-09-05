# SIGMA I5B — Wikipedia Native Candidate Selector Source Ready

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: SOURCE_READY / RUNTIME_ADMISSION_NOT_RUN

## Dependency

I5A Fix2 is admitted PASS in exact tested scope:

```text
I5A_WIKIPEDIA_EN_DISCOVERY_ADAPTER_V1=PASS
NATIVE_SOURCE_DISCOVERY_REQUEST=PASS_IN_EXACT_TESTED_SCOPE
WIKIPEDIA_DISCOVERY_TRANSPORT=PASS_IN_EXACT_TESTED_SCOPE
LIVE_WIKIPEDIA_CANDIDATE_COUNT=10
HOST_DECODED_COMPLETE_BOUNDED_CANDIDATE_SET=YES
REMOTE_API_ORDER=PROVENANCE_ONLY
HOST_CANDIDATE_SELECTION=NO
HOST_RESOURCE_SELECTION=NO
```

Immutable dependency checkpoint:
`DOCS/GPT_REFERENCE/CHECKPOINTS/20260906_I5A_FIX2_WIKIPEDIA_EN_DISCOVERY_NATIVE_ADMISSION_PASS.md`

## I5B capability contract

I5B consumes the exact complete bounded candidate set returned by I5A and selects one Wikipedia resource inside native SIGMA.

Bounded native operational exploration policy:

```text
1. LEAST_PREVIOUSLY_SELECTED_PAGE
2. THEN_HIGHER_WORDCOUNT
3. THEN_HIGHER_PAGE_SIZE
4. THEN_LOWER_PAGE_ID_DETERMINISTIC_TIEBREAK
```

The policy does not use remote API order.

```text
REMOTE_API_ORDER_USED_FOR_SELECTION=NO
HOST_RESULT_RANKING=NO
HOST_CANDIDATE_SELECTION=NO
HOST_RESOURCE_SELECTION=NO
```

This is a teacher-authored static native operational policy, not a learned general research/resource policy and not a semantic relevance model.

```text
STATIC_RESOURCE_SELECTION_POLICY_LEARNED=NOT_PROVEN
SEMANTIC_RESOURCE_RELEVANCE=NOT_PROVEN
```

## Exact identities

```text
BUNDLE_NAME=SIGMA_I5B_NATIVE_ADMISSION_V1_WIKIPEDIA_CANDIDATE_SELECTOR_BUNDLE.zip
BUNDLE_SHA256=cba7913b0084109629375b7fa123808a35f01c53537c67bd7421dcea78634dae
I5B_SOURCE_SHA256=e2f1035092d2c1bc0141d9982f575a8dd88091de7080982bfd2fe53f61bd3ae8
I5B_RUNNER_SHA256=1942670b450a7272059a131dbf086e51462e8ae2c2c11e35dc0e9a557267505f
I5A_DEPENDENCY_SOURCE_SHA256=0d49e744c1d0395ca18dc87f40ea706da29d94474c42ac948ff2071980addd11
I5B_BYTECODE_SHA256=UNKNOWN_NOT_COMPILED
```

## Canonical dependency binding

Runner reads the existing I5A Fix2 PASS artifacts on OPPO:

```text
I5A_PASS_OUTPUT=$HOME/SIGMA/sigma_genesis1/I5A_NATIVE_ADMISSION_V1_FIX2_RUN/SIGMA_I5A_NATIVE_ADMISSION_V1_FIX2_WIKIPEDIA_EN_DISCOVERY/I5A_NATIVE_ADMISSION_V1_FIX2.out
I5A_CANONICAL_CANDIDATE_SET=<same package>/runtime/host/canonical.candidates.state
```

It compiles exact admitted I5A source and replays only native `VERIFY` against that persisted live candidate set. No new HTTP request is made.

```text
I5A_REPLAY_MODE=VERIFY_ONLY_NO_HTTP
SOURCE_CANDIDATE_SET=I5A_FIX2_LIVE_CANONICAL_ARTIFACT
```

Only after native I5A emits a fresh valid result event does the harness copy the complete candidate set into I5B input.

## Anti-hardcode / admission plan

Canonical selected resource is not prewritten in the runner:

```text
CANONICAL_EXPECTED_RESOURCE_PREWRITTEN_IN_RUNNER=NO
```

Runner accepts the canonical native selection only if exact page ID/title are members of the candidate set.

Planned locked-VM invocations:

```text
TOTAL_VM_INVOCATIONS=16
I5A_VERIFY_REPLAY_VM_INVOCATIONS=1
I5B_VM_INVOCATIONS=15
```

Admission includes:

- live canonical resource selection;
- canonical candidate row reorder invariance;
- persistent selection history changing later selection;
- idempotency;
- zero-candidate hold;
- malformed candidate-set refusal;
- duplicate page-ID refusal;
- dynamic candidate metric change causing selection change;
- dynamic candidate reorder invariance;
- wrong-family refusal;
- 64-record native memory bound refusal;
- canonical page-ID token leak audit;
- high-entropy dynamic title token leak audit;
- identical replay from identical prestate.

Native event shape:

```text
I5B_EVENT||RUN_ID||WIKIPEDIA||EN||PAGE_ID||TITLE||COMMIT||YES
```

## Persistence/boundedness

I5B native selection ledger is bounded to 64 prior records in this version.
The current run ID is excluded when counting prior selections so exact idempotent replay recomputes the same pre-run decision.

```text
MEMORY_RECORD_BOUND=64
PERSISTENT_SELECTION_LEDGER=PLANNED_RUNTIME_TEST
IDEMPOTENCY=PLANNED_RUNTIME_TEST
```

## Claim boundaries until runtime PASS

```text
I5B_RUNTIME_ADMISSION=NOT_RUN
NATIVE_RESOURCE_SELECTION=NOT_PROVEN
V5K2_EXACT_FETCH_DISPATCH_FOR_SIGMA_SELECTED_WIKIPEDIA_RESOURCE_UNLOCKED=NO_PENDING_I5B_PASS
STATIC_RESOURCE_SELECTION_POLICY_LEARNED=NOT_PROVEN
SEMANTIC_RESOURCE_RELEVANCE=NOT_PROVEN
TRUTH_DECISION=NOT_EXECUTED
KNOWLEDGE_PROMOTION=NOT_EXECUTED
SEMANTIC_UNDERSTANDING=NOT_PROVEN
DIRECT_I4_TO_V5_RUNTIME_INTEGRATION=NOT_PROVEN_PENDING_EXACT_FETCH_BINDING
CLOSED_AUTONOMOUS_NATURAL_LANGUAGE_WEB_LEARNING_LOOP=NOT_PROVEN
```

Next action: run this exact bundle on the locked OPPO/Termux runtime and preserve the first HOLD/FAIL or final I5B summary exactly.
