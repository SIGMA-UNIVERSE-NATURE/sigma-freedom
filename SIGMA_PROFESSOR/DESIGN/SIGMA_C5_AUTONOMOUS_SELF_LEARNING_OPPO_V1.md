# SIGMA C5 — Autonomous Self-Learning on Oppo + Self-Initiated Internet V1

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Status: DESIGN + COMPLETE IMPLEMENTATION CANDIDATE / RUNTIME NOT YET PROVEN
Runtime root: `$HOME/SIGMA/sigma_genesis1`

## User requirement

Run SIGMA from the existing `sigma_genesis1` installation on the Oppo device. SIGMA must learn from material already stored under `$HOME/SIGMA`. SIGMA may request Internet material while local work still exists when native SIGMA itself generates the request. No Git branch/worktree is part of the runtime path.

## Ownership invariant

All cognitive arrows remain native SIGMA under the locked VM:

```text
SIGMA_NATIVE_OWNS_WORK_ACCEPTANCE=YES
SIGMA_NATIVE_OWNS_SEGMENT_ANALYSIS=YES
SIGMA_NATIVE_OWNS_EVIDENCE_UPDATE=YES
SIGMA_NATIVE_OWNS_KNOWLEDGE_PROMOTION=YES
SIGMA_NATIVE_OWNS_EXTERNAL_QUERY_GENERATION=YES
SIGMA_NATIVE_OWNS_NEXT_ACTION=YES
HOST_LEARNING=NO
HOST_QUERY_GENERATION=NO
HOST_KNOWLEDGE_PROMOTION=NO
HOST_SEMANTIC_INTERPRETATION=NO
```

The mechanical bridge may enumerate filesystem records, hash exact identifiers/bytes, maintain SQLite routing/index state, read exact bounded byte ranges, perform format/protocol decode, execute exact actions already emitted by native SIGMA, and transport exact network queries/responses.

## Runtime layout

```text
$HOME/SIGMA/sigma_genesis1
  native/sigmac
  native/sigma-vm.v09_candidate
  .sigma_native/knowledge_v2             existing memory, read as local material, not overwritten by C5
  .sigma_c5/
      src/
      tools/
      bin/
      runtime/.sigma_exec/
      catalog/catalog.sqlite3
      state/state.sqlite3
      external/cache/
      external/raw_json/
      decoded/
      log/
```

C5 does not require a second Git worktree and does not copy the approximately 10 GB archive into a second corpus.

## Local archive

The mechanical catalog enumerates regular non-symlink files under `$HOME/SIGMA`, excluding only C5's own `.sigma_c5` runtime subtree to prevent self-recursion. Entry identity is mechanically derived from exact path bytes plus device/inode/size/mtime_ns metadata.

Catalog records are bounded and opaque:

```text
ENTRY_ID=... || PATH_B64=... || SIZE=... || MTIME=... || STATE=... || POLICY=...
```

Security/result/control policy classes are mechanical governance holds, not semantic curriculum ranking. `LEARN` records are offered to native SIGMA. `SECURITY_HOLD`, `RESULT_HOLD`, and `CONTROL_HOLD` remain visible and are held rather than silently ingested. Git internal `.git/**` data is catalog-visible but mechanically classified `CONTROL_HOLD` rather than wasting learning cycles on Git object internals.

## Bounded material transport

Native SIGMA emits `READ_LOCAL_SEGMENT` or `READ_EXTERNAL_SEGMENT` plus a target record and a native-requested byte budget. The mechanical bridge validates path/version/root, reads a bounded exact UTF-8 byte prefix, limits line count mechanically, computes segment SHA/ID, and returns exact bytes plus transport metadata.

Native SIGMA decides whether to accept the segment, reduce the requested byte budget, hold the entry, analyze evidence, continue, or finish the entry. The host advances the byte offset only after native SIGMA emits `COMMIT_SEGMENT`. Offset arithmetic and SQLite transaction persistence are mechanical.

Default native segment budget ladder:

```text
16384 -> 8192 -> 4096 -> 2048 -> 1024
```

Native reduction occurs only when runtime density exceeds the bounded line/token envelope. A file that still cannot fit at the minimum budget is held instead of forcing a pass.

## Native learning rule in this revision

For each accepted segment, native SIGMA normalizes bounded structural punctuation, counts adjacent token relations, and selects up to eight strongest relations in the segment. The host does not rank or select them.

