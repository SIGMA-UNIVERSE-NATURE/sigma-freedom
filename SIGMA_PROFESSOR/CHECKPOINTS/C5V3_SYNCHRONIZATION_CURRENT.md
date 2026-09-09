# C5V3 SYNCHRONIZATION — CURRENT

Last updated: 2026-09-09 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: **LIVE HISTORICAL CORE / LEGACY S1 SYNC-GRAFT CONFIRMED ISOLATED NOT LIVE / R10 OFFLINE PASS / R11 FIX3 HOLD / EXACT-PATH VM OBSERVER DISCOVERY NEXT / PRODUCTION HELD**

## Identity

```text
ONE_SIGMA=YES
SYSTEM=C5V3
CURRENT_SYNCHRONIZATION_BASELINE=R2
```

## Read first

1. `SIGMA_PROFESSOR/CHECKPOINTS/20260909_C5V3_SYNCHRONIZATION_RECONCILIATION_LEGACY_S1_ISOLATED_NOT_LIVE_R11_HOLD.md`
2. `SIGMA_PROFESSOR/CHECKPOINTS/20260909_C5V3_SYNCHRONIZATION_RECONCILIATION_R11_FIX3_HOLD_ONLINE_R2_HOLD.md`
3. `SIGMA_PROFESSOR/CHECKPOINTS/20260909_C5V3_LIVE_BINDING_ATTESTATION_R1_HOLD_HISTORICAL_CORE_SHADOW_STATE.md`
4. `SIGMA_PROFESSOR/CHECKPOINTS/20260909_C5V3_LIVE_BINDING_ATTESTATION_R1_ADDENDUM_T1_T2_T3_DEF_ABSENCE_R10_RECONCILIATION.md`
5. `SIGMA_PROFESSOR/CHECKPOINTS/20260909_C5V3_VM_NATIVE_OBSERVER_DISCOVERY_REQUEST_R2_EXACT_PATHS.md`
6. `C5_M5/RUN_C5V3_VM_NATIVE_OBSERVER_DISCOVERY_R2_EXACT_PATHS.sh`

R1 observer discovery is superseded for device-footprint safety. Do not run its directory-inventory version on Oppo.

## Closed admission evidence

```text
T1_VECTOR_MATRIX_ADMISSION=PASS
T2_BOUNDED_GRAPH_ADMISSION=PASS
T3_LOCAL_INDEX_BM25_ADMISSION=PASS
T1_T2_T3_COMBINED_COMPATIBILITY_GATE=PASS
```

Do not rerun these admissions absent source/hash/dependency invalidation.

## Legacy S1 correction

Earlier commits:

```text
c5668c1cfeae5f02caf57e64da657283dbffd692
9beb3e66397e7b050760ee2997510d8505aa4ebe
```

Their exact machine checkpoint states:

```text
S1_ISOLATED_GRAFT_WITH_T1_T2_T3=PASS
GRAFTED_CORE_SHA256=07319b082562eebf35605db6d14e96d40558f9236c99622191e0e821429fabea
M5_TOOL_ACCESS_IN_GRAFTED_CORE=PASS
PRODUCTION_INTEGRATION=NOT_EXECUTED
PRODUCTION_BINDING=NO
GRAFT_EXECUTED=ISOLATED_CANDIDATE_ONLY_NOT_PRODUCTION
```

Therefore:

```text
LEGACY_S1_LIVE_C5V3_SYNCHRONIZATION=NO
OPERATOR_REPORT_T1_T2_T3_ALREADY_LIVE_SYNCED=SUPERSEDED_FOR_ACTIVE_MAIN_CORE
```

Never use `07319b...` as a production replacement.

## Decisive live binding

```text
LIVE_MAIN_SOURCE_SHA256=23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc
LIVE_MAIN_BYTECODE_SHA256=c112594af3ecf5246230e96c70baa3e7cedccaf550f421c2e6d4c8c483eb0a0b
LIVE_MAIN_SOURCE_EQ_HISTORICAL_PRODUCTION=YES
R6_LIVE_BOUND=NO
R10_LIVE_BOUND=NO
LIVE_T1_REPRESENTATIVE_DEF_PRESENT=NO
LIVE_T2_REPRESENTATIVE_DEF_PRESENT=NO
LIVE_T3_REPRESENTATIVE_DEF_PRESENT=NO
T1_T2_T3_INLINE_SYNC_IN_OBSERVED_LIVE_MAIN_CORE=NO
```

