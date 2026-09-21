# SIGMA Operating Language Roadmap — G11 through G20

## Goal

Extend Sigma beyond the G1-G10 VM/language substrate into an operating-language/system-orchestration layer.

This roadmap is authoritative for future work windows unless superseded by later empirical evidence and an explicit roadmap update.

## Start point

- G1-G10: finish and prove the Sigma-VKM language/VM substrate.
- **Operating-language expansion begins immediately after G10 is PROVEN, starting at G11.**
- The 300 public API program may begin after the G10 substrate is stable and may proceed alongside G11-G20 where dependencies permit.
- Every generation/API still requires real compile/execution evidence before PASS/PROVEN.

## G11-G15 — system runtime

### G11 — Module/package ABI
Module identity, loading, version/interface boundaries, dependency resolution primitives and Sigma-level module policy.

### G12 — Process/task model
Tasks/process abstraction, lifecycle, scheduling interface and minimal native process/thread primitives where mechanically required.

### G13 — IPC/channel/event runtime
Channels, messages, event loop/wait primitives and Sigma-owned orchestration.

### G14 — Filesystem/storage abstraction
Filesystem/storage interfaces, handles, metadata and durable operations; native kernel limited to mechanical OS access.

### G15 — Network/runtime services
Socket/network primitives, DNS/TLS bindings where required, service-facing runtime abstractions and Sigma-level networking policy.

## G16-G20 — operating-language layer

### G16 — Permissions and capabilities
Capability model, authority boundaries, resource permissions and explicit access policy in Sigma.

### G17 — Service lifecycle and supervision
Service definitions, start/stop/restart, dependency ordering, health state and supervision policy.

### G18 — Transactional system state and recovery
Atomic state transitions, journals/checkpoints, rollback/recovery orchestration and persistent system state.

### G19 — Observability and audit
Metrics, traces, structured events, audit/provenance and resource/accounting visibility.

### G20 — Boot/runtime orchestration and self-hosting acceptance
Top-level runtime orchestration, service graph activation, recovery path, integrated operating-language acceptance and end-to-end self-hosting target.

## Architecture rule

PRIMARY_LANGUAGE=SIGMA
IMPLEMENTATION_POLICY=SIGMA_FIRST_MINIMAL_KERNEL

Kernel remains mechanical: bytes, memory, file/syscall primitives, socket, clock, atomic OS operation, cryptographic/numeric/tensor primitives.

Sigma owns semantics/policy/orchestration, including goals, beliefs, planning, learning policy, source preference, service policy and system coordination.

Do not migrate behavior into C merely for implementation convenience.

## Acceptance rule

For every generation:

SOURCE_WRITTEN
→ COMPILE_PASS
→ SIGMA_CALLABLE
→ SELFTEST_PASS
→ REGRESSION_PASS
→ PROVEN

No generation is COMPLETE based on source existence alone.

## 300 API relationship

300_API_CATALOG=COMPLETE
300_API_GROUPING=30_GROUPS_X_10
300_API_SOURCE_IMPLEMENTATION=IN_PROGRESS

After G10 is proven, begin/continue API implementation according to HANDOFF_300_API_SOURCE_PLAN.md while G11-G20 progresses where dependency ordering permits.

## Current transition

At creation of this roadmap:
G5_LOOP_OPCODE_DECODING=PASS
NEXT=GENERATION_6_CALL_RETURN_AND_CONTROL_FLOW

OPERATING_LANGUAGE_START=AFTER_G10_PROVEN
OPERATING_LANGUAGE_FIRST_GENERATION=G11
OPERATING_LANGUAGE_TARGET=G20
