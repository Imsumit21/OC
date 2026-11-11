# P2 deep recheck findings, rev13 (Eval 1 Phase 5, blind)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
SQL reviewed: sha256 1f2175a297fd390960f22c3767f790fc980a881023affa6ece970745fb40289b, read only, never run.
Previous: rev12, sha256 b5ccbfa577fc9f2c8f6eb3098f8d62a16623d799f41d11285de8227f1bed60d3. Prompt unchanged (diff empty).

## Result

Fail-level: 0. Low-impact: 0. Advisory: 12 items.
Cross-Service Coherence: DR1 no longer counts as low-impact, so P2 finds nothing that scores. P2's view is PASS, not NON-FAIL.
Feasibility, Persona access, Data exists, Tool use and cross-service: no finding, unchanged.

Checked: all 7 changed lines, which are 5 of the 111 statements. Lint on this SQL: 111 statements (81 inserts, 30 updates), 0 FAIL, 0 CHECK, 0 INFO. The other 106 statements are byte-identical to rev12, so their rev12 checks carry over.

## What changed

| # | Statement | rev12 | rev13 |
|---|---|---|---|
| C1 | Brief, Scope | "the shop rotation is not a beat" | "the rotating shop is not a beat" |
| C2 | Brief, Push copy | "Anything else is held, with what its row is missing." | "Anything else is held, with which of those its row is missing." |
| C3 | Brief, style_runs | Config locks 2863-2875 | Config locks 2873-2885 |
| C4 | GitHub `#468#rc_38` | see DR1 | see DR1 |
| C5 | Slack mirror `78aa8ed7...` | same text as C4 | same text as C4 |
| C6 | Linear `cmt_zom465_3` | "does have to land before the beta" | "does have to land before the event runs" |
| C7 | Trello action `68dac8204f...` | no `list` key | adds `"list":{"id":"6851a674975da1fe76e70d93","name":"BETA: Sep 30"}` |

## DR1: closed as low-impact, one advisory residue

rev12: "The Collect & Win vials that spawn in the levels are still the first-pass models. The final vial models are missing and need to be in before the beta, Claire has those on her list."

rev13: "The Collect & Win vials that spawn in the levels still need their final models before the event runs. Not a blocker for this PR, Claire has those on her list."

Base side, unchanged: `741527de5c` 2025-08-14 claire changed `Skull_Potion.fbx` (LFS oid `c1fad70e...` to `80a6dd4e...`) after `a4872cfbec` 2025-08-08 "Collect&Win Items". DM D076Y0SDV18, Claire 08-12: "değiştireyim sıkıntı değil". Notes `f_b7aae618602a7ccc0cc9a7`, Sep 29: "Um, I'm working on some leave objects."

Why it closes: DR1 rested on the descriptor "first-pass", which the Aug 14 revision did not fit. That word is gone from both the GitHub row and the mirror (0 hits). What remains is a dated need statement. A commit six weeks earlier cannot contradict it, and no base record calls the repo models final. This also meets the rev12 fix text: the first-pass claim is removed, and the ask stands as an art need raised after Aug 14.

Residue (advisory R1): "Claire has those on her list" still has no record on Claire's side. Her 13 open Linear tickets have none on vials, and her Sep 29-30 updates are about other objects. That is silence, not contradiction, and the item stands on Arthur's flag whether or not the list exists. No graded value moves.

Added benefit: "Not a blocker for this PR" fits the review state (COMMENTED) and the merge 37 minutes later by another engineer. rev12's text did not say this.

## Break attempts on each change

