#!/usr/bin/env python3
"""node_verdicts.py - propose a verdict for every designed node in every run, with event citations (plan §7.7, 01a B3).

For each node x run it asks three questions:
  1. Was the deciding record in a result the responsible agent saw?  (reach: the covering subagent's calls, or the
     main context, returned the record - its id or a unique text window of it)
  2. Did the briefs for the affected records carry the rule?          (brief transmission: the brief text, the files
     the brief tells the worker to read - with the worker's Read of them - and rule-bearing scripts the main context
     wrote)
  3. Does the written value match the solver for THAT revision?      (the run is bound to its revision by content
     with trajectory_ledger.binding and graded with that revision's solver)

Every register difference from the truth is classified once:
  mechanism       the column is one a rule decides, the component is one the rule acts on (solver.touched), and the
                  rule's ablation reproduces the written value (several such rules: mechanism (ambiguous))
  mechanism?      the same, but no ablation reproduces the value: pending review, never a landing until dispositioned
                  (H1; the old fallback gave every in-cohort error to the rule)
  slip            no rule that decides the column acts on the component (an unattributed error, never a mechanism)
  representation  a blank / missing spelling where the truth has a value, and the class is still right
  cascade         a class difference that follows the component's own field differences (one cause, not two). Round 2
                  (H1-9): a class difference is attributed to a rule only when that rule's ablation reproduces the
                  written class AND leaves every other written column of the key equal to the written row; a column the
                  row omits is unobserved, never equal by default. This is a conservative convention: it undercounts a
                  landing when an independent slip sits in the same row (planted as a labelled known false negative).
Rule verdicts (proposals): LANDED · LEAKED · NOT-REACHED · BYPASSED · FALSE; SURFACE-ONLY for a rule that decides no
register column (its surface slots are listed; never proposed to the ledger). CONFOUNDED is never proposed: tool,
fairness, verifier and run (mixed-model) causes are FLAGGED as candidates for the author's disposition.
Every landed key, control trial and channel member names who decided it: the last brief naming the key before the
key's own last write (trajectory_ledger.table() meta["key_events"], falling back to the last table event when the key
is absent), else the register write (trajectory_ledger.deciders). A deciding model that is not recorded is an unknown
decision: it is counted per rule and per channel (`unknown_decisions`) and is never eligible for the go rule, which
needs a known, matching model for every counted decision.
Control trials (H1): when a rule declares control members and an over-application operator (oracle_kit), each written
member is OVER-APPLIED (its row reproduces all of the operator's own change) or HELD, beside the rule's verdict on its
scope (a rule can land and over-apply in one run). The operator's own change is computed from truth vs degrade across
the declared columns; the class counts only when the operator changes nothing else, since a class can match as the
cascade of another error. An own field the written row does not carry is UNOBSERVED (it was not held, and not failed).
Complexity channels (F1): each declared channel is FAILED (a member's row reproduces all of the channel degrade's own
change), HELD (observed, not reproduced) or UNOBSERVED (nothing observed: it proposes nothing). Observed, held and
unobserved members are counted separately; unobserved members never enter the held denominator. A slots-only channel
is judged on the run's surface grades and takes its deciding event and models from the failed slots' decided_by. A
HELD channel lists its held members with their provenance. A slip that a failed channel member or an over-applied
control explains is listed there, not as a slip. The go-rule tally (01a MODE B step 6) counts designed mechanisms that
LANDED and pre-registered channels that FAILED, each only when every deciding model is the expected model's own and no
decision is unknown, and merges those that share a landed key or a source; (key, field) evidence that an over-applied
control already explains is subtracted from a channel before the channel is counted. Control trials, slips and
pending reviews count for neither.
Degrade operators (e.g. trusting a stale export) are nodes too: read and copied (>= --trust-min values) = LANDED,
read and not copied = LEAKED, never read = NOT-REACHED. Every manifest fragment, authority and decoy record is a
reach node: READ (first event) or NOT-READ.

The tool proposes; the model reviews every call in the review queue (calls that touch a landed node's deciding
records, its briefs and its writes, plus calls the tool cannot classify) and dispositions each verdict. Read-only,
stdlib only, never executes SQL.

Usage:
  python3 -B Task_Authoring/tools/node_verdicts.py --task-dir DIR [--solver S] [--sql LABEL=PATH ...] [--run LABEL=PATH ...]
      [--surface S] [--manifest M] [--reference attribution.json] [--seed-ledger proposals.jsonl]
      [--ledger-out proposals.jsonl] [--source S] [--out OUT.json] [--json]
  python3 -B Task_Authoring/tools/node_verdicts.py --self-test
The first --sql is the revision under test (default: the task's 01_Universe_Inject.sql); pass every stored revision
(Working_Files/run_forensics/<rev>/01_Universe_Inject.sql) to bind against. Each run is bound on evidence
(trajectory_ledger.binding): one candidate alone is INSUFFICIENT, unless --sole-revision REASON (refused when the task
stores another revision) and the run saw its content. A run that is not BOUND is reported and never evaluated (no
fallback to the first SQL); proposals carry each run's own revision and sql_sha256. --seed-ledger is compared against
each run's own bound revision and needs --reference (the comparison is reported there); it is refused without it.
Exit 0 = proposals written, 1 = a reference comparison disagrees or a run is not bound, 2 = usage error.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path


def _bundle() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "difficulty_stats.py").is_file():
            return parent
    raise SystemExit("node_verdicts: cannot find the Task_Authoring bundle (no tools/difficulty_stats.py above)")


HERE = Path(__file__).resolve().parent
BUNDLE = _bundle()
for _p in (BUNDLE / "tools", HERE):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
import difficulty_stats as ds  # noqa: E402  (model labels have one owner)
import gradable_surface as gs  # noqa: E402
import oracle_kit as ok  # noqa: E402
import surface_grader as sg  # noqa: E402
import trajectory_ledger as tl  # noqa: E402

VERSION = "node_verdicts/1"
TRUST_MIN = 10
RX_PATH = re.compile(r"(?:/app|/tmp|/home|/workspace)/[\w./-]+\.(?:md|txt|json|py|csv|yaml|yml)")
FILE_TOOLS = ("Write", "Edit", "MultiEdit")


# ------------------------------------------------------------------ record needles (ported season_pass_runs.attention)

def needles(sql_text: str) -> dict:
    """{record id: [needles]}: the id (8+ characters), a Slack ts, or a unique 40-character window of its text."""
    from base_check import parse_sql
    recs = []
    for x in parse_sql(sql_text):
        if x["op"] != "insert":
            continue
        r = x["row"]
        txt = ""
        for k in ("text", "body", "body_text", "description", "desc", "content", "snippet", "summary", "title", "name",
                  "data_json", "grid_json"):
            v = r.get(k)
            if isinstance(v, str) and len(v) > len(txt):
                if k in ("data_json", "grid_json"):
                    try:
                        v = " ".join(tl.strings(json.loads(v)))
                    except ValueError:
                        pass
                txt = v
        rid = str(r.get("id") or r.get("spreadsheet_id") or r.get("document_id") or r.get("presentation_id") or "")
        recs.append((rid, tl.flat(txt), str(r.get("ts") or "") if x["table"].endswith("slack_messages") else ""))
    texts = [t for _, t, _ in recs]
    out = {}
    for rid, t, ts in recs:
        window = None
        if len(t) >= 60:
            for start in (len(t) // 2 - 20, len(t) // 3, 10, max(0, len(t) - 60)):
                cand = t[max(0, start):max(0, start) + 40]
                if len(cand) == 40 and sum(1 for o in texts if cand in o) == 1:
                    window = cand
                    break
        ns = [n.lower() for n in (rid if len(rid) >= 8 else None, window, ts or None) if n]
        if rid and ns:
            out.setdefault(rid, [])
            out[rid] += [n for n in ns if n not in out[rid]]
    return out


# ------------------------------------------------------------------ run structure

class RunView:
    """Calls grouped by agent (main context and each brief's subtree) with cached result text."""

    def __init__(self, run: tl.Run, key_rx):
        self.run = run
        self.briefs = tl.briefs(run, key_rx)
        self.by_parent = collections.defaultdict(list)
        for c in run.calls:
            self.by_parent[c["parent"]].append(c)
        self._subtree = {}

    def subtree(self, brief_id: str) -> list:
        if brief_id not in self._subtree:
            out, stack = [], [brief_id]
            while stack:
                b = stack.pop()
                for c in self.by_parent.get(b, []):
                    out.append(c)
                    if c["name"] in tl.BRIEF_TOOLS:
                        stack.append(c["id"])
            self._subtree[brief_id] = out
        return self._subtree[brief_id]

    def main_calls(self) -> list:
        return self.by_parent.get(None, [])

    def first_seen(self, calls, ns) -> int | None:
        for c in sorted(calls, key=lambda c: c["event"] or 0):
            t = self.run.result_text(c["id"])
            if t and any(n in t for n in ns):
                r = self.run.results.get(c["id"])
                return r["event"] if r else c["event"]
        return None

    def covering(self, key: str) -> list:
        return [b for b in self.briefs if key in b["keys"]]


def file_writes(view: RunView, context: str | None = "main") -> list:
    out = []
    for c in view.run.calls:
        if c["name"] in FILE_TOOLS and (context is None or c["context"] == context):
            q = c["input"] or {}
            text = q.get("content") or q.get("new_string") or "\n".join(e.get("new_string", "") for e in q.get("edits", []) or [])
            out.append({"event": c["event"], "path": q.get("file_path") or q.get("path"), "text": text or "",
                        "model": c["model"], "context": c["context"], "id": c["id"], "parent": c["parent"]})
    return out


def transmission(view: RunView, brief: dict, rx, main_files: list) -> dict:
    """Does a brief carry the rule: in its own text, or in a file it tells the worker to read (and did the worker?)."""
    own = bool(rx.search(brief["description"] + "\n" + brief["prompt"]))
    refs = []
    for path in sorted(set(RX_PATH.findall(brief["prompt"]))):
        before = [f for f in main_files if f["path"] == path and f["event"] < brief["event"]]
        if not before:
            continue
        f = before[-1]
        read = [c["event"] for c in view.subtree(brief["id"]) if c["name"] == "Read"
                and (c["input"] or {}).get("file_path") == path]
        refs.append({"path": path, "written_event": f["event"], "written_by": f["model"], "carries": bool(rx.search(f["text"])),
                     "worker_read_events": read})
    by_ref = any(r["carries"] and r["worker_read_events"] for r in refs)
    return {"event": brief["event"], "writer_model": brief["writer_model"], "worker_models": brief["subagent_models"],
            "text_carries": own, "referenced_files": refs, "carries": own or by_ref,
            "via": "brief text" if own else "referenced file read by the worker" if by_ref else None}


def worker_lines(view: RunView, briefs: list, key: str) -> list:
    out = []
    for b in briefs:
        for c in view.subtree(b["id"]):
            if c["name"] not in FILE_TOOLS:
                continue
            text = (c["input"] or {}).get("content") or (c["input"] or {}).get("new_string") or ""
            for line in text.splitlines():
                if line.startswith(key) or re.match(r"^\W*" + re.escape(key) + r"\b", line):
                    out.append({"event": c["event"], "path": (c["input"] or {}).get("file_path"), "line": line[:400]})
                    break
    return out


def _parents(rules: dict, names) -> list:
    out = []
    for r in names:
        p = (rules.get(r) or {}).get("part_of") or r
        if p not in out:
            out.append(p)
    return out


def decider(view: RunView, key: str, table_events: list, key_events: dict | None = None) -> dict:
    """Who decided a written register value: the last brief naming the key before that key's OWN last write (its writer
    model), else the write itself (its model). `key_events` is trajectory_ledger.table()'s meta["key_events"] ({key:
    event}); a key absent from it falls back to the last table event. Every naming brief and write is listed."""
    events = list(table_events or ())
    own = (key_events or {}).get(key) if isinstance(key_events, dict) else None
    last = own if isinstance(own, (int, float)) and not isinstance(own, bool) else (max(events) if events else None)
    cov = view.covering(key)
    before = [b for b in cov if last is None or b["event"] < last]
    writes = [w for w in tl.deciders(view.run, view.briefs, keys=[key], tools=sg.TABLE_TOOLS)["writes"]
              if w["event"] in set(events)]
    if writes and last is not None:                     # the write that supplied this key's final value, when known
        own_write = [w for w in writes if w["event"] == last]
        writes = own_write or [w for w in writes if w["event"] <= last]
    if before:
        ev, model, via = before[-1]["event"], before[-1]["writer_model"], "brief"
    elif writes:
        ev, model, via = writes[-1]["event"], writes[-1]["model"], "register write"
    else:
        ev, model, via = None, None, None
    return {"deciding_event": ev, "deciding_model": tl._family(model) if model else None, "via": via,
            "briefs": [[b["event"], tl._family(b["writer_model"])] for b in cov][:8],
            "register_writes": [[w["event"], tl._family(w["model"])] for w in writes][:4]}


def _surface_results(run: tl.Run, surface: dict, truth: dict, briefs: list | None = None) -> tuple:
    """({slot: True | False | None}, {failed slot: decided_by}) for the run on the surface (empty when no slots)."""
    if not surface.get("slots"):
        return {}, {}
    d = sg.decode(run, surface)
    res = sg.grade(surface, truth, d)
    dec = {s["id"]: sg.decided_by(run, briefs or [], s, d, truth, surface)
           for s in surface["slots"] if res.get(s["id"]) is not None}
    return res, dec


def control_trials(view: RunView, rules: dict, controls: dict, rows: dict, truth: dict, *, mod, state, tspec: dict,
                   class_field: str, table_events: list, key_events: dict | None = None) -> dict:
    """{rule: {trials, over_applied, held}}: every declared control member written in the run, on the rule's columns
    and the class (see the module docstring)."""
    out = {}
    for r, c in controls.items():
        op = c["over_application"]
        dg = mod.solve(state, degrade={op}) if op else None
        fields = list(dict.fromkeys(f for f in list(rules[r].get("decides") or []) + [class_field]
                                    if f in (tspec.get("columns") or [])))
        trials = []
        for k in c["members"]:
            if k not in rows or k not in truth:
                trials.append({"key": k, "outcome": "NOT-WRITTEN", "error": None})
                continue
            # H1-6: the operator's own change is computed from truth vs degrade across the declared fields, never from
            # which columns the row happens to carry; a missing own field is unobserved (not held, not over-applied)
            changed = [f for f in fields if dg is not None and dg[k].get(f) != truth[k].get(f)]
            own = [f for f in changed if f != class_field] or changed
            if not own or any(f not in rows[k] for f in own):
                trials.append({"key": k, "outcome": "UNOBSERVED", "error": None, "fields": own, "written": {},
                               "truth": {f: truth[k].get(f) for f in own}, "over_applied_value": None,
                               **decider(view, k, table_events, key_events)})
                continue
            wrong = [f for f in own if sg.compare(rows[k][f], truth[k].get(f), f, tspec) != "MATCH"]
            over = [f for f in own if f in wrong and sg.compare(rows[k][f], dg[k].get(f), f, tspec) == "MATCH"]
            over = over if len(over) == len(own) else []
            shown = over or wrong
            trials.append({"key": k, "outcome": "OVER-APPLIED" if over else "HELD", "error": bool(wrong),
                           "fields": shown, "written": {f: rows[k][f] for f in shown},
                           "truth": {f: truth[k].get(f) for f in shown},
                           "over_applied_value": {f: dg[k].get(f) for f in over} if over else None,
                           **decider(view, k, table_events, key_events)})
        out[r] = {"mechanism": rules[r].get("mechanism"), "family": rules[r].get("family"), "over_application": op,
                  "trials": trials, "over_applied": [x["key"] for x in trials if x["outcome"] == "OVER-APPLIED"],
                  "held": [x["key"] for x in trials if x["outcome"] == "HELD"],
                  "rule": "a control member written as the over-application gives is OVER-APPLIED, else HELD; never a "
                          "landing for the go rule or the priors"}
    return out


def channel_reports(view: RunView, channels: dict, rows: dict, truth: dict, *, mod, state, tspec: dict,
                    table_events: list, graded: dict | None = None, class_field: str = "class",
                    key_events: dict | None = None, deciders: dict | None = None,
                    slot_targets: dict | None = None) -> dict:
    """{channel: {...}} for every declared complexity channel. H1-7: observed, failed, held and unobserved members are
    counted apart (an unobserved member is never a held trial); a slots-only channel is judged on the run's surface
    grades and carries the failed slots' deciding model; a channel whose degrade moves no register column is
    UNOBSERVED (judged on the surface). Records carry the unit the forecast draws (member or run)."""
    cols = [f for f in tspec.get("columns") or [] if f not in (tspec.get("key_column"), tspec.get("reason_column"))]
    out = {}
    for cid, c in channels.items():
        base = {"kind": c.get("kind"), "rule": c.get("rule"), "source": c.get("source"),
                "preregistered": bool(c.get("preregistered", True))}
        if not c.get("degrade"):                        # slots-only: judge the declared surface slots
            declared = list(c.get("slots") or [])
            bad = [s for s in declared if (graded or {}).get(s) is False]
            ok = [s for s in declared if (graded or {}).get(s) is True]
            unobs = [s for s in declared if (graded or {}).get(s) is None or s not in (graded or {})]
            dec = [deciders.get(s) or {} for s in bad] if deciders else []
            models = sorted({m for d in dec for m in d.get("models") or []})
            # H1 residual f: a failed slot the ledger has no deciding record for is an UNKNOWN decision, never a
            # known trial of the harness model (this also covers deciders=None, where `dec` is empty)
            provenance_missing = [s for s in bad if not ((deciders or {}).get(s) or {}).get("models")]
            obs_dec = [deciders.get(s) or {} for s in (bad + ok)] if deciders else []

            def _slot_event(d):
                evs = list(d.get("write_events") or []) + list(d.get("brief_events") or [])
                return max(evs) if evs else None

            events = [e for e in (_slot_event(d) for d in obs_dec) if e is not None]
            out[cid] = dict(base, verdict="FAILED" if bad else ("HELD" if ok else "UNOBSERVED"), members=0,
                            observed=len(bad) + len(ok), held=len(ok), unobserved=len(unobs), slots=declared,
                            failed_slots=bad, failed_members=[], held_members=[
                                {"slot": s, **((deciders or {}).get(s) or {})} for s in ok],
                            deciding_models=models, unknown_decisions=len(provenance_missing),
                            provenance_missing=provenance_missing,
                            failed_slot_targets=[{"slot": s, **slot_targets[s]} for s in bad
                                                 if (slot_targets or {}).get(s)],
                            failed_slot_details=[{"slot": s, "models": list(((deciders or {}).get(s) or {})
                                                                           .get("models") or [])} for s in bad],
                            deciding_event=max(events) if events else None,
                            counts={"unit": "run", "n": 1, "failed": int(bool(bad))})
            continue
        dg = mod.solve(state, degrade={c["degrade"]})
        moved = [k for k in c.get("members") or [] if k in dg and k in truth
                 and any(dg[k].get(f) != truth[k].get(f) for f in cols)]      # the trials: members the degrade moves
        if not moved and c.get("slots"):
            # H1 residual b: a register-invisible channel that declares surface slots is judged on those slots, never
            # silently UNOBSERVED
            declared = list(c.get("slots") or [])
            bad = [s for s in declared if (graded or {}).get(s) is False]
            ok = [s for s in declared if (graded or {}).get(s) is True]
            unobs = [s for s in declared if (graded or {}).get(s) is None or s not in (graded or {})]
            dec = [deciders.get(s) or {} for s in bad] if deciders else []
            models = sorted({m for d in dec for m in d.get("models") or []})
            # H1 residual f: a failed slot the ledger has no deciding record for is an UNKNOWN decision, never a
            # known trial of the harness model (this also covers deciders=None, where `dec` is empty)
            provenance_missing = [s for s in bad if not ((deciders or {}).get(s) or {}).get("models")]
            obs_dec = [deciders.get(s) or {} for s in (bad + ok)] if deciders else []

            def _slot_event(d):
                evs = list(d.get("write_events") or []) + list(d.get("brief_events") or [])
                return max(evs) if evs else None

            events = [e for e in (_slot_event(d) for d in obs_dec) if e is not None]
            out[cid] = dict(base, verdict="FAILED" if bad else ("HELD" if ok else "UNOBSERVED"), members=0,
                            observed=len(bad) + len(ok), held=len(ok), unobserved=len(unobs), slots=declared,
                            failed_slots=bad, failed_members=[], held_members=[
                                {"slot": s, **((deciders or {}).get(s) or {})} for s in ok],
                            deciding_models=models, unknown_decisions=len(provenance_missing),
                            provenance_missing=provenance_missing,
                            failed_slot_targets=[{"slot": s, **slot_targets[s]} for s in bad
                                                 if (slot_targets or {}).get(s)],
                            failed_slot_details=[{"slot": s, "models": list(((deciders or {}).get(s) or {})
                                                                           .get("models") or [])} for s in bad],
                            deciding_event=max(events) if events else None,
                            counts={"unit": "run", "n": 1, "failed": int(bool(bad))})
            continue
        if not moved:
            out[cid] = dict(base, verdict="UNOBSERVED", members=0, observed=0, held=0, unobserved=0,
                            failed_members=[], deciding_models=[], unknown_decisions=0,
                            why="the degrade moves no register column and no surface slots are declared")
            continue
        failed, observed = [], []
        for k in moved:
            if k not in rows:
                continue                                  # not written: unobserved
            # the member reproduces the channel's own change; the class counts only when the degrade changes nothing
            # else (otherwise it is a cascade that another error can produce), and every own field must be readable
            changed = [f for f in cols if dg[k].get(f) != truth[k].get(f)]
            own = [f for f in changed if f != class_field] or changed
            if not own or any(f not in rows[k] for f in own):
                continue                                  # unobserved: not held, not failed
            observed.append(k)
            hit = [f for f in own if sg.compare(rows[k][f], truth[k].get(f), f, tspec) != "MATCH"
                   and sg.compare(rows[k][f], dg[k].get(f), f, tspec) == "MATCH"]
            if len(hit) == len(own):
                failed.append({"key": k, "fields": hit, **decider(view, k, table_events, key_events)})
        seen = {x["key"] for x in failed}
        latent = c.get("latent") if isinstance(c.get("latent"), str) else "member"
        unit = "member" if latent == "member" else "run"      # batch channels record per run (the forecast's unit)

        n_units = len(observed) if unit == "member" else 1
        f_units = len(failed) if unit == "member" else int(bool(failed))
        out[cid] = dict(base, verdict="FAILED" if failed else ("HELD" if observed else "UNOBSERVED"),
                        members=len(moved), observed=len(observed), held=len(observed) - len(seen),
                        unobserved=len(moved) - len(observed), failed_members=failed,
                        held_members=[{"key": k, **decider(view, k, table_events, key_events)}
                                      for k in observed if k not in seen],
                        deciding_models=sorted({x["deciding_model"] for x in failed if x["deciding_model"]}),
                        unknown_decisions=sum(1 for x in failed if not x["deciding_model"]),
                        counts={"unit": unit, "n": n_units, "failed": f_units})
    for cid, v in out.items():                  # the ledger pool for the channel's rate (default: its kind)
        v["family"] = channels[cid].get("family") or channels[cid].get("kind")
    return out


def go_rule(out_rules: dict, channels: dict, controls: dict, items: list, prov: dict, expected: str, rules: dict) -> dict:
    """The go rule's loss-channel tally for one run (see the module docstring)."""
    own = lambda models, unknown=0: bool(models) and unknown == 0 and all(ds.model_id(m) == expected for m in models)  # noqa: E731
    # H1-8: evidence a control over-application already explains is not also a channel failure
    over = collections.defaultdict(set)
    for c in controls.values():
        for x in c["trials"]:
            if x["outcome"] == "OVER-APPLIED":
                over[x["key"]] |= set(x.get("fields") or [])       # several controls may explain one key
    counted, excluded, control_explained = [], [], []
    over_keys = set(over)
    over_pairs = {(k, f) for k, fields in over.items() for f in fields}
    for r, v in out_rules.items():
        if v["verdict"] == "LANDED":
            src = (rules.get(r) or {}).get("source") or r
            if v.get("keys"):
                # H1 residual a: subtract the (key, field) evidence a control explains, not the whole key. Keep the
                # key's other landed fields and recompute model provenance from the surviving keys only.
                kept, models, unknown = set(), set(), 0
                for kd in v["keys"]:
                    key = kd.get("key")
                    if key not in v["landed_keys"]:
                        continue
                    residual = set(kd.get("fields") or []) - over.get(key, set())
                    if not residual:
                        continue
                    kept.add(key)
                    dec = kd.get("decided_by") or {}
                    if dec.get("deciding_model"):
                        models.add(dec["deciding_model"])
                    else:
                        unknown += 1
                if not kept:
                    continue
                x = (f"mechanism {r}", kept, src, sorted(models))
                (counted if own(sorted(models), unknown) else excluded).append(x)
            else:
                ks = set(v["landed_keys"]) - over_keys      # legacy callers carry no per-key detail
                if not ks:
                    continue
                x = (f"mechanism {r}", ks, src, v["deciding_models"])
                (counted if own(v["deciding_models"], v.get("unknown_decisions", 0)) else excluded).append(x)
    for cid, v in channels.items():
        if v["verdict"] == "FAILED" and not v.get("failed_members"):
            # a slots-only failure: the evidence is its failed slots and their reported decisions. H1 residual a:
            # a failed slot whose (key, field) target a control over-application already explains is removed from the
            # residual; every other failed slot stays, including one with no field target (never silently dropped),
            # and the residual models / unknown count are recomputed over the surviving slots only.
            models = v.get("deciding_models") or []
            unknown = v.get("unknown_decisions", 0)
            targets = v.get("failed_slot_targets") or []
            details = {d["slot"]: d for d in v.get("failed_slot_details") or []}
            residual = []
            for s in (v.get("failed_slots") or []):
                t = next((x for x in targets if x.get("slot") == s), None)
                if t and (t.get("key"), t.get("field")) in over_pairs:
                    continue
                residual.append(s)
            if targets and not residual:
                control_explained.append(f"channel {cid}")
                continue
            # recompute UNCONDITIONALLY over the surviving slots: a survivor with no detail is an UNKNOWN decision,
            # never the channel-wide aggregate (which may have been computed over removed slots)
            models = sorted({m for s in residual for m in (details.get(s) or {}).get("models") or []})
            unknown = sum(1 for s in residual if not (details.get(s) or {}).get("models"))
            keys = {t["key"] for t in targets if t.get("slot") in residual} | set(residual)
            x = (f"channel {cid}", keys, v.get("source") or cid, models)
            (counted if own(models, unknown) and v["preregistered"] else excluded).append(x)
            continue
        if v["verdict"] == "FAILED":
            residual = []
            for m in v["failed_members"]:
                left = set(m.get("fields") or []) - over.get(m["key"], set())
                if left:
                    residual.append(dict(m, fields=sorted(left)))
            if not residual and v["failed_members"]:
                control_explained.append(f"channel {cid}")
                continue
            models = sorted({m["deciding_model"] for m in residual if m["deciding_model"]})
            unknown = sum(1 for m in residual if not m["deciding_model"])
            x = (f"channel {cid}", {m["key"] for m in residual} or {m["key"] for m in v["failed_members"]},
                 v.get("source") or cid, models)
            (counted if own(models, unknown) and v["preregistered"] else excluded).append(x)
    groups = []
    for name, ks, src, _ in counted:
        g = {"names": [name], "keys": set(ks), "sources": {src}}
        for m in [m for m in groups if m["keys"] & ks or src in m["sources"]]:
            g["names"] += m["names"]
            g["keys"] |= m["keys"]
            g["sources"] |= m["sources"]
            groups.remove(m)
        groups.append(g)
    # an error that a failed channel member or an over-applied control explains is listed there, never again as a slip
    explained = {(m["key"], f) for v in channels.values() for m in v.get("failed_members") or []
                 for f in m.get("fields") or []} | \
        {(x["key"], f) for c in controls.values() for x in c["trials"] if x["outcome"] == "OVER-APPLIED"
         for f in x.get("fields") or []}
    return {"expected_model": expected, "independent_channels": len(groups),
            "channels": [sorted(g["names"]) for g in groups],
            "not_counted": {"off_model_or_unregistered": [[n, m] for n, _, _, m in excluded],
                            "control_over_applications": [f"{r}:{k}" for r, c in controls.items() for k in c["over_applied"]],
                            "slips": sorted({d["key"] for d in items if d["classification"] == "slip"
                                             and (d["key"], d.get("field")) not in explained}),
                            "explained_by_control": sorted(control_explained),
                            "pending_review": sorted({d["key"] for d in items if d["classification"] == "mechanism?"
                                                      and (d["key"], d.get("field")) not in over_pairs})},
            "run_valid": prov.get("v3_valid"),
            "rule": "count designed mechanisms that LANDED and pre-registered channels that FAILED in the expected "
                    "model's own decisions; items sharing a landed key or a source are one channel; control trials, "
                    "slips and pending reviews count for neither; the run must also be valid"}


# ------------------------------------------------------------------ classification

def class_attribution_ok(row: dict, ablation: dict, columns: list, tspec: dict, class_field: str) -> bool:
    """The H1-9 class predicate shared by classify() and reference comparison.

    A class is attributed to a rule only when the rule's ablation reproduces the written class and leaves every other
    written column equal to the written row. A column the row omits is not equal by default.
    """
    if sg.compare(ablation.get(class_field), row.get(class_field), class_field, tspec) != "MATCH":
        return False
    return all(f in row and sg.compare(ablation.get(f), row.get(f), f, tspec) == "MATCH"
               for f in columns if f != class_field)


def classify(rows: dict, truth: dict, abl: dict, touched: dict, rules: dict, tspec: dict, class_field: str,
             legacy=None, explained=None) -> list:
    """Every register difference from the truth, classified once (see the module docstring).

    `explained` is the set of (key, field) pairs a declared control's over-application already accounts for. Such a
    difference gets its own class, "control": never a slip, never a mechanism and never a landing. The subtraction is
    strictly per (key, field), so a control that changes only the class does not erase an unrelated field landing."""
    columns = [c for c in tspec.get("columns", []) if c != tspec.get("key_column") and c != tspec.get("reason_column")]
    missing = {tl.norm(m) for m in (tspec.get("missing_values") or tl.MISSING)}
    items = []
    for k in truth:
        if k not in rows:
            continue
        diffs = []
        for f in columns:
            if f not in rows[k] or f not in truth[k]:
                continue
            if sg.compare(rows[k][f], truth[k][f], f, tspec) == "MATCH":
                continue
            rep = [r for r in abl if abl[r][k][f] != truth[k][f] and sg.compare(rows[k][f], abl[r][k][f], f, tspec) == "MATCH"]
            diffs.append({"key": k, "field": f, "run": rows[k][f], "truth": truth[k][f], "reproduced_by_ignoring": rep})
        class_ok = not any(d["field"] == class_field for d in diffs)
        own = [d for d in diffs if d["field"] != class_field]
        for d in diffs:
            f = d["field"]
            d["attributed"], d["candidates"] = [], []
            if explained and (k, f) in explained:
                d["classification"] = "control"
                d["note"] = ("a declared control's over-application already accounts for this (key, field): a control "
                             "trial, never a slip and never a landing")
                continue
            if f == class_field:
                # H1-9: attribute the class only to a class-deciding rule whose ablation reproduces it without moving
                # any other written column (class-only rows included); otherwise cascade (a stated conservative
                # convention that undercounts a genuine class failure when an independent slip sits in the same row)
                cand = [r for r in rules if k in touched.get(r, set()) and class_field in rules[r].get("decides", [])]
                won = []
                for r in cand:
                    if class_attribution_ok(rows[k], abl[r][k], columns, tspec, class_field):
                        won.append(r)
                d["class_context"] = {
                    "row": {c: rows[k].get(c) for c in columns if c in rows[k]},
                    "ablations": {r: {c: abl[r][k].get(c) for c in columns if c in abl[r][k]} for r in abl},
                    "columns": list(columns),
                    "tspec": tspec,
                }
                if won:
                    parents = _parents(rules, won)
                    d["classification"] = "mechanism" if len(parents) == 1 else "mechanism (ambiguous)"
                    d["attributed"], d["candidates"] = parents, cand
                    d["note"] = "a class-deciding rule's ablation reproduces the class with the other written fields equal"
                else:
                    d["classification"] = "cascade"
                    d["note"] = ("class follows the component's field differences, or no class-deciding rule "
                                 "reproduces it with the other written fields equal (a conservative convention)")
            elif f != class_field and tl.norm(d["run"]) in missing and d["truth"] is not None and class_ok:
                d["classification"] = "representation"
                d["note"] = "blank or missing spelling where the truth has a value; the class is right"
            else:
                cand = [r for r in rules if k in touched.get(r, set()) and f in rules[r].get("decides", [])]
                won = [r for r in cand if r in d["reproduced_by_ignoring"]]
                d["candidates"] = cand
                if won:
                    parents = _parents(rules, won)
                    d["classification"] = "mechanism" if len(parents) == 1 else "mechanism (ambiguous)"
                    d["attributed"] = parents
                    d["note"] = "the rule's ablation reproduces the written value"
                elif cand:
                    d["classification"] = "mechanism?"
                    d["note"] = (f"wrong inside the cohort of {', '.join(_parents(rules, cand))}, but no ablation "
                                 f"reproduces the value: pending review, never a landing until dispositioned")
                elif f == class_field:
                    d["classification"] = "slip"
                    d["note"] = "class wrong with every input column right: the class rule was misapplied"
                else:
                    d["classification"] = "slip"
                    d["note"] = "no rule that decides this column acts on this component: an unattributed error"
            if legacy is not None:
                d["reproduced_by_legacy_flags"] = [r for r in d["reproduced_by_ignoring"] if r in legacy]
        items += diffs
    return items


# ------------------------------------------------------------------ one run

def verdicts_for_run(run: tl.Run, *, mod, state, truth: dict, surface: dict, manifest: dict | None, need: dict,
                     legacy=None, trust_min=TRUST_MIN, expected_model=None) -> dict:
    key_rx = re.compile(getattr(mod, "KEY_REGEX", r"\w+-\d+"))
    view = RunView(run, key_rx)
    expected = expected_model or ds.V3_POLICY["model"]
    rules = ok.active_rules(mod, getattr(state, "revision", None))
    controls_decl = ok.controls_of(mod, getattr(state, "revision", None))
    channels_decl = ok.channels_of(mod)
    tname, tspec = gs.table_deliverable(surface)
    t = tl.table(run, dict(tspec, classes=surface.get("classes", [])))
    rows = t["rows"]
    abl = {r: mod.solve(state, disable={r}) for r in rules}
    touched = {r: mod.touched(state, r) if hasattr(mod, "touched") else
               {k for k in truth if abl[r][k] != truth[k]} for r in rules}
    cf = ok.class_field(mod)
    prov = tl.provenance(run, view.briefs, expected)
    fallback_events = [f["event"] for f in prov["fallbacks"]]
    main_files = file_writes(view, "main")
    table_events = t["meta"].get("events") or ([t["meta"]["event"]] if t["meta"].get("event") is not None else [])
    key_events = t["meta"].get("key_events") or {}          # H1-5: the write that set each key's final value
    # H1 residual a: a control's over-application is decided BEFORE classification, so its evidence is never a slip,
    # never a mechanism and never a landing downstream (go_rule repeats the subtraction as an independent check).
    controls = control_trials(view, rules, controls_decl, rows, truth, mod=mod, state=state, tspec=tspec,
                              class_field=cf, table_events=table_events, key_events=key_events)
    over_pairs = {(x["key"], f) for c in controls.values() for x in c["trials"]
                  if x["outcome"] == "OVER-APPLIED" for f in x.get("fields") or []}
    items = classify(rows, truth, abl, touched, rules, tspec, cf, legacy, explained=over_pairs or None)
    graded, slot_deciders = _surface_results(run, surface, truth, view.briefs)
    out_rules = {}
    for r, spec in rules.items():
        if spec.get("part_of"):
            continue
        rx = re.compile(spec.get("signature") or r"(?!x)x", re.I)
        sub = [x for x, v in rules.items() if v.get("part_of") == r]
        landed = sorted({d["key"] for d in items if r in d.get("attributed", [])
                         and d.get("classification") != "control"})
        rule_over = {(x["key"], f) for x in (controls.get(r) or {}).get("trials", [])
                     if x["outcome"] == "OVER-APPLIED" for f in x.get("fields") or []}
        control_keys = sorted({k for k, _f in rule_over if k not in set(landed)})
        pending = sorted({d["key"] for d in items if d["classification"] == "mechanism?"
                          and r in _parents(rules, d.get("candidates") or [])})
        cohort = set(touched.get(r, set())) | {k for s in sub for k in touched.get(s, set())}
        keys_detail, not_reached = [], []
        for k in landed:
            cov = view.covering(k)
            calls = [c for b in cov for c in view.subtree(b["id"])] or run.calls
            deciding = mod.deciding(state, r, k) if hasattr(mod, "deciding") else mod.evidence(truth, k, spec["decides"][0])
            seen = {i: view.first_seen(calls + view.main_calls(), need.get(i, [i.lower()])) for i in deciding}
            reached = any(v is not None for v in seen.values())
            tx = [transmission(view, b, rx, main_files) for b in cov]
            keys_detail.append({"key": k, "fields": [d["field"] for d in items if d["key"] == k and r in d.get("attributed", [])
                                                     and d.get("classification") != "control"],
                                "deciding_records_seen": {i: e for i, e in seen.items() if e is not None},
                                "deciding_records_unseen": [i for i, e in seen.items() if e is None][:12],
                                "covering_briefs": tx, "worker_writes": worker_lines(view, cov, k),
                                "decided_by": decider(view, k, table_events, key_events)})
            if not reached:
                not_reached.append(k)
        landed_reached = [k for k in landed if k not in not_reached]
        authority = {a: view.first_seen(run.calls, need.get(a, [a.lower()])) for a in spec.get("authority", [])}
        carriers = [{"event": f["event"], "path": f["path"], "model": f["model"]} for f in main_files if rx.search(f["text"])]
        flags, hidden = [], []
        if landed_reached:
            writers = collections.Counter(b["writer_model"] for kd in keys_detail for b in kd["covering_briefs"])
            fb_written = [b for kd in keys_detail for b in kd["covering_briefs"] if fallback_events and b["event"] > min(fallback_events)]
            if prov["mixed_model"] and (fb_written or not any(kd["covering_briefs"] for kd in keys_detail)):
                flags.append(f"CONFOUNDED-run candidate (mixed-model): {len(fb_written)} covering brief(s) written after the "
                             f"model_refusal_fallback at event {min(fallback_events)} by {sorted({b['writer_model'] for b in fb_written})}; "
                             f"brief writers {dict(writers)}")
            seen_events = {e for kd in keys_detail for e in kd["deciding_records_seen"].values()}
            deciding_tools = {tl.short(c["name"]) for c in run.calls
                              if (run.results.get(c["id"]) or {}).get("event") in seen_events}
            for kd in keys_detail:
                if not kd["deciding_records_unseen"]:
                    continue        # every deciding record reached the writer: no tool error hid one
                writers = [c for b in view.covering(kd["key"]) for c in view.subtree(b["id"])] or view.main_calls()
                for c in writers:
                    got = run.results.get(c["id"])
                    if tl.short(c["name"]) in deciding_tools and got and (got["error"] or tl.RX_SPILL.search(
                            " ".join(tl.strings(got["data"])))):
                        hidden.append({"key": kd["key"], "event": c["event"], "tool": tl.short(c["name"]),
                                       "kind": "error" if got["error"] else "spill"})
            if hidden:
                flags.append(f"CONFOUNDED-tool candidate: {len(hidden)} errored or spilled call(s) of the deciding tools "
                             f"in the agents that wrote {sorted({h['key'] for h in hidden})}, whose deciding records "
                             f"were not all seen (events {[h['event'] for h in hidden][:6]}); confirm none hid a record")
        slots = [s["id"] for s in surface.get("slots") or [] if set(s.get("mechanisms") or []) & {r, spec.get("mechanism")}]
        surface_view = {"slots": slots, "failed": [sid for sid in slots if graded.get(sid) is False],
                        "ungraded": [sid for sid in slots if sid in graded and graded[sid] is None]}
        if not spec.get("decides"):
            verdict = "SURFACE-ONLY"
            why = (f"the rule decides no register column; {len(slots)} surface slot(s) declare it, failed in this run: "
                   f"{surface_view['failed'] or 'none'} (judge it there; never proposed to the ledger)")
        elif not rows:
            verdict = "NOT-REACHED"
            why = "the run wrote no table deliverable"
        elif landed_reached:
            verdict = "LANDED"
            why = f"{len(landed_reached)} component(s) wrong on a column the rule decides"
        elif not cohort:
            verdict = "FALSE"
            why = "the rule acts on no component of this revision (candidate; the mutation disposition decides)"
        elif not (cohort & set(rows)):
            verdict = "BYPASSED"
            why = "the register has none of the components the rule acts on"
        elif not_reached:
            verdict = "NOT-REACHED"
            why = f"the deciding records of {not_reached} never reached the agents that wrote them"
        else:
            verdict = "LEAKED"
            why = (f"all {len(cohort & set(rows))} components the rule acts on are right" if not pending else
                   f"no component is wrong the way the rule's ablation gives; {len(pending)} in-cohort error(s) "
                   f"pending review")
            if authority and not any(v is not None for v in authority.values()):
                why += "; the rule's authority record was never read (the outputs are right from another source)"
        if pending:
            flags.append(f"PENDING REVIEW (mechanism?): {pending} - wrong inside the cohort, but no ablation reproduces "
                         f"the value; disposition them before the verdict is final")
        tx_all = [b for kd in keys_detail for b in kd["covering_briefs"]]
        out_rules[r] = {"verdict": verdict, "why": why, "mechanism": spec.get("mechanism"), "family": spec.get("family"),
                        "nodes": spec.get("nodes", []), "cohort": len(cohort), "landed_keys": landed_reached,
                        "control_explained_keys": control_keys,
                        "not_reached_keys": not_reached, "pending_review_keys": pending, "keys": keys_detail,
                        "deciding_models": sorted({kd["decided_by"]["deciding_model"] for kd in keys_detail
                                                   if kd["key"] in landed_reached and kd["decided_by"]["deciding_model"]}),
                        "unknown_decisions": sum(1 for kd in keys_detail if kd["key"] in landed_reached
                                                 and not kd["decided_by"]["deciding_model"]),
                        "surface": surface_view,
                        "brief_transmission": {"covering_briefs": len(tx_all),
                                               "carry_in_text": sum(b["text_carries"] for b in tx_all),
                                               "carry_by_reference": sum(b["carries"] and not b["text_carries"] for b in tx_all),
                                               "omit": sum(not b["carries"] for b in tx_all),
                                               "writers_of_omitting": dict(collections.Counter(b["writer_model"] for b in tx_all if not b["carries"])),
                                               "writers_of_carrying": dict(collections.Counter(b["writer_model"] for b in tx_all if b["carries"]))},
                        "main_context_rule_carriers": carriers[:8], "authority_first_seen": authority,
                        "flags": flags, "tool_confound_check": {
                            "rule": "a candidate needs a landed key with an unseen deciding record and an errored or "
                                    "spilled call of a deciding tool in the agents that wrote it",
                            "keys_with_unseen_records": [kd["key"] for kd in keys_detail if kd["deciding_records_unseen"]],
                            "candidates": hidden},
                        "citations": {"register_write_events": table_events,
                                                      "brief_events": sorted({b["event"] for b in tx_all})}}
    slot_targets = {}
    for s in surface.get("slots") or []:
        sel = s.get("selector") or []
        if len(sel) >= 3 and sel[0] == "field":
            slot_targets[s["id"]] = {"key": sel[1], "field": sel[2]}
    channels = channel_reports(view, channels_decl, rows, truth, mod=mod, state=state, tspec=tspec,
                               table_events=table_events, graded=graded, class_field=cf, key_events=key_events,
                               deciders=slot_deciders, slot_targets=slot_targets)
    special = {c["over_application"] for c in controls_decl.values() if c["over_application"]} | \
        {c.get("degrade") for c in channels_decl.values()}
    # degrade nodes (e.g. trusting a stale export); over-application operators and channel degrades are reported above
    degrades = {}
    for op in [o for o in getattr(mod, "DEGRADES", {}) if o not in special]:
        dg = mod.solve(state, degrade={op})
        rid = op.split(":", 1)[1] if ":" in op else op
        first = view.first_seen(run.calls, need.get(rid, [rid.lower()]))
        copied = [(k, f) for k in dg for f in tspec.get("columns", []) if k in rows and f in rows[k] and f in dg[k]
                  and dg[k][f] != truth[k].get(f) and sg.compare(rows[k][f], dg[k][f], f, tspec) == "MATCH"
                  and f != cf]
        differs = sorted({k for k in dg if any(dg[k].get(f) != truth[k].get(f) for f in tspec.get("columns", []) if f != cf)})
        verdict = "NOT-REACHED" if first is None else "LANDED" if len(copied) >= trust_min else "LEAKED"
        degrades[op] = {"verdict": verdict, "first_seen_event": first, "values_copied": len(copied),
                        "copied": copied[:20], "rows_where_it_differs_from_truth": len(differs),
                        "rule": f"LANDED = read and >= {trust_min} register values copied where it contradicts the truth"}
    # reach nodes: every manifest fragment, authority and decoy record
    reach = {}
    for f in (manifest or {}).get("ask_fragments", []) or []:
        for rid in (f.get("seeded_ids") or []) + (f.get("base_pointers") or []):
            reach[f"{f['id']}:{rid}"] = view.first_seen(run.calls, need.get(rid, [str(rid).lower()]))
    for a in (manifest or {}).get("authorities", []) or []:
        for rid in a.get("seeded_ids") or []:
            reach[f"{a['id']}:{rid}"] = view.first_seen(run.calls, need.get(rid, [str(rid).lower()]))
        for rid in a.get("decoy_seeded_ids") or []:
            reach[f"{a['id']}-decoy:{rid}"] = view.first_seen(run.calls, need.get(rid, [str(rid).lower()]))
    review = sorted({e for x in out_rules.values() for e in x["citations"]["brief_events"]} |
                    {e for x in out_rules.values() for kd in x["keys"] for e in kd["deciding_records_seen"].values()} |
                    {w["event"] for x in out_rules.values() for kd in x["keys"] for w in kd["worker_writes"]} | set(table_events))
    unclassified = [{"event": c["event"], "tool": c["name"]} for c in run.calls
                    if not str(c["name"]).startswith("mcp__") and c["name"] not in tl.BRIEF_TOOLS + FILE_TOOLS +
                    ("Read", "Bash", "Grep", "Glob", "TodoWrite", "ToolSearch", "SendMessage", "TaskOutput", "KillShell",
                     "BashOutput", "WebFetch", "WebSearch", "NotebookEdit", "ExitPlanMode", "TaskStop", "Monitor")]
    return {"label": run.label, "file": tl._rel(run.path), "sha256": tl.sha256_file(run.path),
            "register": {"kind": t["kind"], "rows": len(rows), "events": table_events},
            "provenance": {"mixed_model": prov["mixed_model"], "details": prov["details"], "fallback_events": fallback_events,
                           "brief_models": prov["brief_models"], "v3_valid": prov.get("v3_valid"),
                           "expected_model": expected,
                           "models": (prov.get("model_check") or {}).get("models"),
                           "valid_for_expected": (prov.get("model_check") or {}).get("valid")},
            "items": items, "rules": out_rules, "degrades": degrades, "controls": controls, "channels": channels,
            "coverage": {"controls": sum(1 for c in controls.values() for x in c["trials"]
                                         if x["outcome"] not in ("NOT-WRITTEN", "UNOBSERVED")),
                         "channels": sum(1 for c in channels.values() if c["verdict"] != "UNOBSERVED"),
                         "dropped": _dropped(controls, channels)},
            "go_rule": go_rule(out_rules, channels, controls, items, prov, expected, rules),
            "reach_nodes": {k: ("READ", v) if v is not None else ("NOT-READ", None) for k, v in reach.items()},
            "review_queue": {"events": review[:400], "unclassified_calls": unclassified[:50],
                             "coverage": "tool-checked: register differences, deciding-record reach, brief text and "
                                         "referenced files, worker write payloads; the model must review the queued "
                                         "events before dispositioning"},
            "confounded": "never proposed; see each rule's flags"}


def evaluate_runs(report: dict, runs: list, sqls: list, *, mod, surface, manifest=None, revision=None, legacy=None,
                  trust_min=TRUST_MIN, sole_revision=None, echo=False, expected_model=None) -> int:
    """Bind every run on evidence, then evaluate it with the solver of THE REVISION IT IS BOUND TO. A run that is not
    BOUND (INSUFFICIENT, AMBIGUOUS, UNBOUND) is recorded with its binding and never evaluated: no fallback to the first
    SQL. Fills report["runs"]; returns how many runs were not bound."""
    states, bad = {}, 0
    for lab, path in runs:
        run = tl.load(path, lab)
        b = tl.binding(run, sqls, sole_revision)          # always on evidence: one candidate alone is INSUFFICIENT
        ok_, why = tl.binding_ok(b)
        if not ok_:
            bad += 1
            report["runs"][lab] = {"evaluated": False, "binding": {
                "verdict": b["verdict"], "bound_to": b.get("bound_to"), "basis": b.get("basis"), "why": why,
                "evidence": b.get("evidence"), "candidates": b.get("candidates"), "revision": None, "sql_sha256": None},
                "rules": {}, "degrades": {}, "items": [], "reach_nodes": {},
                "provenance": tl.provenance(run), "register": {"kind": None, "rows": 0}}
            if echo:
                print(f"{lab}: NOT EVALUATED - {why}; mark it historical in the intake, or bind it (--sql for every "
                      f"stored revision)")
            continue
        bound = b["bound_to"][0]
        sql_text = dict(sqls)[bound]
        if bound not in states:
            st = mod.load_state(sql_text, revision)
            states[bound] = (st, mod.solve(st), needles(sql_text), hashlib.sha256(sql_text.encode()).hexdigest())
        st, truth, need, sha = states[bound]
        st_rev = st.get("revision") if isinstance(st, dict) else getattr(st, "revision", None)
        r = verdicts_for_run(run, mod=mod, state=st, truth=truth, surface=surface, manifest=manifest, need=need,
                             legacy=legacy, trust_min=trust_min, expected_model=expected_model)
        r["evaluated"] = True
        r["binding"] = {"verdict": b["verdict"], "bound_to": b.get("bound_to"), "basis": b["basis"],
                        "sole_revision": b.get("sole_revision"), "evidence": b["evidence"], "why": why,
                        "sql_sha256": sha, "solver_revision": st_rev, "revision": str(st_rev or bound)}
        report["runs"][lab] = r
        if echo:
            landed = {k: v["landed_keys"] for k, v in r["rules"].items() if v["verdict"] == "LANDED"}
            slips = [(d["key"], d["field"]) for d in r["items"] if d["classification"] == "slip"]
            print(f"{lab}: bound {b['verdict']}:{bound} ({b['basis']}) · register {r['register']['kind']}:"
                  f"{r['register']['rows']} · LANDED {landed or 'none'} · slips {slips or 'none'} · degrades "
                  f"{ {op: (v['verdict'], v['values_copied']) for op, v in r['degrades'].items()} }"
                  + (" · MIXED-MODEL" if r["provenance"]["mixed_model"] else "")
                  + ("" if r["provenance"]["v3_valid"] else " · V3-INVALID"))
            for rule, v in r["rules"].items():
                for f in v["flags"]:
                    print(f"    - {rule}: {f}")
            for rule, c in r["controls"].items():
                for x in c["trials"]:
                    if x["outcome"] == "OVER-APPLIED" or x.get("error"):
                        print(f"    - control {rule} {x['key']}: {x['outcome']} {x['written']} (truth {x['truth']}); decided "
                              f"by the {x['via']} at event {x['deciding_event']} ({x['deciding_model']})")
            for cid, c in r["channels"].items():
                print(f"    - channel {cid} ({c['kind']}): {c['verdict']} {[m['key'] for m in c['failed_members']][:8]}")
            g = r["go_rule"]
            print(f"    - go rule: {g['independent_channels']} independent loss channel(s) in {g['expected_model']}'s own "
                  f"decisions {g['channels']}; not counted {g['not_counted']['off_model_or_unregistered']}; run valid "
                  f"{g['run_valid']}")
    return bad


# ------------------------------------------------------------------ reference comparison and ledger proposals

def reference_landed(ref_items: list, rules: dict, class_field: str, legacy=None,
                     context: dict | None = None, unresolved: set | None = None) -> dict:
    """{rule: keys} a reference's items imply under the classification rules: a key lands for a rule when an item the
    rule decides is reproduced by ignoring it. A class item is judged only by the shared class predicate from the
    observed row and full ablation row; another wrong field does not veto it, because the predicate already checks
    that the ablation leaves every written column equal. A diff-only item that cannot supply that context is added to
    `unresolved` instead of being synthesized into either a landing or an empty landed-key set. Rules outside `legacy`
    are not judged.

    The trichotomy (H1 residual c): a reference item lands only when the classifier would also land it. An item labelled
    cascade, mechanism?, mechanism (ambiguous) or control lands nothing and, when it names an ablation, is recorded in
    `unresolved` so the comparison reports a contract disagreement instead of silently agreeing. A class item whose
    own label is not "mechanism" never lands, even with a stale reproduced_by_ignoring list."""
    out = collections.defaultdict(set)
    for d in ref_items:
        cls = d.get("classification")
        if cls == "representation":
            continue
        if cls is not None and cls != "mechanism":
            for r in d.get("reproduced_by_ignoring") or []:
                if ((legacy is None or r in legacy) and r in rules
                        and d.get("field") in (rules[r].get("decides") or []) and unresolved is not None):
                    unresolved.add((_parents(rules, [r])[0], d["key"]))
            continue
        for r in d.get("reproduced_by_ignoring") or []:
            if not ((legacy is None or r in legacy) and r in rules
                    and d["field"] in (rules[r].get("decides") or [])):
                continue
            parent = _parents(rules, [r])[0]
            if d["field"] == class_field:
                ctx = (context or {}).get((d["key"], d["field"]))
                if ctx is None:
                    if unresolved is not None:
                        unresolved.add((parent, d["key"]))
                    continue
                ablation = (ctx.get("ablations") or {}).get(r)
                if ablation is None:
                    if unresolved is not None:
                        unresolved.add((parent, d["key"]))
                    continue
                if not class_attribution_ok(ctx.get("row") or {}, ablation, ctx.get("columns") or [],
                                            ctx.get("tspec") or {}, class_field):
                    continue
                if cls is not None and cls != "mechanism":
                    if unresolved is not None:
                        unresolved.add((parent, d["key"]))
                    continue
            out[parent].add(d["key"])
    return out


def compare_attribution(report: dict, ref: dict, *, rules: dict | None = None, class_field: str = "class",
                        legacy=None, seeds=None) -> list:
    """Items (key, field, run value, truth, reproduced_by_ignoring) against attribution.json, run by run; then, with
    `rules`, each run's landed-key set per rule against the set the reference's items imply and against the seeded
    ledger records (`seeds`: {(run, rule): (record id, keys)}). Landed-key differences carry kind "landed_keys"."""
    diffs = []
    names = {"precheck": "precheck", **{f"run-{i}": f"base-run-{i}" for i in range(1, 7)}}
    for lab, r in report["runs"].items():
        want = ref.get("runs", {}).get(names.get(lab, lab))
        if want is None:
            continue
        if not r.get("evaluated", True):
            diffs.append({"run": lab, "item": None, "grader": f"not evaluated ({r['binding']['verdict']})",
                          "reference": f"{len(want)} item(s)"})
            continue
        mine = {(d["key"], d["field"]): d for d in r["items"]}
        theirs = {(d["key"], d["field"]): d for d in want}
        for k in sorted(set(mine) | set(theirs)):
            a, b = mine.get(k), theirs.get(k)
            if a is None or b is None:
                diffs.append({"run": lab, "item": list(k), "grader": bool(a), "reference": bool(b)})
                continue
            got = a.get("reproduced_by_legacy_flags", a["reproduced_by_ignoring"])
            if str(a["run"]) != str(b["run"]) or a["truth"] != b["truth"] or sorted(got) != sorted(b["reproduced_by_ignoring"]):
                diffs.append({"run": lab, "item": list(k), "grader": [a["run"], a["truth"], got],
                              "reference": [b["run"], b["truth"], b["reproduced_by_ignoring"]]})
        if rules is None:
            continue
        ctx = {key: item["class_context"] for key, item in mine.items() if item.get("class_context")}
        unresolved = set()
        implied = reference_landed(want, rules, class_field, legacy, context=ctx, unresolved=unresolved)
        for rule, v in r["rules"].items():
            judged = legacy is None or rule in legacy          # the reference's ablations can't judge other rules
            mine_k = sorted(v["landed_keys"])
            rev = (r.get("binding") or {}).get("revision")
            seed = (seeds or {}).get((rev, lab, rule))      # a seeded record is compared whatever the reference holds
            if any(u[0] == rule for u in unresolved):
                diffs.append({"run": lab, "item": None, "kind": "reference_insufficient", "rule": rule,
                              "grader": mine_k,
                              "reference": "a reference item this classifier never lands (cascade/mechanism?/control), or "
                                           "a diff-only class item without its written row and ablation",
                              "pending_review": v.get("pending_review_keys", [])})
                continue
            ref_k = sorted(implied.get(rule, set())) if judged else None
            if (judged and mine_k != ref_k) or (seed is not None and sorted(seed[1]) != mine_k):
                diffs.append({"run": lab, "item": None, "kind": "landed_keys", "rule": rule, "grader": mine_k,
                              "reference": ref_k, "seed": {"id": seed[0], "keys": sorted(seed[1])} if seed else None,
                              "pending_review": v.get("pending_review_keys", [])})
    return diffs


def seeded_landings(ledger_path, task: str) -> dict:
    """{(revision, run, rule): (record id, keys)} for the LANDED verdict records of a task in a ledger file (read-only).
    H1-1: supersession-resolved (a correction replaces the record it supersedes, so a LANDED corrected to LEAKED no
    longer claims keys), keyed by revision as well: two revisions' run-1 must not overwrite each other."""
    rows = [json.loads(x) for x in Path(ledger_path).read_text().splitlines() if x.strip()]
    superseded = {r.get("supersedes") for r in rows if r.get("supersedes")}
    out = {}
    for x in rows:
        if x.get("kind") == "verdict" and x.get("task") == task and x["id"] not in superseded \
                and x.get("verdict") == "LANDED":
            out[(x.get("revision"), x.get("run"), x.get("node"))] = (x["id"], list(x.get("keys") or []))
    return out


def _channel_provenance(c: dict) -> tuple:
    """(models, unknown) from the members that actually produced the channel's verdict.

    A HELD channel's provenance is its held members, not the failed-member list (which is empty). A FAILED channel
    with any unknown decision must not be attributed to its one known model. Slots-only channels have no member
    objects; their failed-slot decisions are already aggregated in deciding_models / unknown_decisions.
    """
    if c["verdict"] == "FAILED":
        members = c.get("failed_members") or []
        if members:
            # a FAILED member channel's proposal covers failed AND held observations: an unknown held member is an
            # unknown decision too, never attributed to a failed member's model
            held = c.get("held_members") or []
            models = {m.get("deciding_model") for m in members + held if m.get("deciding_model")}
            unknown = (sum(1 for m in members if not m.get("deciding_model"))
                       + sum(1 for m in held if not m.get("deciding_model")))
            # declared observations with NO detail object are unknown too: reconcile with the declared counts
            declared = max(int(c.get("observed") or 0), int(c.get("held") or 0))
            unknown += max(0, declared - len(members) - len(held))
            return sorted(models), unknown
        # a FAILED slots-only channel's proposal covers failed AND held slots: recompute from the per-slot details so
        # an off-model or unknown HELD slot is neither dropped from the model set nor counted as known
        details, held = c.get("failed_slot_details") or [], c.get("held_members") or []
        if details or held or c.get("failed_slots"):
            models, unknown = set(), 0
            by_slot = {d["slot"]: d for d in details if d.get("slot")}
            for s_ in (c.get("failed_slots") or []):
                ms = set((by_slot.get(s_) or {}).get("models") or [])
                models |= ms
                unknown += 0 if ms else 1               # a failed slot with no detail is an UNKNOWN decision
            for m in held:
                ms = set(m.get("models") or []) if "models" in m else (
                    {m["deciding_model"]} if m.get("deciding_model") else set())
                models |= ms
                unknown += 0 if ms else 1
            declared = max(int(c.get("observed") or 0), int(c.get("held") or 0))
            unknown += max(0, declared - len(c.get("failed_slots") or []) - len(held))
            return sorted(models), unknown
        models = sorted(set(c.get("deciding_models") or []))
        unknown = int(c.get("unknown_decisions") or 0)
        if not unknown and not models and c.get("failed_slots"):
            unknown = len(c["failed_slots"])       # a failed slot with no recorded decider is an unknown decision
        if not (c.get("failed_slot_details") or c.get("held_members")):
            unknown = max(unknown, int(c.get("observed") or 0), int(c.get("held") or 0))   # no details at all
        return models, unknown
    models, unknown = set(), 0
    held = c.get("held_members") or []
    for m in held:
        if "models" in m:                       # a surface slot's decided_by carries a model list
            ms = set(m.get("models") or [])
        else:                                    # a register member carries one deciding_model
            ms = {m["deciding_model"]} if m.get("deciding_model") else set()
        if not ms:
            unknown += 1
        models |= ms
    declared = max(int(c.get("observed") or 0), int(c.get("held") or 0))
    unknown += max(0, declared - len(held))       # a declared HELD observation with no detail is unknown
    return sorted(models), unknown


def _dropped(controls: dict, channels: dict) -> list:
    """Every observation a run dropped, with its reason: never a trial, but never invisible either (H1 residual d)."""
    out = []
    for rule, c in (controls or {}).items():
        for x in c.get("trials") or []:
            if x.get("outcome") in ("NOT-WRITTEN", "UNOBSERVED"):
                out.append({"kind": "control", "node": rule, "key": x.get("key"), "outcome": x["outcome"],
                            "reason": ("the control member was not written in the run" if x["outcome"] == "NOT-WRITTEN"
                                       else "the row does not carry the operator's own field"),
                            "deciding_event": x.get("deciding_event")})
    for cid, c in (channels or {}).items():
        if c.get("verdict") == "UNOBSERVED":
            out.append({"kind": "channel", "node": cid, "key": None, "outcome": "UNOBSERVED",
                        "reason": c.get("why") or "nothing observed: no member written and no grade",
                        "deciding_event": c.get("deciding_event")})
    return out


def ledger_proposals(report: dict, *, task: str, source_for, harness_for) -> list:
    """One proposed record per (run, rule) of every evaluated run, stamped with THAT run's bound revision and sql_sha256
    (a batch can bind runs to different revisions). A run that is not evaluated proposes nothing."""
    out = []
    for lab, r in report["runs"].items():
        if not r.get("evaluated", True):
            continue
        b = r["binding"]
        h = harness_for(lab)
        base = {"task": task, "revision": b["revision"], "sql_sha256": b["sql_sha256"], "source": source_for(lab),
                "harness": h["harness"], "run": lab, "epistemic": "derived", "weight": 1.0}
        for rule, v in r["rules"].items():
            if v["verdict"] == "SURFACE-ONLY":
                continue                   # the register view can't judge it: never a ledger trial
            observed = {"controls": sum(1 for c in (r.get("controls") or {}).values() for x in c["trials"]
                                        if x["outcome"] not in ("NOT-WRITTEN", "UNOBSERVED")),
                        "channels": sum(1 for c in (r.get("channels") or {}).values() if c["verdict"] != "UNOBSERVED")}
            out.append(dict(base, kind="verdict", model=h["model"], node=rule, mechanism=v["mechanism"],
                            family=v["family"], verdict=v["verdict"],
                            keys=[k for k in v["landed_keys"] if k not in set(v.get("control_explained_keys") or [])],
                            evidence={"producer": VERSION, "why": v["why"], "citations": v["citations"]},
                            features={"mixed_model": r["provenance"]["mixed_model"], "flags": v["flags"],
                                      "pending_review": v.get("pending_review_keys", []),
                                      "control_explained": v.get("control_explained_keys", []),
                                      "observed_units": observed,
                                      "deciding_models": v.get("deciding_models", []),
                                      "unknown_decisions": v.get("unknown_decisions", 0),
                                      "disposition": "PROPOSED - review the queue and disposition before appending"}))
        for rule, c in (r.get("controls") or {}).items():
            for x in c["trials"]:
                if x["outcome"] in ("NOT-WRITTEN", "UNOBSERVED"):
                    continue                   # not a trial: nothing was written or nothing could be read
                out.append(dict(base, kind="control", model=x.get("deciding_model") or h["model"], node=rule,
                                key=x["key"], mechanism=c["mechanism"], family=c["family"], verdict=x["outcome"],
                                evidence={"producer": VERSION, "deciding_event": x.get("deciding_event"),
                                          "via": x.get("via"), "briefs": x.get("briefs"), "fields": x["fields"],
                                          "written": x["written"], "truth": x["truth"],
                                          "over_applied_value": x["over_applied_value"]},
                                features={"run_model": h["model"], "mixed_model": r["provenance"]["mixed_model"],
                                          "error": x["error"], "deciding_model_unknown": not x.get("deciding_model"),
                                          "disposition": "PROPOSED - a control trial, never a landing"}))
        for cid, c in (r.get("channels") or {}).items():
            if c["verdict"] == "UNOBSERVED":
                continue                   # no trial the register view can count
            models, unknown = _channel_provenance(c)
            if models and unknown == 0:
                model = models[0] if len(models) == 1 else h["model"]
                model_unknown = False
            else:
                model = h["model"]
                model_unknown = unknown > 0
            n = c["members"] or 1                     # a slots-only channel is one trial per run
            observed_members = sorted({(m.get("key") or m.get("slot")) for m in
                                       (c["failed_members"] or []) + (c.get("held_members") or [])
                                       if (m.get("key") or m.get("slot"))} | set(c.get("failed_slots") or []))
            member_events = [m.get("deciding_event") for m in
                             (c["failed_members"] or []) + (c.get("held_members") or [])
                             if isinstance(m, dict) and m.get("deciding_event") is not None]
            # the channel's own aggregate may be later than any member copy (failed slots are not in held_members)
            deciding_event = max(member_events + ([c["deciding_event"]] if c.get("deciding_event") is not None else [])) \
                if (member_events or c.get("deciding_event") is not None) else None
            out.append(dict(base, kind="channel", model=model, node=cid,
                            mechanism=c["kind"], family=c.get("family") or c["kind"], verdict=c["verdict"],
                            keys=observed_members,
                            counts=dict(c.get("counts") or {"unit": "run", "n": 1, "failed": int(c["verdict"] == "FAILED")}),
                            evidence={"producer": VERSION, "failed_members": c["failed_members"][:20],
                                      "held_members": (c.get("held_members") or [])[:20],
                                      "failed_slots": c.get("failed_slots") or [],
                                      "covered": {"members": c.get("members"), "observed": c.get("observed"),
                                                  "unobserved": c.get("unobserved")},
                                      "deciding_event": deciding_event,
                                      "deciding_run": lab, "sql_sha256": b["sql_sha256"]},
                            features={"run_model": h["model"], "deciding_models": models,
                                      "unknown_decisions": unknown,
                                      "deciding_model_unknown": model_unknown,
                                      "model_is_fallback": not (models and unknown == 0),
                                      "preregistered": c["preregistered"], "mixed_model": r["provenance"]["mixed_model"],
                                      "disposition": "PROPOSED - a complexity-channel trial"}))
    return out


# ------------------------------------------------------------------ self-test

_SOLVER = '''
import collections, json, re
KEY_REGEX = r"K-\\d{2}"
FIELDS = ["key", "count", "class"]
CLASS_FIELD = "class"
RULES = {"late": {"mechanism": "A15", "family": "A15", "requirement": "R1", "natural_reading": "latest note wins",
                  "nodes": ["T1"], "decides": ["count"], "signature": r"ignore drafts", "authority": ["auth_rule_0001"],
                  "controls": ["K-04"], "over_application": "over:late"},
         "listing": {"mechanism": "M1", "family": "A16", "requirement": "R2", "natural_reading": "skip the notes list",
                     "nodes": ["T2"], "decides": []}}
DEGRADES = {"trust:exp_sheet_0001": "copy the export", "over:late": "drop every note that mentions a draft",
            "slip:count": "misread a count by one"}
CHANNELS = {"scale:count": {"kind": "scale", "degrade": "slip:count", "members": ["K-01", "K-02", "K-03", "K-04"],
                            "source": "notes", "description": "a member's count misread by one"}}
def load_state(sql_text, revision=None):
    from base_check import parse_sql
    return {"rows": [x["row"] for x in parse_sql(sql_text) if x["op"] == "insert"], "revision": revision}
def keys():
    return ["K-01", "K-02", "K-03", "K-04"]
def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    out = {}
    for k in keys_ or keys():
        notes = [r for r in state["rows"] if r.get("issue_id") == k]
        off = "late" in disable or any(isinstance(d, tuple) and d[0] == "late" and k in d[1] for d in disable)
        on = lambda op: op in degrade or any(isinstance(d, tuple) and d[0] == op and k in d[1] for d in degrade)
        pool = notes if off else [r for r in notes if "draft rerun" not in r["body"]]
        if on("over:late"):
            pool = [r for r in pool if "draft" not in r["body"]]
        pick = max(pool, key=lambda r: r["created_at"]) if pool else None
        n = int(re.search(r"count=(\\d+)", pick["body"]).group(1)) if pick else None
        if "trust:exp_sheet_0001" in degrade:
            n = 9
        if on("slip:count") and n is not None:
            n += 1
        out[k] = {"key": k, "count": str(n) if n is not None else None, "class": "HOLD" if n else "READY", "groups": [],
                  "evidence": {"note": pick["id"] if pick else None}}
    return out
def aggregates(rows):
    return {"classes": dict(collections.Counter(v["class"] for v in rows.values())), "groups": {}}
def evidence(rows, key, field):
    return [rows[key]["evidence"]["note"]]
def touched(state, rule):
    return {r["issue_id"] for r in state["rows"] if "draft rerun" in r.get("body", "")}
def deciding(state, rule, key):
    return [r["id"] for r in state["rows"] if r.get("issue_id") == key]
'''


def _self_test() -> None:
    import base64
    sql = ("INSERT INTO linear.linear_comments (id, issue_id, body, created_at) VALUES "
           "('cmt_note_k01_a', 'K-01', 'count=2 final run of the k01 entitlement suite with every assertion recorded', '2026-01-01T00:00:00Z'), "
           "('cmt_note_k01_b', 'K-01', 'count=0 draft rerun for k01 that was abandoned before the suite finished', '2026-01-02T00:00:00Z'), "
           "('cmt_note_k02_a', 'K-02', 'count=0 final run of the k02 entitlement suite with every assertion recorded', '2026-01-01T00:00:00Z'), "
           "('cmt_note_k03_a', 'K-03', 'count=4 final run of the k03 entitlement suite with every assertion recorded', '2026-01-01T00:00:00Z'), "
           "('cmt_note_k04_a', 'K-04', 'count=3 final run of the k04 suite; the draft checklist was attached to it', '2026-01-01T00:00:00Z');\n"
           "INSERT INTO trello.trello_actions (id, data_json) VALUES ('auth_rule_0001', '{\"text\": \"ignore drafts\"}');\n")
    surface = {"kind": "GRADABLE_SURFACE", "version": 1, "classes": ["READY", "HOLD"], "truth_fields": {"class": "class"},
               "deliverables": {"register": {"kind": "table", "name_regex": "register", "key_column": "key",
                                             "key_regex": r"K-\d{2}", "columns": ["key", "count", "class"],
                                             "class_column": "class", "missing_values": ["", "missing"]}},
               "slots": []}

    def use(i, name, inp, parent=None, model="claude-opus-4-8"):
        return {"type": "assistant", "parent_tool_use_id": parent,
                "message": {"model": model, "content": [{"type": "tool_use", "id": f"t{i}", "name": name, "input": inp}]}}

    def res(i, content, parent=None):
        return {"type": "user", "parent_tool_use_id": parent, "message": {"content": [
            {"type": "tool_result", "tool_use_id": f"t{i}", "content": json.dumps({"result": json.dumps(content)})}]}}
    reg = "key,count,class\nK-01,0,READY\nK-02,missing,HOLD\nK-03,missing,HOLD\n"
    ev = [{"type": "system", "subtype": "init", "model": "claude-opus-4-8", "claude_code_version": "1"},
          use(1, "mcp__hg__trello_get_comments", {"cardId": "x"}), res(1, {"id": "auth_rule_0001", "text": "ignore drafts"}),
          use(2, "Write", {"file_path": "/app/RULES.md", "content": "Rule: ignore drafts when choosing the note."}),
          res(2, "ok"),
          use(3, "Agent", {"description": "Audit K-01..K-02", "prompt": "Read /app/RULES.md. Handle K-01..K-02."}),
          use(4, "Read", {"file_path": "/app/RULES.md"}, parent="t3"), res(4, "Rule: ignore drafts", parent="t3"),
          use(5, "mcp__hg__linear_list_comments", {"issueId": "K-01"}, parent="t3"),
          res(5, {"comments": [{"id": "cmt_note_k01_a"}, {"id": "cmt_note_k01_b"}]}, parent="t3"),
          use(6, "Write", {"file_path": "/app/out.txt", "content": "K-01 | count=0 | trace=took the rerun"}, parent="t3"),
          res(6, "ok", parent="t3"), res(3, "done"),
          use(7, "mcp__hg__gsheets_values_get", {"spreadsheetId": "exp_sheet_0001"}), res(7, {"values": "exp_sheet_0001"}),
          use(8, "mcp__hg__gdrive_create_file", {"name": "register.csv", "content": base64.b64encode(reg.encode()).decode()}),
          res(8, {"id": "f1"}),
          {"type": "result", "subtype": "success", "is_error": False}]
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("node_verdicts_selftest_") as tmp:
        sp = Path(tmp) / "solver.py"
        sp.write_text(_SOLVER)
        mod = ok.load_solver(sp)
        state = mod.load_state(sql)
        truth = mod.solve(state)
        p = Path(tmp) / "trajectory-run-1.json"
        p.write_text(json.dumps(ev))
        run = tl.load(p, "run-1")
        need = needles(sql)
        manifest = {"ask_fragments": [{"id": "K1", "seeded_ids": ["auth_rule_0001"]}, {"id": "K2", "seeded_ids": ["never_read_0001"]}]}
        r = verdicts_for_run(run, mod=mod, state=state, truth=truth, surface=surface, manifest=manifest, need=need)
        cls = {(d["key"], d["field"]): d["classification"] for d in r["items"]}
        assert cls[("K-01", "count")] == "mechanism" and cls[("K-01", "class")] == "cascade", cls
        assert cls[("K-02", "count")] == "slip" and cls[("K-02", "class")] == "cascade", cls  # K-02 not in the rule's cohort
        assert cls[("K-03", "count")] == "representation", cls                                # blank, class right
        late = r["rules"]["late"]
        assert late["verdict"] == "LANDED" and late["landed_keys"] == ["K-01"], late
        assert r["go_rule"]["not_counted"]["slips"] == ["K-02"], r["go_rule"]       # no rule acts on K-02's count
        # K-02's class HOLD equals the scale:count degrade's class only as a cascade of its missing count: not the
        # channel (planted: matching on any column attributed it)
        assert r["channels"]["scale:count"]["verdict"] == "HELD", r["channels"]
        tx = late["keys"][0]["covering_briefs"][0]
        assert not tx["text_carries"] and tx["carries"] and tx["via"].startswith("referenced file"), tx
        assert late["keys"][0]["worker_writes"][0]["line"].startswith("K-01"), late["keys"][0]
        assert "cmt_note_k01_b" in late["keys"][0]["deciding_records_seen"], late["keys"][0]
        assert r["degrades"]["trust:exp_sheet_0001"]["verdict"] == "LEAKED", r["degrades"]
        assert r["reach_nodes"]["K1:auth_rule_0001"][0] == "READ" and r["reach_nodes"]["K2:never_read_0001"][0] == "NOT-READ"
        assert all(v["verdict"] != "CONFOUNDED" for v in r["rules"].values())
        assert not late["flags"] and not late["tool_confound_check"]["candidates"], late["flags"]   # every record seen
        # one deciding record hidden behind an errored call of the deciding tool in the writer's brief: a candidate
        ev_tool = ev[:9] + [                       # ev[9] is the list_comments result; it now returns one record
            res(5, {"comments": [{"id": "cmt_note_k01_b"}]}, parent="t3"),
            use(9, "mcp__hg__linear_list_comments", {"issueId": "K-01", "cursor": "2"}, parent="t3"),
            {"type": "user", "parent_tool_use_id": "t3", "message": {"content": [
                {"type": "tool_result", "tool_use_id": "t9", "content": "upstream timeout", "is_error": True}]}}] + ev[10:]
        p.write_text(json.dumps(ev_tool))
        r4 = verdicts_for_run(tl.load(p, "run-1"), mod=mod, state=state, truth=truth, surface=surface, manifest=manifest, need=need)
        cand = r4["rules"]["late"]["tool_confound_check"]["candidates"]
        assert r4["rules"]["late"]["verdict"] == "LANDED" and [c["kind"] for c in cand] == ["error"], r4["rules"]["late"]
        assert any(f.startswith("CONFOUNDED-tool candidate") for f in r4["rules"]["late"]["flags"])
        # the deciding record never reached the worker: NOT-REACHED, not LANDED
        ev2 = [e for e in ev if not (e.get("type") == "user" and "t5" in json.dumps(e) and "cmt_note" in json.dumps(e))]
        p.write_text(json.dumps(ev2))
        r2 = verdicts_for_run(tl.load(p, "run-1"), mod=mod, state=state, truth=truth, surface=surface, manifest=manifest, need=need)
        assert r2["rules"]["late"]["verdict"] == "NOT-REACHED", r2["rules"]["late"]
        # no register at all: every rule NOT-REACHED
        p.write_text(json.dumps([e for e in ev if "gdrive_create_file" not in json.dumps(e) and "t8" not in json.dumps(e)]))
        r3 = verdicts_for_run(tl.load(p, "run-1"), mod=mod, state=state, truth=truth, surface=surface, manifest=manifest, need=need)
        assert r3["rules"]["late"]["verdict"] == "NOT-REACHED" and r3["register"]["rows"] == 0, r3["rules"]["late"]
        # planted mislabel: one batch binds two runs to two revisions; each proposal carries its own run's revision
        # and sql_sha256 (the old proposals stamped every run with the first revision's)
        marker = ("INSERT INTO linear.linear_comments (id, issue_id, body, created_at) VALUES ('{0}', 'K-09', "
                  "'marker', '2026-01-01T00:00:00Z');\n")
        sql1, sql2 = sql + marker.format("cmt_rev1_marker"), sql + marker.format("cmt_rev2_marker")
        paths = {}
        for lab, mk in (("run-1", "cmt_rev1_marker"), ("run-2", "cmt_rev2_marker"), ("run-3", None)):
            extra = [use(20, "mcp__hg__linear_list_comments", {"issueId": "K-09"}),
                     res(20, {"comments": [{"id": mk}]})] if mk else []
            paths[lab] = Path(tmp) / f"trajectory-{lab}.json"
            paths[lab].write_text(json.dumps(ev[:-1] + extra + ev[-1:]))
        rep = {"runs": {}}
        bad = evaluate_runs(rep, [(k, v) for k, v in paths.items()], [("rev-1", sql1), ("rev-2", sql2)], mod=mod,
                            surface=surface, manifest=manifest)
        b1, b2, b3 = (rep["runs"][k]["binding"] for k in ("run-1", "run-2", "run-3"))
        assert (b1["revision"], b2["revision"]) == ("rev-1", "rev-2"), (b1, b2)
        assert b1["sql_sha256"] == hashlib.sha256(sql1.encode()).hexdigest() != b2["sql_sha256"], (b1, b2)
        assert b3["verdict"] == "INSUFFICIENT" and not rep["runs"]["run-3"]["evaluated"] and bad == 1, b3
        recs = ledger_proposals(rep, task="t", source_for=lambda lab: "platform-baseline",
                                harness_for=lambda lab: {"model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}})
        by_run = {(x["run"], x["revision"], x["sql_sha256"]) for x in recs}
        assert by_run == {("run-1", "rev-1", b1["sql_sha256"]), ("run-2", "rev-2", b2["sql_sha256"])}, by_run
        # planted: one SQL alone never binds, so the run is not evaluated against it (the old SINGLE evaluated it)
        rep1 = {"runs": {}}
        assert evaluate_runs(rep1, [("run-1", paths["run-1"])], [("rev-1", sql1)], mod=mod, surface=surface) == 1
        assert rep1["runs"]["run-1"]["binding"]["verdict"] == "INSUFFICIENT" and not rep1["runs"]["run-1"]["rules"]
        rep2 = {"runs": {}}
        assert evaluate_runs(rep2, [("run-1", paths["run-1"])], [("rev-1", sql1)], mod=mod, surface=surface,
                             sole_revision="the task's first revision") == 0
        assert rep2["runs"]["run-1"]["binding"]["basis"] == "sole revision" and rep2["runs"]["run-1"]["rules"]
        # an unevaluated run the reference holds is a difference, never skipped
        assert compare_attribution(rep1, {"runs": {"base-run-1": []}})[0]["grader"].startswith("not evaluated")

        # H1 planted runs: the same trajectory with another register
        def with_register(csv_text):
            e = json.loads(json.dumps(ev))
            e[-3]["message"]["content"][0]["input"]["content"] = base64.b64encode(csv_text.encode()).decode()
            p.write_text(json.dumps(e))
            return verdicts_for_run(tl.load(p, "run-1"), mod=mod, state=state, truth=truth, surface=surface,
                                    manifest=manifest, need=need, expected_model="claude-opus-4-8")
        # an error inside the cohort that no ablation reproduces is mechanism? and pending review, never a landing
        # (the old fallback attributed it to the rule and proposed LANDED)
        ru = with_register("key,count,class\nK-01,7,HOLD\nK-02,0,READY\nK-03,4,HOLD\n")
        assert [(d["key"], d["field"], d["classification"]) for d in ru["items"]] == [("K-01", "count", "mechanism?")], ru["items"]
        assert ru["rules"]["late"]["verdict"] == "LEAKED" and ru["rules"]["late"]["pending_review_keys"] == ["K-01"]
        assert any(f.startswith("PENDING REVIEW") for f in ru["rules"]["late"]["flags"]) and \
            ru["go_rule"]["not_counted"]["pending_review"] == ["K-01"] and ru["go_rule"]["independent_channels"] == 0
        # over-applying the rule to its control member gives a control record and no landing
        ro = with_register("key,count,class\nK-01,2,HOLD\nK-02,0,READY\nK-03,4,HOLD\nK-04,missing,READY\n")
        tr = ro["controls"]["late"]["trials"]
        assert ro["rules"]["late"]["verdict"] == "LEAKED" and not ro["rules"]["late"]["landed_keys"], ro["rules"]["late"]
        assert [(x["key"], x["outcome"], x["via"], x["deciding_model"]) for x in tr] == [
            ("K-04", "OVER-APPLIED", "register write", "claude-opus-4-8")], tr
        assert ro["go_rule"]["independent_channels"] == 0 and ro["go_rule"]["not_counted"]["control_over_applications"] == ["late:K-04"]
        assert ro["rules"]["listing"]["verdict"] == "SURFACE-ONLY" and ro["channels"]["scale:count"]["verdict"] == "HELD"
        # a control member whose class matches the over-application only as a cascade of another error is HELD with
        # its error, never OVER-APPLIED (planted: matching on any column called it over-applied)
        rh = with_register("key,count,class\nK-01,2,HOLD\nK-02,0,READY\nK-03,4,HOLD\nK-04,7,READY\n")
        assert [(x["key"], x["outcome"], x["error"]) for x in rh["controls"]["late"]["trials"]] == [
            ("K-04", "HELD", True)], rh["controls"]
        # a run that does both: the landing and the control record, side by side; plus a failed scale channel
        rb = with_register("key,count,class\nK-01,0,READY\nK-02,0,READY\nK-03,5,HOLD\nK-04,missing,READY\n")
        assert rb["rules"]["late"]["verdict"] == "LANDED" and rb["rules"]["late"]["landed_keys"] == ["K-01"], rb["rules"]["late"]
        assert rb["controls"]["late"]["over_applied"] == ["K-04"], rb["controls"]
        kd = rb["rules"]["late"]["keys"][0]["decided_by"]
        assert (kd["via"], kd["deciding_event"], kd["deciding_model"]) == ("brief", 5, "claude-opus-4-8"), kd
        ch = rb["channels"]["scale:count"]
        assert ch["verdict"] == "FAILED" and [m["key"] for m in ch["failed_members"]] == ["K-03"], ch
        g = rb["go_rule"]
        assert g["independent_channels"] == 2 and g["channels"] == [["mechanism late"], ["channel scale:count"]], g
        # K-03's error is the failed channel's member, K-04's the over-applied control: neither is listed as a slip
        assert g["not_counted"]["control_over_applications"] == ["late:K-04"] and g["not_counted"]["slips"] == [], g
        # H1 residual a (classification, not just the summary): a control-explained (key, field) is its own class,
        # never a slip and never a mechanism, and it appears in no landed key
        assert [(x["key"], x["field"], x["classification"]) for x in rb["items"] if x["key"] == "K-04"] == [
            ("K-04", "count", "control"), ("K-04", "class", "cascade")], rb["items"]
        assert "K-04" not in rb["rules"]["late"]["landed_keys"], rb["rules"]["late"]
        # the proposal carries the control-explained key and lands only the unexplained one
        prb = {(x["node"], x["kind"]): x for x in ledger_proposals(
            {"runs": {"run-1": dict(rb, evaluated=True, binding={"revision": "rev-1", "sql_sha256": "0" * 64})}},
            task="t", source_for=lambda lab: "platform-baseline",
            harness_for=lambda lab: {"model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}})}
        assert prb[("late", "verdict")]["keys"] == ["K-01"] and \
            prb[("late", "verdict")]["features"]["control_explained"] == ["K-04"], prb[("late", "verdict")]
        # all-dropped provenance: the run says which observations it dropped and why, and a proposal says how many
        # units it actually observed
        assert prb[("late", "verdict")]["features"]["observed_units"] == {"controls": 1, "channels": 1}, prb
        p.write_text(json.dumps(json.loads(json.dumps(ev))))      # the go rule counts only the expected model's decisions
        e5 = verdicts_for_run(tl.load(p, "run-1"), mod=mod, state=state, truth=truth, surface=surface, manifest=manifest,
                              need=need)
        assert e5["go_rule"]["expected_model"] == "claude-opus-5-5" and e5["go_rule"]["independent_channels"] == 0
        merged = go_rule(rb["rules"], dict(rb["channels"], **{"scale:count": dict(ch, source="late")}), rb["controls"],
                         rb["items"], {}, "claude-opus-4-8", {"late": {"source": "late"}})
        assert merged["independent_channels"] == 1, merged                 # a shared source is one channel
        # H1-4: an unknown deciding model on a landing means the rule is not counted, even with one expected model
        gu = go_rule({"late": {"verdict": "LANDED", "landed_keys": ["K-01"], "deciding_models": ["claude-opus-4-8"],
                               "unknown_decisions": 1, "mechanism": "late"}}, {}, {}, [], {}, "claude-opus-4-8",
                     {"late": {"source": "notes"}})
        assert gu["independent_channels"] == 0 and gu["not_counted"]["off_model_or_unregistered"] == [
            ["mechanism late", ["claude-opus-4-8"]]], gu
        # H1 residual a: a control member's over-applied key is never a mechanism landing
        gcl = go_rule({"late": {"verdict": "LANDED", "landed_keys": ["K-03"], "deciding_models": ["claude-opus-4-8"],
                               "unknown_decisions": 0, "mechanism": "late"}}, {},
                      {"late": {"trials": [{"key": "K-03", "outcome": "OVER-APPLIED", "fields": ["count"]}],
                                "over_applied": ["K-03"]}}, [], {}, "claude-opus-4-8", {"late": {"source": "notes"}})
        assert gcl["independent_channels"] == 0, gcl
        # H1 residual a (field-level): over-applying one field does not erase the rule's other landed field
        gfield = go_rule({"late": {"verdict": "LANDED", "landed_keys": ["K-03"],
                                   "keys": [{"key": "K-03", "fields": ["count", "class"],
                                             "decided_by": {"deciding_model": "claude-opus-4-8"}}],
                                   "deciding_models": ["claude-opus-4-8"], "unknown_decisions": 0}},
                         {}, {"late": {"trials": [{"key": "K-03", "outcome": "OVER-APPLIED", "fields": ["class"]}],
                                       "over_applied": ["K-03"]}}, [], {}, "claude-opus-4-8",
                         {"late": {"source": "notes"}})
        assert gfield["independent_channels"] == 1, gfield
        # the aggregate model list is recomputed after a whole key is subtracted: K-03's off-model decision must not
        # disqualify the surviving K-05 landing
        gprov = go_rule({"late": {"verdict": "LANDED", "landed_keys": ["K-03", "K-05"],
                                  "keys": [{"key": "K-03", "fields": ["count"],
                                            "decided_by": {"deciding_model": "claude-opus-5"}},
                                           {"key": "K-05", "fields": ["receipt"],
                                            "decided_by": {"deciding_model": "claude-opus-4-8"}}],
                                  "deciding_models": ["claude-opus-4-8", "claude-opus-5"], "unknown_decisions": 0}},
                         {}, {"late": {"trials": [{"key": "K-03", "outcome": "OVER-APPLIED", "fields": ["count"]}],
                                       "over_applied": ["K-03"]}}, [], {}, "claude-opus-4-8",
                         {"late": {"source": "notes"}})
        assert gprov["independent_channels"] == 1, gprov
        # H1 residual b: a register-invisible channel that declares slots is judged on them
        _, ts = gs.table_deliverable(surface)
        ss = channel_reports(None, {"surface:declared": {"kind": "surface", "degrade": "slip:count", "members": [],
                                                         "slots": ["D1"]}}, {}, {}, mod=mod, state=state,
                             tspec=ts, table_events=[], graded={"D1": False})
        assert ss["surface:declared"]["verdict"] == "FAILED" and ss["surface:declared"]["failed_slots"] == ["D1"], ss
        # H1-8: a channel failure whose every member/field a control over-application explains is listed there, not counted
        gx = go_rule({}, {"scale:count": {"verdict": "FAILED", "failed_members": [{"key": "K-03", "fields": ["count"]}],
                                          "deciding_models": ["claude-opus-4-8"], "unknown_decisions": 0,
                                          "preregistered": True}},
                      {"late": {"trials": [{"key": "K-03", "outcome": "OVER-APPLIED", "fields": ["count"]}],
                                "over_applied": ["K-03"]}}, [], {}, "claude-opus-4-8", {})
        assert gx["independent_channels"] == 0 and gx["not_counted"]["explained_by_control"] == [
            "channel scale:count"], gx
        # two controls jointly explaining one key's fields exclude the channel (the old map kept only the last)
        gxu = go_rule({}, {"scale:count": {"verdict": "FAILED",
                                           "failed_members": [{"key": "K-03", "fields": ["count", "receipt"]}],
                                           "deciding_models": ["claude-opus-4-8"], "unknown_decisions": 0,
                                           "preregistered": True}},
                       {"a": {"trials": [{"key": "K-03", "outcome": "OVER-APPLIED", "fields": ["count"]}],
                              "over_applied": ["K-03"]},
                        "b": {"trials": [{"key": "K-03", "outcome": "OVER-APPLIED", "fields": ["receipt"]}],
                              "over_applied": ["K-03"]}}, [], {}, "claude-opus-4-8", {})
        assert gxu["independent_channels"] == 0, gxu
        # H1 residual a (slots-only): a failed slot whose (key, field) target a control over-application explains is
        # listed as control-explained, never counted as an independent channel
        gsl = go_rule({}, {"surface:deck": {"verdict": "FAILED", "failed_slots": ["D1"], "failed_members": [],
                                            "failed_slot_targets": [{"slot": "D1", "key": "K-03", "field": "count"}],
                                            "deciding_models": ["claude-opus-4-8"], "unknown_decisions": 0,
                                            "preregistered": True}},
                       {"late": {"trials": [{"key": "K-03", "outcome": "OVER-APPLIED", "fields": ["count"]}],
                                 "over_applied": ["K-03"]}}, [], {}, "claude-opus-4-8", {})
        assert gsl["independent_channels"] == 0 and gsl["not_counted"]["explained_by_control"] == [
            "channel surface:deck"], gsl
        # H1 residual a (slots, partial): only the control-explained slot is removed. A failed slot with no field
        # target stays, and the residual models / unknown count are recomputed over the survivors (a subset of mapped
        # slots is never treated as the whole channel)
        gpart = go_rule({}, {"surface:deck": {
            "verdict": "FAILED", "failed_slots": ["D1", "D2"], "failed_members": [],
            "failed_slot_targets": [{"slot": "D1", "key": "K-03", "field": "count"}],
            "failed_slot_details": [{"slot": "D1", "models": ["claude-opus-5"]},
                                    {"slot": "D2", "models": ["claude-opus-4-8"]}],
            "deciding_models": ["claude-opus-5", "claude-opus-4-8"], "unknown_decisions": 0,
            "preregistered": True}},
            {"late": {"trials": [{"key": "K-03", "outcome": "OVER-APPLIED", "fields": ["count"]}],
                      "over_applied": ["K-03"]}}, [], {}, "claude-opus-4-8", {})
        assert gpart["independent_channels"] == 1 and gpart["channels"] == [["channel surface:deck"]] and \
            gpart["not_counted"]["off_model_or_unregistered"] == [], gpart
        # the same, with the explained slot's decision unknown: its unknown status must not contaminate the residual
        gun = go_rule({}, {"surface:deck": {
            "verdict": "FAILED", "failed_slots": ["D1", "D2"], "failed_members": [],
            "failed_slot_targets": [{"slot": "D1", "key": "K-03", "field": "count"}],
            "failed_slot_details": [{"slot": "D1", "models": []}, {"slot": "D2", "models": ["claude-opus-4-8"]}],
            "deciding_models": ["claude-opus-4-8"], "unknown_decisions": 1, "preregistered": True}},
            {"late": {"trials": [{"key": "K-03", "outcome": "OVER-APPLIED", "fields": ["count"]}],
                      "over_applied": ["K-03"]}}, [], {}, "claude-opus-4-8", {})
        assert gun["independent_channels"] == 1, gun
        # H1 residual a (class): an over-application that changes ONLY the class is control-explained there, so a
        # class-deciding rule cannot land through the class (a control's class cascade cannot survive)
        ts_cls0 = {"columns": ["key", "count", "class"], "key_column": "key", "class_column": "class",
                   "missing_values": [""]}
        ic = classify({"K-04": {"key": "K-04", "count": "3", "class": "READY"}},
                      {"K-04": {"key": "K-04", "count": "3", "class": "HOLD"}},
                      {"cls": {"K-04": {"key": "K-04", "count": "3", "class": "READY"}}}, {"cls": {"K-04"}},
                      {"cls": {"mechanism": "M3", "decides": ["class"]}}, ts_cls0, "class",
                      explained={("K-04", "class")})
        assert [(d["key"], d["field"], d["classification"], d["attributed"]) for d in ic] == [
            ("K-04", "class", "control", [])], ic
        # a control-explained off-model member does not disqualify the separate expected-model member
        gxr = go_rule({}, {"scale:count": {"verdict": "FAILED", "failed_members": [
            {"key": "K-03", "fields": ["count"], "deciding_model": "claude-opus-5"},
            {"key": "K-04", "fields": ["receipt"], "deciding_model": "claude-opus-4-8"}],
            "deciding_models": ["claude-opus-4-8", "claude-opus-5"], "unknown_decisions": 0, "preregistered": True}},
                       {"a": {"trials": [{"key": "K-03", "outcome": "OVER-APPLIED", "fields": ["count"]}],
                              "over_applied": ["K-03"]}}, [], {}, "claude-opus-4-8", {})
        assert gxr["independent_channels"] == 1 and gxr["channels"] == [["channel scale:count"]], gxr
        # channel proposals keep provenance straight: a HELD channel's known held model is reported; a FAILED channel
        # with an unknown decision is not attributed to its one known model
        repc = {"runs": {"run-1": {
            "evaluated": True, "binding": {"revision": "rev-1", "sql_sha256": "0" * 64},
            "provenance": {"mixed_model": False}, "rules": {}, "controls": {},
            "channels": {
                "scale:held": {"kind": "scale", "verdict": "HELD", "members": 1, "failed_members": [],
                               "held_members": [{"key": "K-01", "deciding_model": "claude-opus-4-8",
                                                 "deciding_event": 7}],
                               "deciding_models": [], "unknown_decisions": 0, "preregistered": True,
                               "counts": {"unit": "member", "n": 1, "failed": 0}},
                "scale:unknown": {"kind": "scale", "verdict": "FAILED", "members": 1,
                                  "failed_members": [{"key": "K-03", "fields": ["count"], "deciding_model": None}],
                                  "deciding_models": [], "unknown_decisions": 1, "preregistered": True,
                                  "counts": {"unit": "member", "n": 1, "failed": 1}},
            }}}}
        pch = ledger_proposals(repc, task="t", source_for=lambda lab: "platform-baseline",
                               harness_for=lambda lab: {"model": "harness-model", "harness": {"name": "h", "version": "1"}})
        pcby = {(x["node"], x["verdict"]): x for x in pch}
        assert pcby[("scale:held", "HELD")]["model"] == "claude-opus-4-8" and \
            pcby[("scale:held", "HELD")]["features"]["deciding_model_unknown"] is False, pcby
        # H1 residual b: a HELD channel proposes its observed record set and its deciding event, not an empty trial
        assert pcby[("scale:held", "HELD")]["keys"] == ["K-01"] and \
            pcby[("scale:held", "HELD")]["evidence"]["deciding_event"] == 7, pcby[("scale:held", "HELD")]
        assert pcby[("scale:unknown", "FAILED")]["model"] == "harness-model" and \
            pcby[("scale:unknown", "FAILED")]["features"]["deciding_model_unknown"] is True, pcby
        # H1 residual f: an unknown failure is never attributed to the harness's model as a known trial
        assert pcby[("scale:unknown", "FAILED")]["features"]["model_is_fallback"] is True, pcby
        # a surviving failed slot with NO detail and a known aggregate is UNKNOWN: the aggregate is never reused
        gnt = go_rule({}, {"surface:nt": {"verdict": "FAILED", "failed_slots": ["D1"], "failed_members": [],
                                          "failed_slot_details": [], "deciding_models": ["claude-opus-4-8"],
                                          "unknown_decisions": 0, "preregistered": True}}, {}, [], {},
                       "claude-opus-4-8", {})
        assert gnt["independent_channels"] == 0, gnt
        # H1 residual b: a FAILED member channel's proposal covers failed AND held observations, so an unknown held
        # member makes the record unknown (never attributed to the failed member's model)
        repm2 = {"runs": {"run-1": {"evaluated": True, "binding": {"revision": "rev-1", "sql_sha256": "0" * 64},
                                    "provenance": {"mixed_model": False}, "rules": {}, "controls": {},
                                    "channels": {"scale:mixedheld": {
                                        "kind": "scale", "verdict": "FAILED", "members": 2, "observed": 2,
                                        "held": 1, "unobserved": 0, "preregistered": True,
                                        "failed_members": [{"key": "K-01", "fields": ["count"],
                                                            "deciding_model": "claude-opus-4-8", "deciding_event": 8}],
                                        "held_members": [{"key": "K-02", "deciding_model": None, "deciding_event": 9}],
                                        "deciding_models": ["claude-opus-4-8"], "unknown_decisions": 0,
                                        "counts": {"unit": "member", "n": 2, "failed": 1}}}}}}
        pm2 = next(x for x in ledger_proposals(
            repm2, task="t", source_for=lambda lab: "platform-baseline",
            harness_for=lambda lab: {"model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}})
            if x["kind"] == "channel")
        assert pm2["features"]["unknown_decisions"] >= 1 and pm2["features"]["model_is_fallback"] is True, pm2
        # H1 residual b (slots): a FAILED slots-only proposal covers held slots too — an off-model held slot is part of
        # the model set, and an unknown held slot is an unknown decision
        soff = channel_reports(None, {"surface:mixed": {"kind": "surface", "slots": ["D1", "D2"],
                                                        "preregistered": True}},
                               {}, {}, mod=mod, state=state, tspec=ts, table_events=[],
                               graded={"D1": False, "D2": True},
                               deciders={"D1": {"models": ["claude-opus-4-8"], "write_events": [8]},
                                         "D2": {"models": ["claude-opus-5"], "brief_events": [9]}})["surface:mixed"]
        poff = next(x for x in ledger_proposals(
            {"runs": {"run-1": {"evaluated": True, "binding": {"revision": "rev-1", "sql_sha256": "0" * 64},
                                "provenance": {"mixed_model": False}, "rules": {}, "controls": {},
                                "channels": {"surface:mixed": soff}}}},
            task="t", source_for=lambda lab: "platform-baseline",
            harness_for=lambda lab: {"model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}})
            if x["kind"] == "channel")
        assert poff["features"]["deciding_models"] == ["claude-opus-4-8", "claude-opus-5"], poff
        sunk = channel_reports(None, {"surface:unk": {"kind": "surface", "slots": ["D1", "D2"],
                                                      "preregistered": True}},
                               {}, {}, mod=mod, state=state, tspec=ts, table_events=[],
                               graded={"D1": False, "D2": True},
                               deciders={"D1": {"models": ["claude-opus-4-8"], "write_events": [8]},
                                         "D2": {"models": [], "brief_events": [9]}})["surface:unk"]
        punk = next(x for x in ledger_proposals(
            {"runs": {"run-1": {"evaluated": True, "binding": {"revision": "rev-1", "sql_sha256": "0" * 64},
                                "provenance": {"mixed_model": False}, "rules": {}, "controls": {},
                                "channels": {"surface:unk": sunk}}}},
            task="t", source_for=lambda lab: "platform-baseline",
            harness_for=lambda lab: {"model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}})
            if x["kind"] == "channel")
        assert punk["features"]["unknown_decisions"] == 1 and punk["features"]["model_is_fallback"] is True, punk
        # declared counts exceeding detail coverage: reconcile against max(observed, held) without double counting
        assert _channel_provenance({"verdict": "HELD", "observed": 3, "held": 3,
                                    "held_members": [{"key": "K-01", "deciding_model": "claude-opus-4-8"}]}) == \
            (["claude-opus-4-8"], 2)
        assert _channel_provenance({"verdict": "FAILED", "observed": 3, "held": 1, "failed_members": [],
                                    "failed_slots": ["D1"],
                                    "failed_slot_details": [{"slot": "D1", "models": ["claude-opus-4-8"]}],
                                    "held_members": []}) == (["claude-opus-4-8"], 2)
        assert _channel_provenance({"verdict": "FAILED", "observed": 2, "held": 1, "failed_members": [],
                                    "failed_slots": [], "deciding_models": ["claude-opus-4-8"],
                                    "unknown_decisions": 0}) == (["claude-opus-4-8"], 2)
        # the proposal's deciding event is the MAXIMUM of the channel aggregate and its member copies (a failed slot
        # is not in held_members, so its later event must not be overwritten by a held member's earlier one)
        p12 = next(x for x in ledger_proposals(
            {"runs": {"run-1": {"evaluated": True, "binding": {"revision": "rev-1", "sql_sha256": "0" * 64},
                                "provenance": {"mixed_model": False}, "rules": {}, "controls": {},
                                "channels": {"surface:ev": {
                                    "kind": "surface", "verdict": "FAILED", "members": 0, "observed": 2,
                                    "failed_slots": ["D1"], "held_members": [{"slot": "D2", "deciding_event": 9,
                                                                              "models": ["claude-opus-4-8"]}],
                                    "failed_slot_details": [{"slot": "D1", "models": ["claude-opus-4-8"]}],
                                    "failed_members": [], "deciding_models": ["claude-opus-4-8"],
                                    "unknown_decisions": 0, "deciding_event": 12, "preregistered": True,
                                    "counts": {"unit": "run", "n": 1, "failed": 1}}}}}},
            task="t", source_for=lambda lab: "platform-baseline",
            harness_for=lambda lab: {"model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}})
            if x["kind"] == "channel")
        assert p12["evidence"]["deciding_event"] == 12, p12
        # H1 residual b (slots-only): a FAILED slot is part of the proposal's record set, and a HELD slots-only
        # channel carries its held slot's deciding event (events are aggregated over observed slots, not failed only)
        sfail = channel_reports(None, {"surface:bad": {"kind": "surface", "slots": ["D1"], "preregistered": True}},
                                {}, {}, mod=mod, state=state, tspec=ts, table_events=[], graded={"D1": False},
                                deciders={"D1": {"models": ["claude-opus-4-8"], "write_events": [8]}})["surface:bad"]
        pbad = next(x for x in ledger_proposals(
            {"runs": {"run-1": {"evaluated": True, "binding": {"revision": "rev-1", "sql_sha256": "0" * 64},
                                "provenance": {"mixed_model": False}, "rules": {}, "controls": {},
                                "channels": {"surface:bad": sfail}}}},
            task="t", source_for=lambda lab: "platform-baseline",
            harness_for=lambda lab: {"model": "m", "harness": {"name": "h", "version": "1"}}) if x["kind"] == "channel")
        assert pbad["keys"] == ["D1"] and pbad["evidence"]["deciding_event"] == 8, pbad
        sheld = channel_reports(None, {"surface:held": {"kind": "surface", "slots": ["D2"], "preregistered": True}},
                                {}, {}, mod=mod, state=state, tspec=ts, table_events=[], graded={"D2": True},
                                deciders={"D2": {"models": ["claude-opus-4-8"], "write_events": [9]}})["surface:held"]
        assert sheld["verdict"] == "HELD" and sheld["deciding_event"] == 9, sheld
        # H1 residual b: each observed slot's own deciding event counts; a write-backed slot must not mask a later
        # brief-only decision for another slot (per-slot aggregation, not write-events-or-brief-events for the channel)
        sboth = channel_reports(None, {"surface:held": {"kind": "surface", "slots": ["D1", "D2"], "preregistered": True}},
                                {}, {}, mod=mod, state=state, tspec=ts, table_events=[], graded={"D1": True, "D2": True},
                                deciders={"D1": {"models": ["claude-opus-4-8"], "write_events": [8]},
                                          "D2": {"models": ["claude-opus-4-8"], "brief_events": [9]}})["surface:held"]
        assert sboth["verdict"] == "HELD" and sboth["deciding_event"] == 9, sboth
        # reference_landed shares classify's class predicate: the written row and full ablation row decide; a
        # diff-only item that lacks them is unresolved, not silently landed or dropped
        ts_cls = {"columns": ["key", "count", "class"], "key_column": "key", "class_column": "class",
                  "missing_values": [""]}
        ref_cls = [{"key": "K-01", "field": "class", "run": "HOLD", "truth": "READY",
                    "reproduced_by_ignoring": ["c"]}]
        rules_cls = {"c": {"decides": ["class", "count"]}}
        ctx_ok = {("K-01", "class"): {"row": {"count": "0", "class": "HOLD"},
                                      "ablations": {"c": {"count": "0", "class": "HOLD"}},
                                      "columns": ["count", "class"], "tspec": ts_cls}}
        assert reference_landed(ref_cls, rules_cls, "class", context=ctx_ok) == {"c": {"K-01"}}, \
            reference_landed(ref_cls, rules_cls, "class", context=ctx_ok)
        ctx_bad = {("K-01", "class"): {"row": {"count": "0", "class": "HOLD"},
                                       "ablations": {"c": {"count": "1", "class": "HOLD"}},
                                       "columns": ["count", "class"], "tspec": ts_cls}}
        assert reference_landed(ref_cls, {"c": {"decides": ["class"]}}, "class", context=ctx_bad) == {}, \
            reference_landed(ref_cls, {"c": {"decides": ["class"]}}, "class", context=ctx_bad)
        unresolved = set()
        assert reference_landed(ref_cls, {"c": {"decides": ["class"]}}, "class", unresolved=unresolved) == {}
        assert ("c", "K-01") in unresolved, unresolved
        # H1 residual c: a reference item the classifier would never land (cascade / mechanism? / control) lands
        # nothing, even with a stale reproduced_by_ignoring flag list, and is recorded as a contract disagreement
        for bad_cls in ("cascade", "mechanism?", "mechanism (ambiguous)", "control", "slip"):
            ub = set()
            assert reference_landed([dict(ref_cls[0], classification=bad_cls)], rules_cls, "class",
                                    context=ctx_ok, unresolved=ub) == {} and ("c", "K-01") in ub, (bad_cls, ub)
        # another wrong field does not veto class attribution when the ablation matches the written row; the count
        # item cannot land for c because c does not decide it
        ref_mixed = [
            {"key": "K-01", "field": "count", "run": "1", "truth": "0", "reproduced_by_ignoring": ["c"]},
            {"key": "K-01", "field": "class", "run": "HOLD", "truth": "READY", "reproduced_by_ignoring": ["c"]},
        ]
        ctx_mixed = {("K-01", "class"): {"row": {"count": "1", "class": "HOLD"},
                                         "ablations": {"c": {"count": "1", "class": "HOLD"}},
                                         "columns": ["count", "class"], "tspec": ts_cls}}
        assert reference_landed(ref_mixed, {"c": {"decides": ["class"]}}, "class", context=ctx_mixed) == \
            {"c": {"K-01"}}, reference_landed(ref_mixed, {"c": {"decides": ["class"]}}, "class", context=ctx_mixed)
        # H1-7: a slots-only channel carries the failed slot's deciding model and write event (it used to carry none,
        # so the go rule always excluded it); a wholly unobserved channel is UNOBSERVED and proposes nothing
        _, ts = gs.table_deliverable(surface)
        sf = channel_reports(None, {"surface:deck": {"kind": "surface", "slots": ["D1"], "preregistered": True}},
                             {}, {}, mod=mod, state=state, tspec=ts, table_events=[], graded={"D1": False},
                             deciders={"D1": {"models": ["claude-opus-4-8"], "write_events": [77], "brief_events": [5]}})
        assert sf["surface:deck"]["verdict"] == "FAILED" and sf["surface:deck"]["deciding_models"] == ["claude-opus-4-8"] \
            and sf["surface:deck"]["deciding_event"] == 77 and sf["surface:deck"]["counts"] == {
                "unit": "run", "n": 1, "failed": 1}, sf["surface:deck"]
        su = channel_reports(None, {"scale:none": {"kind": "scale", "degrade": "slip:count", "members": []}},
                             {}, {}, mod=mod, state=state, tspec=ts, table_events=[])
        assert su["scale:none"]["verdict"] == "UNOBSERVED" and su["scale:none"]["members"] == 0, su
        # H1 residual f: a failed slot with no deciding record is an UNKNOWN decision (deciders=None included)
        for dc in (None, {}, {"D1": {}}):
            snp = channel_reports(None, {"surface:none": {"kind": "surface", "slots": ["D1"], "preregistered": True}},
                                  {}, {}, mod=mod, state=state, tspec=ts, table_events=[], graded={"D1": False},
                                  deciders=dc)["surface:none"]
            assert snp["verdict"] == "FAILED" and snp["unknown_decisions"] == 1, (dc, snp)
        # an absent or ungraded slots-only grade is UNOBSERVED, never a held trial
        for grades in ({"D1": None}, {}):
            sn = channel_reports(None, {"surface:none": {"kind": "surface", "slots": ["D1"]}}, {}, {}, mod=mod,
                                 state=state, tspec=ts, table_events=[], graded=grades)
            assert sn["surface:none"]["verdict"] == "UNOBSERVED" and sn["surface:none"]["counts"]["n"] == 1, sn
        # H1-7: a held member carries its own provenance (a HELD channel used to have none)
        sh = channel_reports(RunView(run, re.compile(r"K-\d{2}")),
                             {"scale:held": {"kind": "scale", "degrade": "slip:count", "members": ["K-01"]}},
                             {"K-01": {"key": "K-01", "count": "0", "class": "READY"}},
                             {"K-01": {"key": "K-01", "count": "0", "class": "READY"}},
                             mod=mod, state=state, tspec=ts, table_events=[])
        assert sh["scale:held"]["verdict"] == "HELD" and sh["scale:held"]["held_members"][0]["key"] == "K-01", sh
        # H1-6: a control member whose own field the register does not carry is UNOBSERVED, not HELD or OVER-APPLIED
        rm = with_register("key,class\nK-01,READY\nK-02,READY\nK-03,HOLD\nK-04,HOLD\n")
        mt = rm["controls"]["late"]["trials"]
        assert [(x["key"], x["outcome"]) for x in mt] == [("K-04", "UNOBSERVED")], mt
        assert rm["channels"]["scale:count"]["verdict"] == "UNOBSERVED", rm["channels"]["scale:count"]
        repm = {"runs": {"run-1": dict(rm, evaluated=True, binding={"revision": "rev-1", "sql_sha256": "0" * 64})}}
        pm = ledger_proposals(repm, task="t", source_for=lambda lab: "platform-baseline",
                              harness_for=lambda lab: {"model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}})
        assert not [x for x in pm if x["kind"] == "control"], pm          # an unobserved control is not a trial
        # H1 residual d: a run whose every observation is dropped retains it, with the reason, and its proposal shows
        # zero observed units (never a silent "no observations at all")
        assert [(x["kind"], x["node"], x["outcome"]) for x in rm["coverage"]["dropped"]] == [
            ("control", "late", "UNOBSERVED"), ("channel", "scale:count", "UNOBSERVED")], rm["coverage"]
        pmv = next(x for x in pm if x["kind"] == "verdict" and x["node"] == "late")
        assert pmv["features"]["observed_units"] == {"controls": 0, "channels": 0}, pmv
        # H1-9: a class difference is attributed only when the class rule's ablation leaves the other written columns
        # equal; a class-only difference still lands, a class plus a moved count cascades (the planted known false
        # negative: the naive rule would land it)
        ts2 = {"columns": ["key", "count", "class"], "key_column": "key", "class_column": "class", "missing_values": [""]}
        tr2 = {"K-01": {"key": "K-01", "count": "0", "class": "READY"}}
        rl2 = {"c": {"mechanism": "M2", "decides": ["class"]}}
        conly = classify({"K-01": {"key": "K-01", "count": "0", "class": "HOLD"}}, tr2,
                         {"c": {"K-01": {"key": "K-01", "count": "0", "class": "HOLD"}}}, {"c": {"K-01"}}, rl2, ts2, "class")
        assert [(d["field"], d["classification"]) for d in conly] == [("class", "mechanism")], conly
        both = classify({"K-01": {"key": "K-01", "count": "2", "class": "HOLD"}}, tr2,
                        {"c": {"K-01": {"key": "K-01", "count": "3", "class": "HOLD"}}}, {"c": {"K-01"}}, rl2, ts2, "class")
        assert [(d["field"], d["classification"]) for d in both] == [("count", "slip"), ("class", "cascade")], both
        # the class-only row is not exempt: an ablation that changes another written column does not reproduce the row
        cbypass = classify({"K-01": {"key": "K-01", "count": "0", "class": "HOLD"}}, tr2,
                           {"c": {"K-01": {"key": "K-01", "count": "1", "class": "HOLD"}}}, {"c": {"K-01"}}, rl2, ts2,
                           "class")
        assert [(d["field"], d["classification"]) for d in cbypass] == [("class", "cascade")], cbypass
        # H1-5: the brief bound is the key's own last write, not the last table write: a later brief naming the key
        # must not become its decider
        ev_late = json.loads(json.dumps(ev))
        ev_late.insert(7, use(30, "Agent", {"description": "Audit K-01 again", "prompt": "Handle K-01 once more"}))
        ev_late.insert(8, res(30, "done"))
        p.write_text(json.dumps(ev_late))
        vw = RunView(tl.load(p, "run-1"), re.compile(r"K-\d{2}"))
        late = decider(vw, "K-01", [12], None)
        own = decider(vw, "K-01", [12], {"K-01": 6})
        assert late["deciding_event"] > own["deciding_event"], (late, own)
        p.write_text(json.dumps(ev))
        # H1-1: seeded landings are supersession-resolved and keyed by revision
        sp = Path(tmp) / "seed_ledger.jsonl"
        rec = lambda i, rev, verdict, keys, sup=None: json.dumps(
            {"id": i, "kind": "verdict", "task": "t", "revision": rev, "run": "run-1", "node": "late", "verdict": verdict,
             "keys": keys, "source": "platform-baseline", "model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"},
             "epistemic": "derived", **({"supersedes": sup} if sup else {})})
        sp.write_text("\n".join([rec("hev_a", "r1", "LANDED", ["K-01"]), rec("hev_b", "r1", "LEAKED", [], "hev_a"),
                                  rec("hev_c", "r2", "LANDED", ["K-02"])]) + "\n")
        seeds = seeded_landings(sp, "t")
        assert ("r1", "run-1", "late") not in seeds and seeds[("r2", "run-1", "late")][1] == ["K-02"], seeds
        # proposals: the verdict, the control trial and the channel; the surface-only rule is never proposed
        repb = {"runs": {"run-1": dict(rb, evaluated=True, binding={"revision": "rev-1", "sql_sha256": "0" * 64})}}
        recs = ledger_proposals(repb, task="t", source_for=lambda lab: "platform-baseline",
                                harness_for=lambda lab: {"model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}})
        assert sorted((x["kind"], x["node"], x["verdict"]) for x in recs) == [
            ("channel", "scale:count", "FAILED"), ("control", "late", "OVER-APPLIED"), ("verdict", "late", "LANDED")], recs
        assert next(x for x in recs if x["kind"] == "channel")["family"] == "scale", recs    # the channel's rate pool
        # compare_attribution compares landed-key sets: with the reference's implied set, and with a seeded record
        ref = {"runs": {"base-run-1": [d for d in rb["items"]]}}
        ld = [d for d in compare_attribution(repb, ref, rules=mod.RULES, class_field="class") if d.get("kind") == "landed_keys"]
        assert ld == [], ld
        ld = [d for d in compare_attribution(repb, ref, rules=mod.RULES, class_field="class",
                                             seeds={("rev-1", "run-1", "late"): ("hev_seed", ["K-01", "K-02"])}) if d.get("kind") == "landed_keys"]
        assert ld and ld[0]["seed"] == {"id": "hev_seed", "keys": ["K-01", "K-02"]} and ld[0]["grader"] == ["K-01"], ld
        ref2 = {"runs": {"base-run-1": rb["items"] + [{"key": "K-02", "field": "count", "run": "5", "truth": "0",
                                                         "reproduced_by_ignoring": ["late"]}]}}
        ld = [d for d in compare_attribution(repb, ref2, rules=mod.RULES, class_field="class") if d.get("kind") == "landed_keys"]
        assert ld and ld[0]["reference"] == ["K-01", "K-02"], ld
    print("self-test: ok (mechanism / slip / representation / cascade, LANDED with reach, NOT-REACHED when the deciding "
          "record never reached the worker or no register exists, brief transmission by text and by a referenced file the "
          "worker read, worker write payloads, degrade read-not-copied = LEAKED, reach nodes, CONFOUNDED never proposed, "
          "CONFOUNDED-tool candidate only when an errored deciding-tool call in the writer's brief left a record unseen; "
          "runs bound on evidence: a two-revision batch labels each proposal with its own revision and sql_sha256, "
          "an INSUFFICIENT run or a lone SQL is never evaluated, --sole-revision binds, an unevaluated reference run "
          "is a difference; H1: an unreproduced in-cohort error is mechanism? pending review (no landing), a control "
          "over-application gives a control record and no landing, a run with both gives both, a failed scale channel, "
          "every landing / trial / failed member names its deciding event and model, the go rule counts only the "
          "expected model's decisions and merges a shared source, proposals carry verdict, control and channel records "
          "and never a surface-only rule, landed-key sets compared with the reference and a seeded record)")


# ------------------------------------------------------------------ main

def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="node_verdicts.py", description="propose node verdicts per run (see docstring)")
    ap.add_argument("--task-dir", type=Path)
    ap.add_argument("--solver", type=Path)
    ap.add_argument("--sql", action="append", default=[], help="LABEL=PATH; the first is the revision under test")
    ap.add_argument("--revision", help="the solver revision for the bound SQL (default: the solver detects it)")
    ap.add_argument("--sole-revision", metavar="REASON",
                    help="the one --sql is the task's only revision (refused when the task stores another one)")
    ap.add_argument("--run", action="append", default=[])
    ap.add_argument("--surface", type=Path)
    ap.add_argument("--manifest", type=Path)
    ap.add_argument("--reference", type=Path, help="attribution.json to compare item by item and by landed keys")
    ap.add_argument("--seed-ledger", type=Path, help="a ledger whose LANDED records the landed keys are compared with "
                                                     "(read-only)")
    ap.add_argument("--expected-model", help="the runs' expected model (default: the task context's baseline_model, "
                                             "else the V3 policy model)")
    ap.add_argument("--legacy-flags", default="", help="comma list: the reference's ablation flags")
    ap.add_argument("--trust-min", type=int, default=TRUST_MIN)
    ap.add_argument("--task", default=None)
    ap.add_argument("--source", choices=("platform-precheck", "platform-baseline", "independent-harness", "probe"))
    ap.add_argument("--ledger-out", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        _self_test()
        return 0
    if a.seed_ledger and not a.reference:
        ap.error("--seed-ledger compares against --reference: give --reference ATTRIBUTION.json as well")
    td = a.task_dir
    wf = td / "Working_Files" if td else None
    solver = a.solver or (wf / "solver" / "solver.py" if wf else None)
    surface_path = a.surface or (wf / "01_Gradable_Surface.json" if wf else None)
    if not solver or not solver.is_file() or not surface_path or not surface_path.is_file():
        print("node_verdicts: need --solver and --surface (or --task-dir with Working_Files/solver/solver.py and "
              "01_Gradable_Surface.json)", file=sys.stderr)
        return 2
    mod = ok.load_solver(solver)
    surface = gs.load(surface_path)
    man_path = a.manifest or (wf / "01_Hardness_Manifest.json" if wf else None)
    manifest = json.loads(man_path.read_text()) if man_path and man_path.is_file() else None
    sqls = [(lab, p.read_text()) for lab, p in tl._pairs(a.sql)]
    if not sqls and td and (td / "01_Universe_Inject.sql").is_file():
        sqls = [("task", (td / "01_Universe_Inject.sql").read_text())]
    runs = tl._pairs(a.run) or (tl.task_runs(td) if td else [])
    if not sqls or not runs:
        print("node_verdicts: no SQL or no runs", file=sys.stderr)
        return 2
    if a.sole_revision is not None:
        if not a.sole_revision.strip() or len(sqls) != 1:
            print("node_verdicts: --sole-revision needs a reason and exactly one --sql", file=sys.stderr)
            return 2
        tl.check_sole_revision(td, sqls[0][1])
    legacy = [x for x in a.legacy_flags.split(",") if x] or None
    report = {"kind": "NODE_VERDICTS_PROPOSED", "tool": VERSION, "solver": tl._rel(solver),
              "solver_sha256": tl.sha256_file(solver), "surface": tl._rel(surface_path),
              "note": "proposals: the model dispositions each verdict after reviewing the queue; CONFOUNDED is never proposed",
              "runs": {}}
    expected = a.expected_model or tl.expected_model_for(td)
    report["expected_model"] = expected
    bad = evaluate_runs(report, runs, sqls, mod=mod, surface=surface, manifest=manifest, revision=a.revision,
                        legacy=legacy, trust_min=a.trust_min, sole_revision=a.sole_revision, echo=not a.json,
                        expected_model=expected)
    summary = collections.defaultdict(collections.Counter)
    for r in report["runs"].values():
        if not r.get("evaluated", True):
            continue
        for rule, v in r["rules"].items():
            summary[rule][v["verdict"]] += 1
        for op, v in r["degrades"].items():
            summary[op][v["verdict"]] += 1
    reach = collections.defaultdict(collections.Counter)
    for r in report["runs"].values():
        if not r.get("evaluated", True):
            continue
        for node, (st_, _) in r["reach_nodes"].items():
            reach[node][st_] += 1
    report["summary"] = {k: dict(v) for k, v in summary.items()}
    report["controls_summary"] = {rule: dict(collections.Counter(x["outcome"] for r in report["runs"].values()
                                                                 for x in (r.get("controls") or {}).get(rule, {}).get("trials", [])))
                                  for rule in ok.controls_of(mod)}
    report["channels_summary"] = {cid: dict(collections.Counter((r.get("channels") or {}).get(cid, {}).get("verdict")
                                                                for r in report["runs"].values() if r.get("evaluated", True)))
                                  for cid in ok.channels_of(mod)}
    report["reach_summary"] = {k: dict(v) for k, v in reach.items()}
    rc = 1 if bad else 0
    if a.reference:
        seeds = seeded_landings(a.seed_ledger, a.task or (td.name if td else "task")) if a.seed_ledger else None
        diffs = compare_attribution(report, json.loads(a.reference.read_text()), rules=ok.active_rules(mod, None),
                                    class_field=ok.class_field(mod), legacy=legacy, seeds=seeds)
        report["reference_comparison"] = {"reference": tl._rel(a.reference), "sha256": tl.sha256_file(a.reference),
                                          "differences": diffs}
        rc = rc or (1 if diffs else 0)
        if not a.json:
            print(f"reference comparison ({a.reference.name}): {len(diffs)} difference(s)")
            for d in diffs[:12]:
                print(f"    - {d}")
    if not a.json:
        print("summary: " + "; ".join(f"{k} {dict(v)}" for k, v in report["summary"].items()))
        never = [k for k, v in report["reach_summary"].items() if v.get("READ", 0) == 0]
        print(f"reach nodes never read in any run: {never or 'none'}")
    if a.ledger_out:
        def source_for(lab):
            return a.source or ("platform-precheck" if lab in ("precheck", "pre") else "platform-baseline")

        harness_cache = {}

        def harness_for(lab):
            if lab not in harness_cache:
                run = tl.load(dict(runs)[lab], lab)
                h = tl.harness(run.events)
                harness_cache[lab] = {"model": tl._family(h.get("init_model")) or "unrecorded",
                                      "harness": {"name": h["name"], "version": h["version"]}}
            return harness_cache[lab]
        recs = ledger_proposals(report, task=a.task or (td.name if td else "task"), source_for=source_for,
                                harness_for=harness_for)
        out = tl.safe_out(a.ledger_out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in recs))
        if not a.json:
            print(f"wrote {len(recs)} proposed ledger record(s) to {tl._rel(out)} (append after disposition)")
    if a.out:
        out = tl.safe_out(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, indent=1, ensure_ascii=False, default=sorted) + "\n")
        if not a.json:
            print(f"wrote {tl._rel(out)}")
    if a.json:
        print(json.dumps(report, indent=1, ensure_ascii=False, default=sorted))
    return rc


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"node_verdicts: {error}", file=sys.stderr)
        raise SystemExit(2)
