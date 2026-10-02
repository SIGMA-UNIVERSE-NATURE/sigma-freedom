#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path

HEX64=re.compile(r'^[0-9a-f]{64}$')
SOURCES={'module97_behavior_gate','module98_semantic_eval','module99_source_bound_adapter'}
CAPS=['referent_identity','relation_support','contradiction','scope_compatibility','evidence_support','cross_document_support']
PROOFS=['DEV','CORE']+[f'BEHAVIOR:{x}' for x in CAPS]
POLICIES={'DEV':'CANDIDATE_GAIN_ON_SOURCE_BOUND_DEV','CORE':'CANDIDATE_NO_REGRESSION_ON_SOURCE_BOUND_CORE','BEHAVIOR':'ALL_CORRECT_AND_NO_REGRESSION_ON_SOURCE_BOUND_CAPABILITY_EXAM'}

def load(p):
    v=json.loads(Path(p).read_text(encoding='utf-8'))
    if not isinstance(v,dict): raise ValueError(f'json_not_object:{p}')
    return v

def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''): h.update(b)
    return h.hexdigest()

def okhash(v): return isinstance(v,str) and bool(HEX64.fullmatch(v))
def nonempty(v): return isinstance(v,str) and bool(v.strip())
def err(E,x):
    if x not in E:E.append(x)

def artifact(E,label,o,expected=None,basename=None):
    if not isinstance(o,dict): err(E,label+':not_object'); return None
    rp=o.get('path'); declared=o.get('sha256')
    if not nonempty(rp): err(E,label+':path_unbound'); return None
    p=Path(rp).expanduser()
    if not p.is_absolute(): err(E,label+':path_not_absolute')
    if basename and p.name!=basename: err(E,label+':basename_mismatch')
    if not okhash(declared): err(E,label+':sha256_unbound'); return p
    if expected and declared!=expected: err(E,label+':declared_sha256_not_checkpoint')
    if not p.is_file(): err(E,label+':file_missing'); return p
    if p.stat().st_size<=0: err(E,label+':file_empty')
    actual=sha(p)
    if actual!=declared: err(E,label+':sha256_mismatch')
    if expected and actual!=expected: err(E,label+':actual_sha256_not_checkpoint')
    return p

def workset(E,pid,o):
    if not isinstance(o,dict): err(E,f'workset:{pid}:not_object'); return
    role='BEHAVIOR' if pid.startswith('BEHAVIOR:') else pid
    cap=pid.split(':',1)[1] if pid.startswith('BEHAVIOR:') else None
    if o.get('role')!=role: err(E,f'workset:{pid}:role_mismatch')
    if o.get('capability')!=cap: err(E,f'workset:{pid}:capability_mismatch')
    sr=artifact(E,f'workset:{pid}:source_root_manifest',{'path':o.get('source_root_manifest_path'),'sha256':o.get('source_root_manifest_sha256')})
    inp=artifact(E,f'workset:{pid}:input',{'path':o.get('input_path'),'sha256':o.get('input_sha256')})
    wm=artifact(E,f'workset:{pid}:workset_manifest',{'path':o.get('workset_manifest_path'),'sha256':o.get('workset_manifest_sha256')})
    if sr and sr.is_file():
        try: r=load(sr)
        except Exception as ex: err(E,f'workset:{pid}:source_root_manifest_json:{type(ex).__name__}'); r={}
        if r.get('schema')!='SIGMA_GATE_B_SOURCE_ROOT_MANIFEST_V1': err(E,f'workset:{pid}:source_root_schema')
        roots=r.get('roots')
        if not isinstance(roots,list) or not roots: err(E,f'workset:{pid}:source_roots_empty')
        else:
            for i,x in enumerate(roots): artifact(E,f'workset:{pid}:source_root:{i}',x)
    if wm and wm.is_file():
        try: w=load(wm)
        except Exception as ex: err(E,f'workset:{pid}:workset_manifest_json:{type(ex).__name__}'); w={}
        if w.get('schema')!='SIGMA_GATE_B_WORKSET_MANIFEST_V1': err(E,f'workset:{pid}:manifest_schema')
        if w.get('role')!=role or w.get('capability')!=cap: err(E,f'workset:{pid}:manifest_role_or_capability')
        if w.get('source_root_manifest_sha256')!=o.get('source_root_manifest_sha256'): err(E,f'workset:{pid}:manifest_source_root_hash')
        if w.get('input_sha256')!=o.get('input_sha256'): err(E,f'workset:{pid}:manifest_input_hash')

def invtext(inv):
    a=inv.get('argv_template'); parts=list(a) if isinstance(a,list) else []
    if isinstance(inv.get('stdin_template'),str): parts.append(inv['stdin_template'])
    return '\n'.join(map(str,parts))

