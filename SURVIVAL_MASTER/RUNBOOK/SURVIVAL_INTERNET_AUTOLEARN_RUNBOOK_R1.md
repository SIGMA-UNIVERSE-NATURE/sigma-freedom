# SURVIVAL + INTERNET AUTOLEARN RUNBOOK R1

Status: ACTIVE COORDINATION / DESIGN + OPERATIONS RUNBOOK
Branch: `AIL_SIGMA`
Date: 2026-09-17

This runbook tells a future window exactly how to continue the Survival + Internet-autolearn program without repeating repository archaeology.

It is intentionally explicit. It is not a claim that every future component described below is already implemented or admitted.

---

# 1. OBJECTIVE

Build one SIGMA.AIL system that can:

```text
1. keep long-running learning work recoverable after Android/Termux/tmux death;
2. resume from the last valid committed checkpoint instead of restarting from zero;
3. preserve ONE_SIGMA_AIL, ONE_WRITER and NO_STATE_FORK;
4. run an Internet lane continuously while a local training lane is active;
5. let native SIGMA choose research intent, query, source family, website/resource, reading path and next action;
6. let host code perform only mechanical network/file/hash/process work;
7. let native SIGMA read complete data in bounded resumable ranges;
8. let native SIGMA decide its own compact representation/compression of what it read;
9. preserve exact provenance and content hashes;
10. queue Internet-derived learning material without mutating a currently sealed local-training dataset;
11. admit any weight/model update only through the single authorized learning/writer path;
12. survive repeated interruption without duplicate commits or divergent model branches.
```

---

# 2. NON-NEGOTIABLE COGNITION BOUNDARY

## Native SIGMA must own

```text
knowledge-gap detection
research-goal selection
query formation/adaptation
source-family selection
resource/site/page selection
candidate ranking where ranking is semantic
whether evidence is sufficient
whether to research more
whether to change strategy
how to group source material into a semantic study unit
what information to retain in a compact representation
summary/narrative generation
uncertainty / unknown state
truth / evidence judgment
learning-candidate formation
learning admission / rejection
curriculum / next-action selection
```

## Host may own only mechanical support

```text
process launch / supervision
network DNS/TLS/HTTP transport
exact protocol decode
exact byte/file transport
hashing
content-addressed identifiers
bounded mechanical text decode
Public Suffix List registrable-domain calculation
range accounting
checkpoint fsync/rename/journal mechanics
return-code capture
resource limits / timeouts
exact event dispatch already selected by native SIGMA
artifact persistence
mechanical post-VM test oracle after native output
```

## Forbidden substitution

If Python/Bash/C/JavaScript/external LLM decides a cognitive arrow that the active capability is supposed to prove, the capability is not a SIGMA-native capability.

```text
HOST_QUERY_GENERATION=NO
HOST_SOURCE_SELECTION=NO
HOST_RESOURCE_SELECTION=NO
HOST_RESULT_RANKING=NO
HOST_SEMANTIC_FILTERING=NO
HOST_SUMMARY_WRITING=NO
HOST_LESSON_SELECTION=NO
HOST_TRUTH_DECISION=NO
HOST_NEXT_ACTION_SELECTION=NO
HOST_CURRICULUM_SELECTION=NO
HOST_WEIGHT_POLICY=NO
```

A host safety or size refusal is allowed, but it must return an observation. The host must not silently pick a replacement site or answer.

---

# 3. CURRENT RUNTIME ENTRY CONTRACT

Root:

```bash
ROOT="$HOME/SIGMA/sigma_genesis1"
```

Session API:

```bash
source "$ROOT/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash"
```

Ordinary work session expected minimum policy:

```text
SESSION=GRANTED
ACCESS=READ_PLUS_ARTIFACT_WRITE
BRAIN_WRITE=REJECT
STATE_WRITE=REJECT
MODEL_WRITE=REJECT
LEARN=REJECT
COMMIT=REJECT
HEAD_CHANGE=REJECT
MODEL_GENERATION_CHANGE=REJECT
HOST_COGNITION=NO
HOST_TEST_ORACLE=NO
SIGMA_NATIVE_VERDICT=MANDATORY
```

