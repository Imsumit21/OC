# Scenario Design — fs-account-custody · design only · contains no prompt, OE or criterion text

Persona Frederick Stone (Co-founder, Executive) · competency Corporate Ops · task skill Analysis and synthesis · horizon Normal
(platform "Task Type": normal) · difficulty mode medium (V3 cap: six-rollout average strictly under 85%; the author's own target is
under 75%, design target about 65%) · universe date October 1, 2025 (V3 freeze 00:00 UTC = Tue Sep 30, 2025 5:00 PM PT).
Builder scripts: `support/task_work/fs_account_custody/` (`mint_ids.py` mints every id into `minted_ids.json`, `planned_text.json`
holds the seeded wording the delegation quotes come from, `build_manifest.py` writes the draft manifest).

## 0 Assignment, persona census and horizon note

| Field | Assigned (verbatim, `00_Assigments.md`) | Resolution |
|---|---|---|
| persona | Frederick Stone | roster `frederick_stone`, frederick.stone@harmonygames.co, Executive (`Evals/references/persona/roster.json`) |
| role | Co-founder | runs the UA, ad-network and social accounts (`references/Persona_Briefs.md` §Frederick); YouTube owner per D05S58U4SAK/1759096868.688389 |
| business function | Executive | Evals category Founders / Exec / Strategy (`Evals/references/rules/task_categories.md`) |
| competency | Corporate Ops | company account custody and offboarding readiness before the planned cuts (C07C2866011/1758739409.488879) |
| task skill | Analysis and synthesis | 12 accounts × user exports, money evidence and two rule sources with two amendments, reconciled into one register |
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
range is allowed"), and an average weighted pass rate under 75%. The honest necessary budget is 63 calls (§9); Opus runs on a
normal task with this many sources typically add 15–40 exploratory calls, so 70+ is the expected range, measured at the pre-check.
The human-time estimate must still fit Normal (under about 8 hours).

Persona reach census (`python3 Task_Authoring/tools/persona_view.py reach frederick_stone --top 10`, verbatim):

{REACH}

Linear / GitHub / Trello identities: Trello member `4b4a68fc0fec0b254e4f9d8e` (Frederick), `2162c1ba310341bf318f48b7` (Arthur),
`PERSON_6094_TRELLO_USER_ID` (Leonard); Confluence `user_EMPLOYEE_0038` (Leonard), `user_EMPLOYEE_0025` (Arthur). No Linear or GitHub
record is used.

## 1 Storyline

**Arc.** After the Sep 28–29 TikTok/YouTube lockout, Arthur posts handover rules for Frederick's accounts on Leonard's founder board
(Trello "Harmony Games", 640643a3fd8f3ca308d9318e) on Sep 29, sweeps every platform's user list into one Drive folder on Sep 30, and
amends the rules twice (card comment, then email). Leonard writes the money definition into his cash notes doc and, at 3:40 PM PT on
Sep 30, asks Frederick in their DM for the register: one row per account with who holds it, whether money is moving, and the action;
saved in the Company Ops folder, with a reply giving the transfer count and any outside access.

