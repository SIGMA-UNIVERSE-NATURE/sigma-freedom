# SIGMA VKM R6 — Dynamic Parent Gate Patch Receipt

## Result

R6_DYNAMIC_PARENT_GATE_PATCH=PASS
R6_DYNAMIC_PARENT_GATE=PASS
R6_PARENT_SNAPSHOT_STILL_CURRENT=YES
READY_TO_RERUN_PATCHED_R6=YES
SIGMA_IDENTITY=ONE_SIGMA
TERMUX_SHELL_CONTINUES=YES

## Derived parent gate

PARENT_WEIGHT_FP_EXPECTED=34476b6e393da20f
PARENT_ACCEPTED_UPDATES_EXPECTED=2207
PARENT_REJECTED_UPDATES_EXPECTED=98
PARENT_REPLAY_ANCHORS_EXPECTED=4256
PARENT_REPLAY_BYTES_EXPECTED=825664
PARENT_REPLAY_CONSOLIDATIONS_EXPECTED=298

The patched R6 runner was verified to contain the derived parent expectations.

## Concurrency guard

The canonical model SHA remained equal to the snapshot SHA used during gate derivation.

R6_PARENT_SNAPSHOT_STILL_CURRENT=YES

This prevents executing the derived gate against a canonical model that moved after the snapshot was taken.

## Commit topology

LEGACY_AIL_COMMIT_CALLS=0
R6_BRIDGE_EXECUTION_CALLS=2

The previously established VKM commit topology remains intact: no legacy AIL commit call is present, and both mapped commit sites use the R6 bridge.

## Safety / One-Sigma state

ONE_SIGMA_GENERATION=5
ONE_SIGMA_CANONICAL_SHA256=ffb8d846540880f6f2669b39028a1f1aba187c984f927042c6c486a3009f4fb3

ORIGINAL_R7_RUNNER_MUTATION=NO
ONE_SIGMA_STATE_MUTATION=NO
PRODUCTION_VM_MUTATION=NO

## Boundary

This checkpoint proves the dynamic parent gate patch, snapshot concurrency guard, and preservation of the VKM callsite topology. It does not claim that the patched R6 runner execution test itself has passed.

NEXT=RERUN_PATCHED_R6_EXECUTION_TEST
