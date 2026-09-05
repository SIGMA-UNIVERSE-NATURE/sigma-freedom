# V2.11R.1 runner bounded-fixture setup failure

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: SIGMA_LIFE

## Status

`V211R1_REVISIT_EXECUTION_ARCHIVE_REENTRY_PREFLIGHT=FAIL`

This is a runner/test-fixture failure, not evidence of a native SIGMA logic failure.

## Runtime evidence before failure

The native V2.11R.1 engine successfully demonstrated:

- `ARCHIVE_FOR_NOW` hold with no revisit mutation;
- later committed `REVISIT` after archive re-entered work;
- fresh-VM archive-reentry completion;
- no lifecycle action -> `WAIT_FOR_LIFECYCLE`;
- lifecycle over-limit refusal;
- evidence over-limit refusal.

Host substitution remained disabled (`HOST_REVISIT_EXECUTION=NO`, `HOST_ARCHIVE_REENTRY_DECISION=NO`, `HOST_DOCUMENT_SELECTION=NO`, `HOST_SEGMENT_SELECTION=NO`, `HOST_LEARNING=NO`).

## Failing gate

The runner attempted to construct a 65-pipe generation-cursor fixture with:

```sh
printf '%0.s|' {1..65}
```

Termux `printf` returned:

```text
printf: %0.s: invalid conversion specification
```

Therefore the intended over-limit generation cursor was not created. The following native invocation correctly observed an ordinary empty generation cursor and proceeded with `EXECUTE_REVISIT`; it did not and should not have reported `GENERATION_CURSOR_LIMIT_EXCEEDED=1`.

## Repair rule

Do not modify the native V2.11R.1 source or weaken the admission criterion.

Repair only the runner fixture construction using a deterministic mechanical shell loop that appends exactly 65 `|` bytes. Apply the same repair to the segment-cursor boundedness fixture.

## Claim scope

- native V2.11R.1 admission remains `NOT_PROVEN`;
- generation-cursor bounded refusal remains `NOT_PROVEN` for this run;
- segment-cursor bounded refusal remains `NOT_PROVEN` for this run;
- already observed positive/runtime evidence above is preserved;
- semantic understanding remains `NOT_PROVEN`;
- bounded file I/O remains `NOT_PROVEN`;
- mid-append crash atomicity remains `NOT_PROVEN`.
