# SIGMA I3C — I2R1 exact-code audit under exclusive self-learning / anti-hardcode lock

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: EXACT_CODE_AUDIT_COMPLETE / DIRECT_I2R1_REPLAN_REUSE_BLOCKED_FOR_CLOSED_CHAIN

## Export identity

User-supplied OPPO export archive was received and verified:

```text
EXPORT_ARCHIVE_SHA256=ba0413abf1080919f13075bf73b8fd49c2e4a57e2672defc8ab983f8b5f5fbf5
```

Inner manifest passed for all exported files.

Exact identities:

```text
REPLAN_SOURCE_SHA256=1d6bdc235eaf8e0e3a94ca1ed62972e50babf7472ef7a6b948d2c3c30ec4976f
UNION_TOOL_SHA256=ce955606d434e2f15ab07608235c3700bddf76312f3583da71194a19b9a074f3
DIRECT_V11_RUNNER_SHA256=f8ef517aaa1143e7e1917e28378b634d3b7a1ca755186c6116c02196f1d4d15e
REPLAN_RUNNER_SHA256=6753cbe7fb34da03024548ba8c2955f3801e7d986c2cd8025094b977d3805572
I2R1_RUNNER_SHA256=39247c41745ae62fb85f10656a3f1bdbc32b32745f1561f232c962fe58c2554c
VERIFIER_PY_SHA256=a39be9ffb6f5ef205400bfa7627ef08a78b1c38b678c0f44e6d5140867b73213
VERIFIER_SH_SHA256=dd04c58ba296b2e9f238a80d0b84640a3ee5e4df8361cb0ee7449e00c53921dd
WRAPPER_SHA256=971b1f0ad89cb1d9f909abcc56ba361291aacb9a722f5b7096fd2b536d7e9a78
```

## Host-side audit

### Mechanical lesson union

`18_MECHANICAL_ALL_LESSON_UNION_I2R1.py`:

- enumerates every `lesson.experience.txt` file;
- sorts only by relative path;
- reads exact bytes from every file;
- joins all bytes with a fixed byte separator;
- records path/size/SHA manifest;
- performs no semantic filtering, ranking, scoring, source selection, truth decision, or next-action selection.

Classification:

```text
UNION_TOOL_ROLE=MECHANICAL_ALL_LESSON_BYTE_UNION
HOST_SEMANTIC_FILTERING=NO_IN_INSPECTED_CODE
HOST_SEMANTIC_RANKING=NO_IN_INSPECTED_CODE
HOST_NEXT_ACTION_SELECTION=NO_IN_INSPECTED_CODE
```

### Bash runners

The Bash runners:

- verify exact identities and required artifacts;
- bind the assessment state/topic/evidence/metrics to native VM inputs;
- check exact native output protocol values before mechanical dispatch;
- invoke native V11 only after the native replan output exists;
- invoke V5 collection only after native V11 emits `RUN_ADAPTED_COLLECTION`;
- do not generate the adapted query/topic themselves.

The checks for `RESEARCH_MORE` and `STRENGTHEN_TOPIC_COOCCURRENCE` are post-native dispatch gates; they do not write those values into SIGMA input. However, those values are prewritten in the native replan source itself, which is the anti-hardcode issue below.

Classification:

```text
I2R1_BASH_NEXT_ACTION_SELECTION=NO_IN_INSPECTED_CODE
I2R1_BASH_QUERY_COMPOSITION=NO_IN_INSPECTED_CODE
I2R1_BASH_SEMANTIC_EVIDENCE_SELECTION=NO_IN_INSPECTED_CODE
I2R1_BASH_ROLE=MECHANICAL_GATE_DISPATCH_AND_VERIFICATION_IN_INSPECTED_CODE
```

## Native replan anti-hardcode finding

Exact source `17_SIGMA_COLLECTION_MORE_EVIDENCE_REPLAN_I2R1.sigma` contains the following static policy:

```text
initial state/action = STOP_UNKNOWN
if assessment_state == MORE_EVIDENCE
and topic/evidence/metrics are nonempty:
    state = COLLECTION_MORE_EVIDENCE_RESEARCH_CONTINUATION_READY
    action = RESEARCH_MORE
    strategy = STRENGTHEN_TOPIC_COOCCURRENCE
```

The source therefore literally contains the current-case next action and strategy tokens that were expected in the canonical I2R1 run.

Before the repository-wide anti-hardcode lock, this was admitted as a bounded native policy and the historical I2R1 runtime PASS remains valid in its exact historical tested scope.

Under the newer directive:

```text
ANTI_HARDCODE=MANDATORY_ADMISSION_CONTROL
HARDCODED_CURRENT_NEXT_ACTION=FORBIDDEN
PREWRITTEN_RUNTIME_SEMANTIC_ANSWER=FORBIDDEN
```

this exact source must NOT be connected directly as the active continuation policy for the future closed autonomous self-learning chain.

```text
I2R1_HISTORICAL_PASS_REVOKED=NO
I2R1_HISTORICAL_PASS_SCOPE_PRESERVED=YES
DIRECT_I2R1_REPLAN_REUSE_FOR_I3C_CLOSED_CHAIN=BLOCKED
BLOCK_REASON=NATIVE_SOURCE_PREWRITES_CURRENT_NEXT_ACTION_AND_SINGLE_CURRENT_STRATEGY
```

## Required I3C successor

I3C must be additive and native-only.

It may reuse:

- exact mechanical all-lesson union;
- exact assessment state/metrics interface from I3B/V6R1;
- native VM execution and persistent state primitives;
- bounded action vocabulary as protocol vocabulary.

But the current canonical next action must not be embedded as the only favorable mapping. I3C admission must show materially different runtime assessment/metric/history inputs causing materially different native continuation actions, with canonical output not prewritten in the host verifier.

Minimum dynamic branches should include, when structurally applicable:

```text
CONTINUE_RESEARCH
CHANGE_RESEARCH_STRATEGY
DIVERSIFY_EVIDENCE_SOURCE
HOLD_UNRESOLVED
STOP_UNKNOWN
ADVANCE_COLLECTION_PHASE
```

Exact final vocabulary may differ, but the canonical result must be observed from SIGMA-native output rather than supplied by the harness.

Required gates:

```text
DYNAMIC_INPUT=YES
MATERIALLY_DIFFERENT_INPUTS=YES
NEGATIVE_OR_COUNTEREXAMPLE=YES
COUNTERFACTUAL_BEHAVIOR_CHANGE=YES
UNSEEN_HIGH_ENTROPY_INPUT=YES_WHEN_PRACTICAL
SOURCE_TOKEN_LEAK_AUDIT=YES
BYTECODE_TOKEN_LEAK_AUDIT=YES
REPLAY_TEST=YES
HOST_SUBSTITUTION_AUDIT=YES
CLAIM_SCOPE_REVIEW=YES
```

## Claim boundaries

```text
I3B_NATIVE_ADMISSION_V1=PASS_IN_EXACT_TESTED_SCOPE
SIGMA_NATIVE_CANONICAL_ASSESSMENT_STATE=MORE_EVIDENCE
I3C_RUNTIME_ADMISSION=NOT_RUN
POST_FOLLOWUP_OUTCOME_CONDITIONED_CONTINUATION=NOT_PROVEN
STATIC_MORE_EVIDENCE_REPLAN_POLICY_LEARNED=NOT_PROVEN
GENERAL_RESEARCH_POLICY_LEARNED=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
CLOSED_AUTONOMOUS_NATURAL_LANGUAGE_WEB_LEARNING_LOOP=NOT_PROVEN
```
