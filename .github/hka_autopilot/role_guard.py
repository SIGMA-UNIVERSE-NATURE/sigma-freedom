#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

CONTROL_ROOT = "DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT"
ACADEMIC_ROOT = "DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING"
SENTINEL_ROOT = f"{CONTROL_ROOT}/STATUS_REPORTS/DIRECTOR-BACKUP-S01/"


def git(repo: Path, *args: str) -> str:
    p = subprocess.run(["git", "-C", str(repo), *args], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode:
        raise RuntimeError(p.stderr.strip() or "git failed")
    return p.stdout.strip()


def find_child(registry: dict, window: str) -> dict | None:
    for stage in registry.get("stages", []):
        for family in stage.get("windows", []):
            if family.get("window_id") == window:
                return family
            for child in family.get("children", []):
                if child.get("window_id") == window:
                    return child
    return None


def check(role: str, action: str, window: str, repo: Path, base: str) -> dict:
    if git(repo, "status", "--porcelain"):
        raise ValueError("working tree is not clean after agent execution")
    head = git(repo, "rev-parse", "HEAD")
    if head == base:
        raise ValueError("agent produced no commit")
    files = [x for x in git(repo, "diff", "--name-only", f"{base}..{head}").splitlines() if x]
    if not files:
        raise ValueError("agent commit has no file changes")

    if role == "WORKER":
        academic_prefix = f"{ACADEMIC_ROOT}/B1.4/{window}/"
        status_prefix = f"{CONTROL_ROOT}/STATUS_REPORTS/{window}/"
        bad = [f for f in files if not (f.startswith(academic_prefix) or f.startswith(status_prefix))]
        if bad:
            raise ValueError(f"WORKER boundary violation: {bad}")
        status_path = repo / status_prefix / "STATUS.json"
        if not status_path.exists():
            raise ValueError("WORKER terminal STATUS.json missing")
        status = json.loads(status_path.read_text(encoding="utf-8"))
        if status.get("status") not in {"PASS_CANDIDATE", "BLOCK", "BLOCKED", "BLOCKED_EXTERNAL"}:
            raise ValueError(f"WORKER non-terminal status: {status.get('status')}")

    elif role == "DIRECTOR":
        bad = [f for f in files if not f.startswith(f"{CONTROL_ROOT}/")]
        if bad:
            raise ValueError(f"DIRECTOR boundary violation: {bad}")
        registry = json.loads((repo / CONTROL_ROOT / "WINDOW_REGISTRY.json").read_text(encoding="utf-8"))
        child = find_child(registry, window)
        if action in {"RUN_DIRECTOR_REVIEW", "RUN_DIRECTOR_BLOCK_REVIEW"}:
            if not child or child.get("status") not in {"REPAIR_REQUIRED", "DIRECTOR_ACCEPTED_PASS_SENTINEL_PENDING", "DIRECTOR_ACCEPTED_PASS_PENDING_SENTINEL"}:
                raise ValueError("DIRECTOR review did not reach ACCEPT-or-REPAIR durable state")
        if action == "RUN_DIRECTOR_APPLY_SENTINEL_RESULT":
            if not child or child.get("status") != "PASS" or child.get("post_acceptance_sentinel") != "TREE_ALIGNMENT_PASS":
                raise ValueError("DIRECTOR did not apply Sentinel PASS to child")
        if action == "RUN_DIRECTOR_OPEN_SUCCESSOR":
            if not child or child.get("status") != "READY" or child.get("unlocked") is not True or not child.get("execution_branch"):
                raise ValueError("DIRECTOR successor opening did not produce READY unlocked child with branch")

    elif role == "SENTINEL":
        bad = [f for f in files if not f.startswith(SENTINEL_ROOT)]
        if bad:
            raise ValueError(f"SENTINEL boundary violation: {bad}")
        status_path = repo / SENTINEL_ROOT / "STATUS.json"
        if not status_path.exists():
            raise ValueError("SENTINEL STATUS.json missing")
        status = json.loads(status_path.read_text(encoding="utf-8"))
        fresh = status.get("fresh_alignment", {})
        if fresh.get("accepted_window") != window:
            raise ValueError("SENTINEL result is not for requested window")
        if status.get("status") not in {"TREE_ALIGNMENT_PASS", "TREE_ALIGNMENT_ALERT", "RECOVERY_REQUIRED"}:
            raise ValueError("SENTINEL did not produce a terminal alignment result")
    else:
        raise ValueError(f"unsupported role: {role}")

    return {"ok": True, "role": role, "action": action, "window": window, "base": base, "head": head, "files": files}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--role", required=True)
    ap.add_argument("--action", required=True)
    ap.add_argument("--window", required=True)
    ap.add_argument("--repo", default="work")
    ap.add_argument("--base", required=True)
    args = ap.parse_args()
    try:
        result = check(args.role, args.action, args.window, Path(args.repo), args.base)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
