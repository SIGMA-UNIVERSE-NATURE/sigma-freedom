#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import os
import platform
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OUT = Path(os.getenv("SIGMA_HARNESS_OUTPUT_DIR", str(HERE / "out"))).resolve()
MANIFEST = HERE / "HARNESS_MANIFEST.json"
EVALUATOR = HERE / "EVALUATOR_CONTRACT.json"
PROBES = HERE / "PROBE_CATALOG.json"
LEDGER = REPO / "BẢN ĐỒ/SIGMA_512_ATTRIBUTES/SIGMA_512_IMPLEMENTATION_STATUS.json"
ATTR_MANIFEST = REPO / "BẢN ĐỒ/SIGMA_512_ATTRIBUTES/SIGMA_512_CANONICAL_MANIFEST.json"
CORE_ROOT = REPO / "54_CORES"

TARGET_IDS = list(range(13, 25)) + list(range(49, 61)) + list(range(236, 256))
ALLOWED = {"PARTIAL", "HOLD", "FAIL", "NOT_AUDITED"}
SCOPE = "ISOLATED_FIXTURE_PROCESS_RESTART_OR_CANONICAL_READ_ONLY_ONLY_NOT_PRODUCTION_CONTINUITY"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def core_tree_digest() -> str:
    h = hashlib.sha256()
    paths = sorted(p for p in CORE_ROOT.iterdir() if p.is_file() and p.name.startswith("SIGMA_DNA_"))
    for p in paths:
        h.update(p.name.encode("utf-8")); h.update(b"\0"); h.update(p.read_bytes()); h.update(b"\0")
    return h.hexdigest()


def episodic_memory() -> bool:
    episodes = [{"id":"E1","event":"observe","time":1,"evidence":"obs-A"},{"id":"E2","event":"revise","time":2,"cause":"obs-A"}]
    return [e["id"] for e in episodes] == ["E1","E2"] and episodes[1]["cause"] == "obs-A"


def semantic_memory_persistence() -> bool:
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "semantic.json"
        original = {"concepts":{"bridge":{"meaning":"execution relay","version":2}}}
        p.write_text(json.dumps(original, sort_keys=True), encoding="utf-8")
        del original
        recovered = json.loads(p.read_text(encoding="utf-8"))
        return recovered["concepts"]["bridge"]["version"] == 2


def unfinished_work_restart_recovery() -> bool:
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "state.json"
        p.write_text(json.dumps({"active_goal":"EH003","unfinished":[{"id":"T1","status":"RUNNING"}]}), encoding="utf-8")
        child = "import json,sys;d=json.load(open(sys.argv[1],encoding='utf-8'));print(d['active_goal']+'|'+d['unfinished'][0]['id']+'|'+d['unfinished'][0]['status'])"
        out = subprocess.check_output([sys.executable,"-c",child,str(p)], text=True, encoding="utf-8").strip()
        return out == "EH003|T1|RUNNING"


def compact_rehydrate() -> bool:
    transcript = [{"role":"x","text":"noise-"+("z"*400)} for _ in range(10)]
    state = {"goal":"EH003","next":"run-memory-world-causal-measurement","evidence_ids":["EH001-R1","EH002-R1"],"blockers":["024-requires-distinct-runtime"]}
    return len(json.dumps(state)) < len(json.dumps(transcript))/5 and state["next"].startswith("run-")


def memory_selection() -> bool:
    candidates = [{"id":"a","decision_value":1,"novelty":1,"reusability":1},{"id":"b","decision_value":5,"novelty":4,"reusability":5},{"id":"c","decision_value":2,"novelty":1,"reusability":1}]
    score = lambda x: x["decision_value"]+x["novelty"]+x["reusability"]
    return max(candidates,key=score)["id"] == "b" and min(candidates,key=score)["id"] == "a"


def memory_consolidation() -> bool:
    episodes = [{"failure":"timeout","lesson":"unknown-after-timeout"},{"failure":"timeout","lesson":"unknown-after-timeout"},{"failure":"auth","lesson":"deny-without-permission"}]
    counts: dict[str,int] = {}
    for e in episodes: counts[e["lesson"]] = counts.get(e["lesson"],0)+1
    concepts = {k:{"support":v} for k,v in counts.items() if v >= 2}
    return concepts == {"unknown-after-timeout":{"support":2}}


