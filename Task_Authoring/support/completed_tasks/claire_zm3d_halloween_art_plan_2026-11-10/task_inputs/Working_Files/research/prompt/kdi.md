# Known-data-issue screen for the Halloween art ask

Scope: every card in `Task_Authoring/references/known_data_issues/synthcut.md`
(SC-1 – SC-73, 73 cards, Oct 1 2025 universe) and the requested entries from
`Task_Authoring/references/universe_kb/trap_catalog.json`
(N01–N03, D01–D08, P01/P02, K02, plus P03 because it is the same hazard).

The task under test: Leonard's ask `C06DJBJL798/1759269913.882683` — Claire writes
a plan doc and a tracker, comments each ad's ART ticket (ART-793 … ART-854) with
its Halloween call and due date, assigns ads that need new work to Marcus Bennett
(`usr_c77c50cc15c5342d`) or Martin Walsh (`usr_51f5f16d46e8cf55`), opens two new
ART tickets (Halloween icon, Halloween iPad set), and replies in the thread with
the links before Thu Oct 2. **No spend figure, no founder status, no timezone, no
payroll, no install number is asked anywhere.** That last sentence is what moves
most of the 73 cards to "not applicable" — and it has to stay true through
revision, because the fastest way to break this task is to add one spend column.

Verdict up front: **8 cards constrain the read/write path** (SC-7, SC-16, SC-22,
SC-26, SC-30, SC-32, SC-36, SC-70), **2 more are identity-adjacent and must stay
ungraded** (SC-49, SC-54), and **9 traps from the trap catalog apply** (N01, N02,
D01, D04, D05, P01, P02, P03, K02).

---

## A. Cards that constrain this task

| Card | Title | "Don't grade" (verbatim) | Touches this task? |
|---|---|---|---|
| **SC-16** | Linear tickets still open after work shipped | **"Linear status as proof of whether work shipped (ZOM-564, ZOM-513/514, ZOM-563, ART-790/792)."** | **Yes — the central one.** The 58 serving creatives are catalogued by ART-793 … ART-854 tickets that sit `Todo`, unassigned (design §"Seeded ART library tickets"). The ticket state is *not* evidence a creative is live, and a rubric must never say "close the ticket because the ad already runs" or "the ticket is Todo therefore the ad is not live". The decision (Halloween version / refresh / reuse / skip) comes from the sheet's campaigns+matrix, not from state. Note ART-790 and ART-792 are named in the card and are exactly this task's ancestors ("Updated ZM Marketing Screenshots", "ZM3D - Marketing Screenshots round 3") — keep both off the graded path, as `01_Scenario_Design.md` §"excluded — off the path (SC-16)" already does. |
| **SC-22** | time_in_status_minutes runs past the clock | **"Ticket durations from Linear's time_in_status_minutes."** | **Yes, as a read hazard.** The field runs to 2026-02-13 while the clock is Oct 1 2025. If the run reasons "this ticket has been open for months" it is reading a future-dated duration. Grade only what the tickets say, or compute from `created_at`/`completed_at`. |
| **SC-30** | Done parent tickets with open children | **"A parent ticket's status implying its children's."** | **Yes.** ART-792 is a `Team Epic` parent over the library tickets. A parent's state must not be read as covering ART-793 … ART-854; each ad's ticket is graded on its own comment and assignee. |
| **SC-32** | 'In Review' tickets with completion dates | **"'In Review' tickets as open or done."** | **Yes, conditionally.** The base ART set contains `In Review` tickets carrying `completed_at`. If any ad's ticket resolves to `In Review`, neither "still open" nor "done" is gradable from state; the comment/assignee writes are the surface. |
| **SC-36** | Victor Barnes still on invites and channels | **"Invite/share lists built from channel or calendar membership."** | **Yes — sharing step.** Deliverables (a) and (b) are "shared so the team can comment". Victor Barnes left April 2025 yet is still in #god-gameart, on recurring invites and owns EPI-4. A share list derived from channel membership or the review's attendee rows can include him. Grade "shared with the review attendees / the art team as the ask names them", never "these 7 exact emails". |
| **SC-7** (`watch`) | People who left channels still listed | **"Channel membership (who is in a channel)."** | **Yes — same step, weaker form.** All leavers stay in `channels.json`; membership is not current staff. Any "who is on the art team" inference is ungraded. |
| **SC-26** | Slack links to ENG-2367/2368/2373 don't exist | **"Resolving Slack's ENG-2367/2368/2373 links."** | **Yes, as a read hazard only.** If the thread or a DM cites those ENG numbers they cannot be resolved (Linear stops at ENG-2366; they are really ZOM-436/521/527). Do not build a step that requires resolving them, and do not inject ENG-2367+. |
| **SC-70** | Slack timezones all Los Angeles | **"A person's timezone from Slack."** | **Yes, as a deadline hazard.** Everyone shows America/Los_Angeles in Slack while calendars hold real zones. "Before Thursday's review" must be resolved from the calendar event (`evt_d947bf7cd910549b674b1f`, Thu 2025-10-02 16:00–16:30Z), never from a Slack profile, and a prompt must not ask for a local-time deadline. |

