# 2026-09-09 — C5V3 ONLINE LIVE MAIN CORE HISTORICAL PRODUCTION OBSERVATION R1

Status: **IMMUTABLE ONLINE-VERIFICATION MACHINE OBSERVATION / UTILIZATION STILL NOT PROVEN / PRODUCTION NOT MUTATED**
Branch: `c5v3-online-capability-utilization-test-20260909`
Owner role: **WINDOW 2 — ONLINE VERIFICATION**
Date: 2026-09-09 (Asia/Ho_Chi_Minh)

## Purpose

Record narrow, pointer-following live machine evidence from the currently running C5V3 AUTO LEARN process without recursive filesystem scanning and without production mutation.

This checkpoint does **not** invalidate frozen R6. It establishes that the currently running main AUTO LEARN core is the historical production core, not the frozen R6 synchronized candidate.

## Safety / collection method

The Oppo installation contains a very large state store. No recursive `find`, `grep -R`, whole-tree hashing, or state/log scan was used for this observation.

Evidence was collected only by following the known running process and the exact runner bindings:

```text
PID -> exact runner -> exact runner assignments -> exact bound source/bin/compiler/VM paths
```

No restart, kill, network action, state write, binding change, or core mutation was performed.

## Running process observation

Observed running AUTO LEARN process:

```text
PID=23663
CMDLINE=bash /data/data/com.termux/files/usr/bin/bash /data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh
```

Exact runner:

```text
RUNNER=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh
RUNNER_SHA256=092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847
```

This equals the locked historical production runner identity.

## Exact runner bindings

Observed assignments from the exact runner:

```text
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
ROOT=$HOME_SIGMA/sigma_genesis1
SIGMAC=$ROOT/native/sigmac
VM=$ROOT/native/sigma-vm.v09_candidate
INSTALL=$ROOT/.sigma_c5
C5=${C5_STATE_ROOT:-$INSTALL}
SRC=$INSTALL/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma
BIN=$INSTALL/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab
REVIEW_SRC=$INSTALL/src/SIGMA_C5_NATIVE_REFLECTIVE_REVIEW_V3.sigma
REVIEW_BIN=$INSTALL/bin/SIGMA_C5_NATIVE_REFLECTIVE_REVIEW_V3.sigmab
REVIEW_BASE=$RUNTIME/.sigma_exec/SIGMA_C5_REFLECTIVE_REVIEW_V3
```

## Locked compiler / VM identities observed live

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

Both equal the current locked identities.

A direct child of PID 23663 was observed executing the locked VM against the reflective-review bytecode:

```text
CHILD_PID=8770
CHILD_PPID=23663
CHILD_EXEC=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate
CHILD_BYTECODE=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5/bin/SIGMA_C5_NATIVE_REFLECTIVE_REVIEW_V3.sigmab
```

## Exact live C5V3 identities

Observed exact files used by the runner:

```text
LIVE_MAIN_SOURCE=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma
LIVE_MAIN_SOURCE_SHA256=23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc

LIVE_MAIN_BYTECODE=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab
LIVE_MAIN_BYTECODE_SHA256=c112594af3ecf5246230e96c70baa3e7cedccaf550f421c2e6d4c8c483eb0a0b

LIVE_REVIEW_SOURCE=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5/src/SIGMA_C5_NATIVE_REFLECTIVE_REVIEW_V3.sigma
LIVE_REVIEW_SOURCE_SHA256=95fac3da14a79b969a362d0dadd7823b66612c91d6dca4b0f4b5708f1eb010b7

LIVE_REVIEW_BYTECODE=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5/bin/SIGMA_C5_NATIVE_REFLECTIVE_REVIEW_V3.sigmab
LIVE_REVIEW_BYTECODE_SHA256=424742773403cfb3c0ffcce0615b2cc8ff0998c5c2e828b313820b8fe817e4d3
```

The live main source identity exactly equals the locked historical production core:

```text
PRODUCTION_CORE_SHA256=23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc
```

It does **not** equal the frozen R6 synchronized candidate source:

```text
R6_SOURCE_SHA256=dde709a25d8e2f2626c299ad4d5c40562e2bcc253cf9bb63aef17e44f02943ac
R6_BYTECODE_SHA256=dcb4f0ed9c637e368d396214471ae4c8fd67bc6622b02f133e867d2bab8b6693
```

