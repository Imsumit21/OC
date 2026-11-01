# Scenario Design — fs-paid-ua-trueup (v2) · design only · contains no prompt, OE or criterion text

Persona Frederick Stone (Co-founder, Executive) · competency Finance · task skill Analysis and synthesis · horizon long-horizon ·
difficulty mode Medium (V3 cap: six-rollout average strictly under 85%) · universe date October 1, 2025 (V3 freeze 00:00 UTC =
Tue Sep 30, 2025 5:00 PM PT). Builder scripts: `support/task_work/fs_ua_trueup/` (`ids.py` mints every id, `texts.py` holds the
seeded wording the delegation quotes come from, `build_manifest.py` writes the draft manifest). v2 applies the 15 red-team findings
of v1 (§13), the requester's option A / option 1 decisions (§0) and a V3 compliance pass (§10, "V3 compliance check").

## 0 Assignment, persona census and horizon note

| Field | Assigned (verbatim, `00_Assigments.md`) | Resolution |
|---|---|---|
| persona | Frederick Stone | roster `frederick_stone`, frederick.stone@harmonygames.co, Executive (`Evals/references/persona/roster.json`) |
| role | Co-founder | owns the UA / ad-network vendors (`references/Persona_Briefs.md` §Frederick); posted the two-bucket proposal C07C2866011/1757961037.465799 |
| business function | Executive | Evals category Finance / Legal / HR / Ops (`Evals/references/rules/task_categories.md`): a financial reconciliation |
| competency | Finance | network-by-month paid-UA reconciliation against the warehouse and ledger |
| task skill | Analysis and synthesis | ~116 source records joined across mail, statements, briefs, ledger and warehouse under four rule sources |
| horizon | long-horizon | manifest `horizon: Long Horizon`, `effective_profile: long` with `profile_exception` |
| universe date | October 1, 2025 07:00 | built on the Oct 1, 2025 freeze; treated as 00:00 UTC (V3 §3), the stricter cut-off |
| difficulty mode | medium | design target: average well under 85%; ≥ 2 failure patterns; SD 0.1–0.3 |

