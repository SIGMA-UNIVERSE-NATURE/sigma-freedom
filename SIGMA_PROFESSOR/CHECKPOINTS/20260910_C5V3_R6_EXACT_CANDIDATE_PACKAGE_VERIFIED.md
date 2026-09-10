# 2026-09-10 — C5V3 R6 EXACT CANDIDATE PACKAGE VERIFIED

Status: **IMMUTABLE EXACT-BYTES VERIFICATION / NON-PRODUCTION**
Branch: `SIGMA_LIFE`
Date: 2026-09-10 (Asia/Ho_Chi_Minh)

## Purpose

This checkpoint upgrades the R6 synchronization evidence from receipt-only identity to exact candidate-package bytes supplied to the synchronization window.

It does not bind or mutate production.

## Exact uploaded package

```text
PACKAGE_NAME=SIGMA_C5V3_R6_PRODUCTION_LINEAGE_CANDIDATE_20260909T184734.zip
PACKAGE_SHA256=c71dabf5732a28c1ffc4de76b0bba22d5daa4985b91313f2288ea5426ee6a436
PACKAGE_FILE_COUNT=6_NON_DIRECTORY_FILES
```

Package contents:

```text
candidate/core.sigma
candidate/STRUCTURAL_REPORT.txt
candidate/M5_ONLY_INSERTION.tsv
candidate/core.a.sigmab
candidate/core.b.sigmab
candidate/core.sigmab
```

## Exact candidate identities verified from package bytes

```text
candidate/core.sigma
SHA256=dde709a25d8e2f2626c299ad4d5c40562e2bcc253cf9bb63aef17e44f02943ac

candidate/core.a.sigmab
SHA256=dcb4f0ed9c637e368d396214471ae4c8fd67bc6622b02f133e867d2bab8b6693

candidate/core.b.sigmab
SHA256=dcb4f0ed9c637e368d396214471ae4c8fd67bc6622b02f133e867d2bab8b6693

candidate/core.sigmab
SHA256=dcb4f0ed9c637e368d396214471ae4c8fd67bc6622b02f133e867d2bab8b6693
```

The source/bytecode identities exactly match the frozen R6 PASS checkpoint and offline-test handoff.

## Structural report verified from exact package

```text
PRODUCTION_DEF_COUNT=11
M5_ONLY_DEF_EXPECTED=63
M5_ONLY_DEF_INSERTED=63
TOOL_DEF_COUNT=82
CANDIDATE_DEF_COUNT=156
PRODUCTION_DEF_BODY_HASHES_PRESERVED=PASS
M5_ONLY_DEF_BODY_HASHES_PRESERVED=PASS
PRODUCTION_UNIVERSE_BYTE_IDENTICAL=PASS
CANDIDATE_HEADER_COUNT=1
M5_PRODUCTION_SYMBOL_COLLISION=NO
M5_TOOL_SYMBOL_COLLISION=NO
```

`candidate/M5_ONLY_INSERTION.tsv` contains a header plus 63 ordered inserted M5-only DEF records.

## Canonical synchronization meaning

```text
R6_PRODUCTION_LINEAGE_CANDIDATE=EXACT_BYTES_PRESENT_AND_VERIFIED
R6_SOURCE_IDENTITY_MATCH=PASS
R6_BYTECODE_IDENTITY_MATCH=PASS
R6_DOUBLE_COMPILE_BYTECODE_IDENTITY_MATCH=PASS
R6_STRUCTURAL_REPORT_MATCH=PASS
```

This does **not** prove activation or utilization:

```text
C5V3_PRODUCTION_CORE_SYNCHRONIZED=NO
M5_CAPABILITY_ACTIVE_IN_PRODUCTION_DISPATCH=NO
C5V3_AUTO_LEARN_USES_SYNCHRONIZED_CAPABILITIES=NOT_PROVEN
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

## Next gate

Use these exact R6 candidate bytes as the synchronization baseline for:

```text
isolated production-runner ABI regression
-> explicit activation/dispatch integration
-> state-lineage compatibility/inheritance
-> native capability-utilization causal verification
```

Do not reconstruct R6 from summaries while these exact bytes are available.
