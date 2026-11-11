#!/usr/bin/env python3
"""Write selfreview.md (the plan's Self-review) from rows.json, a fresh re-read of the records and the probe output.

    build_selfreview.py          re-verify every value, write selfreview.md
    build_selfreview.py --probe  turn probe_raw.txt (real shortcut_probe.py output) into probe.txt: the output verbatim in a
                                 fence, then one SHORTCUT-OK line per record hit, its reason read from that record; an
                                 unclassified hit stops the build instead of getting a stock reason

Values are re-read here, never copied: seeded values from a fresh parse of 01_Universe_Inject.sql (never executed), base
records through tools/hg.py, per-line figures, buckets and bank names against solver/truth.json, build costs recomputed from
truth.json's lines, and revenue recomputed from the warehouse export (hg.py get, paged, summed with Decimal). A value that
disagrees stops the build; a stale field outside the JSON is listed under Unresolved.
Rows are classified as in build_plan.py, by prefix, fact, vals and grp, never by full tag.
Run build_plan.py after this one, since the plan embeds selfreview.md and probe.txt."""
import collections
import json
import re
import sys
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_plan as B  # noqa: E402
from build_plan import ENG_LINE, G, LINES, P, TI, WF, family, key_of, rows, run_tool  # noqa: E402
from base_check import parse_sql  # noqa: E402

PROBE_RAW = HERE / "probe_raw.txt"
BETS = {"Do": "Domino Delights", "ZM": "ZM", "Co": "Combo Fighter"}


def record_ids(r, n=2):
    """The first n record pointers of a row's evidence, before its Accept clause."""
    src = r["ev"].split("Accept:")[0]
    out = []
    for m in G.OPAQUE.finditer(src):
        x = m.group(0).rstrip(".,);'")
        if x not in out:
            out.append(x)
    return "; ".join(out[:n]) or r["fids"]


def wrong_reading(r):
    """The strongest plausible wrong answer against the title alone, from what the row names."""
    alt = r["alt"]
    if re.search(r"\bfails?\b", alt):
        return alt
    fam = family(r)
    lits = "/".join(B.literals(r)) or "the named value"
    if fam == "sheet cell":
        return f"{alt} A figure other than {lits} in that cell fails, because the title names the exact value and the line by ENG id and account ending."
    if fam == "sheet setup" or fam == "sheet share":
        return f"{alt} A run that skips this fails it."
    if fam == "reason comment":
        return f"{alt} A comment that omits this reason, or a comment on another issue, fails it."
    if fam == "reply":
        return f"{alt} A reply that leaves this out fails it."
    return f"{alt} A wrong value fails it, since the title names {lits}."


# rows where the counter-reading needs a sentence the row's own fields do not hold: (tag, test on the current title, text); a text prints only while its test holds, so a reworded row drops it
EXTRA_CR = [
    ("cell_jpm", lambda t: t.count(" column") == 1 and "Domino Delights column" in t, "One cell of the line (Domino Delights, where the 4,000.00 notice's date falls); the other cells are left ungraded, so a run that files the 4,000.00 under another column passes this row and is caught only by the bucket row and the build total."),
    ("cell_jpm", lambda t: t.count(",") >= 4 and "Company columns" in t, "Four cells of one line, tested as one fact (the line carries no spending): an attribute of one record, not four independently graded facts (Eval 3 §2.2 exception)."),
    ("cell_oleg", lambda t: "Domino Delights column" in t, "One cell of the line (the wire's date falls in Domino Delights); a run that files the 125.00 under another bet passes this row and is caught only by the reason comment."),
    ("bkt_lauren", lambda t: True, "Weighted 1 as a lookup: Leonard's note on ENG-2455 states the bucket outright since the rev6 note ('so she’s marketing, not build'); the surface slot X8 says 5 because it predates that note, and the surface never sets a weight (gate 17)."),
    ("rev_Do", lambda t: "on the brought-in line" in t, "§4b places brought-in figures anywhere on the sheet; the title's 'brought-in line' is read as any labelled line."),
    ("rev_hold", lambda t: True, "Brief §4b says a Combo Fighter figure is outside acceptance and 'nothing grades it (NB-26)', while this row fails a Combo Fighter figure: the row grades the method's hold ('Leave Combo Fighter’s revenue off for now, on the page'), not whether Combo Fighter sold, so NB-26 is not breached, but the requester should confirm against the §4b line (Unresolved)."),
    ("r_hold", lambda t: True, "Same §4b tension as the held-back sheet row: the row grades the method's hold ('and when you tell me'), never whether Combo Fighter sold; flagged for the requester (Unresolved)."),
    ("r_build_Do", lambda t: True, "Weighted 5 as multi-source, the same fact as the sheet's build cost row (two rows are legal under gate 6); a reviewer could read the reply's restatement as lighter work, as surface R1 does (3); recorded under Unresolved."),
    ("r_build_ZM", lambda t: True, "Same weight question as the Domino Delights reply row."),
    ("r_build_Co", lambda t: True, "Same weight question as the Domino Delights reply row."),
]


