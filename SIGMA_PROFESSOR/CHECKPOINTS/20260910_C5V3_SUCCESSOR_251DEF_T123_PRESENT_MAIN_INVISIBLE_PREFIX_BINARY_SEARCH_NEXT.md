# C5V3 successor 251-DEF composition PASS / exact T1-T3 present / main compiler-invisible / R4 prefix binary search next

Date: 2026-09-10 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Scope

This checkpoint records the FIX1 deterministic successor composition/compiler matrix. No VM execution, production binding, or production mutation occurred.

## Exact successor source composition

Machine result:

```text
GATEA_PURE_DEF_COUNT=77
GATEA_PURE_NORMALIZED_SHA256=4d0ea071c5844938ccc264afbd76494e21279655988ad95f6bdd2842d989cb64
T1_T2_T3_DEF_COUNT=82
T1_T2_T3_NORMALIZED_SHA256=f48552534f2e5690b2b79a7a913cd2b5d376c13ba401b251eff63190820a8e07
T1_T2_T3_FIRST_DEF=WA_H
T1_T2_T3_LAST_DEF=T2_SHORTEST_PATH_BOUNDED
SUCCESSOR_DEF_COUNT=251
SUCCESSOR_UNIQUE_DEF_COUNT=251
SUCCESSOR_ENTRY_COUNT=1
SUCCESSOR_HEADER_COUNT=1
SUCCESSOR_SOURCE_BYTES=163746
SUCCESSOR_SOURCE_SHA256=b1ceedffa11497cab5454639eb1872cc5ecb95a5824b95e4d1be22c2ea2b7406
SUCCESSOR_STATIC_COMPOSITION=PASS
```

Legacy narrow cognition remains absent:

```text
legacy_analyze_segment=0
legacy_merge_evidence=0
LEFT=0
RIGHT=0
```

Classification:

```text
T1_T2_T3_SUCCESSOR_COMPOSITION=PRESENT_EXACT_BODY_SCOPE
T1_T2_T3_NATIVE_UTILIZATION=NOT_YET_PROVEN
```

## Compiler boundary matrix

```text
S1 Gate-A 77 + sentinel:
  bytes=31549
  sha=bdb9d2cc4e1832effb7ad1875560831e07803ce85f460de98489fd7b9df8545c
  class=NONTRIVIAL

S2 Gate-A 77 + P0 R4 14 + sentinel:
  bytes=31496
  sha=a1df1ad7d7c25c8c12125602679b6ea568fe055705e0288e31da126e8c3a1d81
  class=NONTRIVIAL

S3 Gate-A 77 + R4 no-P0 78 + sentinel:
  bytes=31496
  sha=a1df1ad7d7c25c8c12125602679b6ea568fe055705e0288e31da126e8c3a1d81
  class=NONTRIVIAL

S4 Gate-A 77 + exact T1/T2/T3 82 + sentinel:
  bytes=50848
  sha=61ed45b79a5c7ae1a85aabc1b36e1cfe4204f61a4252630cc57090cc0cb7c719
  class=NONTRIVIAL

S5 Gate-A 77 + full R4 92 + sentinel:
  bytes=31496
  sha=a1df1ad7d7c25c8c12125602679b6ea568fe055705e0288e31da126e8c3a1d81
  class=NONTRIVIAL

S6 all 251 DEF + sentinel:
  bytes=31496
  sha=a1df1ad7d7c25c8c12125602679b6ea568fe055705e0288e31da126e8c3a1d81
  class=NONTRIVIAL

Final successor:
  bytes=31496
  sha=a1df1ad7d7c25c8c12125602679b6ea568fe055705e0288e31da126e8c3a1d81
  class=NONTRIVIAL

Final counterfactual literal mutation:
  bytes=31496
  sha=a1df1ad7d7c25c8c12125602679b6ea568fe055705e0288e31da126e8c3a1d81

Final unbalanced entry:
  compile_rc=0
  bytes=31496
  sha=a1df1ad7d7c25c8c12125602679b6ea568fe055705e0288e31da126e8c3a1d81
```

## Classification

The successor is no longer a 29-byte header-only capsule. However nontrivial emission alone is insufficient for runtime admission.

```text
SUCCESSOR_NONTRIVIAL_EMISSION=PASS
SUCCESSOR_MAIN_SOURCE_SENSITIVITY=NO
FINAL_UNBALANCED_ENTRY_REJECTED=NO
SUCCESSOR_EXECUTABLE_MAIN_ADMISSION=NO
```

The byte-identical result across S2/S3/S5/S6/final/counterfactual/unbalanced strongly indicates compiler top-level emission stops after entering the R4 DEF region, while exact Gate-A+T1/T2/T3 remains compiler-visible.

Do not classify the 31,496-byte artifact as a full successor executable.

## Exact next diagnostic

```text
C5_M5/RUN_C5V3_R4_SUCCESSOR_R4_PREFIX_ENTRY_VISIBILITY_BINARY_SEARCH_R1.sh
COMMIT=673180f5d21245ea961d857bbd4884aa16654d54
```

The diagnostic locks the exact successor source SHA and compares two entry literals for each R4 prefix:

```text
bytecode(A) != bytecode(B) => entry visible
bytecode(A) == bytecode(B) => entry invisible
```

It binary-searches the first R4 DEF prefix that makes the entry invisible and reports:

```text
LAST_VISIBLE_R4_PREFIX_COUNT
FIRST_INVISIBLE_R4_PREFIX_COUNT
FIRST_SUSPECT_R4_DEF_INDEX
FIRST_SUSPECT_R4_DEF_NAME
FIRST_SUSPECT_SUCCESSOR_DEF_INDEX
FIRST_SUSPECT_DEF_SHA256
```

It also runs dummy uppercase/lowercase DEF controls and unbalanced-entry controls at the visibility boundary.

## Production

```text
VM_EXECUTION=NO
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
LIVE_MAIN_SOURCE_SHA256=23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc
LIVE_RUNNER_SHA256=092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847
```

`CLAIM <= EVIDENCE`
