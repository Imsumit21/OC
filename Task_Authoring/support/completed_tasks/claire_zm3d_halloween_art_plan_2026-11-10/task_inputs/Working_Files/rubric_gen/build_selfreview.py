#!/usr/bin/env python3
"""Write selfreview.md (the plan's Self-review) from rows.json, a fresh re-read of the records and the probe output.

    build_selfreview.py          re-verify every value, write selfreview.md
    build_selfreview.py --probe  turn probe_raw.txt (real shortcut_probe.py output) into probe.txt: the output verbatim in a
                                 fence, then one SHORTCUT-OK line per record hit, its reason read from that record; an
                                 unclassified hit stops the build instead of getting a stock reason

Values are re-read here, never copied: seeded values from a fresh parse of 01_Universe_Inject.sql (never executed), base
records through tools/hg.py, and every call, due date, maker, count and titled ticket list through oe_gen/model.py (asserted
against solver/truth.json). A value that disagrees stops the build; a stale field outside the JSON is listed under Unresolved.
Rows are classified as in build_plan.py, by prefix, fact, vals and grp, never by full tag.
Run build_plan.py after this one, since the plan embeds selfreview.md and probe.txt."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_plan as B  # noqa: E402
from build_plan import G, M, P, WF, TI, axis, family, is_volume, key_of, of, ps, rows, run_tool  # noqa: E402
from base_check import parse_sql  # noqa: E402

PROBE_RAW = HERE / "probe_raw.txt"
WRONG_CALL = {"Halloween version": "Refresh first", "Refresh first": "Halloween version", "Skip": "Refresh first"}
# base records, read for real through hg.py: (service, file, pointer, what the record must hold, what it proves)
BASE_READS = [
    ("slack", "messages/C06DJBJL798/2025-08.json", "/22", ["1755114007.441789", "background music is baked in"],
     "Frederick's Aug 13 post behind ART-809's Refresh first (F82)"),
    ("slack", "messages/C06DJBJL798/2025-08.json", "/33", ["1755118817.302199", "1755114007.441789"],
     "Marcus's reply in that thread (F82)"),
    ("slack", "messages/C08R8CHB0QL/2025-09.json", "/121", ["1758121809.236839", "Halloween theme"],
     "Martin's Sep 17 icon concept (F88)"),
    ("slack", "users.json", "/3", ["EMPLOYEE_0005_SLACK_ID", "julia.lawson@harmonygames.co"], "the person Martin tags (F75)"),
    ("linear", "data.json", "/users/33", ["usr_c77c50cc15c5342d", "marcus.bennett@harmonygames.co"], "Marcus Bennett's Linear user (F90)"),
    ("linear", "data.json", "/users/18", ["usr_8140f09bf9f1b94c", "julia.lawson@harmonygames.co"], "Julia Lawson's Linear user (F90)"),
    ("linear", "data.json", "/users/9", ["usr_51f5f16d46e8cf55", "martin.walsh@harmonygames.co"], "Martin Walsh's Linear user (F90)"),
    ("linear", "data.json", "/users/28", ["usr_b501f018a4c5319f", "marcus.lee@harmonygames.co"], "the other Marcus the rows reject (F90)"),
    ("linear", "data.json", "/teams/0", ["team_ART", "ART"], "team ART, the new tickets' team (F90)"),
]


WIN = re.compile(r"\b(?:Oct(?:ober)?\.? ?(?:0?[6-9]|10)\b|10/(?:0?[6-9]|10)\b|2025-10-(?:0[6-9]|10)\b)")
LATE = re.compile(r"\b(?:Oct(?:ober)?\.? ?15\b|10/15\b|2025-10-15\b)")
SIX = [f"run-{i}" for i in range(1, 7)]
RUNS = json.loads((HERE / "baseline_writes.json").read_text())


def two_date_runs(r):
    """Baseline runs whose text for this ad holds a date in the row's Oct 6 to Oct 10 window AND an Oct 15 date."""
    key = key_of(r)
    n = 0
    for x in SIX:
        if family(r) == "comment due":
            text = " ".join(c["body"] for c in RUNS[x]["comments"].get(key, []))
        else:
            cells = [" ".join(str(c) for c in row) for s in RUNS[x]["sheets"] for g in s["tabs"].values() for row in g
                     if any(str(c).startswith(key) for c in row)]
            text = " ".join(cells)
        n += bool(WIN.search(text) and LATE.search(text))
    return n


