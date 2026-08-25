# SIGMA Semantic Capsule Codec v0.1

**Status:** supportor tool / experimental interface.  
**Reference:** `SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.1_EXTENSION_20260825`, inheriting v1.0 provenance.  
**Boundary:** this tool does **not** define executable SIGMA grammar and does not promote its own output to verified knowledge.

## 1. Purpose

The 10-domain experiment showed that SIGMA can use a very short surface while keeping much deeper meaning behind it, but removed information must still exist in a semantic graph or exact sidecar.

The tool therefore separates:

1. **Compact surface** — short semantic locator.
2. **SSC semantic graph** — language-neutral propositions, relations, status, uncertainty, evidence and provenance.
3. **RAW lossless sidecar** — compressed original UTF-8 text plus SHA-256, used when exact wording must be restored.

Core rules:

```text
SHORT_SURFACE != SMALL_TOTAL_STORAGE
SEMANTIC_LOSSLESS != LEXICAL_EXACT
HASH = VERIFICATION, NOT RECONSTRUCTION
COMPACT_TOKEN = LOCATOR, NOT RUNTIME_CAPABILITY_PROOF
```

## 2. Method used for the ten examples

```text
READ
 -> identify atomic propositions
 -> classify epistemic status
 -> preserve negation / modality / quantities / conditions / scope
 -> attach evidence + provenance
 -> assign stable concept/proposition IDs
 -> build relations
 -> generate compact SIGMA locator
 -> reconstruct graph
 -> verify proposition-by-proposition
 -> retain RAW sidecar for exact lexical round-trip
```

The ten compact examples are in `examples_10_domains.json` and cover medicine, climate science, distributed systems, macroeconomics, contract law, evolution, cybersecurity, power grids, exoplanets, and soil science.

## 3. What “no loss of meaning” requires

A semantic round trip is eligible to pass only if all relevant fields survive:

- proposition identity;
- concept/sense identity;
- negation;
- modality;
- quantities and units;
- conditions;
- temporal/causal relations;
- scope/jurisdiction/domain;
- epistemic type: `FACT/EVID/INF/OP/HYP/TRAD/INTERP/DECL/UNKNOWN`;
- uncertainty;
- evidence references;
- provenance;
- contradiction/revision links where applicable.

Different sentences can express the same graph, so semantic equivalence does not imply the original wording can be recovered. Exact original wording requires:

```text
RAW_REF + LOSSLESS_CODEC + HASH
```

## 4. Language-neutral mapping

The canonical identity layer should be IDs, not Vietnamese, English, Chinese or any other natural language.

Example proposition:

```json
{
  "id": "P0001",
  "epistemic": "FACT",
  "subject_id": "CLIMATE.GHG",
  "predicate_id": "CAUSES",
  "object_id": "CLIMATE.ENERGY_IMBALANCE",
  "negated": false,
  "modality": "asserted",
  "conditions": [],
  "quantities": [],
  "scope": {"domain": "climate"},
  "provenance_refs": ["SRC001"]
}
```

Natural-language text is a rendering around these stable IDs:

```text
LANGUAGE_A_TEXT
 -> proposition IDs / concept IDs
 -> CANONICAL SSC GRAPH
 -> proposition IDs / concept IDs
 -> LANGUAGE_B_TEXT
```

## 5. Twelve-language demonstration

`multilingual_mapping_demo.json` includes:

`vi, en, fr, de, es, pt, it, zh, ja, ko, ru, ar`

That is Vietnamese, English, French, German, Spanish, Portuguese, Italian, Chinese, Japanese, Korean, Russian and Arabic.

Verification has two gates:

### Gate A — structural coverage

Every required proposition ID must be referenced by target-language clauses, and no unknown proposition may be introduced.

### Gate B — semantic round-trip

Re-extract the target-language text back to an SSC graph and compare the normalized semantic signature:

```text
subject_id
predicate_id
object_id / normalized object
negated
modality
conditions
quantities
scope
relations
uncertainty
```

Only Gate B supports a strong semantic-equivalence claim. Word overlap or translation confidence alone is not enough.

## 6. Files

```text
SIGMA_TOOLS/SEMANTIC_CODEC/
├── README.md
├── requirements.txt
├── sigma_semantic_codec_service.py
├── self_test.py
├── examples_10_domains.json
└── multilingual_mapping_demo.json
```

Recommended HP installation target:

```text
E:\SIGMA\TOOLS\SEMANTIC_CODEC
```

Keep it outside `RUNTIME\CORE54\GENES` and outside Canon until separately verified and explicitly integrated.

## 7. Install and run on HP

PowerShell:

```powershell
cd E:\SIGMA\TOOLS\SEMANTIC_CODEC
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python self_test.py
python sigma_semantic_codec_service.py --host 127.0.0.1 --port 8765
```

Web UI:

```text
http://127.0.0.1:8765/
```

OpenAPI/Swagger:

```text
http://127.0.0.1:8765/docs
```

Health:

```text
GET http://127.0.0.1:8765/v1/health
```

FastAPI publishes the API schema and interactive documentation automatically.

## 8. API

### `POST /v1/encode`

```json
{
  "text": "source text",
  "source_language": "vi",
  "semantic_graph": {},
  "provenance": [{"id":"SRC001","url":"https://example.org/source"}],
  "preserve_exact_raw": true
}
```

