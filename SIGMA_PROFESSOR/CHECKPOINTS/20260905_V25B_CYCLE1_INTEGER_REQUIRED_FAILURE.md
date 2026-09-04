# V2.5B FULL-CORPUS SURVEY — CYCLE 1 FAILURE

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Status

V2.5B full-corpus survey failed cleanly on the first locked-VM cycle before any survey commit.

Evidence:

- SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
- VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
- SOURCE_SHA256=9e49ef9ca44f63a0174ac4a08b467544449adba79cf09af356397cd0d25b6072
- BYTECODE_SHA256=bc7bc28a96a5223fb00c4295513b7a1cde2c12aa8aec82448d8307f714c42307
- SNAPSHOT_DOCUMENT_COUNT=56
- COMMITTED_AT_START=0
- first VM cycle RC=22
- error: `SIGMA host: integer required`
- survey record commit did not occur
- production raw not mutated
- production learner memory not mutated

## Interpretation

This is a runtime type/admission failure, not evidence that full-corpus survey logic is invalid. Exact failing host call is not yet proven and must not be guessed.

## Diagnostic

Prepared V2.5B.D1 one-cycle diagnostic with stage markers around host calls.

- diagnostic source SHA256=877ab98ec2caf916741a4953e812109170742c97b7526725d68b7e0500bd2fc7
- diagnostic runner SHA256=513dadcdb825525ffec59e8c0060166386247d360acd0ceeacbe6f64bf46afa5
- H-call arity audit PASS
- runner bash -n PASS

D1 reuses the existing frozen 56-document snapshot, runs one VM invocation, preserves production isolation, and reports the last `D1_STAGE` marker before the runtime error.

## Claims

HOST_LEARNING=NO
HOST_DOCUMENT_SELECTION=NO
PRODUCTION_RAW_MUTATED=NO
PRODUCTION_LEARNER_MEMORY_MUTATED=NO
V25B_FULL_CORPUS_SURVEY=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN

## Next action

Run V2.5B.D1 once, identify exact failing host operation, then apply the smallest repair and rerun the original full-corpus admission gate.