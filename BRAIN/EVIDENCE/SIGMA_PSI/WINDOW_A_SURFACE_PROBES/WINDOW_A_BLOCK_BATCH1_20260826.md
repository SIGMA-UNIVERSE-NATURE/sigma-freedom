# WINDOW A — BLACK-BOX DIFFERENTIAL GRAMMAR EVIDENCE — BLOCK BATCH 1

ROLE=WINDOW_A_ONLY
DATE=2026-08-26
PRIMARY_ROOT=~/SIGMA/sigma_genesis1
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_EXECUTION_USED=NO
NO_EXPECTED_SEMANTIC_ANSWER=YES
PRIVATE_SOURCE_INSPECTED=NO
PRIVATE_SOURCE_PUBLISHED=NO
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21

Evidence target for this batch is compiler acceptance only:
SOURCE FORM → CURRENT COMPILER RC → BYTECODE CREATED OR NOT.

No runtime namespace semantics, cognition, understanding, or universal grammar claim is made.

## TEST WA-BLK-01

TEST_ID=WA-BLK-01
QUESTION=For the same exact addressed block surface, does an empty body compile compared with a one-binding body?
VARIANT_A=Header plus `⟡(Σ.MAIN) { ⚡ a: 1; }`
VARIANT_B=Same header plus `⟡(Σ.MAIN) { }`
NO_EXPECTED_SEMANTIC_ANSWER=YES
COMPILER_COMMAND_A=./native/sigmac <BLK01_A.sigma> <BLK01_A.sigmab>
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875
BYTECODE_SIZE_A=53
COMPILER_COMMAND_B=./native/sigmac <BLK01_B.sigma> <BLK01_B.sigmab>
COMPILER_RC_B=0
BYTECODE_CREATED_B=YES
BYTECODE_SHA256_B=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a
BYTECODE_SIZE_B=29
OBSERVATION=Both the one-binding addressed block and the empty addressed block were accepted and emitted bytecode.
PROVEN_SCOPE=The exact tested empty `⟡(Σ.MAIN) { }` block form is accepted by the identified current compiler.
NOT_PROVEN_BEYOND=Does not establish all empty-block placements, runtime meaning, or a generic block grammar beyond the tested surface.

## TEST WA-BLK-02

TEST_ID=WA-BLK-02
QUESTION=For the same exact block body, does removing the block address change current-compiler acceptance?
VARIANT_A=Header plus `⟡(Σ.MAIN) { ⚡ a: 1; }`
VARIANT_B=Same header/body with `⟡() { ⚡ a: 1; }`
NO_EXPECTED_SEMANTIC_ANSWER=YES
COMPILER_COMMAND_A=./native/sigmac <BLK02_A.sigma> <BLK02_A.sigmab>
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875
BYTECODE_SIZE_A=53
COMPILER_COMMAND_B=./native/sigmac <BLK02_B.sigma> <BLK02_B.sigmab>
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
OBSERVATION=The addressed block was accepted; the exact otherwise-matched empty-address form was rejected and emitted no bytecode.
PROVEN_SCOPE=In this exact block context, the tested addressed form is accepted while the tested empty-address form is rejected.
NOT_PROVEN_BEYOND=Does not define the full address grammar or namespace semantics.

## TEST WA-BLK-03

TEST_ID=WA-BLK-03
QUESTION=For the same two addressed blocks, does nesting the second block inside the first change current-compiler acceptance compared with top-level placement?
VARIANT_A=Two addressed blocks at top level, `Σ.MAIN` then `Σ.INNER`, each with one neutral binding
VARIANT_B=Same `Σ.INNER` block nested inside the `Σ.MAIN` block after the same neutral binding
NO_EXPECTED_SEMANTIC_ANSWER=YES
COMPILER_COMMAND_A=./native/sigmac <BLK03_A.sigma> <BLK03_A.sigmab>
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=b09169118603025cb52adfa78cc935e95575b376775c1622163fcc6064d71838
BYTECODE_SIZE_A=63
COMPILER_COMMAND_B=./native/sigmac <BLK03_B.sigma> <BLK03_B.sigmab>
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
OBSERVATION=The two top-level addressed blocks were accepted; the tested nested addressed block form was rejected and emitted no bytecode.
PROVEN_SCOPE=The exact tested top-level two-block form is accepted and the exact tested nested-block form is rejected by the current compiler.
NOT_PROVEN_BEYOND=Does not prove every possible nesting construct is forbidden; it freezes only the tested `⟡(...)`-inside-`⟡(...)` surface.

## BATCH SUMMARY

DIFFERENTIAL_PROBES_RUN=3
COMPILER_VARIANTS_RUN=6
COMPILER_ACCEPT_CASES=4
COMPILER_REJECT_CASES=2
TIMEOUT_CASES=0
GPT_ANSWER_IMPOSITION_USED=NO
CAPABILITY_RESEARCH_RERUNS=0
