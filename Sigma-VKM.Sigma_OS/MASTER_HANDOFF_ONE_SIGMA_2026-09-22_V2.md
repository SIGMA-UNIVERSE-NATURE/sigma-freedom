# SIGMA MASTER HANDOFF V2 — ONE SIGMA / CAPABILITY CONVERGENCE
Date: 2026-09-22
Supersedes for forward planning: MASTER_HANDOFF_ONE_SIGMA_2026-09-22.md
Historical proofs remain valid; this file does not renumber or reinterpret them.

## 1. Objective
Build ONE cumulative Sigma, not 500 labels.

Target capabilities:
- language understanding
- persistent/cumulative learning
- reasoning and causal/evidence control
- planning/adaptation
- real tool/API use
- grounded retrieval/knowledge
- secure action and workflow recovery
- representation/learning machinery
- model/orchestration capability
- self-improvement
- held-out autonomous acceptance

API count is bookkeeping only. A capability is accepted only by behavioral evidence.

## 2. One Sigma identity
SIGMA_OWNER_FINGERPRINT=c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222
SIGMA_VKM_VM_SHA256=c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95
SIGMA_VKM_COMPILER_SHA256=60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98
OWNER_PARENT_STATE_CHECKPOINT_SHA256=5397fe8312bf0af17fe2d8fd26e56071923771d19c70a71c8dfdbe5fa1f3fe95

Fingerprint is the strongest current Owner identity marker. VM/compiler hashes identify toolchain generations, not Sigma itself. Mutable Owner-state SHA is not identity.

ONE_NATIVE_SIGMA=REQUIRED
CANONICAL_WRITER_COUNT_MAX=1
NO_PARALLEL_OWNER_FORK=REQUIRED
OWNER_CAPABILITY_MONOTONIC_GROWTH=REQUIRED

## 3. Historical architecture boundaries
G01-G20 = canonical Operating Language/substrate roadmap, COMPLETE/FROZEN.
Do not extend substrate numbering merely to count generations.

Post-G20 G21/G22 artifacts are classified as extended learning/Owner-integration experiments, not canonical substrate generations.

Future Owner integration uses OWNER_BIND_APIxxx / OWNER_GATE_xxx naming rather than creating G23/G24 merely for API promotion.

## 4. Proven API history must not be rewritten
Experimental/public API numbering after 300 evolved during implementation. Older proposed catalogs collide semantically with actual execution logs.

Rule:
NEVER infer capability semantics from API number.
Bind/map by:
CAPABILITY_ID + CAPABILITY_PROOF_SHA256 + demonstrated behavior.

Known actual phases from evidence:
301-310: experiment/reproducibility family (retain actual proofs)
311-320: evaluation/benchmark family
321-330: continual/persistent learning family
331-340: autonomous study/learning family
341-350: transfer/generalization family
351-360: epistemic/uncertainty control family
361-370: evidence-quality family
371-380: causal-learning family
381-390: adaptive-strategy family

These proofs are not invalidated by older catalog collisions.

## 5. Current Owner integration
API383 native ownership has a completed receipt.
API383-387 preservation and API388 native ownership have been reported in the same Owner lineage.

Latest reported:
API388_NATIVE_OWNERSHIP=PASS
API383_NATIVE_CAPABILITY_PRESERVED=PASS
API384_NATIVE_CAPABILITY_PRESERVED=PASS
API385_NATIVE_CAPABILITY_PRESERVED=PASS
API386_NATIVE_CAPABILITY_PRESERVED=PASS
API387_NATIVE_CAPABILITY_PRESERVED=PASS
LATEST_REPORTED_PROMOTED_OWNER_SHA256=026d1e7e91be5fd46df18273c1948e5db6056d506ae1b67e3b93601de228cc25
READ_ONLY_SHA_INVARIANT=PASS
OWNER_FINGERPRINT_UNCHANGED=PASS
NEXT_OWNER_TEST=OWNER_BIND_API389

Finish API389/API390 Owner binding, then close with cumulative API383-390 fresh-owner audit.

## 6. Two parallel tracks
### API WINDOW
Build/prove missing capabilities.
Every proof requires as applicable:
positive behavior
negative control
ablation
novel/unseen case
no answer leakage
fail-closed
provenance
regression
three-run deterministic proof where deterministic behavior is required
immutable proof envelope
previous-proof binding.

