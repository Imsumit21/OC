#!/usr/bin/env python3
"""trajectory_ledger.py - run facts from a trajectory export: what ran, on which model, what it read and wrote.

One owner for run facts (plan §7.7, §7.9 step 1; 01a B0-B2). Reads Claude Code stream-json exports (platform
or independent harness) and the derived revision-10 call ledgers (`hardening_rev11/run-*.calls.json`).
Read-only on every input, stdlib only, never executes SQL. Writes only to explicit paths inside Task_Authoring/
and never into a frozen copy (a folder with a SHA256SUMS file above it).

  validity     final result event, error results, auto-compaction, events after the final result, unpaired calls,
               spilled results, whether the export carries the user prompt
  provenance   harness (init event), main-agent model per phase (init, model_refusal_fallback), the model of every
               call and every subagent brief, requested subagent models, the mixed-model flag
  calls        every tool call: event, id, tool, input, model, context (main | subagent of brief X), result event,
               error / failed, spilled
  briefs       every Agent/Task call: writer model, description, prompt, the cohort keys it names (lists and
               ranges), requested model, the subagent's actual models, calls under it, its result
  writes       every write call (catalog verbs) with its decoded payload: files (base64 or text, CSV rows), native
               Sheets (update / batch update / append, per spreadsheet), Linear description or patch appends,
               Slides requests, mail, Slack, sharing
  tables       a table deliverable (CSV upload or native Sheet) chosen by a spec - the rule of the proxy grader
               (support/analysis/season_pass_runs.py register()), generalised to any key column and key pattern
  binding      revision binding by content, compared by key: BOUND only on needles one candidate revision holds (or,
               with --sole-revision and no other stored revision, the one candidate's content); INSUFFICIENT when only
               shared content appears (one --sql alone is always INSUFFICIENT); AMBIGUOUS; UNBOUND
  counts       tools/difficulty_stats.count_tool_calls, the only owner of counted calls

Event numbers are 0-based indexes into the export array (as in season_pass_runs.py and plans/Rev13_Results.md).
Derived calls.json files number events from 1; they are converted on read and the original is kept as event_1b.

Usage (from the workspace root):
  python3 -B Task_Authoring/tools/trajectory_ledger.py --task-dir DIR [--run LABEL=PATH ...] [--derived LABEL=PATH ...]
      [--surface 01_Gradable_Surface.json] [--key-regex RX] [--sql LABEL=PATH ...] [--prompt 04_Prompt.txt]
      [--source platform-baseline] [--harness NAME@VERSION] [--brief-regex RX] [--out-dir DIR] [--json]
      [--sole-revision REASON]
  python3 -B Task_Authoring/tools/trajectory_ledger.py --self-test

Without --run/--derived the runs come from --task-dir: 06_PreCheck_Trajectory/trajectory.json (or the single
export there) as `precheck`, and 07_Baseline_Trajectories/*run-N*.json as `run-N`. The first --sql is the
revision under test; pass every stored revision (Working_Files/run_forensics/<rev>/01_Universe_Inject.sql) to bind
against. --sole-revision REASON is for a task's first revision only: refused when the task stores another revision, it
still runs the content check (hits: BOUND on "sole revision" with the reason and counts; none: UNBOUND). --out-dir writes, per run,
<label>/ledger.json, calls.jsonl, writes.json and briefs.json, plus summary.json.
Exit 0 = every run parsed, 1 = a run is unbound or errored, 2 = usage error.
"""
from __future__ import annotations

import argparse
import base64
import collections
import csv
import hashlib
import io
import json
import re
import sys
import tempfile
from pathlib import Path


def _bundle() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "difficulty_stats.py").is_file():
            return parent
    raise SystemExit("trajectory_ledger: cannot find the Task_Authoring bundle (no tools/difficulty_stats.py above)")


HERE = Path(__file__).resolve().parent
BUNDLE = _bundle()
WS = BUNDLE.parent
for _p in (BUNDLE / "tools", HERE):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
import difficulty_stats as ds  # noqa: E402  (counted calls and the trajectory status have one owner)

VERSION = "trajectory_ledger/1"
BRIEF_TOOLS = ("Agent", "Task")
READ_VERBS = {"get", "list", "search", "read", "show", "describe", "query", "fetch", "check", "find", "lookup",
              "count", "download", "export", "view", "submit", "status", "preview", "diff", "history", "health",
              "compare", "replies", "time"}
WRITE_VERBS = {"create", "update", "delete", "send", "reply", "share", "move", "append", "add", "trash", "restore",
               "untrash", "merge", "modify", "archive", "remove", "patch", "upload", "copy", "rename", "set", "post",
               "edit", "insert", "close", "reopen", "assign", "invite", "respond", "push", "schedule", "react"}
RX_SPILL = re.compile(r"exceeds maximum allowed tokens|Output has been saved to (\S+)", re.I)
MISSING = ("", "missing", "na", "none", "withdrawn", "nocurrentreceipt", "unavailable")


# ------------------------------------------------------------------ small helpers (ported from season_pass_runs.py)

def norm(v) -> str:
    return re.sub(r"[^a-z0-9]", "", str(v).casefold())


def unpack(v):
    """JSON strings and {"result": ...} wrappers unpacked recursively (Working_Files/hardening_intake.py)."""
    if isinstance(v, str):
        try:
            return unpack(json.loads(v))
        except (ValueError, TypeError):
            return v
    if isinstance(v, dict):
        return unpack(v["result"]) if set(v) == {"result"} else {k: unpack(x) for k, x in v.items()}
    if isinstance(v, list):
        return [unpack(x) for x in v]
    return v


def blocks(e) -> list:
    m = e.get("message") if isinstance(e, dict) else None
    c = m.get("content") if isinstance(m, dict) else None
    return c if isinstance(c, list) else []


def failed(r) -> bool:
    if r is None or r.get("error"):
        return True
    d = r.get("data")
    return isinstance(d, dict) and (bool(d.get("error")) or d.get("ok") is False)


def strings(v, out=None) -> list:
    out = [] if out is None else out
    if isinstance(v, str):
        out.append(v)
    elif isinstance(v, dict):
        for x in v.values():
            strings(x, out)
    elif isinstance(v, list):
        for x in v:
            strings(x, out)
    return out


def flat(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("\\n", " ").replace("\\", " ")).strip().lower()


def short(name: str) -> str:
    return str(name).split("__")[-1]


def is_write(name: str) -> bool:
    """Business write by its verb: the first verb token after the service prefix (catalog naming)."""
    s = short(name)
    if s == "set_acting_user":
        return False
    for tok in s.split("_")[1:]:
        if tok in READ_VERBS:
            return False
        if tok in WRITE_VERBS:
            return True
    return False


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def frozen_root(p: Path):
    for parent in [p] + list(p.parents):
        if (parent / "SHA256SUMS").is_file():
            return parent
    return None


def safe_out(p) -> Path:
    """Outputs stay inside Task_Authoring/ and never land in a frozen copy (a folder with SHA256SUMS above it)."""
    p = Path(p).resolve()
    p.relative_to(BUNDLE.resolve())
    root = frozen_root(p if p.is_dir() else p.parent)
    if root is not None:
        raise ValueError(f"refusing to write into the frozen copy {root}")
    return p


def key_regex_list(rx):
    return re.compile(rx) if rx else None


# ------------------------------------------------------------------ loading

class Run:
    """One trajectory: the events (stream-json) or the derived calls, indexed."""

    def __init__(self, label: str, path: Path, fmt: str, events, calls: list, results: dict):
        self.label, self.path, self.format = label, Path(path), fmt
        self.events, self.calls, self.results = events, calls, results
        self.uses = {c["id"]: c for c in calls}
        self._texts = None

    def result_text(self, call_id: str) -> str:
        """Every string in the unpacked result, flattened (lower case, whitespace collapsed)."""
        if self._texts is None:
            self._texts = {}
        if call_id not in self._texts:
            r = self.results.get(call_id)
            self._texts[call_id] = flat(" ".join(strings(r["data"]))) if r else ""
        return self._texts[call_id]

    def corpus(self) -> str:
        return " ".join(self.result_text(c["id"]) for c in self.calls)


def index_events(events: list):
    """(calls, results): every tool_use with its event, model and context; every tool_result (ported index_run)."""
    calls, results = [], {}
    for i, e in enumerate(events):
        if not isinstance(e, dict):
            continue
        for b in blocks(e):
            if not isinstance(b, dict):
                continue
            if b.get("type") == "tool_use":
                parent = e.get("parent_tool_use_id")
                calls.append({"event": i, "id": b.get("id"), "name": b.get("name"), "input": b.get("input", {}) or {},
                              "model": (e.get("message") or {}).get("model"), "parent": parent,
                              "context": "subagent" if parent else "main"})
            elif b.get("type") == "tool_result":
                results[b.get("tool_use_id")] = {"event": i, "error": b.get("is_error", False),
                                                 "data": unpack(b.get("content"))}
    return calls, results


def load(path, label: str | None = None) -> Run:
    path = Path(path)
    data = json.loads(path.read_text(encoding="utf-8")) if path.stat().st_size else []
    label = label or path.stem
    if isinstance(data, list) and data and isinstance(data[0], dict) and "name" in data[0] and "result" in data[0] \
            and "type" in data[0] and data[0].get("type") == "tool_use":
        calls, results = [], {}
        for c in data:   # derived revision-10 ledger: events are 1-based
            r = c.get("result") or {}
            ev = c.get("event")
            call = {"event": (ev - 1) if isinstance(ev, int) else None, "event_1b": ev, "id": c.get("id"),
                    "name": c.get("name"), "input": c.get("input", {}) or {}, "model": None,
                    "parent": c.get("parent_tool_use_id"), "context": "unknown"}
            calls.append(call)
            if r:
                rev = r.get("event")
                results[c.get("id")] = {"event": (rev - 1) if isinstance(rev, int) else None, "event_1b": rev,
                                        "error": r.get("error", False), "data": r.get("data")}
        return Run(label, path, "derived-calls", None, calls, results)
    if not isinstance(data, list):
        raise ValueError(f"{path}: not a stream-json event array or a derived calls list")
    calls, results = index_events(data)
    return Run(label, path, "stream-json", data, calls, results)


