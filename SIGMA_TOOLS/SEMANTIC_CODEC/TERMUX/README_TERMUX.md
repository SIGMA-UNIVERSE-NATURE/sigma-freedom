# SIGMA OPPO / TERMUX — Semantic Codec Application v0.1

**Role:** external supportor tool for SIGMA running inside Termux on Android/OPPO.

**Do not interpret this package as a new SIGMA compiler/runtime.** The compact `Σ.SSC@...` form is a semantic locator (`P/M` notation) backed by a Semantic Capsule/graph. Tool output remains candidate/evidence material until independently verified and promoted by authorized SIGMA logic.

## 1. Mobile layout

```text
Termux private HOME
~/.sigma/
├── vendor/
│   └── sigma-freedom-codec/       # managed Git checkout; tool source only
└── semantic_codec/                 # private mutable state
    ├── state/
    │   └── service.pid
    ├── packages/                   # optional stored SSC packages
    └── logs/
        └── service.log

Local service:
http://127.0.0.1:8765
```

The tool deliberately keeps mutable knowledge packages under Termux private app storage rather than shared `/sdcard` storage. Shared storage should be used only for explicit import/export.

## 2. Why the Termux edition is separate

The desktop service uses FastAPI/Pydantic. The Termux edition uses only Python's standard library so Android does not need to compile Python extension dependencies.

Required Termux packages:

```sh
python
git
curl
```

No `pip install` is required for the Termux service.

## 3. Install

From Termux:

```sh
pkg install -y python git curl
mkdir -p "$HOME/.sigma/bootstrap"
curl -fL \
  https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/SIGMA_LIFE/SIGMA_TOOLS/SEMANTIC_CODEC/TERMUX/install_termux.sh \
  -o "$HOME/.sigma/bootstrap/install_termux.sh"
bash "$HOME/.sigma/bootstrap/install_termux.sh"
```

The installer clones a managed copy of the `SIGMA_LIFE` branch into:

```text
$HOME/.sigma/vendor/sigma-freedom-codec
```

It **does not overwrite an existing SIGMA Termux runtime path**. If the managed vendor checkout contains local modifications, update is refused rather than overwritten.

## 4. Start / status / stop

```sh
TOOL="$HOME/.sigma/vendor/sigma-freedom-codec/SIGMA_TOOLS/SEMANTIC_CODEC/TERMUX"

bash "$TOOL/start_termux.sh"
bash "$TOOL/status_termux.sh"
bash "$TOOL/stop_termux.sh"
```

Start behavior:

1. Check `127.0.0.1:8765/v1/health` first.
2. If already healthy, return `ALREADY RUNNING` and do not create a second codec.
3. If a live PID exists but health is unavailable, refuse duplicate start.
4. Bind to loopback by default.
5. A non-loopback host is refused unless `SIGMA_CODEC_API_KEY` exists.
6. Store only its own PID; `stop_termux.sh` refuses to kill a PID whose command line is not this codec.

## 5. Web and API

Open on the OPPO phone:

```text
http://127.0.0.1:8765/
```

Health:

```sh
curl http://127.0.0.1:8765/v1/health
```

Endpoints:

```text
GET  /v1/health
POST /v1/encode
POST /v1/decode
POST /v1/verify
POST /v1/map-languages
POST /v1/roundtrip-languages
```

### Basic encode

```sh
curl -sS -X POST http://127.0.0.1:8765/v1/encode \
  -H 'Content-Type: application/json' \
  -d '{
    "text":"SIGMA giữ nghĩa, evidence và provenance.",
    "source_language":"vi",
    "preserve_exact_raw":true,
    "store":true
  }'
```

Without a supplied `semantic_graph`, the service returns `LEXICAL_FALLBACK_NOT_SEMANTIC_LOSSLESS`. This preserves RAW exactly but **does not falsely claim semantic extraction**.

## 6. Correct semantic-lossless workflow