**Remit argument.** Frederick is the UA owner: the Adjoe spike report C07UCC631A6/1757132965.831109, the two-bucket proposal
C07C2866011/1757961037.465799 and the playable-bucket rule C07C2866011/1757961129.250809 are his; the Meta ad account ending 3125
bills his mailbox (frederick.stone@harmonygames.co/1836836899676941724); he ran the Unity account (Unity Support thread
frederick.stone@harmonygames.co/1813530307529968502). Leonard runs the bridge and the Oct 14 board (evt_bd61f3209523d19fdd6ba2 on
Frederick's calendar, created 2025-09-17). A twelve-month paid-UA true-up for the data room is the finance work a UA co-founder is
pulled into in late Sep 2025.

**Clock retrofit (bundle change).** `tools/hg_clock.py` resolves the clock from `universe_date` in `00_Assigments.md`
(2025-10-01T00:00Z); `sql_lint.py`, `base_check.py`, `persona_view.py` and `references/universe_kb/_build/` use it, and the KB was
rebuilt at the new clock (Feb 2026 KB and tools backed up in `support/clock_backup_feb2026/`).

**Effective profile and horizon (requester decisions, 2026-10-22).** The requester chose the long profile (AskUserQuestion), then
option A (per-record Google Sheets / Docs) after the v1 red team showed Gmail batch reads collapse per-thread volume. `tools/hardness_gate.py`
`long` = extreme breadth / authority / chain / trap thresholds with **V3's 100-call floor**. After the V3 review (§13b) the honest
necessary minimum is **104** calls (§9): Unity statements are weekly during the ZM3D tests (Jun – Sep 2025, when Frederick and Leonard
reviewed UA weekly in #executives) and the two PvZ-named tests need their briefs. V3 measures ≥ 100 on the golden run if one exists,
else the six-rollout average; a correct run cannot finish under 104 calls, so a golden run meets the floor. The margin is small; the
Opus pre-check records the measured count.

Persona reach census (`python3 Task_Authoring/tools/persona_view.py reach frederick_stone --top 15`, verbatim):

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
  C069FF9Q57S    analytics                              private mem=28  msgs=4301   2023-12-05..2026-01-28
  D05S58U4SAK    D05S58U4SAK                            im      mem=5   msgs=4251   2023-09-15..2025-10-23
  C04RYU8TJ8K    random                                 public  mem=32  msgs=4059   2023-03-02..2026-01-30
  C04V7N09LE7    god-gameart                            private mem=30  msgs=3803   2023-03-22..2026-02-11
  C08R8CHB0QL    zombie-art                             public  mem=23  msgs=3489   2025-05-06..2025-12-24

GMAIL  mailbox=frederick.stone@harmonygames.co threads=5009 messages=5891 range=2024-06-25..2025-11-13
  threads by last-message month (recent): {'2025-06': 333, '2025-07': 249, '2025-08': 108, '2025-09': 177, '2025-10': 275, '2025-11': 89}
  top correspondents: SVC_0107_EMAIL (1870), SVC_4131_EMAIL (1531), leonard.hayes@harmonygames.co (594), robert@harmonygames.co (392), arthur.blake@harmonygames.co (314), SVC_0521_EMAIL (192), brian.foster@harmonygames.co (114), SVC_0009_EMAIL (103), SVC_5366_EMAIL (79), PERSON_5681_EMAIL (76), marcus@harmonygames.co (75), PERSON_1294_EMAIL (75), PERSON_1298_EMAIL (72), martin.walsh@harmonygames.co (71), julia.lawson@harmonygames.co (63)

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

Other identities (`entity.py resolve`): Linear `usr_175c0d7bc72ed244`, Trello `4b4a68fc0fec0b254e4f9d8e`, Confluence `user_EMPLOYEE_0008`,
Contacts `175c0d7bc72ed244b944cb90`. The base holds records after the freeze (Slack to 2026-02-13); nothing in this design depends on
any of them and nothing seeded is dated on or after 2025-10-01T00:00Z.

## 1 Storyline

**The story (Sep 2025).** After the July board ("runway ends in ~5 months", gdocs f_af99b76ff4da59a710edba), Leonard opens a $2.5M
bridge (C07C2866011/1756749288.785249; timeline spine "2025-09-03 funding"). Zombie Match 3D runs a small UK iOS test so the deck can
show a CPI: Leonard turns on UK Retention iOS (C07C2866011/1757689941.099589, Sep 12), Unity phone and tablet campaigns cap out and
Frederick cuts the bid (C07C2866011/1758060268.307769, Sep 16), Leonard drops Unity to $1 (C07C2866011/1758313197.701479) and calls
Facebook "$20/day" (C07C2866011/1758313330.170339). Frederick proposes two buckets, fundraising vs real UA
(C07C2866011/1757961037.465799). Adjoe switches a Domino Delights campaign on by mistake on Sep 1; its rep confirms in a thread reply
that the cost is not ours (C07UCC631A6/1757349668.681539, thread C07UCC631A6/1757346020.196019).

The warehouse misses real spend: `ANALYTICS.MARKETING.AD_SPEND_DAILY` (2,590 rows, re-read this session) carries Unity Ads at $0
in every month with installs every month (DD Oct 2024 – Apr 2025, ZM3D Apr – Sep 2025), and no Meta spend May–Sep 2025, while
Frederick's mailbox holds Meta receipts for those months (frederick.stone@harmonygames.co/1835778053085762169, Jun 23 $900). Unity
is prepaid ("All prepaid funds are non-refundable", frederick.stone@harmonygames.co/1813530307529968502). The trailing-twelve-month
warehouse total is $81,168.77 (Adjoe 46,201.54 · Meta 28,308.20 · AppLovin 6,226.24 · Google UAC 432.79 · Unity 0). **Seeded (Mon
Sep 29):** Leonard asks Frederick in #executives for the real twelve-month paid-UA number for the data room and the Oct 14 board,
pointing at his close rules, the bucket split on the UA/BD board and the Q4 board pack; on Sep 30 he amends one clause in a reply.

| Anchor / beat | Service | Record | Date | Use |
|---|---|---|---|---|
| Leonard's ask (hub, seeded) | slack | C07C2866011/1759176840.271025 | 2025-09-29 20:14Z | anchor A1 |
| Amendment reply (seeded) | slack | C07C2866011/1759255500.938286 | 2025-09-30 18:05Z | Adjoe month clause |
| Rough rules mail (seeded, superseded) | gmail | frederick.stone@harmonygames.co/1843732571750494737 | 2025-09-19 | first version of H2 |
| Close rules doc (seeded) | gdocs | f_4591ef30be4f920ba1ed14 | 2025-09-26 | authority H2 |
| Bucket card (seeded) | trello | 68c99c40e5d9eb6f3a988838 | 2025-09-16 | authority H1 |
| Bucket review meeting (seeded) | gcal | evt_2f9b60002516e45ff04160 | 2025-09-18 17:00Z | effective date |
| Q4 board pack (seeded) | gsheets | f_0cd1e1402e8052d3d4e903 | 2025-09-29 | destination H3 |
| UA test briefs folder (seeded, 18 docs) | gdocs / gdrive | d_6930b716ea5b1457adb4a4; f_6d0c2209baa3ff54633836 … f_887def6eed0e1b022f7ab0 | 2024-10 … 2025-09 | authority H4 |
| Unity statements (seeded, 25 sheets: HG account monthly Oct 2024 – Apr 2025; Calm Play account monthly Apr – May 2025, weekly Jun – Sep 2025) | gsheets / gdrive | d_3885933a334aef16e40e84; f_c34b364c50bf4ed59ae6ce … f_0c302b9a0529823a0c6209 | 2024-10 … 2025-09 | Unity spend |
| Meta receipts (base, 38 threads) | gmail | frederick.stone@harmonygames.co/1812262106647207041 … /1843428112007517388 | 2024-10-11 … 2025-09-16 | cohort |
| Adjoe invoices + reminders (base) | gmail | frederick.stone@harmonygames.co/1830999337380347892, /1836528865848810632 | 2025-05-02 … 2025-08-04 | cohort + wire dates |
| Adjoe Sep reply chain (base) | slack | C07UCC631A6/1757345931.336429 → C07UCC631A6/1757349668.681539 | 2025-09-08 | R7 |
| Warehouse + ledger (base) | snowflake | snowflake.json /tables/0 (AD_SPEND_DAILY), /tables/38 (FINANCE_LEDGER FIN-000499, FIN-000529, FIN-000555) | 2024-10 … 2025-09 | gap check; Adjoe/AppLovin/Google amounts |
| July board doc (base) | gdocs | f_af99b76ff4da59a710edba "Board Meeting Jul 25" | 2025-07-16 | "$50K in UA spend" stale summary |

**Universe KB.** Timeline (`references/universe_kb/timeline.md`, rebuilt at the 2025-10-01 clock): spine events "2025-07-16
board/funding (Q3 board, ~5 months runway)", "2025-09-03 funding ($2.5M bridge outreach)"; the Oct 14 board and Oct 24 layoffs lie
after the freeze. Cohort: `cohorts.json`: no fit — the 191 natural sets are Linear/GitHub/Slack/Gmail-bot populations; the closest,
GM-TF-ZombieMatch3-frederick.stone (TestFlight mails), is not billing. Trap precedent from `trap_catalog.json`: K02 (app-name
lineage PvZ / Puzzles vs Zombies / Domino Adventures) for T11, B02 (automated senders) for T1–T3, D04 (near-duplicate spreadsheets)
for T16, C01 (thread replies that correct) for T6/T10, X03 (redacted vendor names: `[USERNAME_14101]` = Adjoe), D01 (lookalike Drive
titles) for the two data-room folders.

**Originality.** Not the Combo Fighters launch record, not the calibration register / RC-flag gate / art-canon control: the cohort is
billing sources (receipts, statements, briefs, ledger months), the vocabulary is buckets / net cost / charge month.

## 1a Coherence audit

Scope = every record a correct run opens: the hub thread, the rules (Sep 19 mail, Sep 26 doc, Sep 30 reply), the bucket card and
decoys, the 57 Meta receipt threads, 25 Unity statements, 6 Unity top-ups, the 18 briefs, the Adjoe threads, 19 revenue lookalikes,
the adjoe channel thread, `AD_SPEND_DAILY`, `FINANCE_LEDGER`, the connector page, ENG-2362, the review event, Contacts, three Drive
folders and the true-up card. Known hazards walked from `references/universe_kb/coherence_hazards.json` (all six categories).

| Record | Category | Fields | Evidence pointer | Hazard id | Disposition |
|---|---|---|---|---|---|
| Meta receipt threads with two messages (Apr 6 two charges; Apr 26 / May 3 / May 4 duplicates) | temporal | message order in thread | frederick.stone@harmonygames.co/1828641403961142838, /1830495542195061363 | T02 | fold in: charges keyed by reference number and charge time (T4/T5) |
| Base Meta charge Dec 31 2024 17:13 PST = Jan 1 2025 UTC | temporal | charge month depends on zone | frederick.stone@harmonygames.co/1820007110310927242 | T02 | V3 §10: both months accepted for this one charge (grading devices); every seeded charge is the same calendar day in PT and UTC |
| Seeded Confluence pages by Simon Walker / Frederick | temporal | created_at vs author activity | confluence:page_singular_cost_connectors (planned) | T08 | avoid: both authors `active_sep_2025`; pages dated Apr / Aug 2025 |
| Base records after the freeze (Oct 1 Adjoe invoice + reply) | temporal | dates after 2025-10-01 | C07UCC631A6/1759326759.229719; leonard.hayes@harmonygames.co/1844773822273338923 | T07 | avoid: no requirement reads them; the designed Adjoe answer (no cost) agrees with them |
| Seeded Aug 31 charge vs base Meta billing ranges | temporal | receipt date range | frederick.stone@harmonygames.co/1839693762261954189 (covers Jul 15–17 only) | T02 | v1's Jun 30 charge overlapped the base Jun 22 – Jul 5 receipt; v2 bills Aug 18–31, no base overlap |
| Contacts job titles (Frederick, Leonard) | semantic | job vs roster role | contacts:175c0d7bc72ed244b944cb90 | S06 | avoid: only the seeded accountant contact is read |
| "Meta" names two products (ads receipts vs Audience Network invoices) | semantic | subject wording | frederick.stone@harmonygames.co/1842698832158940633 | S06 | fold in as T1; H2 "money a network pays us is not spend" |
| "ADV" campaigns vs the deprecated Domino Adventures Unity game | semantic | campaign name vs title | frederick.stone@harmonygames.co/1813530307529968502; frederick.stone@harmonygames.co/1820132039739740641 | S06 | fold in: briefs B05/B06/B08 say ADV = the Domino Adventures store listing used for DD (T11) |
| Gmail "Invitation:" mails vs calendar instances | cross-service referential | invitation with no GCal copy | evt_2f9b60002516e45ff04160 (planned) | R08 | seed the invitation mail with the event (INT-11), one GCal copy per attendee calendar |
| Slack links to Google files | cross-service referential | native ids ≠ f_ ids | C07C2866011/1759176840.271025 (planned) | R04 | avoid: seeded messages name documents by title, no links |
| Warehouse + ledger vs billing sources (Unity $0; Meta May–Sep absent) | quantitative | AD_SPEND_DAILY.spend_usd, FINANCE_LEDGER marketing_ua vs receipts / statements | snowflake.json /tables/0; snowflake.json /tables/38; frederick.stone@harmonygames.co/1835778053085762169 | Q08 | dated claim + explanation: Leonard's Sep 29 claim quotes the warehouse; the Aug 14 connector page states the ledger and warehouse are booked from Singular's cost per network-month; reconciling is the incorporated job (R12); no warehouse or ledger field modified |
| Adjoe April PDF $12,005.00 vs ledger FIN-000499 −10,733.60 | quantitative | invoice total vs ledger | frederick.stone@harmonygames.co/1830999337380347892 (att_0001.pdf) | Q08 | dated human resolution seeded in that thread: Leonard contests the Canada installs (May 5), Adjoe credits $1,271.40 (May 7) = $10,733.60; H2 says ledger amount after credit (T21) |
| Ledger cash vs MONTHLY_BURN | quantitative | totals | snowflake.json /tables/38 and /tables/15 | Q05 | avoid: only marketing_ua rows read |
| AD_SPEND_DAILY vs AD_SPEND vs UA_SPEND_UNIFIED_V2 | quantitative | mirrored tables | snowflake.json /tables/0, /tables/34, /tables/3 | Q09 | checked clean; either gives the same network-month values |
| Adjoe June invoice booked (FIN-000555) while the Aug 4 reminder says outstanding | state/lifecycle | paid status | snowflake.json /tables/38; frederick.stone@harmonygames.co/1839518563856917373 | L14 | dated explanation: the connector page says the ledger's marketing rows are booked from Singular per month, not cash; the register has no paid column |
| UA/BD "Done" list is closed | state/lifecycle | list closed | trello:66da196af476ab78deaa0cf8 | L11 | avoid: seeded cards on "Doing" 66da196af476ab78deaa0cf7; the write is a comment |
| ENG-2362 (Todo) gets a seeded comment | state/lifecycle | updated_at vs comment | linear:ENG-2362 | L08 | assignee-free Todo issue by Leonard (active); updated_at bumped to the comment time (companion) |
| v1's ZOM-673 numbering | identifier/format | issue number vs creation order | linear:ZOM-672 (created 2025-11) | I10 | removed: v2 comments on base ENG-2362 instead of minting an issue |
| Mailbox filename aliases | identifier/format | thread file vs user_email | frederick.stone@harmonygames.co/1836528865848810632 | I03 | avoid: seeded ids use the roster address |
| Leonard's Trello member id is a token | identifier/format | idMemberCreator | trello:PERSON_6094_TRELLO_USER_ID on board 66da196af476ab78deaa0cef | I17 | fold in: seeded Leonard actions use the same token |
| Redacted vendor `[USERNAME_14101]` = Adjoe | other | subject redaction | frederick.stone@harmonygames.co/1836438286741039931 | X03 | fold in: sender SVC_2836 + the adjoe channel identify Adjoe |

**Sibling-defect sweep.** Defect 1 — spend the warehouse misses: every network × month in `AD_SPEND_DAILY` (snowflake.json /tables/0)
was checked: only Unity (all 12 months) and Meta (May–Sep 2025) are $0 while a billing source exists; Google UAC and AppLovin have
ledger rows every month they spent (FIN-000333 … FIN-000599) — no further sibling. Defect 2 — a mail that reads like a bill but pays
us: all 19 in the window are listed (T1–T3); Singular's renewal frederick.stone@harmonygames.co/1837914783244638008 is out of scope
(attribution tool); the Calm Play LLC Singular alert frederick.stone@harmonygames.co/1839175088393392199 is a T22 lookalike (v3: the Calm Play Unity account itself is in scope). Defect 3 — a
duplicate notice: the 38 base threads hold exactly three duplicate pairs (frederick.stone@harmonygames.co/1830495542195061363,
/1831122183306732471, /1831236341456877471) and one two-charge thread (/1828641403961142838), all cohort members. Defect 4 — a
campaign name that does not say its game: the sweep of the 85 in-window base receipt messages found 36 campaign names; every one is
listed in a brief (`texts.py` BRIEFS), including Creative_AB_Test, Advantage+ and the NM_ / ADV names the v1 legend missed. Defect 5
— a charge whose month depends on the time zone: the sweep found one base charge (frederick.stone@harmonygames.co/1820007110310927242)
and no seeded one.

## 1b Active speakers

Every person given a seeded voice, with `status_at_clock` from `references/universe_kb/activity.json` (rebuilt at the 2025-10-01 clock).

| Person | Email | status_at_clock (activity.json) | Seeding role |
|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025 | hub + amendment (Slack), Sep 19 rough rules (Gmail), close rules (Docs), board packs (Sheets), review event organizer, tablet comment + true-up card (Trello), Adjoe contest mail |
| Frederick Stone | frederick.stone@harmonygames.co | active_sep_2025 | persona; bucket card + DD bucket card (Trello), 18 test briefs (Docs), 25 Unity statements (Sheets), DD bucket page (Confluence) |
| Robert | robert@harmonygames.co | active_sep_2025 | non-authoritative reply in the hub thread |
| Simon Walker | simon.walker@harmonygames.co | active_sep_2025 | connector page (Confluence), comment on ENG-2362 (Linear) |

External automated senders (Meta receipts SVC_0521, Unity billing, Adjoe SVC_2836) follow the base sender tokens; they are not people
in activity.json. Briefs are dated at each test's start (Oct 2024 – Sep 2025), when Frederick was active every month
(activity.json monthly_authored_total).

## 1c Identity traps

`python3 Task_Authoring/tools/entity.py collisions` (verbatim, first sections) and `resolve` for every person the design names:

```
SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <marcus@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']

PERSONA_ROLE_VS_CONTACTS_JOB (4)
  - Frederick Stone <frederick.stone@harmonygames.co> [persona frederick_stone]: roster role 'Co-founder' vs Contacts job 'Commercial Lead, Marketing & Business Development'
  - Leonard Hayes <leonard.hayes@harmonygames.co> [persona leonard_hayes]: roster role 'Co-founder & Creative Director' vs Contacts job 'Co-founder & CEO'
  - Robert <robert@harmonygames.co> [persona robert]: roster role 'Co-Founder & Creative Director' vs Contacts job 'Co-founder & Chief Product Officer'

ENTITY email:simon.walker@harmonygames.co  name=Simon Walker  kind=person  emails=['simon.walker@harmonygames.co']
  linear     id=usr_eac7fcafa75e4935, email=simon.walker@harmonygames.co, name=simon.walker@harmonygames.co, is_active=True   [join: exact_email]
  confluence id=user_STAFF_2, account_id=acct_STAFF_2, email=simon.walker@harmonygames.co, display_name=Simon Walker, is_active=True   [join: exact_email]
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=129939, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
no exact match for 'Nadia'
no exact match for 'Ferreira'
```

| Correct entity | Lookalike | Pin |
|---|---|---|
| Leonard Hayes, Slack EMPLOYEE_0038_SLACK_ID, Trello PERSON_6094_TRELLO_USER_ID, Linear usr_63fffeb4fab5233e | none in scope | `entity.py resolve "Leonard Hayes"` |
| Meta ad account ending 3125 (receipts to Frederick, frederick.stone@harmonygames.co/1836836899676941724) | Leonard's own Meta test account (receipts only in Leonard's mailbox) | H2 scope clause (f_4591ef30be4f920ba1ed14) |
| Unity: two accounts in scope (v3) — the HG account (Domino Delights, statements f_c34b364c50bf4ed59ae6ce …) and the Calm Play LLC account Zombie Match 3D runs from (f_1311b8c998f28831b1cf43 …) | the $1,673.43 prepaid balance stranded in Calm Play in Oct 2024 (frederick.stone@harmonygames.co/1813530307529968502) — a balance, not spend | T22 |
| Adjoe (sender SVC_2836; subjects redact it as `[USERNAME_14101]`) | `[USERNAME_14101]` in #executives (C07C2866011/1757958950.065609) | the adjoe channel C07UCC631A6 |
| outside accountant PERSON_6098 / PERSON_6098_EMAIL (contacts:049f5555b01fd07b0f9d673c; v3: base contacts carry no literal external emails, so the minted next-free token is used) | no Nadia / Ferreira in the base (resolve above) | new contact |
| Domino Delights tests on the "Domino Adventures" listing (B05 f_cc0200cda2a03d6f444916, B06 f_f017eafb1e59601f888460) | Domino Adventures as a separate, deprecated title (trap K02) | the briefs |

## 2 Cohort spine

**Rule (H2, f_4591ef30be4f920ba1ed14).** Paid-UA spend Oct 1, 2024 – Sep 30, 2025 on Meta (ad account ending 3125), Unity Ads, Adjoe,
AppLovin and Google UAC; revenue documents and Leonard's own Meta test account are out. Register grain (red team #10): **one row per
network, month, title and bucket**. The cohort is the set of **source records that decide those rows** — 116: 57 Meta receipt threads
(38 base, 2 seeded copies of base account-3125 receipts held only in Leonard's mailbox, 16 seeded Sep, the seeded Aug 31 late charge), 25 Unity statements (HG account 7 monthly Oct 2024 – Apr 2025; Calm Play 2 monthly Apr – May 2025, 16 weekly Jun – Sep 2025), 18 briefs, 4 Adjoe months (Apr, May, Jun invoices + the
Sep not-payable case), 5 AppLovin ledger months, 7 Google UAC ledger months (FIN-000333 … FIN-000501). The injection
generator emits the exact row set (expected ≈ 55–65 rows) and every total; no hand-typed totals (§2.6 item 14).

| Surface | Tool | Calls × records | Why no bulk | Short-circuit analysis | Requirement → decides |
|---|---|---|---|---|---|
| Unity statement (gsheets, one spreadsheet per period in d_3885933a334aef16e40e84) | gsheets_values_get | 1 × 24 | `gsheets_values_batch_get` reads ranges of one spreadsheet only; no other record has Unity spend | Unity spend per month and campaign is its own register value; Snowflake has $0 | R6 → Unity Ads spend from the statements |
| Test brief (gdocs, one doc per test in d_6930b716ea5b1457adb4a4) | gdocs_get_document | 1 × 12 | a Docs search returns titles and snippets, not the campaign list; counted only for the 12 tests whose names do not say the game (incl. the PvZ / PVZ store-name tests) | the title column depends on the brief; the 6 self-describing ZM tests count 0 | R3 → title per row from the test briefs |
| Meta receipt thread (gmail) | gmail_search_messages + gmail_get_messages_batch | 0.3 × 55 | batch reads collapse bodies (red team #1), so 0.3 per thread: search pages, batches, spill-file chunks of the 28-charge thread frederick.stone@harmonygames.co/1812262106647207041 | payment method and reference number decide net cost and duplicates per charge | R2 → spend, credit used and net cost per row |

**Predicate details.** Net cost = spend unless a Meta charge is paid with advertising credit (credit used = the charge, net 0) — the
seeded Sep 20 charge (Sep 19 spend, $61.40) is paid with advertising credit (red team #14; v3 amount follows Leonard's Sep 19 "$20/day" context). Unity: a top-up is a prepayment, not spend (house rule A15, T20).
Month: Meta = Pacific charge date; Unity = statement month; Adjoe = the month the invoice is for (after the amendment). **Dual regime:**
Sep 12 starts the fundraising bucket for the UK iOS Unity campaigns and the Meta ZM_UK campaigns; the tablet campaign returns to Real
UA from the review day (Sep 18). The September Unity statements (weekly, e.g. f_76007a5c131f92019df2a0 for Sep 15–21) carry daily rows per campaign so the split is
decidable; the generator gives the tablet campaign $0 on Sep 18 itself, so "from the day of the review" and "from the day after" give
the same totals (V3: every fair reading passes).

**Boundary records (A17).** Sep 30 2025 16:40 PT Meta charge (Sep 30 in PT and UTC, before the freeze;
frederick.stone@harmonygames.co/1844734171545827192); Aug 31 2025 15:15 PT charge (late August in both zones;
frederick.stone@harmonygames.co/1842010914816895400); the Aug 6 ZM_UK_vidCPI_football charge (ZM_UK name, before Sep 12 → Real UA;
frederick.stone@harmonygames.co/1839693762261954189); the Sep 12 Unity top-up ($1,000; base receipt 15:11Z, Leonard's "added $1K" C07C2866011/1757689941.099589; his forward to Frederick 15:33Z) inside the Fundraising window
(frederick.stone@harmonygames.co/1843072786759807900).

## 3 Hidden authorities

| Id | Authority (as named) | Home | Governs | Decoy (where Opus looks first) | Decoy scope | Findability proof |
|---|---|---|---|---|---|---|
| H1 | the bucket split agreed on the UA/BD board | trello:68c99c40e5d9eb6f3a988838 (list Doing 66da196af476ab78deaa0cf7) + comment 68d195a805df8c30c455f99c | R4 | confluence:page_ua_spend_buckets + same-board card trello:6807be2c1ea290e4382b33be | game: Domino Delights incent test Apr–Jun vs Zombie Match 3D bridge test Sep | planned seed; a Trello search "UA spend buckets" must return both cards (re-run at /create-injection) |
| H2 | Leonard's close rules for the data room | gdocs:f_4591ef30be4f920ba1ed14 in d_b563e7f1e1608c4d36f3b0 | R1, R2, R5, R11, R12 | gmail:frederick.stone@harmonygames.co/1843732571750494737 (Sep 19 rough rules, same window and purpose) | superseded: oldest entry of T6 (Sep 19 → Sep 26 → Sep 30); the doc says it replaces the 19th | planned seed; "Paid UA close rules" |
| H3 | the Marketing tab of the Q4 board pack | gsheets:f_0cd1e1402e8052d3d4e903 in d_b563e7f1e1608c4d36f3b0 | R9 | gsheets:f_9f7fb3ec09a20b2b6aa6da "Q3 Board Pack - Jul 16" | superseded: older entry of T16 | planned seed; "Board Pack" |
| H4 | the UA test briefs | gdocs folder d_6930b716ea5b1457adb4a4 with 18 briefs (f_6d0c2209baa3ff54633836 …) | R3 | snowflake:ANALYTICS.MARKETING.AD_SPEND.campaign_key | issuer: Singular keys vs Meta Ads Manager names | planned seed; "UA test briefs" |

`governs` sets do not overlap. Per red team #7, H2 now states principles only: it names no trap documents, no Unity cause, no Adjoe
outcome and no gap months. The deciding facts sit in their own records: Unity's missing cost on the Confluence page and the ENG-2362
comment, the Adjoe outcome in the rep's thread reply, the credit in the Adjoe thread, the titles in the briefs.

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Leonard's paid UA true-up request | slack:C07C2866011/1759176840.271025 |

Hub = A1 (Leonard's voice, `texts.py` HUB; no gap description, no "don't trust it" hint). Incorporation table (every quote is an exact substring of the
delegating record's text in `texts.py`, asserted by `build_manifest.py`; the gate re-reads it from the SQL at /create-injection):

| Fragment | Service · container | Kind | Via | Delegated by record | Delegation quote (verbatim) | Requirements | Names authority |
|---|---|---|---|---|---|---|---|
| K1 | slack · C07C2866011/1759176840.271025 | delegation | A1 | C07C2866011/1759176840.271025 | "drop the per-bucket totals as a reply here" | R10 R8 | H1 "buckets are what we agreed on the UA/BD board"; H2 "Close rules are in the doc I put in the data room folder"; H3 "Put it in the Marketing tab of the Q4 board pack" |
| K2 | gdocs · f_4591ef30be4f920ba1ed14 | requirement | A1 | C07C2866011/1759176840.271025 | "Close rules are in the doc I put in the data room folder" | R1 R2 R5 R12 | H4 "Each Meta test has a brief in the UA test briefs folder that says which game it was for." |
| K3 | trello · 68c99c40e5d9eb6f3a988838 | requirement | A1 | C07C2866011/1759176840.271025 | "buckets are what we agreed on the UA/BD board" | R4 | — |
| K4 | gsheets · f_0cd1e1402e8052d3d4e903 Marketing!A1:H1 | format | A1 | C07C2866011/1759176840.271025 | "Put it in the Marketing tab of the Q4 board pack" | R9 | — |
| K5 | gdocs · d_6930b716ea5b1457adb4a4 (18 briefs) | requirement | A1 → K2 | gdocs:f_4591ef30be4f920ba1ed14 | "Each Meta test has a brief in the UA test briefs folder that says which game it was for." | R3 | — |
| K6 | slack · C07C2866011/1759255500.938286 (reply in the hub thread) | amendment | A1 | C07C2866011/1759176840.271025 | "Close rules are in the doc" | R5 | — (amends K2's Adjoe month; rest stands) |
| K7 | trello · comment 68d195a805df8c30c455f99c | amendment | A1 → K3 | trello:68c99c40e5d9eb6f3a988838 | "Spend goes in the bucket that applied on the day it was spent." | R4 | — |
| K8 | gcal · evt_2f9b60002516e45ff04160 | requirement | A1 → K3 → K7 | trello:68d195a805df8c30c455f99c | "from the day of the review" | R4 | — |
| K9 | contacts · 049f5555b01fd07b0f9d673c | recipient | A1 → K2 | gdocs:f_4591ef30be4f920ba1ed14 | "Send the sheet link to our outside accountant." | R11 | — |
| K10 | gdrive · d_b563e7f1e1608c4d36f3b0 | destination | A1 | C07C2866011/1759176840.271025 | "the doc I put in the data room folder" | R9 R11 | — |
| K11 | confluence · page_singular_cost_connectors | requirement | A1 → K2 | gdocs:f_4591ef30be4f920ba1ed14 | "The connector page on Confluence explains what Singular misses." | R12 R6 | — |
| K12 | linear · ENG-2362 comment cmt_6b4787a755ac66787e8c | requirement | A1 → K2 → K11 | confluence:page_singular_cost_connectors | "See ENG-2362." | R6 | — |
| K13 | gsheets · d_3885933a334aef16e40e84 (25 Unity statements) | requirement | A1 → K2 | gdocs:f_4591ef30be4f920ba1ed14 | "Spend is what Unity's statements say we used that month." | R6 R2 | — |
| K14 | slack · C07UCC631A6/1757346020.196019 thread (base replies) | requirement | A1 → K2 | gdocs:f_4591ef30be4f920ba1ed14 | "Use the ledger amount for each invoice, it already has any credit Adjoe gave us." | R7 | — |
| K15 | snowflake · snowflake.json /tables/38 (FINANCE_LEDGER) + /tables/0 (AD_SPEND_DAILY) | requirement | A1 → K2 | gdocs:f_4591ef30be4f920ba1ed14 | "Take the monthly amounts from the ledger." | R2 R12 | — |
| K16 | trello · 68dae1bc8ec7eb683dc15a8d | destination | A1 | C07C2866011/1759176840.271025 | "and on the true-up card when you're done" | R13 | — |
| K17 | gmail · frederick.stone@harmonygames.co/1830999337380347892 (contest + credit reply) | requirement | A1 → K2 | gdocs:f_4591ef30be4f920ba1ed14 | "it already has any credit Adjoe gave us" | R2 | — |

17 fragments · 11 services · 15 containers. **Amendments:** K6 (Slack reply, Sep 30, changes only the Adjoe month: "put Adjoe in the
month the invoice is for, not the month we wired it" — red team #3 wording; "everything else in there stands"), K7 (Trello comment,
Sep 22, changes only the tablet bucket; date from K8). **Non-authoritative distractors:** Robert's reply C07C2866011/1759178460.557708,
the DD bucket card trello:6807be2c1ea290e4382b33be and page confluence:page_ua_spend_buckets (another title and window), the Sep 19
rough rules frederick.stone@harmonygames.co/1843732571750494737 (replaced by the doc). K14's thread holds the Adjoe answer; the rules
only say how Adjoe amounts are sourced (the Sep case is decided by the reply, red team #7).

## 5 Chains and trap register

| Chain | Root cause | Hops (service · record · finding) | Ends in |
|---|---|---|---|
| C1 | A1 | slack C07C2866011/1759176840.271025 Leonard quotes $81,169 → snowflake.json /tables/0 Unity $0, Meta $0 May–Sep → gmail frederick.stone@harmonygames.co/1843154072371887815 receipts bill those months | R12 |
| C2 | A13 | confluence page_singular_cost_connectors "Unity: installs only, see ENG-2362" → linear cmt_6b4787a755ac66787e8c "real Unity spend is on the statements … for our account and the Calm Play one" → gsheets f_1a3c4303fe9b70a0c5d725 (Jul 8–14 statement) | R6 |
| C3 | A14 | slack C07UCC631A6/1757345931.336429 campaign switched on → reply C07UCC631A6/1757349668.681539 not responsible for the cost → snowflake INSTALL_ATTRIBUTION Adjoe Sep installs without spend | R7 |
| C4 | A5 | gmail frederick.stone@harmonygames.co/1823871870039001820 "RE: meta Invoice" = Audience Network → gmail frederick.stone@harmonygames.co/1832284589165430342 Tipalti payout → snowflake.json /tables/38 ad_revenue rows | R1 |
| C5 | A15 | gdocs f_4591ef30be4f920ba1ed14 credit = net 0, top-up ≠ spend → gmail frederick.stone@harmonygames.co/1843788314050589285 Sep 20 $61.40 credit-funded charge → gmail frederick.stone@harmonygames.co/1843072786759807900 Sep 12 Calm Play top-up | R2 |
| C6 | A12 | trello 68c99c40e5d9eb6f3a988838 Fundraising from Sep 12 → trello 68d195a805df8c30c455f99c tablet back "from the day of the review" → gcal evt_2f9b60002516e45ff04160 Sep 18 | R4 |
| C7 | A9 | gmail frederick.stone@harmonygames.co/1830999337380347892 April invoice ($12,005 PDF) → Leonard contests 2,401 invoiced vs 1,923 Singular installs (May 5) → Adjoe credits $1,271.40 (May 7) = snowflake.json /tables/38 FIN-000499 −10,733.60 | R2 |

| Trap | Family | Records | Req | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T1 | distractor (keyword_collision) | 8 "RE: meta Invoice" mails, e.g. frederick.stone@harmonygames.co/1842698832158940633 | R1 | counts them as Meta ad bills | body: Audience Network activity (pays us) | "meta invoice" search hits first |
| T2 | distractor (near_duplicate_record) | 5 Tipalti mails, e.g. frederick.stone@harmonygames.co/1843224116132323892 | R1 | adds "Invoice UI_…" lines | "payment was sent to you" | subject lists invoice numbers |
| T3 | distractor (lookalike_entity) | AppLovin payout mails, e.g. frederick.stone@harmonygames.co/1826512613443318423 | R1 | reads a failed MAX payout as a failed charge | MAX payouts are revenue | — |
| T4 | exact_predicate | duplicates frederick.stone@harmonygames.co/1830495542195061363, /1831122183306732471, /1831236341456877471 + seeded /1843516837725026041 | R2 | counts both notifications | same reference number = one charge | same thread |
| T5 | exact_predicate | frederick.stone@harmonygames.co/1828641403961142838 ($273.26 + $224.59) | R2 | drops one as a duplicate | different reference numbers | looks like the duplicates |
| T6 | superseding (3 versions, 3 services) | gmail frederick.stone@harmonygames.co/1843732571750494737 (Sep 19) → gdocs f_4591ef30be4f920ba1ed14 (Sep 26) → slack C07C2866011/1759255500.938286 (Sep 30) | R5 | Adjoe by wire month (May invoice in July; unwired June dropped) | reply: the month the invoice is for | doc and mail read first; reply in the hub thread |
| T7 | effective_date (3 versions, 2 services) | trello 68c99c40e5d9eb6f3a988838 → evt_2f9b60002516e45ff04160 → trello 68d195a805df8c30c455f99c | R4 | tablet Fundraising all Sep, or from Sep 22 | "from the day of the review" + Sep 18 | date in another service |
| T8 | stale_summary | C07C2866011/1759176840.271025 ($81,169); f_af99b76ff4da59a710edba ("$50K in UA spend") | R8 | reports a summary figure | totals from the register | first hits |
| T9 | tool_surface | snowflake.json /tables/0 (Unity $0); gsheets f_1a3c4303fe9b70a0c5d725 | R6 | Unity at $0 | the statements (C2) | Snowflake before Drive |
| T10 | conclusion_stop | C07UCC631A6/1757345931.336429 → C07UCC631A6/1757349668.681539 | R7 | estimates a Sep Adjoe cost | rep's reply | root reads as open |
| T11 | scope_alias | briefs f_cc0200cda2a03d6f444916 (B05), f_f017eafb1e59601f888460 (B06), f_50ffc8312fcfd96d096754 (B08), f_c37d51b92f6c34b520fd73 (B07) | R3 | ADV under a separate Domino Adventures title; Node_/NM_ as vendor fees; Creative_AB_Test unknown | briefs: Domino Delights (trap K02) | — |
| T12 | exact_predicate (window edge) | frederick.stone@harmonygames.co/1844734171545827192 (Sep 30 16:40 PT = 23:40Z, same day in both zones) | R1 | drops the charge as past the cut-off | the window ends Sep 30; the charge precedes the freeze | — |
| T13 | distractor (non_authoritative_instruction) | C07C2866011/1759178460.557708 (Robert) | R8 | uses the Singular number | no authority | in the hub thread |
| T14 | distractor (scope_adjacent) | trello 6807be2c1ea290e4382b33be; confluence page_ua_spend_buckets | R4 | applies the DD split to Apr–Jun | the Sep card says "This replaces the DD incent test split from April" | Confluence before Trello |
| T15 | reuse_exclusion | trello 68dae1bc8ec7eb683dc15a8d | R13 | creates a new card | the true-up card exists | — |
| T16 | superseding | gsheets f_9f7fb3ec09a20b2b6aa6da (Jul) → f_0cd1e1402e8052d3d4e903 (Sep 29) | R9 | Q3 format, no bucket column | Q4 columns | Q3 pack fuller |
| T17 | near_miss_mention | frederick.stone@harmonygames.co/1839693762261954189 (Aug 6, ZM_UK) | R4 | Fundraising by name | before Sep 12 = Real UA | — |
| T18 | superseding | C07C2866011/1758313330.170339 ("$20/day") → frederick.stone@harmonygames.co/1843878722273509005 | R8 | $20/day for Sep Meta | the receipts | claim met first |
| T19 | synthesis_omission | gsheets f_76007a5c131f92019df2a0 (Sep 15–21 statement) | R4 | one bucket for all of Sep Unity | split by campaign and day | — |
| T20 | exact_predicate | 6 Unity top-ups, e.g. frederick.stone@harmonygames.co/1834226118820623605, /1843072786759807900 (Sep 12) | R2 | counts top-ups as spend (the Sep 12 one as Fundraising) | prepaid: spend = statement | top-ups are card charges in mail |
| T21 | superseding | gmail frederick.stone@harmonygames.co/1830999337380347892 (PDF $12,005, May 2) → credit reply (May 7) | R2 | uses the PDF total | credit reply + H2 ledger clause | the PDF is in the first Adjoe mail |
| T22 | distractor (scope_adjacent) | frederick.stone@harmonygames.co/1839175088393392199 (Calm Play LLC Singular alert); /1813530307529968502 ($1,673.43 stranded); Calm Play statements f_1311b8c998f28831b1cf43 … | R6 | counts the stranded Calm Play balance as spend, or drops the Calm Play statements as the old alpha account (v3) | the Harmony Games account statements | a "Unity" search hits these first |

22 traps · 11 families · 10 requirements · 19 with decisive evidence in rarely-opened services · 5 supersessions (T6 with 3 versions in
3 services; T7 3 versions in 2 services; T16; T18 and T21 cross-service) · 6 distractors of 5 types. Independence: T4/T5 (reference
number) and T12 (window edge) fall to different clauses; T6 and T7 differ in service, owner and requirement; T1–T3 share one
principle (money paid to us) but are counted as three distractors, not three mechanisms; T20 and T22 are different Unity mistakes.

## 6 Failure-diversity plan

| Chain / trap group | Runs that plausibly miss it | Requirements touched | Independent of |
|---|---|---|---|
| C1/T8/T13 summary figures (C07C2866011/1759176840.271025) | runs that quote Snowflake | R8, R12 | H1, H4 |
| C2/T9/T20/T22 Unity (page_singular_cost_connectors, cmt_6b4787a755ac66787e8c) | runs that trust $0, count top-ups or Calm Play | R2, R6 | C3, C6 |
| C3/T10 Adjoe reply (C07UCC631A6/1757349668.681539) | runs that never open thread replies (A14) | R7 | C2, C6 |
| C6/T7/T19 tablet date (evt_2f9b60002516e45ff04160) | runs that skip the comment, use its date, or don't split Sep | R4 | C2, C3 |
| T6 Adjoe month (C07C2866011/1759255500.938286) | runs that read the doc but not the reply | R5 | C6, H4 |
| C7/T21 Adjoe credit (frederick.stone@harmonygames.co/1830999337380347892) | runs that read the PDF and not the ledger clause | R2 | C6 |
| T4/T5/T12 per-charge predicates | runs that count notifications or cut the window early | R1, R2 | the authorities |
| T11 briefs (d_6930b716ea5b1457adb4a4) | runs that guess titles from names | R3 | C1–C7 |

No single discovery gates most requirements: H1 governs R4, H3 R9, H4 R3; H2 is named by the hub and fails runs through per-row
application. Per-bucket totals are graded once (red team #10).

## 7 Deliverables and dependent writes

| Write | Service · target | Tool | Content depends on | Requirements |
|---|---|---|---|---|
| W1 | gsheets f_0cd1e1402e8052d3d4e903 Marketing tab (rows + gap list under the table) | gsheets_values_update ×2 | C1, C2, C4–C7, T4, T6, T11, T12 | R1–R9, R12 |
| W2 | slack reply in thread C07C2866011/1759176840.271025 | slack reply | per-bucket totals | R10 (graded for presence and target; totals graded once in W1) |
| W3 | gmail to the accountant (contacts:049f5555b01fd07b0f9d673c) | gmail_send_message | sheet link; no new sharing (she is a viewer on d_b563e7f1e1608c4d36f3b0) | R11 |
| W4 | trello comment on 68dae1bc8ec7eb683dc15a8d | trello_add_comment | totals | R13 (presence and target) |

Register columns are fixed by H3 (Month · Network · Title · Bucket · Spend (USD) · Credit used (USD) · Net cost (USD) · Source; no Snowflake column, the gap list carries
the Snowflake comparison once). The persona can edit the Q4 pack (Leonard shares it with Frederick as writer — planned seed). The accountant is a
viewer on the data-room folder already (planned seed, red team #15), so sending the link creates one end state.

## 8 Service role map

| Service | Role | Load-bearing fact / write | Carrier |
|---|---|---|---|
| Slack | hub, amendment, Adjoe replies, write W2 | Adjoe month clause; rep's reply (C07UCC631A6/1757349668.681539) | ● message / reply |
| Gmail | Meta receipts, Adjoe credit, top-ups, lookalikes, Sep 19 rules, write W3 | Meta charges (frederick.stone@harmonygames.co/1836836899676941724); credit $1,271.40 | ● body / thread |
| Calendar | effective date | review day Sep 18 (evt_2f9b60002516e45ff04160) | ● start |
| Drive | three folders | live board pack; briefs; statements (d_b563e7f1e1608c4d36f3b0) | ● folder path, sharing |
| Docs | H2 rules + 18 briefs | rules (f_4591ef30be4f920ba1ed14); titles (f_6d0c2209baa3ff54633836 …) | ● body_text |
| Sheets | H3 destination + Q3 pack + 25 statements, write W1 | Unity spend (f_c34b364c50bf4ed59ae6ce …) | ● grid |
| Slides | none (f_7793bb93e59e9c0dee5129 context only) | — | — |
| Contacts | accountant | email (049f5555b01fd07b0f9d673c) | ● email |
| GitHub | none | — | — |
| Linear | ENG-2362 comment | where real Unity spend is kept (cmt_6b4787a755ac66787e8c) | ● comments (§6b verified) |
| Trello | H1 + amendment + decoy + write W4 | bucket rule (68c99c40e5d9eb6f3a988838) | ● desc, commentCard |
| Confluence | connector page + decoy | which networks Singular misses; ledger booking (page_singular_cost_connectors) | ● body |
| Snowflake | warehouse + ledger | Adjoe / AppLovin / Google amounts; network-month gaps (snowflake.json /tables/38) | ● rows |

11 services carry weight; 10 are injected (Slack, Gmail, GCal, Drive, Docs, Sheets, Contacts, Linear, Trello, Confluence).

## 9 Call budget

Necessary calls (all unconditional; `build_manifest.py` BUDGET = the manifest's `call_budget`):

| Phase | Slack | Gmail | Docs | Sheets | Drive | Trello | Confluence | Linear | GCal | Contacts | Snowflake | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| discovery | 4 | 3 | 1 | 1 | 3 | 2 | 1 | 1 | 1 | 1 | 2 | 20 |
| rules | 1 | 1 | 1 | 1 | 0 | 3 | 1 | 1 | 1 | 0 | 0 | 10 |
| per-record | 0 | 19 | 12 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 56 |
| reconciliation | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 9 |
| reads-before-writes | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 |
| writes | 1 | 1 | 0 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 6 |
| **Total** | 9 | 24 | 14 | 32 | 3 | 7 | 2 | 2 | 2 | 1 | 8 | **104** |

Gmail is costed at 0.3 per receipt thread (red team #1); lookalike opens are not counted (their subjects identify them). Per-record:
25 Unity statements (each its own spreadsheet), 12 briefs, Meta threads at 0.3. **Horizon:** 104 is the minimum a correct run needs,
above V3's 100 on a golden run; small margin, measured at the pre-check.

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolved by | Evidence |
|---|---|---|---|---|
| Adjoe month | the month the invoice is for (Apr, May, Jun) | issue month (May, Jun, Jul) or wire month | reply wording "the month the invoice is for" (red team #3) | C07C2866011/1759255500.938286 |
| Adjoe April amount | $10,733.60 (ledger, after credit) | $12,005.00 (PDF) | H2 ledger clause + Adjoe credit reply | frederick.stone@harmonygames.co/1830999337380347892; FIN-000499 |
| AppLovin net cost | the applovin marketing_ua ledger row | spend minus MAX payout | H2 "Don't net AppLovin against our MAX payouts" (red team #5) | f_4591ef30be4f920ba1ed14 |
| Tablet bucket from | Sep 18 (review day) | from the next day, or Sep 22 (comment date) | the tablet has $0 on Sep 18, so Sep 18 vs Sep 19 gives the same totals; Sep 22 is ruled out by "from the day of the review" | trello 68d195a805df8c30c455f99c; evt_2f9b60002516e45ff04160 |
| Sep 30 16:40 PT charge | in | after the cut-off | Sep 30 in PT and UTC; freeze 2025-10-01T00:00Z | frederick.stone@harmonygames.co/1844734171545827192 |
| Dec 31 2024 17:13 PST charge | December (PT) or January (UTC) — both accepted | — | V3 §10: either date unless the prompt names a zone; the rubric accepts both months for this charge | frederick.stone@harmonygames.co/1820007110310927242 |
| Two-message receipt thread | one charge if the reference number repeats; two if it differs | always one / always two | H2 reference-number clause | frederick.stone@harmonygames.co/1830495542195061363; /1828641403961142838 |
| Adjoe September | no cost: a $0 row or no row (both accepted) | estimated cost from installs | the rep's reply | C07UCC631A6/1757349668.681539 |
| Unity top-ups | not spend | spend | H2 prepaid clause | frederick.stone@harmonygames.co/1843072786759807900 |
| Apr–Jun Adjoe / AppLovin bucket | Real UA | Fundraising under the April DD split (V3 review #2) | the Sep 16 card replaces the April split: "nothing before Sep 12 is fundraising" | trello 68c99c40e5d9eb6f3a988838 vs trello 6807be2c1ea290e4382b33be |
| Register destination | Q4 pack in the data room folder | Q3 pack / new sheet | hub names the Q4 pack | f_0cd1e1402e8052d3d4e903 vs f_9f7fb3ec09a20b2b6aa6da |
| Recipient | the accountant in Contacts, no new sharing | Leonard / investors / share the sheet | H2 "already on the data room folder as a viewer … Not to investors" | contacts:049f5555b01fd07b0f9d673c |
| Trello write | comment on the true-up card | new card | hub "on the true-up card" | trello 68dae1bc8ec7eb683dc15a8d |

### Reach table (load-bearing records)

Base records, `persona_view.py can-see frederick_stone …` (78 run this session, all YES; representative lines in §12). Planned seeds are
verified at the injection gate (`check-sql`). LB = load-bearing.

| Record | Service | Verdict | LB |
|---|---|---|---|
| C07C2866011/1757961037.465799 | slack | YES (member of executives) | LB |
| C07C2866011/1758060268.307769 | slack | YES | LB |
| C07C2866011/1758313330.170339 | slack | YES | LB |
| C07UCC631A6/1757345931.336429 | slack | YES (member of adjoe-[ORG]) | LB |
| C07UCC631A6/1757346020.196019 | slack | YES | LB |
| C07UCC631A6/1757348929.625759 | slack | YES | LB |
| C07UCC631A6/1757349668.681539 | slack | YES | LB |
| frederick.stone@harmonygames.co/1812262106647207041 | gmail | YES (own mailbox) | LB |
| frederick.stone@harmonygames.co/1813049887158875039 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1820007110310927242 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1820132039739740641 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1828481095554769555 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1828641403961142838 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1830495542195061363 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1831122183306732471 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1831236341456877471 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1835778053085762169 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1836836899676941724 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1839693762261954189 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1843428112007517388 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1830999337380347892 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1836528865848810632 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1839518563856917373 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1842698832158940633 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1843224116132323892 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1813530307529968502 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1839175088393392199 | gmail | YES | LB |
| f_af99b76ff4da59a710edba | gdocs | YES (shared with the persona) | LB |
| C07C2866011/1759176840.271025 | slack (planned seed) | U4 — verified at injection | LB |
| C07C2866011/1759255500.938286 | slack (planned seed) | U4 | LB |
| frederick.stone@harmonygames.co/1843732571750494737 | gmail (planned seed) | U4 | LB |
| frederick.stone@harmonygames.co/1843154072371887815 | gmail (planned seed) | U4 | LB |
| frederick.stone@harmonygames.co/1843788314050589285 | gmail (planned seed) | U4 | LB |
| f_4591ef30be4f920ba1ed14 | gdocs (planned seed) | U4 | LB |
| f_0cd1e1402e8052d3d4e903 | gsheets (planned seed) | U4 | LB |
| f_76007a5c131f92019df2a0 | gsheets (planned seed) | U4 | LB |
| f_cc0200cda2a03d6f444916 | gdocs (planned seed) | U4 | LB |
| d_b563e7f1e1608c4d36f3b0 | gdrive (planned seed) | U4 | LB |
| d_6930b716ea5b1457adb4a4 | gdrive (planned seed) | U4 | LB |
| d_3885933a334aef16e40e84 | gdrive (planned seed) | U4 | LB |
| evt_2f9b60002516e45ff04160 | gcal (planned seed) | U4 | LB |

No designed denials (no `denied_probes`). The April invoice PDF (att_0001.pdf) is never the deciding record: the deciding amount is in
the ledger and in the credit reply's body text (V3 §9: no deciding evidence in an attachment).

**Feasibility.** Writes exist in `Evals/references/tools/catalog.json` (`gsheets_values_update`, Slack thread reply,
`gmail_send_message`, `trello_add_comment`). The Q4 pack is shared with Frederick as writer; the accountant is already a viewer on the
data-room folder. All amounts are dollars and cents in the records.

**Explicit rules.** H2 month clause per network + K6 (newest wins, rest stands); H1 "the bucket that applied on the day it was
spent"; freeze Sep 30 17:00 PT. Every cross-reference postdates its target: hub (Sep 29 20:14Z) after H2 (Sep 26), H1 (Sep 16), the Q4 pack (Sep 29 19:30Z) and the true-up card (Sep 29 19:45Z) (V3 review #5); H2 says it
replaces the Sep 19 mail; K7 (Sep 22) after K8 (Sep 18); the connector page (Aug 14) cites ENG-2362 (created Jun 3), and Simon's
ENG-2362 comment (Aug 13) points to the statements folder, which holds statements from Oct 2024 on.

**Precedence (carrier eligibility).** Load-bearing facts sit only in ● carriers (Ask_Carriers §5 as amended by §6b): Slack text and
replies, Gmail bodies, Docs body_text, Sheets grids, Trello desc + commentCard, GCal start, Confluence body, Linear comments, Contacts
email, Snowflake rows. No load-bearing fact is in a GCal description, Slides notes, Drive content_text, Contacts description or an
attachment.

**Prompt naturalness constraints (for the human's prompt; V3 §8).** The prompt is the human author's own words, plain prose, clean
spelling, no Markdown or numbered steps. It **names the destinations** Frederick knows (V3: "Name the destination"): the Marketing
tab of the Q4 board pack, a reply in Leonard's #executives thread, the true-up card, and sending it to our accountant. It may name
Leonard's true-up request, the data room / Oct 14 board and the last twelve months. It must not contain: trap hints or riddles ("don't
trust the summary", "go by the rules in the doc"), answer-key clauses ("if two amounts differ…"), spec language, the bucket rule, rule
clauses, Unity's $0 or prepaid model, the Adjoe reply or credit, the lookalikes, reference numbers, the review date, the briefs, the
statements, or any id. Avoid the framings V3 flags as overused: "Actually", "go by the rules in the doc", "don't trust the summary",
shutdown backdrops.

**Grading devices (for the human's rubric; red team #10, V3 §9–§10).** The generator emits the row set (network × month × title ×
bucket), the per-bucket totals and the gap list, each with the record it comes from. V3: one fact per criterion, no fact in three or
more criteria, every fair reading passes. Suggested shape (the human writes the criteria):
- one criterion per **network group** (Meta, Unity, Adjoe, AppLovin, Google UAC), each checking that group's month rows and titles —
  not one exact-set criterion over all rows;
- trap facts graded only where they are not already a group row: Adjoe September ($0 row or no row — both pass), the tablet split after
  Sep 18 (one criterion), the Sep 20 credit-funded charge's net cost (one criterion);
- per-bucket totals graded once (in the sheet); W2 and W4 graded for presence and target only;
- the gap list (17 network-months: Unity Oct 2024 – Sep 2025, Meta May – Sep 2025) as one criterion; the register has no Snowflake
  column, so the warehouse $0 fact appears in that criterion only;
- the recipient (accountant, link only, no new sharing) as one criterion.

Fact budget per criterion (check before writing): the Sep 20 credit feeds the Meta group row and the Fundraising total (2); Adjoe April
feeds the Adjoe group row and the Real UA total (2); Unity's $0 feeds the gap list only (1). Accept rounded and exact figures; either
month for the Dec 31 2024 17:13 PST charge; dates in PT with UTC beside them where the day differs.

### V3 compliance check

Walked against `references/Docs/11_V3_Changes.md` (V3 supersedes the Oct 2 changelog where they conflict).

| V3 rule | Where it applies | Status in this design |
|---|---|---|
| §2 Role is plausible for the prompt | Frederick, Co-founder and UA owner, closing his own channels' spend | met: remit argument §0 |
| §2/§3 Built on the assigned universe date; nothing seeded on or after the freeze | every seeded timestamp | met: latest seed Sep 30 23:40Z; the last Unity export is saved Sep 30 22:30Z with rows through Sep 29; `sql_lint.py` enforces the 2025-10-01 clock |
| §3 A deadline after the freeze is allowed | the Oct 14 board | met: used only as the deadline |
| §2/§5 Difficulty mode Medium: six-rollout average strictly under 85% | baseline | design targets well under; measured at the baseline, not claimed |
| §5 pass@k: five or more full passes of six fails | baseline | a 60-row exact set + four writes makes full passes rare; measured at the baseline |
| §4 Long-Horizon ≥ 100 tool calls on the golden run, else the average | baseline | met by design: honest minimum 104 for a correct run (§9); small margin, measured at the pre-check |
| §5 Opus 5.5 for pre-check and all six baselines | platform runs | process item for the human (select Opus 5.5 before every run) |
| §6 Judge difficulty only after every row is fair | rubric stage | process item: fix unfair rows and re-grade before comparing to 85% |
| §8 Ordinary request, no trap hints / riddles / answer-key clauses, destination named, clean spelling, human-written | the prompt and the hub | constraints above; the hub quotes Snowflake neutrally (no "don't trust it"); the prompt and rubric are written by the human, never drafted here |
| §9 Every row traces to the prompt and tests one fact; no fact in 3+ rows | rubric | grading devices above: per-group criteria, fact budget ≤ 2 per fact, no Snowflake column |
| §9 Accept every fair reading | rubric | Adjoe Sep ($0 row or no row); Dec 31 2024 charge (either month); rounded or exact figures; tablet Sep 18 has no spend; the Sep bucket card replaces the April DD split, so Apr–Jun Adjoe/AppLovin have one bucket |
| §9 Expected values cite and match reachable records; no deciding evidence in Trash, unreferenced comments or attachments | all deciding facts | met: every deciding record is pointed to by an incorporated record; the April PDF is never deciding |
| §10 Pacific dates, UTC beside them when the day differs; either accepted | dates in outputs and rows | met: no seeded charge differs by day between zones; the one base charge accepts both |
| §7 Five reviews in the Eval Portal, whole pass screenshot with verification code | process | process item for the human |

### Seeding rail (cross-service consistency)

| Rule | Plan | Pointer |
|---|---|---|
| Every S1 audit row dispositioned | §1a | coherence_hazards.json T02 T07 T08 S06 R04 R08 Q05 Q08 Q09 L08 L11 L14 I03 I10 I17 X03 |
| Designed disagreements are dated human claims or dated explanations | Leonard's Sep 29 claim; Sep 19 "$20/day"; the Aug 14 ledger-booking note; the May 7 Adjoe credit | C07C2866011/1759176840.271025; C07C2866011/1758313330.170339; page_singular_cost_connectors; frederick.stone@harmonygames.co/1830999337380347892 |
| Unity statements follow the dated budget messages (v3) | daily spend per campaign follows C07C2866011 bid/budget/top-up messages (Oct 9 2024 … Sep 29 2025); no installs column, so Singular's install counts (snowflake.json /tables/0) are never contradicted | `support/task_work/fs_ua_trueup/model.py` |
| Meta Sep receipts do not overlap base ranges | base Sep 16 receipt covers Sep 15; seeded receipts cover Sep 12–14 and Sep 16–30 | frederick.stone@harmonygames.co/1843428112007517388 |
| Companions | hub thread counters; Trello badges + dateLastActivity; one GCal row per attendee calendar; Drive sharing mirrored into docs/sheets; Confluence version rows; ENG-2362 updated_at; Adjoe thread message count | §11 |
| Id schemes | Slack id = sha256(channel\|ts)[:32]; Trello ids from creation seconds; Gmail thread = ms << 20; `f_`/`d_` + 22 hex; `evt_` + 22 hex | `support/task_work/fs_ua_trueup/ids.py` |

## 11 Record plan for /create-injection

| # | Service · table | Records (ids from `ids.py`) | Count | Notes |
|---|---|---|---|---|
| 1 | slack.slack_messages | hub C07C2866011/1759176840.271025, Robert C07C2866011/1759178460.557708, amendment C07C2866011/1759255500.938286 | 3 | UPDATE hub reply_count = 2, reply_users_count, latest_reply |
| 2 | gmail | Sep 19 rough rules frederick.stone@harmonygames.co/1843732571750494737 (Frederick + Arthur + Leonard's Sent) | 3 | `texts.py` H2_V1 |
| 3 | gmail | 16 Meta Sep receipts frederick.stone@harmonygames.co/1843154072371887815 … /1844734171545827192 (#3 duplicate notice, #6 $61.40 credit-funded, #16 Sep 30 16:40 PT) + Aug 31 receipt /1842010914816895400 | 18 | base receipt format (SVC_0521); campaigns ZM_UK_CPE_CopyAds, ZM_UK_Retention_iOS |
| 4 | gmail | 6 Unity top-up receipts frederick.stone@harmonygames.co/1813907358352348391 … /1843072786759807900 (v4: Leonard's forwards of six base "Receipt from Unity Ads" mails; Leonard SENT + Frederick INBOX) | 12 | Leonard's voice; base receipt text quoted |
| 5 | gmail | Adjoe contest (May 5) + credit reply (May 7) added to base thread frederick.stone@harmonygames.co/1830999337380347892 (Frederick + Leonard copies) | 4 | `texts.py` ADJOE_CONTEST / ADJOE_CREDIT |
| 6 | gmail | invitation "Invitation: UA bucket review" to Frederick (INT-11) | 1 | companion of row 8 |
| 7 | trello.trello_cards + trello_actions | H1 68c99c40e5d9eb6f3a988838 (+ create 68c99c40bea93a0a49f0deaf), DD decoy 6807be2c1ea290e4382b33be (+ 6807be2c6be1987c38394c1c), true-up 68dae1bc8ec7eb683dc15a8d (created Sep 29 19:45Z, + 68dae1bc20b9e658fe2b21c0), comment 68d195a805df8c30c455f99c | 7 | list Doing; badges; idShort; dateLastActivity |
| 8 | gcal.gcal_events | evt_2f9b60002516e45ff04160 on Leonard's and Frederick's calendars | 2 | created 2025-09-17T23:10Z |
| 9 | gdrive.drive_files | folders d_b563e7f1e1608c4d36f3b0 (data room; Frederick writer, accountant viewer), d_e4fc39bd54316ab8653b4b (2023 data room), d_6930b716ea5b1457adb4a4 (briefs), d_3885933a334aef16e40e84 (statements); files: the rules doc, 2 board packs, 18 briefs, 24 statements | 49 | sharing mirrored |
| 10 | gdocs.docs_documents | f_4591ef30be4f920ba1ed14 (H2) + 18 briefs f_6d0c2209baa3ff54633836 … f_887def6eed0e1b022f7ab0 | 19 | `texts.py` H2_DOC, BRIEFS |
| 11 | gsheets | f_0cd1e1402e8052d3d4e903 (Q4 pack, created Sep 29 19:30Z, 3 tabs), f_9f7fb3ec09a20b2b6aa6da (Q3 pack), 25 Unity statements f_c34b364c50bf4ed59ae6ce … f_0c302b9a0529823a0c6209, each saved after its period (`ids.UNITY_PERIODS`; the Sep 22–29 export Sep 30 22:30Z) | 26 + tabs | statement grids from the generator; tablet $0 on Sep 18 |
| 12 | contacts.contacts | 049f5555b01fd07b0f9d673c PERSON_6098 (outside accountant) | 1 | — |
| 13 | confluence pages + versions | page_singular_cost_connectors (ENG, Simon, Aug 14), page_ua_spend_buckets (PROD, Frederick, Apr 24) | 4 | version 1 rows |
| 14 | linear.linear_comments | cmt_6b4787a755ac66787e8c on ENG-2362 (Simon, Aug 13) | 1 | UPDATE ENG-2362 updated_at |

Planned ≈ 150 INSERT rows (≥ 120 required) without padding.

### Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| gcal | INT-11 | invitation mail for evt_2f9b60002516e45ff04160 | seed it (row 6) |
| gdrive | INT-13 | Drive Slack app DM on share | none: base shares from Leonard to Frederick carry no DM in this window; declared as an integration exception if base_check asks |
| linear | INT-03 INT-04 INT-05 | linear[bot] / Slack DM / digest mail | none: the comment names no PR and Frederick is not subscribed to ENG-2362 |
| trello | INT-21 | Trello → Slack | none: no Trello integration exists |
| slack | INT-22 | Slack e-mail notification for the @-mention | none: declared at injection if base_check flags it |
| gmail | — | gmail: none (no integration originates in Gmail) | — |
| confluence | — | confluence: none in integrations.json | — |
| contacts | — | contacts: none | — |
| gsheets / gdocs | INT-13 | covered with gdrive | — |

## 12 Self-test results

`python3 Task_Authoring/tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.draft.json --design` (verbatim):

```
HARDNESS GATE (long (design)): PASS
  [ok] effective_profile: effective_profile 'long' for 'Long Horizon' → thresholds 'long'
  [ok] sql_lint_clean: skipped (--design: no SQL yet)
  [ok] base_consistency: skipped (--design: no SQL yet)
  [ok] services_injected: skipped (--design: no SQL yet)
  [ok] rows: skipped (--design: no SQL yet)
  [ok] services_carrying_weight: 11 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: skipped (--design: no SQL yet)
  [ok] seeded_ids_exist_in_sql: skipped (--design: no SQL yet)
  [ok] anchors: 1 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 17 fragments; need ≥ 12
  [ok] ask_fragment_services: 11 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 15 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 13 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 116; need ≥ 30 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 3 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 54; need ≥ 30
  [ok] call_budget: unconditional (verified) floor 104 of 104 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 100 (Long Horizon; plan ~600 for headroom)
  [ok] call_budget_spread: 11 services in budget; largest share outside the per-record phase 19% (≤ 50%)
  [ok] traps: 22 traps across 11 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 10 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 5 supersessions (3 with versions in ≥ 2 services, 2 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 6 distractors of 5 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 12 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 7 chains with 7 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] hidden_authorities: 4 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 1 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 19 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 13 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 4 writes over 4 services; each must depend on findings
```

**Lazy-solver pass** (one broad search per service, first hits, no replies, first conclusion, every bulk shortcut):

| Leak found | Fix |
|---|---|
| v1 hub stated "Unity is $0 in there and Meta stops after April" (C07C2866011/1759176840.271025) | removed; the hub only quotes the total, neutrally ("Snowflake has $81,169 for it", V3 review #6) |
| v1 rules named the revenue lookalikes, the Unity cause and the Adjoe outcome (f_4591ef30be4f920ba1ed14) | rules state principles; facts moved to page_singular_cost_connectors, cmt_6b4787a755ac66787e8c, the adjoe reply and the credit thread |
| The connector page names networks (page_singular_cost_connectors) | it gives no months or amounts; the gap list still needs the sources per month |
| "Advertising credit" search returns the credit-funded receipts (frederick.stone@harmonygames.co/1843788314050589285) | accepted: the amount and month still need each charge; the rule word never sits next to a total |
| v1 decoys failed on title (Q2 window) — red team #12 | H2's decoy is now the Sep 19 mail with the same window and purpose, differing on Unity, Meta and Adjoe clauses |

**Literal-value sweep** (to re-run at /create-injection with `tools/hg.py search search-many` once the SQL exists): "Sep 18", "3125",
"1,271.40", "10,733.60", "the month the invoice is for", "Fundraising". `texts.py` keeps "Sep 18" out of every rule-bearing record except the
calendar event and its INT-11 invitation mail (the comment says "the day of the review"); the date appears elsewhere only as a receipt range or statement date; $1,271.40 only in the Adjoe thread (contest line and credit reply).

**"The rest stands" check.** K6 changes only the Adjoe month; no later record restates the wire-month clause. K7 changes only the
tablet bucket; no later record restates "phone and tablet" for Fundraising after Sep 22.

Representative `persona_view.py can-see frederick_stone` lines (78 run, 78 YES):

```
frederick_stone gmail frederick.stone@harmonygames.co/1836528865848810632: YES
frederick_stone slack C07UCC631A6/1757346020.196019: YES
frederick_stone slack C07UCC631A6/1757349668.681539: YES
frederick_stone slack C07C2866011/1757961037.465799: YES
frederick_stone gmail frederick.stone@harmonygames.co/1813530307529968502: YES
frederick_stone gmail frederick.stone@harmonygames.co/1839175088393392199: YES
frederick_stone gdocs f_af99b76ff4da59a710edba: YES
```

### Self-review

Re-read `Evals/1_Prompt_Eval.md` §2.1, §2.2, §3.2, `Evals/0_Injection_Quality_Eval.md` Check C and `references/Docs/11_V3_Changes.md`,
then walked the design in order.

| # | Check / category | Verdict | Counter-reading (strongest argument the other way) | Resolution with evidence |
|---|---|---|---|---|
| 1 | temporal | PASS | post-freeze base records (C07UCC631A6/1759326759.229719, Oct 1 "invoice got sent out") are visible | no requirement reads them; the designed Adjoe answer agrees with them; hazard T07 avoid |
| 2 | temporal (seeded) | PASS | the Sep 30 16:40 PT charge sits 20 minutes before the freeze | 2025-09-30T23:40Z < 2025-10-01T00:00Z (V3 §3); frederick.stone@harmonygames.co/1844734171545827192 |
| 3 | temporal (overlap) | PASS | a seeded receipt could double-bill a base date range (red team #11) | Aug 31 charge covers Aug 18–31; the only Aug base receipt frederick.stone@harmonygames.co/1839693762261954189 covers Jul 15–17 |
| 4 | temporal (time zone) | PASS | a charge near midnight could fall in two months (V3 §10) | sweep found one base case (frederick.stone@harmonygames.co/1820007110310927242): both months accepted; no seeded case (Aug 31 moved to 15:15 PT) |
| 5 | semantic | PASS | "Meta Invoice" mails are genuinely Meta invoices | bodies say Audience Network activity = money paid to us; H2 "Money a network pays us is not spend" (frederick.stone@harmonygames.co/1842698832158940633) |
| 6 | semantic (titles) | PASS | ADV could be the separate Domino Adventures Unity game (frederick.stone@harmonygames.co/1813530307529968502) | briefs B05/B06/B08 (f_cc0200cda2a03d6f444916) say ADV is the store listing DD tested under |
| 7 | cross-service referential | PASS | the hub cites "the true-up card" and "the doc I put in the data room folder"; a dropped seed dangles | both planned and dated before the hub (trello 68dae1bc8ec7eb683dc15a8d, f_4591ef30be4f920ba1ed14); injection gate checks seeded ids |
| 8 | quantitative | PASS | ledger and warehouse agree with each other but not with the sources — system vs system (Atlas rule 12) | the Aug 14 connector page dates and explains it (both booked from Singular); reconciling is R12; hazard Q08 dated_claim |
| 9 | quantitative (Adjoe) | PASS | the April PDF says $12,005.00 vs ledger $10,733.60 (red team #2) | seeded dated credit reply in frederick.stone@harmonygames.co/1830999337380347892 ($1,271.40) + H2 ledger clause; PDF never deciding |
| 10 | quantitative (Unity) | PASS | nine months of Unity installs with no billing (red team #4) | 25 statements (both Unity accounts; v3 drops the installs column so Singular's counts in snowflake.json /tables/0 are never contradicted; spend follows the dated budget messages); prepaid model per frederick.stone@harmonygames.co/1813530307529968502 |
| 11 | state/lifecycle | PASS | June Adjoe booked (FIN-000555) yet still outstanding on Aug 4 (red team #9) | the connector page says the ledger's marketing rows are booked from Singular per month, not cash; no paid column; snowflake.json /tables/38 |
| 12 | identifier/format | PASS | v1's ZOM-673 broke creation order (red team #8) | removed; the Unity note is a comment on base ENG-2362 (created Jun 3, Todo) |
| 13 | other (persona plausibility, V3 role) | PASS | Frederick is laid off on Oct 24 (after the freeze); a finance close may look like Leonard's job | at the freeze he is `active_sep_2025` and owns these channels (C07C2866011/1757961037.465799); Leonard delegates it to him in the hub |
| 14 | DP Adjoe month | PASS | "everything else in there stands" might keep the wire clause for wired invoices | the reply names the clause it replaces; C07C2866011/1759255500.938286 |
| 15 | DP Adjoe amount | PASS | a run may prefer the vendor's own PDF | H2 "Use the ledger amount for each invoice"; credit reply in frederick.stone@harmonygames.co/1830999337380347892 |
| 16 | DP AppLovin | PASS | spend minus MAX payout is a defensible net (red team #5) | H2 "Don't net AppLovin against our MAX payouts" (f_4591ef30be4f920ba1ed14) |
| 17 | DP tablet date | PASS | "the day of the review" could mean from the next day | the tablet has $0 on Sep 18 (f_76007a5c131f92019df2a0, generator), so both readings give the same rows; evt_2f9b60002516e45ff04160 |
| 18 | DP Sep 30 boundary | PASS | a run may cut the window at Sep 30 00:00 | the window is "Oct 1 to Sep 30" and the charge is Sep 30 in both zones; frederick.stone@harmonygames.co/1844734171545827192 |
| 19 | DP Dec 31 2024 charge | PASS | grading one month only would fail a fair reading (V3 §10) | both months accepted (grading devices); frederick.stone@harmonygames.co/1820007110310927242 |
| 20 | DP duplicate thread | PASS | Meta may genuinely bill the same amount twice | identical reference numbers ([TAX_ID_4752] twice in frederick.stone@harmonygames.co/1830495542195061363) |
| 21 | DP Adjoe September | PASS | with no invoice, a row may be unnecessary | both a $0 row and no row are accepted (grading devices §10); C07UCC631A6/1757349668.681539 |
| 22 | DP Unity top-ups | PASS | a top-up is real cash leaving the company | H2 defines spend for Unity as the statement; frederick.stone@harmonygames.co/1843072786759807900 |
| 23 | DP destination | PASS | two data-room folders (d_b563e7f1e1608c4d36f3b0, d_e4fc39bd54316ab8653b4b) | the 2023 folder holds no Q4 pack; the prompt names the board pack (V3 §8) |
| 24 | DP recipient | PASS | the accountant may also need the sheet shared (red team #15) | H2 "already on the data room folder as a viewer, so no new sharing" |
| 25 | DP Trello write | PASS | the bucket card is also "the card" | the hub and the prompt say "the true-up card" (68dae1bc8ec7eb683dc15a8d) |
| 26 | Feasibility §2.2 | PASS | the 28-message Oct 11 thread may spill to a file | counted in the 0.3 per-thread cost; frederick.stone@harmonygames.co/1812262106647207041 |
| 27 | Injection Check C | PASS | 25 Unity statements and 18 briefs have no base precedent as files | Frederick owns base Docs / Sheets (census: owned=46) and ran the Unity account; statements are Google Sheets, not attachments |
| 28 | V3 compliance (§10 table) | PASS | a golden run could be efficient and land under 100 (V3 review #1) | the honest minimum for a correct run is now 104 (§9: 25 statements, 12 briefs); small margin, pre-check measures |
| 30 | V3 fair readings (bucket rule) | PASS | the April DD card on the same board could govern Apr–Jun (V3 review #2) | the Sep 16 card text says it replaces the April split (trello 68c99c40e5d9eb6f3a988838) |
| 31 | V3 one fact per row | PASS | one exact-set criterion plus spot checks and totals would grade a fact 3+ times (V3 review #3) | per-group criteria and a fact budget of ≤ 2 (§10); no Snowflake column; f_0cd1e1402e8052d3d4e903 header A1:H1 |
| 32 | V3 freeze (statement) | PASS | a full-September statement cannot exist before the freeze (V3 review #4) | the last export covers Sep 22–29, saved Sep 30 22:30Z (f_0c302b9a0529823a0c6209) |
| 29 | hardness_gate output (HARDNESS GATE (long (design)): PASS, pasted in §12) | PASS | the long profile is a bundle change made in this session | requester-confirmed (`profile_exception`); its floor equals V3's 100; §0 |

Load-bearing base values re-read through the exports in this session: warehouse TTM $81,168.77 and unity_ads installs per month
(snowflake.json /tables/0), ledger FIN-000499 (−10,733.60), FIN-000529 (−20,537.92), FIN-000555 (−14,930.02), the 85 in-window
receipt messages, their 36 campaign names and the one zone-crossing charge, the adjoe thread structure (root C07UCC631A6/1757346020.196019,
six replies), the Unity prepaid mail (frederick.stone@harmonygames.co/1813530307529968502).

Unresolved: (1) the horizon margin is small (104 honest vs 100); the Opus pre-check records the measured count; (2) the v2 fixes
after the V3 review and the v3 injection-stage fixes (§13c) were not re-reviewed by a red team.

```
STAGE GATE scenario: PASS — Task_Authoring-2/task_inputs · 01_Scenario_Design.md#23e3fa08eb19 · 01_Hardness_Manifest.draft.json#0b36d392118d · blocking 0 · warnings 0 · checks 26
[PASS] structure.outputs: 2 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 14/14 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 27/27 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 4/4 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 18/18 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 29/29 items carry a source pointer (min 90%)
[PASS] evidence.record_plan: 20/23 items carry a source pointer (min 80%); unsourced e.g. L586: 'gmail | — | gmail: none (no integration originates in Gmail) | —'
[PASS] evidence.active_speakers: 4/4 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for frederick.stone@harmonygames.co and matches the re-run (106 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 20 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 4 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (7 INT ids, services ['confluence', 'contacts', 'gcal', 'gdocs', 'gdrive', 'gmail', 'gsheets', 'linear', 'slack', 'snowflake', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts ['GM-TF-ZombieMatch3-frederick.stone']; trap_catalog ['B02', 'B04', 'B05', 'C01', 'D01', 'D04']
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: red team unavailable, error recorded
[PASS] reach.scenario: 41 scoped load-bearing ids YES for frederick_stone (13 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 31 evidenced counter-readings (of 32 found; need ≥ 20) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```






## 13 Red team (dual)

RED TEAM UNAVAILABLE: redteam_review: set REDTEAM_MODEL or pass --model (no REDTEAM_* environment configured — error)

Substitute: one independent reviewer (a fresh subagent with only the v1 design, manifest, `texts.py` and the eval rules) red-teamed v1.
All 15 findings and their v2 dispositions:

| Finding | Source | Disposition with evidence |
|---|---|---|
| 1 Blocker: Gmail per-thread reads collapse with batch calls; golden run could fall under 100 | subagent | fixed in costing: Gmail at 0.3 per thread; per-record Sheets (24 statements) and Docs (12 briefs) added (option A, V3 review); honest minimum 103 ≥ V3 100 (§0, §9) |
| 2 Blocker: April Adjoe PDF $12,005 vs ledger $10,733.60 | subagent | fixed: dated contest + credit reply ($1,271.40) seeded in frederick.stone@harmonygames.co/1830999337380347892; H2 says ledger amount after credit; false "can't open attachments" line removed (T21) |
| 3 "The month on the invoice" has two readings | subagent | fixed: amendment says "the month the invoice is for" (C07C2866011/1759255500.938286) |
| 4 Unity installs every month, prepaid model contradicted | subagent | fixed: Unity modelled as prepaid top-ups (not spend) + 24 statements matching warehouse installs (d_3885933a334aef16e40e84) |
| 5 AppLovin net cost two readings | subagent | fixed: H2 "Don't net AppLovin against our MAX payouts" (f_4591ef30be4f920ba1ed14) |
| 6 Legend missed base campaign names | subagent | fixed: legend replaced by 18 briefs covering all 36 swept campaign names (d_6930b716ea5b1457adb4a4) |
| 7 Seeded records stated chain conclusions | subagent | fixed: hub and rules reduced to principles; facts moved to page_singular_cost_connectors, cmt_6b4787a755ac66787e8c, the adjoe reply, the credit thread |
| 8 ZOM-673 out of creation order | subagent | fixed: comment on base ENG-2362 instead (linear:ENG-2362) |
| 9 Ledger dates vs wires; ledger Meta vs receipts | subagent | fixed: dated explanation on page_singular_cost_connectors (booked from Singular per month); register has no paid column |
| 10 Grading devices vs row rules; totals graded three times | subagent | fixed: row grain network × month × title × bucket; Adjoe Sep optional; totals graded once; W2/W4 presence and target (§10) |
| 11 Jun 30 boundary overlapped a base range | subagent | fixed: replaced by an Aug 31 15:15 PT charge (frederick.stone@harmonygames.co/1842010914816895400), same day in PT and UTC (V3 §10) |
| 12 Decoys self-advertise by title | subagent | fixed for H2 (Sep 19 mail, same window and purpose, frederick.stone@harmonygames.co/1843732571750494737); H1/H3 decoys keep a different scope / older version by design |
| 13 Wrong thread root; TRUEUP window; "call yesterday" | subagent | fixed: root C07UCC631A6/1757346020.196019; true-up card says Oct 1 to Sep 30; H1 cites the executives thread |
| 14 Credit-funded charges too small to matter | subagent | fixed: seeded Sep 20 charge paid with a $150 advertising credit (frederick.stone@harmonygames.co/1843788314050589285) |
| 15 Accountant's access to the sheet unspecified | subagent | fixed: she is already a viewer on the data-room folder; H2 says no new sharing (d_b563e7f1e1608c4d36f3b0) |

### 13b V3 review of v2 (independent subagent, `11_V3_Changes.md` only)

| Finding | Source | Disposition with evidence |
|---|---|---|
| 1 Major: honest minimum 89 < V3's 100; a golden run could fail Wrong Horizon | V3 subagent | fixed: weekly Unity statements Jun – Sep 2025 (24 in all) and the PvZ briefs; honest minimum 103; floor 100 (§9, d_3885933a334aef16e40e84) |
| 2 Major: the April DD bucket card is a second fair reading for Apr–Jun | V3 subagent | fixed: the Sep 16 card says it replaces the April split (trello 68c99c40e5d9eb6f3a988838); two-reading row added |
| 3 Major: exact-set + spot checks + totals grade one fact 3+ times | V3 subagent | fixed: per-group criteria, fact budget ≤ 2, Snowflake column removed (f_0cd1e1402e8052d3d4e903 Marketing!A1:H1) |
| 4 Major: a full-September statement cannot predate the freeze | V3 subagent | fixed: last export Sep 22–29 saved Sep 30 22:30Z; every statement's saved-at time pinned (f_0c302b9a0529823a0c6209) |
| 5 Minor: hub cites the Q4 pack and true-up card before they exist | V3 subagent | fixed: pack Sep 29 19:30Z, card Sep 29 19:45Z, hub 20:14Z (trello 68dae1bc8ec7eb683dc15a8d) |
| 6 Minor: "I don't trust it" acts as a trap hint | V3 subagent | fixed: "Snowflake has $81,169 for it" (C07C2866011/1759176840.271025) |

### 13c Injection-stage revision (v3, `/create-injection` base read)

Implementing the SQL meant re-reading every base record the statements, top-ups and receipts sit next to. Five design facts did not
survive that read; the design and the draft manifest were changed here and both gates re-run (playbook 01 Universe Injection,
"update the design and its draft manifest, re-run the design gate"). The final manifest records the same items in `design_delta`.

| Finding (base evidence) | Change | Evidence |
|---|---|---|
| ZM3D Unity campaigns ran from the Calm Play LLC Unity account from May 2025 ("another $1k on the CalmPlay Unity account … not our Harmony Games account", "We may need to keep running our Unity campaigns out of the CalmPlay account") — v2 treated Calm Play as out of scope | H2 scope names "Unity Ads (our account and the Calm Play one we run Zombie Match 3D from)"; statements per account (HG 7 monthly; Calm Play 2 monthly + 16 weekly = 25); T22 now = stranded $1,673.43 balance or dropping Calm Play | C07C2866011/1747847918.209079; C07C2866011/1752552226.101149; frederick.stone@harmonygames.co/1813530307529968502 |
| v2 top-up dates (Jan 8, Apr 3, Jul 21, Sep 11) matched no base balance message | top-ups Oct 29, Dec 24 2024; May 21, Jun 10, Jul 25, Sep 12 2025 (the Sep 12 one inside the Fundraising window) | C07C2866011/1729874790.378899 ("final $200"); C07C2866011/1735082160.147609 ("added $2K"); C07C2866011/1757689941.099589 |
| v2 statements equalled Singular's install counts while base Slack shows Unity and Singular disagree ("Unity thinks we should have 81 installs") | statements carry spend only (Date, App, Campaign, Spend); daily spend follows the bid/budget messages (Sep 12 $400/day, Sep 13 "$600/day", Sep 15 $150/campaign, Sep 16 $5 CPI, Sep 19 budget $1, Sep 29 22:48Z $150/campaign) | C07C2866011/1757793516.055679; C07C2866011/1758060268.307769; C07C2866011/1758313197.701479; C07C2866011/1759186080.203099 |
| AppLovin Jun and Jul 2025 ran on both games in AD_SPEND_DAILY, so "one row per month" and "one row per … title" were two fair readings | H2: "Take the monthly amounts from the ledger. Where a month ran on both games, split it by game the way AD_SPEND_DAILY does." (K15 quote) | snowflake.json /tables/38 FIN-000556, FIN-000579; snowflake.json /tables/0 |
| Two account-3125 receipts exist only in Leonard's / Robert's mailboxes (May 6 $136.50, Jun 6 $143.06); Meta Sep spend of ~$150/day contradicted Frederick's Sep 16 "$80 of spend" and Leonard's Sep 19 "$20/day" context | Frederick's copies of the two receipts seeded (cohort 57 Meta threads); Sep receipts $0.07–$186.40/day, the credit-funded one $61.40; H2 "Use the receipts, even where Snowflake shows something else" | leonard.hayes@harmonygames.co/1831357378751331011; leonard.hayes@harmonygames.co/1834164377682810022; C07C2866011/1758033786.874909 |
| base Contacts hold no literal external email (171 contacts, 0 literal) | accountant = minted next-free token PERSON_6098 / PERSON_6098_EMAIL | contacts:049f5555b01fd07b0f9d673c |

Effect: cohort 116, honest call minimum 104 (25 statements), design gate `HARDNESS GATE (long (design)): PASS` (§12, re-run).

### 13d Revision v4 (after `/injection` advisories and the `/prompt` FAIL on Cross-Service Coherence, 2026-10-22)

`/prompt` (attempt 6ad83eebbd6456fd065bbd20) scored the prompt 5 on every prompt dimension but Cross-Service Coherence 2: two
minor inconsistencies in task-touched data. `/injection` had raised the top-up advisory earlier. Fixes, with no change to any
register value, bucket, gap month, trap answer or the call budget:

| Defect | Fix | Evidence |
|---|---|---|
| brief "Started:" dates after the campaigns were billed (ZM UK statics 2025-08-04 vs receipt Jul 15–17; Android CA/AU NZ re-test 2025-01-03 vs Dec 30 – Jan 2) | swept all 18 briefs against the first receipt or ad-approval mail naming each campaign in Frederick's mailbox; nine briefs re-dated to that date (B04 Oct 19, B06 Nov 17, B08 Dec 30 2024; B11 Apr 8, B13 Jun 13, B14 Jun 14, B15 Jul 6, B16 Jul 15, B17 Jul 6 2025) and the "Started:" line dropped (a brief records the game, not the launch) | frederick.stone@harmonygames.co/1839693762261954189; frederick.stone@harmonygames.co/1820132039739740641 |
| connector page called FINANCE_LEDGER rows "booked from Singular's cost" while the table comment says "Signed cash movements including inflows" and Adjoe rows sit on invoice month-ends before the wires | page now says the marketing_ua amounts come from the same Singular cost and that the ledger books operating costs by month (dated to the month's last day, not the day money moved) — true of every in-window operating row (snowflake.json /tables/38) | page_singular_cost_connectors |
| seeded Unity top-up notices sat minutes from base "Receipt from Unity Ads" mails in Leonard's mailbox with other amounts and accounts (Eval 0 advisories 1–2) | the six top-ups are now Leonard's forwards to Frederick of six base receipts (Oct 25, Dec 24 2024; May 21, Jun 6, Jul 25, Sep 12 2025), quoting them verbatim; no seeded Unity sender mail; amounts $2,000, $2,000, $1,000 ×4 | leonard.hayes@harmonygames.co/1843071417603742140 → frederick.stone@harmonygames.co/1843072786759807900 |
| Adjoe credit Message-ID encoded an Oct 2025 SES timestamp (Eval 0 advisory 3) | SES prefix now encodes 2025-05-07 09:12Z (01070196aa042300) | frederick.stone@harmonygames.co/1830999337380347892 |

Unchanged: T20 still tests counting top-ups as spend (the Sep 12 forward lies in the Fundraising window); C5 hop 3 is the Sep 12
forward. Residual: the newer-format base receipts say the details are "as an attachment"; the forwards carry no attachment
(not deciding evidence; the amount is in the body).

### 13e Revision v5 (second `/prompt` run, Cross-Service Coherence 2, 2026-10-22)

| Defect | Fix | Evidence |
|---|---|---|
| Leonard's May 5 Adjoe contest said "From our Singular export: … CA,212,1271.40", but the Singular-built tables have no Canada Adjoe installs for Apr 2025 (AD_SPEND_DAILY 20 US rows, 1,923 installs; INSTALL_EVENTS 0 CA) | the email now says Singular shows no Canada installs and quotes the two lines "From the invoice". The credit reply ($1,271.40 → $10,733.60) and FIN-000499 are unchanged | frederick.stone@harmonygames.co/1830999337380347892; snowflake.json /tables/0 |
| FINANCE_LEDGER table comment "Signed cash movements including inflows." vs month-end-dated rows (FIN-000529 2025-05-31; the 05/2025 wire went out Jul 3) | not fixable by SQL: the comment is base Snowflake metadata and Snowflake is not injectable. The connector page documents the month-end convention. With the email fixed, this is the one remaining minor inconsistency (QC form: Non-Fail 3) | snowflake.json /tables/38; frederick.stone@harmonygames.co/1836528865848810632 |

### 13f Revision v6 (`/injection` rev 7 advisory 1, 2026-10-22)

| Defect | Fix | Evidence |
|---|---|---|
| v5 said "From the invoice: CA,212,1271.40", but the invoice export shows 2,401 installs for $12,005.00 (a flat $5.00 each), so 212 installs for $1,271.40 (about $6.00) cannot come from it, and at $5.00 the credit is no whole number of installs | the Canada claim is gone. Leonard contests the gap between the invoice's 2,401 installs and Singular's 1,923 (AD_SPEND_DAILY adjoe 2025-04, the Q3 pack's 1,923). Adjoe grants a partial credit of $1,271.40 ("part of the gap is installs Singular doesn't count"). $1,271.40, $10,733.60 and FIN-000499 are unchanged; $10,733.60 / 1,923 = $5.58, the Q3 pack's CPI | frederick.stone@harmonygames.co/1830999337380347892; snowflake.json /tables/0; f_9f7fb3ec09a20b2b6aa6da |


### 13g Revision v7 (third `/prompt` run, 2026-10-22)

| Finding | Disposition | Evidence |
|---|---|---|
| "Robert's mailbox has 12 in-window account-3125 receipts Frederick lacks ($3,720.06)" | false positive, no change. All 12 are in Frederick's own mailbox with identical reference numbers and transaction IDs (e.g. $596.00 Oct 24–26, ref [TAX_ID_13351], tx [IDENTIFIER_38151]). They sit inside multi-message threads, which the reviewer appears to have missed. Swept every mailbox by (amount, date range): the only in-window charges outside Frederick's base mailbox are May 3–4 $136.50 and May 5–20 $143.06, both already seeded as Frederick copies | frederick.stone@harmonygames.co/1814042565503776727; frederick.stone@harmonygames.co/1812262106647207041; frederick.stone@harmonygames.co/1836905421544429882 |
| Android Nordics brief (created Nov 17, 2024) says "Ran on and off until April" | the note is now a dated closing update ("Update Apr 28: ran on and off until April, now off.") and the doc's modified time is 2025-04-28, after the last billed run (Apr 26) | f_f017eafb1e59601f888460 |
| iOS CA brief (Apr 2, 2025) says "Last DD test before we stopped DD marketing", contradicted by the Apr–Jun DD incent test and DD spend through July | the note now describes the test only ("Tutorial-complete optimisation on iOS in Canada, Domino Adventures listing.") | f_9e4be4822ec79ce7ff5d17 |
| FINANCE_LEDGER comment vs month-end rows | unchanged: base Snowflake metadata (§13e) | snowflake.json /tables/38 |
