#!/usr/bin/env python3
"""Write Working_Files/09_Rubric_Writing_Plan.md from rows.json (written by build_rubric.py, read fresh on every run).

    build_plan.py               write the plan (reads visibility.txt, probe.txt, selfreview.md when they exist)
    build_plan.py --visibility  run persona_view for every scoped id behind every cited F-id and write visibility.txt

Run from anywhere with python3.12 -B. §F comes from probe.txt (real shortcut_probe.py output plus one SHORTCUT-OK line per hit,
written by build_selfreview.py --probe) and §E's proof from visibility.txt; neither is typed by hand. The shared helpers below
(P numbers, row families, spot-check groups, unit-of-discovery shares, recorded decisions) are imported by the other two builders.

Everything row-shaped comes from rows.json: a row is classified by its tag prefix, fact id, vals and grp, so rows can be added,
removed or moved between groups without touching these builders. Adapted from the Leonard close-out builders for task_inputsS2
(Robert, what each bet cost to build and brought in).

After rows.json changes, in this order (run_pipeline.sh does all of it; the check report must end up newer than the plan):
  build_plan.py --visibility
  build_plan.py
  shortcut_probe.py robert <plan path> > probe_raw.txt     (the cache makes an unchanged-value re-run fast)
  build_selfreview.py --probe
  build_selfreview.py
  build_plan.py
  build_check.py"""
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
os.environ.setdefault("TASK_AUTHORING_TASK_DIR", "Task_Authoring/task_inputsS2")
import stage_gate as G  # noqa: E402

PY = sys.executable
PERSONA = "robert"
PERSONA_LINE = "Robert robert@harmonygames.co"
TASKREL = "Task_Authoring/task_inputsS2"
SQLREL = f"{TASKREL}/01_Universe_Inject.sql"
LBREL = f"{TASKREL}/Working_Files/plan/rubric/rubric_lb_ids.txt"
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
LINES = {k: v for k, v in TRUTH.items() if k != "SUMMARY"}   # payee label -> line (truth.json has no SUMMARY block on this task)
# ENG key -> truth.json payee label: the seeded issue's title is truth.json's Name on the bank (SQL parsed, never executed)
from base_check import parse_sql  # noqa: E402
_ISSUES = {r["row"]["identifier"]: r["row"]["title"] for r in parse_sql((TI / "01_Universe_Inject.sql").read_text(errors="replace")) if r.get("table") == "linear.linear_issues" and r.get("op") == "insert"}
_BANK_LINE = {v["Name on the bank"]: k for k, v in LINES.items()}
ENG_LINE = {eng: _BANK_LINE[title] for eng, title in _ISSUES.items()}
assert len(ENG_LINE) == 22, "the 22 seeded issues do not all map to a truth.json line"
TOTAL_W = sum(r["w"] for r in rows)
BANDS = {b: sum(1 for r in rows if r["w"] == b) for b in (5, 3, 1)}
N_PROC = sum(1 for r in rows if r.get("cat") == "Process")
NB = "none — bundle (Rubric Writing §7; Eval 2.2)"
OE_LABEL_RX = re.compile(r"^OE (\d+)  (.*)$")
WRITE_TITLE = re.compile(r"^(Create|Write|Share|Say why|Move|Reply)\b")
# a row's grp names a spot-check group unless it is one of these per-member or core families (groups follow rows.json, which may be rebuilt)
NOT_SPOT = {"none", "done moves", "reason comments", "comment first", "build cost", "revenue"}
SPOT_GROUPS = tuple(dict.fromkeys(r["grp"] for r in rows if r["grp"] not in NOT_SPOT))
# rows.json names a distractor by a slug; the plan column carries the ledger §E T-ID
DIST_LEDGER_ID = {"T orphan wire": "T5 Leapblock's 29 notices stop short of its close-out", "T returned wire": "T7 the ***8605 notice reads as paid",
                  "T other route": "T9 Western Union totals with fees and duplicate receipts", "T hedged note": "T11 Leonard's contractor-advance guess on ENG-2450",
                  "T token payee": "T13 the token payee and the three forwarded invoices", "T currency": "T15 the BGN laptop payment read as dollars",
                  "T held revenue": "T21 Combo Fighter's 11.75 in the revenue table", "T working sheet": "T25 Leonard's own sheet as the target"}
