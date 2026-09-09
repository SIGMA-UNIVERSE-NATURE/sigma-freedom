#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import urllib.request
from typing import Any

MARKER = "hka-autopilot-request:"
ALLOWED_ROLES = {"WORKER", "DIRECTOR", "SENTINEL"}


def api(method: str, url: str, payload: dict[str, Any] | None = None) -> Any:
    token = os.environ["GITHUB_TOKEN"]
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, method=method, data=data)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("Authorization", f"Bearer {token}")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode("utf-8")
        return json.loads(raw) if raw else None


def parse_request(body: str) -> dict[str, Any] | None:
    if MARKER not in body:
        return None
    start = body.find("```json")
    if start < 0:
        return None
    start = body.find("\n", start)
    end = body.find("```", start + 1)
    if start < 0 or end < 0:
        return None
    try:
        data = json.loads(body[start + 1:end].strip())
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict) or data.get("role") not in ALLOWED_ROLES:
        return None
    action = str(data.get("action") or "")
    role = data["role"]
    if role == "WORKER" and action not in {"RUN_WORKER", "RUN_WORKER_REPAIR"}:
        return None
    if role == "SENTINEL" and action != "RUN_SENTINEL":
        return None
    if role == "DIRECTOR" and not action.startswith("RUN_"):
        return None
    return data


def work_branch(req: dict[str, Any]) -> str:
    if req["role"] == "WORKER":
        branch = req.get("target_branch")
        if not branch:
            raise ValueError("WORKER request missing target_branch")
        return str(branch)
    if req["role"] == "SENTINEL":
        return "hka-tree/director-backup-sentinel"
    return str(req.get("control_plane_branch") or "hka-tree/curriculum-master")


def select(repo: str) -> dict[str, Any]:
    issues = api("GET", f"https://api.github.com/repos/{repo}/issues?state=open&sort=created&direction=asc&per_page=100") or []
    for issue in issues:
        if issue.get("pull_request"):
            continue
        req = parse_request(issue.get("body") or "")
        if not req:
            continue
        return {
            "active": True,
            "issue_number": issue["number"],
            "title": issue.get("title"),
            "request": req,
            "role": req["role"],
            "action": req.get("action"),
            "target_window": req.get("target_window"),
            "target_branch": req.get("target_branch"),
            "work_branch": work_branch(req),
        }
    return {"active": False}


def close(repo: str, issue_number: int) -> dict[str, Any]:
    return api("PATCH", f"https://api.github.com/repos/{repo}/issues/{issue_number}", {"state": "closed", "state_reason": "completed"})


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("select")
    cp = sub.add_parser("close")
    cp.add_argument("--issue", type=int, required=True)
    args = ap.parse_args()
    repo = os.environ["GITHUB_REPOSITORY"]
    if args.cmd == "select":
        print(json.dumps(select(repo), ensure_ascii=False, indent=2))
        return 0
    close(repo, args.issue)
    print(json.dumps({"closed": True, "issue_number": args.issue}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
