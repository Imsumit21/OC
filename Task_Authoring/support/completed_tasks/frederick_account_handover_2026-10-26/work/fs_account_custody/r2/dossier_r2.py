import sys
P = sys.argv[1]
s = open(P, encoding='utf-8').read()
YT = "frederick.stone@harmonygames.co/1834647853990444617"
TT = "frederick.stone@harmonygames.co/1837824433193834721"
IG = "frederick.stone@harmonygames.co/1839715197125206004"

def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (s.count(old), old[:80])
    s = s.replace(old, new)

rep("# Grounding Dossier — fs-account-custody (injection rev 4)", "# Grounding Dossier — fs-account-custody (injection rev 6, hardening round 2)")

# 1.D findability rows
rep('| "admob" | gmail | 200 base hit(s)',
    '| "Brand Account" | gmail | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gmail ' + YT + ' (Google notice), reached by a YouTube / Brand Account / [EMAIL_126620] mail search |\n'
    '| "Node Media" | gmail | 59 base hit(s) (scan_complete), first threads/00007026.json /messages/0/headers/26/value (2024 link notices) | gmail ' + TT + ' (TikTok partner reminder) is the only 2025 hit |\n'
    '| "full control" | gmail | 20+ base hit(s), all marketing copy (threads/00000459.json /messages/0/body) | gmail ' + IG + ' (Meta portfolio notice) |\n'
    '| "admob" | gmail | 200 base hit(s)')

# 1.E reach rows
rep("| d_6cae3483dd469c189a528e | gdrive | shared with the persona (reader) | LB |",
    "| " + YT + " | gmail | own mailbox (seeded) | LB |\n| " + TT + " | gmail | own mailbox (seeded) | LB |\n| " + IG + " | gmail | own mailbox (seeded) | LB |\n| d_6cae3483dd469c189a528e | gdrive | shared with the persona (reader) | LB |")

# 1.F collisions
rep("Sheets and Docs rows reuse their Drive ids (checked under gdrive).",
    "Round 2 (hardening): thread ids 1834647853990444617, 1837824433193834721, 1839715197125206004 — 0 filename hits over 88,726 thread files;\n"
    "Message-ID stems CsalywIzVSffkEGTDj2Cow, 25b931cc-8e32-759f, b1548908-9860-3c7e — 0 hits (`grep -rlF` over HarmonyGames_Gmail threads).\n"
    "Sender tokens reused from the base: SVC_0065 (Google Accounts, frederick.stone@harmonygames.co/1809398634936399225), SVC_0009\n"
    "(facebookmail / TikTok, frederick.stone@harmonygames.co/1843994863135585583).\n\n"
    "Sheets and Docs rows reuse their Drive ids (checked under gdrive).")

# 2 ledger
rep("| 21 | gsheets | sheets (Access) | f_2f0abe2f1f6726fef63f80 | cohort TikTok; T6; T13 |",
    "| 21 | gsheets | sheets (Access, Scope row 'Account logins') | f_2f0abe2f1f6726fef63f80 | cohort TikTok; T6; T13; T21 face reading |")
rep("| 22 | gsheets | sheets (Permissions, Removed users) | f_fc27672c5bfea8b760b074 | cohort YouTube; T6 |",
    "| 22 | gsheets | sheets (Permissions, Removed users) | f_fc27672c5bfea8b760b074 | cohort YouTube; T6; T16 apparent conclusion (C4 hop 1) |")
rep("| 25 | gsheets | sheets (Access) | f_215ff8da73e4173f78515c | cohort Instagram; T6; T14 |",
    "| 25 | gsheets | sheets (Access) | f_215ff8da73e4173f78515c | cohort Instagram; T6; T14; T18 face reading (C8 hop 1) |")
rep("| 33 | confluence | confluence_pages + page_versions | page_company_accounts_access | H1 decoy; T2 v1 | ● body | unscoped | decoy (oldest version) |",
    "| 33 | confluence | confluence_pages + page_versions | page_company_accounts_access | H1 decoy; T2 v1 | ● body | unscoped | decoy (oldest version) |\n"
    "| 34 | gmail | gmail.gmail_threads + gmail_messages | " + YT + " | T16 resolver; C4 hop 2 | ● body | own mailbox | overturning evidence |\n"
    "| 35 | gmail | gmail.gmail_threads + gmail_messages | " + TT + " | T21 resolver; C7 hop 2 | ● body | own mailbox | overturning evidence |\n"
    "| 36 | gmail | gmail.gmail_threads + gmail_messages | " + IG + " | T18 resolver; C8 hop 2 | ● body | own mailbox | overturning evidence |")
rep("Totals from `sql_lint.py`: 76 INSERT, 0 UPDATE over 7 schemas.", "Totals from `sql_lint.py`: 87 INSERT, 0 UPDATE over 7 schemas.")

