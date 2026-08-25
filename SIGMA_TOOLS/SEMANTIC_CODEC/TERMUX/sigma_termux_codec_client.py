#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-
"""Small stdlib client/adapter for SIGMA -> local Termux Semantic Codec."""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.request
from typing import Any, Dict

DEFAULT_URL = os.environ.get("SIGMA_CODEC_URL", "http://127.0.0.1:8765").rstrip("/")
API_KEY = os.environ.get("SIGMA_CODEC_API_KEY", "").strip()
TOOL_NAME = "SIGMA_SEMANTIC_CODEC_TERMUX"


def request_json(path: str, payload: Dict[str, Any] | None = None) -> Dict[str, Any]:
    url = DEFAULT_URL + path
    headers = {"Accept": "application/json"}
    data = None
    method = "GET"
    if payload is not None:
        method = "POST"
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    if API_KEY:
        headers["X-SIGMA-API-Key"] = API_KEY
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=30) as response:
        result = json.loads(response.read().decode("utf-8"))
    if not isinstance(result, dict):
        raise RuntimeError("SIGMA_CODEC_RESPONSE_OBJECT_REQUIRED")
    return result


def encode(text: str, source_language: str = "vi", semantic_graph: Dict[str, Any] | None = None, *, store: bool = False) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "text": text,
        "source_language": source_language,
        "preserve_exact_raw": True,
        "store": store,
    }
    if semantic_graph is not None:
        payload["semantic_graph"] = semantic_graph
    return request_json("/v1/encode", payload)


def dna12_evidence(output: Dict[str, Any], invocation_id: str | None = None) -> Dict[str, Any]:
    invocation_id = invocation_id or f"TERMUX-CODEC-{int(time.time() * 1000)}"
    return {
        "tool_decision_context": {
            "internal_reasoning_sufficient": False,
            "tool_available": True,
            "candidate_tool": TOOL_NAME,
            "requires_retrieval": False,
            "requires_exact_computation": True,
            "requires_current_external_state": False,
            "requires_observation_or_measurement": False,
            "requires_external_action": False,
        },
        "tool_output": {
            "tool_name": TOOL_NAME,
            "invocation_id": invocation_id,
            "output": output,
            "provenance": [
                {
                    "source": DEFAULT_URL,
                    "classification": "UNVERIFIED_TOOL_OUTPUT",
                    "promotion": "REQUIRES_INDEPENDENT_VERIFICATION",
                }
            ],
            "truth_claim": None,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("health")
    enc = sub.add_parser("encode")
    enc.add_argument("--lang", default="vi")
    enc.add_argument("--store", action="store_true")
    enc.add_argument("text", nargs="?")
    args = parser.parse_args()

    if args.cmd == "health":
        result = request_json("/v1/health")
    else:
        text = args.text if args.text is not None else sys.stdin.read()
        result = encode(text, args.lang, store=args.store)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