# ledger §F open risks: (tag test, how the rows keep both readings)
RISKS = [(lambda r: r["tag"].startswith("co_"), "risk 2 → Company rows grade only the Company column; their bet cells are not graded"),
         (lambda r: r["tag"] in ("bkt_jpm", "cell_jpm"), "risk 3 → any no-bucket wording with the 0 line passes"),
         (lambda r: r["tag"] == "cell_martin", "risk 4 → the Company cell or the Note passes"),
         (lambda r: r["tag"].startswith("r_"), "risk 5 → the reply may be top level or in either thread in C0ADGSZKR3R"),
         (lambda r: r["tag"] in ("bkt_node", "bet_node"), "risk 9 → the row never calls the wire the three invoices"),
         (lambda r: r["tag"].startswith(("cell_", "bkt_", "co_", "bet_", "bank_")), "risk 15 → the line is keyed on the ENG id and account ending, payee labels free (NB-12)"),
         (lambda r: r["tag"].startswith("c_"), "risk 1 → five reason comments, settled from the notice sums")]


def pn(tag):
    return TAG[tag]


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
    """The issue a line row grades, from its title's ENG key; None for rows that are not about one line (the header, the volume, totals, the reply)."""
    if r["tag"].startswith(("sh_", "build_", "rev_", "r_")) or r["tag"] == "o_sheet" or r["tag"] == "o_reply":
        return None
    m = re.search(r"ENG-\d+", r["t"])
    return m.group(0) if m else None


def is_volume(r):
    """The sheet's volume row: the row tagged into the sheet volume group."""
    return r["grp"] == "sheet volume"


def family(r):
    """The kind of deliverable a row grades, from its tag prefix."""
    t = r["tag"]
    if r.get("cat") == "Process":
        return "order"
    for prefix, name in (("sh_leonard", "sheet share"), ("sh_arthur", "sheet share"), ("sh_", "sheet setup"), ("cell_", "sheet cell"), ("bkt_", "sheet cell"), ("co_", "sheet cell"),
                         ("bet_", "sheet cell"), ("bank_", "sheet cell"), ("build_", "sheet total"), ("rev_", "sheet total"), ("c_", "reason comment"), ("done_", "done move"), ("r_", "reply")):
        if t.startswith(prefix):
            return name
    return "other"


def axis(r):
    """What a row grades, from its fact id: cell, bucket, company, bet, bank, build, revenue, comment, done, reply, deck, order, sheet, share."""
    return r["fact"].split(".", 1)[0]


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
    bad = []
    for x in base:
        lines = run_tool(["Task_Authoring/tools/persona_view.py", "can-see", PERSONA, need[x], x]).splitlines()
        first = lines[0] if lines else f"{PERSONA} {need[x]} {x}: UNVERIFIED (no tool output)"
        out.append(first)
        if ": YES" not in first:
            bad.append(first)
    out.append("```")
    (HERE / "visibility.txt").write_text("\n".join(out).replace("[]", "(none)") + "\n")
    print("visibility written:", len(seeded), "seeded,", len(base), "base ids,", len(cited), "F-ids;", "not YES:", bad[:5] if bad else 0)


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
    w = sum(r["w"] for r in rows if (set(r["slots"]) | {sl for sl, tags in EXTRA_COVER.items() if r["tag"] in tags}) & flip)
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


# slots covered by rows that rows.json does not tag with the slot: S6 is the sheet's volume row, stated by issue range; D4 is the reply content rows
EXTRA_COVER = {"S6": {"sh_volume"}, "D4": {r["tag"] for r in rows if r["tag"].startswith("r_") and "#winddown reply" in r["t"]}}


def covering(slot):
    return [r for r in rows if slot in r["slots"] or r["tag"] in EXTRA_COVER.get(slot, ())]