# 3 findability
rep("| snowflake.json /tables/35 | snowflake query AD_REVENUE by network, 2025-09 |",
    "| " + YT + " | gmail search \"YouTube\" / \"Brand Account\" / \"[EMAIL_126620]\" (undated) | \"[EMAIL_126620] - Owner\"; \"People you add in YouTube Studio > Permissions are listed in Studio, not here\" | the export's Scope row 'Studio channel permissions' and Removed users tab (same address) are met first; dated 2025-06-11, before every baseline run's dated youtube search (after Aug 20) | overturning (T16, C4) |\n"
    "| " + TT + " | gmail search \"Node Media\" / \"tiktok\" (undated) / \"partner\" | \"Partner: Node Media LLC\", \"Permission: Admin\" | the export (Scope 'Account logins') is met first; base Node hits are 2024 link notices; Node's Leadsie request for TikTok partner access C08MCEP1B9B/1728234009.536219 | overturning (T21, C7) |\n"
    "| " + IG + " | gmail search \"instagram\" / \"harmonygames\" / \"business portfolio\" (undated) | \"Full control (admin)\" + both harmonygames.co logins | the export says 'Login only'; Arthur's C07C2866011/1759266627.118342 claims two holders on everything but YouTube and TikTok | overturning (T18, C8) |\n"
    "| snowflake.json /tables/35 | snowflake query AD_REVENUE by network, 2025-09 |")

# 5 lazy solver
rep("| Money from Gmail receipts only |",
    "| Read every export and every tab, trust them for holders | YouTube, TikTok, Instagram SINGLE → TRANSFER (4 TRANSFER); Node on Meta and Unity only | the exports state their scope (Studio permissions, account logins, login only); the three notices " + YT + ", " + TT + ", " + IG + " decide them |\n"
    "| Money from Gmail receipts only |")

# 6 disagreements
rep("| Deactivated AdMob vs the active one |",
    "| YouTube export (Node removed) vs Google's Brand Account notice | f_fc27672c5bfea8b760b074 Removed users; " + YT + " | removing an agency in Studio leaves its Brand Account role | the notice: the Brand Account list is separate from Studio, and the export's Scope row says Studio |\n"
    "| TikTok export (Fred's login only) vs TikTok Business Center | f_2f0abe2f1f6726fef63f80; " + TT + " | a login export does not list Business Center partners | the reminder (2025-07-16) names Node Media LLC as Admin; no removal record |\n"
    "| Instagram export (personal login) vs the portfolio | f_215ff8da73e4173f78515c; " + IG + " | the login and the portfolio admins are separate in Meta | the notice lists Leonard and Fred with full control |\n"
    "| Deactivated AdMob vs the active one |")

# 8 fact sheet
rep("| Unlinked / Removed (Node) | 2024-12-20 | date | f_ab70b02c329d038a72fb9f; f_63b42f52fa11d7df238a4e; f_fc27672c5bfea8b760b074 |",
    "| Unlinked / Removed (Node) | 2024-12-20 | date | f_ab70b02c329d038a72fb9f; f_63b42f52fa11d7df238a4e; f_fc27672c5bfea8b760b074 |\n"
    "| Deactivated AdMob publisher | pub-2341961509332343 | id | home f_e239ffb975eb7c66d7287d, f_4521c272960dd1836a5196 |\n"
    "| Ad revenue threshold | $100 | amount | D05S58U4SAK/1759272498.304117 |\n"
    "| Brand Account owner address | [EMAIL_126620] | id | home f_fc27672c5bfea8b760b074, f_b463693cd3779d4d25374f; must appear in " + YT + " |")
rep("FACT CHECK: PASS — 71 text-bearing rows, 4 declared facts, 5 declared superseded records",
    "FACT CHECK: PASS — 79 text-bearing rows, 7 declared facts, 6 declared superseded records")

# 9.1 records
rep("| f_2f0abe2f1f6726fef63f80 | seeded | TikTok @harmonygames: login frederick.stone@ Admin, Leonard signs in with it; @harmonygames.app deleted 2025-09-29 |",
    "| f_2f0abe2f1f6726fef63f80 | seeded | TikTok: Scope row 'Account logins'; @harmonygames: login frederick.stone@ Admin, Leonard signs in with it; @harmonygames.app deleted 2025-09-29 |")
rep("Removed users: Node Media LLC 2024-12-20 by Fred (Studio); tab 'Brand Account': Fred Primary owner, Node Media LLC [EMAIL_126620] Owner since 2024-11-21 |",
    "Removed users: Node Media LLC [EMAIL_126620] Manager, removed 2024-12-20 by Fred (Studio). No Brand Account tab (round 2) |")
