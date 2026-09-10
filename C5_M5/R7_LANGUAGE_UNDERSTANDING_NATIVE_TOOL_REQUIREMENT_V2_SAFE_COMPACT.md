# R7 LANGUAGE UNDERSTANDING — NATIVE TOOL REQUIREMENT V2 (SAFE / COMPACT)

## Objective

Build bounded native/mechanical compute so SIGMA can learn language representations, relations, discourse, evidence, revision, multilingual transfer and whole-work structure.

```text
SIGMA cognition
-> chooses capability + arguments
-> admitted bounded native tool
-> raw mechanical result + receipt
-> SIGMA interprets/learns/revises
-> transactional native commit
```

Hard boundary:

```text
TOOL MAY COMPUTE
TOOL MUST NOT PROVIDE SEMANTIC ANSWERS
HOST MUST NOT CHOOSE MEANING / TOOL / EVIDENCE / TRUTH
```

Current authoritative substrate: T1-T3 admitted; T4-T9 FULL PASS; T10A PASS; T10B/T10 combined/T11 pending. ONLINE_SYNC=NO. PRODUCTION_BINDING=NO.

## Required families

### T10B_DOCUMENT_INPUT
EPUB; deterministic PDF text-layer; MIME multipart; charset decode; exact source/span provenance.

Run in isolated fingerprinted parser sandbox. Return only bounded UTF-8 text + mechanical ordering/provenance/transform hashes. NO JS/macros/actions/DRM execution/embedded executables/arbitrary filesystem/network/OCR/semantic-layout/pretrained NLP/LLM. Reuse T10A archive bounds. Unsupported/ambiguous/encrypted inputs fail closed. Then run exact T10A+T10B combined admission.

### R7L-T01 NUMERIC/SERIALIZATION
int64/uint64 parse+format; checked arithmetic; saturating counters; bounded float32/64; min/max/clamp; stable comparisons; canonical numeric + typed record serialization. Explicit overflow/div0/NaN/Inf semantics.

### R7L-T02 COLLECTIONS
map/set/multimap/ordered-map/deque/priority-queue/stable-sort/top-k/dedupe/bounded cache/exact iterator. SIGMA supplies scores/priorities. Cache MUST NOT silently evict canonical epistemic memory.

### R7L-T03 UNICODE/SPANS
byte<->codepoint; codepoint<->grapheme; Unicode grapheme/word/sentence boundary views; exact span table; parent/child/ordered spans; interval lookup; source-version-bound span IDs. Freeze Unicode version. Boundary != semantic word/sentence.

### R7L-T04 SEQUENCE ALGORITHMS
edit distance; weighted edit; LCS; bounded alignment; trie; suffix index; rolling hash; multi-pattern matching; bounded DP; diff; caller-defined finite-state execution. SIGMA supplies costs/rules.

### R7L-T05 GENERIC STRUCTURE INDUCTION
chart tables; CKY/Earley mechanics; weighted finite-state mechanics; constraint propagation; matching/assignment; bounded beam/search; generic trees. NO embedded language grammar or hidden POS/NER/dependency/semantic-role oracle.

### R7L-T06 TENSOR/AUTODIFF
dense+sparse tensors; batching; gather/scatter; reductions; softmax/logsumexp; normalization; masks; generic losses; autodiff; gradient clipping; deterministic init; checkpoint/load; bounded SGD/Adam-like optimizer.

Mandatory MAX_TENSOR_ELEMENTS/MAX_MEMORY/MAX_OPS/MAX_STEPS/MAX_TIME/MAX_BACKWARD_STEPS. NO Python eval/shell/arbitrary JIT/network/model download/unfrozen weights. Updates produce candidate parameter state; SIGMA accepts/rejects; authoritative commit is transactional. Every invocation gets bounded aggregate receipt; per-scalar logging is not required.

### R7L-T07 TRAINABLE SEQUENCE REPRESENTATION
embedding lookup/update; positional mechanics; masked attention; multi-head composition; recurrent state; 1-D convolution; pooling; residuals; normalization; SIGMA-supplied masks. NO pretrained weights/LLM/embeddings/vocabulary meaning. Learned parameters are versioned native state with architecture SHA, training evidence root, checkpoint SHA, provenance and revision lineage.