Do not manually edit any field above. Canonical learning/model mutation requires a separate explicit admission/lease.

---

# 4. NEW WINDOW BOOTSTRAP

A new window must first determine whether it is already bound to a session.

```bash
ROOT="$HOME/SIGMA/sigma_genesis1"
source "$ROOT/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash"
sigma-session status
```

If status says no session in this shell, register the actual task in plain human text:

```bash
sigma-session "Survival Master inspect and continue exact recovery/autolearn task; artifacts only; no cognition and no canonical mutation"
```

Then:

```bash
sigma-session status
```

Do not create a second session in the same active pane merely to change wording.

---

# 5. RUNTIME IDENTITY CHECK

Before touching an active run:

```bash
ROOT="$HOME/SIGMA/sigma_genesis1"
printf 'BRAIN_HEAD='; cat "$ROOT/.sigma_ail/BRAIN_HEAD"; printf '\n'
printf 'MODEL_GENERATION='; cat "$ROOT/.sigma_ail/MODEL_GENERATION"; printf '\n'
sha256sum "$ROOT/native/sigmac" "$ROOT/native/sigma-vm.v09_candidate"
```

Expected locked toolchain hashes from the current project contract:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

Last observed, not guaranteed current after Android kill:

```text
BRAIN_HEAD=700d5c1b4845322d7c14800029c629b0
MODEL_GENERATION=1
```

Mismatch with expected runtime identity is a HOLD. Do not "fix" BRAIN_HEAD or model generation manually.

---

# 6. TARGETED LIVENESS CHECK — NO BROAD REPOSITORY SCAN

Use tmux metadata first:

```bash
tmux list-sessions -F '#{session_name}\t#{session_windows}\t#{session_attached}' 2>/dev/null || true
```

Then panes:

```bash
tmux list-panes -a -F '#{session_name}:#{window_index}.#{pane_index}\tdead=#{pane_dead}\tpid=#{pane_pid}\tcmd=#{pane_current_command}\tstart=#{pane_start_command}' 2>/dev/null || true
```

Only if process identity remains unclear, use a targeted process query:

```bash
pgrep -af 'sigma-vm|RUN_SIGMA|SIGMA_C5V4|G3B|G3_SELF_LEARNED|R8' || true
```

Do not `pkill`, `killall`, or `tmux kill-server` merely because a pane is confusing.

---

# 7. DEAD TMUX PANE VS DEAD TERMUX

A pane showing:

```text
Pane is dead (status 0, ...)
```

means the process in that pane completed and `remain-on-exit` retained the pane. It does not necessarily mean tmux or Termux is broken.

If the prefix works, normal detach is:

```text
Ctrl-b d
```

If the current shell is unavailable or prefix handling is uncertain, open another Termux session and inspect:

```bash
tmux list-clients -F '#{client_tty}\t#{session_name}'
```

Then detach an exact known client only if necessary:

```bash
tmux detach-client -t '<exact-client-target>'
```

Do not guess nested-tmux key sequences before inspecting session/client layout.

---

# 8. SURVIVAL MODEL

## Correct invariant

```text
PROCESS_CAN_DIE=YES
TASK_PROGRESS_MUST_SURVIVE=YES
```

The system must restore work from a committed checkpoint.

## Recovery state machine

A mechanical recovery supervisor may implement only this kind of logic:

```text
READ_RECOVERY_DESCRIPTOR
VERIFY_DESCRIPTOR_HASH
VERIFY_ENTRYPOINT_HASH
VERIFY_DEPENDENCY_HASHES
CHECK_COMPLETION_RECEIPT
CHECK_MATCHING_PROCESS
CHECK_WRITER_LOCK_IF_REQUIRED
CHECK_LAST_COMMITTED_CHECKPOINT
VERIFY_CHECKPOINT_MANIFEST/HASH

if completed:
    do nothing
elif matching process alive:
    do nothing
elif identity mismatch:
    HOLD
elif checkpoint invalid:
    HOLD
elif writer conflict:
    HOLD
else:
    launch exact recorded resume entrypoint
```

This is mechanical recovery, not cognition.

The recovery layer must never decide:

```text
what lesson to study
what site to visit
what query to use
which candidate is semantically better
whether knowledge is true
what model change should be admitted
```

---

# 9. DURABLE RECOVERY DESCRIPTOR — REQUIRED DESIGN

Future survival implementation should persist one durable descriptor per long-running work item.

Suggested mechanical schema:

```text
RECOVERY_SCHEMA_VERSION=1
WORK_ID=<opaque stable id>
TASK_KIND=<mechanical task class only>
SOURCE_RUN_ID=<original run id>
SOURCE_SESSION_CODE=<historical provenance only>
ENTRYPOINT=<absolute or root-relative path>
ENTRYPOINT_SHA256=<sha256>
DEPENDENCY_MANIFEST=<path>
DEPENDENCY_MANIFEST_SHA256=<sha256>
CHECKPOINT_ROOT=<path>
LAST_COMMITTED_CHECKPOINT=<path>
LAST_COMMITTED_CHECKPOINT_MANIFEST_SHA256=<sha256>
LAST_COMMITTED_PROGRESS=<mechanical progress token>
OPEN_HEAD=<hash>
OPEN_MODEL_GENERATION=<integer>
WRITER_REQUIRED=YES|NO
WRITER_LOCK_PATH=<path or NONE>
COMPLETION_RECEIPT=<path>
RESTART_POLICY=RESUME_EXACT_TASK
```

The descriptor should be written transactionally:

```text
write temp
-> fsync where available
-> hash
-> atomic rename
-> verify readback
```

No semantic contents are chosen by the survival supervisor.

---

# 10. SURVIVAL TEST LADDER

Do not jump directly from one successful restart to a general "survives Android" claim.

## L1 — child worker dies

Prove:

```text
same WORK_ID
same checkpoint lineage
no duplicate commit
resume from next unfinished offset/update
one worker after recovery
```

## L2 — wrapper dies

Kill/terminate only wrapper in a controlled test. Prove supervisor starts exact wrapper and does not restart completed work.

## L3 — supervisor dies

Use outer resurrection mechanism. AIL-016 already has historical evidence for dead-supervisor restart scope. Reuse design; do not claim more than tested.

## L4 — tmux server dies

Prove task state is not stored only in tmux. Recovery after a new tmux server must use persistent descriptor/checkpoint state.

## L5 — Termux process group dies

This is the user's real failure mode. The recovery trigger must exist outside the killed process group or be started when Termux restarts. Prove exact work reattachment/resume after Termux relaunch.

## L6 — device reboot

Only after L5. Prove boot/autostart path with hash guard and no duplicate worker.

## L7 — race/dedup

Simultaneously trigger recovery paths and prove only one worker wins the lock.

## L8 — writer safety

For a run that can mutate an admitted learning model, prove a recovery race never creates two model writers.

---

# 11. CURRENT LONG-RUN LOCAL LEARNING POLICY

When a long local trainer is already running on a sealed dataset:

```text
DO_NOT change its dataset mid-run
DO_NOT inject fresh Internet pages directly into its current minibatch stream
DO_NOT create a second trainer writing the same model
DO checkpoint frequently
DO allow Internet acquisition/research to continue in a separate artifact-writing lane
```

Internet material becomes input for a later learning generation unless the active learner was explicitly designed and admitted for online curriculum ingestion.

---

# 12. ONE SIGMA — TWO-LANE CONCURRENCY

## Lane A — local learning

```text
sealed input snapshot
-> native/admitted learner
-> candidate weight updates
-> committed checkpoints
-> final candidate model
-> evaluation
```

## Lane B — Internet autolearn

```text
native SIGMA research state
-> native gap/goal
-> native query/source/resource decision
-> mechanical HTTP transport
-> exact content/provenance
-> native full-input reading
-> native evidence assessment
-> native compact representation
-> immutable evidence/learning-candidate packet
```

Both lanes belong to one SIGMA. They may run concurrently, but only one canonical learning writer may hold authority at a time.

---

# 13. INTERNET AUTOLEARN — EXISTING CAPABILITY CHAIN TO REUSE

Do not write a new Bash/Python crawler that makes semantic choices.

Existing evidence shows bounded native capabilities across AIL and SIGMA_LIFE history:

```text
research_more -> fresh Internet collection
strategy-conditioned query adaptation
query outcome feedback/diversity
source-family selection
resource/candidate selection
exact selected-resource fetch binding
bounded web discovery/link selection
provenance-bound web learning
persistent replay memory
study-value selection
full-document sequential learning
200 real Internet source selections + full-input native consumption
```

A future controller should compose these capability patterns inside native SIGMA rather than moving them into the host.

---

# 14. 500-WEBTOOLS R2 — EXACT INTERFACE

The mechanical tool package currently provides native request helpers conceptually equivalent to:

```text
WT_status()
WT_fetch(url)
WT_decode(object_id)
WT_read_range(object_id, offset, size)
WT_read_text_range(object_id, offset, size)
WT_ack(delivery_id)
WT_publish(story_id, source_ids, summary, mode)
WT_finish()
```

Each native invocation emits one request and exits. Host performs that one mechanical operation, writes response files, then the next VM invocation reads the response.

This is suitable for durable checkpoint/resume because native state can advance in explicit steps.

---

# 15. HOW THE NATIVE INTERNET CONTROLLER SHOULD BE WRITTEN

This section is a design template, not a prewritten semantic answer.

The controller should be a native `.sigma` state machine with persistent state such as:

```text
phase
research_goal_state
query_history_hashes
source_family_history
selected_resource_history
current_object_id
current_source_identity
current_read_offset
acked_range_coverage
current_evidence_state
current_compact_representation_state
current_story_or_document_state
next_native_action
```

Names are implementation suggestions only. The semantic decisions must be native.

## Phase A — observe own state

Native SIGMA reads its existing evidence/memory/uncertainty state and decides whether research is needed.

Possible native outputs:

```text
STOP_SUFFICIENT
RESEARCH_MORE
TRY_ALTERNATIVE
UNKNOWN
```

The host may not manufacture these.

## Phase B — native research surface

SIGMA forms or adapts a natural-language research query or exact source request using its native capability.

If a search/discovery API is used, SIGMA must originate the actual query bytes/URL parameters. Host may URL-encode mechanically only if that transform is exact and semantic-free.

## Phase C — native source-family selection

SIGMA selects from an available capability catalog based on native policy/state. The catalog may expose mechanical capability metadata. Host must not rank it.

## Phase D — discovery transport

Host sends the exact native-selected request and returns complete bounded candidate metadata/provenance.

Remote order is provenance only unless native policy explicitly consumes it.

## Phase E — native candidate/resource selection

SIGMA receives the complete bounded candidate set and selects a specific resource. Reorder-invariance/counterfactual tests must be used where relevant.

## Phase F — exact fetch

Host fetches exactly the selected public resource. Redirects, final URL, HTTP status, payload length and hash are recorded.

## Phase G — full-input bounded reading

SIGMA requests ranges until full coverage is complete.

Recommended mechanical loop:

```text
native emits READ_TEXT_RANGE(object, offset, bounded_size)
host returns exact UTF-8 complete range + next_offset + delivery_id
native consumes it
native emits ACK_RANGE(delivery_id)
host records acknowledged byte coverage
native persists next offset/state
repeat
```

If input is not UTF-8 text, a different exact admitted mechanical decoder is needed. Host must not semantically summarize unsupported formats.

## Phase H — native evidence evaluation

SIGMA decides what the material contributes, whether it conflicts with prior evidence, and whether more research is required.

The host may mechanically count bytes/words/sources, but may not decide relevance or truth.

## Phase I — native compact representation

SIGMA creates its own compact durable representation.

Required ownership:

```text
COMPRESSION_DECISION_PLANE=SIGMA_NATIVE_VM
REPRESENTATION_CONTENT_PLANE=SIGMA_NATIVE_VM
HOST_SEMANTIC_COMPRESSION=NO
HOST_SUMMARY_WRITING=NO
```

Host stores exact emitted bytes and provenance.

## Phase J — native next action

SIGMA decides one of:

```text
RESEARCH_MORE
TRY_ALTERNATIVE_SOURCE
TRY_ALTERNATIVE_QUERY
KEEP_EVIDENCE
QUEUE_FOR_LEARNING
HOLD_UNKNOWN
STOP
```