# ------------------------------------------------------------------ provenance and validity

def fallbacks(events: list) -> list:
    return [{"event": i, "category": e.get("api_refusal_category"), "scope": e.get("scope"), "trigger": e.get("trigger"),
             "original_model": e.get("original_model"), "fallback_model": e.get("fallback_model")}
            for i, e in enumerate(events or []) if isinstance(e, dict) and e.get("type") == "system"
            and e.get("subtype") == "model_refusal_fallback"]


def harness(events: list, override: str | None = None) -> dict:
    if override:
        name, _, version = override.partition("@")
        return {"name": name, "version": version or "unrecorded", "source": "--harness"}
    init = next((e for e in events or [] if isinstance(e, dict) and e.get("type") == "system"
                 and e.get("subtype") == "init"), None)
    if not init:
        return {"name": "unrecorded", "version": "unrecorded", "source": "no init event"}
    name = "claude-code" if "claude_code_version" in init else "unknown"
    return {"name": name, "version": str(init.get("claude_code_version") or "unrecorded"), "source": "init event",
            "init_model": init.get("model"), "cwd": init.get("cwd"), "session_id": init.get("session_id"),
            "permission_mode": init.get("permissionMode"), "mcp_tools": sum(1 for t in init.get("tools") or []
                                                                             if str(t).startswith("mcp__"))}


def _family(model) -> str:
    """Model family without context suffixes: claude-opus-4-8[1m] -> claude-opus-4-8."""
    return re.sub(r"\[.*?\]$", "", str(model or "")).strip()


def provenance(run: Run, briefs_: list | None = None, expected_model: str | None = None) -> dict:
    """Who ran: harness, main-agent phases, call and brief models, and the message-level model check owned by
    difficulty_stats.model_provenance (mixed_model and V3 validity are separate outcomes)."""
    events = run.events or []
    fb = fallbacks(events)
    init = harness(events).get("init_model")
    calls = run.calls
    by = collections.Counter((c["model"], c["context"]) for c in calls)
    briefs_ = briefs_ if briefs_ is not None else briefs(run)
    phases, start, model = [], 0, init
    for f in fb:
        if f.get("scope") in ("session", None):
            phases.append({"from_event": start, "to_event": f["event"], "main_model": model})
            start, model = f["event"], f.get("fallback_model")
    phases.append({"from_event": start, "to_event": len(events), "main_model": model})
    last_main = max((c["event"] for c in calls if c["context"] == "main"), default=-1)
    details, mixed = [], False
    for f in fb:
        after_calls = sum(1 for c in calls if c["context"] == "main" and c["event"] > f["event"])
        after_briefs = sum(1 for b in briefs_ if b["context"] == "main" and b["event"] > f["event"])
        if after_calls or after_briefs:
            mixed = True
            details.append(f"main agent switched to {f['fallback_model']} at event {f['event']} "
                           f"({f.get('category')}, scope {f.get('scope')}); {after_calls} main calls and {after_briefs} "
                           f"subagent briefs after it")
        else:
            details.append(f"main agent switched to {f['fallback_model']} at event {f['event']} after its last tool call "
                           f"(event {last_main}): final summary only")
    families = {_family(m) for m in by_model(events) if m and not str(m).startswith("<")}
    sub_families = {_family(c["model"]) for c in calls if c["context"] == "subagent" and c["model"]
                    and not str(c["model"]).startswith("<")}
    main_families = {_family(c["model"]) for c in calls if c["context"] == "main" and c["model"]
                     and not str(c["model"]).startswith("<")}
    if len(main_families | sub_families) > 1 and not mixed:
        mixed = True
        details.append(f"calls ran on several model families: main {sorted(main_families)}, subagents {sorted(sub_families)}")
    mc = ds.model_provenance(events, expected_model) if run.format == "stream-json" else None
    if mc:
        for o in mc["off_model"]:
            details.append(f"{o['count']} message(s) labelled {o['label']} ({o['source']}"
                           + (f", {o['subagent_briefs']} brief(s)" if o["source"] == "subagent" else "")
                           + f", events {o['first_event']}-{o['last_event']}; "
                           + (f"after the fallback at event {o['after_fallback_event']})" if o["after_fallback_event"]
                              is not None else "no fallback event before them)"))
        if mc["unknown_labels"]:
            details.append(f"unrecognised model label(s) {mc['unknown_labels']}: UNKNOWN, never valid")
        mixed = mixed or mc["mixed_model"]      # keep a fallback/call mixed signal; never let label-only reset it
    requested = sorted({b["requested_model"] for b in briefs_ if b.get("requested_model")})
    honoured = []
    for b in briefs_:
        if b.get("requested_model") and b.get("subagent_models"):
            ok = all(norm(b["requested_model"]) in norm(m) for m in b["subagent_models"])
            honoured.append(ok)
    if requested and honoured and not all(honoured):
        details.append(f"subagent model requested {requested} but the subagent events report "
                       f"{sorted({m for b in briefs_ for m in b.get('subagent_models', [])})}")
    return {"init_model": init, "fallbacks": fb, "main_model_phases": phases, "mixed_model": mixed, "details": details,
            "model_check": mc, "v3_valid": False if mixed else (mc or {}).get("v3_valid"),
            "models_seen": sorted(families), "calls_by_model_context": {f"{m}|{ctx}": n for (m, ctx), n in sorted(
                by.items(), key=lambda x: (str(x[0][0]), x[0][1]))},
            "brief_models": dict(collections.Counter(b["writer_model"] for b in briefs_)),
            "subagent_launches": len(briefs_), "requested_subagent_models": requested,
            "trajectory_models": sorted({m["label"] for m in ds.message_models(events)}) if run.format == "stream-json"
            else []}                                # = ds.trajectory_models(run.path), from the events already loaded


def deciders(run: Run, briefs_: list, keys=(), tools=()) -> dict:
    """Who decided a written value (V1: a failure is attributed to the deciding model): the briefs that name any of
    `keys`, with their writer models, and the successful write calls to `tools`, with their thread and model."""
    ks = set(keys or ())
    bs = [{"event": b["event"], "writer_model": b["writer_model"], "context": b["context"],
           "keys": sorted(ks & set(b["keys"]))} for b in briefs_ if ks & set(b["keys"])]
    ws = [{"event": c["event"], "tool": short(c["name"]), "model": c["model"], "context": c["context"]}
          for c in run.calls if short(c["name"]) in set(tools or ()) and not failed(run.results.get(c["id"]))]
    models = sorted({x["writer_model"] for x in bs if x["writer_model"]} | {x["model"] for x in ws if x["model"]})
    return {"briefs": bs, "writes": ws, "models": models}


def expected_model_for(task_dir) -> str:
    """The run's expected model: the task context's baseline_model, else the V3 policy model."""
    if task_dir:
        ctx = Path(task_dir) / "Working_Files" / "00_Task_Context.json"
        try:
            m = json.loads(ctx.read_text()).get("baseline_model")
            if m:
                return str(m)
        except (OSError, ValueError):
            pass
    return ds.V3_POLICY["model"]


def by_model(events) -> set:
    out = set()
    for e in events or []:
        if isinstance(e, dict) and e.get("type") == "assistant":
            m = (e.get("message") or {}).get("model")
            if m:
                out.add(m)
    return out


def validity(run: Run, prompt_text: str | None = None) -> dict:
    out = {"format": run.format}
    if run.format != "stream-json":
        out.update(status="derived", reason="derived call ledger: events, results and models beyond the calls are not available",
                   compactions=[], events_after_result=[], prompt_in_export=None)
        out["unpaired_calls"] = [c["event"] for c in run.calls if c["id"] not in run.results]
        return out
    status, reason, _ = ds.read_trajectory(run.path)
    events = run.events
    results_ev = [i for i, e in enumerate(events) if isinstance(e, dict) and e.get("type") == "result"]
    last = results_ev[-1] if results_ev else None
    out.update(status=status, reason=reason, events=len(events), result_events=results_ev,
               final_result={k: events[last].get(k) for k in ("subtype", "is_error", "terminal_reason", "num_turns",
                                                             "total_cost_usd", "duration_ms")} if last is not None else None,
               compactions=[{"event": i, "trigger": (e.get("compact_metadata") or {}).get("trigger")
                             if isinstance(e.get("compact_metadata"), dict) else None,
                             "pre_tokens": (e.get("compact_metadata") or {}).get("pre_tokens")
                             if isinstance(e.get("compact_metadata"), dict) else None}
                            for i, e in enumerate(events) if isinstance(e, dict) and "compact" in str(e.get("subtype", ""))],
               events_after_result=[{"event": i, "type": e.get("type"), "subtype": e.get("subtype")}
                                    for i, e in enumerate(events) if last is not None and i > last and isinstance(e, dict)])
    out["unpaired_calls"] = [{"event": c["event"], "tool": c["name"], "id": c["id"]} for c in run.calls
                             if c["id"] not in run.results]
    out["error_results"] = [{"event": c["event"], "tool": short(c["name"]), "context": c["context"],
                             "error": str(run.results[c["id"]]["data"])[:160]}
                            for c in run.calls if c["id"] in run.results and run.results[c["id"]]["error"]]
    spills = []
    for c in run.calls:
        r = run.results.get(c["id"])
        if r is None:
            continue
        text = " ".join(strings(r["data"]))
        m = RX_SPILL.search(text)
        if m:
            p = re.search(r"Output has been saved to (\S+)", text)
            spills.append({"event": c["event"], "tool": short(c["name"]), "file": p.group(1).rstrip(".,") if p else None})
    out["spilled_results"] = spills
    main_user, summaries = [], []
    for i, e in enumerate(events):
        if not isinstance(e, dict) or e.get("type") != "user" or e.get("parent_tool_use_id"):
            continue
        for t in user_texts(e):
            (summaries if e.get("isSynthetic") else main_user).append((i, t))
    out["prompt_in_export"] = bool(main_user)
    if prompt_text is not None:
        want = flat(prompt_text)
        quoted = [i for i, t in summaries if want and want in flat(t)]
        out["prompt_match"] = ("MATCH" if any(want and want in flat(t) for _, t in main_user) else "DIFFERENT"
                               if main_user else f"absent; quoted in the post-compaction summary at event {quoted[0]}"
                               if quoted else "absent from the export; bind by content")
    cont = collections.Counter(e.get("parent_tool_use_id") for e in events if isinstance(e, dict)
                               and e.get("type") == "user" and e.get("parent_tool_use_id") and e.get("isSynthetic")
                               and any(t.startswith("This session is being continued") for t in user_texts(e)))
    out["subagent_compactions"] = {"continuations": sum(cont.values()), "briefs_affected": len(cont)}
    return out


