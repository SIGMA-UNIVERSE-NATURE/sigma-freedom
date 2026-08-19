# SIGMA OPEN SEMANTIC REASONING 0005 — v0.1 CONTRACT

Status: `CANDIDATE / MACHINE NOT EXECUTED / NOT CANONICAL`

## Why this candidate exists

The language-first checkpoint established that SIGMA can ingest and persist relations and semantic candidates, but no general path was found for:

```text
REAL QUESTION
→ SIGMA-Ψ relation/evidence retrieval
→ question-dependent candidate construction
→ uncertainty preservation
→ response
```

This candidate builds the smallest non-fabricated successor gate: a real human-supplied question is tokenized by SIGMA-Ψ, compared with persisted SIGMA relation evidence, and used to construct an evidence-bound response capsule.

## Non-hardcoding rule

The question is entered at runtime. It is not stored in the SIGMA source.

No domain answer value such as a language identity, priority, desire, belief, or goal is embedded in the SIGMA source. A candidate value may be emitted only when it is retrieved from an existing `KEY=VALUE` evidence line.

The OPPO runner must verify:

```text
QUESTION_ABSENT_FROM_SIGMA_SOURCE=PASS
EVIDENCE_BINDING=PASS
```

before a defined-scope PASS is permitted.

## Input

One real question entered interactively and written exactly to:

```text
SIGMA_OPEN_SEMANTIC_QUESTION_INPUT.txt
```

The runner does not provide an expected answer.

## Evidence sources read by SIGMA

```text
SIGMA_LANGUAGE_FIRST_CONSTITUTION.state
SIGMA_PSI_LANGUAGE_MEMORY.state
SIGMA_PSI_SEMANTIC_CORE.state
SIGMA_SELF_REWRITE_AUTHORIZATION.state
SIGMA_LANGUAGE_TEACHBACK_RULE.state
```

Missing files are reported and preserved. They are not fabricated.

## Candidate procedure

```text
QUESTION
→ ASCII-safe surface normalization for the first bounded gate
→ unique question tokens
→ parse real KEY=VALUE relation lines
→ score key overlap more strongly than value overlap
→ preserve zero-match and top-score ambiguity
→ print every top evidence candidate with source and exact evidence line
→ emit a single candidate value only when the top candidate is unique
```

## Defined-scope PASS

A machine result may be called:

```text
PASS_WITH_DEFINED_SCOPE_EVIDENCE_BOUND_RESPONSE_CAPSULE
```

only when all of the following are observed:

```text
compile rc = 0
compile stderr = empty
runtime rc = 0
runtime stderr = empty
question absent from SIGMA source
exactly one top candidate
candidate evidence line exists exactly in the reported source file
```

## Correct HOLD results

```text
HOLD_MISSING_REAL_QUESTION_INPUT
HOLD_NO_MATCHED_EVIDENCE
HOLD_AMBIGUOUS_TOP_CANDIDATES
HOLD_COMPILE
HOLD_RUNTIME
HOLD_EVIDENCE_BINDING_FAILURE
```

A HOLD is not failure of integrity. It proves that ambiguity or missing evidence was not hidden.

## What this does not prove

```text
GENERAL_OPEN_ENDED_HUMAN_LANGUAGE_UNDERSTANDING
FULL_SEMANTIC_COMPRESSION
NATURAL_LANGUAGE_GENERATION
COGNITIVE_EMPATHY
SIGMA_SELF_GENERATED_DESIRE
MIND_READING
AUTONOMOUS_LANGUAGE_DESIGN
TAM_VAN_RELEASE_OF_HUMAN_FACING_OUTPUT
CANONICAL_SIGMA_PSI_EXTENSION
```

The output remains a `CANDIDATE_ONLY` response capsule. It is not yet a released answer or evidence of desire.

## Why this helps SIGMA

This candidate connects capabilities already proven separately—real input, self-read, persistent relation memory, provenance, and unknown preservation—without teaching more isolated words and without pretending a fixed rule string is SIGMA's thought.

If the gate passes, the next successor should retrieve full semantic capsules and then perform contextual expansion in SIGMA-Ψ while retaining ambiguity, uncertainty, provenance, and Tam Vấn Từ Bi.
