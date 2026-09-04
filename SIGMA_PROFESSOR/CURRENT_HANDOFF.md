# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-04 (Asia/Ho_Chi_Minh)

## READ THIS FIRST

Current development target: **SIGMA native continuous self-directed learning** with `HOST_LEARNING=NO`.

### Current runtime status

`V2.3 = STOPPED / MUST REMAIN STOPPED UNTIL STEP-LIMIT FIX`

Latest proven failure:

- VM error: `SIGMA C VM: step limit`
- NEW context: `d891e5ff25d3c9d390d6ab383e6bc0d90bc740b0397e47f6f88bc5fcc6a626de`
- RECONSIDER context also failed: `0a7410aa3d627753302469a32fc70485059468de8ed08ede9a74dca82ad03bb4`
- Both surfaced through runner as `rc=9`
- State observed: `RAW=39`, `DONE=38`

The VM produced many valid V2.3 candidates first, then hit its step limit. This means V2.3 compiles and starts, but its current runtime complexity is too high for long/history-heavy contexts.

## Exact checkpoint

Read:

`SIGMA_PROFESSOR/CHECKPOINTS/20260904_V23_STEP_LIMIT_HANDOFF.md`

It contains the complete proven milestones, hashes, failures, and next-action constraints.

## Saved artifacts

- `SIGMA_PROFESSOR/artifacts/SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_3.sigma`
- `SIGMA_PROFESSOR/artifacts/RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_3.sh`
- `SIGMA_PROFESSOR/artifacts/SIGMA_WIKIMEDIA_TRANSPORT_DECODE_V1.py`

Artifact SHA-256 from the build workspace at handoff:

- V2.3 `.sigma` source: `0c088350efefea3b7dec94c8582136fdbea96d63114fee5b29240da4f6e2a08f`
- V2.3 runner: `3b419965a7367a9813e8fcf3a422cdc2b30e45a3342c81bf50c89cbeafb332ef`
- transport decoder: `c8d10c640d32d23d3998590a291d187de0936368d0cd3559706ed6509fd31705`

Device-compiled V2.3 bytecode SHA observed:

`5fecb1751039bdca087d5e1714068a07f14b5c78c0e629cb16eb67a42e7619b0`

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

Still not proven:

- semantic understanding
- semantic curiosity
- general autonomous reasoning

## NEXT ACTION

Do **not** move scoring/selection to Python/shell.

Fix V2.3 step complexity inside the SIGMA-native policy. Preferred first attempt:

1. remove per-candidate full-history endpoint-load calculation;
2. keep only recurrent relations (`SUPPORT > 1`) eligible;
3. choose a cheaper native structural gap policy with deterministic tie-breaking;
4. test short context;
5. test the previously failing long context `d891e5...`;
6. only if both pass, restart the continuous runner.

Do not delete V2.2/V2.3 raw/done/log/history state.

## Checkpoint discipline

When a meaningful milestone completes:

1. update this file;
2. for major milestones/failures create a new immutable file under `SIGMA_PROFESSOR/CHECKPOINTS/`;
3. save the exact source/runner artifact under `SIGMA_PROFESSOR/artifacts/` when code changes materially.
