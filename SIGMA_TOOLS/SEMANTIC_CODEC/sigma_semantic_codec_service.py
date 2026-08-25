#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SIGMA Semantic Capsule Codec v0.1.

Supportor tool only. The compact surface is a semantic locator (P/M notation),
not machine-verified SIGMA compiler grammar. Tool output is evidence/candidate
material, never automatic verified knowledge.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import secrets
import urllib.request
import zlib
from datetime import datetime, timezone
from typing import Any, Dict, List, Literal, Optional

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

APP_VERSION = "0.1.0"
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
            errors.append(f"P{i}:OBJECT_REQUIRED"); continue
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
    keep = ("id", "epistemic", "subject_id", "predicate_id", "object_id", "object", "negated", "modality", "conditions", "quantities", "scope")
    props = [{k: p.get(k) for k in keep} for p in graph.get("propositions", []) if isinstance(p, dict)]
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
    return f"Σ.SSC@{digest[:16]}{{P={len(graph.get('propositions', []))};EPI={epi};SRC={src};VER={REFERENCE_VERSION}}}"


def coverage(graph: Dict[str, Any], clause_map: List[Dict[str, Any]]) -> Dict[str, Any]:
    required = {p.get("id") for p in graph.get("propositions", []) if p.get("id")}
    covered, unknown = set(), set()
    for c in clause_map:
        for pid in c.get("proposition_ids", []) if isinstance(c, dict) else []:
            (covered if pid in required else unknown).add(pid)
    missing = sorted(required - covered)
    return {
        "coverage": len(covered) / len(required) if required else 1.0,
        "missing": missing, "unknown_refs": sorted(unknown),
        "pass": not missing and not unknown,
    }


def provider(payload: Dict[str, Any]) -> Dict[str, Any]:
    if not MODEL_URL:
        raise RuntimeError("SIGMA_SEMANTIC_MODEL_URL_NOT_CONFIGURED")
    headers = {"Content-Type": "application/json"}
    if MODEL_KEY:
        headers["Authorization"] = f"Bearer {MODEL_KEY}"
    req = urllib.request.Request(MODEL_URL, data=json.dumps(payload, ensure_ascii=False).encode("utf-8"), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=90) as response:
        result = json.loads(response.read().decode("utf-8"))
    if not isinstance(result, dict):
        raise RuntimeError("MODEL_RESPONSE_OBJECT_REQUIRED")
    return result


class EncodeRequest(BaseModel):
    text: str = Field(min_length=1)
    source_language: str = "vi"
    semantic_graph: Optional[Dict[str, Any]] = None
    provenance: List[Dict[str, Any]] = Field(default_factory=list)
    preserve_exact_raw: bool = True


class PackageRequest(BaseModel):
    package: Dict[str, Any]


class DecodeRequest(PackageRequest):
    mode: Literal["exact", "semantic"] = "exact"


class LanguageView(BaseModel):
    language: str
    text: str
    clause_map: List[Dict[str, Any]] = Field(default_factory=list)


class MapRequest(PackageRequest):
    views: List[LanguageView]


class RoundTripRequest(PackageRequest):
    target_languages: List[str]


def auth(x_sigma_api_key: Optional[str] = Header(default=None)) -> None:
    if API_KEY and (not x_sigma_api_key or not secrets.compare_digest(x_sigma_api_key, API_KEY)):
        raise HTTPException(401, "INVALID_SIGMA_CODEC_API_KEY")


app = FastAPI(title="SIGMA Semantic Capsule Codec", version=APP_VERSION)


@app.get("/v1/health")
def health() -> Dict[str, Any]:
    return {"ok": True, "version": APP_VERSION, "languages": LANGUAGES, "model_configured": bool(MODEL_URL), "api_key_required": bool(API_KEY)}


