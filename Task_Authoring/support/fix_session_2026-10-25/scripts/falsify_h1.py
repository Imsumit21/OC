#!/usr/bin/env python3
"""H1 falsification: undo each H1 fix in memory, one at a time, and show that the self-test that plants it fails.

  node_verdicts     mechanism? (back to the old fallback: every in-cohort error goes to the rule), control trials,
                    deciders (who decided), the go rule's model and independence checks, landed-key comparison,
                    surface-only rules kept out of the proposals; slips that a channel or control already explains;
                    channel and control matching on any column (a class cascade)
  hardness_ledger   the control / channel kinds, the pending-review refusal; H2's design effect over weighted trials
  hardness_forecast F1's channel rates matched by channel id (never pooled across tasks)
  trajectory_ledger a revision-14 surface read raw (briefs without key lists)
  difficulty_mutation keyless briefs accepted as empty batches (M6)
  oracle_kit        the live-controls contract check
It runs inside a selftest_sandbox workspace (it re-runs itself there): oracle_kit's self-test reads base records
through tools/hg.py, whose caches must stay out of the shared folder. Control: nothing undone, every self-test passes.
"""
import contextlib
import io
import json
import sys
from pathlib import Path

def _bundle() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "difficulty_stats.py").is_file():
            return parent
    raise SystemExit("falsify_h1: no Task_Authoring bundle above this script")


BUNDLE = _bundle()
sys.path.insert(0, str(BUNDLE / "tools"))
import selftest_sandbox as sx  # noqa: E402

if __name__ == "__main__" and not sx.in_sandbox(BUNDLE):       # re-run inside a sandbox, from its tools/
    import shutil
    with sx.Sandbox("live") as _sb:
        shutil.copy2(__file__, _sb.bundle / "tools" / "_falsify_h1.py")
        _rc = _sb.run(["_falsify_h1.py"] + sys.argv[1:])
    raise SystemExit(_rc)
import difficulty_mutation as dm  # noqa: E402
import hardness_forecast as hf  # noqa: E402
import hardness_ledger as hl  # noqa: E402
import node_verdicts as nv  # noqa: E402
import oracle_kit as ok  # noqa: E402
import trajectory_ledger as tl  # noqa: E402


def old_classify(classify):                       # the fallback `won = reproduced or candidates`
    def f(*args, **kw):
        items = classify(*args, **kw)
        rules = args[4]
        for d in items:
            if d["classification"] == "mechanism?":
                parents = nv._parents(rules, d["candidates"])
                d["classification"] = "mechanism" if len(parents) == 1 else "mechanism (ambiguous)"
                d["attributed"] = parents
        return items
    return f


def old_go_rule(out_rules, channels, controls, items, prov, expected, rules):   # every landing and failure counts
    names = [f"mechanism {r}" for r, v in out_rules.items() if v["verdict"] == "LANDED"] + \
            [f"channel {c}" for c, v in channels.items() if v["verdict"] == "FAILED"]
    return {"expected_model": expected, "independent_channels": len(names), "channels": [[n] for n in names],
            "not_counted": {"off_model_or_unregistered": [], "control_over_applications": [], "slips": [],
                            "pending_review": []}, "run_valid": prov.get("v3_valid")}


def items_only(compare):                          # the old compare: items, never landed-key sets
    return lambda *a, **kw: [d for d in compare(*a, **kw) if d.get("kind") != "landed_keys"]


def proposing_everything(proposals):              # surface-only rules proposed like the rest
    def f(report, **kw):
        out = proposals(report, **kw)
        for lab, r in report["runs"].items():
            for rule, v in r["rules"].items():
                if v["verdict"] == "SURFACE-ONLY":
                    out.append({"kind": "verdict", "run": lab, "node": rule, "verdict": "FALSE"})
        return out
    return f


def slips_unfiltered(go_rule):                    # slips listed again when a channel or control explains them
    def f(out_rules, channels, controls, items, prov, expected, rules):
        g = go_rule(out_rules, channels, controls, items, prov, expected, rules)
        g["not_counted"]["slips"] = sorted({d["key"] for d in items if d["classification"] == "slip"})
        return g
    return f


