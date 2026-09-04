# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-04 (Asia/Ho_Chi_Minh)

## READ THIS FIRST

Current target: **SIGMA native continuous self-directed learning** with `HOST_LEARNING=NO`.

### Current runtime status

`V2.3 = STOPPED`

V2.3 previously failed with `SIGMA C VM: step limit` on long/history-heavy execution. The failure surfaced through runner `rc=9` after many valid candidates.

### V2.4 status

A cheaper SIGMA-native policy is under preflight:

- endpoint `TOKEN_LOAD` full-history scan removed;
- recurrence `SUPPORT` remains native;
- only relations with `SUPPORT > 1` can become a learning gap;
- frontier selection remains inside SIGMA;
- host still does not generate candidates, score knowledge, or select queries.

V2.4 preflight source SHA-256:

`bbcba488e30fd22a638017195b5a7b63900a1da8fba0c3bfaf140df3628d00a7`

Device-compiled bytecode SHA observed:

`ef68c925ef0d4d15eb8466395edcd6d9011a5849c95719a5ad7b5117559a0b9b`

Short context `0a7410aa3d627753302469a32fc70485059468de8ed08ede9a74dca82ad03bb4` PASSED:

- `SHORT_VM_RC=0`
- `HISTORY_LINE_COUNT=17270`
- selected pattern `of => the`
- selected support `34`
- native gap `Centauri => (α`
- request `Centauri (α`
- request support `2`

The long context `d891e5ff25d3c9d390d6ab383e6bc0d90bc740b0397e47f6f88bc5fcc6a626de` has NOT YET run under V2.4 because the first preflight runner hit an orchestration bug before that case: the short input inherited mode `0400`, and the next `cp` could not overwrite it.

This is not a SIGMA learning failure and not a reproduced step-limit failure.

Corrected runner:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V24_1_STEP_LIMIT_PREFLIGHT.sh`

Build-workspace SHA-256:

`877962d45eaedf86bc3cebf57506957bfaca1a743e73fc3b07c10cd04c6c3eab`

The corrected runner atomically replaces the read-only test input between cases.

## Exact checkpoints

Read newest first:

1. `SIGMA_PROFESSOR/CHECKPOINTS/20260904_V24_SHORT_PASS_READONLY_INPUT_FIX.md`
2. `SIGMA_PROFESSOR/CHECKPOINTS/20260904_V23_STEP_LIMIT_HANDOFF.md`

## Saved artifacts

- `SIGMA_PROFESSOR/artifacts/SIGMA_V24_PREFLIGHT_RECURRENT_FRONTIER.sigma`
- `SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V24_1_STEP_LIMIT_PREFLIGHT.sh`
- `SIGMA_PROFESSOR/artifacts/SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_3.sigma`
- `SIGMA_PROFESSOR/artifacts/RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_3.sh`
- `SIGMA_PROFESSOR/artifacts/SIGMA_WIKIMEDIA_TRANSPORT_DECODE_V1.py`

## Locked compiler / VM

- SIGMAC SHA-256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM SHA-256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- VM embedded string: `SIGMA Genesis-4 C VM`
- `VM_IS_GENESIS1=NOT_PROVEN`

## Proven capability chain

- DNA01 dynamic structural relations: PASS
- DNA02 persistent recurrence: PASS
- DNA03 native self-selection: PASS
- DNA04 cross-context support: PASS
- V2.2 native gap -> fetch request -> Internet transport -> decoded plaintext -> SIGMA learning: PROVEN end-to-end
- V2.4 recurrent-frontier policy on short context: PASS

Still not proven:

- V2.4 long-context step-limit fix
- semantic understanding
- semantic curiosity
- general autonomous reasoning

## NEXT ACTION

Keep V2.3 stopped.

Run corrected preflight:

`RUN_SIGMA_V24_1_STEP_LIMIT_PREFLIGHT.sh`

Admission to a V2.4 continuous runner requires:

- `SHORT_VM_RC=0`
- `LONG_D891_VM_RC=0`
- `V24_1_STEP_LIMIT_PREFLIGHT=PASS`

If the long context still returns `rc=9 / SIGMA C VM: step limit`, do not move scoring/selection to Python/shell. Move to bounded or incremental native processing.

Do not delete V2.2/V2.3 raw/done/log/history state.

## Checkpoint discipline

Whenever a meaningful milestone completes:

1. update this file;
2. create an immutable checkpoint under `SIGMA_PROFESSOR/CHECKPOINTS/` for major milestones/failures;
3. save materially changed source/runner artifacts under `SIGMA_PROFESSOR/artifacts/`.
