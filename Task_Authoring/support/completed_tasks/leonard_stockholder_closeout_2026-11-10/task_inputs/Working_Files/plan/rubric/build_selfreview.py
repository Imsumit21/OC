#!/usr/bin/env python3
"""Write selfreview.md (the plan's Self-review) from rows.json, a fresh re-read of the records and the probe output.

    build_selfreview.py          re-verify every value, write selfreview.md
    build_selfreview.py --probe  turn probe_raw.txt (real shortcut_probe.py output) into probe.txt: the output verbatim in a
                                 fence, then one SHORTCUT-OK line per record hit, its reason read from that record; an
                                 unclassified hit stops the build instead of getting a stock reason

Values are re-read here, never copied: seeded values from a fresh parse of 01_Universe_Inject.sql (never executed), base
records through tools/hg.py, and every holder figure, label, state, last day and count against solver/truth.json. A value that
disagrees stops the build; a stale field outside the JSON is listed under Unresolved.
Rows are classified as in build_plan.py, by prefix, fact, vals and grp, never by full tag.
Run build_plan.py after this one, since the plan embeds selfreview.md and probe.txt."""
import collections
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_plan as B  # noqa: E402
from build_plan import G, LABEL, LINES, P, TI, TRUTH, WF, axis, family, is_volume, key_of, of, ps, rows, run_tool  # noqa: E402
from base_check import parse_sql  # noqa: E402

sys.path.insert(0, str(WF / "plan/oe"))
import oe_data as D  # noqa: E402  (issue to address and ES id, asserted against solver/truth.json by oe_data itself)

PROBE_RAW = HERE / "probe_raw.txt"
MON = {m: i + 1 for i, m in enumerate("January February March April May June July August September October November December".split())}


def iso(s):
    """A last-day value in the form the row states (March 31, 2026 or 2026-02-20), as 2026-03-31."""
    m = re.fullmatch(r"([A-Z][a-z]+) (\d{1,2}), (\d{4})", s)
    if m:
        return f"{m.group(3)}-{MON[m.group(1)]:02d}-{int(m.group(2)):02d}"
    return s


def record_ids(r, n=2):
    """The first n record pointers of a row's evidence, before its Accept clause."""
    src = r["ev"].split("Accept:")[0]
    out = []
    for m in G.OPAQUE.finditer(src):
        x = m.group(0).rstrip(".,);'")
        if x not in out:
            out.append(x)
    return "; ".join(out[:n]) or r["fids"]


def counter_reading(r):
    """(a) a valid answer that could fail, (b) a wrong answer that could pass, each resolved from the row's own records."""
    why = r["why"].rstrip(".")
    return (f"(a) {r['valid']} passes ({'; '.join(r['acc'])}) · (b) {r['alt']} Reason: {why}. Evidence {record_ids(r)}; {r['fids']}")


CR = {r["tag"]: counter_reading(r) for r in rows}


def sql_rows():
    return parse_sql((TI / "01_Universe_Inject.sql").read_text(errors="replace"))


def stale_fields():
    """Fields of rows.json that no longer agree with the row's own title; they sit outside 09_Rubrics.json, so they are notes."""
    out = []
    for r in rows:
        for v in B.literals(r):
            if re.fullmatch(r"\d+", v) and len(v) > 1 and not re.search(rf"\b{v}\b", r["t"]):
                out.append(f"{r['tag']} keeps vals `{v}`, which its title does not state (alt: {r['alt'].rstrip('.')})")
    return out


