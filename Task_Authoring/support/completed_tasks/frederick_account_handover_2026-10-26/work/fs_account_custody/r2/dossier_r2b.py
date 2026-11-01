import re, sys
P, O = sys.argv[1], sys.argv[2]
s = open(P, encoding='utf-8').read()
rd = lambda n: open(f'{O}/{n}', encoding='utf-8').read().rstrip('\n')
YT = "frederick.stone@harmonygames.co/1834647853990444617"
TT = "frederick.stone@harmonygames.co/1837824433193834721"
IG = "frederick.stone@harmonygames.co/1839715197125206004"

def block_after(marker, new):
    global s
    i = s.index(marker); a = s.index("```\n", i) + 4; b = s.index("\n```", a)
    s = s[:a] + new + s[b:]

block_after("persona_view.py check-sql frederick_stone", rd('checksql.txt'))
block_after("tools/sql_lint.py Task_Authoring/task_inputs/01_Universe_Inject.sql`:", rd('sql_lint.txt'))
block_after("tools/base_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql`:", rd('base_check.txt'))
block_after("tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json", rd('hardness.txt'))

old = "| Inventory | PASS | 76 INSERT, 0 UPDATE, 0 DELETE, no upsert: gdrive 20, gsheets 38, gdocs 1, slack 4, trello 5, gmail 6, confluence 2 |"
assert old in s
s = s.replace(old, "| Inventory | PASS | 87 INSERT, 0 UPDATE, 0 DELETE, no upsert: gdrive 21, gsheets 41, gdocs 1, slack 5, trello 5, gmail 12, confluence 2 |")

# counter-readings for the round-2 records
anchor = "| Designed disagreement (claim) |"
new_rows = (
 "| Temporal | the Brand Account notice (Jun 11) is older than the Sep 30 export, so the export should win | the export's own Scope row is 'Studio channel permissions' (f_fc27672c5bfea8b760b074 #0) and the notice says Studio people are listed in Studio, not on the Brand Account list (" + YT + "); no base or seeded record removes [EMAIL_126620] from the Brand Account | PASS |\n"
 "| State / Lifecycle | TikTok partner access could have ended with Node's termination (Dec 20, 2024) | the reminder is dated 2025-07-16, after the termination (" + TT + "); Fred's Dec 20 cleanup covered Google Ads links and YouTube Studio only (f_ab70b02c329d038a72fb9f #1, f_fc27672c5bfea8b760b074 #1) | PASS |\n"
 "| Cross-service Referential | Node never asked for TikTok, so a TikTok partnership is invented | Node's Leadsie request C08MCEP1B9B/1728234009.536219 (Oct 6, 2024): 'Partner Access to Facebook, Google, TikTok and Shopify'; shared Oct 8, 2024, the day after Fred shared Meta (f_f7e7c5bf089029cee91175 #1, 2024-10-07) | PASS |\n"
 "| Semantic / Category | 'Full control' is not one of the card's holder roles (Owner, Admin, Super admin) | the notice says 'Full control (admin)' (" + IG + "); card rule 2 68dc406c7b0d03e53b334bab | PASS |\n"
 "| Unique ground truth | Instagram could still read SINGLE because the login is a personal address | card rule 3 makes the login not a company holder, but holders are Owner/Admin on a person's harmonygames.co login: the portfolio admins are two (" + IG + ") -> COMPANY-HELD; Arthur's summary C07C2866011/1759266627.118342 agrees | PASS |\n"
 "| Identifier / Format | anonymized sender tokens on vendor notices look planted | base vendor notices carry the same tokens: SVC_0065 on Google Accounts mail (frederick.stone@harmonygames.co/1809398634936399225), SVC_0009 on facebookmail and TikTok mail (frederick.stone@harmonygames.co/1843994863135585583) | PASS |\n")
assert anchor in s
s = s.replace(anchor, new_rows + anchor, 1)

rev6 = """### Revision 6 — baseline (six Opus rollouts, 07_Baseline_Trajectories) too easy, hardening round 2 (01a_Hardening_Report.md)

All six rollouts listed every tab of every export and read the YouTube Brand Account tab (run-6 #48) and the Instagram portfolio tab
(run-6 #29); none searched Gmail for access or ownership notices or for Node Media. Round 2 moves three custody facts out of the
exports into vendor notices in Fred's mailbox, each dated before every run's dated vendor search (after Aug 20–Sep 1):

| Change | Records | Answer effect | Why the runs missed it / would miss it |
|---|---|---|---|
| YouTube Brand Account tab removed; Google notice lists [EMAIL_126620] as Owner | f_fc27672c5bfea8b760b074; """ + YT + """ | unchanged truth (REVOKE); face reading now TRANSFER | the tab was on the first-read surface (6/6) |
| TikTok Scope row 'Account logins'; TikTok for Business partner reminder (Node Media LLC Admin) | f_2f0abe2f1f6726fef63f80; """ + TT + """; base C08MCEP1B9B/1728234009.536219 | TikTok TRANSFER -> OUTSIDE ACCESS / REVOKE | no run searched Node Media or partners in Gmail (run-3's partner query uses phrases the notice does not contain) |
| Instagram portfolio tab removed, note 'Login only'; Meta notice lists Leonard and Fred with full control | f_215ff8da73e4173f78515c; """ + IG + """ | unchanged truth (KEEP); face reading now TRANSFER | the tab was on the first-read surface (6/6) |

New totals: REVOKE 4 · TRANSFER 1 (X) · KEEP 5 · CLOSE 3; reply 1 TRANSFER, Node Media on Meta, Unity, YouTube and TikTok; checklist X
only. Coherence: no base record mentions a Brand Account, Node's address [EMAIL_126620] is in no base mail, and no base record removes Node from
TikTok; the three notices reuse the base sender tokens.

"""
anchor = "### Re-verified facts"
s = s.replace(anchor, rev6 + anchor, 1)

old_unres = s[s.index("Unresolved: (0) hardening round 1"):]
old_unres = old_unres[:old_unres.index("\n\n")]
s = s.replace(old_unres, "Unresolved: (0) hardening round 2 needs re-applied SQL, a new pre-check or baseline and /hardness; (1) whether the six-rollout average lands under 80% is\nunverified until the runs (prediction in 01a_Hardening_Report.md); (2) no red team ran on this injection (the endpoint is not configured).")
s = s.replace("Re-read from the sources in this stage: the DM D05S58U4SAK",
              "Round 2 re-read: the Node channel C08MCEP1B9B 2024-10 shard (Leadsie request /62, Page access /107–/110), Fred's Google Accounts and TikTok\nsender tokens, 'Brand Account' / 'full control' / [EMAIL_126620] base sweeps. Earlier: the DM D05S58U4SAK", 1)
# drop the stale pasted gate block; stage_gate --paste writes a fresh one
i = s.find("```\nSTAGE GATE injection: PASS")
if i >= 0:
    j = s.index("\n```", i + 4) + 4
    s = s[:i].rstrip('\n') + '\n' + s[j:].lstrip('\n')
open(P, 'w', encoding='utf-8').write(s)
print('ok')
