# SIGMA I3B — V6R1 native-policy repair source ready

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: SOURCE_READY / RUNTIME_ADMISSION_NOT_RUN

## Dependency

I3A is already machine-admitted in exact tested scope:

```text
I3A_NATIVE_ADMISSION_V1=PASS
POST_FOLLOWUP_OUTCOME_GATE_TESTED_SCOPE=PASS
TOTAL_VM_INVOCATIONS=24
POST_VM_ALIGNMENT_PASS_COUNT=24
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
```

Exact V6 code audit checkpoint:

`DOCS/GPT_REFERENCE/SIGMA_I3B_V6_EXACT_CODE_AUDIT_HOST_THRESHOLD_BLOCK_20260905.md`

The exact audit established:

```text
PYTHON_BUILD_VIEW_ROLE=MECHANICAL_STRUCTURAL_VIEW_BUILDING_ONLY_IN_INSPECTED_CODE
V6_NATIVE_CONTENT_READING_AND_ASSESSMENT=YES
DIRECT_V6_REUSE_FOR_I3B=BLOCKED_PENDING_NATIVE_POLICY_OWNERSHIP
```

## Repair

A new additive native successor has been prepared:

`SIGMA_I3B_NATIVE_CORPUS_EVIDENCE_ASSESSOR_V6R1.sigma`

The historical V6 source is not deleted or rewritten in place.

V6R1 preserves the original native:

- topic reading;
- lesson reading;
- ASCII/script classification;
- unique topic-token overlap calculation;
- compatible-lesson counting;
- distinct-source counting;
- native state vocabulary:
  - `UNKNOWN`
  - `INSUFFICIENT`
  - `MORE_EVIDENCE`
  - `COLLECTION_ENOUGH_FOR_NEXT_STAGE`.

The material change is policy ownership:

```text
HISTORICAL_V6_BASH_MIN_COMPATIBLE=2
HISTORICAL_V6_BASH_MIN_SOURCES=2
HISTORICAL_V6_BASH_MIN_OVERLAP=2

V6R1_BASH_THRESHOLD_POLICY=REMOVED_FROM_ACTIVE_PATH
V6R1_NATIVE_STATIC_MIN_COMPATIBLE=2
V6R1_NATIVE_STATIC_MIN_SOURCES=2
V6R1_NATIVE_STATIC_MIN_OVERLAP=2
ASSESSMENT_POLICY_OWNER=SIGMA_NATIVE_V6R1
```

These are a bounded teacher-authored native capability policy, not a learned policy.

Keep:

```text
STATIC_EVIDENCE_THRESHOLD_POLICY_LEARNED=NOT_PROVEN
GENERAL_RESEARCH_POLICY_LEARNED=NOT_PROVEN
```

## Exact identities

```text
I3A_SOURCE_SHA256=be998fd907d93337cc3befe8582503a80256c1fea658fa8691d00fa8c5a67574
V6R1_SOURCE_SHA256=c2c34f0df600910fa4ccfa7deb8344ab83a61b86bfeaf369bafced4ad7b73938
MECHANICAL_VIEW_BUILDER_SHA256=8ebd9d22b7b6f649d77f8cbf056f2d2eb2df03b7ef7fc7d2b03f40022322d66e
I3B_RUNNER_SHA256=98247b80dabf2575b4444c47a558f8db046dd8d54a423f0aecf8d80558c5ce82
I3B_BUNDLE_SHA256=a93797176581b18c85728ccdd0367af3679b0a1d2b5142240618d6f0f4845213
```

## I3A -> I3B causality

The final event file left by the I3A 24-case admission matrix is not used as canonical integration evidence because later replay fixtures overwrite that file.

I3B therefore:

1. recompiles the exact admitted I3A source under the locked compiler;
2. replays I3A once on the exact canonical prior/fresh control interfaces in a clean isolated namespace;
3. requires native I3A to emit a fresh exact event;
4. mechanically validates the event protocol;
5. dispatches V6R1 only if native SIGMA emitted `ASSESS_FRESH_EVIDENCE`;
6. binds the event RUN_ID to the fresh collection path mechanically;
7. uses the exact historical Python view builder only for structural view construction;
8. runs V6R1 native assessment;
9. accepts the canonical assessment state as machine output — no canonical state is prewritten in the runner.

```text
HOST_EVENT_SELECTION=NO
HOST_EVENT_GENERATION=NO
HOST_ASSESSMENT_STATE_SELECTION=NO
HOST_UNDERSTANDING_CLASSIFICATION=NO
HOST_SEMANTIC_EVIDENCE_SELECTION=NO
```

If I3A does not emit `ASSESS_FRESH_EVIDENCE`, the runner HOLDS instead of manufacturing the event.

## Anti-hardcode admission plan

Planned locked-VM invocations:

```text
TOTAL_VM_INVOCATIONS=12
I3A_CANONICAL_REPLAY_VM_INVOCATIONS=1
V6R1_VM_INVOCATIONS=11
```

V6R1 runtime cases include:

- canonical fresh collection — exact native state accepted without a prewritten expected state;
- dynamic `UNKNOWN` fixture;
- dynamic `INSUFFICIENT` fixture;
- dynamic `MORE_EVIDENCE` fixture;
- dynamic `COLLECTION_ENOUGH_FOR_NEXT_STAGE` fixture;
- same-source counterexample;
- mixed compatible/incompatible counterexample;
- unseen high-entropy dynamic topics;
- identical replay cases.

Required anti-hardcode checks:

```text
CANONICAL_RUN_ID_LEAK_IN_V6R1_SOURCE_OR_BYTECODE=0
CANONICAL_TOPIC_SHA_LEAK_IN_V6R1_SOURCE_OR_BYTECODE=0
DYNAMIC_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_V6R1_SOURCE_OR_BYTECODE=0
DYNAMIC_COUNTEREXAMPLE_STATE_CHANGE=YES
REPLAY_IDENTICAL_STATE=YES
REPLAY_IDENTICAL_METRICS=YES
REPLAY_IDENTICAL_VM_OUTPUT=YES
```

Expected states for synthetic fixtures exist only in the post-VM test oracle and are never supplied to SIGMA.

## Understanding-state sovereignty

I3B/V6R1 assesses bounded collection evidence sufficiency. It does not emit an understanding state and does not decide truth.

```text
UNDERSTANDING_STATE_EMITTED_BY_I3B=NO
TRUTH_DECISION=NOT_EXECUTED
KNOWLEDGE_PROMOTION=NOT_EXECUTED
SEMANTIC_UNDERSTANDING=NOT_PROVEN
```

No GPT/host/human may translate `COLLECTION_ENOUGH_FOR_NEXT_STAGE` into “SIGMA understands”.

## Runtime proof state

```text
I3B_SOURCE_READY=YES
I3B_LOCKED_SIGMAC_COMPILE=NOT_RUN
I3B_BYTECODE_SHA256=UNKNOWN
I3B_RUNTIME_ADMISSION=NOT_RUN
I3A_TO_NATIVE_FRESH_EVIDENCE_ASSESSMENT_DISPATCH=NOT_PROVEN
I3C_NATIVE_CONTINUATION_FROM_ASSESSMENT_STATE_UNLOCKED=NO_PENDING_I3B_PASS
CLOSED_AUTONOMOUS_NATURAL_LANGUAGE_WEB_LEARNING_LOOP=NOT_PROVEN
```

## Exact next action

Run the source-ready bundle on the locked OPPO/Termux runtime. Preserve the first HOLD/FAIL or final I3B summary exactly.

Do not rerun I2R1. Do not weaken the event gate. Do not prewrite the canonical assessment state.
