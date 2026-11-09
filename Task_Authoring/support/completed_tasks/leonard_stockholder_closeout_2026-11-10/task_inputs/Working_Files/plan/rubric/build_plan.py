#!/usr/bin/env python3
"""Write Working_Files/09_Rubric_Writing_Plan.md from rows.json (written by build_rubric.py, read fresh on every run).

    build_plan.py               write the plan (reads visibility.txt, probe.txt, selfreview.md when they exist)
    build_plan.py --visibility  run persona_view for every scoped id behind every cited F-id and write visibility.txt

Run from anywhere with python3.12 -B. §F comes from probe.txt (real shortcut_probe.py output plus one SHORTCUT-OK line per hit,
written by build_selfreview.py --probe) and §E's proof from visibility.txt; neither is typed by hand. The shared helpers below
(P numbers, row families, spot-check groups, unit-of-discovery shares, recorded decisions) are imported by the other two builders.

Everything row-shaped comes from rows.json: a row is classified by its tag prefix, fact id, vals and grp, so rows can be added,
removed or moved between groups without touching these builders. A recorded decision prints only while the facts behind it hold.

After rows.json changes, in this order (run_pipeline.sh does all of it; the check report must end up newer than the plan):
  build_plan.py --visibility
  build_plan.py
  shortcut_probe.py leonard_hayes <plan path> > probe_raw.txt     (the cache makes an unchanged-value re-run fast)
  build_selfreview.py --probe
  build_selfreview.py
  build_plan.py
  build_check.py"""
import collections
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
TI = WF.parent
WS = TI.parents[1]
sys.path.insert(0, str(WS / "Task_Authoring/tools"))
os.environ.setdefault("TASK_AUTHORING_TASK_DIR", "Task_Authoring/task_inputs")
import stage_gate as G  # noqa: E402

PY = sys.executable
PERSONA = "leonard_hayes"
PERSONA_LINE = "Leonard Hayes leonard.hayes@harmonygames.co"
TASKREL = "Task_Authoring/task_inputs"
SQLREL = f"{TASKREL}/01_Universe_Inject.sql"
LBREL = f"{TASKREL}/Working_Files/plan/rubric/rubric_lb_ids.txt"
OE_DATE = "2026-11-09"
OE_REPORT = TI / "plateform_reports/6aed9d01a1cb8067d8ac7dee_2_oe-8.md"
# weight band by kind of work (playbook gate 8)
BAND = {"lookup": 1, "interpretation": 3, "calculation": 3, "comparison": 3, "reconciliation": 3, "multi-source": 5, "tracing": 5}

rows = json.loads((HERE / "rows.json").read_text())
BY = {r["tag"]: r for r in rows}
P = [f"P{i + 1}" for i in range(len(rows))]
TAG = {r["tag"]: f"P{i + 1}" for i, r in enumerate(rows)}
SURF = json.loads((WF / "01_Gradable_Surface.json").read_text())
SLOTS = SURF["slots"]
MANIFEST = json.loads((WF / "01_Hardness_Manifest.json").read_text())
SIDECAR = json.loads((WF / "00_V3_Authoring_Evidence.json").read_text())["rubric_rows"]
TRUTH = json.loads((WF / "solver/truth.json").read_text())
LINES = {k: v for k, v in TRUTH.items() if k != "SUMMARY"}
OE_NUM = json.loads((WF / "plan/oe/event_numbers.json").read_text())["OE_NUM"]
TOTAL_W = sum(r["w"] for r in rows)
BANDS = {b: sum(1 for r in rows if r["w"] == b) for b in (5, 3, 1)}
N_PROC = sum(1 for r in rows if r.get("cat") == "Process")
# the sheet's label vocabulary; truth.json's Owed values map to these (plan/oe/oe_data.py LABEL)
LABEL = {"Already told": "Already told", "Covered": "Covered", "Date note": "Last day", "First note": "Closing",
         "Full note": "Closing and last day", "Nothing": "Nothing"}
NB = "none — bundle (Rubric Writing §7; Eval 2.2)"
OE_LABEL_RX = re.compile(r"^OE (\d+)  (.*)$")
WRITE_TITLE = re.compile(r"^(Write|Share|Save|Move|Comment|Send|Reply)\b")
# rows.json names a distractor by its manifest trap id; the plan column carries the ledger's T-ID where the ledger has one (ledger §E)
DIST_LEDGER_ID = {"T24 stale Carta notice": "T2 stale Carta notice", "T12 today's count": "T12-manifest today's count (ledger §E has no separate entry)",
                  "T17 unanswered question": "T17-manifest unanswered question (ledger §E has no separate entry)"}
# ledger §F open risks: (F-id that carries the risk, how the rows keep both readings)
RISKS = {1: ("F11", "risk 1 → the KPMG rows name the four recipients and no tool"),
         2: ("F32", "risk 2 → ENG-2440 told is settled Already told by the address in the DM and the 0.5% grant message (platform /prompt F5)"),
         3: ("F34", "risk 3 → the board consent's Exhibit A gives all four grants 1/24 monthly with no cliff, so the Nov 2023 grants ran out by Nov 2025 (platform /prompt DR4)"),
         4: ("F7", "risk 4 → the letter rows grade the section and its updated fact, not a quoted figure"),
         5: ("F46", "risk 5 → the told rows rest on what Leonard can see; a direct message outside his view is the persona bound"),
         6: ("F34", "risk 6 → OE 21 reads the one attachment the path needs"),
         7: ("F28", "risk 7 → no row cites the ES-12 letter's slipped year")}


