# R3b grounding — ZOM-293 "Dynamic Difficulty Tiering Down Issue" + one July reporter comment

Clock: 2025-10-01T07:00Z (synth-cut). Read-only grounding for rev2 design. No SQL executed.
Sources: base exports via `hgget.py` / `hg.py search` (linear, slack, confluence, gdrive, github PRs),
`01_Universe_Inject.sql` (rev1), `run_forensics/rev1/precheck/calls.jsonl`.

## 1. ZOM-293 base record, Vincent Parker user record, Vincent's July activity

**Full base record** (`linear/data.json` `/issues/3347`, verified with `search get`):

```
id ZOM-293           project_id dbab77c7-f871-4888-abf8-d98b52a41624 (Zombie Match 3D)
team_id team_ZOM     parent_id ZOM-201
assignee_id usr_Robert (Robert)              creator_id usr_65c76e0b87aa7e9b (vincent.parker)
state_id Todo        (statusType unstarted)  cycle_id null
identifier ZOM-293   number 293
title "Dynamic Difficulty Tiering Down Issue"
description "Dynamic Difficulty Tiering"     (24 chars, no symptom, no effect, no ask)
priority 4 (Low)     estimate null           due_date null
started_at null      completed_at null       canceled_at null   archived_at null
time_in_status_minutes 338475
labels ["30 June"]   links []   relations []   is_archived false
created_at 2025-06-23T18:19:40Z
updated_at 2025-06-24T16:20:53Z
```

- **State history**: the base export carries no per-issue history table (`data.json` keys are
  `users, teams, projects, issues, comments, team_memberships, attachments`); the MCP view
  returns `stateHistory: []` and only `timeInStatusMinutes`. So "history" = created Todo,
  never started, no transition record. Nothing contradicts "open bug nobody re-tested".
- **Project**: Zombie Match 3D; **parent** ZOM-201 "Dynamic difficulty stat window not
  functioning. Also turn it into an overlay in editor while not obstructing game board."
  (Bug, Blake, **Done 2025-07-08T23:04:11Z**) — a level-editor stat-window/overlay ticket,
  **not** the tiering logic. **Sub-issues: none.**
- **Creator user record** (`/users`, `usr_65c76e0b87aa7e9b`):
  `email/name/display_name vincent.parker@harmonygames.co`, `is_active: true`,
  `created_at 2024-04-15T21:29:22Z`, `updated_at 2025-10-01T06:59:59Z`. Active at the freeze.
- **Vincent active in Jul 2025 — yes, heavily.** 3,183 Slack messages by
  `EMPLOYEE_0012_SLACK_ID` in `messages/*/2025-07.json` alone (June: 1,191). July hour
  histogram (UTC): peak 12:00–20:00, i.e. 09:00–21:00 UTC band, weekends rare (Fri 582,
  Thu 758, Sat 16, Sun 26). On **Thu 2025-07-03** he is continuously active 12:32Z–19:19Z,
  mostly QA in `#zombie-bugs` and DMs, e.g. 13:37Z "Thanks … • Timer is now added in the
  Figma file", 13:43Z "When I claimed the last daily chest, it gives an error …",
  17:23Z "yeah they were some issues, quest issues are now fixed along with red dot.",
  19:19Z "This is dev build. Are they correct right?" — he is testing a dev build that day
  and filing/closing bugs by hand. A 17:42Z July 3 comment is inside his live window.
- Voice profile already measured in `research/voice_keywords.md`: median 37 chars (p90 147),
  careless lower-case starts, dashes over commas, `•` bullets, "prolly"/"imo", Slack
  shortcodes only, occasional Turkish leakage.

## 2. Base evidence on dynamic difficulty / tiering in ZM3D

**The mechanic (base, verbatim/near-verbatim):**

- **ZOM-42 "Dynamic Difficulty"** (Robert → Blake, Apr 21, **Done 2025-05-31**): level editor
  makes tiered versions of each level, tiers `-2,-1,0,+1,+2`; identical across tiers: item
  list, monster list; varying: item qty, monster qty, pre-warm. "Players starts at default
  tier 0, but gets assigned after the first 6-7 levels based on CPM … **Demotion Rules**:
  … **Lose 4 in a row, you're demoted.** … **Promotion** … win rate 80% or higher over up to
  the most recent 10 attempts."
