# DNA-16 NATIVE ADMISSION V1 — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Canon reference

Historical static contract:
`54_CORES/SIGMA_DNA_16_EXPERIENCE_DRIVEN_LEARNING.py`

CANON_REFERENCE_BLOB_SHA1=acd712d3e57d2a850cff8c3849cdfeebbc490332

Canon purpose:
`observation + hypothesis + action + outcome + verification`; only sufficiently qualified experience may be retained.

Exact static contract requires:
- DNA-03 Unified Cognitive State;
- DNA-09 Independent Verification Wall;
- DNA-10 Memory Genome;
- DNA-15 F174 Development Dynamics state/output;
- all five experience components;
- independent verifier separation, independence basis, method, scope, evidence, candidate binding, and verifier pass;
- qualified-only retention;
- no duplicate retention for the same already-retained qualified unit;
- no mutation of earlier DNA-09 wall or DNA-10 Memory Genome;
- no Learning Runtime, persistent Memory Runtime, neural learning, knowledge promotion, model call, F174 experiment, or external action execution by DNA-16.

## Dependency state

DNA-01 through DNA-15 are admitted in exact tested scopes.

DNA-15 exact admitted dependency:
SOURCE_SHA256=e0ac36559b85a189152709238e176a99e48f325f3f1308aba8b360a768e74d8f
BYTECODE_SHA256=f81f4542d2813f69ef308bf54dff3cc0528227ea4d5100d08683d13b1b0b2028
CHECKPOINT=SIGMA_PROFESSOR/CHECKPOINTS/20260905_DNA15_NATIVE_ADMISSION_V2_FIX1_PASS.md

## Native artifact

SOURCE_PATH=DNA16_EXPERIENCE_DRIVEN_LEARNING_NATIVE_V1.sigma
SOURCE_SHA256=1a27ef2198c1b36c5d24ddd9107e45084a9efdc86312cb0c0157f12e15b76b76
RUNNER_PATH=run_DNA16_NATIVE_ADMISSION_V1.sh
RUNNER_SHA256=e58bb971f734658677282e016f9f1c0a006bfd8f5a828222d5f53d929a663a99
CANON_REFERENCE_SHA256=7b1aa07ae0c733dc610fadd3e7e9492227611a67aabe36deaf8b36c7de33c01c
README_SHA256=9286759b95442a7f2570a1aaad59d861c03d3fea5f7a9403dea25afc80f54e1d
MANIFEST_SHA256=956dbd16986f7a7cf62fe2721a83eea2c6d38a0e5683140f231c660c0a3c59de
BUNDLE_SHA256=ab2e1dffd471988bfdf33c052980cc29f9a0793ae7ca880b96a452a81f8e6299

## Native binding encoding

The native V1 does not claim canonical JSON SHA-256 generation.

Verification is bound inside SIGMA by exact equality of dynamic opaque copies of the four candidate components:
`observation / hypothesis / action / outcome`.

```text
VERIFICATION_BINDING_ENCODING=EXACT_OPAQUE_COMPONENT_TUPLE
CANDIDATE_SHA256_DERIVATION=NOT_PROVEN
UNIT_SHA256_DERIVATION=NOT_PROVEN
```

The `candidate_sha256` field remains required/preserved as an audit field, but its cryptographic derivation is not claimed.

## Admission design

Compile/freeze before dynamic input creation.

Expected full suite:
- 16 directed cases;
- 32 randomized stress cases;
- 2 byte-identical replay cases;
- TOTAL_VM_INVOCATIONS=50 if the runner reaches completion.

Directed coverage includes:
- qualified new retention;
- same qualified unit already retained -> no duplicate;
- qualified new unit with a different existing qualified unit -> bounded retention count 2;
- missing observation;
- missing verification component;
- learner == verifier;
- independent verifier false;
- missing independence basis;
- wrong candidate component binding;
- missing verification method/scope/evidence;
- verifier failed;
- bad DNA-09 verification-wall schema;
- bad DNA-10 Memory-Genome schema;
- missing DNA-15 output.

Post-VM oracle validates SIGMA output only after each VM invocation and is never injected back into SIGMA.

## Static audit

```text
MIDFILE_HASH_COMMENT_COUNT=0
SLASH_COMMENT_COUNT=0
TOP_LEVEL_COMMAND_COUNT=1
BARE_TOP_LEVEL_BLOCK_COUNT=0
SOURCE_PYTHON_TOKEN_COUNT=0
RUNNER_PYTHON_COMMAND_COUNT=0
GLOBAL_FOR_S_COUNT=0
DUPLICATE_DEF_NAMES=0
MULTI_PRINT_SAME_LINE_COUNT=0
READ_TEXT_CALL_COUNT=1
MAP_NEW_CALL_COUNT=5
LIST_NEW_CALL_COUNT=4
BASH_SYNTAX=PASS
MANIFEST=PASS
ZIP_INTEGRITY=PASS
```

## Claim boundaries before runtime

```text
DNA16_SOURCE=SOURCE_ONLY
DNA16_COMPILE=NOT_RUN
DNA16_VM=NOT_RUN
DNA16_ADMISSION=NOT_RUN
DYNAMIC_INPUT=NOT_RUN
PERSISTENT_STATE=NA
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PYTHON_USED_BY_DEVICE_RUNNER=NO
CANDIDATE_SHA256_DERIVATION=NOT_PROVEN
UNIT_SHA256_DERIVATION=NOT_PROVEN
PERSISTENT_MEMORY_RUNTIME=NOT_EXECUTED
LEARNING_RUNTIME=NOT_EXECUTED
NEURAL_LEARNING=NOT_EXECUTED
KNOWLEDGE_PROMOTION=NOT_EXECUTED
F174_EXPERIMENT=NOT_EXECUTED
MODEL_CALL_RUNTIME=NOT_EXECUTED
EXTERNAL_ACTION_RUNTIME=NOT_EXECUTED
SEMANTIC_UNDERSTANDING=NOT_PROVEN
```

Static source readiness is not runtime capability evidence.
