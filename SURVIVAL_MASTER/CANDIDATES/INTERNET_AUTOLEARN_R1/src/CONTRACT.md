# SIGMA SURVIVAL INTERNET AUTOLEARN R1 — CANDIDATE CONTRACT

Status: `CANDIDATE_UNREVIEWED_DO_NOT_RUN`
Base branch: `AIL_SIGMA`
Base commit: `44cb72292496378c6ddbab96bf152cf7c1c76a50`
Authority: `SURVIVAL_MASTER/REQUESTS/20260917_INTERNET_AUTO_BUNDLE_IMPLEMENTATION_REQUEST_R1.md`

This candidate is a fail-closed composition package. It does not recreate missing SIGMA cognition from checkpoint prose. It composes exact native capability artifacts only after their bytes are resolved and hash-verified. If any required native dependency cannot be resolved by exact SHA256, the runtime path must return `HOLD=DEPENDENCY_MISSING`.

## Invariants

```text
ONE_SIGMA_AIL=YES
ONE_WRITER=YES
NO_STATE_FORK=MANDATORY
DEFAULT_SESSION=READ_PLUS_ARTIFACT_WRITE
HOST_COGNITION=NO
HOST_TEST_ORACLE=NO_FOR_SEMANTIC_VERDICT
SIGMA_NATIVE_VERDICT=MANDATORY
CANONICAL_MUTATION=EXPLICIT_ADMISSION_ONLY
CANONICAL_LEARN_COMMIT=LEASE_REQUIRED
```

The Internet lane is artifact-only by default:

```text
READ=ALLOW
ARTIFACT_WRITE=ALLOW
BRAIN_WRITE=REJECT
STATE_WRITE=REJECT
MODEL_WRITE=REJECT
LEARN=REJECT
COMMIT=REJECT
HEAD_CHANGE=REJECT
MODEL_GENERATION_CHANGE=REJECT
```

No file in this package authorizes canonical learning or production enablement.

## Cognition ownership

The host package contains no query composer, source selector, resource selector, semantic ranker, relevance scorer, truth decider, summarizer, compact-representation writer, learning policy, curriculum selector, or semantic next-action selector.

Any claimed cognitive action must arrive as an exact event emitted by a hash-locked native SIGMA capability executed under the locked SIGMA VM. This candidate's native composition gate validates provenance/control fields and emits only a mechanical dispatch envelope; it does not invent the underlying semantic action.

## Fail closed

The candidate must HOLD on dependency identity mismatch, unresolved dependency, malformed native event, canonical-mutation request, Session R4 mutation authority, unsafe URL, private-network resolution, raw/native hash mismatch, partial queue item, replay conflict, or unknown recovery state.

`HOLD` and `UNKNOWN` are valid evidence and must never be remapped to a favorable semantic outcome.