If `semantic_graph` is omitted, the tool creates a lexical fallback and explicitly marks it as **not semantic-lossless**. It still retains the RAW sidecar for exact recovery.

### `POST /v1/decode`

- `mode="exact"`: restore RAW and verify SHA-256.
- `mode="semantic"`: expand to the language-neutral graph/signature.

### `POST /v1/verify`

Checks package schema, graph structure/hash and RAW exact round-trip. It intentionally does not claim linguistic equivalence from structure alone.

### `POST /v1/map-languages`

Checks clause-to-proposition structural coverage for supplied natural-language views.

### `POST /v1/roundtrip-languages`

When a semantic model/provider is configured, the codec performs:

```text
CANONICAL_GRAPH
 -> RENDER(target language)
 -> CLAUSE/P-ID COVERAGE
 -> RE-EXTRACT(target language)
 -> GRAPH SIGNATURE COMPARISON
```

## 9. Connect to a semantic model/provider

Set an authorized provider endpoint:

```powershell
$env:SIGMA_SEMANTIC_MODEL_URL = "http://127.0.0.1:9000/semantic"
# optional
$env:SIGMA_SEMANTIC_MODEL_API_KEY = "provider-secret"
```

The provider contract is intentionally vendor-neutral.

Render request:

```json
{
  "operation": "render",
  "language": "ja",
  "semantic_graph": {},
  "constraints": {
    "preserve_proposition_ids": true,
    "return_clause_map": true
  }
}
```

Expected render response:

```json
{
  "text": "...",
  "clause_map": [{"clause":1,"proposition_ids":["P0001"]}]
}
```

Extraction request:

```json
{
  "operation": "extract",
  "language": "ja",
  "text": "...",
  "schema": "SIGMA_SEMANTIC_GRAPH_V0.1",
  "constraints": {"do_not_invent_claims": true}
}
```

Expected response:

```json
{"semantic_graph": {}}
```

SIGMA's own authorized model service can implement this contract, or another model endpoint can be used. The codec itself remains deterministic and auditable.

## 10. Connect SIGMA/Core54 to the tool

Use the codec as an **external evidence-producing tool**, not as a new gene.

Recommended flow:

```text
SIGMA task/source
 -> DNA-12 decides tool use is required
 -> HTTP POST /v1/encode
 -> codec output remains UNVERIFIED_TOOL_OUTPUT
 -> independent verifier checks source + graph + round-trip
 -> DNA-09 eligibility gate
 -> DNA-10/DNA-11 memory/knowledge path only if verified + authorized
```

This preserves the existing separation between learner, verifier, tool output and promoted knowledge.

Minimal Python client:

```python
import json
import urllib.request

payload = {
    "text": source_text,
    "source_language": "vi",
    "semantic_graph": semantic_graph,
    "provenance": provenance,
    "preserve_exact_raw": True,
}

req = urllib.request.Request(
    "http://127.0.0.1:8765/v1/encode",
    data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)

with urllib.request.urlopen(req, timeout=60) as response:
    package = json.loads(response.read().decode("utf-8"))
```

## 11. Existing HP bridge

Do not create another Remote Operator. The codec sits behind the existing control path:

```text
C:\SIGMA_REMOTE_OPERATOR
        |
        | existing control bridge
        v
http://127.0.0.1:8765
        |
        v
E:\SIGMA\TOOLS\SEMANTIC_CODEC
        |
        +--> SSC/evidence package
        +--> independent verifier
        +--> authorized knowledge path
```

Nothing in this package needs to rebuild, reinstall or duplicate the Remote Operator.

## 12. Local-first security

Default: bind only to `127.0.0.1`.

If LAN access is necessary, set an API key first:

```powershell
$env:SIGMA_CODEC_API_KEY = "long-random-secret"
python sigma_semantic_codec_service.py --host 0.0.0.0 --port 8765
```

The service refuses a non-loopback bind without `SIGMA_CODEC_API_KEY`. Restrict Windows Firewall scope. Do not port-forward the service directly to the public Internet.

If a public frontend is later built, use an authenticated HTTPS server-side gateway/BFF. Never embed the semantic API key in public browser JavaScript.

## 13. Acceptance gates

```text
EXACT_LOSSLESS_PASS:
RAW_DECODE_SHA256 == RAW_SOURCE_SHA256

STRUCTURAL_LANGUAGE_PASS:
required_proposition_ids == covered_proposition_ids
AND unknown_proposition_refs == ∅

SEMANTIC_EQUIVALENCE_PASS:
RENDER -> REEXTRACT -> NORMALIZED_GRAPH_SIGNATURE == CANONICAL_GRAPH_SIGNATURE
```

None of these automatically promotes knowledge. Promotion remains a separate verification/authorization decision.

## 14. Intentional non-claims

- No invented SIGMA compiler/VM grammar.
- Sentence splitting is not called understanding.
- No automatic knowledge promotion.
- No Canon overwrite.
- No second Remote Operator/watchdog/guardian.
- No public exposure by default.
- A shorter surface is not claimed to mean equally smaller total storage.

The goal is an auditable bridge from natural-language documents to SSC packages while preserving the v1.0/v1.1 evidence and provenance discipline.
