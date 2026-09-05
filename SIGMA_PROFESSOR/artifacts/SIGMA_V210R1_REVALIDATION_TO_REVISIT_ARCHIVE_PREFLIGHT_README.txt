SIGMA V2.10R.1 REVALIDATION -> REVISIT / ARCHIVE_FOR_NOW

Goal:
Convert committed structural revalidation evidence into a persistent lifecycle scheduling action inside native SIGMA.

Policy:
- `NOT_REOBSERVED` -> `REVISIT`
- `REOBSERVED` -> `ARCHIVE_FOR_NOW`
- no committed valid result -> `WAIT_FOR_REVALIDATION`
- conflicting committed results -> `WAIT_FOR_REVALIDATION`

Important:
- `ARCHIVE_FOR_NOW` is a scheduling state, not deletion.
- raw documents, survey state, deep evidence and revalidation evidence remain immutable.
- `REVISIT` does not mean semantically false.
- `ARCHIVE_FOR_NOW` does not mean semantically true.

Real path:
The runner mechanically regenerates the exact admitted real chain:
V2.8R.1 native selection -> V2.8D.1 real deep evidence -> V2.9R.1 real revalidation.
The real admitted result must remain `NOT_REOBSERVED`; V2.10 must therefore select `REVISIT`.

Branch/gate coverage:
- real NOT_REOBSERVED -> REVISIT;
- synthetic REOBSERVED -> ARCHIVE_FOR_NOW;
- uncommitted revalidation -> WAIT, no mutation;
- conflicting committed results -> WAIT, no mutation;
- fresh VM lifecycle-state reuse;
- deterministic replay;
- partial lifecycle record ignored;
- lifecycle and revalidation over-budget refusal;
- real upstream survey/document/deep-evidence/revalidation immutability.

Lifecycle state record:
`WORK=<id> || ACTION=<REVISIT|ARCHIVE_FOR_NOW> || FROM_RESULT=<result> || COMMIT=YES`

Bounds:
MAX_REVALIDATION_SPLIT_LINES=65
MAX_LIFECYCLE_SPLIT_LINES=65

Host boundary:
HOST_LIFECYCLE_DECISION=NO
HOST_REVISIT_DECISION=NO
HOST_ARCHIVE_DECISION=NO
HOST_TRUTH_DECISION=NO
HOST_LEARNING=NO

Claim limits:
STRUCTURAL_LIFECYCLE_ONLY=YES
SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
BOUNDED_FILE_IO=NOT_PROVEN
MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN

Source SHA256:
67fb7234c0cd9e84c602a6dadb55f6e1ced6265406745ba6b3b9a7a95e0c4993

Runner SHA256:
6a0f9749c640cf9477815daa7387765ba461b5822296a40bdb9fbd7ea905b6d2

Static:
H_CALL_ARITY_AUDIT=PASS
NATIVE_NOT_EQUAL_DEPENDENCY=NONE
STR_STARTS_DEPENDENCY=NONE
DIRECT_STR_DEPENDENCY=NONE
BASH_N_RC=0
