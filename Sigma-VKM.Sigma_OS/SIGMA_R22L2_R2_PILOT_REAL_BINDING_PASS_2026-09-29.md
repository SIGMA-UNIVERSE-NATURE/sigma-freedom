# SIGMA R22L2 — R2 Pilot Real Binding PASS

Date: 2026-09-29
Source: user-supplied Termux runtime output.

VALIDATOR_SCRIPT_SHA256=
fe6fbf6c1edc21db6ceab6e876e6ace687920c196c460a1348d279ac17dc5687

R22L2_PACKAGE_SHA256=
cee0215255a5cf9342509811723274bd8aa25afc2f1d508d200b657f9183190f

R22L2_READY_TASKS=referent_identity
R22L2_SEMGOLD_RECORDS=10
R22L2_BINDING_RECORDS=8
R22L2_FRESH_FINAL_RECORDS=2
R22L2_ERROR_COUNT=0

REAL_BINDING_READY=YES

FRESH_FINAL_EXPOSED_TO_SIGMA=NO
LEARNING_BYTES_EXPOSED_TO_SIGMA=NO

R22L2_R2_PILOT_REAL_BINDING=PASS

READY_SEMANTIC_TASKS=referent_identity
BINDING_RECORD_COUNT=8

PACKAGE_CHECKSUMS=PASS
SOURCE_SPAN_BINDING=PASS
PROVENANCE_V2_BINDING=PASS
GLOBAL_SPLIT_LEAKAGE_AUDIT=PASS
FRESH_FINAL_SEAL=PASS

FRESH_FINAL_INCLUDED_IN_LEARNING_BINDING=NO
FRESH_FINAL_EXPOSED_TO_SIGMA=NO

REAL_SEMANTIC_CORPUS_CONSUMED=NO
REAL_SEMANTIC_LEARNING_EXECUTED=NO

NEXT=
R22M3_REAL_SEMANTIC_PILOT_IMPORT_AND_CANDIDATE

MANUAL_REBOOT_REQUIRED=NO

## Interpretation boundary

This checkpoint establishes a real semantic corpus binding package suitable for pilot import.

It establishes:
- package checksums pass;
- source spans and provenance bindings pass;
- split leakage audit passes;
- fresh-final partition is sealed and excluded from learning bindings;
- referent_identity is the ready semantic task;
- real binding is ready.

It does not establish real corpus consumption or semantic learning yet.