Minimum handoff:
API_PROOF_SCHEMA_VERSION
CAPABILITY_ID
CAPABILITY_PROOF_SHA256
PROOF_INPUT_ROOT
PROOF_OUTPUT_ROOT
PREVIOUS_API_PROOF_SHA256

API Window never self-declares NATIVE_OWNED.

### OWNER TESTING
VERIFY proof
-> verify semantic behavior
-> bind same canonical Owner identity
-> promote
-> kill process
-> fresh restart
-> real capability use
-> verify all previous capabilities remain
-> foreign-owner/copy/replay rejection
-> ownership receipt.

Only Owner Testing may issue NATIVE_OWNED=YES.

## 7. Unified capability roadmap 391-500
This V2 deliberately merges the strongest parts of prior roadmaps. It is goal-derived, not copied wholesale from any earlier catalog.

### 391-400 — REAL TOOL / API USE
391 understand novel tool/API specification
392 discover/registry/lookup tools
393 autonomously select appropriate tool
394 authorization/permission/least-privilege decision
395 perform real invocation with constructed arguments
396 interpret and consume real returned result
397 diagnose real tool/API error and recover
398 timeout/retry/backoff/replan without fake success
399 compose multiple tools and persist execution trace
400 REAL TOOL USE NATIVE OWNER GATE

Acceptance: novel spec, real invocation, causal ablation, failure injection, no fixture result, fresh restart/no reteach, Native Owner real use.

### 401-410 — LANGUAGE & TASK UNDERSTANDING
401 semantic intent
402 entity/reference/coreference
403 explicit constraints
404 implicit requirements
405 ambiguity detection
406 clarification decision
407 paraphrase semantic equivalence
408 multi-turn discourse state
409 instruction/constraint hierarchy
410 HELD-OUT LANGUAGE UNDERSTANDING GATE

Acceptance must use held-out language tasks; parser/keyword matching alone is insufficient.

### 411-420 — NOVEL TASK LEARNING
411 read unfamiliar specification
412 infer executable procedure
413 learn from examples
414 learn from correction
415 derive/generalize rule
416 test learned rule on unseen case
417 detect knowledge/procedure gap
418 seek/acquire missing evidence
419 transfer learned procedure after fresh restart
420 NOVEL TASK LEARNING GATE

### 421-430 — AUTONOMOUS PROBLEM SOLVING
421 goal decomposition
422 subgoal/dependency model
423 candidate solution/action generation
424 hypothesis generation
425 experiment/test selection
426 outcome interpretation
427 failure diagnosis
428 adaptive replanning
429 independent completion verification
430 AUTONOMOUS PROBLEM SOLVING GATE

### 431-440 — GROUNDED RETRIEVAL & REPRESENTATION
This merges missing retrieval/representation primitives from earlier ML/knowledge roadmaps with grounding requirements.
431 corpus/dataset ingest + schema/lineage integrity
432 representation/embedding creation
433 similarity/distance semantics
434 vector index/retrieval
435 hybrid/metadata-filtered retrieval
436 relevance ranking/reranking
437 independent-source corroboration/deduplication
438 contradiction/freshness handling
439 provenance/citation/evidence binding
440 GROUNDED RETRIEVAL & REPRESENTATION GATE

### 441-450 — STRUCTURED KNOWLEDGE & MEMORY CONSOLIDATION
441 knowledge/memory node
442 relation/edge semantics
443 graph/path/multi-hop retrieval
444 semantic deduplication/merge
445 episodic-to-semantic consolidation
446 importance/retention/decay policy
447 revision/supersession with history
448 compositional recall across generations
449 capability/procedure memory
450 ONE-SIGMA MEMORY & KNOWLEDGE GATE

### 451-460 — SECURE ACTION, POLICY & TRANSACTION
451 capability permission check
452 least privilege/read-write separation
453 untrusted-input isolation
454 secret/credential isolation
455 side-effect preview/verification
456 transaction stage
457 commit
458 rollback/compensation
459 crash/idempotent recovery
460 SECURE ACTION & TRANSACTION OWNER GATE

### 461-470 — WORKFLOW, SERVICE & COMPUTER OPERATION
461 workflow create/dependencies
462 workflow execute
463 pause/resume persistent workflow
464 service discovery/spec
465 service invocation/routing
466 health/failure observation
467 restart/recovery/supervision
468 resource/budget/quota control
469 long-running cross-service orchestration
470 SERVICE/WORKFLOW AUTONOMY GATE