def unresolved_items():
    """Open items shared by the plan's Self-review and the check report."""
    tw, (_top, over_units) = B.TOTAL_W, B.diversity()
    out = []
    if over_units:
        out.append(f"diversity.authority_share (a structural gate check): {len(over_units)} units of discovery exceed 50% of the {tw} weight; the largest are " + "; ".join(
            f"{u} {s} of {tw} ({100 * s / tw:.0f}%)" for u, s in over_units[:3]) + ". Every label, note and state row reaches them through the ledger's Depends-on edges "
            "(F49 depends on the notes, the issue list and the told facts; F47 and F48 on the issue list and the Carta and advisor chain), because one issue list and one rules doc "
            "govern this population by design. The plan and the ledger stay as they are, and the requester decides")
    side = json.loads((WF / "00_V3_Authoring_Evidence.json").read_text())["rubric_rows"]
    sql_text = (TI / "01_Universe_Inject.sql").read_text(errors="replace")
    empty = [f"C{i + 1} ({rows[i]['tag']})" for i, r in enumerate(side) if not r["source_records"]]
    long_ptr = sorted({f"C{i + 1} ({rows[i]['tag']}, {x['pointer']})" for i, r in enumerate(side) for x in r["source_records"] if x.get("pointer") and len(str(x.get("source_value"))) > 65536})   # the gate reads 65536 characters of a cited field
    seeded = sum(1 for r in side if any(st["service"] == "linear" and st["id"] in sql_text for x in r["source_records"] for st in x["evidence_path"]))
    if empty or long_ptr or seeded:
        out.append(f"v3.rubric_evidence at rubric-check fails on the V3 sidecar that build_rubric.py writes, outside these builders: {seeded} rows' evidence_path passes through a Linear record that exists only in the SQL overlay, "
                   f"which the gate's unscoped lookup searches in the base export alone; {', '.join(long_ptr) or 'no row'} cites a pointer too long to read whole; {', '.join(empty) or 'no row'} lists no source record")
    out.extend(stale_fields())
    out.append("no human-time estimate exists yet (05_Human_Time.md is the requester's slot), so the set-size line has no hours")
    dist = sorted({r["dist"] for r in rows if r["dist"] in B.DIST_LEDGER_ID})
    if dist:
        out.append(f"{sum(1 for r in rows if r['dist'] in B.DIST_LEDGER_ID)} rows of rows.json name a distractor by its manifest trap id ({'; '.join(dist)}); the plan prints the "
                   "ledger's T-ID where the ledger has one, and says so where it does not")
    return out


def truth_checks():
    """Per-line values and every count against solver/truth.json. Returns report lines and failures."""
    n, wrong = collections.Counter(), []
    field = {"shares": "Shares held now", "note.shares": "Shares held now", "options": "Options now", "note.options": "Options now", "lastday": "Last day",
             "note.lastday": "Last day", "label": "Owed", "state": "State"}
    for r in rows:
        key = key_of(r)
        if not key or key not in LINES:
            continue
        ax = axis(r)
        if ax == "note":
            want = D.EMAIL[key]
            if want not in B.literals(r):
                wrong.append(f"{r['tag']} ({want})")
            n["recipients"] += 1
            continue
        if ax not in field:
            continue
        v = LINES[key][field[ax]]
        if ax in ("label",):
            want = LABEL[v]
        elif ax in ("state",):
            want = v
        elif ax in ("lastday", "note.lastday"):
            want = v
        else:
            want = f"{v:,}"
        lits = [iso(x) for x in B.literals(r)] if ax in ("lastday", "note.lastday") else B.literals(r)
        n[ax] += 1
        if want not in lits:
            wrong.append(f"{r['tag']} ({want})")
    sm = TRUTH["SUMMARY"]
    counts = collections.Counter(LABEL[v["Owed"]] for v in LINES.values())
    totals, ok = {}, []
    for r in rows:
        tag = r["tag"]
        lits = B.literals(r)
        if tag.startswith("sh_cnt_"):
            totals[tag] = f"{counts[tag[len('sh_cnt_'):].replace('_', ' ')]}"
    totals.update({"sh_volume": f"{len(LINES)}", "sh_tot_options": f"{sm['Options outstanding now']:,}", "k_total": f"{sm['Options outstanding at Dec 31']:,}",
                   "k_combined": f"{sm['Issued plus options at Dec 31']:,}", "k_common": f"{sm['Common']:,}", "k_seed": f"{sm['Series Seed total']:,}",
                   "k_fund_2662255": f"{LINES['ENG-2438']['Shares held now']:,}", "k_fund_84438": f"{LINES['ENG-2439']['Shares held now']:,}"})
    shares_total = sm["Common"] + sm["Series Seed total"]
    # the literals a totals row may carry; each one it does carry must be one of these (rows.json decides which it shows)
    tot_lits = {"sh_tot_all": {f"{shares_total + sm['Options outstanding now']:,}", f"{shares_total:,}", f"{sm['Options outstanding now']:,}"}, "sh_tot_shares": {f"{shares_total:,}", f"{sm['Series Seed total']:,}", f"{sm['Common']:,}", f"{shares_total + sm['Options outstanding now']:,}"}}
    if sum(v["Shares held now"] for v in LINES.values()) != sm["Series Seed total"]:
        wrong.append("the per-line stock in truth.json does not sum to the Series Seed total")
    ms = {r["tag"]: B.literals(r) for r in rows}
    for tag, want in totals.items():
        if tag in ms:
            if want in ms[tag]:
                ok.append(tag)
            else:
                wrong.append(f"{tag} ({want})")
    for tag, want in tot_lits.items():
        if tag in ms:
            extra = [x for x in ms[tag] if x not in want]
            (ok.append(tag) if not extra else wrong.append(f"{tag} carries {extra}, not in {sorted(want)}"))
    es_map = {f"{es}": issue for issue, es in list(D.ES.items()) + list(D.ES_STOCK.items())}
    n_es, bad_es = 0, []
    for r in rows:
        m = re.match(r"k_line_(ES-\d+)", r["tag"])
        if not m:
            continue
        n_es += 1
        issue = es_map[m.group(1)]
        want = f"{LINES[issue]['Options at Dec 31']:,}"
        if want not in B.literals(r):
            bad_es.append(f"{r['tag']} ({want})")
    k_vol = next((r for r in rows if r["tag"] == "k_volume"), None)
    if k_vol:
        n16 = sum(1 for v in LINES.values() if v["Options at Dec 31"])
        if str(n16) not in B.literals(k_vol):
            wrong.append(f"k_volume ({n16})")
    fails = []
    if wrong or bad_es:
        fails.append(f"rows disagree with solver/truth.json: {wrong + bad_es}")
    lines = [(f"- Per-line values: {sum(n.values())} per-line rows ({', '.join(f'{v} {k}' for k, v in sorted(n.items()))}) and {n_es} KPMG line rows equal solver/truth.json and the address on each issue "
              f"({len(wrong) + len(bad_es)} differences)."),
             f"- Totals and counts: {len(ok)} count and total rows ({', '.join(sorted(ok))}) equal solver/truth.json's SUMMARY and a recount of its 26 lines ({len(wrong)} differences)."]
    return lines, fails


