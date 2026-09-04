SIGMA V2.8D.1 REAL SELECTED WORK -> DEEP RE-LEARN SEGMENT CURSOR PREFLIGHT

Goal:
Prove an end-to-end native bridge from real curriculum selection to bounded deep re-learning of that selected real snapshot document.

Stage A — native curriculum selection:
- reuses exact admitted V2.8R.1 source;
- compiles with locked sigmac;
- compiled bytecode must match observed admitted bytecode SHA:
  0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5
- real V2.5B.2 56-document survey is the source evidence;
- native curriculum must select:
  0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b

Stage B — native deep re-learning:
- deep engine reads selected work directly from `.sigma_exec/SIGMA_V28R1_SELECTED_WORK.memory`;
- reads only a mechanical snapshot-directory config;
- SIGMA constructs `<snapshot>/<selected>.document` itself;
- SIGMA verifies file existence via host("file_exists") as a mechanical ABI primitive;
- host does not choose the document or segment.

Selected real document:
0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b.document
Known V2.5 survey line count: 10.

Expected deep traversal:
- segment 0: [0,8)
- fresh VM segment 1: [8,10)
- fresh VM completion at segment index 2

Persistence:
- active work identity persisted separately;
- cursor is work-local and reset natively when selected work changes;
- evidence records:
  `WORK=<id> || CURSOR=<pipe-state> || BEST_LOCAL_RELATION=<relation> || COMMIT=YES`
- committed work+cursor evidence is deduplicated before append;
- evidence append occurs before cursor advance;
- partial/uncommitted evidence records are ignored.

Tests:
- real native selected work;
- two real document segments + completion across fresh VM processes;
- exact deterministic evidence replay;
- negative empty selected work refuses all mutation;
- over-budget evidence state refuses mutation;
- real survey SHA unchanged;
- selected snapshot document SHA unchanged.

Bounds:
MAX_EVIDENCE_SPLIT_LINES=65
SEGMENT_LINE_BUDGET=8

Claim limits:
- structural deep re-learning only;
- semantic importance NOT_PROVEN;
- semantic understanding NOT_PROVEN;
- whole-file read_text remains current ABI, so bounded file I/O NOT_PROVEN;
- append mid-write crash atomicity NOT_PROVEN.

Source SHA256:
3dfc25c5f6e9cdbabd193bb7c3d8845ba025cb12e1b3824430a1a6ec280ec74f

Runner SHA256:
461f4ca50add41e067a9402a64e2f7451b47c4491d08f3cc7b5f51b1c987f059

Static:
H_CALL_ARITY_AUDIT=PASS
NATIVE_NOT_EQUAL_DEPENDENCY=NONE
STR_STARTS_DEPENDENCY=NONE
DIRECT_STR_DEPENDENCY=NONE
BASH_N_RC=0
