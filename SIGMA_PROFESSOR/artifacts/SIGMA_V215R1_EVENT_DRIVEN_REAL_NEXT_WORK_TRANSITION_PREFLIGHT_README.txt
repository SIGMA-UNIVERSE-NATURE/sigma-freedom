SIGMA V2.15R.1 EVENT-DRIVEN REAL NEXT-WORK TRANSITION PREFLIGHT

This is a composition/admission step; it adds no new cognitive native source.

Purpose:
Prove that an exact SELECT_NEXT_WORK event emitted by native SIGMA can drive the already-admitted real-survey selector to a DIFFERENT real document, and that the native deep learner can begin bounded learning on that second real document.

Native chain under test:
1. exact V2.8R.1 selector selects first real work and persists DISPATCHED state;
2. V2.13 receives a structural matching TEST fixture for the current work/cycle and itself decides REOBSERVED -> ARCHIVE_FOR_NOW;
3. V2.14C1 consumes that native lifecycle and emits SELECT_NEXT_WORK;
4. mechanical host dispatcher routes only that exact stage to V2.8R.1;
5. V2.8R.1 selects the second real work from the same frozen 56-document survey;
6. V2.8D.1 resolves and begins segment learning on the second real snapshot document;
7. fresh VM continuation must reuse persisted work/cursor state.

Expected deterministic real selector sequence already observed in admitted V2.8R.1:
- first: 0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b
- second: 26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6

Important claim limit:
The archive-producing evidence in this transition preflight is a structural TEST fixture. Therefore this does NOT prove that the current real first work autonomously archives, and it does NOT prove a multi-document closed autonomous cycle.

What it can prove after PASS:
REAL_NATIVE_FIRST_TO_SECOND_WORK_TRANSITION=PROVEN_IN_FROZEN_56_DOCUMENT_SURVEY_SCOPE
and
SECOND_REAL_WORK_NATIVE_LEARNING_STARTED=PASS.

Negative route:
A native EXECUTE_REVISIT event must not invoke the real selector; selector state hash must remain unchanged.

No new native cognitive source is introduced here. It composes already-admitted native capabilities and tests the host as a mechanical event router only.

Runner SHA256:
3b54dc2fce2d408c9ffb9f4cedead91a2b82f69ec8a1688d6518837e9e02e687

Static:
BASH_N_RC=0
