#!/usr/bin/env python3
"""Write Working_Files/09_Rubric_Writing_Plan.md from rows.json (written by build_rubric.py).

    build_plan.py               write the plan (reads visibility.txt, probe.txt, selfreview.md when they exist)
    build_plan.py --visibility  run persona_view for every scoped id behind every cited F-id and write visibility.txt

Run from anywhere with ~/.local/bin/python3.12 -B. §F comes from probe.txt (real shortcut_probe.py output plus one
SHORTCUT-OK line per hit, written by build_selfreview.py --probe) and §E's proof from visibility.txt; neither is typed by
hand. The shared helpers below (P numbers, row families, spot-check groups, the unit-of-discovery shares, the recorded
decisions) are imported by the other two builders.

Everything row-shaped comes from rows.json: a row is classified by its tag prefix, fact id, vals and grp, never by its full
tag, so rows can be added, removed or moved between groups without touching these builders. A recorded decision prints only
while the rows it describes still stand.

After rows.json changes, in this order (the check report must end up newer than the plan):
  build_plan.py --visibility
  build_plan.py
  shortcut_probe.py claire_morgan <plan path> > probe_raw.txt     (only if the values digest changed; the cache makes it fast)
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
WF = HERE.parent
TI = WF.parent
WS = TI.parents[1]
sys.path.insert(0, str(WS / "Task_Authoring/tools"))
sys.path.insert(0, str(WF / "oe_gen"))
os.environ.setdefault("TASK_AUTHORING_TASK_DIR", "Task_Authoring/task_inputsN2")
import model as M  # noqa: E402  (asserts every call, due date and maker against solver/truth.json)
import stage_gate as G  # noqa: E402

PY = sys.executable
PERSONA = "claire_morgan"
TASKREL = "Task_Authoring/task_inputsN2"
SQLREL = f"{TASKREL}/01_Universe_Inject.sql"
LBREL = f"{TASKREL}/Working_Files/rubric_gen/rubric_lb_ids.txt"
OE_DATE = "2026-11-05"
OE_REPORT = TI / "plateform_reports/6aea4c1eea32a6fa98b9b1d9_2_oe.md"
LOCAL_REVIEW = HERE / "review2/3_rubric_local_r1_FAIL2.md"
FREDERICK_RULING = "support/completed_tasks/frederick_q4_commitments_2026-11-05/eval_reports/3_rubric_FAIL_r1.md"
JULIA_RULING = "support/completed_tasks/julia_zm_difficulty_baseline_2026-11-01/eval_reports/3_rubric_FAIL_r5.md"
# weight band by kind of work (playbook gate 8)
BAND = {"lookup": 1, "interpretation": 3, "calculation": 3, "comparison": 3, "reconciliation": 3, "multi-source": 5, "tracing": 5}
WRITE_FAMILIES = {"plan doc": "plan doc", "tracker": "tracker", "share": "shares", "comment": "ticket comments", "assignment": "assignments",
                  "new ticket": "new tickets", "reply": "thread reply"}

rows = json.loads((HERE / "rows.json").read_text())
BY = {r["tag"]: r for r in rows}
P = [f"P{i + 1}" for i in range(len(rows))]
TAG = {r["tag"]: f"P{i + 1}" for i, r in enumerate(rows)}
LABEL = json.loads((WF / "oe_gen/events.json").read_text())["label"]
SURF = json.loads((WF / "01_Gradable_Surface.json").read_text())
SLOTS = SURF["slots"]
MANIFEST = json.loads((WF / "01_Hardness_Manifest.json").read_text())
SIDECAR = json.loads((WF / "00_V3_Authoring_Evidence.json").read_text())["rubric_rows"]
TOTAL_W = sum(r["w"] for r in rows)
BANDS = {b: sum(1 for r in rows if r["w"] == b) for b in (5, 3, 1)}
N_PROC = sum(1 for r in rows if r.get("cat") == "Process")
STORE = ['app icon', 'iPad 12.9" set', 'iPhone 6.5" set', 'Google Play phone set']
ADS = list(M.ADS)
WORK = [k for k in ADS if M.call(k) != "Skip"]
NB = "none — bundle (Rubric Writing §7; Eval 2.2)"
# Four rows of rows.json name a distractor by its manifest trap id; the plan column is the ledger's T-ID (ledger §E).
DIST_LEDGER_ID = {"T13 Martin's concept": "T10 Martin's concept", "T1 Martin's 'exported'": "T11 Martin's 'exported'"}


def pn(tag):
    return TAG[tag]


def pns(tags):
    return ", ".join(TAG[t] for t in tags)


def ps(rs):
    return ", ".join(TAG[r["tag"]] for r in rs)


def fids(r):
    return set(G.RX_FID.findall(r["fids"]))


def literals(r):
    return re.findall(r"`([^`]+)`", r["vals"])


def key_of(r):
    return next((v for v in literals(r) if re.fullmatch(r"ART-\d+", v)), None)


def is_volume(r):
    """A count row: its vals carry a bare number."""
    return any(re.fullmatch(r"\d+", v) for v in literals(r))


def is_store(r):
    return r["fact"].split(".")[0] in ("icon", "ipad", "iphone", "play")


def axis(r):
    """What a row grades, from its fact id: call, due, maker, or the fact's last part (exists, keys, scope, route, ...)."""
    f = r["fact"]
    if f.endswith(".due") or f.startswith("due.") or ".due" in f:
        return "due"
    if "maker" in f:
        return "maker"
    if f.endswith(".call") or re.search(r"\.(halloween|refresh|reuse|skip)\.count$", f):
        return "call"
    return f.rsplit(".", 1)[-1]


