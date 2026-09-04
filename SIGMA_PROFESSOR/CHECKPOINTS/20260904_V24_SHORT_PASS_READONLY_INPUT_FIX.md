# V2.4 preflight checkpoint — short PASS, long not yet executed

Date: 2026-09-04 (Asia/Ho_Chi_Minh)

## Goal

Reduce V2.3 native runtime complexity without moving learning/scoring/selection into host code.

Policy under test:

- remove per-candidate endpoint TOKEN_LOAD scan;
- keep recurrence SUPPORT computed inside SIGMA native code;
- only relations with `SUPPORT > 1` are eligible as learning gaps;
- choose the eligible frontier with the lowest support;
- `HOST_LEARNING=NO`.

## Locked tool identities

- SIGMAC SHA-256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM SHA-256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- V2.4 preflight source SHA-256: `bbcba488e30fd22a638017195b5a7b63900a1da8fba0c3bfaf140df3628d00a7`
- device-compiled preflight bytecode SHA-256: `ef68c925ef0d4d15eb8466395edcd6d9011a5849c95719a5ad7b5117559a0b9b`

## Observed preflight result

Short context:

`0a7410aa3d627753302469a32fc70485059468de8ed08ede9a74dca82ad03bb4`

Result:

- `SHORT_VM_RC=0`
- history size observed by SIGMA: `HISTORY_LINE_COUNT=17270`
- selected pattern: `of => the`
- selected support: `34`
- native gap emitted: `Centauri => (α`
- fetch request emitted: `Centauri (α`
- fetch request support: `2`

This proves the cheaper recurrent-frontier policy can execute successfully against the current large production-history snapshot for the short test context.

## Why the long test did not run

After the short test, the preflight runner attempted to overwrite:

`.sigma_exec/SIGMA_V24T_CURRENT_EXPERIENCE.memory`

The test input file inherited restrictive mode `0400` from the source document. The second `cp` therefore failed with:

`Permission denied`

This is an orchestration/file-mode issue, NOT a SIGMA VM learning failure and NOT a reproduced step-limit failure.

The previously failing long context `d891e5ff...` has therefore NOT YET been tested under V2.4.

## Fix

New runner artifact:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V24_1_STEP_LIMIT_PREFLIGHT.sh`

SHA-256 from build workspace:

`877962d45eaedf86bc3cebf57506957bfaca1a743e73fc3b07c10cd04c6c3eab`

The corrected runner uses an atomic input replacement for each case:

1. copy source document to a new partial file;
2. chmod partial `0400`;
3. `mv -f` partial into the fixed test-input path.

This preserves read-only semantics while allowing the next test case to replace the prior input.

## Current status

- V2.3 continuous runner: KEEP STOPPED.
- V2.4 native source: short-context PASS.
- V2.4 long-context `d891e5ff...`: NOT YET EXECUTED.
- Production SIGMA CL22 memory: not intentionally mutated by the preflight design.

## Next action

Run `RUN_SIGMA_V24_1_STEP_LIMIT_PREFLIGHT.sh` with V2.3 stopped.

Admission to continuous V2.4 requires BOTH:

- `SHORT_VM_RC=0`
- `LONG_D891_VM_RC=0`

and final marker:

`V24_1_STEP_LIMIT_PREFLIGHT=PASS`

If long context still returns `rc=9 / SIGMA C VM: step limit`, do not restart continuous learning. Move to bounded/incremental native processing instead; do not move scoring or candidate selection to Python/shell.