```text
RAW
 -> preserve source/provenance
 -> extract atomic propositions
 -> FACT/EVID/INF/OP/HYP/TRAD/INTERP/DECL/UNKNOWN
 -> concept_id + sense_id
 -> preserve negation/modality/conditions/quantity/unit/time/scope
 -> relations + uncertainty + evidence + provenance
 -> SSC graph
 -> compact locator
 -> render target language
 -> clause ↔ proposition IDs
 -> re-extract
 -> normalize
 -> compare semantic signature
```

A translation passes semantic equivalence only when the re-extracted normalized signature matches the canonical graph.

Exact wording has a separate gate:

```text
RAW UTF-8 -> zlib -> base64 + SHA-256 -> decode -> SHA-256 equality
```

So:

```text
SEMANTIC_LOSSLESS != EXACT_LEXICAL_LOSSLESS
```

## 7. Twelve language IDs already supported

```text
vi  Vietnamese
en  English
fr  French
de  German
es  Spanish
pt  Portuguese
it  Italian
zh  Chinese
ja  Japanese
ko  Korean
ru  Russian
ar  Arabic
```

Never translate language A -> B -> C as the canonical learning path. Every language maps independently to/from the same SSC graph.

## 8. SIGMA integration from the same Termux process

Use the stdlib client:

```sh
python "$TOOL/sigma_termux_codec_client.py" health
python "$TOOL/sigma_termux_codec_client.py" encode --lang vi 'Nội dung cần đóng capsule'
```

Python integration:

```python
from sigma_termux_codec_client import encode, dna12_evidence

package = encode(text, "vi", semantic_graph=graph, store=True)
tool_evidence = dna12_evidence(package)
```

`dna12_evidence()` deliberately labels the result `UNVERIFIED_TOOL_OUTPUT` and `REQUIRES_INDEPENDENT_VERIFICATION`. It is designed to fit the current SIGMA discipline:

```text
SIGMA decision
 -> local Termux codec
 -> UNVERIFIED_TOOL_OUTPUT
 -> independent verification
 -> eligible/blocked
 -> authorized memory/knowledge promotion
```

## 9. External semantic model provider

The codec does **not** silently call an LLM. For real `render -> re-extract -> signature equality` tests, explicitly configure a compatible provider:

```sh
export SIGMA_SEMANTIC_MODEL_URL='https://your-authorized-provider.example/v1/sigma-semantic'
export SIGMA_SEMANTIC_MODEL_API_KEY='...'
```

Provider contract:

### Render request

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

Expected response:

```json
{
  "text": "...",
  "clause_map": [
    {"clause_id":"C1","proposition_ids":["P001"]}
  ]
}
```

### Extract request

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

## 10. Boot persistence — optional

After installing the official **Termux:Boot** add-on and launching that add-on once:

```sh
bash "$TOOL/install_boot_hook.sh"
```

This writes:

```text
~/.termux/boot/30-sigma-semantic-codec
```

The boot hook starts only this local codec. It does not create a new SIGMA runtime or another Remote Operator.

A wake lock is **not enabled by default**. If Android/ColorOS actually suspends the service and continuous availability is required, enable it explicitly for starts:

```sh
export SIGMA_TERMUX_WAKE_LOCK=1
```

This requires the appropriate Termux API command to be available. Continuous wake locks consume battery; do not enable one merely for appearance of uptime.

## 11. Security boundary

Default:

```text
HOST=127.0.0.1
PORT=8765
```

Do not expose it over Wi-Fi/LAN unless required. If exposure is explicitly needed:

```sh
export SIGMA_CODEC_API_KEY='a-long-random-secret'
export SIGMA_TERMUX_CODEC_HOST='0.0.0.0'
```

Clients must then send:

```text
X-SIGMA-API-Key: <key>
```

The service refuses a non-loopback bind without an API key.

## 12. Shared storage

`termux-setup-storage` is optional and is **not required** to run the codec. Use it only when SIGMA must import/export files through Android shared storage.

Do not make shared storage the canonical private knowledge store.

## 13. Self-test gates

```sh
python "$TOOL/termux_self_test.py"
```

Expected:

```text
PASS exact_raw_roundtrip
PASS graph_integrity
PASS multilingual_structural_coverage=12
NOTE semantic equivalence requires render->re-extract provider round-trip
```

Do not promote the final NOTE to PASS until machine evidence exists.