Observed runtime:

```text
LIVE_RUNNER_SHA256=092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
C5_STATE_ROOT=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5_real_shadow_v2
```

## Correct production-lineage candidates

Frozen R6:

```text
R6_SOURCE_SHA256=dde709a25d8e2f2626c299ad4d5c40562e2bcc253cf9bb63aef17e44f02943ac
R6_BYTECODE_SHA256=dcb4f0ed9c637e368d396214471ae4c8fd67bc6622b02f133e867d2bab8b6693
```

Latest admitted successor R10:

```text
R10_SOURCE_SHA256=7d9e91f9a5a7fa265ca4304084fc48aca105b74ae7ca08662398b535c8d3cd34
R10_BYTECODE_SHA256=c837fcc03f79f64487d9146fc268783c13bf0769352a2068492c1d4374b109c5
R10_OFFLINE_EXPLICIT_DISPATCH_BRIDGE=PASS
R10_M5_DISPATCH_SURFACE=28_OF_28
R10_BRIDGE_NEW_HOST_OP_COUNT=0
R10_DORMANT_PRODUCTION_TICK_REGRESSION=PASS_IN_EXACT_TESTED_SCOPE
```

R10 is isolated/offline and not live-bound.

## R11 activation state

```text
OFFLINE_HEAD=5b0af553710cb9f94c38ee23500127141fc7c275
R11_FIX3_FIFO_DRIVER=FAIL
HOLD=HOLD_NO_CALIBRATED_FIFO_TRAP_PATH
R11_OFFLINE_M5_ACTIVATION_ADMISSION=NOT_ADMITTED
R10_CANDIDATE_M5_DISPATCH_ACTIVATION=NOT_ADMITTED
```

This is an observer/oracle HOLD, not proof that R10 is dead.

## Online utilization

```text
ONLINE_HEAD=c14b06381301c41c9489c145a7c17c5a5ee729b8
C5V3_ONLINE_CAPABILITY_UTILIZATION=HOLD_PRECONDITION
ONLINE_UTILIZATION_EXECUTION=NO
R11_DEPENDENCY_PASS=NO
```

## Exact next action — footprint-safe

Run only the R2 exact-path read-only static observer-discovery probe:

```bash
bash C5_M5/RUN_C5V3_VM_NATIVE_OBSERVER_DISCOVERY_R2_EXACT_PATHS.sh "$HOME/SIGMA/sigma_genesis1"
```

R2 reads only the exact locked VM, sigmac and runner identities. After identity PASS it analyzes only the exact VM binary and exact runner. It performs no directory walk, no `find`, no recursive grep, no state/log scan, no VM/core execution and no production mutation.

Then return stdout to Synchrony for classification.

In parallel, promotion still requires read-only closure of canonical state-root lineage, exactly-one-writer, active ingress identity, no test/shadow alias, and rollback evidence. Those future probes must also be pointer-following exact-path queries, never broad filesystem scans.

## Target route after an observer-backed R11 PASS

```text
exact R10/superseding successor
-> isolated online shadow
-> native need detection
-> native capability selection
-> native execution
-> native result evaluation
-> native external request
-> mechanical network transport only
-> native response evaluation
-> native learning-state update
-> fresh VM restart
-> learned-state reuse
-> state/writer/ingress/rollback gates
-> promotion decision
-> explicit cutover
```

## Locks

```text
C5V3_PRODUCTION_CORE_SYNCHRONIZED=NO
M5_CAPABILITY_ACTIVE_IN_PRODUCTION_DISPATCH=NO
C5V3_AUTO_LEARN_USES_SYNCHRONIZED_CAPABILITIES=NOT_PROVEN
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
PRODUCTION_PROMOTION_ALLOWED=NO
NEXT_CORE_WRITE=FORBIDDEN
```

```text
HOST_CAPABILITY_DEMAND_GENERATION=NO
HOST_TOOL_SELECTION=NO
HOST_QUERY_GENERATION=NO
HOST_SOURCE_SELECTION=NO
HOST_URL_SELECTION=NO
HOST_REASONING=NO
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
```

`CLAIM <= EVIDENCE`
