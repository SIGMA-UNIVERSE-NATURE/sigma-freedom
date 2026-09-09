# C5V3 — SIGMBC01 29-byte partial forensics / FIX1 probe

Date: 2026-09-10 Asia/Ho_Chi_Minh

## Machine evidence received

Locked identities remained:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
R3_FIX1_SOURCE_SHA256=152f5b90033e3ee7a67c8847d95cb6eb6b17ab1f659f079a9533b749e8d0b7d8
R3_FIX1_29B_SHA256=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a
```

Exact 29-byte payload:

```text
5349474d424330310100000000000000000000000000000001000000ff
```

Byte interpretation without assigning undocumented field semantics:

```text
00..07 = ASCII "SIGMBC01"
08..11 = 01 00 00 00 = u32le 1
12..15 = 00 00 00 00
16..19 = 00 00 00 00
20..23 = 00 00 00 00
24..27 = 01 00 00 00 = u32le 1
28     = ff
```

This shape is consistent with a versioned SIGMA bytecode/capsule container header containing mostly empty/zero fields plus a terminator/flag. It is not yet evidence of lossless source compression.

## Probe failure

The first export probe stopped before the control matrix because Bash `set -u` exposed a local-variable initialization bug in `compile_case`: `label` was referenced in another `local` initializer before binding.

```text
FAILURE_CLASS=HARNESS_SHELL_BUG
CORE_RESULT=NOT_REACHED
VM_EXECUTION=NO
PRODUCTION_MUTATION=NO
```

## Replacement probe

Use:

```text
C5_M5/RUN_C5V3_SIGMAC_CAPSULE_FORENSICS_EXPORT_R1_FIX1.sh
SCRIPT_COMMIT=966f2f14c52ad9bb075f26eed6972a86e3543f5f
```

The FIX1 probe:

```text
locks sigmac/VM/runner/R2/R3 identities
parses the 29-byte payload by offset
compiles empty/plain/header-only/invalid/minimal-A/minimal-B/unbalanced/R2/R3 controls
counts distinct output bytes/hashes/sizes
extracts static printable strings + ELF metadata from local sigmac and VM
extracts exact compiler/VM invocation lines from the locked production runner
exports exact binaries, sources, capsules and controls to one forensic ZIP
VM_EXECUTION=NO
PRODUCTION_MUTATION=NO
```

Decision rule:

```text
all arbitrary controls -> identical SIGMBC01 29B
    => constant container/stub strongly established; not source lossless compression
source-sensitive capsules and/or invalid rejection
    => continue capsule/decoder/reference investigation
```

`CLAIM <= EVIDENCE`.
