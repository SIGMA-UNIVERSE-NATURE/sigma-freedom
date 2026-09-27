# SIGMA V09 -> VKM R5A3 FIX1 Targeted Trainer/Curriculum Provenance Audit — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE

Root cause repaired:
- removed AUTO.rglob("*") over SIGMA_AUTOLEARN_ADMIN;
- original depth filter happened only after recursive traversal and therefore did not bound traversal cost.

FIX1 scan scope:
- exact current SEM68 candidate directory, max depth 2;
- exact current 06B3 curriculum directory, max depth 3;
- exact current data-vs-mechanism directory, max depth 2;
- matching files directly at SIGMA_AUTOLEARN_ADMIN top level only.

Progress markers:
R5A3_SCAN_PROGRESS=x_OF_y

Safety unchanged:
TRAINING_ALLOWED=NO
SEMANTIC_EXECUTION_ALLOWED=NO
CANONICAL_MUTATION_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
GIA_ADMISSION_ALLOWED=NO
DNA15_ALLOWED=NO

Release:
R5A3_FIX1_RELEASE_VERIFY=PASS
ZIP_SHA256=ed349269db5862c0f6148e2a715442a835aaaff9944a6e6841c1329d88ff0498

NEXT=RUN_R5A3_FIX1_TARGETED_AUDIT
