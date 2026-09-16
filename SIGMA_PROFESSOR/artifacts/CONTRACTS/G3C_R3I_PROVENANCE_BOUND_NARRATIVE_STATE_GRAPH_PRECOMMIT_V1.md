# G3C R3I — Provenance-Bound Narrative State Graph Architecture Precommit V1

```text
DESIGN_ID=G3C_R3I_PROVENANCE_BOUND_NARRATIVE_STATE_GRAPH_PRECOMMIT_V1
DESIGN_DATE=2026-09-16
SYSTEM_IDENTITY=SIGMA.AIL
SESSION_CODE=SCC48903CAF08
SESSION_ACCESS=READ_PLUS_ARTIFACT_WRITE
CANONICAL_MUTATION=NO

CURRENT_PROGRAM_GENERATION=G2_ONE_SIGMA_AIL
TARGET_GENERATION=G3_LEARNED_NARRATIVE_BRAIN
ACTIVE_REVISION=R3
ACTIVE_BRAIN_HEAD=700d5c1b4845322d7c14800029c629b0
MODEL_GENERATION=1

PARENT_G3_CHECKPOINT=BRAIN/GENERATIONS/G3_LEARNED_NARRATIVE_BRAIN/G3C_R3H_SEED104729_GATE_PASS_20260916.md
PARENT_G3_COMMIT=dfc2bbe8cdd1e319c289aa4b752809b373b003ca
PARENT_G3_BLOB=ac5acae863f46f95bc173c4f1c167d7ff98a3105

STATUS=ARCHITECTURE_PRECOMMIT_SOURCE_DESIGN_ONLY
RUNTIME_EXECUTED=NO
NATIVE_SOURCE_COMPILED=NO
CAPABILITY_PROVEN=NO
G3_PROMOTION=NO
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_SELECTION=NO
HOST_CAUSAL_SELECTION=NO
HOST_SUMMARY_GENERATION=NO
ANTI_HARDCODE=MANDATORY
CLAIM_LE_MACHINE_EVIDENCE=YES
```

## 1. Why R3I exists

R3A through R3H demonstrate that better candidate-conditioned evidence representations can improve candidate ranking, but a ranking head is not itself a narrative model.

The target capability is not "select the correct line." The target is to construct and maintain a provenance-bound internal state sufficient to represent who/what participates in events, how events alter state, which hypotheses compete, how later evidence revises earlier hypotheses, which relations are merely ordered versus causally/dependency-linked, what remains unresolved, and which parts of the story are necessary to preserve the resulting state.

R3I therefore changes the principal learned object:

```text
OLD
raw story
-> segment representation
-> scalar evidence features
-> candidate score
-> answer

R3I TARGET
raw story
-> native structural hypotheses
-> participant/event narrative state
-> state transitions
-> evidence + counterevidence ledger
-> temporal order hypotheses
-> dependency/causal hypotheses
-> unresolved competition
-> consolidated narrative state
-> narrative spine
-> summary/query decision heads
```

Candidate ranking remains useful, but becomes an auxiliary observable of the narrative state rather than the definition of understanding.

## 2. Governance and execution boundary

This contract does not authorize canonical brain/model mutation.

All cognitive arrows must execute in native `.sigma` bytecode under the locked compiler/VM identities. Host/shell may transport exact bytes, invoke compiler/VM, isolate state, hash artifacts, preserve receipts, and run post-VM mechanical verification only.

Forbidden substitutions include:

```text
HOST_RAW_TEXT_TO_EVENT_GRAPH=FORBIDDEN
HOST_ENTITY_SELECTION=FORBIDDEN
HOST_ROLE_ASSIGNMENT=FORBIDDEN
HOST_REFERENCE_RESOLUTION=FORBIDDEN
HOST_TEMPORAL_INTERPRETATION=FORBIDDEN
HOST_CAUSAL_INTERPRETATION=FORBIDDEN
HOST_EVIDENCE_SCORING=FORBIDDEN
HOST_STATE_REVISION_DECISION=FORBIDDEN
HOST_SUMMARY_SPINE_SELECTION=FORBIDDEN
HOST_SUMMARY_GENERATION_AS_SIGMA=FORBIDDEN
EXPECTED_ANSWER_INJECTION=FORBIDDEN
STORY_SPECIFIC_RULES=FORBIDDEN
PHRASE_SPECIFIC_RULES=FORBIDDEN
```

## 3. Dependency-first integration

R3I must reuse admitted native structural capabilities instead of creating a second incompatible language stack.

Admitted structural dependency lineage available in the repository:

```text
LANG-01A = distributional event-frame hypothesis induction
LANG-01B = role-hypothesis contrast and frame revision
LANG-01C = participant identity and cross-utterance role binding
LANG-01D = cross-form mention-equivalence hypothesis
LANG-01E = discourse reference-chain hypothesis
LANG-01F = competing antecedent hypotheses and reference ambiguity
LANG-01G = reference-resolution evidence integration
```

