# SIGMA-Ψ PARALLEL COMPLETION PROTOCOL v1.0 — 2026-08-25

**ROLE:** `SUPPORTOR_WORKSPLIT_PROTOCOL`

**PURPOSE:** Complete SIGMA-Ψ across multiple independent chat/supportor windows without losing continuity, duplicating work, or silently changing frozen references.

## 0. LOCKED BASE

Every window MUST read/use these references before doing work:

1. `DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.0_20260825.md`
2. `DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.1_EXTENSION_20260825.md`
3. `DOCS/GPT_REFERENCE/SIGMA_PSI_SYMBOL_MATRIX_256_REFERENCE_v1.0_20260825.md`
4. `BRAIN/GUIDANCE/SIGMA_SUPPORTOR_MASTER_REFERENCE_LOCK_v1.0_20260825.md`

Authority rule:

`MACHINE EVIDENCE > VERIFIED SEMANTICS > VERSIONED SPEC/DECLARATION > FROZEN REFERENCE > HUMAN EXPOSITION`

Core law: `CLAIM <= EVIDENCE`.

No worker window may directly rewrite frozen v1.0/v1.1 references.

---

# 1. WORKSTREAMS

## WS-01 — GLYPH / TOKEN REGISTRY

Scope:
- 256-symbol matrix
- canonical glyph identity
- duplicate glyph detection
- multi-sense separation
- token/glyph status `V/D/R/X/P/C/M/H`

Output:
`BRAIN/WORKSTREAMS/SIGMA_PSI/WS01_GLYPH_TOKEN_REGISTRY_RESULT.md`

Do NOT invent executable semantics for unverified glyphs.

## WS-02 — LEXER / LEXICAL RULES

Scope:
- UTF-8 tokenization
- whitespace/newline behavior
- identifiers
- numbers/strings/null/bool
- comments
- `//` FLOORDIV vs comment distinction
- operators
- reserved words

Output:
`BRAIN/WORKSTREAMS/SIGMA_PSI/WS02_LEXER_RESULT.md`

Every lexical rule must include examples, counterexamples, ambiguity notes, and evidence status.

## WS-03 — GRAMMAR / COMPOSITION

Scope:
- headers
- `⟡(...) { ... }`
- `⚡`
- namespace composition `Σ.A.B`
- function/control-flow forms only when source/machine evidence exists
- block/scope/composition rules
- precedence/associativity references

Output:
`BRAIN/WORKSTREAMS/SIGMA_PSI/WS03_GRAMMAR_RESULT.md`

Rule: do not translate Python/C grammar into SIGMA.

## WS-04 — TYPES / VALUES / OPERATORS

Scope:
- minimum observed ValueType: NULL/BOOL/INT/FLOAT/STR
- candidate collection/value types
- unary/binary operators
- coercion/conversion
- equality/comparison
- arithmetic semantics
- FLOORDIV
- error cases

Output:
`BRAIN/WORKSTREAMS/SIGMA_PSI/WS04_TYPES_OPERATORS_RESULT.md`

Separate `observed implementation` from `proposed language design`.

## WS-05 — CONTROL FLOW / FUNCTIONS / STATE TRANSITIONS

Scope:
- CALL / RETURN
- IF / ELSE / WHILE only where exact executable surface is evidenced
- JUMP / JUMP_IF_FALSE semantic relationship
- scope/state transition
- iteration/traversal
- no hard-coded discovery

Output:
`BRAIN/WORKSTREAMS/SIGMA_PSI/WS05_CONTROL_STATE_RESULT.md`

Must report `OBSERVED / PROVEN / NOT_PROVEN`.

## WS-06 — BYTECODE ABI / COMPILER / VM CONTRACT

Scope:
- `SIGMBC01`
- opcodes
- operands/encoding
- stack/state behavior
- compiler-to-bytecode mapping
- runtime behavior
- ABI compatibility/fingerprint
- failure/error behavior

Output:
`BRAIN/WORKSTREAMS/SIGMA_PSI/WS06_ABI_VM_RESULT.md`

Machine evidence is authoritative.

## WS-07 — SEMANTIC CAPSULE / ONTOLOGY / HUMAN BRIDGE

Scope:
- SSC schema
- concept_id
- sense_id
- ontology/relations
- provenance/evidence fields
- mapping to Vietnamese/English/programming/runtime terminology
- semantic-loss notation

