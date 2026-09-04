# SIGMA GLOBAL NATIVE TEACHING + ADMISSION STANDARD V1

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Purpose

This directive is the common rule for **every window / lane / teacher / development thread that teaches or extends SIGMA**.

It applies to:

- DNA capabilities;
- lessons;
- curriculum stages;
- learning algorithms;
- memory systems;
- concept formation;
- reasoning capabilities;
- curiosity and research behavior;
- knowledge graph capabilities;
- uncertainty / evidence / truth handling;
- self-improvement;
- revalidation;
- self-repair;
- runtime extensions;
- host tools and ABI additions;
- production integration.

This standard replaces the idea of "adding a lesson by adding a file" with a runtime admission discipline.

## Core principle

DO_NOT_LOAD_RESULTS=YES
LOAD_CAPABILITIES=YES
CAPABILITY_MUST_RUN_INSIDE_SIGMA=YES
RUNTIME_PROOF_REQUIRED=YES

A lesson is not accepted because a document exists, code compiles, a Python implementation works, a prompt describes the behavior, or an external system produces the correct answer.

A capability is accepted only when SIGMA itself performs the required behavior in the admitted runtime under dynamic test conditions.

## Global non-negotiable boundaries

HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN
HOST_CANDIDATE_GENERATION=FORBIDDEN
HOST_KNOWLEDGE_SELECTION=FORBIDDEN
HOST_CONCEPT_FORMATION=FORBIDDEN
HOST_TOPIC_CLASSIFICATION=FORBIDDEN
HOST_LESSON_SELECTION=FORBIDDEN
HOST_KNOWLEDGE_SCORING=FORBIDDEN
HOST_GAP_DETECTION=FORBIDDEN
HOST_RESEARCH_GOAL_SELECTION=FORBIDDEN
HOST_TRUTH_DECISION=FORBIDDEN
HOST_CURRICULUM_PRIORITY=FORBIDDEN

ANTI_HARDCODE=ADMISSION_CONTROL_NOT_TOOL_REMOVAL
LEARNING_CAPABILITIES_REMOVED=NO

The host may provide mechanical operations. It must not replace SIGMA's cognition.

## Active cognition language

ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
ACTIVE_PYTHON_COGNITION=FORBIDDEN

Historical Python artifacts may remain as:

- provenance;
- archived design references;
- old contracts;
- migration references.

They must not be executed as SIGMA cognition and must not be used as evidence that SIGMA possesses a capability.

No new active teaching logic should be authored in Python.

## Allowed implementation layers

### Native `.sigma`

Required for every cognitive decision, including:

- generating learning candidates;
- selecting knowledge;
- forming concepts;
- comparing evidence;
- grouping/classifying from learned evidence;
- detecting contradictions;
- estimating uncertainty;
- detecting knowledge gaps;
- forming research goals;
- choosing curriculum work;
- consolidating knowledge;
- revalidating knowledge;
- choosing self-improvement actions;
- metacognitive scheduling;
- semantic decisions of any kind.

### C / VM host ABI

Allowed only for mechanical primitives such as:

- byte and file I/O;
- exact storage operations;
- containers;
- hashing;
- time;
- deterministic ordering;
- exact protocol decode;
- network transport;
- process/runtime support;
- bounded mechanical transforms.

A C primitive must fail admission if it embeds semantic policy on SIGMA's behalf.

### Shell / runner

Allowed only for deterministic:

- build;
- install;
- identity verification;
- process supervision;
- namespace isolation;
- exact file copying;
- hashing;
- VM invocation;
- test orchestration;
- mechanical recovery.

Shell must not generate lessons, candidates, knowledge, summaries, semantic scores, topic labels, research goals, or curriculum decisions.

## Locked runtime identities

Unless explicitly superseded by a separately approved runtime migration:

SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

Runtime identity must be bound by proven binary identity and capability tests, not inferred from folder names.

## Universal teaching lifecycle

Every lesson or capability must move through this lifecycle:

TEACHING_GOAL
-> CAPABILITY_CONTRACT
-> DEPENDENCY_CHECK
-> NATIVE `.sigma` IMPLEMENTATION
-> STATIC REVIEW
-> COMPILE WITH LOCKED SIGMAC
-> LOCKED-VM RUNTIME TEST
-> DYNAMIC INPUT TEST
-> COUNTEREXAMPLE / NEGATIVE TEST
-> PERSISTENT-STATE TEST WHEN APPLICABLE
-> RESTART / REPLAY TEST WHEN APPLICABLE
-> HOST SUBSTITUTION AUDIT
-> STEP-LIMIT / BOUNDEDNESS TEST
-> FAILURE-STATE / PARTIAL-WRITE REVIEW WHEN APPLICABLE
-> CLAIM-SCOPE REVIEW
-> ADMISSION PASS OR FAIL
-> ONLY THEN PRODUCTION BINDING

