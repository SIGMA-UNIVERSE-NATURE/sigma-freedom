#!/usr/bin/env python3
"""Durable mechanical per-cycle request/byte/rate/disk budget; no semantic fallback."""
from __future__ import annotations
import fcntl, json, os, shutil, time
from pathlib import Path

MAX_TOTAL_BYTES_PER_CYCLE=64*1024*1024
MAX_REQUESTS_PER_CYCLE=32
PER_DOMAIN_BACKOFF=2.0
GLOBAL_BACKOFF=1.0
DISK_HIGH_WATER_MARK_PERCENT=85.0

class BudgetError(RuntimeError): pass

class CycleBudget:
    def __init__(self, root: str | Path):
        self.root=Path(root); self.root.mkdir(parents=True,exist_ok=True)
        self.lock_path=self.root/'budget.lock'; self.state_path=self.root/'budget.state.json'
        self.fd=None; self.state=None; self.domain=None
    def __enter__(self): return self
    def __exit__(self, *exc): self.release()
    def _read(self):
        if not self.state_path.exists(): return {'request_count':0,'total_bytes':0,'last_global_epoch':0.0,'last_domain_epoch':{}}
        try: return json.loads(self.state_path.read_text())
        except Exception as e: raise BudgetError('BUDGET_STATE_INVALID') from e
    def acquire(self, domain: str, storage_root: str | Path):
        self.fd=os.open(self.lock_path, os.O_CREAT|os.O_RDWR, 0o600)
        try: fcntl.flock(self.fd, fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError as e:
            os.close(self.fd); self.fd=None; raise BudgetError('MAX_INFLIGHT_REQUESTS_REACHED') from e
        self.state=self._read(); self.domain=domain
        if int(self.state.get('request_count',0)) >= MAX_REQUESTS_PER_CYCLE: raise BudgetError('MAX_REQUESTS_PER_CYCLE_REACHED')
        if int(self.state.get('total_bytes',0)) >= MAX_TOTAL_BYTES_PER_CYCLE: raise BudgetError('MAX_TOTAL_BYTES_PER_CYCLE_REACHED')
        usage=shutil.disk_usage(Path(storage_root))
        pct=(usage.used/usage.total*100.0) if usage.total else 100.0
        if pct >= DISK_HIGH_WATER_MARK_PERCENT: raise BudgetError('DISK_HIGH_WATER_MARK_REACHED')
        now=time.time(); lastg=float(self.state.get('last_global_epoch',0.0)); lastd=float(self.state.get('last_domain_epoch',{}).get(domain,0.0))
        wait=max(GLOBAL_BACKOFF-(now-lastg), PER_DOMAIN_BACKOFF-(now-lastd), 0.0)
        if wait > 0: raise BudgetError(f'RATE_BACKOFF_REQUIRED_SECONDS={wait:.3f}')
        return self
    def commit_attempt(self, response_bytes: int):
        if self.fd is None or self.state is None or self.domain is None: raise BudgetError('BUDGET_NOT_ACQUIRED')
        now=time.time(); self.state['request_count']=int(self.state.get('request_count',0))+1
        self.state['total_bytes']=int(self.state.get('total_bytes',0))+max(0,int(response_bytes))
        self.state['last_global_epoch']=now
        d=dict(self.state.get('last_domain_epoch',{})); d[self.domain]=now; self.state['last_domain_epoch']=d
        tmp=self.state_path.with_name(self.state_path.name+'.partial')
        data=(json.dumps(self.state,sort_keys=True)+'\n').encode()
        with tmp.open('wb') as f: f.write(data); f.flush(); os.fsync(f.fileno())
        os.replace(tmp,self.state_path)
        dfd=os.open(self.root,os.O_RDONLY)
        try: os.fsync(dfd)
        finally: os.close(dfd)
    def release(self):
        if self.fd is not None:
            try: fcntl.flock(self.fd,fcntl.LOCK_UN)
            finally: os.close(self.fd); self.fd=None
