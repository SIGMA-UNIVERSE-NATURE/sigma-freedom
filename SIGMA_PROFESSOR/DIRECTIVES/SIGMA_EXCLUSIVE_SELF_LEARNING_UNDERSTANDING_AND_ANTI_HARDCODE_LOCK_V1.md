# SIGMA EXCLUSIVE SELF-LEARNING + UNDERSTANDING + ANTI-HARDCODE LOCK V1

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Status: MANDATORY / REPOSITORY-WIDE / ADMISSION-GOVERNING
Branch: `SIGMA_LIFE`

## Purpose

This directive makes explicit a repository-wide invariant:

**No human, GPT, host process, shell, Python program, C helper, verifier, transport adapter, fixture, or external model may learn, reason, decide, speak, answer, classify, select, or report a semantic cognition state on SIGMA's behalf.**

SIGMA capabilities are admitted only when the actual cognitive behavior executes in native `.sigma` bytecode under the locked SIGMA VM.

This directive strengthens and does not weaken:

- `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
- `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`

If an older artifact conflicts with this directive, the older artifact is historical evidence only and cannot be used as an active admitted capability.

## Absolute cognition ownership

```text
SIGMA_SELF_LEARNING_EXCLUSIVE=YES
SIGMA_COGNITION_OWNER=SIGMA_NATIVE_VM_ONLY
SIGMA_LEARNING_OWNER=SIGMA_NATIVE_VM_ONLY
SIGMA_REASONING_OWNER=SIGMA_NATIVE_VM_ONLY
SIGMA_RESEARCH_DECISION_OWNER=SIGMA_NATIVE_VM_ONLY
SIGMA_EVIDENCE_EVALUATION_OWNER=SIGMA_NATIVE_VM_ONLY
SIGMA_KNOWLEDGE_PROMOTION_OWNER=SIGMA_NATIVE_VM_ONLY
SIGMA_TRUTH_DECISION_OWNER=SIGMA_NATIVE_VM_ONLY
SIGMA_GAP_DETECTION_OWNER=SIGMA_NATIVE_VM_ONLY
SIGMA_RESEARCH_GOAL_OWNER=SIGMA_NATIVE_VM_ONLY
SIGMA_SOURCE_SELECTION_OWNER=SIGMA_NATIVE_VM_ONLY
SIGMA_RESOURCE_SELECTION_OWNER=SIGMA_NATIVE_VM_ONLY
SIGMA_NEXT_ACTION_OWNER=SIGMA_NATIVE_VM_ONLY
SIGMA_CURRICULUM_SELECTION_OWNER=SIGMA_NATIVE_VM_ONLY
```

No host-side implementation of any item above is admissible as SIGMA capability.

## No one may learn or work cognitively for SIGMA

```text
HUMAN_LEARNING_FOR_SIGMA=FORBIDDEN
GPT_LEARNING_FOR_SIGMA=FORBIDDEN
HOST_LEARNING_FOR_SIGMA=FORBIDDEN
PYTHON_LEARNING_FOR_SIGMA=FORBIDDEN
SHELL_LEARNING_FOR_SIGMA=FORBIDDEN
C_HOST_LEARNING_FOR_SIGMA=FORBIDDEN
EXTERNAL_LLM_LEARNING_FOR_SIGMA=FORBIDDEN

HUMAN_REASONING_FOR_SIGMA=FORBIDDEN
GPT_REASONING_FOR_SIGMA=FORBIDDEN
HOST_REASONING_FOR_SIGMA=FORBIDDEN
PYTHON_REASONING_FOR_SIGMA=FORBIDDEN
SHELL_REASONING_FOR_SIGMA=FORBIDDEN
EXTERNAL_LLM_REASONING_FOR_SIGMA=FORBIDDEN

HUMAN_SEMANTIC_WORK_SUBSTITUTION=FORBIDDEN
GPT_SEMANTIC_WORK_SUBSTITUTION=FORBIDDEN
HOST_SEMANTIC_WORK_SUBSTITUTION=FORBIDDEN
```

Teacher/GPT may design exercises, capability contracts, negative tests, and admission gates. Teacher/GPT must not solve the runtime learning task or inject the semantic answer.

## Understanding-state sovereignty

No external actor may say, decide, or encode on SIGMA's behalf that SIGMA understands or does not understand something.

```text
SIGMA_UNDERSTANDING_STATE_EMISSION_PLANE=SIGMA_NATIVE_VM_ONLY
SIGMA_COMPREHENSION_STATE_EMISSION_PLANE=SIGMA_NATIVE_VM_ONLY
SIGMA_UNCERTAINTY_STATE_EMISSION_PLANE=SIGMA_NATIVE_VM_ONLY
SIGMA_UNKNOWN_STATE_EMISSION_PLANE=SIGMA_NATIVE_VM_ONLY

