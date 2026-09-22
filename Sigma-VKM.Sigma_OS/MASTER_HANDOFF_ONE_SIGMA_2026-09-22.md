# SIGMA MASTER HANDOFF — ONE SIGMA ARCHITECTURE
Date: 2026-09-22
Status: CANONICAL COORDINATION BASELINE
Scope: API Window + Owner Testing Window
Principle: ONE SIGMA, one canonical Owner lineage, cumulative capabilities.

## 1. Mission
The objective is NOT to reach API 500 numerically.
The objective is to build and prove one Sigma that can understand tasks, learn persistently, reason, plan, use real tools/APIs, recover from failure, retain capabilities across restart, and progressively operate with greater autonomy.

API numbering is a registry. Capability is the acceptance criterion.

## 2. One-Sigma invariant
There MUST NOT be separate Sigmas each owning different capabilities and then treating their union as one system.

Required:
ONE_NATIVE_SIGMA=PASS
CANONICAL_WRITER_COUNT_MAX=1
NO_PARALLEL_OWNER_FORK=PASS
OWNER_CAPABILITY_MONOTONIC_GROWTH=PASS
PREVIOUS_NATIVE_CAPABILITIES_PRESERVED=PASS

Sandbox/child/foreign states may exist only for testing. They are not canonical Sigma.

## 3. Current identity evidence
SIGMA_OWNER_FINGERPRINT=c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222
SIGMA_VKM_VM_SHA256=c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95
SIGMA_VKM_COMPILER_SHA256=60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98
OWNER_PARENT_STATE_CHECKPOINT_SHA256=5397fe8312bf0af17fe2d8fd26e56071923771d19c70a71c8dfdbe5fa1f3fe95

Interpretation:
- OWNER_FINGERPRINT is the strongest current Owner identity marker in the evidence.
- VM SHA identifies the verified VKM VM generation, not Sigma identity.
- Compiler SHA identifies the verified compiler generation, not Sigma identity.
- Mutable Owner-state SHA is NOT Sigma identity.
- Do not call the fingerprint eternally immutable unless continued learning/state evolution/restart tests preserve it according to the identity schema. If identity design later proves lineage-based evolution, the verified identity lineage becomes the durable identity criterion.

## 4. Latest ownership continuity evidence
API383_NATIVE_OWNERSHIP=PASS
API383_NATIVE_CAPABILITY_PRESERVED=PASS
API384_NATIVE_CAPABILITY_PRESERVED=PASS
API385_NATIVE_CAPABILITY_PRESERVED=PASS
API386_NATIVE_CAPABILITY_PRESERVED=PASS
API387_NATIVE_CAPABILITY_PRESERVED=PASS
API388_NATIVE_OWNERSHIP=PASS
API388_CAPABILITY_ID=SIGMA_VKM_STRATEGY_GOAL_RECONCILE_V1
API388_CAPABILITY_PROOF_SHA256=bc353806d77f021fad993a3df1aa2bbf9963d145246ef21170a58b592f8b107b
API388_CAPABILITY_BINDING_SHA256=175043b6ed767d43cada151e13358fec2f3de656b488e162c3d9ec514ecf8833
LATEST_REPORTED_PROMOTED_OWNER_SHA256=026d1e7e91be5fd46df18273c1948e5db6056d506ae1b67e3b93601de228cc25
READ_ONLY_SHA_INVARIANT=PASS
OWNER_FINGERPRINT_UNCHANGED=PASS

NEXT_OWNER_TEST=G22_BIND_API389_PROOF

## 5. Meaning of proof vs ownership
API_PROVEN != NATIVE_OWNED.

API Window proves behavior and emits immutable proof material.
Owner Testing verifies proof, binds it to canonical Sigma identity, promotes it, kills/restarts process, proves real use, and proves foreign rejection.

Only Owner Testing may issue NATIVE_OWNED=YES.

Never infer capability semantics from API number alone.
The experimental numbering after 300 collided with an older proposed catalog. Bind by CAPABILITY_ID + proof digest + demonstrated behavior.