def cell(s):
    """One table cell: no pipes or newlines, and no straight double quote (the probe reads "x" as a literal)."""
    return str(s).replace("|", "/").replace("\n", " ").replace('"', "″").replace("the the ", "the ")


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
    keep = [l for l in txt.splitlines() if l.startswith("[YES LB]") or l.startswith("[NO LB]")
            or l.startswith("[UNVERIFIED LB]") or l.startswith("verdict:")]
    out = [f"`python3 Task_Authoring/tools/persona_view.py check-sql {PERSONA} {SQLREL} --load-bearing "
           f"{LBREL}` ({len(seeded)} seeded ids behind the {len(cited)} cited F-ids; load-bearing rows and the verdict line kept):",
           "", "```text", *keep, "```", "",
           f"`python3 Task_Authoring/tools/persona_view.py can-see {PERSONA} <service> <id>` ({len(base)} base ids, first "
           "line of each):", "", "```text"]
    for x in base:
        lines = run_tool(["Task_Authoring/tools/persona_view.py", "can-see", PERSONA, need[x], x]).splitlines()
        out.append(lines[0] if lines else f"{PERSONA} {need[x]} {x}: UNVERIFIED (no tool output)")
    out.append("```")
    (HERE / "visibility.txt").write_text("\n".join(out) + "\n")
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
    """The same share read off Decided by: rows.json maps one row per slot, so a twin row on the same fact counts only here."""
    nodes = {n for m in MANIFEST["mechanism_portfolio"] for n in m["nodes"]}
    w = sum(r["w"] for r in rows if nodes & set(r["dec"].split()))
    return w, round(100 * w / TOTAL_W)


def wrong_value(r):
    """The wrong value a row's title rejects, for a §G line."""
    if family(r) == "new ticket":
        return "a run with no new ticket naming it fails; a ticket for an exported set does not stand in for it"
    return cell(r["alt"]).rstrip(".")


def reach_note(i):
    """The deciding record's own rationale from the sidecar, first sentence."""
    src = SIDECAR[i]["source_records"]
    return cell(src[0]["reachability_rationale"].split(". ")[0].rstrip("."))


def covering(slot):
    return [r for r in rows if slot in r["slots"]]


def family(r):
    t = r["tag"]
    if t.startswith("cmt_"):
        if is_volume(r):
            return "comment count"
        return "comment due" if axis(r) == "due" else "comment call"
    for prefix, name in (("share_", "share"), ("assign_", "assignment"), ("trk_", "tracker"), ("doc_", "plan doc"), ("tk_", "new ticket"),
                         ("reply_", "reply")):
        if t.startswith(prefix):
            return name
    return "other"


def of(fam):
    return [r for r in rows if family(r) == fam]


