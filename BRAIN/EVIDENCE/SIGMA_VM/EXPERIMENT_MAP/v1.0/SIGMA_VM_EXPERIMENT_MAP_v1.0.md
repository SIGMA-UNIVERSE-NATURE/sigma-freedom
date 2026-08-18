# SIGMA VM — EXPERIMENT MAP v1.0

**Map ID:** `SIGMA-VM-EXPERIMENT-MAP-20260818-001`  
**Mode:** `ONE_WINDOW_ONE_TASK / DEPENDENCY_GATED / EVIDENCE_ONLY`  
**Repository:** `SIGMA-UNIVERSE-NATURE/sigma-freedom`  
**Integration branch:** `agent/sigma-experiment-ledger-20260818`  
**Current frontier:** `SIGMA_NATIVE_FLOAT64_BITCAST_CAPABILITY_001`

## 1. Why this map exists

No window may “try things until something passes.” Every experiment must begin from a measured gap, one explicit hypothesis, one bounded mutation, an evaluator contract, and a stop condition.

```text
MEASURED GAP
→ HYPOTHESIS
→ ONE CANDIDATE
→ FREEZE SHA
→ INDEPENDENT EVALUATION
→ FULL REGRESSION
→ COLD BOOTSTRAP
→ CROSS-SUBSTRATE REPLAY
→ PASS / HOLD / REJECT
```

## 2. Immutable baseline

- Foundation V7 SHA-256: `fe513c20f4df9077e1d12acaa441dc90dceae566e70640b1b383ff185cf3ada1`
- Frozen ABI SHA-256: `c48c9883c6aedaa1ca7bfbc04b2ad05335040375bed942be73ae3ace9a5b8416`
- Self-host fixed point: `2ef3949b93260d64f99d5e407fc20b26aff0b240e972c7521927385d6584a667`
- Experiment Ledger v3 SHA-256: `349618e0c677b7d8c5e314cc083fc14df9e1209f0eb308d8b4e5439cdf567d5a`
- SIGMA-written VM proof: `PASS`
- Trusted-boundary reduction #1 (`math_floordiv` removed): `PASS`
- Measured custom trusted primitive count currently recorded: `5`
- `bytes_f64_le_at` removal: `HOLD`
- Full C-free native stack: `HOLD`

The exact names of all five remaining primitives are **not inferred**. Node E04 must measure and record them from the current source and binary.

## 3. Global rules

```text
ONE_WINDOW_ONE_TASK
ONE_MUTATING_OWNER_PER_CONTRACT
IMPLEMENTER_CANNOT_SELF_CERTIFY
CANDIDATE_SHA_PINNED_BEFORE_EVALUATION
CORPUS_FROZEN_BEFORE_EVALUATION
NO_FOUNDATION_MUTATION
NO_FROZEN_ABI_MUTATION
NO_PHASE2_REOPEN
NO_CANONICAL_512_PROMOTION
NO_TEST_SPECIFIC_HARDCODE
FAILURE_PRESERVED
PASS_REQUIRES_EXECUTION_EVIDENCE
```

## 4. Dependency graph

```text
CLOSED:
E00 Foundation V7
  ↓
E01 Frozen ABI
  ↓
E02 SIGMA-written VM proof
  ↓
E03 remove math_floordiv (6 → 5)

READY NOW, PARALLEL-SAFE:
E04 exact boundary inventory ─────┐
                                  ├→ E06 one FLOAT64 candidate
E05 freeze FLOAT64 corpus/oracle ─┘
                                      ↓
E07 freeze candidate + deterministic compile
                                      ↓
E08 independent bit-exact evaluation
                                      ↓
E09 complete VM regression
                                      ↓
E10 two-cycle cold bootstrap
                                      ↓
E11 cross-substrate replay
                                      ↓
E12 independent reduction verdict (5 → 4 or HOLD/REJECT)
                                      ↓
E13 select exactly one next measured primitive
```

Only **E04 and E05** may start now. E06 is blocked until both return SHA-pinned PASS handoffs.

## 5. Window ownership

### W00 — HAND TO HAND_ CỬA 2 / Integrator

Owns only:
- dependency map;
- ledger;
- conflict detection;
- integration receipts;
- next-window activation.

Must not implement or self-certify.

### W01 — Boundary Auditor

**One task:** E04, exact inventory of the five remaining custom trusted C primitives.

