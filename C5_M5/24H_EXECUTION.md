# SIGMA C5 M5 — Immediate Execution Ladder

This file exists so work can continue on-device even if chat access disappears.

## One-command ladder

Bundle: `SIGMA_C5_C5V3_M5_24H_EXECUTION_LADDER_R1_BUNDLE.zip`

Bundle SHA256: `87118eebdda1ee1af2d5bb247516905da26ded4f1ce60595c8da6e859fe32197`

Stages execute in strict dependency order and stop at the first non-zero RC:

1. `M5_MECHANICAL_EVIDENCE_TOOL_TRANSPORT_R2`
   - Core SHA256 `c3ec9d2436f965046ac53bc8b4dba67870f1fb937868d3b667cad6779ea51285`
   - Transport SHA256 `32c54f4f2f342652b27f4639b1b7ae74c4cc30f27a80bf202eebe309594ddb35`
   - Adds native recomputation of request from native gap state before provider invocation.
   - Retains all R1H2 boundedness/revision/freeze gates.
2. `M5_BLIND_HOST_SUBSTITUTION_R1`
   - Auditor SHA256 `25d9ae0401d7784672c7f284a710876bb5a5b9875743a8307f3c775131281045`
   - Tests forged correlated request, stale cross-gap request, raw protocol injection, irrelevant evidence and native-only revision.
3. `M5_NATIVE_GAP_SEARCH_QUERY_R1`
   - Core SHA256 `286b1c557a2cbe027d67fb645448bdd8ff09540d5a628b89517ef2a3fa38bd5f`
   - Search query bytes are produced inside SIGMA by verbatim serialization of the native unresolved gap pair.
   - Host query expansion/rewriting remains forbidden.
4. `M5_REAL_INTERNET_SEARCH_DISCOVERY_R1`
   - Same query core SHA256 `286b1c557a2cbe027d67fb645448bdd8ff09540d5a628b89517ef2a3fa38bd5f`
   - Fixed mechanical provider calls the English Wikipedia MediaWiki search API with native query bytes.
   - Raw compact search-response bytes are returned to native SIGMA; host does not summarize them.

## Stop discipline

A stage failure is evidence. Do not bypass it and do not run later stages on a broken dependency.

Logs are stored under:

`.sigma_c5/candidates/M5_EXECUTION_LADDER_R1_<timestamp>/`

## Claims after ladder

Even if all four stages PASS, only the transport/search-discovery substrate is established. The following remain FAIL until dedicated long-form blind tests pass:

- full source fetch/read;
- whole-work narrative understanding;
- evidence-backed whole-work summary;
- theme/human-value induction;
- multilingual narrative transfer;
- semantic compression after source deletion;
- continual learning from compressed local memory.

The next architecture after a fully passing ladder is a bounded transient long-form work stream followed by source-removal semantic retention tests. Do not return to sentence-fixture optimization as the primary goal.