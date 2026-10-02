#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, subprocess, sys
from pathlib import Path
from validate_gate_b import load, sha, validate_all

PH=['{VM}','{UNIFIED_BYTECODE}','{ENTRYPOINT}','{POLICY_TOKEN}','{WORKSET}','{CAPABILITY}','{BASELINE_REF}','{CANDIDATE_REF}','{BASELINE_FINGERPRINT}','{CANDIDATE_FINGERPRINT}']
def render(s,m):
    for k in PH:s=s.replace(k,m.get(k,''))
    return s

def bound_paths(m,proofs):
    r=m['runtime']; g=m['gate_a_evidence']; out=[]
    for k in ('module97_behavior_gate','module98_semantic_eval','module99_source_bound_adapter','unified_source','unified_bytecode','vm'):out.append(Path(r[k]['path']).expanduser().resolve())
    for k in ('rbseed','builder_log','model_pair_binding_receipt'):out.append(Path(g[k]['path']).expanduser().resolve())
    for pid in proofs:
        w=m['worksets'][pid]
        for k in ('source_root_manifest_path','input_path','workset_manifest_path'):out.append(Path(w[k]).expanduser().resolve())
        root=load(w['source_root_manifest_path'])
        for x in root['roots']:out.append(Path(x['path']).expanduser().resolve())
    return sorted(set(out),key=str)
def snap(paths):return {str(p):sha(p) for p in paths}
def changed(before):return [p for p,h in before.items() if not Path(p).is_file() or sha(p)!=h]
def mapping(m,pid):
    r=m['runtime'];g=m['gate_a_evidence'];w=m['worksets'][pid];i=m['invocations'][pid]
    return {'{VM}':r['vm']['path'],'{UNIFIED_BYTECODE}':r['unified_bytecode']['path'],'{ENTRYPOINT}':i['entrypoint_token'],'{POLICY_TOKEN}':i['policy_token'],'{WORKSET}':w['input_path'],'{CAPABILITY}':w.get('capability') or '', '{BASELINE_REF}':g['baseline_model_ref'],'{CANDIDATE_REF}':g['candidate_model_ref'],'{BASELINE_FINGERPRINT}':g['baseline_model_fingerprint'],'{CANDIDATE_FINGERPRINT}':g['candidate_model_fingerprint']}
def required(c,m,pid):
    w=m['worksets'][pid];g=m['gate_a_evidence'];r=m['runtime'];q=list(c['required_common_stdout_literals'])+[w['input_sha256'],g['baseline_model_ref'],g['candidate_model_ref'],g['baseline_model_fingerprint'],g['candidate_model_fingerprint'],r['one_sigma_identity_sha256']]
    if pid.startswith('BEHAVIOR:'):q+=c['required_behavior_stdout_literals']+[w['capability']]
    return q

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--contract',required=True,type=Path);ap.add_argument('--manifest',required=True,type=Path);ap.add_argument('--output-dir',required=True,type=Path);a=ap.parse_args()
    c=load(a.contract);m=load(a.manifest);v=validate_all(c,m)
    if v['status']!='READY':sys.stdout.write(json.dumps(v,ensure_ascii=False,indent=2)+'\n');return 2
    proofs=c['proof_ids']; paths=bound_paths(m,proofs); out=a.output_dir.expanduser().resolve()
    for p in paths:
        if out==p or out in p.parents or out==p.parent or p.parent in out.parents: raise SystemExit('BLOCKED_SAFE:output_dir_overlaps_bound_input_tree')
    out.mkdir(parents=True,exist_ok=False); before=snap(paths); results=[]
    for n,pid in enumerate(proofs,1):
        inv=m['invocations'][pid]; mp=mapping(m,pid); d=out/f'{n:02d}_{pid.replace(":","__")}';d.mkdir()
        argv=[render(x,mp) for x in inv['argv_template']]; stdin=render(inv['stdin_template'],mp) if isinstance(inv.get('stdin_template'),str) else None
        env=os.environ.copy();env.update({'SIGMA_GATE_B_PROOF_ID':pid,'SIGMA_GATE_B_LIVE_MUTATION':'NO','SIGMA_SERVER_SEED':'NO','SIGMA_ADMISSION':'NO','SIGMA_CUTOVER':'NO','TMPDIR':str(d)})
        timed=False
        try:p=subprocess.run(argv,input=stdin,cwd=d,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=inv['timeout_seconds'],shell=False,check=False)
        except subprocess.TimeoutExpired as ex:
            timed=True
            class P:pass
            p=P();p.returncode=124;p.stdout=ex.stdout or '';p.stderr=ex.stderr or ''
            if isinstance(p.stdout,bytes):p.stdout=p.stdout.decode('utf-8','replace')
            if isinstance(p.stderr,bytes):p.stderr=p.stderr.decode('utf-8','replace')
        so=d/'stdout.txt';se=d/'stderr.txt';so.write_text(p.stdout,encoding='utf-8');se.write_text(p.stderr,encoding='utf-8')
        miss=[x for x in required(c,m,pid) if x not in p.stdout]; mut=changed(before);policy=inv['policy_token'] in p.stdout;acc=inv['accept_token'] in p.stdout;rej=inv['reject_token'] in p.stdout
        accepted=p.returncode==0 and not timed and policy and acc and not rej and not miss and not mut
        rec={'proof_id':pid,'policy_contract':c['proof_policies']['BEHAVIOR' if pid.startswith('BEHAVIOR:') else pid],'returncode':p.returncode,'timeout':timed,'native_policy_token_seen':policy,'native_accept_token_seen':acc,'native_reject_token_seen':rej,'missing_required_stdout_literals':miss,'bound_input_mutations_detected':mut,'stdout_sha256':sha(so),'stderr_sha256':sha(se),'decision':'ACCEPTED_NATIVE' if accepted else 'REJECTED_OR_BLOCKED'}
        results.append(rec);(d/'result.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        if not accepted:break
    mut=changed(before);allok=len(results)==len(proofs) and all(x['decision']=='ACCEPTED_NATIVE' for x in results) and not mut
    final={'schema':'SIGMA_GATE_B_DEV_CORE_BEHAVIOR_TINY_PROOF_RESULT_V1','decision':'ACCEPT' if allok else 'BLOCKED_OR_REJECT','scope':c['scope'],'proofs_required':len(proofs),'proofs_executed':len(results),'proofs':results,'final_bound_input_mutations_detected':mut,'host_semantic_answer':False,'host_semantic_score':False,'live_mutation':False,'server_seed':False,'final_or_reserve':False,'admission':False,'cutover':False,'claim_ceiling':'TINY_SOURCE_BOUND_DEV_CORE_BEHAVIOR_ONLY'}
    (out/'gate_b_result.json').write_text(json.dumps(final,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(final,ensure_ascii=False,indent=2));return 0 if allok else 3
if __name__=='__main__':raise SystemExit(main())
