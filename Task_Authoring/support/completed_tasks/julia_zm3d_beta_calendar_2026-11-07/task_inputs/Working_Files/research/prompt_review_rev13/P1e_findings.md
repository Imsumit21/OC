# P1e findings, rev13: Unique Ground Truth and Clarity (deep recheck pass P1)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

SQL reviewed: sha256 1f2175a297fd390960f22c3767f790fc980a881023affa6ece970745fb40289b (hash confirmed). Diffed against rev12, b5ccbfa5...

## Result

P1 returns `none`: no open fork and no fail-level finding.

- **DR1: settled.** The new rule sentence kills its Reading B.
- **F5: stronger.** Arthur's comment now says "Not a blocker for this PR".
- **F12: settled** with DR1.
- **Changed text:** I tried to break it with 7 new candidates (F31-F37). Each is killed by a quote.
- **Clarity:** no write divergence. The 5 writes are unchanged.

Checked: 7 changed SQL lines, plus the unchanged sweep of 45 rule-source sentences, 14 PNs Beta rows and 16 sheet columns.

## What changed

Seven lines differ. Everything else is byte-identical.

| Line | Record | Rev12 | Rev13 |
|---|---|---|---|
| 115 | Brief, Scope | "the shop rotation is not a beat" | "the rotating shop is not a beat" |
| 125 | Brief, Push copy | "with what its row is missing" | "with which of those its row is missing" |
| 127 | Brief style runs | Config locks heading 2863-2875 | 2873-2885 |
| 157 | #468 rc_38 (Arthur) | "are still the first-pass models. The final vial models are missing and need to be in before the beta" | "still need their final models before the event runs. Not a blocker for this PR" |
| 170 | #zombie-prs mirror of rc_38 | Old text | New text |
| 210 | ZOM-465 cmt_3 (Brian) | "does have to land before the beta" | "does have to land before the event runs" |
| 259 | Trello action on card 61 | No list field | Adds `"list":{"id":"6851a674975da1fe76e70d93","name":"BETA: Sep 30"}` |

Mechanical checks:
- All 9 style-run offsets match the rev13 brief text.
- The mirror text equals rc_38 after decoding `&amp;`.
- No "first-pass", "shop rotation" or "what its row" text remains.
- `hg.py lint` reports 0 FAIL and 0 CHECK.
- 54 of 56 base commentCard actions carry `data.list`, so line 259 matches the base shape.

## DR1: settled

Rule, brief, Push copy: "A push goes out only if its row is Ready and LIVE and the English copy on that row names the game as Zombie Match 3D and events by their ZM3D names (Login Calendar and Weekly Rankings are fine). Anything else is held, with which of those its row is missing."

"Those" binds the cell to the listed conditions. Reading B's extra clause (new quests, from row 2's Details "Revisit once new quests roll out.") is not one of them, so a rule-source sentence rules it out as required content. Row 2's cell is Ready.

A run that adds the Details note as an aside contradicts nothing, so the rubric should not fail it.

Reading A's Pushes tab, rebuilt under the new sentence:

| Row | Push | Which of those is missing |
|---|---|---|
| 2 | Quests | Ready |
| 5 | Lapsed 1d | Game name (copy says Puzzles vs Zombies) |
| 7 | FTUE | Game name (copy says Puzzles vs Zombies) |
| 8 | Win & Collect | Ready, LIVE, ZM3D event name |
| 10 | Plague Race | LIVE |
| 13 | Login Calendar | Ready, LIVE |
| 14 | Season Pass | Ready, LIVE |
| 15 | Weekly Leaderboard | LIVE |

Rows 4 and 6 still send. The Calendar tab and the 5 writes are unchanged.

## Forks the changed text touches

- F5: C&W held by #468 review notes | A: not held | B: held | Settled by: rc_38 "Not a blocker for this PR", on top of rev12's kills: both CodeRabbit reviews and rev_3 are state COMMENTED; brief "cosmetic ... gaps" do not hold and "player-facing art" goes in Still to do. CodeRabbit rc_1's guard is at HEAD, GameLoader.cs line 184.
- F12: Quests push "What is missing" | A: Ready | B: Ready plus new quests | Settled by: "with which of those its row is missing". See DR1.
- F16: C&W title, info text, token travel, analytics | A: out | B: in, because "before the beta" no longer matches "before the event runs" | Settled by: ZOM-566 "The event runs fine with the current text"; ZOM-526 "the events run without it". See F32.
- F21: Row 8 event name, now a required part of the cell | A: listed | B: Ready and LIVE only, since Slack and PR titles say Win & Collect | Settled by: calendar page "Same feature as Win & Collect on Domino Delights, under a different name"; brief "Collect & Win runs". ZOM-566 mentions "name changes", but I found no in-game title text at HEAD, so nothing supports B.

## Attacks on the changed text

