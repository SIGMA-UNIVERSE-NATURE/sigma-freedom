# V4-B2 real rc9 context characterization — 49c16...

Date: 2026-09-05 Asia/Ho_Chi_Minh

Production V2.4 remains baseline and must remain running unchanged.

Observed real held context:

`49c16c567fcbd0df0241b249e2b51dbf8e20d23ec1dc78ff8d92e3233dda9382`

Exact raw document SHA256 matched filename/context id.

Mechanical characterization supplied from Termux:

- `DOCUMENT_BYTES=3948`
- `DOCUMENT_LINES=10`
- `MAX_TOKENS_PER_LINE=209`
- `MAX_TOKEN_LINE_NUMBER=2`
- per-line token counts: `77, 209, 50, 0, 25, 29, 0, 71, 124, 74`
- total tokens by the same whitespace-field characterization: `659`
- with a structural 16-token window, this document requires 45 non-empty-line token windows.

Prior V4-B1 real replay result:

- native VM was reached;
- native status: `REFUSE_TOKEN_LIMIT`;
- cursor/evidence/completion commit counts all remained 0;
- therefore no partial learning mutation occurred;
- `REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN`.

Conclusion:

The observed production blocker is not context line count. The blocker is line-local token width: V4-B1 segmented by two lines per invocation but still required each selected line to be <=65 tokens. A production line reached 209 tokens.

Required successor design:

- native cursor must persist `(line_index, token_offset)`;
- native learner must process bounded token windows rather than whole selected lines;
- host must not split tokens, choose windows, decide retry, or decide completion;
- cross-window bigram continuity must be preserved exactly once;
- malformed/foreign progress records must remain ignorable;
- progress-with-missing-completion recovery must remain idempotent;
- whole-file / whole-selected-line split behavior remains an ABI limitation and must not be mislabeled bounded file I/O.

Claims remain:

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`
`BOUNDED_FILE_IO=NOT_PROVEN`
`REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN`
`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

Next action:

Build and admit V4-B3 native token-window resumable received-context learner, then replay the same exact held production context before attempting the remaining observed rc9 contexts.