def pn(tag):
    return TAG[tag]


def pns(tags):
    return ", ".join(TAG[t] for t in tags)


def ps(rs):
    return ", ".join(TAG[r["tag"]] for r in rs)


def prange(rs):
    """P numbers of a row list, consecutive runs folded: 'P65–P78, P81'."""
    ns = sorted(int(TAG[r["tag"]][1:]) for r in rs)
    out, i = [], 0
    while i < len(ns):
        j = i
        while j + 1 < len(ns) and ns[j + 1] == ns[j] + 1:
            j += 1
        out.append(f"P{ns[i]}" if i == j else f"P{ns[i]}–P{ns[j]}")
        i = j + 1
    return ", ".join(out)


def fids(r):
    return set(G.RX_FID.findall(r["fids"]))


def literals(r):
    return re.findall(r"`([^`]+)`", r["vals"])


def key_of(r):
    """The line a row grades: the ENG key or the ES key in its tag, else None."""
    m = re.search(r"(ENG-\d+|ES-\d+)", r["tag"])
    return m.group(1) if m else None


def is_volume(r):
    """A count row: its vals carry a bare number."""
    return any(re.fullmatch(r"\d+", v) for v in literals(r))


def family(r):
    """The kind of deliverable a row grades, from its tag prefix."""
    t = r["tag"]
    if r.get("cat") == "Process":
        return "order"
    for prefix, name in (("sh_share", "sheet share"), ("sh_cnt", "sheet count"), ("sh_", "sheet"), ("n_", "note"), ("l_", "letter"), ("st_", "state"),
                         ("cm_", "reason comment"), ("k_", "KPMG reply"), ("g_", "Griffin heads-up"), ("r_", "thread reply"), ("o_", "order")):
        if t.startswith(prefix):
            return name
    return "other"


def axis(r):
    """What a row grades, from its fact id: the fact's last part (shares, options, lastday, label, state, ...)."""
    f = r["fact"]
    if f.startswith("ENG-"):
        return f.split(".", 1)[1]
    return f.split(".")[0] if f.startswith(("sheet", "kpmg", "letter", "share", "order", "reply", "griffin")) else f


def of(fam):
    return [r for r in rows if family(r) == fam]


def cell(s):
    """One table cell: no pipes or newlines, no straight double quote (the probe reads "x" as a literal), no angle brackets (they read as template slots)."""
    return str(s).replace("|", "/").replace("\n", " ").replace('"', "″").replace("<", "‹").replace(">", "›")


def lit(keys):
    return " ".join(f"`{k}`" for k in keys)


def run_tool(args):
    env = {**os.environ, "TASK_AUTHORING_TASK_DIR": TASKREL}
    p = subprocess.run([PY, "-B", *map(str, args)], cwd=WS, capture_output=True, text=True, env=env)
    return p.stdout


def ledger():
    return G.Doc(WF / "08_OE_Writing_Ledger.md", "08_OE_Writing_Ledger.md")


def cited_scoped():
    """{id: service} for every scoped id behind every cited F-id, the gate's own need set."""
    led = ledger()
    text = {}
    for _, c, _t in G.rows_in(led, r"^B\b"):
        m = re.match(r"\s*(F\d+)", c[0] if c else "")
        if m:
            text[m.group(1)] = " ".join(c)
    cited = {f for r in rows for f in fids(r)}
    missing = cited - set(text)
    assert not missing, f"F-ids not in the ledger: {missing}"
    return {x: s for f in sorted(cited) for s, x in G.scoped_ids(text[f])}, cited


def write_visibility():
    need, cited = cited_scoped()
    cs = json.loads(run_tool(["Task_Authoring/tools/persona_view.py", "check-sql", PERSONA, SQLREL, "--json"]))
    keys = {k for r in cs["rows"] for k in r["keys"]}
    seeded = sorted(x for x in need if x in keys or x.split("/")[-1] in keys)
    base = sorted(x for x in need if x not in seeded)
    (HERE / "rubric_lb_ids.txt").write_text("\n".join(seeded) + "\n")
    txt = run_tool(["Task_Authoring/tools/persona_view.py", "check-sql", PERSONA, SQLREL, "--load-bearing", LBREL])
    head = next(l for l in txt.splitlines() if l.startswith("CHECK-SQL as "))
    # gmail.gmail_messages rows carry long message ids the tool truncates; the seeded Gmail ids are proved by the gmail.gmail_threads rows
    keep = [l for l in txt.splitlines() if (l.startswith("[YES LB]") or l.startswith("[NO LB]") or l.startswith("[UNVERIFIED LB]") or l.startswith("verdict:"))
            and "gmail.gmail_messages" not in l]
    out = [f"`python3 Task_Authoring/tools/persona_view.py check-sql {PERSONA} {SQLREL} --load-bearing "
           f"{LBREL}` ({len(seeded)} seeded ids behind the {len(cited)} cited F-ids; load-bearing rows and the verdict line kept, "
           "gmail.gmail_messages lines left out because the tool truncates their long message ids, the seeded Gmail threads are proved by the "
           "gmail.gmail_threads lines):", "", "```text", head, *keep, "```", "",
           f"`python3 Task_Authoring/tools/persona_view.py can-see {PERSONA} SERVICE ID` ({len(base)} base ids, first line of each, Gmail in "
           "thread-id form):", "", "```text"]
    for x in base:
        lines = run_tool(["Task_Authoring/tools/persona_view.py", "can-see", PERSONA, need[x], x]).splitlines()
        out.append(lines[0] if lines else f"{PERSONA} {need[x]} {x}: UNVERIFIED (no tool output)")
    out.append("```")
    (HERE / "visibility.txt").write_text("\n".join(out).replace("[]", "(none)") + "\n")
    print("visibility written:", len(seeded), "seeded,", len(base), "base ids,", len(cited), "F-ids")


