#!/usr/bin/env python3
from __future__ import annotations

import base64
import json
import os
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path('DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/AUTOPILOT')
FEDERATION = ROOT / 'HKA_AUTOPILOT_FEDERATION.json'


def read_json(path: Path) -> dict[str, Any]:
    with path.open('r', encoding='utf-8') as f:
        value = json.load(f)
    if not isinstance(value, dict):
        raise ValueError(f'{path} must contain an object')
    return value


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        text = str(value).strip().replace('Z', '+00:00')
        dt = datetime.fromisoformat(text)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return None


def http_json(url: str, token: str | None = None, timeout: int = 10) -> tuple[int, Any]:
    req = urllib.request.Request(url, method='GET')
    req.add_header('Accept', 'application/vnd.github+json, application/json')
    req.add_header('User-Agent', 'hka-autopilot-federation-probe-v1')
    if token:
        req.add_header('Authorization', f'Bearer {token}')
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode('utf-8', errors='replace')
            try:
                body = json.loads(raw) if raw else None
            except json.JSONDecodeError:
                body = raw[:2000]
            return resp.status, body
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode('utf-8', errors='replace')
        return exc.code, raw[:2000]


def git_head() -> str | None:
    try:
        p = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, timeout=10)
        return p.stdout.strip() if p.returncode == 0 else None
    except Exception:
        return None


def probe_github(cfg: dict[str, Any]) -> dict[str, Any]:
    return {
        'status': 'ACTIVE',
        'required': bool(cfg.get('required', True)),
        'mode': cfg.get('mode'),
        'control_plane_sha': git_head(),
        'github_repository': os.getenv('GITHUB_REPOSITORY') or None,
        'github_actions': bool(os.getenv('GITHUB_ACTIONS')),
    }


def probe_vercel(cfg: dict[str, Any]) -> dict[str, Any]:
    base = (os.getenv('HKA_VERCEL_OBSERVER_URL') or str(cfg.get('observer_url') or '')).strip()
    if not base:
        return {
            'status': str(cfg.get('status_hint') or 'UNCONFIGURED'),
            'required': bool(cfg.get('required', False)),
            'mode': cfg.get('mode'),
            'probe_url': None,
            'detail': cfg.get('last_verified_failure'),
        }
    health_path = str(cfg.get('health_path') or '/api/hka-autopilot-health')
    url = base.rstrip('/') + (health_path if health_path.startswith('/') else '/' + health_path)
    try:
        status, body = http_json(url, timeout=10)
        if status == 200 and isinstance(body, dict) and body.get('ok') is True:
            state = 'HEALTHY'
        elif status == 402:
            state = 'BLOCKED_DEPLOYMENT'
        else:
            state = 'DEGRADED'
        return {
            'status': state,
            'required': bool(cfg.get('required', False)),
            'mode': cfg.get('mode'),
            'probe_url': url,
            'http_status': status,
            'body': body if isinstance(body, dict) else str(body)[:1000],
        }
    except Exception as exc:
        return {
            'status': 'UNREACHABLE',
            'required': bool(cfg.get('required', False)),
            'mode': cfg.get('mode'),
            'probe_url': url,
            'error': f'{type(exc).__name__}: {exc}',
        }


def probe_hp(cfg: dict[str, Any]) -> dict[str, Any]:
    repo = str(cfg.get('repository') or '')
    branch = str(cfg.get('branch') or 'main')
    path = str(cfg.get('heartbeat_path') or '')
    token = (os.getenv('SIGMA_REMOTE_OPERATOR_TOKEN') or '').strip()
    heartbeat: dict[str, Any] | None = None
    source = 'contract_last_known'
    fetch_status: int | None = None

    if token and repo and path:
        url = f'https://api.github.com/repos/{repo}/contents/{path}?ref={branch}'
        try:
            fetch_status, body = http_json(url, token=token, timeout=10)
            if fetch_status == 200 and isinstance(body, dict):
                raw = base64.b64decode(body.get('content') or b'').decode('utf-8', errors='replace')
                value = json.loads(raw)
                if isinstance(value, dict):
                    heartbeat = value
                    source = 'private_repo_live_read'
        except Exception:
            heartbeat = None

    observed = None
    if heartbeat:
        observed = heartbeat.get('time')
    if not observed:
        observed = cfg.get('last_known_heartbeat')

    dt = parse_dt(str(observed) if observed else None)
    age_seconds = (now_utc() - dt).total_seconds() if dt else None
    freshness = int(cfg.get('freshness_seconds') or 600)
    if dt is None:
        state = 'UNKNOWN'
    elif age_seconds is not None and age_seconds <= freshness:
        state = 'FRESH'
    else:
        state = 'STALE'

    return {
        'status': state,
        'required': bool(cfg.get('required', False)),
        'mode': cfg.get('mode'),
        'host_id': cfg.get('host_id'),
        'heartbeat_time': observed,
        'age_seconds': round(age_seconds, 3) if age_seconds is not None else None,
        'freshness_seconds': freshness,
        'source': source,
        'private_repo_fetch_status': fetch_status,
        'live_private_read_configured': bool(token),
        'capabilities': cfg.get('allowed_hka_capabilities', []),
    }


def main() -> int:
    federation = read_json(FEDERATION)
    runners = federation.get('runners') or {}
    result = {
        'schema_version': '1.0',
        'federation_id': federation.get('federation_id'),
        'observed_at': now_utc().isoformat(),
        'routing_policy': federation.get('routing_policy'),
        'runners': {
            'GITHUB_ACTIONS': probe_github(runners.get('GITHUB_ACTIONS') or {}),
            'VERCEL_CLOUD_OBSERVER': probe_vercel(runners.get('VERCEL_CLOUD_OBSERVER') or {}),
            'HP_REMOTE_OPERATOR': probe_hp(runners.get('HP_REMOTE_OPERATOR') or {}),
        },
    }
    result['can_continue_control_loop'] = result['runners']['GITHUB_ACTIONS']['status'] == 'ACTIVE'
    result['optional_degraded'] = [
        name for name, probe in result['runners'].items()
        if not probe.get('required') and probe.get('status') not in {'ACTIVE', 'HEALTHY', 'FRESH'}
    ]
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['can_continue_control_loop'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