These are examples of action classes, not a fixed semantic policy. Actual decision logic belongs to native SIGMA.

---

# 16. DO NOT CALL MECHANICAL LABELS "UNDERSTANDING"

These are not equivalent:

```text
HTTP 200 != read
bytes delivered != consumed
all ranges ACKed != understood
summary emitted != abstractive understanding
NLL improvement != semantic truth
content hash != source quality
source count != evidence agreement
```

Claim only what tests prove.

---

# 17. COMPACT REPRESENTATION / "SIGMA LANGUAGE"

The user's target is for SIGMA to compress Internet material into its own useful internal form.

Do not implement this as a Python JSON summarizer.

Correct pattern:

```text
raw exact source bytes
-> native SIGMA reads ranges
-> native SIGMA forms compact representation
-> native SIGMA emits representation bytes/state + source bindings
-> host hashes/stores exact output
-> fresh VM later reopens representation
-> native behavior materially changes because representation exists
```

For a learning claim, require causal evidence:

```text
WITHOUT_REPRESENTATION -> native decision/state A
WITH_REPRESENTATION    -> native decision/state B
```

For persistent memory, require fresh process/restart replay.

---

# 18. SEALED INTERNET-TO-LEARNING PACKET

To connect Internet research to the local trainer without state fork, create a content-addressed packet only after native SIGMA decides it is a learning candidate.

Suggested packet mechanics:

```text
packet_id = hash(manifest)
manifest contains mechanical references to:
  source identities
  exact source hashes
  retrieval receipts
  native representation hash
  native evidence/admission event hash
  open BRAIN_HEAD/model generation
  creation time/run id
```

Host may build the manifest from exact native-emitted IDs mechanically. It may not add semantic labels that SIGMA did not emit.

The packet is immutable once sealed.

---

# 19. LEARNING QUEUE

A queue may be mechanical:

```text
QUEUE/<packet_hash>.ready
```

But host must not prioritize packets semantically.

Options:

1. native SIGMA emits exact next packet ID;
2. native SIGMA emits a bounded ordering/ranking;
3. host presents complete mechanically ordered candidate list and native SIGMA selects.

Forbidden:

```text
Python ranks packets by topic/relevance/quality and feeds winner to learner
```

---

# 20. LOCAL TRAINER HANDOFF

When the current sealed local run finishes:

```text
1. verify final checkpoint manifest and hashes
2. preserve exact parent model identity
3. run native evaluation/admission gate
4. do not promote automatically
5. have native SIGMA select/approve next sealed learning input
6. start a new learning generation/work run
7. keep previous final checkpoint rollbackable
```

A PASS in an experiment does not itself authorize canonical cutover.

---

# 21. CHECKPOINT FORMAT FOR LONG TRAINING

A durable training checkpoint should make resume unambiguous.

Minimum mechanical contents:

```text
MODEL_BYTES / WEIGHT_STATE
OPTIMIZER_STATE if applicable
TRAINING_OFFSET / cursor
UPDATE_COUNT
EPOCH / phase
DATASET_IDENTITY
SOURCE_FILE_HASHES
RNG_STATE if stochastic replay matters
PARENT_MODEL_HASH
OPEN_BRAIN_HEAD
OPEN_MODEL_GENERATION
CHECKPOINT_MANIFEST
CHECKPOINT_MANIFEST_SHA256
COMMIT_MARKER written last
```

A checkpoint is valid only if the final commit marker and manifest verify.

Never resume from a partially written directory just because files exist.

---

# 22. CHECKPOINT COMMIT ORDER

Recommended mechanical sequence:

```text
create checkpoint.tmp.<id>/
write all state
hash all state
write MANIFEST.sha256
verify MANIFEST.sha256
write metadata
fsync where available
write COMMIT marker last
atomic rename temp -> checkpoint-<id>
update LAST pointer atomically
```

If atomic directory rename semantics are not proven on the actual filesystem, claim only the tested durability scope.

---

# 23. RESUME ALGORITHM

Mechanical resume procedure:

```text
read LAST pointer
-> if invalid, scan only known checkpoint directory names newest-to-oldest mechanically
-> require COMMIT marker
-> verify manifest
-> verify parent model/dataset identity
-> verify checkpoint progress monotonicity
-> ensure no matching worker already alive
-> acquire recovery/writer lock if required
-> launch exact resume entrypoint with exact checkpoint path
```

Do not use shell to infer a semantic "best checkpoint" from loss metrics. Use committed progress and identity only.

---

# 24. WRITER LOCK RULE

For any worker capable of model/state mutation:

```text
ACQUIRE_LOCK_BEFORE_MUTATING=YES
LOCK_NONBLOCKING_OR_BOUNDED=YES
SECOND_WRITER_ON_LOCK_CONFLICT=HOLD
LOCK_RELEASE_ON_CLEAN_EXIT=YES
STALE_LOCK_RECOVERY=MECHANICALLY_PROVEN_REQUIRED
```

Do not delete a lock file simply because no tmux pane is visible. Verify process/lock semantics.

---

# 25. tmux IS UI, NOT DURABLE STATE

Never keep the only copy of any of these in tmux environment/history:

```text
work id
checkpoint path
model parent hash
learning offset
writer authority
completion state
next exact resume command
```

They must live in durable files/receipts.

---

# 26. ANDROID / TERMUX REALITY

Android can kill the full Termux process group while tmux is running.

Therefore:

```text
TMUX_DETACH_SURVIVAL != ANDROID_PROCESS_GROUP_SURVIVAL
```

A true survival chain requires a resurrection trigger that runs when Termux is available again, verifies exact identity, reads the durable run journal, and starts only missing unfinished workers.

Do not claim this is complete until a real or controlled equivalent Termux-death/relaunch test passes.

---

# 27. HISTORICAL R8 SURVIVAL EVIDENCE — REUSE WITH CLAIM BOUNDARY

Existing AIL history includes:

```text
R8_CHILD_CRASH_RECOVERY=PASS
R8_CYCLE_DEDUPLICATION=PASS
R8_SHADOW_BOOT_RESURRECTION_INSTALLED=PASS
R8_DEAD_SUPERVISOR_RECOVERY=PASS
R8_OUTER_RESURRECTION=PASS_IN_DEAD_SUPERVISOR_RESTART_SCOPE
```

But:

```text
ANDROID_WHOLE_TERMUX_PROCESS_GROUP_SURVIVAL=NOT_PROVEN
```

Use the admitted design ideas, but rerun only the new scope needed for whole-process-group survival.

---

# 28. CURRENT G3 SELF-LEARNED-SURFACE FAILURE PROCEDURE

Do not touch this lane unless it is the active task.

Current failure:

```text
sigmac: line 46 col 2: top-level item must be DEF or ⟡ command (token=⚡)
HOLD=LEARN_COMPILE_FAILED
```

Correct repair process:

```text
1. preserve original source/hash and compile log
2. inspect only source around failing line plus grammar/examples needed for that token
3. make the smallest syntax correction
4. new source hash
5. compile with same locked sigmac
6. if compile fails, preserve new failure
7. if compile passes, hash/freeze bytecode
8. run full original admission suite unchanged
```

Do not remove semantic checks or replace native learning with Python.

---

# 29. CURRENT 500-WEBTOOLS PRECHECK PROCEDURE

The package itself can be preflighted only as tool IO.

After it is installed/staged into the current `ARTIFACT_ROOT` and `CODE_DEST` is known:

```bash
bash "$CODE_DEST/RUN_NATIVE_WEBTOOLS_R2.sh" --preflight
```

This proves only the tool request/response interface if it passes.

It does NOT prove:

```text
real Internet access
native autonomous controller
5000 websites
500 stories
learned summarization
semantic understanding
```

---

# 30. RUN WITH A REAL NATIVE CONTROLLER

The package requires an actual native controller source path:

```bash
bash "$CODE_DEST/RUN_NATIVE_WEBTOOLS_R2.sh" --tmux /absolute/path/to/native-controller.sigma
```

The controller must actually implement the native research/reading/state machine. Do not pass the old three-span summarizer as if it were the controller.

---

# 31. WEBSITE COUNTING

The 500-webtools package uses registrable domains under a packaged Public Suffix List.

