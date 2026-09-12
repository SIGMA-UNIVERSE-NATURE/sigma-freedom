# R7 LANGUAGE UNDERSTANDING — NATIVE TOOL GRANT V3 (SAFE / COMPLETE)

Date: 2026-09-12

## 0. Authority and grant meaning

This document grants permission to DESIGN, IMPLEMENT and RUN OFFLINE ADMISSION for the mechanical/native tool substrate required by R7 language learning.

It does NOT grant semantic authority, production binding, online synchronization, autonomous host tool selection, or a language-understanding PASS.

```text
TOOL_GRANT_KIND=BUILD_AND_OFFLINE_ADMISSION_ONLY
SIGMA_NATIVE_COGNITION_AUTHORITY=YES
HOST_SEMANTIC_AUTHORITY=NO
HOST_TOOL_SELECTION=FORBIDDEN
ONLINE_SYNC=NO
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
TOOL_AVAILABLE!=TOOL_LEARNED
CLAIM<=MACHINE_EVIDENCE
```

Target architecture:

```text
SIGMA native cognition
-> creates NEED_FAMILY / chooses exact admitted capability
-> supplies native state + arguments
-> exactly-one admitted bounded mechanical capability executes
-> raw mechanical result + receipt returns
-> SIGMA interprets / learns / revises
-> candidate state
-> native SIGMA accept / reject
-> transactional commit + provenance
```

Tool execution success never authorizes semantic claims.

## 1. T10A dependency correction before T10B

Historical T10A exact source/runner/admission provenance was not recoverable from connected evidence. Historical `T10A PASS` therefore MUST NOT be imported as an exact dependency by declaration alone.

Current reconstruction lineage:

```text
T10A_RECONSTRUCTION_ID=T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1
SOURCE_SHA256=953df93174d314354542daae66842652e30e13d9b92950bc997d08fbb9e15ee4
HISTORICAL_T10A_PROVENANCE_IMPORTED=NO
HISTORICAL_T10A_BOUNDS_IMPORTED=NO
T10A_RECONSTRUCTION_RUNTIME_ADMISSION=NOT_RUN
```

T10B may inherit archive/container bounds only after the reconstruction has an exact runtime admission root and an exact resource-profile identity. Until then:

```text
T10B_IMPLEMENTATION_DESIGN_ALLOWED=YES
T10B_RUNTIME_ADMISSION_BLOCKED_ON_T10A_RECONSTRUCTION=YES
T10B_PRODUCTION_BINDING=NO
```

A future combined gate must be named exactly as the evidence supports, e.g. `T10A_RECONSTRUCTION_V1 + T10B`, not silently renamed historical `T10A + T10B`.

## 2. Global mechanical safety envelope

Every family MUST freeze:

```text
CAPABILITY_ID
ABI_VERSION
SOURCE_SHA256
BUILD_RECIPE_SHA256
BINARY_SHA256
INPUT_SCHEMA_SHA256
OUTPUT_SCHEMA_SHA256
RESOURCE_PROFILE_SHA256
ADMISSION_ROOT_SHA256
STATE
```

Every callable capability must be `STATE=ADMITTED`. Registry semantics:

```text
exactly 1 exact ADMITTED match -> callable
0 match -> HOLD
>1 match -> HOLD
identity mismatch -> HOLD
schema mismatch -> HOLD
resource-profile mismatch -> HOLD
admission-root mismatch -> HOLD
fallback / reordering / argument invention -> FORBIDDEN
host capability selection -> FORBIDDEN
```

Every resource profile MUST bound input bytes before expensive parsing/conversion, in addition to semantic-free internal bounds. At minimum as applicable:

```text
MAX_INPUT_BYTES
MAX_FIELD_BYTES
MAX_RECORDS
MAX_NESTING_DEPTH
MAX_OUTPUT_BYTES
MAX_MEMORY
MAX_OPS
MAX_STEPS
MAX_TIME
MAX_STATE_BYTES
```

Pre-execution byte/resource refusal is mechanical and allowed. It must emit a receipt and MUST NOT be counted as native cognition.

Network, shell, arbitrary process execution, dynamic code loading, unfrozen JIT, hidden model download and arbitrary filesystem access are forbidden unless a future separately admitted mechanical capability explicitly proves them necessary and safe.

## 3. T10B_DOCUMENT_INPUT

Required:

```text
EPUB
DETERMINISTIC_PDF_TEXT_LAYER
MIME_MULTIPART
CHARSET_DECODE
EXACT_SOURCE_SPAN_PROVENANCE
```

