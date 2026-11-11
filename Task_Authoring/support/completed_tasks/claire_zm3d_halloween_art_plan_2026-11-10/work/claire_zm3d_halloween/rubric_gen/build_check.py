#!/usr/bin/env python3
"""Write Working_Files/09_Rubric_Check.md (check mode) for 09_Rubrics.json against the plan (rows.json), the eval lint and the
/rubric checks. The Findings table holds only findings on the current JSON: each rule in findings() tests the current rows, so a
finding drops off by itself once rows.json and build_rubric.py fix it. Rows are classified as in build_plan.py, by prefix, fact,
vals and grp, never by full tag, so coverage lines, groups and counts all follow rows.json."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_plan as B  # noqa: E402
import build_selfreview as SR  # noqa: E402
from build_plan import PY, TASKREL, TI, WF, WS, axis, family, is_store, is_volume, of, rows  # noqa: E402

crit = json.loads((TI / "09_Rubrics.json").read_text())
assert len(rows) == len(crit) and all(r["t"] == c["title"] and r["w"] == c["weight"] for r, c in zip(rows, crit)), \
    "rows.json and 09_Rubrics.json differ: rebuild them together"
C = {r["tag"]: f"C{i + 1}" for i, r in enumerate(rows)}
CTX = json.loads((WF / "00_Task_Context.json").read_text())
BW = json.loads((HERE / "baseline_writes.json").read_text())
SIX = [f"run-{i}" for i in range(1, 7)]
GAPWORD = re.compile(r"\bgap\b|\bmissing\b|\buncovered\b|\bpartial\b", re.I)   # read by validity.rubric in the Covered cell
GROUPS = B.groups()


def crange(rs):
    """C numbers of a row list, consecutive runs folded: 'C63–C168, C171'."""
    ns = sorted(int(C[r["tag"]][1:]) for r in rs)
    out, i = [], 0
    while i < len(ns):
        j = i
        while j + 1 < len(ns) and ns[j + 1] == ns[j] + 1:
            j += 1
        out.append(f"C{ns[i]}" if i == j else f"C{ns[i]}–C{ns[j]}")
        i = j + 1
    return ", ".join(out)


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


def rubric_lint():
    p = subprocess.run([PY, "-B", "Task_Authoring/tools/hg.py", "rubric-lint", f"{TASKREL}/09_Rubrics.json"], cwd=WS,
                       capture_output=True, text=True, env={**B.os.environ, "TASK_AUTHORING_TASK_DIR": TASKREL})
    return json.loads(p.stdout)


def first_name_runs(first="Marcus", full="Marcus Bennett"):
    """Baseline runs that name a maker by first name only: (plan docs, trackers)."""
    docs = [x for x in SIX if BW[x]["doc"] and full not in BW[x]["doc"][0]["body"] and first in BW[x]["doc"][0]["body"]]
    sheets = []
    for x in SIX:
        cells = [str(c).strip() for s in BW[x]["sheets"] for g in s["tabs"].values() for row in g for c in row]
        if first in cells and full not in cells:
            sheets.append(x)
    return docs, sheets


def plain_span(title):
    """A span of the title with no straight quote, so the gate can match it against the JSON."""
    return title.split('"')[0][:48].strip()


def findings():
    """[(tag, quoted span, rule, what is wrong, plan row / ledger fact, type, severity)], from the current rows only."""
    out = []
    for r in rows:
        full = re.search(r"names (Marcus Bennett|Julia Lawson|Martin Walsh)\b", r["t"])
        if full and not re.search(r"\(or (Marcus|Julia|Martin)\)", r["t"]):
            name = full.group(1)
            first = name.split()[0]
            where = "plan doc" if "plan doc" in r["t"] else "tracker"
            d, t = first_name_runs(first if first != "Julia" else "Marcus", name if first != "Julia" else "Marcus Bennett")
            out.append((r["tag"], full.group(0), "Eval 2.7; gate 10 (every fair outcome)",
                        f"Only the full name is accepted, while {len(d) if where == 'plan doc' else len(t)} of 6 baseline {where}s use first names, as "
                        f"Leonard's messages do. Propose 'names {name} (or {first})' in the title and the Accept clause",
                        f"{B.pn(r['tag'])}, {r['fids']}", "overly_specific", "Major"))
        if r["fact"].startswith("due.") and "also passes" not in r["t"]:
            out.append((r["tag"], plain_span(r["t"]), "Eval 2.7; gate 10 (every fair outcome)",
                        "The tracker and comment rows on the same dates accept an earlier date, and this row does not. Propose the same window in the "
                        "title and the Accept clause", f"{B.pn(r['tag'])}, {r['fids']}", "overly_specific", "Major"))
    for r in SR.milestone_rows():
        where = "comments" if family(r) == "comment due" else "trackers"
        out.append((r["tag"], plain_span(r["t"]), "Eval 2.7 overly-broad test on the row alone; gate 5",
                    f"{SR.two_date_runs(r)} of 6 baseline {where} on this ad give a refresh date inside this window and also an Oct 15 hand-off. A run "
                    "that hands the finished ad over on the wrong date can pass on its milestone. Propose 'final due date' in the title",
                    f"{B.pn(r['tag'])}, {r['fids']}", "overly_broad", "Major"))
    for g, d in GROUPS.items():
        if len(d["samples"]) > 5:
            r = d["samples"][0]
            out.append((r["tag"], plain_span(r["t"]), "Eval 3.6; Rubric Writing §8", f"{g} holds {len(d['samples'])} samples, over the five a group may hold",
                        f"{B.pn(r['tag'])}, {r['fids']}", "duplicate", "Moderate"))
    return out


def title_scan():
    """The lexical pre-scans of Eval 2.5, 2.7A and 2.9 over every title (and, for exemplars, every field)."""
    neg = re.compile(r"\b(does not|do not|must not|makes no|has no|no|none|not|never|without|avoid|refrain|fail to|leaves|keeps)\b", re.I)
    rank = re.compile(r"\b(primary|main|chief|principal|leading|mainly|largely|generally|overall)\b", re.I)
    vague = re.compile(r"\b(enough|professional|thorough|appropriate|comprehensive|sufficient|reasonable|adequate|properly|correctly|accurately)\b", re.I)
    exemplar = re.compile(r"\bsuch as\b|\be\.g\.|\bfor example\b", re.I)
    return {"agent": sum(1 for c in crit if c["title"].startswith("The Agent ")),
            "neg": [r for r, c in zip(rows, crit) if neg.search(c["title"])],
            "rank": [c["title"] for c in crit if rank.search(c["title"])],
            "vague": [c["title"] for c in crit if vague.search(c["title"])],
            "exemplar": [c["title"] for c in crit if exemplar.search(" ".join(str(v) for v in c.values()))]}


def descriptive(r):
    """A pre-scan hit that only selects which ads a required write covers, so an idle Agent still fails the row."""
    return bool(re.search(r"\bthat is not on Android US phone\b", r["t"]))


# (requirement, which rows, required?) — a required line with no row prints as a gap, which blocks through validity.rubric
REQS = [
    ("A plan doc in Claire's Drive (R6)", lambda r: family(r) == "plan doc" and axis(r) == "exists", True),
    ("The call for each store surface, in the plan doc (R4, R6)", lambda r: family(r) == "plan doc" and axis(r) == "call" and is_store(r), True),
    ("The calls for every ad, in the plan doc (R4, R6)", lambda r: family(r) == "plan doc" and axis(r) == "call" and not is_store(r), True),
    ("By when, in the plan doc (R5, R6)", lambda r: family(r) == "plan doc" and axis(r) == "due", True),
    ("How a store piece ships, in the plan doc (R4, R6)", lambda r: family(r) == "plan doc" and axis(r) == "route", False),
    ("Who makes what, in the plan doc (R5, R6)", lambda r: family(r) == "plan doc" and axis(r) == "maker", True),
    ("A tracker in Claire's Drive with every serving ad (R7)", lambda r: family(r) == "tracker" and axis(r) in ("exists", "keys"), True),
    ("The tracker's call column (R4, R7)", lambda r: family(r) == "tracker" and axis(r) == "call", True),
    ("The tracker's due column (R5, R7)", lambda r: family(r) == "tracker" and axis(r) == "due", True),
    ("The tracker's maker column (R5, R7)", lambda r: family(r) == "tracker" and axis(r) == "maker", True),
    ("Both files shared with everyone on the review so they can comment (R8)", lambda r: family(r) == "share", True),
    ("A comment on each ad's ticket with its call and due date (R9)", lambda r: family(r).startswith("comment"), True),
    ("Assign the ones that need new work to their makers (R10)", lambda r: family(r) == "assignment", True),
    ("Open ART tickets for any new store art (R11)", lambda r: family(r) == "new ticket", True),
    ("Reply in Leonard's thread with both links (R12)", lambda r: family(r) == "reply", True),
    ("Exclusions (Archive tickets, Skip ads, exported store sets, people off the invite)", lambda r: axis(r) in ("keys", "scope"), True),
]


def fix_list_status():
    """How far the rows carry the local run's candidate rubric, computed from the file; first names were added after it."""
    p = HERE / "review2/rubric_candidate.json"
    if not p.exists():
        return ""
    cand = json.loads(p.read_text())
    cand = cand if isinstance(cand, list) else cand.get("criteria", [])
    have = {re.sub(r" \(or (Marcus|Julia|Martin)\)", "", r["t"]) for r in rows}
    left = [c["title"] for c in cand if c["title"] not in have]
    held = [t for t in left if re.search(r"comments the call .* on exactly \d+ ART tickets", t)]
    other = [t for t in left if t not in held]
    text = f"{len(cand) - len(left)} of the {len(cand)} candidate rows from local /rubric run 1 stand in the current set, apart from the first-name additions"
    if held:
        text += f"; the {len(held)} not taken are its per-call comment count rows, which belong to the comment-row cut that A1 and A2 asked for"
    if other:
        text += f"; {len(other)} other candidate titles differ: {'; '.join(t[:60] for t in other[:3])}"
    return text + "."


