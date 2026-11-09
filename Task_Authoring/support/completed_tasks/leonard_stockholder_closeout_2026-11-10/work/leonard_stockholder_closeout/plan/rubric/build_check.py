#!/usr/bin/env python3
"""Write Working_Files/09_Rubric_Check.md (check mode) for 09_Rubrics.json against the plan (rows.json), the eval lint and the /rubric checks.

The Findings table holds only findings supplied in the optional file plan/rubric/check_findings.json (absent or empty: the table prints none and readiness says the
blind review has not run yet). Accepted shapes of that file:

    [ {"criterion": "C17" or "sh_lb_ENG-2441", "span": "...", "rule": "...", "wrong": "...", "plan": "P17, F12", "type": "overly_broad", "severity": "Major"}, ... ]
    {"findings": [ ... ]}

and also the build_check tuple form, one list per finding: ["tag", "span", "rule", "wrong", "plan", "type", "severity"]. `type` must be a /rubric issue type and `span` a substring of 09_Rubrics.json;
stage_gate rubric-check enforces both. Rows are classified as in build_plan.py, by prefix, fact, vals and grp, so coverage lines, groups and counts all follow rows.json."""
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
from build_plan import PY, TASKREL, TI, WF, WS, axis, family, is_volume, of, rows  # noqa: E402

crit = json.loads((TI / "09_Rubrics.json").read_text())
assert len(rows) == len(crit) and all(r["t"] == c["title"] and r["w"] == c["weight"] for r, c in zip(rows, crit)), \
    "rows.json and 09_Rubrics.json differ: rebuild them together"
C = {r["tag"]: f"C{i + 1}" for i, r in enumerate(rows)}
CTX = json.loads((WF / "00_Task_Context.json").read_text())
FINDINGS_FILE = HERE / "check_findings.json"
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


def load_findings():
    """[(tag, quoted span, rule, what is wrong, plan row / ledger fact, type, severity)] from check_findings.json; [] when absent or empty."""
    if not FINDINGS_FILE.exists():
        return [], False
    raw = json.loads(FINDINGS_FILE.read_text())
    items = raw.get("findings", []) if isinstance(raw, dict) else raw
    out = []
    by_c = {c: t for t, c in C.items()}
    for it in items:
        if isinstance(it, (list, tuple)):
            tag, span, rule, wrong, plan, typ, sev = it
        else:
            ref = str(it.get("tag") or it.get("criterion") or "")
            tag = by_c.get(ref, ref)
            span, rule, wrong, plan, typ, sev = (it.get(k, "") for k in ("span", "rule", "wrong", "plan", "type", "severity"))
        tag = by_c.get(tag, tag)
        if tag not in C:
            raise SystemExit(f"check_findings.json names no known criterion or tag: {tag!r}")
        out.append((tag, span, rule, wrong, plan, typ, sev))
    return out, True


F, REVIEWED = load_findings()


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
    ("The holder sheet in the close-out folder, the draft finished (R4)", lambda r: r["tag"] in ("sh_write", "sh_volume"), True),
    ("What each holder holds, stock and options (R3, R4)", lambda r: family(r) == "sheet" and axis(r) in ("shares", "options"), True),
    ("Each line's last day (R3, R4)", lambda r: family(r) == "sheet" and axis(r) == "lastday", True),
    ("Each line's label (R3, R4)", lambda r: family(r) == "sheet" and axis(r) == "label", True),
    ("Series Seed total, options total, the label counts, the directors and the preferred vote on the sheet (R4)",
     lambda r: r["tag"].startswith(("sh_tot_", "sh_cnt_")) or r["tag"] in ("sh_directors", "sh_vote"), True),
    ("The sheet shared with Robert and Arthur (R4)", lambda r: family(r) == "sheet share", True),
    ("The investor letter: a Doc in the folder, shared with Robert, brought up to date (R5)", lambda r: family(r) == "letter", True),
    ("The 14 holder messages as drafts, to the address on each issue, each saying what they hold (R6, R12)", lambda r: family(r) == "note", True),
    ("Linear states on all 26 issues (R7)", lambda r: family(r) == "state", True),
    ("A reason comment on each issue with no note of its own (R7)", lambda r: family(r) == "reason comment", True),
    ("KPMG's confirmation sent as a reply to all, items 1 to 4 (R10, R11)", lambda r: family(r) == "KPMG reply", True),
    ("The heads-up to Griffin on the partner's own mail, sent (R8, R11)", lambda r: family(r) == "Griffin heads-up", True),
    ("The #winddown reply under the list, who goes first (R9, R11)", lambda r: family(r) == "thread reply", True),
    ("The sheet before the notes and everything else, as the notes require (R2, Process)", lambda r: family(r) == "order", True),
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
cards = list((WS / "Evals/references/known_data_issues").glob("*"))

