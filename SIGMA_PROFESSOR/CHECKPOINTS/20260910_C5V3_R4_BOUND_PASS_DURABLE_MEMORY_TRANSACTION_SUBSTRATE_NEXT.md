# C5V3 — R4 bound-learning PASS; durable memory + transaction substrate next

Date: 2026-09-10 Asia/Ho_Chi_Minh
Branch: `SIGMA_LIFE`

## Machine PASS received

The corrected bound adapter + one-cycle kernel source gate passed:

```text
STATE_SHA256=83a43ed6e778775c4b0ea823fa1ab4179adfccbf8a0478c2a7e4a9f8cfd5af33
TRANSITIONS_SHA256=3273a9d6e09728882244e5428cac994d505f58b1e54b69c2fb009a6a714bb3e9
ADAPTER_R3_SHA256=223aeb84c4d4fcc8e1cbdbf62943a38382efa8250de72eb4df4ba3df79e5b02b
KERNEL_R2_SHA256=91d660902bc400ec967904d21aab3be876006777926dee55f7b8b2ec4f01e2f6
R4_BOUND_COMBINED_DEF_COUNT=66
MAX_DEF_ARITY=6
MULTILINE_DEF_SIGNATURE_COUNT=0
CONTRARY_EVIDENCE_MAPPING=PASS
CLAIM_EVIDENCE_SUBJECT_BINDING=PASS
STANCE_SOURCE_BINDING=PASS
GATEA_TRUTH_POSTURE_INTERNALIZATION=PASS
TRUTH_POSTURE_GUARD_PER_TRANSITION=PASS
NATIVE_CAPABILITY_AUTO_SELECTION=ABSENT
R4_BOUND_COMBINED_SHA256=2c3a4352e6ad0035b82774e274556b66fae0bffbd2cc664439c144d1f73584fe
R4_BOUND_STATIC_GOVERNANCE=PASS
R4_BOUND_ADAPTER_KERNEL_SOURCE_AUDIT=PASS
RUNTIME_ADMISSION=NO
PRODUCTION_MUTATION=NO
```

## New pre-runtime durability finding

The 66-DEF bound source is valid in its tested static scope, but runtime composition review found that the R4 R2 claim record did not retain the claim content and the R2 memory format did not retain evaluation SUPPORT/CONTRARY history.

That would be insufficient for the required source-removal + restart/reuse target: after deleting source text, a claim ID alone does not preserve what was learned, and evidence references alone do not preserve why the claim was supported or opposed.

This is not a retroactive failure of the 66-DEF gate. It is a newly identified dependency before runtime admission.

## Durable learning correction

Added:

```text
C5_M5/R4_NATIVE_LEARNING/C5_R4_DURABLE_LEARNING_MODEL_R1.sigma.inc
COMMIT=b334a1ff23d068551d46b1f114b8ad45afbf46e3
SOURCE_SHA256=514c52fcc2e8e1fc5ea64e78b664b7651c8c0ce20c2d463b5fe505c95f9becd2
DEF_COUNT=10
```

It introduces bounded durable claims containing claim content, compact memory with an evaluation bank, evaluation recall, and evidence-posture reconstruction after restart.

Added durable one-cycle kernel:

```text
C5_M5/R4_NATIVE_LEARNING/C5_R4_ONE_CYCLE_LEARNING_KERNEL_R3.sigma.inc
COMMIT=89019543f98b39cd34ea95535a14c77f050360ea
SOURCE_SHA256=db2a0454fc429d58b9617a40a6e4283f632b35df2c6190e6389820402e1035b1
DEF_COUNT=12
```

The kernel binds claim content exactly to the candidate input and packs evaluation history into native compact memory.

## Transaction trust substrate

Added:

```text
C5_M5/R4_NATIVE_LEARNING/C5_R4_P0_TRANSACTION_TRUST_R1.sigma.inc
COMMIT=ba42087f602baf274c6ed5c90ae3f7a92d647eba
SOURCE_SHA256=cad40e8ded7138d7e56c8cbb219eba5e43d10d78fc18e7f335073f048f1bad82
DEF_COUNT=14
```

This defines a 20-field exact R4 state schema and phases/events for native request materialization, evidence return, memory materialization, restart reuse, and later capability result handling. It remains mechanical trust only.

## Exact next source gate

```text
C5_M5/RUN_C5V3_R4_DURABLE_TRANSACTION_SUBSTRATE_SOURCE_AUDIT_R1.sh
COMMIT=27c617fcf363bb40bc453d1f19d962b7ca0fac4a
```

Expected composition:

```text
28 State R2
12 Transitions R2
16 Adapter R3
10 Durable model R1
12 Kernel R3
14 P0 transaction trust R1
= 92 DEF
```

After PASS, write/freeze the transaction-aware R4 main, then compose exact Gate-A pure donor and exact admitted T1/T2/T3 into the successor C5V3 source.

## Claim boundary

```text
R4_BOUND_66_STATIC_AUDIT=PASS
R4_DURABLE_TRANSACTION_SOURCE=WRITTEN
R4_DURABLE_TRANSACTION_STATIC_AUDIT=PENDING
R4_RUNTIME_LEARNING=NOT_ADMITTED
T1_T2_T3_SUCCESSOR_COMPOSITION=PENDING_NEXT_AFTER_TRANSACTION_MAIN
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
PRODUCTION_PROMOTION_ALLOWED=NO
```
