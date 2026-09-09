# C5V3 WINDOW ROLE REALIGNMENT — CAPABILITY ARCHITECTURE / SYNCHRONIZATION vs ONLINE VERIFICATION

Date: 2026-09-09 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: **CANONICAL OWNERSHIP REALIGNMENT**

## Identity

```text
ONE_SIGMA=YES
SYSTEM=C5V3
```

## Window 1 — Capability Architecture + Core Integration / Synchronization

This window owns:

- long-range capability architecture for T0-T11;
- design and preparation of new capability packs after the currently admitted T1/T2/T3 slices;
- source/bytecode identity discipline and capability composition rules;
- production-lineage successor construction;
- core rewrite/integration when required by the architecture;
- exact synchronization of admitted capability payloads into the C5V3 successor lineage;
- shadow-runner/binding design and synchronization-state reconciliation;
- state/writer/ingress/rollback compatibility gates required for promotion;
- canonical synchronization checkpoints and current handoff state.

This window must preserve:

```text
HOST_REASONING=NO
HOST_LEARNING=NO
HOST_TOOL_SELECTION=NO
HOST_QUERY_GENERATION=NO
HOST_SOURCE_SELECTION=NO
HOST_URL_SELECTION=NO
DO_NOT_LOAD_RESULTS=YES
LOAD_CAPABILITIES=YES
```

It may design/build/integrate capability code, but it must not convert design authority into an unsupported admission claim.

## Independent admission / machine evidence

Capability admission must remain machine-evidence based. A capability is not considered admitted merely because this window designed or integrated it.

Required pattern:

```text
capability design/build
-> exact source/bytecode freeze
-> independent machine test/admission evidence
-> synchronization/integration into successor lineage
-> activation/shadow verification
```

## Window 2 — Online Capability Utilization Verification

The online-verification window owns only verification that an already synchronized/admitted successor can actually:

```text
native need detection
-> native capability selection
-> native capability execution
-> native result evaluation
-> native external request when needed
-> mechanical network transport
-> native response evaluation
-> native learning-state update
-> fresh restart
-> learned-state reuse
```

It must not:

- redesign the core;
- silently add capabilities;
- host-force capability demand or tool choice;
- generate query/source/URL on SIGMA's behalf;
- promote or bind production.

## Current synchronization frontier

At this role realignment:

```text
T1_VECTOR_MATRIX_ADMISSION=PASS
T2_BOUNDED_GRAPH_ADMISSION=PASS
T3_LOCAL_INDEX_BM25_ADMISSION=PASS
T1_T2_T3_COMBINED_COMPATIBILITY_GATE=PASS

R10_SUCCESSOR_STAGE=PASS
R10_SHADOW_RUNNER_BINDING=PASS_MATERIALIZED_NOT_EXECUTED
R11_ACTIVATION_ADMISSION=HOLD
C5V3_PRODUCTION_CORE_SYNCHRONIZED=NO
PRODUCTION_BINDING=NO
```

The next synchronization work remains closure of bounded catalog/shared-root/network behavior before shadow execution.

## Capability roadmap ownership

After the current synchronization lane is stable, this window owns preparation of the next capability families, with each family admitted only in its exact tested scope:

```text
T4 text / syntax / codecs
T5 filesystem + durable state
T6 transport
T7 scheduler / resource controls
T8 process / IPC / isolation
T9 integrity / identity / provenance
T10 archive / document containers
T11 observability / replay
```

T7/T9/T11 may also provide cross-cutting minimum substrate before their full-tier completion.

## Governance

```text
WRITE_CORE_OR_CAPABILITY != ADMIT_CAPABILITY
ADMIT_CAPABILITY != LIVE_BIND_CAPABILITY
LIVE_BIND_CAPABILITY != ONLINE_AUTONOMY_PASS
```

Each transition requires its own evidence.

`CLAIM <= EVIDENCE`
