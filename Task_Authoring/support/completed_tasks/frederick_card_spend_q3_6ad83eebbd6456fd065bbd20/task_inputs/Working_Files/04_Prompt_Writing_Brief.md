# Prompt Brief — fs-paid-ua-trueup · prep
> Built 2026-10-22 from 00_Assigments.md, 01_Universe_Inject.sql (sha256 c983da3d0a7d, revision v7), Working_Files/01_Grounding_Dossier.md,
> 01_Scenario_Design.md, 01_Hardness_Manifest.json, 03_Error_Async_Config.txt (Friction: none) · no
> 02_Reference_Files_Manifest.md (no attachments; V3 forbids deciding evidence in attachments) · Persona view verified: all
> load-bearing records YES for frederick_stone (Leonard's and Arthur's mailbox copies are NO and are not needed).
> **Authorship (V3, `references/Docs/11_V3_Changes.md` §8, overrides GEN_EXECUTION §2):** the human writes every word of
> `04_Prompt.txt`. This brief holds facts, noun phrases and locators only. It contains no draft sentence, and draft mode is not used for this task.
> **Clock:** the bundle's 2026-02-14 default does not apply. The universe date is Oct 1, 2025. Under V3 §3 the freeze is
> 00:00 UTC (Tue Sep 30, 2025, 5:00 PM PT), the stricter reading of the assignment's "October 1, 2025 07:00". The latest seeded
> event is 2025-09-30T23:40:00Z (4:40 PM PT), which is before both readings.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Executive → Finance / Legal / HR / Ops (`Evals/references/rules/task_categories.md`) | a financial reconciliation for a fundraising data room; Leonard's ask C07C2866011/1759176840.271025 |
| Persona / role | Frederick Stone, frederick.stone@harmonygames.co, Co-founder (roster `frederick_stone`, Executive) | Voice: short, casual and numbers-first, e.g. "Both Unity campaigns (phone and tablet) capped out today. I just reduced CPI bid from $6 to $5." (C07C2866011/1758060268.307769). Remit: he runs UA. He proposed the two buckets (C07C2866011/1757961037.465799), the Meta account ending 3125 bills his inbox (frederick.stone@harmonygames.co/1836836899676941724), and the true-up card says "Frederick owns it" (68dae1bc8ec7eb683dc15a8d). Read scope: own mailbox, own calendar, #executives C07C2866011 and the adjoe channel C07UCC631A6 (both member), and the Drive items shared with him |
| Role plausibility (V3 §2) | Co-founder | a co-founder who owns the ad networks being asked by the CEO for the real paid UA number for the data room is ordinary co-founder work (C07C2866011/1759176840.271025) |
| Competency | Finance | a network-by-month paid-UA reconciliation against the warehouse and the ledger; the output is a register in the board pack (f_0cd1e1402e8052d3d4e903) |
| Task skill | Analysis and synthesis | about 116 source records (57 Meta receipt threads, 25 Unity statements, 18 briefs, Adjoe/AppLovin/Google ledger months) joined under four rule sources; the authored artifact is the Marketing-tab register plus the gap list (W1). A chat reply alone would not exercise it |
| Task type / tier | Long Horizon (100–500+ calls); V3 minimum 100 | Weight-bearing services and measured volumes: Gmail 57 receipt threads + 6 top-ups + Adjoe thread; Sheets 25 statements + 2 packs; Docs 19; Drive 4 folders; Slack 3 seeded + 34 base Adjoe hits; Trello 3 cards / 4 actions; Confluence 2 pages; Linear 1 comment; Calendar 2 events; Contacts 1; Snowflake AD_SPEND_DAILY 2,590 rows + FINANCE_LEDGER. 11 services; honest minimum 104 calls (design §9). `HARDNESS GATE (long): PASS` is pasted in the dossier |
| Difficulty mode / date | Medium (six-rollout average strictly under 85%); Oct 1, 2025 | the prompt must not say anything after Sep 30, 5:00 PM PT has happened; the Oct 14 board (evt_bd61f3209523d19fdd6ba2) is a future deadline |

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
|---|---|---|---|
| Leonard needs "the real paid UA number for the last twelve months" for the data room and the Oct 14 board. He quotes Snowflake's $81,169 and points to his close rules, the bucket split on the UA/BD board and the Q4 board pack | Frederick, @-mentioned in #executives | C07C2866011/1759176840.271025 (Mon Sep 29, 1:14 PM PT) | Leonard's copy of the Sep 19 rough-rules mail (leonard.hayes@harmonygames.co/1843732571750794917; Frederick holds his own copy) |
| Robert replies that they should just give the data room the Singular number | Frederick | C07C2866011/1759178460.557708 | — (no hidden record needed) |
| The task card waits on the UA/BD board, in Doing, with Frederick as a member | Frederick | trello 68dae1bc8ec7eb683dc15a8d | base Unity Ads receipts in Leonard's mailbox (e.g. leonard.hayes@harmonygames.co/1838649409811811442); not needed, since top-ups are not spend |

No cause belongs in the situation. Why Snowflake is short (Unity cost never reaches Singular; Meta connector lost access in May) is discovery-only (§5, never in the prompt).

## 3 · Investigation → action

Questions to resolve (no answers here):
1. Which rules govern the number, and in what order were they replaced (mail of the 19th, the doc, the thread reply)?
2. Which networks, ad accounts and months count, and what counts as spend for each network?
3. Which game each Meta charge and Unity line belongs to.
4. Which bucket applied on each day, including the tablet change after the review.
5. Where Snowflake shows $0 for a network-month in which money was spent.
6. Who receives the link, and whether any sharing has to change.