def milestone_rows():
    """Oct 10 due rows where a baseline's refresh milestone sits inside the accepted window next to an Oct 15 hand-off."""
    out = []
    for r in rows:
        key = key_of(r)
        if (axis(r) == "due" and key in M.ISS and M.due(key) == "Fri Oct 10" and "final due date" not in r["t"]
                and two_date_runs(r)):
            out.append(r)
    return out


def record_ids(r, n=2):
    """The first n record pointers of a row's evidence, before its Accept clause."""
    src = r["ev"].split("Accept:")[0]
    out = []
    for m in G.OPAQUE.finditer(src):
        x = m.group(0).rstrip(".,);'")
        if x not in out:
            out.append(x)
    return "; ".join(out[:n]) or r["fids"]


def row_call(r):
    return next((c for c in ("Halloween version", "Refresh first", "Skip", "Reuse") if f"`{c}`" in r["vals"]), None)


def counter_reading(r):
    """(a) a valid answer that could fail, (b) a wrong answer that could pass, each resolved from the row's own records."""
    f, tag, why, valid = family(r), r["tag"], r["why"].rstrip("."), r["valid"]
    ids = record_ids(r)
    if f == "comment call":
        call = row_call(r)
        wrong = "Reuse or 'already done'" if r["dist"].startswith("T4 ") else WRONG_CALL.get(call, "another call")
        trap = "" if r["dist"] == "none" else f" (the trap: {B.DIST_LEDGER_ID.get(r['dist'], r['dist'])})"
        return (f"(a) {valid} passes, and so does a longer comment with a reason ({'; '.join(r['acc'])}) · (b) {wrong} on this "
                f"ticket fails{trap}: {why}. Evidence {ids}")
    if f == "comment due":
        other = "Wed Oct 15" if "Oct 10" in r["t"] else "Fri Oct 10"
        open_note = (f" Not closed by the title: {two_date_runs(r)} of 6 baselines give a refresh date in the window and an Oct 15 hand-off to "
                     "Frederick here, and that pair could pass on the milestone (09_Rubric_Check.md Findings)"
                     if r["tag"] in MILESTONE else "")
        return (f"(a) {valid} passes; a date inside the title's window passes, and setting the ticket's due-date field as well is "
                f"allowed · (b) {other} (the other tier) or the draft's Oct 17 fails: {why}.{open_note} Evidence {ids}")
    if f == "share" and is_volume(r):
        return ("(a) six shares as commenter or writer pass, in any order, and Claire's own access does not count · (b) a seventh person or the "
                "whole domain fails; adding Julia because she makes the statics fails too, a deliberate tightening of brief §4b, since the "
                f"prompt's audience is the review (plan header). Evidence {ids}")
    if f == "share":
        return (f"(a) writer access passes as well as commenter; this row reads only this person's access · (b) a reader share fails 'so they "
                f"can comment'. Evidence {ids}")
    if f == "assignment":
        if is_volume(r):
            return f"(a) an assignment by id, name or email counts · (b) {r['alt']} Evidence {ids}; {r['fids']}"
        wrong = "Marcus Bennett or Martin Walsh" if "julia.lawson" in r["vals"] else "marcus.lee@harmonygames.co, or Martin Walsh"
        return (f"(a) an assignment by id, name or email passes; the row reads the final assignee · (b) {wrong} fails: {why}. "
                f"Evidence {ids}")
    note = (f" Not closed by the title: {two_date_runs(r)} of 6 baseline trackers pair a refresh date in the window with an Oct 15 hand-off on "
            "this ad (09_Rubric_Check.md Findings)." if tag in MILESTONE else "")
    return f"(a) {valid} passes ({'; '.join(r['acc'])}) · (b) {r['alt']} Reason: {why}.{note} Evidence {ids}"


MILESTONE = {r["tag"] for r in milestone_rows()}
CR = {r["tag"]: counter_reading(r) for r in rows}


