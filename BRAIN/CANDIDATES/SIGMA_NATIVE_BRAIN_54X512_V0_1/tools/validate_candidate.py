#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path

R=Path(__file__).resolve().parents[1]; S=R/'src'; T=R/'tests'; E=R/'evidence'
PARTS=[S/'00_core_registry.sigma',S/'10_skill_router_a.sigma.part',S/'10_skill_router_b.sigma.part',S/'20_accuracy_kernel.sigma',S/'90_main.sigma']
OUT=S/'sigma_native_brain_54x512_v0_1.sigma'; REPORT=E/'STATIC_VALIDATION.json'
MOJI=('\ufffd','Ã','Â','â€”','Ä‘','Æ°','á»','áº')

def h(b): return hashlib.sha256(b).hexdigest()
def j(p): return json.loads(p.read_text(encoding='utf-8'))
def add(rows,i,ok,d=None): rows.append({'id':i,'pass':bool(ok),'detail':d})
def balanced(x):
    y=re.sub(r'//[^\n]*','',re.sub(r'"(?:\\.|[^"\\])*"','',x)); st=[]; pair={')':'(',']':'[','}':'{'}
    for c in y:
        if c in '([{': st.append(c)
        elif c in pair:
            if not st or st.pop()!=pair[c]: return False
    return not st

def reconcile(a):
    cp,mp=a['canonical_present'],a['machine_present']
    if cp and mp:
        if a['canonical_value']==a['machine_value']: return 'ASSERT_CANONICAL_MACHINE_AGREE'
        if a['machine_newer'] and not a['machine_ingested']: return 'HOLD_MACHINE_AHEAD_NOT_CANONICALLY_INGESTED'
        return 'HOLD_AUTHORITATIVE_CONTRADICTION'
    if cp: return 'ASSERT_CANONICAL_STATE_ONLY_NOT_LIVE_TRUTH'
    if mp: return 'ASSERT_MACHINE_EVIDENCE_ONLY_NOT_CANONICAL_STATE'
    if a['memory_present'] and a['memory_verified']: return 'HOLD_MEMORY_ONLY_REQUIRES_FRESH_EVIDENCE'
    return 'HOLD_NO_VERIFIED_EVIDENCE'

def main():
    E.mkdir(exist_ok=True); rows=[]; raw=b''.join(p.read_bytes() for p in PARTS); OUT.write_bytes(raw)
    src=raw.decode('utf-8','strict'); add(rows,'assembly_exact',OUT.read_bytes()==raw,h(raw))
    add(rows,'mandatory_header',bool(re.fullmatch(r'#SIGMAUNIVERSE_LANGUAGE\[DOMAIN=[\w.-]+\]\[VERSION=[\w.-]+\]',src.splitlines()[0])),src.splitlines()[0])
    add(rows,'no_bom','\ufeff' not in src); add(rows,'no_mojibake',not any(m in src for m in MOJI)); add(rows,'delimiters_balanced',balanced(src))
    cr=j(R/'CORE_REGISTRY_54.json'); cores=cr['cores']; ids=[x['id'] for x in cores]; names=[x['name'] for x in cores]
    add(rows,'core_ids_1_54',ids==list(range(1,55))); add(rows,'core_names_unique',len(set(names))==54)
    add(rows,'core_source_matches',re.findall(r'LPUSH\(names,\s*"([A-Z0-9_]+)"\)',src)==names)
    rt=j(R/'SKILL_ROUTER_512.json'); secs=rt['sections']; cur=1; errs=[]; th=[]
    for x in secs:
        if x['from']!=cur or x['to']<x['from']: errs.append(x['id'])
        cur=x['to']+1; th.append(x['to'])
        if any(not 1<=int(c)<=54 for c in x['primary']+x['supporting']): errs.append(x['id']+':core')
    add(rows,'31_contiguous_sections',len(secs)==31 and cur==513 and not errs,errs)
    add(rows,'source_router_matches',list(map(int,re.findall(r'skill_id\s*<=\s*(\d+)',src)))==th)
    corpus=j(T/'ACCURACY_CORPUS_V0_1.json'); cres=[]
    for c in corpus['cases']:
        a=c['inputs']; cid=c['case_id']
        if 'canonical_present' in a: got=reconcile(a)
        elif cid.startswith('A007') or cid.startswith('A008'): got='PROVENANCE_COMPLETE' if all(a.values()) else 'HOLD_MISSING_PROVENANCE'
        elif cid.startswith('A009'): got='NO_MEASURED_DELTA' if not a['metric_improved'] else ('HOLD_METRIC_ALONE_CANNOT_PROVE_PROGRESS' if not a['independent_evidence_present'] else ('REJECT_REGRESSION' if not a['regression_pass'] else 'ELIGIBLE_FOR_EXTERNAL_PROMOTION_REVIEW'))
        else: got='COHERENT_WITH_OBSERVATION' if a['prediction']==a['observation'] else 'MISMATCH_PRESERVED_REALITY_PRIORITY'
        cres.append({'id':cid,'expected':c['expected'],'observed':got,'pass':got==c['expected']})
    add(rows,'static_reference_corpus_10_10',len(cres)==10 and all(x['pass'] for x in cres),cres)
    golden=(T/'EXPECTED_STDOUT_UTF8.txt').read_bytes(); add(rows,'utf8_golden_literal',b'B\xc3\x80I 001 \xe2\x80\x94 \xc4\x90\xe1\xbb\x98 CH\xc3\x8dNH X\xc3\x81C' in raw)
    add(rows,'expected_stdout_utf8',golden.decode('utf-8','strict').encode('utf-8')==golden,h(golden))
    add(rows,'hostvm_contract','sigma-hostvm' in (R/'EVIDENCE_CONTRACT.json').read_text(encoding='utf-8'))
    fail=sum(not x['pass'] for x in rows); status='PASS_STRUCTURAL_ONLY_NOT_COMPILE_EVIDENCE' if not fail else 'FAIL_STRUCTURAL_VALIDATION'
    rep={'schema_version':'1.0.0','evidence_id':'SIGMA-NATIVE-BRAIN-54X512-v0.1-STATIC-VALIDATION','recorded_at':datetime.now(timezone.utc).isoformat(),'status':status,'scope':'STATIC_STRUCTURE_UTF8_CONTRACT_ONLY','counts':{'checks':len(rows),'pass':len(rows)-fail,'fail':fail},'artifacts':{'source_sha256':h(raw),'source_bytes':len(raw),'source_lines':len(src.splitlines()),'expected_stdout_sha256':h(golden)},'checks':rows,'non_claims':['NOT_SIGMAC_COMPILE_EVIDENCE','NOT_SIGMA_HOSTVM_EXECUTION_EVIDENCE','NOT_512_BEHAVIORAL_IMPLEMENTATION_EVIDENCE','NOT_IMPROVEMENT_OR_PROMOTION_EVIDENCE'],'decision':'HOLD_PENDING_SIGMAC_AND_SIGMA_HOSTVM_MACHINE_EXECUTION'}
    REPORT.write_text(json.dumps(rep,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(json.dumps({'status':status,'counts':rep['counts'],'source_sha256':h(raw)},ensure_ascii=False)); return 1 if fail else 0
if __name__=='__main__': raise SystemExit(main())
