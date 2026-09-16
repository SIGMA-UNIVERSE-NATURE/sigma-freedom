#!/usr/bin/env python3
"""Public read-only HTTP transport. No semantic ranking, fallback, or rewriting."""
from __future__ import annotations
import argparse, hashlib, http.client, ipaddress, json, os, socket, ssl, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from resource_budget import CycleBudget, BudgetError
from urllib.parse import urljoin, urlsplit, urlunsplit

DEFAULT_MAX_BYTES = 8 * 1024 * 1024
DEFAULT_MAX_REDIRECTS = 5
DEFAULT_CONNECT_TIMEOUT = 10.0
DEFAULT_TRANSFER_TIMEOUT = 30.0

class PolicyError(RuntimeError):
    pass


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _safe_ip(text: str) -> bool:
    try:
        ip = ipaddress.ip_address(text)
    except ValueError:
        return False
    return bool(ip.is_global and not ip.is_multicast and not ip.is_unspecified)


def resolve_public(host: str, port: int) -> list[str]:
    infos = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
    ips = sorted({row[4][0] for row in infos})
    if not ips:
        raise PolicyError('DNS_EMPTY')
    bad = [ip for ip in ips if not _safe_ip(ip)]
    if bad:
        raise PolicyError('DNS_CONTAINS_NONPUBLIC_ADDRESS')
    return ips


def validate_url(raw_url: str, allow_http: bool = False) -> tuple[str, str, int, str, list[str]]:
    if '\r' in raw_url or '\n' in raw_url or '\x00' in raw_url:
        raise PolicyError('URL_CONTROL_BYTE')
    parts = urlsplit(raw_url)
    if parts.scheme not in ({'https', 'http'} if allow_http else {'https'}):
        raise PolicyError('SCHEME_REJECTED')
    if parts.username is not None or parts.password is not None:
        raise PolicyError('URL_CREDENTIALS_REJECTED')
    if not parts.hostname:
        raise PolicyError('HOST_MISSING')
    host = parts.hostname.rstrip('.').lower()
    if host == 'localhost' or host.endswith('.localhost') or host.endswith('.local'):
        raise PolicyError('LOCAL_HOSTNAME_REJECTED')
    try:
        port = parts.port or (443 if parts.scheme == 'https' else 80)
    except ValueError as e:
        raise PolicyError('PORT_INVALID') from e
    if port < 1 or port > 65535:
        raise PolicyError('PORT_INVALID')
    # Fragments are never transmitted by HTTP. Preserve selected URL as provenance,
    # but derive request URL only by this protocol-defined mechanical removal.
    request_url = urlunsplit((parts.scheme, parts.netloc, parts.path or '/', parts.query, ''))
    ips = resolve_public(host, port)
    return request_url, host, port, parts.scheme, ips


class PinnedHTTPConnection(http.client.HTTPConnection):
    def __init__(self, host: str, port: int, ip: str, timeout: float):
        super().__init__(host, port, timeout=timeout)
        self._pinned_ip = ip
    def connect(self):
        self.sock = socket.create_connection((self._pinned_ip, self.port), self.timeout)


class PinnedHTTPSConnection(http.client.HTTPSConnection):
    def __init__(self, host: str, port: int, ip: str, timeout: float):
        super().__init__(host, port, timeout=timeout, context=ssl.create_default_context())
        self._pinned_ip = ip
    def connect(self):
        sock = socket.create_connection((self._pinned_ip, self.port), self.timeout)
        self.sock = self._context.wrap_socket(sock, server_hostname=self.host)


def request_once(method: str, selected_url: str, max_bytes: int, connect_timeout: float,
                 transfer_timeout: float, allow_http: bool) -> tuple[int, dict, bytes, dict]:
    request_url, host, port, scheme, ips = validate_url(selected_url, allow_http=allow_http)
    ip = ips[0]  # deterministic mechanical choice from validated public addresses
    parts = urlsplit(request_url)
    path = urlunsplit(('', '', parts.path or '/', parts.query, ''))
    conn_cls = PinnedHTTPSConnection if scheme == 'https' else PinnedHTTPConnection
    conn = conn_cls(host, port, ip, connect_timeout)
    headers = {
        'Host': host if port in (80, 443) else f'{host}:{port}',
        'User-Agent': 'SIGMA-Survival-Mechanical-Bridge-R1/1',
        'Accept': '*/*',
        'Connection': 'close',
    }
    start = time.monotonic()
    try:
        conn.request(method, path, body=None, headers=headers)
        if conn.sock is not None:
            conn.sock.settimeout(transfer_timeout)
        resp = conn.getresponse()
        body = b'' if method == 'HEAD' else resp.read(max_bytes + 1)
        if len(body) > max_bytes:
            raise PolicyError('RESPONSE_SIZE_BOUND_REACHED')
        hdrs = {k.lower(): v for k, v in resp.getheaders()}
        meta = {
            'request_url': request_url,
            'host': host,
            'port': port,
            'scheme': scheme,
            'resolved_public_ips': ips,
            'connected_ip': ip,
            'elapsed_ms': int((time.monotonic() - start) * 1000),
        }
        return resp.status, hdrs, body, meta
    finally:
        conn.close()


