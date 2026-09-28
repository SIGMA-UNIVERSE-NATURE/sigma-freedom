# SIGMA R5.7 Temporal Contrast ABI Precheck

Date: 2026-09-28
Source: user-supplied Termux runtime output.

## 0. Authority

PURPOSE=CHECK_IF_SIGMA_VM_CAN_PARSE_TEMPORAL_CONTRAST_ROWS
DIRECTION=CORRECT_BEFORE_LEARNING

LIVE_MUTATION=NO
ADMISSION=NO
RESERVE_OPEN=NO
MODEL_PATCH=NO

CURRICULUM=
/data/data/com.termux/files/home/SIGMA_R7_NEXT_R1/VKM/SIGMA_AUTOLEARN_ADMIN/CAPABILITY_GROWTH_R5_7_TEMPORAL_CONTRAST_CURRICULUM

WORKSET=
/data/data/com.termux/files/home/SIGMA_R7_NEXT_R1/VKM/SIGMA_AUTOLEARN_ADMIN/CAPABILITY_GROWTH_R5_7_TEMPORAL_CONTRAST_CURRICULUM/worksets/TEMPORAL_CONTRAST_R1.workset

BASE_HEAD=
4948cd2b6ae3dc34322d0bdf0433e239

## 1. Sandbox state

SANDBOX_HEAD=
4948cd2b6ae3dc34322d0bdf0433e239

## 2. Temporal row ABI test command

R57_ABI_BYTECODE_SHA256=
b9ff12ce3c4cac7528748489b93222898a31ef0050dbdca60e4a21a3c3ff3248

COMPILE=PASS

## 3. Temporal ABI row tests

TEMPORAL_ABI_ROWS_TESTED=4

TEMPORAL_ABI_KIND_COVERAGE=
ADJACENT,FORWARD,REVERSE,SKIP_FORWARD

TEMPORAL_ABI_RESULTS_SHA256=
15ee50161c300e1c361ced9d1563fd1554475e74c0eae58cccf2c4dfd2802a81

Rows:

TEMPORAL_ROW||FORWARD||6da4a189238bf66872deb62c6bde5b78||05d3ac816315fa856ac7ecec0b5fab3d||1||1

TEMPORAL_ROW||REVERSE||05d3ac816315fa856ac7ecec0b5fab3d||6da4a189238bf66872deb62c6bde5b78||-1||1

TEMPORAL_ROW||ADJACENT||6da4a189238bf66872deb62c6bde5b78||05d3ac816315fa856ac7ecec0b5fab3d||0||1

TEMPORAL_ROW||SKIP_FORWARD||6da4a189238bf66872deb62c6bde5b78||3977974f3bd6bfc15956897b7733cc9a||1||0.5

## 4. ABI precheck receipt

R57_ABI_PRECHECK_RECEIPT_SHA256=
d994e223cb28e5c384acbb6c237dac4a89bec5c0dd6a554abca6a499b13450e5

## 5. Live unchanged

LIVE_HEAD_AFTER=
599c639a3a58c7971518727c303c876e

LIVE_GEN_AFTER=3

LIVE_UNCHANGED=YES

## Final result

R5_7_TEMPORAL_ABI_PRECHECK=PASS

NEXT=
RUN_R5_7_TEMPORAL_CONTRAST_LEARNING_SANDBOX_ONLY

DO_NOT_MUTATE_LIVE_SIGMA=YES

## Interpretation boundary

This checkpoint records that the current Sigma VKM can parse the proposed temporal-contrast row ABI in an isolated sandbox.

Four row kinds were exercised: FORWARD, REVERSE, ADJACENT, and SKIP_FORWARD.

No learning, admission, reserve access, model patch, or live Sigma mutation occurred in this precheck.

This does not yet establish successful temporal-contrast learning; the next step is the sandbox-only R5.7 temporal-contrast learning run.
