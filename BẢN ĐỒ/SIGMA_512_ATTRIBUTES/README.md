# SIGMA 512 — Canonical Architecture Contract

## Status

This directory contains the 512 architectural requirements for SIGMA.

The historical files are preserved as **legacy source segments**. They are not independently authoritative because their numeric ranges overlap.

The canonical specification is assembled by `SIGMA_512_CANONICAL_MANIFEST.json` using exactly these spans:

1. `Full PART 01 TO 21.` → attributes **1–275**
2. `PART 21 to 28` → attributes **276–440** only
3. `PART 28 TO END` → attributes **441–512**

Any duplicate occurrence outside those selected spans is archival context and MUST NOT be counted as a second canonical attribute.

## Source-of-truth hierarchy

1. `SIGMA_512_CANONICAL_MANIFEST.json` — defines which text is canonical.
2. `SIGMA_512_TRACEABILITY_MAP.json` — maps every attribute range to responsible SIGMA DNA cores and required evidence classes.
3. `validate_512_architecture.py` — reconstructs the 512 canonical records, verifies exact coverage 1..512, checks 54-core references, and can emit an expanded item-level registry.
4. `../06_512_TO_54_CORE_TRACEABILITY.md` — human-readable implementation contract.
5. Historical source segment files — preserved evidence/history, not standalone authority.

## Status semantics

A requirement has separate statuses. They MUST NOT be collapsed into one PASS flag.

- `SPEC_PASS` — the requirement exists in the canonical 1..512 specification.
- `MAPPED` — responsibility is mapped to one or more cores.
- `NOT_AUDITED` — implementation evidence has not yet been inspected.
- `PARTIAL` — some implementation evidence exists but the contract is not fully demonstrated.
- `PASS` — implementation + test + evidence satisfy the requirement.
- `HOLD` — evidence is insufficient or contradictory.
- `FAIL` — evidence demonstrates violation.
- `NOT_APPLICABLE` — only valid with an explicit rationale.

**No implementation may inherit PASS from the existence of a document, core filename, class, function, comment, test name, or self-report.**

## Traceability invariant

For every attribute `001..512`, SIGMA must eventually be able to answer:

```text
ATTRIBUTE
  -> canonical requirement
  -> responsible core(s)
  -> implementation artifact(s)
  -> test(s) / experiment(s)
  -> evidence
  -> evaluator
  -> current status
  -> last verified version/time
  -> rollback or correction path
```

Until those links exist, the requirement may be `SPEC_PASS` and `MAPPED`, but its implementation remains `NOT_AUDITED`.

## Anti-self-certification rule

The component that proposes or implements a change MUST NOT be the sole authority that changes its own evaluation rule and then declares itself compliant.

`change != improvement != permission`

## Preservation rule

Do not delete or rewrite historical 512 source segments merely to make the directory look clean. Historical overlap is preserved as provenance. Canonical selection resolves the ambiguity without destroying history.