Read-only. Must reconcile current adapter source with compiled host binary and produce exact names, call sites, semantic categories, and bootstrap dependencies.

### W02 — FLOAT64 Corpus Curator

**One task:** E05, freeze public corpus, withheld-generator specification, and independent raw-bit oracle.

Must not edit the VM candidate or host adapter.

### W03 — FLOAT64 Implementer

**One task:** E06, implement exactly one candidate.

Primary hypothesis:

> Preserve raw 64-bit payload alongside the numeric view in SIGMA data structures. Untouched constants retain exact bits; numeric operations consume the numeric view.

Already rejected path:

> Numeric reconstruction alone. v13a reached 11/14 and lost three NaN payload/signaling patterns.

Forbidden shortcut:

> Add a target-specific C bitcast and still claim trusted-boundary reduction.

The implementer may not issue a PASS verdict.

### W04 — Candidate Freezer

**One task:** E07, pin source/bytecode/adapter/binary SHAs and prove deterministic compilation. No source patches.

### W05 — Independent FLOAT64 Evaluator

**One task:** E08, run public and withheld raw-bit corpora and prove `bytes_f64_le_at` absence from source and binary. No patches.

### W06 — Regression Runner

**One task:** E09:
- positive differential 11/11;
- malformed fail-closed 19/19;
- C malformed agreement 17/19 with the same two classified divergences;
- FLOORDIV stress 17/17;
- opcode/unary/binary/constant coverage.

No patches.

### W07 — Cold-Bootstrap Runner

**One task:** E10, run two actual cycles. Both must reproduce `2ef3949b93260d64f99d5e407fc20b26aff0b240e972c7521927385d6584a667`.

No patches and no stale output.

### W08 — Portability Runner

**One task:** E11, replay the frozen candidate on OPPO and an independent x86_64 substrate. Native executable hashes need not match across architectures; source, ABI, corpus, semantics and fixed point must match.

### W09 — Verdict Evaluator

**One task:** E12, issue `PASS_WITH_DEFINED_SCOPE`, `HOLD`, or `REJECT`. It cannot repair evidence.

### W10 — Next Primitive Selector

**One task:** E13, choose exactly one primitive from the measured remaining list and define one non-blind experiment. No implementation.

## 6. Current two-window launch

Open now:

```text
W01_BOUNDARY_AUDITOR
W02_F64_CORPUS_CURATOR
```

Do not open W03 yet.

W01 and W02 are parallel-safe because they own disjoint artifacts and neither may mutate the candidate.

## 7. Invalidation rules

Any of these invalidates downstream evidence:

- candidate source changes after E07 freeze;
- corpus changes without a version increment;
- candidate SHA differs from evaluator input;
- missing RC/stdout/stderr;
- Foundation or ABI SHA changes;
- a new trusted primitive replaces the removed primitive;
- evaluator patches the candidate;
- test-specific labels/hashes appear in implementation;
- cold bootstrap reuses stale generated output.

## 8. Verdict semantics

- `PASS`: all gates in the declared scope pass.
- `PASS_WITH_DEFINED_SCOPE`: capability proven, but larger claims remain excluded.
- `HOLD`: evidence incomplete, environment/resource block, or dependency unresolved.
- `FAIL`: executed behavior contradicts required semantics.
- `REJECT`: candidate design is disproven or violates the experiment contract.

A timeout is normally `HOLD`, not semantic `FAIL`, unless it violates an explicit bounded-performance contract.

## 9. Handoff schema

Every window returns:

```text
WINDOW_ID:
NODE_ID:
PARENT_CHECKPOINT:
INPUT_SHA256:
COMMANDS:
RETURN_CODES:
STDOUT:
STDERR:
OUTPUT_ARTIFACT_SHA256:
OBSERVED_FAILURE:
FAILURE_CLASSIFICATION:
VERDICT:
FORBIDDEN_MUTATIONS_CONFIRMED:
NEXT_DEPENDENCY_UNLOCKED:
```

The window stops after producing its handoff. It must not begin the next node.

## 10. Promotion boundary

```text
CANONICAL_MERGE = NONE
FOUNDATION_MERGE = NONE
PHASE2_REOPEN = NONE
512_PROMOTION = NONE
```

This map controls experimental work only. Capability promotion requires the independent verdict node and a separate authorized integration decision.
