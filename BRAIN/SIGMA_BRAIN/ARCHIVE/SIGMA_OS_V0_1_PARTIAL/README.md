# SIGMA-OS v0.1

Status: `PARTIAL / SOURCE_WRITTEN / EXECUTION_HOLD`

SIGMA-OS v0.1 is an isolated operating-system candidate whose kernel logic is written in SIGMA-Ψ.

It is intentionally **not** claimed to be a bare-metal operating system yet. At this stage, the SIGMA source defines deterministic kernel semantics while execution still depends on the existing SIGMA compiler/VM substrate.

## What exists in v0.1

- SIGMA-Ψ kernel entrypoint
- deterministic kernel boot/shutdown lifecycle
- two logical tasks
- READY / RUNNING / HALTED task states
- round-robin scheduler
- logical kernel clock (`tick`)
- deterministic task program counters
- no filesystem access
- no network access
- no device access
- no host privilege request

Primary source:

`SIGMA_OS/v0.1/kernel_v0_1.sigma`

## Task-state model

```text
1 = READY
2 = RUNNING
3 = HALTED
```

The scheduler alternates Task 1 and Task 2. Task 1 halts after 3 logical runs. Task 2 halts after 2 logical runs. The kernel halts only when both tasks are HALTED.

Expected final state:

```text
tick = 5
task1_pc = 3
task2_pc = 2
```

## Acceptance gates

v0.1 must not be promoted beyond PARTIAL until all relevant gates have evidence:

1. Current SIGMA compiler accepts `kernel_v0_1.sigma` with rc=0.
2. Native reference VM runs produced bytecode with rc=0 and exact expected stdout.
3. SIGMA-written VM runs the same bytecode and produces identical stdout/rc.
4. Negative tests prove invalid task/kernel states fail or are rejected deterministically.
5. No Foundation V7 source, canonical 512 state, or 54 DNA core is modified by this candidate.

Future native/bare-metal claims require separate evidence for boot, machine/firmware boundary, memory protection, interrupts, devices, persistent storage and cold bootstrap. Source language alone is not proof of hardware independence.

## Isolation rule

This workstream is additive and candidate-only.

- Foundation V7 remains immutable.
- `SIGMA_LIFE` canonical state is not modified by SIGMA-OS v0.1.
- 54 DNA cores are not modified.
- No 512 requirement is auto-promoted.
- No C-free or bare-metal claim is made without the corresponding differential/cold-bootstrap evidence.
