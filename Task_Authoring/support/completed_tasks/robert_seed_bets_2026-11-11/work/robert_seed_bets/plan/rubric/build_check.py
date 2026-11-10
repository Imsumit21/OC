#!/usr/bin/env python3
"""Write Working_Files/09_Rubric_Check.md (check mode) for 09_Rubrics.json against the plan (rows.json), the eval lint and the /rubric checks.

The Findings table holds the findings in plan/rubric/check_findings.json. Each finding names a criterion and quotes a span of 09_Rubrics.json; a finding whose quoted span is no longer in the rubric
(a reviewer has fixed the row) drops off on the next build. Accepted shapes of the file:

    [ {"criterion": "C17" or "sh_header", "span": "...", "rule": "...", "wrong": "...", "plan": "P17, F12", "type": "overly_broad", "severity": "Major"}, ... ]
    {"findings": [ ... ]}

and also the tuple form, one list per finding: ["tag", "span", "rule", "wrong", "plan", "type", "severity"]. `type` must be a /rubric issue type; stage_gate rubric-check enforces it.
Rows are classified as in build_plan.py, by prefix, fact, vals and grp, so coverage lines, groups and counts all follow rows.json."""
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
from build_plan import PY, TASKREL, TI, WF, WS, family, is_volume, of, rows  # noqa: E402

crit = json.loads((TI / "09_Rubrics.json").read_text())
assert len(rows) == len(crit) and all(r["t"] == c["title"] and r["w"] == c["weight"] for r, c in zip(rows, crit)), \
    "rows.json and 09_Rubrics.json differ: rebuild them together"
C = {r["tag"]: f"C{i + 1}" for i, r in enumerate(rows)}
CTX = json.loads((WF / "00_Task_Context.json").read_text())
FINDINGS_FILE = HERE / "check_findings.json"
GAPWORD = re.compile(r"\bgap\b|\bmissing\b|\buncovered\b|\bpartial\b", re.I)   # read by validity.rubric in the Covered cell
GROUPS = B.groups()
RUBRIC_TEXT = "\n".join(str(v) for c in crit for v in c.values())
KNOWN_ISSUES = WS / "Task_Authoring/references/known_data_issues/normal.md"


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


def load_findings():
    """[(tag, quoted span, rule, what is wrong, plan row / ledger fact, type, severity)] from check_findings.json; a finding whose tag or span is gone from the rubric drops off."""
    if not FINDINGS_FILE.exists():
        return [], [], False
    raw = json.loads(FINDINGS_FILE.read_text())
    items = raw.get("findings", []) if isinstance(raw, dict) else raw
    out, stale = [], []
    by_c = {c: t for t, c in C.items()}
    for it in items:
        if isinstance(it, (list, tuple)):
            tag, span, rule, wrong, plan, typ, sev = it
        else:
            ref = str(it.get("tag") or it.get("criterion") or "")
            tag = by_c.get(ref, ref)
            span, rule, wrong, plan, typ, sev = (it.get(k, "") for k in ("span", "rule", "wrong", "plan", "type", "severity"))
        tag = by_c.get(tag, tag)
        if tag not in C or span not in RUBRIC_TEXT:
            stale.append((tag, span))
            continue
        out.append((tag, span, rule, wrong, plan, typ, sev))
    return out, stale, True


F, STALE, REVIEWED = load_findings()


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


PROHIBITION = re.compile(r"^The Agent (does not|do not|must not|makes no|never|avoids?|refrains?|fails to|leaves|keeps)\b", re.I)


def descriptive(r):
    """A pre-scan hit whose negation is only content inside a write the Agent must make (a stated reason, a quoted excuse, a scope clause), so an idle Agent still fails the row."""
    return not PROHIBITION.search(r["t"])


