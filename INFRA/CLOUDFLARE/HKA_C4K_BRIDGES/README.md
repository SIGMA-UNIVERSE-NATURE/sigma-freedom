# HKA C4K Bridges

Server-side bridge implementation for Amendment 1.2.

- `production/`: create-only writes to `hka-c4k-staging`.
- `qa/`: exact binary reads from staging and QA evidence writes to `hka-c4k-audit`.
- `release/`: durable QA-gated copy/verify/release into `hka-c4k-vault`; preserves bucket-lock rules and updates GitHub Release Index.

Workers use explicit R2 bindings rather than exposing R2 credentials to ChatGPT windows. Bearer credentials and release/GitHub secrets are Worker secrets set by CI.

`hka-c4k-delivery` is intentionally not bound. Delivery remains gated by `WEB_APPROVED`.