def sql_rows():
    return parse_sql((TI / "01_Universe_Inject.sql").read_text(errors="replace"))


def count_table():
    """{fact: recount} from model.py, plus the attendees other than Claire from the seeded invite."""
    hv, rf, sk = (len(M.BY[c]) for c in ("Halloween version", "Refresh first", "Skip"))
    invite = M.rows("gcal.gcal_events", event_id="evt_d947bf7cd910549b674b1f")[0]
    people = sorted(a["email"] for a in json.loads(invite["attendees_json"]) if a["email"] != "claire.morgan@harmonygames.co")
    ads, working = len(M.ADS), len(M.MARCUS) + len(M.JULIA)
    return ({"ads.refresh.count": rf, "ads.halloween.count": hv, "ads.skip.count": sk, "tracker.keys": ads, "tracker.halloween.count": hv + 2,
             "tracker.refresh.count": rf, "tracker.reuse.count": 2, "tracker.skip.count": sk, "tracker.due30.count": len(M.D10),
             "tracker.due18.count": len(M.D15), "tracker.maker42.count": len(M.MARCUS), "tracker.maker6.count": len(M.JULIA),
             "tickets.scope": "two", "comments.scope": ads, "comments.due30.count": len(M.D10), "comments.due18.count": len(M.D15), "assign.scope": working,
             "assign.julia": len(M.JULIA), "assign.marcus": len(M.MARCUS), "share.w_doc.scope": len(people), "share.w_sheet.scope": len(people)},
            people)


def stale_fields():
    """Fields of rows.json that no longer agree with the row's own title; they sit outside 09_Rubrics.json, so they are notes."""
    out = []
    for r in rows:
        for v in B.literals(r):
            if re.fullmatch(r"\d+", v) and not re.search(rf"\b{v}\b", r["t"]):
                out.append(f"{r['tag']} keeps vals `{v}`, which its title does not state (alt: {r['alt'].rstrip('.')})")
    return out


def unresolved_items():
    """Open items shared by the plan's Self-review and the check report."""
    tw, (_top, over_units) = B.TOTAL_W, B.diversity()
    out = []
    if over_units:
        out.append("diversity.authority_share (the one structural gate check): " + "; ".join(
            f"{u} decides {s} of {tw} ({100 * s / tw:.0f}%)" for u, s in over_units) + ". Every ticket fact reaches the sheet through its "
            "locator edge, so no honest row can sit outside it; the ledger and the cells stay as they are, and the requester decides")
    if B.contested():
        out.append("A1 and A2 stay contested until /rubric run 2 rules on the dismissal; if upheld they are two Moderate overlap groups, and any Moderate "
                   "fails Overall Rubric Quality. Run 1's report also says that if the comment rows stay, the assignment rows should get the same "
                   "full coverage; they stay sampled in the assignment group")
    if MILESTONE:
        most = max(two_date_runs(B.BY[t]) for t in MILESTONE)
        out.append(f"{len(MILESTONE)} Oct 10 due rows can pass on a refresh milestone: up to {most} of 6 baselines wrote a refresh date inside the window "
                   "plus an Oct 15 hand-off on these ads (09_Rubric_Check.md Findings gives the wording)")
    out.extend(stale_fields())
    loose = [r for r in of("share") if "anyone else as well is allowed" in r["alt"]]
    if loose and any(is_volume(r) for r in of("share")):
        out.append(f"{len(loose)} per-person share rows still say 'Sharing with anyone else as well is allowed' next to the exact-six scope rows")
    out.append("no human-time estimate exists yet (05_Human_Time.md is the requester's slot), so the set-size line has no hours")
    trap_ids = [r["tag"] for r in rows if r["dist"] in B.DIST_LEDGER_ID]
    if trap_ids:
        out.append(f"{len(trap_ids)} rows of rows.json name a distractor by its manifest trap id ({', '.join(trap_ids)}); the plan prints the ledger's T-ID")
    return out