Writes they feed: W1 (register rows + gap list in the Marketing tab) depends on 1–5. W2 (thread reply) and W4 (card comment) carry the per-bucket totals from W1. W3 (mail to the accountant) needs W1's link and the answer to 6. Every write needs the investigation; none is a bolt-on.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents (requirements) | Destination (exact) | Recipient(s) (exact) | Catalog write (reference only; never in the prompt) | Fed by |
|---|---|---|---|---|---|
| W1 register | one row per network, month, title and bucket for Oct 2024 – Sep 2025, using the columns already in the tab; the Snowflake-$0 network-months listed under the table | Marketing tab of f_0cd1e1402e8052d3d4e903 ("Q4 Board Pack - Oct 14", folder d_b563e7f1e1608c4d36f3b0) | readers of the pack (Leonard, Arthur, accountant), no new sharing | gsheets_values_update | §3 Q1–Q5 |
| W2 thread reply | the per-bucket totals | reply in thread C07C2866011/1759176840.271025 | Leonard (thread owner), leonard.hayes@harmonygames.co | slack_send_message (thread_ts) | W1 |
| W3 mail | the sheet link | new mail | the outside accountant, contacts 049f5555b01fd07b0f9d673c (PERSON_6098_EMAIL) | gmail_send_message | W1 + rules doc f_4591ef30be4f920ba1ed14 |
| W4 card comment | the per-bucket totals | comment on trello 68dae1bc8ec7eb683dc15a8d | card members (Leonard, Frederick) | trello_add_comment | W1 |

| Decision-ambiguity risk | Alternative a careful run could take | What pins it |
|---|---|---|
| register destination | the Q3 pack f_9f7fb3ec09a20b2b6aa6da or a new sheet | the hub names "the Marketing tab of the Q4 board pack" (C07C2866011/1759176840.271025) |
| gap-list placement | a separate tab or a mail | the doc says "Under the table" (f_4591ef30be4f920ba1ed14) |
| reply form | a new channel post or a DM | the hub says "as a reply here" (C07C2866011/1759176840.271025) |
| Trello write | a new card, a description edit or moving the card | the hub says "on the true-up card" (68dae1bc8ec7eb683dc15a8d); moving it is not asked |
| link delivery | sharing the sheet, sending to Leonard or investors, or saving a draft | the doc: "Send the sheet link … already on the data room folder as a viewer, so no new sharing. Not to investors." (f_4591ef30be4f920ba1ed14) |
| act vs ask | asking Leonard first | Frederick owns the card (68dae1bc8ec7eb683dc15a8d); the rules exist, so act |
| persona vs agent | the prompt's "I'll …" assigning a write to Frederick | Frederick owns the card (68dae1bc8ec7eb683dc15a8d), so the human's wording must give all four writes to the agent (see §11) |

### 4b · Canonical outcome (one acceptance class)

V3 §9 replaces "one accepted reading" with "every fair reading passes". Each field below is either fixed, or its equivalence class lists the fair readings the rubric must accept.

| Deliverable | Field | Fixed value (pinned, with locator) | Delegated by | Allowed equivalence class | Material / representational |
|---|---|---|---|---|---|
| W1 | destination | Marketing tab, f_0cd1e1402e8052d3d4e903 | — | rows anywhere in that tab under its header | material |
| W1 | row key | network × month × title × bucket (f_4591ef30be4f920ba1ed14 "Rows") | — | same-key rows merged or split; any row order | representational |
| W1 | amounts | per-row net cost per dossier §9.2 (e.g. 2025-09 Unity Ads ZM3D Fundraising 2,730.60 from f_e8f75f70da75c40e9d395e … f_0c302b9a0529823a0c6209) | — | exact cents or rounded dollars; the Dec 31, 2024 5:13 PM PST charge (frederick.stone@harmonygames.co/1820007110310927242) in Dec 2024 or Jan 2025; the tablet back to Real UA from Sep 18 or Sep 19 (no tablet spend on Sep 18, so same totals; 68d195a805df8c30c455f99c); Adjoe Sep 2025 as a $0 row or no row (C07UCC631A6/1757349668.681539) | material (values), representational (rounding) |
| W1 | gap list | 17 network-months: Meta 2025-05 … 2025-09 and Unity Ads 2024-10 … 2025-09 (snowflake.json /tables/0) | — | any list form under the table; months as names or numbers | material (set), representational (form) |
| W1 | columns | existing header Marketing!A1:H1 (f_0cd1e1402e8052d3d4e903) | — | header kept as is | representational |
| W2 | destination | thread reply on C07C2866011/1759176840.271025 | — | also sent to channel is fine | material |
| W2 | contents | Fundraising $3,376.20 and Real UA $95,612.56 net (dossier §9.2, from statements f_e8f75f70da75c40e9d395e … f_0c302b9a0529823a0c6209 and receipts frederick.stone@harmonygames.co/1843154072371887815 … frederick.stone@harmonygames.co/1844734171545827192) | — | rounded figures; spend and credit shown alongside net, provided net is identified; one grand total added | material (values) |
| W2 | wording | — | the prompt leaves the wording open; the hub asks only for "the per-bucket totals" (C07C2866011/1759176840.271025) | any wording | representational |
| W3 | recipient | contacts 049f5555b01fd07b0f9d673c, PERSON_6098_EMAIL | — | cc Frederick or Leonard is fine; no investor recipient | material |
| W3 | contents | link to f_0cd1e1402e8052d3d4e903 | — | the link in any wording; a subject of any wording | material (link), representational (text) |
| W3 | sharing | no permission change (accountant already a viewer on d_b563e7f1e1608c4d36f3b0) | — | no sharing call | material |
| W4 | destination | comment on trello 68dae1bc8ec7eb683dc15a8d | — | one comment | material |
| W4 | contents | the same per-bucket totals as W2, on 68dae1bc8ec7eb683dc15a8d | — | as W2 | material (values) |

