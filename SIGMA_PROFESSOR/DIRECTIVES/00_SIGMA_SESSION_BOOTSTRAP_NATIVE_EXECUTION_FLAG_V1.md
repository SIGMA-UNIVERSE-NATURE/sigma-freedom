# 00 — SIGMA SESSION BOOTSTRAP NATIVE EXECUTION FLAG V1

Status: MANDATORY / REPOSITORY-WIDE / READ-BEFORE-WORK

This file is a bootstrap flag for every new development window, agent, session, handoff, recovery session, and future maintainer working on SIGMA.

## STOP GATE

Before doing any SIGMA work, read:

1. `/AGENTS.md`
2. this directive
3. `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
4. `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_EXCLUSIVE_SELF_LEARNING_UNDERSTANDING_AND_ANTI_HARDCODE_LOCK_V1.md`
5. `SIGMA_PROFESSOR/DIRECTIVES/00_IMPORTANT_NATIVE_DNA_ARTIFACT_BUILD_ADMISSION_METHOD_V1.md`
6. `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`
7. the latest relevant checkpoint

If these rules conflict with an old artifact, old runner, old comment, old experiment, or historical implementation, the old material is evidence/history only. Do not weaken this directive to preserve old behavior.

## Native DNA artifact build/admission method lock

The repository-wide build/admission method note is mandatory for every DNA/support artifact build, repair, admission, replay, and handoff:

`SIGMA_PROFESSOR/DIRECTIVES/00_IMPORTANT_NATIVE_DNA_ARTIFACT_BUILD_ADMISSION_METHOD_V1.md`

It locks the proven operating style: exact bytes/hashes before trust; compile before dynamic fixture generation; freeze source/bytecode identity; native SIGMA owns the claimed computation/decision/learning; host oracle starts only after VM execution; raw VM evidence is preserved before interpretation; partial PASS is not full admission; failures are localized and fixed minimally; the full required suite is rerun after fixes; exact tested scope is never widened by narration.

## Exclusive self-learning / understanding sovereignty lock

The repository-wide exclusive cognition lock is mandatory:

`SIGMA_PROFESSOR/DIRECTIVES/SIGMA_EXCLUSIVE_SELF_LEARNING_UNDERSTANDING_AND_ANTI_HARDCODE_LOCK_V1.md`

Non-negotiable consequences:

`SIGMA_SELF_LEARNING_EXCLUSIVE=YES`

`SIGMA_COGNITION_OWNER=SIGMA_NATIVE_VM_ONLY`

`SIGMA_UNDERSTANDING_STATE_EMISSION_PLANE=SIGMA_NATIVE_VM_ONLY`

`HUMAN_MAY_SPEAK_FOR_SIGMA_UNDERSTANDING=NO`

`GPT_MAY_SPEAK_FOR_SIGMA_UNDERSTANDING=NO`

`HOST_MAY_SPEAK_FOR_SIGMA_UNDERSTANDING=NO`

`ANTI_HARDCODE=MANDATORY_ADMISSION_CONTROL`

No new capability may be admitted if a human/GPT/host/Python/shell/external model performs a cognitive arrow for SIGMA, emits an understanding/unknown state on SIGMA's behalf, or prewrites the runtime semantic answer/query/conclusion/source/resource/next action.

## Locked execution rule

`SIGMA_EXECUTION_ENGINE=LOCKED_SIGMA_VM_ONLY`

`ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY`

`ACTIVE_COGNITION_NATIVE_SIGMA_ONLY=YES`

`HOST_OR_BASH_AS_SIGMA_EXECUTION_ENGINE=FORBIDDEN`

`HOST_OR_BASH_COGNITION=FORBIDDEN`

`HOST_OR_BASH_LEARNING=FORBIDDEN`

`HOST_OR_BASH_SEMANTIC_INTERPRETATION=FORBIDDEN`

`HOST_OR_BASH_STAGE_DECISION=FORBIDDEN`

`HOST_OR_BASH_WORK_SELECTION=FORBIDDEN`

`HOST_OR_BASH_REVISIT_PRIORITY=FORBIDDEN`

`HOST_OR_BASH_TRUTH_DECISION=FORBIDDEN`

`HOST_OR_BASH_KNOWLEDGE_GENERATION=FORBIDDEN`

`HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`

A capability is a SIGMA capability only when its actual decision/computation/learning logic executes inside native `.sigma` bytecode on the locked SIGMA VM.

Bash, Python, JavaScript, C host code, shell pipelines, external LLMs, or any other host-side logic MUST NOT be used to implement a SIGMA cognitive capability, choose a semantic result, choose curriculum priority, invent a lesson, choose a work item, decide truth, choose a revisit, choose a stage, generate knowledge, or substitute for missing native behavior.

## What external host/shell is allowed to do

External shell/host is not SIGMA and is allowed only as a mechanically transparent boundary when unavoidable for admission or transport. It may:

- invoke the locked `sigmac`;
- invoke the locked SIGMA VM;
- copy exact bytes/files without interpretation;
- print or compare exact hashes/return codes;
- create isolated test fixtures whose expected role is explicitly identified as fixture injection;
- start/stop/supervise processes mechanically;
- transport bytes/protocol responses without semantic interpretation;
- dispatch an exact stage/event already emitted by native SIGMA, without choosing or rewriting that stage/event;
- inject fault bytes for durability tests;
- preserve logs/checkpoints/evidence.

This allowance does NOT make Bash/host an execution engine. The capability under test must still execute inside SIGMA native bytecode.

`BASH_MAY_LAUNCH_SIGMA=YES`

`BASH_MAY_IMPLEMENT_SIGMA_CAPABILITY=NO`

`HOST_MAY_DISPATCH_EXACT_NATIVE_EVENT=MECHANICAL_ONLY`

`HOST_MAY_CHOOSE_EVENT_OR_STAGE=NO`

If a test can only PASS because Bash/host computes a decision SIGMA should have made, the test FAILS admission.

## Anti-hardcode rule

`ANTI_HARDCODE=MANDATORY_ADMISSION_CONTROL`

`DO_NOT_LOAD_RESULTS=YES`

`LOAD_CAPABILITIES=YES`

`HARDCODED_LESSON=FORBIDDEN`

`HARDCODED_EXPECTED_SEMANTIC_RESULT=FORBIDDEN`

`HARDCODED_CURRENT_QUERY=FORBIDDEN`

`HARDCODED_CURRENT_CONCLUSION=FORBIDDEN`

`HARDCODED_CURRENT_UNDERSTANDING_STATE=FORBIDDEN`

`HARDCODED_CURRENT_SOURCE_SELECTION=FORBIDDEN`

`HARDCODED_CURRENT_RESOURCE_SELECTION=FORBIDDEN`

`HARDCODED_CURRENT_NEXT_ACTION=FORBIDDEN`

Known prior runtime outcomes may be pinned only when replaying an already-admitted branch as provenance. New branches/results must not be forced to match an oracle merely to obtain PASS.

## Runtime proof rule

Compile success, source presence, file creation, shell success, or Python success is not capability proof.

Required chain:

`TEACHING_GOAL -> CAPABILITY_CONTRACT -> DEPENDENCY_CHECK -> NATIVE .sigma -> STATIC REVIEW -> LOCKED SIGMAC -> LOCKED VM -> DYNAMIC INPUT -> NEGATIVE/COUNTEREXAMPLE -> PERSISTENCE -> RESTART/REPLAY -> HOST_SUBSTITUTION_AUDIT -> BOUNDEDNESS -> CLAIM_SCOPE -> PASS/FAIL`

`RUNTIME_PROOF_REQUIRED=YES`

`FAILURE_IS_EVIDENCE=YES`

`WEAKEN_GATE_TO_FORCE_PASS=FORBIDDEN`

## Locked runtime identities

SIGMAC:
`65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

