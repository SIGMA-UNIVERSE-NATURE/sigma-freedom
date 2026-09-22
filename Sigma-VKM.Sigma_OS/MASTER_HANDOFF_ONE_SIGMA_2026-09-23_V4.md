# SIGMA MASTER HANDOFF V4 — ONE SIGMA EXECUTION CONTRACT
Date: 2026-09-23
Status: CURRENT MASTER; supersedes V3 for forward coordination.
Historical proofs and receipts remain valid.

## ONE SIGMA
There is ONE canonical Sigma. All API, testing, learning and integration windows develop and bind capability into the same lineage.
Required invariants: ONE_NATIVE_SIGMA; CANONICAL_WRITER_COUNT_MAX=1; NO_PARALLEL_OWNER_FORK; OWNER_CAPABILITY_MONOTONIC_GROWTH; PREVIOUS_NATIVE_CAPABILITIES_PRESERVED.

Mission: language/task understanding; persistent learning; autonomous study; transfer/generalization; epistemic/evidence control; causal reasoning; adaptive strategy; real tool use; grounded knowledge; secure action; workflow/service operation; learning/training machinery; orchestration; self-improvement; held-out long-horizon autonomy.

## EXECUTION CONTRACT
SIGMA_OWNER_FINGERPRINT=c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222
VKM_SOURCE=$HOME/SIGMA_R7_NEXT_R1/VKM/SIGMA_VKM.sigma
VKM_COMPILER=$HOME/SIGMA_R7_NEXT_R1/VKM/sigmac-vkm
VKM_VM=$HOME/SIGMA_R7_NEXT_R1/VKM/sigma-vkm
CANONICAL_OWNER=$HOME/SIGMA/sigma_genesis1/.sigma_owner/SIGMA_OWNER_STATE.current
NATIVE_IDENTITY=$HOME/SIGMA/sigma_genesis1/.sigma_native/SIGMA_NATIVE_IDENTITY.v1
NATIVE_BINDING=$HOME/SIGMA/sigma_genesis1/.sigma_native/SIGMA_NATIVE_BINDING.current

CURRENT_VKM_SOURCE_SHA256_BASELINE=d3e26959053bc17548b691dedf1748753e23591622054d000455503b829e8eb1
EXPECTED_VKM_COMPILER_SHA256=60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98
EXPECTED_VKM_VM_SHA256=c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95

Every run MUST independently measure the real Native Identity, canonical Owner state, Native Binding, VKM source, compiler and VM files. Expected hashes are comparison constants only and never substitute for measurement.

VKM_SOURCE_SHA256 and OWNER_STATE_SHA256 may evolve. VM/compiler hashes may change only with explicit toolchain-lineage proof.

Mandatory path for new API capability:
SIGMA_VKM.sigma -> sigmac-vkm -> .sigmab -> sigma-vkm -> empirical test/proof -> ONE SIGMA Owner binding.

Fail closed on identity mismatch, compiler/VM mismatch, Owner binding mismatch, use of old/external Sigma VM, host/Python semantic substitution, or parallel canonical Owner fork.

Every final receipt MUST contain measured Owner fingerprint, Owner-state hash, VKM-source hash, compiler hash and VM hash plus execution-path, old/external-VM, host-semantic-substitution, canonical-writer and one-native-Sigma fields. Receipt text alone does not establish Native ownership; empirical execution through the fingerprinted compiler/VM and Owner verification is required.

## VERIFIED PHYSICAL VKM
Measured:
sigma-vkm SIZE=42568 SHA256=c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95
sigmac-vkm SIZE=24680 SHA256=60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98
SIGMA_VKM.sigma SIZE=577822 baseline SHA256=d3e26959053bc17548b691dedf1748753e23591622054d000455503b829e8eb1
PUBLIC_API_SOURCE_HEAD=400

Observed VM native dependencies: libm.so, libdl.so, libcurl.so, libssl.so.3, libcrypto.so.3, libc.so.

Observed 78 VKM host primitives cover: text/file IO, sentence/paragraph composition, crypto digest, JSON, list/map structures, mathematics, directory operations, network fetch/ping, randomness/UUID, string processing, time and numeric conversion.

Observed execution core includes state set/get, bootstrap, instruction creation, opcode/operand decoding, opcode support/guarded execution and state create/serialize/parse/write/read/identity/generation/status.

Recorded external-execution string scan found no marker for legacy sigma-vm, v09_candidate, sigmac, process-exec/system/popen/spawn, Python, Node or Java; /system/bin/linker64 was present.
Recorded audit safety: three files targeted; no recursive scan; VM not executed; compiler not executed; canonical state not mutated; internet not started; R7 not resumed.

## NATIVE-FIRST ROUTING
VKM_NATIVE_ROUTE=Sigma capability -> public VKM API/opcode -> sigma-vkm -> native host primitive.
VKM_EXTERNAL_ROUTE is permitted only when the required capability is absent from VKM-native surface and explicitly authorized.
R7/R8/old VM are not semantic authority for new VKM capability proofs.