def counter_reading(r):
    """(a) a valid answer that could fail, (b) a wrong answer that could pass, each resolved from the row's own records."""
    why = r["why"].rstrip(".")
    extra = "".join(f" {text}" for tag, test, text in EXTRA_CR if tag == r["tag"] and test(r["t"]))
    return (f"(a) a valid run could differ in form: {r['valid']} passes ({'; '.join(r['acc'])}) · (b) {wrong_reading(r)} Reason: {why}.{extra} Evidence {record_ids(r)}; {r['fids']}")


CR = {r["tag"]: counter_reading(r) for r in rows}


def sql_rows():
    return parse_sql((TI / "01_Universe_Inject.sql").read_text(errors="replace"))


def snow_sums():
    """Lifetime revenue per game, summed with Decimal from REVENUE_DAILY in the export, read through hg.py get (paged)."""
    text, offset = "", 0
    while True:
        got = json.loads(run_tool(["Task_Authoring/tools/hg.py", "search", "get", "snowflake", "--file", "snowflake.json", "--pointer", "/tables/12/rows", "--offset", offset, "--max-chars", 60000, "--compact"]))
        text += got["text"]
        if not got.get("truncated"):
            break
        offset = got["next_offset"]
    data = json.loads(text)
    tot = collections.defaultdict(Decimal)
    for row in data:
        tot[row["game_id"]] += Decimal(str(row["total_revenue_usd"]))
    return {k: f"{v:,.2f}" for k, v in tot.items()}, len(data)


SNOW = None


