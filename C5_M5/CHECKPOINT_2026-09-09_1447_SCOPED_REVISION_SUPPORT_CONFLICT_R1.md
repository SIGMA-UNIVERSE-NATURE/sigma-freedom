# 2026-09-09 14:47 +07 — Scoped Revision Support Conflict R1

Gate: M5 TEST.

Core SHA256: `460461d6273145fcedcf20e2c75b97e718ff61a6afa8f71dc8d0812f739f850e`.
Bytecode SHA256 observed on Oppo: `e4a3e18029e93a4f97c4808fcda5518a89fa925d7c160471f83cb4635f28ee2a`.

Admission PASS, `RC=0`. Independent blind PASS, `RC=0`.

PASS facts:

- parent continual compact-memory regression;
- native revision scope derived from native relation-discrimination gap;
- native scoped support;
- native scoped conflict;
- false-conflict rejection;
- same-source duplication does not force revision;
- distinct-source conflict authority;
- evidence-driven A→B revision;
- bidirectional A→B→A revision;
- replay idempotence;
- evidence-ID conflict rejection;
- work-scope isolation;
- protocol-injection rejection;
- revision restart;
- production artifact hash freeze and `PRODUCTION_MUTATION=NO`.

Admitted exact claim:

`NATIVE_SCOPED_SUPPORT_CONFLICT_REVISION=PASS`

Claim remains narrow: conflict means evidence supporting the competing candidate inside a native two-candidate relation-discrimination scope. It does not establish broad logical contradiction or truth.

Still FAIL:

- `BROAD_SEMANTIC_SUPPORT_CONFLICT_TRUTH=FAIL`;
- `WHOLE_WORK_UNDERSTANDING=FAIL`;
- autonomous free-form summary generation;
- zero-shot low-overlap summary;
- human-value/theme induction;
- multilingual narrative transfer;
- unbounded lifelong capacity.

New blind dependency:

Probe source-consistency calibration. Current R1 counts distinct SOURCE_ID separately per candidate; a single source that supports both candidates may be counted as authority on both sides. The next diagnostic blind requires a self-contradicting source to contribute authority to neither side until explicitly resolved.