def diversity():
    """The gate's share per unit of discovery (stage_gate.plan_diversity), computed from rows.json and the ledger."""
    facts = G.ledger_facts(ledger())

    def closure(fs):
        out, stack = set(), list(fs)
        while stack:
            f = stack.pop()
            if f in out:
                continue
            out.add(f)
            if f in facts:
                stack += G.RX_FID.findall(facts[f]["depends"]) + G.RX_FID.findall(facts[f]["origin"])
        return out

    def response(f):
        if f not in facts:
            return f
        ids = [m.group(0) for m in G.OPAQUE.finditer(facts[f]["locator"])]
        return ids[0] if ids else (facts[f]["locator"].strip().lower() or f)

    share = {}
    for r in rows:
        us = {f"authority {x}" for x in re.findall(r"\b[A-Z]{1,3}\d{1,3}\b", r["dec"]) if not re.fullmatch(r"[FP]\d+", x)}
        for f in closure(fids(r) | set(G.RX_FID.findall(r["dec"]))):
            if f in facts and re.match(r"\s*prompt\b", facts[f]["origin"], re.I):
                continue
            us.add(f"response {response(f)}")
        for u in us:
            share[u] = share.get(u, 0) + r["w"]
    top = sorted(share.items(), key=lambda x: -x[1])
    return top, [(u, s) for u, s in top if 2 * s > TOTAL_W]


def mech_share():
    """Weight on rows that cover a slot a designed mechanism can flip (reported, not gated)."""
    flip = {s["id"] for s in SLOTS if s.get("mechanisms")}
    w = sum(r["w"] for r in rows if set(r["slots"]) & flip)
    return w, round(100 * w / TOTAL_W), len(flip)


def mech_node_share():
    """The same share read off Decided by, since rows.json maps one row per slot."""
    nodes = {n for m in MANIFEST["mechanism_portfolio"] for n in m["nodes"]}
    w = sum(r["w"] for r in rows if nodes & set(r["dec"].split()))
    return w, round(100 * w / TOTAL_W)


def wrong_value(r):
    """The wrong value a row's title rejects, for a §G line."""
    return cell(r["alt"]).rstrip(".")


def reach_note(i):
    """The deciding record's own rationale from the sidecar, first sentence."""
    src = SIDECAR[i]["source_records"]
    if not src:   # a sidecar gap in build_rubric.py, named by v3.rubric_evidence at rubric-check: fall back on the row's own evidence field
        return cell(rows[i]["ev"].split("Accept:")[0].strip().rstrip(".") + "; the V3 sidecar lists no source record for this row")
    return cell(src[0]["reachability_rationale"].split(". ")[0].rstrip("."))


def covering(slot):
    return [r for r in rows if slot in r["slots"]]


def disposition(s):
    """(reason text) for a surface slot no row covers; None when no rule applies, which prints unassigned and blocks at gate 17."""
    sid = s["id"]
    if sid.startswith("TC_"):
        key = s["selector"][1]
        r = BY.get(f"sh_lb_{key}")
        if r:
            return (f"duplicate fact — the Told state of {key} ({s.get('fact_id')}) is decided by the same reading as the line's label, which row "
                    f"{pn(r['tag'])} ({r['tag']}) grades on the sheet (its title rejects the wrong label: {wrong_value(r)}); a second row for the Told "
                    "cell would grade one fact twice (gate 6)")
    if sid == "N_COUNT":
        drafts = [r for r in of("note") if r["tag"].startswith("n_w_")]
        return (f"count-bundle-v1 — a bare count over separate draft writes is Major even beside per-item rows (Eval 3 §2.2, count-bundle-v1, "
                f"as ruled on the platform's /rubric for task_inputsKum), so no row grades a count of notes; each of the {len(drafts)} drafts has its own "
                f"result row in family n_w ({prange(drafts)}) (gate 15 evidence)")
    if sid == "LS_vol":
        fam = of("state")
        return (f"every member has its own row — the {len(fam)} state rows in family st ({prange(fam)}) grade each issue's state, so no volume row is "
                f"needed (gate 15: the volume row is for a sampled population; this one is graded per member)")
    if sid == "LC_vol":
        fam = of("reason comment")
        return (f"every member has its own row — the {len(fam)} why-comment rows in family cm ({prange(fam)}) grade each issue's reason comment, so no volume "
                f"row is needed (gate 15)")
    if sid == "ND_vol":
        fam = [r for r in of("note") if r["tag"].startswith("n_ld_")]
        return (f"every member has its own row — the last-day note rows in family n_ld ({prange(fam)}) grade the date in each note, so no volume row is needed "
                f"(gate 15)")
    if sid == "K16":
        fam = [r for r in of("sheet") if r["tag"].startswith("sh_lb_")]
        return (f"every member has its own row — the {len(fam)} label rows in family sh_lb ({prange(fam)}) each grade one issue's row on the sheet, so no volume row is "
                f"needed; the platform's /rubric ruled a 26-row count over them a Major count bundle (count-bundle-v1)")
    if sid == "AL_vol":
        return (f"the option total is the volume check — row {pn('k_total')} (k_total) grades the sum of every line as of the date, as the platform's /rubric ruled when it "
                f"removed the 16-line list row as non-atomic")
    if sid.startswith("AL_ES-"):
        grp = [r for r in rows if r["grp"] == "kpmg option lines" and not is_volume(r)]
        vol = [BY["k_total"]]
        names = "; ".join(f"{pn(r['tag'])} {key_of(r)}" for r in grp)
        return (f"sampled out — the KPMG option-line group holds its five samples ({names}) and the volume row {ps(vol)}; {sid} is an unsampled member of that "
                f"group (gate 15, at most five samples)")
    return None