def _any_column(row, truth, dg, fields, tspec) -> bool:
    """The first rule: some column differs from the truth and matches the operator's value (a class cascade counts)."""
    return any(f in row and dg.get(f) != truth.get(f) and nv.sg.compare(row[f], truth.get(f), f, tspec) != "MATCH"
               and nv.sg.compare(row[f], dg.get(f), f, tspec) == "MATCH" for f in fields)


def any_column_channels(channel_reports):         # channel members matched on any column
    def f(view, channels, rows, truth, *, mod, state, tspec, table_events, graded=None, class_field="class",
          key_events=None, deciders=None, slot_targets=None):
        out = channel_reports(view, channels, rows, truth, mod=mod, state=state, tspec=tspec,
                              table_events=table_events, graded=graded, class_field=class_field,
                              key_events=key_events, deciders=deciders, slot_targets=slot_targets)
        cols = [c for c in tspec.get("columns") or [] if c not in (tspec.get("key_column"), tspec.get("reason_column"))]
        for cid, c in channels.items():
            if c.get("degrade") and out[cid]["verdict"] != "UNOBSERVED":
                dg = mod.solve(state, degrade={c["degrade"]})
                hit = [{"key": k} for k in c.get("members") or [] if k in rows and k in truth
                       and _any_column(rows[k], truth[k], dg[k], cols, tspec)]
                out[cid].update(verdict="FAILED" if hit else "HELD", failed_members=hit)
        return out
    return f


def any_column_controls(control_trials):          # control trials matched on any column
    def f(view, rules, controls, rows, truth, *, mod, state, tspec, class_field, table_events, key_events=None):
        out = control_trials(view, rules, controls, rows, truth, mod=mod, state=state, tspec=tspec,
                             class_field=class_field, table_events=table_events, key_events=key_events)
        for r, c in controls.items():
            if not c["over_application"]:
                continue
            dg = mod.solve(state, degrade={c["over_application"]})
            fields = [x for x in list(rules[r].get("decides") or []) + [class_field] if x in (tspec.get("columns") or [])]
            for x in out[r]["trials"]:
                k = x["key"]
                if x["outcome"] != "NOT-WRITTEN" and _any_column(rows[k], truth[k], dg[k], fields, tspec):
                    x["outcome"] = "OVER-APPLIED"
            out[r]["over_applied"] = [x["key"] for x in out[r]["trials"] if x["outcome"] == "OVER-APPLIED"]
            out[r]["held"] = [x["key"] for x in out[r]["trials"] if x["outcome"] == "HELD"]
        return out
    return f


def old_seeded_landings(ledger_path, task):       # raw lines, (run, node) only: no supersession, no revision
    out = {}
    for line in Path(ledger_path).read_text().splitlines():
        if not line.strip():
            continue
        x = json.loads(line)
        if x.get("kind") == "verdict" and x.get("task") == task and x.get("verdict") == "LANDED":
            out[(x.get("run"), x.get("node"))] = (x["id"], list(x.get("keys") or []))
    return out


def ignoring_key_events(decider):                 # H1-5 undone: the last table write bounds every key
    def f(view, key, table_events, key_events=None):
        return decider(view, key, table_events, None)
    return f


def ignoring_unknown(go_rule):                    # H1-4 undone: an unknown deciding model is not counted
    def f(out_rules, channels, controls, items, prov, expected, rules):
        return go_rule({r: dict(v, unknown_decisions=0) for r, v in out_rules.items()},
                       {c: dict(v, unknown_decisions=0) for c, v in channels.items()},
                       controls, items, prov, expected, rules)
    return f


def unobserved_as_held(control_trials):           # H1-6 undone: an unreadable own field becomes a held trial
    def f(*a, **kw):
        out = control_trials(*a, **kw)
        for c in out.values():
            for x in c["trials"]:
                if x["outcome"] == "UNOBSERVED":
                    x["outcome"] = "HELD"
        return out
    return f