def snow():
    global SNOW
    if SNOW is None:
        SNOW = snow_sums()
    return SNOW


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
            f"{u} {s} of {tw} ({100 * s / tw:.0f}%)" for u, s in over_units[:3]) + ". Every sheet and Linear row reaches them through the ledger's Depends-on edges: F73 and F70 depend on F68, whose Depends-on lists every per-account notice fact (F32 to F53) and the method doc F2, and F8 is the project's issue list. "
            "One issue list, one method doc and one notice population govern the whole sheet by design, and even with the derived rows' F-ids stripped the method doc and the issue list stay over 50%, so the plan cannot meet this check without a ledger or task-design change; the requester decides")
    side = json.loads((WF / "00_V3_Authoring_Evidence.json").read_text())["rubric_rows"]
    sql_text = (TI / "01_Universe_Inject.sql").read_text(errors="replace")
    empty = [f"C{i + 1} ({rows[i]['tag']})" for i, r in enumerate(side) if not r["source_records"]]
    long_ptr = sorted({f"C{i + 1} ({rows[i]['tag']}, {x['pointer']})" for i, r in enumerate(side) for x in r["source_records"] if x.get("pointer") and len(str(x.get("source_value"))) > 65536})   # the gate reads 65536 characters of a cited field
    seeded = sum(1 for r in side if any(st["service"] == "linear" and st["id"] in sql_text for x in r["source_records"] for st in x["evidence_path"]))
    if empty or long_ptr or seeded:
        out.append(f"v3.rubric_evidence at rubric-check: {seeded} rows' evidence_path passes through a Linear record that exists only in the SQL overlay, "
                   f"which the gate's unscoped lookup searches in the base export alone; {', '.join(long_ptr) or 'no row'} cites a pointer too long to read whole; {', '.join(empty) or 'no row'} lists no source record")
    bad_end = [f"C{i + 1}" for i, r in enumerate(side) if any(x.get("evidence_path") and (x["evidence_path"][-1].get("service"), x["evidence_path"][-1].get("id")) != (x.get("service"), x.get("id")) for x in r["source_records"])]
    if bad_end:
        out.append(f"v3.rubric_evidence at rubric-check blocks on the V3 sidecar build_rubric.py writes, outside these builders: {len(bad_end)} rows ({', '.join(bad_end[:12])}{' and others' if len(bad_end) > 12 else ''}) have a source record whose evidence_path does not end at the cited record; 00_V3_Authoring_Evidence.json is the requester's to fix")
    out.extend(stale_fields())
    hold = [r["tag"] for r in rows if r["tag"] in ("rev_hold", "r_hold")]
    if hold:
        out.append(f"brief §4b says of the Combo Fighter figure 'nothing grades it (NB-26)', while rows {', '.join(hold)} fail 11.75 or any Combo Fighter revenue figure: the rows grade the method's hold, not whether Combo Fighter sold, and need the requester's call")
    rep = [r["tag"] for r in rows if r["tag"].startswith("r_build_")]
    if rep:
        out.append(f"rows {', '.join(rep)} carry weight 5 (multi-source) as the same fact as the sheet's build-cost rows, while surface R1 says 3 (interpretation); weights follow the kind of work (gate 8), but a reviewer may read the reply's restatement as lighter")
    return out