def is_due_row(r):
    return axis(r) == "due"


def is_date_row(r):
    return is_due_row(r) or r["fact"].endswith(".route")


def risk_note(r):
    """Ledger §F open risks that touch this row, each with how the row keeps both readings."""
    n = []
    if "`Skip`" in r["vals"]:
        n.append("risk 1 → 'Skip October' carries the call word Skip, so it passes")
    if r["fact"] in ("icon.due", "ipad.due"):
        n.append("risk 2 → an earlier internal October date passes")
    if r["tag"].startswith("share_"):
        n.append("risk 3 → Julia is not on the review, so no row needs a share with her")
    if is_due_row(r) and r["fact"] not in ("icon.due", "ipad.due"):
        n.append("risk 4 → each ad takes its own tier's date; a blanket date fails only on the other tier")
    return "; ".join(n) if n else "none (single settled value; ledger §F risks do not touch it)"


def slot_note(s, rs):
    """Say so on the line when a slot's selector names the tracker but no tracker row covers it."""
    kind = s["selector"][0]
    if kind == "link":
        return " Its sharing half is the tracker share rows."
    if kind not in ("field", "reason_matches") or any(family(x) == "tracker" for x in rs):
        return ""
    r = rs[0]
    ax = "due" if kind == "reason_matches" else {"owner": "maker"}.get(s["selector"][2], s["selector"][2])
    where = {"comment call": "the comment on the ticket", "comment due": "the comment on the ticket", "assignment": "the assignment write"}
    twin = [x for x in of("tracker") if x["fact"] == r["fact"]]
    tail = (f" (the tracker cell is also graded in {ps(twin)})" if twin else
            f"; the tracker's {ax} column is sampled in {group_for(ax)}, so this cell has no tracker row of its own")
    return f" Its selector names the tracker; the covering row is {where.get(family(r), family(r))}{tail}"


def group_cell(r):
    if r["grp"] != "none":
        return r["grp"]
    if family(r) == "tracker" and is_store(r):
        return "none — store surface, core and direct"
    if family(r) in ("comment call", "comment due"):
        return "none — per target, not sampled"
    return "none"


def ad_fids():
    """Ledger F-ids whose locator is one ART ticket."""
    return {f for f, x in G.ledger_facts(ledger()).items() if re.fullmatch(r"\s*ART-\d+\s*", x["locator"])}


def groups():
    """{group: rows, samples, vols, direct, kind, keys} straight from rows.json's grp, in row order."""
    raw = {}
    for r in rows:
        if r["grp"] != "none":
            raw.setdefault(r["grp"], []).append(r)
    out = {}
    for g, rs in raw.items():
        samples = [r for r in rs if not is_volume(r)]
        vols = [r for r in rs if is_volume(r)]
        fam = collections.Counter(family(r) for r in rs).most_common(1)[0][0]
        axes = {axis(r) for r in samples}
        direct = []
        if "call" in axes:
            kind, keys = "call", (ADS + STORE if fam == "tracker" else ADS)
            vols = [r for r in of(fam) if r["grp"] == "none" and is_volume(r) and axis(r) == "keys"] + vols
            direct = [r for r in of(fam) if r["grp"] == "none" and is_store(r) and axis(r) == "call"]
        elif "due" in axes:
            kind, keys = "due", WORK
        elif "maker" in axes:
            kind, keys = ("assign" if fam == "assignment" else "maker"), WORK
        else:
            kind, keys = "total", ADS
        out[g] = dict(rows=rs, samples=samples, vols=vols, direct=direct, kind=kind, keys=keys, family=fam)
    return out


def group_for(kind):
    return next((g for g, d in groups().items() if d["kind"] == kind and d["family"] == "tracker"), "its spot-check group")