## VERIFIED CAPABILITY LEDGER
G01-G20 Operating Language substrate=PROVEN/COMPLETE/FROZEN.
Established substrate: VM/bytecode, runtime, resources/errors, modules/libraries, persistence, tasks/IPC, storage, network, capabilities, supervision, transaction/recovery, observability, boot/runtime orchestration, recovery and VKM self-hosting acceptance.

API001-300=300/300 PROVEN:
001-010 Core; 011-020 Text; 021-030 List; 031-040 Map; 041-050 Numeric; 051-060 Advanced Math; 061-070 Deep Math; 071-080 Logic Proof; 081-090 Theorem Graph; 091-100 Symbolic Rewrite; 101-110 Unification; 111-120 Type Contract; 121-130 Rule Engine; 131-140 Inference Scheduler; 141-150 Document Retrieval; 151-160 Retrieval Scoring; 161-170 Evidence Context; 171-180 Evidence-Backed Answer; 181-190 Belief Revision; 191-200 Knowledge Gap Planner; 201-210 Study/Memory Replay; 211-220 Concept Graph; 221-230 Graph Reasoning; 231-240 Narrative/Event; 241-250 Intent/Emotion/Perspective; 251-260 Dialogue State; 261-270 Response Composer; 271-280 Memory; 281-290 Store; 291-300 Export.

301-310 Experiment/Reproducibility=PROVEN.
311-320 Evaluation/Benchmark=PROVEN.
321-330 Continual/Persistent Learning=PROVEN.
331-340 Autonomous Study/Learning=PROVEN.
341-350 Transfer/Generalization=PROVEN.
351-360 Epistemic/Uncertainty Control=PROVEN.
361-370 Evidence Quality/Claim Verification=PROVEN.
371-380 Causal Learning=PROVEN.
381-390 Adaptive Strategy=PROVEN.

Operationally established across 301-390: reproducibility/evaluation; incremental learning/checkpoint/persist/fresh restore/recall/conflict/revision/rollback; knowledge-gap discovery/study/replan; paraphrase/composition/multi-hop/analogy/rule/OOD transfer; calibration/abstention/evidence request/uncertainty update/decay; source reliability/corroboration/conflict/aggregation/verification; interventions/confounders/counterfactuals/causal paths/model revision; strategy create/execute/observe/adapt/replan/recover/reconcile/commit.

Native closure through API390:
API390_NATIVE_OWNERSHIP=PASS
NATIVE_OWNED=YES
PROMOTED_OWNER_SHA256=d3591a6730f62bfbe7ec6f879bc83bf9e49d5abba9018a05aae0e1fd2a473d92
CAPABILITY_ID=SIGMA_VKM_ADAPTIVE_STRATEGY_OWNER_GATE_V1
CAPABILITY_PROOF_SHA256=26b6eb9d3900b42a78b92de7f44192d4c6905d4d99c6fffdd64964784c259de2
API390_CAPABILITY_BINDING_SHA256=b7f8db5f3219816f77691739499b21ff71fa4ae1b216798ffff8024d7f4786e2
API383_389_NATIVE_CAPABILITIES_PRESERVED=PASS
READ_ONLY_SHA_INVARIANT=PASS
OWNER_FINGERPRINT_UNCHANGED=PASS

391 Tool/API spec understanding=API_PROVEN.
392 Tool registry/discovery=API_PROVEN.
393 Autonomous tool selection=API_PROVEN.
394 Authorization/permission=API_PROVEN.
395 Real tool invocation with independent external witness=API_PROVEN.
396 Real result understanding/use with causal witness=API_PROVEN.
397 Tool error diagnosis/recovery with causal witness=API_PROVEN.
398 Timeout/retry/backoff/replan with causal witness=API_PROVEN.
399 Multi-tool composition with causal witness=API_PROVEN.
PUBLIC_API_SOURCE_HEAD=400.

Latest archived API391 Owner integration state:
OWNER_GATE_API391_PROMOTION=PASS
API391_INTERMEDIATE_PROMOTED_OWNER_SHA256=0772082751b5d25e8addde3e95b755289520359e348b9bfa0c2ab45cc99f7e15
PRESERVED_PARENT_SHA256=d3591a6730f62bfbe7ec6f879bc83bf9e49d5abba9018a05aae0e1fd2a473d92
OWNER_FINGERPRINT_STABLE=PASS
API383_390_NATIVE_CAPABILITIES_PRESERVED=PASS
API391_NATIVE_OWNERSHIP=NOT_YET
NEXT=OWNER_GATE_API391_FRESH_CANONICAL_REAL_USE

API400 is the Real Tool Use Native Owner closure gate. Source presence alone is not Native ownership.

