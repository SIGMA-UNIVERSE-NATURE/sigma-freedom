# C5V3 — SIGMAC real emitter / full-core zero-code capsule checkpoint

Date: 2026-09-10 +07
Window: core architecture rewrite + synchronization
Production mutation: NO

## Exact compiler/VM identities

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
SIGMAC_BYTES=24352
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
VM_BYTES=35016
```

## Forensics result

The locked compiler is not a constant-output stub.

Negative/positive controls:

```text
empty source -> RC=3 invalid/missing SIGMA header, no output
plain text -> RC=3 invalid/missing SIGMA header, no output
invalid broken body -> RC=4 parse error, no output
unbalanced main -> RC=4 expected '}', no output
minimal A -> RC=0, 59-byte distinct SIGMBC01 artifact
minimal B -> RC=0, 77-byte distinct SIGMBC01 artifact
```

Minimal A/B literals are visibly encoded in the emitted bytecode, proving source-sensitive parser/emitter behavior in that tested direct-print scope.

## Current 29-byte artifact

R2 and R3 FIX1 both emit:

```text
SHA256=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a
BYTES=29
HEX=5349474d424330310100000000000000000000000000000001000000ff
MAGIC_ASCII=SIGMBC01
```

This is byte-identical to the artifact emitted from a valid SIGMA header with no executable body.

R2 source and R3 FIX1 source are materially different, yet both compile to that exact header-only artifact.

Therefore current evidence does NOT support the claim that R2/R3 source is losslessly self-compressed into 29 bytes. The exact 29 bytes contain no source-specific payload visible in the bytecode artifact.

## Remaining alternative

The VM may derive or resolve source from the `.sigmab` path or another external dependency. The live runner invokes:

```text
"$VM" "$BIN"
```

so source-path coupling must be tested before concluding that the 29-byte artifact is merely inert.

## Exact next machine test

Use:

```text
C5_M5/RUN_C5V3_VM_29B_CAPSULE_SOURCE_COUPLING_PROBE_R1.sh
SCRIPT_COMMIT=c698f50c9770fcb8e2ff5d9941007e42f2320eb4
```

The probe uses only fresh temporary trees and does not invoke the live runner. It places the exact same 29-byte capsule beside two different sibling sources and also with no source, then runs the locked VM. Separate emitted bytecode A/B are executed as positive controls.

Classification:

```text
A/B sibling source changes VM output
-> SOURCE_RESOLVING_LOADER_OR_REFERENCE_CAPSULE

same 29B behaves identically with A/B/no source
+ real emitted A/B bytecode behaves differently
-> EMPTY_OR_GENERIC_EXECUTION_CAPSULE in tested environment
```

## Current claim boundary

```text
SIGMAC_REAL_PARSER=PASS
SIGMAC_SOURCE_SENSITIVE_EMITTER=PASS_IN_MINIMAL_DIRECT_PRINT_SCOPE
R2_R3_FULL_CORE_EXECUTABLE_EMISSION=FAIL_OR_ZERO_CODE_UNEXPLAINED
CURRENT_29B_SELF_COMPRESSION_OF_FULL_CORE=NOT_SUPPORTED
VM_EXTERNAL_SOURCE_COUPLING=UNTESTED
R3_FIX1_RUNTIME_ADMISSION=NO
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

`CLAIM <= EVIDENCE`