### 471-480 — LEARNING MATH / TRAINING RUNTIME
Preserve important machinery from the earlier 401-490 ML roadmap rather than dropping it.
471 running statistics/probability/confidence
472 tensor creation/shape/indexing
473 tensor operations/matmul/reductions
474 computational graph
475 gradient/backward validation
476 parameter/loss representation
477 optimizer/update step
478 batch/epoch/schedule runtime
479 checkpoint/resume + validation/generalization evaluation
480 TRAINING RUNTIME GATE

Important: these APIs prove actual machinery, not that Sigma has magically become a GPT-scale pretrained model.

### 481-490 — MODEL / MULTI-AGENT ORCHESTRATION & SELF-IMPROVEMENT
481 model/service capability specification
482 choose model/specialist/delegate
483 context/task handoff
484 verify delegate/model result
485 disagreement/critic evaluation
486 aggregate results with evidence
487 identify own capability/knowledge deficit
488 construct and execute learning goal
489 benchmark before/after + reject regression + persist improvement
490 SELF-IMPROVING ORCHESTRATION GATE

### 491-500 — HELD-OUT AUTONOMOUS ACCEPTANCE
491 unseen language-understanding task
492 unseen reasoning/causal task
493 unseen real-tool task
494 unseen multi-tool workflow task
495 learn unfamiliar API from documentation and use it
496 injected failure/timeout/permission-denial recovery
497 long-horizon task requiring memory + planning + tools + grounding
498 process death -> fresh restart -> continue without reteach
499 adversarial zero-leak / foreign-owner / catastrophic-forgetting acceptance
500 SIGMA AUTONOMOUS CAPABILITY ACCEPTANCE GATE

API500 is an exam over held-out tasks, not an existence check for APIs 1-499.

## 8. What was intentionally merged
From the newer autonomy roadmap:
real tools, language understanding, novel task learning, autonomous problem solving, secure action, workflow, service operation, orchestration, self-improvement, held-out acceptance.

From the earlier ML/knowledge roadmap:
dataset/corpus integrity, representations/embeddings, vector retrieval, knowledge graph, memory consolidation, statistics, tensor/autodiff, training runtime, model evaluation/provenance.

No roadmap is accepted merely because an earlier assistant proposed it. A component is retained only when it materially supports the target capabilities.

## 9. Memory acceptance
In ONE canonical Sigma prove:
PERSISTENT_MEMORY
CUMULATIVE_MULTI_GENERATION_MEMORY
REVISION_MEMORY
COMPOSITIONAL_RECALL
TRANSFER_TO_UNSEEN_TASK
PROCEDURE_MEMORY
CAPABILITY_MEMORY
NO_CATASTROPHIC_FORGETTING
FRESH_RESTART_NO_RETEACH
UNTAUGHT_CONTROL_UNKNOWN
PROVENANCE_CONTINUITY

Metadata CAPABILITY_PRESENT is insufficient; fresh Sigma must know when/how to execute the capability.

## 10. Anti-fake invariants
NO_HARDCODED_EXPECTED_ANSWER
NO_FIXTURE_ANSWER_LEAK
NO_HARNESS_REASONING_FOR_SIGMA
NO_METADATA_ONLY_CAPABILITY
NO_API_NUMBER_SEMANTIC_INFERENCE
NO_TEXTUAL_PASS_AS_OWNERSHIP
NO_MULTIPLE_SIGMAS_AGGREGATED_AS_ONE
NO_NATIVE_OWNED_WITHOUT_OWNER_RECEIPT
NO_WRAPPER_ONLY_PASS_FOR_INTEGRATION_GATE

## 11. Capability target and GPT comparison
Do not infer “70-80% of GPT” from API count.
Any comparison to modern language models requires an external held-out benchmark suite measuring language, reasoning, knowledge, tool use, learning, robustness, and long-horizon autonomy under comparable conditions.

The engineering target is substantial autonomous cognitive capability; API500 must produce benchmark evidence rather than a percentage claim.

## 12. Immediate next steps
OWNER TESTING:
finish OWNER_BIND_API389
finish OWNER_BIND_API390
run ONE-SIGMA cumulative 383-390 fresh-restart audit
then begin consuming 391+ proof handoffs.

API WINDOW:
begin API391 REAL TOOL SPEC UNDERSTAND using V2 roadmap.
Continue without waiting for Owner Testing, while preserving proof-chain order.

Both windows must read this V2 before continuing.