### R7L-T08 VECTOR MEMORY
vector insert/update/delete; exact kNN; bounded ANN; cosine/L2/dot; quantization; caller-controlled index; candidate provenance. SIGMA learns vectors. RESULT_ROLE=CANDIDATE_NEIGHBORS_ONLY. nearest != same meaning; retrieved != relevant.

### R7L-T09 STATISTICS/UNCERTAINTY
count/distinct/weighted count; mean/variance/covariance; histogram; entropy/cross-entropy/conditional entropy/MI; PMI-like caller-defined statistics; probability normalization; caller-defined count/Bayesian mechanics; confidence intervals; distribution comparison; bounded sampling. SIGMA supplies features/groups/priors/assumptions/weights/population. Tool returns numbers only. correlation != causation; significance != truth.

### R7L-T10 GRAPH/RELATION SUPPORT
Extend T2 if needed: multigraph/hyperedges/temporal edges/bounded subgraph matching/graph edit/clustering/message-passing/path comparison/evidence components. SIGMA supplies edge meaning. Tool MUST NOT label CAUSE/MOTIVE/PERSON/AGENT/THEME/VALUE. Bound nodes/edges/search/message steps.

### R7L-T11 CONTINUAL LEARNING
bounded replay; reservoir/stratified sampling; checkpoint delta; parameter diff; bounded rehearsal; caller-weighted regularization; versioned snapshots; candidate state merge; rollback; quantization/compression; retention metrics. Merge creates candidate only; no silent canonical-memory eviction.

### R7L-T12 CAPABILITY REGISTRY/CALL GATE
Remain compatible with R4 academic native selection semantics:

```text
SIGMA creates NEED_FAMILY
-> exactly one matching ADMITTED capability
-> native SIGMA selects it
0 or >1 match -> WAIT/HOLD
HOST_SELECTION=FORBIDDEN
```

Bind CAPABILITY_ID to exact manifest: ABI_VERSION, SOURCE_SHA256, BINARY_SHA256, INPUT_SCHEMA_SHA256, OUTPUT_SCHEMA_SHA256, RESOURCE_PROFILE_SHA256, ADMISSION_ROOT_SHA256, STATE. Any mismatch/missing/duplicate -> HOLD. No fallback/reordering/argument invention.

### R7L-T13 EXECUTION RECEIPTS
Every learned-compute invocation: INVOCATION_ID, TX_ID if stateful, CAPABILITY_ID+identity, input/arguments/result/output hashes, parameter before/after hashes, seed, operation count, peak memory, monotonic elapsed, step/timeout limits+hits, failure status. Receipt persistence uses admitted transactional path and T9 provenance where applicable.

### R7L-T14 MULTILINGUAL TEXT MECHANICS
Unicode script/category; grapheme/codepoint stats; normalization views; bidi-safe spans; combining-mark-safe slicing; case-fold; locale-independent raw view. NO translation/dictionary meaning/multilingual semantic oracle/pretrained multilingual embeddings.

### R7L-T15 LEARNED TOKENIZER/SUBWORDS
byte/codepoint/grapheme views; frequency mechanics; deterministic BPE training; generic unigram-subword mechanics; bounded vocabulary construction; merge/split; token IDs; byte fallback; versioned tokenizer state. NO pretrained vocabulary/English morphology/dictionary semantics. TOKEN != WORD; TOKEN != MEANING.

### R7L-T16 GENERIC TRAINING OBJECTIVES
cross-entropy/NLL/MSE/Huber/logistic/margin/ranking/triplet-style/contrastive/masked-sequence/regularization mechanics. SIGMA supplies all targets, positive/negative pairs, masks, weights, margins and temperatures. Tool never creates semantic labels. LOSS_DECREASE != UNDERSTANDING.

## Forbidden semantic-oracle APIs

Do NOT implement mechanical tools equivalent to: understand, summarize, translate, pretrained semantic_embedding, paraphrase/synonym oracle, infer_intent/motive, detect_theme/value, semantic_role, hidden semantic coreference/POS/NER/dependency, choose_evidence, choose_important_memory, choose_training_examples, decide_support/contradiction/truth, generate_search_query/answer, select_best_interpretation.