def no_slot_provenance(channel_reports):          # H1-7 undone: a slots-only channel carries no deciding model/event
    def f(*a, **kw):
        out = channel_reports(*a, **kw)
        for v in out.values():
            if v.get("members") == 0 and v["verdict"] != "UNOBSERVED":
                v["deciding_models"], v["deciding_event"] = [], None
        return out
    return f


def naive_class(classify):                        # H1-9 undone: any reproduced class is attributed
    def f(*a, **kw):
        items = classify(*a, **kw)
        cf = a[6]
        for d in items:
            if d["field"] == cf and d["classification"] == "cascade":
                d["classification"] = "mechanism"
        return items
    return f


def _exec_ledger(replace):
    path = BUNDLE / "tools" / "hardness_ledger.py"
    src = path.read_text()
    for old, new in replace:
        assert src.count(old) == 1, f"anchor moved: {old[:50]}"
        src = src.replace(old, new)
    ns = {"__name__": "hardness_ledger_undo", "__file__": str(path)}
    exec(compile(src, str(path), "exec"), ns)
    return ns["priors"]


def old_observation_priors():                    # H1-2 undone: every observation record's outcomes summed
    return _exec_ledger([('T = int(max(o["counted"] for o in os_))', 'T = int(sum(o["counted"] for o in os_))'),
                         ('L = int(max(o["landed"] for o in os_))', 'L = int(sum(o["landed"] for o in os_))')])


def unvalidated_rho():                            # H1-3 undone: rho is not checked
    return _exec_ledger([('    if not isinstance(rho, (int, float)) or not math.isfinite(rho) or not 0 <= rho <= 1:\n'
                          '        raise ValueError(f"rho must be a finite correlation in [0, 1], got {rho!r}")\n', '')])


def run_only_rate(rate):                          # F1-1 undone: the run key drops the revision
    def f(recs, rho, unit="member"):
        return rate([(x[0], "", x[2], x[3], x[4], x[5]) for x in recs], rho, unit)
    return f


def no_channel_guard(*a, **kw):                   # F1-2 undone: a channel op is accepted as a mechanism
    return None


def weighted_deff_priors():                       # H2's first version: the design effect over weighted trials
    path = BUNDLE / "tools" / "hardness_ledger.py"
    src, fixed = path.read_text(), 'deff = design_effect(x["trials"], rho)'
    assert src.count(fixed) == 1, "the H2 anchor moved"
    ns = {"__name__": "hardness_ledger_weighted_deff", "__file__": str(path)}
    exec(compile(src.replace(fixed, "deff = design_effect(m, rho)"), str(path), "exec"), ns)
    return ns["priors"]


class _OnlyNode:
    """A ledger view holding one node's records: F1's first version matched rates by channel id (or rule id)."""

    def __init__(self, led, node):
        self.led, self.node = led, node

    def current(self):
        return [r for r in self.led.current() if r.get("node") == self.node]


def by_channel_id(channel_rate):                  # rates from the channel's own id only, never pooled across tasks
    def f(led, model, cid, kind, family, overrides, **kw):
        node = cid.split(":", 1)[1] if kind == "control" else cid
        return channel_rate(_OnlyNode(led, node), model, cid, kind, family, overrides, **kw)
    return f


def raw_surface_spec(path):                       # the CLI's first reader: raw JSON, no format conversion
    s = json.loads(Path(path).read_text())
    spec = next((v for v in (s.get("deliverables") or {}).values() if isinstance(v, dict) and v.get("kind") == "table"),
                None)
    return (dict(spec, classes=s.get("classes", [])) if spec else None), (spec or {}).get("key_regex")


def silent_shards_for(engine, briefs=None, size=dm.SHARD_SIZE):   # the first version: keyless briefs, no batches
    if briefs:
        seen, out = set(), []
        for b in briefs:
            ks = tuple(k for k in engine.keys if k in set(b.get("keys") or []))
            if ks and ks not in seen:
                seen.add(ks)
                out.append(list(ks))
        return out
    return [engine.keys[i:i + size] for i in range(0, len(engine.keys), size)]


