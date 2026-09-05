SIGMA V4-B.1 — SEGMENTED RECEIVED-CONTEXT LEARNER

Purpose
-------
Replace V2.4 whole-context NEW learning pressure with native bounded segment
progress. A received context is not considered learned merely because it was
fetched. It becomes complete only after every line segment has been committed.

Native behavior
---------------
- exact context id + text input;
- native cursor recovery bound to context id;
- two context lines per VM invocation;
- per-segment structural profile: relation occurrences, first-encounter
  highest-support bigram, unary support/occurrence counts;
- append-only segment evidence;
- append-only cursor ledger;
- append-only completion ledger;
- fresh-VM resume;
- evidence-only crash retry without duplicate segment evidence;
- final-cursor / missing-completion recovery without empty-segment duplication;
- syntactically valid out-of-range cursor refusal;
- malformed/foreign cursor filtering;
- bounded refusal for >65 context lines or >65 tokens in a selected line.

Admission boundary
------------------
This is structural learning progress only. It does not prove semantic
understanding, semantic truth, bounded file I/O, or that all real V2.4 rc=9
held contexts are recoverable. The next gate must replay real held contexts.

Claim after PASS
----------------
`SEGMENTED_RECEIVED_CONTEXT_LEARNING=PROVEN_IN_BOUNDED_TESTED_SCOPE`

Still
-----
`REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN`
`V4_PRODUCTION_PROMOTION_ALLOWED=NO`
`BOUNDED_FILE_IO=NOT_PROVEN`
`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

Native source SHA256
--------------------
2edd2d4f36d3dd9c2d03dab4218ceff1f2ef290feee711a49ef18ff53b056ad4

Runner SHA256
-------------
1ca13459579fb066d9c179f1befb1013a495a5cb2b4f4919bb7031465126e2f1

Static
------
H_CALL_ARITY_AUDIT=PASS
NATIVE_NOT_EQUAL_DEPENDENCY=NONE
STR_STARTS_DEPENDENCY=NONE
DIRECT_STR_DEPENDENCY=NONE
STR_LEN_DEPENDENCY=REQUIRED_AND_PREVIOUSLY_RUNTIME_PROVEN_IN_V222_SCOPE
BASH_N_RC=0
