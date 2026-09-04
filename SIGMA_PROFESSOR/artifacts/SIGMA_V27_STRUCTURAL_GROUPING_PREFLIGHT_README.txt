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
c82320003b0f5b76b7a8eeb578a54a9fe720fddea2513cf698baa792a3f542d5

Runner SHA256:
e4798911cfac76f87e85d8e885e52547bd4ad4421cfe25330e90ff902661aa6b

Static:
H_CALL_ARITY_AUDIT=PASS
STR_STARTS_DEPENDENCY=NONE
DIRECT_STR_DEPENDENCY=NONE
BASH_N_RC=0

Runner failure-propagation audit: PASS (case RC preserved across diagnostic printing).