def user_texts(e) -> list:
    c = (e.get("message") or {}).get("content")
    if isinstance(c, str):
        return [c]
    return [b.get("text", "") for b in c or [] if isinstance(b, dict) and b.get("type") == "text" and b.get("text")]


# ------------------------------------------------------------------ briefs

def keys_named(text: str, key_rx) -> list:
    """Cohort keys a brief names: explicit keys plus expanded ranges (SP-001..SP-016, SP-001..016, SP-001–016,
    SP-001 through SP-016, SP-001 to SP-016)."""
    if key_rx is None or not text:
        return []
    found = []
    pat = key_rx.pattern
    m0 = re.match(r"^([A-Za-z]+-)\\d\{(\d)\}$", pat)
    for m in key_rx.finditer(text):
        found.append(m.group(0))
    if m0:
        prefix, width = m0.group(1), int(m0.group(2))
        rng = re.compile(re.escape(prefix) + r"(\d{%d})\s*(?:\.\.|–|—|-|to|through|thru)\s*(?:%s)?(\d{%d})\b"
                         % (width, re.escape(prefix), width), re.I)
        for m in rng.finditer(text):
            a, b = int(m.group(1)), int(m.group(2))
            if a < b <= a + 1000:
                found += [f"{prefix}{n:0{width}d}" for n in range(a, b + 1)]
    return sorted(set(found))


def briefs(run: Run, key_rx=None) -> list:
    out = []
    sub_models = collections.defaultdict(set)
    continued, interrupted = collections.Counter(), collections.Counter()
    for e in run.events or []:
        if isinstance(e, dict) and e.get("type") == "assistant" and e.get("parent_tool_use_id"):
            m = (e.get("message") or {}).get("model")
            if m and not str(m).startswith("<"):
                sub_models[e["parent_tool_use_id"]].add(m)
        elif isinstance(e, dict) and e.get("type") == "user" and e.get("parent_tool_use_id"):
            texts = user_texts(e)
            if e.get("isSynthetic") and any(t.startswith("This session is being continued") for t in texts):
                continued[e["parent_tool_use_id"]] += 1
            if any(t.startswith("[Request interrupted") for t in texts):
                interrupted[e["parent_tool_use_id"]] += 1
    under = collections.Counter(c["parent"] for c in run.calls if c["parent"])
    for c in run.calls:
        if c["name"] not in BRIEF_TOOLS:
            continue
        q = c["input"] or {}
        prompt = str(q.get("prompt") or "")
        desc = str(q.get("description") or "")
        r = run.results.get(c["id"])
        rtext = " ".join(strings(r["data"])) if r else ""
        out.append({"event": c["event"], "event_1b": c.get("event_1b"), "id": c["id"], "tool": c["name"],
                    "writer_model": c["model"], "context": c["context"], "parent": c["parent"],
                    "description": desc, "subagent_type": q.get("subagent_type"), "requested_model": q.get("model"),
                    "background": q.get("run_in_background"), "prompt": prompt,
                    "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()[:16], "prompt_chars": len(prompt),
                    "keys": keys_named(desc + "\n" + prompt, key_rx),
                    "subagent_models": sorted(sub_models.get(c["id"], ())), "calls_under": under.get(c["id"], 0),
                    "continuations": continued.get(c["id"], 0), "interrupted": interrupted.get(c["id"], 0),
                    "result_event": r["event"] if r else None, "result_chars": len(rtext),
                    "result_error": bool(r and r["error"])})
    return out


def brief_matches(briefs_: list, rx: str, field: str = "prompt") -> dict:
    pat = re.compile(rx)
    hits = [b for b in briefs_ if pat.search(json.dumps({"description": b["description"], "prompt": b["prompt"]},
                                                         ensure_ascii=False) if field == "input" else b.get(field) or "")]
    return {"matching": len(hits), "briefs": len(briefs_), "events": [b["event"] for b in hits],
            "writer_models": dict(collections.Counter(b["writer_model"] for b in hits))}


# ------------------------------------------------------------------ writes

def _b64_text(content):
    try:
        return base64.b64decode(content, validate=True).decode("utf-8-sig"), True
    except (ValueError, UnicodeError, TypeError):
        return content, False


def _maybe_json(v):
    if isinstance(v, str):
        try:
            return json.loads(v)
        except ValueError:
            return v
    return v


def decode_write(c: dict, r: dict | None) -> dict:
    q, n = c["input"] or {}, short(c["name"])
    out = {"event": c["event"], "id": c["id"], "tool": n, "context": c["context"], "model": c["model"],
           "ok": not failed(r), "result_event": r["event"] if r else None}
    data = r["data"] if r else None
    if n in ("gdrive_create_file", "gdrive_update_file_content") and "content" in q:
        text, b64 = _b64_text(q["content"])
        out.update(name=q.get("name"), mime_type=q.get("mimeType"), parent=q.get("parentId"), base64=b64,
                   chars=len(str(q["content"])), file_id=(data or {}).get("id") if isinstance(data, dict) else None)
        out["text"] = text if isinstance(text, str) else None
        if isinstance(text, str) and (str(q.get("mimeType", "")).endswith("csv") or str(q.get("name", "")).lower().endswith(".csv")):
            try:
                out["csv_rows"] = list(csv.reader(io.StringIO(text)))
            except csv.Error as error:
                out["csv_error"] = str(error)
    elif n == "gsheets_create_spreadsheet":
        out.update(title=q.get("title"), spreadsheet_id=(data or {}).get("spreadsheetId") if isinstance(data, dict) else None)
    elif n in ("gsheets_values_update", "gsheets_values_append"):
        out.update(spreadsheet_id=q.get("spreadsheetId"), range=q.get("range"), values=q.get("values") or [])
    elif n == "gsheets_values_batch_update":
        out.update(spreadsheet_id=q.get("spreadsheetId"), data=q.get("data") or [])
    elif n == "linear_update_issue":
        patch = _maybe_json(q.get("patch"))
        appended = [x.get("text", "") for x in patch if isinstance(x, dict)] if isinstance(patch, list) else []
        out.update(issue=q.get("id") or q.get("issueId"), state=q.get("state") or q.get("stateId"),
                   description=q.get("description"), patch=patch, appended=appended)
    elif n == "linear_create_comment":
        out.update(issue=q.get("issueId") or q.get("issue_id"), body=q.get("body"))
    elif n == "gslides_batch_update":
        reqs = _maybe_json(q.get("requests")) or []
        texts = []
        for rq in reqs if isinstance(reqs, list) else []:
            if not isinstance(rq, dict):
                continue
            if "insertText" in rq:
                texts.append(str(rq["insertText"].get("text", "")))
            if "replaceAllText" in rq:
                texts.append(str(rq["replaceAllText"].get("replaceText", "")))
        out.update(presentation_id=q.get("presentationId"), requests=reqs, texts=texts)
    elif n in ("gmail_reply_to_message", "gmail_send_message", "gmail_create_draft", "gmail_send_draft"):
        out.update(message_id=q.get("message_id"), to=q.get("to"), cc=q.get("cc"), bcc=q.get("bcc"),
                   subject=q.get("subject"), body=q.get("body"), reply_all=q.get("reply_all"),
                   attachments=q.get("attachments"))
    elif n in ("slack_send_message", "slack_conversations_add_message"):
        out.update(channel=q.get("channel_id") or q.get("channel"), thread_ts=q.get("thread_ts"),
                   text=q.get("message") or q.get("text") or q.get("payload"))
    elif n == "gdrive_share_file":
        out.update(file_id=q.get("fileId"), role=q.get("role"), type=q.get("type"), email=q.get("emailAddress"))
    elif n in ("gdrive_move_file", "gdrive_delete_file", "gdrive_trash_file"):
        out.update(file_id=q.get("fileId"), new_parent=q.get("newParentId"))
    else:
        out["input"] = q
    return out


def writes(run: Run) -> list:
    return [decode_write(c, run.results.get(c["id"])) for c in run.calls if is_write(c["name"])]


def sheet_titles(run: Run) -> dict:
    out = {}
    for c in run.calls:
        if short(c["name"]) == "gsheets_create_spreadsheet":
            r = run.results.get(c["id"])
            d = r["data"] if r else None
            if isinstance(d, dict) and d.get("spreadsheetId"):
                out[d["spreadsheetId"]] = (c["input"] or {}).get("title")
    return out


# ------------------------------------------------------------------ table deliverables

def _col_index(letters: str) -> int:
    col = 0
    for ch in letters:
        col = col * 26 + ord(ch) - 64
    return col


def keyed_rows(values: list, spec: dict) -> dict:
    """{key: {column: value}} from table rows (header rows remap the columns; ported component_rows)."""
    return _keyed_rows(values, spec)[0]


def _keyed_rows(values: list, spec: dict) -> tuple:
    """({key: {column: value}}, {key: index of its row in values}) from table rows."""
    cols = spec["columns"]
    key_col = spec["key_column"]
    key_rx = re.compile(spec["key_regex"])
    mapping = {norm(f): i for i, f in enumerate(cols)}
    rows, at = {}, {}
    for r, value in enumerate(values):
        if not isinstance(value, list) or not value:
            continue
        normalized = [norm(v) for v in value]
        if norm(key_col) in normalized:
            mapping = {v: i for i, v in enumerate(normalized)}
            continue
        ki = mapping.get(norm(key_col), 0)
        if ki >= len(value) or not key_rx.fullmatch(str(value[ki]).strip()):
            continue
        key = str(value[ki]).strip()
        rows[key] = {f: str(value[mapping[norm(f)]]).strip() for f in cols
                     if norm(f) in mapping and mapping[norm(f)] < len(value)}
        at[key] = r
    return rows, at