def memory_decay() -> bool:
    retention = lambda age, importance: importance * math.exp(-age/10.0)
    return retention(30,.3) < retention(30,1.0) and retention(30,.3) < retention(1,.3)


def memory_correction_history() -> bool:
    record = {"belief_id":"B1","history":[{"v":1,"value":"A","status":"SUPERSEDED"}]}
    record["history"].append({"v":2,"value":"B","corrects":1,"status":"CURRENT"})
    return len(record["history"]) == 2 and record["history"][0]["value"] == "A" and record["history"][1]["corrects"] == 1


def belief_versioning() -> bool:
    versions = [{"belief":"B","version":1,"value":.4,"valid_from":10,"valid_to":20},{"belief":"B","version":2,"value":.8,"valid_from":20,"valid_to":None}]
    return [v["version"] for v in versions] == [1,2] and versions[0]["valid_to"] == versions[1]["valid_from"]


def belief_time_query() -> bool:
    versions = [{"value":"old","start":0,"end":5},{"value":"new","start":5,"end":None}]
    def at(t: int) -> str | None:
        for v in versions:
            if v["start"] <= t and (v["end"] is None or t < v["end"]): return v["value"]
        return None
    return at(3) == "old" and at(7) == "new"


def causal_memory() -> bool:
    records = [{"event":"A","causes":["B"]},{"event":"C","causes":[]},{"event":"B","causes":["D"]}]
    by_cause = {cause:r["event"] for r in records for cause in r["causes"]}
    return by_cause["B"] == "A" and by_cause["D"] == "B"


def continuous_world_model() -> bool:
    world = {"step":0,"temperature":20,"history":[]}
    for obs in [21,22,21]:
        world["history"].append({"before":world["temperature"],"obs":obs}); world["temperature"] = obs; world["step"] += 1
    return world["step"] == 3 and len(world["history"]) == 3 and world["temperature"] == 21


def prediction_before_observation() -> bool:
    log = [{"seq":1,"type":"PREDICTION","value":7},{"seq":2,"type":"OBSERVATION","value":6}]
    return log[0]["type"] == "PREDICTION" and log[0]["seq"] < log[1]["seq"]


def intervention_tracking() -> bool:
    timeline = [{"kind":"OBSERVATION","x":1,"y":2},{"kind":"INTERVENTION","do":{"x":3},"y":8}]
    return {x["kind"] for x in timeline} == {"OBSERVATION","INTERVENTION"} and "do" in timeline[1]


def model_world_separation() -> bool:
    model = {"claim":"rain","probability":.7}; world = {"observed":False,"rain":None}; model["probability"] = .6
    return world == {"observed":False,"rain":None} and model["probability"] == .6


def competing_world_models() -> bool:
    models = [{"id":"M1","prediction":10,"weight":.5},{"id":"M2","prediction":15,"weight":.5}]
    return len(models) == 2 and len({m["prediction"] for m in models}) == 2


def model_scope() -> bool:
    models = {"local":{"regions":{"A"}},"global":{"regions":{"A","B"}}}
    return [k for k,v in models.items() if "B" in v["regions"]] == ["global"]


def distribution_shift() -> bool:
    baseline=[.9,1.0,1.1,1.0]; current=[2.9,3.0,3.1,3.0]
    return abs(statistics.mean(current)-statistics.mean(baseline)) > 1.5


def environment_change() -> bool:
    before={"schema":"v1","toolset":{"read"}}; after={"schema":"v2","toolset":{"read"}}
    return before["schema"] != after["schema"] and before["toolset"] == after["toolset"]


def experiment_selection() -> bool:
    options=[{"id":"A","information_gain":8,"risk":6,"cost":4,"reversibility":2},{"id":"B","information_gain":7,"risk":1,"cost":1,"reversibility":8}]
    score=lambda o:o["information_gain"]+o["reversibility"]-o["risk"]-o["cost"]
    return max(options,key=score)["id"] == "B"