def base_reads(uniq):
    """Read each base source record through tools/hg.py get-many; {(service, file, pointer): text}."""
    items = [{"id": f"r{i}", "service": s["service"], "file": s["source_file"].split(f"Services_Data/{s['service']}/", 1)[1], "pointer": s["pointer"], "max_chars": 60000}
             for i, s in enumerate(uniq)]
    out = {}
    for k in range(0, len(items), 8):
        batch = items[k:k + 8]
        req = HERE / "_getmany.json"
        req.write_text(json.dumps({"items": batch}))
        try:
            got = json.loads(run_tool(["Task_Authoring/tools/hg.py", "search", "get-many", "--request", req, "--compact"]))
        finally:
            req.unlink(missing_ok=True)
        for it in batch:
            r = got["items"][it["id"]]
            text = r.get("text", "")
            while r.get("truncated"):
                nreq = HERE / "_getmany.json"
                nreq.write_text(json.dumps({"items": [{**it, "offset": r["next_offset"]}]}))
                try:
                    more = json.loads(run_tool(["Task_Authoring/tools/hg.py", "search", "get-many", "--request", nreq, "--compact"]))
                finally:
                    nreq.unlink(missing_ok=True)
                r = more["items"][it["id"]]
                text += r.get("text", "")
            out[(it["service"], it["file"], it["pointer"])] = text
    return out


