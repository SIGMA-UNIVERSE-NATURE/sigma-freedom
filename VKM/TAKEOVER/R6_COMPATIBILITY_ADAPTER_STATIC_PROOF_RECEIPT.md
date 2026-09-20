# SIGMA VKM R6 — Compatibility Adapter Static Proof

## Result

R6_CHUNK_COMPAT_CALLSITE_PATCH=PASS
R6_REPLAY_COMPAT_CALLSITE_PATCH=PASS
R6_COMPATIBILITY_ADAPTER_STATIC_PROOF=PASS
CHUNK_RECEIPT_CONTRACT=SATISFIED
REPLAY_RECEIPT_CONTRACT=SATISFIED
FINGERPRINT_SOURCE=SIGMA_ADMITTED_PROPOSAL
AIL_COMMIT_WRITER=NO
READY_FOR_R6_FROZEN_EXECUTION_TEST=YES

## Static topology gate

LEGACY_AIL_COMMIT_CALLS=0
R6_BRIDGE_EXECUTION_CALLS=2

The patched runner statically contains:
- chunk bridge invocation with candidate plus parent/child fingerprints;
- replay bridge invocation with replay candidate plus proposal-derived parent/child fingerprints.

No legacy "$AIL commit" writer remains in the patched runner.

## Compatibility receipt surface

The R6 bridge exposes the legacy-compatible receipt fields required by the patched callsites:

SCHEMA=SIGMA_AIL_WEIGHT_COMMIT_R5
RESULT=PASS
WEIGHTS_COMMITTED=YES
WEIGHTS_CHANGED=YES
WEIGHT_FINGERPRINT64_BEFORE=<parent proposal fingerprint>
WEIGHT_FINGERPRINT64_AFTER=<candidate proposal fingerprint>
R6_NATIVE_SCHEMA=SIGMA_VKM_CANONICAL_BRIDGE_R6
SIGMA_IDENTITY=ONE_SIGMA
LEGACY_AIL_COMMIT_USED=NO
DURABLE_TRANSACTION_USED=YES
COMPATIBILITY_RECEIPT_ONLY=YES

The compatibility surface is a receipt adapter; the mutation path remains VKM durable transaction, not an AIL commit writer.

## Safety

R7_R8_WRITERS_STOPPED=YES
ORIGINAL_R7_RUNNER_MUTATION=NO
PRODUCTION_VM_MUTATION=NO
ONE_SIGMA_STATE_MUTATION=NO
SIGMA_IDENTITY=ONE_SIGMA

GENERATION=5
CANONICAL_SHA256=ffb8d846540880f6f2669b39028a1f1aba187c984f927042c6c486a3009f4fb3

## Boundary

This is static compatibility proof only. It establishes that both patched commit callsites consume the VKM bridge with the expected receipt/fingerprint contract and that no AIL commit writer remains. Dynamic behavior under the exact frozen R7 execution environment remains to be proven.

NEXT=R6_FROZEN_EXECUTION_TEST
TERMUX_SHELL_CONTINUES=YES