Correct mechanical intent:

```text
https://a.example.com/x
https://b.example.com/y
=> same registrable website example.com
```

Depending on PSL rules, private suffixes are honored.

Website count is mechanical source diversity. It does not imply source quality or truth.

---

# 32. SOURCE DEDUP

Keep distinct notions separate:

```text
same canonical URL + same bytes = exact duplicate revision
same canonical URL + changed bytes = revision changed
multiple URLs + same content hash = cross-source content duplicate mechanically
multiple URLs + different bytes = distinct material mechanically
```

These are mechanical classifications only. Semantic equivalence/conflict must be native.

---

# 33. QUERY HISTORY / NOVELTY

For autonomous research, query history can be content-addressed mechanically.

```text
query_sha256 = hash(exact native-emitted query bytes)
```

Host may reject an exact duplicate query only if the native protocol explicitly asks for mechanical dedup behavior, or present the duplicate observation back to SIGMA. Host must not invent an alternative query.

---

# 34. NETWORK FAILURES

Mechanical network layer may return:

```text
DNS_FAILURE
TLS_FAILURE
HTTP_STATUS
REDIRECT_CHAIN
TIMEOUT
BODY_TOO_LARGE
UNSUPPORTED_CONTENT_TYPE
RATE_LIMIT
ROBOTS_OR_ACCESS_REFUSAL if mechanically detected
```

Then native SIGMA decides next action.

Never map a network failure to "try Wikipedia" or another semantic fallback inside Bash/Python.

---

# 35. SAFETY / CREDENTIALS

Autonomous Internet research should default to public unauthenticated sources unless a separately designed credential policy exists.

```text
CREDENTIALS_SENT=NO_DEFAULT
NO_LOGIN_BYPASS
NO_PAYWALL_BYPASS
NO_CAPTCHA_BYPASS
NO_SILENT_CROSS_ORIGIN_SUBSTITUTION
```

This also improves provenance/replay.

---

# 36. RESOURCE BOUNDS

Resource limits must be observations, not semantic decisions.

Examples:

```text
MAX_BODY_BYTES
MAX_RANGE_BYTES
MAX_VM_STEPS
MAX_RETRIES_PER_MECHANICAL_REQUEST
MAX_CONCURRENT_NETWORK_REQUESTS
DISK_BUDGET
```

When a bound is hit, native SIGMA receives the bound condition and decides whether/how to continue.

---

# 37. CONTROL-PLANE VS KNOWLEDGE

Machine labels such as:

```text
RESEARCH_MORE
KEEP_QUERY_PATTERN
ACK_RANGE
COMMIT
```

are allowed as control-plane protocol.

They do not themselves count as natural-language understanding or knowledge.

Natural-language evidence and native representation behavior must be tested separately.

---

# 38. NATIVE SUMMARY / REPRESENTATION ADMISSION

A future non-three-span summarizer must pass at least:

```text
locked source + bytecode identities
multiple materially different full inputs
output changes with input
counterexample cases
source/bytecode token-leak audit
host summary generation = NO
full-input coverage verified
restart/replay where stateful
bounded step behavior
no fixed expected answer embedded
independent post-VM verification
claim-scope review
```

Do not design the test oracle so that it writes the expected summary.

---

# 39. INTERNET-TO-MEMORY ADMISSION

If native SIGMA stores a compact memory item after Internet reading, prove:

```text
memory item emitted by native VM
source bindings exact
memory persists across fresh process
without memory -> native behavior A
with memory -> native behavior B
raw source not required for reuse if that is the claim
corrupted memory rejected or held
host semantic reconstruction = NO
```

---

# 40. INTERNET-TO-WEIGHTS ADMISSION

For a learning claim:

```text
candidate update proposed from exact native-selected/processed evidence
source model unchanged during proposal
native SIGMA owns accept/reject
host commits only the exact accepted candidate mechanically
rejected candidate not committed
fresh-process model persists
held-out/counterfactual evaluation defined before inspecting result
rollback path proven if canonical promotion is contemplated
```

This pattern already has historical AIL evidence in bounded scopes. Reuse it.

---

# 41. GITHUB CONTINUITY RULE

After every meaningful event, checkpoint enough information that the next window does not need chat history.

