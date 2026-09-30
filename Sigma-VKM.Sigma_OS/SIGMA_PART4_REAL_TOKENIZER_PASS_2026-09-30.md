# SIGMA PART4 — Real Tokenizer PASS

Date: 2026-09-30
Source: user-supplied Oppo/Termux runtime output.

## Candidate VKM

TOKENIZER_FILESYSTEM_SIDE_EFFECT=NONE

P4_VKM_CANDIDATE_SHA256=
6ec6d5a71289045d9120608bd052f63ca48c68e8f3bdc1fbd2076734d382d9c3

PART3_TENSOR_CAPABILITY_PRESERVED=YES

PART4_TOKENIZER_CAPABILITY_PRESENT=YES

SELF_CERTIFICATE_IN_53=NONE

## Incremental Sigma source / compile

SOURCE=
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/SIGMA_INTEGRAL_OWNER_CORE_R3_MAX_MERGE_R1_FIX1/native/SIGMA_INTEGRAL_INCREMENTAL.sigma

P4_BYTECODE_SHA256=
fc80a4f63a49be458602054727e64d61b472d327acbca2b6f1745f5cd25d3dfa

P4_DETERMINISTIC_COMPILE=YES

## Observed tokenizer behavior

OBSERVED_VOCAB_LIMIT=131072

OBSERVED_ENCODE=
300,301,300

OBSERVED_BYTE_FALLBACK=
65,90

OBSERVED_ROUNDTRIP=
hello worldhello

PART4_TRANSACTION=COMMITTED

PART4_EXTERNAL_VERIFY=PASS

TOKENIZER_VOCAB_CAPACITY=131072

BYTE_FALLBACK_0_255=IMPLEMENTED

SPARSE_TRIE_LONGEST_MATCH=IMPLEMENTED

TOKENIZER_ROUNDTRIP=VERIFIED

TOKENIZER_LANGUAGE_SPECIFIC_POLICY=NO

## Persistence / filesystem boundary

TOKENIZER_FILESYSTEM_PERSISTENCE=NO

TOKEN_FILE_PER_TOKEN=NO

UNBOUNDED_DUPLICATE_FILE_CREATION=NO

TOKENIZER_FILESYSTEM_SIDE_EFFECT=NONE

## Authority boundary

SELF_CERTIFICATE_USED=NO

HOST_LEARNING=NO

HOST_SEMANTIC_SELECTION=NO

PART4_EXECUTION_UNDER_10M=PASS

## Canonical / admission boundary

LIVE_SIGMA_VKM_REPLACED=NO

CANONICAL_MUTATION=NO

ONE_SIGMA=YES

ADMISSION=NO

## Interpretation boundary

This checkpoint establishes the supplied PART4 tokenizer candidate/verifier result only.

It supports:
- tokenizer capability is present in the candidate;
- Part3 tensor capability is preserved;
- deterministic compile passes;
- vocab capacity is 131072;
- byte fallback for 0..255 is implemented;
- sparse-trie longest-match behavior is implemented;
- tokenizer roundtrip is externally verified;
- tokenizer behavior does not claim a language-specific policy;
- no tokenizer filesystem persistence or file-per-token design is used;
- no unbounded duplicate-file creation is reported;
- no self-certificate is used;
- host does not perform learning or semantic selection.

It does NOT establish:
- replacement of the live sigma-vkm executable;
- canonical mutation;
- production admission.

LIVE_SIGMA_VKM_REPLACED=NO
CANONICAL_MUTATION=NO
ADMISSION=NO