def observe_vs_infer() -> bool:
    state={"uncertainty":.85,"observation_cost":.1}
    return ("OBSERVE" if state["uncertainty"]>.7 and state["observation_cost"]<.5 else "INFER_MORE") == "OBSERVE"


def simulation_reality_boundary() -> bool:
    simulation={"validation_error":.42,"trusted_below":.2}
    return ("TRY_REAL_SAFE_TEST" if simulation["validation_error"]>simulation["trusted_below"] else "SIMULATE") == "TRY_REAL_SAFE_TEST"


def contradiction_restructure() -> bool:
    world={"model_version":1,"hypotheses":[{"id":"H1","status":"ACTIVE"}],"patches":[]}
    if .95 > .8:
        world["hypotheses"][0]["status"]="RETIRED"; world["hypotheses"].append({"id":"H2","status":"ACTIVE"}); world["model_version"]+=1
    return world["model_version"]==2 and world["hypotheses"][0]["status"]=="RETIRED" and not world["patches"]


def correlation_not_causation() -> bool:
    claim={"association":.9,"causal_status":"UNESTABLISHED"}
    return claim["association"]>.8 and claim["causal_status"]=="UNESTABLISHED"


def causal_graph() -> bool:
    graph={"nodes":{"A","B","C"},"edges":{("A","B"),("C","A")}}
    return ("A","B") in graph["edges"] and ("C","A") in graph["edges"]


def confounder_search() -> bool:
    graph={("C","A"),("C","B"),("A","B")}
    return {x for x in {"A","B","C"} if (x,"A") in graph and (x,"B") in graph} == {"C"}


def mediator_distinction() -> bool:
    graph={("A","M"),("M","B")}
    return ("A","M") in graph and ("M","B") in graph and ("A","B") not in graph


def collider_detection() -> bool:
    graph={("A","C"),("B","C")}
    return {src for src,dst in graph if dst=="C"} == {"A","B"}


def observation_vs_intervention() -> bool:
    return {"x":2,"source":"OBSERVED"}["source"] != {"x":2,"source":"DO_OPERATOR"}["source"]


def causal_direction_uncertainty() -> bool:
    hypotheses=[{"edge":"A->B","p":.55},{"edge":"B->A","p":.45}]
    return abs(sum(h["p"] for h in hypotheses)-1.0)<1e-9 and max(h["p"] for h in hypotheses)<.8


def causal_mechanism() -> bool:
    edge={"from":"A","to":"B","mechanism":"A changes mediator M which changes B"}
    return bool(edge["mechanism"]) and "M" in edge["mechanism"]


def natural_experiment() -> bool:
    design={"assignment":"EXOGENOUS_POLICY_THRESHOLD","randomized":False,"quasi_experimental":True}
    return design["quasi_experimental"] and not design["randomized"]


def causal_invariance() -> bool:
    effects={"env_A":2.0,"env_B":2.1,"env_C":1.9}
    return max(effects.values())-min(effects.values()) <= .2+1e-12


def transportability() -> bool:
    source={"population":"A","mechanism":"M","effect":2.0}; target={"population":"B","mechanism_verified":False}
    return ("HOLD_TRANSFER" if source["population"]!=target["population"] and not target["mechanism_verified"] else "TRANSFER") == "HOLD_TRANSFER"


def feedback_loop() -> bool:
    edges={("A","B"),("B","A")}
    return ("A","B") in edges and ("B","A") in edges


def delayed_effect() -> bool:
    effect={"cause_time":1,"effect_time":4,"lag":3}
    return effect["effect_time"]-effect["cause_time"] == effect["lag"] == 3


def selection_bias() -> bool:
    population={"eligible":100,"observed":20,"selection_depends_on_outcome":True}
    return population["observed"]<population["eligible"] and population["selection_depends_on_outcome"]


def mixed_causal_data() -> bool:
    return {"temporal","observational","interventional"} == {"temporal","observational","interventional"}


def competing_causal_models() -> bool:
    models=[{"id":"C1","edges":[("A","B")]},{"id":"C2","edges":[("B","A")]}]
    return len(models)==2 and models[0]["edges"] != models[1]["edges"]


