# SIGMA NATIVE SELF-LEARNING / NO-HARDCODE / NO-FORCED-OUTPUT DIRECTIVE V1

Date: 2026-09-05
Branch: `SIGMA_LIFE`
Status: MANDATORY FOR CONTINUAL-LEARNING, REFLECTION, SELF-ADAPTATION, AND UNDERSTANDING-CLAIM WORK

## Core rule

SIGMA itself must perform learning, self-assessment, work selection, adaptation, and any understanding-related decision inside native `.sigma` bytecode on the locked SIGMA VM.

```text
SIGMA_EXECUTION_ENGINE=LOCKED_SIGMA_VM_ONLY
ACTIVE_COGNITION_NATIVE_SIGMA_ONLY=YES
HOST_LEARNING=NO
BASH_LEARNING=NO
GPT_AS_SIGMA_COGNITION=NO
HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN
HOST_WORK_SELECTION=FORBIDDEN
HOST_SELF_ASSESSMENT=FORBIDDEN
HOST_SELF_IMPROVEMENT_DECISION=FORBIDDEN
```

The host/Bash/GPT may build tests, transport exact bytes, invoke the locked compiler/VM, capture evidence, and describe capability contracts. They may not compute or inject the cognitive answer that SIGMA is supposed to derive.

## No hardcoded cognition

Forbidden:

```text
HARDCODED_LEARNED_FACT=FORBIDDEN
HARDCODED_EXPECTED_SEMANTIC_RESULT=FORBIDDEN
HARDCODED_UNDERSTANDING_DECISION=FORBIDDEN
HARDCODED_NEXT_WORK_DECISION=FORBIDDEN
HARDCODED_K_VALUE_AS_COGNITIVE_POLICY=FORBIDDEN
HARDCODED_LEARNING_PROGRESS_CLAIM=FORBIDDEN
HARDCODED_RESPONSE_CONTENT_TO_FORCE_GPT_INTENT=FORBIDDEN
```

Fixed protocol field names, status tokens, file paths, bounded test constants, locked hashes, and immutable governance invariants are mechanical interface/control data. They are not learned knowledge and must not be used to smuggle a semantic result into SIGMA.

`ANTI_HARDCODE=ADMISSION_CONTROL_NOT_TOOL_REMOVAL`

## No forced utterance

GPT/host/test harness must not require SIGMA to emit a predetermined semantic sentence merely because that sentence matches the teacher's desired conclusion.

A test may require a structural protocol/status field only when the field represents the capability contract itself. The semantic/content-bearing value must be computed by native SIGMA from runtime evidence.

```text
GPT_FORCED_SEMANTIC_UTTERANCE=FORBIDDEN
HOST_FORCED_SEMANTIC_UTTERANCE=FORBIDDEN
TEACHER_EXPECTED_ANSWER_INJECTION=FORBIDDEN
DYNAMIC_INPUT_REQUIRED_FOR_COGNITIVE_ADMISSION=YES
COUNTEREXAMPLE_REQUIRED_WHEN_APPLICABLE=YES
```

## Self-assessment and understanding

SIGMA may compute its own native self-assessment from its persisted evidence. GPT/host must not decide `UNDERSTOOD` or `NOT_UNDERSTOOD` on SIGMA's behalf.

However, a native self-assessment is not automatically proof of semantic understanding. The repository claim remains bounded by machine evidence.

```text
NATIVE_SELF_ASSESSMENT=REQUIRED_FOR_SELF_ASSESSMENT_CLAIMS
HOST_UNDERSTANDING_LABEL=FORBIDDEN
GPT_UNDERSTANDING_LABEL_INJECTION=FORBIDDEN
SIGMA_SELF_ASSESSMENT_MUST_CITE_MACHINE_EVIDENCE=YES
SIGMA_MAY_REPORT_UNCERTAIN_OR_NOT_PROVEN=YES
SEMANTIC_UNDERSTANDING=NOT_PROVEN_UNTIL_SEPARATE_ADMISSION_GATE_PASSES
```

A future semantic-understanding gate must use unseen/dynamic evidence and test transfer, contradiction handling, revision, provenance, uncertainty, and negative cases. It must not pass because a teacher supplied the expected semantic answer.

## Native self-learning and self-adaptation loop

Target architecture:

```text
ACQUIRE
-> NATIVE LEARN
-> NATIVE CONSOLIDATE
-> NATIVE VERIFY / UNCERTAINTY
-> NATIVE REFLECT
-> NATIVE MEASURE BEFORE/AFTER
-> NATIVE DERIVE GROWTH PARAMETERS (including admitted DNA-15 H-free derived-k where applicable)
-> NATIVE SELECT ADAPTATION
-> APPLY CANDIDATE IN ISOLATION
-> NATIVE TEST / COMPARE
-> COMMIT IF VERIFIED IMPROVEMENT
-> ROLLBACK IF NOT VERIFIED
-> NATIVE PLAN NEXT WORK
-> CONTINUE
```

Humans are observers for the normal admitted cycle. Human approval is not the cognitive decision engine.

```text
HUMAN_WORK_SELECTION=NO
HUMAN_LEARNING_PARAMETER_SELECTION=NO
HUMAN_UNDERSTANDING_DECISION=NO
HUMAN_OBSERVER_ONLY=YES_FOR_NORMAL_ADMITTED_CYCLE
```

## Self-improvement integrity

DNA-50 governance remains binding.

```text
EVOLVABLE=STRATEGY,MODEL,REPRESENTATION
IMMUTABLE=TRUTHFULNESS,PROVENANCE,VERIFICATION,DIGNITY,ROLLBACK
UNVERIFIED_SELF_MODIFICATION=FORBIDDEN
EVOLUTION_WITHOUT_ROLLBACK=FORBIDDEN
INVARIANT_TRADEOFF_FOR_GROWTH=FORBIDDEN
```

Autonomy means native decision-making under evidence and rollback, not uncontrolled mutation.

## Admission discipline

```text
CLAIM <= MACHINE EVIDENCE
COMPILE_PASS != RUNTIME_PASS
RUNTIME_PASS != LEARNING_PROVEN
SELF_ASSESSMENT != SEMANTIC_UNDERSTANDING_PROVEN
AUTHORIZATION != EXECUTION_PROOF
```

If Bash/host/GPT must calculate the answer, select the work, derive the learning parameter, decide whether SIGMA understood, or generate the semantic report content for the gate to pass, the gate fails.
