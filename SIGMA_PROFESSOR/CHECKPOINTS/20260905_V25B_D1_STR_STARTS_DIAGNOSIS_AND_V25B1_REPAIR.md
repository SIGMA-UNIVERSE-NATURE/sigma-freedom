# V2.5B D1 str_starts diagnosis + V2.5B.1 repair

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Failure evidence

V2.5B full-corpus survey initialized a frozen snapshot of 56 `.document` files and compiled successfully, but cycle 1 failed on the locked VM:

- `SIGMAC_RC=0`
- V2.5B bytecode SHA-256: `bc7bc28a96a5223fb00c4295513b7a1cde2c12aa8aec82448d8307f714c42307`
- `COMMITTED_AT_START=0`
- `VM_RC=22`
- error: `SIGMA host: integer required`
- production raw mutation: NO
- production learner memory mutation: NO

## D1 diagnostic

Diagnostic source SHA-256:

`877ab98ec2caf916741a4953e812109170742c97b7526725d68b7e0500bd2fc7`

Diagnostic compiled bytecode SHA-256 on device:

`1e81197b42f9dee26e3c06989cba71f577eb3dab9f5ec69dc65ffd7d5130a0af`

The last diagnostic marker before the host error was:

`D1_STAGE BEFORE_OLD_RECORD_STR_STARTS`

Markers immediately before it proved successful locked-VM execution through:

- `read_text`
- `listdir`
- `list_sort`
- `list_len`
- `str_split`
- `list_get`
- `str_ends`
- `str_replace`

The failing call-site was therefore isolated to:

`host("str_starts", OLD_RECORD, DOC_PREFIX, NULL)`

`COMMITTED_AT_END=0`, so no committed survey state requires rollback.

Important claim discipline:

- `str_starts` support with this argument contract is NOT PROVEN.
- Do not infer its exact intended ABI from the error alone.

## V2.5B.1 repair

V2.5B.1 removes the `str_starts` dependency entirely.

Survey record identity matching is now implemented natively with already exercised primitives:

1. `str_split(OLD_RECORD, " || ")`
2. `list_len(parts)`
3. `list_get(parts, 0)`
4. exact equality against `"DOC=" + DOC_ID`

No semantic policy changes.

Native source SHA-256:

`24d6e762dc4fffde15ef911a11602094f5b2b948c0727a935c7993ee71932607`

Runner SHA-256:

`c1c03de90de5f87817eddb00b30bfe360d915f4d82035358708dc68b14ecb112`

Static checks:

- `H_CALL_ARITY_AUDIT=PASS`
- `STR_STARTS_DEPENDENCY=NONE`
- `DIRECT_STR_DEPENDENCY=NONE`
- runner `bash -n`: PASS

State policy:

- reuse existing frozen 56-document snapshot;
- reuse existing canonical V2.5B survey state;
- at repair time committed count remains 0;
- keep V2.4 production learner running;
- do not mutate production raw or V2.4 learning memory.

Admission target:

- all survey VM cycles `RC=0`;
- final committed survey count equals 56;
- native `SURVEY_COMPLETE YES`;
- `HOST_LEARNING=NO`;
- `HOST_DOCUMENT_SELECTION=NO`;
- semantic understanding remains NOT PROVEN.

## Next action

Install/run V2.5B.1 on the locked VM. If PASS, checkpoint full-corpus survey and proceed to V2.6 bounded segment cursor + crash/restart resume.