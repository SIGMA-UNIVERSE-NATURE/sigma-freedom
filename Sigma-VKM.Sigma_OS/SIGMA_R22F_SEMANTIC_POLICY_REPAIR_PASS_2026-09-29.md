# SIGMA R22F — Semantic Policy Repair PASS

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Native semantic policy repair

R22F_SEMANTIC_POLICY_PATCH=PASS

R22F_COMPILE_DETERMINISTIC=PASS

R22F_BYTECODE_SHA256=
7557c588539b0ebcf302f3c586974bc43e0d50d4f3f9808d70876c1c6ce53c4f

## Native semantic-policy self-test

R22F_SEMANTIC_POLICY_SELFTEST=PASS

NO_ACTIVE_EVIDENCE_TO_ACQUIRE=PASS
SINGLE_SOURCE_TO_ACQUIRE=PASS
CROSS_DOCUMENT_GAP_TO_ACQUIRE=PASS
LEARNING_REPLAY_TO_LEARN=PASS
UNKNOWN_GAP_FAILS_CLOSED=PASS

HOST_POLICY_DECISION=NO
HOST_SCORING=NO
HOST_SEMANTIC_SELECTION=NO

## Live native policy

SCHEMA=SIGMA_R22_NATIVE_POLICY_DECISION_V1

DECISION=ACQUIRE_EVIDENCE
REASON=CROSS_DOCUMENT_GAP
KNOWLEDGE_GAP=CROSS_DOCUMENT_GAP

PENDING=NONE
ACTIVE=NONE

MODEL=
4a9f5ef84131c4162633fed959d4fb4d

G3_SEMANTIC_GENERATION=3

POLICY_SOURCE=SIGMA_NATIVE_STATE_ONLY

HOST_POLICY_DECISION=NO
HOST_SCORING=NO
HOST_OBJECTIVE_SELECTION=NO

## R22E candidate disposition

R22E_EXPERIMENTAL_MODEL=
466e9fcd423836d533d1d21c765e7e53

R22E_CANDIDATE_RETAINED=YES

R22E_CANDIDATE_SEMANTIC_ADMISSION_ELIGIBLE=NO

R22E_CANDIDATE_DISPOSITION=
RETAIN_AS_EXPERIMENTAL_LEARNING_EVIDENCE

## Semantic acquisition ABI audit

R22F_SEMANTIC_ACQUISITION_ABI_SHA256=
189bd6db8ba685c869dbd8caf81bffb84326294a46ecab679610842d7c5b713b

Observed native semantic machinery includes:
- E_event
- E_scope_valid / E_scope_make / E_scope_bind
- E_register
- E_latest
- E_counts
- E_cross_commit
- G_gap
- G_choose
- D_cross
- QUERY / REFRESH / CROSS / EPISTEMIC_STATUS / STUDY dispatch

Observed gap policy from G_gap:
- zero documents -> NO_ACTIVE_EVIDENCE
- one document -> SINGLE_SOURCE_COVERAGE
- no cross-document evidence -> CROSS_DOCUMENT_GAP
- replay available -> LEARNING_REPLAY_AVAILABLE
- otherwise -> NONE

Observed capability selection from G_choose:
- for NO_ACTIVE_EVIDENCE / SINGLE_SOURCE_COVERAGE / CROSS_DOCUMENT_GAP, online web.fetch receives higher score than replay;
- for LEARNING_REPLAY_AVAILABLE, memory.replay is favored.

Observed cross-document evidence path:
- requires both documents;
- requires both documents SEALED;
- may require refresh;
- stores CROSS_DOCUMENT hypothesis;
- registers native epistemic CROSS_DOCUMENT evidence.

## Final status

R22F_SEMANTIC_POLICY_REPAIR=PASS

LIVE_KNOWLEDGE_GAP=CROSS_DOCUMENT_GAP

LIVE_POLICY_DECISION=ACQUIRE_EVIDENCE

LIVE_POLICY_REASON=CROSS_DOCUMENT_GAP

CROSS_DOCUMENT_GAP_ACTION=ACQUIRE_EVIDENCE

LEARNING_REPLAY_AVAILABLE_ACTION=START_LEARNING

R22E_CANDIDATE_RETAINED=YES

R22E_CANDIDATE_SEMANTIC_ADMISSION_ELIGIBLE=NO

SEMANTIC_GROUNDING_CERTIFIED=NO

IR_SEMANTIC_GROUNDING=UNVERIFIED

REAL_FRESH_FINAL_CONSUMED=NO

PRODUCTION_ADMISSION_ENABLED=NO

ADMISSION=NO

NEXT=
R22G_NATIVE_SEMANTIC_ACQUISITION_AND_GROUNDING

MANUAL_REBOOT_REQUIRED=NO

## Interpretation boundary

This checkpoint repairs semantic policy, not candidate admission.

The supplied evidence establishes:
- CROSS_DOCUMENT_GAP must trigger ACQUIRE_EVIDENCE, not immediate learning;
- LEARNING_REPLAY_AVAILABLE may trigger START_LEARNING;
- unknown gap classes fail closed;
- host does not decide policy, score, or perform semantic selection;
- the R22E learned private candidate is retained as experimental evidence but is not semantically admission-eligible;
- semantic grounding remains uncertified/unverified;
- fresh-final remains unconsumed;
- production admission remains disabled.

NEXT is R22G_NATIVE_SEMANTIC_ACQUISITION_AND_GROUNDING.
