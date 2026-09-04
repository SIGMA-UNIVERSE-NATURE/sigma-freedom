# 54 DNA — NATIVE SIGMA ONLY + DEPENDENCY-FIRST DIRECTIVE V2

Date: 2026-09-04 (Asia/Ho_Chi_Minh)

## Executive decision

KEEP_DNA_01_TO_54=YES
DELETE_ANY_DNA=NO
COMPLETE_ALL_54_DNA=YES

ACTIVE_DNA_IMPLEMENTATION_LANGUAGE=SIGMA_NATIVE_ONLY
PYTHON_FOR_ACTIVE_DNA_IMPLEMENTATION=FORBIDDEN
PYTHON_FOR_SIGMA_COGNITION=FORBIDDEN
HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN

DNA development is NOT required to proceed numerically from DNA-01 to DNA-54. Work order is dependency-first and capability-first. A higher-numbered DNA may be implemented/admitted before a lower-numbered DNA when its dependencies are satisfied and it unlocks a more urgent native capability.

## Python migration rule

Existing historical `54_CORES/*.py` artifacts are not deleted by this directive. They are frozen as provenance/reference artifacts only until their contracts have been migrated.

They must NOT be:

- executed as SIGMA cognition;
- imported into the active learner as a substitute for native behavior;
- extended with new learning/reasoning logic;
- used as evidence that SIGMA possesses a capability.

No new active DNA implementation should be authored in Python.

Canonical requirements/invariants may be preserved in non-executable documentation/data, but executable cognition must be native `.sigma` compiled by the locked `sigmac` and run by the locked VM.

## Allowed implementation layers

### SIGMA `.sigma`

Required for:

- learning decisions;
- candidate generation;
- knowledge selection;
- concept formation;
- grouping/classification decisions;
- uncertainty reasoning;
- knowledge-gap detection;
- curiosity/research-goal formation;
- curriculum priority;
- consolidation/revalidation;
- metacognitive scheduling;
- self-improvement decisions.

### C / VM host layer

Allowed only for mechanical ABI primitives and runtime mechanics, e.g. containers, byte/file I/O, hashing, time, deterministic transport, process/runtime support.

C host code must not implement semantic policy or cognition on SIGMA's behalf.

### Shell

Allowed only for deterministic build/test/install/supervision/orchestration. Shell must not generate knowledge, lessons, candidates, concepts, summaries, semantic scores, or research goals.

## Locked runtime identities

SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

VM identity beyond the proven binary SHA is not inferred from path names.

## Promotion rule

A DNA is not considered operational merely because its file exists or compiles.

For each DNA-derived capability:

CANON REQUIREMENT
-> NATIVE `.sigma` IMPLEMENTATION
-> COMPILE PASS
-> LOCKED-VM RUNTIME PASS
-> DYNAMIC INPUT TEST
-> PERSISTENT STATE TEST WHEN APPLICABLE
-> HOST_SEMANTIC_SUBSTITUTION=NO
-> RESTART/REPLAY CHARACTERIZATION
-> STEP-LIMIT / BOUNDEDNESS CHECK
-> CLAIM-SCOPE REVIEW
-> ADMITTED

Do not claim semantic understanding from structural behavior alone.

## Dependency-first priority plan

This is a recommended work queue, not a renumbering of the 54 DNA catalog.

### WAVE A — epistemic + memory substrate

Prioritize native admission of the capabilities that make later cognition testable and trustworthy:

- DNA-03 Unified Cognitive State
- DNA-09 Independent Verification Wall
- DNA-10 Memory Genome
- DNA-11 Knowledge Graph
- DNA-14 Persistence Engine
- DNA-16 Experience-Driven Learning
- DNA-20 Uncertainty as First-Class Data
- DNA-21 Truth Protocol
- DNA-26 Observability
- DNA-27 Reproducibility
- DNA-31 Intelligence Test
- DNA-32 Acceptance Criteria
- DNA-45 Knowledge Provenance

