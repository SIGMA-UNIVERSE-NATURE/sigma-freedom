# WINDOW A — BLACK-BOX DIFFERENTIAL GRAMMAR EVIDENCE — ELSE BATCH 1

ROLE=WINDOW_A_ONLY
DATE=2026-08-26
PRIMARY_ROOT=~/SIGMA/sigma_genesis1
PROBE_DIR=.sigma_tmp/WINDOW_A_SURFACE_PROBES_ELSE1_20260826_141200
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_EXECUTION_USED=NO
NO_EXPECTED_SEMANTIC_ANSWER=YES
PRIVATE_SOURCE_INSPECTED=NO
PRIVATE_SOURCE_PUBLISHED=NO
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21

Evidence target for this batch is compiler acceptance only:
SOURCE FORM → CURRENT COMPILER RC → BYTECODE CREATED OR NOT.

No branch semantics, runtime truth evaluation, cognition, understanding, or universal grammar claim is made.

## TEST WA-ELSE-01

TEST_ID=WA-ELSE-01
QUESTION=Does exact uppercase `ELSE { ... }` attached to an already accepted exact IF form compile under the current compiler?
VARIANT_A=Header + `⟡(Σ.MAIN) { IF (1 < 2) { ⚡ a: 1; } }`
VARIANT_B=Same exact IF form with attached `ELSE { ⚡ a: 2; }`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=38c8e8a597b935be735aa9e0f498e0cfca23cb26764071bc03d9bcd418062393
SOURCE_SHA256_B=021accd524de53d00d4c3bfd10d3f0b48a18ccac7685780c6ea7f9ba0693c4a3
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=6f4ca13ad055980679b157b97c8c7dcc8af2adc8c97c5992c63a3e94cf2d974e
BYTECODE_SIZE_A=84
COMPILER_STDOUT_SIZE_A=157
COMPILER_STDERR_SIZE_A=0
COMPILER_RC_B=0
BYTECODE_CREATED_B=YES
BYTECODE_SHA256_B=ccc7872e8683ec805c75688124e13776b3c317bde5efc3e89143f6f86600a677
BYTECODE_SIZE_B=94
COMPILER_STDOUT_SIZE_B=157
COMPILER_STDERR_SIZE_B=0
OBSERVATION=Both the exact IF control and the same form with attached uppercase `ELSE { ... }` were accepted and emitted bytecode.
PROVEN_SCOPE=Exact compiler acceptance of the tested uppercase `ELSE { ... }` attachment to the tested parenthesized IF form under the identified current compiler.
NOT_PROVEN_BEYOND=No ELSE runtime branch semantics, association rules beyond this exact one-IF/one-ELSE form, ELSE-IF surface, nesting semantics, or cognition claim is established.

## CONFLICT RESOLUTION BOUNDARY

PRIOR_CONFLICT=Current runtime-scope prose mentioned IF/ELSE behavior while the 21-capability list did not include ELSE.
CURRENT_EXACT_SURFACE_RESULT=The exact tested uppercase ELSE source form is now machine-accepted by current compiler.
CONFLICT_RESOLVED_FOR_EXACT_SOURCE_ACCEPTANCE=YES
CONFLICT_RESOLVED_FOR_ALL_RUNTIME_ELSE_CLAIMS=NO

## BATCH SUMMARY

DIFFERENTIAL_PROBES_RUN=1
COMPILER_VARIANTS_RUN=2
COMPILER_ACCEPT_CASES=2
COMPILER_REJECT_CASES=0
TIMEOUT_CASES=0
GPT_ANSWER_IMPOSITION_USED=NO
CAPABILITY_RESEARCH_RERUNS=0
