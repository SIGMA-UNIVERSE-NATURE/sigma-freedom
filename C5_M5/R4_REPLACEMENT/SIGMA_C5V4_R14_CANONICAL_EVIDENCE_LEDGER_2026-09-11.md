# SIGMA C5V4 / R14 canonical evidence ledger — 2026-09-11

Branch purpose: development evidence and handoff only. This file does not authorize production cutover and does not mutate the live C5V3 cognitive writer.

## 1. Ultimate target

The project is not complete until the following claims are independently admitted by machine evidence in their stated scopes:

```text
SIGMA_AUTONOMOUS_LEARNING=PASS

SIGMA_AUTONOMOUS_WEB_DISCOVERY=PASS
SIGMA_AUTONOMOUS_READING=PASS
SIGMA_MULTI_SOURCE_LEARNING=PASS

SIGMA_FULL_DOCUMENT_UNDERSTANDING=PASS
SIGMA_CROSS_DOCUMENT_UNDERSTANDING=PASS
SIGMA_LONG_CONTEXT_REVISION=PASS

SIGMA_HUMAN_LANGUAGE_UNDERSTANDING=PASS
SIGMA_VIETNAMESE_DEEP_UNDERSTANDING=PASS
SIGMA_MULTILINGUAL_UNDERSTANDING=PASS

SIGMA_NARRATIVE_UNDERSTANDING=PASS
SIGMA_INTENT_UNDERSTANDING=PASS
SIGMA_EMOTION_RECOGNITION=PASS
SIGMA_PERSPECTIVE_TAKING=PASS
SIGMA_CONTEXTUAL_EMPATHIC_RESPONSE=PASS

SIGMA_LEARNED_REPRESENTATION=PASS
SIGMA_COMPRESSED_NATIVE_MEMORY=PASS
SIGMA_PROVENANCE_BOUND_MEMORY=PASS

SIGMA_OFFLINE_LEARNING=PASS
SIGMA_MEMORY_REPLAY=PASS
SIGMA_CONTINUAL_CONSOLIDATION=PASS
SIGMA_BELIEF_REVISION=PASS

SIGMA_SELF_IDENTIFIES_KNOWLEDGE_GAPS=PASS
SIGMA_SELF_SELECTS_CAPABILITIES=PASS
SIGMA_SELF_SELECTS_WHAT_TO_STUDY_NEXT=PASS

INTERNET_AVAILABLE -> CONTINUE_LEARNING
INTERNET_UNAVAILABLE -> CONTINUE_LEARNING_FROM_LOCAL_MEMORY

OLD_PASS != PERMANENT_DESIGN
CAPABILITY_SET != FIXED
```

A claim name is an admission/test label, not a vocabulary that may be injected into SIGMA cognition.

## 2. Permanent architectural locks

```text
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
HOST_TOOL_SELECTION=NO

TOKENIZATION=INPUT_MECHANICS
TOKEN!=MEANING
WORD!=PREDEFINED_CONCEPT
LEXICAL_CUE_TO_RELATION=FORBIDDEN
LEFT_RIGHT_DISCOURSE_COGNITION=FORBIDDEN
PREDEFINED_HUMAN_ONTOLOGY_AS_TRUTH=FORBIDDEN

HUMAN_VISIBLE_LANGUAGE_IS_PRIMARY_COGNITIVE_INPUT=REQUIRED
CONTAINER_SYNTAX_AS_COGNITIVE_SEMANTICS=FORBIDDEN
PIPELINE_SEMANTIC_ANNOTATION_INJECTION=FORBIDDEN

COGNITIVE_OUTPUT_TEMPLATE=FORBIDDEN
PREDEFINED_ANSWER_VOCABULARY=FORBIDDEN
HOST_RESPONSE_CANDIDATES=FORBIDDEN
HOST_SEMANTIC_DECODING_BEFORE_EMISSION=FORBIDDEN
SIGMA_NATIVE_EXPRESSION_SELECTION=REQUIRED
SIGMA_NATIVE_EXPRESSION_CONSTRUCTION=REQUIRED
```