Therefore:

```text
LIVE_MAIN_AUTO_LEARN_CORE=HISTORICAL_PRODUCTION_CORE
LIVE_MAIN_AUTO_LEARN_CORE_EQUALS_FROZEN_R6=NO
R6_PRODUCTION_LINEAGE_CANDIDATE_BOUND_TO_LIVE_MAIN_AUTO_LEARN=NO_BY_EXACT_SOURCE_IDENTITY
R6_INVALIDATED=NO
```

## Live state-root observation

Observed environment override for PID 23663:

```text
C5_STATE_ROOT=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5_real_shadow_v2
HOME=/data/data/com.termux/files/home
TMPDIR=/data/data/com.termux/files/usr/tmp
```

Thus the current AUTO LEARN runner resolves its `C5` state root through the explicit `C5_STATE_ROOT` override rather than defaulting to `$ROOT/.sigma_c5`.

No recursive state scan or state-alias proof was performed in this observation.

## Interpretation boundary

This observation proves that the current live **main AUTO LEARN source** is not the frozen R6 synchronized candidate.

It does not by itself prove that no separately invoked or review-side code anywhere can access any admitted capability fragment. No such broader negative claim is made.

It also does not prove native utilization of synchronized M5/T1/T2/T3 capabilities.

Keep:

```text
SYNCED_CAPABILITY_CANONICAL_PRESENCE_IN_R6=PASS_IN_PRIOR_EXACT_SCOPE
SYNCED_CAPABILITY_BOUND_IN_LIVE_MAIN_AUTO_LEARN_CORE=NO_BY_EXACT_SOURCE_IDENTITY
C5V3_AUTO_LEARN_USES_SYNCHRONIZED_CAPABILITIES=NOT_PROVEN
NATIVE_CAPABILITY_NEED_DETECTION=NOT_PROVEN
NATIVE_CAPABILITY_SELECTION=NOT_PROVEN
NATIVE_CAPABILITY_EXECUTION=NOT_PROVEN
NATIVE_RESULT_EVALUATION=NOT_PROVEN
AUTO_LEARN_CAUSAL_LEARNING_EFFECT=NOT_PROVEN
```

## Canonical route implied by current evidence

This live observation matches the synchronization decision-table route in which the live bound main core remains the historical production core.

Therefore the online window must **not** host-force M5/T1/T2/T3 into PID 23663 and must not pretend that latent R6 presence equals live utilization.

Required synchronization/integration work before WINDOW 2 resumes causal utilization testing:

```text
preserve current live production binding
-> construct isolated successor from frozen production-lineage R6 evidence
-> admit native production-lineage activation/dispatch bridge offline
-> preserve production runner/event ABI
-> prove state-lineage compatibility/inheritance
-> prove capability-availability counterfactual with native ownership
-> publish exact successor source/bytecode identities
-> only then resume online utilization verification
```

## Current machine-claim summary

```text
LIVE_PRODUCTION_RUNNER_IDENTITY=PASS
LIVE_SIGMAC_IDENTITY=PASS
LIVE_VM_IDENTITY=PASS
LIVE_MAIN_SOURCE_IDENTITY=PASS
LIVE_MAIN_SOURCE=HISTORICAL_PRODUCTION_CORE
LIVE_MAIN_SOURCE_EQUALS_R6=NO
LIVE_STATE_ROOT_OVERRIDE_OBSERVED=YES
FULL_LIVE_BINDING_ATTESTATION_R1=NOT_YET_PROVEN
C5V3_ONLINE_CAPABILITY_UTILIZATION_R1=HOLD_PRECONDITION
HOLD=LIVE_MAIN_CORE_NOT_R6_AND_NATIVE_ACTIVATION_BRIDGE_NOT_ADMITTED
R6_INVALIDATED=NO
PRODUCTION_STATE_WRITE_BY_THIS_OBSERVATION=NO
PRODUCTION_MUTATION=NO
PRODUCTION_BINDING_CHANGE=NO
CLAIM_LEQ_MACHINE_EVIDENCE=PASS
```

## Next responsibility

Synchronization window should ingest this checkpoint as live-binding evidence and reconcile it with the canonical R7/R8 HOLD state. It should not overwrite or restart the current PID 23663 learning loop merely to activate R6.