def truth_checks():
    """Per-line values and every total against solver/truth.json and the warehouse export. Returns report lines and failures."""
    n, wrong = collections.Counter(), []
    money = lambda x: f"{x:,.2f}"  # noqa: E731
    build = {b: sum(Decimal(str(v[b])) for v in LINES.values() if v["Bucket"] == "Build") for b in ("Domino Delights", "ZM", "Combo Fighter")}
    if len(LINES) != 22:
        wrong.append(f"truth.json holds {len(LINES)} lines, not 22")
    for r in rows:
        t, lits, key = r["tag"], B.literals(r), key_of(r)
        if t == "sh_volume":
            n["volume"] += 1
            if "22" not in lits:
                wrong.append("sh_volume (22)")
        elif t.startswith("build_") or t.startswith("r_build_"):
            bet = BETS[t.rsplit("_", 1)[1]]
            n["build costs"] += 1
            if money(build[bet]) not in lits:
                wrong.append(f"{t} (truth {money(build[bet])})")
        elif t in ("rev_Do", "rev_ZM", "r_rev_Do", "r_rev_ZM", "rev_hold", "r_hold"):
            game = "domino_delights" if t.endswith("Do") else "zombie_match_3d" if t.endswith("ZM") else "combo_fighter"
            n["revenue"] += 1
            if snow()[0][game] not in lits:
                wrong.append(f"{t} (warehouse {snow()[0][game]})")
        elif key:
            line = LINES[ENG_LINE[key]]
            if t in ("cell_jpm", "cell_oleg"):
                cols = re.findall(r"Domino Delights|ZM|Combo Fighter|Company", r["t"].split(" line")[0])
                n["zero lines"] += 1
                if any(line[c] != 0 for c in cols) or "0" not in lits:
                    wrong.append(f"{t} (truth {[line[c] for c in cols]})")
            elif t == "cell_martin":
                n["currency"] += 1
                if line["Company"] != "1,999.00 BGN" or "1,999.00 BGN" not in lits:
                    wrong.append(f"{t} (truth {line['Company']})")
            elif t.startswith(("cell_", "co_", "bet_")):
                m = re.search(r"in the (Domino Delights|ZM|Combo Fighter|Company) column", r["t"])
                n["figures"] += 1
                if not m or money(line[m.group(1)]) not in lits:
                    wrong.append(f"{t} (truth {line[m.group(1)] if m else '?'})")
            elif t.startswith("bkt_"):
                n["buckets"] += 1
                want = "Own transfer" if line["Bucket"] == "Not a cost" else line["Bucket"]
                if want not in lits or (t == "bkt_jpm") != (line["Bucket"] == "Not a cost"):
                    wrong.append(f"{t} (truth {line['Bucket']})")
            elif t.startswith("bank_"):
                n["bank names"] += 1
                if line["Name on the bank"] not in lits:
                    wrong.append(f"{t} (truth {line['Name on the bank']})")
            elif t.startswith("c_") or t.startswith("o_ENG"):
                n["reason comments"] += 1
                if "reason_comment" not in line["groups"] or key not in lits:
                    wrong.append(f"{t} (truth groups {line['groups']})")
            elif t.startswith("done_"):
                n["done moves"] += 1
                if key not in lits:
                    wrong.append(f"{t} ({key})")
    reason_keys = sorted(k for k, v in ENG_LINE.items() if "reason_comment" in LINES[v]["groups"])
    commented = sorted(key_of(r) for r in rows if r["tag"].startswith("c_"))
    if commented != reason_keys:
        wrong.append(f"reason-comment rows {commented} differ from truth.json's group {reason_keys}")
    done_keys = sorted(key_of(r) for r in rows if r["tag"].startswith("done_"))
    if done_keys != sorted(ENG_LINE):
        wrong.append("the Done rows are not one per issue ENG-2438 to ENG-2459")
    fails = [f"rows disagree with solver/truth.json or the warehouse: {wrong}"] if wrong else []
    lines = [f"- Per-line and total values: {sum(n.values())} rows ({', '.join(f'{v} {k}' for k, v in sorted(n.items()))}) equal solver/truth.json, the build costs recomputed from its Build lines "
             f"({', '.join(f'{k} {money(v)}' for k, v in build.items())}) and REVENUE_DAILY recomputed from the export ({snow()[1]:,} rows through `python3 Task_Authoring/tools/hg.py search get snowflake --file snowflake.json --pointer /tables/12/rows`, paged, summed with Decimal: "
             f"{', '.join(f'{k} {v}' for k, v in sorted(snow()[0].items()))}); {len(wrong)} differences. The five reason-comment rows equal truth.json's reason_comment group; the Done rows are the 22 issues."]
    return lines, fails


def base_reads(uniq):
    """Read each base source record through tools/hg.py get-many; {(service, file, pointer): text}."""
    items = [{"id": f"r{i}", "service": s["service"], "file": s["source_file"].split(f"Services_Data/{s['service']}/", 1)[1], "pointer": s["pointer"], "max_chars": 60000}
             for i, s in enumerate(uniq)]
    out = {}
    for k in range(0, len(items), 8):
        batch = items[k:k + 8]
        req = HERE / "_getmany.json"   # overwritten on each read and left in place
        req.write_text(json.dumps({"items": batch}))
        got = json.loads(run_tool(["Task_Authoring/tools/hg.py", "search", "get-many", "--request", req, "--compact"]))
        for it in batch:
            r = got["items"][it["id"]]
            text = r.get("text", "")
            while r.get("truncated"):
                nreq = HERE / "_getmany.json"
                nreq.write_text(json.dumps({"items": [{**it, "offset": r["next_offset"]}]}))
                more = json.loads(run_tool(["Task_Authoring/tools/hg.py", "search", "get-many", "--request", nreq, "--compact"]))
                r = more["items"][it["id"]]
                text += r.get("text", "")
            out[(it["service"], it["file"], it["pointer"])] = text
    return out