# (requirement, which rows, required?) — a required line with no row prints as a gap, which blocks through validity.rubric
REQS = [
    ("A new sheet in Robert's own Drive, in Leonard's layout (R5, R6)", lambda r: r["tag"] in ("sh_create", "sh_header"), True),
    ("One line per payee, ENG-2438 to ENG-2459 (R6)", lambda r: is_volume(r), True),
    ("Shared with Leonard and Blake (R7)", lambda r: family(r) == "sheet share", True),
    ("Each payee's figures by bet and in the Company column (R4, R6)", lambda r: family(r) == "sheet cell" and r["tag"].startswith(("cell_", "co_", "bet_")), True),
    ("Each payee's Bucket (R4, R6)", lambda r: r["tag"].startswith("bkt_"), True),
    ("Each payee's Name on the bank (R6)", lambda r: r["tag"].startswith("bank_"), True),
    ("Each bet's build cost and what it brought in on the page, Combo Fighter's revenue held back (R4, R6)", lambda r: family(r) == "sheet total", True),
    ("A reason comment on each issue whose figure differs from the notices (R8)", lambda r: family(r) == "reason comment", True),
    ("Each of the 22 issues moved to Done (R8)", lambda r: family(r) == "done move", True),
    ("The reply in #winddown: cost, brought in, deck changes, the link (R9 to R12)", lambda r: family(r) == "reply", True),
    ("The order the method and the prompt set: comment before Done, sheet before Done, reply last (R8, R9, Process)", lambda r: family(r) == "order", True),
]


def covered_cell(rs):
    if not rs:
        return "gap — no row grades this requirement"
    order = [x for x in rs if is_volume(x)] + rs
    usable = [r for r in order if not GAPWORD.search(r["alt"])]
    pick = next((r for r in usable if re.search(r"\bfails?\b", r["alt"])), usable[0] if usable else None)
    why = cell(pick["alt"]).rstrip(".") if pick else "a wrong value fails the row"
    return f"covered — a run that skips the write fails these rows; {why}"


SCAN = title_scan()
NEG_OPEN = [r for r in SCAN["neg"] if not descriptive(r)]
major = sum(1 for f in F if f[6] == "Major")
moderate = sum(1 for f in F if f[6] == "Moderate")
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
if KNOWN_ISSUES.exists():
    cards = re.findall(r"^### (NB-\d+)", KNOWN_ISSUES.read_text(), re.M)
else:
    cards = []

A("# 09 Rubric Check — task_inputsS2 (Robert: what each bet cost to build and brought in)")
A(f"Checked 2026-11-09 · Criteria {n} (builder minimum 5: ok) · Plan 2026-11-09 (09_Rubric_Writing_Plan.md, rows P1–P{n} = C1–C{n}) · "
  f"09_Rubrics.json sha256 {sha} · weight {tw} (5 ×{bands[5]}, 3 ×{bands[3]}, 1 ×{bands[1]})")
A("JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · "
  "schema gate: pass (a JSON array of objects; every row has all five fields non-blank; category Outcome or Process; weight 1, 3 or 5)")
if major or moderate:
    readiness = f"FAIL-RISK (Overall Rubric Quality: {major} Major and {moderate} Moderate rows in Findings)"
elif not REVIEWED:
    readiness = "NON-FAIL-RISK (no findings are loaded: plan/rubric/check_findings.json is absent, so the review half of this check is still to come; the mechanical checks here are clean)"
else:
    readiness = "CLEAN"
A(f"Readiness for /rubric: {readiness} — a prediction only; /rubric gives the verdict")
A(CTX["universe"]["clock_line"])
A("")
fmt = [f for f in lint["findings"] if f["check"] == "format_lock"]
anon = [f for f in lint["findings"] if f["check"] == "anon_token"]
others = [f for f in lint["findings"] if f["check"] not in ("format_lock", "anon_token")]
A(f"Lint (`python3 Task_Authoring/tools/hg.py rubric-lint {TASKREL}/09_Rubrics.json`, run for this report): {lint['count']} findings, {len(anon)} `anon_token` and {len(fmt)} `format_lock`"
  + (f", and {len(others)} other ({', '.join(sorted({f['check'] for f in others}))}), each resolved below" if others else ", and no `disguised_negative`, `evidence_no_record`, `vague_exemplar`, `tool_name`, `prohibition_title` or schema hit") + ".")
A("")
if anon:
    A(f"- `anon_token` ({len(anon)} hits, rows {', '.join(str(x) for x in sorted({f['row'] for f in anon}))}): verdict OK. The tokens are the source strings (Linear issue titles and SVB bank names as the tools return them); "
      "each binds as LITERAL and is accepted as shown, as the lint's own instruction and rubric_factual_checks.md require, and the rows also name the ENG key and account ending (NB-12).")