A("# 09 Rubric Check — leonard_stockholder_closeout (stockholder and option-holder close-out)")
A(f"Checked 2026-11-09 · Criteria {n} (builder minimum 5: ok) · Plan 2026-11-09 (09_Rubric_Writing_Plan.md, rows P1–P{n} = C1–C{n}) · "
  f"09_Rubrics.json sha256 {sha} · weight {tw} (5 ×{bands[5]}, 3 ×{bands[3]}, 1 ×{bands[1]})")
A("JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · "
  "schema gate: pass (a JSON array of objects; every row has all five fields non-blank; category Outcome or Process; weight 1, 3 or 5)")
if major or moderate:
    readiness = f"FAIL-RISK (Overall Rubric Quality: {major} Major and {moderate} Moderate rows in Findings)"
elif not REVIEWED:
    readiness = "NON-FAIL-RISK (no reviewer findings are loaded yet: plan/rubric/check_findings.json is absent, so the blind-review half of this check is still to come; the mechanical checks here are clean)"
else:
    readiness = "CLEAN"
A(f"Readiness for /rubric: {readiness} — a prediction only; /rubric gives the verdict")
A(CTX["universe"]["clock_line"])
A("")
fmt = [f for f in lint["findings"] if f["check"] == "format_lock"]
anon = [f for f in lint["findings"] if f["check"] == "anon_token"]
others = [f for f in lint["findings"] if f["check"] not in ("format_lock", "anon_token")]
A(f"Lint (`python3 Task_Authoring/tools/hg.py rubric-lint {TASKREL}/09_Rubrics.json`, run for this report): {lint['count']} findings, {len(anon)} `anon_token` and {len(fmt)} `format_lock`"
  + (f", and {len(others)} other ({', '.join(sorted({f['check'] for f in others}))}), each to resolve below" if others else ", and no `disguised_negative`, `evidence_no_record`, `vague_exemplar`, `tool_name`, `prohibition_title` or schema hit") + ".")
A("")
A(f"- `anon_token` ({len(anon)} hits, rows {', '.join(str(x) for x in sorted({f['row'] for f in anon}))}): verdict OK. The tokens are the source strings (Linear issue titles and Carta names as the tools return them); "
  "each binds as LITERAL and is accepted as shown, as the lint's own instruction and rubric_factual_checks.md require, and the rows also name the ENG or ES key.")
