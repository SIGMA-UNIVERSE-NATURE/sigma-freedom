SIGMA V2.5A.1 DOCUMENT SURVEY PREFLIGHT

Repair from V2.5A:
- Fixed wrapper arity for str_replace.
- Before: H("str_replace", SELECTED_FILE, ".document", "", NULL) -> 5 arguments.
- After:  H("str_replace", SELECTED_FILE, ".document", "") -> 4 arguments.
- No survey policy change.
- No production learner namespace mutation.
- Static H-call arity audit: PASS; every H invocation has exactly 4 arguments.

V2.5A failure evidence:
VM_RC=8
SIGMA C VM: arg mismatch for H
No survey state was written.

Source SHA256:
210b1227f2805ddd460f95db89dd71258f84ba5a892aa5b50787cea84cf3eb85

Runner SHA256:
7ab3f2b157aa21d2effc3eeff7b6ae816e5ae88d27f32a15ffaaf1d840796ed3

HOST_LEARNING=NO
HOST_DOCUMENT_SELECTION=NO
SEMANTIC_UNDERSTANDING=NOT_PROVEN