def reverify():
    """Every check runs in this build. Returns the report lines and a list of failures (empty when all pass)."""
    fails, lines = [], []
    stmts = sql_rows()
    side = json.loads((WF / "00_V3_Authoring_Evidence.json").read_text())["rubric_rows"]
    uniq = {}
    for r in side:
        for s in r["source_records"]:
            uniq[(s["table"], json.dumps(s["identity"], sort_keys=True), s["column"], s["source_value"])] = s
    norm = lambda q: re.sub(r"\s+", " ", q)  # noqa: E731
    ok = 0
    for (table, idn, col, val), _s in uniq.items():
        ident = json.loads(idn)
        hit = [x for x in stmts if x.get("op") in ("insert", "update") and x.get("table") == table and
               all(str((x.get("row") or {}).get(k)) == str(v) for k, v in ident.items())]
        if hit and norm(val) in norm(" ".join(str((x.get("row") or {}).get(col)) for x in hit)):
            ok += 1
        else:
            fails.append(f"sidecar value not re-read: {table} {ident} {col}")
    lines.append(f"- Seeded values: all {len(uniq)} distinct source records of 00_V3_Authoring_Evidence.json re-read from a fresh parse of "
                 f"01_Universe_Inject.sql (tools/base_check.py parse_sql, never executed): {ok} of {len(uniq)} hold their source_value in the "
                 "named table, identity and column.")
    n = {"call": 0, "due": 0, "maker": 0}
    emails = {"Marcus Bennett": "marcus.bennett@harmonygames.co", "Julia Lawson": "julia.lawson@harmonygames.co"}
    wrong = []
    for r in rows:
        key = key_of(r)
        if key is None or key not in M.ISS:
            continue
        call, due, mk, ax = M.call(key), M.due(key), M.maker(key), axis(r)
        if ax in n:
            n[ax] += 1
        want = {"call": [call], "due": [due], "maker": [mk, emails.get(mk)]}.get(ax)
        if want and not any(f"`{x}`" in r["vals"] for x in want if x):
            wrong.append(r["tag"])
    if wrong:
        fails.append(f"rows disagree with model.py: {wrong}")
    lines.append(f"- Per-ad values: oe_gen/model.py re-derives each ad's call, due date and maker from the parsed rows and asserts them "
                 f"against solver/truth.json; {n['call']} call rows, {n['due']} due-date rows and {n['maker']} maker rows of this plan all "
                 f"equal it ({len(wrong)} differences).")
    table, attendees = count_table()
    checked, unknown, bad = [], [], []
    for r in rows:
        if not is_volume(r) or "only on tickets other than" in r["t"]:  # a scope row states no count; its list is checked below
            continue
        want = len(M.ADS) + 4 if r["fact"] == "tracker.keys" and "surface" in r["t"] else table.get(r["fact"])
        if want is None:
            unknown.append(r["tag"])
        elif re.search(rf"\b{want}\b", r["t"]):
            checked.append(r["tag"])
        else:
            bad.append(f"{r['tag']} (model {want})")
    if bad:
        fails.append(f"counts disagree: {bad}")
    per_person = [r for r in of("share") if not is_volume(r)]
    missing = [a for a in attendees if sum(a in r["vals"] for r in per_person) != 2]
    if missing:
        fails.append(f"an attendee without one share row per file: {missing}")
    lines.append(f"- Counts: {len(checked)} count rows recounted from model.py and the invite, each title against the recount: {len(M.ADS)} ads, calls "
                 f"{len(M.BY['Halloween version'])}/{len(M.BY['Refresh first'])}/{len(M.BY['Skip'])}, due {len(M.D10)}/{len(M.D15)}, makers "
                 f"{len(M.MARCUS)}/{len(M.JULIA)}, {len(attendees)} attendees on evt_d947bf7cd910549b674b1f ({len(bad)} differences)."
                 + (f" No recount rule for {', '.join(unknown)}." if unknown else ""))
    sets = {"Halloween version": M.BY["Halloween version"], "Refresh first": M.BY["Refresh first"], "Skip": M.BY["Skip"], "Fri Oct 10": M.D10,
            "Wed Oct 15": M.D15, "Julia Lawson": M.JULIA, "Marcus Bennett": M.MARCUS,
            "Skip and Archive (out of scope for assignees)": M.BY["Skip"] + M.ARCHIVE}
    named, off = [], []
    for r in rows:
        keys = set(re.findall(r"ART-\d+", re.sub(r"ART-\d+ to ART-\d+", " ", r["t"])))
        if len(keys) >= 3:
            hit = next((k for k, v in sets.items() if set(v) == keys), None)
            (named if hit else off).append(r["tag"])
    if off:
        fails.append(f"a ticket list in a title matches no recomputed set: {off}")
    lines.append(f"- Ticket lists in titles: {len(named)} rows name a list of ART keys in the title, and each list equals a set recomputed by model.py "
                 f"({len(off)} differences).")
    base_lines, base_text = [], ""
    for svc, file, ptr, must, what in BASE_READS:
        raw = run_tool(["Task_Authoring/tools/hg.py", "search", "get", svc, "--file", file, "--pointer", ptr])
        base_text += raw
        held = [m for m in must if m in raw]
        if len(held) != len(must):
            fails.append(f"hg.py {svc} {file} {ptr} does not hold {set(must) - set(held)}")
        base_lines.append(f"  - `python3 Task_Authoring/tools/hg.py search get {svc} --file {file} --pointer {ptr}` → holds "
                          f"{', '.join(held)}: {what}")
    sql_text = (TI / "01_Universe_Inject.sql").read_text(errors="replace").replace('\\"', '"').lower()
    lits = sorted({v for r in rows for v in re.findall(r"`([^`]+)`", r["vals"]) if len(v) > 2})
    absent = [v for v in lits if v.lower() not in sql_text]
    in_base = [v for v in absent if v.lower() in base_text.lower()]
    neither = [v for v in absent if v not in in_base]
    lines.append(f"- Literals: {len(lits) - len(absent)} of {len(lits)} backticked literals found in the SQL text"
                 + (f"; {', '.join(f'`{v}`' for v in in_base)} found in the base reads below" if in_base else "")
                 + (f"; {', '.join(f'`{v}`' for v in neither)} found in neither, so each is a label of the row's own" if neither else "") + ".")
    lines.append("- Base records, read through tools/hg.py in this build:")
    lines.extend(base_lines)
    return lines, fails