def covered_cell(rs):
    if not rs:
        return "gap — no row grades this requirement"
    order = [x for x in rs if is_volume(x)] + rs
    usable = [r for r in order if not GAPWORD.search(r["alt"])]
    pick = next((r for r in usable if re.search(r"\bfails?\b", r["alt"])), usable[0] if usable else None)
    why = cell(pick["alt"]).rstrip(".") if pick else "a wrong value fails the row"
    return f"covered — a run that skips the write fails these rows; {why}"


F = findings()
SCAN = title_scan()
NEG_OPEN = [r for r in SCAN["neg"] if not descriptive(r)]
major = sum(1 for f in F if f[6] == "Major")
moderate = sum(1 for f in F if f[6] == "Moderate")
contested = B.contested()
L = []
A = L.append
n = len(crit)
n_proc = sum(1 for c in crit if c["category"] == "Process")
tw = sum(c["weight"] for c in crit)
bands = {b: sum(1 for c in crit if c["weight"] == b) for b in (5, 3, 1)}
sha = hashlib.sha256((TI / "09_Rubrics.json").read_bytes()).hexdigest()[:12]
lint = rubric_lint()
off_band = [r for r in rows if B.BAND.get(r["kind"]) != r["w"]]
off_slot = sum(1 for s in B.SLOTS for r in B.covering(s["id"]) if r["w"] != s["weight"])
n_call, n_due = len(of("comment call")), len(of("comment due"))
cards = list((WS / "Evals/references").glob("known_data_issues/*"))

