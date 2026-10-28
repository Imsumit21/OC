#!/usr/bin/env python3
"""G1 falsification (read-only): undo each surface_grader fix in memory, one at a time, and show that the planted case
guarding it fails, and which of the 12 Season Pass format fixtures flip. The old rules are those of the frozen proxy
support/analysis/season_pass_runs_rev14.py (defects 1-4, 6-8), of the reference's earlier count rule "bullets by first
key" (defect 5), and of the pre-G1 grader (undecodable writes dropped; UNGRADED converted to false before the gates).
Nothing is written: the tools are patched in this process only. Control: with nothing undone, every case passes.
"""
import json
import re
import sys
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(BUNDLE / "tools"))
import gradable_surface as gs  # noqa: E402
import surface_grader as sg  # noqa: E402
import trajectory_ledger as tl  # noqa: E402


def old_section_start(lines, heading_regex, krx):        # 1: the first mention
    hits = [i for i, line in enumerate(lines) if re.search(heading_regex, line, re.I)]
    return hits[0] if hits else None


def old_section_body(lines, start, krx):                  # 2: consecutive key lines; prose or a table header ends it
    found, body = bool(re.findall(krx, lines[start])), []
    for nxt in lines[start + 1:]:
        if not nxt.strip():
            if found:
                break
            continue
        if not re.findall(krx, nxt):
            break
        body.append(nxt)
        found = True
    return body


def old_strings(v, out):                                  # 3: the JSON dump
    out.append(json.dumps(v, ensure_ascii=False))
    return out


def old_final_state(ups):                                 # 4: the last update only
    q = ups[-1]["input"] if ups else {}
    return str(q.get("state") or q.get("stateId") or "")


def old_preserved(ups, original):
    q = ups[-1]["input"] if ups else {}
    return original in sg.tracker_text(ups)[0] or isinstance(q.get("patch"), list)


def old_row_keys(line, krx):                              # 5: a bullet counts its first key
    s = line.strip()
    keys = re.findall(krx, s)
    if not keys:
        return []
    if s.startswith("|"):
        return re.findall(krx, s.strip("|").split("|")[0])[:1]
    if re.match(r"([-*•]|\d+[.)])\s+", s):
        return keys[:1]
    residue = re.sub(krx + r"|\b(and|or|PR|ZOM)\b|[\W_\d]", "", s)
    return keys if len(residue) <= 6 * len(keys) else []


def old_entry_match(line, pattern, known_hex):            # 8: the value as a plain regex
    return bool(re.search(str(pattern), line, re.I))


def old_tracker_text(ups):                                # round 1: every description appended, replacements concatenated
    text = ""
    for c in ups:
        q, patch = c["input"], sg._patch(c["input"])
        vals = []
        if isinstance(q.get("description"), str):
            vals.append(q["description"])
        if isinstance(patch, dict):
            if isinstance(patch.get("description"), str):
                vals.append(patch["description"])
        elif isinstance(patch, list):
            for op in patch:
                if isinstance(op, dict):
                    v = op.get("value") if isinstance(op.get("value"), str) else op.get("text")
                    if isinstance(v, str):
                        vals.append(v)
        for v in vals:
            text = (text + "\n" + v) if text else v
    return text, []


def old_table_unreadable(table):                          # a readable earlier register masked a later unreadable one
    def f(run, spec):
        t = table(run, spec)
        if t["meta"].get("unreadable"):
            for c in reversed(t["candidates"]):
                if c.get("rows") is not None:
                    t = dict(t, rows=c["rows"], meta=dict(t["meta"], unreadable=False))
                    break
        return t
    return f


def old_decode_identity(decode):                          # the last shared file, not the register's own id
    def f(run, surface):
        d = decode(run, surface)
        shares = d["writes"].get("gdrive_share_file", [])
        d["table_identity"] = shares[-1]["input"].get("fileId", "") if shares else ""
        d["link"] = d["table_identity"]
        return d
    return f


def old_delivery_reply(args, sent):                       # the id and "false" anywhere in the serialized inputs
    return any(args[0] in json.dumps(c["input"]) and "false" in json.dumps(c["input"]).lower()
               for c in sent("gmail_reply_to_message"))


def old_delivery_thread(args, sent):                      # the id anywhere in the payload
    return any(args[0] in json.dumps(c["input"]) for c in sent("slack_send_message"))


