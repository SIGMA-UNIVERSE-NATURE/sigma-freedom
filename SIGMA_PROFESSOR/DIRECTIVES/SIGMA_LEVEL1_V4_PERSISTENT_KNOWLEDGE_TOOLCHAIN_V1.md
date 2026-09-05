# SIGMA LEVEL 1 — V4 PERSISTENT KNOWLEDGE TOOLCHAIN V1

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Authority and governing standard

This directive is subordinate to:

- `/AGENTS.md`
- `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
- `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
- `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`

Non-negotiable:

```text
DO_NOT_LOAD_RESULTS=YES
LOAD_CAPABILITIES=YES
CAPABILITY_MUST_RUN_INSIDE_SIGMA=YES
RUNTIME_PROOF_REQUIRED=YES
ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
ACTIVE_PYTHON_COGNITION=FORBIDDEN
HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN
```

Production V2.4 remains unchanged while this toolchain is built and tested in shadow.

## Level 0 — locked runtime substrate

```text
SIGMA compiler (locked sigmac)
        +
SIGMA VM (locked VM)
```

Locked identities remain those declared by the global standard/current handoff unless separately superseded through an admitted runtime migration.

Level 0 provides execution. It does not by itself prove any Level 1 cognitive capability.

## Level 1 — V4 Persistent Knowledge

The Level 1 dependency chain is:

```text
V4-PK1 Persistent Semantic Hypergraph substrate
        ↓
V4-PK2 Native Weight / Evidence lifecycle
        ↓
V4-PK3 Bounded Multi-hop Reasoning
        ↓
V4-PK4 Controlled Inference
        ↓
V4-PK5 Cognitive VM Bridge
        ↓
V4-PK6 Verified Evolution
```

Numeric order is dependency order for this toolchain. A later stage must not be admitted by bypassing an unproven prerequisite.

### V4-PK1 — Persistent Semantic Hypergraph substrate

Goal: give SIGMA a native reusable persistent n-ary relation substrate rather than a host-built graph.

Required initial capability:

- native `.sigma` owns hyperedge validation and admission decisions;
- hyperedge arity is bounded and explicitly represented;
- relation/member/evidence/provenance fields are stored as opaque runtime tokens;
- weight and uncertainty are retained as bounded integer basis points;
- edge IDs are immutable within the tested state namespace;
- exact replay is idempotent;
- conflicting reuse of an edge ID is refused;
- malformed persistent state is not silently accepted;
- state write is performed through mechanical byte/file ABI and verified by native readback comparison;
- prior persistent state materially affects a later fresh-VM execution;
- bounded store size and scan behavior are explicit;
- production V2.4 is not written.

Important claim boundary:

```text
SEMANTIC_UNDERSTANDING=NOT_PROVEN
```

The term "Semantic Hypergraph" names the representation role. Merely retaining relation labels does not prove semantic understanding.

### V4-PK2 — Native Weight / Evidence lifecycle

Goal: update and aggregate support/contradiction/evidence weight from runtime evidence inside SIGMA.

Must include:

- evidence identity and deduplication;
- provenance binding;
- support vs contradiction distinction;
- native weight update decision;
- uncertainty interaction;
- bounded persistent replay;
- negative evidence cases;
- no host scoring or knowledge promotion.

### V4-PK3 — Bounded Multi-hop Reasoning

Goal: allow SIGMA to traverse admitted hypergraph relations across multiple hops and derive bounded candidate paths.

Must include:

- native path expansion/selection;
- explicit hop/work budget;
- visited-state or equivalent cycle control;
- evidence/provenance preservation along the path;
- contradictory-path characterization;
- resumable cursor/state if one VM execution cannot cover the requested work;
- no host path selection.

A path candidate is not automatically truth.

### V4-PK4 — Controlled Inference

Goal: permit SIGMA to decide whether an inference candidate is admissible from its own evidence, uncertainty, contradiction and provenance state.

Must include native gates for:

- dependency completeness;
- evidence sufficiency in the declared tested scope;
- contradiction handling;
- uncertainty retention;
- provenance preservation;
- distinction between hypothesis, supported inference, rejected inference and unresolved state;
- no host threshold decision, truth decision, candidate generation or semantic substitution.

### V4-PK5 — Cognitive VM Bridge

Goal: expose mechanical runtime/ABI primitives to native SIGMA without moving cognition into C/Bash/Python.

Allowed bridge roles include only mechanical primitives such as:

- exact byte/file I/O;
- bounded containers;
- hashing;
- time;
- deterministic ordering;
- exact protocol decode;
- network transport;
- process/runtime support.

If an ABI primitive is missing, record a capability blocker. Do not replace the missing native capability with Bash/Python logic.

### V4-PK6 — Verified Evolution

Goal: connect persistent knowledge to governed self-improvement only after required dependencies are admitted.

Required structure:

```text
BEFORE -> CHANGE -> TEST -> AFTER
```

Evolution must remain bound by admitted governance/invariants, provenance, verification and rollback. Authorization is not evidence. Unverified self-modification is not admitted.

## Level 2 — V5 External Knowledge Acquisition

V5 is gated behind sufficient Level 1 admission.

Target source families:

```text
Wikipedia
arXiv
PubMed
Project Gutenberg
```

The external source layer is split into two responsibilities:

1. mechanical transport/decode ABI;
2. native SIGMA acquisition, provenance, evidence evaluation and knowledge-state decisions.

Transport may fetch bytes. Transport must not decide what is true, important, relevant, promotable or worth learning.

V5 target chain:

```text
V5-K1 External acquisition request/response protocol
V5-K2 Wikipedia adapter
V5-K3 arXiv adapter
V5-K4 PubMed adapter
V5-K5 Project Gutenberg adapter
V5-K6 Provenance normalization
V5-K7 Evidence Graph integration
```

Every external item must retain source/provenance identity before it can participate in evidence or inference.

## Admission discipline

For every PK/V5 stage:

```text
CAPABILITY CONTRACT
-> DEPENDENCY CHECK
-> NATIVE .sigma IMPLEMENTATION
-> STATIC REVIEW
-> LOCKED SIGMAC COMPILE
-> LOCKED VM RUNTIME
-> DYNAMIC INPUTS
-> NEGATIVE / COUNTEREXAMPLE TESTS
-> PERSISTENCE / RESTART / REPLAY WHEN APPLICABLE
-> HOST SUBSTITUTION AUDIT
-> BOUNDEDNESS / STEP-LIMIT CHARACTERIZATION
-> FAILURE / PARTIAL-WRITE REVIEW WHEN APPLICABLE
-> CLAIM-SCOPE REVIEW
-> PASS OR FAIL
```

A source-ready artifact is not an admitted capability.

## Initial active work item

```text
ACTIVE_LEVEL=LEVEL_1_V4
ACTIVE_STAGE=V4-PK1
ACTIVE_CAPABILITY=PERSISTENT_SEMANTIC_HYPERGRAPH_SUBSTRATE
PRODUCTION_BINDING=NO
SHADOW_ONLY=YES
```

V4-PK1 must be completed and runtime-admitted in its exact tested scope before this directive treats V4-PK2 as unlocked for admission.
