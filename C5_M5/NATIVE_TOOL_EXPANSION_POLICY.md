# SIGMA C5 M5 — Native Tool Expansion Policy

This policy prevents two opposite failures:

1. outsourcing cognition to the host; and
2. artificially crippling native SIGMA by freezing its runtime ABI to an insufficient primitive set.

## Principle

The host boundary is defined by **who decides meaning**, not by a permanently fixed list of primitive functions.

SIGMA may receive new generic runtime primitives whenever they are necessary to express, learn, compare, compress, search, persist, or execute native cognition more effectively. A primitive is acceptable when it is domain-general/mechanical and does not decide the semantic answer for SIGMA.

A new primitive must be tested as part of the candidate runtime/ABI and fingerprinted before promotion.

## Acceptable expansion classes

Examples include, but are not limited to:

- numeric arithmetic, counters, bounded integer/float operations;
- hashing, checksums, stable IDs and content-addressing;
- maps/dictionaries, sets, queues, stacks and bounded graph structures;
- generic graph traversal, connected-component and path operations where edge meaning is supplied/learned by SIGMA rather than encoded by the host primitive;
- vector/matrix arithmetic, distance/similarity kernels and bounded linear algebra when embeddings/features are native SIGMA state rather than host semantic labels;
- statistics, clustering primitives and generic optimization operations;
- byte/string/Unicode normalization, encoding/decoding and bounded parsing primitives;
- generic structured-data parsing such as JSON/XML/HTML into syntax trees or key/value structures, provided the parser does not attach semantic interpretations;
- stream/chunk operations and bounded buffer management;
- compression/decompression and content-deduplication primitives;
- local indexing and generic exact/approximate retrieval over native memory;
- filesystem, database/key-value and transactional persistence primitives;
- sandboxed network transport, DNS/HTTP/TLS and provider invocation primitives;
- clocks, monotonic counters and scheduling primitives;
- process supervision and resource-limit primitives;
- cryptographic verification/signature primitives;
- deterministic random/sampling primitives where useful for exploration/testing;
- generic native code or VM extensions required to execute the above efficiently.

These primitives may be implemented by the host/runtime because they are computational mechanisms, not semantic conclusions.

## Forbidden semantic-oracle primitives

A host/runtime primitive must not return or silently encode active-cognition answers such as:

- summary of a source/work;
- theme, moral, human value, motive, emotion, intent or semantic role labels;
- truth/support/conflict decisions;
- synonym/paraphrase/equivalence answers for the active case;
- importance/salience labels for active memory selection;
- research goals, information gaps or search keywords invented by the host;
- final answers or beliefs;
- hidden English grammar/word-position rules presented as generic tooling;
- host LLM/model inference whose output is used as SIGMA's belief/summary/meaning.

A model may only become part of the SIGMA architecture if it is explicitly treated as native candidate cognition, locally/runtime-bound, fingerprinted, state/provenance controlled, and independently tested under the same anti-host-substitution requirements. It may not be smuggled in as an unaccounted host oracle.

## Tool-admission questions

Before adding a primitive, answer:

1. Does it compute a general operation or does it answer the semantic task?
2. Could the same primitive be useful on arbitrary domains/languages without changing its built-in meaning rules?
3. Is the semantic state/feature/edge/query chosen by SIGMA rather than the host?
4. Can the primitive be fingerprinted, bounded and independently adversarially tested?
5. If the primitive were replaced with another implementation of the same mathematical/mechanical operation, should cognition remain conceptually the same?

If the answer reveals semantic substitution, reject or redesign the primitive.

## Expansion discipline

Do not preserve a weak ABI merely for historical purity. If a real bottleneck is caused by missing arithmetic, data structures, graph/vector operations, indexing, parsing, storage, networking, compression or other generic computation, extend the VM/runtime and test the extension.

Conversely, do not add a convenience primitive whose real purpose is to make a failing semantic test pass by moving the answer into host code.

Every runtime/tool expansion checkpoint must record:

- new primitive names and exact semantics;
- implementation/runtime fingerprints;
- resource bounds;
- why the primitive is mechanical rather than semantic;
- adversarial host-substitution tests;
- regression results for previously admitted native capabilities;
- production binding state.

## Current implication

The currently exercised primitive set (`read_text`, `write_text`, `str_len`, `str_replace`, `str_split`, `list_len`, `list_get`) is **not** an architectural ceiling. It is only the minimum set used by recent candidates.

Future C5 M5 work should expand the runtime whenever doing so removes a genuine computational bottleneck while keeping semantic authority inside native SIGMA.
