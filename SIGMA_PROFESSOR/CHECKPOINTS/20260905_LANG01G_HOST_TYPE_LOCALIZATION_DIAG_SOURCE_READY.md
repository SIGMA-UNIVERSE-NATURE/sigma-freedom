# LANG-01G — NATIVE HOST-TYPE LOCALIZATION DIAGNOSTIC SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane: `TEACHER_GPT_LANGUAGE_LANE`
Status: `DIAGNOSTIC_SOURCE_READY / NOT_AN_ADMISSION`

Predecessor runtime failure checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_LANG01G_R2_RUNTIME_FAIL_CASE001_STRING_REQUIRED.md`

Purpose: localize the first locked-VM host primitive/argument type failure observed as `VM_RC=22` / `SIGMA host: string required` in `CASE_001_TIE` without changing the canonical LANG-01G lesson, its scoring policy, persistence policy, fixtures, or 20-case admission oracle.

Native diagnostic source:
`SIGMA_PROFESSOR/artifacts/SIGMA_LANG_01G_HOST_TYPE_LOCALIZATION_DIAG_V1.sigma`

- source commit: `d0da14b84e88f6c44c3ebcdcf7986984d022f01e`
- source Git blob: `53ca847aa3eebe77e18c404e8dad8b717c9234cb`

Diagnostic runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_LANG_01G_HOST_TYPE_LOCALIZATION_DIAG_V1.sh`

- runner commit: `afebab24827f6bd62126e359cc05e72b5a5b9928`
- runner Git blob: `fe96a52e92e5b1b77bf929374dcf586f226961d1`

Boundary:

- `DIAGNOSTIC_ONLY=YES`
- `CANONICAL_LANG01G_SOURCE_CHANGED=NO`
- `CANONICAL_ADMISSION_ORACLE_CHANGED=NO`
- `HOST_COGNITION=NO`
- `HOST_EVIDENCE_SCORING=NO`
- `HOST_ANTECEDENT_SELECTION=NO`
- `LOCKED_SIGMAC_VM_REQUIRED=YES`

The native diagnostic program emits ordered trace sentinels immediately before/after the host primitives used by the failing CASE_001 evidence/persistence path. The first sentinel without its corresponding after-sentinel localizes the failing primitive region. The runner supplies only the same mechanical two-candidate/two-evidence fixture shape and locked compiler/VM invocation.

This diagnostic is not a capability proof and cannot change `LANG_01G_ADMISSION=FAIL/NOT_ADMITTED` by itself.
