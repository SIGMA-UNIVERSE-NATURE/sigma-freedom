# 2026-09-09 — C5V3 LIVE BINDING ATTESTATION REQUEST R1

Status: **MANDATORY READ-ONLY PRE-CORE-WRITE GATE / PRODUCTION NOT BOUND BY THIS REQUEST**
Branch: `SIGMA_LIFE`
Owner role: **WINDOW 1 — SYNCHRONIZATION**
Date: 2026-09-09 (Asia/Ho_Chi_Minh)

## Governing canonical state

Read first:

1. `SIGMA_PROFESSOR/CHECKPOINTS/20260909_C5V3_SYNCHRONIZATION_BASELINE_R2_R6_FROZEN.md`
2. `SIGMA_PROFESSOR/CHECKPOINTS/20260909_C5V3_SYNCHRONIZATION_RECONCILIATION_R7_R8_ONLINE_HOLD_R1.md`
3. `C5_M5/RESUME_SYNC_2026-09-09_AFTER_T1_T2_T3.md` on the offline branch for the historical operator-report/live-attestation distinction.

Canonical state-layer identity:

```text
ONE_SIGMA=YES
SYSTEM=C5V3
CURRENT_SYNCHRONIZATION_BASELINE=R2
R6_PRODUCTION_LINEAGE_CANDIDATE=FROZEN_PASS
R6_SOURCE_SHA256=dde709a25d8e2f2626c299ad4d5c40562e2bcc253cf9bb63aef17e44f02943ac
R6_BYTECODE_SHA256=dcb4f0ed9c637e368d396214471ae4c8fd67bc6622b02f133e867d2bab8b6693
```

Latest consumed evidence:

```text
R7_OFFLINE_PRODUCTION_RUNNER_ABI_REGRESSION=PASS_IN_EXACT_TESTED_SCOPE
R8_M5_DISPATCH_STRUCTURAL_MAP=PASS
ONLINE_R1=HOLD_NATIVE_ACTIVATION_DISPATCH_BRIDGE_REQUIRED
```

The above is repository/canonical evidence. It is **not** proof of what the Oppo/Termux production runner currently binds.

## Why this gate is mandatory

The next architectural task is a native production-lineage activation/dispatch bridge. R8 proves that the production and M5 universes have disjoint equality-literal dispatch surfaces, while the 63 M5-only DEFs are reachable from the original M5 universe. Therefore bridge work is sensitive to the exact current live core/tool/state lineage.

A historical operator report says T1/T2/T3 were already synchronized by a previous window. Blindly grafting frozen R6 over a live core that already contains those definitions could duplicate capabilities or break the one-core lineage. Conversely, assuming canonical Baseline R2 is already the live binding could mutate the wrong runtime lineage.

Hence:

```text
CANONICAL_SYNCHRONIZATION_STATE_LAYER=R2_R6_FROZEN
LIVE_PRODUCTION_BINDING_IDENTITY=UNKNOWN_UNTIL_MACHINE_ATTESTATION
NEXT_CORE_WRITE=FORBIDDEN_UNTIL_ATTESTATION_RECONCILED
```

## Frozen known identities for comparison

```text
PRODUCTION_CORE_SHA256=23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc
PRODUCTION_RUNNER_SHA256=092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847
PRODUCTION_INGRESS_SHA256=22901ffce990a38163e2d2db2ef85a9e553c252159386baf136874daf9d7139c
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
R6_SOURCE_SHA256=dde709a25d8e2f2626c299ad4d5c40562e2bcc253cf9bb63aef17e44f02943ac
R6_BYTECODE_SHA256=dcb4f0ed9c637e368d396214471ae4c8fd67bc6622b02f133e867d2bab8b6693
```

Admitted capability-fragment identities carried by the probe for discovery only:

```text
T1_SOURCE_SHA256=d92bbd5bc36d798496fd04191e3d385e668cc4e5d1d37b59c25567b77a7091ca
T1_BYTECODE_SHA256=e43d983806936599eafb507872784b578a1cfa95a1f47425b730d52e2d2a9562
T2_SOURCE_SHA256=81bc18d6ce7c8c9a2cd54324360a948257074d60f5fa864d4951e8d5e4a3e135
T2_BYTECODE_SHA256=1c80fc66bf8e0326a7ce0fd21235b39c445f68841ee8442b53a20902174d8f5b
T3_SOURCE_SHA256=ed46788b55bea3e39c2c5c46bae28d2d9a077ff4cf70a08bc9dfdbb88fb33955
T3_BYTECODE_SHA256=1828dcd53d1f062a785329bab3c88e135d8f5e4779976c8c128933bee6f9801e
T1_T2_T3_COMBINED_SOURCE_SHA256=14f280342ba9e7925aecdcef47a0861aea56667c0bb28463fcfa4e75990e83c6
T1_T2_T3_COMBINED_BYTECODE_SHA256=79bdde5548548c570a7d33ab880f50f3c1bbf106a283a16ad9a6a2b5193180a4
```

These hashes do not imply those fragments are separately stored or currently bound live.

## Mechanical probe

Canonical probe path:

`C5_M5/RUN_C5V3_LIVE_BINDING_ATTESTATION_R1.sh`

Probe creation commit:

`3079b36f9ef16f71972419954ad7788e36dd3d0d`

Git object blob observed after creation:

`778e413b1ef2bc8ee9fd2ef29cffe9adaeb53cfa`

The Git blob identity is repository transport identity; it is not a SHA256 claim about machine execution.

Default historical installation root used only as a discovery starting point:

`$HOME/SIGMA/sigma_genesis1`

Historical R6 candidate root from machine evidence:

`$HOME/SIGMA/sigma_genesis1/.sigma_c5v3_sync/OFFLINE_PRODUCTION_LINEAGE_LATENT_GRAFT_R6_20260909T184734`

## Execution contract

Run the probe from a trusted local copy of the exact `SIGMA_LIFE` file. The probe accepts an optional installation root argument.

Canonical invocation when the historical root is still correct:

```bash
bash C5_M5/RUN_C5V3_LIVE_BINDING_ATTESTATION_R1.sh "$HOME/SIGMA/sigma_genesis1"
```

If the repository checkout is not located adjacent to the installation root, invoke the script by its actual local path and pass the installation root explicitly.

Do **not** redirect output into the production state/root. Return stdout directly to the Synchronization window for reconciliation.

## Hard execution locks

```text
READ_ONLY=YES
NETWORK_REQUIRED=NO
PRODUCTION_STATE_WRITE=NO
PRODUCTION_MUTATION=NO
PRODUCTION_RESTART=NO
PRODUCTION_BINDING_CHANGE=NO
PROCESS_KILL=NO
CHMOD=NO
COPY_OR_MOVE_RUNTIME_FILES=NO
PACKAGE_ACTION=NO
```

The probe performs read/hash/path/process/reference discovery only. It does not claim that a discovered file is bound merely because its hash matches a known identity.

## Required evidence to return

The stdout must preserve the probe labels for:

1. requested and resolved installation root;
2. known-identity targets;
3. exact historical R6 candidate-path presence and hashes;
4. state-root candidate paths, realpaths and stat identities;
5. relevant symlinks and resolved targets;
6. candidate code/runtime file path + SHA256 + known-identity classification;
7. static runner/supervisor/ingress reference-file discovery without dumping semantic contents or secrets;
8. active SIGMA-related process PIDs/PPIDs, executable identity and root-contained file/directory arguments when mechanically visible;
9. generic DEF duplicate scan for any exact known production/R6 source core found;
10. final collection status.

Expected terminal footer is intentionally non-promotional:

```text
LIVE_BINDING_DECISION=REQUIRES_SYNCHRONIZATION_RECONCILIATION
LIVE_BINDING_PASS_NOT_CLAIMED_BY_PROBE=YES
CORE_WRITE_ALLOWED_FROM_PROBE_OUTPUT_ALONE=NO
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

## Synchronization reconciliation after machine output

WINDOW 1 must classify the returned evidence into exactly one of these broad routes.

### A — exact frozen R6 is mechanically shown as the bound cognition core

Do not re-graft R6 or reinsert T1/T2/T3. Freeze the exact live references and design an isolated activation/dispatch bridge successor from that attested lineage.

### B — live production lineage already contains admitted T1/T2/T3 but is not exact R6

Compute the exact live-vs-R6 DEF/source/runtime delta. Preserve already-integrated admitted definitions and insert only missing production-lineage capability pieces. Duplicate logical tools/DEF names are forbidden.

### C — live bound core is the historical production core

Do not claim Baseline R2 is live. Construct only an isolated successor from frozen evidence; keep production binding unchanged until a later explicit cutover gate.

### D — live identity is divergent, ambiguous, multi-bound, or writer/state lineage cannot be resolved

```text
HOLD=LIVE_RUNTIME_IDENTITY_DIVERGENCE_OR_AMBIGUITY
```

Publish the discrepancy. Do not write core or activation bridge.

## PASS criterion for this gate

The probe itself never grants PASS. Synchrony may publish `LIVE_BINDING_ATTESTATION_R1=PASS_IN_EXACT_OBSERVED_SCOPE` only when machine output mechanically resolves, without contradiction:

- the bound cognition core identity;
- runner, ingress, sigmac and VM identities/references needed by the live path;
- production state-root lineage and relevant pointers;
- T1/T2/T3 binding/duplication status sufficiently to compute a non-duplicating live-vs-R6 delta;
- exactly one permitted cognitive writer on the attested path;
- no evidence that shadow/test state is aliased into production state lineage.

Missing or conflicting evidence is HOLD, never an inferred PASS.

## Current frontier

```text
CURRENT_SYNCHRONIZATION_BASELINE=R2
R6=FROZEN_PASS
R7=PASS_IN_EXACT_TESTED_SCOPE
R8=PASS_STRUCTURAL
ONLINE_R1=HOLD_NATIVE_ACTIVATION_DISPATCH_BRIDGE_REQUIRED
LIVE_BINDING_ATTESTATION_R1=AWAITING_MACHINE_OUTPUT
NEXT_CORE_WRITE=FORBIDDEN
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```
