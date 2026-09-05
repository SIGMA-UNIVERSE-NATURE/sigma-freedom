# V2.11R.1 — Revisit execution + archive re-entry — source ready

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

Dependency admitted:

- V2.10R.1 lifecycle PASS checkpoint: `220fa78bce0d9873533cb8acce102fc411107924`.

User-delivery candidate:

- source file: `SIGMA_REVISIT_EXECUTION_ARCHIVE_REENTRY_V2_11R1.sigma`
- source SHA256: `88568071e657cb94845d97d94237688ec62d88121f6ff90dc8cbc96cbe685d9e`
- runner file: `RUN_SIGMA_V211R1_REVISIT_EXECUTION_ARCHIVE_REENTRY_PREFLIGHT.sh`
- runner SHA256: `47ba6cb8e1f6c93adb080a99a6cd3fb9c28d17ccf86f555dd04263265705030a`

Static audits:

- `H_CALL_ARITY_AUDIT=PASS`
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`
- `STR_STARTS_DEPENDENCY=NONE`
- `DIRECT_STR_DEPENDENCY=NONE`
- runner `bash -n` RC = 0
- generation-cursor bounded gate present
- segment-cursor bounded gate present

Native design:

- consume committed V2.10 lifecycle records;
- `REVISIT` creates pending work only when committed revisit-event count exceeds completed revisit-generation count;
- work-local state paths are constructed natively from selected document ID + mechanical state-directory config;
- `<id>.generation` stores one `|` per completed revisit generation;
- `<id>.cursor` stores one `|` per committed segment in the current pending generation;
- `<id>.evidence` stores `WORK + GEN + CURSOR + BEST_LOCAL_RELATION + COMMIT=YES`;
- evidence commit precedes segment-cursor advance;
- generation advances only after document completion;
- segment cursor resets only after generation completion;
- latest `ARCHIVE_FOR_NOW` holds without deleting evidence;
- archive re-entry proven target is a later committed `REVISIT` lifecycle action only;
- time-based archive re-entry is NOT_PROVEN;
- semantic-novelty archive re-entry is NOT_PROVEN.

Admission target on real selected 10-line document:

- real lifecycle regenerated natively from exact admitted V2.8R.1 -> V2.8D.1 -> V2.9R.1 -> V2.10R.1 chain;
- lifecycle action must be `REVISIT`;
- revisit generation token `|`;
- segment 0 `[0,8)` expected best relation `in => the`;
- fresh VM segment 1 `[8,10)` expected best relation `As => disagreements`;
- fresh VM completion must advance generation cursor to `|` and reset segment cursor empty;
- post-completion fresh VM must report no pending revisit for that lifecycle event;
- deterministic evidence replay required.

Counterexamples / policy gates:

- archive-only -> hold and no evidence deletion;
- archive followed by later committed revisit -> re-entry and execution;
- no committed lifecycle action -> wait;
- lifecycle/evidence/generation cursor/segment cursor over-budget -> refuse mutation.

Important schema limitation:

V2.10 lifecycle records do not yet contain an explicit event/epoch ID. Repeated identical revisit decisions for the same work/result are deduplicated upstream. V2.11R.1 therefore proves execution of admitted lifecycle events, not unrestricted repeated identical revisit epochs. Explicit cycle/event identity is a dependency for the later autonomous cycle controller.

Current runtime truth:

- compile PASS = NOT_PROVEN;
- runtime PASS = NOT_PROVEN;
- bytecode SHA256 = UNKNOWN;
- admission = NOT_PROVEN;
- semantic understanding = NOT_PROVEN;
- semantic truth validation = NOT_PROVEN;
- bounded file I/O = NOT_PROVEN;
- mid-append crash atomicity = NOT_PROVEN.