No stage may be skipped merely because the capability appears obvious.

## Lesson design rule

Every teaching window must begin by specifying **what SIGMA must be able to do**, not what answer should be injected into it.

Bad lesson:

"Store that X means Y."

Preferred capability lesson:

"Given varying evidence that relates X and Y, SIGMA must derive, retain, test, revise, and cite the relation according to its native evidence rules."

Bad lesson:

"Here is the correct concept. Save it."

Preferred capability lesson:

"Given multiple qualified experiences, SIGMA must generate and test a concept candidate itself."

The aim is transferable capability, not one memorized output.

## Dynamic-input requirement

INPUT_DYNAMIC=YES is required for cognitive capability admission.

At least two materially different inputs must be used when practical.

The test must demonstrate that SIGMA's output/state changes because runtime evidence changes.

A constant output, hardcoded answer, fixed lookup, preselected candidate, or externally generated result does not prove cognition.

## Counterexample / negative testing

Every important capability should be tested not only on a positive example but also on a case where SIGMA must *not* make the same decision.

Examples:

- a relation that appears once must not be promoted when recurrence is required;
- contradictory evidence must not be silently treated as confirmation;
- an already completed curriculum item must not be reselected as unfinished unless revalidation policy explicitly reopens it;
- concept formation must not fire when qualification requirements are absent.

A capability that only passes a single happy-path example is not mature proof.

## Persistence rule

If the capability concerns learning, memory, curriculum, knowledge, identity, revalidation, or long-lived state:

PERSISTENT_STATE_TEST=REQUIRED

SIGMA must demonstrate that past runtime state materially affects a later run.

Restart must not silently erase the learned state.

For resumable workflows:

RECOVERY -> RESUME_VALID_UNFINISHED_WORK

not:

RECOVERY -> HOST_RECREATES_COGNITIVE_DECISION

## Boundedness / step-limit rule

Any capability that scans documents, memory, histories, graphs, evidence, or curriculum state must be characterized for computational growth.

Required questions:

- Is the work bounded per VM execution?
- Can the cursor/state resume later?
- Does the implementation perform nested full-history scans?
- Can real production history reproduce step-limit failure?
- Can large documents be segmented without host semantic selection?

STEP_LIMIT_SAFE may only be claimed in the tested scope.

## Provenance rule

Knowledge and derived capability state should preserve provenance whenever applicable.

A promoted item should be traceable to evidence such as:

- document identity;
- segment identity;
- experience identity;
- context identity;
- source/evidence identity;
- creation/revalidation cycle;
- supporting and competing evidence.

Host-generated semantic provenance is forbidden. Host may persist exact identifiers supplied by SIGMA or mechanically derived content identities.

## Claim discipline

Claims must never exceed runtime evidence.

Examples:

STRUCTURAL_RELATION_LEARNING=PROVEN

does not imply:

SEMANTIC_UNDERSTANDING=PROVEN

STRUCTURAL_GROUPING=PROVEN

does not imply:

HUMAN_TOPIC_UNDERSTANDING=PROVEN

NATIVE_GAP_SELECTION=PROVEN

does not imply:

SEMANTIC_CURIOSITY=PROVEN

Every admission record must include an explicit CLAIM_SCOPE.

Current global constraints remain:

SEMANTIC_UNDERSTANDING=NOT_PROVEN
SEMANTIC_CURIOSITY=NOT_PROVEN
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN

until separately admitted tests prove otherwise.

## Tool / ABI admission standard

Mechanical tools are allowed, but each new tool must be justified by a real capability need.

Before requesting a new host primitive:

1. inventory existing ABI;
2. verify exact semantics in source;
3. smoke-test the locked VM where important;
4. prove that the required behavior cannot be built safely from existing primitives;
5. request the smallest mechanical addition.

Do not add semantic convenience tools.

Forbidden examples:

- summarize
- classify_topic
- make_concept
- extract_concept
- semantic_similarity used to make SIGMA's decision for it
- choose_lesson
- score_knowledge
- detect_knowledge_gap
- choose_research_goal
- decide_truth
- select_candidate

For each admitted mechanical tool, record when applicable:

TOOL_NAME=
INPUT_DYNAMIC=YES/NO
OUTPUT_DETERMINISTIC=YES/NO/CONDITIONED
SIDE_EFFECT_SCOPE=
REPLAY_SAFE=YES/NO/CONDITIONED
HOST_SEMANTIC_POLICY=NO
FAILURE_MODE=
LOCKED_VM_RUNTIME_TEST=PASS/FAIL