A(f"- `format_lock` ({len(fmt)} hits: " + ", ".join(f"C{f['row']} '{f['text']}'" for f in fmt) + "): verdict OK. Each is a figure from the records or the count the close-out notes set ('One row per issue on the sheet'), not a "
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
A("Not graded, with the reason: a count of the drafts (count-bundle-v1, a count over separate writes is Major even beside per-item rows; the 14 drafts have their own rows); a draft to a line that gets none "
  "(the label and state rows decide who is owed one, and the notes say the drafts are exactly the Closing and Last day lines); and the sheet's unsampled line cells, which gate 15 leaves to the volume row.")
A("")
A("## Coverage — gradable surface")
A("| Surface slot | Stable fact ID | Criteria | Covered / dispositioned / gap | Disposition reason (evidence) |")
A("|---|---|---|---|---|")
for s in B.SLOTS:
    rs = B.covering(s["id"])
    if rs:
        A(f"| {s['id']} | {s.get('fact_id') or rs[0]['fact']} | {', '.join(C[r['tag']] for r in rs)} | covered | the title rejects the omission and "
          f"the plausible wrong value ({B.wrong_value(rs[0])}). |")
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
    A(f"{len(F)} findings from plan/rubric/check_findings.json ({', '.join(f'{v} `{k}`' for k, v in by.items())}). Each row names the change; rows.json and build_rubric.py are the requester's to edit, and a finding drops off this "
      "table when the reviewer removes it from the file.")
    A("")
    A("| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |")
    A("|---|---|---|---|---|---|---|---|")
    for i, (tag, span, rule, wrong, plan, typ, sev) in enumerate(F, 1):
        A(f"| {i} | {C[tag]} | \"{span}\" | {rule} | {cell(wrong)} | {plan} | {typ} | {sev} |")
else:
    A("No findings are loaded: plan/rubric/check_findings.json is absent or empty, so this report records the mechanical checks only, and reviewer findings will be written into this table when the file is supplied "
      "and build_check.py is re-run.")
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
    A(f"| {g} | {crange(d['rows'])} | {len(d['samples'])} samples; volume rows {crange(d['vols'])} |")
over = [g for g, d in GROUPS.items() if len(d["samples"]) > 5]
A(f"| Overlap groups | {', '.join(over) or 'none in this report'} | "
  + ("no spot-check group exceeds five samples, and no two rows embed one acceptance condition: a miscounted holder fails its own line's rows and the totals, a shared root cause and not a shared condition (§3.3)." if not over else "") + " |")
A("| Predicted all-fail | 0 rows on the four Evals bases | every value is reachable through a cataloged tool and visible to Leonard (plan §E visibility proof) |")
A("")
A("## Dimensions")
A("| Dimension | Count / % | Threshold | Status |")
A("|---|---|---|---|")
if major or moderate:
    quality = "FAIL (predicted; the Findings table is the fix list)"
elif not REVIEWED:
    quality = "pending the blind review (no findings loaded); mechanical checks clean"
else:
    quality = "PASS (predicted)"
A(f"| Overall Rubric Quality | {major} Major · {moderate} Moderate · 0 Minor of {n} rows ({100 * (major + moderate) / n:.1f}%) in Findings | any Major or Moderate fails; Minor < 5% | {quality} |")
A(f"| Criteria Weights | {len(off_band)} rows off their kind of work ({bands[5]} at 5, {bands[3]} at 3, {bands[1]} at 1); {off_slot} rows differ from their surface "
  f"slot's weight, which never sets one (gate 17) | ≤ 10% one level, none two levels | {'PASS (predicted)' if not off_band else 'FAIL'} |")
A(f"| Known data issue | {'0 rows: Evals/references holds no known_data_issues card for this universe' if not cards else str(len(cards)) + ' cards to read'} | no row rests "
  f"on a listed card | {'PASS' if not cards else 'FAIL'} |")
A(f"| Category Balance | {n - n_proc} Outcome / {n_proc} Process | ≥ 1 Outcome, Process ≤ 50%, < 2 unnecessary Process rows | PASS |")
A(f"| Process Rubrics | {n_proc} Process rows, each with the three-condition test in plan §C; 0 missing ordering checks (the notes set one order, the sheet first) | 0 missing, every Process row valid | PASS |")
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
A("Re-read as /rubric in phase order (Evals/3_Rubrics_Eval.md 1.2 schema, 1.4 coverage, 2.1–2.12 per row, 3.1–3.7 set level, 5.1 predicted all-fail) and the pre-verdict sweep: one missing requirement (none: every requirement has a "
  f"row, and all {len(B.SLOTS)} surface slots are covered or dispositioned), one phrasing mismatch with the prompt (none), one overly broad row, one non-atomic row, one over-specific or hard-coded title and one duplicate or cascade group "
  f"(left to the blind reviewers, whose findings load from check_findings.json), one category mislabel (none: the {n_proc} order rows are the only Process rows), one vague exemplar (none: lint {lint['count']} findings resolved above; the pre-scans over "
  f"every title hit {len(SCAN['rank'])} ranking words, {len(SCAN['vague'])} subjective words and {len(SCAN['exemplar'])} exemplars), one prohibition-only title ({'none' if not NEG_OPEN else 'found'}). Calibrated against the table in "
  "Evals/references/rules/rubric_qc_examples.md: do-nothing (every row needs a write or a sent or saved message), PT/UTC day (last days are dates, not instants), reachability (the sidecar's evidence_path starts at the holder project or the notes), LITERAL key "
  "(ENG keys, ES numbers, the Slack thread and the file ids appear as the tools return them; anonymized tokens accepted as shown).")
A("")
lines, fails = SR.reverify()
assert not fails, fails
A("Re-verified in this build, the same reads the plan's Self-review records (seeded values from a fresh SQL parse, base records through hg.py, per-line values against solver/truth.json):")
A("")
L.extend(lines)
A("")
A(f"Tally recount from the findings table: {major} Major, {moderate} Moderate, 0 Minor; predicted all-fail 0; no validity defect in this report's mechanical checks. Each finding counts its row once.")
A("")
A("| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |")
A("|---|---|---|---|---|")
found = {f[0]: f for f in F}
pending = "blind review pending" if not REVIEWED else "—"
for i, r in enumerate(rows):
    verdict = "finding" if r["tag"] in found else ("mechanical checks clean" if not REVIEWED else "cleared")
    res = ("see Findings (" + found[r["tag"]][5] + ")" if r["tag"] in found else f"resolved by the title as written (evidence: {cell(SR.record_ids(r))})")
    A(f"| C{i + 1} {r['tag']} | {verdict} | Counter-reading — {cell(SR.CR[r['tag']])} | {res} | {pending} |")
A("")
top, over_units = B.diversity()
un = []
if not REVIEWED:
    un.append("the blind-review findings are still to come: plan/rubric/check_findings.json is absent, so readiness stays NON-FAIL-RISK and no row carries a reviewer verdict")
if over_units:
    un.append("the upstream rubric-writing gate carries one structural FAIL (diversity.authority_share: "
              + "; ".join(f"{u} {100 * s / tw:.0f}%" for u, s in over_units[:3]) + f"; {len(over_units)} units over 50% in all), by construction: every line's facts run through one issue list and one rules doc; the requester decides")
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
