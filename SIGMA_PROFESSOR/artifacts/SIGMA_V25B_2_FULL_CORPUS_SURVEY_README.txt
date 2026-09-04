SIGMA V2.5B.2 FULL-CORPUS SURVEY — FILTERED + BATCHED

Why V2.5B.1 is not continued:
- User stopped after cycle 47.
- Output exposed a structural data-quality failure:
  BEST_LOCAL_RELATION  =>
  BEST_LOCAL_SUPPORT 110
- Cause: str_split(line, " ") can produce empty tokens from repeated/leading spaces.
- Empty-token relations could dominate the structural survey.
- Existing V2.5B.1 survey records are preserved as tainted evidence; they are not deleted or promoted.

V2.5B.2 changes:
1. Native empty-token gate:
   LEFT == "" or RIGHT == "" => relation is skipped.
2. Tracks SKIPPED_EMPTY_RELATIONS.
3. Fresh derived survey namespace:
   .sigma_exec/SIGMA_V25B2_DOCUMENT_SURVEY.memory
   Raw corpus is unchanged.
4. Reuses the frozen 56-document snapshot.
5. Runs at most 5 VM cycles per invocation to avoid output flooding.
   Rerun the same runner for the next batch.
6. Crash-isolating append framing:
   each valid committed record starts with a newline and ends with || COMMIT=YES.
   A partial interrupted append therefore cannot silently become the next valid record.
   append_text is still not claimed atomic.

Source SHA256:
b260544d4afdf8787a2653ee4b3350a6b76663c4377252623638db82e2502d3b

Runner SHA256:
6ec22ed2b0df2ac2fe854daccd1f9821f20e96ab164050303a64a8e05c8f6364

Static checks:
H_CALL_ARITY_AUDIT=PASS
STR_STARTS_DEPENDENCY=NONE
DIRECT_STR_DEPENDENCY=NONE
BASH_N_RC=0

Admission requirement:
- no BEST_LOCAL_RELATION may be an empty-token relation;
- all cycles VM_RC=0;
- after repeated batches COMMITTED_SURVEY_COUNT == SNAPSHOT_DOCUMENT_COUNT;
- SURVEY_COMPLETE YES;
- HOST_LEARNING=NO;
- HOST_DOCUMENT_SELECTION=NO;
- production state untouched.

SEMANTIC_UNDERSTANDING=NOT_PROVEN