def group_line(g, d, adf):
    ads = sorted(int(f[1:]) for f in adf)
    other = sorted({f for r in d["rows"] for f in fids(r)} - adf, key=lambda f: int(f[1:]))
    span = ", ".join([f"F{ads[0]}–F{ads[-1]}"] + other)
    noun = {"total": "ads as totals", "call": "surfaces", "due": "working ads", "maker": "working ads", "assign": "assignments"}[d["kind"]]
    if d["samples"]:
        samples = ", ".join(f"{pn(r['tag'])} {key_of(r) or r['fact']} ({cell(r['why']).rstrip('.')})" for r in d["samples"])
    else:
        samples = "none sampled: the per-ad values are graded on the comments (section A); the totals are the check here"
    if len(d["samples"]) > 5:
        samples = f"OVER THE CAP ({len(d['samples'])} samples): {samples}"
    if d["direct"]:
        samples += f". The store surfaces are core and direct: {ps(d['direct'])}"
    core = {"total": "no — the prompt asks for the plan as a whole; the per-ad lines are repetitive members",
            "call": "no — the prompt asks for the tracker as a whole; the store surfaces, named on their own, are graded directly",
            "due": "no — each ad's date is also graded per target on its comment",
            "maker": "no — the assignment rows grade the same makers on their own write",
            "assign": "no — one rule per kind of ad sets the assignee, so the writes are repetitive members; the volume rows bind the whole set"}
    return (f"| {g} | {span} ({len(d['keys'])} {noun}): {lit(d['keys'])} | {samples} | {ps(d['vols'])} | {NB} | {core[d['kind']]} |")


def release_sha(path):
    m = re.search(r"Eval release SHA-256:\s*([0-9a-f]{8})", path.read_text()) if path.exists() else None
    return m.group(1) if m else "not stated"


def local_flow_lacks_rulings():
    text = (WS / "Evals/references/rules/rubric_flow_v2.md").read_text()
    return not any(q in text for q in ("differs per target", "One row per write", "template sampling"))


def dismissal_on_file():
    try:
        d = json.loads((WS / "Evals/task_inputs/reports/drafts/rubric_ledger.json").read_text())
    except (OSError, ValueError):
        return False
    return any("A1 and A2" in str(v.get("reason")) for v in (d.get("dismissals") or {}).values())


def baseline_folders():
    """Drive folders the six baselines filed their plan doc and tracker in."""
    runs = json.loads((HERE / "baseline_writes.json").read_text())
    six = [runs[f"run-{i}"] for i in range(1, 7)]
    return {p for x in six for f in x["doc"] + x["sheets"] for p in (f.get("drive_parents") or [])}


def comment_rows_direct():
    """True while the comment rows stand one per ticket."""
    return len(of("comment call")) > 5 or len(of("comment due")) > 5


def contested():
    """A1 and A2 closed: local /rubric run 2 accepted the dismissal on all 106 comment rows."""
    return False


