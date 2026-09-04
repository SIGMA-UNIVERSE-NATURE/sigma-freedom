SIGMA V2.7P.1 STRICT PERSISTENT + BOUNDED STRUCTURAL GROUPING PREFLIGHT

Status:
SOURCE_READY_STATIC_PASS
ADMISSION=NOT_PROVEN

Purpose:
Tighten the existing V2.7 structural-grouping preflight so the curriculum lane can test two global admission requirements that the original non-incremental synthetic runner does not by itself establish:
1. prior native persistent state materially affects a later fresh VM run;
2. profile-state/input scan work is bounded in the admitted QA scope and over-budget inputs are refused before native scan/mutation.

This remains STRUCTURAL grouping only.
SEMANTIC_GROUPING=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN

Native source:
SIGMA_PROFESSOR/artifacts/SIGMA_STRUCTURAL_GROUPING_V2_7P_1.sigma
SOURCE_SHA256=3142d5f5bcc75f7a7c3640be2352de373604713a39f977ef54ba14c414455163
GIT_BLOB_SHA1=88e52075c8d1025d2034da7c732c30f8eda86d35

Runner:
SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V27P1_PERSISTENT_STRUCTURAL_GROUPING_PREFLIGHT.sh
RUNNER_SHA256=9ff2269fb1450f3d128200e52b89ce1c800fa427a000131a9f9f91823054e3f5
GIT_BLOB_SHA1=4dec69928adf701062a3ffa5694dbd8e301b275d

Locked runtime required:
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

Native state/input protocol in this QA scope:
- new input: .sigma_exec/SIGMA_V27P1_NEW_PROFILES.memory
- persisted committed state: .sigma_exec/SIGMA_V27P1_PROFILE_STATE.memory
- native assignments: .sigma_exec/SIGMA_V27P1_GROUP_ASSIGNMENTS.memory
- state record: DOC=<id> || ANCHOR=<structural-anchor> || COMMIT=YES
- input record: DOC=<id> || ANCHOR=<structural-anchor>

Scope limits:
- MAX_STATE_SPLIT_LINES=65 (supports up to 64 leading-newline committed records in this format);
- MAX_INPUT_SPLIT_LINES=16;
- whole-file read remains current ABI behavior, so BOUNDED_FILE_IO=NOT_PROVEN;
- field delimiters are trusted protocol syntax in this QA scope; arbitrary delimiter-bearing document IDs/anchors are not admitted;
- append_text crash atomicity is NOT_PROVEN; state reuse requires a complete COMMIT=YES field and malformed/uncommitted records are ignored.

Prepared runtime gates, same compiled bytecode:

A. POSITIVE PERSISTENCE
1. fresh state + DOC=A/anchor X -> singleton;
2. fresh VM process + DOC=B/anchor X -> persisted A must be reused, producing one shared group with A and B;
3. fresh VM replay of B/X -> no state growth; exact assignment hash must reproduce.

B. NEGATIVE / COUNTEREXAMPLE
1. duplicate A/X in later run must not inflate support or create a group;
2. B/Y with Y != X must leave A and B as singletons;
3. malformed historical state lacking COMMIT=YES must not count.

C. BOUNDEDNESS
1. state above the native line budget -> STATE_LIMIT_EXCEEDED=1, STATE_MUTATION_ALLOWED=NO, state hash unchanged;
2. input above the native line budget -> INPUT_LIMIT_EXCEEDED=1, STATE_MUTATION_ALLOWED=NO, state hash unchanged.

Static review completed before device run:
H_CALLS=56
H_CALL_ARITY_AUDIT=PASS
STR_STARTS_DEPENDENCY=NONE
NATIVE_NOT_EQUAL_DEPENDENCY=NONE
BASH_N_RC=0
SOURCE_BYTE_IDENTITY_VIA_GIT_BLOB_MATCH=PASS
RUNNER_BYTE_IDENTITY_VIA_GIT_BLOB_MATCH=PASS

Host role in runner:
- supplies synthetic QA bytes;
- resets isolated preflight state between independent test families;
- hashes exact bytes;
- invokes locked sigmac and VM;
- checks exact protocol outputs/hashes.

HOST_GROUP_SELECTION=NO
HOST_TOPIC_CLASSIFICATION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO

Not yet proven until device execution:
COMPILE_PASS=NOT_PROVEN
RUNTIME_PASS=NOT_PROVEN
DYNAMIC_CAPABILITY_PROVEN=NOT_PROVEN
PERSISTENT_STATE_TEST=NOT_PROVEN
FRESH_VM_STATE_REUSE=NOT_PROVEN
NEGATIVE_TEST=NOT_PROVEN
STEP_LIMIT_STATUS=NOT_PROVEN
BYTECODE_SHA256=UNKNOWN
VM_RC=UNKNOWN
ADMISSION=NOT_PROVEN

Required next action:
Install the exact P1 source + runner into the isolated Termux preflight namespace, run once under the locked compiler/VM, preserve every exact RC/log/state hash, and checkpoint PASS or FAIL without changing the admission definition.