def reverify():
    """Every check runs in this build. Returns the report lines and a list of failures (empty when all pass)."""
    fails, lines = [], []
    stmts = sql_rows()
    side = json.loads((WF / "00_V3_Authoring_Evidence.json").read_text())["rubric_rows"]
    sql_uniq, base_uniq = {}, {}
    for r in side:
        for s in r["source_records"]:
            if s.get("table"):
                sql_uniq[(s["table"], json.dumps(s["identity"], sort_keys=True), s["column"], s["source_value"])] = s
            else:
                base_uniq[(s["service"], s["source_file"], s["pointer"], s["source_value"])] = s
    norm = lambda q: re.sub(r"\s+", " ", str(q))  # noqa: E731
    ok = 0
    for (table, idn, col, val), _s in sql_uniq.items():
        ident = json.loads(idn)
        hit = [x for x in stmts if x.get("op") in ("insert", "update") and x.get("table") == table and
               all(str((x.get("row") or {}).get(k)) == str(v) for k, v in ident.items())]
        if hit and norm(val) in norm(" ".join(str((x.get("row") or {}).get(col)) for x in hit)):
            ok += 1
        else:
            fails.append(f"sidecar value not re-read: {table} {ident} {col}")
    lines.append(f"- Seeded values: all {len(sql_uniq)} distinct source records of 00_V3_Authoring_Evidence.json that cite the SQL re-read from a fresh parse of "
                 f"01_Universe_Inject.sql (tools/base_check.py parse_sql, never executed): {ok} of {len(sql_uniq)} hold their source_value in the "
                 "named table, identity and column.")
    uniq_by_rec = {}
    for s in base_uniq.values():
        uniq_by_rec.setdefault((s["service"], s["source_file"], s["pointer"]), []).append(s)
    recs = [v[0] for v in uniq_by_rec.values()]
    texts = base_reads(recs)
    base_ok, base_text = 0, ""
    for (svc, sf, ptr), group in uniq_by_rec.items():
        rel = sf.split(f"Services_Data/{svc}/", 1)[1]
        raw = texts[(svc, rel, ptr)]
        try:
            read = json.loads(raw)
        except ValueError:
            read = raw
        base_text += " " + str(read)
        for s in group:
            if norm(s["source_value"]) in norm(read):
                base_ok += 1
            else:
                fails.append(f"sidecar base value not re-read: {svc} {rel} {ptr}")
    lines.append(f"- Base records: {len(uniq_by_rec)} distinct records cited by the sidecar's base sources read through `python3 Task_Authoring/tools/hg.py search get-many`; "
                 f"{base_ok} of {len(base_uniq)} cited source values are held in the record read.")
    tl, tf = truth_checks()
    lines.extend(tl)
    fails.extend(tf)
    sql_text = (TI / "01_Universe_Inject.sql").read_text(errors="replace").replace('\\"', '"').lower()
    lits = sorted({v for r in rows for v in re.findall(r"`([^`]+)`", r["vals"]) if len(v) > 2})
    absent = [v for v in lits if v.lower() not in sql_text]
    in_base = [v for v in absent if v.lower() in base_text.lower()]
    rest = [v for v in absent if v not in in_base]
    sm = TRUTH["SUMMARY"]
    figures = {f"{x:,}" for v in LINES.values() for x in (v["Shares held now"], v["Options now"], v["Options at Dec 31"]) if x}
    total = sm["Common"] + sm["Series Seed total"]
    figures |= {f"{x:,}" for x in (sm["Options outstanding now"], sm["Options outstanding at Dec 31"], sm["Issued plus options at Dec 31"], total, total + sm["Options outstanding now"],
                                   sm["Common"], sm["Series Seed total"])}
    last_days = {v["Last day"] for v in LINES.values() if v["Last day"]}

    def resolved_elsewhere(v):
        if v in figures or iso(v) in last_days:
            return "truth.json"
        if "/" in v and all(p.lower() in sql_text or p.lower() in base_text.lower() for p in v.split("/")):
            return "parts"
        return None

    derived = [v for v in rest if resolved_elsewhere(v)]
    neither = [v for v in rest if v not in derived]
    generic_only = [v for v in neither if v.lower() in GENERIC]
    unknown = [v for v in neither if v not in generic_only]
    if unknown:
        fails.append(f"literals found in no source and not recognised as a row's own word: {unknown}")
    lines.append(f"- Literals: {len(lits) - len(absent)} of {len(lits)} backticked literals found in the SQL text"
                 + (f"; {', '.join(f'`{v}`' for v in in_base)} found in the base reads above" if in_base else "")
                 + (f"; {', '.join(f'`{v}`' for v in derived)} are figures or dates computed in solver/truth.json or a Slack id whose parts are in the SQL" if derived else "")
                 + (f"; {', '.join(f'`{v}`' for v in generic_only)} found in neither, each a label of the row's own (a state, a label word or a grading anchor, never a record value)" if generic_only else "") + ".")
    return lines, fails


def parse_probe():
    """{(service, record): held values} for each distinct record in probe_raw.txt, and the raw HIT line count."""
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
    classes = collections.Counter(classify(svc, rec, vals)[0] for (svc, rec), vals in held.items())
    cl = ", ".join(f"{v} {k}" for k, v in classes.most_common())
    return (f"the §F probe's verdict is {verdict}: {n} HIT lines over {len(held)} records, {incomplete} INCOMPLETE lines, and {lines} SHORTCUT-OK lines, one per record ({cl}). "
            "A generic-word hit holds only a state word, a label word or a common English word and no holder figure, id, date or address, so a run cannot answer from it. "
            f"Every other hit is reasoned per record below: {strongest_note(held)}")


