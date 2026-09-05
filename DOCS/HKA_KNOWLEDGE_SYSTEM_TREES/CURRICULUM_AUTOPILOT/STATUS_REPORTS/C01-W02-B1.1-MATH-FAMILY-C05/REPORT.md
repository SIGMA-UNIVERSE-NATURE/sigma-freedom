# C01-W02-B1.1-MATH-FAMILY-C05 — Durable Status Report

Status: `READY`
Stage: `CURRICULUM`
Scope: `B1.1-C05 — Giải tích và biến đổi liên tục`
Execution branch: `hka-tree/c01-w02-math-c05`

## Why C05 is active before C04

Director audit after C03 found an execution-order contradiction: `B1.1-C04-T08 — Hình học vi phân` requires derivative and multivariable-calculus primitives owned by C05, while the old sequence attempted C04 before C05 and forbade future-scope support.

The durable amendment `B1_1_MATH_EXECUTION_DEPENDENCY_AMENDMENT_1.md` therefore changes execution order only:

`C03 → C05 → C04`

No stable topic ID, name or primary ownership changed.

## Accepted inputs

- C03: `7546ad74fb0e71ad2120c7091947993690bef82d`
- C02: `cfd9746e2296280705e2e2e67b2c5980d440f02d`
- C01: `5659288da80a239e2ded408da87348670c1410c2`
- Canonical tree: `fc799bf1104ab6352710e1801777a971b5179995`

## Assigned scope

Ten canonical topics T01–T10: limits, continuity, derivative, integral, series, multivariable analysis, real analysis, complex analysis, functional analysis and harmonic analysis.

## Mandatory gates

- Complete knowledge, minimum redundancy.
- 100% Claim → Learning Objective closure.
- Zero locked-scope support claims.
- Source identity/version audit.
- Semantic duplicate and ownership audit against accepted C01–C03.
- Acyclic prerequisite/sequence graph.
- Clean stage boundary.

C04 geometry is locked and may be referenced only as non-support boundary/example. C06, C07, C09 and C10 are also locked.

## Durable recovery

Read in this order:

1. canonical pipeline;
2. curriculum state from `hka-tree/curriculum-master`;
3. active dependency amendment;
4. this window contract/open order/execution prompt;
5. this STATUS/REPORT and latest checkpoint;
6. exact accepted C01–C03 inputs.

## Next action

Execute `DIRECTOR_OPEN_ORDER.md`, then the locked `GPT_EXECUTION_PROMPT.md`, and author only B1.1-C05.

On worker candidate PASS, C04 remains gated until independent Director acceptance of C05.
