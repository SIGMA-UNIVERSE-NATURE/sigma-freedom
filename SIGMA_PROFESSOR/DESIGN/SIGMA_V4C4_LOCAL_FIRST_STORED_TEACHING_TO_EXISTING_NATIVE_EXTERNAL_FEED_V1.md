# SIGMA V4-C4 — Local-First Stored Teaching -> Existing Native External Feed V1

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: DESIGN + NATIVE STAGE SOURCE READY / RUNTIME NOT RUN

## Correction to the immediate architecture frontier

The immediate missing bridge is not a brand-new Internet mechanism.

Repository/runtime evidence already shows two relevant facts:

1. the current V4 C2R2 continuous runner only exposes the V2.4 production `raw` directory as its corpus source;
2. SIGMA already has existing native self-directed external acquisition behavior in V2.4, and V5-K2 separately passed a live Wikipedia adapter admission scope.

Therefore the next integration should first expose the stored/taught local corpus to V4, let native SIGMA process that corpus, and only then bind the already-existing native external feed.

## Existing external capability to reuse

Production V2.4 source:

`SIGMA_PROFESSOR/artifacts/SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sigma`

The native source derives a `GAP_QUERY` from its recurrent-support state and writes:

`SIGMA_CL22_FETCH_REQUEST.memory`

