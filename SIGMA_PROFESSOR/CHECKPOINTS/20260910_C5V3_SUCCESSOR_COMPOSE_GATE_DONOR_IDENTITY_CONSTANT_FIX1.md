# C5V3 Successor Compose Gate — donor identity constant FIX1

Date: 2026-09-10 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Context

The first successor composition run stopped before T1/T2/T3 extraction with:

```text
GATEA_PURE_DEF_COUNT=77
GATEA_PURE_NORMALIZED_SHA256=4d0ea071c5844938ccc264afbd76494e21279655988ad95f6bdd2842d989cb64
HOLD=GATEA_PURE_NORMALIZED_IDENTITY
```

This is a harness identity-constant defect, not a Gate-A source failure.

## Independent exact donor reconstruction

Using the same DEF-block extraction/normalization algorithm against the exact recovered artifacts gives:

```text
GATEA_PARENT_SOURCE_SHA256=bf468c564451839d3be9b22243039fe71ceb87b766a165d996f4be055f7cbbf1
GATEA_PURE_DEF_COUNT=77
GATEA_PURE_NORMALIZED_SHA256=4d0ea071c5844938ccc264afbd76494e21279655988ad95f6bdd2842d989cb64
GATEA_EXCLUDED_DEF=append_line

R6_SOURCE_SHA256=dde709a25d8e2f2626c299ad4d5c40562e2bcc253cf9bb63aef17e44f02943ac
T1_T2_T3_DEF_COUNT=82
T1_T2_T3_FIRST_DEF=WA_H
T1_T2_T3_LAST_DEF=T2_SHORTEST_PATH_BOUNDED
T1_T2_T3_NORMALIZED_SHA256=f48552534f2e5690b2b79a7a913cd2b5d376c13ba401b251eff63190820a8e07
```

These match the previously locked R3 FIX1 cognition/tool donor identities.

## Defect

The R1 composition harness embedded two incorrect expected normalized SHA256 constants:

```text
OLD_GATEA_EXPECTED=986465097126d33598ebb83ec9f0af331eadb3a2443f9605dded3a1e4ab04d52
OLD_T1_T2_T3_EXPECTED=8b6f231a23c2ab5cd19e2ba2806ced29e9ed6bb8c9590c0559e9532a9feb7d06
```

No Gate-A, R4, transaction-main, T1/T2/T3, compiler, VM, live core or runner source is changed for this fix.

## FIX1

```text
PATH=C5_M5/RUN_C5V3_R4_SUCCESSOR_T1_T2_T3_COMPOSE_COMPILE_R1_FIX1.sh
COMMIT=2244f5270fe969d19fb512505495736493c1b3ea
FIX_SCOPE=HARNESS_DONOR_NORMALIZED_IDENTITY_CONSTANTS_ONLY
```

FIX1 downloads the immutable R1 gate at commit `5b97501a3f9f84e690d4bc57caa09242ddb25e6e`, verifies each old bad constant appears exactly once, replaces only those two constants, verifies the replacements, then executes the corrected gate.

## Classification

```text
SUCCESSOR_COMPOSE_R1_FIRST_RUN=HOLD_HARNESS_DONOR_IDENTITY_CONSTANT_DEFECT
GATEA_SOURCE_FAIL=NO_EVIDENCE
T1_T2_T3_SOURCE_FAIL=NO_EVIDENCE
R4_SOURCE_FAIL=NO_EVIDENCE
PRODUCTION_MUTATION=NO
VM_EXECUTION=NO
```

Next action: run FIX1 and continue through the full compiler boundary matrix.

`CLAIM <= EVIDENCE`
