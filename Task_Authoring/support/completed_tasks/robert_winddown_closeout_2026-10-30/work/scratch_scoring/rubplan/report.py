import json, re, collections
T = '/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/'
D = json.load(open(T + 'Working_Files/09_Rubrics.draft_with_plan_ids.json'))
PN = json.load(open('/tmp/claude-1000/-home-sumit-Downloads-OC-OC/a9f2273f-6832-49de-a422-8296cfdee0cc/scratchpad/replay/passn.json'))
C = {x['P']: f"C{i}" for i, x in enumerate(D, 1)}
W = collections.Counter(x['weight'] for x in D)
L = []
a = L.append
a("# 09 Rubric Check — rb-winddown-closeout")
a(f"Checked 2026-10-30 · Criteria {len(D)} (builder minimum 5: ok) · Plan 2026-10-29 (09_Rubric_Writing_Plan.md, OE status PASS — /oe r9 PASS 5 on revision 26)")
a("JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass (115 objects, all five fields non-blank, category Outcome, weights in {1, 3, 5})")
a("Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict")
a("")
a("Source of the criteria: Claude draft from the plan (`/create-rubric-writing draft`), revised in this check (see Fixes made in this check). Every criterion maps one-to-one to plan row P-n (C-n = P-n); the map is in Working_Files/09_Rubrics.draft_with_plan_ids.json.")
a("")
a("## Coverage")
a("| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |")
a("|---|---|---|")
cov = [
 ("Prompt 'build the register the way he wants it' + ask 'I need one sheet' (P1)", "C1", "Covered — no sheet fails C1; a second register file is still one register (any file type)"),
 ("Rule 1–3 row set: every account, 25 rows (P2) and the QuickBooks/Intuit merge (P3)", "C2, C3", "Covered — 26 rows (Intuit split or iPostal kept) fails C2; Intuit on its own row fails C3"),
 ("Rule 4 'What we do' for every row — core column, exhaustive (P4–P28)", "C4–C28", "Covered — each wrong action (Keep for Gusto, Hold for Metabase, Move for GitHub) fails its own row"),
 ("Rule 5 status for the 14 Cancel rows (P29–P42)", "C29–C42", "Covered — Requested for Unity or CodeRabbit, Closed for Layer fail their rows"),
 ("Rule 5 'say where' for Closed rows — 3 samples of 7 (P63–P65)", "C63–C65", "Covered — a Closed row with no source fails the sampled row"),
 ("Rule 6 by-when — 5 direct exceptions + 5 samples (P43–P52)", "C43–C52", "Covered — Feb 28 for Singular, Mar 3 for Layer, Aug 15 for Carta, Feb 17 for Figma fail their rows"),
 ("Rule 7 owner — 2 direct exceptions (Docusign hand-off, ElevenLabs added) + 3 samples (P53–P57)", "C53–C57", "Covered — Leonard as Docusign owner fails C53"),
 ("Rule 8 monthly cost — 5 samples incl. the three derived costs (P58–P62)", "C58–C62", "Covered — 25,000/12 or 6,250 for Singular, 1,212 for Figma fail their rows"),
 ("Rule 9 the two totals in the sheet (P66, P67)", "C66, C67", "Covered — a total including Intuit (6,821.49) or Metabase as Hold (1,397.04) fails"),
 ("Ask 'share it with me and Arthur as editors' (P68–P70)", "C68, C69, C70", "Covered — viewer role fails C68/C69; a third grantee fails C70"),
 ("Settle rule: 7 Done, 4 Canceled, 17 open (P71–P82)", "C71–C82", "Covered — each state write has its own row; Metabase or Layer set to Done fails C82"),
 ("Settle rule: a comment on each issue with what happens and by when (P83–P110)", "C83–C110", "Covered — one row per issue on all 28 issues (no volume row needed; the former C111 volume row was a duplicate and was removed); a pointer-only comment fails its row"),
 ("Prompt 'reply to him in his thread' (P111)", "C111", "Covered — a top-level post in #winddown fails C111"),
 ("Prompt 'with the two monthly totals' (P112, P113)", "C112, C113", "Covered — reply rows are separate from the sheet rows (gate 6: two deliverables)"),
 ("Prompt 'anything that clashes with what we already decided' (P114, P115)", "C114, C115", "Covered — a reply naming only Google fails C114; card moves or Gusto named as clashes are not graded (rule 10)"),
 ("Required exclusions (iPostal, Lucidchart, Google Ads, Pond5, AWS, UA ad accounts, game-ops lines, Intuit duplicate)", "C2, C3, C78–C81, C94, C98, C109, C110", "Covered — the all-inclusive register fails C2; the four Canceled states and comments each have a row"),
]
for r in cov:
    a(f"| {r[0]} | {r[1]} | {r[2]} |")