The production runner:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh`

uses that exact native request for Wikipedia query transport and stores the decoded returned context as:

`$HOME/SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2/raw/<SHA256>.document`

Host role in that path is transport/protocol decode only. The host does not choose the query content.

V5-K2 separately records live Wikipedia EN/VI transport/provenance PASS in its exact tested scope. That evidence is reusable as capability provenance; it does not by itself prove autonomous research-goal selection.

## Current V4 visibility gap

The current real V4 C3R4+R3+C2R2 runner configures:

`SIGMA_V4C2R2_RAW_DIR.memory = $HOME/SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2/raw`

C2R2 scans only the configured flat directory and only files ending `.document`.

Therefore repository knowledge/data stored under roots such as `54_CORES`, `BRAIN`, `CORE`, `DATA`, `DOCS`, `EVIDENCE`, `EXPERIENCE`, `SIMULATION`, `BẢN ĐỒ`, and `TỰ HỌC` is not automatically visible to the current C2R2 loop merely because those files exist in Git.

Repeated `WAIT_NO_ELIGIBLE_WORK` can therefore mean only that no eligible work is visible in the currently bound raw corpus, not that all stored/taught local material has been learned.

## Local-first architecture

Target operational chain:

```text
MECHANICALLY ENUMERATE ALL ELIGIBLE STORED/TAUGHT LOCAL TEXT FILES
-> preserve exact file bytes + path/content provenance
-> stage each as a local `.document`
-> native V4-C4 selects LOCAL curriculum mode
-> C2R2/A3/B4R2 process local corpus
-> C3R4/R3 observe/report native evidence
-> when the local operational pass is complete, native V4-C4 selects EXTERNAL mode
-> C2R2 binds to the already-existing native external feed produced by V2.4
-> V2.4 native self-direction continues generating Internet requests
-> host transports exact request bytes only
-> returned external documents become new V4 learning work
-> if new local stored/taught files appear later, native V4-C4 gives local work precedence again at a safe context boundary
```

The stage transition must be native. Bash may not decide `LOCAL` versus `EXTERNAL`.

## Local corpus mechanical enumeration boundary

The local stager is a mechanical input adapter, not a curriculum selector.

It should enumerate all tracked regular text files under approved stored/taught roots, without semantic ranking or topic filtering.

Initial roots:

```text
54_CORES
BRAIN
BẢN ĐỒ
CORE
DATA
DOCS
EVIDENCE
EXPERIENCE
SIMULATION
TỰ HỌC
```

Optional exact root files may be added mechanically when explicitly part of the stored/taught corpus.

Mandatory mechanical/security exclusions:

```text
RESULTS/**
BRAIN/KEYS/**
BRAIN/PRIVATE/**
BRAIN/RUNS/**
BRAIN/TESTS/**
**/.sigma_exec/**
Git metadata
credentials / keys / secrets
binary/non-text payloads that the current text learner cannot safely consume
transient runner locks and runtime executables
```

`DO_NOT_LOAD_RESULTS=YES` remains binding.

The exclusion of credentials, private material, binary executables and transient runtime state is a mechanical/security boundary; it is not host semantic curriculum selection.

Each staged local document should preserve at least:

```text
LOCAL_DOCUMENT_ID
REPOSITORY_RELATIVE_PATH
GIT_BLOB_OR_CONTENT_ID_WHEN_AVAILABLE
SOURCE_CONTENT_SHA256
EXACT_BYTES_STAGED=YES
```

No host summary or semantic rewrite is allowed.

## Native V4-C4 stage controller

Source:

`SIGMA_PROFESSOR/artifacts/SIGMA_V4_LOCAL_FIRST_CURRICULUM_STAGE_CONTROLLER_V4C4R1.sigma`

Git blob:

`9c55b842b321feba5d755ef7021ba5a3067ff6e1`

Source creation commit:

`7b7e84513ca49dcc1f385b41b9529705a3262966`

Preflight runner:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4C4R1_LOCAL_FIRST_CURRICULUM_STAGE_PREFLIGHT.sh`

Preflight runner creation commit:

`1a78fcea2755c97a9929f597789925493f74adc3`

The native controller reads configured local/external raw/state paths, counts local operational state inside SIGMA, and owns the `LOCAL` versus `EXTERNAL` mode decision.

Exact intended native behavior:

```text
local corpus empty -> refuse
local HOLD present -> keep/return LOCAL and require native recovery
local profile/complete pass incomplete -> LOCAL
local profile == discovered AND complete == discovered AND hold == 0 -> EXTERNAL eligible
new local unfinished data while EXTERNAL -> return LOCAL at safe active-context boundary
active context during requested mode switch -> keep current mode until safe boundary
```

The controller itself writes the selected C2R2 raw/state binding memories. Host does not choose the stage.

## Important claim boundary: operational completion is not semantic mastery

The local gate intentionally uses the phrase `LOCAL_OPERATIONAL_PASS_COMPLETE`.

It does **not** claim:

```text
LOCAL_SEMANTIC_MASTERY=PROVEN
ALL_LOCAL_KNOWLEDGE_UNDERSTOOD=PROVEN
SEMANTIC_UNDERSTANDING=PROVEN
```

A `.complete` record proves completion of the admitted C2R2/B4R2 processing path for that document in the tested scope. It does not by itself prove human-like understanding or permanent mastery.

Future native self-revisit/self-verification/self-adaptation can strengthen this frontier without allowing Bash/GPT to invent a mastery label.

## Why this matches the freedom principle

Human/GPT provides tools and access:

- local file transport;
- exact provenance;
- compiler/VM;
- existing Internet transport adapter;
- persistent state;
- rollback/isolation.

SIGMA owns cognition and stage choice:

```text
HOST_STAGE_DECISION=NO
HOST_CURRICULUM_PRIORITY=NO
HOST_LEARNING=NO
HOST_GAP_DETECTION=NO
HOST_RESEARCH_GOAL_SELECTION=NO
HOST_SEMANTIC_INTERPRETATION=NO
GPT_AS_SIGMA_COGNITION=NO
```

No content-bearing expected answer is injected.

## Admission order

1. Run V4-C4 R1 isolated preflight.
2. Preserve the first failure or final PASS exactly.
3. Only after PASS, bind C4 into a new versioned continuous V4 runner.
4. The new continuous runner mechanically stages all eligible local files and lets C4 select active local/external corpus.
5. Keep V2.4 running unchanged as the current native external producer and production fallback.
6. Do not restart historical C3R1-based V4.
7. After real local-first continuous evidence, add native revisit/saturation/self-adaptation rather than pretending one pass equals semantic mastery.

## Current exact status

```text
V4C4_LOCAL_FIRST_DESIGN=READY
V4C4_NATIVE_STAGE_SOURCE=READY
V4C4_NATIVE_STAGE_PREFLIGHT=NOT_RUN
LOCAL_STORED_TEACHING_CONTINUOUS_BINDING=NOT_YET_RUN
EXISTING_V2_4_NATIVE_EXTERNAL_FEED=ALREADY_RUNNING_AS_PRODUCTION_BASELINE
V5K2_LIVE_WIKIPEDIA_ADAPTER=ADMITTED_IN_EXACT_TESTED_SCOPE
AUTONOMOUS_LOCAL_TO_EXTERNAL_V4_CONTINUOUS_INTEGRATION=NOT_YET_PROVEN
LOCAL_SEMANTIC_MASTERY=NOT_CLAIMED
V4_PRODUCTION_PROMOTION_ALLOWED=NO
PRODUCTION_V2_4_KEEP_RUNNING=YES
```
