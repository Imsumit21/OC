import json
S='/tmp/claude-1000/-home-sumit-Downloads-OC-OC/64ffea75-2ed7-4766-a065-99d4d43b34de/scratchpad/rub/'
meta=json.load(open(S+'meta.json'))
CR={
'P1':("valid fails: a run creates the sheet in its own Drive and then moves it","accepted — the row grades the final parent d_69fcebc484d472907b0b5c (L6), route ungraded; wrong passes: the client QA folder d_d71300168ca5dffa4db8b3 fails the exact folder"),
'P2':("valid fails: a run adds a notes line listing ZOM-547/ZOM-553 as excluded","accepted if kept apart from the ticket rows (brief §4b); wrong passes: 18 or 19 rows (547/553 kept) fail the count — runs 1, 3, 4, 6 had 18 (baseline replay)"),
'P20':("valid fails: sharing the folder instead of the file","Leonard asked to have it shared \"directly\" with comment access (L71, douglas@harmonygames.co/1844721277206562572); a folder share is not the file share the email asks for, and all six runs shared the file"),
'P21':("valid fails: reply posted under the ask as a thread reply","accepted — top level or thread (brief §4b W4, D05QQF7V404/1759266764.508127); a #zombie-match3d copy is extra (T14)"),
'P22':("valid fails: \"two of seventeen\" in words","accepted — number or word; wrong passes: \"5 of 17\" (runs 2, 5) and \"9 are on prod\" (runs 1, 4) fail"),
'P23':("valid fails: the 15 listed as titles, not keys","the count is graded, not the form; wrong passes: 8, 9 or 12 listed (baseline) fail"),
'P33':("valid fails: a run moves a 16th ticket (e.g. ZOM-547)","that is a wrong move under F11 and the count rightly fails; the ZOM Todo state is named by F15 (team_ZOM states in linear data.json)"),
'P43':("valid fails: one ticket gets two comments","the row counts tickets commented (15), not comments"),
}
lines=[]
for r in meta['rows']:
    P=r['P']; w=r['what']
    if P in CR: a,b=CR[P]
    elif 'register row — marked' in w or 'present and marked' in w:
        t=w.split()[0]; v='Y' if '(Y)' in w else 'N'
        a=f"valid fails: {t} written as \"not on prod\"/\"No\" instead of {v}" if v=='N' else f"valid fails: {t} written as \"yes\""
        b=f"Y/N, yes/no and on prod / not on prod are one class (brief §4b); wrong passes: the opposite value fails — {t} {v} re-derived from the PR rows and the deploy log (01_Universe_Inject.sql, F31)"
    elif 'server change(s) include' in w:
        t=w.split()[0]
        a=f"valid fails: {t}'s change written as \"HP table\", \"economy sheet import\" or \"#52\" without the repo"
        b="any recognisable words are accepted (brief §4b, \"phrase broadly\"); wrong passes: a cell naming only the PR fails (run 2 listed only #48 for ZOM-487, f_78bedc46245090a160d2dd row 2025-09-17 15:50 shows the import)"
    elif w.startswith('Reply —') and 'named among' in w:
        t=w.split()[2]
        a=f"valid fails: {t} given by title, not key"
        b=f"key or title accepted; wrong passes: {t} listed under \"on prod\" fails — the row requires it among the not-on-prod tickets (F32, D05QQF7V404/1759266764.508127 asks \"which ones aren't\")"
    elif 'moved to Todo' in w:
        t=w.split()[0]
        a=f"valid fails: {t} moved to Backlog or In Validation"
        b=f"card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d); In Validation is the client card's rule (T7) — exact state is right; {t} is Done at the clock (linear data.json)"
    elif 'comment — names' in w:
        t=w.split()[0]
        a=f"valid fails: {t}'s comment phrases the change loosely"
        b="wording delegated; only the named change is graded (brief §4b W5); wrong passes: a comment naming only the PR fails (run 2's ZOM-487 comment named #48, harmonygames-Games/match3d-backend#48 is on prod)"
    else:
        a,b=("check","F31")
    lines.append(f"| {P} | counter-reading: {a} | {b} |")
body='\n'.join(lines)
txt=f'''
## Self-review

No-criterion-text scan: the plan holds noun phrases and values only; no drafted criterion titles.

1. Re-read as /rubric (3_Rubrics_Eval.md 1.4, 3.1): every requirement R1–R7 of the ledger has rows on the correct artifact — register (P1–P19), share (P20), reply (P21–P32), Todo moves (P33–P42), comments (P43–P52). Both told facts (count, list) have reply rows. The exclusions ZOM-547/ZOM-553 are graded affirmatively through the volume rows P2, P22, P23 (no prohibition-only row). Each population has its volume row and direct exception rows; samples ≤ 5 per group.
2. Re-verified: every literal was re-read in this run — the 17 tickets and their Y/N values recomputed from the SQL PR rows (L164–L713) and the deploy log grid (L23) under the doc (L15) and freeze (L156); the amendment records L36, L96, L211, L243, L463; the Todo state name from linear data.json team_ZOM states (hg.py); the folder L6 and Leonard's address L71. The /oe PASS report (score 5) verified the same values independently.
3. Predicted all-fail re-check: every scoped record behind the cited F-ids is YES for douglas (Visibility proof above: check-sql verdict PASS, 2 can-see YES); every write maps to a catalog tool (gdrive_create_file, gdrive_share_file, slack_send_message, linear_update_issue, linear_create_comment); no friction; no evidence outside the persona's view. Predicted all-fail rows on the four bases: 0. The 17 rows that failed all six baseline runs (§E) are genuine model failures — run 3 even opened #38#rc_1 and #39#rc_1 and kept ZOM-459/ZOM-509 as Y — and go to /create-allfail with VALID justifications.
4. Weights by work kind: 5 where the result needs a hidden amendment, the freeze or a full-audit count; 3 for a single comparison or for naming a change the register already holds; 1 for the share and the DM placement. Bands 5 ×30 · 3 ×20 · 1 ×2.
5. Atomicity: one ticket × one column per register row; one ticket per reply-list row; one write per Todo row; ZOM-503's two changes graded only on #52 (P15), so no row bundles two PRs.
6. Shortcut and diversity: the probe output is in §F with each HIT dispositioned. The rules card F2 is in the Depends-on closure of every row (100%); the card is the task's own instruction source, so the 50% cap cannot be met without falsifying the ledger's dependencies. This is reported as a design finding, as in the accepted Frederick account-handover task, and the human decides. Independent chains land on distinct rows (§E).

| P | Counter-reading | Resolution (evidence) |
|---|---|---|
{body}

Unresolved: diversity.authority_share (rules card at 100% of the weight) — a structural design finding for the human to accept, not a value or visibility gap.
'''
open(S+'selfrev.md','w').write(txt); print(len(lines))