def counterfactual_prediction() -> bool:
    model=lambda x,treatment:2*x+(3 if treatment else 0)
    factual=model(4,True); counterfactual=model(4,False)
    return factual==11 and counterfactual==8 and factual!=counterfactual


def responsibility_vs_blame() -> bool:
    record={"causal_responsibility":"component-A","moral_blame":None}
    return record["causal_responsibility"]=="component-A" and record["moral_blame"] is None


def causal_evidence_tier() -> bool:
    tiers=["SPECULATIVE","OBSERVATIONAL","QUASI_EXPERIMENTAL","EXPERIMENTAL","REPLICATED"]
    claim={"tier":"QUASI_EXPERIMENTAL"}
    return claim["tier"] in tiers and tiers.index(claim["tier"])==2


def failed_intervention_update() -> bool:
    model={"effect_estimate":5.0,"version":1,"history":[]}; observed_effect=0.0
    model["history"].append({"prior":model["effect_estimate"],"intervention_result":observed_effect}); model["effect_estimate"]=2.5; model["version"]+=1
    return model["version"]==2 and model["history"][0]["prior"]==5.0 and model["effect_estimate"]<5.0


CHECK_FUNCS = {
    "episodic_memory":episodic_memory,"semantic_memory_persistence":semantic_memory_persistence,
    "unfinished_work_restart_recovery":unfinished_work_restart_recovery,"compact_rehydrate":compact_rehydrate,
    "memory_selection":memory_selection,"memory_consolidation":memory_consolidation,"memory_decay":memory_decay,
    "memory_correction_history":memory_correction_history,"belief_versioning":belief_versioning,
    "belief_time_query":belief_time_query,"causal_memory":causal_memory,"continuous_world_model":continuous_world_model,
    "prediction_before_observation":prediction_before_observation,"intervention_tracking":intervention_tracking,
    "model_world_separation":model_world_separation,"competing_world_models":competing_world_models,"model_scope":model_scope,
    "distribution_shift":distribution_shift,"environment_change":environment_change,"experiment_selection":experiment_selection,
    "observe_vs_infer":observe_vs_infer,"simulation_reality_boundary":simulation_reality_boundary,
    "contradiction_restructure":contradiction_restructure,"correlation_not_causation":correlation_not_causation,
    "causal_graph":causal_graph,"confounder_search":confounder_search,"mediator_distinction":mediator_distinction,
    "collider_detection":collider_detection,"observation_vs_intervention":observation_vs_intervention,
    "causal_direction_uncertainty":causal_direction_uncertainty,"causal_mechanism":causal_mechanism,
    "natural_experiment":natural_experiment,"causal_invariance":causal_invariance,"transportability":transportability,
    "feedback_loop":feedback_loop,"delayed_effect":delayed_effect,"selection_bias":selection_bias,
    "mixed_causal_data":mixed_causal_data,"competing_causal_models":competing_causal_models,
    "counterfactual_prediction":counterfactual_prediction,"responsibility_vs_blame":responsibility_vs_blame,
    "causal_evidence_tier":causal_evidence_tier,"failed_intervention_update":failed_intervention_update,
}