No hidden pretrained LLM/NLP/embedding/translation model. Any future learned model must become explicit native cognition with frozen identity, provenance, bounded execution and independent blind admission.

## Global state rule

```text
OLD STATE
-> SIGMA request
-> raw tool result
-> SIGMA interpretation
-> candidate state
-> exact hash
-> SIGMA accept/reject
-> transactional commit
-> NEW STATE
```

TOOL_EXECUTION_SUCCESS != COGNITIVE_AUTHORITY.

## Offline admission standard

For each family: source freeze -> deterministic build -> binary/ABI/schema/resource freeze -> post-freeze fixtures -> directed -> randomized-after-freeze -> replay -> malformed/adversarial -> resource/timeout/step limits -> counterfactual -> high-entropy + semantic-oracle leakage audits -> host-substitution audit -> prior-layer regression -> combined compatibility.

Stateful families additionally: crash before/during/after write-before-receipt; restart/replay; duplicate/conflicting TX; rollback; corruption; state-hash mismatch.

Always: ONLINE_SYNC=NO; PRODUCTION_BINDING=NO; PRODUCTION_MUTATION=NO.

## Combined offline pipeline

```text
T10 document
-> exact spans
-> learned tokenizer
-> tensor/autodiff
-> trainable sequence representation
-> vector candidates
-> statistics
-> graph candidate state
-> continual-learning candidate
-> capability gate
-> receipt
-> T5 durable commit
-> T9 provenance
-> restart/resume
```

COMBINED_TOOL_PASS != LANGUAGE_UNDERSTANDING.

## Language-understanding blind gate

R7 must pass unseen post-freeze tests covering: low-overlap same meaning; high-overlap different meaning; compositional generalization; role reversal; negation; quantifier/scope; distant reference/coreference; ambiguity; ellipsis/context; temporal vs causal; entity persistence/relationship change; support/contrary/neutral evidence; later revision/hypothesis retirement; cross-chapter QA; whole-work synthesis after source deletion; unique-event retention; irrelevant-frequency suppression; novel story transfer; cross-language transfer; compact-memory recall/revision; native gap + refusal to guess; native capability use; wrong-tool rejection; unavailable-tool HOLD.

Causal learning gates: normal learned state works; randomized parameters degrade; removing relevant memory changes evidence-dependent behavior; exact restore recovers; counterfactual training evidence changes learned state; replay of same training TX causes no duplicate mutation.

## Claim ceiling

```text
TOOL_AVAILABLE != TOOL_LEARNED
TOKEN != MEANING
TOKENIZER != UNDERSTANDING
FREQUENCY != IMPORTANCE
CO-OCCURRENCE != MEANING
VECTOR_SIMILARITY != SEMANTIC_EQUIVALENCE
EMBEDDING != MEANING
PARSE_TREE != UNDERSTANDING
GRAPH_EDGE != REAL-WORLD RELATION
ATTENTION_WEIGHT != EXPLANATION
LOSS_DECREASE != UNDERSTANDING
PARAMETER_CHANGE != USEFUL_LEARNING
TRAINED != GENERALIZED
HIGH_PROBABILITY != TRUE
RETRIEVED != RELEVANT
SUPPORTED != TRUE
CITATION != TRUTH
EOF != UNDERSTOOD
SOURCE_REMOVED + RECALL != WHOLE_WORK_UNDERSTANDING
COMPRESSION_RATIO != SEMANTIC_RETENTION
```

## Promotion order

T10B PASS -> T10 combined PASS -> R7L-T01..T16 offline PASS -> cross-family combined PASS -> R7A1 epistemic revision -> R7A2 whole-work -> R7A3 autonomous capability use -> R7A4 cross-work revision -> R7A5 continual research/curriculum -> crash/restart + source-removal + multilingual + anti-host-substitution PASS -> READ-ONLY SYNC -> isolated graft -> offline shadow -> real-source online shadow -> bounded soak -> promotion candidate -> explicit cutover.

## Final invariant

```text
MECHANICAL COMPUTE MAY BE POWERFUL.
SEMANTIC AUTHORITY REMAINS NATIVE SIGMA.
CLAIM <= MACHINE EVIDENCE.
```
