# V4-B3R.1 exact real 49c16 rc9 replay — SOURCE READY

Date: 2026-09-05 Asia/Ho_Chi_Minh

Prerequisite admitted:
`TOKEN_WINDOW_RECEIVED_CONTEXT_LEARNING=PROVEN_IN_209_TOKEN_LINE_BOUNDED_TEST_SCOPE`

V4-B3 runtime PASS checkpoint:
`0cfc855068ce0f5b7d0952ff3c00575f751007a0`

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_V4_TOKEN_WINDOW_RECEIVED_CONTEXT_LEARNER_V4B3.sigma`

Native source SHA256:
`8a5687b4e83d74947dd9b1ca1a2729be104eff3d4b935cc64c6ef800f628af83`

Native source Git blob:
`a20279d529422c3c380fc832babd89fd6fe6e34b`

Real replay runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4B3R1_REAL_49C16_RC9_REPLAY_PREFLIGHT.sh`

Runner Git blob:
`966b721f2fad86b5b8deb90270957c90ba9942f4`

Runner commit:
`58eca425200d74355b9907468b2342e2444bf703`

Exact production context:
`49c16c567fcbd0df0241b249e2b51dbf8e20d23ec1dc78ff8d92e3233dda9382`

Observed production evidence:
- V2.4 hold marker must contain exact context id, `VM_RC=9`, and locked VM SHA;
- raw document SHA must equal the context id;
- mechanically characterized raw document: 3948 bytes, 10 awk-observed lines, max 209 whitespace fields on one line, 659 whitespace fields total.

Replay protocol:
- unique isolated shadow namespace per run;
- exact raw bytes mechanically copied using partial -> hash -> chmod 0400 -> atomic rename;
- fixed 64 locked-VM invocations; host does not inspect native status to decide continuation or stopping;
- native V4-B3 owns line/token cursor, window selection, progress and completion;
- after fixed invocations, completion must exist exactly once and final native status must be `ALREADY_COMPLETE`;
- no native `REFUSE_*` status may occur;
- exact production raw document and hold marker hashes must remain unchanged;
- production V2.4 PID must remain identical before/after.

No runtime claim yet:
`REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN`

Still:
`V4_PRODUCTION_PROMOTION_ALLOWED=NO`
`BOUNDED_FILE_IO=NOT_PROVEN`
`SEMANTIC_UNDERSTANDING=NOT_PROVEN`