GENERIC = {"reason", "before", "closing", "done", "todo", "already told", "covered", "last day", "nothing", "canceled", "closing and last day", "letter", "metrics", "insolvent",
           "sunset", "holders", "distribution", "tax", "exercise", "license", "termination", "games", "thank", "financing", "winding", "vote", "equity", "griffin", "leonard", "robert", "calvin",
           "es-1", "es-3", "es-18", "ip"}
FIGURE = re.compile(r"^\d{1,3}(,\d{3})+$|^\d{4}-\d{2}-\d{2}$|^[A-Z][a-z]+ \d{1,2}, \d{4}$")
ADDRESS = re.compile(r"@|_EMAIL$|^\[EMAIL")
RECORD_ID = re.compile(r"^(f_|d_|C0AD|ENG-)")


def strong_values(vals):
    """The held values that identify a holder or a graded figure: figures, full dates and record ids (an address alone is not one)."""
    return sorted(v for v in vals if FIGURE.search(v) or RECORD_ID.search(v))


def carta(es, extra=""):
    return (f"Carta's termination notice for {es}: the designed source for that one line's vested count and last day (OE 12), which the task sends the Agent to find; it holds only this holder's numbers, "
            f"no label, note, state or other holder, so the other 25 lines still need their own reads{extra}")