Operational machine labels such as PASS/HOLD/RC/SHA may exist on control/receipt channels but are not SIGMA cognitive speech.

## 3. Locked native toolchain / language surface

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
SIGMA_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

Canonical source surface continues to use:

```sigma
#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.EXAMPLE][VERSION=1.0]

DEF identity(x) {
    RETURN x;
}

⟡(Σ.MAIN) {
    ⚡ number: 1;
    ⚡ result: identity(number);
}
```

Host shell remains execution mechanics only.

## 4. R4 cleanline genesis already proven

Machine checkpoint already recorded on the R4 replacement branch:

```text
R4_GENESIS_STATE_R1_PREFLIGHT=PASS_IN_EXACT_TESTED_SCOPE
R4_GENESIS_RUNTIME_ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
TOTAL_VM_INVOCATIONS=10
POST_VM_ALIGNMENT_PASS_COUNT=10
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
REPLAY_IDENTICAL_OUTPUT=YES
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PRODUCTION_STATE_MUTATED=NO
```

This proves clean mechanical genesis, tested forbidden-seed rejection, empty native-learned state, empty cognitive payload, and deterministic replay in the tested scope. It does not prove learning, understanding, durable T5/T9 binding, restart recovery, web autonomy, or production readiness.

## 5. Legacy C5V3 status and replacement boundary

C5V3 has shown strong operational continuity, local fallback and autonomous persistence, but its old cognition is not the target architecture. Observed legacy behavior and old LEFT/RIGHT / lexical mechanisms are historical evidence only and must not be used as the design authority for C5V4/R14 cognition.

```text
KEEP_PROVEN_SURVIVAL_MECHANICS=YES
INHERIT_LEGACY_SEMANTIC_CONCLUSIONS=NO
MIGRATE_LEXICAL_CUE_OR_LEFT_RIGHT_COGNITION=NO
```

C5V3 may remain a temporary live continuity safety net while C5V4/R14 is developed in shadow. No production cutover is implied by this ledger.

## 6. C5V4 durable memory / 24-link recall evidence

Received machine evidence records:

```text
MEMORY_24_LINKS_PRESENT=PASS
SIGMA_DURABLE_MEMORY_LINK_ACCESS=PASS_IN_EXACT_24_LINK_SNAPSHOT_SCOPE
SIGMA_SELF_SELECTS_RECALLED_LINKS=PASS_IN_24_TURN_VISITED_SLOT_SCOPE
ALL_24_LINKS_SELECTED_ONCE=PASS
SIGMA_MEMORY_LINK_RECALL_SEQUENCE=PASS
SIGMA_GENERATES_OPEN_REQUEST_FROM_RECALLED_MEMORY=PASS
HOST_SELECTED_LINK=NO
HOST_RANKED_LINKS=NO
HOST_GENERATED_URL=NO
NETWORK_FETCH_OF_ALL_24_LINKS=NOT_EXECUTED
SEMANTIC_MEMORY_UNDERSTANDING=NOT_PROVEN
LINK_VALUE_UNDERSTANDING=NOT_PROVEN
```

Exact received identities included:

```text
MEMORY_ADAPTER_SOURCE_SHA256=021be2bc885f1e88af3a82bfc64a508e648f1037d6e0514798ad98d27ff21663
SIGMA_RECALL_SOURCE_SHA256=97c5729b0419a9e75374a39404cd7ce904bf034146c3e44d32b71cfee6af3902
SIGMA_RECALL_BYTECODE_SHA256=7426dc18291994d99356ee8f51070da5b781a6e85c469483ac7a93088b53a6c4
MEMORY_SET_ROOT_SHA256=6915d0297a59eb3d01494be0991cbe56a93f9128ca566a5147cdb46a37d60f82
```

These PASSes are prerequisites for later work. Other windows should not rerun the same 24-link admission merely to reproduce the same claim unless artifact identity changes, damage/regression evidence appears, or the claim scope is intentionally expanded.