GENERIC = {"done", "after", "link", "new spreadsheet", "own transfer", "build", "marketing", "company", "name on the bank", "to fill in"}


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
    figures = {f"{x:,.2f}" for v in LINES.values() for x in (v["Domino Delights"], v["ZM"], v["Combo Fighter"], v["Company"], v["paid"], v["notices_sum"]) if isinstance(x, (int, float)) and x}
    figures |= {f"{sum(Decimal(str(v[b])) for v in LINES.values() if v['Bucket'] == 'Build'):,.2f}" for b in ("Domino Delights", "ZM", "Combo Fighter")} | set(snow()[0].values())
    figures |= {v["Company"] for v in LINES.values() if isinstance(v["Company"], str)}   # the BGN line, kept as text in truth.json

    def resolved_elsewhere(v):
        return "figure" if v in figures or v.replace("$", "").replace("K", "") in figures else None

    derived = [v for v in rest if resolved_elsewhere(v)]
    neither = [v for v in rest if v not in derived]
    generic_only = [v for v in neither if v.lower() in GENERIC]
    unknown = [v for v in neither if v not in generic_only]
    if unknown:
        fails.append(f"literals found in no source and not recognised as a row's own word: {unknown}")
    lines.append(f"- Literals: {len(lits) - len(absent)} of {len(lits)} backticked literals found in the SQL text"
                 + (f"; {', '.join(f'`{v}`' for v in in_base)} found in the base reads above" if in_base else "")
                 + (f"; {', '.join(f'`{v}`' for v in derived)} are figures computed in solver/truth.json or the warehouse sums" if derived else "")
                 + (f"; {', '.join(f'`{v}`' for v in generic_only)} found in neither, each a label of the row's own (a state, a bucket word or a grading anchor, never a record value)" if generic_only else "") + ".")
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
            "A generic-word or address hit holds only common words of the task or a founder's mail address and no rubric figure, id or bank name, so a run cannot answer from it. "
            f"Every other hit is reasoned per record below: {strongest_note(held)}")


FIGURE = re.compile(r"^\d[\d,]*\.\d{2}$|^\d{1,3}(,\d{3})+$|^\d{4}-\d{2}-\d{2}$|^\$\d")
ADDRESS = re.compile(r"@|_EMAIL$|^\[EMAIL")
GENERIC_PROBE = {"done", "after", "link", "new spreadsheet", "build", "marketing", "company", "note", "payee", "bucket", "zm"}   # common words that hold no answer on their own

RECORD_REASONS = {}   # filled from probe_reasons.json, keyed "service record" to a reason read from that record
if (HERE / "probe_reasons.json").exists():
    RECORD_REASONS = {tuple(k.split(" ", 1)): v for k, v in json.loads((HERE / "probe_reasons.json").read_text()).items()}


def strong_values(vals):
    """The held values that identify a payee or a graded figure: everything but the common words and mail addresses."""
    return sorted(v for v in vals if v.lower() not in GENERIC_PROBE and not ADDRESS.search(v))


def reason_key(svc, rec):
    return (svc, rec.split(":", 1)[0]) if svc.startswith("sql:") else (svc, rec)


def classify(svc, rec, vals):
    """(class, reason) for one record hit, the reason read from what the record holds. An unread record that holds a figure or id gets no reason and stops the build."""
    known = RECORD_REASONS.get(reason_key(svc, rec)) or RECORD_REASONS.get((svc, rec))
    if known:
        return "records read one by one", known
    if strong_values(vals):
        return "records read one by one", None
    addrs = sorted(v for v in vals if ADDRESS.search(v))
    words = sorted(v for v in vals if not ADDRESS.search(v))
    if addrs:
        return "address hits", (f"of the answer values it holds only the mail addresses {', '.join(addrs)} and the common words {', '.join(words) or 'none'}: no figure, file id, issue key or bank name from the rubric, so it cannot stand in for the sheet or the reply")
    return "generic-word hits", (f"of the answer values it holds only the common words {', '.join(words)}: no figure, file id, issue key, bank name or address from the rubric, so it cannot stand in for the sheet, the comments or the reply")


