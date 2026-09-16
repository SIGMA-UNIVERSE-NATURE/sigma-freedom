# SURVIVAL MASTER STATIC REVIEW — SIGMA INTERNET AUTOLEARN R1

Date: 2026-09-17 (Asia/Ho_Chi_Minh)
Branch: `AIL_SIGMA`
Candidate content commit: `cb914a41c4d1224eea6b84e5561f7099ad154b9d`
Candidate metadata HEAD reviewed: `1cc8000a0d0203a369b57807d9e097c100ef84dc`
Authority request: `SURVIVAL_MASTER/REQUESTS/20260917_INTERNET_AUTO_BUNDLE_IMPLEMENTATION_REQUEST_R1.md`

```text
REVIEW_VERDICT=HOLD_NEEDS_FIX
APPROVE_FOR_OPPO_PREFLIGHT_ONLY=NO
HUMAN_MUST_NOT_INSTALL=YES
HUMAN_MUST_NOT_RUN_ON_OPPO=YES
PRODUCTION_ENABLEMENT=NO
```

## What passed static review

```text
BASE_TO_CANDIDATE_AHEAD_BY=2
CHANGES_OUTSIDE_SURVIVAL_MASTER_CANDIDATES_INTERNET_AUTOLEARN_R1=NO
CANDIDATE_ISOLATION=PASS
DEFAULT_SESSION_TARGET=READ_PLUS_ARTIFACT_WRITE
SESSION_GUARD_REQUIRES_BRAIN_STATE_MODEL_LEARN_COMMIT_HEAD_GENERATION_REJECT=YES
HOST_QUERY_GENERATION_PATH_FOUND=NO_IN_REVIEWED_FILES
HOST_SEMANTIC_SOURCE_FALLBACK_PATH_FOUND=NO_IN_REVIEWED_FILES
WEB_BRIDGE_PUBLIC_READ_ONLY_POLICY_PRESENT=YES
PRIVATE_NONPUBLIC_DNS_REJECT_PRESENT=YES
TLS_VERIFY_DEFAULT=YES
GET_HEAD_ONLY_DEFAULT=YES
CANONICAL_MUTATION_DEFAULT=NO
FAIL_CLOSED_INTENT=PASS
CLAIM_SCOPE_BOUNDED=YES
```

The candidate correctly refuses to recreate missing cognition from prose. The host bridge is written as mechanical public-web transport, and the candidate explicitly preserves unresolved native dependencies instead of pretending they are solved.

## Blocking defects

### BLOCKER 1 — review approval is not bound to the exact reviewed bytes

`control/start_preflight.sh` and `verify/native_runtime_admission_harness.sh` trust only:

```text
SURVIVAL_REVIEW_VERDICT=APPROVE_FOR_OPPO_PREFLIGHT_ONLY
```

That environment string is not bound to:

```text
candidate commit
root manifest SHA256
bundle SHA256
review receipt SHA256
```

Therefore an approval for one reviewed candidate could be reused after candidate bytes change. This violates the request rule that any post-review source change invalidates approval.

Required FIX1: preflight must require an external Survival-Master approval receipt containing the exact reviewed candidate commit, root manifest SHA256, bundle SHA256 and approval status, and must equality-gate those values against the bytes being run. The candidate must not be able to self-issue this approval receipt.

### BLOCKER 2 — dependency receipt is text-trusted, not evidence-bound

`control/start_preflight.sh` currently accepts any file containing these literal lines:

```text
EXACT_NATIVE_DEPENDENCIES_VERIFIED=YES
GENERAL_ARBITRARY_WEBSITE_NATIVE_SELECTION=PROVEN_FOR_THIS_INTERFACE
NATIVE_CONDENSER_INTERFACE=PROVEN_FOR_THIS_INTERFACE
```

It does not verify that the receipt was mechanically generated from exact dependency files, does not bind source/bytecode/interface hashes, and does not bind the receipt to this candidate/toolchain.

Required FIX1: dependency receipt must record and verify, for every required native capability:

```text
capability id
exact source path
source SHA256
bytecode path/hash when applicable
checkpoint/commit provenance
interface/ABI contract identity
locked SIGMAC SHA256
locked VM SHA256
candidate commit/root-manifest identity
```

The preflight must recompute/equality-gate these hashes. Literal claim lines alone are insufficient.

### BLOCKER 3 — README claims dependency resolution that start_preflight does not perform

`README_RUN.md` says `start_preflight.sh` checks exact native dependency resolution. The actual script only checks a supplied receipt with `grep -Fqx`; it does not invoke `host/exact_dependency_resolver.py` or verify the resolved files/interfaces.