def old_declared_gates(surface, runs, context, views, _g=sg.gates):   # declared gradable:false slots dropped
    s = dict(surface, slots=[x for x in surface["slots"] if x.get("gradable") is not False])
    return _g(s, runs, context, views)


def old_tracker_updates(w, tool, issue):                  # substring issue match, else every update
    ups = sorted(w.get(tool, []), key=lambda c: c["event"])
    if not issue:
        return ups
    named = [c for c in ups if str(issue) in str(c["input"].get("id") or c["input"].get("issueId") or "")]
    return named or ups


def old_tracker_entry(sel, line, known_hex, kreg=None):    # key and every value anywhere on the line
    return bool(re.search(re.escape(sel[2]), line)) and all(old_entry_match(line, rx, known_hex) for rx in sel[3])


def old_range_only(line, krx):                            # every key occurrence is a range endpoint
    keys = re.findall(krx, line)
    if not keys:
        return False
    ends = set()
    for m in re.finditer(f"(?P<a>{krx})\s*(?:\.\.|–|—|\bthrough\b|\bthru\b|\bto\b)\s*(?P<b>{krx})", line, re.I):
        ends.update((m.group("a"), m.group("b")))
    return all(k in ends for k in keys)


def dropping_unreadable(table):                           # undecodable register writes dropped silently
    def f(run, spec):
        t = table(run, spec)
        t["candidates"] = [c for c in t["candidates"] if c.get("rows") is not None]
        t["meta"] = dict(t["meta"], unreadable=False)       # the old decoder had no uncertainty flag
        return t
    return f


def ignoring_unreadable(tracker_text):                    # unreadable tracker patches ignored
    return lambda ups: (tracker_text(ups)[0], [])


def unknown_as_false(gates):                              # UNGRADED converted to false before the gates
    def f(surface, runs, context, views):
        runs = {lab: dict(r, results={k: bool(v) for k, v in r["results"].items()}) for lab, r in runs.items()}
        return gates(surface, runs, context, views)
    return f


def old_content_strings(calls):                           # 3: the JSON dump, identifiers included
    return "\n".join(json.dumps(c["input"], ensure_ascii=False) for c in calls)


def old_tracker_groups(text, spec):                       # 6: endpoints only, no range rule, last-number count
    groups, pending = {}, None
    krx = sg._krx(spec)
    prefix = re.split(r"\\", krx)[0]
    for line in text.split("\n"):
        s = line.strip()
        if not s:
            continue
        keys = re.findall(krx, s)
        head = s.split(prefix)[0] if keys and prefix else s
        g = sg._group_of(head, spec.get("groups") or [])
        nums = re.findall(r"\d+", re.sub(r">\s*0|above zero|^\W*\d+\.\s", "", head))
        if keys and g and nums and g not in groups:
            groups[g] = (int(nums[-1]), keys)
            pending = None
        elif keys and pending and not head.strip(" *-|:"):
            groups.setdefault(pending[0], (pending[1], keys))
            pending = None
        elif not keys and g and nums and len(s) < 160:
            pending = (g, int(nums[-1]))
        else:
            pending = None
    return groups


def pre_r8_groups(text: str, spec: dict) -> dict:
    """The pre-R8 decoder: a pending group takes only its first continuation line (the defect G1 R8 plants)."""
    groups, pending = {}, None
    krx = sg._krx(spec)
    for line in text.split("\n"):
        s = line.strip()
        if not s:
            continue
        keys = sg._expand_keys(s, krx)
        first = re.search(krx, s)
        head = s[:first.start()] if first else s
        g = sg._group_of(head, spec.get("groups") or [])
        tail = re.sub(r"[\s*_:.)\-\u2014\u2013]+$", "", head.strip())
        tail_n = re.search(r"(?:^|[\s*_:(\u2014\u2013-])(\d+)$", tail)
        nums = [tail_n.group(1)] if tail_n else re.findall(r"\((\d+)\)", head)
        if keys and g and nums and g not in groups:
            groups[g] = (int(nums[-1]), keys)
            pending = None
            continue
        if sg._range_only(s, krx):
            pending = None
            continue
        elif keys and pending and not head.strip(" *-|:"):
            groups.setdefault(pending[0], (pending[1], keys))
            pending = None
        elif not keys and g and nums and len(s) < 160:
            pending = (g, int(nums[-1]))
        else:
            pending = None
    return groups