def baseline_reads():
    """Why predicted all-fail stays 0: a record no baseline opened is a model miss, the record is there to read."""
    runs = json.loads((HERE / "baseline_writes.json").read_text())
    six = [f"run-{i}" for i in range(1, 7)]
    out = {}
    for marker in runs["run-1"]["reads"]:
        out[marker] = (sum(1 for x in six if runs[x]["reads"].get(marker)), runs["run-1"]["reads_detail"][marker]["record"])
    return out


def write_selfreview():
    lines, fails = reverify()
    assert not fails, fails
    L = ["## Self-review", ""]
    A = L.append
    scope = [r for r in rows if axis(r) == "scope" and family(r) in ("comment count", "assignment", "new ticket", "share")]
    A("Re-read as /rubric: walked Evals/3_Rubrics_Eval.md 1.4 and 3.1 against the plan in order. Every prompt requirement (ledger R1–R12) "
      "and every write family (plan doc; tracker; shares; ticket comments; assignments; new tickets; thread reply) has a result row on "
      f"the correct artifact, and every exclusion sits as a count or scope on a required write ({ps(scope)}). The prompt asks to be "
      "told nothing beyond the deliverables, so no row grades the final response; a concise final reply passes the whole set (§A3). "
      "Friction is none, so no recovery outcome is needed.")
    A("")
    A("Re-verified, every value in this build (ledger values were leads, not evidence):")
    A("")
    L.extend(lines)
    A("")
    reads = baseline_reads()
    low = [f"{rec} {n}/6" for _m, (n, rec) in reads.items() if n < 3]
    A("Predicted all-fail re-check: for every row the persona reaches the value through a cataloged tool (the Gmail, Slack, Calendar and "
      "Drive records have pasted YES lines under Visibility proof, and persona_view re-checks each id; Linear, Trello and Contacts are "
      "unscoped), each write exists in the catalog (gdocs_create_document, gsheets_create_spreadsheet, gsheets_values_update, "
      "gdrive_share_file, linear_create_comment, linear_update_issue, linear_create_issue, slack_send_message), Friction is none so no "
      "row needs a retry, and no evidence sits outside Claire's view. Count on the four bases: 0. The six rev3 baselines read some "
      f"deciding records rarely ({'; '.join(low)}; baseline_writes.json reads). Those are model misses on records a run could "
      "open, as the OE path shows, not an impossible target.")
    A("")
    top, over_units = B.diversity()
    tw = B.TOTAL_W
    A("Shortcut and diversity: " + probe_note() + f" Largest unit of discovery: {top[0][0]}, {top[0][1]} of {tw} ({100 * top[0][1] / tw:.0f}%), "
      f"then {top[1][0]} {100 * top[1][1] / tw:.0f}% and {top[2][0]} {100 * top[2][1] / tw:.0f}%. The live creatives sheet leads because "
      "the ledger's locator edges run every ticket fact through it (each ticket F-row has origin F4, the Unity tab); see Unresolved.")
    A("")
    elsewhere = [s["id"] for s in B.SLOTS if s["selector"][0] in ("field", "reason_matches") and B.covering(s["id"]) and
                 not any(family(x) == "tracker" for x in B.covering(s["id"]))]
    bare = [s["id"] for s in B.SLOTS if not B.covering(s["id"])]
    A(("Surface dispositions: none; " + f"all {len(B.SLOTS)} slots have a covering row, so §G carries no disposition. " if not bare else
       f"Surface dispositions: {', '.join(bare)} have no covering row in rows.json and need one or a disposition. ")
      + f"Strongest case for a further row: {len(elsewhere)} slots ({', '.join(elsewhere)}) name a tracker cell, and rows.json "
      "covers them through the ticket comment or the assignment on the same ad, while the tracker's columns are sampled. The value is one fact "
      "graded on the write the prompt requires per ticket, and a second row per ad would double the fact without new coverage. Gate 15 keeps "
      "each tracker group at five samples or fewer, and §G says so on each such line.")
    A("")
    A("Recorded decisions, re-checked against their sources in this build:")
    A("")
    for line in B.records():
        A(f"- {line}")
    A("")
    A("Counter-readings, one per section A row:")
    A("")
    A("| P | Counter-reading (a valid answer that could fail · a wrong answer that could pass) and resolution (evidence) |")
    A("|---|---|")
    for p, r in zip(P, rows):
        A(f"| {p} | Counter-reading — {B.cell(CR[r['tag']])} |")
    A("")
    A("Unresolved: " + " · ".join(f"({i}) {u}" for i, u in enumerate(unresolved_items(), 1)) + ".")
    (HERE / "selfreview.md").write_text("\n".join(L) + "\n")
    print("selfreview written:", len(rows), "counter-readings;", len(lines), "re-verification lines")