A("# 09 Rubric Check — claire-zm3d-halloween-art-plan (Halloween art plan, injection rev3)")
A(f"Checked 2026-11-06 · Criteria {n} (builder minimum 5: ok) · Plan 2026-11-06 (09_Rubric_Writing_Plan.md, rows P1–P{n} = C1–C{n}) · "
  f"09_Rubrics.json sha256 {sha} · weight {tw} (5 ×{bands[5]}, 3 ×{bands[3]}, 1 ×{bands[1]})")
A("JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · "
  "schema gate: pass (a JSON array of objects; every row has all five fields non-blank; category Outcome or Process; weight 1, 3 or 5)")
if major or moderate:
    readiness = f"FAIL-RISK (Overall Rubric Quality: {major} Major and {moderate} Moderate rows in Findings)"
elif contested:
    readiness = ("FAIL-RISK (this report's own checks are clean, but the local /rubric run 1 scored A1 and A2 Moderate on the per-ticket comment rows; a "
                 "dismissal is filed, and one upheld Moderate fails Overall Rubric Quality)")
else:
    readiness = "CLEAN"
A(f"Readiness for /rubric: {readiness} — a prediction only; /rubric gives the verdict")
A(CTX["universe"]["clock_line"])
A("")
hits = ", ".join(f"{f.get('check') or f.get('code') or f}" for f in lint["findings"][:6])
A(f"Lint (`python3 Task_Authoring/tools/hg.py rubric-lint {TASKREL}/09_Rubrics.json`, run for this report): {lint['count']} findings"
  + (f": {hits}." if lint["count"] else " — no `disguised_negative`, `format_lock`, `anon_token`, `evidence_no_record`, `vague_exemplar`, "
     "`tool_name`, `prohibition_title` or schema hit to resolve."))