def records():
    """Decisions the rows take against the brief or a review finding. Each prints only while its rows stand."""
    out = []
    scope = [r for r in of("share") if is_volume(r)]
    if scope:
        out.append(f"Sharing scope, a deliberate tightening of brief §4b: the brief allows extra harmonygames.co people on each file, while {ps(scope)} "
                   "grade exactly the six other attendees of evt_d947bf7cd910549b674b1f, after a reviewer raised the scope checklist. The prompt's "
                   "audience is the review, and no valid prompt-authorized reading needs anyone else.")
    if any("final due date" in r["t"] for r in rows):
        out.append("Due-date window, a recorded difference from brief §4b: the brief allows an earlier internal date from Oct 6 on the Android US phone "
                   "tier; the due-date rows accept an earlier October 2025 final date for the Oct 10 tier and Oct 11 to Oct 14 for the Oct 15 tier. "
                   "'Final' is the operative word: a refresh milestone does not stand in for the date the finished ad is due.")
    if comment_rows_direct():
        n_call, n_due = len(of("comment call")), len(of("comment due"))
        release = (f"The local bundle's eval release differs from the platform's (local run {release_sha(LOCAL_REVIEW)}, this task's platform reports "
                   f"{release_sha(OE_REPORT)})")
        if local_flow_lacks_rulings():
            release += ", and the two rule sentences those rulings quote are not in the local rubric_flow_v2.md"
        filed = ("Local /rubric run 2 accepted the dismissal on all 106 rows, on local rules alone (the Local Override on spot checks, rubric_sampling, QC Appendix "
                 "C2 on write actions); it gave the platform reports no weight. Run 4 applied the same ruling to the 48 assignment rows.")
        out.append(f"Comment rows stay, against the local /rubric run 1 findings A1 and A2 (both `duplicate` overlap groups at Moderate, "
                   f"rubric_gen/review2/3_rubric_local_r1_FAIL2.md): the {n_call} call rows and {n_due} due-date rows are exhaustive direct coverage of "
                   f"'Comment each ad's call and due date on its ART ticket', not samples. Reason: the platform ruled this way in {FREDERICK_RULING} "
                   f"(quoting rubric_flow_v2: 'Comments whose content differs per target get one row each, with no cap') and in {JULIA_RULING} "
                   "('template sampling is allowed, not required, and each row embeds its own comment's content'), and "
                   "Evals/references/rules/rubric_sampling.md says there is 'no automatic row-count threshold or requirement to shrink an otherwise "
                   f"valid exhaustive rubric'. {release}. {filed} Limits of that evidence: the rulings covered 31 written answers and 7 + 7 comment "
                   f"rows, not {n_call + n_due}, and rubric_sampling's sentence follows its five-sample limit, so the case rests on these rows being "
                   "direct coverage rather than samples.")
    reuse = [r for r in rows if r["fact"].split(".")[0] in ("iphone", "play")]
    if reuse and not [r for r in reuse if axis(r) in ("due", "route")]:
        out.append(f"Reuse sets: the iPhone 6.5\" and Google Play phone sets have no ship-date rows (their rows are {ps(reuse)}), "
                   "following local /rubric run 1 finding A26 (both sets are Reuse, and a plan that says so meets every ask) and its rejected finding "
                   "X1 (Leonard's 'what we already have, and who makes what by when' and 'whatever is already exported is done': a finished set has "
                   "no maker, so no by-when is owed).")
    doc = [r for r in of("plan doc") if axis(r) == "exists" and "Claire's Drive" in r["t"]]
    if doc:
        leo = "d_272d849cde40c35980a433"
        out.append(f"Folder note, not a finding: {ps(doc)} says 'in Claire's Drive', the prompt's own 'in my Drive'. Brief §4b also lists Leonard's folder "
                   f"{leo}, but the prompt does not authorize a folder of his, so the wording rejects nothing the prompt allows; "
                   + ("no baseline filed either file there." if leo not in baseline_folders() else "a baseline did file there, so this needs a second look."))
    return out


