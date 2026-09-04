SIGMA V2.5A.2 DOCUMENT SURVEY PREFLIGHT

Repair from V2.5A.1:
- Removed all direct str(value) calls because the locked VM returned:
  VM_RC=8
  SIGMA C VM: undefined function str
- Numeric survey metrics remain native integers and are printed directly.
- Persistent survey record now stores only textual fields that require no host or bridge stringification:
  DOC=<sha> || SURVEY_STATUS=COMPLETE || BEST_LOCAL_RELATION=<relation>
- No survey-selection policy change.
- No production learner namespace mutation.
- H-call arity audit: PASS.
- Direct str(...) dependency audit: PASS (none remain).

Source SHA256:
153431aa3f78e282ddf0b2ddd73be993440abd9ce4118d4e717aa5ce83f14eb8

Runner SHA256:
c3bbed189661275fda1eb5394965c87b605108a0a316aa1466a7fe3c782ecca5

HOST_LEARNING=NO
HOST_DOCUMENT_SELECTION=NO
SEMANTIC_UNDERSTANDING=NOT_PROVEN