def table(run: Run, spec: dict) -> dict:
    """The table deliverable: the CSV upload or native Sheet with the most keyed rows.

    CSV uploads (drive create/update with content, name matching spec['name_regex']) are decoded from base64 when
    valid, else read as text; a later CSV with as many rows replaces an earlier one. Native Sheets are rebuilt per
    spreadsheet from values updates (A1 ranges), batch updates and appends (appended rows follow the grid rows); a
    Sheet replaces the CSV only with strictly more keyed rows. Failed writes are ignored. This is the rule of
    support/analysis/season_pass_runs.py register(); Sheets whose title is known must also match the name pattern.

    Round 2 (G1-3): a register write the decoder can't read is a candidate of its own with its `file_id`; because a
    later write replaces an earlier one and a write with no row count cannot be shown to lose, it becomes the
    selected table (rows {}, meta unreadable) until a later readable write re-establishes the content. So the
    uncertainty comes from the delivered register's own writes, never from "some rows exist elsewhere".

    meta["key_events"] (G1, consumed by the attribution stage) maps every key of the selected table to the last write
    event that contributed to its final row: a CSV's selected candidate event; a native Sheet's last values-update or
    append event touching the key's row."""
    name_rx = re.compile(spec.get("name_regex") or ".", re.I)
    width = len(spec["columns"])
    titles = sheet_titles(run)
    best, kind, raw, meta = {}, None, [], {}
    grids, row_events = collections.defaultdict(dict), collections.defaultdict(dict)
    appends, append_events = collections.defaultdict(list), collections.defaultdict(list)
    events = collections.defaultdict(list)
    candidates, states = [], []
    known_csv = set()
    for c in run.calls:
        q, r, n = c["input"] or {}, run.results.get(c["id"]), c["name"]
        if failed(r):
            continue
        update = "gdrive" in n and str(n).endswith("update_file")
        if "gdrive" in n and n.endswith(("create_file", "update_file")) and "content" in q \
                and (name_rx.search(str(q.get("name", ""))) or (update and q.get("fileId") in known_csv)):
            text, b64 = _b64_text(q["content"])
            # G1-3: an update's identity is the file it targets; only a create takes the result id
            fid = q.get("fileId") if str(n).endswith("update_file") else None
            if not fid:
                fid = r["data"].get("id") if isinstance(r.get("data"), dict) else None
            if fid:
                known_csv.add(fid)
            try:
                values = list(csv.reader(io.StringIO(text)))
                cand = keyed_rows(values, spec)
            except (csv.Error, TypeError) as error:
                # a register write the decoder can't read: it may be the delivered register, so it is selected and
                # its slots are UNGRADED, never false (a later readable write re-establishes the content)
                candidates.append({"kind": "CSV", "event": c["event"], "rows": None, "name": q.get("name"),
                                   "file_id": fid, "identity": fid,
                                   "error": f"{type(error).__name__}: {str(error)[:80]}"})
                best, kind, raw = {}, "CSV", []
                meta = {"event": c["event"], "name": q.get("name"), "file_id": fid, "mime_type": q.get("mimeType"),
                        "parent": q.get("parentId"), "identity": fid, "unreadable": True, "key_events": {}}
                states.append({"kind": "CSV", "last": c["event"], "rows": {}, "raw": [], "meta": meta,
                               "identity": fid, "readable": False, "bound": True})
                continue
            candidates.append({"kind": "CSV", "event": c["event"], "rows": len(cand), "name": q.get("name"),
                               "file_id": fid, "identity": fid, "base64": b64})
            cmeta = {"event": c["event"], "name": q.get("name"), "file_id": fid, "mime_type": q.get("mimeType"),
                     "parent": q.get("parentId"), "identity": fid, "key_events": {k: c["event"] for k in cand}}
            if len(cand) >= len(best):
                best, kind, raw, meta = cand, "CSV", values, cmeta
            states.append({"kind": "CSV", "last": c["event"], "rows": cand, "raw": values, "meta": cmeta,
                           "identity": fid, "readable": True, "bound": True})
        sn = short(n)
        if sn == "gsheets_values_append":
            rows_added = q.get("values") or []
            appends[q.get("spreadsheetId")].extend(rows_added)
            append_events[q.get("spreadsheetId")].extend([c["event"]] * len(rows_added))
            events[q.get("spreadsheetId")].append(c["event"])
        ups = [q] if sn == "gsheets_values_update" else (q.get("data") or []) if sn == "gsheets_values_batch_update" else []
        for u in ups:
            m = re.search(r"(?:!|^)([A-Z]+)(\d+)", str(u.get("range", "A1")))
            if not m:
                continue
            col = _col_index(m.group(1))
            sid = u.get("spreadsheetId", q.get("spreadsheetId"))
            events[sid].append(c["event"])
            for dy, vs in enumerate(u.get("values") or []):
                for dx, v in enumerate(vs):
                    grids[sid][(int(m.group(2)) - 1 + dy, col - 1 + dx)] = v
                    row = int(m.group(2)) - 1 + dy
                    row_events[sid][row] = max(row_events[sid].get(row, -1), c["event"])
    for sid in list(dict.fromkeys(list(grids) + list(appends))):
        if sid in titles and titles[sid] is not None and not name_rx.search(str(titles[sid])):
            continue
        g = grids.get(sid, {})
        grid_rows = sorted({a for a, _ in g})
        values = [[g.get((rr, cc), "") for cc in range(width)] for rr in grid_rows]
        row_event = [row_events[sid].get(rr) for rr in grid_rows]
        values += appends.get(sid, [])
        row_event += append_events.get(sid, [])
        cand, at = _keyed_rows(values, spec)
        candidates.append({"kind": "NATIVE_SHEET", "events": events.get(sid, []), "rows": len(cand),
                           "spreadsheet_id": sid, "identity": sid, "title": titles.get(sid)})
        nmeta = {"events": events.get(sid, []), "spreadsheet_id": sid, "title": titles.get(sid),
                 "identity": sid, "appended_rows": len(appends.get(sid, [])),
                 "key_events": {k: row_event[r] for k, r in at.items()}}
        # R3-1: a native Sheet is bound to this table only when its title is known and matches name_regex; an
        # untitled Sheet written and shared later is not evidence that it is this deliverable's table.
        states.append({"kind": "NATIVE_SHEET", "last": max(events.get(sid, [0]) or [0]), "rows": cand,
                       "raw": values, "meta": nmeta, "identity": sid, "readable": True,
                       "bound": bool(titles.get(sid)) and bool(name_rx.search(str(titles[sid])))})
        if len(cand) > len(best):
            best, kind, raw, meta = cand, "NATIVE_SHEET", values, nmeta
    # the delivered register is the candidate the run shared; the latest write to it decides (a later unreadable
    # write is UNGRADED, a later readable one re-establishes the content). With no share, the row-count rule above is
    # the fallback.
    shares = [str(c["input"].get("fileId")) for c in run.calls
              if short(c["name"]) == "gdrive_share_file" and not failed(run.results.get(c["id"]))]
    delivered = [s for s in states if s["identity"] and str(s["identity"]) in shares]
    bound = [s for s in delivered if s.get("bound")]
    if bound:
        delivered = bound              # an unbound candidate never displaces an identified one (R3-1)
    if delivered:
        s = max(delivered, key=lambda x: x["last"])
        return {"rows": s["rows"], "kind": s["kind"], "raw": s["raw"], "meta": s["meta"], "candidates": candidates}
    # no share: the latest write to each identity is its effective state (a smaller update replaces its own earlier
    # content), then the identity with the most keyed rows wins
    latest = {}
    for s in states:
        if s["identity"] and (s["identity"] not in latest or s["last"] >= latest[s["identity"]]["last"]):
            latest[s["identity"]] = s
    pool = list(latest.values()) or states
    if pool:
        # R10-1: an unreadable candidate bound to this deliverable has unknown cardinality, not zero: it outranks a
        # readable candidate so its slots are UNGRADED rather than guessed from a smaller readable file.
        s = max(pool, key=lambda x: (bool(x.get("bound") and not x.get("readable")), len(x["rows"]), x["last"]))
        return {"rows": s["rows"], "kind": s["kind"], "raw": s["raw"], "meta": s["meta"], "candidates": candidates}
    return {"rows": best, "kind": kind, "raw": raw, "meta": meta, "candidates": candidates}


def printed_totals(raw: list, key_regex: str, classes) -> dict:
    """Class totals written outside the keyed rows (the totals block): ['READY', '50'] or 'READY 50'."""
    krx = re.compile(key_regex)
    text = " | ".join(" ".join(str(c) for c in row) for row in raw
                      if isinstance(row, list) and not any(krx.fullmatch(str(c).strip()) for c in row))
    out = {}
    for cls in classes:
        m = re.search(r"\b" + re.escape(cls) + r"\b\D{0,20}?(\d+)", text)
        if m:
            out[cls] = int(m.group(1))
    return out


def tracker_text(run: Run, tool: str = "linear_update_issue", issue: str | None = None) -> str:
    """Text a run wrote into a Linear issue: description, appended patch text, a patch description or string."""
    texts = []
    for c in run.calls:
        if short(c["name"]) != tool or failed(run.results.get(c["id"])):
            continue
        q = c["input"] or {}
        if issue and str(q.get("id") or q.get("issueId") or "") not in (issue, ""):
            continue
        p = q.get("patch")
        if isinstance(p, str):
            try:
                p = json.loads(p)
            except ValueError:
                pass
        if q.get("description"):
            texts.append(q["description"])
        if isinstance(p, list):
            texts.extend(x.get("text", "") for x in p if isinstance(x, dict))
        elif isinstance(p, dict) and p.get("description"):
            texts.append(p["description"])
        elif isinstance(p, str):
            texts.append(p)
    return "\n".join(texts)