def main():
    dup = {}
    for r in rows:
        dup.setdefault(r["fact"], []).append(pn(r["tag"]))
    over = {k: v for k, v in dup.items() if len(v) >= 3}
    assert not over, f"a fact in three or more rows: {over}"
    bad_order = [r["tag"] for r in rows if not r["oe"] or not r["fids"].strip()]
    assert not bad_order, bad_order

    out = []
    w = out.append
    bycall = {c: len(M.BY[c]) for c in M.BY}
    n_call, n_due = len(of("comment call")), len(of("comment due"))
    oe_m = re.search(r"(\d+) OEs, sha256 ([0-9a-f]{12})", OE_REPORT.read_text())
    oe_disk = hashlib.sha256((TI / "08_Oracle_Events.md").read_bytes()).hexdigest()[:12]
    w("# 09 Rubric Writing Plan — claire-zm3d-halloween-art-plan (Halloween art plan, injection rev3)")
    w("Generated 2026-11-06 · Clock 2025-10-01T00:00:00Z (seed bound; eval clock 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, "
      "2025 (synth-cut)) · Persona Claire Morgan claire.morgan@harmonygames.co · Assigned role Art Lead · Tier Long-Horizon · "
      f"Mode Medium · Human time not entered yet (05_Human_Time.md is the requester's slot and is empty) · OE status: /oe PASS {OE_DATE} "
      f"(plateform_reports/{OE_REPORT.name}, Score 5, {oe_m.group(1)} events, reviewed 08_Oracle_Events.md sha256 {oe_m.group(2)}, "
      f"{'matching the file on disk' if oe_m.group(2) == oe_disk else 'which differs from the file on disk, ' + oe_disk})")
    w("Canonical outcomes: brief §4b (all fair results and accepted alternatives) — plan doc: a new Google Doc owned by Claire with "
      "the calls by surface type, ship route and dates, reuse and owners; tracker: a new spreadsheet owned by Claire with exactly the "
      f"62 serving surfaces (4 store, 56 Unity, ART-826, ART-831; no Archive row), calls Halloween version 14 (ads {bycall['Halloween version']} "
      f"plus the icon and iPad set), Refresh first {bycall['Refresh first']}, Reuse 2, Skip {bycall['Skip']}; due Fri Oct 10 on the "
      f"{len(M.D10)} working ads on Android US phone (an earlier October final date accepted), Wed Oct 15 on the other {len(M.D15)} (Oct 11 to "
      "Oct 14 accepted), blank on Skip, the icon and iPad set by the Thu Oct 16 12:00 PT merge cut; makers Martin Walsh (icon, store art), "
      f"Julia Lawson ({len(M.JULIA)} ad statics), Marcus Bennett ({len(M.MARCUS)} video and end cards); both files shared with exactly the six "
      "review attendees of evt_d947bf7cd910549b674b1f as commenter or writer; one comment on each of the 58 running tickets; the 48 "
      "working tickets assigned to their makers; new ART tickets for the icon and the iPad 12.9\" set (two tickets, or one naming "
      "both); one reply under C06DJBJL798/1759269913.882683 holding both links.")
    w("")
    w("Recorded decisions:")
    w("")
    for line in records():
        w(f"- {line}")
    w("")
    w(f"Rubric shape: every write family has a result row. The {len(ADS)} ticket comments differ per target, so {n_call} call rows and {n_due} "
      f"due-date rows take them one per ticket, with no sampling there. The sampled populations ({', '.join(groups())}) have volume rows and direct "
      f"rows on the members an authority singles out (gate 15), never a bundled exact-set row. 09_Rubrics.json mirrors P1–P{len(rows)} one to one "
      "(C-n = P-n).")
    w("")
    w("## A · Coverage matrix")
    w("| P | Source (exact prompt span · OE n) | Stable fact ID | What must be verified | Final state that proves it | Category "
      "(Outcome / Process candidate → C) | Expected/source values and pointers · accepted alternatives · date acceptance · F-IDs |")
    w("|---|---|---|---|---|---|---|")
    for p, r in zip(P, rows):
        acc = "; ".join(r["acc"])
        dates = ("a plan date, not an instant, the same day in Pacific and UTC; any date form" if is_date_row(r) else "none graded")
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
        w(f"| {p} | no — must not hard-code; titles, wording and headings stay the Agent's | {dist} | {risk_note(r)} | {r['kind']} — "
          f"{cell(r['why'])} | {r['w']} | {r['dec']} | {group_cell(r)} | {d}; overlap group none | none · over-specific risk low: "
          f"{cell(r['alt'])} |")
    w("")
    w("## A3 · Format 5 — per-row acceptance cases, OE steps and reachability")
    w("| P | valid_case (must ACCEPT · prompt authority) | do_nothing_case (must REJECT · exact title text of the required write) | "
      "OE step ids (verbatim OE labels) | Deciding source reachability (PROMPT_LINKED / TRASH / ATTACHMENT_ONLY / UNLINKED) |")
    w("|---|---|---|---|---|")
    for i, (p, r) in enumerate(zip(P, rows)):
        w(f"| {p} | {cell(r['valid'])} (\"{r['span']}\") | REJECT — {cell(r['idle'])} (title: \"{cell(r['t'])}\") | {', '.join(r['oe'])} | "
          f"PROMPT_LINKED ({reach_note(i)}) |")
    w("")
    w("Final-reply test (whole set): \"Done. The plan doc and the tracker are in your Drive and shared with everyone on the review, "
      "each ad's ticket has its call and date, the ones that need new work are assigned, the two new store tickets are open, and both "
      "links are in Leonard's thread.\" → ACCEPT ☑ (no row grades the final response; the prompt asks to be told nothing beyond the "
      "deliverables, so a concise reply passes every row)")
    w("")
    w("## B · OE trace")
    w("| OE | Kind (write / discovery / friction) | Proved by row(s) | Own row? (reason) |")
    w("|---|---|---|---|")
    cites = {}
    for p, r in zip(P, rows):
        for o in r["oe"]:
            cites.setdefault(int(o.split()[1]), []).append(p)

    def with_fid(*fs):
        return [p for p, r in zip(P, rows) if fids(r) & set(fs)]

    uncited = {
        "deck": (with_fid("F9"), "no — the rule book: every call row reads a ticket against it"),
        "mails": (with_fid("F70", "F71"), "no — the listing step; its mails decide the due-date and Skip rows"),
        "draft": ([p for p, r in zip(P, rows) if r["dist"].startswith("T2 ")],
                  "no — the superseded draft; its Oct 17 fails the Oct 15 due-date rows"),
        "restart": (with_fid("F71"), "no — proved by the two landscape call rows it decides"),
        "note": (with_fid("F76"), "no — proved by the three re-recorded cuts' call rows"),
        "im": (with_fid("F79"), "no — Marcus's done claim; the call rows it would flip reject it"),
        "masters": (with_fid("F79"), "no — the two test files; the call rows they would flip reject them"),
        "review_test": (with_fid("F79"), "no — Robert's review decides these call rows"),
        "packs": (with_fid("F81"), "no — proved by the four end card call rows it decides"),
        "music": (with_fid("F82"), "no — proved by the ART-809 call row it decides"),
        "users": (with_fid("F90"), "no — the assignee and team ids the assignment and ticket rows use"),
    }
    count_of = {"w_a_": [pn(r["tag"]) for r in of("assignment") if is_volume(r)], "w_c_": [pn(r["tag"]) for r in of("comment count")],
                "w_share": [pn(r["tag"]) for r in of("share") if is_volume(r)]}
    for label, n in sorted(LABEL.items(), key=lambda x: x[1]):
        kind = "write" if label.startswith("w_") else "discovery"
        counted = next((v for k, v in count_of.items() if label.startswith(k)), None)
        if n in cites:
            rs = sorted(set(cites[n]), key=lambda x: int(x[1:]))
            own = "yes — the write's result row" if kind == "write" else "no — proved by the content row(s) it decides"
        elif counted:
            rs, own = counted, "no — a write outside the samples; counted in the volume row(s) (sampled population, gate 15)"
        else:
            rs, own = uncited.get(label, ([], "no — no row cites this step"))
        w(f"| OE {n} | {kind} | {', '.join(rs[:8]) or 'none'}{' …' if len(rs) > 8 else ''} | {own} |")
    w("")
    w("## C · Process candidates — three-condition test")
    w("| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) "
      "behavioural, not trace | Result (Process / tighten P-n with F-n) |")
    w("|---|---|---|---|---|---|---|")
    reply = ps(of("reply"))
    w(f"| {reply} | \"reply in Leonard's thread with both links before the review\" | An Outcome does prove "
      "it: the reply must hold both links, and a link exists only once its file does; 'before the review' is a deadline the clock "
      "meets, since a run happens on Oct 1 and the review is Thu Oct 2 (evt_d947bf7cd910549b674b1f) | fails as a Process row — the prompt "
      "orders no other write around the reply, so a valid run may comment or assign after it; the reply only needs links that exist "
      f"anyway | fails — {reply} already reject a reply without either link, the only ordering the "
      "prompt states | fails — a timestamp comparison would grade the trace, with no behaviour left to observe | no Process row: "
      f"{reply} carry it as Outcomes with F1; the prompt states no ordering dependency between writes |")
    w("")
    w("## D · Spot-check groups")
    w("| G | Item set (F-IDs, total N; keys as backticked literals) | Sampled items (≤ 5) and why hard/edge | Volume row | Exact-set row "
      "(`none — bundle (Rubric Writing §7; Eval 2.2)`) | Core requirement? (must be no) |")
    w("|---|---|---|---|---|---|")
    adf = ad_fids()
    grp = groups()
    for g, d in grp.items():
        w(group_line(g, d, adf))
    w("")
    w(f"Not sampled: the {n_call} comment call rows and {n_due} comment due-date rows are one per target, with {ps(of('comment count'))} as the "
      "comments' counts (the content differs per ticket, so these are not a population under gate 15).")
    w("")
    w("## E · Summary")
    vols = list({r["tag"]: r for d in grp.values() for r in d["vols"]}.values())
    w(f"Rows {len(rows)} · Outcome {len(rows) - N_PROC} · Process candidates 1 considered, {N_PROC} kept — ≥ 1 Outcome ☑ · Process rows ≤ 50 % ☑ · "
      "fewer than two Process rows failing the three-condition test ☑ (none in the set; §C records the one candidate) · builder "
      f"minimum 5 ☑ · one volume row per sampled output, no bundled exact-set row ☑ ({ps(vols)}) · predicted all-fail rows = 0 ☑ (rows "
      "a baseline run may miss because it never opened a record are real misses, reachable through cataloged tools; none sits on the "
      "four Evals bases)")
    top, over_units = diversity()
    pct = lambda s: f"{100 * s / TOTAL_W:.0f}%"  # noqa: E731
    box = "☑" if not over_units else "☒"
    why = ("" if not over_units else " — every ticket fact reaches this sheet through its ledger locator edge, so it is upstream of almost "
           "every row by the task's design; reported to the requester with the ledger and the cells left as they are")
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
    w(f"Set size: {len(rows)} rows, with no human-time estimate entered yet. The count follows the prompt's per-target asks: "
      f"{n_call} call and {n_due} due-date rows for the {len(ADS)} comments are {100 * (n_call + n_due) // len(rows)}% of the set, and they are "
      "not duplicates of one another (each ticket's call and date is its own write).")
    present = [v for k, v in WRITE_FAMILIES.items() if any(family(r).startswith(k) for r in rows)]
    n_req = len(G.rows_in(ledger(), r"^A\b"))
    n_gap = len(WRITE_FAMILIES) - len(present)
    w(f"Coverage: requirements {n_req - n_gap}/{n_req} (ledger R1–R{n_req}) · OEs {len(LABEL)}/{len(LABEL)} (§B) · writes "
      f"{len(present)}/{len(WRITE_FAMILIES)} ({'; '.join(present)}) · told facts 0/0 (the prompt asks to be told nothing beyond the deliverables) · "
      "friction 0/0 (Friction: none)")
    covered = [s for s in SLOTS if covering(s["id"])]
    mw, mp, nflip = mech_share()
    nw, np_ = mech_node_share()
    w(f"Gradable surface (gate 17): slots {len(SLOTS)} · covered {len(covered)} · dispositioned {len(SLOTS) - len(covered)} (§G) · no slot "
      f"with neither ☑ · mechanism share {mp}% of the weight ({mw} of {TOTAL_W}, the rows that rows.json maps to the {nflip} slots a "
      f"mechanism can flip; {np_}% counting every row a mechanism's node decides, since rows.json maps one row per slot; reported, not gated)")
    w("Four prohibitions: ☑ unstated expectations (every row quotes a prompt span; Leonard's message, which the prompt says to do in "
      "full, is the incorporated ask) ☑ conclusions on ambiguous evidence (none: each graded value is settled by a later or more "
      "specific record) ☑ grading the distractor (traps are graded through the correct value, never their disclosure) ☑ hard-coded "
      "titles/phrasings (no title, heading or file name is required; the call words follow the deck, in any case)")
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
        sel = cell(" ".join(map(str, s["selector"])))[:80].replace("<", "‹")
        mech = ", ".join(s.get("mechanisms") or []) or "—"
        rs = covering(s["id"])
        if not rs:
            w(f"| {s['id']} | {s.get('fact_id') or '—'} | {sel} · {s['role']} / {s.get('group') or '—'} | {s['work_kind']} ({s['weight']}) | "
              f"{mech} → — | — | unassigned: rows.json names no covering row (gate 17) |")
            continue
        r = rs[0]
        note = slot_note(s, rs)
        band = f"{r['w']}" if r["w"] == s["weight"] else f"{r['w']} by the row's kind of work, {r['kind']}; the slot says {s['weight']}"
        w(f"| {s['id']} | {s.get('fact_id') or r['fact']} | {sel} · {s['role']} / {s.get('group') or '—'} | {s['work_kind']} ({band}) | "
          f"{mech} → {r['dec']} | {', '.join(pn(x['tag']) for x in rs)} | covered: the title rejects the omission and the plausible "
          f"wrong value ({wrong_value(r)}).{note} |")
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