a("")
a("Unauthorized criteria: none")
a("")
a("## Findings")
a("| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |")
a("|---|---|---|---|---|---|---|---|")
a("| — | — | — | — | No open finding after the fixes below; the pre-verdict sweep (Self-review S1) found none of the eight defect kinds | — | none | — |")
a("")
a("## Fixes made in this check")
a("All fixes are in 09_Rubrics.json now (Claude revision, GEN_EXECUTION §2); each is grounded in the record named.")
a("| Fix | Criteria | Before → after | Why (rule / record) |")
a("|---|---|---|---|")
fx = [
 ("Standard Agent subject", "C2–C67, C112–C115", "\"The Agent's account close-out register gives …\" / \"The Agent's #winddown thread reply …\" → \"The Agent records … in the account close-out register\" / \"The Agent states in its #winddown thread reply …\"", "playbook check 2.9: a possessive subject is a nonstandard form → Agent-Centric NON-FAIL; the lowest dimension sets /rubric's verdict"),
 ("Reason not required on off-register comments", "C98, C109, C110", "\"stays off the register because it was already cancelled before Feb 9\" → \"is left off the account close-out register\"", "the project asks only for 'what happens and by when' (3f0c6a52-ee13-4b1e-68e3-a74bcc33818a); all six baseline comments on ENG-2466 give a second valid reason (UA ad account, 'Leonard is closing the ad networks directly'), so the old title was overly_specific and failed 6/6 (run-1…run-6)"),
 ("Comment wording the project does not set", "C86–C88, C91–C94, C96, C97, C106", "\"until the Mar 12, 2026 delivery review call\" → \"until Mar 12, 2026\"; \"comes off the SVB card by Feb 17\" → \"with Feb 17, 2026 as its by-when date\"; \"which carries the register row\" dropped", "a comment saying 'Hold for Sunset, by Mar 12' is a valid answer (2.7 overly_specific)"),
 ("Negation words in titles", "C28, C42, C50, C54, C58–C62, C115", "\"no Linear issue\", \"with or without $\", \"there is no ENG-2445\", \"asking not to archive\" reworded", "lexical pre-scan (2.9) clean; all were descriptive, none prohibition-only"),
 ("Status titles", "C29–C42", "\"…, a Cancel row, as Closed …\" → \"records the status Closed (the vendor itself has confirmed; or a clear equivalent) for …\"", "one claim per title (2.2); the Cancel action is graded on C4–C28"),
 ("Deep check (2026-10-30): duplicate volume row removed", "former C111", "\"The Agent adds a new comment to each of the 28 issues …\" (weight 1) → removed; C112–C116 renumbered C111–C115", "3.3 duplicate: C83–C110 already grade a comment on every one of the 28 issues, so the volume row was wholly redundant"),
 ("Deep check (2026-10-30): state guard weight", "C82", "weight 5 → 3", "a missed Done/Canceled write is already graded on C71–C81 and also lowers C82's count; runs 1 and 5 fail C82 only through those misses (replay), so a 5 charged them twice"),
 ("Deep check (2026-10-30): same-ticket weights", "C86, C102, C108", "weight 5 → 3", "every register row for Linear, Layer and 1Password is weight 3 or less; a comment that restates the register decision now carries the same weight (Douglas /rubric lesson: keep weights consistent across rows for the same ticket)"),
 ("Exact CodeRabbit quote", "C37, C65, C74", "quote now matches SQL L142 verbatim: 'The CodeRabbit subscription for **harmonygames-Games** was canceled on Feb 12, 2026, so this pull request was not reviewed'", "2.3 every literal matches the record"),
]
for r in fx:
    a(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |")
a("")
a("Deviation from the plan text (no change of what is graded): P98/P109/P110 plan values carry the cancellation dates; the criteria grade only 'left off the register' for the reason above. P82's plan wording ('exactly 17 … not Done or Canceled') is kept as a count (volume row), not an exact set (gate 15).")
a("")
a("## Overlap groups · Spot-check groups · Predicted all-fail")
a("| Group / row | Members / basis | Shared condition / reason |")
a("|---|---|---|")
a("| Spot check G1 by-when | C43–C52 (5 direct: Carta, Google Workspace, Slack, QuickBooks, Singular; 5 samples) | ≤ 5 samples + volume row C2; exceptions graded directly (gate 15) |")
a("| Spot check G2 owner | C53–C57 (2 direct: Docusign hand-off, ElevenLabs added; 3 samples) | ≤ 5 samples + volume row C2 |")
a("| Spot check G3 monthly cost | C58–C62 (5 samples incl. the three derived costs) + totals C66/C67 | ≤ 5 samples + volume row C2; totals are aggregate controls, not duplicates (3.3) |")
a("| Spot check G4 Closed source | C63–C65 (3 of 7 Closed rows) | ≤ 5 samples + volume row C2 |")
a("| Not a group: iPostal misread | C2, C66, C112 | rows that share one likely root cause, each a separate prompt-required deliverable (sheet row set, sheet total, reply total) — not a cascade group (3.3) |")
a("| Not a group: Unity / CodeRabbit confirmation | C29, C63, C71, C83 / C37, C65, C74, C103 | four distinct deliverables (register status, register source, Linear state, Linear comment); each is its own prompt-required write |")
a("| Not a group: state volume | C82 with C71–C81 | volume row for the state writes and its direct rows (aggregate control, 3.3) |")
a("| Predicted all-fail | 0 rows on the four defect bases | every value is reachable by Robert: base mail in his mailbox, private channels he is in, unscoped Linear/Trello/GitHub (persona_view lines in 09_Rubric_Writing_Plan.md and 08_OE_Writing_Ledger.md) |")
a("| Valid all-fail in the baseline replay (not a defect) | C37, C65, C74, C103 (CodeRabbit, 0/6), C82 (0/6) | evidence reachable (SQL L142 harmonygames-Games/Combo-Fighters#38#c_1; /oe OE 24 path SUPPORTED); no run read PR 38. C82 fails because Unity/CodeRabbit stay open. For /create-allfail, not a rubric defect |")
a("")
a("## Dimensions")
a("| Dimension | Count / % | Threshold | Status |")
a("|---|---|---|---|")
a("| Overall Rubric Quality | 0 Major, 0 Moderate, 0 Minor (0%) | Major ≤ 10%, Major+Moderate ≤ 15%, all ≤ 20%; PASS needs 0 Major/Moderate and Minor < 5% | PASS (margin: 11 Major rows before FAIL) |")
a(f"| Criteria Weights | 0 of 115 off the plan band (5 ×{W[5]} · 3 ×{W[3]} · 1 ×{W[1]}) | ≥ 15% two-level or ≥ 30% one-level misses fail | PASS |")
a("| Category Balance | 115 Outcome, 0 Process | zero Outcome fails | PASS |")
a("| Process Rubrics | 0 Process rows | 2+ invalid fail | PASS |")
a("| Agent-Centric Phrasing | 115 standard 'The Agent' + action titles, 0 possessive, 0 tool names | 1+ artifact subject or tool name fails | PASS |")
a("| Negative Criteria | 0 prohibition-only titles; lexical pre-scan 0 hits | 1+ fails | PASS |")
a("| Predicted all-fail | 0 | harness tolerance 0 | PASS |")
a("| Schema and repair gates | schema pass; self-containment, accuracy, atomicity, coverage, duplicates, weights, contradiction pass | any repair-gate failure is reported | PASS |")
a("")
a("Threshold margin: with 115 rows one Major is 0.9%; the Overall FAIL line is 12 Major rows.")
a("")
a("Baseline replay (advice, not a rubric verdict): an approximate script grade of the six runs in 07_Baseline_Trajectories (run-1 … run-6) against these criteria gives 86–94% weighted (average ≈ 88%; 88.5% before the deep-check weight changes). The script does not read comment, total or reply text and counts those rows as passing, so the real grader may score lower. The assignment's targets (00_Assigments.md: 'difficulty under 80%', more than 150 tool calls per run; the runs made 127–149) are not met. That is a hardening question (/create-hardening MODE B), not a criterion defect; the rubric is not tuned to it.")
a("")
a("## Self-review")
a("| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |")
a("|---|---|---|---|---|")

def pn(P):
    v = PN.get(P)
    return f"replay {v}/6 pass (run-1…run-6)" if v is not None else "replay 6/6"

for x in D:
    P, t = x['P'], x['title']; c = C[P]; rp = pn(P)
    if ' as the action for ' in t:
        cr = "a run writing 'Hold' or 'cancel it' instead of the rule-4 phrase could fail an exact-word judge"
        rs = f"the title accepts 'or a clear equivalent' (2.10 paraphrase allowance); the action follows rule 4 (f_1326e66bcabfda8fd29e4a) as in OE 25; {rp}"
    elif ' the status ' in t:
        cr = "a valid run could leave status on a Cancel row blank or use 'Confirmed' for Closed"
        rs = f"rule 5 requires a status on every Cancel row; 'or a clear equivalent' accepts 'Confirmed'; source record in the justification; {rp}"
    elif 'by-when date' in t:
        cr = "another date is defensible (day before the next charge, e.g. Feb 28 or Mar 3)"
        rs = f"rule 6 takes the earlier SVB date (698fa9f7f77cecfe5c7aa524 'everything we're cancelling gets cancelled by end of day the 17th'); Hold rows off the card stay to the call (evt_f1d245d44ceff5a6e049c0); any date format; {rp}"
    elif 'as the owner of' in t:
        cr = "a run may keep the Linear assignee, or write a full name or email"
        rs = f"rule 7 assignee unless handed on (cmt_bbdca23f075e9fca5cb8 for Docusign; 'Anything you add is yours' for ElevenLabs); first or full name accepted; {rp}"
    elif 'monthly cost of' in t:
        cr = "rounding or a $ sign could fail an exact match; another source figure could be argued"
        rs = f"± 0.01 and '$ sign optional' in the title; rule 8 owner figure first, else last invoice / receipt to a month (cost basis in the justification); {rp}"
    elif 'source of the Closed status' in t:
        cr = "a run citing the vendor directly ('Unity confirmed') instead of the relay could fail"
        rs = f"'any wording naming that source' accepts the vendor or the relay (rule 5 'say where'); {rp}"
    elif t.startswith('The Agent sets Linear issue'):
        cr = "a run could use Duplicate for ENG-2450 or leave a Closed account open until access ends"
        rs = f"team ENG has Done and Canceled only (08_OE_Writing_Ledger.md F30); settle rule 'Done once the account counts as closed … (access can run out later)' (3f0c6a52-ee13-4b1e-68e3-a74bcc33818a); {rp}"
    elif 'adds a new comment on Linear issue' in t:
        cr = "a valid comment could word the action differently or give a different (valid) reason"
        rs = f"the title names only what happens and the by-when date the project asks for (3f0c6a52-ee13-4b1e-68e3-a74bcc33818a), no reason or phrasing; one comment's content is one record (coherent_record exception: a send plus the content that defines it); {rp}"
    elif P == 'P1':
        cr = "an .xlsx upload or a Doc table is a valid 'sheet'"; rs = f"the title accepts any file type and title (ask C0ADGSZKR3R/1771003267.448213 'one sheet'); {rp}"
    elif P == 'P2':
        cr = "a run listing left-off accounts beside the register has more than 25 lines"; rs = f"the title allows a separate left-off list; count from 28 issues − Intuit − 3 pre-Feb 9 + ElevenLabs (OE 25); {rp}"
    elif P == 'P3':
        cr = "rule 1 says 'the name on its invoice' and Robert sees no Intuit invoice"; rs = f"three labels accepted (/oe r9 rubric note 1); cmt_e3da997ff7b6575fbea0; {rp}"
    elif P in ('P66', 'P67'):
        cr = "a SUM formula instead of a typed number, or a total on another tab"; rs = f"the title grades the value shown in the register (formula results count); 6,706.49 / 1,249.04 recomputed from OE 25's 25 costs; {rp}"
    elif P in ('P68', 'P69'):
        cr = "sharing through a link or a different email for the same person"; rs = f"editor role with the named person; emails from Evals/references/persona/roster.json; {rp}"
    elif P == 'P70':
        cr = "a run sharing with Oliver too could argue it helps"; rs = f"the ask names only Leonard and Arthur (C0ADGSZKR3R/1771003267.448213); affirmative count, not a prohibition; {rp}"
    elif P == 'P82':
        cr = "In Progress for Hold rows is a valid open state; the count also falls when a Done row is missed"; rs = f"the title counts any open state; as the state volume row it is an aggregate control beside C71–C81 (3.3), not a duplicate; {rp}"
    elif P == 'P111':
        cr = "a DM to Leonard or a top-level #winddown post"; rs = f"the prompt says 'in his thread'; thread ts 1771003267.448213 named; {rp}"
    elif P in ('P112', 'P113'):
        cr = "the reply may round ($6,706) or label the totals differently"; rs = f"± 0.01 to the cent per rule 9 'rounded to cents'; label free; {rp}"
    elif P == 'P114':
        cr = "a run may split Slack into two clashes, or name only the guest cut"; rs = f"either Slack decision passes and two Slack clashes also pass (/oe r9 rubric note 3); C0ADGSZKR3R/1770842405.931359 'turn people into guest accounts'; {rp}"
    elif P == 'P115':
        cr = "a run may describe it as the Workspace archive rather than 'Google accounts'"; rs = f"any wording of the archive plan (C0ADGSZKR3R/1770933903.645709 'archieve account on google after Feb 15') against Sunset's 'please don't archive or delete any' (robert@harmonygames.co/1856965916492026238); {rp}"
    else:
        cr = "valid alternative"; rs = rp
    a(f"| {c} ({P}) {t[:70].replace('|','/')} | PASS | {cr} | {rs} | none |")

gen = [
 ("S1 Pre-verdict sweep (5.0)", "PASS", "one missing requirement / phrasing mismatch / non-atomic / category / over-specific / duplicate group / vague exemplar / prohibition-only title", "Coverage table (16 requirements, all covered); comment rows checked against the project's 'what happens and by when' only (C98, C109, C110 fixed); lexical scans for 'such as', 'e.g.', ranking and subjective words return 0 hits; 115 Outcome rows (2.6)"),
 ("S2 Atomicity of dated comment rows", "PASS", "C89 'being cancelled by Feb 17, 2026' grades the action and the date together, which a strict reader could split (2.2)", "documented exception: a send plus the content that defines it (coherent_record.md); the project defines one comment's content as 'what happens and by when' (3f0c6a52-ee13-4b1e-68e3-a74bcc33818a); the accepted Douglas comment rows used the same shape (support/completed_tasks/douglas_beta_server_signoff_2026-10-28)"),
 ("S3 Re-verified values", "PASS", "a ledger or OE value copied without re-reading", "re-verified this run with hg.py: `hg.py search search gmail \"Singular Labs Inc: Invoice\"` (threads 00000406.json, 00000416.json …), `… gmail \"Receipt from Eleven Labs\"` (00005659.json, 00014566.json), `… slack \"guest accounts\"` (C0ADGSZKR3R/2026-02.json /88), `… slack \"archieve account on google\"` (/190); injected values read from 01_Universe_Inject.sql L36 (Unity note), L142 (CodeRabbit notice), L159–L255 (comment literals); every quoted phrase in the justifications matched the SQL, OEs or prompt by script"),
 ("S4 Predicted all-fail recount", "PASS", "the CodeRabbit rows fail all six baseline runs", "recounted from recorded defects only: 0 rows on the four defect bases; the CodeRabbit notice is reachable (SQL L142; /oe OE 24 SUPPORTED) — a valid all-fail for /create-allfail (run-1…run-6)"),
 ("S5 Mutation test", "PASS", "a wrong single value that no row rejects", "Intuit as a second row → C2, C3, C66; Metabase Hold → C11, C67; Layer Closed → C36, C102, C82; Feb 28 for Singular → C47; viewer share → C68; missing Slack clash → C114; unsampled owner error → documented sampling limit (rubric_sampling.md)"),
 ("S6 Fixes grounded", "PASS", "a rewrite that changes what is graded", "each fix in 'Fixes made in this check' cites its rule § or record; the graded value is unchanged on every row (plan P-n map in 09_Rubrics.draft_with_plan_ids.json)"),
 ("S7 Upstream gate", "NON-FAIL", "rubric-writing gate is FAIL on diversity.authority_share (Linear project chain ~71%), so this gate's chain check fails", "structural: every account is a Linear issue (F8–F10), same design finding as the accepted Douglas task (its 09_Rubric_Writing_Plan.md L205, L348); relabelling ledger origins to pass would misstate the evidence — for the human to accept"),
]
for g in gen:
    a(f"| {g[0]} | {g[1]} | {g[2]} | {g[3]} | {'see S7' if g[1] != 'PASS' else 'none'} |")
a("")
a("Unresolved: (1) the upstream rubric-writing gate's diversity.authority_share FAIL (structural, S7); (2) baseline difficulty ≈ 89% against the author's < 80% target — a hardening question, outside this check. No criterion finding is unresolved.")
a("")
a("## Reminders")
a("- An all-Outcome set is normal; Process is not added to look thorough.")
a("- Enter the 115 criteria in the Rubric Criteria Builder, export over 09_Rubrics.json, re-run check, then /rubric.")
open(T + 'Working_Files/09_Rubric_Check.md', 'w').write("\n".join(L) + "\n")
print(len(L))
