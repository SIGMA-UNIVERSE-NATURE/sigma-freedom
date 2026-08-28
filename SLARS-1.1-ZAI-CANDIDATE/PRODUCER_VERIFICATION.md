# SLARS-1.1-ZAI Producer Verification

**Role:** Producer / Creative Director candidate verification  
**Date:** 2026-08-28 UTC  
**Release authority:** not assumed  
**Independent technical PASS:** not issued

## Input provenance

```text
BASE_SLARS_ARCHIVE=SLARS-1.0.zip
BASE_SLARS_ARCHIVE_SHA256=4ba9c4759fdf2c39a1572099c02aa631fbadda1a652438c3c582671f91a16049

AUDITED_CANDIDATE=SIGMA_COGNITION_CANDIDATE.sigma
AUDITED_CANDIDATE_SHA256=4583a601153325ac97a067d74e6ad84cb51b787f0ae6c11f7d06df76759b2d51
```

## Producer checks

Commands:

```bash
python3 -m py_compile \
  tools/zai_core.py \
  tools/validate_zai_bundle.py \
  tests/test_validate_zai_bundle.py

python3 tools/validate_zai_bundle.py \
  --protocol templates/zai_protocol.template.json \
  --run templates/zai_run_bundle.template.json \
  --evidence-root . \
  --mode structure

python3 -m unittest discover -s tests -v
```

Observed result at this checkpoint:

```text
PY_COMPILE=PASS
ZAI_TEMPLATE_STRICT_SCHEMA=PASS
ZAI_TEMPLATE_ACTUAL_EXECUTION=UNVERIFIED
FULL_UNIT_AND_MUTATION_TESTS=68/68_PASS
PACKAGE_MANIFEST_EXACT_COVERAGE=PASS
VALIDATOR_CRASHES_OBSERVED=0
```

The mutation suite includes a real materialized clean-control bundle and rejects
registered exact/normalized/encoded/filename leaks, key visibility/order
violations, host semantic derivation, hidden output writes, duplicate VM
execution, role collisions, unsafe paths, symlinks, hash/event/RUN_ID replay,
rubric/output binding faults, malformed/ambiguous JSON, and answer material in
pre-key argv. It also rejects extra host/event inputs that would let VM
execution depend on raw output or post-output review material. It confirms the
required orthogonality:

```text
CLEAN_WRONG_TASK_RESULT:
    INJECTION_INTEGRITY_STATUS=PASS
    TASK_OUTCOME=FAIL
SIGMA_COGNITION=NOT_PROVEN
```

Additional regressions bind artifact bytes into every event hash; require
hash-bound semantic-review coverage of the full scan surface; reject hostile
report-line injection, invalid/non-finite JSON numbers and non-RFC3339 dates;
enforce canonical artifact metadata and bounded evidence resources; and detect
registered material behind invalid UTF-8 prefixes, full percent encoding and
JSON Unicode escapes. Toolchain claim text was narrowed because binary hashes
do not independently attest an approved native build.

The retained SLARS-1.0 validator is explicitly legacy-scoped and cannot emit a
SLARS-1.1 full-package PASS. A future composite validator must bind ZAI evidence
for every candidate-origin A3/A4/R1/V1 output before that package-level claim is
eligible.

## Evidence ceiling

These are Producer tests of the specification and validator. They do not show
that a native SIGMA blind run occurred and do not authorize any cognition claim.

```text
SLARS_ZAI_PRODUCER_IMPLEMENTATION=TESTED
ACTUAL_LOCKED_NATIVE_BLIND_RUN=NOT_RUN
ZERO_ANSWER_INJECTION_FOR_REAL_SIGMA_RUN=UNVERIFIED
SIGMA_SELF_OBSERVES_AND_ANSWERS=NOT_PROVEN
HUMAN_LANGUAGE_AS_SIGMA_COGNITION=FORBIDDEN_UNTIL_PROVEN
INDEPENDENT_TECHNICAL_VERIFICATION=REQUIRED
```
