# V2.8D.1 file_exists boolean-render hardening

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

Before device execution, static review found that the original V2.8D.1 candidate stored the raw `file_exists` boolean directly in `DOCUMENT_EXISTS` and the runner expected protocol text `DOCUMENT_EXISTS 1`.

Locked-VM boolean print rendering had not been characterized. Runtime logic should not depend on how a boolean is displayed.

Hardening applied before admission:

Old shape:

```sigma
⚡ DOCUMENT_EXISTS:
    H("file_exists", DOCUMENT_PATH, NULL, NULL);
```

New shape:

```sigma
⚡ DOCUMENT_EXISTS:
    0;

⚡ DOCUMENT_EXISTS_RAW:
    H("file_exists", DOCUMENT_PATH, NULL, NULL);

IF (DOCUMENT_EXISTS_RAW) {
    ⚡ DOCUMENT_EXISTS:
        1;
}
```

The rest of the engine uses numeric `DOCUMENT_EXISTS=0/1`.

No curriculum, document-selection, segment-selection, learning, evidence, or priority policy changed.

New exact candidate identities:

- source SHA256: `3da9195db5cf24fb3bc5094823ca13e52caa4335b6605c185e7921033079e8ce`
- runner SHA256: `7b53912116383027bcba00fa6393ded61d2de0b74a7219af36148bfd2273353a`

Static checks:

- H_CALL_ARITY_AUDIT=PASS
- NATIVE_NOT_EQUAL_DEPENDENCY=NONE
- STR_STARTS_DEPENDENCY=NONE
- DIRECT_STR_DEPENDENCY=NONE
- FILE_EXISTS_BOOL_RENDER_DEPENDENCY=NONE
- runner bash -n RC=0

Admission remains NOT_PROVEN until locked-device execution.
