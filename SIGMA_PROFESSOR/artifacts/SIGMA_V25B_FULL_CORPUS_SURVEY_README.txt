SIGMA V2.5B FULL-CORPUS DOCUMENT SURVEY

Purpose:
- Promote the V2.5A.2 QA capability to a finite snapshot of the real raw corpus.
- Keep V2.4 production learner running.
- Freeze all *.document files present in production raw at initialization by exact mechanical copy.
- SIGMA, not the host, selects the first unsurveyed document from the sorted snapshot on every VM cycle.
- One document is surveyed per VM cycle.
- Survey computation is limited to at most 32 lines.
- Current read_text ABI still reads the whole file before the 32-line computation limit; this is explicitly NOT claimed as bounded file I/O.

Persistence improvement over V2.5A.2:
- One canonical append-only survey state file.
- A document is considered surveyed only when a record both matches DOC=<id> and ends with:
  || COMMIT=YES
- This avoids a two-file survey/marker consistency problem.
- append_text itself is still plain stdio and not a fully crash-atomic transaction.

Host boundary:
- HOST_LEARNING=NO
- HOST_DOCUMENT_SELECTION=NO
- Host snapshot operation mechanically copies ALL *.document files present at initialization.
- Host loop only supervises locked-VM invocations and stops on the exact SURVEY_COMPLETE protocol sentinel.

Native source SHA256:
9e49ef9ca44f63a0174ac4a08b467544449adba79cf09af356397cd0d25b6072

Runner SHA256:
9d029b846f3ec1fe5522ea34d9d7863aad1898f5ed439024a73ca9c4f5c520d4

Static checks:
H_CALL_ARITY_AUDIT=PASS
DIRECT_STR_DEPENDENCY=NONE
BASH_N_RC=0

PASS:
- every VM cycle RC=0;
- final COMMITTED_SURVEY_COUNT equals SNAPSHOT_DOCUMENT_COUNT;
- native output reaches SURVEY_COMPLETE YES;
- no production raw or V2.4 learner memory mutation.

Claim scope after PASS:
NATIVE_STRUCTURAL_FULL_CORPUS_SURVEY=PROVEN_FOR_FROZEN_SNAPSHOT
SEMANTIC_UNDERSTANDING=NOT_PROVEN