def old_classify_no_controls(classify):           # control-explained items kept as slips / mechanisms
    def f(*args, **kw):
        kw.pop("explained", None)
        return classify(*args, **kw)
    return f


def held_keys_from_failed_members(ledger_proposals):   # the old HELD record set: failed members only (always empty)
    def f(*a, **kw):
        out = ledger_proposals(*a, **kw)
        for r in out:
            if r["kind"] == "channel" and r["verdict"] == "HELD":
                r["keys"] = []
        return out
    return f


def old_reference_landed(reference_landed):       # a reference item's own classification never vetoes a landing
    def f(ref_items, rules, class_field, legacy=None, context=None, unresolved=None):
        stripped = [{k: v for k, v in d.items() if k != "classification"} for d in ref_items]
        return reference_landed(stripped, rules, class_field, legacy, context=context, unresolved=unresolved)
    return f


def ignoring_slot_targets(go_rule):               # a slots-only channel counted although a control explains its target
    def f(out_rules, channels, controls, items, prov, expected, rules):
        return go_rule(out_rules, {cid: {k: v for k, v in c.items() if k != "failed_slot_targets"}
                                   for cid, c in channels.items()}, controls, items, prov, expected, rules)
    return f


def priors_without_control_gate(priors):          # a control-explained LANDED verdict enters the priors again
    def f(led, model, **kw):
        for r in led.records:
            if isinstance(r.get("features"), dict):
                r["features"].pop("control_explained", None)
        return priors(led, model, **kw)
    return f


def subset_slot_targets(go_rule):                 # the subset defect: only the mapped slots are treated as the channel
    def f(out_rules, channels, controls, items, prov, expected, rules):
        ch = {}
        for cid, c in channels.items():
            if c.get("failed_slot_targets") and not c.get("failed_members"):
                ch[cid] = dict(c, failed_slots=[t["slot"] for t in c["failed_slot_targets"]])
            else:
                ch[cid] = c
        return go_rule(out_rules, ch, controls, items, prov, expected, rules)
    return f


def stale_slot_provenance(go_rule):               # targets and slots kept, but the residual models/unknown not recomputed
    def f(out_rules, channels, controls, items, prov, expected, rules):
        ch = {cid: ({k: v for k, v in c.items() if k != "failed_slot_details"}
                    if c.get("failed_slot_details") else c) for cid, c in channels.items()}
        return go_rule(out_rules, ch, controls, items, prov, expected, rules)
    return f


def old_check_provenance(check):                  # the provenance requirement for control/channel records disabled
    def f(rec):
        if isinstance(rec, dict) and rec.get("kind") in ("control", "channel"):
            rec = dict(rec, evidence=dict(rec.get("evidence") or {}, covered={"members": 1}))
        return check(rec)
    return f


def blanket_control_exclusion(priors):           # a control tag removes a whole LANDING that also has an unexplained key
    def f(led, model, **kw):
        saved = list(led.records)
        keep = []
        for r in led.records:
            ce = set((r.get("features") or {}).get("control_explained") or [])
            if r.get("kind") == "verdict" and r.get("verdict") == "LANDED" and ce \
                    and set(r.get("keys") or []) - ce:
                continue                              # the over-broad rule; control-only records stay for the real gate
            keep.append(r)
        led.records = keep
        try:
            return priors(led, model, **kw)
        finally:
            led.records = saved
    return f


def old_proposal_slot_keys(ledger_proposals):     # a FAILED slot omitted from a channel proposal's record set
    def f(*a, **kw):
        out = ledger_proposals(*a, **kw)
        for r in out:
            if r["kind"] == "channel" and r["verdict"] == "FAILED":
                r["keys"] = [k for k in r["keys"] if not str(k).startswith("D")]
        return out
    return f