**Timeline placement** (`references/universe_kb/timeline.md`, clock 2025-10-01): the bridge outreach that begins 2025-09-03
(`gmail:leonard@harmonygames.co_1842219327413774622.json`) and the A16Z Speedrun rejection dated 2025-10-01
(`slack:C07C2866011:1759288987.503349`, after the freeze, not used) frame the cuts; the Season Pass merge 2025-09-15 (match3d#438) is
the ZM3D release the Unity campaigns promote (C07C2866011/1759186080.203099). The Oct 24 layoffs are after the freeze and are not
referenced.

**Anchors per service.**

| Service | Record | Role |
|---|---|---|
| slack | D05S58U4SAK/{HUB_TS} (seed) | hub, Leonard → Frederick, 2025-09-30T22:40:12Z |
| slack | D05S58U4SAK/{CLAIM_TS} (seed) | Leonard's wrong admin claim, 2025-09-29T23:05:41Z |
| slack | C07UCC631A6/1757345931.336429, /1757347560.891949, /1757349668.681539 | Adjoe accidental campaign, pause, written waiver (thread replies) |
| slack | C07C2866011/1759186080.203099, /1759264050.305069; D05S58U4SAK/1758922541.613439 | Unity iOS campaigns on Sep 29–30; FB campaign off Sep 26 |
| trello | {H1} (seed) on 640643a3fd8f3ca308d9318e | H1 handover rules card; comment {CMT} (seed) |
| trello | {ENG} (seed) | same-board engineering decoy |
| trello | 67cf1b506d78ad3c72e02a35 (base, UA/BD board) | "Lock up social handles and domain?" — W4 target |
| trello | 670010236b89198587ca45b6 (base) | "Access to meta and Google Ad account shared with Node" (Oct 2024) |
| gmail | {GAMEND} (seed) | Arthur's Google Ads amendment |
| gmail | frederick.stone@harmonygames.co/1843428112007517388, /1843223812315546201 | Meta receipt Sep 16; AppLovin payout Sep 14 |
| gmail | frederick.stone@harmonygames.co/1835153849970828373, /1838369017520543217 | Google Ads 569-350-5790 (Harmony Games, Inc.); 449-481-1590 ads "funded by Calmplay LLC" |
| gdrive | {SWEEP} (seed) | "Admin sweep - Sep 30" folder with 15 exports |
| gdrive | {OPS} (seed) | "Company Ops" folder (destination) |
| gsheets | {SW_unity_ads} … (15 seeds) | per-platform user exports |
| gsheets | {MARCH} (seed) | Fred's "Marketing & UA logins" (Mar 10, 2025) |
| gdocs | {DOC} (seed) | Leonard's "Runway & shutdown cash notes" (H2) |
| confluence | {CONF} (seed) | "Company Accounts & Access" (2024, superseded) |

**Cohort.** `cohorts.json`: no fit — the 191 natural sets are Linear, GitHub, Slack and Gmail-bot populations; none is a set of
company accounts. The cohort is source-defined by H1 rule 1 over the sweep folder {SWEEP}.

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
card + comment, the engineering card, the handles card, the Node access card, Arthur's email, the cash notes doc, the 15 exports, the
March sheet, the Confluence page, the Meta / AppLovin / Google Ads / AdMob / LevelPlay mails. Known hazards walked from
`references/universe_kb/coherence_hazards.json` (all six categories).

| Record | Category | Fields | Evidence pointer | Hazard id | Disposition |
|---|---|---|---|---|---|
| Post-freeze base records (Adjoe Oct 1 invoice; Google Ads 449 cancellation Oct 16; Meta receipt Oct 6) | temporal | dates after 2025-10-01 | frederick.stone@harmonygames.co/1844773822453719122; /1846207913166171315; /1845217497507372901 | T07 | avoid: no requirement reads them; designed answers (Adjoe no cost; 449 CLOSE; Meta money moving) agree with them |
| Seeded Confluence page by Leonard dated 2024-03-12 | temporal | created_at vs author activity | confluence:{CONF} (planned) | T08 | avoid: Leonard active in Mar 2024 (activity.json); no edits after his activity |
| Seeded Trello card ids | temporal | id timestamp vs action date | trello:{H1}, {ENG}, {CMT} | T06 | fold in: ids minted from their own timestamps (`mint_ids.py`); card dateLastActivity = comment time |
| Frederick is_founder=false in PAYROLL_ROSTER | semantic | roster vs "Co-founder" | snowflake.json /tables/39 (PAYROLL_ROSTER) | S05 | avoid: not read; the prompt uses the assigned role only |
| Calm Play LLC vs Harmony Games naming | semantic | entity on store/ad accounts | C07C2866011/1752552076.522209; frederick.stone@harmonygames.co/1838369017520543217 | S06 | fold in as T8: the exports and Arthur's email name both entities and customer IDs |
| Slack links to Google files use native ids | cross-service referential | docs.google.com ids ≠ f_ ids | C08H78VJG80/1759174925.309129 | R04 | avoid: no seeded text carries a Google URL; records are named by title |
| UA claims vs warehouse (Unity Sep spend $0 in AD_SPEND_DAILY while Slack shows campaigns on) | quantitative | spend vs Slack | snowflake.json /tables/0 (AD_SPEND_DAILY); C07C2866011/1759186080.203099 | Q08 | avoid: money moving is decided by switched-on campaigns, receipts, payouts and waivers (H2); Snowflake is neither cited nor modified; Unity's answer is the same either way (campaign on) |
| Mirrored warehouse tables | quantitative | row-by-row | snowflake.json /tables/0, /tables/34 (AD_SPEND_DAILY, AD_SPEND) | Q09 | avoid: not read or modified |
| Thread reply counters on the adjoe parent | quantitative | reply_count | C07UCC631A6/1757345931.336429 | Q01 | avoid: no seeded reply on that thread |
| Done-list cards with open checklists | state/lifecycle | list vs checklist | trello:67cf1b506d78ad3c72e02a35 | L12 | avoid: the handles card is in "ZM 3d Technical Launch / Alpha", not Done; W4 adds an open checklist there |
| Token mailbox SVC_0009 forwards AppLovin payout mails ("Dear Leonard Hayes") | identifier/format | sender token | frederick.stone@harmonygames.co/1843223812315546201 | I05 | fold in: the export lists Leonard and Frederick as AppLovin admins, so the salutation agrees |
| Mixed Gmail date formats | identifier/format | RFC-2822 vs ISO | frederick.stone@harmonygames.co/1843428112007517388 | I04 | avoid: seeded mail uses the base RFC-2822 header form |
| Leonard is a token on Trello | identifier/format | member id | trello member PERSON_6094_TRELLO_USER_ID | I17 | fold in: seeded Trello actions are Arthur's (2162c1ba310341bf318f48b7); Leonard is named in text only |
| other: Brian Cooper / Brian Foster naming | other | display name | frederick.stone@harmonygames.co/1823332883409810377 | S04 | avoid: no Brian is a holder on any export |

**Sibling-defect sweep.** For each designed defect, other records with the same kind in scope:
- *Outside access on an ad account:* the Oct 2024 card shared both Meta and Google Ads with Node (trello:670010236b89198587ca45b6). The Sep 30 Google Ads exports (newer) list no partner, so only Meta carries Node; the export is the newest record and the card is history. Disposition: designed (Meta only); the Google Ads exports say "no linked managers or partners".
- *A holder who is not a company holder:* YouTube manager (base), TikTok shared login (base), Unity pending invite, Instagram personal address, LinkedIn — LinkedIn is checked against base: Leonard added Frederick to manage the page (C07KRTX5SCE/1726169948.231349), so LinkedIn has two company super admins (KEEP); Discord: Leonard created it and added the founders as admins (C07C2866011/1734154451.509769), so Discord is COMPANY-HELD (KEEP).
- *An account with money in the window that is not really money:* Meta "RE: meta Invoice" mails are Audience Network activity, not bills (frederick.stone@harmonygames.co/1842698832158940633); Meta is REVOKE whatever money says, so no row depends on them.
- *A closed account still on a list:* AdMob deactivated 2025-08-24 (frederick.stone@harmonygames.co/1841349862518331350) and the 2025-08-25 invite to an AdMob account; AdMob has no export in the sweep and is out of the cohort (T4). ironSource/LevelPlay (frederick.stone@harmonygames.co/1837038650805365569) is a MAX bidder — excluded by H1 rule 1 (T10).
- *Adjoe unpaid June invoice:* the Aug 4 reminder (frederick.stone@harmonygames.co/1839518563856917373) was paid in August (C04UEQVDVB7/1755117283.864129, not visible to Frederick); the design never uses an unpaid-bill clause, so no row depends on it.

## 1b Active speakers

Every person given a seeded voice, with `status_at_clock` from `references/universe_kb/activity.json` (clock 2025-10-01).

| Person | Email | status_at_clock (activity.json) | Seeding role |
|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025 | hub + claim (Slack DM), 90-day remark (#executives), cash notes (Docs), Company Ops folder (Drive), 2024 Confluence page |
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025 | H1 card + comment and engineering card (Trello), sweep folder + 15 exports (Drive/Sheets), Google Ads email (Gmail) |
| Frederick Stone | frederick.stone@harmonygames.co | active_sep_2025 | persona; owner of the March logins sheet (Sheets) |

Seeded text follows `references/universe_kb/conventions.json` (DM messages lowercase, median ~38–66 characters except the hub;
Arthur's card prose short numbered lines). Platform export rows are data, not speech.

## 1c Identity traps

`python3 Task_Authoring/tools/entity.py collisions` (verbatim, first sections) and `resolve` for every person the design names:

{ENTITY}

Correct entity vs lookalikes: Leonard Hayes is `leonard.hayes@harmonygames.co` (mailbox files `leonard@…`), Arthur Blake is
`arthur.blake@harmonygames.co` (mailbox files `blake@…`), Frederick is `frederick.stone@harmonygames.co` (files `frederick@…`). The
exports list holders by full address, so no shared first name decides a row. Node Media LLC is the agency Frederick terminated on
2024-12-20 (C07C2866011/1734721828.378119; D05S58U4SAK/1734719973.099339).

## 2 Cohort spine

**Rule (H1 rule 1).** Every marketing, UA, ad-monetization and social account in Arthur's Sep 30 sweep folder ({SWEEP}) that has
Frederick on it in any role; store accounts and data tools are on the engineering card; MAX-only bidders are not separate accounts.
The folder holds 15 exports; 12 are in scope.

**Per-account truth** (planned export content; money evidence is base unless marked seed):

| # | Account (export) | Holders that count | Class | Money moving (Sep 2025) | Action | Evidence |
|---|---|---|---|---|---|---|
| 1 | Meta ad account "Harmony Games" ({SW_meta}) | Frederick (Admin) — Leonard is Advertiser; Partners block: Node Media LLC, partner admin | OUTSIDE ACCESS | Y (receipt Sep 16; FB campaign off Sep 26) | REVOKE | frederick.stone@harmonygames.co/1843428112007517388; D05S58U4SAK/1758922541.613439 |
| 2 | Google Ads 569-350-5790 Harmony Games, Inc. ({SW_gads_569}) | Frederick, Leonard (Admin) | COMPANY-HELD | N | KEEP (Arthur's email) | frederick.stone@harmonygames.co/1835153849970828373; {GAMEND} |
| 3 | Google Ads 449-481-1590 Calm Play LLC ({SW_gads_449}) | Frederick (Admin) — Leonard Standard | SINGLE | N | CLOSE | frederick.stone@harmonygames.co/1838369017520543217 |
| 4 | Unity Ads org Calm Play LLC ({SW_unity_ads}) | Frederick (Owner) — Leonard Manager; Arthur Owner invite pending | SINGLE | Y (iOS campaigns on Sep 29–30) | TRANSFER | C07C2866011/1759186080.203099; /1759264050.305069 |
| 5 | AppLovin ({SW_applovin}) | Leonard, Frederick (Admin) | COMPANY-HELD | Y (payout Sep 14) | KEEP | frederick.stone@harmonygames.co/1843223812315546201 |
| 6 | adjoe advertiser dashboard ({SW_adjoe}) | Frederick, Leonard (Admin) | COMPANY-HELD | N (Sep installs waived in writing; paused Sep 8) | CLOSE | C07UCC631A6/1757349668.681539; /1757347560.891949 |
| 7 | TikTok Business Center ({SW_tiktok}) | Frederick (Admin) — Leonard uses Fred's login | SINGLE | N | TRANSFER (social) | D05S58U4SAK/1759170013.491159 |
| 8 | YouTube channel ({SW_youtube}) | Frederick (Owner) — Leonard Manager | SINGLE | N | TRANSFER (social) | D05S58U4SAK/1759096868.688389 |
| 9 | LinkedIn page ({SW_linkedin}) | Leonard, Frederick (Super admin) | COMPANY-HELD | N | KEEP (social) | C07KRTX5SCE/1726169948.231349 |
| 10 | X account ({SW_x}) | Frederick (Owner) | SINGLE | N | TRANSFER (social) | seed export only |
| 11 | Instagram ({SW_instagram}) | none — owner login is a personal Gmail address | SINGLE | N | TRANSFER (social) | seed export only |
| 12 | Discord server ({SW_discord}) | Leonard (Owner), Frederick, Robert (Admin) | COMPANY-HELD | N | KEEP (social) | C07C2866011/1734154451.509769 |
| — | Play Console ({SW_play_console}), App Store Connect ({SW_app_store_connect}), Singular ({SW_singular}) | — | out of scope (engineering card) | — | — | H1 rule 1 |

Totals the deliverables carry: REVOKE 1 · TRANSFER 5 (Unity, TikTok, YouTube, X, Instagram) · KEEP 4 · CLOSE 2; social transfers for
the handles card 4 (TikTok, YouTube, X, Instagram).

**Surfaces and shortcut audit.**

| Surface | Per-record call | Bulk call that does not cover it | Requirement · decides |
|---|---|---|---|
| per-platform export ({SW_meta} … 12 in scope) | `gsheets_values_get` × 12 | `gsheets_values_batch_get` reads one spreadsheet; `gdrive_list_files` returns names only | R2 · holders that count |
| money evidence (Gmail) | `gmail_search_messages` per platform sender | no one query spans SVC_0521 Meta, SVC_0009 AppLovin, SVC_0516 Google Ads, Adjoe, Unity | R4 · money moving (Y/N) |
| campaign state / waiver (Slack) | `slack_conversations_replies` on the adjoe thread; DM / #executives reads | channel history returns parents only; the waiver is a reply | R4 · money moving (Y/N) |

**Short-circuit audit.** Holders decide the class only together with the partner block (Meta) and the scope clause; money decides
CLOSE for any class but OUTSIDE ACCESS; the socials exemption and the Google Ads amendment override CLOSE for six rows. No surface is
skippable: a run that reads holders only gets CLOSE rows wrong; a run that reads money only gets every class wrong.

**Predicate details.** Closed vocabulary (classes OUTSIDE ACCESS / SINGLE / COMPANY-HELD; actions REVOKE / CLOSE / TRANSFER / KEEP);
"holder" = Owner or Admin only; order REVOKE → CLOSE → TRANSFER/KEEP. **House rule overriding the natural reading (A15):** a manager,
a pending invite, a shared login or a personal address is not a holder, so four accounts that look shared are SINGLE. **Dual regime:**
none (a single September window). **Boundary records (A17):** AdMob on the March sheet only; the Calm Play Google Ads, X, Instagram and
Discord on the sweep only; three out-of-scope exports inside the sweep folder.

## 3 Hidden authorities

| Id | Name (how the hub names it) | Home | Governs | Decoy(s) | Decoy scope / supersession | Findability proof |
|---|---|---|---|---|---|---|
| H1 | Arthur's account handover rules ("arthur's handover rules are on the ops board", D05S58U4SAK/{HUB_TS}) | trello {H1} + comment {CMT} | R1, R2, R3, R5, R8 | same-board engineering card {ENG}; Confluence {CONF} | {ENG}: team scope (engineering, store, data-tool accounts); {CONF}: older version (T2 version_records) | a Trello search "handover rules" returns both cards (same title stem); seeded at injection, proven there with `hg.py search search trello "handover rules"` |
| H2 | Leonard's cash notes ("for money moving go by my cash notes doc", D05S58U4SAK/{HUB_TS}) | gdocs {DOC} section "Money still moving" | R4 | #executives remark C07C2866011/{DECOY90_TS} (seed) | older version (T3 version_records) | a Docs/Drive search "cash notes" returns the doc title "Runway & shutdown cash notes" |

`governs` lists do not overlap. H1's comment points to Arthur's email ({GAMEND}), so the email is reached through the card.

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Leonard's account handover ask | slack D05S58U4SAK/{HUB_TS} |

**Hub** = A1 (Leonard's voice) delegating to H1, H2, the sweep and the destination folder.

**Incorporation table** (quotes are exact substrings of `planned_text.json`; the gate re-reads them from the SQL at injection):

| Fragment | Service · container | Kind | Chain | delegated_by_record | delegation_quote | Requirements | Names |
|---|---|---|---|---|---|---|---|
| K1 | slack · D05S58U4SAK/{HUB_TS} | delegation | A1 | D05S58U4SAK/{HUB_TS} | "reply here with how many need a transfer and anything an outsider still has access to" | R6 | H1, H2 |
| K2 | trello · {H1} | requirement | A1 | D05S58U4SAK/{HUB_TS} | "arthur's handover rules are on the ops board, they decide the action" | R1 R2 R3 R5 | — |
| K3 | trello · {CMT} | amendment | A1→K2 | trello:{H1} | "If anything changes I'll put it in the comments here." | R5 | — |
| K4 | gmail · {GAMEND} | amendment | A1→K2→K3 | trello:{CMT} | "I'll email you both once he decides" | R5 | — |
| K5 | gdocs · {DOC} | requirement | A1 | D05S58U4SAK/{HUB_TS} | "for money moving go by my cash notes doc" | R4 | — |
| K6 | gdrive · {SWEEP} | requirement | A1 | D05S58U4SAK/{HUB_TS} | "arthur's sweep from today is the list" | R1 R2 | — |
| K7 | gdrive · {OPS} | destination | A1 | D05S58U4SAK/{HUB_TS} | "save the register in the Company Ops folder" | R7 | — |
| K8 | trello · 67cf1b506d78ad3c72e02a35 | destination | A1→K2 | trello:{H1} | "Socials that need a transfer go as a checklist on Fred's" | R8 | — |

**Amendments.** K3 (Trello comment, 2025-09-30T15:22:40Z) changes H1 rule 5 for socials only; K4 (Gmail, 2025-09-30T23:21:09Z) changes
rule 5 for one named Google Ads account; both say the rest stands.

**Non-authoritative instruction distractors.** The #executives 90-day remark (seed, C07C2866011/{DECOY90_TS}) is Leonard's earlier
view, superseded by his own doc; the engineering card's "one Owner is fine … mark each one KEEP or MOVE" governs another team's list.

## 5 Chains and trap register

**Chains** (manifest `chains`): C1 A1 (Leonard's claim → Unity export → H1 rule 2 → Unity TRANSFER); C2 A9 (Adjoe accidental
campaign → rep's waiver reply → H2 waiver clause → Adjoe CLOSE); C3 A13 (H1 CLOSE rule → comment pointer → Arthur's email → 569 KEEP,
449 CLOSE); C4 A17 (March sheet → sweep folder → H1 scope → the 12 accounts).

| Trap | Family | Records | Requirement | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T1 | superseding | D05S58U4SAK/{CLAIM_TS} → {SW_unity_ads}, {SW_meta}, {SW_gads_449} | R2 | Leonard counted as admin on Meta, Calm Play Google Ads, Unity | newer exports (Sep 30) | claim sits above the hub in the DM |
| T2 | superseding (4 versions) | {CONF} → {H1} → {CMT} → {GAMEND} | R5 | 2024 page or card alone applied | card replaces page; comment; email | Confluence search returns the page first |
| T3 | superseding | C07C2866011/{DECOY90_TS} → {DOC} | R4 | 90-day paid rule keeps Adjoe | the doc named in the hub | Slack search hits the remark first |
| T4 | distractor · partial_listing | {MARCH} | R1 | register built from the March sheet | hub: the sweep is the list | the hub names both |
| T5 | distractor · scope_adjacent | {ENG} | R3 | one-owner-is-fine rule applied | engineering scope | same Trello search |
| T6 | exact_predicate | {SW_unity_ads}, {SW_youtube}, {SW_tiktok}, {SW_instagram}; D05S58U4SAK/1759096868.688389 | R3 | manager / pending / shared / personal counted | H1 rules 2–3 | — |
| T7 | eliminating_evidence | C07UCC631A6/1757345931.336429 → /1757349668.681539 | R4 | Adjoe money moving | waiver in the reply | parent visible, reply not |
| T8 | entity_collision | {SW_gads_569}, {SW_gads_449}; frederick.stone@harmonygames.co/1838369017520543217 | R5 | one Google Ads, or the wrong one kept | customer IDs in the email | March sheet says "Google Ads" |
| T9 | tool_surface | {SW_meta}; trello:670010236b89198587ca45b6 | R3 | Meta SINGLE → TRANSFER | Partners block lists Node Media LLC | People block is first |
| T10 | scope_alias | {SW_play_console}, {SW_app_store_connect}, {SW_singular}; frederick.stone@harmonygames.co/1837038650805365569 | R1 | stores / Singular / ironSource added | H1 rule 1 | exports sit in the same folder |
| T11 | reuse_exclusion | trello:67cf1b506d78ad3c72e02a35 | R8 | new card for socials | H1 rule 7 | — |
| T12 | distractor · keyword_collision | C08H78VJG80/1759174925.309129; frederick.stone@harmonygames.co/1840501641217286806 | R1 | PlayableX / Balancy listed as accounts | no export in the sweep | vendor threads are recent |
| T13 | distractor · stale_summary | C07C2866011/1759110509.707539 → D05S58U4SAK/1759170013.491159 | R1 | TikTok dropped ("doesn't exist anymore") | same-day recovery + export | #executives message first |

Trap independence: T6 and T9 fail different rows (T6 four accounts, T9 Meta); T7 and T3 hit Adjoe through different sources (an
agent that has the doc still needs the reply); T8 is independent of T2 (a run can read the email and still keep the wrong Google Ads
account). No record states a conclusion: the exports list users and roles, the doc defines money, the replies state facts.

## 6 Failure-diversity plan

| Chain / trap | Runs that plausibly miss it | Rows it touches |
|---|---|---|
| C1/T1/T6 (holder rules) | runs that trust Leonard's claim or count managers | Unity, YouTube, TikTok, Instagram class + action (8 values) |
| T9 (partner block) | runs that read the first rows of each export | Meta class + action + reply's outside-access clause |
| C2/T7 (waiver reply) | runs that never open thread replies (A14: 67/124) | Adjoe money + action |
| C3/T2 (comment + email) | runs that read the card description only, or never open Gmail (A13) | 569 action; 4 dormant socials |
| T4/T10/T12/T13 (cohort) | runs that start from the March sheet or include every export | register membership, row count |
| T11 / K7 (writes) | runs that create a new card or leave the sheet in My Drive | W4 target; R7 |

No single discovery gates more than about a third of the graded values; H1 is named in the hub and is likely found, so its
failures come from applying rules 2–5, not from finding it.

## 7 Deliverables and dependent writes

| Write | Tool | Content depends on | Requirements |
|---|---|---|---|
| W1 register (Google Sheet, 12 rows: account, holders that count, class, money moving, action) | `gsheets_create_spreadsheet` + `gsheets_values_update` | K2–K6, C1–C4, T6, T9 | R1–R5 |
| W2 register in Company Ops ({OPS}) | `gdrive_move_file` (or create with parent) | K7 | R7 |
| W3 DM reply to Leonard (D05S58U4SAK): 5 transfers, Node Media still has partner admin on Meta | `slack_send_message` | K1, C1, T6, T9 | R6 |
| W4 checklist on 67cf1b506d78ad3c72e02a35 with TikTok, YouTube, X, Instagram | `trello_create_checklist` + `trello_create_check_item` | K3, K8, T6, T11 | R8 |

Reuse-vs-create (A8): W4 reuses the existing handles card. Frederick can edit: Trello unscoped writes; the Company Ops folder is shared
with him as writer (record plan); the DM is his.

## 8 Service role map

| Service | Role | Load-bearing fact / write | Carrier |
|---|---|---|---|
| slack | hub, claim, Adjoe waiver reply, campaign state; W3 | D05S58U4SAK/{HUB_TS}; C07UCC631A6/1757349668.681539 | ● |
| trello | H1 + comment, decoy, handles card; W4 | {H1}; {CMT}; 67cf1b506d78ad3c72e02a35 | ● (description, comment) |
| gmail | Google Ads amendment; money evidence | {GAMEND}; frederick.stone@harmonygames.co/1843223812315546201 | ● |
| gsheets | 15 exports; March sheet; W1 | {SW_meta} | ● |
| gdocs | H2 | {DOC} | ● |
| gdrive | sweep folder; destination; W2 | {SWEEP}; {OPS} | ● (metadata, folder path) |
| confluence | superseded rules page | {CONF} | ● (body) |
| gcal | none | — | — |
| gslides | none | — | — |
| contacts | none | — | — |
| github | none | — | — |
| linear | none | — | — |
| snowflake | none (warehouse spend deliberately not used; hazard Q08) | — | — |

## 9 Call budget

| Phase | Service | Calls | Reason |
|---|---|---|---|
| discovery | slack | 3 | hub and surrounding DM; #executives context; adjoe channel |
| discovery | trello | 3 | search handover rules; read both cards |
| discovery | gdrive | 3 | find sweep folder; list 15 exports; find Company Ops |
| discovery | gdocs | 2 | find and read the cash notes |
| discovery | gmail | 2 | find and read Arthur's email |
| discovery | confluence | 2 | find and read the page the card replaces |
| discovery | gsheets | 1 | March logins sheet |
| rules | trello | 1 | card comments |
| per-record | gsheets | 12 | one export per in-scope account |
| per-record | gmail | 12 | September money evidence per account |
| per-record | slack | 6 | Unity on; Meta off; Adjoe parent + replies; YouTube/TikTok ownership |
| per-record | trello | 1 | the Node access card behind the Meta partner |
| reads-before-writes | trello | 2 | find handles card; check its checklists |
| writes | gsheets | 3 | create, write, read back |
| writes | gdrive | 2 | move, confirm parent |
| writes | slack | 2 | reply, read back |
| writes | trello | 6 | checklist + 4 items + read back |
| **total** | 7 services | **63** | unconditional; largest share outside the per-record phase trello 38% |

Golden-run rule: a correct run cannot skip the 12 exports (holders exist nowhere else), the money evidence (decides CLOSE), the
comment or the email (they flip six rows). Expected measured range 70–95 with ordinary exploration.

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolved by |
|---|---|---|---|
| ironSource/LevelPlay on the register? | no | Fred has an ironSource account (frederick.stone@harmonygames.co/1837038650805365569) | H1 rule 1 MAX-bidder clause; no export in the sweep |
| Store and Singular exports on the register? | no | they are in the sweep folder with Fred on them | H1 rule 1 (engineering card) |
| AdMob on the register? | no | listed on the March sheet | hub: the sweep is the list; deactivated frederick.stone@harmonygames.co/1841349862518331350 |
| Unity class | SINGLE | Arthur is listed as Owner; Leonard runs campaigns | export: Arthur's invite pending; Leonard Manager; H1 rule 2 |
| Meta action | REVOKE | TRANSFER (Fred is the only company admin) | Partners block; H1 rule 4–5 order (OUTSIDE wins) |
| Adjoe money | N | campaign ran Sep 1–8 | waiver reply C07UCC631A6/1757349668.681539 + H2 clause; paused /1757347560.891949 |
| Google Ads 569 action | KEEP | CLOSE (no money) | Arthur's email (newer, names 569-350-5790) |
| Dormant socials (X, LinkedIn, Discord, Instagram, TikTok, YouTube) | TRANSFER/KEEP by class | CLOSE (no money) | card comment {CMT} (newer, same author) |
| Instagram class | SINGLE | OUTSIDE ACCESS (non-company address) | H1 rule 3: a personal address isn't outside access |
| Destination | Company Ops folder | the sweep folder or My Drive | hub quote "save the register in the Company Ops folder" |
| Reply placement | DM with Leonard (top level or thread) | #executives | hub "reply here"; both DM forms accepted |
| Socials write | checklist on the existing handles card | new card | H1 rule 7 |

### Reach table (load-bearing records)

Base records verified with `persona_view.py can-see frederick_stone …` (lines pasted in §12). Planned seeds are verified at the
injection gate (`check-sql`): the DM is Frederick's, the Gmail copy is in his mailbox, the sweep folder/exports, the doc and the
Company Ops folder are shared with him, Trello and Confluence are unscoped. LB = load-bearing.

| Record | Service | Verdict | LB |
|---|---|---|---|
| D05S58U4SAK/1759096868.688389 | slack | YES (im member) | LB |
| D05S58U4SAK/1759170013.491159 | slack | YES | LB |
| D05S58U4SAK/1758922541.613439 | slack | YES | LB |
| C07C2866011/1759186080.203099 | slack | YES (executives member) | LB |
| C07C2866011/1759264050.305069 | slack | YES | LB |
| C07UCC631A6/1757345931.336429 | slack | YES (adjoe member) | LB |
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

**Feasibility.** Writes exist in `Evals/references/tools/catalog.json`: `gsheets_create_spreadsheet`, `gsheets_values_update`,
`gdrive_move_file` (newParentId), `slack_send_message` (channel D05S58U4SAK), `trello_create_checklist`, `trello_create_check_item`.
Frederick must be a writer on {OPS} (record plan). Values are categorical, no precision issue.

**Explicit rules.** Window: September 2025, or a campaign still switched on (H2). Holder: Owner/Admin only (H1 rule 2). Order of
actions: REVOKE → CLOSE → TRANSFER/KEEP (rule 5). Amendments retain the rest ("Rest of the card stands"; "Everything else on the card
and my comment stands"). Every cross-reference postdates its target: the hub (22:40Z) postdates the card (Sep 29 21:31Z), the doc
(modified 17:48Z), the sweep (19:52–20:31Z) and the folder (22:31Z); the comment (15:22Z) postdates the card; the email (23:21Z)
postdates the comment.

**Precedence (carrier eligibility).** Load-bearing facts sit in ● carriers only (Slack messages and replies, Trello description and
comment, Gmail body, Sheets values, Docs body, Confluence body, Drive metadata) — `references/Ask_Carriers.md` §5 as amended by §6b.

**Prompt naturalness.** The human's trigger should name the anchor (Leonard's ask in the DM) and the deliverable kind; it must not
list the accounts, the rules, the folder names, the classes or the actions.

**Grading devices** (for the human's rubric later): the exact 12-account set; per-account action (≤ 5 spot checks per group + one
row-count criterion); the transfer count 5 and the outside party (Node Media LLC on Meta) in the reply; the four checklist items on
the existing card; the register's location. Both DM reply forms accepted; holders may be written by name or address.

## 11 Record plan for /create-injection

| Row(s) | Table | Id / key | Time (UTC) | Owner / author | Notes |
|---|---|---|---|---|---|
| 1 | slack.slack_messages | D05S58U4SAK/{CLAIM_TS} | 2025-09-29T23:05:41Z | Leonard | claim (planned_text S_CLAIM) |
| 2 | slack.slack_messages | D05S58U4SAK/{HUB_TS} | 2025-09-30T22:40:12Z | Leonard | hub (S_HUB) |
| 3 | slack.slack_messages | C07C2866011/{DECOY90_TS} | 2025-09-15T19:02:33Z | Leonard | 90-day remark (S_DECOY90), top level |
| 4–5 | trello.trello_cards + createCard action | {H1} / {H1C} | 2025-09-29T21:31:07Z | Arthur | board 640643a3fd8f3ca308d9318e list To Do; desc H1_DESC; badges.comments 1; dateLastActivity = comment time |
| 6–7 | trello.trello_cards + createCard action | {ENG} / {ENGC} | 2025-09-29T21:44:52Z | Arthur | ENG_DESC |
| 8 | trello.trello_actions commentCard | {CMT} | 2025-09-30T15:22:40Z | Arthur | H1_CMT on {H1} |
| 9–12 | gmail threads + messages | {GAMEND} (+ copies in leonard.hayes@ and arthur.blake@ mailboxes) | 2025-09-30T23:21:09Z | Arthur → Frederick, cc Leonard | G_AMEND_SUBJECT / BODY |
| 13 | gdrive.drive_files (folder) | {SWEEP} "Admin sweep - Sep 30" | 2025-09-30T19:50:00Z | Arthur | shared Leonard (writer), Frederick (reader) |
| 14–43 | gdrive + gsheets (15 spreadsheets × file/spreadsheet/sheet rows) | {SW_meta} … {SW_singular} | 2025-09-30T19:52–20:31Z | Arthur | one export per platform; Meta export has People then Partners blocks; Unity row "Arthur Blake · Owner · Invited 2025-09-30 (pending)" |
| 44–46 | gdrive + gsheets | {MARCH} "Marketing & UA logins" | 2025-03-10T17:40:00Z | Frederick | lists Meta, Google Ads, Unity Ads, AppLovin, Adjoe, AdMob, Singular, TikTok, YouTube, LinkedIn, PlayableX |
| 47–48 | gdrive + gdocs | {DOC} "Runway & shutdown cash notes" | created 2025-09-25T16:12Z, modified 2025-09-30T17:48Z | Leonard | shared Frederick (reader); section DOC_CASH_MONEY among other notes |
| 49 | gdrive.drive_files (folder) | {OPS} "Company Ops" | 2025-09-30T22:31:00Z | Leonard | shared Frederick and Arthur as writers |
| 50–51 | confluence pages + page_versions | {CONF} | 2024-03-12T16:20:00Z | Leonard (user_EMPLOYEE_0038) | parent page_company_home, space_COMPANY, version 1 |

About 60 inserted rows over 7 services (slack, trello, gmail, gdrive, gsheets, gdocs, confluence) — ≥ 50 rows and ≥ 6 injected
services for the normal profile. No base row is updated except the Trello card's own badges at insert time.

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
- Reads the hub, trusts Leonard's claim, takes the March sheet → wrong set (AdMob, Singular, PlayableX in; 4 missing). Leak? No: the
  hub says the sweep is the list; a lazy run scores only rows that coincide.
- Reads the H1 card but not its comments → closes six dormant socials. Leak fixed in v1 design by keeping the socials exemption out of
  the card description and the hub.
- Reads the adjoe channel history (parents only) → Adjoe money Y. The waiver is only in replies (C07UCC631A6/1757349668.681539).
- Reads the first block of each export → Meta TRANSFER. The Partners block decides REVOKE.
- Bulk shortcut check: no Snowflake table, Sheet or Confluence page lists accounts with roles; `gsheets_values_batch_get` cannot
  read 12 spreadsheets in one call; Gmail has no cross-sender query that returns September money for every account.

**Literal-value sweep** (planned, re-run at injection on the SQL): "569-350-5790" appears in base Google mails and in the seeded export
and email only; "Node Media LLC" appears in base Dec 2024 termination messages, never with "partner admin"; "REVOKE", "TRANSFER",
"OUTSIDE ACCESS" appear only in the H1 card. **Wording sweep:** the waiver reply says "not be responsible for the cost", the doc says
"agreed in writing to drop" — no shared decisive phrase. **"The rest stands" check:** no record after the comment re-asserts CLOSE for
socials; no record after the email re-asserts CLOSE for 569.

### Self-review

Re-read `Evals/1_Prompt_Eval.md` §2.1 (Unique Ground Truth), §2.2 (Feasibility), §3.2 (Cross-Service Coherence),
`Evals/0_Injection_Quality_Eval.md` Check C and `references/Docs/11_V3_Changes.md`, then walked the design in order. Re-read every
load-bearing base value through `tools/hg.py` / direct reads of the exports this session (Slack DM, adjoe thread, #executives,
Gmail receipts/payouts, Google Ads mails, Trello cards).

| # | Check / category | Verdict | Counter-reading (strongest argument the other way) | Resolution with evidence |
|---|---|---|---|---|
| 1 | temporal | PASS | base records after the freeze (Adjoe Oct 1 invoice, 449 canceled Oct 16) are visible and could be read as "already happened" | not cited by any requirement; designed answers agree with them; hazard T07 (frederick.stone@harmonygames.co/1846207913166171315) |
| 2 | temporal (seeded) | PASS | the email at 23:21Z sits 39 minutes before the freeze | 2025-09-30T23:21:09Z < 2025-10-01T00:00Z (V3 §3); `minted_ids.json` G_AMEND |
| 3 | temporal (chronology) | PASS | the hub could cite a sweep made after it | sweep exports 19:52–20:31Z, hub 22:40Z (record plan rows 2, 14–43) |
| 4 | semantic | PASS | "Google Ads" names two accounts and the email could be read as the Calm Play one | email names "Harmony Games, Inc." and 569-350-5790; base mails tie 569 to "[SOURCE_ORG_0001], Inc." (frederick.stone@harmonygames.co/1835153849970828373) and 449 to Calmplay (/1838369017520543217) |
| 5 | semantic (Instagram) | PASS | a personal Gmail owner could be "outside access" → REVOKE | H1 rule 3 states a personal address isn't outside access (planned_text H1_DESC) |
| 6 | cross-service referential | PASS | the hub names "arthur's sweep from today" and "the Company Ops folder"; a dropped seed dangles | both planned and dated before the hub ({SWEEP} 19:50Z, {OPS} 22:31Z); injection gate checks seeded ids |
| 7 | cross-service referential (Node) | PASS | the Oct 2024 card shared Google Ads with Node too; the 569 export without Node contradicts it | the export is 11 months newer and describes current access; the card is a to-do, not a state (trello:670010236b89198587ca45b6) |
| 8 | quantitative | PASS | Snowflake shows Unity September spend $0, so money moving could be N and Unity CLOSE | H2 counts a switched-on campaign; Unity iOS campaigns on (C07C2866011/1759186080.203099, /1759264050.305069); hazard Q08 excluded |
| 9 | quantitative (Meta) | PASS | warehouse Meta Sep spend is $0 while a receipt exists | Meta's action is REVOKE whatever money says (H1 rule 5 order); receipt frederick.stone@harmonygames.co/1843428112007517388 |
| 10 | state/lifecycle | PASS | Adjoe: the June invoice reminder (Aug 4) suggests an unpaid bill | paid in August (C04UEQVDVB7/1755117283.864129); the design has no unpaid-bill clause, so no row depends on it |
| 11 | state/lifecycle (TikTok) | PASS | "our TikTok account doesn't exist anymore" (C07C2866011/1759110509.707539) | recovered the same day (D05S58U4SAK/1759170013.491159); export lists the account |
| 12 | identifier/format | PASS | seeded Trello ids could break the timestamp scheme (I16/T06) | minted from their own timestamps (`mint_ids.py`): {H1} → 2025-09-29T21:31:07Z |
| 13 | identifier/format (Gmail) | PASS | the seeded email id could collide or break the 19-digit scheme | id = ms<<20 pattern of base ids (frederick.stone@harmonygames.co/1843428112007517388 is Sep 16); collision check at injection |
| 14 | other (persona plausibility) | PASS | a custody register might look like Arthur's job, not Frederick's | the hub delegates it to Frederick and the accounts are his (D05S58U4SAK/1759096868.688389; C07C2866011/1759186080.203099) |
| 15 | other (Leonard as wrong author) | PASS | the requester's own claim being wrong could read as a truthfulness defect | it is a dated human claim (Sep 29) overturned by newer exports (Sep 30); Atlas rule 12 human-claim-vs-record (T1) |
| DP1 | two-reading: ironSource | PASS | a careful run adds ironSource from the Jul 8 welcome mail | H1 rule 1 MAX-bidder clause decides (frederick.stone@harmonygames.co/1837038650805365569) |
| DP2 | two-reading: stores/Singular | PASS | they are in the sweep with Fred on them | H1 rule 1 names them on the engineering card ({ENG}) |
| DP3 | two-reading: AdMob | PASS | the March sheet lists it | no export; deactivated frederick.stone@harmonygames.co/1841349862518331350 |
| DP4 | two-reading: Unity | PASS | Arthur Owner → COMPANY-HELD → KEEP | pending invite (export {SW_unity_ads}); H1 rule 2 |
| DP5 | two-reading: Meta | PASS | Fred is the only company admin → TRANSFER | Partners block ({SW_meta}); rule 5 order |
| DP6 | two-reading: Adjoe | PASS | ran in September → money Y | waiver reply C07UCC631A6/1757349668.681539 |
| DP7 | two-reading: 569 | PASS | no money → CLOSE | Arthur's email {GAMEND} is newer and names it |
| DP8 | two-reading: dormant socials | PASS | no money → CLOSE | comment {CMT} |
| DP9 | two-reading: Instagram | PASS | non-company address → OUTSIDE | H1 rule 3 |
| DP10 | two-reading: destination | PASS | the sweep folder is "Arthur's" place for this | hub quote names Company Ops (D05S58U4SAK/{HUB_TS}) |
| DP11 | two-reading: reply | PASS | a new top-level message vs a thread reply | both in D05S58U4SAK accepted (grading devices) |
| DP12 | two-reading: socials write | PASS | a new card is cleaner | H1 rule 7 (trello:67cf1b506d78ad3c72e02a35) |

HARDNESS GATE output: pasted above (normal, design PASS).

Unresolved: (1) the honest necessary budget is 63 calls against the author's 70+ target; the measured count comes from the Opus
pre-check (expected 70–95). (2) Red team unavailable (§13); an independent subagent review substitutes. (3) Findability searches for
the seeded H1/H2 names are proven at injection, when the records exist.

## 13 Red team (dual)

{REDTEAM}
