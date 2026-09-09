# C5V3 COGNITIVE KERNEL SUCCESSOR R1 — DRAFT CREATED

Date: 2026-09-09 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: **SUCCESSOR CORE SOURCE WRITTEN / NOT COMPILED / NOT ADMITTED / NOT PRODUCTION-BOUND**

## Trigger

Exact live-source audit classified the historical production core as unsuitable as the long-range T0-T11 cognitive kernel. The historical core remains mechanically meaningful, but its center is a monolithic event state machine plus a narrow adjacent-token co-occurrence learner.

Audit checkpoint:

```text
SIGMA_PROFESSOR/CHECKPOINTS/20260909_C5V3_LIVE_CORE_ARCHITECTURE_AUDIT_R1_REWRITE_REQUIRED.md
```

## New draft source

```text
C5_M5/SIGMA_C5V3_COGNITIVE_KERNEL_SUCCESSOR_R1_DRAFT.sigma
```

Git blob identity at creation:

```text
GIT_BLOB_SHA=188f1df348291758147abd438004b35a88372639
LOCAL_CONSTRUCTION_SHA256=af70010cdb8ba78fcaf9291b23babdcd23c9dce21936dee8816d6d4a049ba39d
SOURCE_LINES=1106
DEF_COUNT=17
```

The local SHA256 is recorded from the exact construction buffer used to create the GitHub source. Machine-side SHA256 must be independently recomputed before any compile/admission claim.

## Architectural changes introduced

The successor keeps the historical event/persistence handshake as a compatibility surface while adding a capability-native control plane:

```text
NATIVE_TASK_READY
-> task_need()
-> need_family()
-> capability registry scan
-> native admitted-family selection
-> EXECUTE_CAPABILITY request
-> CAPABILITY_RESULT_READY
-> exact pending-ID match
-> result-status/kind evaluation
-> persistence / next need
```

New native capability families are represented explicitly as:

```text
T0 PRIMITIVE
T1 NUMERIC
T2 STRUCTURE
T3 RETRIEVAL
T4 TEXT_SYNTAX
T5 DURABLE_STATE
T6 TRANSPORT
T7 RESOURCE
T8 PROCESS_ISOLATION
T9 INTEGRITY_PROVENANCE
T10 CONTAINER
T11 OBSERVE_REPLAY
```

The draft does not claim those families are admitted. Registry selection requires `STATE=ADMITTED` supplied mechanically from exact machine-admission state.

## Compatibility behavior

The historical adjacent-token co-occurrence learner is retained only as a compatibility fallback:

```text
T4 admitted -> raw segment goes to native-selected T4 capability first
T4 unavailable -> compatibility analyzer may run

candidate evidence need
-> native-selected T3 when admitted
-> historical LOOKUP_EVIDENCE fallback when unavailable
```

This allows migration without pretending the old heuristic is the intended final cognition model.

## Host sovereignty locks

The draft explicitly preserves:

```text
HOST_CAPABILITY_DEMAND_GENERATION=NO
HOST_TOOL_SELECTION=NO
HOST_QUERY_GENERATION=NO
HOST_SOURCE_SELECTION=NO
HOST_URL_SELECTION=NO
HOST_REASONING=NO
HOST_LEARNING=NO
```

The host/runtime is allowed only to execute/transport the exact capability/request selected by the native kernel.

## R10 disposition

```text
R10_SUCCESSOR_STAGE=PASS
R10_SHADOW_RUNNER_BINDING=PASS_MATERIALIZED_NOT_EXECUTED
R10_LONG_RANGE_PRODUCTION_TARGET=NO_AFTER_CORE_ARCHITECTURE_AUDIT
R10_ROLE=TRANSITION_REFERENCE_AND_CAPABILITY_PROVENANCE
```

R10 remains valuable evidence for exact production-lineage coexistence and the already-admitted M5/T1/T2/T3 payload. Its capability provenance should be reused when constructing the new kernel successor. It should not be blindly promoted merely because its staging path is further advanced.

## Required next gates

```text
R1 source freeze on Oppo
-> sigmac compile
-> bytecode freeze
-> host-op audit
-> historical event compatibility regression
-> native task/need/registry selection tests
-> capability-result identity/counterfactual tests
-> integrate exact admitted M5/T1/T2/T3 libraries
-> later integrate offline-admitted T4-T11 packs
-> isolated shadow runner for new kernel
-> machine admission
-> online independent utilization verification
-> promotion/cutover decision
```

## Locks

```text
DRAFT_SOURCE_CREATED=YES
SIGMAC_COMPILE=NOT_EXECUTED
BYTECODE_IDENTITY=NOT_ESTABLISHED
CORE_ADMISSION=NO
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
PRODUCTION_PROMOTION_ALLOWED=NO
```

`CLAIM <= EVIDENCE`