def write_calls(run: Run, tools) -> dict:
    """{short tool name: [calls]} for successful calls of the named tools (ported writes())."""
    out = {}
    for c in run.calls:
        n = short(c["name"])
        if n in tools and not failed(run.results.get(c["id"])):
            out.setdefault(n, []).append(c)
    return out


# ------------------------------------------------------------------ revision binding by content

KEY_COLS = ("id", "identifier", "event_id", "ical_uid", "document_id", "spreadsheet_id", "presentation_id", "object_id",
            "contact_id", "sha", "calendar_id")
TEXT_COLS = ("text", "body", "body_text", "description", "desc", "content", "snippet", "summary", "title", "name",
             "data_json")


def revision_content(sql_text: str) -> dict:
    """{"ids": row ids of 8+ characters (and Slack channel/ts), "rows": {key: flattened text}}.

    INSERT rows are keyed by table and their first id (or Slack channel/ts) and carry their longest text column; an
    UPDATE is keyed by table and its WHERE values and carries the values it sets. Keyless rows keep their text."""
    from base_check import parse_sql
    ids, rows = set(), {}
    for n, x in enumerate(parse_sql(sql_text)):
        if x["op"] == "insert":
            r = x["row"]
            keys = [r[k] for k in KEY_COLS if isinstance(r.get(k), str) and len(r[k]) >= 8]
            if x["table"] == "slack.slack_messages" and r.get("channel_id") and r.get("ts"):
                keys.append(f"{r['channel_id']}/{r['ts']}")
            ids.update(keys)
            txt = ""
            for k in TEXT_COLS:
                v = r.get(k)
                if isinstance(v, str) and len(v) > len(txt):
                    if k == "data_json":
                        try:
                            v = " ".join(strings(json.loads(v)))
                        except ValueError:
                            pass
                    txt = v
            key = f"{x['table']}:{keys[0]}" if keys else f"{x['table']}:#{n}"
        elif x["op"] == "update":
            sets = {}
            for k, v in (x.get("set") or {}).items():
                if isinstance(v, str) and k == "data_json":
                    try:
                        v = " ".join(strings(json.loads(v)))
                    except ValueError:
                        pass
                sets[k] = v
            txt = " ".join(str(v) for v in sets.values() if isinstance(v, str))
            key = f"{x['table']}:where:{json.dumps(x.get('where'), sort_keys=True, default=str)}"
        else:
            continue
        if txt:
            rows[key] = flat(txt)
    return {"ids": ids, "rows": rows}