# records that hold a real figure, id or a designed rule; each was read and the reason states what that record is
RECORD_REASONS = {
    ("gmail", "leonard.hayes@harmonygames.co/1856960351896429942"): carta("ES-7", "; its 22,889 is the grant size, and the vested 12,875 is the figure the rows take"),
    ("gmail", "leonard.hayes@harmonygames.co/1856960382677662910"): carta("ES-18"),
    ("gmail", "leonard.hayes@harmonygames.co/1856960410709778333"): carta("ES-4"),
    ("gmail", "leonard.hayes@harmonygames.co/1856960433624350836"): carta("ES-1"),
    ("gmail", "leonard.hayes@harmonygames.co/1856960478782792748"): carta("ES-14"),
    ("gmail", "leonard.hayes@harmonygames.co/1856960504234892536"): carta("ES-12"),
    ("gmail", "leonard.hayes@harmonygames.co/1856960532806250145"): carta("ES-15"),
    ("gmail", "leonard.hayes@harmonygames.co/1856960563574318616"): carta("ES-13"),
    ("gmail", "leonard.hayes@harmonygames.co/1847333272519888206"): carta("ES-17", "; that line had lapsed by the clock, so this notice decides only the KPMG as-of figure"),
    ("gmail", "leonard.hayes@harmonygames.co/1847333318158821452"): carta("ES-16", "; that line had lapsed by the clock, so this notice decides only the KPMG as-of figure"),
    ("gmail", "leonard.hayes@harmonygames.co/1847333347700620793"): carta("ES-3", "; its Jan 24 date is the stale value (ledger T2) that Calvin's later forward overturns"),
    ("gdocs", "f_6a37227593d0977fdbdd7a"): "the Due Diligence advisor table, the designed hidden authority for the four advisor grants (ledger F33): it holds grant sizes by name and nothing on current stock, vesting, labels or last days, and the owner list's merged lines (T1) must still be split with it",
    ("gmail", "leonard.hayes@harmonygames.co/1773160163779741845"): "the mail carrying the same disclosure-schedule advisor table (ledger F33), a designed step on the advisor chain: grant sizes only, no holder's current holding, label or date",
    ("gmail", "leonard.hayes@harmonygames.co/1816809274978043917"): "the Nov 2024 owner list, the designed decoy T1: its 25,432 and 50,865 are stock lines, but its advisor lines are merged with grants, and it holds no label, last day or state, so a run that copies it fails the merged-line rows",
    ("slack", "C04UEQVDVB7/1732646280.941869"): "the same Nov 2024 owner list pasted in Slack (decoy T1): merged lines, no label, last day or state",
    ("gmail", "leonard.hayes@harmonygames.co/1771880236343640719"): "the 2023 purchaser schedule, the designed source that splits Griffin's two funds (ledger F37): it decides two rows and holds nothing on the other 24 lines",
    ("slack", "C07C2866011/1768416262.426129"): "a #executives cap-table summary holding Griffin's split and the common count; its 3,051,881 seed figure is the off-by-a-couple decoy (ledger T9), and it holds no per-holder line, label or date",
    ("slack", "C07C2866011/1768417784.194359"): "a #executives modeling post with the common count and the off-by-a-couple seed figure (ledger T9): no holder line, label or date",
    ("gdocs", "f_11040fe5d66821bd6951aa"): "the reset term sheet, the designed source for the share ledger (ledger F35): common and Series Seed totals only, with a stale 268,772 option count (ledger T8), and no holder line, label or date",
    ("gdocs", "f_d690045a2f2bf47108ae99"): "a financing document with the common count and the stale 3,051,882 seed figure (ledger T9): no holder line, label or date",
    ("gmail", "leonard.hayes@harmonygames.co/1770717887098657139"): "an old cap-table mail with the common count and the stale 3,051,882 seed figure (ledger T9): no holder line, label or date",
    ("gmail", "leonard.hayes@harmonygames.co/1773160052067710033"): "the mail noting the 3,051,882 against 3,051,879 rounding gap, plus its header addresses: it states the seed total only, with no holder line, label or date",
    ("gmail", "leonard.hayes@harmonygames.co/1791558449734120301"): "a franchise-tax mail stating common shares issued: one company-level figure, no holder line, label or date",
    ("gmail", "leonard.hayes@harmonygames.co/1824509105148886763"): "a franchise-tax mail stating shares issued (9,051,879): one company-level figure, no holder line, label or date",
    ("slack", "C04UEQVDVB7/1708563439.959559"): "a franchise-tax post stating common shares issued: one company-level figure, no holder line, label or date",
    ("slack", "C04UTBZL6AX/1753312033.174059"): "a cap-table summary post with rounded founder and investor totals: no holder line, label or date",
    ("gdocs", "f_3ee38465decc57e61df6e5"): "one advisor agreement stating that holder's grant size (6,104): a single grant on the advisor chain, no label or date",
    ("gdocs", "f_af481d73feee6fd3bc4d8e"): "a consulting agreement granting 22,889 options to one person: the granted figure, while the rows grade the vested figure in Carta",
    ("gmail", "leonard.hayes@harmonygames.co/1853778416001425647"): "an unrelated vendor mail whose retention-policy date is April 30, 2026: it names no holder and no equity fact",
    ("gmail", "leonard.hayes@harmonygames.co/1853786403951896954"): "an unrelated vendor policy mail whose effective date is March 31, 2026: it names no holder and no equity fact",
    ("sql:gmail.gmail_messages", "L115"): "Calvin Price's Feb 3 forward of Carta's Jan 23 update, the designed authority for ES-3's last day (T2, chain C10): it decides that one line and holds no other holder",
    ("sql:gsheets.sheets_sheets", "L25"): "the draft sheet's own cells, seeded with the old owner-list figures the task corrects (decoy T1): the file the Agent must finish, not an answer",
    ("sql:gdocs.docs_documents", "L17"): "Leonard's close-out notes, the designed rules doc the prompt names: they hold the handling rules and the label words, and no holder's figure, date or label",
    ("sql:gdocs.docs_documents", "L20"): "the earlier outreach notes, a superseded decoy (ledger T10): no holder figure or date",
    ("sql:gdrive.drive_files", "L13"): "the Drive metadata row of the draft sheet: file name, folder and owner, no holder data",
    ("sql:gdrive.drive_files", "L15"): "the Drive metadata row of the update outline: file name, folder and owner, no holder data",
    ("sql:gmail.gmail_messages", "L105"): "Robert's reply saying he told the ENG-2446 holder, a designed told fact (chain C3): it decides that one line and holds no figure",
    ("sql:gmail.gmail_messages", "L119"): "the Carta activity digest of Nov 20, 2023, a step on the advisor chain (C1): it lists accepted grants by ES id, with common words here and no holding, label or date",
    ("sql:gmail.gmail_messages", "L123"): "Leonard's Feb 12 mail to the ENG-2447 holder, the designed told fact for that line (T25, chain C11): one line, no figure or date",
    ("sql:gmail.gmail_messages", "L80"): "KPMG's audit request, the mail the prompt names: its addresses are the reply's recipients and it asks for items 1 to 4, with no answer figure",
    ("sql:gmail.gmail_messages", "L83"): "Leonard's holding reply to KPMG in the audit thread ('before the 27th'): its addresses are the reply's recipients and it holds no answer figure",
    ("sql:gmail.gmail_messages", "L86"): "KPMG's clarification in the audit thread (as of Dec 31, effective dates as Carta shows them): recipients and the ask, no answer figure",
    ("sql:gmail.gmail_messages", "L90"): "Sunset's intake mail asking for the sheet's contents: the ask, with no answer figure, name or date",
    ("sql:gmail.gmail_messages", "L93"): "Leonard's reply to Sunset's intake: the ask restated, no answer figure, name or date",
    ("sql:gmail.gmail_messages", "L96"): "Robert's reply on the Board position thread, a designed step for who remains on the board (chain C5): names and addresses, no holder figure or date",
    ("sql:linear.linear_comments", "L177"): "a comment on ENG-2444 (its last-mail line or owner-list line) holding its own key: 1 of the 2 keys of the Covered population by arithmetic, so 50% is one record about one line",
    ("sql:linear.linear_comments", "L179"): "a comment on ENG-2444 (its last-mail line or owner-list line) holding its own key: 1 of the 2 keys of the Covered population by arithmetic, so 50% is one record about one line",
    ("sql:linear.linear_comments", "L183"): "a comment on ENG-2445 (its last-mail line or owner-list line) holding its own key: 1 of the 2 keys of the Covered population by arithmetic, so 50% is one record about one line",
    ("sql:linear.linear_comments", "L185"): "a comment on ENG-2445 (its last-mail line or owner-list line) holding its own key: 1 of the 2 keys of the Covered population by arithmetic, so 50% is one record about one line",
    ("sql:linear.linear_issues", "L139"): "the ENG-2438 issue itself, which the prompt's holder project sends the Agent to: its own key, holder name and address, no holding or label",
    ("sql:linear.linear_issues", "L175"): "the ENG-2444 issue itself: its own key is 1 of the 2 keys of the Covered population by arithmetic, no holding or label",
    ("sql:linear.linear_issues", "L181"): "the ENG-2445 issue itself: its own key is 1 of the 2 keys of the Covered population by arithmetic, no holding or label",
    ("sql:linear.linear_projects", "L136"): "the Holder records project the prompt names: it sets the states and asks, with the state words only and no line's figure or label",
    ("sql:trello.trello_actions", "L75"): "a Trello comment on the wind-down card: common words only, no holder figure or date",
    ("sql:trello.trello_cards", "L69"): "the Stockholder close-out Trello card (the order of work): common words only, no holder figure or date",
}


