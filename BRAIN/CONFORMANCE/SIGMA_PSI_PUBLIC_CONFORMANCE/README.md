# SIGMA-PSI Public Conformance Suite

WINDOW_G_PUBLIC_CONFORMANCE_SUITE_FREEZE=YES
DATE=2026-08-26
BRANCH=SIGMA_LIFE
BASELINE_WINDOW_F_COMMIT=25fdf0109658d4e1fc97d72fd4c701c44401ba0c

This suite is evidence-bounded. It publishes PASS, NOT_PROVEN, OUT_OF_CURRENT_LANGUAGE_SURFACE, and CONFLICTED rows without inventing missing semantics.

Core laws:
- CLAIM <= EVIDENCE
- UNKNOWN != FAIL
- NOT_PROVEN != UNSUPPORTED
- EXPECTED_CONDITION comes from an already frozen contract
- GPT_PREFERENCE != EXPECTED_CONDITION
- AGGREGATE_PASS != SUBCLAIM_PROOF
- PREWRITTEN_RESULT != DERIVED_RESULT

Files:
- CONFORMANCE_MANIFEST.tsv: category counts and release-blocking gaps.
- POSITIVE_CASES.tsv: public PASS cases from frozen evidence.
- NEGATIVE_CASES.tsv: exact compiler rejection cases from Window E.
- BOUNDARY_CASES.tsv: exact boundary rows, including slash and namespace distinctions.
- NOT_PROVEN_CASES.tsv: known public gaps that must not be counted as FAIL.
- CONFLICTED_CASES.tsv: retained conflicts.
- PROVENANCE_MAP.tsv: frozen contract and evidence references.

No test was rerun for Window G. The 21 locked capabilities are preserved.
READY_FOR_PUBLIC_LANGUAGE_SPEC=NO.