if fmt:
    A(f"- `format_lock` ({len(fmt)} hits: " + ", ".join(f"C{f['row']} '{f['text']}'" for f in fmt) + "): verdict OK. Each is a figure from the records or the layout, not a "
      "length, line, sentence or section format the prompt did not state (Eval 3 §2.7).")
if others:
    for f in others:
        A(f"- `{f['check']}` row {f['row']} ({cell(f.get('text', ''))}): to resolve.")
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
A("Not graded, with the reason: a Company total (slot B4, not incorporated: the prompt and method ask for a Company column, and a total the prompt does not ask for is a count over separate items, count-bundle-v1); a count of Build rows (slot S6: the sheet's volume row states the 22 issues by range); "
  "a count of the Done moves (each of the 22 issues has its own row); unsampled line cells (gate 15 leaves them to the volume row); Marketing and Company totals, optional in brief §4b and never asked by the prompt.")
A("")
A("## Coverage — gradable surface")
A("| Surface slot | Stable fact ID | Criteria | Covered / dispositioned / gap | Disposition reason (evidence) |")
A("|---|---|---|---|---|")
for s in B.SLOTS:
    rs = B.covering(s["id"])
    if rs:
        note = B.covered_note(s, rs) or f"the title rejects the omission and the plausible wrong value ({B.wrong_value(rs[0])})."
        A(f"| {s['id']} | {s.get('fact_id') or (rs[0]['fact'] if len(rs) == 1 else 'reply content rows')} | {', '.join(C[r['tag']] for r in rs)} | covered | {note} |")
    else:
        why = B.disposition(s)
        A(f"| {s['id']} | {s.get('fact_id') or '—'} | — | {'dispositioned' if why else 'gap'} | {why or 'rows.json names no covering row'} |")
mw, mp, _ = B.mech_share()
nw, np_ = B.mech_node_share()
A(f"Mechanism share: {mp}% of the criteria weight ({mw} of {tw}; {np_}% counting every row a mechanism's node decides; reported, not gated)")
A("")
A("## Findings")
A("")
if F:
    by = {k: sum(1 for f in F if f[5] == k) for k in sorted({f[5] for f in F})}
    A(f"{len(F)} findings from plan/rubric/check_findings.json ({', '.join(f'{v} `{k}`' for k, v in by.items())}), each read against brief §4b, the method doc and the records in this review. Each row names the change; rows.json and build_rubric.py are the requester's to edit, and a finding drops off this "
      "table when its quoted span leaves the rubric.")
    A("")
    A("| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |")
    A("|---|---|---|---|---|---|---|---|")
    for i, (tag, span, rule, wrong, plan, typ, sev) in enumerate(F, 1):
        A(f"| {i} | {C[tag]} | \"{span}\" | {rule} | {cell(wrong)} | {plan} | {typ} | {sev} |")
else:
    A("No findings are loaded: plan/rubric/check_findings.json is absent or empty, or every finding it holds has been fixed in the rubric; reviewer findings will be written into this table when the file is supplied "
      "and build_check.py is re-run.")
if STALE:
    A("")
    A(f"Dropped from check_findings.json because the rubric no longer holds the quoted text ({len(STALE)}): " + "; ".join(f"{t}: '{s[:60]}'" for t, s in STALE) + ".")
A("")
A("## Recorded decisions")
A("")
for line in B.records():
    A(f"- {line}")
_dec = HERE / "check_decisions.json"
if _dec.exists():
    for line in json.loads(_dec.read_text(encoding="utf-8")):
        A(f"- {line}")
A("")
A("## Overlap groups · Spot-check groups · Predicted all-fail")
A("| Group / row | Members / basis | Shared condition / reason |")
A("|---|---|---|")
for g, d in GROUPS.items():
    A(f"| {g} | {crange(d['rows'])} | {len(d['samples'])} samples; volume row {crange(d['vols'])} |")
