# Director Amendment — B1.1 Mathematics Execution Dependency 1

STATUS: ACTIVE
STAGE: CURRICULUM

## Purpose

Correct an execution-order dependency discovered during independent Director audit after C03.

Stable scope IDs, canonical topic IDs, names, and primary ownership are unchanged.

## Problem

`B1.1-C04-T08 — Hình học vi phân` requires derivative and multivariable-calculus primitives owned by `B1.1-C05 — Giải tích và biến đổi liên tục`.

The previous execution order required C04 to PASS before C05, while forbidding C04 from using claims from an unlocked future scope. That creates an academic dependency contradiction: C04-T08 would either have to duplicate calculus or rely on an unopened scope.

## Corrected execution dependency

After Director-accepted C03:

`C03 → C05 → C04 → C06...`

For this correction:

- C05 may execute after accepted C02 + C03.
- C04 remains locked until accepted C05.
- C04 may then consume accepted C05 calculus primitives, especially for differential geometry, while retaining geometry ownership.
- C05 must not take ownership of C04 geometry. Geometric interpretations of calculus may be boundary references only.
- C05 must not depend on C04 claims for academic closure.

## Locked boundaries

- C04 retains all nine canonical geometry topics and their primary ownership.
- C05 retains all ten canonical analysis topics and their primary ownership.
- No topic ID is moved, renamed, deleted, duplicated, or renumbered.
- Claim-to-Learning-Objective closure and zero-unlocked-support rules remain mandatory.
- Pipeline remains `CURRICULUM`; `ACADEMIC_LOCKED` and all later stages remain gated.

## Recovery rule

Any replacement window must read this amendment before using the older B1 authoring sequence where the two conflict.
