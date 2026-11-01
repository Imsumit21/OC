# Scenario Design — fs-account-custody · design only · contains no prompt, OE or criterion text

Persona Frederick Stone (Co-founder, Executive) · competency Corporate Ops · task skill Analysis and synthesis · horizon Normal
(platform "Task Type": normal) · difficulty mode medium (V3 cap: six-rollout average strictly under 85%; the author's own target is
under 75%, design target about 65%) · universe date October 1, 2025 (V3 freeze 00:00 UTC = Tue Sep 30, 2025 5:00 PM PT).
Builder scripts: `support/task_work/fs_account_custody/` (`mint_ids.py` mints every id into `minted_ids.json`, `planned_text.json`
holds the seeded wording the delegation quotes come from, `build_manifest.py` writes the draft manifest). **v2** applies the
independent review of v1 (§13): AdMob added (13 accounts), the rules card moved after the sweep, Node's other access closed out in the
exports, holder logins made explicit, the hub's self-advertising pointers removed, a confident wrong summary by Arthur added, and the
AdMob money decided by warehouse ad revenue (Snowflake).

## 0 Assignment, persona census and horizon note

| Field | Assigned (verbatim, `00_Assigments.md`) | Resolution |
|---|---|---|
| persona | Frederick Stone | roster `frederick_stone`, frederick.stone@harmonygames.co, Executive (`Evals/references/persona/roster.json`) |
| role | Co-founder | runs the UA, ad-network and social accounts (`references/Persona_Briefs.md` §Frederick); YouTube owner per D05S58U4SAK/1759096868.688389 |
| business function | Executive | Evals category Founders / Exec / Strategy (`Evals/references/rules/task_categories.md`) |
| competency | Corporate Ops | company account custody and offboarding readiness before the planned cuts (C07C2866011/1758739409.488879) |
| task skill | Analysis and synthesis | 13 accounts × user exports (5 with a second tab), money evidence in Gmail, Slack and the warehouse, two rule sources and two amendments, reconciled into one register |
| horizon | normal | manifest `horizon: Normal Horizon`, `effective_profile: normal` (no exception) |
| universe date | October 1, 2025 07:00 | built on the Oct 1, 2025 freeze, treated as 00:00 UTC (V3 §3, the stricter cut-off); latest seed 2025-09-30T23:21:09Z |
| difficulty mode | medium | author target: average under 75% (design ~65%), ≥ 2 failure patterns, per-rollout SD 0.1–0.3 |

**Remit argument.** On Sep 24 Leonard told the founders "we have 2 months left before letting everyone go"
(C07C2866011/1758739409.488879). On Sep 28–29 the team found that the company TikTok login was tied to Frederick's address
(D05S58U4SAK/1759170013.491159), that only the YouTube owner could request live streaming and Leonard was only a manager
(D05S58U4SAK/1759096868.688389, C07C2866011/1759110509.707539), and Leonard deactivated one of Frederick's Slack accounts by accident
(C07C2866011/1759093544.175549). Frederick owns the marketing, UA and social accounts (Unity budget hand-off
C07C2866011/1759186080.203099; Meta receipts in his mailbox frederick.stone@harmonygames.co/1843428112007517388). A custody register of
those accounts, before people are let go, is the Corporate Ops work a UA co-founder is pulled into on Sep 30, 2025.