def invocation(E,pid,inv,source_texts,forbidden):
    if not isinstance(inv,dict): err(E,f'invocation:{pid}:not_object'); return
    sk=inv.get('binding_source')
    if sk not in SOURCES: err(E,f'invocation:{pid}:binding_source_unbound'); return
    src=source_texts.get(sk)
    if src is None: err(E,f'invocation:{pid}:binding_source_unavailable'); return
    for k in ('entrypoint_token','policy_token','accept_token','reject_token'):
        v=inv.get(k)
        if not nonempty(v): err(E,f'invocation:{pid}:{k}_unbound')
        elif v not in src: err(E,f'invocation:{pid}:{k}_not_source_bound')
    if nonempty(inv.get('accept_token')) and inv.get('accept_token')==inv.get('reject_token'): err(E,f'invocation:{pid}:accept_equals_reject')
    a=inv.get('argv_template')
    if not isinstance(a,list) or not a or not all(nonempty(x) for x in a): err(E,f'invocation:{pid}:argv_unbound'); a=[]
    elif a[0]!='{VM}': err(E,f'invocation:{pid}:argv_must_start_bound_vm')
    if '{UNIFIED_BYTECODE}' not in a: err(E,f'invocation:{pid}:missing_unified_bytecode')
    if inv.get('stdin_template') is not None and not isinstance(inv.get('stdin_template'),str): err(E,f'invocation:{pid}:stdin_invalid')
    t=invtext(inv)
    for ph in ('{ENTRYPOINT}','{POLICY_TOKEN}','{WORKSET}','{BASELINE_REF}','{CANDIDATE_REF}'):
        if ph not in t: err(E,f'invocation:{pid}:missing:{ph}')
    if pid.startswith('BEHAVIOR:') and '{CAPABILITY}' not in t: err(E,f'invocation:{pid}:missing:{{CAPABILITY}}')
    up=t.upper()
    for x in forbidden:
        if x in up: err(E,f'invocation:{pid}:forbidden:{x}')
    to=inv.get('timeout_seconds')
    if not isinstance(to,int) or to<=0 or to>86400: err(E,f'invocation:{pid}:timeout_invalid')

def validate_all(c,m):
    E=[]; resolved={'sources':{},'proofs':PROOFS}
    if c.get('schema')!='SIGMA_GATE_B_DEV_CORE_BEHAVIOR_SOURCE_BOUND_CONTRACT_V1': err(E,'contract:schema')
    if c.get('required_capabilities')!=CAPS or c.get('proof_ids')!=PROOFS or c.get('proof_policies')!=POLICIES: err(E,'contract:exact_policy_or_proof_set_mismatch')
    if m.get('schema')!='SIGMA_GATE_B_DEV_CORE_BEHAVIOR_PREREQUISITES_V1': err(E,'manifest:schema')
    if m.get('binding_state')!='BOUND_BY_OPPO_MEASUREMENT': err(E,'manifest:binding_state_not_bound')
    if m.get('boundaries')!=c.get('boundaries'): err(E,'manifest:boundaries_mismatch')
    r=m.get('runtime') if isinstance(m.get('runtime'),dict) else {}; x=c.get('expected_bindings') or {}
    if r.get('one_sigma_identity_sha256')!=x.get('one_sigma_identity_sha256'): err(E,'runtime:one_sigma_identity')
    specs={'module97_behavior_gate':(x.get('module97_behavior_gate_sha256'),None),'module98_semantic_eval':(x.get('module98_semantic_eval_sha256'),x.get('module98_basename')),'module99_source_bound_adapter':(None,x.get('module99_basename'))}
    texts={}
    for k,(h,b) in specs.items():
        p=artifact(E,'runtime:'+k,r.get(k),h,b)
        if p and p.is_file(): texts[k]=p.read_text(encoding='utf-8',errors='replace'); resolved['sources'][k]=str(p)
    artifact(E,'runtime:unified_source',r.get('unified_source'),x.get('unified_source_sha256'))
    artifact(E,'runtime:unified_bytecode',r.get('unified_bytecode'),x.get('unified_bytecode_sha256'))
    artifact(E,'runtime:vm',r.get('vm'))
    g=m.get('gate_a_evidence') if isinstance(m.get('gate_a_evidence'),dict) else {}
    artifact(E,'gate_a:rbseed',g.get('rbseed')); artifact(E,'gate_a:builder_log',g.get('builder_log'))
    pr=artifact(E,'gate_a:model_pair_binding_receipt',g.get('model_pair_binding_receipt'))
    fields=('baseline_model_ref','baseline_model_fingerprint','candidate_model_ref','candidate_model_fingerprint')
    for f in fields:
        if not nonempty(g.get(f)): err(E,'gate_a:'+f+'_unbound')
    if pr and pr.is_file():
        t=pr.read_text(encoding='utf-8',errors='replace')
        for f in fields:
            if nonempty(g.get(f)) and g[f] not in t: err(E,'gate_a:model_pair_receipt_missing:'+f)
    ws=m.get('worksets') if isinstance(m.get('worksets'),dict) else {}
    if set(ws)!=set(PROOFS): err(E,'worksets:proof_set')
    for pid in PROOFS: workset(E,pid,ws.get(pid))
    iv=m.get('invocations') if isinstance(m.get('invocations'),dict) else {}
    if set(iv)!=set(PROOFS): err(E,'invocations:proof_set')
    forbidden=c.get('forbidden_invocation_fragments') or []
    for pid in PROOFS: invocation(E,pid,iv.get(pid),texts,forbidden)
    return {'schema':'SIGMA_GATE_B_PREREQUISITE_VALIDATION_V1','status':'READY' if not E else 'BLOCKED_SAFE','errors':E,'resolved':resolved,'proof_count_required':8,'capability_count_required':6,'host_semantic_answer':False,'host_semantic_score':False,'live_mutation':False,'server_seed':False,'admission':False,'cutover':False}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--contract',required=True,type=Path); ap.add_argument('--manifest',required=True,type=Path); ap.add_argument('--json-out',type=Path); a=ap.parse_args()
    try: out=validate_all(load(a.contract),load(a.manifest))
    except Exception as ex: out={'schema':'SIGMA_GATE_B_PREREQUISITE_VALIDATION_V1','status':'BLOCKED_SAFE','errors':[f'validator_exception:{type(ex).__name__}:{ex}']}
    s=json.dumps(out,ensure_ascii=False,indent=2)+'\n'; sys.stdout.write(s)
    if a.json_out: a.json_out.parent.mkdir(parents=True,exist_ok=True); a.json_out.write_text(s,encoding='utf-8')
    return 0 if out.get('status')=='READY' else 2
if __name__=='__main__': raise SystemExit(main())
