# Whole-Work R1 failure and R1H1 correction

## Oppo result — Whole-Work Ladder R1 Stage A

Observed:

- `LOCKED_COMPILE=PASS`
- `WHOLE_WORK_PASS1_NATIVE_RECURRENCE=PASS`
- `WHOLE_WORK_RECURRENT_UNIT_SIGNATURES=PASS`
- `FAIL=FINALIZE_VM`
- `RC=35`

Production PID snapshot reported `5710,23663`; the failure occurred before the final production-identity gate and no production mutation was reported.

## Root cause

Static audit found that `FINALIZE_WHOLE_WORK_SKELETON` computed native integer counts `MC` and `SC` correctly, then attempted to concatenate those integers directly into persistent text:

`... UNIT_COUNT=" + MC + " || SIGNATURE_COUNT=" + SC`

No integer-to-text primitive has been previously admitted in the locked VM lineage. This is the only direct numeric-to-string concatenation found in the candidate and is the exact runtime path first exercised at FINALIZE. Compile therefore passed while the VM could type-fault at runtime.

## R1H1 correction

Candidate: `M5_NATIVE_WHOLE_WORK_STRUCTURAL_MEMORY_R1H1`

- Core SHA256: `a9549a65e3e7229a5ab74e27c0a26514415f3f7a117930d6e52bfbd93b562195`
- Preflight SHA256: `bda40ee9ae3ec8a799a34dc53cfbe7234745243a9d8a6c6bd35b3195bc79e289`
- Candidate bundle SHA256: `d031e73cd766beb6202a16d0527770c989397d1b758a2a9b783c31a023400d15`

The native count gates are unchanged: minimum whole-work units and minimum retained signatures are still checked as integers inside SIGMA. R1H1 only stops serializing the integers into text state. Persistent state records that the native admission count gate was satisfied.

Admission criteria weakened: NO.

## Independent blind R1H1

The blind fixtures and cognitive criteria remain unchanged. Only the target core SHA is updated to R1H1. A separate blind scorer defect was also corrected: the summary PASS/FAIL state is snapshotted at the summary test before a later restart-recall action can overwrite `out/action.txt`.

- Blind auditor SHA256: `0b1b105a9902e0fddc6b8ed090e098c7674ea52d5a949f4ddab6c1812107017f`
- Blind bundle SHA256: `3b47f8f454424406e8c4c0c14315799c367d4054795f7b419c982df4d9a2587e`

Blind still tests distant recurrent recall, role-reversal configuration, high-frequency background suppression, once-only event retention, source removal, restart, and direct whole-work summary. It is expected to expose semantic limitations rather than protect a high score.

## Combined ladder R1H1

- Runner SHA256: `f6431921da6c69055f52293e979ff9216830e6f0d7dda33fcd45e518941db7ff`
- Ladder bundle SHA256: `bb384565fa79294a8ec4ab853ec03dde69350111669627db2c9ab63caa4fc935`

Run R1H1 Stage A first. Only if admission passes should the independent source-removal blind run. Whole-work understanding, summary, theme/value induction, semantic compression and continual narrative learning remain FAIL until their own blind results justify otherwise.