def details_only_provenance(channel_provenance):    # declared observed/held counts ignored (only detail objects count)
    def f(c):
        if c.get("verdict") == "FAILED" and (c.get("failed_members") or []):
            ms = c["failed_members"]
            return (sorted({m["deciding_model"] for m in ms if m.get("deciding_model")}),
                    sum(1 for m in ms if not m.get("deciding_model")))
        if c.get("verdict") == "FAILED":
            details, held = c.get("failed_slot_details") or [], c.get("held_members") or []
            if details or held or c.get("failed_slots"):
                models, unknown = set(), 0
                by = {d["slot"]: d for d in details if d.get("slot")}
                for s in (c.get("failed_slots") or []):
                    ms = set((by.get(s) or {}).get("models") or [])
                    models |= ms
                    unknown += 0 if ms else 1
                for m in held:
                    ms = set(m.get("models") or []) if "models" in m else (
                        {m["deciding_model"]} if m.get("deciding_model") else set())
                    models |= ms
                    unknown += 0 if ms else 1
                return sorted(models), unknown
            return sorted(set(c.get("deciding_models") or [])), int(c.get("unknown_decisions") or 0)
        models, unknown = set(), 0
        for m in c.get("held_members") or []:
            ms = set(m.get("models") or []) if "models" in m else (
                {m["deciding_model"]} if m.get("deciding_model") else set())
            models |= ms
            unknown += 0 if ms else 1
        return sorted(models), unknown
    return f


def aggregate_when_no_details(go_rule):          # a slot with no detail reuses the channel aggregate (known)
    def f(out_rules, channels, controls, items, prov, expected, rules):
        ch = {}
        for cid, c in channels.items():
            if not c.get("failed_members") and not (c.get("failed_slot_details") or []) and c.get("failed_slots"):
                # the old behaviour: a slot with no detail inherits the channel-wide aggregate as if it were its own
                ch[cid] = dict(c, failed_slot_details=[{"slot": s, "models": list(c.get("deciding_models") or [])}
                                                       for s in c["failed_slots"]], unknown_decisions=0)
            else:
                ch[cid] = c
        return go_rule(out_rules, ch, controls, items, prov, expected, rules)
    return f


def failed_only_models(channel_provenance):      # a FAILED member channel ignores its HELD observations' models
    def f(c):
        if c.get("verdict") == "FAILED" and (c.get("failed_members") or []):
            ms = c["failed_members"]
            return (sorted({m["deciding_model"] for m in ms if m.get("deciding_model")}),
                    sum(1 for m in ms if not m.get("deciding_model")))
        if c.get("verdict") == "FAILED" and (c.get("failed_slot_details") or c.get("held_members")):
            return sorted(set(c.get("deciding_models") or [])), int(c.get("unknown_decisions") or 0)
        return channel_provenance(c)
    return f


def member_events_only(ledger_proposals):        # proposal event from member copies only, ignoring the aggregate
    def f(*a, **kw):
        out = ledger_proposals(*a, **kw)
        for r in out:
            if r["kind"] == "channel":
                me = [m.get("deciding_event") for m in (r["evidence"].get("held_members") or [])
                      if m.get("deciding_event") is not None]
                if me:
                    r["evidence"]["deciding_event"] = max(me)
        return out
    return f


def truthy_unknown(check):                       # the explicit unknown flag accepted by truthiness (a string passes)
    def f(rec):
        if isinstance(rec, dict):
            fe = dict(rec.get("features") or {})
            if "deciding_model_unknown" in fe and fe["deciding_model_unknown"] is not True:
                fe["deciding_model_unknown"] = bool(fe["deciding_model_unknown"])
            rec = dict(rec, features=fe)
        return check(rec)
    return f


def fallback_by_emptiness(ledger_proposals):     # model_is_fallback = "no deciding models", not the selection branch
    def f(*a, **kw):
        out = ledger_proposals(*a, **kw)
        for r in out:
            if r["kind"] == "channel":
                r["features"]["model_is_fallback"] = not (r["features"].get("deciding_models") or [])
        return out
    return f


