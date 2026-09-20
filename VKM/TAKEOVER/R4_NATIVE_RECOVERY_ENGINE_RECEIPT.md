# SIGMA VKM R4 — Native Crash Recovery Engine Receipt

## Final R4 gate

SCHEMA=SIGMA_VKM_NATIVE_CRASH_CONSISTENCY_R4
RESULT=PASS
SIGMA_IDENTITY=ONE_SIGMA

CRASH_MATRIX=PASS
NATIVE_RECOVERY_ENGINE=PASS
PARTIAL_TRANSACTION_ROLLBACK=PASS
COMMITTED_TRANSACTION_PRESERVED=PASS
RECOVERY_IDEMPOTENCE=PASS
NO_COMMIT_REEXECUTION=YES

REAL_GENERATION=5
REAL_CANONICAL_MUTATION=NO

AIL_CRASH_RECOVERY_REQUIRED=NO
PRODUCTION_VM_MUTATION=NO
VKM_PRODUCTION_CUTOVER=NO

NEXT=R4_OWNERSHIP_TAKEOVER

## Recovery pass 1

All four disposable crash states returned RESULT=PASS and STATE_VALID=YES:

- complete: ACTION=NOOP_ALREADY_COMMITTED; generation 6 preserved.
- replay_canonical: ACTION=ROLLBACK_PARTIAL_TRANSACTION; restored generation 5.
- replay_canonical_generation: ACTION=ROLLBACK_PARTIAL_TRANSACTION; restored generation 5.
- replay_only: ACTION=ROLLBACK_TO_DURABLE_GENERATION; restored generation 5.

Committed state:
- canonical: bc8455afe2923d05eba6576f0ae0c7b10e6290628fbae86a35ee35b0ea00878d
- replay: ffb8d846540880f6f2669b39028a1f1aba187c984f927042c6c486a3009f4fb3

Recovered partial/pre-commit states:
- canonical: ffb8d846540880f6f2669b39028a1f1aba187c984f927042c6c486a3009f4fb3
- replay: 614d420b945eeac49b66312ca28871a2f3ffd644adf010eed4815ff00d24811e
- generation: 5

## Recovery pass 2 / idempotence

complete IDEMPOTENT=YES
replay_canonical IDEMPOTENT=YES
replay_canonical_generation IDEMPOTENT=YES
replay_only IDEMPOTENT=YES

RECOVERY_IDEMPOTENCE=PASS

## Real-state isolation

R4_REAL_STATE_UNTOUCHED=PASS
R4_REAL_STATE_MUTATION=NO
CURRENT_GENERATION=5

The recovery tests operated on disposable recovery targets. Real canonical, replay, generation and lineage identities remained unchanged.

## Evidence SHA-256

- sigma_recovery_r4.py: 5a11bc5f9cbc3d362e41538a085ebfa892d5b361172423b89687fcd9f966a9a8
- R4_RECOVERY.contract: 53d37e6f19814c58cdef34398eb390ab9fda83963fcdeac7365e69999c91a107
- R4_RECOVERY_ENGINE.receipt: f4a685cfd79abb2a1ac87ece8ff85943c3c127bb7b48c49557611f99189ca2a0
- canonical.memory: ffb8d846540880f6f2669b39028a1f1aba187c984f927042c6c486a3009f4fb3
- replay.memory: 614d420b945eeac49b66312ca28871a2f3ffd644adf010eed4815ff00d24811e
- generation.txt: f0b5c2c2211c8d67ed15e75e656c7862d086e9245420892a7de62cd9ec582a06
- lineage.memory: 9991207dd59e1f182baef33c7da5e99489a881e7e524cb3de08227e4d08a04c1
- sigma-vkm: 0791205449dc0d8ff982b9eae39d2f7b516e4eb46bbf69ab36808c9ae41cbe1c
- sigma-vm.v09_candidate: 029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

## Takeover boundary

The R4 native crash-consistency machine proof is complete and READY_FOR_R4_OWNERSHIP=YES. This receipt records the completed proof but leaves the explicit capability ownership transition to the R4 ownership checkpoint.

SIGMA_R4_NATIVE_CRASH_CONSISTENCY=PASS
READY_FOR_R4_OWNERSHIP=YES
TERMUX_SHELL_CONTINUES=YES