rep("owner login [EMAIL_912045], Fred's personal gmail (note: login only, portfolio access on the next tab); tab 'Business portfolio access' (Domino Delights): Leonard Hayes, Frederick Stone Admin (full control) since 2024-10-08 |",
    "owner login [EMAIL_912045], Fred's personal gmail (note: 'Login only'). No portfolio tab (round 2) |")
rep("| D05S58U4SAK/1759272498.304117 | seeded |",
    "| " + YT + " | seeded | Google (SVC_0065) → Fred, 2025-06-11T15:42:18Z, 'Review who can manage Harmony Games': Brand Account Harmony Games (YouTube channel); Frederick Stone Primary owner; [EMAIL_126620] Owner; Studio permissions listed in Studio | own mailbox | LB overturning evidence (YouTube OUTSIDE ACCESS) | no |\n"
    "| " + TT + " | seeded | TikTok for Business (SVC_0009) → Fred, 2025-07-16T17:12:40Z, 'Partner reminder: Node Media LLC can manage @harmonygames': Business Center partner Node Media LLC, Admin, shared Oct 8, 2024 | own mailbox | LB overturning evidence (TikTok OUTSIDE ACCESS) | no |\n"
    "| " + IG + " | seeded | Meta (SVC_0009) → Fred, 2025-08-06T14:05:33Z, 'People with full control of @harmonygames': Domino Delights portfolio; Leonard Hayes and Frederick Stone Full control (admin), added Oct 8, 2024, harmonygames.co logins; partners none | own mailbox | LB overturning evidence (Instagram COMPANY-HELD) | no |\n"
    "| C08MCEP1B9B/1728234009.536219 | base | Node (PERSON_0498), 2024-10-06, Leadsie link 'Node Media is requesting Partner Access to Facebook, Google, TikTok and Shopify' | #node-external member | supporting (T21) | no |\n"
    "| D05S58U4SAK/1759272498.304117 | seeded |")

# 9.2 ground truth
rep("| TikTok (f_2f0abe2f1f6726fef63f80) | Frederick Stone | SINGLE | N | TRANSFER (comment 68dc529406d8087e5a6b8403) |",
    "| TikTok (f_2f0abe2f1f6726fef63f80) | Frederick Stone | OUTSIDE ACCESS (Node Media LLC Business Center partner, Admin: " + TT + ") | N | REVOKE |")
rep("| YouTube (f_fc27672c5bfea8b760b074) | Frederick Stone | OUTSIDE ACCESS (Node Media LLC Brand Account Owner) | N | REVOKE |",
    "| YouTube (f_fc27672c5bfea8b760b074) | Frederick Stone | OUTSIDE ACCESS (Node Media LLC's [EMAIL_126620] Brand Account Owner: " + YT + ") | N | REVOKE |")
rep("| Instagram (f_215ff8da73e4173f78515c) | Leonard Hayes, Frederick Stone (Business portfolio access tab) | COMPANY-HELD |",
    "| Instagram (f_215ff8da73e4173f78515c) | Leonard Hayes, Frederick Stone (portfolio full control: " + IG + ") | COMPANY-HELD |")
rep("""Totals: REVOKE 3 (Meta, Unity, YouTube), TRANSFER 2 (TikTok,
X), KEEP 5 (Google Ads 569, AppLovin, LinkedIn, Instagram, Discord), CLOSE 3 (Google Ads 449, adjoe, AdMob). Reply: 2 marked TRANSFER;
Node Media LLC still has access on the Meta ad account (partner admin), the Unity Ads advertiser (Admin) and the YouTube Brand Account (Owner).
Checklist on 67cf1b506d78ad3c72e02a35: TikTok, X.""",
"""Totals: REVOKE 4 (Meta, Unity, YouTube, TikTok), TRANSFER 1 (X),
KEEP 5 (Google Ads 569, AppLovin, LinkedIn, Instagram, Discord), CLOSE 3 (Google Ads 449, adjoe, AdMob). Reply: 1 marked TRANSFER (X);
Node Media LLC still has access on the Meta ad account (partner admin), the Unity Ads advertiser (Admin), the YouTube Brand Account (Owner)
and TikTok @harmonygames (Business Center partner, Admin). Checklist on 67cf1b506d78ad3c72e02a35: X only.""")

# 12 follow-ups
rep("- Second tabs: whether `gsheets_values_get` without a range returns only the first tab is confirmed in the Opus pre-check (the design\n  budgets a read per tab; no budget row is conditional).",
    "- Second tabs: the baseline runs listed every tab (run-6 #22–#38 gdrive_list_sheets on all exports) and read them by index; five exports keep a\n  second tab. Round 2 moved the YouTube Brand Account and Instagram portfolio facts out of the exports into Gmail (§ Revision 6).")
open(P, 'w', encoding='utf-8').write(s)
print('ok')
