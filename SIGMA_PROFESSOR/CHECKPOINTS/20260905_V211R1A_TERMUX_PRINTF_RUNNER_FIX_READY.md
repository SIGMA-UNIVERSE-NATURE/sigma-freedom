# V2.11R.1A Termux-safe runner fixture repair — source ready

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: SIGMA_LIFE

## Native source unchanged

`SIGMA_REVISIT_EXECUTION_ARCHIVE_REENTRY_V2_11R1.sigma`

SHA256:
`88568071e657cb94845d97d94237688ec62d88121f6ff90dc8cbc96cbe685d9e`

No native SIGMA logic was changed.

## Failure repaired

Prior runner attempted to create bounded cursor fixtures with `printf '%0.s|' {1..65}`. Termux printf rejected that format.

The repaired runner uses deterministic shell loops to append exactly 65 `|` bytes for both:

- generation-cursor over-limit fixture;
- segment-cursor over-limit fixture.

## Repaired runner

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V211R1A_REVISIT_EXECUTION_ARCHIVE_REENTRY_PREFLIGHT.sh`

SHA256:
`31005526c5ec1a4c33ec1759965b9810e19198fae08235dc1ca16d8c5c739907`

Static:

- `bash -n` RC = 0;
- bad `%0.s` format absent;
- two explicit 65-iteration bounded-fixture loops present;
- admission criteria unchanged.

## Runtime status

V2.11R.1 admission remains `NOT_PROVEN` until this repaired runner completes on the locked compiler/VM.

Required final gates still include generation-cursor and segment-cursor over-limit refusal plus all previously defined positive/replay/archive/re-entry/wait/immutability gates.
