# V2.5B.1 EMPTY-TOKEN CONTAMINATION + V2.5B.2 REPAIR

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Evidence

V2.5B.1 successfully progressed through full-corpus survey cycles on the frozen 56-document snapshot. User stopped after observing cycle 47.

Observed output:

- `VM_RC=0`
- `COMMITTED_SURVEY_COUNT_BEFORE=46`
- document `ccfdecb4cd296cd18d5d44c53be4638b027b212a2c6df2372abd350e2782efac`
- `LINE_TOTAL=63`
- `SURVEY_LINE_LIMIT=32`
- `BEST_LOCAL_RELATION= =>`
- `BEST_LOCAL_SUPPORT=110`

## Interpretation

The empty-looking best relation demonstrates a structural data-quality defect: `str_split(line, " ")` can emit empty tokens from repeated or leading spaces, and adjacent empty-token relations can dominate local support.

Therefore:

`V25B1_STRUCTURAL_PROFILE_QUALITY=FAIL`

Do not promote V2.5B.1 survey records as valid structural profiles. Preserve them as tainted evidence; do not delete them.

This is NOT evidence of semantic understanding.

## V2.5B.2 repair

- Native empty-token gate: skip any relation where `LEFT == ""` or `RIGHT == ""`.
- Track `SKIPPED_EMPTY_RELATIONS`.
- Fresh derived survey namespace: `.sigma_exec/SIGMA_V25B2_DOCUMENT_SURVEY.memory`.
- Reuse the same frozen 56-document snapshot.
- Batch runner executes at most 5 VM cycles per invocation to avoid output flooding.
- Crash-isolating append framing: each committed record begins with a newline and ends `|| COMMIT=YES` so a partial interrupted append cannot silently merge into the next valid record.
- `append_text` remains non-atomic; atomic persistence is still NOT proven.

Source SHA256:
`b260544d4afdf8787a2653ee4b3350a6b76663c4377252623638db82e2502d3b`

Runner SHA256:
`6ec22ed2b0df2ac2fe854daccd1f9821f20e96ab164050303a64a8e05c8f6364`

Static checks:

- `H_CALL_ARITY_AUDIT=PASS`
- `STR_STARTS_DEPENDENCY=NONE`
- `DIRECT_STR_DEPENDENCY=NONE`
- `BASH_N_RC=0`

## Admission target

After repeated batches:

- every VM cycle `RC=0`;
- no empty-token best relation;
- committed survey count equals 56;
- SIGMA emits `SURVEY_COMPLETE YES`;
- production raw and V2.4 learner memory remain unmodified;
- `HOST_LEARNING=NO`;
- `HOST_DOCUMENT_SELECTION=NO`.

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`