def fetch(method: str, selected_url: str, max_bytes: int, max_redirects: int,
          connect_timeout: float, transfer_timeout: float, allow_http: bool):
    current = selected_url
    chain = []
    total_body = b''
    for hop in range(max_redirects + 1):
        status, headers, body, meta = request_once(method, current, max_bytes, connect_timeout,
                                                   transfer_timeout, allow_http)
        chain.append({'selected_url': current, 'status': status, **meta})
        if status in (301, 302, 303, 307, 308) and 'location' in headers:
            if hop >= max_redirects:
                raise PolicyError('REDIRECT_BOUND_REACHED')
            current = urljoin(meta['request_url'], headers['location'])
            continue
        total_body = body
        return status, headers, total_body, chain
    raise PolicyError('REDIRECT_BOUND_REACHED')


def atomic_write(path: Path, data: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.partial')
    with tmp.open('wb') as f:
        f.write(data); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--method', choices=['GET', 'HEAD'], required=True)
    ap.add_argument('--url-file', required=True, help='exact native-selected URL bytes, UTF-8')
    ap.add_argument('--out-root', required=True)
    ap.add_argument('--cycle-root', required=True, help='durable mechanical resource-budget state root')
    ap.add_argument('--max-bytes', type=int, default=DEFAULT_MAX_BYTES)
    ap.add_argument('--max-redirects', type=int, default=DEFAULT_MAX_REDIRECTS)
    ap.add_argument('--connect-timeout', type=float, default=DEFAULT_CONNECT_TIMEOUT)
    ap.add_argument('--transfer-timeout', type=float, default=DEFAULT_TRANSFER_TIMEOUT)
    ap.add_argument('--allow-http', action='store_true')
    args = ap.parse_args()
    raw_url_bytes = Path(args.url_file).read_bytes()
    try:
        selected_url = raw_url_bytes.decode('utf-8', errors='strict').strip('\n')
    except UnicodeDecodeError:
        print('HOLD=URL_NOT_UTF8')
        return 2
    request_id = sha256_bytes(args.method.encode() + b'\0' + raw_url_bytes)
    out = Path(args.out_root) / request_id
    out.mkdir(parents=True, exist_ok=True)
    budget = CycleBudget(args.cycle_root)
    attempted = False
    try:
        _, initial_host, _, _, _ = validate_url(selected_url, allow_http=args.allow_http)
        budget.acquire(initial_host, args.out_root)
        attempted = True
        status, headers, body, chain = fetch(args.method, selected_url, args.max_bytes,
                                             args.max_redirects, args.connect_timeout,
                                             args.transfer_timeout, args.allow_http)
        budget.commit_attempt(len(body))
    except (BudgetError, PolicyError, OSError, ssl.SSLError, http.client.HTTPException) as e:
        if attempted:
            try: budget.commit_attempt(0)
            except Exception: pass
        observation = {
            'request_id': request_id,
            'transport_status': 'REJECT_OR_FAIL',
            'failure_class': type(e).__name__,
            'failure_observation': str(e),
            'host_fallback_source_selected': False,
        }
        atomic_write(out/'observation.json', (json.dumps(observation, sort_keys=True) + '\n').encode())
        print(f'REQUEST_ID={request_id}')
        print(f'HOLD_OR_OBSERVATION={type(e).__name__}:{e}')
        return 2
    finally:
        budget.release()
    atomic_write(out/'raw.response', body)
    meta = {
        'request_id': request_id,
        'method': args.method,
        'selected_url_sha256': sha256_bytes(raw_url_bytes),
        'http_status': status,
        'response_sha256': sha256_bytes(body),
        'response_bytes': len(body),
        'redirect_chain': chain,
        'response_headers': headers,
        'tls_verification_disabled': False,
        'credentials_sent': False,
        'cookie_jar_reuse': False,
        'host_semantic_selection': False,
        'host_fallback_source_selected': False,
    }
    atomic_write(out/'transport.receipt.json', (json.dumps(meta, sort_keys=True) + '\n').encode())
    print(f'REQUEST_ID={request_id}')
    print(f'HTTP_STATUS={status}')
    print(f'RAW_SHA256={meta["response_sha256"]}')
    print(f'RAW_BYTES={len(body)}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