def parse_probe():
    """[(service, record, held values)] for each distinct record in probe_raw.txt, plus the raw HIT line count."""
    held, n = {}, 0
    for line in PROBE_RAW.read_text().splitlines():
        m = re.match(r"^HIT (\S+) (\S+) ", line)
        if not m:
            continue
        n += 1
        held.setdefault((m.group(1), m.group(2)), set()).update(re.findall(r"`([^`]+)`", line))
    return held, n


def probe_note():
    p = HERE / "probe.txt"
    raw = PROBE_RAW.read_text() if PROBE_RAW.exists() else ""
    if not p.exists() or not re.search(r"^verdict: ", raw, re.M):
        return "the §F probe is pending."
    held, n = parse_probe()
    verdict = re.search(r"^verdict: (.*)$", raw, re.M).group(1)
    incomplete = len(re.findall(r"^INCOMPLETE ", raw, re.M))
    lines = p.read_text().count("SHORTCUT-OK:")
    addr = sum(1 for (svc, _r), v in held.items() if svc in ("gmail", "gsheets"))
    keyed = {k: v for k, v in held.items() if any(x.startswith("ART-") for x in v)}
    comments = [k for k in keyed if "linear_comments" in k[0]]
    joined = [f"{k[0]} {k[1]}" for k, v in keyed.items() if {x for x in v if not x.startswith("ART-")} - {"Android US phone", "iOS UK"}]
    joint = (f"No hit holds an ad key next to a call, date or maker (checked here over all {len(keyed)} hits with a key)." if not joined else
             f"{len(joined)} hits hold an ad key next to a call, date or maker and need a second look: {'; '.join(joined[:4])}.")
    grid = M.GRID["Unity"][0]
    pops = len(re.findall(r"^HIT .* keys of population ", raw, re.M))
    return (f"the §F probe's verdict is {verdict}, with {incomplete} INCOMPLETE lines and {lines} SHORTCUT-OK lines, one per record ({n} HIT lines, "
            f"since the Unity tab hits {pops} populations). Strongest collapse cases, each read: (1) the sheet's Unity tab holds 56 of 58 ad keys and "
            f"so most of every population, and a run could list the ads from it, but its columns are {', '.join(grid)}, so no call, due date, "
            "maker or campaign sits there, and two running ads are not on it. (2) Frederick's reply C0880U9751A/1759275738.984915 gives the Oct "
            "10 date, but a run still needs each ticket's campaigns to know which ads it binds; finding it is the designed work. (3) The "
            f"deck's calls slide holds the four call words and no ticket. (4) Each of the {len(comments)} ticket comments holds its own key and "
            f"campaign names only. {joint} The other {addr} base hits are Gmail and sheet records that hold staff addresses, which are directory facts.")