def strongest_note(held):
    strong = sorted(((svc, rec, strong_values(vals)) for (svc, rec), vals in held.items() if strong_values(vals)), key=lambda x: -len(x[2]))
    return ("; ".join(f"{svc} {rec} ({len(v)} figures or ids)" for svc, rec, v in strong[:4]) + ". The largest holds "
            f"{len(strong[0][2])} of the {len({v for r in rows for v in B.literals(r)})} values, so no record holds more than one payee's or one line's worth of the answer") if strong else "none."


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
    return (f"{v} is a short or common token that reached the search's match limit on {svc} (it occurs inside unrelated text there); {svc} holds no record with any graded figure "
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
    for svc, v in incomplete:
        ok.append(f'SHORTCUT-OK: {svc} value:"{v}" — {incomplete_reason(svc, v)}')
    if undone:
        (HERE / "probe_undone.txt").write_text("\n".join(undone) + "\n")
        raise SystemExit(f"{len(undone)} probe hits have no read reason (written to probe_undone.txt): add entries to probe_reasons.json")
    (HERE / "probe.txt").write_text("```text\n" + raw + "\n```\n\n" + "\n".join(ok) + "\n")
    print("probe.txt written:", len(ok), "SHORTCUT-OK lines")


def write_selfreview():
    lines, fails = reverify()
    assert not fails, fails
    L = ["## Self-review", ""]
    A = L.append
    A("Re-read as /rubric: walked Evals/3_Rubrics_Eval.md 1.4 and 3.1 against the plan in order. Every prompt requirement (ledger R1–R12) and every write family (the new sheet in Robert's Drive and its two shares; "
      "the 22 payee lines with buckets, bet columns, the Company column, build costs and revenue; the five reason comments; the 22 Done moves; the #winddown reply with costs, revenue, deck changes and the link) has a result row on the correct artifact. The final response is ungraded: the prompt's 'reply to him in #winddown' is a Slack write, "
      "so a concise chat answer passes the whole set (§A3). Friction is none, so no recovery outcome is needed.")
    A("")
    A("Re-verified, every value in this build (ledger values were leads, not evidence):")
    A("")
    L.extend(lines)
    A("")
    A("Predicted all-fail re-check: for every row the persona reaches the value through a cataloged tool (the Gmail, Slack, Drive, Docs, Sheets and Slides records have pasted YES lines under Visibility proof, "
      "and persona_view re-checks each id; Linear, Contacts, Trello and Snowflake are unscoped), each write exists in the catalog (gsheets_create_spreadsheet, gsheets_values_update, gdrive_share_file, "
      "linear_create_comment, linear_update_issue, slack_send_message; ledger §C), Friction is none so no row needs a retry, and no evidence sits outside Robert's view. Count on the four bases: 0.")
    A("")
    top, over_units = B.diversity()
    tw = B.TOTAL_W
    A("Shortcut and diversity: " + probe_note() + f" Largest unit of discovery: {top[0][0]}, {top[0][1]} of {tw} ({100 * top[0][1] / tw:.0f}%), then {top[1][0]} "
      f"{100 * top[1][1] / tw:.0f}% and {top[2][0]} {100 * top[2][1] / tw:.0f}%. Every line's facts reach the issue list, the method doc and the notice population through the ledger's Depends-on edges (see Unresolved).")
    A("")
    bare = [s for s in B.SLOTS if not B.covering(s["id"])]
    samples = [s for s in bare if s["role"] == "sample"]
    A(f"Surface dispositions: {', '.join(s['id'] for s in bare) if bare else 'none'} have no covering row and carry a §G disposition. Strongest case for a further row: B4 is a total, but the prompt and the method ask for a Company column and the OE's sheet write grades no Company total, "
      "so a Company-total row would be a count over separate items (count-bundle-v1, release b9281224) with no prompt span behind it (gate 3). "
      + (f"{', '.join(f'{s['id']} ({s['selector'][1]} {s['selector'][2]})' for s in samples)} are ordinary per-payee cells; each is a sum of notices with no adjustment of its own, the dollar-figure group already holds its five samples (gate 15), and the sheet volume row carries the rest. " if samples else "")
      + "S6 is covered by the sheet's volume row, stated by issue range, because a Build-row count of nine would be a bare count over separate cells; D4 is covered by the reply content rows, each naming its #winddown reply, since a bare 'replied' row duplicates them.")
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
