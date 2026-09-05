SIGMA V2.9R.1 DEEP RE-LEARN COMPLETION -> STRUCTURAL REVALIDATION

Goal:
Revalidate a previously surveyed structural anchor only after the selected work has completed deep re-learning.

This is NOT semantic truth validation.

Real positive path:
1. exact admitted V2.8R.1 regenerates native selected work from the real 56-document survey;
2. exact admitted V2.8D.1 regenerates real committed segment evidence;
3. V2.9R.1 derives deep-completion from selected document line count + persisted cursor;
4. V2.9R.1 reads the old committed V2.5 baseline anchor for the selected document;
5. V2.9R.1 reads committed deep segment best-anchor evidence;
6. result is REOBSERVED iff the old baseline anchor appears as a committed deep segment best anchor.

Expected real selected document:
0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b

Expected real baseline:
in => the

Expected admitted real deep evidence:
- segment 0 best anchor: in => the
- segment 1 best anchor: As => disagreements
- therefore baseline matching segments = 1
- result = REOBSERVED

Important D1 terminal-state handling:
The prior V2.8D.1 runner ended with a synthetic evidence-limit fixture.
This runner first preserves that terminal QA state as reference, then regenerates the real evidence using the exact admitted D1 native bytecode before revalidation.

Persistent revalidation state:
`WORK=<id> || RESULT=<REOBSERVED|NOT_REOBSERVED> || BASELINE=<anchor> || COMMIT=YES`

Gates:
- real positive REOBSERVED;
- fresh VM reuse must not duplicate committed revalidation state;
- deterministic replay;
- synthetic completed counterexample -> NOT_REOBSERVED;
- incomplete deep traversal -> PENDING and no state mutation;
- uncommitted matching evidence ignored;
- state/evidence/survey over-budget refusal;
- real survey, real snapshot document, and regenerated real evidence immutable through revalidation tests.

Bounds:
MAX_SURVEY_SPLIT_LINES=65
MAX_EVIDENCE_SPLIT_LINES=65
MAX_STATE_SPLIT_LINES=65
SEGMENT_LINE_BUDGET=8

Host boundary:
HOST_REVALIDATION_DECISION=NO
HOST_TRUTH_DECISION=NO
HOST_LEARNING=NO

Claim limits:
STRUCTURAL_REVALIDATION_ONLY=YES
SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
BOUNDED_FILE_IO=NOT_PROVEN
MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN

Source SHA256:
94b12091d0d0727f23f57b298ee9ed71d11a2085571273496138990ca56f920b

Runner SHA256:
c87fdcd46587b3e0200eed4be1f631ee5c2d5b270c1ef2a10141bd94e1ad4ce7

Static:
H_CALL_ARITY_AUDIT=PASS
NATIVE_NOT_EQUAL_DEPENDENCY=NONE
STR_STARTS_DEPENDENCY=NONE
DIRECT_STR_DEPENDENCY=NONE
BASH_N_RC=0