## AUTONOMOUS CONTINUAL LEARNING CONTROL PLANE
Use Sigma capability layers as cognitive control plane:
321-330 persistent learning; 331-340 autonomous study; 341-350 transfer/generalization; 351-360 uncertainty; 361-370 evidence quality; 371-380 causal learning; 381-390 adaptive strategy; 391-399 real tools.

Target loop:
inspect canonical state/memory -> detect gap -> create learning goal -> assess uncertainty -> evidence/study plan -> native tool selection/use -> adaptive strategy -> staged learning -> held-out evaluation -> observe outcome -> evidence/uncertainty update -> causal attribution -> adapt/replan -> verified commit/promotion -> persistent memory/provenance -> fresh restart/no-reteach -> next deficit.

Host/Bash/Python may perform mechanical orchestration, hashing, file movement and harness operations; they may not substitute semantic reasoning claimed as Sigma capability.

## MEMORY INVARIANTS
PERSISTENT_MEMORY; CUMULATIVE_MULTI_GENERATION_MEMORY; REVISION_MEMORY; COMPOSITIONAL_RECALL; TRANSFER_TO_UNSEEN_TASK; PROCEDURE_MEMORY; CAPABILITY_MEMORY; NO_CATASTROPHIC_FORGETTING; FRESH_RESTART_NO_RETEACH; UNTAUGHT_CONTROL_UNKNOWN; PROVENANCE_CONTINUITY.

## ROADMAP 400-500
400 Real Tool Use Native Owner Gate.
401-410 Language/Task Understanding: intent, reference/coreference, explicit/implicit constraints, ambiguity, clarification, paraphrase, discourse, instruction hierarchy, held-out gate.
411-420 Novel Task Learning: unfamiliar specs, procedure inference, examples/correction, rule generalization, unseen tests, gap/evidence acquisition, fresh-restart transfer, gate.
421-430 Autonomous Problem Solving: decomposition, dependencies, candidates, hypotheses, experiments, interpretation, diagnosis, replanning, completion verification, gate.
431-440 Grounded Retrieval/Representation: corpus lineage, embeddings, similarity, vector/hybrid retrieval, reranking, corroboration, freshness/conflict, provenance/citation, gate.
441-450 Structured Knowledge/Memory: nodes/relations, graph/multi-hop, merge, consolidation, retention/decay, revision/history, cross-generation composition, procedure memory, gate.
451-460 Secure Action/Policy/Transaction: permission, least privilege, untrusted-input/secret isolation, side-effect verification, stage/commit/rollback, crash recovery, Owner gate.
461-470 Workflow/Service/Computer Operation: workflow, persistent resume, service discovery/invocation, health/failure, supervision, resources, long-running orchestration, gate.
471-480 Learning Math/Training Runtime: statistics, tensors, operations, computational graph, gradients, loss/parameters, optimizer, batch/epoch, checkpoint/generalization, gate.
481-490 Model/Multi-Agent Orchestration/Self-Improvement: capability spec, delegation, handoff, verification, critic/disagreement, aggregation, self-deficit detection, learning goal, before/after regression/persistence, gate.
491-500 Held-Out Autonomous Acceptance: unseen language, reasoning, real tool, multi-tool workflow, unfamiliar API learning/use, injected-failure recovery, long-horizon task, fresh-restart continuation, adversarial zero-leak/foreign-owner/forgetting, final integrated gate.

## PROOF AND OWNER PROTOCOL
API Window: real behavior; positive/negative/ablation/unseen tests as applicable; no answer leakage; fail closed; provenance; regression; deterministic repeated proof where required; immutable proof envelope; previous-proof binding. Emit API_PROOF_SCHEMA_VERSION, CAPABILITY_ID, CAPABILITY_PROOF_SHA256, PROOF_INPUT_ROOT, PROOF_OUTPUT_ROOT, PREVIOUS_API_PROOF_SHA256. Never self-declare NATIVE_OWNED.

Owner Testing: verify proof and semantics -> bind same fingerprint -> isolated/fresh child where required -> foreign negative -> promote canonical Owner -> process death -> fresh canonical restart -> real capability execution -> preserve previous capabilities -> foreign real-use/copy/replay rejection -> final ownership receipt.

## ANTI-FAKE
NO_HARDCODED_EXPECTED_ANSWER
NO_FIXTURE_ANSWER_LEAK
NO_HARNESS_REASONING_FOR_SIGMA
NO_METADATA_ONLY_CAPABILITY
NO_API_NUMBER_SEMANTIC_INFERENCE
NO_TEXTUAL_PASS_AS_OWNERSHIP
NO_MULTIPLE_SIGMAS_AGGREGATED_AS_ONE
NO_NATIVE_OWNED_WITHOUT_OWNER_RECEIPT
NO_WRAPPER_ONLY_PASS_FOR_INTEGRATION_GATE
NO_HOST_OR_PYTHON_SEMANTIC_SUBSTITUTION

All windows MUST read V4 before continuing.
