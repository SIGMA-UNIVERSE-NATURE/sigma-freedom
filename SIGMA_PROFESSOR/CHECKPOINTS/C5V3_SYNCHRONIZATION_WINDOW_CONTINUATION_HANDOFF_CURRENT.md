# C5V3 SYNCHRONIZATION WINDOW — CONTINUATION HANDOFF CURRENT

Date: 2026-09-09 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: **CANONICAL HANDOFF / SYNCHRONIZATION AUTHORITY**

## Purpose

This file tells any future synchronization window exactly where to continue without reconstructing state from chat history.

The system identity remains:

```text
ONE_SIGMA=YES
SYSTEM=C5V3
```

Do not create a second SIGMA identity or replace the production C5V3 universe with the standalone M5 universe.

## Current canonical synchronization baseline

Read first:

`SIGMA_PROFESSOR/CHECKPOINTS/20260909_C5V3_SYNCHRONIZATION_BASELINE_R2_R6_FROZEN.md`

Baseline identity:

```text
C5V3_SYNCHRONIZATION_BASELINE=R2
BASELINE_STATUS=FROZEN_NON_PRODUCTION
R6_SOURCE_SHA256=dde709a25d8e2f2626c299ad4d5c40562e2bcc253cf9bb63aef17e44f02943ac
R6_BYTECODE_SHA256=dcb4f0ed9c637e368d396214471ae4c8fd67bc6622b02f133e867d2bab8b6693
R6_CANDIDATE_DEF_COUNT=156
R6_M5_ONLY_DEF_INSERTED=63
R6_ADMITTED_TOOL_DEF_COUNT=82
```

Canonical R6 checkpoint:

`SIGMA_PROFESSOR/CHECKPOINTS/20260909_C5V3_R6_OFFLINE_PRODUCTION_LINEAGE_LATENT_GRAFT_PASS.md`

Authoritative offline-test handoff source:

```text
BRANCH=c5v3-r5-r6-sync-handoff-20260909
HEAD=d8b3a6277db3e64bea8694548658de9f7a60bb6e
CHECKPOINT=C5_M5/CHECKPOINT_2026-09-09_1847_GATE_B_R5_R6_PRODUCTION_LINEAGE_HANDOFF.md
```

## What is already synchronized into Baseline R2

Only capability state / exact identities / admission receipts are synchronized. Test answers and test-learned state are not.

```text
DO_NOT_LOAD_RESULTS=YES
LOAD_CAPABILITIES=YES
TEST_KNOWLEDGE_IMPORTED=NO
PRODUCTION_KNOWLEDGE_IMPORTED=NO
```

Synchronized admitted substrate:

```text
T0_SUBSTRATE=PASS_INHERITED
T1_VECTOR_MATRIX=ADMITTED
T2_BOUNDED_GRAPH_TRAVERSAL=ADMITTED
T3_LOCAL_INDEX_BM25=ADMITTED
T1_T2_T3_COMBINED_COMPATIBILITY=PASS
M5_CAPABILITY_LIBRARY_PRESENT_IN_R6=YES
S2_ABI_RESOLUTION=PASS
SHADOW_MECHANICAL_WIRING=PASS
```

Exact T1/T2/T3 identities are frozen in:

`SIGMA_PROFESSOR/CHECKPOINTS/20260909_M5_T1_T2_T3_R2_CURRENT_STANDARD_ADMISSION_PASS.md`

Do not rerun these admissions merely for synchronization unless source/hash/dependency evidence changes.

## What is NOT synchronized / NOT proven yet

