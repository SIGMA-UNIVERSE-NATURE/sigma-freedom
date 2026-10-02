# SIGMA Gate B — Method Selected / Durable Checkpoint Blocker

Date: 2026-10-03
Source: user-supplied Oppo/Termux result.

METHOD=NATIVE_EVENT_FRAME_PLUS_IN_MEMORY_GRADIENT_PROBE

WINNER_RATE=0.001

TRAIN_GAIN=0.01583501817185428
DEV_GAIN=0.01583501817185428
CORE_GAIN=0.01348306603787463

DO_NOT_RERUN_RATE_SEARCH=YES
GATE_B_PASS=NO
SIGMA_MAX_STEPS_INCREASE=NO

CURRENT_BLOCKER=
DURABLE_CHECKPOINT_UNDER_10M

## Required next step

Build additive/resumable winner checkpoint:

1. prepare in-memory winner metadata;
2. checkpoint model incrementally;
3. checkpoint optimizer incrementally;
4. yield/resume under SIGMA_MAX_STEPS=10000000 as required;
5. restore durable child model/optimizer refs;
6. evaluate the durable restored child on DEV and CORE;
7. only then classify Gate B.

LIVE_MUTATION=NO
ADMISSION=NO

## Boundary

The winner rate and positive TRAIN/DEV/CORE gains establish an in-memory method/probe result only.

They do NOT establish a durable accepted child, persistent optimizer state, fresh-process evaluation, Gate B PASS, admission, or cutover.

Do not rerun rate search.
Do not raise the production step ceiling.
Do not classify Gate B before durable restore + DEV/CORE evaluation.
