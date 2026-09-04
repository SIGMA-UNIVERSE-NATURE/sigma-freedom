# V2.8D.1 SELECTED WORK -> DEEP RE-LEARN — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

Dependency admission:
- V2.8R.1 real survey -> curriculum bridge: PASS.
- first native-selected real work in frozen 56-document snapshot: `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`.
- admitted V2.8R.1 source SHA256: `8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8`.
- observed admitted V2.8R.1 bytecode SHA256: `0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5`.

New native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_SELECTED_WORK_DEEP_RELEARN_V2_8D1.sigma`

SOURCE_SHA256:
`3dfc25c5f6e9cdbabd193bb7c3d8845ba025cb12e1b3824430a1a6ec280ec74f`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V28D1_SELECTED_WORK_DEEP_RELEARN_PREFLIGHT.sh`

RUNNER_SHA256:
`461f4ca50add41e067a9402a64e2f7451b47c4491d08f3cc7b5f51b1c987f059`

Static checks:
- H_CALL_ARITY_AUDIT=PASS
- NATIVE_NOT_EQUAL_DEPENDENCY=NONE
- STR_STARTS_DEPENDENCY=NONE
- DIRECT_STR_DEPENDENCY=NONE
- runner bash -n RC=0

Admission design:
1. rerun exact admitted V2.8R.1 natively against the real V2.5B.2 survey to produce the selected real work;
2. deep engine reads that selected work directly;
3. deep engine receives only the snapshot directory as mechanical config and constructs the document path natively;
4. deep engine processes fixed 8-line windows with persistent cursor;
5. deep evidence persists work identity + cursor identity + best local structural relation + COMMIT=YES;
6. committed work/cursor evidence is deduplicated before append;
7. fresh VM must resume the next segment;
8. deterministic replay must reproduce evidence SHA;
9. empty selection and over-budget evidence state must refuse mutation;
10. real survey and selected snapshot document must remain immutable.

New mechanical ABI admission exercised:
`file_exists` locked-VM runtime support.

Current truth:
- COMPILE_PASS=NOT_PROVEN
- RUNTIME_PASS=NOT_PROVEN
- BYTECODE_SHA256=UNKNOWN
- ADMISSION=NOT_PROVEN
- SEMANTIC_IMPORTANCE=NOT_PROVEN
- SEMANTIC_UNDERSTANDING=NOT_PROVEN
- BOUNDED_FILE_IO=NOT_PROVEN
- MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN

Next action:
Run the exact V2.8D.1 source + runner on the locked Termux runtime and preserve all output/evidence.