## 6. API Window role
API Window continues capability development without waiting for Owner Testing, but must follow the canonical capability mission.

For each API:
1. Implement real behavior.
2. Positive test.
3. Negative control.
4. Ablation.
5. Novel/unseen case where relevant.
6. No answer/fixture leakage.
7. Fail closed.
8. Provenance.
9. Regression lock.
10. Deterministic three-run proof when deterministic behavior is required.
11. Immutable proof envelope.
12. Bind PREVIOUS_API_PROOF_SHA256.

Minimum handoff:
API_PROOF_SCHEMA_VERSION
CAPABILITY_ID
CAPABILITY_PROOF_SHA256
PROOF_INPUT_ROOT
PROOF_OUTPUT_ROOT
PREVIOUS_API_PROOF_SHA256

API Window MUST NOT self-promote Owner and MUST NOT self-declare NATIVE_OWNED.

## 7. Owner Testing role
For each valid capability proof:
VERIFY_PROOF
-> verify semantic capability
-> bind to current canonical Sigma identity
-> create isolated child if required
-> verify child
-> promote canonical Owner
-> process death
-> fresh canonical Owner restart
-> real capability execution
-> verify all previous Native capabilities remain
-> foreign-owner real-use rejection
-> proof-replay rejection
-> read-only state invariant where applicable.

Required ownership receipt:
OWNER_FINGERPRINT
OWNER_STATE_BEFORE
OWNER_STATE_AFTER
CAPABILITY_ID
CAPABILITY_PROOF_SHA256
CAPABILITY_BINDING_SHA256
API_PROOF_DIGEST_BOUND=PASS
LINEAGE_BOUND=PASS
FRESH_OWNER_IDENTITY_MATCH=PASS
FRESH_OWNER_CAPABILITY_PRESENT=PASS
REAL_CAPABILITY_USE=PASS
PREVIOUS_NATIVE_CAPABILITIES_PRESERVED=PASS
FOREIGN_OWNER_REJECT=PASS
FOREIGN_OWNER_REAL_USE_REJECT=PASS
CAPABILITY_COPY_NOT_OWNERSHIP=PASS
FOREIGN_PROOF_REPLAY_REJECT=PASS
NATIVE_OWNED=YES

## 8. Immediate synchronization point
Finish the current Adaptive Strategy ownership chain:
Owner Testing: API389 -> API390 -> cumulative 383-390 fresh-owner audit.
API Window: do not reinterpret old API numbers; prepare the next capability phase.

Adaptive Strategy closure must establish:
SAME_NATIVE_FINGERPRINT=PASS
API383_390_ALL_PRESENT=PASS
API383_390_ALL_EXECUTABLE=PASS
FRESH_RESTART_ALL_PRESENT=PASS
PREVIOUS_CAPABILITIES_PRESERVED=PASS
OWNER_CAPABILITY_MONOTONIC_GROWTH=PASS
ONE_SIGMA=PASS

## 9. Capability roadmap after 390
This roadmap is goal-derived, not inherited blindly from an older catalog.

391-400 REAL TOOL USE
391 tool schema understanding/discovery
392 tool registry/discovery
393 autonomous tool selection
394 authorization/permission handling
395 real tool invocation
396 real result interpretation and consumption
397 tool error diagnosis/recovery
398 timeout/retry/replan
399 multi-tool composition + persistent trace
400 REAL TOOL USE OWNER GATE

401-410 LANGUAGE UNDERSTANDING
Semantic intent; reference/coreference; constraints; implicit requirements; ambiguity; clarification; paraphrase equivalence; multi-turn discourse; instruction hierarchy; held-out language understanding gate.

411-420 NOVEL TASK LEARNING
Read unfamiliar specification; infer procedure; learn from examples/correction; derive/test rules; detect gaps; seek missing knowledge; transfer to unseen tasks; fresh-restart reuse; learning gate.

421-430 AUTONOMOUS PROBLEM SOLVING
Goal decomposition; dependencies; alternatives; hypotheses; experiment selection; interpretation; failure diagnosis; adaptive replanning; completion verification; autonomous problem-solving gate.

