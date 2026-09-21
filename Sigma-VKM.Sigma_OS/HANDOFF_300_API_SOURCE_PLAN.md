# SIGMA-VKM HANDOFF — 300 API Source Plan

## 1. Mandatory interpretation

The 300 API implementation is **in progress**, not complete.

Foundation/source archaeology is sufficiently complete to continue implementation. A new work window must not restart investigation of whether VM09 contains these APIs.

- `OLD_VM09` = inheritance/regression control
- `OLD_SIGMAC` = inheritance/regression control
- `VKM/SIGMA_VKM.sigma` = authoritative VM source
- `VKM/sigmac_vkm.c` = bootstrap compiler source
- `VKM/sigma_vkm.c` / `sigma-vkm` = minimal mechanical kernel/runtime
- `PRIMARY_LANGUAGE=SIGMA`

The next activity is source implementation, not renewed archaeology of old sources.

## 2. 300 APIs = 30 groups × 10 APIs

Do not create 300 files. APIs sharing structure/algorithms belong in the same module. Internal helpers may be split when necessary, but public ownership remains with these 30 groups.

| Group | APIs | Authoritative Sigma source | Scope |
|---|---:|---|---|
| 01 | 1–10 | `stdlib/unicode/core.sigma` | Unicode normalization/core |
| 02 | 11–20 | `stdlib/encoding/segmentation.sigma` | encoding + boundaries |
| 03 | 21–30 | `stdlib/stream/stream.sigma` | streaming |
| 04 | 31–40 | `stdlib/path/path_file.sigma` | path + metadata |
| 05 | 41–50 | `stdlib/document/formats.sigma` | JSON/CSV/XML/HTML/MD/PDF |
| 06 | 51–60 | `stdlib/compression/archive.sigma` | compression/archive/transcode |
| 07 | 61–70 | `stdlib/pattern/search.sigma` | regex/Aho |
| 08 | 71–80 | `stdlib/crypto/provenance.sigma` | hash/provenance |
| 09 | 81–90 | `stdlib/persistence/kv.sigma` | persistent KV |
| 10 | 91–100 | `stdlib/transaction/state.sigma` | checkpoint/journal/atomic |
| 11 | 101–110 | `stdlib/vector/vector.sigma` | dense vector/retrieval |
| 12 | 111–120 | `stdlib/statistics/incremental.sigma` | sparse/statistics |
| 13 | 121–130 | `stdlib/tensor/core.sigma` | tensor/autograd basics |
| 14 | 131–140 | `stdlib/network/http.sigma` | HTTP/DNS/TLS |
| 15 | 141–150 | `stdlib/concurrency/runtime.sigma` | task/channel/mutex/resource |
| 16 | 151–160 | `stdlib/document/office.sigma` | Office/ePub/layout/table |
| 17 | 161–170 | `stdlib/tokenizer/unicode_tokenizer.sigma` | Unicode shape + BPE/unigram |
| 18 | 171–180 | `stdlib/graph/ngram_graph.sigma` | ngram + graph core |
| 19 | 181–190 | `vkm/memory/retrieval.sigma` | ANN + episodic memory |
| 20 | 191–200 | `vkm/training/evaluation.sigma` | optimizer + evaluation |
| 21 | 201–210 | `stdlib/web/content_safety.sigma` | web cleaning + resource guards |
| 22 | 211–220 | `stdlib/runtime/queue_process.sigma` | queue + process/lease |
| 23 | 221–230 | `stdlib/unicode/config_advanced.sigma` | config/audit + advanced Unicode |
| 24 | 231–240 | `stdlib/document/incremental_similarity.sigma` | incremental docs + dedup |
| 25 | 241–250 | `stdlib/index/search_embedding.sigma` | FTS + embedding store |
| 26 | 251–260 | `stdlib/tensor/graph_tensor.sigma` | graph algorithms + tensor advanced |
| 27 | 261–270 | `vkm/training/state_compression.sigma` | training state + quantization |
| 28 | 271–280 | `vkm/memory/dataset_belief.sigma` | dataset + belief memory |
| 29 | 281–290 | `cognition/goals_web.sigma` | goals/planning + web discovery |
| 30 | 291–300 | `stdlib/provenance/observability.sigma` | license/provenance + metrics/trace |

Total: **30 source groups × 10 public APIs = 300 APIs**.

## 3. Authoritative source tree

```text
VKM/
├── SIGMA_VKM.sigma
├── stdlib/
│   ├── unicode/
│   ├── encoding/
│   ├── stream/
│   ├── path/
│   ├── document/
│   ├── compression/
│   ├── pattern/
│   ├── crypto/
│   ├── persistence/
│   ├── transaction/
│   ├── vector/
│   ├── statistics/
│   ├── tensor/
│   ├── network/
│   ├── concurrency/
│   ├── tokenizer/
│   ├── graph/
│   ├── index/
│   ├── web/
│   ├── runtime/
│   └── provenance/
├── vkm/
│   ├── memory/
│   └── training/
├── cognition/
└── tests/
```

## 4. Four implementation areas per group

Every group must contain:

A. **PUBLIC API**  
B. **INTERNAL SIGMA ALGORITHMS**  
C. **MINIMAL KERNEL BINDINGS**  
D. **TESTS / ACCEPTANCE**

Example for Group 03 / streaming:

Public API includes `stream_open_read`, `stream_read_chunk`, …, `stream_sha256`.