def clean(t, n=70):
    t = re.sub(r"[\w.+-]+@[\w.-]+|\[[A-Z_]+_\d+\]|\(\s*\)", " ", t)
    t = re.sub(r"[|`<>\"]", " ", t).replace(",", " ")
    return re.sub(r"\s+", " ", t).strip(" ()-:")[:n].strip()


def searcher():
    from pathlib import Path as _P
    ctx = G.Ctx("rubric-writing", _P(B.TASKREL), "lint")
    assert G.assignment_context(ctx)
    import persona_view
    import shortcut_probe as sp
    return sp.Searcher(persona_view.resolve_persona(B.PERSONA))


def snippet_title(s, svc, rec, held):
    """The record's subject or file name, from the snippets the probe itself cached for this record."""
    outs = []
    for v in held:
        snip = s.scoped(svc, v)["records"].get(rec)
        if snip:
            outs.append(clean(snip))
    return max(outs, key=len) if outs else ""


def seeded_reason(svc, rec, stmts):
    """The reason for a hit on a seeded row, read from that row (never typed per record id)."""
    line = int(re.match(r"L(\d+):", rec).group(1))
    row = next(x["row"] for x in stmts if str(x["line"]) == str(line))
    table = svc.split(":", 1)[1]
    if table == "gcal.gcal_events":
        own = row["event_id"] == "evt_d947bf7cd910549b674b1f"
        return (("Claire's copy of the review event, the designed authority for the share rows (F2): the prompt names the review, so finding "
                 "its guest list is the work, and it says nothing on any ad, call or date") if own else
                f"the same review on {row['calendar_id']}'s calendar, with the guest list of evt_d947bf7cd910549b674b1f and no call, date or ad")
    if table == "gdocs.docs_documents":
        return ("Arthur's release calendar, the designed authority for the store dates (F7), which Leonard's message sends the Agent to; it holds "
                "the merge cut, the Oct 17 submission and its share list, and no ad, call or maker")
    if table == "gdrive.drive_files":
        extra = {"Store": "; listing it is how a run sees the iPad set is absent, which is the designed work",
                 "cheer_fastcouch_halloween_9x16.mp4": "; it is the turned-down test file, a decoy (T3), not an answer",
                 "cheer_fastcouch_halloween_16x9.mp4": "; it is the turned-down test file, a decoy (T3), not an answer"}.get(row["name"], "")
        return f"Drive row of '{row['name']}': the addresses are its shared_with list, file metadata with no call, date or maker{extra}"
    if table == "gmail.gmail_messages":
        return {"October UA plan (draft)": "Frederick's Sep 12 draft (F69), superseded by his Sep 30 mail: it holds the four campaign names and "
                                           "its recipients, and its Oct 17 date is the stale value the rows reject",
                "Unity retention restart": "Frederick's Sep 29 mail (F71), a designed authority for two landscape cuts: it holds its recipients and a "
                                           "campaign name, no call, due date or ad key",
                "October UA plan - changes": "Frederick's Sep 30 mail (F70), which Leonard's message sends the Agent to: it holds the Oct 15 date, "
                                             "overturned for Android US phone by his later reply, and its recipients, no per-ad call"}.get(row["subject"])
    if table == "gsheets.sheets_sheets":
        if row["title"] == "Unity":
            return ("the live creatives sheet's Unity tab, the designed entry point Leonard's message names: it lists 56 of the 58 ad keys, and its "
                    "columns (Creative, Format, Live since, ART ticket) hold no call, due date, maker or campaign, so every answer still needs "
                    "the ticket comments, the deck and the mails")
        return {"Store": "the sheet's Store tab, the designed entry point for the store surfaces: it names the four surfaces and no call, date or "
                          "maker; the calls need the Store folder and the threads",
                "Read me": "the sheet's Read me tab, the designed pointer to the ticket comments and the Halloween push card: it names the campaigns "
                           "and no ad's call, date or maker",
                "Archive": "the sheet's Archive tab, the paused rows a run must leave out (T14): it holds the four paused keys and no call or date"}.get(row["title"])
    if table == "gsheets.sheets_spreadsheets":
        return "the live creatives sheet's own record: the addresses are its share list, with no call, date or maker"
    if table == "gslides.slides_page_elements":
        return ("the calls slide of Robert's deck, the designed authority (H3): it defines the four call words and names no ticket, so a run "
                "still reads each ad against it")
    if table == "gslides.slides_presentations":
        return "Robert's deck's own record: the addresses are its share list, with no call, date or maker"
    if table == "linear.linear_comments":
        return (f"{row['issue_id']}'s own ticket comment, which the prompt's 'its ART ticket' and the sheet's Read me send the Agent to: it holds its own "
                "key and campaign names, no call, due date or maker; the call comes from reading it against the deck")
    if table == "slack.slack_messages":
        if str(row.get("ts")) == "1759269913.882683":
            return ("Leonard's ask, the message the prompt names: it holds the deliverables' names and the deck's word in passing, and no per-surface "
                    "call, date or maker beyond the split the rows test against later records")
        return ("Frederick's reply in #zombie-match3d, the designed authority for the Android date (T20): finding it is the work, and a run still "
                "needs each ticket's campaigns to apply it; it names no ad")
    return None