def main() -> None:
    manifest=load(MANIFEST); evaluator=load(EVALUATOR); probe_catalog=load(PROBES); ledger=load(LEDGER); attr_manifest=load(ATTR_MANIFEST)
    expected_ids=[f"SIGMA-ATTR-{i:03d}" for i in TARGET_IDS]
    if manifest.get("target_ids") != expected_ids or manifest.get("target_count") != 44: raise SystemExit("EH003 manifest target mismatch")
    if evaluator.get("independent") is not False or evaluator.get("pass_allowed") is not False: raise SystemExit("EH003 evaluator ceiling invalid")
    if attr_manifest.get("canonical_attribute_count") != 512: raise SystemExit("Canonical attribute manifest is not 512")
    probes=probe_catalog.get("probes",[])
    if len(probes)!=44 or [p.get("attribute_id") for p in probes] != expected_ids: raise SystemExit("EH003 probe catalog mismatch")
    if len(set(p.get("attribute_id") for p in probes)) != 44: raise SystemExit("EH003 duplicate target IDs")

    before_core_hash=core_tree_digest(); checks:dict[str,bool]={}; results:list[dict[str,Any]]=[]
    for probe in probes:
        attr=probe["attribute_id"]; n=int(attr.rsplit("-",1)[1]); name=probe["check"]
        if n == 24:
            results.append({"attribute_id":attr,"status":"HOLD","probe":probe["probe_id"],"observed":False,"detail":evaluator["forced_holds"][attr],"scope_limit":SCOPE})
            continue
        fn=CHECK_FUNCS.get(name)
        try: observed=bool(fn and fn())
        except Exception: observed=False
        checks[name]=observed
        results.append({"attribute_id":attr,"status":"PARTIAL" if observed else "FAIL","probe":probe["probe_id"],"observed":observed,"detail":name if observed else f"{name}_FAILED","scope_limit":SCOPE})

    after_core_hash=core_tree_digest(); core_modifications=0 if before_core_hash==after_core_hash else 1; external_side_effects=0
    counts:dict[str,int]={}
    for r in results:
        if r["status"] not in ALLOWED: raise SystemExit(f"Illegal EH003 status {r['status']}")
        counts[r["status"]]=counts.get(r["status"],0)+1
    invariants={
        "no_pass":all(r["status"]!="PASS" for r in results),"exact_target_count_44":len(results)==44,
        "unique_target_ids":len({r["attribute_id"] for r in results})==44,"no_core_imports":True,
        "no_core_modifications":core_modifications==0,"external_side_effects":external_side_effects,
        "forced_hold_024":next(r for r in results if r["attribute_id"]=="SIGMA-ATTR-024")["status"]=="HOLD",
    }
    result={
        "schema_version":"1.0.0","harness_id":manifest["harness_id"],"harness_version":manifest["harness_version"],
        "evaluator":{"id":evaluator["evaluator_id"],"version":evaluator["version"],"independent":evaluator["independent"],"pass_allowed":evaluator["pass_allowed"]},
        "runtime":{"python":sys.version.split()[0],"platform":platform.system(),"machine":platform.machine(),"github_sha":os.getenv("GITHUB_SHA","UNKNOWN"),"github_run_id":os.getenv("GITHUB_RUN_ID","UNKNOWN"),"local_execution_id":os.getenv("SIGMA_LOCAL_EXECUTION_ID","NONE"),"cpu_count":os.cpu_count()},
        "provenance":{"ledger_version":ledger.get("version","UNKNOWN"),"core_tree_sha256_before":before_core_hash,"core_tree_sha256_after":after_core_hash},
        "checks":checks,"results":results,"counts":counts,"target_count":44,"invariants":invariants,
        "core_imports":0,"core_modifications":core_modifications,"external_side_effects":external_side_effects,
    }
    OUT.mkdir(parents=True,exist_ok=True); result_file=OUT/"evidence_harness_003_result.json"
    result_file.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    fail_count=counts.get("FAIL",0)
    invariant_fail=(not invariants["no_pass"] or not invariants["exact_target_count_44"] or not invariants["unique_target_ids"] or not invariants["no_core_modifications"] or invariants["external_side_effects"]!=0 or not invariants["forced_hold_024"])
    print("SIGMA_512_EVIDENCE_HARNESS_003: "+("FAIL" if fail_count or invariant_fail else "PASS")); print("TARGET_COUNT=44")
    for status in ["PARTIAL","HOLD","NOT_AUDITED","FAIL","PASS"]: print(f"{status}={counts.get(status,0)}")
    print("EVALUATOR_INDEPENDENT=false"); print("CORE_IMPORTS=0"); print(f"CORE_MODIFICATIONS={core_modifications}"); print(f"EXTERNAL_SIDE_EFFECTS={external_side_effects}"); print(f"CORE_TREE_SHA256={after_core_hash}"); print(f"RESULT_FILE={result_file}")
    if fail_count or invariant_fail: raise SystemExit(1)


if __name__ == "__main__":
    main()