def _windows(text: str, avoid: str, n: int = 2) -> list:
    """Up to n 40-character windows of text that occur nowhere in avoid."""
    out = []
    if len(text) < 60:
        return out
    for start in (len(text) // 2 - 20, len(text) // 3, 10, max(0, len(text) - 60), 2 * len(text) // 3):
        w = text[max(0, start):max(0, start) + 40]
        if len(w) == 40 and w not in avoid and w not in out:
            out.append(w)
            if len(out) == n:
                break
    return out


BINDING_RULE = ("needles compared by key: a row id (8+ characters, or Slack channel/ts) only one candidate revision "
                "holds, or a 40-character window of a keyed row's text that no other candidate holds (the same key with "
                "different text discriminates both ways); shared content (the same key and text in several revisions) "
                "is counted, never binding")
BINDING_BASES = ("discriminating content", "sole revision")


def binding(run: Run, candidates: list, sole_revision: str | None = None) -> dict:
    """Bind a run to the candidate revision whose discriminating content its tool results contain.

    candidates: [(label, sql_text)]. Revisions with identical parsed statements are one revision (canonical and
    comment-free copies). Verdicts:
      BOUND         exactly one revision's discriminating needles appear (basis "discriminating content"), or, with
                    sole_revision, the one candidate's content appears (basis "sole revision", with the reason)
      AMBIGUOUS     discriminating needles of two or more revisions appear
      INSUFFICIENT  only content several revisions share appears: the run saw an injection, but nothing tells the
                    revisions apart. One candidate without sole_revision is always INSUFFICIENT when its content appears
      UNBOUND       no candidate content appears
    sole_revision: the reason the one candidate is the task's only revision; the caller refuses it when the task stores
    any other revision (stored_revisions). It still runs the content check: no hits give UNBOUND."""
    from base_check import parse_sql
    groups = []
    for label, sql_text in candidates:
        sig = hashlib.sha256(json.dumps([(x["op"], x["table"], x.get("row"), x.get("where"), x.get("set"))
                                         for x in parse_sql(sql_text)], sort_keys=True, default=str).encode()).hexdigest()
        g = next((g for g in groups if g["sig"] == sig), None)
        if g is None:
            groups.append({"sig": sig, "labels": [label], "sha256": [hashlib.sha256(sql_text.encode()).hexdigest()],
                           **revision_content(sql_text)})
        else:
            g["labels"].append(label)
            g["sha256"].append(hashlib.sha256(sql_text.encode()).hexdigest())
    if sole_revision is not None and len(groups) != 1:
        raise ValueError(f"--sole-revision needs exactly one candidate revision, got {len(groups)}")
    corpus = run.corpus()
    out = []
    for g in groups:
        others = [o for o in groups if o is not g]
        other_ids = set().union(*[o["ids"] for o in others]) if others else set()
        other_txt = " \n ".join(t for o in others for t in o["rows"].values())
        disc_ids = sorted(i for i in g["ids"] if i not in other_ids)
        shared_ids = sorted(i for i in g["ids"] if i in other_ids)
        disc_w, shared_w = [], []
        for key, text in g["rows"].items():
            same_elsewhere = any(o["rows"].get(key) == text for o in others)
            if same_elsewhere or (others and text in other_txt):
                shared_w += [(key, w) for w in _windows(text, "", 1)]
            else:
                disc_w += [(key, w) for w in _windows(text, other_txt)]
        seen_ids = [i for i in disc_ids if i.lower() in corpus]
        seen_w = [(k, w) for k, w in disc_w if w in corpus]
        seen_shared = [i for i in shared_ids if i.lower() in corpus] + [k for k, w in shared_w if w in corpus]
        out.append({"labels": g["labels"], "sql_sha256": g["sha256"],
                    "unique_ids": len(disc_ids), "seen_ids": seen_ids[:40], "seen_id_count": len(seen_ids),
                    "unique_text_windows": len(disc_w), "seen_text_windows": len(seen_w),
                    "seen_window_keys": sorted({k for k, _ in seen_w})[:40],
                    "shared_needles": len(shared_ids) + len(shared_w), "shared_seen": len(seen_shared),
                    "discriminating_seen": len(seen_ids) + len(seen_w)})
    hits = [o for o in out if o["discriminating_seen"]]
    any_seen = any(o["discriminating_seen"] or o["shared_seen"] for o in out)
    basis, bound = None, None
    if len(out) == 1:
        if not any_seen:
            verdict = "UNBOUND"
        elif sole_revision is not None:
            verdict, basis, bound = "BOUND", "sole revision", out[0]["labels"]
        else:
            verdict = "INSUFFICIENT"
    elif len(hits) == 1:
        verdict, basis, bound = "BOUND", "discriminating content", hits[0]["labels"]
    elif hits:
        verdict = "AMBIGUOUS"
    else:
        verdict = "INSUFFICIENT" if any_seen else "UNBOUND"
    chosen = next((o for o in out if bound and o["labels"] == bound), None)
    why = {"BOUND": f"bound on {basis}", "AMBIGUOUS": "discriminating content of several revisions appears",
           "INSUFFICIENT": ("one candidate: content alone can't tell this revision from another one (pass every stored "
                            "revision with --sql, or --sole-revision with a reason when the task has no other revision)"
                            if len(out) == 1 else "only content the candidates share appears"),
           "UNBOUND": "no candidate's content appears in the run's tool results"}[verdict]
    return {"verdict": verdict, "bound_to": bound, "basis": basis, "sole_revision": sole_revision, "why": why,
            "evidence": {"discriminating_seen": chosen["discriminating_seen"] if chosen else 0,
                         "shared_seen": sum(o["shared_seen"] for o in out),
                         "sole_revision_hits": (out[0]["discriminating_seen"] if sole_revision is not None else None)},
            "candidates": out, "rule": BINDING_RULE}


def binding_ok(b: dict | None) -> tuple:
    """(True, why) only for a BOUND binding that records its evidence: one owner for what certifies a revision."""
    b = b or {}
    if b.get("verdict") != "BOUND":
        return False, f"binding {b.get('verdict') or 'missing'}" + (f" ({b['why']})" if b.get("why") else "")
    if b.get("basis") not in BINDING_BASES:
        return False, f"BOUND without an evidence basis (basis {b.get('basis')!r}; an unchecked label never binds)"
    if not (b.get("evidence") or {}).get("discriminating_seen"):
        return False, "BOUND without seen evidence (0 discriminating needles)"
    if b["basis"] == "sole revision" and not str(b.get("sole_revision") or "").strip():
        return False, "BOUND on sole revision without its reason"
    return True, f"BOUND on {b['basis']} ({b['evidence']['discriminating_seen']} needle(s) seen)"


def stored_revisions(task_dir: Path | None) -> list:
    """[(revision, path)]: the SQL /create-injection stores per revision, Working_Files/run_forensics/<rev>/
    01_Universe_Inject.sql."""
    if not task_dir:
        return []
    root = Path(task_dir) / "Working_Files" / "run_forensics"
    return sorted((p.parent.name, p) for p in root.glob("*/01_Universe_Inject.sql") if p.is_file())


def check_sole_revision(task_dir: Path | None, sql_text: str) -> None:
    """Raise ValueError unless the task can be checked and stores no revision other than this SQL's."""
    from base_check import parse_sql
    if not task_dir:
        raise ValueError("--sole-revision needs --task-dir, to check that the task stores no other revision")

    def sig(text):
        return hashlib.sha256(json.dumps([(x["op"], x["table"], x.get("row"), x.get("where"), x.get("set"))
                                          for x in parse_sql(text)], sort_keys=True, default=str).encode()).hexdigest()
    mine = sig(sql_text)
    other = [rev for rev, p in stored_revisions(task_dir) if sig(p.read_text(errors="replace")) != mine]
    if other:
        raise ValueError(f"--sole-revision refused: the task stores other revision(s) {other} under "
                         f"Working_Files/run_forensics/; pass every stored revision with --sql instead")


# ------------------------------------------------------------------ ledger assembly

def summarize(run: Run, *, key_rx=None, table_spec=None, sql=None, prompt_text=None, source=None, harness_override=None,
              brief_rx=None, sole_revision=None, expected_model=None) -> dict:
    bl = briefs(run, key_rx)
    prov = provenance(run, bl, expected_model)
    val = validity(run, prompt_text)
    counts = ds.count_tool_calls(run.events) if run.events is not None else _derived_counts(run)
    counts["by_tool"] = dict(collections.Counter(short(c["name"]) for c in run.calls).most_common())
    counts["briefs"] = len(bl)
    out = {"kind": "TRAJECTORY_LEDGER", "tool": VERSION, "label": run.label, "file": _rel(run.path),
           "sha256": sha256_file(run.path), "format": run.format, "event_base": 0, "source": source,
           "harness": harness(run.events, harness_override), "validity": val, "provenance": prov, "counts": counts,
           "writes": [_write_summary(w) for w in writes(run)]}
    if table_spec:
        t = table(run, table_spec)
        out["table"] = {"kind": t["kind"], "rows": len(t["rows"]), "meta": t["meta"], "candidates": t["candidates"],
                        "printed_totals": printed_totals(t["raw"], table_spec["key_regex"], table_spec.get("classes", []))}
    if sql:
        out["binding"] = binding(run, sql, sole_revision)
    if brief_rx:
        out["brief_regex"] = {"regex": brief_rx, **brief_matches(bl, brief_rx)}
    flags = []
    if val.get("status") not in ("completed", "derived"):
        flags.append(f"errored: {val.get('reason')}")
    if val.get("compactions"):
        flags.append(f"auto-compaction at event(s) {[c['event'] for c in val['compactions']]}: complete but flagged")
    sc = val.get("subagent_compactions") or {}
    if sc.get("continuations"):
        flags.append(f"subagent context compactions: {sc['continuations']} continuation(s) in {sc['briefs_affected']} "
                     f"brief(s) (see briefs.json 'continuations')")
    if prov["mixed_model"]:
        flags.append("mixed-model: " + "; ".join(prov["details"]))
    elif prov["details"]:
        flags.append("model note: " + "; ".join(prov["details"]))
    mc = prov.get("model_check")
    if mc and mc["v3_valid"] is not True:
        flags.append(f"V3 {'invalid' if mc['v3_valid'] is False else mc['v3_verdict']}: messages from {mc['models']} "
                     f"(V3 needs {ds.V3_POLICY['model']} only; a fallback run is invalid for V3)")
    if mc and mc["expected_model"] != ds.V3_POLICY["model"] and mc["valid"] != "VALID":
        flags.append(f"off the expected model {mc['expected_model']}: {mc['valid']}")
    if mc and mc["synthetic_messages"]:
        flags.append(f"{mc['synthetic_messages']} synthetic harness message(s) (<synthetic>): complete but counted")
    if val.get("events_after_result"):
        flags.append(f"{len(val['events_after_result'])} event(s) after the final result")
    if val.get("unpaired_calls"):
        flags.append(f"{len(val['unpaired_calls'])} call(s) without a result")
    if sql and not binding_ok(out["binding"])[0]:
        flags.append(f"revision binding {out['binding']['verdict']}: {out['binding']['why']}")
    out["flags"] = flags
    return out


def _derived_counts(run: Run) -> dict:
    service = [c for c in run.calls if str(c["name"]).startswith("mcp__")]
    acting = [c for c in service if str(c["name"]).endswith("set_acting_user")]
    blocked = [c for c in service if (run.results.get(c["id"]) or {}).get("error") and c not in acting]
    seen, repeats = set(), 0
    for c in service:
        if c in acting or c in blocked:
            continue
        key = (c["name"], json.dumps(c["input"], sort_keys=True))
        repeats += key in seen
        seen.add(key)
    return {"raw": len(run.calls), "service": len(service), "harness": len(run.calls) - len(service),
            "blocked": len(blocked), "repeats": repeats, "set_acting_user": len(acting),
            "counted": len(service) - len(acting) - len(blocked) - repeats,
            "note": "recomputed from the derived ledger with the difficulty_stats.count_tool_calls rule"}


def _write_summary(w: dict) -> dict:
    keep = ("event", "tool", "context", "model", "ok", "name", "mime_type", "base64", "spreadsheet_id", "range",
            "issue", "state", "presentation_id", "message_id", "reply_all", "channel", "thread_ts", "file_id", "role",
            "email", "title", "new_parent")
    out = {k: w[k] for k in keep if k in w and w[k] is not None}
    if "values" in w:
        out["rows"] = len(w["values"])
    if "csv_rows" in w:
        out["csv_rows"] = len(w["csv_rows"])
    if "appended" in w and w["appended"]:
        out["appended_chars"] = sum(len(x) for x in w["appended"])
    if w.get("description"):
        out["description_chars"] = len(w["description"])
    return out


def _rel(p: Path) -> str:
    try:
        return str(Path(p).resolve().relative_to(WS.resolve()))
    except ValueError:
        return str(p)


def write_outputs(run: Run, summary: dict, out_dir: Path, key_rx=None) -> None:
    d = safe_out(out_dir / run.label)
    d.mkdir(parents=True, exist_ok=True)
    (d / "ledger.json").write_text(json.dumps(summary, indent=1, ensure_ascii=False) + "\n")
    with open(d / "calls.jsonl", "w", encoding="utf-8") as fh:
        for c in run.calls:
            r = run.results.get(c["id"])
            text = run.result_text(c["id"])
            fh.write(json.dumps({"event": c["event"], **({"event_1b": c["event_1b"]} if "event_1b" in c else {}),
                                 "id": c["id"], "tool": c["name"], "model": c["model"], "context": c["context"],
                                 "parent": c["parent"], "input": c["input"],
                                 "result_event": r["event"] if r else None, "error": bool(r and r["error"]),
                                 "failed": failed(r), "result_chars": len(text),
                                 "spilled": bool(RX_SPILL.search(text))}, ensure_ascii=False) + "\n")
    (d / "writes.json").write_text(json.dumps(writes(run), indent=1, ensure_ascii=False) + "\n")
    (d / "briefs.json").write_text(json.dumps(briefs(run, key_rx), indent=1, ensure_ascii=False) + "\n")


# ------------------------------------------------------------------ task folder discovery

def task_runs(task_dir: Path) -> list:
    """[(label, path)] from a task folder: the pre-check and the six baseline exports."""
    out = []
    pre = task_dir / "06_PreCheck_Trajectory"
    if (pre / "trajectory.json").is_file():
        out.append(("precheck", pre / "trajectory.json"))
    elif pre.is_dir():
        found = sorted(p for p in pre.glob("*.json") if p.is_file())
        if len(found) == 1:
            out.append(("precheck", found[0]))
        elif found:
            raise ValueError(f"{pre}: {len(found)} exports and no trajectory.json - name the pre-check with --run")
    base = task_dir / "07_Baseline_Trajectories"
    if base.is_dir():
        for p in sorted(base.glob("*.json")):
            n = ds._run_number(p)
            if n is not None:
                out.append((f"run-{n}", p))
    return out


def table_spec_from_surface(surface_path: Path) -> tuple:
    """The surface's table deliverable and key regex, read through gradable_surface.load (the owner of the surface
    formats: a revision-14 surface is converted, so the briefs get their key lists); other JSON is read as it is."""
    import gradable_surface as gs        # lazy: the surface formats have one owner
    try:
        s = gs.load(surface_path)
    except ValueError:
        s = json.loads(Path(surface_path).read_text())
    d = (s.get("deliverables") or {})
    spec = next((v for v in d.values() if isinstance(v, dict) and v.get("kind") == "table"), None)
    if spec is not None:
        spec = dict(spec, classes=s.get("classes", []))
    return spec, (spec or {}).get("key_regex")


def _pairs(items) -> list:
    out = []
    for item in items or []:
        if "=" not in item:
            raise ValueError(f"expected LABEL=PATH, got {item!r}")
        a, b = item.split("=", 1)
        out.append((a, Path(b)))
    return out


# ------------------------------------------------------------------ self-test

def _fixture_events():
    """A small stream-json export covering every shape the parsers must handle."""
    def use(i, name, inp, parent=None, model="claude-opus-4-8"):
        return {"type": "assistant", "parent_tool_use_id": parent,
                "message": {"model": model, "content": [{"type": "tool_use", "id": f"t{i}", "name": name, "input": inp}]}}

    def res(i, content, err=False):
        return {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": f"t{i}",
                                                         "content": json.dumps({"result": json.dumps(content)}),
                                                         "is_error": err}]}}
    csv_text = ("component key,issue,class\nSP-001,ZOM-1,READY\nSP-002,ZOM-2,HOLD\n\nREADY,1\nHOLD,1\n")
    b64 = base64.b64encode(csv_text.encode()).decode()
    ev = [{"type": "system", "subtype": "init", "model": "claude-opus-4-8[1m]", "claude_code_version": "9.9.9",
           "tools": ["Agent", "mcp__hg__slack_send_message"], "session_id": "s1", "cwd": "/app"},
          use(1, "mcp__hg__linear_list_comments", {"issueId": "ZOM-1"}),
          res(1, {"comments": [{"id": "cmt_seeded_one", "body": "the release console export is stale"}]}),
          use(2, "Agent", {"description": "Audit SP-001..SP-002", "prompt": "Check SP-001 through SP-002; ignore the "
                           "aborted runs", "subagent_type": "general-purpose", "model": "sonnet"}),
          use(3, "mcp__hg__github_get_issue_comments", {"issue_number": 1}, parent="t2"),
          res(3, "x" * 10 + " exceeds maximum allowed tokens. Output has been saved to /tmp/tool-results/a.txt"),
          use(4, "mcp__hg__github_get_issue_comments", {"issue_number": 1}, parent="t2"),
          res(4, {"ok": True}),
          res(2, "done"),
          {"type": "system", "subtype": "compact_boundary", "compact_metadata": {"trigger": "auto", "pre_tokens": 9}},
          {"type": "system", "subtype": "model_refusal_fallback", "scope": "session", "fallback_model": "claude-opus-5[1m]",
           "original_model": "claude-opus-4-8[1m]", "api_refusal_category": "bio", "trigger": "refusal"},
          use(5, "mcp__hg__gdrive_create_file", {"name": "register.csv", "mimeType": "text/csv", "content": "!!notb64"},
              model="claude-opus-5"),
          res(5, {"error": {"code": 400, "message": "content is not valid base64"}}),
          use(6, "mcp__hg__gdrive_create_file", {"name": "register.csv", "mimeType": "text/csv", "content": b64},
              model="claude-opus-5"),
          res(6, {"id": "file1", "name": "register.csv"}),
          use(7, "mcp__hg__gsheets_create_spreadsheet", {"title": "scratch"}, model="claude-opus-5"),
          res(7, {"spreadsheetId": "sh_scratch", "title": "scratch"}),
          use(8, "mcp__hg__gsheets_values_update", {"spreadsheetId": "sh_scratch", "range": "A1",
                                                    "values": [["component key"], ["SP-001"], ["SP-002"], ["SP-003"]]},
              model="claude-opus-5"),
          res(8, {"updatedRange": "A1:A4"}),
          use(9, "mcp__hg__gsheets_values_update", {"spreadsheetId": "sh_reg", "range": "Sheet1!A1",
                                                    "values": [["component key", "issue", "class"], ["SP-001", "ZOM-1", "READY"]]},
              model="claude-opus-5"),
          res(9, {"updatedRange": "A1:C2"}),
          use(10, "mcp__hg__gsheets_values_append", {"spreadsheetId": "sh_reg", "range": "Sheet1!A1",
                                                     "values": [["SP-002", "ZOM-2", "HOLD"], ["SP-003", "ZOM-3", "WATCH"]]},
              model="claude-opus-5"),
          res(10, {"updates": 2}),
          use(11, "mcp__hg__linear_update_issue", {"id": "ZOM-9", "state": "In Validation",
                                                   "patch": json.dumps([{"op": "append", "text": "Blockers: 1 SP-002"}])},
              model="claude-opus-5"),
          res(11, {"id": "ZOM-9"}),
          use(12, "mcp__hg__linear_update_issue", {"id": "ZOM-9", "description": "original text\nmore"}, model="claude-opus-5"),
          res(12, {"id": "ZOM-9"}),
          use(13, "mcp__hg__set_acting_user", {"u": 1}, model="claude-opus-5"),
          res(13, {"ok": True}),
          use(14, "Bash", {"command": "ls"}, model="claude-opus-5"),
          {"type": "user", "parent_tool_use_id": "t2", "isSynthetic": True,
           "message": {"content": [{"type": "text", "text": "This session is being continued from a previous conversation"}]}},
          {"type": "user", "isSynthetic": True,
           "message": {"content": "This session is being continued ... the user asked: finish the handoff for me"}},
          {"type": "result", "subtype": "success", "is_error": False, "result": "done", "num_turns": 3},
          {"type": "system", "subtype": "task_notification"}]
    return ev


