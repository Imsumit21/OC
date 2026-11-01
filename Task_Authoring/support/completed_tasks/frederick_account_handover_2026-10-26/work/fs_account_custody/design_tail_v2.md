## 2 Cohort spine

**Rule (H1 rule 1).** Every marketing, UA, ad-monetization and social account in today's sweep folder ({SWEEP}) that has Frederick on
it in any role; store accounts and data tools are on the engineering card; MAX-only bidders are not separate accounts; accounts deleted
or deactivated before the sweep are off. The folder holds 16 exports; 13 are in scope.

**Per-account truth** (planned export content; money evidence is base unless marked seed):

| # | Account (export) | Company holders | Class | Money moving (Sep 2025) | Action | Evidence |
|---|---|---|---|---|---|---|
| 1 | Meta ad account "Harmony Games" ({SW_meta}) | Frederick (Admin) — Leonard is Advertiser; Partners tab: Node Media LLC, partner admin | OUTSIDE ACCESS | Y (receipt Sep 16; FB campaign off Sep 26) | REVOKE | frederick.stone@harmonygames.co/1843428112007517388; D05S58U4SAK/1758922541.613439 |
| 2 | Google Ads 569-350-5790 Harmony Games, Inc. ({SW_gads_569}) | Frederick, Leonard (Admin); Linked managers tab: Node MCC unlinked 2024-12-20 | COMPANY-HELD | N (0 enabled campaigns; UAC last spend 2025-04-10) | KEEP (Arthur's email) | frederick.stone@harmonygames.co/1835153849970828373; {GAMEND} |
| 3 | Google Ads 449-481-1590 Calm Play LLC ({SW_gads_449}) | Frederick (Admin) — Leonard Standard; Node MCC unlinked 2024-12-20 | SINGLE | N | CLOSE | frederick.stone@harmonygames.co/1838369017520543217 |
| 4 | Unity Ads org Calm Play LLC ({SW_unity_ads}) | Frederick (Owner) — Leonard Manager; Invites tab: Arthur, Owner, pending | SINGLE | Y (iOS campaigns on Sep 29–30) | TRANSFER | C07C2866011/1759186080.203099; /1759264050.305069 |
| 5 | AppLovin ({SW_applovin}) | Leonard, Frederick (Admin) | COMPANY-HELD | Y (payout Sep 14; paid revenue Sep) | KEEP | frederick.stone@harmonygames.co/1843223812315546201 |
| 6 | adjoe advertiser dashboard ({SW_adjoe}) | Frederick, Leonard (Admin) | COMPANY-HELD | N (Sep installs waived in writing; paused Sep 8) | CLOSE | C07UCC631A6/1757349668.681539; /1757347560.891949 |
| 7 | AdMob (Leonard's active account) ({SW_admob}) | Leonard, Frederick (Admin) | COMPANY-HELD | Y (AD_REVENUE admob Sep rows paid) | KEEP | snowflake.json /tables/35; D05S58U4SAK/1756147086.813789 |
| 8 | TikTok @harmonygames profile ({SW_tiktok}) | Frederick (Admin, frederick.stone@ login) — Leonard uses Fred's login; Sep 29 account deleted | SINGLE | N | TRANSFER (social) | D05S58U4SAK/1759170013.491159; /1759155793.573669 |
| 9 | YouTube channel ({SW_youtube}) | Frederick (Owner) — Leonard Manager; Removed tab: Node 2024-12-20 | SINGLE | N | TRANSFER (social) | D05S58U4SAK/1759096868.688389; C08MCEP1B9B/1732203251.229079 |
| 10 | LinkedIn page ({SW_linkedin}) | Leonard, Frederick (Super admin) | COMPANY-HELD | N | KEEP (social) | C07KRTX5SCE/1726169948.231349 |
| 11 | X account ({SW_x}) | Frederick (Owner) | SINGLE | N | TRANSFER (social) | seed export only |
| 12 | Instagram ({SW_instagram}) | none — owner login is Frederick's personal Gmail address | SINGLE | N | TRANSFER (social) | seed export only |
| 13 | Discord server ({SW_discord}) | Leonard (Owner), Frederick, Robert (Admin), all harmonygames.co logins | COMPANY-HELD | N | KEEP (social) | C07C2866011/1734154451.509769 |
| — | Play Console ({SW_play_console}), App Store Connect ({SW_app_store_connect}), Singular ({SW_singular}) | — | out of scope (engineering card) | — | — | H1 rule 1 |

Totals the deliverables carry: REVOKE 1 · TRANSFER 5 (Unity, TikTok, YouTube, X, Instagram) · KEEP 5 · CLOSE 2; social transfers for
the handles card 4 (TikTok, YouTube, X, Instagram).

**Surfaces and shortcut audit.**

| Surface | Per-record call | Bulk call that does not cover it | Requirement · decides |
|---|---|---|---|
| per-platform export ({SW_meta} … 13 in scope; second tab on 5) | `gsheets_values_get` / `gsheets_get_spreadsheet` × 18 | `gsheets_values_batch_get` reads one spreadsheet; `gdrive_list_files` returns names only; a first-tab read misses the second tab | R2 · company holders |
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
| H1 | Arthur's account handover rules ("arthur's handover rules are on the ops board", D05S58U4SAK/{HUB_TS}) | trello {H1} + comment {CMT}; reply {GAMEND} | R1, R2, R3, R5, R8 | same-board engineering card {ENG}; Confluence {CONF} | {ENG}: team scope (engineering, store, data-tool accounts); {CONF}: older version (T2 version_records) | a Trello search "handover rules" returns both cards (same title stem); proven at injection with `hg.py search search trello "handover rules"` |
| H2 | Leonard's definition of money moving for the cuts (card rule 5: "Money moving is whatever Leonard defined it as for the cuts", trello:{H1}) | gdocs {DOC} section "Money still moving (for the cuts)" | R4 | #executives remark C07C2866011/{DECOY90_TS} (seed, Sep 15, "for the cuts list") | older version by the same author (T3 version_records) | a search for "for the cuts" or "money moving" returns both; the doc is newer |

`governs` lists do not overlap. The hub names only H1; H2, the comment and the email are reached from the card (its rule 5, its
comment thread, and Gmail replies carrying the card's title as subject).

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Leonard's account handover ask | slack D05S58U4SAK/{HUB_TS} |

**Hub** = A1 (Leonard's voice) delegating to H1, the sweep and the destination folder.

**Incorporation table** (quotes are exact substrings of `planned_text.json`; the gate re-reads them from the SQL at injection):

| Fragment | Service · container | Kind | Chain | delegated_by_record | delegation_quote | Requirements | Names |
|---|---|---|---|---|---|---|---|
| K1 | slack · D05S58U4SAK/{HUB_TS} | delegation | A1 | D05S58U4SAK/{HUB_TS} | "reply here with how many you've marked TRANSFER and anything an outsider still has access to" | R6 | H1 |
| K2 | trello · {H1} | requirement | A1 | D05S58U4SAK/{HUB_TS} | "arthur's handover rules are on the ops board, they decide the action" | R1 R2 R3 R5 | H2 |
| K3 | trello · {CMT} | amendment | A1→K2 | trello:{H1} | "For Fred's accounts before the cuts." (the comment sits on this card) | R5 | — |
| K4 | gmail · {GAMEND} | amendment | A1→K2 | trello:{H1} | "For Fred's accounts before the cuts." (Arthur's reply on the card's subject) | R5 | — |
| K5 | gdocs · {DOC} | requirement | A1→K2 | trello:{H1} | "Money moving is whatever Leonard defined it as for the cuts" | R4 | — |
| K6 | gdrive · {SWEEP} | requirement | A1 | D05S58U4SAK/{HUB_TS} | "arthur's sweep from today is the list" | R1 R2 | — |
| K7 | gdrive · {OPS} | destination | A1 | D05S58U4SAK/{HUB_TS} | "save the register in the Company Ops folder" | R7 | — |
| K8 | trello · 67cf1b506d78ad3c72e02a35 | destination | A1→K2 | trello:{H1} | "Socials that need a transfer go as a checklist on Fred's" | R8 | — |

**Amendments.** K3 (Trello comment, 2025-09-30T21:58:44Z) changes rule 5 for socials only; K4 (Gmail reply, 2025-09-30T23:21:09Z,
subject "Re: Account handover rules - marketing, UA & socials") changes rule 5 for one named Google Ads account; both say the rest
stands. Neither is announced by the hub or the card (later applicable updates supersede without announcement, `Evals/WORKFLOW.md`
`prompt-incorporation-v1`); K4 is from the rules' author on the rules' own subject, addressed to Frederick and Leonard.

**Non-authoritative instruction distractors.** The #executives 90-day remark (seed, C07C2866011/{DECOY90_TS}) is Leonard's earlier view,
superseded by his own doc; the engineering card's "One Owner is fine … mark each one KEEP or MOVE" governs another team's list; Arthur's
#executives summary (C07C2866011/{ARTHUR_SUM_TS}) is a claim, not a rule.

## 5 Chains and trap register

**Chains** (manifest `chains`): C1 A1 (Arthur's summary → Unity export with the pending invite on its Invites tab → card rule 2 → Unity
TRANSFER); C2 A9 (Adjoe accidental campaign → rep's waiver reply → H2 waiver clause → Adjoe CLOSE); C3 A13 (card rule 5 CLOSE → Arthur's
email reply → the 569 export → 569 KEEP, 449 CLOSE); C4 A17 (March sheet → sweep folder → card scope → the 13 accounts); C5 A19 (card
rule 5 → doc revenue clause → AD_REVENUE admob paid Sep → AdMob KEEP).

| Trap | Family | Records | Requirement | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T1 | superseding | D05S58U4SAK/{CLAIM_TS} → {SW_unity_ads}, {SW_meta}, {SW_gads_449} | R2 | Leonard counted as admin on Meta, Calm Play Google Ads, Unity | newer exports (Sep 30) | claim sits above the hub in the DM |
| T2 | superseding (4 versions) | {CONF} → {H1} → {CMT} → {GAMEND} | R5 | 2024 page or card alone applied | card replaces page; comment; email | Confluence search returns the page first; comment and email are unannounced |
| T3 | superseding | C07C2866011/{DECOY90_TS} → {DOC} | R4 | 90-day paid rule keeps Adjoe | newer definition by the same author | a Slack search for "for the cuts" hits the remark first |
| T4 | distractor · partial_listing | {MARCH} | R1 | register built from the March sheet | hub: the sweep from today is the list | the March sheet is Frederick's own and titled "logins" |
| T5 | distractor · scope_adjacent | {ENG} | R3 | one-owner-is-fine rule applied | engineering scope | same Trello search |
| T6 | exact_predicate | {SW_unity_ads}, {SW_youtube}, {SW_tiktok}, {SW_instagram}; D05S58U4SAK/1759096868.688389 | R3 | manager / pending / shared / personal counted | card rules 2–3 | — |
| T7 | eliminating_evidence | C07UCC631A6/1757346020.196019 → /1757349668.681539 | R4 | Adjoe money moving | waiver in the reply | parent visible, reply not |
| T8 | entity_collision | {SW_gads_569}, {SW_gads_449}; frederick.stone@harmonygames.co/1838369017520543217 | R5 | one Google Ads, or the wrong one kept | customer IDs in the email and exports | the March sheet says "Google Ads" |
| T9 | tool_surface | {SW_meta} (Partners tab); trello:670010236b89198587ca45b6 | R3 | Meta SINGLE → TRANSFER | Partners tab lists Node Media LLC | a first-tab read shows People only |
| T10 | scope_alias | {SW_play_console}, {SW_app_store_connect}, {SW_singular}; frederick.stone@harmonygames.co/1837038650805365569 | R1 | stores / Singular / ironSource added | card rule 1 | exports sit in the same folder |
| T11 | reuse_exclusion | trello:67cf1b506d78ad3c72e02a35 | R8 | new card for socials | card rule 7 | — |
| T12 | distractor · keyword_collision | C08H78VJG80/1759174925.309129; frederick.stone@harmonygames.co/1840501641217286806 | R1 | PlayableX / Balancy listed as accounts | no export in the sweep | vendor threads are recent |
| T13 | distractor · stale_summary | C07C2866011/1759110509.707539 → D05S58U4SAK/1759170013.491159 | R1 | TikTok dropped ("doesn't exist anymore") | same-day recovery + export | #executives message first |
| T14 | stale_summary | C07C2866011/{ARTHUR_SUM_TS}; {SW_unity_ads}, {SW_x}, {SW_instagram}, {SW_meta} | R3 | only YouTube and TikTok SINGLE | exports under rules 2–4 | the summary is the newest #executives message about the sweep |
| T15 | entity_collision | {SW_admob}; frederick.stone@harmonygames.co/1841349862518331350; D05S58U4SAK/1756147086.813789 | R1 | AdMob dropped as deactivated | the deactivated pub id is a different account | the deactivation mail is the top AdMob search hit |

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
| W2 register in Company Ops ({OPS}) | `gdrive_move_file` | K7 | R7 |
| W3 DM reply to Leonard (D05S58U4SAK): 5 marked TRANSFER, Node Media still has partner admin on Meta | `slack_send_message` | K1, C1, T6, T9 | R6 |
| W4 checklist on 67cf1b506d78ad3c72e02a35 with TikTok, YouTube, X, Instagram | `trello_create_checklist` + `trello_create_check_item` | K3, K8, T6, T11 | R8 |

Reuse-vs-create (A8): W4 reuses the existing handles card. Frederick can edit: Trello writes are unscoped; the Company Ops folder is
shared with him as writer (record plan); the DM is his.

## 8 Service role map

| Service | Role | Load-bearing fact / write | Carrier |
|---|---|---|---|
| slack | hub, claims, Adjoe waiver reply, campaign state; W3 | D05S58U4SAK/{HUB_TS}; C07UCC631A6/1757349668.681539 | ● |
| trello | H1 + comment, decoy, handles card; W4 | {H1}; {CMT}; 67cf1b506d78ad3c72e02a35 | ● (description, comment) |
| gmail | Google Ads amendment; money evidence | {GAMEND}; frederick.stone@harmonygames.co/1843223812315546201 | ● |
| gsheets | 16 exports; March sheet; W1 | {SW_meta} | ● |
| gdocs | H2 | {DOC} | ● |
| gdrive | sweep folder; destination; W2 | {SWEEP}; {OPS} | ● (metadata, folder path) |
| snowflake | AdMob paid revenue | snowflake.json /tables/35 | ● (rows) |
| confluence | superseded rules page | {CONF} | ● (body) |
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
| Dormant socials | TRANSFER/KEEP by class | CLOSE (no money) | card comment {CMT} (newer, same author) |
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
`trello_create_checklist`, `trello_create_check_item`. Frederick must be a writer on {OPS} (record plan). Values are categorical.

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
| 1 | slack.slack_messages | D05S58U4SAK/{CLAIM_TS} | 2025-09-29T23:05:41Z | Leonard | claim (planned_text S_CLAIM) |
| 2 | slack.slack_messages | D05S58U4SAK/{HUB_TS} | 2025-09-30T22:40:12Z | Leonard | hub (S_HUB) |
| 3 | slack.slack_messages | C07C2866011/{DECOY90_TS} | 2025-09-15T19:02:33Z | Leonard | 90-day remark (S_DECOY90), top level |
| 4 | slack.slack_messages | C07C2866011/{ARTHUR_SUM_TS} | 2025-09-30T21:10:27Z | Arthur | summary (S_ARTHUR_SUM), top level |
| 5–6 | trello.trello_cards + createCard action | {H1} / {H1C} | 2025-09-30T20:41:16Z | Arthur | board 640643a3fd8f3ca308d9318e list To Do; name H1_TITLE, desc H1_DESC; badges.comments 1; dateLastActivity = comment time |
| 7–8 | trello.trello_cards + createCard action | {ENG} / {ENGC} | 2025-09-30T20:52:03Z | Arthur | ENG_TITLE, ENG_DESC |
| 9 | trello.trello_actions commentCard | {CMT} | 2025-09-30T21:58:44Z | Arthur | H1_CMT on {H1} |
| 10–13 | gmail threads + messages | {GAMEND} (+ copies in leonard.hayes@ and arthur.blake@ mailboxes) | 2025-09-30T23:21:09Z | Arthur → Frederick, cc Leonard | G_AMEND_SUBJECT / BODY |
| 14 | gdrive.drive_files (folder) | {SWEEP} "Admin sweep - Sep 30" | 2025-09-30T19:50:00Z | Arthur | shared Leonard (writer), Frederick (reader) |
| 15–50 | gdrive + gsheets (16 spreadsheets; 21 sheet tabs) | {SW_meta} … {SW_singular}, {SW_admob} | 2025-09-30T19:52–20:31Z | Arthur | one export per platform with each holder's login address; second tabs: Meta "Partners" (Node Media LLC, partner admin), Google Ads 569/449 "Linked managers" (Node MCC unlinked 2024-12-20), YouTube "Removed users" (Node removed 2024-12-20 by Frederick), Unity "Invites" (Arthur Blake, Owner, pending since 2025-09-30); Google Ads tabs say "enabled campaigns: 0"; TikTok lists the Sep 29 account as deleted; Instagram owner login is Frederick's personal Gmail |
| 51–53 | gdrive + gsheets | {MARCH} "Marketing & UA logins" | 2025-03-10T17:40:00Z | Frederick | lists Meta, Google Ads, Unity Ads, AppLovin, Adjoe, AdMob (old pub id), Singular, TikTok, YouTube, LinkedIn, PlayableX |
| 54–55 | gdrive + gdocs | {DOC} "Runway & shutdown cash notes" | created 2025-09-25T16:12Z, modified 2025-09-30T17:48Z | Leonard | shared Frederick (reader); section DOC_CASH_MONEY among other notes |
| 56 | gdrive.drive_files (folder) | {OPS} "Company Ops" | 2025-09-30T22:31:00Z | Leonard | shared Frederick and Arthur as writers |
| 57–58 | confluence pages + page_versions | {CONF} | 2024-03-12T16:20:00Z | Leonard (user_EMPLOYEE_0038) | parent page_company_home, space_COMPANY, version 1 |

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

{GATE}

`persona_view.py can-see` for the base records in the reach table (verbatim first lines):

{CANSEE}

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
| 3 | temporal (chronology) | PASS | v1's card (Sep 29) cited "my Sep 30 sweep folder" before it existed (review finding 2) | v2 card at 2025-09-30T20:41:16Z after the last export (20:31Z); text says "today's sweep folder" ({H1}) |
| 4 | semantic | PASS | "Google Ads" names two accounts and the email could be read as the Calm Play one | email names "Harmony Games, Inc." and 569-350-5790; base ties 569 to "[SOURCE_ORG_0001], Inc." (frederick.stone@harmonygames.co/1835153849970828373) and 449 to Calmplay (/1838369017520543217) |
| 5 | semantic (TikTok) | PASS | a "Business Center" export could be read as an ads account outside the socials exemption (review finding 5) | v2 export is the @harmonygames profile (D05S58U4SAK/1759170013.491159); the Sep 29 account is marked deleted (/1759155793.573669) |
| 6 | cross-service referential | PASS | the hub names "arthur's sweep from today" and "the Company Ops folder"; a dropped seed dangles | both planned and dated before the hub ({SWEEP} 19:50Z, {OPS} 22:31Z); injection gate checks seeded ids |
| 7 | cross-service referential (Node) | PASS | Node had YouTube invites and an MCC request, never revoked in base (review finding 3) | v2 exports record Node removed/unlinked 2024-12-20 on YouTube and both Google Ads (C08MCEP1B9B/1732203251.229079, /1727063903.359939); only Meta keeps the partner |
| 8 | quantitative | PASS | Snowflake shows Unity September spend $0, so money moving could be N and Unity CLOSE | H2 counts a switched-on campaign; Unity iOS campaigns on (C07C2866011/1759186080.203099, /1759264050.305069); hazard Q08 excluded |
| 9 | quantitative (AdMob) | PASS | AdMob revenue is small ($38.70) and could be "accrued, not paid" | AD_REVENUE rows for admob Sep 2025 are `paid` (snowflake.json /tables/35); doc counts ad revenue paid to us |
| 10 | state/lifecycle | PASS | Adjoe's June invoice reminder (Aug 4) suggests an unpaid bill | paid in August (C04UEQVDVB7/1755117283.864129); no rule uses unpaid bills |
| 11 | state/lifecycle (AdMob) | PASS | AdMob "has been deactivated" (frederick.stone@harmonygames.co/1841349862518331350) | that is pub-2341961509332343; Leonard's account is active (D05S58U4SAK/1756147086.813789) |
| 12 | identifier/format | PASS | seeded Trello ids could break the timestamp scheme (I16/T06) | minted from their own timestamps (`mint_ids.py`): {H1} → 2025-09-30T20:41:16Z |
| 13 | identifier/format (holders) | PASS | Discord/LinkedIn admins are personal profiles, so rule 3 gives zero company holders (review finding 4) | v2 exports list each holder's harmonygames.co login; rule 3 says "a person's harmonygames.co address" (planned_text H1_DESC) |
| 14 | other (persona plausibility) | PASS | a custody register might look like Arthur's job, not Frederick's | the hub delegates it to Frederick and the accounts are his (D05S58U4SAK/1759096868.688389; C07C2866011/1759186080.203099) |
| 15 | other (wrong summaries) | PASS | the rules' author contradicting his own exports could read as an inconsistency | Arthur's summary is a dated human claim (C07C2866011/{ARTHUR_SUM_TS}); it overcounts pending invites and managers, which the exports show; Atlas rule 12 human-claim-vs-record |
| DP1 | two-reading: ironSource | PASS | a careful run adds ironSource from the Jul 8 welcome mail | card rule 1 MAX-bidder clause (frederick.stone@harmonygames.co/1837038650805365569) |
| DP2 | two-reading: stores/Singular | PASS | they are in the sweep with Fred on them | card rule 1 names them on the engineering card ({ENG}) |
| DP3 | two-reading: AdMob in | PASS | it was deactivated | different pub id; active account in the sweep (D05S58U4SAK/1756147086.813789) |
| DP4 | two-reading: TikTok second account | PASS | the Sep 29 account is a second TikTok | deleted per the export; D05S58U4SAK/1759155793.573669 |
| DP5 | two-reading: Unity | PASS | Arthur Owner → COMPANY-HELD → KEEP | Invites tab: pending ({SW_unity_ads}); card rule 2 |
| DP6 | two-reading: Meta | PASS | Fred is the only company admin → TRANSFER | Partners tab ({SW_meta}); rule 5 order |
| DP7 | two-reading: transfer count | PASS | 6 if Meta counts (review finding 6) | hub asks "how many you've marked TRANSFER" (D05S58U4SAK/{HUB_TS}) |
| DP8 | two-reading: Adjoe | PASS | ran in September → money Y | waiver reply C07UCC631A6/1757349668.681539 |
| DP9 | two-reading: AdMob money | PASS | no AdMob mail in September → N | AD_REVENUE admob Sep paid (snowflake.json /tables/35) |
| DP10 | two-reading: 569 | PASS | no money → CLOSE | Arthur's reply {GAMEND} is newer and names it |
| DP11 | two-reading: dormant socials | PASS | no money → CLOSE | comment {CMT} |
| DP12 | two-reading: Instagram | PASS | non-company address → OUTSIDE | card rule 3 (planned_text H1_DESC) |
| DP13 | two-reading: YouTube outside access | PASS | Node got YouTube invites in 2024 | Removed users tab ({SW_youtube}); C08MCEP1B9B/1732203251.229079 |
| DP14 | two-reading: destination | PASS | the sweep folder is Arthur's place for this | hub quote names Company Ops (D05S58U4SAK/{HUB_TS}) |
| DP15 | two-reading: reply | PASS | a new top-level message vs a thread reply | both in D05S58U4SAK accepted (grading devices) |
| DP16 | two-reading: socials write | PASS | a new card is cleaner | card rule 7 (trello:67cf1b506d78ad3c72e02a35) |

HARDNESS GATE output: pasted above (normal, design PASS).

Unresolved: (1) the honest necessary budget is 61 calls against the author's 70+ target; the measured count comes from the Opus
pre-check, and hardening adds records if it falls short. (2) The review predicted 80–90% for v1; v2 removes the hub pointers to the
money definition, the March sheet and the amendments, adds Arthur's wrong summary, second tabs and a Snowflake-only fact — the
predicted average is not verified until the pre-check. (3) Findability searches for the seeded H1/H2 records are proven at injection.

## 13 Red team (dual)

{REDTEAM}