Required FIX1: make documentation and executable behavior identical. The exact resolver/receipt-builder path must be explicit and mechanically verifiable.

### BLOCKER 4 — no executable end-to-end native controller composition exists yet

`host/artifact_worker.sh` accepts a small action class and then unconditionally ends with:

```text
HOLD=UNRESOLVED_EXACT_NATIVE_CONTROLLER_INTERFACE
```

The native `SIGMA_INTERNET_AUTOLEARN_COMPOSITION_GATE_R1.sigma` only checks dependency-status text and whether an event file is present. It does not itself prove the query/source/resource/read/evaluate/condense/next-action composition chain.

This fail-closed behavior is safe, but the requested Internet-auto bundle is not operational yet.

Required FIX1: after exact native interfaces are resolved, wire only exact native-emitted events to mechanical host operations and exact receipts back to the native controller. Host must still never choose query/site/resource/semantic retry/condensation/next action.

### BLOCKER 5 — native runtime admission harness is a placeholder

`verify/native_runtime_admission_harness.sh` explicitly prints that locked SIGMAC compile and VM runtime are not executed and exits nonzero. That is acceptable for an unreviewed skeleton but not sufficient for Oppo preflight approval of an operational candidate.

Required FIX1: provide a reviewer-controlled preflight harness that, after approval + exact dependency verification, performs only isolated artifact-lane compile/freeze/dynamic/negative/replay checks. No production/canonical mutation.

### BLOCKER 6 — the two human-required cognitive capabilities remain unresolved

The candidate itself correctly records:

```text
GENERAL_ARBITRARY_WEBSITE_NATIVE_SELECTION=NOT_PROVEN_BY_THESE_DEPENDENCIES
NATIVE_ABSTRACTIVE_CONDENSER=DEPENDENCY_MISSING_NOT_PROVEN
```

`DEPENDENCIES.lock` also has unresolved I5B/I5C exact source identities. Therefore the requested target — SIGMA freely selecting mechanically reachable public websites/resources and SIGMA-native retained-data condensation — is not yet satisfied by exact active bytes/interfaces.

Required FIX1: locate/reuse exact native artifacts where they exist and bind exact interfaces. If the general capability truly does not yet exist, keep HOLD and build/admit the missing native capability separately; do not move it into Bash/Python.

## Important positive finding

The V11 query-adapter source/bytecode identities in `DEPENDENCIES.lock` match the immutable V11 checkpoint evidence:

```text
V11_ADAPTER_SOURCE_SHA256=82e25898da18059c3abee97c77529a137db4a33ae85fdd4c042e3ce7b7e14b3f
V11_ADAPTER_BYTECODE_SHA256=40f6b83e55c5dff238b7fe4a9f208e6bfabec3c73a70e5b5c95b93941fa353f0
```

This supports the candidate's reuse discipline, but does not resolve the blockers above.

## FIX1 submission contract

The implementing window must preserve the current candidate and submit a new FIX1 commit under the same candidate directory with `SUBMISSION.md` updated to identify FIX1. Do not touch production/canonical files.

FIX1 must demonstrate statically:

```text
APPROVAL_RECEIPT_EXTERNAL_TO_CANDIDATE=YES
APPROVAL_BOUND_TO_EXACT_CANDIDATE_COMMIT=YES
APPROVAL_BOUND_TO_ROOT_MANIFEST_SHA256=YES
APPROVAL_BOUND_TO_BUNDLE_SHA256=YES
DEPENDENCY_RECEIPT_HASH_BOUND=YES
DEPENDENCY_SOURCE_AND_INTERFACE_HASHES_RECOMPUTED=YES
README_MATCHES_EXECUTABLE_PREFLIGHT=YES
ARTIFACT_WORKER_NO_LONGER_UNCONDITIONALLY_HOLDS_AFTER_VALID_RESOLVED_NATIVE_EVENT=YES
HOST_COGNITION=NO
HOST_QUERY_GENERATION=NO
HOST_SOURCE_SELECTION=NO
HOST_RESOURCE_SELECTION=NO
HOST_SUMMARY_WRITING=NO
CANONICAL_MUTATION=NO_FOR_R1
```

If arbitrary-website selection or native condensation remains genuinely unavailable, FIX1 must remain HOLD rather than fake the missing capability.

## Next action

```text
NEXT_ACTION=IMPLEMENT_FIX1_AND_COMMIT_CANDIDATE_ONLY
DO_NOT_RUN_OPPO=YES
DO_NOT_INSTALL=YES
SEND_NEW_COMMIT_SHA_TO_SURVIVAL_MASTER_FOR_REVIEW=YES
```
