# MULTI-TEACHER CANONICAL CANDIDATE PACKET R1

Each teacher window produces one descriptor file inside its own `ARTIFACT_ROOT`. The sealing tool verifies it and creates a content-addressed READY packet under that same workspace.

Required descriptor fields:

```text
SCHEMA=SIGMA_MULTI_TEACHER_WEIGHT_CANDIDATE_R1
SOURCE_SESSION_CODE=<current teacher session>
SOURCE_RUN_ID=<current teacher run>
PARENT_HEAD=<teacher OPEN_HEAD>
PARENT_MODEL_GENERATION=<teacher OPEN_MODEL_GENERATION>
TEACHING_EVIDENCE_PATH=<absolute path under teacher ARTIFACT_ROOT>
TEACHING_EVIDENCE_SHA256=<sha256>
CANONICAL_REPLAY_ENTRYPOINT=<absolute executable path under teacher ARTIFACT_ROOT>
CANONICAL_REPLAY_ENTRYPOINT_SHA256=<sha256>
NATIVE_OWNERSHIP_RECEIPT=<absolute path under teacher ARTIFACT_ROOT>
NATIVE_OWNERSHIP_RECEIPT_SHA256=<sha256>
CANONICAL_MUTATION_REQUEST=QUEUE_FOR_NATIVE_REEVALUATION
HOST_COGNITION=NO
HOST_LEARNING=NO
SIGMA_NATIVE_LEARNING_OWNER=YES
```

The ownership receipt must contain exact lines:

```text
SIGMA_NATIVE_LEARNING_OWNER=YES
HOST_COGNITION=NO
HOST_LEARNING=NO
CANONICAL_REPLAY_SAFE=YES
```

The queue framework treats these as admission metadata, not proof of semantic quality. The lane-specific replay entrypoint remains responsible for actual native runtime evidence.

The replay entrypoint is invoked as:

```text
CANONICAL_REPLAY_ENTRYPOINT <descriptor-path> <attempt-root>
```

The drainer exports:

```text
SIGMA_QUEUE_DESCRIPTOR=<descriptor path>
SIGMA_QUEUE_ATTEMPT_ROOT=<attempt root>
SIGMA_QUEUE_CURRENT_HEAD=<current BRAIN_HEAD bytes>
SIGMA_QUEUE_CURRENT_MODEL_GENERATION=<current MODEL_GENERATION bytes>
SIGMA_QUEUE_CANONICAL_SESSION_CODE=<current canonical learner session>
```

It must write:

```text
<attempt-root>/result.env
```

Common required result fields:

```text
SCHEMA=SIGMA_MULTI_TEACHER_CANONICAL_RESULT_R1
QUEUE_RESULT=ACCEPTED|REJECTED|HOLD
SOURCE_CANDIDATE_ID=<packet id>
SIGMA_NATIVE_LEARNING_OWNER=YES
HOST_COGNITION=NO
HOST_LEARNING=NO
BEFORE_HEAD=<current head received by replay>
BEFORE_MODEL_GENERATION=<current generation received by replay>
CANONICAL_MUTATION_OBSERVED=YES|NO
```

If `QUEUE_RESULT=ACCEPTED`, also require:

```text
AFTER_HEAD=<observed canonical head after native commit>
AFTER_MODEL_GENERATION=<observed generation after native commit>
NATIVE_COMMIT_RECEIPT_PATH=<absolute path>
NATIVE_COMMIT_RECEIPT_SHA256=<sha256>
```

The replay entrypoint must use the existing canonical learner protocol for commit/model-generation advancement. It must not edit `.sigma_ail/BRAIN_HEAD`, `.sigma_ail/MODEL_GENERATION`, or writer locks manually.

If `QUEUE_RESULT=REJECTED`, require:

```text
CANONICAL_MUTATION_OBSERVED=NO
```

If `QUEUE_RESULT=HOLD`, the drainer records the attempt but does not mark the candidate processed.
