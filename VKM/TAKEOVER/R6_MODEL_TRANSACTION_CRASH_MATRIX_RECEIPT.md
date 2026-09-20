# SIGMA VKM R6 — Model Transaction Crash Matrix Receipt

SCHEMA=SIGMA_R6_MODEL_TRANSACTION_CRASH_MATRIX
RESULT=PASS
SIGMA_IDENTITY=ONE_SIGMA

PARENT_MODEL_SHA256=e6a74ece7ceddf757e2b909cf0a7e3062d16d95f2557ade74dc9e4b14ad4e8e7
CANDIDATE_MODEL_SHA256=bf58d4a035106b3f564ac8c012fc4c2cc1daa5eccd96099feb263d638fd8ec82

PRE_TRANSACTION_STATE=PROVEN
PREPARED_STATE=PROVEN
ROLLBACK_WRITTEN_STATE=PROVEN
PARTIAL_MODEL_WRITE_STATE=PROVEN
COMMITTED_STATE=PROVEN

COMMITTED_STATE_REQUIRES_JOURNAL_COMMIT=YES
PARTIAL_NEW_MODEL_REQUIRES_ROLLBACK=YES
ROLLBACK_PARENT_PRESERVED=YES
NO_AMBIGUOUS_COMMIT=YES

REAL_MODEL_MUTATION=NO
ONE_SIGMA_STATE_MUTATION=NO
LEGACY_AIL_COMMIT_USED=NO

## Crash-state classification

- untouched=PRE_TRANSACTION
- prepared=PRE_COMMIT_RECOVERABLE
- rollback_written=PRE_COMMIT_RECOVERABLE
- model_written=PARTIAL_REQUIRES_ROLLBACK
- committed=COMMITTED

The model_written state contains the candidate as model.ail and the parent as model.ail.rollback, but lacks STATE=COMMITTED in the transaction journal. It is therefore explicitly not accepted as committed.

The committed state requires:
- model.ail = candidate SHA;
- model.ail.rollback = parent SHA;
- transaction journal contains STATE=COMMITTED.

## Final gate

R6_MODEL_TRANSACTION_CRASH_MATRIX=PASS
NO_HALF_MODEL_COMMIT_ACCEPTED=YES
ROLLBACK_PARENT_AVAILABLE=YES
READY_FOR_R6_NATIVE_MODEL_RECOVERY_ENGINE=YES

## Safety

REAL_MODEL_SHA256=e6a74ece7ceddf757e2b909cf0a7e3062d16d95f2557ade74dc9e4b14ad4e8e7
ONE_SIGMA_GENERATION=5
ONE_SIGMA_CANONICAL_SHA256=ffb8d846540880f6f2669b39028a1f1aba187c984f927042c6c486a3009f4fb3

REAL_MODEL_MUTATION=NO
ONE_SIGMA_STATE_MUTATION=NO
R7_R8_RESTARTED=NO
PRODUCTION_VM_MUTATION=NO

## Evidence SHA-256

- real model.ail: e6a74ece7ceddf757e2b909cf0a7e3062d16d95f2557ade74dc9e4b14ad4e8e7
- fresh.candidate.ail: bf58d4a035106b3f564ac8c012fc4c2cc1daa5eccd96099feb263d638fd8ec82
- R6_MODEL_CRASH_MATRIX.receipt: e03521859d4b1f977ff3627139aaace7e6a2956a44b0aec6d2cca063cc235673
- model_written/model.ail: bf58d4a035106b3f564ac8c012fc4c2cc1daa5eccd96099feb263d638fd8ec82
- model_written/model.ail.rollback: e6a74ece7ceddf757e2b909cf0a7e3062d16d95f2557ade74dc9e4b14ad4e8e7
- committed/model.ail: bf58d4a035106b3f564ac8c012fc4c2cc1daa5eccd96099feb263d638fd8ec82
- committed/model.ail.rollback: e6a74ece7ceddf757e2b909cf0a7e3062d16d95f2557ade74dc9e4b14ad4e8e7

## Boundary

This checkpoint proves crash-state classification and the no-ambiguous-commit rule for native model transactions. Recovery execution and idempotence across these states remain to be proven by the native model recovery engine.

NEXT=R6_NATIVE_MODEL_RECOVERY_ENGINE
TERMUX_SHELL_CONTINUES=YES