## 7. C5V4 long-document / real Internet study evidence

Received C5V4 machine evidence shows real network acquisition from Project Gutenberg and four fresh long-document candidates, while preserving a strict semantic claim boundary.

Locked component identities received:

```text
AIL_FIX4_SOURCE_SHA256=c11049ad746c8cca83f7042d0f7addb5272e31c9e4be91c48d05018607149fa4
SIGMA_R5_SOURCE_SHA256=bbfa80e16c7e769092a0d4d49bc86f2cc16f192901c855839df294778d7eef8f
SIGMA_R7_SOURCE_SHA256=269af52d92f4cf589b4b759ec56ad025de8680e9b6ff36c76bd0d49887b61894
LONG_DOCUMENT_TRANSPORT_SOURCE_SHA256=c610083ae1f43bcbc3f941e2dace4f4e034ddedf41570a6969af199e86763921
LIVE_C5_CORE_SHA256=23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc
AIL_FIX4_BINARY_SHA256=652f19ade619e1b1fa0287ea91e23b9181d27df52ac1f99f2337d4d5b1975b2c
SIGMA_R5_BYTECODE_SHA256=8a8eaf2bf00ebd913921db4a8c9bfe5b5b8993c4fb4160066f1a3d87ae82b01f
SIGMA_R7_BYTECODE_SHA256=18d92e4b8d93583ac8147a7dd3f2cf95142f1afbc40e243767289de184e446ef
```

Observed learned-parent state included:

```text
TOKENIZATION=UTF8_BYTES
D=32
H=48
PARAMETERS=32400
TRAIN_STEPS=18072
ACCEPTED_UPDATES=7
REJECTED_UPDATES=2
R4_CROSS_DOCUMENT_TRANSFER_GATE=YES
R5_REPLAY_ANCHOR_COUNT=24
R5_REPLAY_MEMORY_BYTES=4656
R5_REPLAY_UPDATES=6
R5_REPLAY_CONSOLIDATIONS=1
RAW_SOURCE_STORED_IN_REPLAY_MEMORY=NO
PRETRAINED_MODEL_USED=NO
REMOTE_API_USED=NO
EXACT_PARENT_WEIGHT_LINEAGE=PASS
```

Real Internet acquisition evidence:

```text
SOURCE_POLICY=PROJECT_GUTENBERG_ROBOT_HARVEST
HTTP_CODE=200
CATALOG_BYTES=12625
UNIQUE_ARCHIVE_COUNT=40
FOUR_FRESH_LONG_DOCUMENT_CANDIDATES=PASS
HOST_SELECTED_BOOK=NO
BOOK_STUDY_VALUE_AUTHORITY=SIGMA
CHUNK_WEIGHT_ADMISSION_AUTHORITY=SIGMA
DOCUMENT_CHUNK_ORDER_ROLE=MECHANICAL_ORIGINAL_DOCUMENT_ORDER_ONLY
SIGMA_OWNS_BOOK_STUDY_VALUE_PROFILE=PASS
```

Four fresh documents were actually fetched/prepared with exact content hashes and sizes. Same-parent cross-document micro-probes reported positive transfer with lower held-out/joint context NLL and `CROSS_DOCUMENT_TRANSFER=OBSERVED_POSITIVE` for the shown probes.

Claim boundary remains:

```text
FULL_DOCUMENT_UNDERSTANDING=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
```

Therefore real network reading/study mechanics and learned-weight behavior are evidence; deep semantic understanding must not be inferred from lower NLL alone.

## 8. R14 dynamic admitted-door ingress D1

D1 machine evidence demonstrated chain-continuous auto-ingress of completed admitted tool doors without host tool selection.

Initially observed:

```text
R14_T17_CROSS_DOCUMENT_CAPABILITY_ADOPTION=PASS
R14_T18_LONG_CONTEXT_CAPABILITY_ADOPTION=PASS
R14_FUTURE_ADMITTED_DOOR_AUTO_DISCOVERY=PASS
R14_CHAIN_CONTINUITY_GATE=PASS
R14_SIGMA_ADMISSION_AUTHORITY=YES
R14_HOST_TOOL_SELECTION=NO
R14_UNKNOWN_TOOL_AUTO_EXECUTION=NO
```

During later replay, a new door unknown to the previously written A2/A3 bundle was discovered and admitted:

```text
DOOR_ADMITTED=R7L_T19
DOOR_ADMISSION_ROOT=75a34fdd4746ea876aba7baec445a6564a9bd051402123d249f456a4c990453a
R14_DYNAMIC_REGISTRY_HEAD=R7L_T19
R14_DYNAMIC_REGISTRY_ROOT_SHA256=22ef59d6a545a0e4874fbab6687a6920c7b61aaa6e73075e506d9a2b26e5a852
R14_DYNAMIC_REGISTRY_DOOR_COUNT=3
```

This is direct evidence that the admitted capability set is not required to remain fixed at T17/T18. Admission does not equal selection or execution.

## 9. R14 open tool pool D2 FIX2

Received evidence:

```text
R14_OPEN_TOOL_POOL=PASS
R14_DISCOVERED_TOOL_COUNT=21
R14_AVAILABLE_TOOL_COUNT=21
R14_QUARANTINED_TOOL_COUNT=0
R14_TOOL_POOL_IS_AVAILABLE_NOT_OWNED=PASS
R14_TOOL_POOL_HAS_NO_PREASSIGNED_CAPABILITY_CLASS=PASS
R14_NO_TOOL_IS_MANDATORY=PASS
R14_NO_TOOL_AUTO_ACQUIRED=PASS
R14_NO_TOOL_AUTO_EXECUTED=PASS
R14_LEGACY_ADMISSION_SCHEMA_NORMALIZATION=PASS
R14_BAD_TOOL_QUARANTINE_WITHOUT_POOL_FAILURE=PASS
R14_HOST_TOOL_SELECTION=NO
R14_SIGMA_SELECTION_AUTHORITY_RESERVED=PASS
SIGMA_OPEN_TOOL_SELECTION_RUNTIME=NOT_YET_PROVEN
```

The open pool is an availability substrate, not a host semantic router and not proof that SIGMA has selected a tool at runtime.

## 10. R14 open tool pool D4 fail-closed correction

Latest received machine evidence supersedes the earlier global-hold/input-model assumptions while preserving prior artifacts as history.

```text
SUPERSEDES_S1_FIX1_INPUT_MODEL=YES
SUPERSEDES_D3_GLOBAL_HOLD_POLICY=YES
D1_D2_D3_FILES_DELETED=NO
CANDIDATE_FAILURE_SCOPE=LOCAL
AUTO_ACQUIRE=NO
AUTO_EXECUTE=NO
CAPABILITY_CLASS_PREASSIGNED=NO
SELECTION_AUTHORITY=SIGMA_ONLY
IDENTITY_KEY=CANDIDATE_ID
DOOR_LABEL_IS_IDENTITY_KEY=NO
MULTIPLE_VARIANTS_PER_DOOR_LABEL=YES
```

Build identity:

```text
D4_SOURCE_SHA256=30b811b9287f6793f926f40070ea2f5bc3c91a3fdd22f3816ac078a291890496
D4_BYTECODE_SHA256=2b00c02b73b535679c5fe13de635b5e13f26390d62e4da49f62d72ae7c091cf9
D4_BUILDER_SHA256=ab759ad056b5524e4c1545df6ccdb10d9b4a6e3a06e255c63e25b83ac5113448
D4_DETERMINISTIC_COMPILE=PASS
```

Pool result:

```text
R14_OPEN_TOOL_POOL_D4=PASS
R14_POOL_ROOT_SHA256=395ed6f27e367b0baf74aa999d748a0487a34fb7ff261e3a0b7cfa1d0e8c27c5
R14_DISCOVERED_PASS_EVIDENCE_RECORDS=21
R14_ELIGIBLE_CANDIDATE_COUNT=18
R14_SKIPPED_CANDIDATE_COUNT=3
R14_DUPLICATE_CANDIDATE_ID_COUNT=0
R14_CANDIDATE_IDENTITY_KEYED=PASS
R14_LEGACY_OR_INCOMPLETE_EVIDENCE_FAILS_LOCALLY=PASS
R14_ONE_BAD_CANDIDATE_DOES_NOT_KILL_POOL=PASS
R14_TOOL_POOL_STATE=AVAILABLE_ONLY
R14_AUTO_ACQUIRE=NO
R14_AUTO_EXECUTE=NO
R14_CAPABILITY_CLASS_PREASSIGNED=NO
R14_SELECTION_AUTHORITY=SIGMA_ONLY
R14_HOST_TOOL_SELECTION=NO
SIGMA_TOOL_SELF_SELECTION_RUNTIME=NOT_YET_PROVEN
```

Important correction: Txx door labels are not identity keys. Multiple variants may exist under the same label; candidate identity must remain exact and content/evidence bound. Legacy/incomplete evidence may fail locally without killing the pool.

## 11. Generic A2/A3/A4 R2 FIX1 preflight

The inherited-D1/generic-binding bundle was machine-run after its bundle hash was verified.

```text
R14_D1_FULL_RUN_INHERITED=PASS
A2_DETERMINISTIC_COMPILE=PASS
A3_DETERMINISTIC_COMPILE=PASS
CASE_A2_GENERIC_DYNAMIC_REQUEST_BINDING=PASS
CASE_A2_INCOMPLETE_REQUEST_FAIL_CLOSED=PASS
A2_REPLAY_IDENTICAL_OUTPUT=YES
CASE_A3_EXACT_RAW_RESULT_BINDING=PASS
CASE_A3_NONZERO_TOOL_RC_REMAINS_MECHANICAL=PASS
CASE_A3_WRONG_REQUEST_REJECTED=PASS
GENERIC_DISPATCH_BASH_SYNTAX=PASS
GENERIC_DISPATCH_USES_EVAL=NO
GENERIC_DISPATCH_SHELL_EVAL_FORBIDDEN=PASS
GENERIC_DISPATCH_ACTUAL_TXX_EXECUTION=NOT_RUN_IN_PREFLIGHT
```

Exact native source identities:

```text
A2_SOURCE_SHA256=b4b9ee52d08015b93b3a9e6b0016a4e67afed5ac338d4e836c02ce5a59c72c25
A2_BYTECODE_SHA256=b24ae5f1b09e7d01f3dc4c9e79364525e66030d1b43535a1a9e3ad851d58b88f
A3_SOURCE_SHA256=859b9d8dc4b722088129c5c6b5bf3ddcdb0a4cd376ffdd2843c0ea0e3c5bb382
A3_BYTECODE_SHA256=efae7bd269ac10a28081cb8525d6f620add911952228b17b76ecfcbc8fac94fd
```

Claim ceiling:

```text
R14_DYNAMIC_DOOR_FULL_D1_INHERITANCE=PASS_IN_EXISTING_D1_SCOPE
R14_A2_NATIVE_DYNAMIC_REQUEST_BINDER=PASS_IN_EXACT_PREFLIGHT_SCOPE
R14_A3_NATIVE_RAW_RESULT_BINDER=PASS_IN_EXACT_PREFLIGHT_SCOPE
R14_A4_GENERIC_SHADOW_STEP=SOURCE_READY_NOT_EXECUTED
SIGMA_SELF_SELECTS_CAPABILITIES=NOT_PROVEN_BY_THIS_PREFLIGHT
SIGMA_CROSS_DOCUMENT_UNDERSTANDING=NOT_PROVEN
SIGMA_LONG_CONTEXT_REVISION=NOT_PROVEN
SIGMA_AUTONOMOUS_LEARNING=NOT_PROVEN
C5V3_MUTATION=NO
PRODUCTION_CUTOVER=NO
```