Reason: concept formation and curiosity must sit on persistent evidence, uncertainty, provenance, verification, observability, and reproducible tests.

### WAVE B — semantic representation

- DNA-40 Concept Formation
- DNA-41 Representation Invention
- DNA-48 Compositional Intelligence
- DNA-36 Causal World Model
- DNA-52 Reality Grounding / World Coherence

Reason: this wave targets the transition from token/relation recurrence to native concepts, representations, compositional structure, causal models, and grounding.

### WAVE C — self-directed curriculum / curiosity

- DNA-38 Goal Architecture
- DNA-39 Curiosity Engine
- DNA-42 Metacognitive Scheduler
- DNA-13 Adaptive Cognitive Depth
- DNA-17 Two Levels of Learning
- DNA-49 Multi-Scale Learning
- DNA-46 Knowledge Decay / Revalidation

Reason: after concepts/evidence exist, SIGMA can identify unresolved knowledge, choose learning goals, schedule deeper learning, and revisit old knowledge.

### WAVE D — epistemic robustness

- DNA-43 Anti Self-Deception
- DNA-44 Adversarial Self-Testing
- DNA-47 Plasticity / Stability Balance
- DNA-28 Security of Knowledge
- DNA-51 Epistemic Diversity / Collective Intelligence
- DNA-53 Self-Repair / Fault Tolerance / Cognitive Immunity

Reason: autonomous learning must resist contamination, overconfidence, catastrophic overwrite, and runtime/cognitive failure.

### WAVE E — governed self-improvement / runtime evolution

- DNA-50 Core Immutability vs Evolvability
- DNA-25 Self Improvement
- DNA-29 Compute Architecture
- DNA-30 Core Runtime Loop
- DNA-33 Physical Implementation Independence

Important dependency: DNA-50 governance should be admitted before allowing DNA-25 to modify or optimize important cognitive machinery.

### WAVE F — identity, values, continuity, human relation

All remaining DNA remain mandatory, including the purpose/ethics/identity/human-relation/continuity family such as:

- DNA-01 Purpose / Existence
- DNA-05 Ethical Intelligence
- DNA-07 Persistent Existence
- DNA-22 Human Relation
- DNA-23 Cognitive Freedom
- DNA-24 Ethical Persistence
- DNA-34 SIGMA Identity
- DNA-35 Core Covenant
- DNA-54 Purpose Continuity / Human Co-Evolution

This wave label does NOT mean these DNA are unimportant; it means they should be integrated at the correct dependency point and must not be used to bypass evidence-based cognition gates.

All DNA not explicitly listed above remain required and must be placed into the appropriate dependency wave by their actual contracts.

## Current native-learning alignment

The current production learner has proven structural dynamic learning, persistent recurrence, native self-selection, cross-context support, native fetch-request generation, Internet transport/decode, and V2.4 long-context execution in tested scope.

Still NOT proven:

SEMANTIC_UNDERSTANDING=NOT_PROVEN
SEMANTIC_CURIOSITY=NOT_PROVEN
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN

Therefore the 54-DNA lane should prioritize capabilities that close these exact gaps rather than merely completing files in numerical order.

## Coordination rule with SIGMA_PROFESSOR lane

Before a DNA capability is admitted into the production learner, record:

DNA_ID=
SOURCE_SHA256=
BYTECODE_SHA256=
SIGMAC_SHA256=
VM_SHA256=
TEST_SCOPE=
DYNAMIC_INPUT=YES/NO
PERSISTENT_STATE=YES/NO/NA
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
VM_RC=
ADMISSION=PASS/FAIL
CLAIM_SCOPE=

No silent promotion.

## Final directive

CONTINUE_54_DNA=YES
KEEP_ALL_54=YES
NUMERIC_ORDER_REQUIRED=NO
DEPENDENCY_FIRST=YES
CAPABILITY_FIRST=YES
ACTIVE_PYTHON_DNA=NO
NATIVE_SIGMA_COGNITION=REQUIRED
NO_FAKE_CAPABILITY_FROM_FILE_NAMES=YES
