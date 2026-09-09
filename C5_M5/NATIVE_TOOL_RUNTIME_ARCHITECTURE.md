# SIGMA C5 M5 — Native Tool Runtime Architecture

## Decision

Generic computational tools belong inside the SIGMA candidate runtime/VM, not in host-side cognition scripts.

The preferred architecture is:

`SIGMA cognition -> native tool ABI -> sandboxed runtime implementation -> OS/kernel`

The host remains an external substrate/observer: process launch, sandbox/resource limits, artifact fingerprinting, logging, rollback, and post-hoc evaluation. The host must not choose semantic goals, tool meaning, queries, evidence interpretation, hypotheses, summaries, themes, values, truth/support/conflict stances, or memory selections.

## Tool ownership

A tool is considered **SIGMA-native** when all of the following hold:

1. SIGMA chooses whether and when to invoke it.
2. SIGMA supplies the arguments from native state.
3. The tool implements a domain-general/mechanical operation.
4. The tool returns raw/mechanical results, not a semantic conclusion for the active task.
5. The tool ABI and implementation are versioned, fingerprinted, bounded, and included in candidate admission/blind tests.
6. Tool results enter SIGMA native state and are interpreted by SIGMA.

The fact that the OS/kernel ultimately executes file, network, math, memory, or device instructions does not make those operations host cognition.

## Initial native tool families

The runtime may expose, as needed:

- arithmetic, integer/float math, counters and comparisons;
- hash/content-address primitives;
- maps, sets, queues, stacks and bounded graphs;
- generic graph traversal/path/connectivity operations;
- vector/matrix arithmetic and generic similarity/distance kernels;
- statistics, clustering and generic optimization operations;
- Unicode/text/byte normalization and encoding primitives;
- generic JSON/XML/HTML parsing into syntax structures;
- local exact/approximate indexing and retrieval;
- compression, deduplication and bounded serialization;
- filesystem/KV/database/transaction primitives;
- stream/buffer/chunk primitives;
- sandboxed DNS/HTTP/TLS/network primitives;
- clocks, scheduling and monotonic counters;
- cryptographic verification and signatures;
- bounded random/sampling primitives;
- resource introspection and limits.

These are not a fixed list. New generic primitives may be added when a real computational bottleneck is demonstrated.

## Forbidden native-tool shortcuts

Do not add an ABI call whose implementation answers the cognition problem for SIGMA, such as:

- `summarize(work)`;
- `detect_theme(work)`;
- `infer_motive(sentence)`;
- `semantic_role(sentence)` backed by hidden language rules;
- `is_paraphrase(a,b)` backed by a host semantic oracle;
- `choose_important_memory(...)` using host salience judgments;
- `generate_search_keywords(gap)` using host cognition;
- `decide_truth/support/conflict(...)`;
- `generate_final_answer(...)`.

If a neural/embedding/language model is later required, it must be incorporated explicitly as a native candidate component: local/runtime-bound, fingerprinted, bounded, state/provenance controlled, and independently adversarially tested. It must not be an unaccounted host oracle.

## Native tool ABI safety

Every tool family must have:

- exact input/output schema;
- deterministic behavior where appropriate;
- explicit resource bounds;
- failure/error semantics;
- provenance/audit record for external I/O;
- no hidden semantic defaults;
- versioned ABI fingerprint;
- regression tests against all previously admitted capabilities;
- host-substitution/adversarial tests.

## Production integration

Tool-runtime expansion is a candidate change. It must not mutate production C5V3 during admission.

The candidate runtime/VM is built and fingerprinted separately, then tested under isolated candidate state. Only after cognition/memory/tool gates pass may it proceed through:

`read-only ABI synchronization -> isolated graft -> autonomous shadow -> soak/restart/recovery -> promotion -> explicit user-authorized cutover -> rollback retained`

## Current implication

The recent seven host-exposed primitives (`read_text`, `write_text`, `str_len`, `str_replace`, `str_split`, `list_len`, `list_get`) are no longer treated as the desired permanent execution model. They are historical minimum plumbing used by recent candidates.

Future M5 work should preferentially migrate generic computational capability into the native SIGMA runtime so the host can remain an independent observer/sandbox rather than an execution middleman for every operation.