def covered_by_truthiness(check):                # any truthy evidence.covered passes, whatever it contains
    def f(rec):
        if isinstance(rec, dict):
            ev = dict(rec.get("evidence") or {})
            cov = ev.get("covered")
            if isinstance(cov, dict) and type(cov.get("members")) is not int:
                ev["covered"] = {"members": 1}
                rec = dict(rec, evidence=ev)
        return check(rec)
    return f


def channel_wide_events(channel_reports):        # HELD event selection channel-wide: write_events OR brief_events
    def f(*a, **kw):
        out = channel_reports(*a, **kw)
        deciders = kw.get("deciders") or {}
        for c in out.values():
            if not c.get("members") and c.get("held") and deciders:
                w = [max(d["write_events"]) for d in deciders.values() if d.get("write_events")]
                b = [max(d["brief_events"]) for d in deciders.values() if d.get("brief_events")]
                c["deciding_event"] = max(w) if w else (max(b) if b else None)
        return out
    return f


def failed_only_events(channel_reports):         # deciding events aggregated over failed slots only (HELD loses it)
    def f(*a, **kw):
        out = channel_reports(*a, **kw)
        for c in out.values():
            if not c.get("failed_slots") and c.get("held_members"):
                c["deciding_event"] = None
        return out
    return f


def old_slot_unknown(channel_reports):           # the pre-fix unknown count: deciders=None means "nothing unknown"
    def f(*a, **kw):
        out = channel_reports(*a, **kw)
        deciders = kw.get("deciders")
        for c in out.values():
            if "provenance_missing" in c:
                c["unknown_decisions"] = (sum(1 for d in deciders.values() if not (d or {}).get("models"))
                                          if deciders else 0)
        return out
    return f