## Teaching-window coordination rule

Every SIGMA teaching window / lane must do the following before substantive work:

1. Read this directive.
2. Read `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`.
3. Read any capability-specific directive/design relevant to the lane.
4. Check whether another lane already implemented or is testing the same capability.
5. Reuse admitted native capabilities instead of duplicating them.
6. Do not overwrite production state during preflight unless the test explicitly requires a controlled production migration.
7. Use isolated namespaces for experimental capability tests.
8. Record meaningful failures as evidence; do not hide or reinterpret them as PASS.
9. Update handoff/checkpoints after meaningful milestones.

## Dependency-first rule

Teaching order is not required to follow filename order, DNA number, lesson number, or historical creation order.

NUMERIC_ORDER_REQUIRED=NO
DEPENDENCY_FIRST=YES
CAPABILITY_FIRST=YES

A later-numbered lesson may be developed first when:

- its dependencies are satisfied;
- it unlocks an urgent missing capability;
- it provides infrastructure needed by several later lessons;
- it closes a known runtime or cognition gap.

Do not skip mandatory dependencies merely to reach an attractive high-level capability faster.

## Standard capability admission record

Every teaching window should report at least:

CAPABILITY_ID=
CAPABILITY_NAME=
TEACHING_GOAL=
DEPENDENCIES=
NATIVE_SOURCE_PATH=
SOURCE_SHA256=
BYTECODE_PATH=
BYTECODE_SHA256=
SIGMAC_SHA256=
VM_SHA256=
TEST_SCOPE=
INPUT_DYNAMIC=YES/NO
OUTPUT_DEPENDS_ON_INPUT=YES/NO
NEGATIVE_TEST=PASS/FAIL/NA
PERSISTENT_STATE=YES/NO/NA
PERSISTENT_STATE_TEST=PASS/FAIL/NA
RESTART_REPLAY_TEST=PASS/FAIL/NA
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
STEP_LIMIT_STATUS=PASS/BOUNDED/FAIL/NOT_PROVEN
PRODUCTION_STATE_MUTATED=YES/NO
VM_RC=
ADMISSION=PASS/FAIL
CLAIM_SCOPE=
NEXT_DEPENDENCY_OR_CAPABILITY=

If any required field is unknown, write UNKNOWN / NOT_PROVEN rather than guessing.

## Standard failure rule

A failed test is useful evidence.

When a test fails:

- preserve the failing source and bytecode identity when useful;
- preserve VM RC and exact error;
- record whether any state was mutated;
- determine whether the failure is language, ABI, runtime, boundedness, persistence, logic, or architecture;
- make the smallest justified repair;
- rerun the same admission gate;
- do not silently change the claim being tested to make the result appear successful.

COMPILE_PASS != RUNTIME_PASS
RUNTIME_PASS != DYNAMIC_CAPABILITY_PROVEN
DYNAMIC_CAPABILITY_PROVEN != SEMANTIC_UNDERSTANDING

## Production promotion rule

Experimental capability code must not be bound into the production learner merely because preflight passed once.

Production promotion should require, according to risk:

- repeatable admission pass;
- relevant restart/replay behavior;
- no host semantic substitution;
- bounded execution;
- known failure behavior;
- namespace/state migration plan;
- rollback or isolation path where appropriate;
- updated checkpoint and CURRENT_HANDOFF.

## Universal instruction to every teaching window

Before starting work, state internally:

WHAT_CAPABILITY_IS_SIGMA_BEING_TAUGHT?
WHAT_MUST_SIGMA_COMPUTE_ITSELF?
WHAT_MAY_HOST_DO_MECHANICALLY?
WHAT_RUNTIME_EVIDENCE_WILL_PROVE_THE_CAPABILITY?
WHAT_RESULT_WOULD_FALSIFY_THE_CLAIM?
WHAT_DEPENDENCY_MUST_EXIST_FIRST?

Then implement the smallest native lesson that can answer those questions through runtime evidence.

## Final directive

GLOBAL_STANDARD_APPLIES_TO_ALL_SIGMA_TEACHING_WINDOWS=YES
NATIVE_SIGMA_COGNITION_REQUIRED=YES
ACTIVE_PYTHON_COGNITION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
RUNTIME_PROOF_REQUIRED=YES
DEPENDENCY_FIRST=YES
CAPABILITY_FIRST=YES
FAILURES_ARE_EVIDENCE=YES
NO_FAKE_CAPABILITY_FROM_FILE_EXISTENCE=YES
NO_FAKE_CAPABILITY_FROM_COMPILE_PASS=YES
NO_FAKE_CAPABILITY_FROM_HOST_OUTPUT=YES
CLAIM_SCOPE_MUST_MATCH_PROOF=YES
