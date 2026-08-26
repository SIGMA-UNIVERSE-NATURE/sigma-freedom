# WINDOW A — BLACK-BOX DIFFERENTIAL GRAMMAR EVIDENCE — GROUPING BATCH 1

ROLE=WINDOW_A_ONLY
DATE=2026-08-26
PRIMARY_ROOT=~/SIGMA/sigma_genesis1
PROBE_DIR=.sigma_tmp/WINDOW_A_SURFACE_PROBES_GRP1_20260826_135757
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_EXECUTION_USED=NO
NO_EXPECTED_SEMANTIC_ANSWER=YES
PRIVATE_SOURCE_INSPECTED=NO
PRIVATE_SOURCE_PUBLISHED=NO
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21

Evidence target is compiler acceptance only:
SOURCE FORM → CURRENT COMPILER RC → BYTECODE CREATED OR NOT.

## TEST WA-GRP-01

TEST_ID=WA-GRP-01
QUESTION=In the exact neutral binding context, are both bare integer literal `1` and parenthesized literal `(1)` accepted?
VARIANT_A=Header + `⟡(Σ.MAIN) { ⚡ a: 1; }`
VARIANT_B=Same exact form with `⚡ a: (1);`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=9e663743c008d54674f4c5abd581ed3547095769e6e5c0b8297c5ccd626b48c8
SOURCE_SHA256_B=0733cd36fb32c227cc3c637e9d30f419ea7dd7cfe2b6dc43d0c52e7771ad26e7
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875
BYTECODE_SIZE_A=53
COMPILER_RC_B=0
BYTECODE_CREATED_B=YES
BYTECODE_SHA256_B=26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875
BYTECODE_SIZE_B=53
OBSERVATION=Both exact forms were accepted and emitted identical bytecode hash/size.
PROVEN_SCOPE=Compiler acceptance of exact `1` and `(1)` forms in this neutral binding context; parentheses are accepted and are not required for this exact literal control.
NOT_PROVEN_BEYOND=No universal grouping rule, runtime semantic equivalence, precedence, associativity, or optimizer behavior is established.

## TEST WA-GRP-02

TEST_ID=WA-GRP-02
QUESTION=In the exact neutral binding context, are both `1 + 2` and parenthesized `(1 + 2)` accepted?
VARIANT_A=Header + `⟡(Σ.MAIN) { ⚡ a: 1 + 2; }`
VARIANT_B=Same exact form with `⚡ a: (1 + 2);`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=ab34fa1d149c625b3ec8a49fd0c3db5d70ca8a5336d831b4720d545af5c2d092
SOURCE_SHA256_B=53541bf547eeddc6c9305fae9b3113b63c0e305ff6a9f74907a14a7f011bbaa2
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=5540af9fb2b936bead4c2c8fdf4fcefbb9487875b1d79f3beca0f44c1476faf6
BYTECODE_SIZE_A=69
COMPILER_RC_B=0
BYTECODE_CREATED_B=YES
BYTECODE_SHA256_B=5540af9fb2b936bead4c2c8fdf4fcefbb9487875b1d79f3beca0f44c1476faf6
BYTECODE_SIZE_B=69
OBSERVATION=Both exact infix forms were accepted and emitted identical bytecode hash/size.
PROVEN_SCOPE=Compiler acceptance of exact `1 + 2` and `(1 + 2)` forms in this neutral binding context; parentheses are accepted and are not required for this exact infix control.
NOT_PROVEN_BEYOND=No precedence/associativity table, arithmetic runtime semantics, or general parenthesized-expression production is inferred beyond these exact forms.

## BATCH SUMMARY

DIFFERENTIAL_PROBES_RUN=2
COMPILER_VARIANTS_RUN=4
COMPILER_ACCEPT_CASES=4
COMPILER_REJECT_CASES=0
TIMEOUT_CASES=0
GPT_ANSWER_IMPOSITION_USED=NO
CAPABILITY_RESEARCH_RERUNS=0