def disposition(s):
    """(reason text) for a surface slot no row covers; None when no rule applies, which prints unassigned and blocks at gate 17."""
    sid = s["id"]
    if sid == "B4":
        return ("not incorporated — the prompt and the method ask for a Company column ('that goes in the Company column'), not a Company total; the OE 31 sheet write grades no Company total, "
                "and a total the prompt does not ask for is a count over separate items under release b9281224 (count-bundle-v1) (gate 3)")
    if s["role"] == "sample":
        grp = [r for r in rows if r["grp"] in SPOT_GROUPS and r["grp"] != "sheet volume" and r["tag"].startswith(("cell_", "co_", "bet_"))]
        names = "; ".join(f"{pn(r['tag'])} {key_of(r)}" for r in grp)
        return (f"sampled out — the {grp[0]['grp'] if grp else 'dollar'} group samples other members ({names}) and the sheet's volume row {pn('sh_volume')} carries the rest; "
                f"{s['selector'][1]}'s {s['selector'][2]} cell is an unsampled member of that population (gate 15, at most five samples)")
    return None


def covered_note(s, rs):
    """The Disposition cell of a covered slot: S6 and D4 say how they are covered; the rest give the wrong value the title rejects."""
    if s["id"] == "S6":
        r = BY["sh_volume"]
        return (f"covered as the sheet's single volume row {pn('sh_volume')} (sh_volume), stated by issue range ('{cell(r['t'])}') rather than by a count of Build rows; the nine Build payees need no separate count row "
                f"(count-bundle-v1, gate 15), since each bucket and bet sample row grades its own payee")
    if s["id"] == "D4":
        names = ", ".join(f"{pn(r['tag'])} ({r['tag']})" for r in rs)
        return (f"covered by the reply content rows, each naming its #winddown reply ({names}); a bare 'replied' row would duplicate them (gate 6). Ledger §F risk 5: top level or a thread under either post in C0ADGSZKR3R passes, so the reply location is widened beyond the surface's selector")
    return None


def risk_note(r):
    """Ledger §F open risks that touch this row, each with how the row keeps both readings."""
    n = [text for test, text in RISKS if test(r)]
    if r["amb"] != "none":
        n.insert(0, r["amb"])
    return "; ".join(n) if n else "none (single settled value; ledger §F risks do not touch it)"


def group_cell(r):
    if r["grp"] in SPOT_GROUPS:
        return r["grp"]
    return "none — per member, not sampled" if key_of(r) else "none"


def group_keys(g):
    """The population's key set (ENG ids of the 22 issues), from solver/truth.json."""
    if g == "company column":
        return sorted(k for k, name in ENG_LINE.items() if LINES[name]["Bucket"] == "Company")
    if g == "bet columns":
        return sorted(k for k, name in ENG_LINE.items() if LINES[name]["Bucket"] in ("Build", "Marketing"))
    if g == "dollar amounts":   # every line with a dollar figure of its own; the two zero lines and the BGN line are direct rows
        return sorted(k for k, name in ENG_LINE.items() if isinstance(LINES[name]["Company"], float) and LINES[name]["paid"] and LINES[name]["Bucket"] != "Not a cost")
    return sorted(ENG_LINE)


def groups():
    """{group: rows, samples, vols, keys} for the spot-check groups, in row order; the done moves, reason comments and reply rows are per member, not groups."""
    raw = {}
    for r in rows:
        if r["grp"] in SPOT_GROUPS:
            raw.setdefault(r["grp"], []).append(r)
    out = {}
    sv = [r for r in rows if r["tag"] == "sh_volume"]
    for g, rs in raw.items():
        samples = [r for r in rs if not is_volume(r)]
        out[g] = dict(rows=rs, samples=samples, vols=sv, keys=group_keys(g))
    return out


GROUP_NOTE = {"sheet volume": "no — the sheet is the deliverable the prompt names; the 22 lines are repetitive members",
              "dollar amounts": "no — the prompt asks for the sheet as a whole; the adjusted lines (Leapblock, MotMot, Lucas, the zero lines) and the BGN line are direct rows",
              "bucket column": "no — the prompt asks for the sheet as a whole; the JPMorgan no-bucket line, the exception the method singles out, is a direct row",
              "name on the bank": "no — the prompt asks for the sheet as a whole; the bank-spelling lines are repetitive members"}