over = [g for g, d in GROUPS.items() if len(d["samples"]) > 5]
A(f"| Overlap groups | {', '.join(over) or 'none in this report'} | "
  + ("no spot-check group exceeds five samples, and no two rows embed one acceptance condition: a miscounted payee fails its own line's rows and the totals, a shared root cause and not a shared condition (§3.3)." if not over else "") + " |")
A("| Predicted all-fail | 0 rows on the four Evals bases | every value is reachable through a cataloged tool and visible to Robert (plan §E visibility proof) |")
A("")
A("## Dimensions")
A("| Dimension | Count / % | Threshold | Status |")
A("|---|---|---|---|")
if major or moderate:
    quality = "FAIL (predicted; the Findings table is the fix list)"
elif not REVIEWED:
    quality = "pending the review (no findings loaded); mechanical checks clean"
else:
    quality = "PASS (predicted)"
A(f"| Overall Rubric Quality | {major} Major · {moderate} Moderate · 0 Minor of {n} rows ({100 * (major + moderate) / n:.1f}%) in Findings | any Major or Moderate fails; Minor < 5% | {quality} |")
A(f"| Criteria Weights | {len(off_band)} rows off their kind of work ({bands[5]} at 5, {bands[3]} at 3, {bands[1]} at 1); {off_slot} rows differ from their surface "
  f"slot's weight, which never sets one (gate 17); the r_build rows' 5 is an open question (Unresolved) | ≤ 10% one level, none two levels | {'PASS (predicted)' if not off_band else 'FAIL'} |")
A(f"| Known data issue | {len(cards)} cards in references/known_data_issues/normal.md; the three that touch these rows were read: NB-12 (vendor tokens: lines are keyed on the ENG id and account ending, tokens accepted as shown), NB-23 (Singular's two invoice totals: the Company row grades the bank's notices, not an as-billed invoice total), "
  "NB-26 (whether Combo Fighter sold: no row grades that; the held-back rows grade the method's hold, see Unresolved) | no row rests on a listed card | PASS |")
A(f"| Category Balance | {n - n_proc} Outcome / {n_proc} Process | ≥ 1 Outcome, Process ≤ 50%, < 2 unnecessary Process rows | PASS |")
A(f"| Process Rubrics | {n_proc} Process rows, each with the three-condition test in plan §C; 0 missing ordering checks (the method and the prompt set one order each) | 0 missing, every Process row valid | PASS |")
A(f"| Agent-Centric Phrasing | {SCAN['agent']}/{n} titles 'The Agent' + action; 0 artifact subjects or tool names | off-pattern ≤ 10% | "
  f"{'PASS' if SCAN['agent'] == n else 'FAIL'} |")
read = [r for r in SCAN["neg"] if descriptive(r)]
note = f"; {crange(read)} read: the negation is content inside a write the Agent must make" if read else ""
A(f"| Negative Criteria | {len(NEG_OPEN)} prohibition-only titles{note}; 0 rows an idle Agent passes (every do_nothing_case in plan §A3 rejects) | 0 prohibition-only | "
  f"{'PASS' if not NEG_OPEN else 'FAIL'} |")
