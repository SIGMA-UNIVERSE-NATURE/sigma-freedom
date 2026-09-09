# C5V3 — R4 92 DEF NOT CAUSAL / RAW VS NORMALIZED SURFACE NEXT

Date: 2026-09-10 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Machine result

Operator ran:

```text
C5_M5/RUN_C5V3_R4_SUCCESSOR_R4_PREFIX_ENTRY_VISIBILITY_BINARY_SEARCH_R1.sh
COMMIT=673180f5d21245ea961d857bbd4884aa16654d54
```

Locked identities passed:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
SUCCESSOR_SOURCE_SHA256=b1ceedffa11497cab5454639eb1872cc5ecb95a5824b95e4d1be22c2ea2b7406
LIVE_CORE_SHA256=23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc
LIVE_RUNNER_SHA256=092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847
```

Parsed successor ordering:

```text
77 Gate-A DEF
92 R4 DEF
82 T1/T2/T3 DEF
=251 DEF
```

Controls:

```text
Gate-A 77 + A/B sentinel                         -> source sensitivity PASS
Gate-A 77 + dummy uppercase DEF + A/B sentinel -> source sensitivity PASS
Gate-A 77 + dummy lowercase DEF + A/B sentinel -> source sensitivity PASS
Gate-A 77 + all 92 normalized R4 DEF + A/B sentinel -> source sensitivity PASS
```

Full normalized R4 result:

```text
CONTROL_GATEA_PLUS_R4_92_A_BYTES=64176
CONTROL_GATEA_PLUS_R4_92_B_BYTES=64176
CONTROL_GATEA_PLUS_R4_92_A_SHA256=da81e01fd1f4870b9603ce9e67ef8c50559c73290f0b5da6d12a75df32758c23
CONTROL_GATEA_PLUS_R4_92_B_SHA256=d71724f9821a018ea9fc0f0c8b31cb33e1102e3ab56328cd3454cb6e854713d2
CONTROL_GATEA_PLUS_R4_92_ENTRY_SOURCE_SENSITIVITY=PASS
R4_FULL_ENTRY_VISIBILITY=PASS
RESULT=R4_92_NOT_CAUSAL_UNDER_PREFIX_TEST
```

## Reclassification

The 92 R4 DEF bodies are not the observed cause of successor entry invisibility under normalized DEF-block composition.

This supersedes the previous working hypothesis that one R4 DEF necessarily caused the compiler to stop before the entry.

The remaining material difference between the earlier failing composition and the successful prefix test is the presence of raw module text outside normalized DEF blocks: module-leading/interstitial comments, blank/separator text, or another raw-composition surface.

Therefore:

```text
R4_DEF_BODY_CAUSALITY=NO_OBSERVED_UNDER_NORMALIZED_PREFIX_TEST
R4_92_NORMALIZED_ENTRY_VISIBILITY=PASS
SUCCESSOR_FINAL_RAW_MAIN_VISIBILITY=STILL_NOT_PROVEN
T1_T2_T3_EXACT_SUCCESSOR_SOURCE_PRESENCE=PASS
T1_T2_T3_NATIVE_UTILIZATION=NOT_YET_PROVEN
R4_RUNTIME_LEARNING=NOT_ADMITTED
```

## Exact next probe

```text
C5_M5/RUN_C5V3_R4_RAW_VS_NORMALIZED_MODULE_ENTRY_VISIBILITY_R1.sh
COMMIT=c46b925abfd8ab9226cd91e5fc058d4d3d6eaeb6
```

The probe compares, with A/B entry-literal source sensitivity:

```text
Gate-A + raw State       vs Gate-A + normalized State
Gate-A + raw Transitions vs Gate-A + normalized Transitions
Gate-A + raw Adapter     vs Gate-A + normalized Adapter
Gate-A + raw Durable     vs Gate-A + normalized Durable
Gate-A + raw Kernel      vs Gate-A + normalized Kernel
Gate-A + raw P0          vs Gate-A + normalized P0
```

and cumulative raw vs normalized module sequences.

Interpretation:

```text
RAW FAIL + normalized PASS -> non-DEF raw module surface causal in tested scope
all raw PASS                -> previous composition difference lies outside R4 module bodies/raw module surfaces
```

No VM execution. No production binding. No production mutation.

`CLAIM <= EVIDENCE`