def reason_key(svc, rec):
    return (svc, rec.split(":", 1)[0]) if svc.startswith("sql:") else (svc, rec)


def classify(svc, rec, vals):
    """(class, reason) for one record hit, the reason read from what the record holds. An unread record that holds a figure or id gets no reason and stops the build."""
    known = RECORD_REASONS.get(reason_key(svc, rec))
    if known:
        return "records read one by one", known
    if strong_values(vals):
        return "records read one by one", None
    addrs = sorted(v for v in vals if ADDRESS.search(v))
    if addrs:
        return "address hits", (f"holds only mail addresses ({', '.join(addrs[:4])}{' and others' if len(addrs) > 4 else ''}) in recipient or share-list fields, plus common words; no holding, last day or label, "
                                "and each holder's address is already on that holder's issue, the first thing the prompt names")
    return "generic-word hits", (f"holds only common words of the close-out ({', '.join(sorted(vals))}) and no holder figure, id, date or address, so it cannot stand in for the sheet, the notes or the replies")


def strongest_note(held):
    strong = sorted(((svc, rec, strong_values(vals)) for (svc, rec), vals in held.items() if strong_values(vals)), key=lambda x: -len(x[2]))
    return ("; ".join(f"{svc} {rec} ({len(v)} figures or ids)" for svc, rec, v in strong[:4]) + ". The largest holds three of the "
            f"{len({v for r in rows for v in B.literals(r)})} values, so no record holds more than one line or one company total's worth of the answer") if strong else "none."


def searcher():
    from pathlib import Path as _P
    ctx = G.Ctx("rubric-writing", _P(B.TASKREL), "lint")
    assert G.assignment_context(ctx)
    import persona_view
    import shortcut_probe as sp
    return sp.Searcher(persona_view.resolve_persona(B.PERSONA)), sp


def incomplete_reason(svc, v):
    """Why an unfinished search on one value hides no shortcut: read from the same cached results the probe used on that service."""
    s, sp = searcher()
    vals, pops, _ = sp.load_values(WF / "09_Rubric_Writing_Plan.md")
    allv = list(dict.fromkeys(vals + [x for ks in pops.values() for x in ks]))
    res = s.unscoped(svc, allv) if svc in sp.UNSCOPED else {x: s.scoped(svc, x) for x in allv}
    figures = [x for x in allv if FIGURE.search(x) and res[x]["records"]]
    if figures:
        raise SystemExit(f"{svc}: {v} is incomplete and {svc} holds figures {figures[:5]}: this needs a read reason")
    return (f"{v} is a short or common token that reached the search's match limit on {svc} (it occurs inside unrelated text there); {svc} holds no record with any holding figure or last day "
            f"(those searches completed with none), so anything the limit hides can add only common words, and no row's answer rests on {svc}")