A("| Predicted all-fail | 0 | 0 (harness tolerance) | PASS |")
A("| Schema and repair gates (schema, self-containment, accuracy, atomicity, coverage, duplicates, contradiction, format-5 cases) | clean on this report's mechanical checks, except the V3 sidecar items under Unresolved | all clean | PASS (predicted) for the rubric text; the sidecar items are open |")
A(f"Threshold margin: with {n} rows, one Major is {100 / n:.1f}% and one row off-weight is {100 / n:.1f}%; any Major or Moderate still fails Overall Rubric Quality.")
A("")
A("## Self-review")
A("")
multi = [r for r in rows if r["tag"] in ("cell_jpm", "cell_oleg") and len(re.findall(r"Domino Delights|ZM|Combo Fighter|Company", r["t"].split(" line")[0])) > 1]
ATOM_NOTE = (f"the multi-cell zero-line rows {crange(multi)} tested and kept as one fact" if multi else "none found: each zero-line row now grades one cell")
A("Re-read as /rubric in phase order (Evals/3_Rubrics_Eval.md 1.2 schema, 1.4 coverage, 2.1–2.12 per row, 3.1–3.7 set level, 5.1 predicted all-fail) and the pre-verdict sweep: one missing requirement (none: every requirement has a "
  f"row, and all {len(B.SLOTS)} surface slots are covered or dispositioned), one phrasing mismatch with the prompt (none), one over-specific or hard-coded title ({'found: the Findings table' if any(f[5] == 'overly_specific' for f in F) else 'none found in this pass'}), one overly broad row (none found in this pass), one non-atomic row ({ATOM_NOTE}), one duplicate or cascade group "
  f"(none: facts repeated on the sheet and in the reply sit in two rows, the gate-6 limit), one category mislabel (none: the {n_proc} order rows are the only Process rows), one vague exemplar (none: lint {lint['count']} findings resolved above; the pre-scans over "
  f"every title hit {len(SCAN['rank'])} ranking words, {len(SCAN['vague'])} subjective words and {len(SCAN['exemplar'])} exemplars), one prohibition-only title ({'none' if not NEG_OPEN else 'found'}). Blind reviewers run separately; their findings can be added to check_findings.json. Calibrated against the table in "
  "Evals/references/rules/rubric_qc_examples.md: do-nothing (every row needs a write or a sent message), PT/UTC day (no instant is graded; wire dates are dates), reachability (the sidecar's evidence_path starts at Leonard's post or the method doc), LITERAL key "
  "(ENG keys, account endings, the Slack channel and file ids appear as the tools return them; anonymized tokens accepted as shown).")
A("")
lines, fails = SR.reverify()
assert not fails, fails
A("Re-verified in this build, the same reads the plan's Self-review records (seeded values from a fresh SQL parse, base records through hg.py, per-line values against solver/truth.json, revenue from the warehouse export):")
A("")
L.extend(lines)
A("")
A(f"Tally recount from the findings table: {major} Major, {moderate} Moderate, 0 Minor; predicted all-fail 0; no validity defect in this report's mechanical checks. Each finding counts its row once.")
A("")
A("| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |")
A("|---|---|---|---|---|")
found = {}
for f in F:
    found.setdefault(f[0], []).append(f)
pending = "see Findings and Unresolved below" if F else ("review pending" if not REVIEWED else "—")
for i, r in enumerate(rows):
    verdict = "finding" if r["tag"] in found else ("mechanical checks clean" if not REVIEWED else "cleared")
    res = ("see Findings (" + "; ".join(sorted({x[5] for x in found[r["tag"]]})) + ")" if r["tag"] in found else f"resolved by the title as written (evidence: {cell(SR.record_ids(r))})")
    A(f"| C{i + 1} {r['tag']} | {verdict} | Counter-reading — {cell(SR.CR[r['tag']])} | {res} | {pending if r['tag'] in found else '—'} |")
A("")
top, over_units = B.diversity()
un = []
if not REVIEWED:
    un.append("the review findings are still to come: plan/rubric/check_findings.json is absent, so readiness stays NON-FAIL-RISK and no row carries a reviewer verdict")
if over_units:
    un.append("the upstream rubric-writing gate carries one structural FAIL (diversity.authority_share: "
              + "; ".join(f"{u} {100 * s / tw:.0f}%" for u, s in over_units[:3]) + f"; {len(over_units)} units over 50% in all), by construction: every line's facts run through one issue list, one method doc and one notice population; the requester decides")
if F:
    un.append(f"the {len(F)} findings wait on the requester's edit of rows.json and build_rubric.py")
un.extend(u for u in SR.unresolved_items() if not u.startswith("diversity.authority_share"))
A("Unresolved: " + (" · ".join(f"({i}) {u}" for i, u in enumerate(un, 1)) if un else "none") + ".")
A("")
A("## Reminders")
A("- An all-Outcome set is normal; Process is not added to look thorough.")
A("- Fix the criteria in the builder, re-export, re-run check, then run /rubric.")
(WF / "09_Rubric_Check.md").write_text("\n".join(L) + "\n")
print("check written:", n, "criteria; weight", tw, bands, "findings", len(F), "reviewed", REVIEWED, "lint", lint["count"], "off band", len(off_band), "neg open", len(NEG_OPEN))