UNDO = [("node_verdicts", "mechanism? -> the old cohort fallback", nv, [(nv, "classify", old_classify(nv.classify))]),
        ("node_verdicts", "no control trials", nv, [(nv, "control_trials", lambda *a, **kw: {})]),
        ("node_verdicts", "no deciding event / model", nv,
         [(nv, "decider", lambda *a, **kw: {"deciding_event": None, "deciding_model": None, "via": None,
                                            "briefs": [], "register_writes": []})]),
        ("node_verdicts", "go rule without model or independence checks", nv, [(nv, "go_rule", old_go_rule)]),
        ("node_verdicts", "compare without landed-key sets", nv,
         [(nv, "compare_attribution", items_only(nv.compare_attribution))]),
        ("node_verdicts", "surface-only rules proposed", nv,
         [(nv, "ledger_proposals", proposing_everything(nv.ledger_proposals))]),
        ("hardness_ledger", "no control / channel kinds", hl, [(hl, "KINDS", tuple(k for k in hl.KINDS
                                                                                 if k not in ("control", "channel")))]),
        ("hardness_ledger", "pending review not refused", hl, [(hl, "check", (lambda check: lambda rec: check(
            dict(rec, features={k: v for k, v in (rec.get("features") or {}).items() if k != "pending_review"})
            if isinstance(rec, dict) else rec))(hl.check))]),
        ("node_verdicts", "slips listed again when a channel or control explains them", nv,
         [(nv, "go_rule", slips_unfiltered(nv.go_rule))]),
        ("node_verdicts", "channel members matched on any column (class cascade)", nv,
         [(nv, "channel_reports", any_column_channels(nv.channel_reports))]),
        ("node_verdicts", "control trials matched on any column (class cascade)", nv,
         [(nv, "control_trials", any_column_controls(nv.control_trials))]),
        ("hardness_ledger", "H2 design effect over weighted trials", hl, [(hl, "priors", weighted_deff_priors())]),
        ("hardness_forecast", "F1 channel rates matched by channel id", hf,
         [(hf, "channel_rate", by_channel_id(hf.channel_rate))]),
        ("trajectory_ledger", "a revision-14 surface read raw (no key pattern for the briefs)", tl,
         [(tl, "table_spec_from_surface", raw_surface_spec)]),
        ("difficulty_mutation", "keyless briefs give silent empty batches", dm, [(dm, "shards_for", silent_shards_for)]),
        ("oracle_kit", "no live-controls check", ok, [(ok, "check_controls", lambda *a, **kw: None)]),
        ("node_verdicts", "seeded landings ignore supersession and revision", nv,
         [(nv, "seeded_landings", old_seeded_landings)]),
        ("node_verdicts", "decider bounded by the last table write", nv, [(nv, "decider", ignoring_key_events(nv.decider))]),
        ("node_verdicts", "unknown deciding models ignored", nv, [(nv, "go_rule", ignoring_unknown(nv.go_rule))]),
        ("node_verdicts", "unobserved control member held", nv,
         [(nv, "control_trials", unobserved_as_held(nv.control_trials))]),
        ("node_verdicts", "slots-only channel without provenance", nv,
         [(nv, "channel_reports", no_slot_provenance(nv.channel_reports))]),
        ("node_verdicts", "class difference always cascade", nv, [(nv, "classify", naive_class(nv.classify))]),
        ("hardness_ledger", "observation records summed per record", hl, [(hl, "priors", old_observation_priors())]),
        ("hardness_ledger", "rho unvalidated", hl, [(hl, "priors", unvalidated_rho())]),
        ("hardness_forecast", "channel rate run key drops the revision", hf,
         [(hf, "_rate_from_records", run_only_rate(hf._rate_from_records))]),
        ("hardness_forecast", "channel ops accepted as mechanisms", hf,
         [(hf, "refuse_channel_elements", no_channel_guard)]),
        ("node_verdicts", "control-explained items kept as slips / mechanisms", nv,
         [(nv, "classify", old_classify_no_controls(nv.classify))]),
        ("node_verdicts", "HELD channel proposes no record set", nv,
         [(nv, "ledger_proposals", held_keys_from_failed_members(nv.ledger_proposals))]),
        ("node_verdicts", "a reference item's classification never vetoes a landing", nv,
         [(nv, "reference_landed", old_reference_landed(nv.reference_landed))]),
        ("node_verdicts", "slots-only channel counted although a control explains its target", nv,
         [(nv, "go_rule", ignoring_slot_targets(nv.go_rule))]),
        ("node_verdicts", "a subset of mapped slots treated as the whole channel (residual lost)", nv,
         [(nv, "go_rule", subset_slot_targets(nv.go_rule))]),
        ("node_verdicts", "residual models/unknown not recomputed after subtraction", nv,
         [(nv, "go_rule", stale_slot_provenance(nv.go_rule))]),
        ("node_verdicts", "all-dropped observations leave no provenance", nv,
         [(nv, "_dropped", lambda *a, **kw: [])]),
        ("node_verdicts", "missing slot provenance counted as known", nv,
         [(nv, "channel_reports", old_slot_unknown(nv.channel_reports))]),
        ("node_verdicts", "failed slot omitted from a channel proposal's record set", nv,
         [(nv, "ledger_proposals", old_proposal_slot_keys(nv.ledger_proposals))]),
        ("node_verdicts", "HELD slots-only channel loses its deciding event", nv,
         [(nv, "channel_reports", failed_only_events(nv.channel_reports))]),
        ("node_verdicts", "a write-backed slot masks another slot's brief-only decision", nv,
         [(nv, "channel_reports", channel_wide_events(nv.channel_reports))]),
        ("node_verdicts", "declared observed/held counts ignored (details only)", nv,
         [(nv, "_channel_provenance", details_only_provenance(nv._channel_provenance))]),
        ("node_verdicts", "a slot with no detail reuses the channel aggregate", nv,
         [(nv, "go_rule", aggregate_when_no_details(nv.go_rule))]),
        ("node_verdicts", "the fallback flag ignores a known-but-unknown model set", nv,
         [(nv, "ledger_proposals", fallback_by_emptiness(nv.ledger_proposals))]),
        ("hardness_ledger", "a truthy covered evidence passes as a count", hl,
         [(hl, "check", covered_by_truthiness(hl.check))]),
        ("node_verdicts", "a FAILED channel ignores its held observations' models", nv,
         [(nv, "_channel_provenance", failed_only_models(nv._channel_provenance))]),
        ("node_verdicts", "the proposal event ignores the channel aggregate", nv,
         [(nv, "ledger_proposals", member_events_only(nv.ledger_proposals))]),
        ("hardness_ledger", "the unknown flag accepted by truthiness", hl,
         [(hl, "check", truthy_unknown(hl.check))]),
        ("hardness_ledger", "control-explained LANDED verdict enters the priors", hl,
         [(hl, "priors", priors_without_control_gate(hl.priors))]),
        ("hardness_ledger", "control/channel record without provenance accepted", hl,
         [(hl, "check", old_check_provenance(hl.check))]),
        ("hardness_ledger", "a legitimate landing removed with its control-explained key", hl,
         [(hl, "priors", blanket_control_exclusion(hl.priors))])]