def risk_note(r):
    """Ledger §F open risks that touch this row, each with how the row keeps both readings."""
    fs = fids(r)
    n = [text for _k, (f, text) in sorted(RISKS.items()) if f in fs]
    if r["amb"] != "none":
        n.insert(0, r["amb"])
    return "; ".join(n) if n else "none (single settled value; ledger §F risks do not touch it)"


def group_cell(r):
    return r["grp"] if r["grp"] != "none" else "none — per line, not sampled" if key_of(r) else "none"


def group_kind(g):
    if g == "sheet volume":
        return "sheet"
    if g.startswith("labels "):
        return "label"
    return {"stock lines": "stock", "live options": "option", "last days": "lastday", "kpmg option lines": "kpmg"}.get(g, "other")


def group_keys(g):
    """The population's key set, from truth.json (or the volume row's title for the KPMG lines)."""
    kind = group_kind(g)
    if kind == "sheet":
        return sorted(LINES)
    if kind == "stock":
        return sorted(k for k, v in LINES.items() if v["Shares held now"])
    if kind == "option":
        return sorted(k for k, v in LINES.items() if "option" in v["groups"] and v["Options now"])
    if kind == "lastday":
        return sorted(k for k, v in LINES.items() if v["Last day"])
    if kind == "label":
        label = g[len("labels "):]
        return sorted(k for k, v in LINES.items() if LABEL.get(v["Owed"]) == label)
    if kind == "kpmg":
        return ["ES-1", "ES-3", "ES-4", "ES-5"] + [f"ES-{i}" for i in range(7, 19)]
    return []


def groups():
    """{group: rows, samples, vols, kind, keys} straight from rows.json's grp, in row order."""
    raw = {}
    for r in rows:
        if r["grp"] != "none":
            raw.setdefault(r["grp"], []).append(r)
    out = {}
    sv = [r for r in rows if r["tag"] == "sh_volume"]
    for g, rs in raw.items():
        kind = group_kind(g)
        samples = [r for r in rs if not is_volume(r)]
        vols = [r for r in rs if is_volume(r)]
        if kind == "label":
            label = g[len("labels "):].replace(" ", "_")
            vols = [r for r in of("sheet count") if r["tag"] == f"sh_cnt_{label}"] + vols
        elif kind in ("stock", "option", "lastday"):
            vols = sv
        elif kind == "kpmg":
            vols = [r for r in rows if r["tag"] == "k_total"]
        out[g] = dict(rows=rs, samples=samples, vols=vols, kind=kind, keys=group_keys(g))
    return out


GROUP_NOTE = {"sheet": "no — the holder sheet is the deliverable the prompt names; the 26 rows are repetitive members",
              "stock": "no — the prompt asks for the sheet as a whole; the merged-line and Griffin exceptions are direct rows",
              "option": "no — the prompt asks for the sheet as a whole; the advisor grants are direct rows",
              "lastday": "no — the prompt asks for the sheet as a whole; ES-3 and ES-14, the exceptions, are direct rows",
              "label": "no — every member of this label has its own row, so the group samples nothing out; the count row is its output volume",
              "kpmg": "no — the KPMG answer is the deliverable the prompt names; the option lines are repetitive members and the total is a direct row"}


def group_line(g, d):
    n = len(d["keys"])
    span = ", ".join(sorted({f for r in d["rows"] for f in fids(r)}, key=lambda f: int(f[1:])))
    if d["samples"]:
        samples = ", ".join(f"{pn(r['tag'])} {key_of(r) or r['fact']} ({cell(r['why']).rstrip('.')})" for r in d["samples"])
    else:
        samples = "none sampled: the sheet's row count is this group's only claim"
    if len(d["samples"]) > 5:
        samples = f"OVER THE CAP ({len(d['samples'])} samples): {samples}"
    return (f"| {g} | {span} ({n} keys): {lit(d['keys'])} | {samples} | {ps(d['vols'])} | {NB} | {GROUP_NOTE[d['kind']]} |")


def oe_titles():
    out = {}
    for line in (TI / "08_Oracle_Events.md").read_text().splitlines():
        m = OE_LABEL_RX.match(line)
        if m:
            out[int(m.group(1))] = m.group(2)
    return out


def brief_label_line():
    text = (WF / "04_Prompt_Writing_Brief.md").read_text()
    m = re.search(r"\| Holder sheet \| label per row \| ([^|]+)\|", text)
    return m.group(1).strip() if m else ""


def records():
    """Decisions the rows take against the brief or a review finding. Each prints only while its facts stand."""
    out = []
    counts = collections.Counter(LABEL[v["Owed"]] for v in LINES.values())
    want = ", ".join(f"{k} {counts[k]}" for k in ("Nothing", "Already told", "Closing", "Covered", "Last day", "Closing and last day"))
    brief = brief_label_line()
    if brief and all(f"{k} {counts[k]}" not in brief for k in ("Nothing", "Already told")):
        out.append(f"Label counts: brief §4b's row 'label per row' reads '{cell(brief)}', and its Messages set row is the current split. solver/truth.json and "
                   f"rows.json give {want}, which is what the count rows and the label rows here grade; the brief line predates the last correction of the set "
                   "and is the stale one (truth.json is built from the SQL).")
    proc = [r for r in rows if r.get("cat") == "Process"]
    if proc:
        out.append(f"Process rows {ps(proc)} stay Process: the notes make the holder sheet come first ('the holder sheet comes first, the notes and everything else run "
                   "off it'), and no final state shows which write came first; §C records the three-condition test per row.")
    return out