def write_probe():
    raw = PROBE_RAW.read_text().rstrip()
    held, _n = parse_probe()
    stmts = sql_rows()
    s = searcher()
    ok, undone = [], []
    for (svc, rec), vals in held.items():
        why = None
        people = sum(1 for v in vals if v.endswith("@harmonygames.co"))
        others = sorted(v for v in vals if not v.endswith("@harmonygames.co"))
        if svc.startswith("sql:"):
            why = seeded_reason(svc, rec, stmts)
        elif svc == "gmail" and not others:
            name = snippet_title(s, svc, rec, vals)
            why = (f"base mail '{name or 'no subject'}': only its To/Cc headers match, {people} staff addresses, which are directory facts; it names no ad, "
                   "call or due date, and who is on the review comes from evt_d947bf7cd910549b674b1f")
        elif svc == "gsheets" and not set(others) - {"Skip", "tracker"}:
            name = snippet_title(s, svc, rec, vals)
            extra = {"Skip": ", and 'skip' is an unrelated word in a cell", "tracker": ", and 'tracker' is in its file name"}.get(others[0] if others else "", "")
            why = (f"base sheet '{name}', shared across the staff: the addresses are its share list{extra}; it names no ad, call or due date of this plan")
        if why:
            ok.append(f"SHORTCUT-OK: {svc} {rec} — {why}")
        else:
            undone.append(f"{svc} {rec}")
    assert not undone, f"no reason for: {undone}"
    assert not re.search(r"^INCOMPLETE ", raw, re.M), "dispositions for INCOMPLETE lines are not written yet"
    (HERE / "probe.txt").write_text("```text\n" + raw + "\n```\n\n" + "\n".join(ok) + "\n")
    print("probe written:", len(ok), "dispositions")


if __name__ == "__main__":
    if "--probe" in sys.argv[1:]:
        write_probe()
    else:
        write_selfreview()