**Effective profile.** Normal Horizon → `effective_profile: normal`. The requester set their own targets (00_Assigments.md "Author
targets"): every run at 70 tool calls or more with no upper limit (V3 `references/Docs/11_V3_Changes.md` §4: "Exceeding the displayed
range is allowed"), and an average weighted pass rate under 75%. The honest necessary budget is 61 calls (§9; the v1 review judged
v1's 63 padded at ~45–60, so v2 removed the read-backs and absence searches and added only reads that decide a row). Ordinary
exploration (searching before finding, opening the decoys) adds to that; whether runs reach 70 is measured at the Opus pre-check.
The human-time estimate must still fit Normal (under about 8 hours).

Persona reach census (`python3 Task_Authoring/tools/persona_view.py reach frederick_stone --top 10`, verbatim):

```
REACH  Frederick Stone <frederick.stone@harmonygames.co>  Co-founder / Executive
clock 2025-10-01

SLACK  user=EMPLOYEE_0008_SLACK_ID  visible channels=106 {'public': 13, 'private': 34, 'mpim': 17, 'im': 42}  messages=172001  public-not-member (UNVERIFIED)=57
  persona posts=4841 last post=2025-10-24  last activity in visible channels=2026-02-13
  C07C2866011    executives                             private mem=9   msgs=28266  2024-07-11..2026-02-13
  C05H8KVNU67    game-design                            private mem=27  msgs=22751  2023-07-16..2025-10-06 archived
  C050WGU41HR    engineering-bots                       private mem=35  msgs=20306  2023-03-29..2026-02-11
  C05V5FNLB9V    god-bugs                               private mem=31  msgs=16889  2023-10-07..2026-02-11
  C0880U9751A    zombie-match3d                         private mem=25  msgs=16773  2025-01-09..2026-02-11
  C04UM32UWKD    investors                              private mem=8   msgs=6581   2023-03-18..2024-10-17
  C0553V44CE4    god-ui-ux                              private mem=30  msgs=5009   2023-04-21..2025-10-06 archived
  C08R27X0EAH    zombie-bugs                            private mem=23  msgs=4688   2025-05-06..2026-02-11
  C05KNDCHAAG    company-internal                       private mem=38  msgs=4605   2023-07-31..2026-02-11
  C04S28HSD0U    product                                private mem=21  msgs=4365   2023-03-02..2024-05-11 archived

GMAIL  mailbox=frederick.stone@harmonygames.co threads=5009 messages=5891 range=2024-06-25..2025-11-13
  threads by last-message month (recent): {'2025-06': 333, '2025-07': 249, '2025-08': 108, '2025-09': 177, '2025-10': 275, '2025-11': 89}
  top correspondents: SVC_0107_EMAIL (1870), SVC_4131_EMAIL (1531), leonard.hayes@harmonygames.co (594), robert@harmonygames.co (392), arthur.blake@harmonygames.co (314), SVC_0521_EMAIL (192), brian.foster@harmonygames.co (114), SVC_0009_EMAIL (103), SVC_5366_EMAIL (79), PERSON_5681_EMAIL (76)

GCAL  own=['frederick.stone@harmonygames.co'] shared=[] events=336 (distinct ical_uid 155, cancelled 31)
  last event before clock=2025-09-30T17:30:00Z  next after clock=2025-10-01T20:30:00Z
  by month: 2023-10:1 2024-07:1 2024-08:1 2024-09:65 2024-10:28 2024-11:27 2024-12:25 2025-01:28 2025-02:15 2025-03:7 2025-04:17 2025-05:25 2025-06:23 2025-07:22 2025-08:7 2025-09:22 2025-10:21 2026-01:1

DRIVE  owned=46 {'application/pdf': 12, 'application/vnd.google-apps.presentation': 12, 'application/vnd.google-apps.document': 8, 'application/json': 4, 'application/vnd.google-apps.spreadsheet': 4, 'folder': 2, 'text/plain': 2, 'text/csv': 2}
  shared-with=197 {'application/vnd.google-apps.document': 65, 'application/vnd.google-apps.spreadsheet': 33, 'text/plain': 28, 'application/pdf': 24, 'application/vnd.google-apps.presentation': 24, 'application/json': 21, 'text/csv': 2}
  shared by owner: {'Resource: -6481757892984311338': 102, 'Resource: 7240535625619857401': 43, 'leonard.hayes@harmonygames.co': 41, 'robert@harmonygames.co': 6, 'arthur.blake@harmonygames.co': 3, 'julia.lawson@harmonygames.co': 2}
  native visible: {'gdocs': 73, 'gsheets': 37, 'gslides': 36}  last modified visible=2026-01-12T17:47:18Z
  UNVERIFIED (domain/anyone, not owned/shared)=134 {'application/vnd.google-apps.document': 45, 'application/vnd.google-apps.spreadsheet': 38, 'application/pdf': 22, 'application/vnd.google-apps.presentation': 18, 'application/json': 11}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2025-10-24 (-23d), slack_visible_channels=2026-02-13 (-135d), gmail=2025-11-13 (-43d), gcal_last_event_before_clock=2025-09-30 (1d), drive_last_modified_visible=2026-01-12 (-103d)
```

Linear / GitHub / Trello identities: Trello member `4b4a68fc0fec0b254e4f9d8e` (Frederick), `2162c1ba310341bf318f48b7` (Arthur),
`PERSON_6094_TRELLO_USER_ID` (Leonard); Confluence `user_EMPLOYEE_0038` (Leonard), `user_EMPLOYEE_0025` (Arthur). No Linear or GitHub
record is used.

## 1 Storyline

**Arc.** After the Sep 28–29 TikTok/YouTube lockout, Arthur sweeps every platform's user list into one Drive folder on Sep 30
(19:50–20:31Z), posts handover rules for Frederick's accounts on Leonard's founder board (Trello "Harmony Games",
640643a3fd8f3ca308d9318e) at 20:41Z, posts a confident (wrong) summary in #executives at 21:10Z, adds a socials exemption as a card
comment at 21:58Z and, after the hub, replies by email on the rules' subject keeping one Google Ads account. Leonard's definition of
money moving for the cuts sits in his cash notes doc (edited 17:48Z), newer than his Sep 15 #executives remark. At 3:40 PM PT
(22:40Z) Leonard asks Frederick in their DM for the register: one row per account with who holds it, whether money is moving, and
the action; saved in the Company Ops folder, with a reply giving how many are marked TRANSFER and any outside access. The hub names
only the rules card, the sweep and the folder; the money definition, the comment, the email and the warehouse are reached from the card.

**Timeline placement** (`references/universe_kb/timeline.md`, clock 2025-10-01): the bridge outreach that begins 2025-09-03
(`gmail:leonard@harmonygames.co_1842219327413774622.json`) and the A16Z Speedrun rejection dated 2025-10-01
(`slack:C07C2866011:1759288987.503349`, after the freeze, not used) frame the cuts; the Season Pass merge 2025-09-15 (match3d#438) is
the ZM3D release the Unity campaigns promote (C07C2866011/1759186080.203099). The Oct 24 layoffs are after the freeze and are not
referenced.

**Anchors per service.**

| Service | Record | Role |
|---|---|---|
| slack | D05S58U4SAK/1759272012.507134 (seed) | hub, Leonard → Frederick, 2025-09-30T22:40:12Z |
| slack | D05S58U4SAK/1759187141.318207 (seed) | Leonard's wrong admin claim, 2025-09-29T23:05:41Z |
| slack | C07UCC631A6/1757346020.196019 (parent, 6 replies), /1757347560.891949, /1757349668.681539 | Adjoe accidental campaign, pause, written waiver (thread replies) |
| slack | C07C2866011/1759266627.118342 (seed) | Arthur's wrong summary, 2025-09-30T21:10:27Z |
| slack | D05S58U4SAK/1756147086.813789, /1756147145.162239 | Leonard's active AdMob account; Fred admitted Aug 25 |
| snowflake | ANALYTICS.MONETIZATION.AD_REVENUE (snowflake.json /tables/35) | paid ad revenue Sep 2025: admob, applovin, meta_audience |
| slack | C07C2866011/1759186080.203099, /1759264050.305069; D05S58U4SAK/1758922541.613439 | Unity iOS campaigns on Sep 29–30; FB campaign off Sep 26 |
| trello | 68dc406c7b0d03e53b334bab (seed) on 640643a3fd8f3ca308d9318e | H1 handover rules card; comment 68dc529406d8087e5a6b8403 (seed) |
| trello | 68dc42f3095ad95194a711ae (seed) | same-board engineering decoy |
| trello | 67cf1b506d78ad3c72e02a35 (base, UA/BD board) | "Lock up social handles and domain?" — W4 target |
| trello | 670010236b89198587ca45b6 (base) | "Access to meta and Google Ad account shared with Node" (Oct 2024) |
| gmail | frederick.stone@harmonygames.co/1844732985606656293 (seed) | Arthur's Google Ads amendment |
| gmail | frederick.stone@harmonygames.co/1843428112007517388, /1843223812315546201 | Meta receipt Sep 16; AppLovin payout Sep 14 |
| gmail | frederick.stone@harmonygames.co/1835153849970828373, /1838369017520543217 | Google Ads 569-350-5790 (Harmony Games, Inc.); 449-481-1590 ads "funded by Calmplay LLC" |
| gdrive | f_6cae3483dd469c189a528e (seed) | "Admin sweep - Sep 30" folder with 16 exports |
| gdrive | f_21f9e11d43739eaef26b38 (seed) | "Company Ops" folder (destination) |
| gsheets | f_1191b7f8c96419e1f4dc88 … (16 seeds) | per-platform user exports |
| gsheets | f_4521c272960dd1836a5196 (seed) | Fred's "Marketing & UA logins" (Mar 10, 2025) |
| gdocs | f_c612c0e68a27b3330eb46a (seed) | Leonard's "Runway & shutdown cash notes" (H2) |
| confluence | page_company_accounts_access (seed) | "Company Accounts & Access" (2024, superseded) |

**Cohort.** `cohorts.json`: no fit — the 191 natural sets are Linear, GitHub, Slack and Gmail-bot populations; none is a set of
company accounts. The cohort is source-defined by H1 rule 1 over the sweep folder f_6cae3483dd469c189a528e.

**Natural traps used** (`references/universe_kb/trap_catalog.json`): K02 (app-name lineage: the Calm Play LLC entity behind ZM3D's
store and ad accounts, C07C2866011/1752552076.522209), P01 (shared first names: Brian Cooper / Brian Foster in Frederick's mail;
not used as a holder), C01 (replies that correct: the Adjoe waiver is only in a reply, C07UCC631A6/1757349668.681539), D04 (lookalike
spreadsheets: the March logins sheet vs the sweep exports), X04 (company name masked unevenly — "[SOURCE_ORG_0001], Inc." in the
Google Ads mails frederick.stone@harmonygames.co/1835153849970828373), B02 (automated senders: Google Ads SVC_0516, Meta SVC_0521).

**Originality.** Not the Combo Fighters launch record, the 133-PR register, the RC-flag gate or the art-canon handoff; not the
previous Frederick tasks (card-spend run-rate, paid-UA true-up): no spend totals, no categories, no ledger. The deliverable is a
custody classification of accounts.

## 1a Coherence audit

Scope = every record a correct run opens: the hub and claim (DM), the adjoe channel thread, the #executives Unity messages, the H1
card + comment, the engineering card, the handles card, the Node access card, Arthur's email, the cash notes doc, the 16 exports, Snowflake AD_REVENUE, the
March sheet, the Confluence page, the Meta / AppLovin / Google Ads / AdMob / LevelPlay mails. Known hazards walked from
`references/universe_kb/coherence_hazards.json` (all six categories).

| Record | Category | Fields | Evidence pointer | Hazard id | Disposition |
|---|---|---|---|---|---|
| Post-freeze base records (Adjoe Oct 1 invoice; Google Ads 449 cancellation Oct 16; Meta receipt Oct 6) | temporal | dates after 2025-10-01 | frederick.stone@harmonygames.co/1844773822453719122; /1846207913166171315; /1845217497507372901 | T07 | avoid: no requirement reads them; designed answers (Adjoe no cost; 449 CLOSE; Meta money moving) agree with them |
| Seeded Confluence page by Leonard dated 2024-03-12 | temporal | created_at vs author activity | confluence:page_company_accounts_access (planned) | T08 | avoid: Leonard active in Mar 2024 (activity.json); no edits after his activity |
| Seeded Trello card ids | temporal | id timestamp vs action date | trello:68dc406c7b0d03e53b334bab, 68dc42f3095ad95194a711ae, 68dc529406d8087e5a6b8403 | T06 | fold in: ids minted from their own timestamps (`mint_ids.py`); card dateLastActivity = comment time |
| Frederick is_founder=false in PAYROLL_ROSTER | semantic | roster vs "Co-founder" | snowflake.json /tables/39 (PAYROLL_ROSTER) | S05 | avoid: not read; the prompt uses the assigned role only |
| Calm Play LLC vs Harmony Games naming | semantic | entity on store/ad accounts | C07C2866011/1752552076.522209; frederick.stone@harmonygames.co/1838369017520543217 | S06 | fold in as T8: the exports and Arthur's email name both entities and customer IDs |
| Slack links to Google files use native ids | cross-service referential | docs.google.com ids ≠ f_ ids | C08H78VJG80/1759174925.309129 | R04 | avoid: no seeded text carries a Google URL; records are named by title |
| UA claims vs warehouse (Unity Sep spend $0 in AD_SPEND_DAILY while Slack shows campaigns on) | quantitative | spend vs Slack | snowflake.json /tables/0 (AD_SPEND_DAILY); C07C2866011/1759186080.203099 | Q08 | avoid: AD_SPEND_DAILY is neither cited nor modified; money moving is decided by switched-on campaigns, receipts, payouts, paid ad revenue and waivers (H2); Unity's answer is the same either way (campaign on) |
| Mirrored warehouse tables | quantitative | row-by-row | snowflake.json /tables/0, /tables/34 (AD_SPEND_DAILY, AD_SPEND) | Q09 | avoid: not read or modified |
| Thread reply counters on the adjoe parent | quantitative | reply_count | C07UCC631A6/1757346020.196019 | Q01 | avoid: no seeded reply on that thread (6 base replies) |
| AdMob paid revenue in AD_REVENUE vs no AdMob mail in September | quantitative | accrued_vs_paid | snowflake.json /tables/35 | Q09 | fold in (C5): the only September AdMob money; nothing contradicts it |
| Done-list cards with open checklists | state/lifecycle | list vs checklist | trello:67cf1b506d78ad3c72e02a35 | L12 | avoid: the handles card is in "ZM 3d Technical Launch / Alpha", not Done; W4 adds an open checklist there |
| Token mailbox SVC_0009 forwards AppLovin payout mails ("Dear Leonard Hayes") | identifier/format | sender token | frederick.stone@harmonygames.co/1843223812315546201 | I05 | fold in: the export lists Leonard and Frederick as AppLovin admins, so the salutation agrees |
| Mixed Gmail date formats | identifier/format | RFC-2822 vs ISO | frederick.stone@harmonygames.co/1843428112007517388 | I04 | avoid: seeded mail uses the base RFC-2822 header form |
| Leonard is a token on Trello | identifier/format | member id | trello member PERSON_6094_TRELLO_USER_ID | I17 | fold in: seeded Trello actions are Arthur's (2162c1ba310341bf318f48b7); Leonard is named in text only |
| other: Brian Cooper / Brian Foster naming | other | display name | frederick.stone@harmonygames.co/1823332883409810377 | S04 | avoid: no Brian is a holder on any export |

**Sibling-defect sweep.** For each designed defect, other records with the same kind in scope:
- *Outside access:* Node was given or asked for access to Meta and Google Ads (trello:670010236b89198587ca45b6; C08MCEP1B9B/1727063903.359939), YouTube (C08MCEP1B9B/1732203251.229079) and the MMP (C08MCEP1B9B/1727689480.986899), and was terminated on 2024-12-20 (D05S58U4SAK/1734719973.099339) with no record of access removal. v2 closes this in the exports: the Google Ads 569/449 "Linked managers" tabs and the YouTube "Removed users" tab record Node unlinked/removed on 2024-12-20 by Frederick; Unity has no outside member; Singular is out of scope; only the Meta "Partners" tab still lists Node Media LLC (designed).
- *A holder who is not a company holder:* YouTube manager (D05S58U4SAK/1759096868.688389), TikTok shared login (D05S58U4SAK/1759170013.491159), Unity pending invite, Instagram personal address; LinkedIn and Discord were checked against base — Leonard added Frederick to the LinkedIn page (C07KRTX5SCE/1726169948.231349) and made the founders Discord admins (C07C2866011/1734154451.509769); v2 exports give every holder's login address, so both are COMPANY-HELD.
- *A second TikTok account:* Frederick created a new TikTok account on the ads@ group inbox on Sep 29 (D05S58U4SAK/1759155793.573669) before recovering the old one; v2's TikTok export lists the recovered @harmonygames profile (login frederick.stone@harmonygames.co) and the Sep 29 account as deleted 2025-09-29 — off the list under rule 1.
- *Money that is not spend:* Meta "RE: meta Invoice" mails are Audience Network payouts (frederick.stone@harmonygames.co/1842698832158940633); they only add to Meta's Y, and Meta is REVOKE whatever money says.
- *A closed account vs a live one:* AdMob pub-2341961509332343 was deactivated 2025-08-24 (frederick.stone@harmonygames.co/1841349862518331350); Leonard's active AdMob account admitted Frederick as admin on 2025-08-25 (D05S58U4SAK/1756147086.813789, frederick.stone@harmonygames.co/1841453218828344296). v1 wrongly left AdMob out; v2 has the active account in the sweep (T15). ironSource/LevelPlay (frederick.stone@harmonygames.co/1837038650805365569) is a MAX bidder — excluded by rule 1 (T10).
- *Adjoe unpaid June invoice:* the Aug 4 reminder (frederick.stone@harmonygames.co/1839518563856917373) was paid in August (C04UEQVDVB7/1755117283.864129, not visible to Frederick); no rule uses unpaid bills, so no row depends on it.
- *Google Ads campaign status:* the Sep 17 EU political-ads mail (frederick.stone@harmonygames.co/1843521869285707849) mentions campaigns; Google UAC spend last ran 2025-04-10 (snowflake.json /tables/0); v2 exports state "enabled campaigns: 0" for both IDs.

## 1b Active speakers

Every person given a seeded voice, with `status_at_clock` from `references/universe_kb/activity.json` (clock 2025-10-01).

| Person | Email | status_at_clock (activity.json) | Seeding role |
|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025 | hub + claim (Slack DM), 90-day remark (#executives), cash notes (Docs), Company Ops folder (Drive), 2024 Confluence page |
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025 | H1 card + comment and engineering card (Trello), sweep folder + 16 exports (Drive/Sheets), #executives sweep summary (Slack), Google Ads email (Gmail) |
| Frederick Stone | frederick.stone@harmonygames.co | active_sep_2025 | persona; owner of the March logins sheet (Sheets) |

Seeded text follows `references/universe_kb/conventions.json` (DM messages lowercase, median ~38–66 characters except the hub;
Arthur's card prose short numbered lines). Platform export rows are data, not speech.

## 1c Identity traps

`python3 Task_Authoring/tools/entity.py collisions` (verbatim, first sections) and `resolve` for every person the design names:

```

SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <marcus@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']

SHARED_LAST_NAMES (5)
  baker: ['Owen Baker <owen.baker@harmonygames.co> [persona owen_baker]', 'Thomas Baker <thomas.baker@harmonygames.co>']
  bennett: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Oscar Bennett <oscar.bennett@harmonygames.co>']
  brooks: ['Lauren Brooks <lauren@harmonygames.co>', 'Oliver Brooks <oliver.brooks@harmonygames.co> [persona oliver_brooks]']
  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']
  price: ['Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]', 'Nathan Price <nathan@harmonygames.co>']

LOOKALIKE_HANDLES_AND_ALIASES (15)
  - Gmail thread files of arthur.blake@harmonygames.co are named 'blake@harmonygames.co_*'
  - Gmail thread files of brian.foster@harmonygames.co are named 'brian@harmonygames.co_*'
  - Gmail thread files of calvin.price@harmonygames.co are named 'calvin@harmonygames.co_*'
  - Gmail thread files of claire.morgan@harmonygames.co are named 'claire@harmonygames.co_*'
  - Gmail thread files of frederick.stone@harmonygames.co are named 'frederick@harmonygames.co_*'
  - Gmail thread files of julia.lawson@harmonygames.co are named 'jlawson@harmonygames.co_*'
  - Gmail thread files of leonard.hayes@harmonygames.co are named 'leonard@harmonygames.co_*'
  - Gmail thread files of oliver.brooks@harmonygames.co are named 'oliver@harmonygames.co_*'
  - Gmail thread files of owen.baker@harmonygames.co are named 'owen@harmonygames.co_*'
  - Gmail thread files of samuel.turner@harmonygames.co are named 'samuel@harmonygames.co_*'
  - Gmail thread files of simon.walker@harmonygames.co are named 'simon@harmonygames.co_*'
  - Gmail thread files of vincent.parker@harmonygames.co are named 'vincent@harmonygames.co_*'
  - Gmail thread files of felix.young@harmonygames.co are named 'felixyoung@harmonygames.co_*'
  - Gmail thread files of oscar.bennett@harmonygames.co are named 'oscar@harmonygames.co_*'
  - Slack handle 'thomas' (U05F0A0D12F) belongs to Thomas Baker <thomas.baker@harmonygames.co> but equals the mailbox local part of Thomas <thomas@harmonygames.co> [persona thomas]

LOOKALIKE_EMAIL_LOCAL_PARTS (4)
  - 'marcus@' vs 'marcus.bennett@': ['Marcus <marcus@harmonygames.co>'] / ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]']
  - 'marcus@' vs 'marcus.lee@': ['Marcus <marcus@harmonygames.co>'] / ['Marcus Lee <marcus.lee@harmonygames.co>']
  - 'thomas@' vs 'thomas.baker@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['Thomas Baker <thomas.baker@harmonygames.co>']
  - 'thomas@' vs 'thomaslee@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['? <thomaslee@harmonygames.co>']

ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
ENTITY email:frederick.stone@harmonygames.co  name=Frederick Stone  kind=person  emails=['frederick.stone@harmonygames.co']
```

Correct entity vs lookalikes: Leonard Hayes is `leonard.hayes@harmonygames.co` (mailbox files `leonard@…`), Arthur Blake is
`arthur.blake@harmonygames.co` (mailbox files `blake@…`), Frederick is `frederick.stone@harmonygames.co` (files `frederick@…`). The
exports list holders by full address, so no shared first name decides a row. Node Media LLC is the agency Frederick terminated on
2024-12-20 (C07C2866011/1734721828.378119; D05S58U4SAK/1734719973.099339).

## 2 Cohort spine

**Rule (H1 rule 1).** Every marketing, UA, ad-monetization and social account in today's sweep folder (f_6cae3483dd469c189a528e) that has Frederick on
it in any role; store accounts and data tools are on the engineering card; MAX-only bidders are not separate accounts; accounts deleted
or deactivated before the sweep are off. The folder holds 16 exports; 13 are in scope.

**Per-account truth** (planned export content; money evidence is base unless marked seed):

| # | Account (export) | Company holders | Class | Money moving (Sep 2025) | Action | Evidence |
|---|---|---|---|---|---|---|
| 1 | Meta ad account "Harmony Games" (f_f7e7c5bf089029cee91175) | Frederick (Admin) — Leonard is Advertiser; Partners tab: Node Media LLC, partner admin | OUTSIDE ACCESS | Y (receipt Sep 16; FB campaign off Sep 26) | REVOKE | frederick.stone@harmonygames.co/1843428112007517388; D05S58U4SAK/1758922541.613439 |
| 2 | Google Ads 569-350-5790 Harmony Games, Inc. (f_ab70b02c329d038a72fb9f) | Frederick, Leonard (Admin); Linked managers tab: Node MCC unlinked 2024-12-20 | COMPANY-HELD | N (0 enabled campaigns; UAC last spend 2025-04-10) | KEEP (Arthur's email) | frederick.stone@harmonygames.co/1835153849970828373; frederick.stone@harmonygames.co/1844732985606656293 |
| 3 | Google Ads 449-481-1590 Calm Play LLC (f_63b42f52fa11d7df238a4e) | Frederick (Admin) — Leonard Standard; Node MCC unlinked 2024-12-20 | SINGLE | N | CLOSE | frederick.stone@harmonygames.co/1838369017520543217 |
| 4 | Unity Ads org Calm Play LLC (f_1191b7f8c96419e1f4dc88) | Frederick (Owner) — Leonard Manager; Invites tab: Arthur, Owner, pending | SINGLE | Y (iOS campaigns on Sep 29–30) | TRANSFER | C07C2866011/1759186080.203099; /1759264050.305069 |
| 5 | AppLovin (f_3996bca752549d3512bfbc) | Leonard, Frederick (Admin) | COMPANY-HELD | Y (payout Sep 14; paid revenue Sep) | KEEP | frederick.stone@harmonygames.co/1843223812315546201 |
| 6 | adjoe advertiser dashboard (f_a552317a929102385c0393) | Frederick, Leonard (Admin) | COMPANY-HELD | N (Sep installs waived in writing; paused Sep 8) | CLOSE | C07UCC631A6/1757349668.681539; /1757347560.891949 |
| 7 | AdMob (Leonard's active account) (f_50ff132ac88169019feeca) | Leonard, Frederick (Admin) | COMPANY-HELD | Y (AD_REVENUE admob Sep rows paid) | KEEP | snowflake.json /tables/35; D05S58U4SAK/1756147086.813789 |
| 8 | TikTok @harmonygames profile (f_2f0abe2f1f6726fef63f80) | Frederick (Admin, frederick.stone@ login) — Leonard uses Fred's login; Sep 29 account deleted | SINGLE | N | TRANSFER (social) | D05S58U4SAK/1759170013.491159; /1759155793.573669 |
| 9 | YouTube channel (f_fc27672c5bfea8b760b074) | Frederick (Owner) — Leonard Manager; Removed tab: Node 2024-12-20 | SINGLE | N | TRANSFER (social) | D05S58U4SAK/1759096868.688389; C08MCEP1B9B/1732203251.229079 |
| 10 | LinkedIn page (f_b89c1c70489f81031bdd4f) | Leonard, Frederick (Super admin) | COMPANY-HELD | N | KEEP (social) | C07KRTX5SCE/1726169948.231349 |
| 11 | X account (f_99d66f33c54338e70f5ed2) | Frederick (Owner) | SINGLE | N | TRANSFER (social) | seed export only |
| 12 | Instagram (f_215ff8da73e4173f78515c) | none — owner login is Frederick's personal Gmail address | SINGLE | N | TRANSFER (social) | seed export only |
| 13 | Discord server (f_2cecf2f81045ec401feb61) | Leonard (Owner), Frederick, Robert (Admin), all harmonygames.co logins | COMPANY-HELD | N | KEEP (social) | C07C2866011/1734154451.509769 |
| — | Play Console (f_5f2f52786dcd8e1168cd40), App Store Connect (f_ad393ed61590f2d22c6cd7), Singular (f_b463693cd3779d4d25374f) | — | out of scope (engineering card) | — | — | H1 rule 1 |

Totals the deliverables carry: REVOKE 1 · TRANSFER 5 (Unity, TikTok, YouTube, X, Instagram) · KEEP 5 · CLOSE 2; social transfers for
the handles card 4 (TikTok, YouTube, X, Instagram).

**Surfaces and shortcut audit.**

| Surface | Per-record call | Bulk call that does not cover it | Requirement · decides |
|---|---|---|---|
| per-platform export (f_f7e7c5bf089029cee91175 … 13 in scope; second tab on 5) | `gsheets_values_get` / `gsheets_get_spreadsheet` × 18 | `gsheets_values_batch_get` reads one spreadsheet; `gdrive_list_files` returns names only; a first-tab read misses the second tab | R2 · company holders |
| money evidence (Gmail) | `gmail_search_messages` per paid platform (7) | no one query spans SVC_0521 Meta, SVC_0009 AppLovin, SVC_0516 Google Ads, Adjoe, Unity | R4 · money moving (Y/N) |
| campaign state / waiver (Slack) | `slack_conversations_replies` on the adjoe thread; DM / #executives reads | channel history returns parents only; the waiver is a reply | R4 · money moving (Y/N) |
| paid ad revenue (Snowflake) | one query, mapped per account | gives networks, not accounts; only AdMob depends on it | R4 · money moving (Y/N) |

**Short-circuit audit.** Holders decide the class only together with the second tabs (Meta partner, Unity invite) and the scope
clause; money decides CLOSE for any class but OUTSIDE ACCESS; the socials exemption and the Google Ads amendment override CLOSE for
seven rows. A run that reads holders only gets the CLOSE rows wrong; a run that reads money only gets every class wrong.

**Predicate details.** Closed vocabulary (classes OUTSIDE ACCESS / SINGLE / COMPANY-HELD; actions REVOKE / CLOSE / TRANSFER / KEEP);
holder = Owner, Admin or Super admin; company holder = a person's harmonygames.co login; order REVOKE → CLOSE → TRANSFER/KEEP.
**House rule overriding the natural reading (A15):** a manager, a pending invite, a shared login, a group inbox or a personal
address is not a company holder, so four accounts that look shared are SINGLE. **Dual regime:** none. **Boundary records (A17):** the
deactivated AdMob vs the active one; the Calm Play Google Ads, X, Instagram and Discord missing from the March sheet; three
out-of-scope exports inside the sweep folder; the deleted Sep 29 TikTok account.

## 3 Hidden authorities

| Id | Name (how it is reached) | Home | Governs | Decoy(s) | Decoy scope / supersession | Findability proof |
|---|---|---|---|---|---|---|
| H1 | Arthur's account handover rules ("arthur's handover rules are on the ops board", D05S58U4SAK/1759272012.507134) | trello 68dc406c7b0d03e53b334bab + comment 68dc529406d8087e5a6b8403; reply frederick.stone@harmonygames.co/1844732985606656293 | R1, R2, R3, R5, R8 | same-board engineering card 68dc42f3095ad95194a711ae; Confluence page_company_accounts_access | 68dc42f3095ad95194a711ae: team scope (engineering, store, data-tool accounts); page_company_accounts_access: older version (T2 version_records) | a Trello search "handover rules" returns both cards (same title stem); proven at injection with `hg.py search search trello "handover rules"` |
| H2 | Leonard's definition of money moving for the cuts (card rule 5: "Money moving is whatever Leonard defined it as for the cuts", trello:68dc406c7b0d03e53b334bab) | gdocs f_c612c0e68a27b3330eb46a section "Money still moving (for the cuts)" | R4 | #executives remark C07C2866011/1757962953.240719 (seed, Sep 15, "for the cuts list") | older version by the same author (T3 version_records) | a search for "for the cuts" or "money moving" returns both; the doc is newer |

`governs` lists do not overlap. The hub names only H1; H2, the comment and the email are reached from the card (its rule 5, its
comment thread, and Gmail replies carrying the card's title as subject).

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Leonard's account handover ask | slack D05S58U4SAK/1759272012.507134 |

**Hub** = A1 (Leonard's voice) delegating to H1, the sweep and the destination folder.

**Incorporation table** (quotes are exact substrings of `planned_text.json`; the gate re-reads them from the SQL at injection):

| Fragment | Service · container | Kind | Chain | delegated_by_record | delegation_quote | Requirements | Names |
|---|---|---|---|---|---|---|---|
| K1 | slack · D05S58U4SAK/1759272012.507134 | delegation | A1 | D05S58U4SAK/1759272012.507134 | "reply here with how many you've marked TRANSFER and anything an outsider still has access to" | R6 | H1 |
| K2 | trello · 68dc406c7b0d03e53b334bab | requirement | A1 | D05S58U4SAK/1759272012.507134 | "arthur's handover rules are on the ops board, they decide the action" | R1 R2 R3 R5 | H2 |
| K3 | trello · 68dc529406d8087e5a6b8403 | amendment | A1→K2 | trello:68dc406c7b0d03e53b334bab | "For Fred's accounts before the cuts." (the comment sits on this card) | R5 | — |
| K4 | gmail · frederick.stone@harmonygames.co/1844732985606656293 | amendment | A1→K2 | trello:68dc406c7b0d03e53b334bab | "For Fred's accounts before the cuts." (Arthur's reply on the card's subject) | R5 | — |
| K5 | gdocs · f_c612c0e68a27b3330eb46a | requirement | A1→K2 | trello:68dc406c7b0d03e53b334bab | "Money moving is whatever Leonard defined it as for the cuts" | R4 | — |
| K6 | gdrive · f_6cae3483dd469c189a528e | requirement | A1 | D05S58U4SAK/1759272012.507134 | "arthur's sweep from today is the list" | R1 R2 | — |
| K7 | gdrive · f_21f9e11d43739eaef26b38 | destination | A1 | D05S58U4SAK/1759272012.507134 | "save the register in the Company Ops folder" | R7 | — |
| K8 | trello · 67cf1b506d78ad3c72e02a35 | destination | A1→K2 | trello:68dc406c7b0d03e53b334bab | "Socials that need a transfer go as a checklist on Fred's" | R8 | — |

**Amendments.** K3 (Trello comment, 2025-09-30T21:58:44Z) changes rule 5 for socials only; K4 (Gmail reply, 2025-09-30T23:21:09Z,
subject "Re: Account handover rules - marketing, UA & socials") changes rule 5 for one named Google Ads account; both say the rest
stands. Neither is announced by the hub or the card (later applicable updates supersede without announcement, `Evals/WORKFLOW.md`
`prompt-incorporation-v1`); K4 is from the rules' author on the rules' own subject, addressed to Frederick and Leonard.

**Non-authoritative instruction distractors.** The #executives 90-day remark (seed, C07C2866011/1757962953.240719) is Leonard's earlier view,
superseded by his own doc; the engineering card's "One Owner is fine … mark each one KEEP or MOVE" governs another team's list; Arthur's
#executives summary (C07C2866011/1759266627.118342) is a claim, not a rule.

## 5 Chains and trap register

**Chains** (manifest `chains`): C1 A1 (Arthur's summary → Unity export with the pending invite on its Invites tab → card rule 2 → Unity
TRANSFER); C2 A9 (Adjoe accidental campaign → rep's waiver reply → H2 waiver clause → Adjoe CLOSE); C3 A13 (card rule 5 CLOSE → Arthur's
email reply → the 569 export → 569 KEEP, 449 CLOSE); C4 A17 (March sheet → sweep folder → card scope → the 13 accounts); C5 A19 (card
rule 5 → doc revenue clause → AD_REVENUE admob paid Sep → AdMob KEEP).

| Trap | Family | Records | Requirement | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T1 | superseding | D05S58U4SAK/1759187141.318207 → f_1191b7f8c96419e1f4dc88, f_f7e7c5bf089029cee91175, f_63b42f52fa11d7df238a4e | R2 | Leonard counted as admin on Meta, Calm Play Google Ads, Unity | newer exports (Sep 30) | claim sits above the hub in the DM |
| T2 | superseding (4 versions) | page_company_accounts_access → 68dc406c7b0d03e53b334bab → 68dc529406d8087e5a6b8403 → frederick.stone@harmonygames.co/1844732985606656293 | R5 | 2024 page or card alone applied | card replaces page; comment; email | Confluence search returns the page first; comment and email are unannounced |
| T3 | superseding | C07C2866011/1757962953.240719 → f_c612c0e68a27b3330eb46a | R4 | 90-day paid rule keeps Adjoe | newer definition by the same author | a Slack search for "for the cuts" hits the remark first |
| T4 | distractor · partial_listing | f_4521c272960dd1836a5196 | R1 | register built from the March sheet | hub: the sweep from today is the list | the March sheet is Frederick's own and titled "logins" |
| T5 | distractor · scope_adjacent | 68dc42f3095ad95194a711ae | R3 | one-owner-is-fine rule applied | engineering scope | same Trello search |
| T6 | exact_predicate | f_1191b7f8c96419e1f4dc88, f_fc27672c5bfea8b760b074, f_2f0abe2f1f6726fef63f80, f_215ff8da73e4173f78515c; D05S58U4SAK/1759096868.688389 | R3 | manager / pending / shared / personal counted | card rules 2–3 | — |
| T7 | eliminating_evidence | C07UCC631A6/1757346020.196019 → /1757349668.681539 | R4 | Adjoe money moving | waiver in the reply | parent visible, reply not |
| T8 | entity_collision | f_ab70b02c329d038a72fb9f, f_63b42f52fa11d7df238a4e; frederick.stone@harmonygames.co/1838369017520543217 | R5 | one Google Ads, or the wrong one kept | customer IDs in the email and exports | the March sheet says "Google Ads" |
| T9 | tool_surface | f_f7e7c5bf089029cee91175 (Partners tab); trello:670010236b89198587ca45b6 | R3 | Meta SINGLE → TRANSFER | Partners tab lists Node Media LLC | a first-tab read shows People only |
| T10 | scope_alias | f_5f2f52786dcd8e1168cd40, f_ad393ed61590f2d22c6cd7, f_b463693cd3779d4d25374f; frederick.stone@harmonygames.co/1837038650805365569 | R1 | stores / Singular / ironSource added | card rule 1 | exports sit in the same folder |
| T11 | reuse_exclusion | trello:67cf1b506d78ad3c72e02a35 | R8 | new card for socials | card rule 7 | — |
| T12 | distractor · keyword_collision | C08H78VJG80/1759174925.309129; frederick.stone@harmonygames.co/1840501641217286806 | R1 | PlayableX / Balancy listed as accounts | no export in the sweep | vendor threads are recent |
| T13 | distractor · stale_summary | C07C2866011/1759110509.707539 → D05S58U4SAK/1759170013.491159 | R1 | TikTok dropped ("doesn't exist anymore") | same-day recovery + export | #executives message first |
| T14 | stale_summary | C07C2866011/1759266627.118342; f_1191b7f8c96419e1f4dc88, f_99d66f33c54338e70f5ed2, f_215ff8da73e4173f78515c, f_f7e7c5bf089029cee91175 | R3 | only YouTube and TikTok SINGLE | exports under rules 2–4 | the summary is the newest #executives message about the sweep |
| T15 | entity_collision | f_50ff132ac88169019feeca; frederick.stone@harmonygames.co/1841349862518331350; D05S58U4SAK/1756147086.813789 | R1 | AdMob dropped as deactivated | the deactivated pub id is a different account | the deactivation mail is the top AdMob search hit |

Trap independence: T6 and T9 fail different rows (T6 four accounts, T9 Meta); T7 and T3 hit Adjoe through different sources; T8 is
independent of T2 (a run can read the email and still keep the wrong Google Ads account); C5 fails only AdMob. No record states a
conclusion: the exports list users, roles and invites; the doc defines money; the replies state facts; Arthur's summary is wrong.

## 6 Failure-diversity plan

| Chain / trap | Runs that plausibly miss it | Rows it touches |
|---|---|---|
| C1/T1/T6/T14 (holder rules) | runs that trust Arthur's or Leonard's summary, count managers, or read only first tabs | Unity, YouTube, TikTok, X, Instagram class + action |
| T9 (Partners tab) | runs that read the first tab of each export | Meta class + action + the reply's outside-access clause |
| C2/T7 (waiver reply) | runs that never open thread replies (A14: 67/124) | Adjoe money + action |
| C3/T2 (comment + email) | runs that read the card description only, or never search Gmail for replies (A13) | 569 action; dormant socials |
| C5 (warehouse revenue) | runs that never query Snowflake (46/131) | AdMob money + action |
| T3 (definition) | runs that take the first "for the cuts" hit | Adjoe |
| T4/T10/T12/T13/T15 (cohort) | runs that start from the March sheet, include every export, or drop AdMob/TikTok | register membership |
| T11 / K7 (writes) | runs that create a new card or leave the sheet in My Drive | W4 target; R7 |

No single discovery gates more than about a third of the graded values.

## 7 Deliverables and dependent writes

| Write | Tool | Content depends on | Requirements |
|---|---|---|---|
| W1 register (Google Sheet, 13 rows: account, company holders, class, money moving, action) | `gsheets_create_spreadsheet` + `gsheets_values_update` | K2–K6, C1–C5, T6, T9 | R1–R5 |
| W2 register in Company Ops (f_21f9e11d43739eaef26b38) | `gdrive_move_file` | K7 | R7 |
| W3 DM reply to Leonard (D05S58U4SAK): 5 marked TRANSFER, Node Media still has partner admin on Meta | `slack_send_message` | K1, C1, T6, T9 | R6 |
| W4 checklist on 67cf1b506d78ad3c72e02a35 with TikTok, YouTube, X, Instagram | `trello_create_checklist` + `trello_create_check_item` | K3, K8, T6, T11 | R8 |

Reuse-vs-create (A8): W4 reuses the existing handles card. Frederick can edit: Trello writes are unscoped; the Company Ops folder is
shared with him as writer (record plan); the DM is his.

## 8 Service role map

| Service | Role | Load-bearing fact / write | Carrier |
|---|---|---|---|
| slack | hub, claims, Adjoe waiver reply, campaign state; W3 | D05S58U4SAK/1759272012.507134; C07UCC631A6/1757349668.681539 | ● |
| trello | H1 + comment, decoy, handles card; W4 | 68dc406c7b0d03e53b334bab; 68dc529406d8087e5a6b8403; 67cf1b506d78ad3c72e02a35 | ● (description, comment) |
| gmail | Google Ads amendment; money evidence | frederick.stone@harmonygames.co/1844732985606656293; frederick.stone@harmonygames.co/1843223812315546201 | ● |
| gsheets | 16 exports; March sheet; W1 | f_f7e7c5bf089029cee91175 | ● |
| gdocs | H2 | f_c612c0e68a27b3330eb46a | ● |
| gdrive | sweep folder; destination; W2 | f_6cae3483dd469c189a528e; f_21f9e11d43739eaef26b38 | ● (metadata, folder path) |
| snowflake | AdMob paid revenue | snowflake.json /tables/35 | ● (rows) |
| confluence | superseded rules page | page_company_accounts_access | ● (body) |
| gcal, gslides, contacts, github, linear | none | — | — |

## 9 Call budget

| Phase | Service | Calls | Reason |
|---|---|---|---|
| discovery | slack | 3 | hub and surrounding DM; #executives for the sweep and the Unity budget; adjoe channel |
| discovery | trello | 3 | search handover rules; read both cards |
| discovery | gdrive | 3 | find sweep folder; list 16 exports; find Company Ops |
| discovery | gdocs | 2 | find Leonard's definition; read it |
| discovery | gmail | 2 | search replies on the rules; read Arthur's reply |
| discovery | confluence | 1 | the page the card replaces |
| discovery | snowflake | 2 | find AD_REVENUE; query September paid revenue by network |
| discovery | gsheets | 1 | March logins sheet |
| rules | trello | 1 | card comments |
| per-record | gsheets | 18 | 13 exports + 5 second tabs |
| per-record | gmail | 7 | September money evidence for the paid accounts |
| per-record | slack | 5 | Unity on; Meta off; Adjoe replies; YouTube/TikTok ownership |
| per-record | trello | 1 | the Node access card behind the Meta partner |
| reads-before-writes | trello | 2 | find handles card; check its checklists |
| writes | gsheets | 3 | create, write, read back |
| writes | gdrive | 1 | move into Company Ops |
| writes | slack | 1 | reply |
| writes | trello | 5 | checklist + 4 items |
| **total** | 8 services | **61** | unconditional; largest share outside the per-record phase trello 37% |

Golden-run rule: a correct run cannot skip the exports and their second tabs (holders, invites and partners exist nowhere else), the
money evidence (decides CLOSE), the comment, the email or the revenue query (they flip eight rows). The v1 review estimated 45–60
calls for v1; v2's floor is 61. Whether a run reaches the author's 70 is measured at the pre-check; if not, hardening adds records
(more accounts or per-account evidence), never padding.

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolved by |
|---|---|---|---|
| ironSource/LevelPlay on the register? | no | Fred has an ironSource account (frederick.stone@harmonygames.co/1837038650805365569) | card rule 1 MAX-bidder clause; no export in the sweep |
| Store and Singular exports on the register? | no | they are in the sweep folder with Fred on them | card rule 1 (engineering card) |
| AdMob on the register? | yes (Leonard's active account) | deactivated (frederick.stone@harmonygames.co/1841349862518331350) | the deactivated pub id is another account; the sweep has the active one (D05S58U4SAK/1756147086.813789) |
| Second TikTok account? | off | created Sep 29 (D05S58U4SAK/1759155793.573669) | export: deleted 2025-09-29; rule 1 |
| Unity class | SINGLE | Arthur listed as Owner; Leonard runs campaigns; Arthur's summary | Invites tab: pending; Leonard Manager; card rule 2 |
| Meta action | REVOKE | TRANSFER (Fred is the only company admin) | Partners tab; rule 4–5 order (OUTSIDE wins) |
| Transfer count in the reply | 5 (marked TRANSFER) | 6 (Meta also needs a second holder) | hub asks "how many you've marked TRANSFER"; Meta is REVOKE |
| Adjoe money | N | campaign ran Sep 1–8; 90-day remark | waiver reply C07UCC631A6/1757349668.681539 + doc clause; doc newer than the remark |
| AdMob money | Y | no AdMob mail in September | doc: ad revenue paid to us counts; AD_REVENUE admob Sep paid (snowflake.json /tables/35) |
| Google Ads 569 action | KEEP | CLOSE (no money) | Arthur's reply (newer, names 569-350-5790) |
| Dormant socials | TRANSFER/KEEP by class | CLOSE (no money) | card comment 68dc529406d8087e5a6b8403 (newer, same author) |
| Instagram class | SINGLE | OUTSIDE ACCESS (non-company address) | card rule 3: a personal address isn't outside access |
| YouTube outside access? | no | Node got YouTube invites (C08MCEP1B9B/1732203251.229079) | Removed users tab: Node removed 2024-12-20 |
| Destination | Company Ops folder | the sweep folder or My Drive | hub quote "save the register in the Company Ops folder" |
| Reply placement | DM with Leonard (top level or thread) | #executives | hub "reply here"; both DM forms accepted |
| Socials write | checklist on the existing handles card | new card | card rule 7 |

### Reach table (load-bearing records)

Base records verified with `persona_view.py can-see frederick_stone …` (lines pasted in §12). Planned seeds are verified at the
injection gate (`check-sql`): the DM is Frederick's, the Gmail copy is in his mailbox, the sweep folder/exports, the doc and the
Company Ops folder are shared with him, Trello, Confluence and Snowflake are unscoped. LB = load-bearing.

| Record | Service | Verdict | LB |
|---|---|---|---|
| D05S58U4SAK/1759096868.688389 | slack | YES (im member) | LB |
| D05S58U4SAK/1759170013.491159 | slack | YES | LB |
| D05S58U4SAK/1758922541.613439 | slack | YES | LB |
| D05S58U4SAK/1756147086.813789 | slack | YES | LB |
| C07C2866011/1759186080.203099 | slack | YES (executives member) | LB |
| C07C2866011/1759264050.305069 | slack | YES | LB |
| C07UCC631A6/1757346020.196019 | slack | YES (adjoe member) | LB |
| C07UCC631A6/1757347560.891949 | slack | YES | LB |
| C07UCC631A6/1757349668.681539 | slack | YES | LB |
| frederick.stone@harmonygames.co/1843428112007517388 | gmail | YES (own mailbox) | LB |
| frederick.stone@harmonygames.co/1843223812315546201 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1835153849970828373 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1838369017520543217 | gmail | YES | LB |
| trello:67cf1b506d78ad3c72e02a35 | trello | YES (unscoped) | LB |
| C07C2866011/1759110509.707539 | slack | YES | distractor |
| frederick.stone@harmonygames.co/1841349862518331350 | gmail | YES | distractor |
| frederick.stone@harmonygames.co/1837038650805365569 | gmail | YES | distractor |
| trello:670010236b89198587ca45b6 | trello | YES | supporting |

**Feasibility.** Writes exist in `Evals/references/tools/catalog.json`: `gsheets_create_spreadsheet` (no parent parameter, so the run
creates then moves), `gsheets_values_update`, `gdrive_move_file` (newParentId), `slack_send_message` (channel D05S58U4SAK),
`trello_create_checklist`, `trello_create_check_item`. Frederick must be a writer on f_21f9e11d43739eaef26b38 (record plan). Values are categorical.

**Explicit rules.** Window: September 2025, or a campaign still switched on; ad revenue paid to us counts; written waivers don't (H2).
Holder: Owner/Admin/Super admin (rule 2); company holder: a person's harmonygames.co login (rule 3). Order: REVOKE → CLOSE →
TRANSFER/KEEP (rule 5). Amendments retain the rest ("Rest of the card stands"; "Everything else on the card stands"). Every
cross-reference postdates its target: the card (20:41Z) postdates the sweep (19:52–20:31Z) and the doc edit (17:48Z); the hub (22:40Z)
postdates the card, the sweep and the folder (22:31Z); Arthur's summary (21:10Z) postdates the sweep; the comment (21:58Z) and the
reply (23:21Z) postdate the card.

**Precedence (carrier eligibility).** Load-bearing facts sit in ● carriers only (Slack messages and replies, Trello description and
comment, Gmail body, Sheets values, Docs body, Confluence body, Drive metadata, Snowflake rows) — `references/Ask_Carriers.md` §5 as
amended by §6b.

**Prompt naturalness.** The human's trigger should name the anchor (Leonard's ask in the DM) and the deliverable kind; it must not
list the accounts, the rules, the folders, the classes, the actions, the money definition or where any of them live.

**Grading devices** (for the human's rubric later): the exact 13-account set; per-account action (≤ 5 spot checks per group + one
row-count criterion); the count 5 and the outside party (Node Media LLC on Meta) in the reply; the four checklist items on the existing
card; the register's location. Both DM reply forms accepted; holders may be written by name or address.

## 11 Record plan for /create-injection

| Row(s) | Table | Id / key | Time (UTC) | Owner / author | Notes |
|---|---|---|---|---|---|
| 1 | slack.slack_messages | D05S58U4SAK/1759187141.318207 | 2025-09-29T23:05:41Z | Leonard | claim (planned_text S_CLAIM) |
| 2 | slack.slack_messages | D05S58U4SAK/1759272012.507134 | 2025-09-30T22:40:12Z | Leonard | hub (S_HUB) |
| 3 | slack.slack_messages | C07C2866011/1757962953.240719 | 2025-09-15T19:02:33Z | Leonard | 90-day remark (S_DECOY90), top level |
| 4 | slack.slack_messages | C07C2866011/1759266627.118342 | 2025-09-30T21:10:27Z | Arthur | summary (S_ARTHUR_SUM), top level |
| 5–6 | trello.trello_cards + createCard action | 68dc406c7b0d03e53b334bab / 68dc406ceb6d064fd62b364f | 2025-09-30T20:41:16Z | Arthur | board 640643a3fd8f3ca308d9318e list To Do; name H1_TITLE, desc H1_DESC; badges.comments 1; dateLastActivity = comment time |
| 7–8 | trello.trello_cards + createCard action | 68dc42f3095ad95194a711ae / 68dc42f343eb3d733ec11459 | 2025-09-30T20:52:03Z | Arthur | ENG_TITLE, ENG_DESC |
| 9 | trello.trello_actions commentCard | 68dc529406d8087e5a6b8403 | 2025-09-30T21:58:44Z | Arthur | H1_CMT on 68dc406c7b0d03e53b334bab |
| 10–13 | gmail threads + messages | frederick.stone@harmonygames.co/1844732985606656293 (+ copies in leonard.hayes@ and arthur.blake@ mailboxes) | 2025-09-30T23:21:09Z | Arthur → Frederick, cc Leonard | G_AMEND_SUBJECT / BODY |
| 14 | gdrive.drive_files (folder) | f_6cae3483dd469c189a528e "Admin sweep - Sep 30" | 2025-09-30T19:50:00Z | Arthur | shared Leonard (writer), Frederick (reader) |
| 15–50 | gdrive + gsheets (16 spreadsheets; 21 sheet tabs) | f_f7e7c5bf089029cee91175 … f_b463693cd3779d4d25374f, f_50ff132ac88169019feeca | 2025-09-30T19:52–20:31Z | Arthur | one export per platform with each holder's login address; second tabs: Meta "Partners" (Node Media LLC, partner admin), Google Ads 569/449 "Linked managers" (Node MCC unlinked 2024-12-20), YouTube "Removed users" (Node removed 2024-12-20 by Frederick), Unity "Invites" (Arthur Blake, Owner, pending since 2025-09-30); Google Ads tabs say "enabled campaigns: 0"; TikTok lists the Sep 29 account as deleted; Instagram owner login is Frederick's personal Gmail |
| 51–53 | gdrive + gsheets | f_4521c272960dd1836a5196 "Marketing & UA logins" | 2025-03-10T17:40:00Z | Frederick | lists Meta, Google Ads, Unity Ads, AppLovin, Adjoe, AdMob (old pub id), Singular, TikTok, YouTube, LinkedIn, PlayableX |
| 54–55 | gdrive + gdocs | f_c612c0e68a27b3330eb46a "Runway & shutdown cash notes" | created 2025-09-25T16:12Z, modified 2025-09-30T17:48Z | Leonard | shared Frederick (reader); section DOC_CASH_MONEY among other notes |
| 56 | gdrive.drive_files (folder) | f_21f9e11d43739eaef26b38 "Company Ops" | 2025-09-30T22:31:00Z | Leonard | shared Frederick and Arthur as writers |
| 57–58 | confluence pages + page_versions | page_company_accounts_access | 2024-03-12T16:20:00Z | Leonard (user_EMPLOYEE_0038) | parent page_company_home, space_COMPANY, version 1 |

About 65 inserted rows over 7 injected services (slack, trello, gmail, gdrive, gsheets, gdocs, confluence) — ≥ 50 rows and ≥ 6
injected services for the normal profile. Snowflake is read, never modified.

### Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| slack | INT-22 | Slack e-mail notification for a DM | none: the base DM D05S58U4SAK carries no notification mails in Sep 2025 for Frederick; declared as an integration exception if base_check asks |
| gdrive | INT-13 | Google Drive Slack app DM on share | none: base shares from Leonard and Arthur to Frederick carry no Drive DM in this window; integration exception if flagged |
| trello | INT-21 | Trello → Slack | none: no Trello integration exists |
| gmail | — | gmail: none (no integration originates in Gmail) | one copy per mailbox (Frederick, Leonard, Arthur's sent) |
| gsheets / gdocs | INT-13 | covered with gdrive | — |
| confluence | — | confluence: none in integrations.json | — |

## 12 Self-test results

`python3 Task_Authoring/tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.draft.json --design` (verbatim):

```
HARDNESS GATE (normal (design)): PASS
  [ok] effective_profile: effective_profile 'normal' for 'Normal Horizon' → thresholds 'normal'
  [ok] sql_lint_clean: skipped (--design: no SQL yet)
  [ok] base_consistency: skipped (--design: no SQL yet)
  [ok] services_injected: skipped (--design: no SQL yet)
  [ok] rows: skipped (--design: no SQL yet)
  [ok] services_carrying_weight: 8 services with a weight_reason; need ≥ 7
  [ok] no_orphan_injection: skipped (--design: no SQL yet)
  [ok] seeded_ids_exist_in_sql: skipped (--design: no SQL yet)
  [ok] anchors: 1 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 8 fragments; need ≥ 7
  [ok] ask_fragment_services: 5 services carry asks; need ≥ 5
  [ok] ask_fragment_containers: 7 distinct containers; need ≥ 6
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 8 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 13; need ≥ 10 (source-defined: True)
  [ok] evidence_surfaces: 4 surfaces over 4 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 34; need ≥ 25
  [ok] call_budget: unconditional (verified) floor 61 of 61 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 60 and total ≤ 100 (Normal Horizon 50–100)
  [ok] call_budget_spread: 8 services in budget; largest share outside the per-record phase 37% (≤ 40%)
  [ok] traps: 15 traps across 9 families; need ≥ 8 / ≥ 5; unknown family: none
  [ok] trap_independence: traps hit 6 distinct requirements; need ≥ 4 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 3 supersessions (3 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 4 distractors of 4 types; need ≥ 4 / ≥ 3
  [ok] discovery_order_proofs: 6 traps carry a discovery-order proof; need ≥ 2
  [ok] independent_chains: 5 chains with 5 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 2, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] hidden_authorities: 2 authorities (need ≥ 1), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 0 (need ≥ 0: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 12 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 2
  [ok] requirements: 8 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 4 writes over 4 services; each must depend on findings
```

`persona_view.py can-see` for the base records in the reach table (verbatim first lines):

```
frederick_stone slack D05S58U4SAK/1759096868.688389: YES
frederick_stone slack D05S58U4SAK/1759170013.491159: YES
frederick_stone slack D05S58U4SAK/1758922541.613439: YES
frederick_stone slack C07C2866011/1759186080.203099: YES
frederick_stone slack C07C2866011/1759264050.305069: YES
frederick_stone slack C07UCC631A6/1757346020.196019: YES
frederick_stone slack C07UCC631A6/1757347560.891949: YES
frederick_stone slack C07UCC631A6/1757349668.681539: YES
frederick_stone slack C07C2866011/1759110509.707539: YES
frederick_stone gmail frederick.stone@harmonygames.co/1843428112007517388: YES
frederick_stone gmail frederick.stone@harmonygames.co/1843223812315546201: YES
frederick_stone gmail frederick.stone@harmonygames.co/1835153849970828373: YES
frederick_stone gmail frederick.stone@harmonygames.co/1838369017520543217: YES
frederick_stone gmail frederick.stone@harmonygames.co/1841349862518331350: YES
frederick_stone gmail frederick.stone@harmonygames.co/1837038650805365569: YES
frederick_stone trello 67cf1b506d78ad3c72e02a35: YES
frederick_stone trello 670010236b89198587ca45b6: YES
```

**Lazy-solver pass** (one broad search per service, first hits, no replies, stop at the first conclusion, every bulk shortcut):
- Reads the hub and #executives, trusts Arthur's summary → only YouTube and TikTok SINGLE; Unity, X, Instagram wrong; Meta wrong.
- Reads the card description only → closes the dormant socials and 569 (comment and email unannounced).
- Reads the adjoe channel history (parents only) → Adjoe money Y. The waiver is only in replies.
- Reads the first tab of each export → misses the Meta partner and the Unity invite.
- Never opens Snowflake → AdMob N → CLOSE.
- Bulk shortcut check: no Sheet or page lists accounts with roles; `gsheets_values_batch_get` cannot read 16 spreadsheets in one call;
  Gmail has no cross-sender query; the revenue table names networks, not accounts.

**Literal-value sweep** (planned, re-run at injection on the SQL): "569-350-5790" appears in base Google mails, the seeded export and
the email only; "Node Media LLC" appears in base termination messages, never with "partner admin"; "REVOKE", "TRANSFER", "OUTSIDE
ACCESS" appear only in the H1 card. **Wording sweep:** the waiver reply says "not be responsible for the cost", the doc says "agreed in
writing to drop" — no shared decisive phrase. **"The rest stands" check:** no record after the comment re-asserts CLOSE for socials; no
record after the email re-asserts CLOSE for 569.

### Self-review

Re-read `Evals/1_Prompt_Eval.md` §2.1 (Unique Ground Truth), §2.2 (Feasibility), §3.2 (Cross-Service Coherence),
`Evals/0_Injection_Quality_Eval.md` Check C and `references/Docs/11_V3_Changes.md`, then walked the design in order. Re-read every
load-bearing base value from the exports this session (Slack DM, adjoe thread, #executives, node channel, Gmail receipts/payouts,
Google Ads and AdMob mails, Trello cards, Snowflake AD_REVENUE and AD_SPEND_DAILY).

| # | Check / category | Verdict | Counter-reading (strongest argument the other way) | Resolution with evidence |
|---|---|---|---|---|
| 1 | temporal | PASS | base records after the freeze (Adjoe Oct 1 invoice, 449 canceled Oct 16) are visible and could be read as "already happened" | not cited by any requirement; designed answers agree with them; hazard T07 (frederick.stone@harmonygames.co/1846207913166171315) |
| 2 | temporal (seeded) | PASS | the email at 23:21Z sits 39 minutes before the freeze | 2025-09-30T23:21:09Z < 2025-10-01T00:00Z (V3 §3); `minted_ids.json` G_AMEND |
| 3 | temporal (chronology) | PASS | v1's card (Sep 29) cited "my Sep 30 sweep folder" before it existed (review finding 2) | v2 card at 2025-09-30T20:41:16Z after the last export (20:31Z); text says "today's sweep folder" (68dc406c7b0d03e53b334bab) |
| 4 | semantic | PASS | "Google Ads" names two accounts and the email could be read as the Calm Play one | email names "Harmony Games, Inc." and 569-350-5790; base ties 569 to "[SOURCE_ORG_0001], Inc." (frederick.stone@harmonygames.co/1835153849970828373) and 449 to Calmplay (/1838369017520543217) |
| 5 | semantic (TikTok) | PASS | a "Business Center" export could be read as an ads account outside the socials exemption (review finding 5) | v2 export is the @harmonygames profile (D05S58U4SAK/1759170013.491159); the Sep 29 account is marked deleted (/1759155793.573669) |
| 6 | cross-service referential | PASS | the hub names "arthur's sweep from today" and "the Company Ops folder"; a dropped seed dangles | both planned and dated before the hub (f_6cae3483dd469c189a528e 19:50Z, f_21f9e11d43739eaef26b38 22:31Z); injection gate checks seeded ids |
| 7 | cross-service referential (Node) | PASS | Node had YouTube invites and an MCC request, never revoked in base (review finding 3) | v2 exports record Node removed/unlinked 2024-12-20 on YouTube and both Google Ads (C08MCEP1B9B/1732203251.229079, /1727063903.359939); only Meta keeps the partner |
| 8 | quantitative | PASS | Snowflake shows Unity September spend $0, so money moving could be N and Unity CLOSE | H2 counts a switched-on campaign; Unity iOS campaigns on (C07C2866011/1759186080.203099, /1759264050.305069); hazard Q08 excluded |
| 9 | quantitative (AdMob) | PASS | AdMob revenue is small ($38.70) and could be "accrued, not paid" | AD_REVENUE rows for admob Sep 2025 are `paid` (snowflake.json /tables/35); doc counts ad revenue paid to us |
| 10 | state/lifecycle | PASS | Adjoe's June invoice reminder (Aug 4) suggests an unpaid bill | paid in August (C04UEQVDVB7/1755117283.864129); no rule uses unpaid bills |
| 11 | state/lifecycle (AdMob) | PASS | AdMob "has been deactivated" (frederick.stone@harmonygames.co/1841349862518331350) | that is pub-2341961509332343; Leonard's account is active (D05S58U4SAK/1756147086.813789) |
| 12 | identifier/format | PASS | seeded Trello ids could break the timestamp scheme (I16/T06) | minted from their own timestamps (`mint_ids.py`): 68dc406c7b0d03e53b334bab → 2025-09-30T20:41:16Z |
| 13 | identifier/format (holders) | PASS | Discord/LinkedIn admins are personal profiles, so rule 3 gives zero company holders (review finding 4) | v2 exports list each holder's harmonygames.co login; rule 3 says "a person's harmonygames.co address" (planned_text H1_DESC) |
| 14 | other (persona plausibility) | PASS | a custody register might look like Arthur's job, not Frederick's | the hub delegates it to Frederick and the accounts are his (D05S58U4SAK/1759096868.688389; C07C2866011/1759186080.203099) |
| 15 | other (wrong summaries) | PASS | the rules' author contradicting his own exports could read as an inconsistency | Arthur's summary is a dated human claim (C07C2866011/1759266627.118342); it overcounts pending invites and managers, which the exports show; Atlas rule 12 human-claim-vs-record |
| DP1 | two-reading: ironSource | PASS | a careful run adds ironSource from the Jul 8 welcome mail | card rule 1 MAX-bidder clause (frederick.stone@harmonygames.co/1837038650805365569) |
| DP2 | two-reading: stores/Singular | PASS | they are in the sweep with Fred on them | card rule 1 names them on the engineering card (68dc42f3095ad95194a711ae) |
| DP3 | two-reading: AdMob in | PASS | it was deactivated | different pub id; active account in the sweep (D05S58U4SAK/1756147086.813789) |
| DP4 | two-reading: TikTok second account | PASS | the Sep 29 account is a second TikTok | deleted per the export; D05S58U4SAK/1759155793.573669 |
| DP5 | two-reading: Unity | PASS | Arthur Owner → COMPANY-HELD → KEEP | Invites tab: pending (f_1191b7f8c96419e1f4dc88); card rule 2 |
| DP6 | two-reading: Meta | PASS | Fred is the only company admin → TRANSFER | Partners tab (f_f7e7c5bf089029cee91175); rule 5 order |
| DP7 | two-reading: transfer count | PASS | 6 if Meta counts (review finding 6) | hub asks "how many you've marked TRANSFER" (D05S58U4SAK/1759272012.507134) |
| DP8 | two-reading: Adjoe | PASS | ran in September → money Y | waiver reply C07UCC631A6/1757349668.681539 |
| DP9 | two-reading: AdMob money | PASS | no AdMob mail in September → N | AD_REVENUE admob Sep paid (snowflake.json /tables/35) |
| DP10 | two-reading: 569 | PASS | no money → CLOSE | Arthur's reply frederick.stone@harmonygames.co/1844732985606656293 is newer and names it |
| DP11 | two-reading: dormant socials | PASS | no money → CLOSE | comment 68dc529406d8087e5a6b8403 |
| DP12 | two-reading: Instagram | PASS | non-company address → OUTSIDE | card rule 3 (planned_text H1_DESC) |
| DP13 | two-reading: YouTube outside access | PASS | Node got YouTube invites in 2024 | Removed users tab (f_fc27672c5bfea8b760b074); C08MCEP1B9B/1732203251.229079 |
| DP14 | two-reading: destination | PASS | the sweep folder is Arthur's place for this | hub quote names Company Ops (D05S58U4SAK/1759272012.507134) |
| DP15 | two-reading: reply | PASS | a new top-level message vs a thread reply | both in D05S58U4SAK accepted (grading devices) |
| DP16 | two-reading: socials write | PASS | a new card is cleaner | card rule 7 (trello:67cf1b506d78ad3c72e02a35) |

HARDNESS GATE output: pasted above (normal, design PASS).

Unresolved: (1) the honest necessary budget is 61 calls against the author's 70+ target; the measured count comes from the Opus
pre-check, and hardening adds records if it falls short. (2) The review predicted 80–90% for v1; v2 removes the hub pointers to the
money definition, the March sheet and the amendments, adds Arthur's wrong summary, second tabs and a Snowflake-only fact — the
predicted average is not verified until the pre-check. (3) Findability searches for the seeded H1/H2 records are proven at injection.

```
STAGE GATE scenario: PASS — Task_Authoring-2/task_inputs · 01_Scenario_Design.md#1b5beaa91f08 · 01_Hardness_Manifest.draft.json#193b0f8092c1 · blocking 0 · warnings 0 · checks 26
[PASS] structure.outputs: 2 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 20/20 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 22/22 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 2/2 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 9/9 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 15/15 items carry a source pointer (min 90%)
[PASS] evidence.record_plan: 18/20 items carry a source pointer (min 80%); unsourced e.g. L524: 'gmail | — | gmail: none (no integration originates in Gmail) | one copy per mailbox (Frede'
[PASS] evidence.active_speakers: 3/3 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for frederick.stone@harmonygames.co and matches the re-run (106 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 16 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 3 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (3 INT ids, services ['confluence', 'gdocs', 'gdrive', 'gmail', 'gsheets', 'slack', 'snowflake', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts []; trap_catalog ['B02', 'C01', 'D04', 'K02', 'P01', 'X04']
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: red team unavailable, error recorded
[PASS] reach.scenario: 18 scoped load-bearing ids YES for frederick_stone (1 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 29 evidenced counter-readings (of 31 found; need ≥ 23) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13 Red team (dual)

RED TEAM UNAVAILABLE: redteam_review: set REDTEAM_MODEL or pass --model (no REDTEAM_* environment configured — error)

Substitute: one independent reviewer (a fresh subagent given only the v1 design, manifest, `planned_text.json`, the assignment and the
eval rules, with read access to the base) red-teamed v1. Every finding was re-verified against the base before acting:

| Finding | Source | Disposition with evidence |
|---|---|---|
| 1 Blocker: AdMob is a live account Fred was made admin of on Aug 25; v1 left it out | subagent | verified (D05S58U4SAK/1756147086.813789, /1756147145.162239; frederick.stone@harmonygames.co/1841453218828344296); fixed: AdMob export f_50ff132ac88169019feeca in the sweep, COMPANY-HELD, money Y from AD_REVENUE admob Sep paid (snowflake.json /tables/35) → KEEP; T15 lookalike |
| 2 Major: Sep 29 card cites the Sep 30 sweep | subagent | verified; fixed: card moved to 2025-09-30T20:41:16Z after the last export, text "today's sweep folder" (68dc406c7b0d03e53b334bab) |
| 3 Major: Node's YouTube/Google Ads/MMP access never revoked in base | subagent | verified (C08MCEP1B9B/1732203251.229079, /1727063903.359939, /1727689480.986899); fixed: Removed users / Linked managers tabs record removal 2024-12-20; only Meta keeps Node |
| 4 Major: Discord/LinkedIn admins are personal profiles under rule 3 | subagent | fixed: exports list each holder's harmonygames.co login; rule 3 reworded to "a person's harmonygames.co address"; group inboxes excluded (planned_text H1_DESC) |
| 5 Major: "TikTok Business Center" vs the social profile; second TikTok account | subagent | verified (D05S58U4SAK/1759155793.573669); fixed: export is the @harmonygames profile; the Sep 29 account is listed as deleted; rule 1 drops deleted accounts |
| 6 Major: transfer count 5 vs 6 | subagent | fixed: hub asks "how many you've marked TRANSFER" (D05S58U4SAK/1759272012.507134) |
| 7 Minor: rule-text gaps (Instagram "second owner", rule 6 wording, Super admin, Adjoe "spend", Google Ads campaign status) | subagent | fixed: "Leonard is added as an owner"; column "company holders"; rule 2 includes Super admin; doc says "Spend or a charge the vendor has agreed in writing to drop"; Google Ads exports state 0 enabled campaigns (UAC last spend 2025-04-10, snowflake.json /tables/0) |
| 8 Minor: Adjoe thread parent wrong | subagent | verified; fixed to C07UCC631A6/1757346020.196019 in T7, C2 and §1 |
| 9 Major: most traps pointed to by name (expected 80–90%) | subagent | partly fixed: the hub no longer names the money definition, the March sheet or the amendments; the card no longer announces its comment or the email; the Partners tab and the Unity invite moved to second tabs; added Arthur's confident wrong summary (T14) and a Snowflake-only fact (C5). Residual risk recorded in the Self-review Unresolved line; the pre-check measures it |
| 10 Major: v1's 63-call budget padded (~40–50 real) | subagent | fixed: removed read-backs and absence searches; added only reads that decide a row (second tabs, revenue query, AdMob): honest floor 61 (§9) |
| 11 Minor: create has no parent; folder write access; "Fred's card" provenance; board named "Harmony Games" | subagent | create-then-move is the designed path; Company Ops shared with Frederick as writer (record plan row 56); the hub calls the board "the ops board" and the card names "Fred's \"Lock up social handles and domain?\" card on the UA/BD board", which resolves the card by title (trello:67cf1b506d78ad3c72e02a35) |
| 12 Minor: base "Operations" folder near-miss | subagent | accepted as a natural distractor: the hub names "Company Ops"; the base folder (d_e4181c7a6ba241b7c60d1b) is Marcus's |