```text
C5V3_PRODUCTION_CORE_SYNCHRONIZED=NO
M5_CAPABILITY_ACTIVE_IN_PRODUCTION_DISPATCH=NO
TOOL_SELECTION_AUTONOMY=NOT_PROVEN
C5V3_AUTO_LEARN_USES_SYNCHRONIZED_CAPABILITIES=NOT_PROVEN
ONLINE_SYNC_STARTED=NO
LIVE_NETWORK_SYNC=NO
PRODUCTION_STATE_WRITE=NO
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

R6 proves latent capability presence in the exact production lineage. It does not prove utilization.

## Canonical architecture

```text
production C5V3 core lineage
+ exact M5 capability delta
+ admitted T1/T2/T3 capability libraries
+ explicit native activation/dispatch integration
```

Forbidden:

```text
standalone M5 core -> replace production C5V3 core
```

Historical M5+tools grafted core `07319b082562eebf35605db6d14e96d40558f9236c99622191e0e821429fabea` is internal M5 compatibility evidence only, not the production synchronization target.

## Window ownership split

### Synchronization window

Owns:

- canonical C5V3 synchronization baseline;
- reconciliation of machine PASS/FAIL checkpoints from other windows;
- exact capability registry / provenance / frozen identities;
- deciding whether evidence is sufficient to advance synchronization baseline;
- preparing integration gates that preserve production lineage.

Must not:

- invent PASS from partial output;
- import test answers/test cognition;
- silently bind production;
- override newer failure evidence from test windows.

### Online verification window

Read:

`SIGMA_PROFESSOR/CHECKPOINTS/20260909_C5V3_ONLINE_CAPABILITY_UTILIZATION_VERIFICATION_REQUEST_R1.md`

Its purpose is to prove whether C5V3 can actually use synchronized capabilities in an isolated online shadow.

Required causal chain:

```text
native need detection
-> native capability selection
-> native capability execution
-> native result evaluation
-> native learning-state update
-> fresh-VM restart
-> learned-state reuse
```

Network may run only after a native SIGMA request and only in isolated shadow.

The online window does not bind/promote production.

### Offline knowledge/capability window

Continues new knowledge/capability experiments and ABI/regression tests.

It must publish immutable checkpoints if:

- R6 is invalidated;
- R6 is superseded by a new candidate;
- a new capability is admitted;
- a dependency/source/hash changes materially.

It does not perform production synchronization.

## Evidence the synchronization window should consume next

Priority order:

1. Newer offline R7 production-runner ABI regression checkpoint if published.
2. Online utilization verification checkpoint from the online verification window.
3. Any superseding failure/candidate checkpoint from offline testing.

On every new evidence item:

```text
verify exact branch/commit/path
-> classify PASS/FAIL/superseded scope
-> preserve old evidence immutable
-> update canonical living handoff
-> advance baseline only if the new required causal gate passes
```

## Baseline R2 -> R3 promotion rule

Do not create Baseline R3 merely because R6 compiles or because capability functions are present.

Baseline R3 may state AUTO LEARN uses synchronized capabilities only after machine evidence proves, in exact tested scope:

```text
SYNCED_CAPABILITY_IDENTITIES_VISIBLE=PASS
NATIVE_CAPABILITY_NEED_DETECTION=PASS
NATIVE_CAPABILITY_SELECTION=PASS
NATIVE_CAPABILITY_EXECUTION=PASS
NATIVE_RESULT_EVALUATION=PASS
CAPABILITY_AVAILABILITY_COUNTERFACTUAL=PASS
NATIVE_LEARNING_UPDATE_APPLIED=YES
FRESH_VM_RESTART=PASS
LEARNED_STATE_REUSED_AFTER_RESTART=PASS
HOST_TOOL_SELECTION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PRODUCTION_BINDING=NO
```

If online evidence passes only capability execution but not learning/restart reuse, record that narrower result and do not widen the baseline claim.

## Production cutover remains separate

Even a Baseline R3 utilization PASS is not automatically a production cutover.

Production promotion still requires separately proven:

```text
production-runner ABI compatibility
state-lineage compatibility/inheritance
explicit native activation/dispatch integration
production non-mutation evidence during shadow
restart/recovery/rollback
bounded soak/stability
explicit user-visible cutover decision
```

Keep until then:

```text
PRODUCTION_BINDING=NO
PRODUCTION_PROMOTION_ALLOWED=NO
```

## Current synchronization frontier

```text
C5V3_SYNCHRONIZATION_BASELINE=R2_R6_FROZEN
R5=CLOSED_PASS
R6=CLOSED_PASS
NEXT_OFFLINE_EVIDENCE=R7_ABI_REGRESSION_WHEN_PUBLISHED
NEXT_ONLINE_EVIDENCE=C5V3_ONLINE_CAPABILITY_UTILIZATION_VERIFICATION_R1
NEXT_SYNC_ACTION=RECONCILE_NEW_MACHINE_EVIDENCE_AND_ADVANCE_ONLY_EXACT_PROVEN_SCOPE
```

This file is the continuation pointer for future synchronization windows.