UNDO = [("defect 1 heading", [(sg, "_section_start", old_section_start)]),
        ("defect 2 section body", [(sg, "_section_body", old_section_body)]),
        ("defect 3 plain text", [(sg, "_content_strings", old_content_strings)]),
        ("defect 4 every update", [(sg, "tracker_final_state", old_final_state), (sg, "tracker_preserved", old_preserved)]),
        ("defect 5 bullet key list", [(sg, "_row_keys", old_row_keys)]),
        ("defect 6 range prose", [(sg, "tracker_groups", old_tracker_groups)]),
        ("defect 7 tool alias", [(sg, "TOOL_ALIASES", {})]),
        ("defect 8 SHA prefix", [(sg, "_entry_match", old_entry_match)]),
        ("unreadable register", [(tl, "table", dropping_unreadable(tl.table))]),
        ("unreadable tracker", [(sg, "tracker_text", ignoring_unreadable(sg.tracker_text))]),
        ("UNGRADED gates", [(sg, "gates", unknown_as_false(sg.gates))]),
        ("replay replacement", [(sg, "tracker_text", old_tracker_text)]),
        ("register replacement", [(tl, "table", old_table_unreadable(tl.table))]),
        ("delivery binding", [(sg, "reply_match", old_delivery_reply), (sg, "thread_match", old_delivery_thread)]),
        ("register identity", [(sg, "decode", old_decode_identity(sg.decode))]),
        ("declared-ungradable gates", [(sg, "gates", old_declared_gates)]),
        ("entry tail", [(sg, "tracker_entry_match", old_tracker_entry)]),
        ("issue exact", [(sg, "tracker_updates", old_tracker_updates)]),
        ("range endpoint member", [(sg, "_range_only", old_range_only)]),
        ("R8 multi-line group", [(sg, "tracker_groups", pre_r8_groups)])]


def planted_failures() -> list:
    out = []
    for name, case in sg.PLANTED_G1:
        if name.startswith("formats"):
            continue
        try:
            case()
        except Exception as error:  # noqa: BLE001 - every failure is the evidence
            out.append((name, f"{type(error).__name__}: {str(error)[:110]}"))
    return out


def fixture_flips() -> list:
    m = json.loads((sg.FORMAT_FIXTURES / "MANIFEST.json").read_text())
    surfaces = {rev: gs.load(sg.FORMAT_FIXTURES / x["surface"]) for rev, x in m["revisions"].items()}
    truths = {rev: json.loads((sg.FORMAT_FIXTURES / x["truth"]).read_text()) for rev, x in m["revisions"].items()}
    flips = []
    for f in m["fixtures"]:
        s = surfaces[f["revision"]]
        res = sg.grade(s, truths[f["revision"]], sg.decode(tl.load(sg.FORMAT_FIXTURES / f["file"], f["label"]), s))
        bad = sorted(k for k in f["results"] if res.get(k) != f["results"][k])
        if bad:
            flips.append(f"{f['revision']} {f['label']}: {bad[:6]}{' …' if len(bad) > 6 else ''}")
    return flips


def main() -> int:
    ok = True
    control, flips = planted_failures(), fixture_flips()
    good = not control and not flips
    ok = ok and good
    print(f"{'ok  ' if good else 'FAIL'} control (nothing undone): {len(sg.PLANTED_G1) - 1} planted cases pass, "
          f"12 format fixtures grade as recorded" + ("" if good else f" - {control} {flips}"))
    for name, patches in UNDO:
        saved = [(mod, attr, getattr(mod, attr)) for mod, attr, _ in patches]
        try:
            for mod, attr, new in patches:
                setattr(mod, attr, new)
            failing, flips = planted_failures(), fixture_flips()
        finally:
            for mod, attr, old in saved:
                setattr(mod, attr, old)
        caught = any(n == name for n, _ in failing)
        ok = ok and caught
        print(f"{'ok  ' if caught else 'FAIL'} {name} undone: its planted case "
              f"{'fails' if caught else 'still passes'}"
              + "".join(f"\n       {n}: {e}" for n, e in failing if n == name)
              + (f"\n       also failing: {[n for n, _ in failing if n != name]}" if any(n != name for n, _ in failing) else "")
              + (f"\n       format fixtures flipped: {flips}" if flips else "\n       format fixtures: none flipped"))
    print("G1 FALSIFICATION " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
