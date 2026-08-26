# Conflict Disclosure

RELEASE_ID=SIGMA_PSI_RELEASE_CANDIDATE_20260826

Unresolved conflicts are preserved and are not silently resolved.

| Conflict | Current frozen classification | Provenance |
|---|---|---|
| IF/ELSE reporting conflict | CONFLICTED | Window A; Window G conflicted cases |
| // cross-epoch conflict | CONFLICTED | Window B; Window E; Window G |
| retained semantic conflicts | CONFLICTED group, 23 underlying conflicts | Window F; Window G |
| upstream locked reference hash variance | retained conflict | Window E / WS09 |
| upstream machine evidence snapshot variance | retained conflict | Window E / WS09 |
| TRUE/FALSE validity conformance ambiguity | retained conflict | Window E / WS09; Window F semantic conflict group |

No conflict is converted into PASS, FAIL, canonical syntax, or stable semantic meaning in Window H.
