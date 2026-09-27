# SIGMA V09 -> VKM R5A3 Interrupted — Unbounded Read-Only Traversal

Date: 2026-09-27
Source: user-supplied Termux runtime output.
Branch: SIGMA_LIFE

Observed output reached identity/toolchain continuity and then the user interrupted with Ctrl+C before any R5A3 audit result markers.

Classification:

R5A3_TRAINING_PERFORMED=NO
R5A3_SEMANTIC_EXECUTION_PERFORMED=NO
R5A3_NATIVE_RUNTIME_STARTED=NO
R5A3_RESULT=INTERRUPTED_DURING_HOST_READ_ONLY_SCAN
FAILURE_CLASS=HARNESS_UNBOUNDED_TRAVERSAL_BUG

Root cause:
The R5A3 Python auditor used AUTO.rglob("*") and only applied a depth filter after traversal. Path-depth filtering did not prevent recursive filesystem walking, so the read-only scan could traverse a much larger SIGMA_AUTOLEARN_ADMIN tree than intended.

This is not SIGMA failure evidence and not trainer failure evidence.

Repair:
- remove AUTO.rglob("*");
- scan only exact already-resolved current target directories/files;
- cap candidate-dir traversal to max depth 2;
- cap curriculum-dir traversal to max depth 3;
- scan only selected top-level AUTO metadata/current files;
- preserve all read-only/no-training/no-mutation rules.

NEXT=R5A3_FIX1_TARGETED_PROVENANCE_BODY_AUDIT