Their existing claim boundaries remain binding. In particular:

```text
STRUCTURAL_HYPOTHESIS != SEMANTIC_UNDERSTANDING
PREFERRED_ANTECEDENT_HYPOTHESIS != RESOLVED_REFERENT
PARTICIPANT_IDENTITY_HYPOTHESIS != REAL_WORLD_ENTITY_IDENTITY
EVENT_FRAME_HYPOTHESIS != HUMAN_SEMANTIC_EVENT_UNDERSTANDING
```

`LANG-02A_NATIVE_OPERATOR_SCOPE_BINDING` is source-ready but not admitted at this parent checkpoint. R3I must not depend on it until separate locked-runtime admission exists.

```text
LANG02A_REQUIRED_FOR_R3I_A=NO
LANG02A_REQUIRED_BEFORE_OPERATOR_SCOPE_INTEGRATION=YES
NEGATION_SEMANTICS=NOT_PROVEN
PROPOSITION_TRUTH=NOT_PROVEN
SEMANTIC_SCOPE=NOT_PROVEN
```

## 4. Record discipline inherited from LANG-01G

R3I adopts the proven evidence-management style used by LANG-01G:

- every material record has a stable record identity;
- records preserve source/provenance identity;
- exact duplicate records are idempotent and must not double-count;
- reuse of one record ID with a different fingerprint is a collision and must fail closed;
- encounter order alone is not winner policy;
- competing support may remain unresolved;
- later counterevidence may remove or reverse a preference without deleting provenance.

Generic R3I record families:

```text
MENTION_HYPOTHESIS
PARTICIPANT_HYPOTHESIS
EVENT_FRAME_HYPOTHESIS
ROLE_BINDING_HYPOTHESIS
REFERENCE_HYPOTHESIS
STATE_HYPOTHESIS
STATE_TRANSITION
ORDER_EDGE
DEPENDENCY_HYPOTHESIS
EVIDENCE_SUPPORT
COUNTEREVIDENCE
REVISION_EDGE
UNRESOLVED_COMPETITION
SUMMARY_SPINE_MEMBERSHIP
```

Every persisted record must expose, directly or through its bound state header, the minimum provenance tuple needed to reconstruct its origin:

```text
RECORD_ID
RECORD_TYPE
SOURCE_ID
SOURCE_SEGMENT_ID_OR_EQUIVALENT
PARENT_STATE_ID_OR_NONE
FINGERPRINT_OR_CONTENT_ID
COMMIT=YES
```

Exact serialization is an implementation detail to be frozen with native source. No host may invent semantic fields not emitted by native SIGMA dependencies.

## 5. Structural roles remain unlabeled

R3I must not inject human semantic role labels as answers.

Use structural role slots/hypotheses such as:

```text
ROLE_SLOT_0
ROLE_SLOT_1
ROLE_SLOT_2
...
```

A role slot may become associated with learned structural behavior through evidence. Mapping that slot to a human semantic label such as AGENT, PATIENT, EXPERIENCER, CAUSE, or GOAL is a later separately tested capability.

This prevents the teacher/host from solving role semantics on SIGMA's behalf.

## 6. Narrative state transition

For an admitted event/frame hypothesis, R3I-A must learn or compute a native transition over structural state:

```text
PRE_STATE
+ EVENT_FRAME_HYPOTHESIS
+ PARTICIPANT_BINDINGS
+ EXISTING_SUPPORT
+ EXISTING_COUNTEREVIDENCE
-> POST_STATE
```

A later observation must not destructively overwrite historical evidence. Native SIGMA may instead emit bounded transition/revision states such as:

```text
SUPPORT_EXISTING
COMPETE_WITH_EXISTING
WEAKEN_EXISTING
SUPERSEDE_HYPOTHESIS
REOPEN_UNCERTAINTY
REMAIN_UNRESOLVED
```

These labels describe state-machine operations, not prewritten story answers.

Required invariant:

```text
LATEST_OBSERVATION != AUTOMATIC_TRUTH
ENCOUNTER_ORDER != AUTOMATIC_TRUTH
REVISION_MUST_PRESERVE_PROVENANCE=YES
```

## 7. Temporal order is not causality

R3I must represent textual/temporal ordering separately from causal/dependency hypotheses.

```text
ORDER_EDGE != DEPENDENCY_HYPOTHESIS
DEPENDENCY_HYPOTHESIS != PROVEN_REAL_WORLD_CAUSE
LATER_IN_TEXT != AUTOMATIC_CAUSE
```

A dependency hypothesis should require evidence beyond adjacency. One admissible training/test family is native counterfactual dependence:

```text
STATE + EVENT_X -> downstream compatibility with EVENT_Y
versus
STATE + perturbed/removed EVENT_X -> changed downstream compatibility with EVENT_Y
```

The native model, not the host, must compute the compatibility/dependency signal and emit the hypothesis/state.

## 8. Learning objective changes

R3I must not optimize only the final-answer line.

The candidate implementation should expose multiple native objective families over public TRAIN only:

```text
EVENT_NEXT_STATE_COMPATIBILITY
WITHIN_STORY_EVENT_CONTRAST
ROLE_SWAP_COUNTERFACTUAL
ENTITY_RENAME_EQUIVARIANCE
PARTICIPANT_CONTINUITY
COUNTEREVIDENCE_STATE_UPDATE
UNRESOLVED_STATE_PRESERVATION
TEMPORAL_ORDER_MODELING
DEPENDENCY_COUNTERFACTUAL
SUMMARY_STATE_RECONSTRUCTION
FINAL_ANSWER_RANKING_AUXILIARY
```

`FINAL_ANSWER_RANKING_AUXILIARY` must remain auxiliary; it may not be the only objective used to claim progress toward narrative representation.

All counterfactual generation/selection that constitutes cognition must be native SIGMA. Host may provide mechanically generated high-entropy identifiers or exact test perturbations only when those perturbations are frozen as test fixtures rather than semantic answers.

## 9. Public TRAIN meta-generalization split

Before R3I training, freeze a deterministic partition of the existing public TRAIN corpus so architecture decisions can be checked without using DEV labels.

Proposed contract:

```text
PUBLIC_TRAIN_TOTAL=160
TRAIN_LEARN=128
TRAIN_META=32
PARTITION_FUNCTION=DETERMINISTIC_HASH_OF_STORY_ID
PARTITION_SPEC_FROZEN_BEFORE_R3I_TRAINING=YES
TRAIN_META_WEIGHT_UPDATE=NO
DEV_LABEL_TRAINING=NO
BLIND_TRAINING=NO
FROZEN20_TRAINING=NO
SEALED_R4_ACCESS=NO
```

The exact partition function, IDs and manifest hash must be produced and frozen as an artifact before any R3I learning run. This document does not precompute the split.

## 10. Structural falsification suite before DEV

R3I must be able to fail before looking at DEV. High final-answer accuracy cannot rescue a broken internal representation.

Required probe families are dynamic and should include at least:

```text
ENTITY_RENAME_EQUIVARIANCE
ROLE_SWAP_COUNTERFACTUAL
DISTRACTOR_STATE_INVARIANCE
LATE_COUNTEREVIDENCE_REVISION
UNRESOLVED_STATE_PRESERVATION
CHRONOLOGY_VS_DEPENDENCY_CONTROL
BRIDGE_EVENT_REMOVAL
SUMMARY_STATE_REPLAY_EQUIVALENCE
```

Proposed precommit thresholds for an R3I-A admission candidate:

```text
ENTITY_RENAME_EQUIVARIANCE=20/20_REQUIRED
ROLE_SWAP_COUNTERFACTUAL>=18/20
DISTRACTOR_STATE_INVARIANCE>=19/20
LATE_COUNTEREVIDENCE_REVISION>=18/20
UNRESOLVED_STATE_PRESERVATION>=18/20
CHRONOLOGY_VS_DEPENDENCY_CONTROL>=18/20
SUMMARY_STATE_REPLAY_EQUIVALENCE>=19/20
MEDIAN_SUMMARY_SPINE_FRACTION<=0.35
```

Thresholds are design gates only until an exact source, fixture generator, manifest and post-VM verifier are frozen before execution.

Hard rule:

```text
HIGH_DEV_SCORE_WITH_STRUCTURAL_GATE_FAIL=HOLD
```

## 11. Narrative spine and summarization

R3I does not define summarization as selecting high-scoring sentences.

Define a native `NARRATIVE_SPINE` as a compact provenance-bound subset of events/evidence whose fresh native replay preserves the important consolidated narrative state, including relevant revisions and unresolved uncertainty.

Required proof shape:

```text
FULL_STORY -> NARRATIVE_STATE_FULL
SIGMA_NATIVE_SPINE_SELECTION -> SOURCE_SUBSET
FRESH_NATIVE_REPLAY(SOURCE_SUBSET) -> NARRATIVE_STATE_SPINE
NARRATIVE_STATE_SPINE ~= NARRATIVE_STATE_FULL
```

The equality/similarity contract must be structural and precommitted; host may compare emitted record identities mechanically after VM execution but may not decide which story facts are important.

The first admitted summary may be extractive/provenance-bound. Fluent abstractive human-language generation is a later capability and must not be produced by GPT/host and attributed to SIGMA.

