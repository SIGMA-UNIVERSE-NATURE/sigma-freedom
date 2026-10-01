# SIGMA RealBrain — B5 to Admission/Cutover Roadmap

Date: 2026-10-01
Type: coordination / roadmap authority
Source: user-supplied current plan.

## Current state

CURRENT=B5_PASS
NEXT=B6

Estimated remaining major gates:

TO_ADMISSION_CUTOVER=~9_MAJOR_GATES
TO_FULL_AUTOLEARN_CLOSED_LOOP=~10_MAJOR_GATES

## Gate 1 — B6 Apply Batch 2

- measure actual gain;
- build epoch-2 statistics;
- full external verifier.

## Gate 2 — B7 Generic Iterative Tokenizer Growth Engine

Replace manual B8/B9/B10-style progression with a Sigma-owned loop:

measure -> select -> append -> remeasure -> stop

Host remains mechanics only.

## Gate 3 — Run Tokenizer Learning to Native Stop Condition

- do not force vocab to 131072;
- stop when no useful marginal gain remains;
- persist final V2 tokenizer state for 32B/70B.

## Gate 4 — Production Tokenizer Qualification

Use fresh reserve not used for training.

Required:
- exact roundtrip;
- determinism;
- no duplicates;
- compression/gain evidence;
- fresh-process restore;
- replay append = 0.

Only after this gate may:
RB_PRODUCTION_TOKENIZER=PASS

## Gate 5 — Bind Qualified Tokenizer to Production MODEL V3

Required:
- exact tokenizer-state hash;
- exact model binding;
- fresh restore;
- forward path;
- continuation scoring;
- no fallback-only path.

## Gate 6 — RealBrain Production Gates

Run real evaluator/retention/semantic preservation gates.

Semantic capabilities:
- referent_identity
- relation_support
- contradiction
- scope_compatibility
- evidence_support
- cross_document_support

Fixture-only evidence is not production retention evidence.

## Gate 7 — R22 Native Admission Policy

Required gates:
- regression;
- dev gain;
- persistence;
- identity;
- storage/recovery;
- native policy ownership.

Result at this stage may be READY only.
No cutover yet.

## Gate 8 — Fresh-Final + DNA15 Step6

- build R22CFINAL_V1;
- immutable fresh-final verification;
- run DNA15 Step6 only after fresh-final;
- treat DNA15 Step6 as final provenance/admission boundary.

## Gate 9 — Atomic Cutover

Atomically transfer live authority for:
- runtime;
- VKM;
- model;
- tokenizer.

Then verify:
- live HEAD;
- generation;
- model generation;
- post-cutover smoke;
- rollback capability.

Only after this gate may claim:

ADMISSION=COMPLETE
CUTOVER=COMPLETE

## Post-cutover production AutoLearn closure

observe
-> build candidate
-> learn
-> checkpoint
-> evaluate
-> retention/semantic gates
-> R22 policy
-> fresh-final
-> admission
-> atomic promotion
-> continue learning

## Architecture principle

R22 = cognitive/autolearn control plane.
RealBrain = neural execution/training plane.
R21 = durable storage/recovery substrate.

Tokenizer foundation already established:
- byte-exact ABI;
- persistence V2;
- real corpus statistics;
- Sigma-owned piece policy;
- exact batch-1 proof;
- generalized epoch-1/batch-2 policy.

Remaining work is primarily:
- iterative learning generalization;
- tokenizer qualification;
- production evaluator/retention/semantic gates;
- R22 admission chain;
- atomic cutover.

## Boundary

This document is a roadmap only.

It does NOT establish PASS for B6-B9, production tokenizer qualification, R22 READY, fresh-final, DNA15 Step6, admission, or cutover.
