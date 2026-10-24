# Scenario Design — ip-sale-defect-schedule · design only · contains no prompt, OE or criterion text

Engine test run (`support/examples/sample_task_01`). Not a platform task.

## Assignment · persona reach census · horizon note

| Field | Value |
|---|---|
| Persona | Arthur Blake · `arthur_blake` · `arthur.blake@harmonygames.co` (roster: Co-founder & CTO, Executive) |
| Business function / Evals category | Executive / Engineering & Live-Ops |
| Competency | Engineering Ops |
| Task skill | Analysis and Synthesis (stacked: Actions) |
| Horizon | Long Horizon → `extreme` profile |

Reach census (verified 2026-10-03 from the exports):
- **Slack**: 216 channels. Member of `#winddown` `C0ADGSZKR3R` (members Robert, Arthur, Leonard + 4 bot/system ids), `#god-bugs` `C05V5FNLB9V`, `#zombie-bugs` `C08R27X0EAH`, `#live-incidents` `C080X4GTZ0E`, `#company-internal` `C05KNDCHAAG`; DMs `D04UGG61DUM` (Arthur–Leonard), `D07H86MU8JC` (Arthur–Oliver).
- **Gmail**: mailbox present; thread ids are `arthur.blake@harmonygames.co/<19-digit>` while export filenames are `blake@harmonygames.co_<thrid>.json` (4,721 thread files). Holds copies of the Sherwood thread, the Feb 11 contractor termination letters (cc), the PE "Offer to Purchase" mails.
- **Drive**: root `d_cc3e90160f490686039986`; Leonard root `d_63fffeb4fab5233ed5bb73`; Robert root `d_9f7ba94f7526d54d8482ba`.
- **GCal**: own calendar; copy of the Feb 11 "Wind Down" call `evt_e02ad4661e15802e6a6e84` (Sunset).
- **Linear** `usr_cc3e90160f490686`; **Trello** member `2162c1ba310341bf318f48b7` (founders' board "Harmony Games" `640643a3fd8f3ca308d9318e`); **GitHub** `EMPLOYEE_0025_GITHUB_USERNAME`; **Confluence** `user_EMPLOYEE_0025`; **Contacts** `cc3e90160f49068603998654`.

Remit argument: on 2026-02-12 Leonard signs the wind-down + data-licensing agreement with Sunset (`#winddown` 1770931777.561519), lists "onboarding with [Sunset] and giving them the data" as his next item (1770934638.035469) and hands Arthur "data stuff" (1770935637.304259, 1770935695.500189). On Feb 11 he said the IP goes to auction (`#executives` 1770850800.723979). A known-defects disclosure per game title is CTO work in that hand-off. Engineering Ops = defect inventory, triage tiers, fix-evidence from code history, release state.

Horizon note: Long Horizon assignment → extreme profile. **Iteration 3 (current, §14): honest budget 386, of which 290 are conditional on unverified tool behaviour → floor 96 if all resolve to bulk. The gate fails `call_budget` (< 500); every other check passes.** Iteration 2's 551 was not established (R1 §6). Expected golden run ≈ 100–390 → Long Horizon tier either way; the engine's extreme volume target is not reachable honestly with this cohort.

## 1 Storyline

**"Known-defects schedule for the IP sale"** (Feb 12–13 2026). Sunset (wind-down + data-licensing provider, chosen over Sherwood on Feb 12) needs, from the CTO, a schedule of every open defect per game lot for the IP listing. Leonard delegates it to Arthur in `#winddown`; the rules live in four different places; claims about what is "fixed" disagree with the tracker and code history.

Anchors per service (base, verified):
- Slack: `#winddown` natural Feb 12 messages 1770931777.561519 (agreement signed), 1770934638.035469, 1770935637.304259, 1770935695.500189 (data stuff → Arthur), 1770937232.664809, 1770937460.360699 (last base message); `D04UGG61DUM` 1770751702.596069 (Leonard: 0.3.309 stuck at the loading screen at 8%); `#executives` 1770850800.723979 (IP to auction), 1770850852.708789 ("Sunset ~$15K").
- Linear: 73 open defect tickets on ENG (48) and ZOM (25) (state Bugs/Regression or label Bug); sub-issue parents ENG-2280 (children ENG-2073/2114/2281) and ENG-2128 (children ENG-2110/2130/2242); Acceptable-Behavior tickets ENG-1411, ENG-1877; WebGL tickets ENG-2406/2407/2408; Bug-labelled lookalikes on other teams ART-695, ART-696, EPI-25.
- GitHub: fix PRs referencing cohort tickets: GameOfDominoes#1583 + #1773 (ENG-1866), #1882 (ENG-2331), match3d#522 (ZOM-616), #529 (ZOM-614), #539 merged + #543 open (ZOM-542); game-of-dominoes-backend#79 "Admin Endpoints and Store Catalog" (Arthur, merged 2025-12-03).
- Gmail: Sherwood "wind-down support request" copy `arthur.blake@harmonygames.co/1856689465050769375`.
- GCal: Sunset "Wind Down" call copies `evt_212e50fb5a53ea8016ce29` (Leonard) / `evt_e02ad4661e15802e6a6e84` (Arthur) / `evt_c6875435ebeb394d3ca298` (Robert).
- Confluence: `page_company_home` (parent for the decoy); `page_qa_runbook` (Vincent left Nov 2025 — constrains who can speak in 2026).
- Trello: founders' board lists To Do `640643a3fd8f3ca308d93195`, Doing `…93196`, Done `…93197`; last activity 2025-11-12; max idShort 455.

Natural contradictions used (all dated human claims vs records): Leonard's "sign-in bugs fixed" claim vs open tickets with no fix PR; Arthur's own Dec-2025 "clamps lives" PR comment vs Leonard's Feb-11 report; the overview deck's placeholder count vs the tracker.

Coherence audit (task-touched data):
- Sunset vs Sherwood: base shows Sherwood was consulted but Sunset signed (Feb 12). Design uses Sunset only; Sherwood thread is not touched.
- Who is active in Feb 2026: Vincent left Nov 2025 (`page_qa_runbook`), Douglas has no activity after Aug 2025. Seeded 2026 voices are Leonard, Arthur, Robert only.
- Lifecycle lags to keep OUT: ENG-2414..2435 "UI Optimization" tickets in state PR whose PRs merged (ENG-2417→#1901 etc.) — none is a defect, none in the cohort; LIVE_EVENT_PERFORMANCE `completed` rows vs Slack outages — Snowflake not used.
- Sherwood mails are labelled SPAM in Arthur's copy; seeded Leonard mails use INBOX (different sender; deliberate).
- Token reuse avoided: `PERSON_3207_EMAIL` already belongs to a MotionCue sender, so the Sunset onboarding contact is minted as `PERSON_9823` (0 hits across Gmail, other services, GitHub). Sunset's CEO uses `PERSON_1674` (appears only as `[PERSON_NAME_1674]`, "Sunset's CEO", `#winddown` 1770924399.692889).
- Trello board `dateLastActivity` is bumped to the new card's activity.

## 2 Cohort spine

- **Rule** (homed in H1): every open ticket on the Linear ENG (Domino Delights) and ZOM (Zombie Match 3D) teams that is a defect — state Bugs or Regression, or label Bug; open = not Done/Canceled/Duplicate; drop label "Acceptable Behavior"; drop tickets created after the intake cut-off; one row per defect, a sub-issue whose parent is also listed is folded into the parent's row.
- **Size**: 73 natural + 2 seeded (ENG-2438 created Feb 10, ENG-2440 created Feb 13 20:31Z) = 75 candidates → 73 tickets after the AB exclusion → **67 rows** (6 folded): Lot A 39, Lot B 25, Not-in-lot Web 3.
- **Surfaces** (per record): Linear `get_issue` (parent/sub-issue + labels + state; list may omit parent [U]); GitHub PR search by ticket id (no Linear↔GitHub link field; `links_json` empty everywhere); GitHub PR conversation comments for each candidate PR (reference can sit only in a comment — backend#79); Slack/Gmail written-reproduction check for each FIX MERGED row.
- **Shortcut audit** (against `Evals/references/tools/catalog.json`):
  - `linear_list_issues` returns state/priority/labels in bulk — tiers and membership are bulk-derivable; only `parent` (sub-issue fold) may need `get_issue` [U]. **Shortcut exists for most fields.**
  - `github_list_pull_requests` (head_ref carries `ENG-####`) or one `github_search_pull_requests "ENG-"` per repo returns titles/branches in ~30 pages → per-ticket searches collapse. **Shortcut exists** for title/branch references; it does **not** return conversation comments (backend#79#c_2) — that hop needs the Slack pointer.
  - `slack_conversations_search_messages` returns parents; the decisive corrections are thread replies (`slack_read_thread` per thread).
  - Net: necessary per-record floor ≈ 1.6 calls/ticket, not 3–6. Honest.
- **House rules overriding the natural reading (A15, per record)**: H2 tiers (No-priority→T3, Regression bump, Hot-Fix clause as amended); sub-issue fold; WebGL tickets off the lot totals.
- **Dual regime**: none forced (storyline has no effective-date rule change; not invented).
- **Boundary records (A17)**: later-added ENG-2440 (in only under the v3 cut-off); ENG-2438 (Feb 10, after the overview deck's count); Acceptable-Behavior ENG-1411/1877; Bug-labelled ART-695/696, EPI-25 (other teams); folded children; stale shorter list (deck "19 open bugs").

## 3 Hidden authorities

| Id | Name used by the hub | Home | Decoy (service) | Governs | Findability proof |
|---|---|---|---|---|---|
| H1 | "Sunset's intake list" (forwarded by Leonard) | **Gmail** thread `arthur.blake@harmonygames.co/1856963042345149306` (fwd + later follow-up) | Confluence `page_ip_sale_data_room` "IP Sale – Data Room Checklist (draft)": engineering item = Linear "Bugs" column only, by priority, no fix evidence | R1 membership, R4 fix status | Gmail search "intake" / "Sunset" in Arthur's mailbox → only seeded hits after Feb 9 (term new, see dossier 1.D) |
| H2 | "the disclosure tiers you put on the founders board" | **Trello** card `698e64e34d281ad67c9017c8` "IP sale – defect disclosure tiers" (desc + 2 comments) | Slack `#god-bugs` 1760971822.613049 (Vincent, Oct 2025): 3-level launch triage scale, no-priority skipped, no regression bump | R3 tier | `trello_search "disclosure tiers"` → the card (term absent from base) |
| H3 | "the data room index" | **Sheets** `f_5a83f7de3271d0ddcb28b5` "HG – IP Sale Data Room Index" | Drive folder `d_bfe053a06cf4d6f1021a98` "Data Room (Jan board prep)" / `d_2f55ba7fcbe116ce345503` "Engineering" | R6 destination + file/tab names, R7 recipients + redaction | `gsheets_search_spreadsheets "Data Room Index"` → the sheet |
| H4 | "Sunset's cut-off (on the calendar)" | **GCal** event copies `evt_0565966dd887050bd9824d` (L) / `evt_dc8a6f6d61d9d99f8d5545` (A) / `evt_977e7982179ff398fb2715` (R), current time Mon Feb 16 17:00Z | Gmail: Sunset's stated "Fri 12:00 PT" (in H1) and the original invitation email (Fri 10:00 PT) | R8 cut-off date (membership boundary + file-name date) | `gcal_search_events "intake cut-off"` → the event |

`governs` sets are disjoint. Each run that misses one authority still scores the others (failure diversity).

## 4 Delegation lattice

- **Anchor A1** — Leonard's `#winddown` thread parent (ts 1770938731.204119, Feb 12 23:25Z). Plain-language handle: the defect schedule Leonard asked Arthur for in the wind-down channel.
- **Hub** = A1 itself (Leonard's voice) — explicitly delegates to: Sunset's forwarded intake list; Arthur's tiers on the founders' board; the data-room index for filing/notify; the asset schedule doc for lots; the overview deck's placeholder count; the Linear ticket he opened; the old Confluence checklist (flag disagreements); reply in the thread with totals; the cut-off on the calendar.

| Frag | Service · container | Kind | Carries | Chain |
|---|---|---|---|---|
| K1 | slack · `C0ADGSZKR3R` hub thread | delegation | the asks + pointers | A1 |
| K2 | gmail · fwd thread (msg 1, Feb 12 23:12Z) | requirement | cohort rule, row fields, fold rule, fix-status definition + vocabulary, "send to me (Sunset) directly" | A1→K2 |
| K3 | gmail · same thread (msg 2, Feb 13 15:41Z) | amendment | WebGL-labelled defects on a separate "Not in lot – Web" list, not in lot totals | A1→K2→K3 |
| K4 | trello · card desc | requirement | tier rules + order of application | A1→K4 |
| K5 | trello · card comments (Robert, then Arthur accepts) | amendment | Hot-Fix clause only for Urgent/High | A1→K4→K5 |
| K6 | gsheets · Index tab row "Known defects schedule" | destination/format | folder, file name with cut-off date, tab names | A1→K6 |
| K7 | gsheets · Notes tab | recipient | notify Sunset onboarding contact + cc Leonard; no player ids/emails; link not attachment | A1→K6→K7 |
| K8 | gcal · cut-off event | requirement | cut-off moved to Mon Feb 16 09:00 PT | A1→K8 |
| K9 | contacts · `cnt_f984dad17a47` | recipient | Sunset onboarding contact's role + email | A1→K6→K7→K9 |
| K10 | linear · ENG-2439 | destination (reuse) | the tracking ticket to update | A1→K10 |
| K11 | gslides · deck slide 5 (index 4) | requirement | placeholder count to replace | A1→K11 |
| K12 | gdocs · asset schedule doc | requirement | lot = Linear team; repos per lot (fix-evidence scope); web build not in any lot | A1→K12 |
| K13 | confluence · decoy page | requirement (conflict to report) | the old checklist whose definition disagrees | A1→K13 |

Amendments in other services/later: K3 (later Gmail message), K5 (later Trello comments), K8 (GCal update vs Gmail/Sunset times).
Non-authoritative instruction distractors: `#god-bugs` triage scale (K-none); Leonard's DM "leave them fixed" claim (a claim, not an instruction); Drive "Data Room (Jan board prep)"; the overview deck count.
Incorporation: every fragment chains to A1 through an explicit pointer in the hub or in the fragment it amends (manifest `incorporated_via`).

## 5 Chains and trap register

Chains (distinct root causes):
- **C1 wrong summary + thread past apparent end (A1/S1/A14)** — Slack DM parent (Leonard, Feb 13 01:15Z: Oliver says the sign-in/account-sync bugs were fixed before Christmas) → Arthur's reply accepting (01:20Z, apparent conclusion) → Linear: ENG-2280 group + ENG-2363 still open → GitHub: no PR references them → Leonard's later reply (15:04Z) retracting. Ends in R4 = NO FIX for ENG-2280 row (with 2073/2114/2281) and ENG-2363.
- **C2 fix claim vs later reproduction (A9, cross-service, persona's own claim)** — GitHub backend#79 comment by Arthur (2025-12-04) "clamps lives at 0 … ENG-2277, ENG-2400" → Slack DM Feb 11 Leonard: "minus-lives bug (2277) is back on 309 … thought you clamped that in the admin endpoints PR" → Linear ENG-2277/2400 open. Ends in R4: ENG-2277 = FIX MERGED – REPRODUCED; ENG-2400 = FIX MERGED – UNVERIFIED.
- **C3 hidden house rule + partial amendment (A12/A15/S13)** — hub → Trello desc → Trello comments → Linear priority/state/labels on 67 rows. Ends in R3 tiers and R5 totals (ZOM-614 T3 not T1; ZOM-616 T2 not T1).
- **C4 scope amendment in a later email (A7/A14 Gmail)** — Gmail msg 1 → Gmail msg 2 → Linear WebGL label → Docs (web build not in a lot). Ends in R2 (ENG-2406/2407/2408 off lot totals).
- **C5 three-version cut-off (S9/A13)** — Sunset's "Fri 12:00 PT" (Gmail) → invitation "Fri 12pm PST" (Gmail) → GCal event moved to Mon 09:00 PT on 2026-02-13 16:05Z with no update email (calendar only). Ends in R8 (ENG-2440 in; file-name date 2026-02-16).
- **C6 stale shorter list (A17/D4)** — Slides "19 open bugs (DD 13 / ZM 6)" → Linear enumeration → schedule totals → slide correction write.

Trap register (family · records · requirement · wrong reading · resolver · discovery order):

| Id | Family | Records | Req | Expected wrong reading | Resolver | Why met first |
|---|---|---|---|---|---|---|
| T1 | stale_summary | DM `D04UGG61DUM` 1770945318.402219 + Arthur reply | R4 | sign-in rows marked fixed / dropped | rule = merged PR reference; Leonard's later reply | parent + "ok" reply look final; correction 14 h later in the same thread |
| T2 | superseding (2 versions) | DM reply 1770995043.286609 | R4 | — | later reply retracts | replies need `read_thread` |
| T3 | superseding (3 versions, cross-service) | H1 msg 1, invitation mail, GCal event | R8 | cut-off Fri; ENG-2440 dropped; file dated 2026-02-13 | GCal current event | Gmail is read before the calendar; the event moved after the invitation |
| T4 | superseding (cross-service) | backend#79#c_2 (Dec 4) → DM 1770779432.118409 (Feb 11) | R4 | ENG-2277 "fix merged, unverified" | later written reproduction | the PR comment is the code-history evidence the rule points at |
| T5 | superseding (Trello) | card comments 698ef91c…, 698eff87… | R3 | Hot-Fix → T1 for every hot-fix ticket | amendment accepted by Arthur | desc read first; comments separate call |
| T6 | superseding (Gmail reply) | H1 msg 2 | R2 | WebGL tickets counted in Lot A | later message in the thread | 41/60 Gmail runs never open threads |
| T7 | distractor · stale_summary | `#god-bugs` 1760971822.613049 | R3 | 3-level scale, no-priority skipped | H2 card | Slack search "triage"/"severity" hits it first |
| T8 | distractor · near_duplicate_record | `page_ip_sale_data_room` | R1 | "Bugs column only" (drops Regression/Bug-labelled Todo/Backlog) | H1 | Confluence search "data room" |
| T9 | distractor · partial_listing | deck `f_fe90457cba7d7620b0b39b` slide 5 | R5 | totals 19 / 13 / 6 | Linear enumeration | deck found by "IP sale" search; looks authoritative |
| T10 | distractor · scope_adjacent | ART-695, ART-696, EPI-25 (base) | R1 | DD art bugs included in Lot A | rule: ENG/ZOM teams only | label-filtered `Bug` list returns them |
| T11 | distractor · lookalike_entity | `d_bfe053a06cf4d6f1021a98`, `d_2f55ba7fcbe116ce345503` | R6 | file filed in "Data Room (Jan board prep)/Engineering" | H3 folder | Drive search "data room" returns both |
| T12 | distractor · lookalike_entity | `cnt_e56c834094c1` (Sunset CEO) | R7 | email to the CEO | H3 role + K9 | contacts search "Sunset" returns 2 |
| T13 | exact_predicate | ENG-1411, ENG-1877 (base) | R1 | AB tickets listed | H1 exclusion | carry the Bug label |
| T14 | reuse_exclusion | ENG-2439 | R9 | new Linear ticket created | hub points at Leonard's ticket | title differs from "defect schedule" |
| T15 | tool_surface | backend#79#c_2 | R4 | ENG-2277/2400 = NO FIX (title/branch search misses the comment) | comment read via DM pointer | reference only in a conversation comment |
| T16 | cross_reference_gap | GoD#1583/#1773/#1882, match3d#522/#529/#539/#543 (base) | R4 | fix status from Linear state alone | PR search by id (no link field) | Linear `links` empty |
| T17 | conclusion_stop | ENG-2280 children ENG-2073/2114/2281; ENG-2128 children ENG-2110/2130/2242 | R5 | 73 rows instead of 67; child tiers counted | H1 fold rule | flat list from `list_issues` |
| T18 | effective_date | ENG-2440 (created 2026-02-13T20:31Z) | R8 | excluded | v3 cut-off | created after Fri cut-off versions |

## 6 Failure-diversity plan

| Discovery missed | Requirements hit | Plausible share of runs |
|---|---|---|
| H1 Gmail never opened → Confluence decoy used | R1 (misses 30+ Bug-labelled Backlog/Todo rows), R4 vocabulary | high (Gmail 60/131) |
| H1 follow-up not read | R2 (Web line), R5 Lot A totals | medium |
| H2 Trello never opened → Linear priority or Slack scale | R3, R5 | high (Trello 50/131) |
| Trello comments not read | R3 for ZOM-614/616, Lot B totals | medium |
| H3 Sheet not opened → Jan folder / own naming | R6, R7 | medium |
| GCal not opened | R8 (ENG-2440, file-name date) | high (Calendar 5/131) |
| DM thread not opened past Arthur's reply | R4 for 2 rows | medium (67/124 skip replies) |
| backend#79 comment not found | R4 for ENG-2277/2400 | medium |
No single discovery gates more than 3 of the 11 requirements.

## 7 Deliverables and dependent writes

Register: one Google Sheet, tabs "Lot A – Domino Delights", "Lot B – Zombie Match 3D", "Not in lot – Web"; one row per (folded) defect: id(s), title, tier, fix status; exact totals per lot × tier.

| W | Service · tool | Depends on |
|---|---|---|
| W1 | gsheets · create_spreadsheet + values_update | R1–R5, R6, R8 (C1–C6) |
| W2 | gdrive · move_file into `04 Technical` | R6 (H3) |
| W3 | gmail · send_message to Sunset onboarding contact, cc Leonard, link only | R5, R7, R8 |
| W4 | linear · update_issue ENG-2439 (reuse) | R5, R9 |
| W5 | gslides · batch_update slide 5 text | R5, R10 |
| W6 | slack · send_message in the hub thread (totals + Confluence disagreement) | R5, R11, R12 |

## 8 Service role map

| Service | Role | Load-bearing fact / write | Carrier |
|---|---|---|---|
| Slack | hub; wrong summary + retraction; reproduction report; decoy scale | A1 delegations; C1; C2 report; W6 | ● message text / thread replies |
| Gmail | H1 rules + amendment; cut-off v1/v2; W3 | cohort rule, fix vocabulary, Web line | ● body + later message |
| GCal | H4 cut-off (current time) | R8 | ● start/end, sequence, updated |
| Drive | destination folders + decoy folder; W2 | R6 | ● name, parents, sharing |
| Docs | lot ↔ team ↔ repos; web build not in a lot | R2, fix-evidence repo scope | ● body_text |
| Sheets | H3 index; W1 target | R6, R7 | ● grid_json |
| Slides | stale count to correct; W5 | R10 | ● element text |
| Contacts | Sunset onboarding contact vs CEO | R7 | ● job, email |
| GitHub | fix evidence (titles, branches, comment on backend#79) | R4 | ● PR title/branch/body, ● PR comments |
| Linear | cohort; reuse ticket; seeded defects | R1, R3, R9 | ● state/priority/labels/parent/description |
| Trello | H2 tiers + amendment | R3 | ● card desc, ● commentCard |
| Confluence | decoy checklist whose disagreement must be reported | R12 | ● page body |
| Snowflake | none (not used; no load-bearing role found without touching incoherent rows) | — | — |

12 of 13 services carry weight; Snowflake deliberately unused.

## 9 Call budget (phase × service) — honest

| Phase | Service | Calls | Reason |
|---|---|---|---|
| discovery | slack | 22 | find hub, read `#winddown` window, DMs, decoy hits |
| discovery | gmail | 10 | find forwarded intake, invitations |
| discovery | trello | 6 | board/card search, board lists |
| discovery | gsheets | 4 | find index, tabs |
| discovery | gcal | 4 | find cut-off event |
| discovery | gdocs | 3 | find asset schedule |
| discovery | gslides | 3 | find overview deck |
| discovery | confluence | 5 | search, page, history |
| discovery | gdrive | 6 | folder tree, decoy folder |
| discovery | contacts | 3 | Sunset contacts |
| rules | gmail | 3 | intake thread messages |
| rules | trello | 3 | card, comments, actions |
| rules | gsheets | 2 | Index + Notes tabs |
| rules | gdocs | 1 | asset schedule body |
| enumeration | linear | 14 | ENG/ZOM open issues across states, paged (≈283 open → ~6 pages × filters) |
| per-record | linear | 75 | get_issue per candidate (sub-issue parent, labels) |
| per-record | github | 75 | PR search per ticket id (no link field) |
| per-record | github | 18 | comments/timeline for each candidate fix PR |
| per-record | slack | 20 | reproduction checks for FIX MERGED rows + DM threads |
| reconciliation | slack | 6 | DM threads (C1, C2) |
| reconciliation | gmail | 3 | invitation + updated invitation |
| reconciliation | gcal | 2 | event detail |
| reconciliation | linear | 4 | parents ENG-2280/2128, ENG-2438/2440 |
| reconciliation | github | 4 | backend#79 detail |
| reads-before-writes | gdrive | 3 | `04 Technical` id |
| reads-before-writes | linear | 2 | ENG-2439 |
| reads-before-writes | gslides | 2 | slide/element ids |
| reads-before-writes | slack | 2 | hub thread ts |
| writes | gsheets | 6 | create + 3 tab writes + 2 read-back |
| writes | gdrive | 2 | move + read-back |
| writes | gmail | 2 | send + read-back |
| writes | linear | 2 | update + read-back |
| writes | gslides | 2 | update + read-back |
| writes | slack | 2 | post + read-back |
| **Total** | 12 services | **321** | largest share github 97/321 = 30% |

Golden-run rule: a correct run needs the per-ticket fix-evidence lookups (GitHub) but bulk PR listings can replace most of them (§2 shortcut audit). Expected golden run ≈ 250–320 → inside Long Horizon (100–500+). **Below the extreme profile's 600; the design gate fails `call_budget` (321) and `per_record_calls` (75 × 3 = 225 < 250). Not inflated — see engine feedback.**

## 10 QC rails

Two-reading tests:

| Decision point | Best reading | Strongest alternative | Resolved by |
|---|---|---|---|
| Cohort definition | Sunset's list (H1) | Confluence checklist | hub names Sunset's list as governing; Confluence only to be compared |
| Sign-in rows status | NO FIX | "fixed" (Leonard/Oliver claim) | rule = merged PR reference; Leonard's later retraction |
| ENG-2400 status | FIX MERGED – UNVERIFIED | REPRODUCED | Leonard's report names 2277 only |
| ZOM-614 tier | T3 | T1 (Hot-Fix) | Trello amendment accepted by the rule owner |
| Cut-off | Mon Feb 16 09:00 PT | Fri Feb 13 (two versions) | current calendar event (later) |
| WebGL tickets | separate list, not in lot totals | Lot A | Sunset follow-up message (later) |
| Destination | IP Sale Data Room / 04 Technical | Data Room (Jan board prep)/Engineering | index sheet |
| Recipient | Sunset onboarding contact, cc Leonard | Sunset CEO / reply to Leonard's forward | index Notes + contact job |
| Tracking | update ENG-2439 | new ticket | hub |

Reach table (scoped records): Slack — Arthur ∈ `#winddown`, `D04UGG61DUM`, `#god-bugs`; Gmail — Arthur copies `user_email = arthur.blake@harmonygames.co`; GCal — Arthur's copy `evt_dc8a6f6d61d9d99f8d5545` with `self:true`; Drive/Docs/Sheets/Slides — owner Leonard (or Robert for the decoy folder), `shared_with_emails_json` includes Arthur. Unscoped: Linear, GitHub, Trello, Contacts, Confluence (pointer: hub names "my old confluence checklist").

Feasibility: writes exist in `Evals/references/tools/catalog.json` — `gsheets_create_spreadsheet`, `gsheets_values_update`, `gdrive_move_file`, `gmail_send_message`, `linear_update_issue`, `gslides_batch_update`, `slack_send_message` (verify in dossier). All values observable from structured fields.

Precedence: every load-bearing fact is in a ● carrier (message text, thread reply, email body, card desc/comment, grid, element text, body_text, PR comment, issue fields). No GCal description, Slides notes, Linear comments or Drive `content_text` carry anything.

Prompt naturalness (constraints for the human, not text): the trigger names the anchor (Leonard's ask in the wind-down channel) and the deliverable kinds; it must not name Gmail/Trello/Sheets/Calendar locations, ticket ids, the tier rule, the cut-off date, the fold rule, the Web line, or the correct totals.

Grading devices (for the human's plan later): exact per-lot × tier totals; row count 67 (39/25/3); spot checks ≤ 5 per group (ENG-2280 fold, ENG-2277 vs ENG-2400, ZOM-614, ZOM-616, ENG-2440); one criterion per write/recipient.

## 11 Record plan for /create-injection

| Service | Records | Notes |
|---|---|---|
| slack | INSERT hub parent + Arthur reply (`C0ADGSZKR3R`); DM lives report; DM claim parent + 2 replies (`D04UGG61DUM`); `#god-bugs` decoy (Oct 2025). UPDATE 2 parents' reply counters | ids = sha256(channel|ts)[:32]; `thread_parent_id` encoding [U] |
| gmail | threads: fwd intake (Arthur INBOX + Leonard SENT; 2 messages each), invitation, updated invitation (Arthur) | ids prefixed per mailbox; `to_json`/`cc_json` shape [U] |
| gcal | 3 event copies (L organizer/self, A self, R self), sequence 1, updated Feb 13 | shared ical_uid |
| gdrive | 6 data-room folders, 2 decoy folders, 3 native files | owner Leonard / Robert; Arthur shared |
| gdocs / gsheets / gslides | asset schedule doc; index sheet (2 tabs); overview deck (4 slides) | ids equal drive ids |
| contacts | 2 Sunset contacts | `PERSON_9823`, `PERSON_1674` |
| github | backend#79 comment c_2 + timeline ev_6; UPDATE PR updated_at | |
| linear | ENG-2438, ENG-2439, ENG-2440 | `links_json` `[]` |
| trello | card + createCard + 2 commentCard; UPDATE board dateLastActivity | ids from epoch |
| confluence | decoy page v1 + version + label | re-verify after regeneration |

## 12 Self-test results

- Gate (`--design`) on the draft manifest: **FAIL on 2 of 26 checks** — `per_record_calls` 225 < 250 and `call_budget` 321 < 600; all other checks ok (12 services carrying weight, 13 fragments / 10 services / 11 containers, cohort 75 × 3 surfaces, 4 authorities non-overlapping, 6 chains, 18 traps / 9 families / 9 requirements, 6 supersessions (4 cross-service, 1 × 3 versions), 6 distractors / 5 types, 6 writes / 6 services). The two failures are recorded, not worked around: the honest per-record floor of a Linear-defect cohort is ~1.6 calls (bulk list paths exist), and the only measured ≥ 5-calls/record surface (GitHub PR cohorts) is the calibration cohort type the originality rule excludes.
- Lazy-solver pass (one broad search per service, first hits, no threads, bulk shortcuts, stop at first conclusion):
  - Slack "defect schedule" → hub (first link findable ✓). Lazy run reads hub only → misses H1 location (Gmail "forwarded you") unless it searches Gmail; with Confluence first hit → T8. Leak check: the hub must NOT restate any rule clause (cohort predicate, tiers, cut-off time, Web line) → it only names the sources. Constraint carried into the SQL text and re-checked in the dossier lazy-solver pass.
  - Linear `list_issues label:Bug` + `state:Bugs` gives most of the cohort in bulk — a lazy solver scores membership partly (leak accepted: volume, not difficulty; difficulty is in exclusions/fold/web/cut-off).
  - Trello not opened → tiers from Linear priority: scores T for ~55/67 rows where priority alone equals the house tier (leak: tiers coincide for plain-priority rows). Mitigation: totals graded per lot × tier, which differ (No-priority→T3, Regression bump, Hot-Fix amended).
  - GitHub search "ENG-2277" misses the comment-only reference → T15 holds.
  - Gmail first hit "Sunset" → forward msg 1; not opening the thread misses msg 2 (WebGL) ✓.
  - Calendar never opened → Fri cut-off; ENG-2440 dropped ✓.
- Red team: optional `redteam_review.py` not run (instructed not to).


## Implementation deltas (recorded by /create-injection; the manifest is final)

- **Cut-off**: the invitation is from Sunset (organizer `PERSON_9823_EMAIL`) at Fri 12:00 PT, same as Sunset's email; the event was moved to Mon Feb 16 09:00 PT at 2026-02-13 16:05Z. Two defects found in self-review and fixed: (1) "Updated invitation" emails put "Mon Feb 16" in a Gmail subject line, collapsing the calendar-only trap — removed (organizer updated without notifying); (2) the move was first timed at 14:05Z, before Sunset's 15:20Z follow-up that says "everything else in my earlier note stands" (which would re-assert Friday) — moved to 16:05Z.
- **C7 (new chain)**: fix evidence that exists only in PR conversation comments — match3d#316 (ZOM-359), #520 (ZOM-608), #528 (ZOM-610), #527 (ZOM-611, partial), GameOfDominoes#1912 (ENG-2345, partial), backend#79 (ENG-2277/2400, server side only). Each comment is worded so the ticket's current Linear state stays consistent (Regression after fix; In Validation after fix; In Progress with an explicitly partial fix; Bugs with a server-side-only fix). Slack pointers in `#zombie-bugs` / `#god-bugs` and written reproductions (ZOM-359, ZOM-608) make the hops findable if PR search does not index comments.
- **New traps**: T19 near-miss mentions (5 merged-PR comments that mention a cohort id without fixing it), T20 already-filed PDFs + Leonard's Friday review block carrying the old date, T21 January bug export CSV in the decoy folder, T22 Oliver links the fix/login PR (GameOfDominoes#1876, no ticket id) to the splash hang.
- **Rows**: 120 (111 INSERT + 9 UPDATE) — reached only by adding records that strengthen existing mechanisms (comment-only references, near-misses, mailbox/calendar copies, stale-dated artefacts). No orphan rows.
- **Budget**: unchanged at 321 (honest). The comment-only references make the per-ticket GitHub lookup genuinely necessary (list endpoints never return comments) but do not lift the total to 600.
- **Final checks**: `sql_lint.py` 11 errors (all composite-key false positives on multi-tab sheets / multi-slide decks), 14 warnings dispositioned in the dossier; `hardness_gate.py` FAIL on `sql_lint_clean`, `per_record_calls` (225) and `call_budget` (321); 23 other checks ok.


## 13 · Iteration 2 — per-record retest trail (supersedes the iteration-1 numbers in §2, §9, §12)

**Why.** Iteration 1's cohort gave ~1.6 honest calls per record (bulk list paths). `Hardness_Mastery.md` §2.5: seed per-record evidence into no-bulk surfaces, decisive for an unpredictable subset, neutral on the rest, nothing upstream telling which records flip.

**What the storyline gains (coherent at the clock).**
- Arthur (persona) sets up a pre-sale retest right after Leonard's hub: private channel `#presale-retest` `C0AE7RTQ2LK` (created 2026-02-12 23:55:12Z; members Arthur, Leonard, Robert, Oliver), kickoff ts 1770940961.204551. The kickoff says only who tests which platform and where results go; it does not restate any rule.
- **iOS (Oliver)**: one thread per ticket in `#presale-retest` (parent = "<id> <title> · iOS", result only in the reply), 2026-02-13 10:02Z–18:05Z. 69 threads (67 cohort tickets + the 2 Acceptable Behavior tickets).
- **Android (Robert)**: one or two Linear comments per ticket, 2026-02-13 12:30Z–21:10Z. 65 tickets (63 cohort + 2 AB); 4 tickets have no Android comment. Linear comments have **no base precedent** — blocking [U] item for the Opus pre-check.
- Testers worked from "open ENG/ZOM tickets with label Bug or state Bugs", minus WebGL. So ENG-1866 and ZOM-542 (Regression, no Bug label), ENG-2406/2407/2408 and ENG-2440 (created later) have no retest. The channel list is therefore a *partial listing*, not the cohort.
- **Sunset rule 7** (added to H1 message 1): NOT REPRODUCED needs a retest on both iOS and Android that could not make the defect happen. An unfinished retest, or a one-platform retest, stays REPRODUCES. NOT REPRODUCED rows stay listed but leave the totals; a folded row is NOT REPRODUCED only if every member is. Rule 5 totals now point at rule 7.
- Existing fix-status rule: a retest that still shows the defect after a fix merge is a written report → REPRODUCED. An unfinished retest is not a report.

**Outcome design (necessity rule).** Of 67 cohort tickets retested, these flip something:
- 14 both-platform "could not make it happen" → 13 rows leave the totals. The 14th, ENG-2130, is a folded child whose parent still reproduces, so its row stays in.
- 11 one-platform-only results (still count). An iOS-only reader wrongly drops 11 rows: ENG-1762, ENG-1839, ENG-2190, ENG-2274, ENG-2402, ZOM-458, ZOM-517, ZOM-535, ZOM-559, ZOM-616, ZOM-667.
- 6 unfinished retests (still count).
- 4 tickets without an Android comment (still count).
- 4 in-thread/in-comment corrections (first "can't get it", then "got it on the third try").
- 2 fix-status flips (ENG-2345, ZOM-611 UNVERIFIED → REPRODUCED).
- 1 subtle non-flip: ENG-2400's retest is unfinished on both platforms → it stays UNVERIFIED and still counts.

The other 28 tickets carry plain confirming notes on both platforms. Reply wording varies, never contains the ticket id, the word "repro", or a build number.

**New per-record surfaces (manifest `evidence_surfaces`).**

| Surface | Tool | Records | Calls/record |
|---|---|---|---|
| iOS retest reply | `slack_conversations_replies` | 67 | 1 |
| Android retest comments | `linear_list_comments` [U] | 63 | 1 |
| PR review comments of PR hits | `github_get_pull_request_reviews` | 18 | 1 |
| (kept) Slack id search, PR search, PR comments, PR merge time, report threads, `linear_get_issue` | — | 75 / 75 / 18 / 13 / 13 / 75 | 1 each |
| **Σ** | | | **417** (gate ≥ 300) |

**Budget (necessary, every row reasoned in the manifest).** 551 calls.

| Service | Calls | Share |
|---|---|---|
| slack | 188 | 34% |
| linear | 160 | 29% |
| github | 128 | 23% |
| gmail | 18 | — |
| gsheets | 12 | — |
| gdrive | 11 | — |
| trello | 9 | — |
| gslides | 7 | — |
| gcal | 6 | — |
| confluence | 5 | — |
| gdocs | 4 | — |
| contacts | 3 | — |

The Android half was put on Linear because an all-Slack retest made Slack 47% of the budget (cap 35%). Two per-ticket lines are counted at 1.0 because the cheaper path depends on an unverified tool behaviour:
- `linear_get_issue` (does the list return `parent`?).
- Slack id search (does PR search index PR comments?).

If the pre-check shows either bulk behaviour, the honest total drops by up to ~140 calls.

**New requirement / traps / chain.**
- R13 current-build status; H1 governs R1, R4, R13.
- C8: two-platform retest with house rules.
- T23 branch named after a ticket, no merged PR (ENG-2149, ENG-2363 — base branches).
- T24 the retest list used as the cohort.
- T25 iOS-only reading.
- T26 in-thread correction, with `version_records`.
- T27 an unfinished retest treated as "not reproduced".
- T28 an unfinished retest treated as a written report (ENG-2400).
- All superseding/effective-date traps now carry `version_records`; every authority has a decoy record.

**Ground truth (iteration 2).**
- Rows: 67 (Lot A 39, Lot B 25, Web 3); 13 NOT REPRODUCED (Lot A 7, Lot B 6).
- Totals over rows that still reproduce: Lot A T1 10 · T2 2 · T3 10 · T4 10; Lot B 11 · 4 · 3 · 1.

| Variant | Lot A | Lot B |
|---|---|---|
| Without the retest | 10/2/12/15 | 14/4/6/1 |
| Without the Trello amendment | — | 12/3/3/1 |
| Friday cut-off | T2 = 1 | — |

**Self-test.**
- Gates: design PASS, SQL PASS. `sql_lint`: 0 errors, 14 warnings, the same three dispositioned kinds.
- Literal sweep: "2026-02-16" appears only on the three calendar copies; the file name with a date appears nowhere; "reproduce" appears in no reply.
- "Rest stands": no later record re-asserts an amended clause.
- Search-surfacing risk: "happen" occurs in ~25–30 % of replies, both kinds. A filtered Slack search could surface a mixed subset of iOS results [U], never a complete list.


## 14 · Iteration 3 — Red-team hardening (supersedes §13 where they differ)

### What changed in the records
- **Hub** (`#winddown` 1770938731.204119) now names sources by issuer or purpose, not location: "sunset's intake list", "your severity tiers", "my data room sheet", "my asset schedule", "sunset's invite". It also states:
  - "cut-off - whatever sunset's invite says when you send, they keep moving it" (precedence);
  - "send it as soon as its done, dont wait for the cut-off" (act now);
  - the slide end state ("per-lot totals by tier you send sunset");
  - "update [the linear ticket] the way it says".
  - The words "placeholder" and "old" are gone.
- **Sunset intake (H1 msg 1)** — rules rewritten:
  - per-row columns: id(s), title, tier, fix status, iOS result, Android result, current-build status;
  - latest-merge rule for multiple fixes;
  - REPRODUCED = in Regression now or a written report after the latest merge;
  - retest values still happens / could not make it happen / could not finish / not retested; another build = not retested;
  - NOT REPRODUCED needs both platforms;
  - totals count REPRODUCES rows only;
  - snapshot = tracker at send time; tickets after the cut-off go to the bring-down;
  - grouping delegated to "the way your team normally presents them".
- **Trello card (H2)** renamed "IP sale - severity tiers" and moved to 2026-02-12 22:20:47Z, before the hub; ids re-minted and collision-checked. It now also carries the row rules:
  - a sub-issue goes in its parent's row;
  - the row takes the most severe tier and the **parent's fix status**;
  - each ticket's retest results show in the row;
  - the row is NOT REPRODUCED only if every member is.
- **Retest trail re-homed.** The dedicated channel is gone.
  - Arthur's kickoff in `#god-bugs` (1770940961.204551) names the builds (DD 0.3.309, ZM 0.3.157, store builds) and where each platform's results go.
  - Oliver's iOS threads sit in `#god-bugs` (DD) and `#zombie-bugs` (ZM), interleaved with base traffic.
  - Robert's Android results are Linear comments.
  - ENG-1854's iOS retest ran on TestFlight 0.3.307, so it counts as not retested.
- **Conclusions removed.** Leonard's retraction now says only "what he fixed before xmas was the splash screen hang. dunno about the rest". Oliver's DM no longer says anything about account sync.
- **New evidence:**
  - GameOfDominoes#1832#c_1: a partial fix for ENG-2242, a folded child of ENG-2128; the row keeps the parent's NO FIX.
  - ZOM-611 report in `#zombie-bugs` (2025-10-21) between two merged fixes: match3d#527#c_3 (Oct 18) and match3d#542#c_3 (Oct 24). Its Feb 13 retest is negative on both platforms, so ZOM-611 is UNVERIFIED and NOT REPRODUCED under the latest-merge rule, and REPRODUCED under an "any merge" reading.
- **Decoys de-labelled:**
  - deck/doc/Confluence titles lose "(draft)";
  - the Confluence page now speaks of Sunset intake items;
  - the January folder becomes Robert's same-named `IP Sale Data Room / Technical` (created Feb 12);
  - the January CSV is deleted.
- **Writes made feasible:**
  - `04 Technical` is created and owned by Arthur (23:45Z);
  - Leonard's folder and deck carry `shared_roles_json` writer entries for Arthur and Robert ([U] shape; sandbox writes are not ACL-governed anyway);
  - the index Notes now authorise "share the file (not the folder) with Sunset's onboarding lead as viewer, then email the link, cc Leonard";
  - ENG-2439's description states the end state (link in description, move to In Review);
  - tabs: `gsheets_create_spreadsheet` creates one tab (`initialSheetTitle`), the other two need `gsheets_batch_update` addSheet ([U] request shape).

### Ground truth (iteration 3)
- 67 rows (Lot A 39, Lot B 25, Web 3).
- NOT REPRODUCED (12 rows):
  - Lot A: ENG-1853, ENG-1878, ENG-1928, ENG-2017, ENG-2181, ENG-2200;
  - Lot B: ZOM-237, ZOM-591, ZOM-598, ZOM-599, ZOM-610, ZOM-611, ZOM-614.
  - Note: ENG-1854 now counts (other build).
- Totals T1–T4: **Lot A 10/2/10/11 · Lot B 10/4/3/1**.
- Fix status:
  - Lot A: NO FIX 34, UNVERIFIED 1 (ENG-2400), REPRODUCED 4 (ENG-1866, 2277, 2331, 2345);
  - Lot B: NO FIX 18, UNVERIFIED 3 (ZOM-610, 611, 614), REPRODUCED 4 (ZOM-359, 542, 608, 616).

| Wrong reading | Lot A | Lot B | Other effect |
|---|---|---|---|
| Ignore the retest | 10/2/12/15 | 14/4/6/1 | — |
| Ignore the amendment | — | 11/3/3/1 | — |
| Friday cut-off | T2 = 1 | — | — |
| "Any merge" | — | — | ZOM-611 REPRODUCED |
| Child fix lifted to the row | — | — | ENG-2128 FIX MERGED |
| iOS-only reading | drops 11 more rows | | |

### Honest budget
386 calls. Conditional (`conditional_on`) rows:

| Calls | Surface | Unverified behaviour it depends on |
|---|---|---|
| 67 | iOS threads | a filtered Slack search could sweep replies |
| 73 | Android comments | `linear_show_data` might dump comments |
| 75 | `linear_get_issue` | the list may return parent |
| 75 | per-id PR search | a broad id-prefix search may sweep PR comments |

Total conditional: 290. **Floor 96** if all four resolve to bulk.

Removed as padding or bulk-replaceable (R1 §6):
- 18 review reads, 13 merge-detail reads (merge times come from the listing), 13 report-thread reads;
- 75 Slack id searches (kept 4 for the unresolved merged-fix tickets);
- repeated reconciliation, oversized discovery.

The engine target (≥ 500) is not met; nothing was padded to meet it.

### Red-team findings → disposition

| # | Finding | Disposition |
|---|---|---|
| 1.1 | Linear bulk enumeration/classification | **Accepted** (tiers/membership are bulk-derivable); `get_issue` marked conditional |
| 1.2–1.3 | PR searches replaceable by listing; either search implementation weakens the floor | **Fixed**: listing charged (28 pages); per-id search conditional; Slack id searches cut to 4 |
| 1.4 | Metadata sweep of the dedicated retest channel | **Mitigated**: trail re-homed to the bug channels with base traffic; iOS reads conditional — a `from:oliver after:` sweep still works if search returns replies |
| 1.5 | Android short-circuit (AND rule) | **Fixed**: per-platform columns in H1 rule 2/4; Android needed for all 73 cohort tickets (incl. absence) |
| 1.6 | Folded rows short-circuit | **Accepted** for current-build (one member suffices); fold now also tests fix aggregation (ENG-2242) |
| 1.7 | Retest settles R4 → report hunts unnecessary | **Fixed**: report search charged only for the 4 still-unresolved merged-fix tickets |
| 1.8 | Retest list as near-complete spine | **Accepted** (partial listing, merged into T1) |
| 1.9 | Authorities land directly via unique terms | **Fixed**: issuer/purpose naming; decoys share terms ("severity tiers", "IP Sale Data Room", "intake") |
| 1.10 | Complete containers in one fetch | **Accepted**; budget charges one fetch each |
| 1.11 | Recipient without Contacts | **Accepted**: Contacts demoted to alternate path (no weight); CEO lookalike merged into T13 |
| 1.12 | Seeded conclusions | **Fixed**: retraction and Oliver DM no longer state account-sync status |
| H1 breadth | H1 governs too much | **Fixed in part**: grouping/aggregation moved to H2 (R14); H1 still governs R1, R4, R13 |
| 2.x | Traps defeated by one rule | **Fixed**: traps merged; **14 independent** (T1–T14); 7 decoy entries kept with `independent: false, merged_into` |
| 3.1 | Clock/snapshot | **Fixed**: H1 rule 6 + hub "send as soon as its done" |
| 3.2 | Build identity | **Fixed**: kickoff names builds; other-build rule + ENG-1854 case |
| 3.3 | Multiple fixes | **Fixed**: latest-merge rule; ZOM-611 exercises it |
| 3.4 | Folded fix aggregation | **Fixed**: parent's status (H2); ENG-2242 exercises it |
| 3.5 | R13 representation | **Fixed**: per-platform + current-build columns required |
| 3.6 | Write end states | **Fixed**: ENG-2439 description; slide content in hub; tabs in index |
| 3.7 | Calendar precedence | **Fixed** in the hub ("whatever the invite says when you send") |
| 4.1 | No prompt supplied | **Accepted** (human-only artefact); constraint recorded for the human |
| 4.2–4.4 | Unstated mutation details; contextual remarks; broader sharing | **Fixed**: end states now in records; sharing scoped to file/viewer/onboarding lead |
| 5.1 | Linear comments unverified | **Open — blocking pre-check** |
| 5.2 | Slack thread encoding | **Open — pre-check** |
| 5.3 | Read ≠ write access | **Fixed**: Arthur owns 04 Technical; writer roles on folder/deck ([U] shape) |
| 5.4 | Sunset access to output | **Fixed**: authorised file share (W7) |
| 5.5 | Tab creation | **Mitigated**: create + `batch_update` addSheet; request shape [U] |
| 5.6 | Native-file sync | **Open — pre-check** |
| 5.7 | Reviews vs inline comments conflated | **Fixed**: review surface removed |
| 5.8 | Calendar/mail serialization | **Open — pre-check** |
| 5.9 | 23:25 vs 23:40 chronology | **Fixed**: card 22:20:47Z; all hub references postdate their targets |
| 6.x | Budget collapses | **Fixed** honestly: 386, floor 96 |
| 7.1 | Both platforms consequential | **Fixed** (per-platform columns) |
| 7.2 | Deterministic joins instead of conclusions | **Fixed**: latest-merge (ZOM-611), parent status (ENG-2242), build (ENG-1854), partial-scope comments |
| 7.3 | Same-purpose amendments without stale cues | **Partly**: decoys de-labelled; the Trello amendment interacts with Regression (ZOM-616 T2) |

## 15 · Iteration 4 — verified per-record surfaces, honest budget (supersedes §14 budget and surfaces)

Inputs settled by the coordinator (Ask_Carriers §6b): Slack search returns thread replies; `linear_list_issues` returns `parent_id`, relations, links, labels and description, never comments; `linear_list_comments` is per-issue with no bulk path and renders injected rows; PR search matches title, body and branch only, so conversation comments are reachable only per PR.

### What changed (records detail: Dossier §12)
- iOS results re-homed from Slack threads to Oliver's Linear comments; the Slack iOS trail is deleted. Both platforms now sit on the same verified per-issue surface, each an output column (rule 2/4).
- `get_issue` (75) and per-id PR search (75) rows removed: the list returns parents, and per-id search cannot see comments.
- Sunset rule 3 gains the buyers' code-review window: only PRs merged on or after 2025-10-13 count. This defines a second, source-defined linked cohort — the 73 lot-repo PRs merged in the window (GameOfDominoes 45, game-of-dominoes-backend 1, match3d 27, match3d-backend 0) — and a new independent trap T16 (ENG-1866 and ZOM-359 are Regression with fixes merged before the window → NO FIX).
- Comment-only fix evidence now has no shortcut. The Slack pointers to the fix PRs and the "admin endpoints PR" phrase are removed (they were R1 #1.2–1.3's bypass). All 13 PR comments are re-timed into the review window, with no `updated_at` bumps, so PR metadata no longer marks them. ENG-2242's partial fix moves to the in-window GameOfDominoes#1907.
- Kickoff text: each tester comments on the Linear ticket itself.

### Per-record surfaces (all verified, no `conditional_on`)

| Surface | Records | Decisive / consequential subset | Why nothing upstream tells which |
|---|---|---|---|
| `linear_list_comments` | 67 retested cohort tickets (6 untouched ones skippable via `updated_at`) | every call yields two output columns; 13 both-negative, 11 one-platform, 6 unfinished, 4 later corrections, 4 without Android | outcome per ticket is unpredictable; no bulk path |
| `github_get_pull_request_comments` | 73 in-window lot-repo PRs | 7 PRs carry the only reference to a cohort ticket; 5 more carry near-miss mentions (12/73 = 16%) | no Slack/Linear pointer names them; pre-merge timing like 865/884 base comments; 71/73 PRs already have base comments |
| `slack_conversations_search_messages` | 4 unresolved merged-fix tickets | ZOM-611 Oct 21 report must be dated against its latest merge | — |

### Honest budget (phase × service) — 190 calls, floor 190

| Phase | slack | gmail | trello | gsheets | gcal | gdocs | gslides | confluence | gdrive | linear | github | Σ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| discovery | 6 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | – | – | 24 |
| enumeration | – | – | – | – | – | – | – | – | – | 6 | 3 | 9 |
| per-record | 4 | – | – | – | – | – | – | – | – | 67 | 73 | 144 |
| writes | 1 | 1 | – | 5 | – | – | 1 | – | 2 | 1 | – | 11 |
| verification | – | – | – | 1 | – | – | – | – | 1 | – | – | 2 |
| **Σ** | 11 | 4 | 3 | 8 | 2 | 2 | 3 | 2 | 5 | 74 | 76 | **190** |

Shares: GitHub 40%, Linear 39%, everything else 21%.

### Why ≥ 500 is not reachable honestly with this storyline
- Only two verified per-record surfaces exist here: Linear comments (one call per issue) and PR conversation comments (one call per PR). Slack replies sweep. Confluence page comments are the only other per-record surface, and the universe has 31 pages.
- The Linear side is capped by the cohort: the ENG/ZOM open-defect population under H1 is 73 tickets, and 67 of them carry comments.
- Non-GitHub calls total 114. With the 45% cap, GitHub can carry at most about 90 calls (0.55·G ≤ 0.45·117 − 3), so the **honest maximum is ≈ 207**. That would need a window from about 2025-10-09 (~90 PRs); the 4-month window chosen gives 190.
- Widening the window only adds GitHub:

  | Window | PRs | Budget | GitHub share |
  |---|---|---|---|
  | 2025-10-07 | 97 | 214 | 47% |
  | 2025-09-16 | 150 | 267 | 57% |
  | 2025-08-06 | 220 | 337 | 66% |
  | 2025-05-12 | 457 | 574 | 80% |

- Adding recently closed defects to the cohort fails too:
  - PRs grow about 3× faster than closed defects (Jul 13 window: 99 closed defects vs 303 PRs).
  - Pre-sale retest comments on Done tickets would contradict their lifecycle.
  - A historical QA-comment layer in a base with zero Linear comments would be a cohort tell.

### Shape that would reach ≥ 500 within the cap
- With about 50 fixed calls (discovery, enumeration, writes, verification), L + G ≥ 450 with each ≤ 0.45·B. That means **≈ 225+ Linear issues and ≈ 225+ candidate PRs** (≈ 270 each for the ~600 headroom).
- Every issue must carry an output-visible per-issue comment fact, and every PR a comment that can be decisive, with no pointer, metadata or AND short-circuit.
- In this universe the PR side is available (a ~6-month window, about 2025-07-28, gives ~250 lot-repo PRs). The issue side is not. It needs either a different defect population of ~250 records (e.g. a storyline over all ENG/ZOM tickets touched in the window, not only open defects) or a third verified per-record surface.

### Red-team non-regression
- Every §14 "Fixed" disposition still holds: clock/snapshot, builds, latest-merge, parent aggregation, per-platform columns, write end states, access, tabs, chronology, issuer naming, no seeded conclusions.
- Rows that change:
  - 1.2–1.3 is now **fully fixed**: no Slack or DM pointer to a fix PR remains, and no PR metadata marks the commented PRs.
  - 1.4 is **fixed**: no retest trail is left on Slack.
  - 5.1 is **resolved**: Linear comments are verified.
  - 6.x is **honest at 190 with floor 190**.