For each native-selected relation, the mechanical bridge performs only exact SHA routing, existing-record lookup, and exact provenance-presence lookup. Native SIGMA receives the prior unary support record plus `PROV_SEEN=YES/NO` and computes the new support itself. A replay of an already-persisted segment provenance contributes zero new support, preventing evidence double-counting across a crash between evidence persistence and segment commit. Support is saturating/bounded at 64.

Native promotion rule in this implementation candidate:

```text
support >= 3 -> native promoted knowledge record
```

Native external-acquisition rule in this implementation candidate:

```text
support >= 2 AND no learned external response for that query
-> native may select the lowest-support eligible relation in the current evidence bundle
-> query = LEFT + " " + RIGHT
-> FETCH_EXTERNAL
```

This is a native structural research rule. It is not a claim of semantic curiosity or general reasoning.

## Internet

Internet is not gated on local completion. If native SIGMA emits `FETCH_EXTERNAL`, the runner transports the exact native query to the currently configured Wikipedia Search adapter. The decoder returns every non-empty extract from up to three API results in response order; it does not rank, summarize, or select a lesson.

Fetched material is cached and enters the same native segment/evidence/knowledge path. Transport acquisition and learning completion remain distinct:

```text
FETCHED != LEARNED
```

A fetched query is marked learned only after native SIGMA finishes processing the external entry and emits external completion.

This revision provides one Internet source family. General multi-source native source-family/resource selection remains a later capability and is not implied by this program.

## Persistence and restart

Mechanical SQLite state stores:

- entry COMPLETE/HOLD state;
- per-entry byte offsets;
- segment commit identities;
- exact native evidence records;
- exact native promoted knowledge records;
- request fetched/learned distinction;
- backup queue records.

SQLite transactions make host persistence replay-safe in its exact mechanical scope. Native active-record/current-stream/request state is held under `.sigma_exec`. Runtime restart therefore resumes an active entry or the catalog frontier rather than requiring the host to recreate a cognitive selection.

## Existing knowledge_v2

C5 does not overwrite the observed `knowledge_v2` versioned store. Its files are part of the Oppo local universe and may be revisited through bounded local transport. A future specialized graph adapter may exploit `HEAD -> commit -> events -> revisions -> objects`, but this complete runner does not require flattening or duplicating that store.

## Mechanical format boundary

Raw UTF-8 text is transported exactly. Binary/UTF-16 material is held explicitly instead of being interpreted as text. Optional PDF decoding exists only when explicitly enabled and a mechanical `pdftotext` tool is present; default is disabled pending a separate decoder admission. Unsupported formats remain visible as HOLD evidence rather than silently disappearing.

## Backup integration point

Every mechanical persistent state/external-fetch change appends a record to the C5 backup queue. This is the integration point for the separately governed Cloudflare R2 encrypted backup daemon. The self-learning core does not contain cloud credentials and does not make backup policy semantic decisions.

## Locked identities

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## Implementation files

```text
SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma
SIGMA_C5_MECHANICAL_BRIDGE_V1.py
RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V1.sh
RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_PREFLIGHT_V1.sh
```

Canonical local content hashes before GitHub bundle creation:

```text
NATIVE_SOURCE_SHA256=1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace
MECHANICAL_BRIDGE_SHA256=66c01ddcc9b229e854266eecd3e91c2c0930ea8a347ff61d0daa447e1083abd5
RUNNER_SHA256=550af3a398c79d52031bf846e254e13fa1762357474f0f9c278075a263ca242a
PREFLIGHT_SHA256=3b49fcd7c56a957e8d2cd88d2105ad8c101fbe90d78ed168ad49ce5eda0ab4b5
```

## Claim boundary before Oppo execution

```text
COMPLETE_IMPLEMENTATION_CANDIDATE_WRITTEN=YES
LOCKED_SIGMAC_COMPILE=NOT_RUN_ON_OPPO
LOCKED_VM_RUNTIME=NOT_RUN_ON_OPPO
REAL_OPPO_10GB_LEARNING=NOT_RUN
REAL_SELF_INITIATED_INTERNET_LOOP=NOT_RUN
GENERAL_SEMANTIC_UNDERSTANDING=NOT_CLAIMED
GENERAL_AUTONOMOUS_REASONING=NOT_CLAIMED
PRODUCTION_ADMISSION=NO
```

The next action is a locked-runtime preflight from `$HOME/SIGMA/sigma_genesis1`, followed by real continuous execution only if the compile/runtime gate passes without host cognitive substitution.
