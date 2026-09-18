# Native + Canonical + Autolearn Snapshot Contract

Snapshot branch: `snapshot/native-canonical-autolearn-20260919`

Expected canonical autolearn source set:

- ID: `SIGMA_AUTOLEARN_SOURCE_SET_R1`
- SHA256: `e098214deef5ba488954d6f9799fcdd350bf5df25b7b9f7b1d0e15f900b3efc5`
- Sources: 2
- Train files: 35
- Total word tokens: 5,500,047

Required payload:

1. `RUNTIME/native-source/` — Native SIGMA source and build metadata.
2. `RUNTIME/native-build/` — exact Native binaries used by the runtime.
3. `DATA/CANONICAL_SOURCE_BUNDLES/` — immutable canonical source bundles.
4. `DATA/CANONICAL_SOURCE_REGISTRY/` — manifests, per-file SHA256 lists, source-set env/fingerprint.
5. `AUTOLEARN/SINGLE_SIGMA_R1/` — durable learned-state backend/checkpoint files.

Rules:

- Preserve canonical bundle bytes exactly.
- Preserve provenance boundaries between source bundles.
- Do not commit session workspaces, tmux state, temporary locks, or transient build caches.
- Verify the source-set fingerprint before upload.
- This snapshot does not itself assert model promotion or canonical model mutation.