@app.post("/v1/encode", dependencies=[Depends(auth)])
def encode(req: EncodeRequest) -> Dict[str, Any]:
    lang = req.source_language.lower().strip()
    if lang not in LANGUAGES:
        raise HTTPException(400, {"error": "UNSUPPORTED_LANGUAGE", "supported": LANGUAGES})
    provenance = req.provenance or [{"id": "SRC_RAW", "source": "CALLER_SUPPLIED_TEXT", "time": datetime.now(timezone.utc).isoformat()}]
    mode = "CALLER_SUPPLIED"
    graph = req.semantic_graph
    if graph is None:
        graph = lexical_fallback(req.text, lang); mode = "LEXICAL_FALLBACK"
    graph.setdefault("schema", GRAPH_SCHEMA)
    errors = graph_errors(graph)
    if errors:
        raise HTTPException(422, {"error": "SEMANTIC_GRAPH_INVALID", "issues": errors})
    raw = raw_pack(req.text) if req.preserve_exact_raw else None
    surface = compact_locator(graph, provenance)
    input_bytes = len(req.text.encode("utf-8")); surface_bytes = len(surface.encode("utf-8"))
    return {
        "schema": PACKAGE_SCHEMA,
        "package_id": f"SSC-{graph_sha(graph)[:20]}",
        "reference": {"version": REFERENCE_VERSION, "notation_status": "P/M_SUPPORTOR_NOT_MACHINE_GRAMMAR", "claim_rule": "CLAIM<=EVIDENCE"},
        "source": {"language": lang, "raw": raw},
        "semantic": {"mode": mode, "graph": graph, "graph_sha256": graph_sha(graph), "semantic_lossless_claim_allowed": mode == "CALLER_SUPPLIED"},
        "compact": {"surface": surface, "role": "SEMANTIC_LOCATOR"},
        "provenance": provenance,
        "metrics": {"input_utf8_bytes": input_bytes, "surface_utf8_bytes": surface_bytes, "surface_reduction_pct": round((1-surface_bytes/input_bytes)*100, 2) if input_bytes else 0.0, "note": "Surface reduction is not total storage compression."},
    }


@app.post("/v1/decode", dependencies=[Depends(auth)])
def decode(req: DecodeRequest) -> Dict[str, Any]:
    if req.package.get("schema") != PACKAGE_SCHEMA:
        raise HTTPException(422, "PACKAGE_SCHEMA_MISMATCH")
    if req.mode == "exact":
        raw = req.package.get("source", {}).get("raw")
        if not raw:
            raise HTTPException(422, "RAW_SIDECAR_REQUIRED")
        text = raw_unpack(raw)
        return {"mode": "exact", "text": text, "sha256": sha(text.encode("utf-8")), "exact_roundtrip_verified": True}
    graph = req.package.get("semantic", {}).get("graph")
    return {"mode": "semantic", "graph": graph, "signature": signature(graph), "note": "Natural-language rendering is separate from semantic expansion."}


@app.post("/v1/verify", dependencies=[Depends(auth)])
def verify(req: PackageRequest) -> Dict[str, Any]:
    package = req.package; failures = []
    if package.get("schema") != PACKAGE_SCHEMA:
        failures.append("PACKAGE_SCHEMA_MISMATCH")
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
            raw_unpack(raw); exact = True
        except Exception as exc:
            exact = False; failures.append(f"RAW_VERIFY_FAILED:{exc}")
    return {"pass": not failures, "failures": failures, "exact_raw_roundtrip": exact, "semantic_equivalence_verified": False, "note": "Graph structure alone does not prove linguistic equivalence."}


@app.post("/v1/map-languages", dependencies=[Depends(auth)])
def map_languages(req: MapRequest) -> Dict[str, Any]:
    graph = req.package.get("semantic", {}).get("graph")
    if not isinstance(graph, dict):
        raise HTTPException(422, "GRAPH_MISSING")
    results = []
    for view in req.views:
        lang = view.language.lower().strip()
        if lang not in LANGUAGES:
            results.append({"language": lang, "pass": False, "error": "UNSUPPORTED_LANGUAGE"}); continue
        check = coverage(graph, view.clause_map)
        results.append({"language": lang, "text_sha256": sha(view.text.encode("utf-8")), "coverage": check, "pass": check["pass"], "semantic_equivalence_verified": False})
    return {"target_language_count": len(results), "all_structural_coverage_pass": bool(results) and all(x["pass"] for x in results), "results": results}