## 12. R3H must close before R3I DEV

R3I does not replace or rewrite the current frozen R3H experiment.

At this parent checkpoint:

```text
R3H_SEED104729=PASS
R3H_SEED130363=NEXT
R3H_SEED155921=CONDITIONAL_AFTER_PRIOR_GATE
R3H_FINAL=NOT_YET_CLOSED
```

R3H must remain byte-identical/frozen for the remaining permitted seeds.

Known pre-R3I fixed-sum references from R3A:

```text
SEED104729_FIXED=14/40
SEED130363_FIXED=13/40
SEED155921_FIXED=11/40
AGGREGATE_FIXED=38/120
```

Under the existing strict R3H contract, final R3H success requires learned correctness strictly above fixed-sum on every permitted seed and in aggregate, plus the already-frozen no-collapse/no-canonical-mutation/no-blind/no-host-cognition gates.

R3I DEV thresholds/control identity must be instantiated only after the final R3H outcome is frozen so R3I cannot choose an easier control after observing its own results.

## 13. R3I DEV gate after structural admission

After R3H closure and after R3I source/bytecode/model/test identities are frozen:

```text
STRUCTURAL_META_GATE=PASS_REQUIRED
R3I_DEV_GT_STRONGEST_FROZEN_PRE_R3I_CONTROL_EACH_SEED=PASS_REQUIRED
R3I_DEV_AGGREGATE_GT_STRONGEST_FROZEN_PRE_R3I_CONTROL=PASS_REQUIRED
PREDICTION_CHANGES_GT_0=PASS_REQUIRED
NO_POSITIONAL_COLLAPSE=PASS_REQUIRED
BASE_CANONICAL_STATE_UNCHANGED=PASS_REQUIRED_FOR_SHADOW_CANDIDATE
HOST_COGNITION=NO_REQUIRED
```

DEV score without structural admission is not evidence of narrative understanding.

## 14. Blind and sealed evidence boundary

```text
BLIND_ACCESS=FORBIDDEN_DURING_R3I_DESIGN_AND_TRAINING
SEALED_G3B_R4_ACCESS=FORBIDDEN_UNTIL_SEPARATELY_AUTHORIZED
FROZEN20_TRAINING_USE=FORBIDDEN
EXTERNAL_R3_TRAINING_USE=FORBIDDEN
```

A future blind run must occur only after source, bytecode, model state, structural test manifest and thresholds are frozen. Blind is one-shot under the governing G3 contract; no blind tuning is permitted.

## 15. Exact next implementation sequence

```text
STEP_1=CLOSE_R3H_UNDER_EXISTING_FROZEN_PROTOCOL
STEP_2=FREEZE_EXACT_ADMITTED_LANGUAGE_DEPENDENCY_IDENTITIES
STEP_3=FREEZE_R3I_TRAIN_LEARN_TRAIN_META_PARTITION_MANIFEST
STEP_4=AUTHOR_NATIVE_R3I_A_NARRATIVE_STATE_INTEGRATOR
STEP_5=STATIC_ANTI_HARDCODE_AND_HOST_SUBSTITUTION_AUDIT
STEP_6=LOCKED_SIGMAC_COMPILE
STEP_7=FREEZE_SOURCE_AND_BYTECODE_HASHES
STEP_8=RUN_DYNAMIC_STRUCTURAL_FALSIFICATION_SUITE
STEP_9=RESTART_REPLAY_AND_PERSISTENCE_GATES
STEP_10=ONLY_IF_STRUCTURAL_GATE_PASS_RUN_DEV
STEP_11=CHECKPOINT_PASS_OR_HOLD_WITH_EXACT_SCOPE
```

Canonical learning/model mutation, BRAIN_HEAD change, MODEL_GENERATION change or production binding require separate explicit admission and are not authorized by this contract/session.

## 16. Claim boundary

This artifact is a design/precommit coordination artifact only.

```text
R3I_ARCHITECTURE_CONTRACT=FROZEN_AS_REPOSITORY_ARTIFACT
R3I_NATIVE_IMPLEMENTATION=NOT_YET_PROVEN
R3I_RUNTIME_PROOF=NOT_RUN
R3I_LEARNED_NARRATIVE_STATE=NOT_PROVEN
SEMANTIC_SELECTION_CORRECTNESS=NOT_PROVEN
WHOLE_STORY_UNDERSTANDING=NOT_PROVEN
HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN
GENERAL_COREFERENCE_RESOLUTION=NOT_PROVEN
CAUSAL_UNDERSTANDING=NOT_PROVEN
G3_PROMOTION=NO
```

The intended breakthrough is architectural: make correct answers and summaries consequences of a persistent, revisable, provenance-bound story representation rather than the sole optimization target.