T10B runs in an isolated fingerprinted parser sandbox. Required hard limits include input bytes, decompressed bytes, entry count, per-entry bytes, nesting depth, output text bytes and parser time/steps.

### EPUB

Mechanical only:

```text
bounded ZIP/container handling
package/spine order
bounded XML/XHTML text extraction
exact source/container/member provenance
transform hashes
```

Forbidden:

```text
JS execution
macros/actions
embedded executable execution
external resource fetch
DRM bypass
arbitrary filesystem access
semantic layout inference
```

Symlink, traversal, absolute paths, duplicate ambiguous paths, encrypted/unsupported members and decompression-bound violations fail closed.

### PDF

Only deterministic existing text-layer extraction is allowed. No OCR. No semantic reading-order oracle. No JavaScript/actions, embedded executable execution, external fetch or arbitrary filesystem access.

Output must preserve page/object/span provenance and parser/transform identity so later SIGMA cognition can decide how to interpret ordering.

### MIME / charset

Multipart parsing and charset decoding must be bounded, versioned and deterministic. Charset tables/version are frozen. Unsupported or ambiguous charset declarations fail closed; raw bytes and transform provenance remain addressable.

T10B returns bounded UTF-8 text + purely mechanical ordering/provenance/transform hashes. It does not summarize, translate, rank importance, infer entities or choose evidence.

## 4. R7L-T01 CHECKED NUMERIC + CANONICAL SERIALIZATION

Required:

```text
int64/uint64 parse+format
checked add/sub/mul/div/mod
saturating counters
bounded float32/float64
min/max/clamp
stable comparisons
canonical numeric serialization
typed tuple/record serialization
```

Freeze overflow, div0, NaN, Inf, signed-zero, rounding and endian/canonicalization semantics. No silent coercion that changes type identity. Tool returns typed numbers/records only.

## 5. R7L-T02 COLLECTION / ORDERED MEMORY CORE

Required:

```text
map
set
multimap
ordered map
deque
priority queue
stable sort
top-k
dedupe
bounded mechanical cache
exact iterator
```

Iteration and tie-breaking must be deterministic in admission mode. Cache is scratch/mechanical only and MUST NOT silently evict canonical epistemic memory. SIGMA supplies keys, scores, priorities and retention decisions.

## 6. R7L-T03 UNICODE / SPAN / POSITION CORE

Required:

```text
byte<->codepoint mapping
codepoint<->grapheme mapping
Unicode grapheme boundary
Unicode word-boundary view
Unicode sentence-boundary view
exact span table
parent/child span
ordered span sequence
interval overlap/containment lookup
source-version-bound span identity
```

Freeze Unicode version and normalization tables. Raw source view is preserved; normalization/case-fold/boundary outputs are views with exact transformation/span mapping. Invalid UTF-8 handling policy is explicit and fail-closed or explicitly loss-marked.

Boundary != semantic word/sentence. No entities, motives, roles or language meaning.

## 7. R7L-T04 GENERIC SEQUENCE ALGORITHMS

Required:

```text
edit distance
weighted edit distance with caller costs
LCS
bounded alignment
prefix/suffix structures
trie
suffix array/index
rolling hash
multi-pattern matching
bounded DP tables
sequence diff
caller-defined finite-state transition execution
```

All costs/rules are caller supplied. Bound sequence length/table cells/memory/steps. No built-in language grammar, lexicon or semantic equivalence.

## 8. R7L-T05 GENERIC STRUCTURE INDUCTION / PARSING COMPUTE

Required:

```text
chart tables
CKY/Earley-style generic mechanics
weighted finite-state mechanics
constraint propagation
bipartite matching/assignment
bounded beam/search
generic tree construction/manipulation
```

Grammar/rules/weights/constraints are supplied or learned by native SIGMA. Output is structural candidate data only.

Forbidden built-ins include English grammar, POS/NER/dependency/semantic-role or subject/object oracle, coreference oracle and hidden language-specific rule tables.

## 9. R7L-T06 TENSOR / AUTODIFF

Required:

```text
dense+sparse tensors
batch matrix operations
gather/scatter
reductions
elementwise functions
softmax/log-softmax/logsumexp
normalization
masked operations
generic losses
autodiff
gradient clipping
deterministic initialization
checkpoint/load
bounded SGD
bounded Adam/AdamW-equivalent
```

Mandatory resource limits:

```text
MAX_TENSOR_ELEMENTS
MAX_TENSOR_BYTES
MAX_MEMORY
MAX_OPS
MAX_STEPS
MAX_BACKWARD_STEPS
MAX_TIME
```

Admission uses a deterministic reference mode with explicit seed. Any accelerated/nondeterministic backend requires a distinct capability identity and separate admission.

Optimizer output is candidate parameter state only. Tool MUST NOT commit authoritative learned state. Native SIGMA accepts/rejects; transactional native path performs authoritative commit.

No Python eval, shell, arbitrary JIT, network, model download, hidden pretrained weights or hidden semantic targets.

## 10. R7L-T07 TRAINABLE SEQUENCE REPRESENTATION

Required:

```text
embedding lookup/update
positional mechanics
masked scaled dot-product attention
multi-head composition
recurrent-state primitive
1-D sequence convolution
pooling
residual composition
normalization
SIGMA-supplied causal/bidirectional masks
```

No pretrained weights, pretrained vocabulary, external LLM or semantic embeddings.

Every candidate learned state binds:

```text
ARCHITECTURE_SHA256
PARAMETER_STATE_SHA256
TRAINING_EVIDENCE_ROOT_SHA256
CHECKPOINT_SHA256
TOKENIZER_STATE_SHA256 if used
REVISION_PARENT_SHA256
```

## 11. R7L-T08 VECTOR MEMORY / RETRIEVAL

Required:

```text
vector insert/update/delete
exact kNN
bounded ANN
cosine/L2/dot kernels
quantization
caller-controlled index
exact candidate provenance
```

Exact kNN is the bounded admission reference. ANN mode freezes index identity, seed/build parameters and must be separately characterized against exact bounded fixtures.

Result role is `CANDIDATE_NEIGHBORS_ONLY`.

```text
nearest != same meaning
retrieved != relevant
```

Tool never generates semantic embeddings.

## 12. R7L-T09 STATISTICS / INFORMATION / UNCERTAINTY

Required:

```text
count/distinct/weighted count
mean/variance/covariance
histogram
entropy/cross-entropy/conditional entropy
mutual information
PMI-like caller-defined statistics
probability normalization
caller-defined Bayesian/count-update mechanics
confidence interval mechanics
distribution comparison
reservoir sampling
seeded random sampling
```

SIGMA supplies features/groups/priors/assumptions/weights/population definitions. Tool returns numbers only.

It MUST NOT return semantic labels such as relevant, important, true, support, contradiction or meaning. Correlation/significance/probability never become truth authority.

## 13. R7L-T10 GENERIC RELATION / GRAPH SUPPORT

Required as extension of admitted graph mechanics where needed:

```text
caller-typed edge storage
multigraph
hyperedge mechanics
temporal/version edges
bounded subgraph matching
bounded graph edit
clustering/community mechanics
numeric message-passing kernel
path comparison
connected evidence-component operations
```

Bound nodes, edges, search states and message steps. Clustering produces mechanical group IDs/numbers only.

Tool MUST NOT label CAUSE, MOTIVE, PERSON, AGENT, THEME, VALUE or real-world relation meaning.

## 14. R7L-T11 CONTINUAL-LEARNING / PARAMETER-MEMORY MECHANICS

Required:

```text
experience replay buffer mechanics
stratified/reservoir sampling
checkpoint delta
parameter diff
bounded rehearsal
caller-weighted regularization
versioned learned-state snapshot
candidate merge construction
rollback
quantization/compression
before/after retention metrics
```

SIGMA chooses what to retain/rehearse and supplies weights/targets. Merge/compaction/rehearsal outputs are candidates only. No silent canonical-memory eviction or autonomous importance scoring by the tool.

## 15. R7L-T12 CAPABILITY REGISTRY / CALL GATE

Required exact manifest binding:

```text
CAPABILITY_ID
ABI_VERSION
SOURCE_SHA256
BUILD_RECIPE_SHA256
BINARY_SHA256
INPUT_SCHEMA_SHA256
OUTPUT_SCHEMA_SHA256
RESOURCE_PROFILE_SHA256
ADMISSION_ROOT_SHA256
STATE
```

SIGMA supplies `CAPABILITY_ID + arguments` or a native `NEED_FAMILY` resolved by native SIGMA under exactly-one-ADMITTED semantics.

Gateway verifies identity only; host does not choose capability, reorder fallbacks or invent arguments.

## 16. R7L-T13 EXECUTION / TRAINING RECEIPTS

Every invocation, success or failure, records at minimum:

```text
INVOCATION_ID
TX_ID if stateful
CAPABILITY_ID + exact manifest identity
INPUT_SHA256
ARGUMENTS_SHA256
RESULT_SHA256
OUTPUT_SHA256
PARAMETER_STATE_BEFORE_SHA256 if applicable
PARAMETER_STATE_AFTER_SHA256 if applicable
SEED if applicable
OPERATION_COUNT
TENSOR_BYTES if applicable
PEAK_MEMORY
MONOTONIC_ELAPSED
STEP_LIMIT + STEP_LIMIT_HIT
TIME_LIMIT + TIMEOUT_HIT
FAILURE_STATUS
```

Receipts are audit facts only and are persisted through admitted transactional/provenance paths where applicable.

## 17. R7L-T14 MULTILINGUAL TEXT MECHANICS

Required:

```text
Unicode script/category lookup
grapheme/codepoint statistics
normalization views
bidi-safe span mapping
combining-mark-safe slicing
case-fold view
locale-independent raw representation
```

No translation, dictionary meaning, morphology labels, multilingual semantic equivalence or pretrained multilingual embeddings. Language identification, if mechanically estimated in a future capability, is never semantic authority.

Cross-language equivalence must be learned by native SIGMA.

## 18. R7L-T15 LEARNED TOKENIZER / SUBWORD MECHANICS — REQUIRED

This family is mandatory and MUST NOT be omitted from the SYNC grant.

Required:

```text
byte/codepoint/grapheme views
frequency mechanics
deterministic BPE training
generic unigram-subword mechanics
bounded vocabulary construction
merge/split mechanics
token IDs
byte fallback
versioned tokenizer state
```

No pretrained vocabulary, dictionary, English morphology or semantic labels. SIGMA selects training evidence/corpus and accepts/rejects tokenizer candidate state.

```text
TOKEN!=WORD
TOKEN!=MEANING
TOKENIZER!=UNDERSTANDING
```

## 19. R7L-T16 GENERIC TRAINING OBJECTIVES — REQUIRED

This family is mandatory and MUST NOT be omitted from the SYNC grant.

Required generic mechanics:

```text
cross-entropy / NLL
MSE
Huber
logistic
margin/ranking
triplet-style
contrastive
masked-sequence objective
regularization
```

SIGMA supplies all targets, positive/negative pairs, masks, weights, margins and temperatures. Tool MUST NOT create semantic labels, positive pairs or curriculum choices.

```text
LOSS_DECREASE!=UNDERSTANDING
```

## 20. Absolutely forbidden semantic-oracle APIs

Do not implement or hide equivalents of:

```text
understand
summarize
translate
pretrained semantic_embedding
is_paraphrase
find_synonym
infer_intent
infer_motive
detect_theme
detect_value
semantic_role
hidden semantic coreference/POS/NER/dependency
choose_evidence
choose_important_memory
choose_training_examples
decide_support
decide_contradiction
decide_truth
generate_search_query
generate_answer
select_best_interpretation
host tool selection
```

No pretrained LLM/NLP/embedding/translation model may enter as an unaccounted host oracle.

Any future learned model becomes an explicit cognition component with frozen architecture/model/parameter identities, native-controlled state/provenance, bounded execution, candidate-only updates and independent blind admission.

## 21. Offline admission standard for every family

Required lifecycle:

```text
CAPABILITY_CONTRACT
-> DEPENDENCY_IDENTITY_CHECK
-> SOURCE_FREEZE
-> BUILD_RECIPE_FREEZE
-> DETERMINISTIC_BUILD
-> BINARY/ABI/INPUT_SCHEMA/OUTPUT_SCHEMA/RESOURCE_PROFILE_FREEZE
-> FIXTURES_CREATED_ONLY_AFTER_FREEZE
-> DIRECTED
-> RANDOMIZED_AFTER_FREEZE
-> REPLAY
-> MALFORMED/ADVERSARIAL
-> PRE_EXECUTION_INPUT_BYTE_BOUND
-> RESOURCE/TIMEOUT/STEP_LIMIT
-> COUNTERFACTUAL
-> HIGH_ENTROPY LEAK AUDIT
-> SEMANTIC-ORACLE LEAK AUDIT
-> RAW RESULT CAPTURE BEFORE ORACLE
-> HOST-SUBSTITUTION AUDIT
-> EXACT PRIOR-LAYER REGRESSION
-> COMBINED COMPATIBILITY
-> PASS/HOLD
```

For stateful families additionally:

```text
crash before write
crash during write
crash after write before receipt
restart/replay
duplicate TX
conflicting TX
rollback
corruption
state-hash mismatch
same-TX idempotence
```

