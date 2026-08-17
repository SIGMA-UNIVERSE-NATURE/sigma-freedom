# NEXT ACTION

## SIGMA-512-CONTINUOUS-LOCAL-EXECUTOR-PROBE-001

**Mode:** `AUTHORIZED_LOCAL_READ_ONLY_AUTODISCOVERY_PROBE`

**Principle:** `DO NOT IMPROVE YET. MEASURE CURRENT REALITY FIRST.`

Remote Operator v0.6.0 is now a contract-validated candidate for bounded continuous SIGMA 512 execution. This probe must determine whether the HP executor can discover the current canonical request by itself, without a human-relayed request ID and without a Remote Operator `COMMANDS` file.

### Required execution

1. Install/switch the authorized HP `SIGMA Remote Operator` Scheduled Task to the already validated v0.6.0 candidate once.
2. Do **not** copy this request ID into any Remote Operator command file.
3. The executor must fetch the latest `SIGMA_LIFE` HEAD and read `CURRENT_STATE.json`, `NEXT_ACTION.md`, `LOCAL_COGNITION_REQUEST.json`, `LOCAL_EXECUTION_BRIDGE_STATUS.json` and the receipt schema directly from canonical Git objects.
4. It may execute only the SHA-256-pinned script declared by the canonical request under `EVIDENCE/.../run_harness.py`, using Python without a shell.
5. Keep paid API OFF, website actions OFF, network-required=false, external side effects at zero, and do not patch/mutate the 54 DNA cores.
6. Return exactly one machine receipt for this request ID. The receipt must show auto-discovery, no Remote Operator command file, no hard-coded request ID and no arbitrary shell.
7. After publishing the receipt, subsequent polls must not execute the same request ID again.
8. The local executor must not modify canonical state, self-promote the result, or invent the following action. Canonical evaluation owns promotion and next-action selection.

### Success evidence

- Executor runtime version >= `0.6.0`.
- `AUTO_DISCOVERED_FROM_CANONICAL_REQUEST=true`.
- `REMOTE_COMMAND_FILE_USED=false`.
- `CANONICAL_REQUEST_ID_NOT_HARDCODED=true`.
- `ARBITRARY_SHELL_USED=false`.
- Probe result: `TARGET_COUNT=8`, `PASS=0`, `PARTIAL=8`, `FAIL=0`.
- 54-core hash unchanged before/after; `core_modifications=0`.
- `external_side_effects=0`, `paid_api_used=false`, `secrets_disclosed=false`.
- A repoll produces no second execution result for the same request ID.

### Evidence boundary

A successful probe would verify bounded continuous canonical request **discovery/execution**, not unrestricted autonomy, independent evaluation, different-model continuity, or automatic truth promotion. The 512 implementation counts remain unchanged until a separate evidence decision justifies changing them.