@app.post("/v1/roundtrip-languages", dependencies=[Depends(auth)])
def roundtrip_languages(req: RoundTripRequest) -> Dict[str, Any]:
    graph = req.package.get("semantic", {}).get("graph")
    if not isinstance(graph, dict):
        raise HTTPException(422, "GRAPH_MISSING")
    if not MODEL_URL:
        raise HTTPException(503, {"error": "SEMANTIC_MODEL_PROVIDER_NOT_CONFIGURED", "required_env": "SIGMA_SEMANTIC_MODEL_URL"})
    canonical = signature(graph); results = []
    for lang in req.target_languages:
        lang = lang.lower().strip()
        if lang not in LANGUAGES:
            results.append({"language": lang, "pass": False, "error": "UNSUPPORTED_LANGUAGE"}); continue
        try:
            rendered = provider({"operation": "render", "language": lang, "semantic_graph": graph, "constraints": {"preserve_proposition_ids": True, "return_clause_map": True}})
            text = rendered["text"]; clause_map = rendered.get("clause_map", [])
            c = coverage(graph, clause_map)
            extracted = provider({"operation": "extract", "language": lang, "text": text, "schema": GRAPH_SCHEMA, "constraints": {"do_not_invent_claims": True}})
            new_graph = extracted["semantic_graph"]; new_graph.setdefault("schema", GRAPH_SCHEMA)
            semantic_equal = not graph_errors(new_graph) and signature(new_graph) == canonical
            results.append({"language": lang, "rendered_text": text, "coverage": c, "semantic_equivalence_verified": semantic_equal, "pass": c["pass"] and semantic_equal})
        except Exception as exc:
            results.append({"language": lang, "pass": False, "error": str(exc)})
    return {"all_roundtrip_pass": bool(results) and all(x["pass"] for x in results), "results": results, "rule": "RENDER->CLAUSE_COVERAGE->REEXTRACT->GRAPH_SIGNATURE_EQUALITY"}


HTML = """<!doctype html><meta charset='utf-8'><meta name='viewport' content='width=device-width'><title>SIGMA Semantic Capsule Codec</title><style>body{font-family:system-ui;max-width:1000px;margin:24px auto;padding:0 16px}textarea{width:100%;min-height:180px}button,input,select{padding:8px;margin:4px}</style><h1>SIGMA Semantic Capsule Codec v0.1</h1><p><b>Compact surface is a semantic locator, not machine-verified SIGMA grammar.</b></p><p>API docs: <a href='/docs'>/docs</a> | health: <a href='/v1/health'>/v1/health</a></p><select id='lang'></select><textarea id='text' placeholder='Source text'></textarea><textarea id='graph' placeholder='Optional complete semantic graph JSON'></textarea><input id='key' type='password' placeholder='API key if enabled'><button onclick='go()'>Encode</button><pre id='out'></pre><script>const L=%s;for(const k in L){let o=document.createElement('option');o.value=k;o.textContent=k+' — '+L[k];lang.appendChild(o)}async function go(){let g=null;if(graph.value.trim())g=JSON.parse(graph.value);let h={'Content-Type':'application/json'};if(key.value)h['X-SIGMA-API-Key']=key.value;let r=await fetch('/v1/encode',{method:'POST',headers:h,body:JSON.stringify({text:text.value,source_language:lang.value,semantic_graph:g,preserve_exact_raw:true})});out.textContent=JSON.stringify(await r.json(),null,2)}</script>""" % json.dumps(LANGUAGES, ensure_ascii=False)


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return HTML


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if args.host not in {"127.0.0.1", "localhost", "::1"} and not API_KEY:
        raise SystemExit("REFUSING_NON_LOOPBACK_WITHOUT_SIGMA_CODEC_API_KEY")
    import uvicorn
    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