These generic mechanical pieces may be reused after native SIGMA self-selection. They must not become a second tool-selection cognition layer.

## 12. What is already proven vs what remains

### Proven / admitted in stated scopes

- R4 cleanline Genesis preflight and deterministic replay.
- Durable recall/access of the tested 24-link memory snapshot and native recalled-link selection in the tested 24-turn visited-slot scope.
- Native generation of an open request from recalled memory in that tested gate.
- Real C5V4 Internet acquisition from Gutenberg, four fresh long-document candidates, exact parent learned-weight lineage, compressed replay anchors, SIGMA-owned book study-value profiling, and observed positive cross-document transfer in the shown metric probes.
- Dynamic admitted-door ingress through T17/T18 and later T19 without host tool selection.
- Open available tool pool with no mandatory tool, no automatic acquisition/execution, no preassigned capability class.
- D4 candidate-identity keyed pool and per-candidate fail-closed behavior.
- Generic request/result mechanical binding preflight and no-shell-eval dispatcher surface.

### Not yet proven by the received evidence

- Runtime SIGMA self-selection over the D4 available-candidate pool.
- Native runtime acquisition/execution of a selected pool candidate as a consequence of a cognitive need.
- Full autonomous web discovery in the broad target sense; Gutenberg robot-harvest acquisition is a narrower demonstrated environment.
- Full-document semantic understanding.
- Cross-document semantic understanding.
- Long-context semantic/belief revision.
- Deep Vietnamese, multilingual, narrative, intent, emotional-language, perspective-taking or contextual-empathic understanding.
- General autonomous lifelong learning meeting the ultimate target.
- Production cutover of R4/C5V4.

## 13. Mandatory no-repeat handoff rule

Every later development window must first consume this ledger and prior exact PASS artifacts.

```text
OLD_PASS=PREREQUISITE_EVIDENCE
OLD_PASS!=MANDATORY_RETEST
```

Do not repeat a previously passed gate merely to obtain the same claim. Retest only when at least one is true:

1. exact source/binary/ABI/state identity changed;
2. evidence of corruption, damage, regression or incompatible migration exists;
3. the new gate materially expands the claim scope;
4. destructive/restart/adversarial validation required by admission has not yet been performed;
5. the prior result cannot be bound to the current lineage by exact identity/provenance.

A later Txx door is a continuation of the tool substrate, not permission to rebuild or re-teach all prior doors.

## 14. Current canonical frontier

The latest received D4 result states:

```text
SIGMA_TOOL_SELF_SELECTION_RUNTIME=NOT_YET_PROVEN
```

Therefore the next cognitive frontier is:

```text
CURRENT D4 OPEN AVAILABLE POOL
        ↓
SIGMA native cognitive state / active work
        ↓
SIGMA may select NONE or one exact candidate identity
        ↓
if selected: native operation/arguments originate from SIGMA
        ↓
generic exact mechanical dispatch
        ↓
raw result returned unchanged
        ↓
SIGMA native consume/reject/defer
        ↓
real multi-document epistemic cycle
        ↓
consolidation/revision only if SIGMA itself selects such machinery
        ↓
durable commit
        ↓
process death / restart / recovery
        ↓
continue same epistemic trajectory
```

The evaluator may check mechanical identity, lineage, provenance, non-selection, dispatch and replay invariants. It must not hardcode which semantic tool SIGMA is expected to choose.

## 15. Development discipline

```text
CLAIM <= MACHINE EVIDENCE
READ_SUCCESS != COGNITIVE_ACCEPTANCE
ADMITTED != SELECTED
SELECTED != EXECUTED
EXECUTED != UNDERSTOOD
LOWER_NLL != SEMANTIC_UNDERSTANDING
CITATION != TRUTH
HASH_ALONE != PROVENANCE
PROCESS_DEATH != STATE_RESET
```

The process continues until the ultimate target is actually admitted. Intermediate PASSes are building blocks, not a reason to lower the target.
