#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-
"""SIGMA Semantic Capsule Codec — Termux stdlib service.

Supportor/external tool only.
- Compact surface is a semantic locator (P/M notation), not verified compiler grammar.
- Tool output is candidate/evidence material, never automatic verified knowledge.
- Exact lexical round-trip requires the RAW lossless sidecar.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
import sys
import urllib.request
import zlib
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, List

APP_VERSION = "0.1.0-termux"
PACKAGE_SCHEMA = "SIGMA_SEMANTIC_CAPSULE_PACKAGE_V0.1"
GRAPH_SCHEMA = "SIGMA_SEMANTIC_GRAPH_V0.1"
REFERENCE_VERSION = "SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.1_EXTENSION_20260825"

LANGUAGES = {
    "vi": "Vietnamese", "en": "English", "fr": "French", "de": "German",
    "es": "Spanish", "pt": "Portuguese", "it": "Italian", "zh": "Chinese",
    "ja": "Japanese", "ko": "Korean", "ru": "Russian", "ar": "Arabic",
}
EPISTEMIC = {"FACT", "EVID", "INF", "OP", "HYP", "TRAD", "INTERP", "DECL", "UNKNOWN"}
MODALITY = {"asserted", "possible", "probable", "required", "forbidden", "conditional", "unknown"}

API_KEY = os.environ.get("SIGMA_CODEC_API_KEY", "").strip()
MODEL_URL = os.environ.get("SIGMA_SEMANTIC_MODEL_URL", "").strip()
MODEL_KEY = os.environ.get("SIGMA_SEMANTIC_MODEL_API_KEY", "").strip()

STATE_ROOT = Path(
    os.environ.get(
        "SIGMA_TERMUX_CODEC_HOME",
        str(Path.home() / ".sigma" / "semantic_codec"),
    )
).expanduser()
PACKAGES_DIR = STATE_ROOT / "packages"
LOGS_DIR = STATE_ROOT / "logs"
STATE_DIR = STATE_ROOT / "state"


def ensure_state_dirs() -> None:
    for path in (STATE_ROOT, PACKAGES_DIR, LOGS_DIR, STATE_DIR):
        path.mkdir(parents=True, exist_ok=True)
        try:
            path.chmod(0o700)
        except OSError:
            pass


def canon(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def graph_sha(graph: Dict[str, Any]) -> str:
    return sha(canon(graph).encode("utf-8"))


def raw_pack(text: str) -> Dict[str, Any]:
    raw = text.encode("utf-8")
    compressed = zlib.compress(raw, 9)
    return {
        "codec": "zlib+base64+utf8",
        "sha256": sha(raw),
        "raw_bytes": len(raw),
        "compressed_bytes": len(compressed),
        "payload_b64": base64.b64encode(compressed).decode("ascii"),
    }


def raw_unpack(record: Dict[str, Any]) -> str:
    if record.get("codec") != "zlib+base64+utf8":
        raise ValueError("UNSUPPORTED_RAW_CODEC")
    raw = zlib.decompress(base64.b64decode(record["payload_b64"], validate=True))
    if sha(raw) != record.get("sha256"):
        raise ValueError("RAW_SHA256_MISMATCH")
    return raw.decode("utf-8")


def graph_errors(graph: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    props = graph.get("propositions") if isinstance(graph, dict) else None
    if not isinstance(props, list) or not props:
        return ["PROPOSITIONS_REQUIRED"]
    seen = set()
    for i, p in enumerate(props, 1):
        if not isinstance(p, dict):
            errors.append(f"P{i}:OBJECT_REQUIRED")
            continue
        pid = p.get("id")
        if not isinstance(pid, str) or not pid:
            errors.append(f"P{i}:ID_REQUIRED")
        elif pid in seen:
            errors.append(f"P{i}:DUPLICATE_ID:{pid}")
        else:
            seen.add(pid)
        if p.get("epistemic") not in EPISTEMIC:
            errors.append(f"{pid or i}:INVALID_EPISTEMIC")
        if "negated" not in p:
            errors.append(f"{pid or i}:NEGATED_REQUIRED")
        if p.get("modality", "asserted") not in MODALITY:
            errors.append(f"{pid or i}:INVALID_MODALITY")
        for field in ("conditions", "quantities", "provenance_refs"):
            if not isinstance(p.get(field, []), list):
                errors.append(f"{pid or i}:{field.upper()}_LIST_REQUIRED")
    return errors


def signature(graph: Dict[str, Any]) -> Dict[str, Any]:
    keep = (
        "id", "epistemic", "subject_id", "predicate_id", "object_id", "object",
        "negated", "modality", "conditions", "quantities", "scope",
    )
    props = [
        {k: p.get(k) for k in keep}
        for p in graph.get("propositions", [])
        if isinstance(p, dict)
    ]
    props.sort(key=lambda x: str(x.get("id")))
    return {
        "propositions": props,
        "relations": sorted(graph.get("relations", []), key=canon),
        "uncertainties": sorted(graph.get("uncertainties", []), key=canon),
    }


def lexical_fallback(text: str, language: str) -> Dict[str, Any]:
    return {
        "schema": GRAPH_SCHEMA,
        "graph_status": "LEXICAL_FALLBACK_NOT_SEMANTIC_LOSSLESS",
        "propositions": [{
            "id": "P0001", "epistemic": "UNKNOWN", "subject_id": None,
            "predicate_id": "RAW_TEXT_PRESENT", "object": text, "negated": False,
            "modality": "unknown", "conditions": [], "quantities": [],
            "scope": {"language": language}, "provenance_refs": ["SRC_RAW"],
        }],
        "relations": [],
        "uncertainties": ["SEMANTIC_GRAPH_NOT_SUPPLIED"],
    }


def compact_locator(graph: Dict[str, Any], provenance: List[Dict[str, Any]]) -> str:
    digest = graph_sha(graph)
    counts: Dict[str, int] = {}
    for p in graph.get("propositions", []):
        e = p.get("epistemic", "UNKNOWN")
        counts[e] = counts.get(e, 0) + 1
    epi = ",".join(f"{k}:{counts[k]}" for k in sorted(counts))
    src = ",".join(str(x.get("id") or x.get("source") or "") for x in provenance[:3]) or "UNSPECIFIED"
    return (
        f"Σ.SSC@{digest[:16]}"
        f"{{P={len(graph.get('propositions', []))};EPI={epi};SRC={src};VER={REFERENCE_VERSION}}}"
    )


def coverage(graph: Dict[str, Any], clause_map: List[Dict[str, Any]]) -> Dict[str, Any]:
    required = {
        p.get("id") for p in graph.get("propositions", [])
        if isinstance(p, dict) and p.get("id")
    }
    covered, unknown = set(), set()
    for c in clause_map:
        if not isinstance(c, dict):
            continue
        for pid in c.get("proposition_ids", []):
            (covered if pid in required else unknown).add(pid)
    missing = sorted(required - covered)
    return {
        "coverage": len(covered) / len(required) if required else 1.0,
        "missing": missing,
        "unknown_refs": sorted(unknown),
        "pass": not missing and not unknown,
    }


def provider(payload: Dict[str, Any]) -> Dict[str, Any]:
    if not MODEL_URL:
        raise RuntimeError("SIGMA_SEMANTIC_MODEL_URL_NOT_CONFIGURED")
    headers = {"Content-Type": "application/json"}
    if MODEL_KEY:
        headers["Authorization"] = f"Bearer {MODEL_KEY}"
    request = urllib.request.Request(
        MODEL_URL,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        result = json.loads(response.read().decode("utf-8"))
    if not isinstance(result, dict):
        raise RuntimeError("MODEL_RESPONSE_OBJECT_REQUIRED")
    return result


def validate_language(lang: str) -> str:
    normalized = str(lang).lower().strip()
    if normalized not in LANGUAGES:
        raise ValueError(f"UNSUPPORTED_LANGUAGE:{normalized}")
    return normalized


def encode_payload(req: Dict[str, Any]) -> Dict[str, Any]:
    text = req.get("text")
    if not isinstance(text, str) or not text:
        raise ValueError("TEXT_REQUIRED")
    lang = validate_language(req.get("source_language", "vi"))
    provenance = req.get("provenance")
    if not isinstance(provenance, list) or not provenance:
        provenance = [{
            "id": "SRC_RAW",
            "source": "CALLER_SUPPLIED_TEXT",
            "time": datetime.now(timezone.utc).isoformat(),
        }]
    graph = req.get("semantic_graph")
    mode = "CALLER_SUPPLIED"
    if graph is None:
        graph = lexical_fallback(text, lang)
        mode = "LEXICAL_FALLBACK"
    if not isinstance(graph, dict):
        raise ValueError("SEMANTIC_GRAPH_OBJECT_REQUIRED")
    graph.setdefault("schema", GRAPH_SCHEMA)
    errors = graph_errors(graph)
    if errors:
        raise ValueError("SEMANTIC_GRAPH_INVALID:" + "|".join(errors))

    preserve_exact_raw = req.get("preserve_exact_raw", True) is not False
    raw = raw_pack(text) if preserve_exact_raw else None
    surface = compact_locator(graph, provenance)
    input_bytes = len(text.encode("utf-8"))
    surface_bytes = len(surface.encode("utf-8"))
    package = {
        "schema": PACKAGE_SCHEMA,
        "package_id": f"SSC-{graph_sha(graph)[:20]}",
        "reference": {
            "version": REFERENCE_VERSION,
            "notation_status": "P/M_SUPPORTOR_NOT_MACHINE_GRAMMAR",
            "claim_rule": "CLAIM<=EVIDENCE",
        },
        "source": {"language": lang, "raw": raw},
        "semantic": {
            "mode": mode,
            "graph": graph,
            "graph_sha256": graph_sha(graph),
            "semantic_lossless_claim_allowed": mode == "CALLER_SUPPLIED",
        },
        "compact": {"surface": surface, "role": "SEMANTIC_LOCATOR"},
        "provenance": provenance,
        "metrics": {
            "input_utf8_bytes": input_bytes,
            "surface_utf8_bytes": surface_bytes,
            "surface_reduction_pct": round((1 - surface_bytes / input_bytes) * 100, 2) if input_bytes else 0.0,
            "note": "Surface reduction is not total storage compression.",
        },
    }
    if req.get("store") is True:
        ensure_state_dirs()
        output = PACKAGES_DIR / f"{package['package_id']}.json"
        output.write_text(json.dumps(package, ensure_ascii=False, indent=2), encoding="utf-8")
        try:
            output.chmod(0o600)
        except OSError:
            pass
        package["stored_at"] = str(output)
    return package


def decode_payload(req: Dict[str, Any]) -> Dict[str, Any]:
    package = req.get("package")
    if not isinstance(package, dict) or package.get("schema") != PACKAGE_SCHEMA:
        raise ValueError("PACKAGE_SCHEMA_MISMATCH")
    mode = req.get("mode", "exact")
    if mode == "exact":
        raw = package.get("source", {}).get("raw")
        if not raw:
            raise ValueError("RAW_SIDECAR_REQUIRED")
        text = raw_unpack(raw)
        return {"mode": "exact", "text": text, "sha256": sha(text.encode("utf-8")), "exact_roundtrip_verified": True}
    if mode == "semantic":
        graph = package.get("semantic", {}).get("graph")
        if not isinstance(graph, dict):
            raise ValueError("GRAPH_MISSING")
        return {"mode": "semantic", "graph": graph, "signature": signature(graph), "note": "Natural-language rendering is separate from semantic expansion."}
    raise ValueError("MODE_MUST_BE_EXACT_OR_SEMANTIC")


def verify_payload(req: Dict[str, Any]) -> Dict[str, Any]:
    package = req.get("package")
    failures: List[str] = []
    if not isinstance(package, dict) or package.get("schema") != PACKAGE_SCHEMA:
        return {"pass": False, "failures": ["PACKAGE_SCHEMA_MISMATCH"], "exact_raw_roundtrip": None, "semantic_equivalence_verified": False}
    graph = package.get("semantic", {}).get("graph")
    if not isinstance(graph, dict):
        failures.append("GRAPH_MISSING")
    else:
        failures.extend(graph_errors(graph))
        if graph_sha(graph) != package.get("semantic", {}).get("graph_sha256"):
            failures.append("GRAPH_SHA256_MISMATCH")
    exact = None
    raw = package.get("source", {}).get("raw")
    if raw:
        try:
            raw_unpack(raw)
            exact = True
        except Exception as exc:
            exact = False
            failures.append(f"RAW_VERIFY_FAILED:{exc}")
    return {
        "pass": not failures,
        "failures": failures,
        "exact_raw_roundtrip": exact,
        "semantic_equivalence_verified": False,
        "note": "Graph integrity alone does not prove linguistic equivalence.",
    }


def map_languages_payload(req: Dict[str, Any]) -> Dict[str, Any]:
    package = req.get("package")
    graph = package.get("semantic", {}).get("graph") if isinstance(package, dict) else None
    if not isinstance(graph, dict):
        raise ValueError("GRAPH_MISSING")
    views = req.get("views")
    if not isinstance(views, list):
        raise ValueError("VIEWS_LIST_REQUIRED")
    results = []
    for view in views:
        if not isinstance(view, dict):
            results.append({"pass": False, "error": "VIEW_OBJECT_REQUIRED"})
            continue
        try:
            lang = validate_language(view.get("language", ""))
        except Exception as exc:
            results.append({"language": view.get("language"), "pass": False, "error": str(exc)})
            continue
        text = view.get("text")
        clause_map = view.get("clause_map", [])
        if not isinstance(text, str) or not isinstance(clause_map, list):
            results.append({"language": lang, "pass": False, "error": "TEXT_AND_CLAUSE_MAP_REQUIRED"})
            continue
        check = coverage(graph, clause_map)
        results.append({"language": lang, "text_sha256": sha(text.encode("utf-8")), "coverage": check, "pass": check["pass"], "semantic_equivalence_verified": False})
    return {"target_language_count": len(results), "all_structural_coverage_pass": bool(results) and all(x.get("pass") for x in results), "results": results}


def roundtrip_languages_payload(req: Dict[str, Any]) -> Dict[str, Any]:
    package = req.get("package")
    graph = package.get("semantic", {}).get("graph") if isinstance(package, dict) else None
    if not isinstance(graph, dict):
        raise ValueError("GRAPH_MISSING")
    targets = req.get("target_languages")
    if not isinstance(targets, list) or not targets:
        raise ValueError("TARGET_LANGUAGES_REQUIRED")
    if not MODEL_URL:
        return {"all_roundtrip_pass": False, "error": "SEMANTIC_MODEL_PROVIDER_NOT_CONFIGURED", "required_env": "SIGMA_SEMANTIC_MODEL_URL", "results": []}
    canonical = signature(graph)
    results = []
    for raw_lang in targets:
        try:
            lang = validate_language(raw_lang)
            rendered = provider({
                "operation": "render",
                "language": lang,
                "semantic_graph": graph,
                "constraints": {"preserve_proposition_ids": True, "return_clause_map": True},
            })
            text = rendered["text"]
            clause_map = rendered.get("clause_map", [])
            check = coverage(graph, clause_map)
            extracted = provider({
                "operation": "extract",
                "language": lang,
                "text": text,
                "schema": GRAPH_SCHEMA,
                "constraints": {"do_not_invent_claims": True},
            })
            new_graph = extracted["semantic_graph"]
            new_graph.setdefault("schema", GRAPH_SCHEMA)
            semantic_equal = not graph_errors(new_graph) and signature(new_graph) == canonical
            results.append({"language": lang, "rendered_text": text, "coverage": check, "semantic_equivalence_verified": semantic_equal, "pass": check["pass"] and semantic_equal})
        except Exception as exc:
            results.append({"language": str(raw_lang), "pass": False, "error": str(exc)})
    return {"all_roundtrip_pass": bool(results) and all(x.get("pass") for x in results), "results": results}


def health_payload() -> Dict[str, Any]:
    ensure_state_dirs()
    return {
        "ok": True,
        "version": APP_VERSION,
        "platform": "TERMUX_STDLIB",
        "languages": LANGUAGES,
        "model_configured": bool(MODEL_URL),
        "api_key_required": bool(API_KEY),
        "state_root": str(STATE_ROOT),
        "claim_rule": "CLAIM<=EVIDENCE",
    }


WEB_UI = """<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>SIGMA Semantic Codec — Termux</title><style>body{font-family:system-ui,sans-serif;max-width:900px;margin:32px auto;padding:0 16px;line-height:1.45}textarea{width:100%;min-height:180px}button{padding:10px 16px}pre{white-space:pre-wrap;word-break:break-word;background:#f3f3f3;padding:12px;border-radius:8px}</style></head><body><h1>SIGMA Semantic Codec — Termux</h1><p>Local-only supportor tool. Compact surface is a semantic locator, not verified SIGMA compiler grammar.</p><textarea id='text' placeholder='Paste text here'></textarea><br><button onclick='run()'>Encode RAW-safe package</button><pre id='out'>Ready.</pre><script>async function run(){const text=document.getElementById('text').value;const r=await fetch('/v1/encode',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({text,source_language:'vi',preserve_exact_raw:true})});document.getElementById('out').textContent=JSON.stringify(await r.json(),null,2);}</script></body></html>"""


class Handler(BaseHTTPRequestHandler):
    server_version = "SIGMA-Termux-Codec/0.1"

    def log_message(self, fmt: str, *args: Any) -> None:
        sys.stderr.write(f"{datetime.now(timezone.utc).isoformat()} " + (fmt % args) + "\n")

    def _json(self, status: int, payload: Dict[str, Any]) -> None:
        raw = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def _auth_ok(self) -> bool:
        if not API_KEY:
            return True
        supplied = self.headers.get("X-SIGMA-API-Key", "")
        return bool(supplied) and hmac.compare_digest(supplied, API_KEY)

    def _read_json(self) -> Dict[str, Any]:
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            raise ValueError("INVALID_CONTENT_LENGTH")
        if length <= 0 or length > 10 * 1024 * 1024:
            raise ValueError("BODY_SIZE_INVALID")
        obj = json.loads(self.rfile.read(length).decode("utf-8"))
        if not isinstance(obj, dict):
            raise ValueError("JSON_OBJECT_REQUIRED")
        return obj

    def do_GET(self) -> None:
        if self.path == "/v1/health":
            self._json(200, health_payload())
            return
        if self.path in ("/", "/index.html"):
            raw = WEB_UI.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(raw)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(raw)
            return
        self._json(404, {"error": "NOT_FOUND"})

    def do_POST(self) -> None:
        if not self._auth_ok():
            self._json(401, {"error": "INVALID_SIGMA_CODEC_API_KEY"})
            return
        handlers = {
            "/v1/encode": encode_payload,
            "/v1/decode": decode_payload,
            "/v1/verify": verify_payload,
            "/v1/map-languages": map_languages_payload,
            "/v1/roundtrip-languages": roundtrip_languages_payload,
        }
        func = handlers.get(self.path)
        if func is None:
            self._json(404, {"error": "NOT_FOUND"})
            return
        try:
            self._json(200, func(self._read_json()))
        except (ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
            self._json(422, {"error": str(exc)})
        except Exception as exc:
            self._json(500, {"error": "INTERNAL_ERROR", "detail": str(exc)})


def main() -> None:
    parser = argparse.ArgumentParser(description="SIGMA Semantic Codec for Termux")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if args.host not in {"127.0.0.1", "::1", "localhost"} and not API_KEY:
        raise SystemExit("REFUSING_NON_LOOPBACK_WITHOUT_SIGMA_CODEC_API_KEY")
    ensure_state_dirs()
    httpd = ThreadingHTTPServer((args.host, args.port), Handler)
    print(json.dumps({"status": "STARTING", "host": args.host, "port": args.port, "state_root": str(STATE_ROOT), "api_key_required": bool(API_KEY)}, ensure_ascii=False), flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
