# V5-K3 arXiv Adapter — HOLD correction: xmllint is in libxml2-utils

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## New machine evidence

The user attempted the previously suggested package install:

```text
libxml2 is already the newest version (2.15.3).
Upgrading: 0, Installing: 0, Removing: 0, Not Upgrading: 0
```

But the runner had already reported:

```text
HOLD=XMLLINT_MISSING_MECHANICAL_DECODE_TOOL
```

## Correction

The prior HOLD checkpoint correctly classified the event as a missing mechanical XML decode tool, but its package-install instruction was incomplete for the current Termux packaging layout.

Current Termux package evidence shows `xmllint` is provided by the separate package:

```text
libxml2-utils
```

rather than the base `libxml2` package.

Therefore:

```text
V5K3_NATIVE_SOURCE_REPAIR_REQUIRED=NO
V5K3_RUNNER_REPAIR_REQUIRED=NO
MECHANICAL_DEPENDENCY_CORRECTION=INSTALL_LIBXML2_UTILS
```

## Correct next action

```bash
pkg install libxml2-utils
command -v xmllint
xmllint --version
```

Then rerun the exact unchanged runner:

```bash
bash run_SIGMA_V5K3_NATIVE_ADMISSION_V1.sh | tee V5K3_NATIVE_ADMISSION_V1.out
```

## Admission state remains unchanged

```text
V5K3_RUNTIME_ADMISSION=NOT_RUN
V5K3_COMPILE=NOT_REACHED_IN_THE_HOLD_RUN
LIVE_ARXIV_RUNTIME=NOT_EXECUTED_IN_THE_HOLD_RUN
ARXIV_ADAPTER_TESTED_SCOPE=NOT_PROVEN
V5K4_PUBMED_ADAPTER_UNLOCKED=NO
```

## Canonical V5-K3 identities

```text
BUNDLE_SHA256=9849b2377ed1f6d711b39254270c0a722d96a2e1109b8761580b6b5170de376b
SOURCE_SHA256=d3ecd3c2683bdf88cc95ef83ec643235251cb2fbaa0d17bc8d8fb1f70c3c750b
RUNNER_SHA256=82e3a543d16995c84b3cf1f17bc70c9964906b8ba2c9859f04d60b49962c794b
```

## Boundaries preserved

```text
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
HOST_HTTP_ROLE=MECHANICAL_EXACT_REQUEST_TRANSPORT_ONLY
HOST_XML_DECODE_ROLE=MECHANICAL_EXACT_PROTOCOL_DECODE_ONLY
RESEARCH_GOAL_SELECTION=NOT_EXECUTED
CONTENT_TRUTH_DECISION=NOT_EXECUTED
KNOWLEDGE_PROMOTION=NOT_EXECUTED
SEMANTIC_UNDERSTANDING=NOT_PROVEN
PRODUCTION_BINDING=NO
```
