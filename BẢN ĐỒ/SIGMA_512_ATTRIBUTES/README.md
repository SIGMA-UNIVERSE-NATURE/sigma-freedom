# SIGMA 512 — Canonical Architecture Contract

## Status

This directory contains the 512 architectural requirements for SIGMA.

The working tree now uses **non-overlapping canonical source segments**. Historical duplicate/overlapping files have been removed from the working tree, but remain recoverable from Git history and their old blob SHAs are recorded in `SIGMA_512_CANONICAL_MANIFEST.json`.

The canonical specification is assembled using exactly these spans:

1. `Full PART 01 TO 21.` → attributes **1–275**
2. `ATTRIBUTES_276_440.md` → attributes **276–440**
3. `PART 28 TO END` → attributes **441–512**

There is no duplicate numeric authority in the current canonical source set.

## Source-of-truth hierarchy

1. `SIGMA_512_CANONICAL_MANIFEST.json` — defines which text is canonical and records deleted duplicate provenance.
2. `SIGMA_512_TRACEABILITY_MAP.json` — maps every attribute range to responsible SIGMA DNA cores and required evidence classes.
3. `SIGMA_512_IMPLEMENTATION_STATUS.json` — evidence ledger; implementation defaults to `NOT_AUDITED`.
4. `validate_512_architecture.py` — reconstructs the 512 canonical records, verifies exact coverage 1..512, checks 54-core references, and can emit an expanded item-level registry.
5. `../06_512_TO_54_CORE_TRACEABILITY.md` — human-readable implementation contract.
6. Git history — historical duplicate/overlapping source artifacts remain recoverable by commit/blob SHA.

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

## Validation

Local validation:

```bash
python "BẢN ĐỒ/SIGMA_512_ATTRIBUTES/validate_512_architecture.py"
```

Generate the expanded 512-item machine-readable registry:

```bash
python "BẢN ĐỒ/SIGMA_512_ATTRIBUTES/validate_512_architecture.py" --write
```

Repository enforcement is defined in:

`.github/workflows/sigma_512_contract.yml`

The workflow must fail if canonical coverage, 54-core discovery, traceability coverage, or evidence-status governance is invalid.

## Anti-self-certification rule

The component that proposes or implements a change MUST NOT be the sole authority that changes its own evaluation rule and then declares itself compliant.

`change != improvement != permission`

## Deduplication and provenance rule

Duplicate working-tree copies are not retained merely for archival convenience. When a duplicate or overlapping source is removed:

1. canonical coverage must remain complete;
2. the replacement must pass the contract validator;
3. the deleted path and blob SHA must be recorded in the manifest;
4. Git history remains the immutable recovery path.

This keeps the active architecture clean without erasing provenance.