- **C1, no finding.** "Rotating shop" is the base term: ZOM-348 "Rotating Shop Discount Issues", doc "[Zombie Feature] Shop" ("uses a rotating shop logic"), code `Assets/Store/Store/RotatingShopManager.cs`. rev12's "shop rotation" has 0 hits in Slack, Linear, Docs and Confluence, so this improves the match. No CDK schedule exists for it. Same length, so offsets hold.
- **C2, no finding.** "Those" are Ready, LIVE, game name and event name, and the sheet column "What is missing" fits. All 8 held rows can state it from the data: row 2 Ready; rows 5 and 7 game name ("Puzzles vs Zombies"); row 8 Ready, LIVE and event name ("Win & Collect"); row 10 LIVE; rows 13 and 14 Ready and LIVE; row 15 LIVE. Frederick's thread reply still narrows the naming test to wrong names, with no clash.
- **C3, no finding.** Body grew 3090 to 3100 characters. All 9 runs land on their headings, including (2873, 2885) "Config locks".
- **C4 and C5, no finding beyond R1.** Mirror text equals the GitHub text after `&amp;`. Path, timestamp, review id and discussion id are unchanged. Voice matches Arthur's other notes ("Fine for this PR", "The client side in this PR is fine").
- **C6, no finding.** Echoes the brief's "before it runs". Marcus's c2 and git still support it: no Collect & Win clip exists in the repo.
- **rev12 to rev13 wording split, no finding.** Needed items now say "before the event runs" (3 rows, one a mirror). Not-needed items keep "before the beta" or "for the beta" (3 and 10 hits, of which 4 are the calendar copies and 1 is Frederick's message). No item is on both sides, and ZOM-526 and ZOM-566 both say the event runs without theirs, so nothing can slip between Oct 6 and Oct 10.
- **C7, no finding beyond A9.** Key order now matches base (`board, card, idCard, list, text, textData`), and 54 of 56 base comment actions carry `list`. "BETA: Sep 30" matches all 71 base actions on this list since the 2025-09-12 rename.

## Advisory only (not scored)

| # | Item | Status | Both sides | Why advisory |
|---|---|---|---|---|
| R1 | Claire's list | New, from DR1 | rc_38 "Claire has those on her list"; no Claire-side record | Silence. No value moves. |
| A1 | Oct 8 vs Sep 29 meeting | Unchanged | GCal created 09-24 "go live with this release"; notes "maybe that's something Douglas can help me with today" | Undated plan. Later visible records settle it: #470 rc_10, ZOM-563 18:17Z. |
| A2 | Season Pass strip art | Unchanged | #472 rc_1 "still shows the October range"; no date field in `LiveOps/SeasonPass` code, art is LFS | Unsupported, not contradicted. |
| A3 | Private QA notes | Unchanged | D07GMT8NVM2 "nothing serious ofc"; self-DM "Kill zombie quests don't work" | Hidden from Julia, not provably a hold. |
| A4 | Bottle VFX DM | Unchanged | D076V3NB6P7 "Could you polish the bottle vfx" | Polish, not stated as needed. |
| A5 | Change-request clause | Narrowed by C4 | Brief "unresolved change-request review blocker"; only CHANGES_REQUESTED since 07-15 is #303 | Empty set. "Not a blocker for this PR" now also shuts out reading rc_38 as one. "Aug-Sep live-ops cohort" stays undefined; wording is P1's. |
| A6 | SC-57 | Unchanged | Injected reply in archived #zm-collect-win | Known issue, no value. |
| A7, A8 | Branch prefix; "All our PNs are local" | Unchanged | As in rev12 | Base mix, no value. |
| A9 | SC-13 | Touched by C7 | Injected action says "BETA: Sep 30"; list name is "BETA: Oct 10" | Known issue. The row joins the action side, as all 71 base actions do. The task uses no date from it. Not scored. |
| A10 | Client delivery of the art | Touched by C4, C6 | "before the event runs" (Oct 10 00:00Z); vial and icon are client assets; builds #50 and #135 were cut Sep 30; Slack 09-26 addressables are local; no record dates the next build | Not an inconsistency. A later build is acknowledged ("rides the next store build"), and the start rule uses server windows only. rev12's "before the beta" was the weaker fit, because the buy starts on the Sep 30 builds. |
| A11 | Trello card 10 complete | Not new, missed in my rev12 report | Base: Leonard ticks "Win and Collect" `dueComplete` true, 2025-09-30T16:40:13Z. rc_38, rc_10 and ZOM-465 show open items around it | Considered as State / Lifecycle and rejected. The tick marks the feature built, which matches Confluence ("Built for the end-of-September beta submission ... not yet live") and base's own POD note that prod deploy was outstanding. The brief separates the two ("not when its client PRs merged"). No value depends on it. |

## Topic lines

- **Cross-Service Coherence:** no scored item. No State / Lifecycle, no Quantitative.
- **Feasibility: no finding.** Writes and tools unchanged. C2 adds no new field need.
- **Persona access: no finding.** No changed record moves visibility. Hidden record line: none.
- **Data exists: no finding.** "Rotating shop" resolves in base.
- **Tool use and cross-service: no finding.** Each named service still changes a graded fact.
- **Derived columns:** none read.
- **Date-slip:** none. No date changed. "Mon Oct 13" and the Oct 8 instant are untouched.

## Checked and consistent (changed text)

- Old strings gone: "first-pass" 0, "need to be in before the beta" 0, "shop rotation" 0, "with what its row" 0, "does have to land before the beta" 0.
- rc_38 and its mirror agree. Timestamps, ids and thread counters are unchanged.
- Hashes match the setup. Only lines 115, 125, 127, 157, 170, 210 and 259 differ.

## Evidence limits

Same as rev12: `catalog.json` has no return schemas, and LFS blobs are not readable.

Platform defects: none.
