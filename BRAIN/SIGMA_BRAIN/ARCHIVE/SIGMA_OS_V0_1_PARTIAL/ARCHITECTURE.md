# SIGMA-OS Architecture — candidate v0.1

## Two distinct targets

SIGMA-OS development separates two claims that must never be conflated.

### A. SIGMA-OS logical kernel

Operating-system semantics are expressed in SIGMA-Ψ and executed on the current SIGMA substrate.

This is the current target.

### B. SIGMA-OS native system

SIGMA-Ψ controls a machine from an independently verified boot boundary with sufficiently small and explicit trusted substrate dependencies.

This is a future target and is currently HOLD.

## Layer model

```text
SIGMA applications / cognitive services
                |
        SIGMA capability API
                |
     SIGMA process/task model
                |
      SIGMA scheduler + IPC
                |
   SIGMA memory / VFS abstractions
                |
     SIGMA syscall/device layer
                |
      substrate machine boundary
                |
              hardware
```

The development direction is to move semantics upward into SIGMA-Ψ while making the lower trusted boundary progressively smaller, explicit, testable and replaceable.

## Version path

### v0.1 — deterministic microkernel semantics

Current candidate:
- kernel lifecycle
- task lifecycle
- round-robin scheduler
- logical clock
- deterministic final state

No filesystem, network, device or privileged host operation.

### v0.2 — capability and syscall contract

Define a typed/bounded SIGMA-side capability table and syscall dispatch semantics. Host access remains denied unless a capability is explicitly present.

### v0.3 — memory and virtual filesystem model

Implement SIGMA-side logical memory ownership and VFS semantics. Physical host/file access may be connected only through primitives that are independently verified to exist and are explicitly included in the trusted-boundary ledger.

### v0.4 — program image and loader

Load verified SIGMA program/bytecode images using the frozen actual ABI. Require malformed/truncated/unsupported image negative corpus before promotion.

### v0.5 — process isolation and IPC

Add per-process state, capability isolation, message passing, scheduler fairness tests and deterministic termination/fault semantics.

### v0.6 — device abstraction

Introduce device contracts without letting device-specific implementation leak into kernel policy. Each driver boundary requires real-device or emulator evidence.

### v0.7 — trusted-substrate reduction

Measure every remaining non-SIGMA primitive. Replace or minimize trusted host logic only when the SIGMA-written successor passes differential and regression gates.

### v1.0 — native boot target

Only eligible for a native/bare-metal label after evidence establishes:
- reproducible boot path
- exact machine/firmware boundary
- native execution or an explicitly minimized verified VM boundary
- memory and fault isolation appropriate to the target
- interrupt/timer semantics
- storage/device behavior needed by the target profile
- cold bootstrap and recovery
- independent differential/regression evidence

## Core invariants

```text
NO_SELF_CERTIFICATION
NO_INHERITED_PASS
NO_HIDDEN_TRUSTED_PRIMITIVES
NO_CANONICAL_CORE_MUTATION_FROM_CANDIDATE
NO_BARE_METAL_CLAIM_FROM_SOURCE_LANGUAGE_ALONE

FAIL_CLOSED
DETERMINISTIC_WHERE_POSSIBLE
CAPABILITY_BEFORE_AUTHORITY
EVIDENCE_BEFORE_PROMOTION
ROLLBACK_BEFORE_MUTATION
```

## Current trusted boundary

The current v0.1 source is SIGMA-Ψ, but execution still uses the existing compiler/VM substrate. That dependency is explicit and therefore the current status is not C-free/native/bare-metal.

The long-term objective is not to hide the bootstrap boundary; it is to shrink it until every remaining primitive has a precise purpose, test and replacement story.