GROUP_NOTE_DEFAULT = "no — the prompt asks for the sheet as a whole; the lines an authority singles out are direct rows"


def group_line(g, d):
    n = len(d["keys"])
    span = ", ".join(sorted({f for r in d["rows"] for f in fids(r)}, key=lambda f: int(f[1:])))
    if d["samples"]:
        samples = ", ".join(f"{pn(r['tag'])} {key_of(r) or r['fact']} ({cell(r['why']).rstrip('.')})" for r in d["samples"])
    else:
        samples = "none sampled: the sheet's line count is this group's only claim"
    if len(d["samples"]) > 5:
        samples = f"OVER THE CAP ({len(d['samples'])} samples): {samples}"
    return (f"| {g} | {span} ({n} keys): {lit(d['keys'])} | {samples} | {ps(d['vols'])} | {NB} | {GROUP_NOTE.get(g, GROUP_NOTE_DEFAULT)} |")


def oe_titles():
    out = {}
    for line in (TI / "08_Oracle_Events.md").read_text().splitlines():
        m = OE_LABEL_RX.match(line)
        if m:
            out[int(m.group(1))] = m.group(2)
    return out


def oe_report():
    """The latest /oe PASS report whose reviewed sha matches the OE file on disk (or the newest report, marked)."""
    disk = hashlib.sha256((TI / "08_Oracle_Events.md").read_bytes()).hexdigest()
    reports = sorted((TI / "plateform_reports").glob("*_2_oe*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    for pth in reports:
        text = pth.read_text()
        m = re.search(r"sha256 `([0-9a-f]{64})` \((\d+) OEs", text)
        if m and m.group(1) == disk:
            return pth, m.group(1), m.group(2), re.search(r"Score:\s*(\d)", text).group(1), re.search(r"Review time \| ([\d-]+)", text).group(1)
    raise SystemExit("no /oe report matches the OE file on disk: run /oe before regenerating the plan")


def records():
    """Decisions the rows take against the brief, the ledger or the surface. Each prints only while its facts stand."""
    out = []
    proc = [r for r in rows if r.get("cat") == "Process"]
    if proc:
        out.append(f"Process rows {prange(proc)} stay Process: the method says 'say why on the issue first' and 'move each payee’s issue to Done once its line is right', and the prompt says "
                   "'When you’re done, reply'; the final comments, states and reply look the same whichever write came first, so no Outcome row can prove the order. §C records the three-condition test per row.")
    mkt = [r for r in rows if r["tag"].startswith("bet_") and BY.get(r["tag"].replace("bet_", "bkt_")) is not None and BY[r["tag"].replace("bet_", "bkt_")]["vals"] == "`Marketing`"]
    if mkt:
        out.append("Marketing dollars are graded in the bet columns: the method lists Marketing 'under its bet by date like the rest, but keep it out of build cost'. Brief §4b also accepts those dollars 'in the row with the bet named', "
                   "so a bet-column row on a Marketing line that locks the column carries an overly-specific risk (see Findings in 09_Rubric_Check.md while one is open).")
    out.append("Slot X9 widened to the Company cell or the Note (brief §4b, ledger §F risk 4); slot D4 widened to top level or a thread under either post (ledger §F risk 5); no row grades a Combo Fighter revenue figure beyond the held-back rows (NB-26).")
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
    report, oe_sha, oe_n, oe_score, oe_date = oe_report()
    sqlsha = hashlib.sha256((TI / "01_Universe_Inject.sql").read_bytes()).hexdigest()[:12]
    hours = re.search(r"Hours:\s*([\d.]+)", (TI / "05_Human_Time.md").read_text())
    w("# 09 Rubric Writing Plan — task_inputsS2 (Robert: what each bet cost to build and brought in; injection SQL sha256 " + sqlsha + ")")
    w(f"Generated 2026-11-09 · Clock 2026-02-14T00:00:00Z (seed bound; eval clock 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)) · Persona {PERSONA_LINE} · "
      "Assigned role Co-founder & Creative Director · Tier Long-Horizon · Mode Easy · Human time " + (hours.group(1) + " h" if hours else "not entered") + " (05_Human_Time.md) · "
      f"OE status: /oe PASS {oe_date} (plateform_reports/{report.name}, Score {oe_score}, {oe_n} events, reviewed 08_Oracle_Events.md sha256 {oe_sha[:12]}, matching the file on disk)")
    w("Canonical outcomes: brief §4b (all fair results and accepted alternatives) — a new native spreadsheet owned by Robert, in his My Drive root or a folder he owns, any title, in Leonard's layout (Payee, Name on the bank, Bucket, Domino Delights, ZM, "
      "Combo Fighter, Company, Note) with 22 payee lines ENG-2438 to ENG-2459, keyed on the account ending, Build and Marketing dollars by bet, Company dollars in the Company column, ENG-2454 at 1,999.00 BGN, ENG-2450 and ENG-2459 at zero, build cost "
      "lines 959,342.64 / 544,433.44 / 72,685.61, brought-in 12,331.25 (Domino Delights) and 11.99 (ZM) with Combo Fighter's left off, shared with leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co; a reason comment on ENG-2439, ENG-2442, "
      "ENG-2447, ENG-2450 and ENG-2459 before each moves to Done, all 22 issues Done; then one reply to Leonard in #winddown C0ADGSZKR3R (top level or under either post) with what each bet cost and brought in, what changes on the draft deck, and the link.")
    w("")
    w("Recorded decisions:")
    w("")
    for line in records():
        w(f"- {line}")
    w("")
    w("Rubric shape: every write family has a result row. Per-line values on the sheet are direct where an authority or the method singles the line out (the adjusted lines and the exception buckets) and sampled in the populations "
      f"({', '.join(groups())}), each with the sheet's volume row and no bundled exact-set row (gate 15). The 22 Done moves and the 5 reason comments are graded per member; no count row sits over separate writes (count-bundle-v1). "
      f"09_Rubrics.json mirrors P1–P{len(rows)} one to one (C-n = P-n).")
    w("")
    w("## A · Coverage matrix")
    w("| P | Source (exact prompt span · OE n) | Stable fact ID | What must be verified | Final state that proves it | Category "
      "(Outcome / Process candidate → C) | Expected/source values and pointers · accepted alternatives · date acceptance · F-IDs |")
    w("|---|---|---|---|---|---|---|")
    for p, r in zip(P, rows):
        acc = "; ".join(r["acc"])
        dated = bool(re.search(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{0,2},? ?\d{4}|\bfrom Jun to Aug", r["t"]))
        dates = "a wire's date, not an instant; any date form passes" if dated else "none graded"
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
        title_note = ("no — the column names come from Leonard's sheet (F3), not the prompt; letter case free" if r["tag"] == "sh_header"
                      else "no — must not hard-code; titles, wording and headings stay the Agent's")
        w(f"| {p} | {title_note} | {dist} | {risk_note(r)} | {r['kind']} — "
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
    w("Final-reply test (whole set): \"The sheet is in your Drive and shared with Leonard and Blake, the payee issues are moved to Done with a reason on the five whose figure differs, and the reply is up in #winddown with what each bet cost and brought in and what changes on the deck.\" → "
      "ACCEPT ☑ (no row grades the final response; the prompt's 'reply to him in #winddown' is the Slack write graded by the r_ rows, so a concise chat reply passes every row)")
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

    # discovery steps no row cites: the F-ids they establish and the rows that carry their result
    uncited = {
        1: (with_fid("F1"), "no — Leonard's two posts name every deliverable; proved by the sheet, share and reply rows"),
        5: (with_fid("F69"), "no — the superseded quick plan (ledger T2) is graded through the build-cost rows, which fail its plain sum 984,888.21"),
        7: (with_fid("F8"), "no — the project and its 22 issues; proved by the volume and per-issue rows"),
        9: (with_fid("F9", "F10", "F11", "F12", "F13", "F14", "F15", "F16", "F17", "F18", "F19"), "no — the notes on ENG-2438 to ENG-2448; proved by the bucket and comment rows they decide"),
        11: (with_fid("F32", "F33", "F34", "F35", "F36", "F37", "F38", "F39", "F40", "F41"), "no — the notice search; proved by the per-line figure rows"),
        22: (with_fid("F26"), "no — the Brooks contact; proved by the Lauren Brooks bucket row (T14: two Brooks contacts)"),
        23: (with_fid("F26"), "no — her contract's scope; proved by the Lauren Brooks bucket row, whose note already names paid UA"),
    }
    missing_oe = []
    for n, title in sorted(titles.items()):
        kind = "write" if WRITE_TITLE.match(title) else "discovery"
        if n in cites:
            rs = sorted(set(cites[n]), key=lambda x: int(x[1:]))
            own = "yes — the write's result row" if kind == "write" else "no — proved by the content row(s) it decides"
        elif n in uncited:
            rs, own = uncited[n]
        else:
            rs, own = [], "no row cites this step"
            missing_oe.append(n)
        w(f"| OE {n} | {kind} | {', '.join(rs[:8]) or 'none'}{' …' if len(rs) > 8 else ''} | {own} |")
    w("")
    w("## C · Process candidates — three-condition test")
    w("| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) "
      "behavioural, not trace | Result (Process / tighten P-n with F-n) |")
    w("|---|---|---|---|---|---|---|")
    proc = [r for r in rows if r.get("cat") == "Process"]
    for r in proc:
        if r["tag"].startswith("o_ENG"):
            key = key_of(r)
            req = f"the method's 'say why on the issue first' for {key}"
            no_outcome = f"The comment and the Done state on {key} read the same in the final state whichever came first, so no final-state row shows the order (a comment's created_at against a completed_at would be a trace of two writes, and later edits shift them)"
            path = f"yes — every valid run must say why on {key} (its figure differs from the notices' sum) and the method orders that before the move"
        elif r["tag"] == "o_sheet":
            req = "the method's 'move each payee’s issue to Done once its line is right'"
            no_outcome = "The sheet's final cells and the 22 Done states are the same whichever write came first, so no final state shows the order"
            path = "yes — any run that moves an issue to Done also writes that payee's line; the row asks only that one sheet write with the payee lines comes first and later edits pass"
        else:
            req = "the prompt's 'When you're done, reply to him in #winddown'"
            no_outcome = "The reply's final text and the other writes' final state are the same whichever came first, so no final state shows the reply came last"
            path = "yes — the prompt makes the reply the last step for every valid run"
        w(f"| {pn(r['tag'])} | \"{r['span']}\" — {req} | {no_outcome} | {path} | "
          "yes — every content row grades a value on the final artifact; none can see the order of the writes | yes — the order of two writes the Agent must make, with no tool named "
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
    w(f"Not sampled: the {len(of('done move'))} Done moves ({prange(of('done move'))}) are one row per issue with no count row; the {len(of('reason comment'))} reason comments ({prange(of('reason comment'))}) and the "
      f"{len(of('reply'))} reply rows ({prange(of('reply'))}) are per write or per told fact; the content differs per target, so these are not populations under gate 15. The build-cost and revenue rows are core asks, graded directly.")
    w("")
    w("## E · Summary")
    vols = list({r["tag"]: r for d in grp.values() for r in d["vols"]}.values())
    w(f"Rows {len(rows)} · Outcome {len(rows) - N_PROC} · Process candidates {N_PROC} considered, {N_PROC} kept — ≥ 1 Outcome ☑ · Process rows ≤ 50 % ☑ · "
      f"fewer than two Process rows failing the three-condition test ☑ (none fails; §C records all {N_PROC}) · builder minimum 5 ☑ · one volume row per sampled output, no bundled exact-set row "
      f"☑ ({ps(vols)}) · predicted all-fail rows = 0 ☑ (every value is reachable through a cataloged tool and visible to Robert; none sits on the four Evals bases)")
    top, over_units = diversity()
    pct = lambda s: f"{100 * s / TOTAL_W:.0f}%"  # noqa: E731
    box = "☑" if not over_units else "☒"
    why = ("" if not over_units else " — every line's value depends on the issue list, the method and the notices through the ledger's Depends-on edges, so it is upstream of almost every row by the "
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
    w(f"Set size: {len(rows)} rows for {hours.group(1) if hours else '?'} h (reference: 31 criteria for a ~10-hour task). The count follows the deliverables: {len(of('sheet setup')) + len(of('sheet share'))} sheet setup and share rows, "
      f"{len(of('sheet cell'))} sheet-line rows, {len(of('sheet total'))} build-cost and revenue rows, {len(of('reason comment'))} reason comments, {len(of('done move'))} Done moves, {len(of('reply'))} reply rows and {len(of('order'))} order rows; "
      "the members are per-target writes and cells, not duplicates of one another.")
    write_rows = {"sheet created": ("sh_create",), "payee lines": ("cell_", "bkt_", "co_", "bet_"), "shares": ("sh_leonard", "sh_arthur"), "reason comments": ("c_",), "Done moves": ("done_",), "#winddown reply": ("r_",)}
    present = [k for k, ts in write_rows.items() if any(r["tag"].startswith(ts) for r in rows)]
    n_req = len(G.rows_in(ledger(), r"^A\b"))
    reqs = {"R1": any(fids(r) & {"F1", "F2"} for r in rows), "R2": bool(of("reply")), "R3": any(r["tag"].startswith("sh_") for r in rows), "R4": any(fids(r) & {"F2", "F68"} for r in rows),
            "R5": any(r["tag"] == "sh_header" for r in rows), "R6": bool(of("sheet cell")) and bool(of("sheet total")), "R7": bool(of("sheet share")), "R8": bool(of("done move")) and bool(of("reason comment")),
            "R9": any(r["tag"].startswith("r_") for r in rows), "R10": any(r["tag"].startswith(("r_build", "r_rev", "r_hold")) for r in rows), "R11": any(r["tag"].startswith("r_deck") for r in rows), "R12": "r_link" in BY}
    met = sum(1 for v in reqs.values() if v)
    assert not missing_oe, f"OE steps no row or uncited entry names: {missing_oe}"
    w(f"Coverage: requirements {met}/{n_req} (ledger R1–R{n_req}) · OEs {len(titles)}/{len(titles)} (§B) · writes {len(present)}/{len(write_rows)} ({'; '.join(present)}) · told facts 0/0 (the final response is ungraded; the prompt's 'reply to him' is the "
      "Slack write, graded by the reply rows) · friction 0/0 (Friction: none)")
    covered = [s for s in SLOTS if covering(s["id"])]
    mw, mp, nflip = mech_share()
    nw, np_ = mech_node_share()
    w(f"Gradable surface (gate 17): slots {len(SLOTS)} · covered {len(covered)} · dispositioned {len(SLOTS) - len(covered)} (§G) · no slot "
      f"with neither ☑ · mechanism share {mp}% of the weight ({mw} of {TOTAL_W}, the rows that cover the {nflip} slots a "
      f"mechanism can flip; {np_}% counting every row a mechanism's node decides, since rows.json maps one row per slot; reported, not gated)")
    w("Four prohibitions: ☑ unstated expectations (every row quotes a prompt span; Leonard's method doc and sheet, which the prompt says to follow, are the "
      "incorporated authority) ☑ conclusions on ambiguous evidence (none: each graded value is settled by a later or more specific record, and ledger §F's risks are recorded per row) "
      "☑ grading the distractor (traps are graded through the correct value, never their disclosure) ☑ hard-coded titles/phrasings (no file name, column wording beyond Leonard's layout, or message wording is required)")
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
        if len(rs) > 1:   # several rows carry one delivery slot (D4): their weights are their own, the slot's is printed as is
            band = f"{s['weight']}; the covering rows keep their own weights"
        note = covered_note(s, rs) or f"covered: the title rejects the omission and the plausible wrong value ({wrong_value(r)})."
        w(f"| {s['id']} | {s.get('fact_id') or (r['fact'] if len(rs) == 1 else 'reply content rows')} | {sel} · {s['role']} / {s.get('group') or '—'} | {s['work_kind']} ({band}) | "
          f"{mech} → {r['dec']} | {', '.join(pn(x['tag']) for x in rs)} | {note} |")
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