For learned-state families additionally require causal learning gates:

```text
normal learned state works
randomized parameters degrade relevant behavior
removing relevant admitted memory changes evidence-dependent behavior
exact restore recovers
counterfactual training evidence changes candidate learned state
replay of same training TX causes no duplicate mutation
```

Failure is evidence. Gates must never be weakened to force PASS.

## 22. Combined mechanical pipeline gate

Only after individual exact admissions:

```text
T10 document bytes
-> admitted T10 document input
-> exact spans
-> admitted learned tokenizer
-> tensor/autodiff
-> trainable sequence candidate state
-> vector candidates
-> statistics
-> graph candidate state
-> continual-learning candidate
-> exact capability gate
-> execution receipt
-> native SIGMA accept/reject
-> transactional commit
-> provenance
-> restart/resume
```

```text
COMBINED_TOOL_PASS!=LANGUAGE_UNDERSTANDING
```

## 23. R7 cognition blind gate after tools exist

No evaluator semantic fixture may be visible to source/build/freeze or to mechanical tools as a hidden oracle.

Native SIGMA cognition must independently pass unseen evidence for at least:

```text
low-overlap same meaning
high-overlap different meaning
compositional generalization
role reversal
negation
quantifier/scope change
distant reference/coreference
ambiguity with multiple retained hypotheses
ellipsis/context dependence
temporal ordering vs causality
entity persistence and relationship change
supporting vs contrary vs neutral later evidence
later revision / hypothesis retirement
cross-chapter QA
whole-work synthesis after source deletion
unique-event retention
irrelevant-frequency suppression
novel story transfer
cross-language transfer
compact-memory recall + revision
native knowledge-gap generation / refusal to guess
native capability selection
wrong-tool rejection
unavailable-tool HOLD
```

Tool availability alone satisfies none of these semantic gates.

## 24. Claim ceiling

```text
TOOL_AVAILABLE!=TOOL_LEARNED
TOKEN!=MEANING
TOKENIZER!=UNDERSTANDING
FREQUENCY!=IMPORTANCE
CO_OCCURRENCE!=MEANING
VECTOR_SIMILARITY!=SEMANTIC_EQUIVALENCE
EMBEDDING!=MEANING
PARSE_TREE!=UNDERSTANDING
GRAPH_EDGE!=REAL_WORLD_RELATION
ATTENTION_WEIGHT!=EXPLANATION
LOSS_DECREASE!=UNDERSTANDING
PARAMETER_CHANGE!=USEFUL_LEARNING
TRAINED!=GENERALIZED
HIGH_PROBABILITY!=TRUE
RETRIEVED!=RELEVANT
SUPPORTED!=TRUE
CITATION!=TRUTH
EOF!=UNDERSTOOD
SOURCE_REMOVED_PLUS_RECALL!=WHOLE_WORK_UNDERSTANDING
COMPRESSION_RATIO!=SEMANTIC_RETENTION
```

## 25. Promotion order

```text
T10A_RECONSTRUCTION_V1 exact runtime admission
-> freeze exact reconstruction resource-profile identity
-> T10B exact admission using that profile
-> T10A_RECONSTRUCTION_V1 + T10B combined admission
-> R7L-T01..T16 individual offline admission
-> cross-family combined admission
-> R7 cognition blind/causal gates
-> READ_ONLY_SYNC candidate
-> isolated graft
-> offline shadow
-> real-source online shadow
-> bounded soak
-> promotion candidate
-> explicit cutover
```

No stage is skipped by declaration.

## 26. Current grant state

```text
R7_TOOL_FAMILY_COUNT=17
T10B_PLUS_R7L_T01_THROUGH_T16=GRANTED_FOR_DESIGN_AND_OFFLINE_ADMISSION
T10A_RECONSTRUCTION_RUNTIME_ADMISSION=NOT_RUN
T10B_RUNTIME_ADMISSION=BLOCKED
R7L_T01_THROUGH_T16_RUNTIME_ADMISSION=NOT_RUN
CROSS_FAMILY_COMBINED=NOT_RUN
LANGUAGE_UNDERSTANDING=NOT_PROVEN
HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN
PRODUCTION_BINDING=NO
ONLINE_SYNC=NO
```

Final invariant:

```text
MECHANICAL COMPUTE MAY BE POWERFUL.
SEMANTIC AUTHORITY REMAINS NATIVE SIGMA.
CLAIM <= MACHINE EVIDENCE.
```