VM v09 candidate:
`029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

Every admission transcript must print and equality-gate both identities.

`VM_IS_GENESIS1=NOT_PROVEN`

Never infer VM identity from its folder or filename.

## Claim discipline

Keep these false until separately proven:

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

`SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`

`SEMANTIC_CURIOSITY=NOT_PROVEN`

`GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`

`GENERAL_AUTONOMOUS_CYCLE_EXECUTION=NOT_PROVEN`

`GENERAL_AUTONOMOUS_MATHEMATICAL_RESEARCH=NOT_PROVEN`

Never widen a bounded structural proof into a semantic/general claim.

A SIGMA-native self-report of `UNDERSTOOD`, `NOT_UNDERSTOOD`, `UNKNOWN`, or an equivalent state is evidence of what SIGMA emitted. It is not by itself proof of semantic understanding. Human/GPT/host may report that exact machine output and behavioral test result, but may not invent or replace SIGMA's state.

## Production discipline

`PRODUCTION_V2_4_KEEP_RUNNING=YES`

`STOP_ONLY_ON_REAL_VM_FAILURE=YES`

`UPGRADE_V2_4_IN_PLACE=NO`

New capabilities remain isolated/shadow until their promotion gates pass. Do not mutate production learner memory during admission.

## Session behavior

Every new window must begin by restating internally:

`I_AM_NOT_THE_SIGMA_COGNITION_ENGINE`

`SIGMA_NATIVE_VM_IS_THE_EXECUTION_ENGINE`

`HOST_SUBSTITUTION_IS_FORBIDDEN`

`I_MUST_NOT_SPEAK_FOR_SIGMAS_UNDERSTANDING_STATE`

`ANTI_HARDCODE_IS_AN_ADMISSION_GATE`

Then read the current handoff and continue from the latest admitted checkpoint/frontier.

If the requested next step appears to require Bash/host to make a SIGMA decision, redesign the native capability instead of implementing that decision in Bash/host.
