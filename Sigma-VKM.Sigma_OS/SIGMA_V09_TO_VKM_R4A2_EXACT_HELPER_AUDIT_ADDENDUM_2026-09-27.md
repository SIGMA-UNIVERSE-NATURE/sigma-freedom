# SIGMA V09 -> VKM R4A2 Exact Helper Audit — Interpretation Addendum

Date: 2026-09-27
Source: user-supplied exact source bodies and binary strings.
Branch: SIGMA_LIFE
Rule: CLAIM <= EVIDENCE

## Exact source findings

### H
H(op,a,b,c) directly returns host(op,a,b,c).

This establishes that mechanically admitted host operations are invoked through the generic H wrapper.

### Current tokenizer is not donor-equivalent

api_g15_clean_text:
- lowercases;
- replaces comma, period, semicolon, colon with space;
- strips.

api_index_tokenize:
- splits the cleaned text on literal spaces;
- strips each resulting field;
- removes empty tokens.

Donor R13-R6 tokenizer is:
[A-Za-z]+(?:'[A-Za-z]+)?|\d+(?:\.\d+)?

Therefore:
CURRENT_API_INDEX_TOKENIZE_EQUIVALENT_TO_R13R6_TOKENIZER=NO

Do not substitute api_index_tokenize for the donor tokenizer.

### Current artifact SHA wrapper is not general SHA-256

api_artifact_content_key only creates explicit keys for artifact byte lengths 0 through 3.
api_artifact_sha256_digest maps a small fixed set of content keys to hardcoded SHA-256 strings and otherwise returns NULL.

Therefore:
API_ARTIFACT_SHA256_DIGEST_GENERAL_SHA256=NO
API_ARTIFACT_SHA256_DIGEST_VALID_R13R6_H64_IMPLEMENTATION=NO

Do not use this wrapper for donor h64.

## Positive binary evidence in exact pinned sigma-vkm

Observed strings:
- bytes_raw_utf8
- bytes_slice
- bytes_slice_string
- crypto_digest
- hex_encode
- list_sort
- math_exp
- math_log
- math_pow
- math_sqrt
- random_float
- str_lower
- str_slice
- str_split
- to_float

The exact VM binary also includes OpenSSL EVP digest symbols:
- EVP_DigestInit_ex
- EVP_DigestUpdate
- EVP_DigestFinal_ex
- EVP_get_digestbyname

Interpretation boundary:
binary-string presence supports primitive-name discovery but not calling signature or behavior.

## Tanh

No direct math_tanh/tanh primitive name was observed.

Possible mechanical route:
tanh(x) = (exp(2x)-1)/(exp(2x)+1)

This route is NOT admitted yet. It requires native numeric microprobes and comparison against donor math.tanh behavior over the actual operating range.

## Next

R4A3 must independently microprobe:
- bytes_raw_utf8
- hex_encode
- candidate crypto_digest signatures
- math_sqrt
- math_exp
- math_pow
- list_sort
- to_float
- string length primitives if present
- exp-derived tanh behavior

Each uncertain host call must execute in a separate sigma-vkm process.

CANONICAL_MUTATION=NO
OWNERSHIP_PROMOTION=NO
DNA15_ALLOWED=NO

NEXT=R4A3_NATIVE_MECHANICAL_MICROPROBES
