# C5V3 R4 Native Learning Architecture R1

Status: source architecture in development; not runtime-admitted; not production-bound.

## Objective

Replace the legacy narrow C5 cognition path with a capability-native, evidence-seeking, restart-safe learning architecture while retaining only useful mechanical/trust contracts.

Canonical flow:

```text
native objective
-> native gap
-> native evidence/capability need
-> native request/query or capability arguments
-> mechanical execution/transport
-> provenance-bound raw result
-> native evaluation
-> claim/hypothesis + support/contrary/uncertainty
-> revision/conflict
-> bounded compact memory
-> restart/reuse
-> next native objective/action
```

## Authority boundary

Host may perform only mechanical substrate work: filesystem/process/network/hash/atomic commit/resource execution.

Host must not create or choose active semantic objects: objective, gap, query, source, claim, hypothesis, support/contrary stance, uncertainty interpretation, truth state, memory selection, summary, theme/value, or capability need.

A capability being present is not evidence that it is admitted, synchronized, used, or autonomously selected.

## Layering

### P0 trust/survival

Retain the R3 FIX1 trust-state principles:

- fresh invocation root;
- exact state-chain parent binding;
- canonical event receipt binding;
- staged readback before commit;
- positive final commit intent;
- no direct persistent-state mutation from cognition;
- host compare-and-swap/atomic commit only after native permission.

P0 is a trust boundary, not cognition.

### P1 native learning state

`C5_NATIVE_LEARNING_STATE_R1.sigma.inc`

Provides bounded pure representations and transforms for:

- `CLAIM` with epistemic class `OBSERVED | DERIVED | HYPOTHESIS | UNRESOLVED | CONTRADICTED`;
- `GAP` with kind `EVIDENCE | CONFLICT | CAPABILITY | MEMORY | STRUCTURE`;
- provenance-bound `EVIDENCE`;
- native `EVALUATION` stance `SUPPORT | CONTRARY | NEUTRAL`;
- exact source-distinct support/contrary accounting;
- mechanical evidence posture `UNRESOLVED | SUPPORTED_ONLY | CONTRARY_ONLY | CONTESTED`;
- bounded banks;
- explicit native-selected gap lookup;
- admitted capability lookup by a native-provided need family;
- bounded compact memory packaging.

Evidence posture is not general truth. The learning substrate does not convert lexical overlap or counts into broad semantics.

### P1 transition helpers

`C5_NATIVE_LEARNING_TRANSITIONS_R1.sigma.inc`

Constructs and validates:

- `OBJECTIVE`;
- `CLAIM`;
- `GAP`;
- `EVIDENCE`;
- `EVALUATION`;
- `REQUEST`;
- gap state changes;
- compact-memory claim/gap recall.

These helpers are pure and contain no direct filesystem or transport operations.

### P2 first semantic seed: admitted Gate-A cognition

The exact Gate-A scoped provisional epistemic truth parent remains a tested semantic dependency:

```text
SOURCE_SHA256=bf468c564451839d3be9b22243039fe71ceb87b766a165d996f4be055f7cbbf1
HISTORICAL_BYTECODE_SHA256=569411458b1bff9c0c9894fd95374a87db6e6e5c04030dc8e8900e1cb0d38ea2
```

Its admitted scope is narrow native relation discrimination, evidence request, source-consistency revision and provisional truth. It is not general truth or whole-work understanding.

R4 will use Gate-A as an evaluator seed, not as the architecture of all cognition.

Initial executable learning slice:

```text
relation-discrimination objective
-> Gate-A native gap signal
-> R4 GAP record
-> Gate-A native evidence request
-> R4 REQUEST record
-> mechanical T6 transport
-> provenance-bound EVIDENCE record
-> Gate-A native relation/source-consistency evaluation
-> R4 EVALUATION ledger
-> evidence posture + scoped provisional epistemic state
-> revised CLAIM
-> gap resolve/retain
-> compact memory
-> restart/reuse test
```

### P3 capability-native substrate

T1/T2/T3 exact admitted tool DEF bodies remain capability dependencies, not semantic authority.

Future T4-T11 may enter only from exact offline machine-admission handoff.

Native cognition provides `NEED_FAMILY`; registry selection may mechanically return only an admitted capability. The host must not infer the need family or choose a capability semantically.

## Memory model

R4 memory is not source text storage. It contains bounded selected native state:

```text
WORK_ID
REVISION
CLAIMS
GAPS
EVIDENCE_REFS
```

Full evidence bytes remain outside compact memory. Provenance references must permit later retrieval/revision when needed.

Compression PASS requires semantic-retention/revision tests after source removal; byte reduction alone is not learning evidence.

## Whole-work direction

The long-range model should evolve from single scoped relations toward a bounded relational work graph:

```text
entities / events / relations / hypotheses / gaps / evidence refs
-> cross-scope dependencies
-> causal-vs-order distinctions
-> competing interpretations
-> whole-work synthesis
-> bounded memory
```

No token adjacency, previous/next relation, English grammar table, synonym table, theme/value table, or host-produced summary may substitute for this model.

## Current compiler boundary

The locked compiler/VM are real and reproduce historical R0 and Gate-A bytecode exactly. Current R3 FIX1 nevertheless emits the valid 29-byte empty/generic `SIGMBC01` capsule and its entry is not compiler-visible under the tested composition.

This is a compiler-facing R3 source/composition defect, not a reason to stop R4 architecture work. R4 source development proceeds independently; runtime admission remains blocked until compiler-entry visibility is repaired and exact source->bytecode identity is established.

## Admission order

1. Static source governance: no legacy LEFT/RIGHT cognition, no direct persistent I/O in learning modules, bounded schema/arity.
2. Compiler visibility: nontrivial source-sensitive bytecode and malformed-entry rejection.
3. Pure learning-state unit tests.
4. Gate-A regression under R4 composition.
5. One complete native learning cycle with exact request/result provenance.
6. Restart/reuse from compact memory with original evidence bytes removed.
7. Multi-scope non-interference and revision.
8. Capability-selection utilization/counterfactual tests.
9. Shadow transaction runner + crash/CAS/replay tests.
10. Independent online autonomy verification.
11. Explicit production cutover only after promotion criteria pass.

## Claim boundary

Current R4 code proves only source architecture construction. It does not yet prove runtime learning, general semantics, whole-work understanding, multilingual transfer, or autonomous production behavior.

`CLAIM <= EVIDENCE` remains mandatory.