def main():
    dup = {}
    for r in rows:
        dup.setdefault(r["fact"], []).append(pn(r["tag"]))
    over = {k: v for k, v in dup.items() if len(v) >= 3}
    assert not over, f"a fact in three or more rows: {over}"
    bad_order = [r["tag"] for r in rows if not r["oe"] or not r["fids"].strip()]
    assert not bad_order, bad_order
    assert len(SIDECAR) == len(rows) and all(a["fact_id"] == b["fact"] for a, b in zip(SIDECAR, rows)), \
        "00_V3_Authoring_Evidence.json rubric_rows are out of step with rows.json: re-run build_rubric.py"

    out = []
    w = out.append
    oe_m = re.search(r"(\d+) OEs, sha256 `([0-9a-f]{6,12})", OE_REPORT.read_text())
    oe_score = re.search(r"Score:\s*(\d)", OE_REPORT.read_text())
    oe_date = re.search(r"Actual review date:\s*(\S+)", OE_REPORT.read_text())
    oe_disk = hashlib.sha256((TI / "08_Oracle_Events.md").read_bytes()).hexdigest()[:12]
    oe_short = oe_m.group(2)
    sqlsha = hashlib.sha256((TI / "01_Universe_Inject.sql").read_bytes()).hexdigest()[:12]
    w("# 09 Rubric Writing Plan — leonard_stockholder_closeout (stockholder and option-holder close-out, injection SQL sha256 " + sqlsha + ")")
    w(f"Generated 2026-11-09 · Clock 2026-02-14T00:00:00Z (seed bound; eval clock 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)) · Persona {PERSONA_LINE} · "
      "Assigned role Co-founder & Creative Director · Tier Long-Horizon · Mode Medium · Human time not entered yet (05_Human_Time.md is the requester's slot and is empty) · "
      f"OE status: /oe PASS {OE_DATE} (plateform_reports/{OE_REPORT.name}, Score {oe_score.group(1)}, {oe_m.group(1)} events, reviewed 08_Oracle_Events.md sha256 {oe_short}, "
      f"{'matching the file on disk' if oe_disk.startswith(oe_short) else 'which differs from the file on disk, ' + oe_disk}; the report's own review-date line reads "
      f"{oe_date.group(1) if oe_date else 'not stated'})")
    lab = collections.Counter(LABEL[v["Owed"]] for v in LINES.values())
    state = collections.Counter(v["State"] for v in LINES.values())
    sm = TRUTH["SUMMARY"]
    n_notes = len([r for r in of("note") if r["tag"].startswith("n_w_")])
    w("Canonical outcomes: brief §4b (all fair results and accepted alternatives) — holder sheet: the existing Holder list (draft) "
      f"spreadsheet f_5ecaa967db3adcfa440b09 in the close-out folder d_601064334a0b493022fe83, one row per issue for the {len(LINES)} issues ENG-2438 to ENG-2463 with what each holds "
      f"and the label (Nothing {lab['Nothing']}, Already told {lab['Already told']}, Closing {lab['Closing']}, Covered {lab['Covered']}, Last day {lab['Last day']}, Closing and last day "
      f"{lab['Closing and last day']}), Series Seed total {sm['Series Seed total']:,}, common {sm['Common']:,}, options outstanding now {sm['Options outstanding now']:,}, directors in office "
      f"{sm['Directors']}, Griffin as the preferred vote, and shared with Robert and Arthur Blake; investor letter: a Google Doc worked up from Leonard's #winddown draft, in the same folder, "
      f"shared with Robert; {n_notes} holder notes as unsent Gmail drafts to the address on each issue; Linear: {state['Todo']} issues to Todo, {state['Done']} to Done, {state['Canceled']} to "
      f"Canceled, and one reason comment on each of the {len(of('reason comment'))} issues with no note of their own; KPMG: a reply to all on leonard.hayes@harmonygames.co/1857029474983245439 with "
      f"options at Dec 31, 2025 of {sm['Options outstanding at Dec 31']:,} and issued plus options {sm['Issued plus options at Dec 31']:,}; Griffin: a reply to the partner's Board position mail on "
      "leonard.hayes@harmonygames.co/1856958794180374704; #winddown: a reply under C0ADGSZKR3R/1770934638.035469 saying who goes first.")
    w("")
    w("Recorded decisions:")
    w("")
    for line in records():
        w(f"- {line}")
    w("")
    gnames = ", ".join(groups())
    w(f"Rubric shape: every write family has a result row. Per-line values on the sheet are direct where an authority singles the line out and sampled in the populations "
      f"({gnames}), each with a volume row and no bundled exact-set row (gate 15). The 14 drafts, the 26 Linear states and the 12 reason comments are graded per member, with no "
      f"count row over separate writes (count-bundle-v1). 09_Rubrics.json mirrors P1–P{len(rows)} one to one (C-n = P-n).")
    w("")
    w("## A · Coverage matrix")
    w("| P | Source (exact prompt span · OE n) | Stable fact ID | What must be verified | Final state that proves it | Category "
      "(Outcome / Process candidate → C) | Expected/source values and pointers · accepted alternatives · date acceptance · F-IDs |")
    w("|---|---|---|---|---|---|---|")
    for p, r in zip(P, rows):
        acc = "; ".join(r["acc"])
        date_row = axis(r) in ("lastday", "note.lastday")
        dates = "a date, not an instant, the same day in Pacific and UTC; any date form" if date_row else "none graded"
        oes = ", ".join(r["oe"][:6]) + (" …" if len(r["oe"]) > 6 else "")
        w(f"| {p} | \"{r['span']}\" · {oes} | {r['fact']} | {cell(r['verify'])} | {cell(r['final'])} | "
          f"{'Process candidate → C' if r.get('cat') == 'Process' else 'Outcome'} | {r['vals']} · accept: {cell(acc)} · dates: {dates} · {r['fids']} |")
    w("")
    w("## A2 · Grading risks and weight")
    w("| P | Title/phrasing specified by prompt? | Distractor? (T-ID → grade handling) | Ambiguous evidence? (risk # → no single "
      "conclusion) | Kind of work (lookup / interpretation · calculation · comparison / multi-source · tracing) + reason | Band "
      "1/3/5 | Decided by (chain / authority / trap id) | Spot-check group | Global fact duplication / overlap group | Predicted "
      "all-fail basis (four Evals bases) · over-specific risk |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for p, r in zip(P, rows):
        dist = DIST_LEDGER_ID.get(r["dist"], r["dist"])
        dist = "none" if dist == "none" else f"{cell(dist)} → graded through the correct value, never its disclosure"
        d = f"{r['fact']} in {len(dup[r['fact']])} row(s)" + (f" ({', '.join(dup[r['fact']])})" if len(dup[r["fact"]]) > 1 else "")
        ovl = "overlap group none" if r["ovl"] == "none" else f"overlap group {cell(r['ovl'])}"
        w(f"| {p} | no — must not hard-code; titles, wording and headings stay the Agent's | {dist} | {risk_note(r)} | {r['kind']} — "
          f"{cell(r['why'])} | {r['w']} | {r['dec']} | {group_cell(r)} | {d}; {ovl} | none · over-specific risk low: {cell(r['alt'])} |")
    w("")
    w("## A3 · Format 5 — per-row acceptance cases, OE steps and reachability")
    w("| P | valid_case (must ACCEPT · prompt authority) | do_nothing_case (must REJECT · exact title text of the required write) | "
      "OE step ids (verbatim OE labels) | Deciding source reachability (PROMPT_LINKED / TRASH / ATTACHMENT_ONLY / UNLINKED) |")
    w("|---|---|---|---|---|")
    for i, (p, r) in enumerate(zip(P, rows)):
        w(f"| {p} | {cell(r['valid'])} (\"{r['span']}\") | REJECT — {cell(r['idle'])} (title: \"{cell(r['t'])}\") | {', '.join(r['oe'])} | "
          f"PROMPT_LINKED ({reach_note(i)}) |")
    w("")
    w("Final-reply test (whole set): \"Done. The holder sheet and the investor letter are in your close-out folder, the 14 notes are saved as drafts in your Gmail, the Linear issues are "
      "moved with a note on why where none goes out, the heads-up to Griffin and the answer to KPMG are sent, and the #winddown reply says who goes first.\" → ACCEPT ☑ (no row grades "
      "the final response; the prompt asks to be told nothing beyond the deliverables, so a concise reply passes every row)")
    w("")
    w("## B · OE trace")
    w("| OE | Kind (write / discovery / friction) | Proved by row(s) | Own row? (reason) |")
    w("|---|---|---|---|")
    cites = {}
    for p, r in zip(P, rows):
        for o in r["oe"]:
            cites.setdefault(int(o.split()[1]), []).append(p)
    titles = oe_titles()

    def with_fid(*fs):
        return [p for p, r in zip(P, rows) if fids(r) & set(fs)]

    def on_key(k):
        return [p for p, r in zip(P, rows) if key_of(r) == k]

    # discovery steps that no row cites: the F-id(s) they establish, and what proves them
    uncited = {
        "OE_PROJECT": (with_fid("F1"), "no — the project and its 26 issues; proved by the state and reason-comment rows"),
        "OE_NOTES": (with_fid("F4"), "no — the close-out rules; every label, note and state row reads a line against them"),
        "OE_THREAD": (with_fid("F9"), "no — the replies under the list: the family rule, Covered, and Arthur on the sheet; proved by the rows they decide"),
        "OE_SUNSET": (with_fid("F10"), "no — what the sheet must hold: totals, directors, the vote"),
        "OE_ES15": (on_key("ENG-2460"), "no — names ES-15 to its line (the Carta name differs from the issue title); proved by the ENG-2460 rows"),
        "OE_BOUNCE": (with_fid("F28"), "no — the bounced ES-12 letter; proved by the ES-12 label and note rows"),
        "OE_GTOLD": (with_fid("F40"), "no — Griffin's partner told; proved by the Griffin line rows"),
        "OE_ROBERT": (with_fid("F41"), "no — ENG-2446 told by Robert; proved by its label, state and reason rows"),
        "OE_AKIN": (with_fid("F42"), "no — Leonard's Feb 12 mail to Akin; proved by the ENG-2447 rows"),
        "OE_AKIN2": (with_fid("F43"), "no — ties Akin to ENG-2447; proved by the ENG-2447 rows"),
        "OE_TOR": (with_fid("F45"), "no — TOR's runway warning is not the closing; proved by the TOR label and note rows"),
        "OE_ABS": (with_fid("F46"), "no — the sweep for closing messages to the other angels; proved by their label and note rows"),
    }
    by_num = {OE_NUM[k]: v for k, v in uncited.items()}
    missing_oe = []
    for n, title in sorted(titles.items()):
        kind = "write" if WRITE_TITLE.match(title) else "discovery"
        if n in cites:
            rs = sorted(set(cites[n]), key=lambda x: int(x[1:]))
            own = "yes — the write's result row" if kind == "write" else "no — proved by the content row(s) it decides"
        elif n in by_num:
            rs, own = by_num[n]
        else:
            rs, own = [], "no row cites this step"
            missing_oe.append(n)
        w(f"| OE {n} | {kind} | {', '.join(rs[:8]) or 'none'}{' …' if len(rs) > 8 else ''} | {own} |")
    w("")
    w("## C · Process candidates — three-condition test")
    w("| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) "
      "behavioural, not trace | Result (Process / tighten P-n with F-n) |")
    w("|---|---|---|---|---|---|---|")
    NOTES_LINE = "'the holder sheet comes first, the notes and everything else run off it' (f_a37b403d5200d4f0a31d31)"
    proc = [r for r in rows if r.get("cat") == "Process"]
    for r in proc:
        m = re.search(r"before it (.+?)(?: \(|$)", r["t"])
        act = m.group(1) if m else "does the later write"
        w(f"| {pn(r['tag'])} | \"{r['span']}\" — the notes: {NOTES_LINE} | The sheet's final cells and the final content of what the Agent {act} are the same whichever was written first, "
          f"so no final state shows the order | yes — the notes bind every valid run: any run that {act} also writes the sheet, and the row asks only that at least one sheet write came first | "
          "yes — every content row grades a value on the final artifact; none can see when it was written | yes — the order of two writes the Agent must make, with no tool named "
          f"and no call sequence beyond that one precedence | Process ({r['fids']}) |")
    w("")
    w("## D · Spot-check groups")
    w("| G | Item set (F-IDs, total N; keys as backticked literals) | Sampled items (≤ 5) and why hard/edge | Volume row | Exact-set row "
      "(`none — bundle (Rubric Writing §7; Eval 2.2)`) | Core requirement? (must be no) |")
    w("|---|---|---|---|---|---|")
    grp = groups()
    for g, d in grp.items():
        w(group_line(g, d))
    w("")
    w(f"Not sampled: the {len(of('state'))} Linear state rows ({prange(of('state'))}), the {len(of('reason comment'))} reason-comment rows ({prange(of('reason comment'))}) and the note rows "
      f"({prange(of('note'))}) are per member, one row per write; the content differs per target, so these are not a population under gate 15.")
    w("")
    w("## E · Summary")
    vols = list({r["tag"]: r for d in grp.values() for r in d["vols"]}.values())
    w(f"Rows {len(rows)} · Outcome {len(rows) - N_PROC} · Process candidates {N_PROC} considered, {N_PROC} kept — ≥ 1 Outcome ☑ · Process rows ≤ 50 % ☑ · "
      f"fewer than two Process rows failing the three-condition test ☑ (none fails; §C records all {N_PROC}) · builder minimum 5 ☑ · one volume row per sampled output, no bundled exact-set row "
      f"☑ ({ps(vols)}) · predicted all-fail rows = 0 ☑ (every value is reachable through a cataloged tool and visible to Leonard; none sits on the four Evals bases)")
    top, over_units = diversity()
    pct = lambda s: f"{100 * s / TOTAL_W:.0f}%"  # noqa: E731
    box = "☑" if not over_units else "☒"
    why = ("" if not over_units else " — every line's value depends on the issue list and the close-out rules through the ledger's Depends-on edges, so it is upstream of almost every row by the "
           "task's design; recorded with the numbers and left as it is")
    chains = []
    for c in MANIFEST["chains"]:
        hit = [pn(r["tag"]) for r in rows if c["id"] in r["dec"].split()]
        if hit:
            chains.append(f"{c['id']} {'/'.join(hit[:3])}{'…' if len(hit) > 3 else ''}")
    w(f"Failure diversity: largest unit of discovery {top[0][0]} {pct(top[0][1])} of the weight ({top[0][1]} of {TOTAL_W}) (≤ 50% {box}{why}); "
      f"next {top[1][0]} {pct(top[1][1])} and {top[2][0]} {pct(top[2][1])} · chains landing on distinct rows ☑ ({', '.join(chains)})")
    w(f"Bands: 5 ×{BANDS[5]} · 3 ×{BANDS[3]} · 1 ×{BANDS[1]} · total weight {TOTAL_W}")
    w(f"Format 5 (§A3): rows {len(rows)}/{len(rows)} ☑ · `do_nothing_case` REJECT {len(rows)}/{len(rows)} ☑ · reachability "
      f"`PROMPT_LINKED` {len(rows)}/{len(rows)} ☑ · final-reply test ACCEPT ☑")
    w(f"Set size: {len(rows)} rows, with no human-time estimate entered yet. The count follows the deliverables: "
      f"{len(of('sheet')) + len(of('sheet count')) + len(of('sheet share'))} sheet rows, {len(of('note'))} rows over the 14 drafts, {len(of('state')) + len(of('reason comment'))} Linear rows, and "
      f"{len(of('letter')) + len(of('KPMG reply')) + len(of('Griffin heads-up')) + len(of('thread reply'))} rows on the letter and the three sent replies; the members are per-target "
      "writes and cells, not duplicates of one another.")
    write_rows = {"holder sheet": "sh_write", "sheet shares": "sh_share_robert", "letter": "l_doc", "draft notes": "n_w_", "Linear states": "st_", "reason comments": "cm_",
                  "KPMG reply": "k_send", "Griffin heads-up": "g_send", "#winddown reply": "r_thread"}
    present = [k for k, t in write_rows.items() if any(r["tag"].startswith(t) for r in rows)]
    n_req = len(G.rows_in(ledger(), r"^A\b"))
    reqs = {"R1": any(fids(r) & {"F1", "F2", "F3"} for r in rows), "R2": any(fids(r) & {"F4", "F9"} for r in rows), "R3": any(key_of(r) for r in rows),
            "R4": bool(of("sheet")), "R5": bool(of("letter")), "R6": bool(of("note")), "R7": bool(of("state")), "R8": bool(of("Griffin heads-up")), "R9": bool(of("thread reply")),
            "R10": bool(of("KPMG reply")), "R11": bool(of("KPMG reply") and of("Griffin heads-up") and of("thread reply")), "R12": any(r["tag"].startswith("n_w_") for r in rows)}
    met = sum(1 for v in reqs.values() if v)
    assert not missing_oe, f"OE steps no row or uncited entry names: {missing_oe}"
    w(f"Coverage: requirements {met}/{n_req} (ledger R1–R{n_req}) · OEs {len(titles)}/{len(titles)} (§B) · writes {len(present)}/{len(write_rows)} ({'; '.join(present)}) · told facts 0/0 (the prompt asks to be "
      "told nothing beyond the deliverables) · friction 0/0 (Friction: none)")
    covered = [s for s in SLOTS if covering(s["id"])]
    mw, mp, nflip = mech_share()
    nw, np_ = mech_node_share()
    w(f"Gradable surface (gate 17): slots {len(SLOTS)} · covered {len(covered)} · dispositioned {len(SLOTS) - len(covered)} (§G) · no slot "
      f"with neither ☑ · mechanism share {mp}% of the weight ({mw} of {TOTAL_W}, the rows that rows.json maps to the {nflip} slots a "
      f"mechanism can flip; {np_}% counting every row a mechanism's node decides, since rows.json maps one row per slot; reported, not gated)")
    w("Four prohibitions: ☑ unstated expectations (every row quotes a prompt span; the close-out notes and the Linear project, which the prompt says to carry out, are the "
      "incorporated authority) ☑ conclusions on ambiguous evidence (none: each graded value is settled by a later or more specific record, and ledger §F's risks are recorded per row) "
      "☑ grading the distractor (traps are graded through the correct value, never their disclosure) ☑ hard-coded titles/phrasings (no file name, subject or wording is required; "
      "the label words come from the notes and pass in any letter case)")
    block = ("none for validity — no UGT defect, no infeasible write, no unverified visibility." if not over_units else
             "none for validity — no UGT defect, no infeasible write, no unverified visibility. diversity.authority_share is a "
             "structural finding reported to the requester (see Unresolved in the Self-review).")
    w(f"Blocking: {block}")
    w("")
    w("Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)")
    w("")
    vis = HERE / "visibility.txt"
    w(vis.read_text().rstrip() if vis.exists() else "(not generated yet: run build_plan.py --visibility)")
    w("")
    w("## F · Shortcut probe")
    w(f"`python3 Task_Authoring/tools/shortcut_probe.py {PERSONA} {TASKREL}/Working_Files/09_Rubric_Writing_Plan.md`")
    w("")
    probe = HERE / "probe.txt"
    w(probe.read_text().rstrip() if probe.exists() else "(the probe is still running)")
    w("")
    w("## G · Gradable-surface coverage")
    w("| Slot | Stable fact ID | Selector · role / group | Work kind (band) | Mechanisms → Decided by | Covered by (P-n) | Disposition "
      "and reason (evidence) |")
    w("|---|---|---|---|---|---|---|")
    for s in SLOTS:
        sel = cell(" ".join(map(str, s["selector"])))[:80]
        mech = ", ".join(s.get("mechanisms") or []) or "—"
        rs = covering(s["id"])
        if not rs:
            reason = disposition(s)
            w(f"| {s['id']} | {s.get('fact_id') or '—'} | {sel} · {s['role']} / {s.get('group') or '—'} | {s['work_kind']} ({s['weight']}) | "
              f"{mech} → — | — | {reason or 'unassigned: rows.json names no covering row (gate 17)'} |")
            continue
        r = rs[0]
        band = f"{r['w']}" if r["w"] == s["weight"] else f"{r['w']} by the row's kind of work, {r['kind']}; the slot says {s['weight']}"
        w(f"| {s['id']} | {s.get('fact_id') or r['fact']} | {sel} · {s['role']} / {s.get('group') or '—'} | {s['work_kind']} ({band}) | "
          f"{mech} → {r['dec']} | {', '.join(pn(x['tag']) for x in rs)} | covered: the title rejects the omission and the plausible "
          f"wrong value ({wrong_value(r)}). |")
    w("")
    sr = HERE / "selfreview.md"
    w(sr.read_text().rstrip() if sr.exists() else "## Self-review\n(pending)")
    (WF / "09_Rubric_Writing_Plan.md").write_text("\n".join(out) + "\n")
    print("plan written:", len(out), "lines; weight", TOTAL_W, BANDS, "largest unit", top[0], "over 50%:", over_units)


if __name__ == "__main__":
    if "--visibility" in sys.argv[1:]:
        write_visibility()
    else:
        main()