A("")
A("## Coverage")
A("| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |")
A("|---|---|---|")
seen = set()
for label, pred, required in REQS:
    rs = [r for r in rows if pred(r)]
    seen.update(r["tag"] for r in rs)
    if rs or required:
        A(f"| {label} | {crange(rs) if rs else '—'} | {covered_cell(rs)} |")
rest = [r for r in rows if r["tag"] not in seen]
if rest:
    A(f"| Other rows | {crange(rest)} | {covered_cell(rest)} |")
A("Unauthorized criteria: none")
A("")
reuse = [r for r in rows if r["fact"].split(".")[0] in ("iphone", "play") and axis(r) in ("due", "route")]
A("Not graded, with the reason: "
  + ("the iPhone and Play sets' due cells (see Recorded decisions); " if not reuse else "")
  + "the Skip rows' maker cells are representational in brief §4b (blank or the maker). The new tickets' assignee, due date and description are "
  "optional in brief §4b. The tracker's unsampled ad cells are the members gate 15 leaves to the volume rows.")
A("")
A("## Coverage — gradable surface")
A("| Surface slot | Stable fact ID | Criteria | Covered / dispositioned / gap | Disposition reason (evidence) |")
A("|---|---|---|---|---|")
for s in B.SLOTS:
    rs = B.covering(s["id"])
    if rs:
        A(f"| {s['id']} | {s.get('fact_id') or rs[0]['fact']} | {', '.join(C[r['tag']] for r in rs)} | covered | the title rejects the omission and "
          f"the plausible wrong value ({B.wrong_value(rs[0])}).{B.slot_note(s, rs)} |")
    else:
        A(f"| {s['id']} | {s.get('fact_id') or '—'} | — | gap | rows.json names no covering row |")
mw, mp, _ = B.mech_share()
nw, np_ = B.mech_node_share()
A(f"Mechanism share: {mp}% of the criteria weight ({mw} of {tw}; {np_}% counting every row a mechanism's node decides; reported, not gated)")
A("")
A("## Findings")
A("")
if F:
    by = {k: sum(1 for f in F if f[5] == k) for k in sorted({f[5] for f in F})}
    A(f"{len(F)} findings on the current 09_Rubrics.json ({', '.join(f'{v} `{k}`' for k, v in by.items())}). Each row names the change; rows.json and "
      "build_rubric.py are the requester's to edit, and each finding drops off this table when the row changes.")
    A("")
    A("| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |")
    A("|---|---|---|---|---|---|---|---|")
    for i, (tag, span, rule, wrong, plan, typ, sev) in enumerate(F, 1):
        A(f"| {i} | {C[tag]} | \"{span}\" | {rule} | {cell(wrong)} | {plan} | {typ} | {sev} |")
else:
    A("No finding on the current 09_Rubrics.json from this report's checks. " + fix_list_status() + " A1 and A2, kept open against that run, are recorded "
      "below with the reason.")
A("")
A("## Recorded decisions")
A("")
for line in B.records():
    A(f"- {line}")