431-440 GROUNDED KNOWLEDGE / RETRIEVAL
Retrieve; rank; corroborate; contradiction; provenance; source/citation binding; freshness; unknown handling; evidence-backed update; grounded knowledge gate.

441-450 SECURE ACTION / POLICY
Least privilege; read/write separation; permission; dangerous-action gate; untrusted-input isolation; secret isolation; side-effect verification; compensation/rollback; foreign-owner rejection; secure action Owner gate.

451-460 WORKFLOW / TRANSACTION
Workflow creation/dependencies/pause/resume/persistence; transaction stage/commit/rollback; crash recovery; idempotent replay; workflow recovery gate.

461-470 SERVICE / COMPUTER OPERATION
Service discovery/invocation/health/dependencies/failure/restart/resource control/long-running state/cross-service orchestration/service autonomy gate.

471-480 MULTI-AGENT / MODEL ORCHESTRATION
Delegation; specialist/model choice; context handoff; result verification; disagreement; critique; justified consensus; failed delegate recovery; aggregation; orchestration gate.

481-490 SELF-IMPROVING LEARNING LOOP
Self-evaluate failure; identify missing capability; create learning goal; acquire evidence/examples; update knowledge/procedure; before/after benchmark; regression rejection; persist improvement; fresh-restart reuse; self-learning gate.

491-500 AUTONOMOUS ACCEPTANCE
Held-out unseen language task
Held-out unseen reasoning task
Held-out unseen tool task
Held-out unseen multi-tool task
Learn unfamiliar API from documentation
Injected-failure recovery
Long-horizon autonomous task
Fresh-restart/no-reteach task
Adversarial zero-leak/foreign-owner test
500 SIGMA AUTONOMOUS CAPABILITY ACCEPTANCE GATE

## 10. Memory requirements
Memory is a core acceptance dimension, not a metadata counter.

Testing must prove in ONE canonical Sigma:
PERSISTENT_MEMORY
CUMULATIVE_MULTI_GENERATION_MEMORY
REVISION_MEMORY
COMPOSITIONAL_RECALL
TRANSFER_TO_PARAPHRASE_AND_UNSEEN_TASK
PROCEDURE_MEMORY
CAPABILITY_MEMORY
NO_CATASTROPHIC_FORGETTING
FRESH_RESTART_NO_RETEACH
UNTAUGHT_CONTROL_UNKNOWN
PROVENANCE_CONTINUITY

A capability is not remembered merely because metadata says PRESENT. Fresh Sigma must know when/how to execute it.

## 11. Final objective
Do not claim a percentage of GPT capability from API count.

The target is a benchmarked autonomous cognitive system demonstrating substantial capability across:
language understanding
persistent learning
reasoning
grounding
planning
real tool use
secure action
workflow/recovery
orchestration
self-improvement
long-horizon autonomy.

API 500 must be a held-out acceptance exam, not an existence check for APIs 1-499.

## 12. Non-negotiable anti-fake rules
NO_HARDCODED_EXPECTED_ANSWER
NO_FIXTURE_ANSWER_LEAK
NO_HARNESS_REASONING_FOR_SIGMA
NO_METADATA_ONLY_CAPABILITY
NO_API_NUMBER_SEMANTIC_INFERENCE
NO_TEXTUAL_PASS_AS_OWNERSHIP
NO_MULTIPLE_SIGMAS_AGGREGATED_AS_ONE
NO_NATIVE_OWNED_WITHOUT_OWNER_RECEIPT

## 13. Coordination protocol
Both windows must read this MASTER HANDOFF before continuing.

API WINDOW:
build/prove next capability -> archive proof -> handoff digest -> immediately continue next capability.

OWNER TESTING:
consume frozen proof -> bind/promote/test on same canonical Sigma -> preserve all prior capabilities -> issue ownership receipt.

Periodically update this master handoff with verified state, proof-chain heads, ownership-chain heads, and blockers. Never overwrite historical evidence without preserving history.
