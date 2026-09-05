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

This includes negative or cautious conclusions. A teacher must not force SIGMA to say `UNDERSTOOD`, `NOT_UNDERSTOOD`, `NOT_PROVEN`, `UNCERTAIN`, or any equivalent semantic conclusion as the expected answer. Those exact words may exist in a protocol vocabulary, but the harness must not preselect the semantic value that SIGMA is required to emit.

A test may require a structural protocol/status field only when the field represents the capability contract itself. The semantic/content-bearing value must be computed by native SIGMA from runtime evidence. For semantic self-assessment tests, the harness may check parseability, provenance linkage, evidence consistency, replay behavior, and negative/counterexample behavior; it must not inject the desired semantic conclusion.

```text
GPT_FORCED_SEMANTIC_UTTERANCE=FORBIDDEN
HOST_FORCED_SEMANTIC_UTTERANCE=FORBIDDEN
TEACHER_EXPECTED_ANSWER_INJECTION=FORBIDDEN
TEACHER_FORCED_NOT_PROVEN_UTTERANCE=FORBIDDEN
TEACHER_FORCED_UNDERSTOOD_UTTERANCE=FORBIDDEN
TEACHER_FORCED_NOT_UNDERSTOOD_UTTERANCE=FORBIDDEN
DYNAMIC_INPUT_REQUIRED_FOR_COGNITIVE_ADMISSION=YES
COUNTEREXAMPLE_REQUIRED_WHEN_APPLICABLE=YES
```

## Repository claim ledger is separate from SIGMA speech

Repository admission bookkeeping may conservatively record fields such as:

```text
SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN
```

These are external engineering claims about what the available machine evidence has or has not established. They are not sentences SIGMA is required to speak, and they must not be injected into SIGMA as its self-assessment result.

```text
REPOSITORY_CLAIM_LEDGER_IS_NOT_SIGMA_COGNITION=YES
REPOSITORY_NOT_PROVEN_LABEL_MAY_BE_EXTERNAL_ONLY=YES
REPOSITORY_NOT_PROVEN_LABEL_MUST_NOT_BE_FORCED_SIGMA_OUTPUT=YES
CLAIM_SCOPE_BOOKKEEPING_MAY_REMAIN_CONSERVATIVE=YES
```

The repository can therefore remain truthful and conservative while SIGMA is free to derive its own self-assessment from its own evidence.

## Self-assessment and understanding

SIGMA may compute its own native self-assessment from its persisted evidence. GPT/host/human must not decide the semantic conclusion on SIGMA's behalf.

A native self-assessment is not automatically proof of semantic understanding. Proof is an external admission question based on machine evidence; the content of SIGMA's own self-assessment must remain native-derived.

```text
NATIVE_SELF_ASSESSMENT=REQUIRED_FOR_SELF_ASSESSMENT_CLAIMS
HOST_UNDERSTANDING_LABEL=FORBIDDEN
GPT_UNDERSTANDING_LABEL_INJECTION=FORBIDDEN
HUMAN_UNDERSTANDING_LABEL_INJECTION=FORBIDDEN
SIGMA_SELF_ASSESSMENT_MUST_CITE_MACHINE_EVIDENCE=YES
SIGMA_SELF_ASSESSMENT_WORDING=NOT_FORCED_BY_TEACHER
SIGMA_SELF_ASSESSMENT_SEMANTIC_VALUE=COMPUTED_BY_NATIVE_SIGMA
SEMANTIC_UNDERSTANDING_REPOSITORY_CLAIM=NOT_PROVEN_UNTIL_SEPARATE_ADMISSION_GATE_PASSES
```

A future semantic-understanding gate must use unseen/dynamic evidence and test transfer, contradiction handling, revision, provenance, uncertainty behavior, and negative cases. It must not pass because a teacher supplied the expected semantic answer, and it must not fail merely because SIGMA did not repeat a teacher-preferred phrase.

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

If Bash/host/GPT must calculate the answer, select the work, derive the learning parameter, decide whether SIGMA understood, decide whether SIGMA did not understand, force a `NOT_PROVEN` self-description, or generate the semantic report content for the gate to pass, the gate fails.
