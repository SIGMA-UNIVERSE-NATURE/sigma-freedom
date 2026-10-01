# SIGMA B7 Final — Two-Phase Resumable Growth Contract

Date: 2026-10-01
Type: coordination / design contract
Source: user-supplied B7 target architecture.

## Phase 1

learn + measure once
-> actual gain > 0
-> persist accepted pieces
-> pair table -> R21 byte-CAS
-> PENDING_STATS(
     pair_blob_ref,
     pair_sha,
     counts,
     new tokenizer states
   )

Required intent:
- accepted piece state becomes durable;
- pair-table payload becomes durable in R21 byte-CAS;
- pending stats stores only durable references + verification metadata;
- no corpus remeasure required after crash.

## Phase 2 — fresh command / crash-resumable

restore pair_blob_ref from R21
-> verify SHA
-> persist RBTSPAGE descriptors
-> stats root
-> growth history
-> CONTINUE / STOP

Required intent:
- phase 2 may run in a fresh process;
- pair data must not be transient;
- stats descriptor persistence must be reconstructible from durable pair data;
- growth history and native stop decision must be durable;
- replay must be exactly-once.

## Final B7 target invariants

RESUMABLE=YES
CRASH_RECOVERABLE=YES
PAIR_DATA_TRANSIENT=NO
CORPUS_REMEASURE=NO
STEP_LIMIT_INCREASE=NO
ONE_SIGMA=YES

## Additional gate requirements

- R21 remains payload/storage authority.
- Sigma owns growth policy and CONTINUE/STOP decision.
- Host performs mechanics only.
- pair_blob_ref must be content-addressed.
- pair_sha must verify before stats descriptor persistence.
- replay of either phase must not duplicate accepted pieces, pair blobs, descriptors, stats roots, or history entries.
- crash after accepted pieces but before PENDING_STATS must reconcile safely.
- crash after PENDING_STATS but before RBTSPAGE must resume from pair_blob_ref.
- crash after RBTSPAGE but before growth-history commit must not double-advance the epoch.
- tokenizer state and stats root must remain generation-consistent.

## Boundary

This document defines the target architecture only.

It does NOT establish B7 PASS, tokenizer convergence, production tokenizer qualification, admission, or cutover.