def self_test(mod) -> str | None:
    """None when the module's self-test passes, else the failure (its last line)."""
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            mod._self_test()
    except Exception as error:  # noqa: BLE001 - the failure is the evidence
        return f"{type(error).__name__}: {str(error)[:150]}"
    return None


INTERFACE_ERRORS = ("unexpected keyword argument", "positional argument", "multiple values for argument")


def failure_kind(err: str | None) -> str | None:
    """'interface' when a mutation crashed on a stale signature, 'semantic' when the planted assertion fired."""
    if err is None:
        return None
    return "interface" if (err.startswith("TypeError") or any(x in err for x in INTERFACE_ERRORS)) else "semantic"


class _TypeErrFixture:
    @staticmethod
    def _self_test():
        raise TypeError("channel_reports() missing 1 required keyword-only argument: 'table_events'")


class _AssertErrFixture:
    @staticmethod
    def _self_test():
        raise AssertionError("planted assertion fired")


def runner_self_test() -> int:
    """Planted negative controls: a TypeError (even a missing keyword-only argument) is an interface error, never a
    semantic falsification; an AssertionError is semantic."""
    assert failure_kind(self_test(_TypeErrFixture)) == "interface"
    assert failure_kind(self_test(_AssertErrFixture)) == "semantic"
    assert failure_kind("TypeError: f() got an unexpected keyword argument 'x'") == "interface"
    assert failure_kind("TypeError: f() missing 1 required keyword-only argument: 'y'") == "interface"
    assert failure_kind("AssertionError: nope") == "semantic"
    assert failure_kind(None) is None
    print("falsify runner self-test: ok (TypeError, including a missing keyword-only argument, is an interface error; "
          "only a semantic failure counts as a falsification)")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        return runner_self_test()
    ok_all = True
    for mod in (nv, hl, hf, ok, tl, dm):
        err = self_test(mod)
        ok_all = ok_all and err is None
        print(f"{'ok  ' if err is None else 'FAIL'} control: {mod.__name__} self-test passes" + (f" - {err}" if err else ""))
    for owner, name, mod, patches in UNDO:
        saved = [(m, attr, getattr(m, attr)) for m, attr, _ in patches]
        try:
            for m, attr, new in patches:
                setattr(m, attr, new)
            err = self_test(mod)
        finally:
            for m, attr, old in saved:
                setattr(m, attr, old)
        # a mutation that crashes on a stale interface is NOT a semantic falsification
        interface = failure_kind(err) == "interface"
        ok_case = err is not None and not interface
        ok_all = ok_all and ok_case
        status = "ok  " if ok_case else "FAIL"
        note = " (interface error, not a semantic falsification: fix the undo wrapper)" if interface else ""
        print(f"{status} {owner}: {name} -> the self-test {'fails' if err and not interface else 'still passes'}"
              f"{note}" + (f"\n       {err}" if err else ""))
    print("H1 FALSIFICATION " + ("PASS" if ok_all else "FAIL"))
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