Do not store secrets or huge raw logs in GitHub.

Master handoff update should contain:

```text
what changed
exact commit/hash identities
machine result
claim scope
failure/hold if any
next exact action
```

Raw machine logs can remain local with their hash/path referenced in a provenance-safe checkpoint.

---

# 42. WHEN CONTEXT WINDOW IS ABOUT TO END

Before doing new work, update:

```text
SURVIVAL_MASTER/CURRENT_HANDOFF.md
```

with:

```text
LATEST_RUNTIME_OBSERVATION
LATEST_SESSION_CODE
LATEST_WORK_ID
LATEST_CHECKPOINT
LATEST_FAILURE_OR_PASS
EXACT_NEXT_COMMAND_OR_NEXT_ACTION
```

If command samples change, update:

```text
SURVIVAL_MASTER/SAMPLES/COMMANDS_R1.md
```

If architecture changes, update this runbook.

Do not leave only a chat explanation.

---

# 43. NEW WINDOW DECISION TREE

```text
START
|
|-- read master files
|
|-- live runtime available?
|     |-- NO -> ask only for the minimal missing runtime evidence
|     `-- YES
|
|-- active unfinished worker found?
|     |-- YES -> inspect its exact checkpoint/status; do not duplicate it
|     `-- NO
|
|-- valid unfinished recovery descriptor/checkpoint exists?
|     |-- YES -> mechanical exact resume
|     `-- NO
|
|-- active task explicitly requested by human?
|     |-- YES -> create/use one session and continue that task
|     `-- NO -> do not invent a new semantic program
```

---

# 44. SURVIVAL MASTER SUCCESS CONDITIONS

Survival Master R1 should eventually be considered complete only when evidence supports all required scopes, for example:

```text
LONG_RUN_CHECKPOINTING=PASS
CHILD_CRASH_RESUME=PASS
SUPERVISOR_CRASH_RESUME=PASS
TMUX_DEATH_RESUME=PASS
TERMUX_PROCESS_GROUP_DEATH_RESUME=PASS
DEVICE_REBOOT_RESUME=PASS_IF_IN_SCOPE
NO_DUPLICATE_WORKER=PASS
NO_DUPLICATE_COMMIT=PASS
ONE_WRITER_ENFORCED=PASS
NO_STATE_FORK=PASS
CHECKPOINT_CORRUPTION_FAIL_CLOSED=PASS
COMPLETION_RECEIPT_PREVENTS_RESTART=PASS
HOST_COGNITION=NO
```

Do not compress these into a single PASS until each required failure mode was actually tested.

---

# 45. INTERNET AUTOLEARN SUCCESS CONDITIONS

A general autonomous Internet-learning claim is much stronger than current bounded results.

A future full-chain admission would need evidence for:

```text
native gap/goal
native query generation/adaptation
native source family selection
native resource selection
exact Internet transport
complete input reading
native evidence evaluation
native uncertainty/unknown
native follow-up decision
native compact representation
persistent reuse
native learning admission if weights change
restart/recovery
no host semantic substitution
```

Until that exact end-to-end chain is admitted:

```text
GENERAL_CLOSED_AUTONOMOUS_NATURAL_LANGUAGE_WEB_LEARNING=NOT_PROVEN
```

This does not erase the many bounded capabilities already proven.

---

# 46. OPERATOR PRINCIPLE

The operator should eventually be able to do only this:

```text
start/restore ONE SIGMA
```

and the system should mechanically recover unfinished work while native SIGMA owns the cognitive choices.

The human should not need to copy SESSION_CODE values, retype hidden state, choose recovery checkpoints, or manually tell each tmux window what another window decided.

---

# 47. FINAL HANDOFF RULE

If you are a future assistant/window and this runbook is the only thing you can read, do this:

```text
1. read SURVIVAL_MASTER/CURRENT_HANDOFF.md
2. read SURVIVAL_MASTER/SAMPLES/COMMANDS_R1.md
3. inspect live session/head/model/tool hashes
4. identify exact unfinished run
5. continue one exact next action
6. preserve native/host boundary
7. checkpoint GitHub before your own context ends
```

Do not restart project archaeology.