def _self_test() -> None:
    ev = _fixture_events()
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("trajectory_ledger_selftest_") as tmp:
        p = Path(tmp) / "trajectory-run-1.json"
        p.write_text(json.dumps(ev))
        run = load(p, "run-1")
        assert run.format == "stream-json" and len(run.calls) == 14, len(run.calls)
        krx = re.compile(r"SP-\d{3}")
        bl = briefs(run, krx)
        assert len(bl) == 1 and bl[0]["keys"] == ["SP-001", "SP-002"] and bl[0]["requested_model"] == "sonnet", bl
        assert bl[0]["calls_under"] == 2 and bl[0]["writer_model"] == "claude-opus-4-8", bl
        # a revision-14 surface goes through its owner (gradable_surface.load), so the CLI gets the key pattern and the
        # briefs their key lists (planted: the raw read found no deliverables, and every brief had keys [])
        s14 = Path(tmp) / "surface14.json"
        s14.write_text(json.dumps({"kind": "GRADABLE_SURFACE_REVISION_14", "truth": {"classes": {"READY": 1}},
                                   "slots": [{"id": "S1", "weight": 3, "selector": ["field", "SP-001", "issue"]}]}))
        spec14, krx14 = table_spec_from_surface(s14)
        assert krx14 == r"SP-\d{3}" and spec14["key_column"] == "component key", (spec14, krx14)
        assert briefs(run, key_regex_list(krx14))[0]["keys"] == ["SP-001", "SP-002"]
        prov = provenance(run, bl)
        assert prov["fallbacks"][0]["fallback_model"] == "claude-opus-5[1m]", prov
        assert prov["mixed_model"] and prov["main_model_phases"][-1]["main_model"] == "claude-opus-5[1m]", prov
        # V1: the message-level check (difficulty_stats owns the label rules): V3-invalid, and each off-model label
        # is named with its source and the fallback event before it
        mc = prov["model_check"]
        assert prov["v3_valid"] is False and mc["models"] == ["claude-opus-4-8", "claude-opus-5"], mc
        assert any("labelled claude-opus-5 (main" in d and "after the fallback at event" in d for d in prov["details"]), prov
        assert provenance(run, bl, "claude-opus-4-8")["model_check"]["valid"] == "INVALID"
        assert deciders(run, bl, keys=["SP-001"], tools=["gdrive_create_file"])["models"] == ["claude-opus-4-8",
                                                                                              "claude-opus-5"]
        val = validity(run, prompt_text="Finish the handoff for me")
        assert val["status"] == "errored" and "no final result event" in val["reason"], val   # an event after the result
        assert val["compactions"] and val["events_after_result"] and val["spilled_results"], val
        assert not val["prompt_in_export"] and val["prompt_match"].startswith("absent; quoted"), val["prompt_match"]
        assert val["subagent_compactions"] == {"continuations": 1, "briefs_affected": 1}, val["subagent_compactions"]
        assert bl[0]["continuations"] == 1, bl[0]
        assert [u["tool"] for u in val["unpaired_calls"]] == ["Bash"], val["unpaired_calls"]
        c = ds.count_tool_calls(ev)
        s = summarize(run, key_rx=krx)
        assert s["counts"]["counted"] == c["counted"] == 10 and s["counts"]["repeats"] == 1, (s["counts"], c)
        spec = {"name_regex": "register", "key_column": "component key", "key_regex": r"SP-\d{3}",
                "columns": ["component key", "issue", "class"], "classes": ["READY", "WATCH", "HOLD"]}
        t = table(run, spec)
        # the CSV (2 rows) loses only to a Sheet with strictly more rows; the 3-key scratch sheet is filtered by title
        assert t["kind"] == "NATIVE_SHEET" and sorted(t["rows"]) == ["SP-001", "SP-002", "SP-003"], t
        assert t["meta"]["spreadsheet_id"] == "sh_reg" and t["meta"]["appended_rows"] == 2, t["meta"]
        csv_only = table(run, dict(spec, name_regex="register.csv"))
        assert csv_only["kind"] == "NATIVE_SHEET"   # sh_reg has no known title: still a candidate (reference rule)
        assert printed_totals(table(Run("x", p, "stream-json", ev[:16], *index_events(ev[:16])), spec)["raw"],
                              spec["key_regex"], spec["classes"]) == {"READY": 1, "HOLD": 1}
        tt = tracker_text(run, issue="ZOM-9")
        assert "Blockers: 1 SP-002" in tt and "original text" in tt, tt
        w = {x["tool"]: x for x in writes(run)}
        assert w["gdrive_create_file"]["base64"] and w["linear_update_issue"]["issue"] == "ZOM-9", w
        assert "set_acting_user" not in w and is_write("mcp__hg__trello_create_list") and not is_write("gsheets_values_batch_get")
        # revision binding: the run saw a needle only the first revision holds
        sql_a = ("INSERT INTO linear.linear_comments (id, issue_id, body) VALUES ('cmt_seeded_one', 'ZOM-1', "
                 "'the release console export is stale and should not be trusted for any package at all');\n")
        sql_b = ("INSERT INTO linear.linear_comments (id, issue_id, body) VALUES ('cmt_seeded_two', 'ZOM-1', "
                 "'an older note about something entirely different that nobody reads in this run');\n")
        b = binding(run, [("rev-b", sql_b), ("rev-a", sql_a), ("rev-a-copy", sql_a)])
        assert b["verdict"] == "BOUND" and b["bound_to"] == ["rev-a", "rev-a-copy"], b
        assert b["basis"] == "discriminating content" and binding_ok(b)[0], b
        # planted: one candidate is never BOUND on its own (the old SINGLE / any-hit BOUND certified nothing)
        b1 = binding(run, [("rev-a", sql_a)])
        assert b1["verdict"] == "INSUFFICIENT" and not binding_ok(b1)[0], b1
        assert binding(run, [("rev-b", sql_b)])["verdict"] == "UNBOUND"
        # --sole-revision runs the content check: hits bind with the reason and counts, no hits stay UNBOUND
        bs = binding(run, [("rev-a", sql_a)], sole_revision="first revision of the task")
        assert bs["verdict"] == "BOUND" and bs["basis"] == "sole revision" and bs["evidence"]["sole_revision_hits"] >= 1, bs
        assert binding_ok(bs)[0] and binding(run, [("rev-b", sql_b)], sole_revision="x")["verdict"] == "UNBOUND"
        # planted: the subset case (the newer revision holds everything the older one does): shared content only
        sql_ab = sql_a + sql_b
        for cands in ([("new", sql_ab), ("old", sql_a)], [("old", sql_a), ("new", sql_ab)]):
            bb = binding(run, cands)
            assert bb["verdict"] == "INSUFFICIENT" and bb["evidence"]["shared_seen"] >= 1, bb
        # keyed values: the same row id with different text in two revisions binds to the text the run saw
        long_old = "the release console export is stale and must not be trusted for the season pass packages"
        long_new = "the release console export was refreshed this morning and is the source for every package"
        kev = [{"type": "system", "subtype": "init", "model": "claude-opus-4-8"},
               {"type": "assistant", "message": {"model": "claude-opus-4-8", "content": [
                   {"type": "tool_use", "id": "k1", "name": "mcp__hg__linear_list_comments", "input": {}}]}},
               {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "k1", "content":
                   json.dumps({"comments": [{"id": "cmt_seeded_one", "body": long_old}]})}]}}]
        krun = Run("k", p, "stream-json", kev, *index_events(kev))
        row = "INSERT INTO linear.linear_comments (id, issue_id, body) VALUES ('cmt_seeded_one', 'ZOM-1', '{}');\n"
        bk = binding(krun, [("rev-new", row.format(long_new)), ("rev-old", row.format(long_old))])
        assert bk["verdict"] == "BOUND" and bk["bound_to"] == ["rev-old"] and bk["candidates"][1]["seen_window_keys"], bk
        # discriminating content of two revisions: AMBIGUOUS, never a pick
        kev2 = kev + [{"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "k1", "content":
                       json.dumps({"comments": [{"id": "cmt_seeded_one", "body": long_new}]})}]}}]
        kev2[1]["message"]["content"].append({"type": "tool_use", "id": "k2", "name": "x", "input": {}})
        kev2[-1]["message"]["content"][0]["tool_use_id"] = "k2"
        krun2 = Run("k2", p, "stream-json", kev2, *index_events(kev2))
        assert binding(krun2, [("rev-new", row.format(long_new)), ("rev-old", row.format(long_old))])["verdict"] == "AMBIGUOUS"
        # planted: a BOUND label without evidence never certifies (a hand-written or legacy SINGLE record)
        assert not binding_ok({"verdict": "BOUND", "bound_to": ["rev-a"]})[0]
        assert not binding_ok({"verdict": "SINGLE", "bound_to": ["rev-a"]})[0]
        assert not binding_ok(dict(bs, sole_revision=" "))[0]
        # --sole-revision is refused when the task stores any other revision, or when it can't be checked
        td = Path(tmp) / "task"
        (td / "Working_Files" / "run_forensics" / "rev1").mkdir(parents=True)
        (td / "Working_Files" / "run_forensics" / "rev1" / "01_Universe_Inject.sql").write_text(sql_a)
        check_sole_revision(td, sql_a + "\n-- a comment-free or commented copy is the same revision\n")
        (td / "Working_Files" / "run_forensics" / "rev0").mkdir()
        (td / "Working_Files" / "run_forensics" / "rev0" / "01_Universe_Inject.sql").write_text(sql_b)
        for bad_td in (td, None):
            try:
                check_sole_revision(bad_td, sql_a)
            except ValueError as exc:
                assert ("rev0" in str(exc)) if bad_td else ("--task-dir" in str(exc)), exc
            else:
                raise AssertionError("--sole-revision accepted although it can't be shown to be the only revision")
        assert [r for r, _ in stored_revisions(td)] == ["rev0", "rev1"]
        assert brief_matches(bl, r"aborted")["matching"] == 1
        # derived revision-10 ledgers number events from 1
        derived = [{"event": 7, "type": "tool_use", "id": "a1", "name": "Agent", "input": {"prompt": "use the control tab"},
                    "result": {"event": 9, "error": False, "data": "ok"}}]
        dp = Path(tmp) / "run-1.calls.json"
        dp.write_text(json.dumps(derived))
        dr = load(dp, "run-1")
        assert dr.format == "derived-calls" and dr.calls[0]["event"] == 6 and dr.calls[0]["event_1b"] == 7
        assert brief_matches(briefs(dr), r"control tab|control sheet")["matching"] == 1
        # outputs never land in a frozen copy
        (Path(tmp) / "SHA256SUMS").write_text("")
        (Path(tmp) / "sub").mkdir()
        assert frozen_root(Path(tmp) / "sub") == Path(tmp)
        try:
            safe_out(BUNDLE / "support" / "x")   # inside the bundle, no freeze above it: fine
        except ValueError:
            raise AssertionError("bundle path rejected")
    try:
        safe_out(Path(tempfile.gettempdir()) / "outside")
    except ValueError:
        pass
    else:
        raise AssertionError("a path outside Task_Authoring was accepted")
    print("self-test: ok (counts via difficulty_stats, briefs with key ranges and requested models, fallback phases, "
          "compaction / spill / unpaired / after-result validity, CSV vs native-Sheet table rule with appends and "
          "title filter, printed totals, tracker description + patch, write verbs, content binding by key (one "
          "candidate INSUFFICIENT, sole revision BOUND with its reason or UNBOUND, the subset case INSUFFICIENT, a "
          "changed value binds to the text seen, AMBIGUOUS, an evidence-free BOUND or SINGLE never certifies, "
          "--sole-revision refused when another revision is stored), derived 1-based ledgers, output boundary)")