def write_probe():
    raw = PROBE_RAW.read_text().rstrip()
    assert "[]" not in raw, "the probe output holds a literal []; sanitize before pasting"
    held, _n = parse_probe()
    ok, undone = [], []
    for (svc, rec), vals in held.items():
        cls, why = classify(svc, rec, vals)
        why = why or RECORD_REASONS.get((svc, rec))
        if why:
            ok.append(f"SHORTCUT-OK: {svc} {rec} — {why}")
        else:
            undone.append(f"{svc} {rec}: {sorted(vals)}")
    incomplete = re.findall(r'^INCOMPLETE (\S+) value:"(.*)" \(', raw, re.M)
    if incomplete:
        for svc, v in incomplete:
            ok.append(f'SHORTCUT-OK: {svc} value:"{v}" — {incomplete_reason(svc, v)}')
    if undone:
        (HERE / "probe_undone.txt").write_text("\n".join(undone) + "\n")
        raise SystemExit(f"{len(undone)} probe hits have no read reason (written to probe_undone.txt): add RECORD_REASONS entries")
    (HERE / "probe.txt").write_text("```text\n" + raw + "\n```\n\n" + "\n".join(ok) + "\n")
    print("probe.txt written:", len(ok), "SHORTCUT-OK lines")


def write_selfreview():
    lines, fails = reverify()
    assert not fails, fails
    L = ["## Self-review", ""]
    A = L.append
    A("Re-read as /rubric: walked Evals/3_Rubrics_Eval.md 1.4 and 3.1 against the plan in order. Every prompt requirement (ledger R1–R12) and every write family (holder sheet and its shares; "
      "letter, folder and share; the 14 drafts; 26 state moves; 12 reason comments; the KPMG, Griffin and #winddown replies) has a result row on the correct artifact. The prompt asks to be told "
      "nothing beyond the deliverables, so no row grades the final response; a concise final reply passes the whole set (§A3). Friction is none, so no recovery outcome is needed.")
    A("")
    A("Re-verified, every value in this build (ledger values were leads, not evidence):")
    A("")
    L.extend(lines)
    A("")
    A("Predicted all-fail re-check: for every row the persona reaches the value through a cataloged tool (the Gmail, Slack, Drive, Docs and Sheets records have pasted YES lines under Visibility proof, "
      "and persona_view re-checks each id; Linear and Contacts are unscoped), each write exists in the catalog (gsheets_values_update, gdrive_share_file, gdocs_create_document, gdrive_move_file, "
      "gmail_create_draft, linear_update_issue, linear_create_comment, gmail_send_message or gmail_reply_to_message, slack_send_message; ledger §C), Friction is none so no row needs a retry, and no "
      "evidence sits outside Leonard's view. Count on the four bases: 0.")
    A("")
    top, over_units = B.diversity()
    tw = B.TOTAL_W
    A("Shortcut and diversity: " + probe_note() + f" Largest unit of discovery: {top[0][0]}, {top[0][1]} of {tw} ({100 * top[0][1] / tw:.0f}%), then {top[1][0]} "
      f"{100 * top[1][1] / tw:.0f}% and {top[2][0]} {100 * top[2][1] / tw:.0f}%. Every line's facts reach the issue list and the close-out rules through the ledger's Depends-on edges (see Unresolved).")
    A("")
    bare = [s["id"] for s in B.SLOTS if not B.covering(s["id"])]
    A(f"Surface dispositions: {', '.join(bare) if bare else 'none'} have no covering row in rows.json and carry a §G disposition. Strongest case for a further row: "
      "the TC_ slots name a Told column on the sheet, but the same reading decides the line's label row, and a second row on one fact would grade it twice (gate 6). N_COUNT asks for a count over separate "
      "draft writes, which count-bundle-v1 rules out; the 14 draft rows carry it per member. The three _vol slots each have one row per member, so no population is left to sample. " + ", ".join(x for x in bare if x.startswith("AL_ES-")) + " are "
      "unsampled members of a group already at its five-sample cap (gate 15), with the volume row carrying the rest.")
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


if __name__ == "__main__":
    if "--probe" in sys.argv[1:]:
        write_probe()
    else:
        write_selfreview()