### A2. Identity-adjacent, must stay ungraded

| Card | Title | "Don't grade" (verbatim) | Touches this task? |
|---|---|---|---|
| **SC-49** | Founder count and Frederick's role | **"Founder counts or Frederick's founder status."** | **Touches the cast, not an ask.** Frederick Stone authored the October UA plan and created the ART catalogue (ART-790/792 and the ART-793 batch). The task leans on his *records*, never on his title: do not write "co-founder" into a criterion, do not grade a founder count, and do not ask the run to state his role. |
| **SC-54** | Frederick paid after his last paycheck | **"Frederick's pay after May 2025 in the ledger."** | **No — no pay, burn or payroll is asked.** Listed only because he is on the path; if a revision ever adds a budget or cost column to the tracker it would land on this card. Keep the tracker free of money columns. |

---

## B. Cards checked and **not** applicable (grouped, with the reason they stay out)

Reason key: **(no-fin)** no financial figure is asked; **(no-metric)** no product or
telemetry metric is asked; **(no-other-svc)** the service is not on this path;
**(no-ask)** the subject simply is not in the ask.

- **Money / ledger / runway — (no-fin):** SC-2 (CASH_BALANCE burn column comment), SC-3 (runway: investor letter vs CASH_BALANCE), SC-4 (adjoe payments ledger vs wires), SC-5 (Sep 2025 payroll/headcount/burn/runway), SC-17 (ad-revenue payouts per network), SC-21 (Jan 2025 Node wire), SC-33/SC-34 (investor-sheet duplicates / row 82), SC-35 (P&L month headers), SC-39 (Singular payment plan), SC-43 (Simon's 2024 pay), SC-46 (HEADCOUNT comment), SC-55 (Mattel RFP deadline), SC-63 (Griffin pro-rata), SC-64 (Node invoices), SC-69 (April BigQuery cost), SC-73 (monthly burn in pitch text). *Deliberate note:* the plan has no budget, and the one date the task does need — "before Thursday's review" — comes from the calendar, not from the RFP or a pitch.
- **Ad spend / UA numbers — (no-fin, no-metric):** SC-11 (Unity spend $0 in Snowflake), SC-12 (Meta spend missing), SC-23 (AppLovin spend dates/geos). **These three are the near-miss group:** the tracker names campaigns (`Android #440`, `Android #1896`, …) and the plan is about the creatives those campaigns run, but no spend, CPI, geo or campaign-date figure is asked or graded. Do not add a spend or performance column, and do not ask which campaign spent what.
- **Product / telemetry metrics — (no-metric):** SC-1 (Domino Delights Sep installs), SC-19 (RAW_EVENTS app versions vs Slack builds), SC-28 (Product OKRs page numbers), SC-29 (MMP report latency), SC-37 (crash-by-level comment), SC-44 (tutorial step events), SC-59 (country of early adjoe installs), SC-65 (average playtime), SC-68 (Boss Arena on prod).
- **Login / live-ops / code — (no-other-svc):** SC-31 (live-ops weekend outage), SC-47 (Weekly Quests), SC-62 (reward-import cadence), SC-45 (Confluence backend pages vs code), SC-52 (backend PR #79), SC-66 (analytics AWS account), SC-72 (Python 3.9 EOL). GitHub is read-only context here; nothing in the ask touches a repo, a build or a deploy.
- **Ticket state minutiae off the ad path — (no-ask):** SC-8 (ZOM-475 glass crash), SC-15 (ZOM-521 VFX master), SC-38 (Season Pass ship date), SC-61 (ENG-2255 owner — Brian or Samuel), SC-71 (ZOM-471 priority from the Linear-bot post), SC-41 (when ENG-2366 was documented), SC-50 (bot comment authors), SC-56 (commit title case), SC-67 (build #1621 lists #1620), SC-18 (PR #477 state), SC-51 (Node Google Ads link), SC-60 (Josh Dempsey identity — neither maker is Josh). None of these tickets is one of ART-793 … ART-854, and no ad decision reads priority, PR state or build number.
- **People / mail identity — (no-ask):** SC-6 (who sent a Node Media email), SC-24 (Tim Steudler's employer), SC-25 (PAYROLL_ROSTER vs actual staff), SC-53 (one player token, two players — it is `[IDENTIFIER_9782]`, a live-incident artefact).
- **Calendar / meeting dates — (no-ask, but see SC-36/SC-70):** SC-10 (LVP meeting Sep 7 vs 9), SC-40 (July board date), SC-42 (Node kickoff date). The task's only calendar read is Thursday's review, which is seeded as one `ical_uid` with matching attendee copies (`01_Scenario_Design.md` "Seeded review event copies | quantitative | attendee copies agree | folded").
- **Slack archive state — (no-ask):** SC-27 (#god-bugs / #god-gameart), SC-57 (`#zm-collect-win`). The reply goes to #zombie_marketing (`C06DJBJL798`), which is live; none of these three channels is a write target.
- **Other — (no-ask):** SC-9 (Play Ventures status), SC-13 (ZM3D beta date in a Trello list name), SC-14 (Trello beta cards' two complete flags), SC-20 (Node channel creation date), SC-48 ('Pitch Sep 25' deck date), SC-58 (ZM3D monster roster). **SC-13/SC-14 deserve a sentence:** Trello is on this task's read path only as *card text* — Frederick's comment `68dc65a0f2d7fb28743f5860` names the two ads the sheet omits (Julia's 4:5 static, ART-826; Marcus's portrait end card, ART-831). The list *name* and the `dueComplete`/`badges.dueComplete` disagreement are never read, so both cards stay out — unless a revision starts deriving status or a date from the board.

---

## C. Trap catalog (`universe_kb/trap_catalog.json`)

Caveat first: the file's `_meta.clock` is `2026-02-14T00:00:00Z` (the normal
universe). The entries below are structural hazards computed from the shared
exports, and every one that matters here is also visible in the synth-cut files
(`01_Grounding_Dossier.md` §"SHARED_FIRST_NAMES / SHARED_LAST_NAMES"); do not quote
a trap's example ids without re-checking them against the Oct 1 universe.

| Id | Title (one line) | Applies? |
|---|---|---|
| **N01** | `ENG-n` and `ZOM-n` exist for 624 numbers — every ZOM number has an unrelated ENG twin; ART/DES/EPI numbers overlap too. | **Yes, in its ART form.** The deliverable is keyed `ART-793` … `ART-854`; a bare "793" or a "ticket 793" resolves to the wrong team's issue. Always the full `ART-` key, and the prompt must never say "ticket 793". |
| **N02** | `GameOfDominoes` PR numbers overlap ENG issue numbers (`#1458` vs `ENG-1458`) and Helpshift numbers (`#118`). | **Weak.** No GitHub or Helpshift step exists here, but the sheet's campaign column carries `#`-prefixed build numbers (`Android #440`). Those are *build* ids, never Linear keys — do not let a criterion conflate `#440` with an issue. |
| **N03** | Branch keys without the hyphen (`ENG1229QuestCollectChapterRewards`) and redacted owners (`[PERSON_NAME_0067]/ENG-1622-1`). | **No.** Linear↔GitHub reconciliation via branch names is not part of this task (`links_json` is empty on all issues; the design reaches tickets through the sheet). |
| **D01** | Drive titles that normalise to the same name under different owners — 131 groups incl. four different owners' "Untitled spreadsheet"/"Untitled document". | **Yes.** Claire already owns one of the four "Untitled spreadsheet" copies in that group. A new doc/sheet titled near an existing family makes the wrong file gradable. Pick a distinguishing title and grade by the link posted in the thread. |
| **D02** | Docs with identical bodies under different ids/owners. | **Weak.** Nothing in the ask requires matching two copies of the same body; if the plan quotes an existing doc, cite one persona-readable id. |
| **D03** | Slide decks sharing a title family (Weekly Update, publisher pitches, BoD decks). | **No.** The seasonal deck (`f_5ebf55ad29e815d46243c8`) is read for Robert's Halloween art, not graded by title. |
| **D04** | Spreadsheets whose titles normalise to the same name (P&L versions, investor lists, KPI exports) — incl. four owners' "Untitled spreadsheet". | **Yes — the tracker.** The new sheet must be identified by the link Claire posts, not by its title; "the tracker" is ambiguous among many near-identical sheet families, and the live creatives sheet (`f_02b1968f5e882366fbb883`) is a separate, pre-existing artefact she must not overwrite. |
| **D05** | Drive title families with version markers (v1/v2/final/draft/copy of/updated) — 35 groups; "final" is not the latest. | **Yes, as a naming instruction.** If Claire names the plan "... final" or "v2" it enters a family where the label means nothing. Prefer no version marker, or one dated marker, and grade by link. |
| **D06** | Confluence pages with readable version history (old bodies via `get_page_version`/diff) — 30 pages. | **No.** Confluence is not on this path (no page is created, updated or cited as a deciding record). |
| **D07** | Trello roadmap is stale against Linear (boards quiet since 2025-11-13; Linear last created 2025-11-07, updated 2026-01-28). | **Conditional — yes if a revision asks "status".** As written, Trello is only card text and Linear only carries the call/assignee. The moment a grader compares "what the board says" with "what Linear says", this card fires. Keep status single-sourced (Linear), Trello evidence single-purpose. |
| **D08** | P&L workbook versions project different zero-cash months (Jun/Jul/Sep-30/Oct/Jan versions). | **No.** No financial workbook is read. |
| **P01** | Shared first names across people and tokens: `marcus` = Marcus Bennett (persona) / Marcus Lee (UA) / `Marcus <marcus@harmonygames.co>` / a GitHub token; `martin` = Martin Lewis / Martin Walsh; also `claire`, `thomas`. | **Yes — and this is the load-bearing hazard.** Leonard's ask says bare "Marcus" and "Martin". Marcus Bennett is `usr_c77c50cc15c5342d` (video, end cards, the `D05V2N6PZNU` IM); Marcus Lee is `usr_b501f018a4c5319f` (UA); Martin Walsh is `usr_51f5f16d46e8cf55` (icon, store screens, stills); Martin Lewis is a different, non-persona contact. The two makers must be decidable from an incorporated record (the roles Leonard states + the IM + the ticket authors), never from the first name. |
| **P02** | Shared surnames: Bennett = Marcus/Oscar; Brooks = Oliver/Lauren; Baker = Owen/Thomas; Lawson = Julia/Peter; Price = Calvin/Nathan. | **Yes.** "Bennett" alone is ambiguous (Marcus vs Oscar Bennett), and "Julia" (the 4:5 static, ART-826) is Julia Lawson — a surface owner, not a maker. Never make a surname or a first name the only key. |
| **P03** | `marcus@harmonygames.co` mailbox — a *different* Marcus, rendered as "Marcus Bennett <marcus@…>", vs persona Marcus Bennett (no mailbox) vs Marcus Lee (UA). | **Yes, unrequested but dangerous.** If the run validates the maker by searching mail, this mailbox will look like Marcus Bennett and is not him. Decide the maker from Linear's `usr_` id and the Slack IM, not from a `marcus@` message. |
| **K02** | App-name lineage: `Puzzles vs Zombies` / `Match 3D` / `Zombie Game 3D` → `Zombie Match 3D`; TestFlight-only `Domino Adventure`, `Trump Billionaires Club`; `Combo Fighter` vs repo `Combo-Fighters`. | **Yes.** The doc and tracker will name the game. The graded name is **Zombie Match 3D** (the convention the sheet and tickets use); `Puzzles vs Zombies` survives only in TestFlight 2025-03..07 records. Do not let a criterion accept a legacy name as the plan's subject, and do not grade a name-count across eras. |

---

## D. Subjects the parent flagged that **no** synthcut card covers

Recorded so the gap is not mistaken for safety:

- **Store screenshots / store art.** No card. The nearest are SC-16 (ART-790/792,
  the screenshot tickets) and D01/D05 (naming families). The Halloween icon and
  iPad-set asks have no known-data-issue at all — they are new tickets, so the only
  risk is the *existing* store-spec ancestor ART-774 (Done Apr 15), which
  `01_Scenario_Design.md` §"ART-774 store spec (Done Apr 15)" keeps out as a dated
  claim.
- **Halloween.** No card. The word is thin in the base data (44 Slack hits 2023-10 →
  2025-09, 8 Drive name hits all in-game `HalloweenMansion` icons), so any Halloween
  *art* fact has to come from the seeded workbook/DM, not from base history.
- **Unity campaigns.** Only SC-11 (spend is $0). The campaign *ids* on the sheet are
  not affected; the card only forbids spend/CPI.
- **Gmail aliases.** No synthcut card covers aliases as such. The adjacent cards are
  SC-6 (HG address on a Node sender), SC-24 (Tim Steudler), SC-60 (Josh Dempsey).
  Claire's own `claire@` file alias is a documented identity fact in
  `01_Grounding_Dossier.md` (I03), not a card — do not build a step that requires
  proving which of her addresses authored a file.
- **Julia.** No card and no ambiguity inside this task: Julia Lawson owns the 4:5
  static (ART-826) that the sheet omits; she is not a maker to assign.
- **Robert / Arthur / Leonard / Claire as records.** No card covers them
  individually. Robert (`robert@harmonygames.co`, `usr_Robert`) owns the seasonal
  deck and writes no Linear record; Arthur owns the Q4 release calendar; Leonard
  writes the ask and organizes the review; Claire is the actor. Only Frederick has
  cards (SC-49, SC-54), and neither is asked.

---

## E. What this means for the prompt (short)

1. No money, no spend, no installs, no metrics, no payroll, no founder titles —
   one clause each and the whole no-fin / no-metric block stays dormant.
2. Ticket state is never evidence: the plan's calls come from the sheet and the
   library comments, and nothing in the ask says "close", "mark done" or "update
   the status".
3. Makers are decided by role + `usr_` id + the IM, never by the bare first names
   Leonard used.
4. "Shared so the team can comment" is graded on the attendees the ask names, not
   on a channel-member list that still contains Victor Barnes.
5. The deadline comes from Thursday's review on the calendar, not from a Slack
   timezone.
6. One sheet, one doc, one thread: identify all three by the links in the reply,
   never by title, version label or name.
