# V4-B.1 SEGMENTED RECEIVED-CONTEXT LEARNER — SOURCE READY

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Frontier

V4-A.1 native productivity/work arbitration is admitted PASS at commit:
`b9f23d3a6a94116818581458fbdb8e788deb2804`

V4-B.1 is now SOURCE READY but NOT runtime-admitted.

`SEGMENTED_RECEIVED_CONTEXT_LEARNING=NOT_YET_PROVEN`

`REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

## Native source

Path:
`SIGMA_PROFESSOR/artifacts/SIGMA_V4_SEGMENTED_RECEIVED_CONTEXT_LEARNER_V4B1.sigma`

SHA256:
`2edd2d4f36d3dd9c2d03dab4218ceff1f2ef290feee711a49ef18ff53b056ad4`

Git blob:
`5aa839c07970f2f5de3c14c4b92fbd465a687f4c`

Hardening commit:
`f0a80c2833054eb3dfefb530612e04fff006f6f2`

## Runner

Path:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4B1_SEGMENTED_RECEIVED_CONTEXT_LEARNER_PREFLIGHT.sh`

SHA256:
`1ca13459579fb066d9c179f1befb1013a495a5cb2b4f4919bb7031465126e2f1`

Git blob:
`4faf37671c591f7201c930bc5f000a542d377d8a`

Hardening commit:
`c0b87b45e12575fd147881d3a19fd041f9909e04`

README update commit:
`1f92e954fabe6f543d301265e8a5f7842e870039`

## Static gates

`H_CALL_ARITY_AUDIT=PASS`

`NATIVE_NOT_EQUAL_DEPENDENCY=NONE`

`STR_STARTS_DEPENDENCY=NONE`

`DIRECT_STR_DEPENDENCY=NONE`

`STR_LEN_DEPENDENCY=REQUIRED_AND_PREVIOUSLY_RUNTIME_PROVEN_IN_V222_SCOPE`

runner `bash -n` RC = 0.

## Native policy under test

- exact received context id + text;
- native two-line segment selection;
- persistent append-only cursor ledger bound to context id;
- append-only segment structural evidence;
- append-only completion ledger;
- context is not LEARNED until all segments complete;
- fresh-VM cursor resume;
- malformed/foreign cursor filtering;
- evidence-only crash retry without duplicate segment evidence;
- final-cursor / missing-completion recovery without an empty duplicate segment;
- syntactically valid cursor beyond context length is refused;
- >65 context lines refused;
- >65 tokens in selected line refused;
- shadow state only; no production-BRAIN test mutation.

## Required runtime gates

- 5-line context progresses 2 + 2 + 1 across fresh VM invocations;
- first segment identifies bounded structural relation profile;
- completion stays false until final segment;
- malformed cursor tail ignored and last valid cursor recovered;
- already-complete replay is idempotent;
- evidence-only crash replay does not duplicate evidence;
- foreign-context cursor ignored;
- token-limit refusal with no learning mutation;
- context-line-limit refusal with no learning mutation;
- final-cursor / missing-completion recovery appends completion only;
- out-of-range cursor refusal;
- production V2.4 same PID before/after;
- all VM invocations rc0;
- host segment/completion/retry/learning decisions remain NO.

## Claim boundary after future PASS

May admit only:

`SEGMENTED_RECEIVED_CONTEXT_LEARNING=PROVEN_IN_BOUNDED_TESTED_SCOPE`

Must still keep:

`REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN`

`BOUNDED_FILE_IO=NOT_PROVEN`

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

Next after PASS: replay real V2.4 `rc=9` held contexts through V4-B in isolated shadow state and compare completion/progress against V2.4 failure evidence.
