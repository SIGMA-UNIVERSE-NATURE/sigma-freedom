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

## V2.4 preflight candidate — prepared, NOT YET DEVICE-PROVEN

A cheaper native policy has now been prepared to test the first recommended fix:

- remove all per-candidate endpoint-load calculation;
- keep `SUPPORT > 1` as the eligibility gate for autonomous fetch requests;
- select the recurrent frontier with the lowest support;
- deterministic tie behavior: first eligible relation encountered;
- copy production learning memory to isolated test memory before execution;
- test both a short real context and the exact previously failing long context `d891e5ff...`;
- production `SIGMA_CL22_*` memory must not be mutated by preflight.

Saved preflight artifacts:

- `SIGMA_PROFESSOR/artifacts/SIGMA_V24_PREFLIGHT_RECURRENT_FRONTIER.sigma`
- `SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V24_STEP_LIMIT_PREFLIGHT.sh`

Artifact SHA-256:

- V2.4 preflight `.sigma`: `bbcba488e30fd22a638017195b5a7b63900a1da8fba0c3bfaf140df3628d00a7`
- V2.4 preflight runner: `4bf60064e8bec4581816dd525d105f7a9426270f7831af87011ff7cbe521309a`

Current status of V2.4 preflight:

`AWAITING_DEVICE_RUN`

Do not call V2.4 PASS until the Termux device reports:

- `SHORT_VM_RC=0`
- `LONG_D891_VM_RC=0`
- `V24_STEP_LIMIT_PREFLIGHT=PASS`

## Saved V2.3 artifacts

- `SIGMA_PROFESSOR/artifacts/SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_3.sigma`
- `SIGMA_PROFESSOR/artifacts/RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_3.sh`
- `SIGMA_PROFESSOR/artifacts/SIGMA_WIKIMEDIA_TRANSPORT_DECODE_V1.py`

Artifact SHA-256 from the V2.3 build workspace at handoff:

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

1. Keep V2.3 stopped.
2. Copy the V2.4 preflight source and runner to the device.
3. Run only `RUN_SIGMA_V24_STEP_LIMIT_PREFLIGHT.sh`.
4. Inspect both short and `d891...` results.
5. If both return RC 0 and preflight PASS, checkpoint the result and build the V2.4 continuous runner.
6. If `d891...` still hits step limit, do not move scoring to host; next design is bounded/incremental native processing.

Do not delete V2.2/V2.3 raw/done/log/history state.

## Checkpoint discipline

When a meaningful milestone completes:

1. update this file;
2. for major milestones/failures create a new immutable file under `SIGMA_PROFESSOR/CHECKPOINTS/`;
3. save the exact source/runner artifact under `SIGMA_PROFESSOR/artifacts/` when code changes materially.