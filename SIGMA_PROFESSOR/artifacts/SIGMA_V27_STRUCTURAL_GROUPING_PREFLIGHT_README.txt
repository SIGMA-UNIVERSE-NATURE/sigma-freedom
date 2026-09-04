SIGMA V2.7 STRUCTURAL GROUPING PREFLIGHT

Goal:
Prove native structural grouping using exact shared structural anchors across distinct document-anchor pairs.

Same bytecode is tested on:
1. positive input with two shared-anchor groups;
2. negative input with no shared anchors across distinct documents;
3. exact positive replay.

Important anti-inflation test:
The same DOC=A / anchor pair is duplicated in both positive and negative fixtures.
SIGMA must deduplicate exact document-anchor pairs before computing cross-document anchor support.
A duplicate within the same document must not create a group.

Expected positive:
- multi-member groups = 2
- grouped documents = 4
- singletons = 1
- duplicate profiles ignored = 1

Expected negative:
- multi-member groups = 0
- grouped documents = 0
- singletons = 5
- duplicate profiles ignored = 1

Persistence:
SIGMA writes group assignments itself to:
.sigma_exec/SIGMA_V27T_GROUP_ASSIGNMENTS.memory

Host:
- supplies QA input bytes;
- invokes compiler/VM;
- mechanically checks protocol counts/hashes;
- does NOT choose groups or classify topics.

Claim:
STRUCTURAL grouping only.
No semantic grouping, topic understanding, or semantic understanding is claimed.

Source SHA256:
ab6eb3bf5e8796f2ec4b772159d70c648458fd85895f59f521407ab4209d6419

Runner SHA256:
420ae29866f39cc087cc95f28b8c1099785d0faf7af51c88727ef3b0bcc325fd

Static:
H_CALL_ARITY_AUDIT=PASS
STR_STARTS_DEPENDENCY=NONE
DIRECT_STR_DEPENDENCY=NONE
NATIVE_NOT_EQUAL_DEPENDENCY=NONE
BASH_N_RC=0

Runner failure-propagation audit: PASS (case RC preserved across diagnostic printing).
