# C5V3 R10 SUCCESSOR SYNCHRONIZATION STAGE REQUEST R1

Date: 2026-09-09 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: **ACTIVE SYNCHRONIZATION STAGING REQUEST / ISOLATED SUCCESSOR WRITE ALLOWED / LIVE PRODUCTION WRITE FORBIDDEN**

## Purpose

Move synchronization work forward without repeating closed T1/T2/T3 admissions and without overwriting the currently running historical C5V3 core.

The current live main core is still the historical production source, while the exact admitted production-lineage successor is R10.

This request authorizes staging the exact frozen R10 payload into an isolated C5V3-style successor tree under `.sigma_c5v3_sync`.

It does **not** authorize production binding, production state import, restart of the live process, cutover, or live core replacement.

## Why this is the correct synchronization step

Closed machine evidence already proves:

```text
T1_VECTOR_MATRIX_ADMISSION=PASS
T2_BOUNDED_GRAPH_ADMISSION=PASS
T3_LOCAL_INDEX_BM25_ADMISSION=PASS
T1_T2_T3_COMBINED_COMPATIBILITY_GATE=PASS
```

Legacy S1 `sync-graft` was isolated M5-candidate work only:

```text
PRODUCTION_BINDING=NO
GRAFT_EXECUTED=ISOLATED_CANDIDATE_ONLY_NOT_PRODUCTION
```

Current live attestation proves:

```text
LIVE_MAIN_SOURCE_SHA256=23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc
LIVE_MAIN_SOURCE_EQ_HISTORICAL_PRODUCTION=YES
T1_T2_T3_INLINE_SYNC_IN_OBSERVED_LIVE_MAIN_CORE=NO
R10_LIVE_BOUND=NO
```

Therefore the correct path is not to rerun admissions and not to resurrect the standalone M5 graft. It is to stage the exact production-lineage R10 successor.

## Exact R10 identities

```text
R10_SOURCE_SHA256=7d9e91f9a5a7fa265ca4304084fc48aca105b74ae7ca08662398b535c8d3cd34
R10_BYTECODE_SHA256=c837fcc03f79f64487d9146fc268783c13bf0769352a2068492c1d4374b109c5
R10_OFFLINE_EXPLICIT_DISPATCH_BRIDGE=PASS
R10_M5_DISPATCH_SURFACE=28_OF_28
R10_BRIDGE_NEW_HOST_OP_COUNT=0
R10_DORMANT_PRODUCTION_TICK_REGRESSION=PASS_IN_EXACT_TESTED_SCOPE
```

R10 contains the exact production-lineage capability payload:

```text
historical production C5V3 parent
+ 63 exact M5-only DEF
+ admitted T1/T2/T3
+ preserved production universe/event contract
+ explicit native M5 dispatch bridge
```

R10 activation remains unadmitted because R11 is currently HOLD on observer/oracle limitations.

## Canonical staging script

```text
C5_M5/RUN_C5V3_R10_SUCCESSOR_STAGE_R1.sh
```

Invocation:

```bash
bash C5_M5/RUN_C5V3_R10_SUCCESSOR_STAGE_R1.sh "$HOME/SIGMA/sigma_genesis1"
```

If the script is obtained from a separate checkout, invoke the script by its exact checkout path and pass the actual SIGMA installation root as the argument.

## Exact write boundary

The script may write only under:

```text
$HOME/SIGMA/sigma_genesis1/.sigma_c5v3_sync/C5V3_R10_SUCCESSOR_STAGE_R1
```

It must not write to:

```text
$HOME/SIGMA/sigma_genesis1/.sigma_c5
$HOME/SIGMA/sigma_genesis1/.sigma_c5_real_shadow_v2
production state roots
native/sigmac
native/sigma-vm.v09_candidate
```

## Staging result required

Expected success classification:

```text
SUCCESSOR_STAGE=PASS
C5V3_SUCCESSOR_CAPABILITY_PAYLOAD_STAGED=YES
T1_T2_T3_PRESENT_IN_STAGED_SUCCESSOR=YES
M5_DISPATCH_BRIDGE_IDENTITY=INHERITED_EXACT_R10
LIVE_CORE_UNCHANGED=YES
LIVE_RUNNER_UNCHANGED=YES
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

This means the synchronization payload has been materially staged into a C5V3 successor tree. It does not yet mean the successor is runnable under the full production loop or that native activation has been admitted.

## Next gate after staging PASS

After the exact staging output is reconciled:

```text
R10 successor stage PASS
-> exact shadow-runner/binding design using the production runner contract
-> R11 native activation observation/admission against exact R10
-> isolated online-shadow utilization
-> native need/selection/execution/evaluation
-> native external-request sovereignty
-> native learning update
-> fresh restart + learned-state reuse
-> state-lineage / exactly-one-writer / ingress / rollback closure
-> promotion decision
-> explicit cutover
```

The production runner currently binds the live `.sigma_c5` install path, so it must not be blindly copied and interpreted as a runnable shadow binding. Shadow runner/binding is a separate exact gate.

## Locks

```text
R2_T1_T2_T3_ADMISSIONS=INHERITED_NOT_RERUN
LEGACY_07319B_PRODUCTION_REPLACEMENT=FORBIDDEN
R10_LIVE_BOUND=NO
R11_ACTIVATION_ADMISSION=HOLD
PRODUCTION_CORE_WRITE=NO
PRODUCTION_STATE_WRITE=NO
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
PRODUCTION_PROMOTION_ALLOWED=NO
```

`CLAIM <= EVIDENCE`
