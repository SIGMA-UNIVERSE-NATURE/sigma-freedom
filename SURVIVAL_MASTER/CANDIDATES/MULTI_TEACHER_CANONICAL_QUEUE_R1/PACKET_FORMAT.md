# MULTI-TEACHER CANONICAL CANDIDATE PACKET R2

This R2 packet schema supersedes the original R1 descriptor before Oppo deployment.

Each teacher window produces one source descriptor inside its own `ARTIFACT_ROOT`. The sealing tool verifies exact bytes and creates a self-contained content-addressed READY packet under that same workspace.

## Source descriptor required fields

```text
SCHEMA=SIGMA_MULTI_TEACHER_WEIGHT_CANDIDATE_R2
SOURCE_SESSION_CODE=<current teacher session>
SOURCE_RUN_ID=<current teacher run>
PARENT_HEAD=<teacher OPEN_HEAD from Oppo session>
PARENT_MODEL_GENERATION=<teacher OPEN_MODEL_GENERATION from Oppo session>
TEACHING_EVIDENCE_PATH=<absolute path under teacher ARTIFACT_ROOT>
TEACHING_EVIDENCE_SHA256=<sha256>
NATIVE_LEARNING_SOURCE_PATH=<absolute .sigma path under teacher ARTIFACT_ROOT>
NATIVE_LEARNING_SOURCE_SHA256=<sha256>
NATIVE_LEARNING_BYTECODE_PATH=<absolute .sigmab path under teacher ARTIFACT_ROOT>
NATIVE_LEARNING_BYTECODE_SHA256=<sha256>
MECHANICAL_REPLAY_RUNNER_PATH=<absolute executable path under teacher ARTIFACT_ROOT>
MECHANICAL_REPLAY_RUNNER_SHA256=<sha256>
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
MECHANICAL_REPLAY_RUNNER_ONLY=YES
CANONICAL_REPLAY_SAFE=YES
NATIVE_LEARNING_SOURCE_SHA256=<same source hash>
NATIVE_LEARNING_BYTECODE_SHA256=<same bytecode hash>
```

The queue framework treats these as control/evidence bindings, not as proof of semantic quality.

## Self-contained sealed packet

The sealing tool copies exact verified bytes into fixed packet-local names:

```text
descriptor.env
teaching.evidence
native_learning.sigma
native_learning.sigmab
mechanical_replay_runner
native_ownership.receipt
MANIFEST.sha256
READY
```

The canonical drainer must consume packet-local copies only. It must not depend on the original teacher process remaining alive.

## Runtime authority

Immediately before replay, the drainer reads:

```text
$HOME/SIGMA/sigma_genesis1/.sigma_ail/BRAIN_HEAD
$HOME/SIGMA/sigma_genesis1/.sigma_ail/MODEL_GENERATION
```

These current Oppo values are authoritative. GitHub HEAD is not used as canonical runtime state.

The drainer exports mechanically:

```text
SIGMA_QUEUE_DESCRIPTOR=<packet-local descriptor path>
SIGMA_QUEUE_ATTEMPT_ROOT=<attempt root>
SIGMA_QUEUE_CURRENT_HEAD=<current Oppo BRAIN_HEAD bytes>
SIGMA_QUEUE_CURRENT_MODEL_GENERATION=<current Oppo MODEL_GENERATION bytes>
SIGMA_QUEUE_CANONICAL_SESSION_CODE=<current canonical learner session>
SIGMA_QUEUE_NATIVE_SOURCE=<packet-local native_learning.sigma>
SIGMA_QUEUE_NATIVE_BYTECODE=<packet-local native_learning.sigmab>
```

The exact mechanical replay runner is invoked as:

```text
MECHANICAL_REPLAY_RUNNER <descriptor-path> <attempt-root>
```

It may launch the locked compiler/VM when required by the lane, move exact bytes, and capture raw evidence. It may not calculate the learning result.

## Native decision receipt

The replay must preserve an exact native SIGMA decision receipt under the attempt root.

Minimum receipt fields:

```text
SCHEMA=SIGMA_NATIVE_CANONICAL_LEARNING_DECISION_R1
SOURCE_CANDIDATE_ID=<packet id>
QUEUE_RESULT=ACCEPTED|REJECTED|HOLD
PARENT_HEAD=<current Oppo head passed into replay>
PARENT_MODEL_GENERATION=<current Oppo generation passed into replay>
NATIVE_LEARNING_SOURCE_SHA256=<packet source hash>
NATIVE_LEARNING_BYTECODE_SHA256=<packet bytecode hash>
SIGMA_NATIVE_LEARNING_OWNER=YES
```

`QUEUE_RESULT` is a native SIGMA output. Bash/Python may copy/parse it mechanically but must not invent, remap, rank, or override it.

## result.env contract

The replay path writes:

```text
<attempt-root>/result.env
```

Common required fields:

```text
SCHEMA=SIGMA_MULTI_TEACHER_CANONICAL_RESULT_R2
QUEUE_RESULT=ACCEPTED|REJECTED|HOLD
SOURCE_CANDIDATE_ID=<packet id>
SIGMA_NATIVE_LEARNING_OWNER=YES
HOST_COGNITION=NO
HOST_LEARNING=NO
BEFORE_HEAD=<current Oppo head>
BEFORE_MODEL_GENERATION=<current Oppo generation>
NATIVE_LEARNING_SOURCE_SHA256=<packet source hash>
NATIVE_LEARNING_BYTECODE_SHA256=<packet bytecode hash>
NATIVE_DECISION_RECEIPT_PATH=<absolute path under attempt root>
NATIVE_DECISION_RECEIPT_SHA256=<sha256>
NATIVE_VM_RC=<exact rc when applicable>
CANONICAL_MUTATION_OBSERVED=YES|NO
```

The drainer must verify that `QUEUE_RESULT` in `result.env` exactly matches `QUEUE_RESULT` in the native decision receipt.

If `QUEUE_RESULT=ACCEPTED`, also require:

```text
AFTER_HEAD=<observed current Oppo head after native commit>
AFTER_MODEL_GENERATION=<observed current Oppo generation after native commit>
NATIVE_COMMIT_RECEIPT_PATH=<absolute path>
NATIVE_COMMIT_RECEIPT_SHA256=<sha256>
CANONICAL_MUTATION_OBSERVED=YES
```

If `QUEUE_RESULT=REJECTED` or `HOLD`:

```text
CANONICAL_MUTATION_OBSERVED=NO
```

No queue script may directly edit `.sigma_ail/BRAIN_HEAD`, `.sigma_ail/MODEL_GENERATION`, `WRITER.lock`, learner lease, or canonical model bytes.