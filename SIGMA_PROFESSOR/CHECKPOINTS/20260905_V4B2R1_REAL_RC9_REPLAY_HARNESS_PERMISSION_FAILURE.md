# V4-B2R.1 REAL V2.4 RC9 REPLAY — HARNESS PERMISSION FAILURE

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Result

`V4B2_REAL_V24_RC9_HELD_CONTEXT_REPLAY_PREFLIGHT=NOT_ADMITTED`

This is a harness/setup failure, not a native V4-B learner failure.

Observed transcript:

- locked SIGMAC SHA256 matched;
- locked VM SHA256 matched;
- V4-B source SHA256 matched `2edd2d4f36d3dd9c2d03dab4218ceff1f2ef290feee711a49ef18ff53b056ad4`;
- installed source matched;
- compile RC = 0;
- bytecode SHA256 = `b21e1f785987ec7547a459041742c4de3dee8350ed15e159c178dcb7eb58fc29`;
- production V2.4 PID before = `831`;
- first real context document SHA matched `49c16c567fcbd0df0241b249e2b51dbf8e20d23ec1dc78ff8d92e3233dda9382`;
- V2.4 `VM_RC=9` hold evidence matched;
- then mechanical copy to shadow `SIGMA_V4B1_CONTEXT_TEXT.memory` failed with `Permission denied` before the first real-context VM invocation.

## Root cause

V4-B2R.1 copied directly to `SIGMA_V4B1_CONTEXT_TEXT.memory` and then set that file to mode `0400`. A stale/reused shadow input file can therefore make a later preflight attempt fail before native execution.

This is a harness idempotency defect. It does not prove or disprove `REAL_V24_RC9_CONTEXT_RECOVERY`.

## Required correction

Use a fresh shadow namespace and install each exact production raw document via:

`partial file -> exact SHA verification -> chmod 0400 -> atomic rename to context input path`.

No host segment selection, completion decision, retry decision, or learning may be introduced.

## Locked status

`SEGMENTED_RECEIVED_CONTEXT_LEARNING=PROVEN_IN_BOUNDED_TESTED_SCOPE` remains admitted from V4-B.1.

`REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

Production V2.4 is not a write target and must remain running unchanged.
