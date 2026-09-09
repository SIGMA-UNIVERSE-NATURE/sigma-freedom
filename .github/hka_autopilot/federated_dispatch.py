#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


def stable_request_id(req: dict[str, Any]) -> str:
    material = "|".join([
        str(req.get("control_plane_branch") or ""),
        str(req.get("role") or ""),
        str(req.get("action") or ""),
        str(req.get("target_window") or ""),
        str(req.get("target_branch") or ""),
    ])
    return hashlib.sha256(material.encode("utf-8")).hexdigest()[:24]


def api(method: str, url: str, token: str, payload: dict[str, Any] | None = None) -> Any:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    r = urllib.request.Request(url, method=method, data=data)
    r.add_header("Accept", "application/vnd.github+json")
    r.add_header("X-GitHub-Api-Version", "2022-11-28")
    r.add_header("Authorization", f"Bearer {token}")
    if data is not None:
        r.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(r, timeout=30) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
        return json.loads(raw) if raw else None


def extract_json_block(body: str) -> dict[str, Any] | None:
    start = body.find("```json")
    if start < 0:
        return None
    start = body.find("\n", start)
    if start < 0:
        return None
    end = body.find("```", start + 1)
    if end < 0:
        return None
    try:
        value = json.loads(body[start + 1:end].strip())
        return value if isinstance(value, dict) else None
    except json.JSONDecodeError:
        return None


def semantic_equal(a: dict[str, Any], b: dict[str, Any]) -> bool:
    keys = ("role", "action", "target_window", "target_branch", "control_plane_branch")
    return all((a.get(k) or None) == (b.get(k) or None) for k in keys)


def existing_equivalent_issue(repo: str, token: str, req: dict[str, Any]) -> dict[str, Any] | None:
    issues = api("GET", f"https://api.github.com/repos/{repo}/issues?state=open&per_page=100", token) or []
    for issue in issues:
        if issue.get("pull_request"):
            continue
        body = issue.get("body") or ""
        if "hka-autopilot-request:" not in body:
            continue
        old = extract_json_block(body)
        if old and semantic_equal(old, req):
            return {"number": issue.get("number"), "title": issue.get("title"), "request_id": old.get("request_id")}
    return None


def try_webhook(req: dict[str, Any]) -> dict[str, Any] | None:
    url = (os.getenv("HKA_AGENT_WEBHOOK_URL") or "").strip()
    if not url:
        return None
    token = (os.getenv("HKA_AGENT_WEBHOOK_TOKEN") or "").strip()
    data = json.dumps(req).encode("utf-8")
    r = urllib.request.Request(url, method="POST", data=data)
    r.add_header("Content-Type", "application/json")
    if token:
        r.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(r, timeout=30) as resp:
            if 200 <= resp.status < 300:
                return {"dispatched": True, "mode": "agent_webhook", "status": resp.status}
            return None
    except Exception:
        return None


def dispatch(req: dict[str, Any]) -> dict[str, Any]:
    action = str(req.get("action") or "")
    if action.startswith("HOLD_") or action.startswith("HALT_"):
        return {"dispatched": False, "mode": "none", "reason": action}

    original_id = req.get("request_id")
    req = dict(req)
    req["planner_request_id"] = original_id
    req["request_id"] = stable_request_id(req)
    req["idempotency_policy"] = "SEMANTIC_ROLE_ACTION_WINDOW_BRANCH_V1"

    webhook_result = try_webhook(req)
    if webhook_result:
        webhook_result["request_id"] = req["request_id"]
        return webhook_result

    token = (os.getenv("GITHUB_TOKEN") or "").strip()
    repo = (os.getenv("GITHUB_REPOSITORY") or "").strip()
    if not token or not repo:
        return {"dispatched": False, "mode": "none", "reason": "no healthy webhook and GitHub queue credentials unavailable"}

    equivalent = existing_equivalent_issue(repo, token, req)
    if equivalent:
        return {
            "dispatched": True,
            "mode": "github_issue_existing_semantic",
            "issue_number": equivalent["number"],
            "existing_request_id": equivalent.get("request_id"),
            "stable_request_id": req["request_id"],
        }

    marker = f"<!-- hka-autopilot-request:{req['request_id']} -->"
    body = marker + "\n\n```json\n" + json.dumps(req, ensure_ascii=False, indent=2) + "\n```\n\n"
    body += "Federated HKA Autopilot request. Preserve role separation and durable governance. Optional runner failure must not advance state or discard this request."
    created = api("POST", f"https://api.github.com/repos/{repo}/issues", token, {
        "title": f"[HKA AUTOPILOT] {req.get('role')} · {req.get('action')} · {req.get('target_window') or 'control-plane'}",
        "body": body,
    })
    return {
        "dispatched": True,
        "mode": "github_issue_created_semantic",
        "issue_number": created.get("number"),
        "request_id": req["request_id"],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--request", required=True)
    args = ap.parse_args()
    with Path(args.request).open("r", encoding="utf-8") as f:
        req = json.load(f)
    result = dispatch(req)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("dispatched") or result.get("mode") == "none" else 2


if __name__ == "__main__":
    raise SystemExit(main())
