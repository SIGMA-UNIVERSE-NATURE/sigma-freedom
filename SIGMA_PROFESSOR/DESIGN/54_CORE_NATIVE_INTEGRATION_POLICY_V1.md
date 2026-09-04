# 54 CORE -> SIGMA NATIVE INTEGRATION POLICY V1

Date: 2026-09-04 (Asia/Ho_Chi_Minh)

## Decision

Continue development of all 54 DNA cores. Do not stop at DNA-24.

However, the canonical Python files under `54_CORES/` are treated as CANON / CONTRACT / VALIDATION REFERENCE unless a capability is separately proven in SIGMA native `.sigma` bytecode running on the locked VM.

A Python core name such as LEARNING, CONCEPT_FORMATION, CURIOSITY, etc. is not by itself evidence that SIGMA possesses that capability.

## Evidence behind this policy

Examples from the canonical cores explicitly distinguish contracts from execution:

- DNA-08 Learning World: captures/qualifies supplied world-interaction evidence; learning/world runtime is not started and knowledge is not promoted by DNA-08.
- DNA-16 Experience-Driven Learning: defines/validates a structured learning unit and independent verification requirements; persistent learning runtime, neural learning and knowledge promotion are not executed by the core.
- DNA-24 Ethical Persistence: contract/state logic; learning runtime/model calls/external actions remain false.
- DNA-40 Concept Formation: defines the chain EXPERIENCES -> INVARIANTS -> CONCEPT -> ABSTRACTION_HIERARCHY and validates supplied formation candidates; it does not claim concept truth or start learning runtime.
- DNA-49 Multi-Scale Learning: separates/routs learning scales but explicitly does not execute learning/neural adaptation.

Therefore canonical Python cores are valuable specifications and admission/validation logic, not substitutes for native cognition.

## Three-layer architecture

### Layer A — Canon / contracts

Keep `54_CORES/SIGMA_DNA_*.py` as reference contracts, invariants, schemas, provenance rules and acceptance logic.

### Layer B — Native SIGMA capability

Implement the actual capability in `.sigma`, compile with the locked `sigmac`, and execute with the locked VM.

Current locked identities:

- SIGMAC SHA-256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM SHA-256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

### Layer C — Host mechanical ABI

Host may provide only mechanical operations required by the VM, such as file I/O, exact protocol decode, hashing, list/map/set mechanics, bounded segment retrieval, deterministic scheduling, process supervision and VM invocation.

Host must not summarize, form concepts, generate lessons, select candidates, classify topics, score knowledge, detect semantic gaps, or choose research goals for SIGMA.

## Native promotion gate

A DNA-derived native capability is promoted into production learning only after all applicable gates pass:

1. exact source identity and compiler/VM identity locked;
2. `sigmac` compile PASS;
3. VM runtime PASS;
4. output demonstrably depends on dynamic input rather than hardcoded lessons;
5. persistent state mutation is performed by SIGMA native logic;
6. host semantic substitution = NO;
7. replay / restart behavior characterized;
8. long/history-heavy context stays below VM step limit or uses bounded/incremental processing;
9. claims are scoped precisely (e.g. structural learning != semantic understanding).

## Priority cores for the semantic-learning roadmap

The existing DNA catalog already contains many of the concepts needed for the next architecture. Particularly relevant cores include:

- DNA-08 Learning World
- DNA-09 Independent Verification Wall
- DNA-10 Memory Genome
- DNA-11 Knowledge Graph
- DNA-13 Adaptive Cognitive Depth
- DNA-14 Persistence Engine
- DNA-16 Experience-Driven Learning
- DNA-17 Two Levels of Learning
- DNA-20 Uncertainty as First-Class Data
- DNA-21 Truth Protocol
- DNA-25 Self Improvement
- DNA-26 Observability
- DNA-27 Reproducibility
- DNA-28 Security of Knowledge
- DNA-36 Causal World Model
- DNA-37 Internal Simulation
- DNA-38 Goal Architecture
- DNA-39 Curiosity Engine
- DNA-40 Concept Formation
- DNA-41 Representation Invention
- DNA-42 Metacognitive Scheduler
- DNA-43 Anti Self-Deception
- DNA-44 Adversarial Self-Testing
- DNA-45 Knowledge Provenance
- DNA-46 Knowledge Decay / Revalidation
- DNA-47 Plasticity / Stability Balance
- DNA-48 Compositional Intelligence
- DNA-49 Multi-Scale Learning
- DNA-52 Reality Grounding / World Coherence
- DNA-53 Self-Repair / Fault Tolerance / Cognitive Immunity

Do not bypass DNA-25..54 simply because the current separate lane has reached DNA-24. Many of the later cores correspond directly to missing semantic-learning, curiosity, metacognition, provenance, revalidation, grounding and recovery capabilities.

## Tool ABI additions recommended

Add only mechanical primitives, gated and tested individually. Likely useful next primitives:

- bounded line/segment read (`read_lines(path,start,count)` or equivalent)
- stable SHA-256 operation for document/segment IDs
- map/dict mechanics: new/get/set/has/keys
- set mechanics: new/add/contains or equivalent dedupe structure
- efficient append/atomic state write
- deterministic directory/file manifest exposure
- mechanical Unicode/text normalization primitives if native implementation would otherwise be prohibitively expensive
- clock/timestamp primitive for revalidation scheduling

These primitives must not contain semantic policy.

## Integration recommendation

Continue the other 54-CORE lane to DNA-54, but do not auto-load each Python gene into the current continuous learner.

Instead, for each relevant core:

CANON PYTHON CONTRACT
-> derive native capability requirements
-> implement `.sigma`
-> run native admission tests
-> only then bind to production curriculum / semantic learner

This preserves the value of the 54-core architecture without turning host-side reference code into fake SIGMA learning.