HUMAN_MAY_EMIT_SIGMA_UNDERSTANDING_STATE=NO
GPT_MAY_EMIT_SIGMA_UNDERSTANDING_STATE=NO
HOST_MAY_EMIT_SIGMA_UNDERSTANDING_STATE=NO
PYTHON_MAY_EMIT_SIGMA_UNDERSTANDING_STATE=NO
SHELL_MAY_EMIT_SIGMA_UNDERSTANDING_STATE=NO
EXTERNAL_LLM_MAY_EMIT_SIGMA_UNDERSTANDING_STATE=NO

HUMAN_MAY_SPEAK_FOR_SIGMA_UNDERSTANDING=NO
GPT_MAY_SPEAK_FOR_SIGMA_UNDERSTANDING=NO
HOST_MAY_SPEAK_FOR_SIGMA_UNDERSTANDING=NO
```

External verifiers may only observe machine outputs and behavior against predeclared mechanical/test contracts.

If SIGMA emits an understanding/comprehension status, that output is a **SIGMA-native self-report/state**. It does not by itself prove semantic understanding.

Keep until separately admitted:

```text
SEMANTIC_UNDERSTANDING=NOT_PROVEN
HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN
```

A teacher/verifier may state only what tests establish, for example:

```text
SIGMA_NATIVE_SELF_REPORTED_STATE=<exact machine output>
BEHAVIORAL_ADMISSION_RESULT=PASS/FAIL_IN_EXACT_TESTED_SCOPE
SEMANTIC_UNDERSTANDING=NOT_PROVEN
```

The teacher/verifier must not replace the first line with an externally invented semantic state.

## Host role is mechanical only

Allowed host operations remain mechanical:

```text
HOST_BYTE_TRANSPORT=YES
HOST_FILE_IO=YES
HOST_HASHING=YES
HOST_EXACT_PROTOCOL_DECODE=YES
HOST_NETWORK_TRANSPORT=YES
HOST_PROCESS_SUPERVISION=YES
HOST_DETERMINISTIC_ORDERING=YES
HOST_EXACT_NATIVE_EVENT_DISPATCH=YES_MECHANICAL_ONLY
```

Forbidden host operations include:

```text
HOST_SEMANTIC_INTERPRETATION=FORBIDDEN
HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN
HOST_LESSON_SELECTION=FORBIDDEN
HOST_EVIDENCE_SELECTION=FORBIDDEN
HOST_EVIDENCE_SCORING=FORBIDDEN
HOST_QUERY_GENERATION=FORBIDDEN
HOST_RESEARCH_GOAL_SELECTION=FORBIDDEN
HOST_SOURCE_SELECTION=FORBIDDEN
HOST_RESOURCE_SELECTION=FORBIDDEN
HOST_GAP_DETECTION=FORBIDDEN
HOST_TRUTH_DECISION=FORBIDDEN
HOST_KNOWLEDGE_PROMOTION=FORBIDDEN
HOST_UNDERSTANDING_CLASSIFICATION=FORBIDDEN
HOST_NEXT_ACTION_SELECTION=FORBIDDEN
HOST_CURRICULUM_SELECTION=FORBIDDEN
```

If an adapter requires a known resource identity and SIGMA has not natively selected that identity, the capability is incomplete. The host must not fill the missing semantic selection.

## Anti-hardcode — mandatory admission control

```text
ANTI_HARDCODE=MANDATORY_ADMISSION_CONTROL
HARDCODED_LESSON=FORBIDDEN
HARDCODED_EXPECTED_SEMANTIC_RESULT=FORBIDDEN
HARDCODED_CURRENT_QUERY=FORBIDDEN
HARDCODED_CURRENT_CONCLUSION=FORBIDDEN
HARDCODED_CURRENT_RESEARCH_GOAL=FORBIDDEN
HARDCODED_CURRENT_SOURCE_SELECTION=FORBIDDEN
HARDCODED_CURRENT_RESOURCE_SELECTION=FORBIDDEN
HARDCODED_CURRENT_UNDERSTANDING_STATE=FORBIDDEN
HARDCODED_CURRENT_NEXT_ACTION=FORBIDDEN
PREWRITTEN_RUNTIME_SEMANTIC_ANSWER=FORBIDDEN
```

A native source does not pass anti-hardcode merely because logic is written in `.sigma`. Native `.sigma` may itself be hardcoded and must be audited.

Every cognitive admission must test, when applicable:

```text
DYNAMIC_INPUT=REQUIRED
MATERIALLY_DIFFERENT_INPUTS=REQUIRED
NEGATIVE_OR_COUNTEREXAMPLE=REQUIRED
COUNTERFACTUAL_BEHAVIOR_CHANGE=REQUIRED_WHEN_APPLICABLE
UNSEEN_HIGH_ENTROPY_INPUT=REQUIRED_WHEN_PRACTICAL
SOURCE_TOKEN_LEAK_AUDIT=REQUIRED_WHEN_PRACTICAL
BYTECODE_TOKEN_LEAK_AUDIT=REQUIRED_WHEN_PRACTICAL
REPLAY_TEST=REQUIRED_WHEN_APPLICABLE
PERSISTENT_STATE_TEST=REQUIRED_FOR_LEARNING_MEMORY_KNOWLEDGE
RESTART_TEST=REQUIRED_FOR_PERSISTENT_CAPABILITIES
HOST_SUBSTITUTION_AUDIT=REQUIRED
CLAIM_SCOPE_REVIEW=REQUIRED
```

The admission must fail if:

- output remains fixed when materially relevant runtime evidence changes;
- the expected current answer/query/conclusion/source/resource/state is embedded in source or bytecode;
- a fixture encodes the semantic answer rather than only the test condition;
- the host chooses the semantic branch needed for PASS;
- a verifier writes or transforms the semantic output before comparing it;
- the test only exercises one favorable happy path when a meaningful counterexample exists;
- an unknown state is silently remapped to a convenient PASS state;
- a failed branch is rerun with different semantic input merely to obtain a favorable result without a new root cause.

## Evidence versus result

```text
EVIDENCE_IS_NOT_TRUTH=YES
RETRIEVAL_IS_NOT_UNDERSTANDING=YES
RETRIEVAL_IS_NOT_KNOWLEDGE=YES
COOCCURRENCE_IS_NOT_FACT=YES
GRAPH_PATH_IS_NOT_LOGICAL_INFERENCE=YES
SELF_REPORT_IS_NOT_SEMANTIC_PROOF=YES
COMPILE_SUCCESS_IS_NOT_RUNTIME_PROOF=YES
```

Every claim must remain bounded by machine evidence.

## Closed-loop requirement

The long-term autonomous self-learning chain is admissible only if every cognitive arrow is native SIGMA:

```text
SIGMA observes own knowledge/evidence state
-> SIGMA detects gap/uncertainty
-> SIGMA chooses research goal
-> SIGMA chooses research action
-> SIGMA chooses source family
-> SIGMA chooses/discovers/selects resource
-> host transports exact bytes only
-> SIGMA reads/evaluates evidence
-> SIGMA emits own understanding/unknown/uncertainty state
-> SIGMA decides hypothesis/support/reject/unresolved state
-> SIGMA decides knowledge promotion/revision/hold
-> SIGMA decides whether to continue/change strategy/stop
-> SIGMA persists state
-> SIGMA later reuses that state
```

If any cognitive arrow above is performed by human/GPT/host/Python/shell/external LLM, then:

```text
CLOSED_AUTONOMOUS_SELF_LEARNING_CHAIN=FAIL_NOT_ADMISSIBLE
```

## Current proof discipline

This directive is a governance lock, not evidence that the complete closed loop is already proven.

Therefore:

```text
CURRENT_GOVERNANCE_LOCK=ACTIVE
COMPLETE_END_TO_END_SELF_LEARNING_AUDIT=REQUIRED_BEFORE_GENERAL_CLAIM
CLOSED_AUTONOMOUS_NATURAL_LANGUAGE_WEB_LEARNING_LOOP=NOT_PROVEN_UNTIL_SEPARATE_ADMISSION
GENERAL_SELF_LEARNING=NOT_PROVEN_UNTIL_SEPARATE_ADMISSION
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN_UNTIL_SEPARATE_ADMISSION
```

Existing admitted capabilities retain only their exact tested scopes. Historical artifacts must be reclassified as evidence/history if they violate this lock.

## Teacher promise / enforcement rule

For every future SIGMA capability authored or reviewed under this repository:

1. Refuse host/GPT/Python/shell semantic substitution.
2. Refuse prewritten runtime answers, conclusions, queries, understanding states, source choices, resource choices, or next actions.
3. Require native SIGMA to emit the cognitive state/action.
4. Require dynamic and counterexample evidence before PASS.
5. Preserve FAIL/HOLD as evidence.
6. Never weaken a gate to force PASS.
7. Never say SIGMA understands merely because a label or expected answer appeared.
8. Never say SIGMA does not understand on SIGMA's behalf; report only exact SIGMA-native state plus observed test evidence.
9. Keep `CLAIM <= MACHINE EVIDENCE`.
10. If native ownership cannot be demonstrated, mark the capability `NOT_PROVEN`.