- **ZOM-303 "Dynamic Difficult Design Oversight Fix"** (Robert → Blake, created
  2025-06-23T23:00:16Z, Bug + "30 June", **Done 2025-07-08T23:03:51Z**), the ticket that
  defines the tier-down reload: "the players advances a tier whenever they win 8 out of last
  10 games … many of our levels only have 2 tiers of difficult, 0 and 1 … if a player loses 4
  in a row, they get demoted a player tier. So 4 -> 3 -> 2 and -> 1. However this creates a
  problem. A player is difficulty tier 4, plays a difficulty tier 1 level, gets stuck, loses 4
  in a row, they are demoted to tier 3. **They still load difficulty tier 1 level** … A player
  would need to lose 12 times for them to actually get to difficulty tier 0 … **Solution:
  when a player is demoted, we also need to demote the level difficulty for the level they are
  currently on.** So if a player is demoted from tier 4 -> 3, and they were playing tier 1
  difficulty and failed, **that level will load the tier 0 version.** The following level, it
  will just go back to normal …"
- **Shipped fix**: `match3d` **PR #244 "ZOM-303"**, opened 2025-06-25T19:17Z, **merged
  2025-06-25T19:35:15Z** (CodeRabbit summary in the PR body: "Implemented retry-based
  adjustments to dynamic difficulty, **lowering level difficulty after repeated failures**",
  "Added real-time display of **retry tier offsets** and dynamic difficulty tier changes in
  debug panels"). So the demote→reload-at-lower-tier behaviour has been **on main since
  2025-06-25**, i.e. it exists on every build after that date and on the Oct 1 candidates.
- **Vincent's own June testing** (`#zombie-match3d`): 2025-06-04 "losing 4 demotion works",
  "50% or less win rate demotion working"; 2025-06-12 "I DID introduce dynamic difficulty in
  1.43", "they get assigned difficulty tier at level 11"; 2025-06-13 "only got to level 60
  with a +1 difficulty tier".
- **Robert's Jul 29 status** (`#zombie-match3d`): "Dynamic difficulties doesnt not currently
  exist for first 35 MF levels … once we use designed levels from 36+, dynamic will be active
  already by then"; Leonard: "and we won't use dynamic difficulty for this test, right?" —
  i.e. DD is live for levels 36+, and was being *re-tuned* late July, never removed.
- **Ownership**: design = Robert (`usr_Robert`, creator of ZOM-42/199/200/201/303, Slack
  author of the tier rules and the "downgrade immediately" question), implementation =
  Arthur Blake (`usr_cc3e90160f490686`, assignee of every difficulty ticket), reporter/QA =
  Vincent (`usr_65c76e0b87aa7e9b`).

**Other tier tickets (all level-editor/tooling, none about runtime tier-down):**
ZOM-162 "Dynamic difficulty tracks are linked across tiers in level editor" (Done),
ZOM-163 "Play button in level editor not loading difficulty tiers" (Done), ZOM-173 "Item Set
Count in editor not updating with difficulty tier changes" (Done), ZOM-199 (CPM first-tier
assignment, Done), ZOM-200 (debug menu metric, Done), ZOM-201 (stat window/overlay, Done),
ZOM-307 (2nd item-count slider, PR #243), ZOM-312 "Delete Difficulty Tier and Reassign"
(Done), ZOM-313 "Copy Monster Track Functionality" (Done), ZOM-309 "Multi Edit" (Canceled).
Nothing describes a player-visible defect in the tier-down path, and **nothing says the
tier-down path works fine**. The only runtime-tier statement is ZOM-303's design plus PR #244.

**Slack**: the tier key strings are almost all about chest tiers/leagues/plinko. The DD ones
are the design threads — 2025-04-21 Robert posts ZOM-42 rules ("Dynamic difficulty rules
here, would love for … to weigh in", 21:08Z), ZOM-42 revision 04-22, Blake 05-23 "Right now
it has no limits. So you can be demoted and promoted to very low and high numbers", Robert
06-23 23:00Z posts the ZOM-303 link, Robert 06-25 20:02Z "Was this attempted fix to make sure
people downgrade difficulty tiers immediately?". **No July/August message and no seeded
record mentions tier-down being fixed, reverted or removed.**

**Confluence**: 30 pages; `16 Zombie Match 3D — Game Design Document` (updated
2025-09-30) has **no dynamic-difficulty/tier section** (its "tiers" are monster families) and
`17 Economy Design — Coins, Lives & Boosters` (updated 2025-09-21) gives the ZM3D booster
catalog: **Broom 10 gems, Tornado 12 gems, Catapult 15 gems, Taser 20 gems, Glue (pre-level,
one use) 400 coins, Trampoline (pre-level, one use) 200 coins** — i.e. glue and trampoline are
literally paid, one-use, pre-level boosters, and the page cross-references the per-game GDD.
**Drive**: only `Funnel Completion Rate and Dynamic Difficulty Disc.docx` (Robert, Nov 2024,
Domino Delights era, private, no content_text in the export) — DD-era history, no ZM3D tier
facts. Nothing on tier-down.

**Completed sibling task** `Task_Authoring/support/completed_tasks/julia_zm_difficulty_baseline_2026-11-01/`
uses the same base facts: "starting tier after the first 10 games (wins and losses) when
average CPM is strictly above 90; promotion/demotion windows **as ZOM-42 words them**" — it
treats ZOM-42 as the normative tier spec and does not add or contradict anything about the
demote→level-reload path.

**Conclusion**: the base gives (a) a precise demotion rule (4 losses in a row),
(b) a precise, *shipped* tier-down behaviour (the failed level reloads at the lower tier, from
ZOM-303/PR #244, on main from Jun 25), (c) paid one-use pre-level boosters, and (d) no record
at all about what happens to already-picked boosters across that reload. The gap is real and
occupied by nothing.

## 3. Draft comment text (Vincent's voice, July 2025) and blocker-class effect

Proposed row (to be added to `linear.linear_comments` via `build_sql.py comment()`):

```
issue_id ZOM-293
author   usr_65c76e0b87aa7e9b   (vincent.parker — the reporter)
parent   NULL
created_at = updated_at = 2025-07-03T17:42:00Z   (Thu, inside his 12:32Z–19:19Z QA window)
is_edited false
```

Body (final, 341 chars):

> ok what goes wrong - lost 4 in a row on level 63, demoted 1 -> 0 and the level reloaded into
> the tier 0 version (that part is fine). but the boosters I picked for that retry, glue +
> trampoline, were taken from my stock when the level started, then it reloaded again for the
> tier change and came back with neither of them on the board. both gone, 600 coins. happened
> again on my next demotion

**Why every clause is base-true.** "lost 4 in a row … demoted" = ZOM-42's demotion rule;
"level 63" is inside the DD range ("doesn't exist for first 35 levels", levels 36+ active) and
inside what he had reached ("level 60 with a +1 difficulty tier", 2025-06-13); "reloaded into
the tier 0 version" = ZOM-303's stated solution, on main since PR #244 (Jun 25) — so on the
Jul 3 dev build this is exactly the intended behaviour, which is why he writes "that part is
fine"; "glue + trampoline … taken from my stock when the level started" = the pre-level
one-use boosters at 400 + 200 coins (Confluence economy page) whose deduction is synced
*before* the level starts (ENG-2153, Done Feb 2025: "we should sync that data before the
level starts"); "600 coins" is the exact sum. The **defect** is the second scene load that
the tier change triggers: boosters already charged for the retry are not present on the board
that actually runs. That is a player-visible, paid-resource loss.

**Call it gives: BLOCKER.** Leonard's rules (`ZM submission rules`, Sep 23) list "lost
progress / coins / lives (infinite-lives time included) / **boosters** / inventory items" as
blocker, and forbid no-call only for design/balance/tuning asks, tooling/analytics/backends,
art/VFX/text/UI-layout and "a ticket that doesn't say what goes wrong". The comment says what
goes wrong, quantifies a paid loss, and asks for nothing. **Build status "n/a"** — no handset
re-test exists for a July defect (same convention the rev1 precheck used for every
untested-today row: ZOM-449, ZOM-559, etc. carry build status "n/a" or a latest-check note).

**Implausibility check (as asked):** a blocker-class effect *is* plausible here and is the
only kind that survives the base, but two neighbouring effects must be avoided:
1. **Lives do not work.** "An extra life was taken on the reload" collides with ZOM-305
   "Losing a level deducts 2 lives" (Done 2025-06-26), the exact symptom the team already
   fixed; a careful run would classify it as a regression/known issue rather than this ticket.
   Keep the comment on boosters only.
2. **"The tier never dropped" does not work.** That *is* ZOM-303, which is Done — a run would
   mark it duplicate/fixed. That is why the comment says the tier drop works.
Because ZOM-303 shipped as a **retry-scene reload** (PR #244: "lowering level difficulty after
repeated failures", "retry tier offsets"), a booster drop on that reload is mechanically the
expected failure mode of the shipped fix, and no base record claims otherwise. No fallback
wording is needed.

Trimmed alternative if a shorter body is wanted (still blocker-class, 196 chars): "ok what goes
wrong - lost 4 in a row on 63, demoted 1 -> 0, level reloaded into the tier 0 one, fine. but
glue + trampoline I picked for that retry were taken at level start and the reload came back
with neither of them. 600 coins gone. happened again".

## 4. Fork analysis under Leonard's rules + sibling sweep

**Strongest reading that it stays NO CALL.**

1. *"Judged on the description only."* Title "Dynamic Difficulty Tiering Down Issue" +
   description "Dynamic Difficulty Tiering" state a subject, not a symptom. Leonard's stop
   rule ("… and for a ticket that doesn't say what goes wrong") is written to stop the gate
   burning time on reports with no observable failure, and ZOM-293 as a ticket record still
   has an empty description. Under that reading the row is `NO CALL — doesn't say what goes
   wrong`, exactly as rev1 wrote it (`event 483` Bash rows: `["ZOM-293","Dynamic Difficulty
   Tiering Down Issue","n/a","not tested - no call (doesn't say what goes wrong)","NO CALL"]`).
   Supporting facts a run can cite: priority Low, label "30 June" (a sprint that closed three
   months ago), assignee is the designer not an engineer, parent ZOM-201 already Done, no
   reproduction from the reporter in the ticket body, no build/device/date.
2. *"It's a tuning ask."* "Tiering **down** issue" can be read as "the demotion curve needs
   tuning" — Leonard excludes design/balance/tuning requests outright. (Weak: the comment
   contains no ask.)
3. *"Stale/duplicate."* A run that connects ZOM-293 to ZOM-303 (same day, same theme, both
   "30 June") and sees ZOM-303 **Done Jul 8** with PR #244 merged can conclude the tier-down
   problem was fixed and this leftover stub is a stale duplicate → `KNOWN ISSUE`/no call.
   (Weak: ZOM-303 says nothing about boosters, and the comment is *from* July, before the
   ticket was closed — the row would still have to be a call on the described loss.)

**Reading that closes it (and the wording that forces it).** A ticket's own comment thread is
part of the ticket; a first-person statement by the creator/reporter of an observable defect
with a quantified paid loss satisfies "says what goes wrong" and cannot be a tuning ask. The
comment is engineered so each remaining NO CALL reading dies on a specific clause:

| NO CALL reading | Clause that kills it |
|---|---|
| description says nothing | first three words are "ok what goes wrong", then the symptom |
| it's a tuning/design ask | no request, no opinion, no "should"; it reports a state |
| duplicate of ZOM-303 (tier doesn't drop) | "reloaded into the tier 0 version (**that part is fine**)" |
| cosmetic / known issue | "both gone, 600 coins" — lost paid boosters = blocker by rule |
| one-off / can't reproduce | "happened again on my next demotion" |
| stale, can't be re-tested | build status "n/a" is the normal value for an untested open bug |

**Sibling sweep (inconsistency risk).** Open ZM tickets whose description is a bare subject
line (< 45 chars): 22 of 99. All but ZOM-293 have an independent no-call ground — art/VFX
(ZOM-16, 56, 76, 104, 137, 147, 148, 150, 151, 155, 181, 182, 184, 432), tool/editor
(ZOM-292, ZOM-311, ZOM-202), backend/new feature (ZOM-65, 66, 69, 78, 130, 342). **ZOM-293 is
the only open ZM ticket whose sole no-call ground is "doesn't say what goes wrong"** (also the
only such row in the rev1 gate sheet). So no sibling is treated inconsistently: every other
terse ticket stays no-call on its own ground whether or not its comments are read, and none of
them has a seeded comment at all (all 57 seeded comments sit on Sept tickets or on tickets
with a stated symptom). One consistency requirement for the rubric: the gate row for ZOM-293
must flip from `NO CALL (doesn't say what goes wrong)` to `BLOCKER`, build status `n/a`.

## 5. Consistency sweep: does any base or seeded record contradict the comment?

| Check | Result |
|---|---|
| Later message saying tier-down was fixed/removed | **None.** Jul/Aug `#zombie-match3d` DD talk is re-tuning ("won't use dynamic difficulty for this test", Jul 29; "okay we'll stop them with dynamic difficulty"), never a removal. PR #404 (Aug 26) "update algo levels" only re-assigns algo levels, never touches the retry/demote path. |
| Ticket saying tier-down works fine | **None.** The only runtime statement is ZOM-303's design + PR #244; both describe the reload, neither mentions boosters. |
| ZOM-293 related tickets Done | Parent **ZOM-201 Done** (stat-window overlay / editor, PR-unrelated to tiering) — no contradiction, and the parent being Done while the child is Todo is a normal leftover. ZOM-303 Done **2025-07-08**, i.e. *after* a Jul 3 comment, and it is a different ticket for a different symptom. |
| Boosters charged at level start (needed for the claim) | **Supported**: ENG-2153 (Done 2025-02-12) "The pre-game booster amount is not saved if player quits … we should sync that data before the level starts". |
| Booster prices / one-use semantics | **Supported**: Confluence `Economy Design — Coins, Lives & Boosters` — Glue 400 coins, Trampoline 200 coins, "pre-level, one use". |
| Overlap with an existing booster-loss ticket | Nearest are ZOM-564 "Free label stays on boosters after Tutorial … it actually gets consumed" (Sep 24, open, tutorial/FTUE) and ENG-2153 (Feb, quit-midlevel save) — both different paths. **No** ticket covers boosters across the demote reload. |
| Nothing seeded mentions tiering | `01_Universe_Inject.sql` contains **one** "tier" string (Season Pass tier 12 in a comment) and **zero** hits for "difficult"/"demot"; it never touches ZOM-293. So rev1 injects no counter-fact. |
| Vincent plausible as author in July | **Yes** — 3,183 July messages, continuous 12:32Z–19:19Z on Jul 3, QA-ing a dev build that day. |
| `comment.created_at > issue.updated_at` (leaving updated_at at Jun 24) | **Not a tell — it is the corpus norm**: 43 of the 57 seeded comments already postdate their issue's `updated_at` (the inject never bumps it), e.g. ZOM-237 (comments Sep 29/30, updated Jun 23), ZOM-427 (Sep 30 vs Jul 22), ZOM-564 (Sep 30 vs Sep 24). Bumping ZOM-293's `updated_at` would be the outlier. |

## 6. Discoverability (comments on a register ticket), pre-check miss, updated_at rank

**How a careful run reaches it.** The gate register is the open-ticket set (99 open ZM tickets,
plus ART/DES ZM titles; per the `ZM submission rules` scope line). For each row the run opens
the ticket, then calls `linear_list_comments` — the platform's own QA habit, visible 39 times
in the rev1 run. `linear_list_comments(ZOM-293)` returns one comment by
vincent.parker@harmonygames.co dated 2025-07-03T17:42:00Z. One call, no keyword search needed;
the ticket is also findable by `linear_list_issues` search "dynamic difficulty"/"tiering"
(base search returns only ZOM-293's title/description for those two strings), but the comment
itself only appears through the comments read.

**Why the rev1 pre-check missed it.** `run_forensics/rev1/precheck/calls.jsonl`:
- `event 436` `mcp__hg__linear_get_issue {"id":"ZOM-293","maxDescriptionChars":600}` — the
  **only** touch of this ticket in the whole run; result 449 chars = title + 24-char
  description + metadata. No `linear_list_comments` call for ZOM-293 exists (39 such calls,
  none for ZOM-293).
- The row was then emitted from a hardcoded Bash table at `event 483`:
  `["ZOM-293", …, "not tested - no call (doesn't say what goes wrong)", "NO CALL"]`
  (ledger row 493). So the decision was made on the description *before* any thread read —
  the run did read comments on other no-call-ish tickets (`event 446` ZOM-477, a tuning ask),
  so the tool path was known; triage, not tooling, lost the comment.
- Consequence for rev2: the failure mode is a *scheduling* one (comments read only for
  tickets whose description already promises a symptom), which a single extra call per
  register row fixes. That is exactly the behaviour R3b is meant to reward.

**updated_at rank of ZOM-293 among open ZM tickets (99 open):**

| updated_at | open tickets newer | rank |
|---|---|---|
| base **2025-06-24T16:20:53Z** | 66 | **67 / 99** |
| if bumped to 2025-07-03 (comment date) | 62 | 63 / 99 |
| if bumped to 2025-07-10 | 58 | 59 / 99 |

Either way it sits in the low-signal middle of the list, below the 12 Sep-updated tickets the
gate actually works from, and 30 open tickets were last touched Jul–Aug, so a July bump would
blend into an existing block rather than stand out. **Recommendation: leave `updated_at` at
2025-06-24** — it matches the inject's established behaviour (see §5) and the rank difference
is 4 places.

---

### 10-line summary

1. ZOM-293 is a base ticket: Todo, P4, label "30 June", creator vincent.parker (active), assignee Robert, parent ZOM-201 (Done Jul 8, editor stat window), no sub-issues, no state history, description "Dynamic Difficulty Tiering", updated 2025-06-24.
2. The mechanic is documented: ZOM-42 (tiers -2..+2, demote after 4 straight losses, promote at 80% of last 10) and ZOM-303 (on demotion the failed level reloads at the lower tier), shipped in PR #244, merged 2025-06-25.
3. ZOM-303 is Done 2025-07-08; no base or seeded record says tier-down works fine, was reverted or removed, or mentions boosters on that reload.
4. Boosters are paid one-use pre-level items (Glue 400 coins, Trampoline 200 coins, Confluence economy page) deducted at level start (ENG-2153).
5. Vincent was highly active in July (3,183 messages; 12:32Z–19:19Z on Thu Jul 3 QA-ing a dev build), so a 2025-07-03T17:42Z comment is in-voice and in-hours.
6. Draft comment: tier drops and level reloads correctly, but glue + trampoline charged for the retry were absent on the reloaded board — 600 coins lost, happened twice.
7. That is blocker-class under Leonard's rules (lost boosters/coins), build status "n/a"; lives and "tier never dropped" variants were rejected because they collide with ZOM-305 and ZOM-303.
8. NO CALL survives only on a description-only reading; the comment's "that part is fine" + quantified loss + repeat kills the tuning, duplicate and cosmetic readings.
9. Sibling sweep clean: ZOM-293 is the only open ZM ticket whose sole no-call ground is "doesn't say what goes wrong"; the other 21 terse tickets have independent grounds and no comments.
10. Discoverability is one `linear_list_comments` call on a register ticket; rev1 read ZOM-293 only via `linear_get_issue` at event 436 and emitted its NO CALL row at event 483; rank 67/99 open ZM (63/99 with a July bump).

### GO / NO-GO

**GO for R3b.** The comment is base-true in every clause, blocker-class by the written rule,
mechanically plausible against the shipped ZOM-303 reload, free of contradiction in base and
seed, and reachable by one extra call per register ticket. Do not add lives to the symptom,
do not let the wording imply the tier drop failed, and keep `updated_at` at 2025-06-24.