Rule for 08/09: two runs reach the same final state when every material field matches within its class. Under V3 §9 one fact
(the bucket totals) is graded in no more than two rows.

## 5 · Discovery map

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 the ask (LB) | window Oct 1 – Sep 30; Snowflake $81,169; four destinations | C07C2866011/1759176840.271025 | YES (#executives member) | met first | none: the persona is @-mentioned | Yes — as "Leonard's paid UA true-up request" (anchor A1). Not the channel id |
| F2 rough rules (superseded) | Unity = top-ups; Adjoe = invoice; AppLovin/Google = Snowflake | frederick.stone@harmonygames.co/1843732571750494737 | YES (own inbox) | met first; overturned by F3 | agent stops at the first rules it finds | No |
| F3 close rules (LB) | scope incl. Calm Play; Meta receipts/credit/duplicates/PT month; Unity statements; ledger for Adjoe/AppLovin/Google; briefs; gap list; accountant | f_4591ef30be4f920ba1ed14 | YES (shared) | overrides F2; amended by F4 | title search "close rules" | No (V3: no "go by the rules in the doc") |
| F4 amendment (LB) | Adjoe in the month the invoice is for | C07C2866011/1759255500.938286 | YES (thread reply) | overrides F3's Adjoe clause | agents rarely read replies | No — never hint at it |
| F5 bucket card (LB) | Fundraising = UK iOS Unity phone + tablet and Meta ZM_UK from Sep 12 | trello 68c99c40e5d9eb6f3a988838 | YES (unscoped) | the DD card 6807be2c1ea290e4382b33be and page_ua_spend_buckets compete | the same query returns the decoy | No |
| F6 tablet change (LB) | tablet back to Real UA from the review day | trello 68d195a805df8c30c455f99c + evt_2f9b60002516e45ff04160 (Sep 18, 10:00 AM PT) | YES | overrides F5 for the tablet | the date is only on the calendar | No |
| F7 Meta receipts (LB) | per-charge amounts, payment method, reference number | frederick.stone@harmonygames.co/1812262106647207041 … frederick.stone@harmonygames.co/1844734171545827192 (57 threads) | YES (own inbox) | "$20/day" C07C2866011/1758313330.170339 and Snowflake compete | 34 base hits include another account's receipts (frederick.stone@harmonygames.co/1810880213558472946) | No |
| F8 briefs (LB) | game per campaign | folder d_6930b716ea5b1457adb4a4 (f_6d0c2209baa3ff54633836 … f_887def6eed0e1b022f7ab0) | YES (owned) | Snowflake campaign keys compete | PvZ naming (trap K02) | No |
| F9 Unity statements (LB) | spend per account per period | folder d_3885933a334aef16e40e84 (f_c34b364c50bf4ed59ae6ce … f_0c302b9a0529823a0c6209) | YES (owned) | top-up mails (frederick.stone@harmonygames.co/1843072786759807900) compete | each statement is its own sheet | No |
| F10 Unity cost missing (LB) | Singular gets installs only | page_singular_cost_connectors → cmt_6b4787a755ac66787e8c (ENG-2362) | YES (unscoped) | Snowflake's $0 | Confluence is not advertised to the agent | No (root cause, never in the prompt) |
| F11 Adjoe credit (LB) | April total $10,733.60 after the $1,271.40 credit | frederick.stone@harmonygames.co/1830999337380347892 | YES (own inbox) | the PDF's $12,005.00 | the base subject redacts Adjoe as [USERNAME_14101] | No |
| F12 Adjoe September (LB) | no cost (the rep's reply) | C07UCC631A6/1757349668.681539 | YES (channel member) | the spike report C07UCC631A6/1757345931.336429 | answer sits in a thread reply | No |
| F13 ledger + warehouse (LB) | Adjoe/AppLovin/Google monthly; game split | snowflake.json /tables/38 (FIN-000499 …), /tables/0 | YES (unscoped) | the "Versioned paid-UA spend mart" snowflake.json /tables/3 | Snowflake is not advertised | No ("Snowflake" as a word is already in the hub) |
| F14 accountant (LB) | PERSON_6098_EMAIL | contacts 049f5555b01fd07b0f9d673c | YES (unscoped) | — | only one accountant contact | Yes, as "our outside accountant": a recipient the sender knows (V3 §8) |
| F15 destinations (LB) | Q4 pack; true-up card | f_0cd1e1402e8052d3d4e903; trello 68dae1bc8ec7eb683dc15a8d | YES | the Q3 pack f_9f7fb3ec09a20b2b6aa6da | "Board Pack" returns both | Yes, as "the Q4 board pack" and "the true-up card"; never the ids |

## 5a · Search-as-persona proof

`persona_view.py search` reads only the base export, so seeded rows return 0 there. Each row therefore has two columns. Base
competition comes from `persona_view.py search` (verbatim below). Seeded reach comes from a scan of the SQL rows containing the same query, with each
row's `check-sql` verdict for frederick_stone (verbatim below). Unscoped services are always YES.

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| F1 | slack | "paid UA number" | base 1 (2023, unrelated); seeded 1 | 0 | C07C2866011/1759176840.271025 | YES (seeded, check-sql YES) |
| F2 | gmail | "data room UA numbers" | base 0; seeded 1 visible | 0 (Leonard/Arthur copies are other mailboxes) | frederick.stone@harmonygames.co/1843732571750494737 | YES (seeded) |
| F3 | gdocs | "close rules" | base 0; seeded 1 | 0 | f_4591ef30be4f920ba1ed14 | YES (seeded) |
| F4 | slack | hub thread replies (reply 2 of 2) | seeded reply row L13 | 0 | C07C2866011/1759255500.938286 | YES (seeded, check-sql YES) |
| F5 | trello | "UA spend buckets" | base 0; seeded 2 cards (H1 + decoy) | 0 | 68c99c40e5d9eb6f3a988838 | YES (unscoped) |
| F6 | trello / gcal | "from the bucket review" / "UA bucket review" | seeded 1 / 2 | 0 | 68d195a805df8c30c455f99c; evt_2f9b60002516e45ff04160 | YES |
| F7 | gmail | "meta ads receipt" | base 34; seeded 20 | 0 | frederick.stone@harmonygames.co/1812262106647207041 | YES |
| F8 | gdrive | "UA test brief" | base 0; seeded 19 | 0 | d_6930b716ea5b1457adb4a4 | YES (seeded) |
| F9 | gsheets | "Unity Ads statement" | base 0; seeded 25 | 0 | f_c34b364c50bf4ed59ae6ce | YES (seeded) |
| F10 | confluence / linear | "Singular cost connectors" / "Singular" | base 5 + 5 (unrelated); seeded 2 / 1 | 0 | page_singular_cost_connectors; cmt_6b4787a755ac66787e8c | YES (unscoped) |
| F11 | gmail | "credit of $1,271.40" (or the Adjoe invoice thread) | seeded 1 visible | 0 | frederick.stone@harmonygames.co/1830999337380347892 | YES |
| F12 | slack | "adjoe" | base 34 visible (9 UNVERIFIED in 2 public containers) | 0 | C07UCC631A6/1757349668.681539 (thread reply; can-see YES) | YES |
| F13 | snowflake | "AD_SPEND_DAILY" | base 5 | 0 | snowflake.json /tables/0 | YES (unscoped) |
| F14 | contacts | "accountant" | base 0; seeded 1 | 0 | 049f5555b01fd07b0f9d673c | YES (unscoped) |
| F15 | gsheets / trello | "Board Pack" / "true-up" | seeded 4 (both packs) / 2 | 0 | f_0cd1e1402e8052d3d4e903; 68dae1bc8ec7eb683dc15a8d | YES (seeded) |

Base searches (verbatim, `python3 Task_Authoring/tools/persona_view.py search frederick_stone <service> "<query>" --limit 5 --no-hidden`, decisive lines):

```
SEARCH slack 'paid UA' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C061D04GU0K/1697829803.028909", "channel": "marketing_partnerships", "kind": "private", "date": "2023-10-20", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "and I don’t mean paid UA on TikTok - that still doesn’t work"}
SEARCH slack 'data room' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=2 (showing 2)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gmail 'data room UA numbers' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gdocs 'close rules' as frederick_stone  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH trello 'UA spend buckets' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gcal 'UA bucket review' as frederick_stone  scope: GCal event summary (base events carry no description/location)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gsheets 'Board Pack' as frederick_stone  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gdrive 'UA test brief' as frederick_stone  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gsheets 'Unity Ads statement' as frederick_stone  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gmail 'meta ads receipt' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=34 (showing 5)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1810880213558472946", "last": "2024-09-22T07:25:49Z", "subject": "Your meta ads receipt (Account ID: [IDENTIFIER_6501])", "snippet": "Your meta ads receipt (Account ID: [IDENTIFIER_6501])"}
  {"id": "frederick.stone@harmonygames.co/1812262106647207041", "last": "2024-10-12T00:29:57Z", "subject": "Your meta ads receipt (Account ID: [IDENTIFIER_3125])", "snippet": "Your meta ads receipt (Account ID: [IDENTIFIER_3125])"}
SEARCH confluence 'Singular' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=5 (showing 5)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH linear 'Singular' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=5 (showing 5)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH contacts 'accountant' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'adjoe' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=34 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=9 in 2 containers
SEARCH snowflake 'AD_SPEND_DAILY' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=5 (showing 5)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

Seeded reach (verbatim, a scan of `task_inputs/01_Universe_Inject.sql` rows containing each query, with the verdict from
`persona_view.py check-sql frederick_stone task_inputs/01_Universe_Inject.sql --json`; script
`/tmp/claude-1000/-home-sumit-Downloads-OC-OC-Task-Authoring-2/96458354-288c-4a9d-bf39-ae4b634fe13c/scratchpad/pw/seedsearch.py`). The L13 row is the
Sep 30 reply. Its key column shows the parent thread id because the reply row carries the parent ts:

```
SEEDED slack 'paid UA number' as frederick_stone: 1 seeded row(s) containing the query
    L9 C07C2866011/1759176840.271025 YES
SEEDED slack 'one change to the doc' as frederick_stone: 1 seeded row(s) containing the query
    L13 C07C2866011/1759176840.271025 YES
SEEDED gmail 'data room UA numbers' as frederick_stone: 3 seeded row(s) containing the query
    L23 frederick.stone@harmonygames.co/1843732571750494737 YES
SEEDED gdocs 'close rules' as frederick_stone: 1 seeded row(s) containing the query
    L189 f_4591ef30be4f920ba1ed14 YES
SEEDED trello 'UA spend buckets' as frederick_stone: 5 seeded row(s) containing the query
    L448 6807be2c1ea290e4382b33be YES (unscoped)
    L452 68c99c40e5d9eb6f3a988838 YES (unscoped)
SEEDED trello 'from the bucket review' as frederick_stone: 1 seeded row(s) containing the query
    L456 68d195a805df8c30c455f99c YES (unscoped)
SEEDED trello 'true-up' as frederick_stone: 2 seeded row(s) containing the query
    L458 68dae1bc8ec7eb683dc15a8d YES (unscoped)
SEEDED gcal 'UA bucket review' as frederick_stone: 2 seeded row(s) containing the query
    L171 evt_2f9b60002516e45ff04160 YES
SEEDED gsheets 'Board Pack' as frederick_stone: 4 seeded row(s) containing the query
    L193 f_0cd1e1402e8052d3d4e903 YES
    L203 f_9f7fb3ec09a20b2b6aa6da YES
SEEDED gdrive 'UA test brief' as frederick_stone: 19 seeded row(s) containing the query
    L183 d_6930b716ea5b1457adb4a4 YES
SEEDED gsheets 'Unity Ads statement' as frederick_stone: 25 seeded row(s) containing the query
    L283 f_c34b364c50bf4ed59ae6ce YES
SEEDED gmail 'meta ads receipt' as frederick_stone: 20 seeded row(s) containing the query
    L31 frederick.stone@harmonygames.co/1842010914816895400 YES
SEEDED gmail 'credit of $1,271.40' as frederick_stone: 2 seeded row(s) containing the query
    L157 frederick.stone@harmonygames.co/1830999337380347892 YES
SEEDED confluence 'Singular cost connectors' as frederick_stone: 2 seeded row(s) containing the query
    L433 page_singular_cost_connectors YES (unscoped)
SEEDED linear 'Unity Ads cost has never come into Singular' as frederick_stone: 1 seeded row(s) containing the query
    L443 cmt_6b4787a755ac66787e8c YES (unscoped)
SEEDED contacts 'accountant' as frederick_stone: 1 seeded row(s) containing the query
    L175 049f5555b01fd07b0f9d673c YES (unscoped)
```

Search-behaviour risks: an agent may stop at the Sep 19 mail (F2) or at the card (F5) without reading the comment. It may skip
the hub's thread replies (F4) or quote Snowflake (Robert's reply). These are the designed difficulty. Each overturning record is one hop from a
record the agent has a reason to open, so V3's reachability rule holds.

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| R1–R7, R12 register rules | f_4591ef30be4f920ba1ed14, C07C2866011/1759255500.938286, 68c99c40e5d9eb6f3a988838 | deliverable: the register Leonard asked for | hub C07C2866011/1759176840.271025 · YES · one hub · it names the rules, buckets and pack, but no number | gotcha → carried by the hub trigger |
| R9 destination | f_0cd1e1402e8052d3d4e903 | destination | hub · YES · Q3 pack is the decoy, hub says Q4 · instructions | named in the prompt (V3: sender knows it) |
| R10 thread reply | C07C2866011/1759176840.271025 | destination | hub · YES · unique thread · instructions | named in the prompt |
| R13 card comment | 68dae1bc8ec7eb683dc15a8d | destination | hub · YES · unique card name · instructions | named in the prompt |
| R11 mail to the accountant | 049f5555b01fd07b0f9d673c via f_4591ef30be4f920ba1ed14 | recipient | doc "When it's done" clause · YES · one accountant contact · instructions | recipient named in the prompt ("our outside accountant"); no sharing step |
| checking the numbers before posting | — | none | — | inferable (competent assistant) |

| Anchor | May be named |
|---|---|
| A1 | Leonard's paid UA true-up request; the data room UA number; the Oct 14 board; the last twelve months |
| destination W1 | the Q4 board pack; the Marketing tab |
| destination W2 | Leonard's thread in #executives |
| destination W4 | the true-up card |
| recipient W3 | our outside accountant |

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| reporting window | Oct 1, 2024 – Sep 30, 2025 | f_4591ef30be4f920ba1ed14; C07C2866011/1759176840.271025 | past |
| Fundraising bucket starts | Sep 12, 2025 | trello 68c99c40e5d9eb6f3a988838 | past |
| bucket review | Thu Sep 18, 2025, 10:00–10:30 AM PT (17:00Z) | evt_2f9b60002516e45ff04160 | past |
| rough rules mail | Fri Sep 19, 2025, 3:20 PM PT (22:20Z) | frederick.stone@harmonygames.co/1843732571750494737 | past |
| close rules doc | Fri Sep 26, 2025, 2:05 PM PT (21:05Z) | f_4591ef30be4f920ba1ed14 | past |
| Leonard's ask | Mon Sep 29, 2025, 1:14 PM PT (20:14Z) | C07C2866011/1759176840.271025 | past |
| amendment reply | Tue Sep 30, 2025, 11:05 AM PT (18:05Z) | C07C2866011/1759255500.938286 | past |
| last seeded charge | Tue Sep 30, 2025, 4:40 PM PT (23:40Z) | frederick.stone@harmonygames.co/1844734171545827192 | past |
| freeze | Tue Sep 30, 2025, 5:00 PM PT = Oct 1, 2025 00:00 UTC (V3 §3) | 00_Assigments.md; `tools/hg_clock.py`; latest record before it frederick.stone@harmonygames.co/1844734171545827192 | the "now" of the prompt |
| zone-dependent charge | Dec 31, 2024, 5:13 PM PST (Jan 1, 2025 01:13 UTC) | frederick.stone@harmonygames.co/1820007110310927242 | past; both months fair |
| board meeting | Tue Oct 14, 2025, 9:00 AM PT (16:00Z) | evt_bd61f3209523d19fdd6ba2 | deadline (future, allowed) |
| Snowflake figure | $81,169 (81,168.77) | C07C2866011/1759176840.271025; snowflake.json /tables/0 | past fact (may be quoted; it is in the hub) |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | yes | yes | rules spread over the doc, card, comment, calendar, briefs (f_4591ef30be4f920ba1ed14; 68c99c40e5d9eb6f3a988838) | the prompt says what to produce and where; it never says where the rules live |
| Dynamic change | yes | yes | Sep 19 mail → doc → Sep 30 reply; card → comment (C07C2866011/1759255500.938286; 68d195a805df8c30c455f99c) | no mention of a correction, a reply or "the latest version" |
| Multi-source | yes | yes | 11 services (§1) | no source named as an exact artifact beyond the §6 destinations |
| Async | no | — | 03_Error_Async_Config.txt says Friction: none | nothing to hide |
| Error recovery | no | — | no friction configured | nothing to announce |
| Access control | no (incidental only) | no | Leonard's mailbox copies are NO but not needed | no ask to read anyone else's mail |

## 9 · Must not appear in the prompt

- **Tool and server names** (`Evals/references/tools/catalog.json`): gsheets_values_update, gsheets_values_get, gsheets_get_spreadsheet,
  slack_send_message, slack_conversations_search_messages, gmail_send_message, gmail_search_messages, trello_add_comment,
  trello_get_comments, gdrive_search, gdrive_list_folder, gdocs_get_document, confluence_search, linear_list_comments,
  contacts_search_contacts, gcal_list_events, snowflake_execute_query; "the X tool"; any MCP server name. Natural product names ("the
  Trello card", "the board pack") are fine.
- **Ids and opaque names**: C07C2866011, C07UCC631A6, any ts, f_/d_ ids, evt_ ids, trello ids, page_ ids, cmt_ ids, ENG-2362,
  FIN- ids, AD_SPEND_DAILY / FINANCE_LEDGER, the account number 3125, PERSON_6098 / PERSON_6098_EMAIL.
- **Hidden authorities and findings**: the close-rules doc and its title, the UA test briefs, the Unity statements and their folder,
  the bucket card's name, the review meeting or its date, Calm Play, the top-ups, the advertising-credit charge, duplicate receipts,
  Adjoe's credit or contested installs, Adjoe September, the connector page, Singular's missing Unity cost, the lost Meta access,
  the Sep 30 amendment, the tablet change, Sep 12.
- **Answers**: any register amount, the bucket totals ($3,376.20 / $95,612.56), the gap list or its count (17), the corrected total.
- **V3 §8 patterns**: "don't trust the Snowflake number" or "the summary", "go by the rules in the doc", "Actually", shutdown
  framing, answer-key clauses ("if receipts and Snowflake differ…"), riddles, trap hints, spec language ("ensure", "governing").
- **Form**: Markdown, numbered steps, a per-deliverable content list, column instructions (the tab already has its header), a
  prescribed reply format, staged typos.
- **No attachment or `/app/artifact` reference** (no reference files).

## 10 · Entity traps

`python3 Task_Authoring/tools/entity.py collisions` and `resolve` (verbatim excerpt; full output in
`/tmp/claude-1000/-home-sumit-Downloads-OC-OC-Task-Authoring-2/96458354-288c-4a9d-bf39-ae4b634fe13c/scratchpad/pw/entity.txt`):

```
SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <marcus@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=143292, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
  trello     id=PERSON_6094_TRELLO_USER_ID, username=leonard.hayes, fullName=Leonard Hayes, last_activity=2025-11-13   [join: exact_name]
  contacts   contact_id=63fffeb4fab5233ed5bb73bf, name=Leonard Hayes, email=leonard.hayes@harmonygames.co, job=Co-founder & CEO, is_user=False   [join: exact_email]
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=129939, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
ENTITY email:simon.walker@harmonygames.co  name=Simon Walker  kind=person  emails=['simon.walker@harmonygames.co']
  persona: simon_walker - Data Analyst (Contractor) / Engineering
  linear     id=usr_eac7fcafa75e4935, email=simon.walker@harmonygames.co, name=simon.walker@harmonygames.co, is_active=True   [join: exact_email]
ENTITY email:frederick.stone@harmonygames.co  name=Frederick Stone  kind=person  emails=['frederick.stone@harmonygames.co']
  persona: frederick_stone - Co-founder / Executive
  contacts   contact_id=175c0d7bc72ed244b944cb90, name=Frederick Stone, email=frederick.stone@harmonygames.co, job=Commercial Lead, Marketing & Business Development, is_user=False   [join: exact_email]
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
|---|---|---|---|
| Leonard Hayes, leonard.hayes@harmonygames.co (CEO in Contacts) | none in scope; his mailbox files are named leonard@harmonygames.co_* | one person | contacts 63fffeb4fab5233ed5bb73bf |
| Robert, robert@harmonygames.co | — | his reply is a decoy, not an authority | C07C2866011/1759178460.557708 |
| the outside accountant, PERSON_6098_EMAIL | no other accountant contact; no name in the base (tokenized) | refer to her by role, never by a name | contacts 049f5555b01fd07b0f9d673c |
| Meta ad account ending 3125 | Meta account [IDENTIFIER_6501] receipts in Frederick's inbox (Sep 2024, outside the window); Leonard's own test account (his mailbox only) | the doc scopes "our ad account ending 3125" | frederick.stone@harmonygames.co/1810880213558472946 vs frederick.stone@harmonygames.co/1812262106647207041 |
| Unity HG account + Calm Play account | Calm Play's 2024 "alpha account" balance | balance, not spend (T22) | frederick.stone@harmonygames.co/1813530307529968502 |
| Adjoe (redacted [USERNAME_14101] in subjects) | — | the vendor's name is tokenized in mail | frederick.stone@harmonygames.co/1830999337380347892 |
| the true-up card | the two "UA spend buckets" cards on the same board | different names and purposes | 68dae1bc8ec7eb683dc15a8d vs 68c99c40e5d9eb6f3a988838 |
| Q4 Board Pack - Oct 14 | Q3 Board Pack - Jul 16 | Q3 has no bucket column | f_0cd1e1402e8052d3d4e903 vs f_9f7fb3ec09a20b2b6aa6da |

Name-swap test: swapping Leonard for any other name breaks the task, because the hub, doc, card and true-up card are his records (C07C2866011/1759176840.271025). The scenario rests on real records.

## 11 · Pre-submit checklist

- [ ] Written entirely by the human, in Frederick's own casual voice. Clean spelling is fine (V3 §8)
- [ ] Reads as something a co-founder would send an assistant; no spec language, no "please ensure"
- [ ] No Markdown, no numbered steps, no list of what each deliverable must contain
- [ ] Names the destinations Frederick knows: the Q4 board pack (Marketing tab), Leonard's thread, the true-up card, our outside accountant
- [ ] Every write is asked of the assistant ("can you …"), with no "I'll post it" beside the same write
- [ ] Says "send" the link (not draft), and asks for no sharing change
- [ ] Nothing from §9: no doc title, no Calm Play, no top-ups, no corrections, no Snowflake-is-wrong hint, no totals, no ids
- [ ] No "Actually", no "don't trust the summary", no "go by the rules in the doc", no shutdown backdrop (V3 §8 batch-repeat list)
- [ ] Nothing after Tue Sep 30, 5:00 PM PT described as done; the Oct 14 board is a deadline
- [ ] Any premise stated is true (e.g. Leonard asked in #executives on Mon Sep 29; the card is his; Robert suggested the Singular number)
- [ ] 20–4,000 words; then run `/create-prompt-writing check`

## 12 · Blockers and routed defects

| Item | Status | Locator |
|---|---|---|
| `/prompt` FAIL (attempt 6ad83eebbd6456fd065bbd20): Cross-Service Coherence 2 for two minor data inconsistencies (brief start dates after billed spend; the connector page vs the ledger's own description) | FIXED in SQL revision v4 (design §13d): nine briefs re-dated and the "Started:" line dropped; the connector page reworded. The prompt text is unchanged | frederick.stone@harmonygames.co/1839693762261954189; page_singular_cost_connectors |
| second `/prompt` FAIL (Cross-Service Coherence 2): the Adjoe contest email cited a "Singular export" with 212 Canada installs that Singular's tables lack; the ledger comment vs month-end rows | email reworded in v5, then v6 after `/injection` rev 7 advisory 1: no Canada claim. Leonard contests 2,401 invoiced vs 1,923 Singular installs, and Adjoe grants a partial $1,271.40 credit. The ledger comment is base metadata and cannot be fixed by SQL, so one minor point remains (expected Non-Fail 3) | frederick.stone@harmonygames.co/1830999337380347892; snowflake.json /tables/38 |
| third `/prompt` FAIL (Cross-Service Coherence 2): a claimed $3,720.06 of Robert-only Meta receipts, plus two brief notes (Android Nordics anachronism; iOS CA "last DD test") and the ledger comment | Robert-only receipts: false positive. All 12 are in Frederick's mailbox with the same reference and transaction IDs (design §13g). The brief notes were fixed in v7. The ledger comment is base metadata | frederick.stone@harmonygames.co/1814042565503776727; f_f017eafb1e59601f888460; f_9e4be4822ec79ce7ff5d17 |
| `/injection` advisories 1–3 (Unity top-up notices beside base receipts; Unity sender token; SES Message-ID timestamp) | FIXED in v4: the top-ups are Leonard's forwards of six base receipts; the Message-ID encodes May 7, 2025 | leonard.hayes@harmonygames.co/1843071417603742140; frederick.stone@harmonygames.co/1843072786759807900 |
| honest call minimum 104 vs V3 floor 100 | measured at the Opus pre-check | 01_Scenario_Design.md §9 |
| facts UNVERIFIED | none | — |

## 13 · Self-review

**Eval walk (`Evals/1_Prompt_Eval.md`).** Phase 1: persona (§1.1) is Frederick, the UA owner, in his own voice (§1). Naturalness
(§1.2) is the human's job; §11 lists the V3 patterns to avoid. Anti-patterns (§1.3): no command list, no bolt-ons (W2–W4 feed
from W1), no pre-solving (§9), no tool names (§9). Diversity (§1.4): four writes in four services. Assignment and complexity
(§1.5): Finance, analysis and synthesis, with Ambiguity, Dynamic change and Multi-source all load-bearing (§8). Phase 2: UGT (§2.1)
has one acceptance class per deliverable (§4b, V3 fair readings). Feasibility (§2.2): every write is in the catalog and every
read is persona-YES (§5a). Truthfulness (§2.3): the facts the prompt may state are in §7/§10. Cross-service (§2.4): 11 services.
Investigation → action (§2.5) is in §3. Clarity (§2.6) is in §4. Contrived (§2.7) is in §9/§11. Today's date (§2.8) is in §7. Originality (§2.9): no
supplied sample. The billing-close scenario differs from the shutdown and launch tasks. Phase 3: universe feasibility rests on the
`/injection` PASS for SQL sha256 ba7ef7d929bb; v4 (ba1685a9ca34) passed `/injection` rev 5; v5 (23b214b0e670) passed `/injection` rev 7; v6 (137eefbd043c) passed `/injection` rev 9; v7 (c983da3d0a7d) fixes two brief notes and needs a fresh `/injection` run.

**Counter-readings.**

| Area | Counter-reading | Resolution (evidence) |
|---|---|---|
| UGT | Reading B: "per-bucket totals" means gross spend, so Fundraising is $3,546.83 (816.23 + 2,730.60), not the $3,485.20 net. That would be a second final state | The doc says "A charge paid with advertising credit cost us nothing" (f_4591ef30be4f920ba1ed14), so net is the paid number. §4b accepts spend shown beside net when net is identified, and the rubric must accept that reading too (V3 §9) |
| UGT | Reading B: the tablet goes back to Real UA on Sep 22, the date of the comment | "from the day of the review" (68d195a805df8c30c455f99c) plus evt_2f9b60002516e45ff04160 gives Sep 18. Sep 18 and Sep 19 give the same totals (no tablet spend Sep 18, f_76007a5c131f92019df2a0), so one class |
| UGT | Reading B: Adjoe in the wire month (the doc's clause) | the newer Sep 30 reply amends only that clause (C07C2866011/1759255500.938286). A newer source with the same scope settles it (Eval 1 §2.1 step 2) |
| Clarity | if the human writes "I'll send it to the accountant", the agent may skip W3 | §11 box: every write is asked of the assistant; check mode C7 tests it on the real text |
| Clarity | "drop the totals on the card" could mean editing the card description | the hub says "on the true-up card when you're done" (C07C2866011/1759176840.271025). A comment or a description edit holds the same material content; 09 must accept either if the prompt leaves it open |
| Incorporation | the prompt points to Leonard's request, which incorporates the doc. Does the doc hand over the answer? | the doc states principles only, with no amount, total or gap month (`fact_check --no-leak` PASS, dossier §8). Each delegation quote is verbatim (manifest `delegation_quote`) |
| Incorporation | the accountant mail is a doc-only requirement, and an untriggered requirement is unauthorized | §6: the prompt names "our outside accountant" as a recipient Frederick knows, and the doc's "When it's done" clause (f_4591ef30be4f920ba1ed14) supplies the action |
| Truthfulness | a premise like "Leonard emailed me" would be false | the ask is a Slack message (C07C2866011/1759176840.271025). The Sep 19 mail is the older rough rules. §11 lists the true premises |
| Feasibility / ACL | can Frederick edit the Q4 pack and comment on the card? | Leonard shares f_0cd1e1402e8052d3d4e903 with Frederick (check-sql YES, SQL L193). Trello writes are unscoped (catalog trello_add_comment). Writes are never ACL-governed |
| Feasibility / ACL | the deciding Adjoe Sep fact sits in a thread reply in a channel the persona might not be in | can-see YES: Frederick is in the members of adjoe-[SOURCE_ORG_0001] (C07UCC631A6/1757349668.681539) |
| Contrived | naming four destinations and a recipient could read as a spec sheet | V3 §8 asks that destinations the sender knows be named. One sentence naming them is the screen-24 skeleton, not a content list (Eval 1 §2.7). The contents stay in records |
| Contrived | quoting "$81,169" might read as a planted hint | the figure is Leonard's own message (C07C2866011/1759176840.271025). Quoting it is optional. A hint would be calling it wrong, and that is on the §9 list |

**Re-verified this run:** hub, amendment, Robert and card texts from `support/task_work/fs_ua_trueup/texts.py` and SQL L9/L11/L13/L452–L460.
Persona reach from `check-sql --json` and `can-see` (C07UCC631A6/1757349668.681539 YES, frederick.stone@harmonygames.co/1830999337380347892
YES, evt_bd61f3209523d19fdd6ba2 YES, leonard.hayes@harmonygames.co/1838649409811811442 NO). Board time 2025-10-14T16:00:00Z from
the gcal export. Write names from `Evals/references/tools/catalog.json`.

Unresolved: SQL revision v7 (sha256 c983da3d0a7d) needs fresh `/injection` and `/prompt` runs. The FINANCE_LEDGER table comment (base Snowflake metadata, snowflake.json /tables/38) cannot be overlaid by SQL, so one minor coherence point remains. The 104-call margin is measured at the pre-check.

```
STAGE GATE prompt-writing: PASS — Task_Authoring-2/task_inputs · 04_Prompt_Writing_Brief.md#ae315a9c5927 · blocking 0 · warnings 0 · checks 21
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#c983da3d0a7d, 01_Hardness_Manifest.json#8b6e3c18def2, 01_Grounding_Dossier.md#84d01f840c36)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#7c92b9c20d3c)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 3/3 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 24/24 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 15/15 items carry a source pointer (min 100%)
[PASS] evidence.dates: 12/12 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 8/8 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 15 facts proven findable by persona_view search as frederick_stone
[PASS] reach.brief: 22 scoped load-bearing ids YES for frederick_stone
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.canonical_outcome: canonical outcome table: 13 field(s), each fixed or delegated
[PASS] boundary.anchor_naming: 5 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 12 evidenced counter-readings (of 12 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```




