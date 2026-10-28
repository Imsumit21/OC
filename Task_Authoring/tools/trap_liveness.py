#!/usr/bin/env python3
"""trap_liveness.py - advisory lexical flags for traps the entry set already neutralises (plan §7.3).

The entry set is what an agent reads first: the prompt, the hub its anchors point at, and the hub's direct delegations
(manifest ask_fragments whose delegated_by_record is the hub). Four flags per trap node:

  breadcrumb      the entry set reaches a decisive record: the hub links or names it, or a direct delegation targets
                  it. Decisive records: the trap's version records other than the superseded one, the seeded records
                  of authorities that govern its requirement in its services, the containers of fragments that serve
                  its requirement in its services, and, for reuse traps, the record to reuse - never one of its decoys.
  self-advertising  a decoy's own title or first 200 characters carry another scope's token (an authority's
                  decoy_scope) or a draft / old / superseded word. A trap's decoys: the earliest of two or more version
                  records (the superseded reading), else its seeded records when it is a distractor, superseding or
                  stale-summary trap. Authority decoys no trap seeds are checked as nodes of their own.
  order           the correction sits in the hub thread: a decisive record is the hub or a reply in its thread, or the
                  hub's delegation pointing at a decoy labels it superseded ("is history", "earlier", ...).
  rule placement  one sentence of a first-read source (prompt, hub, direct delegations) states the trap's resolver:
                  it holds at least max(2, ceil(0.6 n)) of the resolver's n content words. A15 nodes only (plan §7.3;
                  decision 2026-10-25): the nodes of the mechanism_portfolio's A15 entries, or a trap whose own
                  mechanism is A15. Every other node, and every node of a legacy manifest (no mechanism ids), reports
                  rule placement as SKIP with its reason: never a pass, never a flag.

Content words have three or more letters and are not stopwords; two words match when equal or when one (four letters
or more) is a prefix of the other. Record text comes from the SQL overlay only; base records are listed as not read
(read them through tools/hg.py). These are lexical warnings, not proof: persona_view search has no SQL overlay and
does not reproduce platform ranking. Every flag needs a written disposition; the response is to redesign the
difficulty, never to remove a fairness link. Read-only, stdlib only, never executes SQL.

Usage:
  python3 -B Task_Authoring/tools/trap_liveness.py --task-dir DIR [--manifest M] [--sql SQL] [--prompt P]
      [--verdicts V.json] [--dispositions D.json] [--require-dispositions] [--out OUT.json] [--json]
  python3 -B Task_Authoring/tools/trap_liveness.py --design --task-dir DIR [--manifest DRAFT]   (scenario S5b: no SQL yet;
      only the manifest-structure flags can fire, and the report says so)
  python3 -B Task_Authoring/tools/trap_liveness.py --self-test
--verdicts ({node: verdict}, e.g. a backtest register) only scores the flags afterwards: hits on FALSE nodes, misses,
and flags on LEAKED / LANDED nodes. Exit 0 = flags reported, 1 = a required disposition is missing, 2 = usage error.
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
import tempfile
from pathlib import Path


def _bundle() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "difficulty_stats.py").is_file():
            return parent
    raise SystemExit("trap_liveness: cannot find the Task_Authoring bundle (no tools/difficulty_stats.py above)")


HERE = Path(__file__).resolve().parent
BUNDLE = _bundle()
for _p in (BUNDLE / "tools", HERE):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
import trajectory_ledger as tl  # noqa: E402

VERSION = "trap_liveness/1"
FLAGS = ("breadcrumb", "self-advertising", "order", "rule placement")
LABEL = "ADVISORY · UNCALIBRATED · lexical warnings, not proof"
NOTE = "on the Season Pass backtests these are development fixtures, not validation"
DECOY_FAMILIES = ("distractor", "superseding", "stale_summary")
REUSE_FAMILIES = ("reuse_exclusion",)
RX_STALE = re.compile(r"\b(?:drafts?|old|older|superseded|obsolete|outdated|deprecated|archived?|history|historical|"
                      r"earlier|previous|no longer|not the final|replaced)\b", re.I)
STOP = set("the and for with that this from into each only its are was but any all per via own use used uses using "
           "than then them they their there when where which while what who whom will would shall should could can "
           "may might must have has had been being does did done not never also more most less such same other "
           "these those here over under after before about above below between every both either neither just "
           "give gives given take takes make makes made one two three".split())
TEXT_COLS = ("text", "body", "body_text", "description", "desc", "content", "snippet", "content_text", "grid_json",
             "data_json")
TITLE_COLS = ("name", "title", "subject")
ID_COLS = ("id", "identifier", "spreadsheet_id", "document_id", "presentation_id", "event_id", "sha")


def words(text: str) -> list:
    return [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'-]{2,}", text or "")]


def content(text: str) -> set:
    return {w for w in words(text) if w not in STOP}


def matches(a: str, b: str) -> bool:
    return a == b or (min(len(a), len(b)) >= 4 and (a.startswith(b) or b.startswith(a)))


def covered(resolver: set, sentence: set) -> list:
    return sorted(w for w in resolver if any(matches(w, s) for s in sentence))


def sentences(text: str) -> list:
    return [s.strip() for s in re.split(r"(?<=[.;!?])\s+|\n+", (text or "").replace("\\n", "\n")) if s.strip()]


# ------------------------------------------------------------------ records from the SQL overlay

class Records:
    """id -> {table, title, text, row}; Slack messages also under channel/ts."""

    def __init__(self, sql_text: str):
        from base_check import parse_sql
        self.by_id = collections.defaultdict(list)
        self.slack = []
        for x in parse_sql(sql_text):
            if x["op"] != "insert":
                continue
            r = x["row"]
            title = next((str(r[k]) for k in TITLE_COLS if isinstance(r.get(k), str) and r[k]), "")
            text = ""
            for k in TEXT_COLS:
                v = r.get(k)
                if isinstance(v, str) and len(v) > len(text):
                    if k in ("grid_json", "data_json"):
                        try:
                            v = " ".join(tl.strings(json.loads(v)))
                        except ValueError:
                            pass
                    text = v
            rec = {"table": x["table"], "title": title, "text": text.replace("\\n", "\n"), "row": r}
            for k in ID_COLS:
                if r.get(k):
                    self.by_id[str(r[k])].append(rec)
            if x["table"].endswith("slack_messages") and r.get("channel_id") and r.get("ts"):
                self.by_id[f"{r['channel_id']}/{r['ts']}"].append(rec)
                self.slack.append(rec)

    def get(self, rid: str) -> list:
        rid = str(rid)
        if rid in self.by_id:
            return self.by_id[rid]
        base = rid.split("/")[0] if "/" in rid and not rid.startswith("C") else rid
        return self.by_id.get(base, [])

    def text(self, rid: str) -> str:
        return "\n".join(r["text"] for r in self.get(rid))

    def head(self, rid: str, n: int = 200) -> str:
        recs = self.get(rid)
        title = next((r["title"] for r in recs if r["title"]), "")
        body = next((r["text"] for r in recs if r["text"]), "")
        return (title + "\n" + body[:n]).strip()


def _ids_in(text: str, candidates) -> set:
    return {c for c in candidates if c and len(c) >= 6 and c in (text or "")}


# ------------------------------------------------------------------ entry set and the four flags

def entry_set(manifest: dict, recs: Records, prompt: str) -> dict:
    anchors = manifest.get("anchors") or []
    frags = manifest.get("ask_fragments") or []
    counts = collections.Counter(f.get("delegated_by_record") for f in frags if f.get("delegated_by_record"))
    hubs = [a.get("locator") for a in anchors if a.get("locator")]
    hub = max(set(hubs), key=lambda h: (counts.get(h, 0), hubs.count(h))) if hubs else (
        counts.most_common(1)[0][0] if counts else None)
    direct = [f for f in frags if f.get("delegated_by_record") == hub]
    hub_text = recs.text(hub) if hub else ""
    channel, _, ts = (hub or "").partition("/")
    hub_ids = {hub} | {str(r["row"].get("id")) for r in recs.get(hub)} if hub else set()
    thread = [r for r in recs.slack if r["row"].get("channel_id") == channel and r["row"].get("ts") != ts and (
        ts in (r["row"].get("thread_ts"), r["row"].get("thread_ts_legacy")) or r["row"].get("thread_parent_id") in hub_ids)]
    thread_ids = {f"{channel}/{r['row']['ts']}" for r in thread} | {str(r["row"].get("id")) for r in thread}
    targets = {}
    for f in direct:
        for rid in [f.get("container"), f.get("locator")] + list(f.get("seeded_ids") or []) + list(f.get("base_pointers") or []):
            if rid:
                targets.setdefault(str(rid), []).append(f["id"])
    sources = [("prompt", prompt or "")] + ([("hub", hub_text)] if hub else [])
    for f in direct:
        rid = f.get("container") or f.get("locator")
        t = recs.text(rid) or recs.text(f.get("locator") or "")
        if t:
            sources.append((f"{f['id']}:{rid}", t))
    unread = sorted({f.get("container") or f.get("locator") for f in direct if not recs.get(f.get("container") or "")
                     and not recs.get(f.get("locator") or "")})
    return {"hub": hub, "hub_ids": hub_ids, "hub_text": hub_text, "thread_ids": thread_ids, "direct": direct,
            "targets": targets, "sources": sources, "unread": unread}


def decisive(trap: dict, manifest: dict) -> list:
    req, svcs = trap.get("requirement"), set(trap.get("services") or [])
    seeded = set(trap.get("seeded_ids") or [])
    out = []
    for v in trap.get("version_records") or []:
        if v.get("id"):
            out.append((str(v["id"]), "version record"))
    for a in manifest.get("authorities") or []:
        if req in (a.get("governs") or []) and (not svcs or a.get("home_service") in svcs):
            out += [(str(i), f"authority {a['id']}") for i in a.get("seeded_ids") or []]
    for f in manifest.get("ask_fragments") or []:
        if req in (f.get("requirement_ids") or []) and (not svcs or f.get("service") in svcs):
            out += [(str(i), f"fragment {f['id']}") for i in (f.get("container"), f.get("locator")) if i]
    if trap.get("family") in REUSE_FAMILIES:
        out += [(str(i), "record to reuse") for i in seeded]
    seen, uniq = set(decoys(trap, manifest)), []      # a delegation that points at the trap's own decoy decides nothing
    for rid, why in out:
        if rid not in seen:
            seen.add(rid)
            uniq.append((rid, why))
    return uniq


def decoys(trap: dict, manifest: dict | None = None) -> list:
    versions = [v for v in trap.get("version_records") or [] if v.get("id")]
    if len(versions) >= 2:
        return [str(min(versions, key=lambda v: str(v.get("at") or ""))["id"])]
    if trap.get("family") in DECOY_FAMILIES or trap.get("distractor_type"):
        return list(dict.fromkeys(str(i) for i in trap.get("seeded_ids") or []))
    return []


def self_advertising(rid: str, recs: Records, scope: list):
    head = recs.head(rid)
    if not head:
        return None
    tokens = [s for s in scope if s.lower() in head.lower()]
    stale = RX_STALE.search(head)
    if tokens or stale:
        return (f"decoy {rid}: " + (f"scope token {tokens}" if tokens else f"'{stale.group(0)}'")
                + f" in its title / first lines ({head[:90]!r})")
    return None


def scope_tokens(manifest: dict) -> list:
    out = set()
    for a in manifest.get("authorities") or []:
        d = (a.get("decoy_scope") or {}).get("decoy")
        if d:
            out.add(d)
    return sorted(out)


def flags_for(trap: dict, manifest: dict, recs: Records, entry: dict, a15_only: set | None) -> dict:
    found = {}
    dec = decisive(trap, manifest)
    hub_blob = (entry["hub_text"] or "") + "\n" + entry["sources"][0][1]
    hits = []
    for rid, why in dec:
        if rid in entry["targets"]:
            hits.append(f"{rid} ({why}) is the target of direct delegation {entry['targets'][rid]}")
        elif _ids_in(hub_blob, [rid]):
            hits.append(f"{rid} ({why}) is linked or named in the hub or prompt")
    if hits:
        found["breadcrumb"] = hits
    scope = scope_tokens(manifest)
    adv, lab = [], []
    for d in decoys(trap, manifest):
        hit = self_advertising(d, recs, scope)
        if hit:
            adv.append(hit)
        for f in entry["direct"]:
            quote = f.get("delegation_quote") or ""
            if d in {str(f.get("container")), str(f.get("locator"))} | set(map(str, f.get("seeded_ids") or [])) \
                    and RX_STALE.search(quote):
                lab.append(f"the hub's delegation {f['id']} labels decoy {d} superseded: {quote!r}")
    if adv:
        found["self-advertising"] = adv
    order = list(lab)
    for rid, why in dec:
        if rid in entry["hub_ids"] or rid in entry["thread_ids"]:
            order.append(f"decisive record {rid} ({why}) is the hub or a reply in its thread")
    if order:
        found["order"] = order
    rp = {"status": "SKIP", "reason": a15_only["why"]}
    if trap.get("id") in a15_only["nodes"]:
        rp = {"status": "CHECKED", "reason": "an A15 node"}
        res = content(trap.get("resolver") or "")
        need = max(2, -(-3 * len(res) // 5))
        placed = []
        for src, text in entry["sources"] if len(res) >= 2 else []:
            for s in sentences(text):
                common = covered(res, content(s))
                if len(common) >= need:
                    placed.append(f"{src}: {len(common)}/{len(res)} resolver words {common} in {s[:110]!r}")
                    break
        if placed:
            found["rule placement"] = placed[:3]
    elif a15_only["nodes"]:
        rp["reason"] = "not an A15 node"
    return {"id": trap.get("id"), "family": trap.get("family"), "distractor_type": trap.get("distractor_type"),
            "requirement": trap.get("requirement"), "flags": found, "flagged": sorted(found), "rule_placement": rp,
            "decisive_records": [r for r, _ in dec], "decoys": decoys(trap, manifest),
            "decoys_not_read": [d for d in decoys(trap, manifest) if not recs.get(d)]}


def a15_nodes(manifest: dict) -> dict:
    """{nodes, source, why}: the trap ids rule placement applies to (A15 only, plan §7.3)."""
    port = manifest.get("mechanism_portfolio") or []
    nodes = {n for p in port if p.get("mechanism") == "A15" for n in p.get("nodes") or []}
    own = {t.get("id") for t in manifest.get("traps") or [] if t.get("mechanism") == "A15"}
    src = " + ".join(s for s, ok_ in (("mechanism_portfolio", nodes), ("trap mechanism ids", own)) if ok_) or None
    why = ("not an A15 node" if nodes | own else
           "the mechanism_portfolio declares no A15 node" if port else
           "legacy manifest: no mechanism_portfolio and no trap mechanism ids, so no node is known to be A15")
    return {"nodes": nodes | own, "source": src, "why": why}


def run(manifest: dict, sql_text: str, prompt: str, verdicts: dict | None = None) -> dict:
    recs = Records(sql_text)
    entry = entry_set(manifest, recs, prompt)
    a15 = a15_nodes(manifest)
    traps = manifest.get("traps") or []
    nodes = [flags_for(t, manifest, recs, entry, a15) for t in traps]
    covered_ids = {str(i) for t in traps for i in list(t.get("seeded_ids") or []) + decoys(t)}
    scope = scope_tokens(manifest)
    authority_decoys = []
    for a in manifest.get("authorities") or []:
        for d in a.get("decoy_seeded_ids") or []:
            if str(d) in covered_ids:
                continue
            hit = self_advertising(str(d), recs, scope)
            authority_decoys.append({"id": f"{a['id']}-decoy", "record": d, "flags": {"self-advertising": [hit]} if hit
                                     else {}, "flagged": ["self-advertising"] if hit else [], "read": bool(recs.get(d))})
    rep = {"kind": "TRAP_LIVENESS", "tool": VERSION, "label": LABEL, "note": NOTE, "hub": entry["hub"],
           "direct_delegations": [f["id"] for f in entry["direct"]], "entry_sources": [s for s, _ in entry["sources"]],
           "entry_records_not_read": entry["unread"],
           "rule_placement_scope": (f"A15 nodes only: {sorted(a15['nodes'])} ({a15['source']}); every other node SKIP"
                                    if a15["nodes"] else f"SKIP for every node: {a15['why']}"),
           "nodes": nodes, "authority_decoys": authority_decoys,
           "summary": {f: [n["id"] for n in nodes + authority_decoys if f in n["flags"]] for f in FLAGS}}
    if verdicts:
        by = collections.defaultdict(list)
        for n in nodes:
            v = verdicts.get(n["id"])
            if v is None:
                for key, val in verdicts.items():
                    if n["id"] in re.split(r"[/,\s]+", key):
                        v = val
                        break
            by[v or "UNKNOWN"].append(n)
        false = by.get("FALSE", [])
        rep["scored_against_verdicts"] = {
            "false_nodes": len(false), "false_flagged": [n["id"] for n in false if n["flagged"]],
            "false_missed": [n["id"] for n in false if not n["flagged"]],
            "flags_on_other_verdicts": {v: {n["id"]: n["flagged"] for n in ns} for v, ns in sorted(by.items())
                                        if v != "FALSE"},
            "note": "verdicts are read only to score the flags afterwards; " + NOTE}
    return rep


def dispositions(rep: dict, path) -> dict:
    """path: a JSON file or an already-loaded {node:flag: {disposition, reason?}} mapping."""
    recorded = path if isinstance(path, dict) else (json.loads(Path(path).read_text()) if path else {})
    need = [f"{n['id']}:{f}" for n in rep["nodes"] + rep.get("authority_decoys", []) for f in n["flagged"]]
    bad = [k for k, v in recorded.items() if not isinstance(v, dict) or not str(v.get("disposition") or "").strip()]
    if bad:
        raise ValueError(f"dispositions need {{disposition, reason?}}: {bad[:6]}")
    return {"required": need, "recorded": {k: recorded[k] for k in need if k in recorded},
            "missing": [k for k in need if k not in recorded],
            "rule": "every flag needs a written disposition; redesign the difficulty, never remove a fairness link"}


def to_text(rep: dict) -> str:
    lines = [f"TRAP LIVENESS · {rep.get('label', LABEL)} · {NOTE}",
             f"  hub {rep['hub']} · direct delegations {len(rep['direct_delegations'])} · rule placement: "
             f"{rep['rule_placement_scope']}"]
    for n in rep["nodes"]:
        rp = n.get("rule_placement") or {}
        lines.append(f"  {n['id']:4} {str(n['family'])[:18]:18} " + (", ".join(n["flagged"]) or "-")
                     + ("" if rp.get("status") != "SKIP" else f"  [rule placement SKIP: {rp['reason']}]"))
    for n in rep.get("authority_decoys") or []:
        lines.append(f"  {n['id']:9} {str(n['record'])[:28]:28} " + (", ".join(n["flagged"]) or "-")
                     + ("" if n["read"] else " (not in the SQL overlay: not read)"))
    s = rep.get("scored_against_verdicts")
    if s:
        lines.append(f"  FALSE nodes flagged {len(s['false_flagged'])}/{s['false_nodes']}: {s['false_flagged']}; "
                     f"missed {s['false_missed'] or 'none'}")
        for v, nodes in s["flags_on_other_verdicts"].items():
            lines.append(f"  flags on {v}: " + "; ".join(f"{k} {fl or '-'}" for k, fl in nodes.items()))
    d = rep.get("dispositions")
    if d:
        lines.append(f"  dispositions: {len(d['recorded'])}/{len(d['required'])} recorded")
    return "\n".join(lines)


# ------------------------------------------------------------------ self-test

def _self_test() -> None:
    sql = ("INSERT INTO slack.slack_messages (id, channel_id, ts, thread_ts, text) VALUES ('m_hub_0001', 'C01', "
           "'100.1', NULL, 'Finish the Alpha handoff. Save it in https://drive.example/folders/d_target_0001. The "
           "earlier notes thread here is history. Record WATCH when the ring is internal.');\n"
           "INSERT INTO slack.slack_messages (id, channel_id, ts, thread_parent_id, thread_ts_legacy, text) VALUES "
           "('m_reply_0001', 'C01', '100.2', 'm_hub_0001', '100.1', 'A receipt only counts on its own package line.');\n"
           "INSERT INTO slack.slack_messages (id, channel_id, ts, thread_ts, text) VALUES ('m_old_0001', 'C01', "
           "'90.1', NULL, 'Send the register to me and cc Robert.');\n"
           "INSERT INTO gdrive.drive_files (id, name) VALUES ('d_target_0001', 'Alpha Handoff - Feb');\n"
           "INSERT INTO gdrive.drive_files (id, name) VALUES ('d_decoy_0001', 'Beta Game Handoff - Feb');\n"
           "INSERT INTO gdrive.drive_files (id, name) VALUES ('d_quiet_0001', 'Alpha Handoff - Jan');\n"
           "INSERT INTO gdrive.drive_files (id, name) VALUES ('d_hdecoy_0001', 'Old Alpha Handoff');\n")
    manifest = {
        "anchors": [{"id": "A1", "locator": "C01/100.1"}],
        "ask_fragments": [
            {"id": "K1", "service": "gdrive", "container": "d_target_0001", "locator": "d_target_0001",
             "delegated_by_record": "C01/100.1", "delegation_quote": "Save it in", "requirement_ids": ["R4"]},
            {"id": "K2", "service": "slack", "container": "m_old_0001", "locator": "m_old_0001",
             "delegated_by_record": "C01/100.1", "delegation_quote": "The earlier notes thread here is history",
             "requirement_ids": ["R5"]},
            {"id": "K3", "service": "slack", "container": "C01/100.2", "locator": "C01/100.2",
             "delegated_by_record": "C01/100.1", "delegation_quote": "Reply here", "requirement_ids": ["R3"]}],
        "authorities": [{"id": "H1", "name": "x", "home_service": "gdrive", "seeded_ids": ["d_target_0001"],
                         "governs": ["R4"], "decoy_seeded_ids": ["d_decoy_0001", "d_hdecoy_0001"],
                         "decoy_scope": {"dimension": "game", "decoy": "Beta Game", "task": "Alpha"}}],
        "traps": [
            {"id": "T1", "family": "distractor", "distractor_type": "keyword_collision", "services": ["gdrive"],
             "seeded_ids": ["d_decoy_0001"], "requirement": "R4", "resolver": "exact hub folder link",
             "expected_wrong_reading": "file in adjacent folder"},
            {"id": "T2", "family": "superseding", "services": ["slack"], "seeded_ids": ["m_old_0001"],
             "requirement": "R5", "resolver": "final protocol says no cc", "expected_wrong_reading": "cc Robert"},
            {"id": "T3", "family": "superseding", "services": ["slack"], "seeded_ids": ["m_x_0001"],
             "requirement": "R3", "resolver": "own package receipt", "expected_wrong_reading": "use foreign receipt",
             "version_records": [{"id": "C01/100.2"}]},
            {"id": "T4", "family": "conclusion_stop", "services": ["github"], "seeded_ids": ["pr_1"],
             "requirement": "R9", "resolver": "a later merge alone is not readiness",
             "expected_wrong_reading": "merged means done"},
            {"id": "T5", "family": "distractor", "services": ["gdrive"], "seeded_ids": ["d_quiet_0001"],
             "requirement": "R8", "resolver": "dated month", "expected_wrong_reading": "use january"}]}
    prompt = "Can you finish the Alpha handoff? A later merge alone does not mean the component is ready."
    rep = run(manifest, sql, prompt, {"T1": "FALSE", "T2": "FALSE", "T3/T9": "LEAKED", "T4": "FALSE", "T5": "LANDED"})
    by = {n["id"]: n for n in rep["nodes"]}
    assert rep["hub"] == "C01/100.1" and rep["direct_delegations"] == ["K1", "K2", "K3"], rep
    assert by["T1"]["flagged"] == ["breadcrumb", "self-advertising"], by["T1"]                       # link + scope token
    assert by["T2"]["flagged"] == ["order"] and by["T2"]["decisive_records"] == [], by["T2"]        # hub labels it history
    # planted: a legacy manifest (no mechanism ids) no longer runs rule placement on every node: SKIP with its reason
    assert by["T3"]["flagged"] == ["breadcrumb", "order"], by["T3"]
    assert by["T4"]["flagged"] == [], by["T4"]
    assert all(n["rule_placement"]["status"] == "SKIP" and "legacy manifest" in n["rule_placement"]["reason"]
               for n in rep["nodes"]), [n["rule_placement"] for n in rep["nodes"]]
    assert rep["rule_placement_scope"].startswith("SKIP for every node: legacy manifest"), rep["rule_placement_scope"]
    assert by["T5"]["flagged"] == [], by["T5"]
    assert [(n["id"], n["record"], n["flagged"]) for n in rep["authority_decoys"]] == [
        ("H1-decoy", "d_hdecoy_0001", ["self-advertising"])], rep["authority_decoys"]          # 'Old' in its title
    s = rep["scored_against_verdicts"]
    assert s["false_flagged"] == ["T1", "T2"] and s["false_missed"] == ["T4"] and "LEAKED" in s["flags_on_other_verdicts"], s
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("trap_liveness_selftest_") as tmp:
        d = Path(tmp) / "d.json"
        d.write_text(json.dumps({"T1:breadcrumb": {"disposition": "keep the link; move the difficulty to the class rule"}}))
        dd = dispositions(rep, d)
        assert "T1:breadcrumb" in dd["recorded"] and "T1:self-advertising" in dd["missing"], dd
    # with A15 nodes declared, only they are checked: T3 (rule in the thread reply), T4 (3 of 4 resolver words in the
    # prompt); T1 is not an A15 node
    port = dict(manifest, mechanism_portfolio=[{"id": "r", "mechanism": "A15", "nodes": ["T3", "T4"]}])
    bp = {n["id"]: n for n in run(port, sql, prompt)["nodes"]}
    assert bp["T3"]["flagged"] == ["breadcrumb", "order", "rule placement"] and bp["T4"]["flagged"] == ["rule placement"]
    assert bp["T1"]["rule_placement"] == {"status": "SKIP", "reason": "not an A15 node"}, bp["T1"]["rule_placement"]
    assert bp["T4"]["rule_placement"]["status"] == "CHECKED"
    # a trap's own mechanism id makes it an A15 node without a portfolio; a portfolio with no A15 node checks none
    own = dict(manifest, traps=[dict(x, mechanism="A15") if x["id"] == "T4" else x for x in manifest["traps"]])
    assert {n["id"]: n for n in run(own, sql, prompt)["nodes"]}["T4"]["flagged"] == ["rule placement"]
    none15 = dict(manifest, mechanism_portfolio=[{"id": "r", "mechanism": "A17", "nodes": ["T4"]}])
    rn = run(none15, sql, prompt)
    assert all(n["rule_placement"]["reason"] == "the mechanism_portfolio declares no A15 node" for n in rn["nodes"]), rn
    print("self-test: ok (hub from anchors and delegation counts, breadcrumb via delegation and literal link, decoy scope "
          "token, hub label as order, correction in the hub thread, rule placement by resolver coverage on A15 nodes "
          "only (portfolio or trap mechanism id; legacy manifest SKIP with its reason, never a pass), authority decoys "
          "no trap seeds, scoring against verdicts, dispositions)")


# ------------------------------------------------------------------ main

def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="trap_liveness.py", description="advisory trap liveness flags (see docstring)")
    ap.add_argument("--task-dir", type=Path)
    ap.add_argument("--manifest", type=Path)
    ap.add_argument("--sql", type=Path)
    ap.add_argument("--prompt", type=Path)
    ap.add_argument("--verdicts", type=Path, help="{node: verdict} to score the flags afterwards (backtests)")
    ap.add_argument("--dispositions", type=Path)
    ap.add_argument("--require-dispositions", action="store_true")
    ap.add_argument("--design", action="store_true", help="no SQL yet (scenario S5b): structure flags only")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        _self_test()
        return 0
    td = a.task_dir
    wf = td / "Working_Files" if td else None
    names = ("01_Hardness_Manifest.draft.json", "01_Hardness_Manifest.json") if a.design else (
        "01_Hardness_Manifest.json", "01_Hardness_Manifest.draft.json")
    man = a.manifest or (next((wf / n for n in names if (wf / n).is_file()), None) if wf else None)
    sql = None if a.design else (a.sql or (td / "01_Universe_Inject.sql" if td else None))
    prompt = a.prompt or (td / "04_Prompt.txt" if td else None)
    if not man or not Path(man).is_file() or (not a.design and (not sql or not sql.is_file())):
        print("trap_liveness: need --manifest and --sql (or --task-dir), or --design", file=sys.stderr)
        return 2
    verdicts = json.loads(a.verdicts.read_text()) if a.verdicts else None
    if isinstance(verdicts, dict) and "verdicts" in verdicts:
        verdicts = verdicts["verdicts"]
    rep = run(json.loads(Path(man).read_text()), sql.read_text() if sql else "",
              prompt.read_text() if prompt and prompt.is_file() else "", verdicts)
    if a.design:
        rep["label"] = LABEL + " · DESIGN (no SQL: record text unavailable, only manifest-structure flags can fire)"
    rep.update(manifest=tl._rel(Path(man)), manifest_sha256=tl.sha256_file(Path(man)),
               sql=tl._rel(sql) if sql else None, sql_sha256=tl.sha256_file(sql) if sql else None,
               prompt=tl._rel(prompt) if prompt and prompt.is_file() else None,
               prompt_sha256=tl.sha256_file(prompt) if prompt and prompt.is_file() else None)
    rep["dispositions"] = dispositions(rep, a.dispositions)
    rc = 1 if a.require_dispositions and rep["dispositions"]["missing"] else 0
    if a.out:
        out = tl.safe_out(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(rep, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps(rep, indent=1, ensure_ascii=False) if a.json else to_text(rep))
    if a.out and not a.json:
        print(f"wrote {tl._rel(a.out)}")
    return rc


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"trap_liveness: {error}", file=sys.stderr)
        raise SystemExit(2)