- F31: Daily free coin as a beat, since the rename could leave it outside "rotating shop" | A: out | B: a daily reset on the calendar | Settled by: brief "the rotating shop is not a beat"; #zombie-match3d Jun 3 "DAILY is rotating and not buyable multiple times"; ShopItem.cs "// free claim" sits on `GetRotatingProductRemainingCount`. "Rotating shop" is the real feature name (ZOM-348, Economy Design "The daily rotating shop", `RotatingShopManager`), so the rename is a gain.
- F32: Mixed "before the beta" and "before the event runs" | A: negatives stay out | B: "not before the beta" leaves those items due before Oct 10 | Settled by: both C&W negatives say the event runs without them (F16). Endless is covered by Brian's "Endless runs fine without them". The positives now match the brief's "before it runs".
- F33: Art gates the C&W start, because it must land "before the event runs" | A: Fri Oct 10 stands | B: first window moves until the art lands | Settled by: brief "A beat starts with the first window that opens after its server windows are live on prod".
- F34: "Not a blocker" read as out of Still to do, or "for this PR" read as a blocker for the event, so held | A: Still to do, not held | B: dropped, or held | Settled by: rc_38 "still need their final models before the event runs"; brief "anything flagged since this brief as still needed", "cosmetic ... gaps". The new text drops "first-pass", so the current model is less explicit, but GameLoader.cs logs "falling back to default asset" and nothing shows players cannot score.
- F35: Antecedent of "those" is the parenthetical names | A: the conditions | B: Login Calendar and Weekly Rankings | Settled by: the same sentence: "Anything else is held" must also report Not Ready and WIP rows, and names the brief calls "fine" cannot be missing.
- F36: Rows with no game name now list it as missing, since "those" includes the naming condition | A: not listed | B: listed on rows 2, 8, 10, 13, 14, 15 | Settled by: thread reply "the naming rule is only about wrong names".
- F37: Non-rotating shop items as beats, for example Pop-up Offers on the Oct 21 Trello list | A: out | B: a beat | Settled by: brief test "an event window, a reset or a start push"; Domino Delights Shop doc (shared with Julia) "pop-up offers around progression triggered events". No window record exists.

Line 259 changes no fork. "BETA: Sep 30" matches the later base actions (SC-13), and no cell reads a Trello list name. F11's comment text is unchanged.

## Timing note

The new wording makes the vial and icon items due before C&W's first window, which is Fri Oct 10 00:00 UTC under Reading A. That date is my derivation. No record states it, so the rubric should not require it.

## Forks not touched (same kill as rev12)

| Fork | Outcome | Kill |
|---|---|---|
| F1 | Local rows stay on Pushes | "a start push" |
| F2 | One ticket note | "the push that goes with it" |
| F3 | Weekly Leaderboard held | Vincent "Same on the second device." |
| F4 | Endless not held | Leonard "Could not get it to freeze" |
| F6 | Cohort term has no effect | 0 of 74 CHANGES_REQUESTED dated Aug-Sep |
| F7 | C&W first window Oct 10 | "first window that opens after" |
| F8 | Lock Oct 31 00:00 UTC | "locked 24h before each season opens" |
| F9 | Oct 31, Sep 26 mail | "Treat Fri Oct 31 as the date I am committing to" |
| F10 | Reply to Brian | "its owner is told in a reply on the mail" (passive, thinnest kill) |
| F11 | Quests not in Still to do | "does not wait on them"; "Nothing else goes in" |
| F13 | Halloween off | "Take it off the beta calendar" |
| F14 | Endless polish and themes out | "nothing waits on new themes" |
| F15 | lightSweep out | "nothing has to land for the beta" |
| F17 | Frame done | "in both submission builds" |
| F18 | Daily gift not held | "claiming works and nothing is lost" |
| F19 | Quest rollover not held | "it is good on prod now" |
| F20 | Zombie Match PNs Beta | "Ready and LIVE", "Weekly Rankings" |
| F22 | One leaderboard beat | "weekly league sessions" |
| F23 | Endless daily and weekly | "Every window is stated" |
| F24 | Julia's sheet | "your ZM Live Ops folder" |
| F25 | ZOM-78 | "Link the sheet here when it is ready." |
| F26 | Boss Arena off | "off this calendar until the pivot call" |
| F27 | Season Pass from Oct 6 | "Clip anything that starts before" |
| F28 | Deploy owner Douglas | GCal organizer; "Backend (Douglas)" |
| F29 | Thread reply applies | "Two things on top of the brief." |
| F30 | Store approval out | "Nothing else goes in" |

## Decision sweep basis

- RECORD: every item in the rev12 sweep, plus F12 (now a rule sentence) and F31-F37.
- SILENCE: none.
- SCOPE_GAP: none.

## Rubric notes

- Pushes: accept the "missing" cells above in any wording. Row 8 needs all three items.
- Accept an aside on row 2's Details note.
- Accept any moved config date before Oct 31 00:00 UTC.
- Accept a compact rendering of the 28 Endless daily windows.
- Do not require an Oct 10 art deadline.

## Platform defects

PLATFORM:anonymized-token: PNs Beta rows 7 and 14 carry [PERSON_NAME_2549] in the copy. A copy cell using the token as shown is correct.

## What I scanned

New for rev13:
- The full character-level diff, and the prompt re-read (unchanged).
- Brief offsets, lint, and the SQL vocabulary sweep.
- "Rotating shop" and free-coin records across Linear, Confluence, Docs, visible Slack and shop code.
- Trello comment shape and list rename history.
- Client assets for the C&W title.

Limits:
- The unchanged statements rest on my rev12 sweep and were not rescanned, so rev12's Slack keyword-sweep and image limits still apply.
- The `[Zombie Feature] Shop` doc is not visible to Julia, so no kill rests on it.
- ShopItem.cs shows a free claim in rotating-product logic, but it does not use the words "daily free coin". The tie to ZOM-539 rests on that code plus the Jun 3 Slack line.
- P2, P3 and P4 topics were not assessed. SQL was read, never run.
- I opened no other reviewer's file and nothing under R/work. In R/prev I opened only the rev12 SQL.