Output:
`BRAIN/WORKSTREAMS/SIGMA_PSI/WS07_SSC_HUMAN_BRIDGE_RESULT.md`

Goal: short SIGMA surface, deep semantic graph.

## WS-08 — EPISTEMIC / ETHICS / GOVERNANCE VOCABULARY

Scope:
- FACT/EVID/INF/OP/HYP/TRAD/INTERP/DECL/UNKNOWN
- uncertainty/certainty
- correction/provenance
- ethics/constitution/declarations/respect/freedom vocabulary
- equal dignity vs authority/permission

Output:
`BRAIN/WORKSTREAMS/SIGMA_PSI/WS08_EPISTEMIC_GOVERNANCE_RESULT.md`

Do not convert constitutional values into runtime proof.

## WS-09 — CONFORMANCE / ERROR TAXONOMY

Scope:
- lexical tests
- parser tests
- type/operator tests
- control-flow tests
- ABI/VM tests
- UTF-8/glyph tests
- negative/error tests
- evidence format

Output:
`BRAIN/WORKSTREAMS/SIGMA_PSI/WS09_CONFORMANCE_RESULT.md`

Every proposed conformance item must state whether a runnable test already exists.

## WS-10 — COMPLETENESS / CONFLICT AUDIT

Scope:
- ingest WS01–WS09
- list duplicates
- list unresolved conflicts
- list missing mandatory language elements
- classify `FROZEN / VERIFIED / DECLARED / PROPOSED / CONFLICT / MISSING`

Output:
`BRAIN/WORKSTREAMS/SIGMA_PSI/WS10_COMPLETENESS_AUDIT_RESULT.md`

This worker MUST NOT resolve conflicts silently; it reports them.

---

# 2. STANDARD RESULT CONTRACT

Every workstream result MUST begin with:

```text
WORKSTREAM_ID=
BASE_REFERENCE_VERSION=
SOURCE_SCOPE=
MACHINE_EVIDENCE_USED=
STATUS=
```

Every substantive entry should use:

```text
ENTRY_ID:
SOURCE:
STATUS: V|D|R|X|P|C|M|H
OBSERVED:
PROVEN:
NOT_PROVEN:
CONFLICT:
PROPOSED_NORMALIZATION:
EVIDENCE:
PROVENANCE:
```

Required ending:

```text
NEW_ENTRIES=
DUPLICATES=
CONFLICTS=
MISSING=
READY_FOR_MERGE=YES|NO
```

---

# 3. MERGE RULE

Only the designated MERGE window may produce the next master candidate.

Merge input:
- frozen v1.0
- frozen v1.1
- WS01–WS10 results
- machine evidence

Merge output target:

`DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_CANDIDATE_v1.2_<date>.md`

No workstream result overwrites another result.
No worker edits historical source.
No merge may upgrade `D/P` to `V` without evidence.
No conflict is resolved by deleting a source meaning; use sense separation/versioning/provenance.

---

# 4. WINDOW HANDOFF PROMPT

A new window can be given this exact compact instruction:

```text
Read BRAIN/GUIDANCE/SIGMA_PSI_PARALLEL_COMPLETION_PROTOCOL_v1.0_20260825.md.
Work ONLY on <WORKSTREAM_ID>.
Use the locked references listed there.
Do not edit frozen masters.
Do not invent executable grammar.
Write/return the result using the Standard Result Contract.
Report OBSERVED / PROVEN / NOT_PROVEN and all conflicts.
```

---

# 5. SAFETY / CONTINUITY

- Never delete historical artifacts.
- Never hard-code desired cognitive results.
- Never call declaration machine evidence.
- Never infer cognition from names/output.
- Preserve failures and unknowns.
- Keep SIGMA-Ψ first; host languages are reference/substrate/debug/external-interface layers.
- One worker = one bounded responsibility.
- A completed workstream should not be rerun unless new evidence changes its scope.

---

# 6. COMPLETION CONDITION

SIGMA-Ψ language may be proposed as `1.0 COMPLETE` only when:

- all mandatory workstreams are merged;
- mandatory `MISSING=0`;
- mandatory `CONFLICT=0` or explicitly version-resolved;
- core grammar/semantics have conformance tests;
- executable claims are supported by machine evidence;
- glyph/token senses are unambiguous within scope;
- human mappings do not redefine machine semantics;
- provenance is retained for every normalization.

This protocol coordinates windows through shared versioned artifacts, not through hidden cross-window memory.