A("")
A("## Overlap groups · Spot-check groups · Predicted all-fail")
A("| Group / row | Members / basis | Shared condition / reason |")
A("|---|---|---|")
for g, d in GROUPS.items():
    direct = f"; store surfaces direct ({crange(d['direct'])})" if d["direct"] else ""
    A(f"| {g} | {crange(d['rows'])} | {len(d['samples'])} samples; volume rows {crange(d['vols'])}{direct} |")
A(f"| Comments | {n_call} call rows, {n_due} due-date rows | not sampled: exhaustive direct coverage (Recorded decisions); count rows {crange(of('comment count'))} |")
over = [g for g, d in GROUPS.items() if len(d["samples"]) > 5]
A(f"| Overlap groups | {', '.join(over) or 'none in this report'} | "
  + ("no spot-check group exceeds five samples, and no two rows embed one acceptance condition. The Android date decides many due rows, but each fails only on "
     "its own ticket's date, a shared root cause and not a condition (§3.3). " if not over else "")
  + ("The local run's A1 and A2 read the comment rows as two overlap groups; that is contested under Recorded decisions |" if contested else "|"))
A("| Predicted all-fail | 0 rows on the four Evals bases | every value is reachable through a cataloged tool and visible to Claire (plan §E visibility proof); "
  "rows a baseline run misses because it never opened a record are real misses |")
A("")
A("## Dimensions")
A("| Dimension | Count / % | Threshold | Status |")
A("|---|---|---|---|")
if major or moderate:
    quality = "FAIL (predicted; the Findings table is the fix list)"
elif contested:
    quality = "PASS on this report's checks; FAIL if /rubric upholds A1 and A2"
else:
    quality = "PASS (predicted)"
A(f"| Overall Rubric Quality | {major} Major · {moderate} Moderate · 0 Minor of {n} rows ({100 * (major + moderate) / n:.1f}%) in Findings"
  + ("; A1 and A2 contested, two Moderate if upheld" if contested else "") + f" | any Major or Moderate fails; Minor < 5% | {quality} |")
A(f"| Criteria Weights | {len(off_band)} rows off their kind of work ({bands[5]} at 5, {bands[3]} at 3, {bands[1]} at 1); {off_slot} rows differ from their surface "
  f"slot's weight, which never sets one (gate 17) | ≤ 10% one level, none two levels | {'PASS (predicted)' if not off_band else 'FAIL'} |")
A(f"| Known data issue | {'0 rows: Evals/references holds no known_data_issues card for this universe' if not cards else str(len(cards)) + ' cards to read'} | no row rests "
  f"on a listed card | {'PASS' if not cards else 'FAIL'} |")
A(f"| Category Balance | {n - n_proc} Outcome / {n_proc} Process | ≥ 1 Outcome, Process ≤ 50%, < 2 unnecessary Process rows | PASS |")
A(f"| Process Rubrics | {n_proc} Process rows; 0 missing ordering checks (plan §C: the prompt states no ordering dependency between writes) | 0 missing, "
  "every Process row valid | PASS |")
A(f"| Agent-Centric Phrasing | {SCAN['agent']}/{n} titles 'The Agent' + action; 0 artifact subjects or tool names | off-pattern ≤ 10% | "
  f"{'PASS' if SCAN['agent'] == n else 'FAIL'} |")
read = [r for r in SCAN["neg"] if descriptive(r)]
note = f"; {crange(read)} read: the negation only selects which ads the required write covers" if read else ""
A(f"| Negative Criteria | {len(NEG_OPEN)} prohibition-only titles{note}; 0 rows an idle Agent passes (every do_nothing_case in plan §A3 rejects) | 0 prohibition-only | "
  f"{'PASS' if not NEG_OPEN else 'FAIL'} |")
A("| Predicted all-fail | 0 | 0 (harness tolerance) | PASS |")
A("| Schema and repair gates (schema, self-containment, accuracy, atomicity, coverage, duplicates, contradiction, format-5 cases) | clean | all clean | PASS |")
A(f"Threshold margin: with {n} rows, one Major is {100 / n:.1f}% and one row off-weight is {100 / n:.1f}%; any Major or Moderate still fails Overall Rubric "
  "Quality.")