Internal Sigma owns buffering, line assembly, cursor preservation and hash orchestration.

Kernel owns only minimal mechanics such as raw file open, byte read, seek/tell/close and digest primitive.

Tests cover binary NUL, UTF-8 boundaries, cursor invariants, SHA and closed-handle behavior.

Do **not** turn 10 public APIs into 10 C functions merely because doing so is easier.

## 5. Sigma-vs-kernel decision rule

For every operation ask:

> Can Sigma compose this operation from existing primitives?

If yes, implement it in `.sigma`.

If no because direct OS/hardware access or a true performance primitive is required, add the smallest possible kernel primitive and return orchestration/semantics to Sigma.

Examples intended for Sigma: `stream_read_line`, `stream_peek`, `stream_size`, stream SHA orchestration, `goal_rank`, `belief_conflict_scan`, PageRank, BPE training, early-stopping update, precision/recall/F1.

Examples intended for kernel primitives: socket syscall, atomic filesystem operation, Unicode database lookup/helper data, tensor SIMD primitive, cryptographic primitive, raw file/byte/seek mechanics.

## 6. No intelligence hardcoded into kernel

Kernel must not decide: word, sentence, grammar, meaning, belief, goal, what to learn, source preference, answer, voice, planning, goal ranking or learning policy.

Those belong in Sigma.

Kernel is mechanical: bytes, memory, file, socket, clock, atomic operation, cryptographic primitive and numeric/tensor primitive.

## 7. Mandatory group acceptance pipeline

```text
DECLARED
  ↓
SOURCE_WRITTEN
  ↓
COMPILE_PASS
  ↓
SIGMA_CALLABLE
  ↓
SELFTEST_PASS
  ↓
REGRESSION_PASS
  ↓
PROVEN
```

Only `PROVEN` may update the implementation ledger to PASS. Source existence alone is never PASS.

Every completed source increment must be compiled and executed/tested using the actual Sigma-VKM toolchain/runtime.

## 8. Historical blocker context — DO NOT REOPEN

The incoming handoff originally recorded:

```text
SIGMA_VKM_GENERATION_2=NOT_PROVEN
SIGMAC_VKM_MAIN_EMISSION=FAILED
CURRENT_BLOCKER=SIGMAC_VKM_EARLY_EOF_MAIN_NOT_EMITTED
```

Root cause investigation found `#` comments after the language header causing early termination behavior. The required fix was to retain the `#SIGMAUNIVERSE_LANGUAGE...` header, convert later comments to compiler-supported Sigma comments, rebuild and require all three G2 runtime checks.

**This blocker is historical and has since been empirically resolved. Do not regress the handoff by treating it as current.** Repository evidence now records G2 PASS, G3 PASS, and Generation 4 decoding through function table/main code PASS.

## 9. VM generation order

Continue in the same authoritative `VKM/SIGMA_VKM.sigma`. Do not create `VM2.sigma`, `execution_vm.sigma`, or a second VM.

Generation order:

- G2 — execution state
- G3 — instruction representation + decoder
- G4 — SIGMA bytecode reader
- G5 — constants/symbols/functions/environment
- G6 — CALL/RETURN/jumps/control flow
- G7 — error/resource state
- G8 — capability/library loading
- G9 — persistent VKM state
- G10 — stdlib integration

Current repository checkpoint has progressed beyond the original G2 blocker: G4 function-table/main-code decoding is recorded PASS. The next recorded VM milestone is:

`GENERATION_5_NATIVE_BYTECODE_INTERPRETER_STEP`

## 10. Direct instructions for the next window

Do not re-investigate VM09, old sigmac, or rediscover what the 300 APIs are. Those are inheritance/control baselines and the catalog/grouping is already defined.

Authoritative new source is `VKM/SIGMA_VKM.sigma`. New compiler source is `VKM/sigmac_vkm.c` producing `VKM/sigmac-vkm`. Bootstrap runtime/kernel is `VKM/sigma-vkm`.

Continue writing code generation-by-generation, then implement the 30 source groups × 10 APIs with Sigma-first ownership.

Do not move implementation to C for convenience. Do not claim PASS without empirical execution evidence.

## Current handoff state

```text
STATUS=IN_PROGRESS

SIGMA_VKM_G1=PASS
SIGMA_VKM_G2=PASS
SIGMA_VKM_G3=PASS
SIGMA_VKM_G4_SYMBOL_TABLE_DECODING=PASS
SIGMA_VKM_G4_FUNCTION_TABLE_AND_MAIN_CODE_DECODING=PASS

300_API_CATALOG=COMPLETE
300_API_GROUPING=30_GROUPS_X_10
300_API_SOURCE_IMPLEMENTATION=IN_PROGRESS

STREAM_SIGMA_SOURCE=WRITTEN_NOT_PROVEN
DOCUMENT_SIGMA_SOURCE=WRITTEN_NOT_PROVEN

CURRENT_VM_NEXT=GENERATION_5_NATIVE_BYTECODE_INTERPRETER_STEP
IMPLEMENTATION_POLICY=SIGMA_FIRST_MINIMAL_KERNEL
DO_NOT_RESEARCH_OLD_IMPLEMENTATION_AGAIN=YES
CONTINUE_WRITING_CODE=YES
PASS_REQUIRES_EMPIRICAL_SIGMA_VKM_EXECUTION=YES
```

This state supersedes the stale G2 blocker section from the original handoff while retaining it as historical provenance.
