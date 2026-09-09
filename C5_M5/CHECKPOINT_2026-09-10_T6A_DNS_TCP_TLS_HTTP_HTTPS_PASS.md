# SIGMA Gate B — T6A DNS/TCP/TLS/HTTP/HTTPS PASS

Updated: 2026-09-10 after genuine OPPO admission PASS.

## Exact admitted artifact

- source SHA256: `e01f8ba8a1e8a42ff6474d3d0f1c739328a9c8a59ad8b42fa97d83041e73abd1`
- binary SHA256: `3b2cdeb0cb18d5105e8a8adb6f2d5f7b90042815b83cf651d634c14d37066660`
- compiler: `/data/data/com.termux/files/usr/bin/clang++`

## Exact admitted scope

- DNS resolution;
- bounded TCP request/response exchange;
- TLS request/response exchange with peer trust verification;
- TLS hostname verification;
- basic HTTP GET;
- basic HTTPS GET;
- response-body size bound.

All admission traffic used loopback servers created after source/binary freeze. TLS certificate/trust-anchor material was generated dynamically after freeze. External Internet was not used.

## Machine evidence

- `DETERMINISTIC_COMPILE=PASS`
- `SOURCE_HASH_FREEZE=PASS`
- `BINARY_HASH_FREEZE=PASS`
- `HIGH_ENTROPY_LITERAL_LEAK_AUDIT=PASS`
- `DYNAMIC_LOOPBACK_SERVERS_AFTER_FREEZE=PASS`
- `DYNAMIC_TLS_CERT_AFTER_FREEZE=PASS`
- directed cases: `16`
- randomized-after-freeze cases: `32`
- replay cases: `2`
- total admission cases: `50`
- total native process invocations: `52`
- `POST_TOOL_MECHANICAL_ORACLE=PASS`
- `DNS_RESOLUTION=PASS`
- `TCP_BOUNDED_EXCHANGE=PASS`
- `TLS_PEER_AND_HOSTNAME_VERIFICATION=PASS`
- `HTTP_BASIC_GET=PASS`
- `HTTPS_BASIC_GET=PASS`
- `BODY_SIZE_BOUND=PASS`
- `COUNTERFACTUAL_BEHAVIOR_CHANGE=PASS`
- `SYNTHETIC_SANDBOX_REMOVED=PASS`

## Anti-hardcoding / cognition boundary

- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`
- `HOST_ENDPOINT_SELECTION=NO`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `CORE_TEST_ORACLE_CONTAMINATION=NO`
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`

The native transport tool executes caller-supplied mechanical transport parameters only. It does not decide which endpoint, URL, source, query, content, or evidence is relevant.

## Production boundary

- `EXTERNAL_INTERNET_USED=NO`
- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

## Current layer state

- `T6A_DNS_TCP_TLS_HTTP_HTTPS_ADMISSION=PASS`
- `T6_FULL_LAYER=NOT_YET_ADMITTED`

Next offline gate: T6B advanced HTTP/flow control — Range, chunked streaming, redirects, ETag/If-Range/conditional fetch, timeout, retry, rate-limit and backpressure — then exact T6A+T6B combined compatibility.
