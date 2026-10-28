#!/usr/bin/env python3
"""V1 acceptance on the frozen Season Pass runs (read-only): message-level model provenance through the one owner
(difficulty_stats.model_provenance via trajectory_ledger.provenance).

  default expected model (the task context's baseline_model, claude-opus-5-5): all five revision-14 runs v3-invalid
  --expected-model claude-opus-4-8: pre, r1, r2, r6 mixed; r3 unmixed (and the only run valid for 4.8)
  audit L4: the revision-13 pre-check (fallback at event 5855, final summary only) with the fallback event removed
            is still flagged by its Opus 5 message(s)
  the six-run model gate (difficulty_stats.model_gate) fails the revision-14 runs: Opus 4.8 is never V3 evidence
"""
import sys
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(BUNDLE / "tools"))
import difficulty_stats as ds  # noqa: E402
import trajectory_ledger as tl  # noqa: E402

S = BUNDLE / "support" / "backtests" / "season_pass"
RUNS = [("pre", S / "rev14/runs/06_PreCheck_Trajectory/trajectory-run-1.json")] + \
       [(f"r{i}", S / f"rev14/runs/07_Baseline_Trajectories/trajectory-run-{i}.json") for i in (1, 2, 3, 6)]
WANT_MIXED = {"pre": True, "r1": True, "r2": True, "r3": False, "r6": True}


def main():
    ok = True
    expected = tl.expected_model_for(S / "rev14")
    print(f"default expected model (rev14 working_files/00_Task_Context.json baseline_model): {expected}")
    for lab, path in RUNS:
        run = tl.load(path, lab)
        d = tl.provenance(run, expected_model=expected)["model_check"]
        e48 = tl.provenance(run, expected_model="claude-opus-4-8")["model_check"]
        good = (d["v3_valid"] is False and d["mixed_model"] == WANT_MIXED[lab] and e48["mixed_model"] == WANT_MIXED[lab]
                and e48["valid"] == ("VALID" if lab == "r3" else "INVALID"))
        ok = ok and good
        print(f"{'ok  ' if good else 'FAIL'} {lab}: models {d['models']} · default: v3_valid {d['v3_valid']} "
              f"({d['v3_verdict']}) · mixed {d['mixed_model']} · expected 4.8: {e48['valid']} · synthetic "
              f"{d['synthetic_messages']} · fallback events {d['fallback_events']}")
        for o in e48["off_model"]:
            print(f"       off 4.8: {o['label']} · {o['source']}" + (f" ({o['subagent_briefs']} brief(s))" if
                  o["source"] == "subagent" else "") + f" · {o['count']} message(s), events {o['first_event']}-"
                  f"{o['last_event']} · after fallback event {o['after_fallback_event']}")
    gate = ds.model_gate([{"id": lab, "models": ds.trajectory_models(p), "model_source": f"trajectory:{p.name}"}
                          for lab, p in RUNS])
    ok = ok and gate["verdict"].startswith("FAIL")
    print(f"{'ok  ' if gate['verdict'].startswith('FAIL') else 'FAIL'} model gate on the five rev14 runs: "
          f"{gate['verdict']} - {gate['value'][:160]}")
    # audit L4: drop the fallback event; the Opus 5 message(s) still flag the run
    pre13 = tl.load(S / "rev13/runs/06_PreCheck_Trajectory/trajectory-run-1.json", "pre13")
    kept = [e for e in pre13.events if not (isinstance(e, dict) and e.get("subtype") == "model_refusal_fallback")]
    with_fb = ds.model_provenance(pre13.events, "claude-opus-4-8")
    no_fb = ds.model_provenance(kept, "claude-opus-4-8")
    good = (len(pre13.events) - len(kept) == 1 and no_fb["mixed_model"] and no_fb["valid"] == "INVALID"
            and all(o["after_fallback_event"] is None for o in no_fb["off_model"]))
    ok = ok and good
    print(f"{'ok  ' if good else 'FAIL'} L4 rev13 pre-check: with the fallback event {with_fb['fallback_events']}: mixed "
          f"{with_fb['mixed_model']}, off {[(o['label'], o['source'], o['count'], o['after_fallback_event']) for o in with_fb['off_model']]}; "
          f"fallback event removed: mixed {no_fb['mixed_model']}, valid {no_fb['valid']}, off "
          f"{[(o['label'], o['source'], o['count']) for o in no_fb['off_model']]}")
    # a synthetic Opus 5.5 run (in memory): bracketed labels, harness <synthetic> messages and an Opus 5.5 subagent
    def msg(model, parent=None):
        return {"type": "assistant", "parent_tool_use_id": parent, "message": {"model": model, "content": []}}
    events = [{"type": "system", "subtype": "init", "model": "claude-opus-5-5[1m]"}, msg("claude-opus-5-5[1m]"),
              msg("<synthetic>"), msg("claude-opus-5-5", "toolu_brief_1"), msg("claude-opus-5-5[1m]"),
              {"type": "result", "subtype": "success", "is_error": False}]
    syn = tl.Run("synthetic-5.5", Path("synthetic.json"), "stream-json", events, *tl.index_events(events))
    sp = tl.provenance(syn, expected_model=expected)
    good = sp["v3_valid"] is True and not sp["mixed_model"] and sp["model_check"]["synthetic_messages"] == 1
    ok = ok and good
    print(f"{'ok  ' if good else 'FAIL'} synthetic Opus 5.5 run: v3_valid {sp['v3_valid']} · mixed {sp['mixed_model']} · "
          f"models {sp['model_check']['models']} · synthetic {sp['model_check']['synthetic_messages']}")
    print("V1 ACCEPTANCE " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
