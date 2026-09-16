# REVIEW NOTES — INTERNET_AUTOLEARN_R1

## Reuse vs new code

This candidate does **not** recreate historical SIGMA cognition from prose. `DEPENDENCIES.lock` records the exact identities currently available from AIL-019 and cross-branch V10/V11/V12/I4/I5B/I5C evidence. Where exact native source bytes or interface identity are absent from GitHub, the dependency remains unresolved and the preflight path fails closed.

New code is limited to: a native composition envelope gate that does not invent semantic decisions; mechanical public-web transport; exact-byte content-addressed queue sealing; exact-SHA dependency resolution; Session R4 artifact-only guard; recovery supervision; static/negative/recovery harnesses.

## Host boundary

Host code can resolve hashes, enforce public-network safety, transport exact selected bytes, hash/store bytes, seal queue items, supervise exact workers, and dispatch only an exact already-native event class. It contains no query generation, semantic ranking, source/resource fallback, summarization, truth decision, learning policy, or canonical writer.

## Same-task recovery

The durable descriptor binds `WORK_ID`, exact entrypoint path/hash, completion receipt, recovery lock, checkpoint pointer, in-flight operation id, native-event path, retry bound, and `CANONICAL_MUTATION=NO`. Recovery verifies descriptor hash and entrypoint hash, takes a dedicated recovery lock, and restarts only that exact entrypoint. It never chooses another query/source/action.

## Duplicate-effect prevention

Network request IDs and queue item IDs are content-addressed. Queue publication uses staging + fsync + atomic rename + final `SEALED` marker; replay of the same item returns idempotent reuse. Partial staging directories are not visible under `sealed/`.

## Local trainer coexistence

Session guard requires `READ_PLUS_ARTIFACT_WRITE` and rejects any session where brain/state/model/learn/commit/head/model-generation mutation is not `REJECT`. The Internet lane therefore cannot become a second canonical writer in R1.

## Native compact bytes

`seal_queue.py` copies the native output byte-for-byte and records its SHA256. It does not decode, paraphrase, summarize, re-rank, or rewrite native payload bytes. A native condenser remains an unresolved exact dependency until exact bytes/interfaces are reviewed.

## Static verification commands

```text
bash src/verify/manifest_verify.sh
bash src/verify/static_audit.sh
bash src/verify/negative_tests.sh
bash src/verify/recovery_idempotency_verify.sh
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Candidate limitation that must survive review

`GENERAL_ARBITRARY_WEBSITE_NATIVE_SELECTION=NOT_PROVEN_BY_CURRENT_RESOLVED_BYTES`
`NATIVE_ABSTRACTIVE_CONDENSER=DEPENDENCY_MISSING_NOT_PROVEN`
`LOCKED_SIGMAC_COMPILE=NOT_RUN_ON_OPPO`
`LOCKED_VM_RUNTIME=NOT_RUN_ON_OPPO`
`REAL_INTERNET_TEST=NOT_RUN_ON_OPPO`
`ANDROID_KILL_RECOVERY=NOT_RUN_ON_OPPO`
`PRODUCTION_INSTALL=NO`

## Side-effect IDs and crash windows

`host/operation_id.py` provides content-addressed IDs for exactly `FETCH`, `DECODE`, `NATIVE_INPUT`, `NATIVE_OUTPUT`, `PERSIST_RECORD`, and `QUEUE_ITEM`; unknown operation classes are rejected. `verify/crash_window_matrix.sh` maps the six request-defined crash windows to committed mechanics. This is static/local design evidence only; Android/Termux kill testing remains `NOT_RUN_ON_OPPO`.