# ------------------------------------------------------------------ main

def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="trajectory_ledger.py", description="run facts from trajectory exports (see docstring)")
    ap.add_argument("--task-dir", type=Path)
    ap.add_argument("--run", action="append", default=[], help="LABEL=PATH of a stream-json export")
    ap.add_argument("--derived", action="append", default=[], help="LABEL=PATH of a derived calls.json ledger")
    ap.add_argument("--surface", type=Path, help="01_Gradable_Surface.json: its table deliverable selects the register")
    ap.add_argument("--key-regex", help="cohort key pattern for brief key lists (default: the surface's)")
    ap.add_argument("--sql", action="append", default=[], help="LABEL=PATH; the first is the revision under test")
    ap.add_argument("--sole-revision", metavar="REASON",
                    help="the one --sql is the task's only revision (refused when the task stores another one)")
    ap.add_argument("--prompt", type=Path)
    ap.add_argument("--source", choices=("platform-precheck", "platform-baseline", "independent-harness", "probe"))
    ap.add_argument("--harness", help="NAME@VERSION when the export has no init event")
    ap.add_argument("--expected-model", help="the run's expected model (default: the task context's baseline_model, "
                                             "else the V3 policy model)")
    ap.add_argument("--brief-regex", help="count subagent briefs whose prompt matches this pattern")
    ap.add_argument("--out-dir", type=Path)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        _self_test()
        return 0
    runs = [(lab, p, "run") for lab, p in _pairs(a.run)] + [(lab, p, "derived") for lab, p in _pairs(a.derived)]
    if not runs and a.task_dir:
        runs = [(lab, p, "run") for lab, p in task_runs(a.task_dir)]
    if not runs:
        ap.print_usage(sys.stderr)
        return 2
    surface = a.surface or (a.task_dir / "Working_Files" / "01_Gradable_Surface.json" if a.task_dir else None)
    spec, krx_s = table_spec_from_surface(surface) if surface and surface.is_file() else (None, None)
    key_rx = key_regex_list(a.key_regex or krx_s)
    sqls = [(lab, p.read_text(errors="replace")) for lab, p in _pairs(a.sql)]
    if not sqls and a.task_dir and (a.task_dir / "01_Universe_Inject.sql").is_file():
        sqls = [("task", (a.task_dir / "01_Universe_Inject.sql").read_text(errors="replace"))]
    if a.sole_revision is not None:
        if not a.sole_revision.strip() or len(sqls) != 1:
            raise ValueError("--sole-revision needs a reason and exactly one --sql")
        check_sole_revision(a.task_dir, sqls[0][1])
    prompt = a.prompt or (a.task_dir / "04_Prompt.txt" if a.task_dir else None)
    prompt_text = prompt.read_text() if prompt and prompt.is_file() else None
    out_dir = safe_out(a.out_dir) if a.out_dir else None
    summaries, bad = [], 0
    for lab, path, kind in runs:
        run = load(path, lab)
        source = a.source or (("platform-precheck" if lab == "precheck" else "platform-baseline") if kind == "run" else None)
        s = summarize(run, key_rx=key_rx, table_spec=spec, sql=sqls or None, prompt_text=prompt_text, source=source,
                      harness_override=a.harness, brief_rx=a.brief_regex, sole_revision=a.sole_revision,
                      expected_model=a.expected_model or expected_model_for(a.task_dir))
        summaries.append(s)
        bad += any(f.startswith(("errored", "revision binding")) for f in s["flags"])
        if out_dir:
            write_outputs(run, s, out_dir, key_rx)
        if not a.json:
            tb = s.get("table") or {}
            br = s.get("brief_regex")
            print(f"{lab}: {s['format']} counted={s['counts']['counted']} briefs={s['counts']['briefs']}"
                  f" models={s['provenance']['brief_models']} fallbacks={[f['event'] for f in s['provenance']['fallbacks']]}"
                  f" mixed={s['provenance']['mixed_model']} v3_valid={s['provenance']['v3_valid']}"
                  + (f" valid_for_{s['provenance']['model_check']['expected_model']}="
                     f"{s['provenance']['model_check']['valid']}" if s['provenance'].get('model_check') else "")
                  + (f" table={tb.get('kind')}:{tb.get('rows')}" if spec else "")
                  + (f" binding={s['binding']['verdict']}:{s['binding']['bound_to']}" if sqls else "")
                  + (f" brief_regex={br['matching']}/{br['briefs']}" if br else "")
                  + (f" flags={len(s['flags'])}" if s["flags"] else ""))
            for f in s["flags"]:
                print(f"    - {f}")
    if out_dir:
        (out_dir / "summary.json").write_text(json.dumps({"kind": "TRAJECTORY_LEDGER_SUMMARY", "tool": VERSION,
                                                          "runs": summaries}, indent=1, ensure_ascii=False) + "\n")
        if not a.json:
            print(f"wrote {_rel(out_dir)}")
    if a.json:
        print(json.dumps(summaries, indent=1, ensure_ascii=False))
    return 1 if bad else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"trajectory_ledger: {error}", file=sys.stderr)
        raise SystemExit(2)