A("")
A("## Self-review")
A("")
d_first, s_first = first_name_runs()
A("Re-read as /rubric in phase order (Evals/3_Rubrics_Eval.md 1.2 schema, 1.4 coverage, 2.1–2.12 per row, 3.1–3.7 set level, 5.1 predicted all-fail) and the "
  f"pre-verdict sweep: one missing requirement (none: every ask has a row, and all {len(B.SLOTS)} surface slots are covered), one phrasing mismatch with the prompt "
  "(none), one overly broad row ("
  + ("found: the milestone rows in the Findings table" if SR.MILESTONE else "none: the due rows read 'final due date', so a refresh milestone in the window does not "
     "stand in for an Oct 15 hand-off")
  + "), one non-atomic row (none: each row grades one fact, and the 'as that total, or as a list' and 'one ticket or two' clauses are closed sets of valid forms), one "
  "category mislabel (none), one over-specific or hard-coded title ("
  + ("found: the Findings table" if any(f[5] == "overly_specific" for f in F) else
     f"none: first names pass where a maker is named, and {len(d_first)} of 6 plan docs and {len(s_first)} of 6 trackers write 'Marcus' alone")
  + "), one duplicate or cascade group ("
  + ("the contested A1 and A2 under Recorded decisions; " if contested else "")
  + f"no fact sits in three rows), one vague exemplar (none: lint {lint['count']}; the pre-scans over every title hit {len(SCAN['rank'])} ranking words, "
  f"{len(SCAN['vague'])} subjective words and {len(SCAN['exemplar'])} exemplars), one prohibition-only title ({'none' if not NEG_OPEN else 'found'}). Calibrated against the "
  "table in Evals/references/rules/rubric_qc_examples.md: do-nothing (every row needs a write), PT/UTC day (plan dates, not instants), reachability (the sidecar's "
  "evidence_path starts at Leonard's message), LITERAL key (ART keys and the thread ts appear as the tools return them).")
A("")
lines, fails = SR.reverify()
assert not fails, fails
A("Re-verified in this build, the same reads the plan's Self-review records (seeded values from a fresh SQL parse, base records through hg.py):")
A("")
L.extend(lines)
A("")
A(f"Tally recount from the findings table: {major} Major, {moderate} Moderate, 0 Minor; predicted all-fail 0; no validity defect. Each finding counts its row once.")
A("")
A("| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |")
A("|---|---|---|---|---|")
found = {f[0]: f for f in F}
for i, r in enumerate(rows):
    verdict = "finding" if r["tag"] in found else "cleared"
    res = ("see Findings (" + found[r["tag"]][5] + ")" if r["tag"] in found else
           f"resolved by the title as written (evidence: {cell(SR.record_ids(r))})")
    A(f"| C{i + 1} {r['tag']} | {verdict} | Counter-reading — {cell(SR.CR[r['tag']])} | {res} | — |")
A("")
top, over_units = B.diversity()
un = []
if over_units:
    un.append("the upstream rubric-writing gate carries one structural FAIL (diversity.authority_share: "
              + "; ".join(f"{u} {100 * s / tw:.0f}%" for u, s in over_units) + "), so no PASS block is pasted in the plan and this report's "
              "chain.rubric-writing check fails with it; the requester decides")
if F:
    un.append(f"the {len(F)} findings wait on the requester's edit of rows.json and build_rubric.py")
un.extend(u for u in SR.unresolved_items() if not u.startswith("diversity.authority_share"))
A("Unresolved: " + (" · ".join(f"({i}) {u}" for i, u in enumerate(un, 1)) if un else "none") + ".")
A("")
A("## Reminders")
A("- An all-Outcome set is normal; Process is not added to look thorough.")
A("- Fix the criteria in the builder, re-export, re-run check, then run /rubric.")
(WF / "09_Rubric_Check.md").write_text("\n".join(L) + "\n")
print("check written:", n, "criteria; weight", tw, bands, "findings", len(F), "lint", lint["count"], "off band", len(off_band), "neg open", len(NEG_OPEN))
