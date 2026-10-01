# SIGMA C2.6C2C4C2B8 — Growth-to-Stop FAIL at Epoch 30 MEASURE / Progress Preserved

Date: 2026-10-01
Source: user-supplied Oppo/Termux runtime output.

## Resume start

B8_RESUME_MODE=STATE

B8_RESUME_REF=
300f8c09798d0ec27f0c245940f5186d

## Accelerator-backed growth progress

Observed accepted steps:

21 -> 22
- actual gain = 13600
- active vocab = 22784
- accelerator state = 7cb9f59160e71a5e43195dd532a41131

22 -> 23
- actual gain = 14025
- active vocab = 23808
- accelerator state = 46ba070c03fc8e0749cd526d49d71099

23 -> 24
- actual gain = 12339
- active vocab = 24832
- accelerator state = 1e876f915142d88c2eb70a280a25cf3e

24 -> 25
- actual gain = 12175
- active vocab = 25856
- accelerator state = 25b213f37bf35c6943ae9c2f30af23dc

25 -> 26
- actual gain = 11123
- active vocab = 26880
- accelerator state = 2d3dfe6150b88c1f6a0bd0297ced3e9e

26 -> 27
- actual gain = 10561
- active vocab = 27904
- accelerator state = 1076c12c3ab06ee46d530e8912c232f7

27 -> 28
- actual gain = 9405
- active vocab = 28928
- accelerator state = 34f0c4376bb53e425203119c0c64e467

28 -> 29
- actual gain = 9720
- active vocab = 29952
- accelerator state = 1bd416d8068fb28f25c0077a4b991254

29 -> 30
- actual gain = 9626
- active vocab = 30976
- accelerator state = 2d3b611d62688eb503531c425f4afc2d

All observed accepted steps:
ADOPTED=YES
PAIR_STORAGE=R21_BYTE_CAS_REUSED
STATUS=CONTINUE
TOKENIZER_DUPLICATE_IDS=0
TOKENIZER_DUPLICATE_PIECES=0
DUP_AUDIT_INCREMENTAL=PASS
TOKENIZER_ACCEL_PROMOTION=PASS

## Epoch 30 plan

PLAN=
4104de1a3eb51cf9009c103464a4d489

EPOCH=30
SELECTED=1024
NOMINAL_PAIR_SAVINGS=8907

ACTIVE_VOCAB_BEFORE=30976
ACTIVE_VOCAB_AFTER=32000

## Failure

At B8 iteration 155:

MODE=PLAN

SIGMA_C_VM_STEP_LIMIT=HIT

C2_6C2C4C2B8_RUN_GROWTH_TO_STOP=FAIL

REASON=
RBX_TOKENIZER_GROWTH_MEASURE_RC=9

B8_RESUMABLE_PROGRESS_PRESERVED=YES

LIVE_MUTATION=NO

CALLING_SHELL_STILL_ALIVE=YES

## Interpretation boundary

This checkpoint establishes that Tokenizer Accelerator V1 successfully removes PREPARE as the immediate scaling bottleneck across growth from epoch 21 through epoch 30.

The next bottleneck has moved to the MEASURE path.

Current blocker:
RBX_TOKENIZER_GROWTH_MEASURE step cost at epoch 30 / target active vocab 32000.

It is NOT currently:
- PREPARE restore/membership;
- accelerator promotion;
- duplicate protection;
- pair sealing;
- R21 byte-CAS reuse;
- growth acceptance policy;
- state-machine resumability.

Do not raise the production SIGMA_MAX_STEPS.
Do not discard resumable progress.
Do not remeasure completed epochs.

Recommended next work:
profile and split/accelerate the MEASURE path under the same principle:

MEASURE ONCE
PERSIST ONCE
VERIFY FRESH ONCE

This checkpoint does NOT establish growth-to-stop completion, tokenizer convergence, production tokenizer qualification, admission, or cutover.
