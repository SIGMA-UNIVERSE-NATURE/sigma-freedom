# SIGMA R57 Proposal/TX — PAGE_HASH Fault Checkpoint

Date: 2026-10-03
Source: user-supplied Oppo/Termux runtime output.

## Proposal

RBX_R57_PROPOSE_TX=PASS
RB57_TX_PROPOSAL_READY=YES

PARENT_MODEL=2be5bedf284e4c304547510063a32726
CHILD_MODEL=12cc5d5d11c7054d727c78284d00ca3f

PARENT_OPT=744330c0193d97100c0f6f452ba7b510
CHILD_OPT=6b219217402bfcf15d583f37645b9fcb

COUNT=4

LOSS_BEFORE_MEAN=5.4841378125112357
LOSS_AFTER_MEAN=5.4687910748283839

OPT_STEP=1

## TX proposal

PROPOSAL=59a5cb47672d80bd0cdb2924307ffd27
TXID=3bccae2e73d5ae807f69869d4fefad05
RECEIPT=4262d090265757d74ac5d9772e648859

MODEL_GENERATION=1
OPT_STEP=1

## Fault

RBX_R57_STATE:
VM_RC=25
INTEGRAL_FAULT=PAGE_HASH
SIGMA host: list_set index
RESULT_MISSING=YES

NEXT=CLASSIFY_R57_PROPOSE_WITH_RATE

R57_PROPOSAL_OUTPUTS_READ=YES
LIVE_MUTATION=NO
NO_EXIT=YES

## Boundary

This checkpoint establishes that the R57 proposal and transaction proposal were produced and show lower mean loss.

It does NOT establish successful R57 state readback/restore because RBX_R57_STATE failed with PAGE_HASH / RC25.

Do not rerun training or create a new proposal before classifying and fixing the state/readback PAGE_HASH fault.

LIVE_MUTATION=NO
ADMISSION=NO
CUTOVER=NO
