# Rev1 delta review: changed seed text, items 1 to 6

Clock: 2026-02-14 00:00 UTC, normal universe. Slack export ends Feb 13 10:03 UTC. Written 2026-11-08 by a cold delta reviewer.

Read: `seed_snapshot.md`, `solver/truth.json`, `plan/sweep_dispositions.md`, the three rev1 sweeps, and the seeded rows in `01_Universe_Inject.sql` (to confirm thread fields and sharing). For finding M3 only, `01_Gradable_Surface.json` (selectors). Base reads went through `hg.py search` only.

Scope: items 1 to 6, as the coordinator narrowed it. Items 7 to 9 (Linear comments, deck, Trello, origin lines, Contacts, timestamps) belong to another agent. Two incidental notes for that agent are at the end.

Result: 0 BLOCKER, 3 MAJOR, 5 MINOR. The KPMG totals (item 4), the states (item 2) and Robert's reply (item 6) hold up.

## MAJOR

### M1. "once the sheet is right": send it, or hold it for Leonard?

Sentences:
- Notes: "Griffin's partner gets a heads-up as a reply on the Feb 12 Board position thread, with what we still need from Griffin. That one can go out once the sheet is right"
- Project: "KPMG's confirmation goes back as a reply to all once the sheet is right."

Readings:
- **A (intended): send.** The run builds the sheet and checks it, so it counts as right. Both replies are then sent.
- **B: draft and wait.** "Right" is a check the run cannot sign off on itself. Three things push this way:
  - Every other gate says "done": "They stay in Backlog until the sheet is done" and "States once the sheet is done". Two different words invite two different meanings.
  - The sheet goes to Robert and Arthur, which reads like a review step.
  - The Trello card "Nothing goes out until the sheet is right" is a team gate on the founders' board.
  - So a careful run (and Opus is careful about sending to an outside auditor) leaves both replies as drafts.
- KPMG is also the only send with no named sender. The sentence before it says "I'll pass it to Sunset myself", but the KPMG sentence is passive.

What moves: the `kpmg` deliverable (35 weight) and the `griffin` deliverable (4) are read only from `gmail_reply_to_message`. Under reading B, all 39 points fail. Separately, surface row G1 is titled "heads-up drafted to Griffin", which contradicts the seed's "can go out". The rubric writer should not inherit that title.

Smallest fix:
- Use "once the sheet is done" in both sentences.
- Project: "Send KPMG's confirmation as a reply to all once the sheet is done."
- Retitle G1 "heads-up sent to Griffin".

### M2. "Each note says what they hold." and the family note (F2)

Sentence (notes): "Each note says what they hold." Read with the thread reply "one note to whoever has always handled it for a family covers the rest of the family's lines".

Readings:
- **A (literal):** "they" is the person the note goes to. The note to [PERSON_NAME_52949] states their own 25,432.
- **B:** a family note says what the family holds: three lines of 25,432, or 76,296.

What moves: F2 (weight 3) needs `76,?296` or `three … 25,?432` in the notes. A run that follows reading A writes the correct note and fails F2. No seeded sentence asks for the family total, so under A, F2 grades an added condition.

Smallest fix, in the family rule's own home with no new pointer, on the thread reply: "...covers the rest of the family's lines and says what each of them holds, so they need no note of their own". The other option is to drop F2.

### M3. Sunset's "(for options, what's vested)" against a single "Shares held now" field

Sentence (Sunset): "One line per holder of stock or options, with what each holds today (for options, what's vested) and any last day".

The surface's schedule has one numeric holding field, "Shares held now". Its meaning shifts by row:
- K4 to K7 (20 weight) want stock only for the four advisors: 25,432 or 50,865.
- P_live_* (5) want vested options in the same field for staff lines, for example ENG-2450 at 17,802.

Sunset's wording asks for stock and vested options per holder, so two honest sheet shapes follow:
- **A: stock and options in separate columns.** "Shares held now" can then map to the stock column (staff lines read 0, so P_live fails) or to the options column (advisors read 6,104 or 61,038, so K4 to K7 fail).
- **B: one "holds today" figure per holder.** A correct run that adds stock and vested options for the advisors writes 31,536, 81,383 and 86,470. Those are exactly the owner-list numbers the ADV trap expects a careless run to write, so the grader cannot tell a right run from a trapped one.

The seed text is fine. The fault is in the surface, and the changed sentence now exposes it.

Fix (surface, no seed edit):
- Add the truth's "Options now" as its own column.
- Grade K4 to K7 on the stock figure and P_live on the options figure.
- Accept a cell that shows both figures.
- Fail only a bare owner-list figure with no split.

## MINOR

| # | Sentence | Second reading, and what moves | Smallest fix |
|---|---|---|---|
| m1 | Notes: "Notice route: the email we have, unless a document says otherwise." | IRA §6.5 (gdocs 90) is a document that "says otherwise" for every Series Seed holder: Schedule A addresses, email consent, and "if notice is given to Stockholders, a copy ... to Orrick". A careful run may write "IRA: email, copy to Orrick" on 12 investor rows, Griffin included. No graded row reads a non-TOR or non-Segerstråle route (only S1 to S3), so nothing moves today. | Keep. Tell the rubric writer never to grade the literal word "Standard" on investor rows. |
| m2 | Thread: "And the sheet goes to Arthur as well as Robert, the rest of my notes stands" | Voice. Arthur is in the thread and replies "sounds good". In #winddown, Leonard @-mentions Arthur (/190, /199, /200) rather than naming them in the third person. The notes doc is shared with no one (SQL: `shared_with_emails_json` '[]'), so "my notes" means nothing to Arthur. D4 does not move. | "And the sheet goes to <@EMPLOYEE_0025_SLACK_ID> too, not just Robert, the rest of my plan stands" |
| m3 | Thread: "One thing on the angels: one note to whoever has always handled it for a family covers..." and "Mark those lines Covered on the sheet..." | Voice. The text is rule-shaped and addressed to nobody in a founders' channel, and Leonard's #winddown register is short and lowercase. It names no holder, which is right. It does announce that a family exists, but the rule has to live somewhere. | Optional: "one thing on the angels, for a family just one note to whoever always handled it for them, the others don't need their own" |
| m4 | Notes: "The three of us only go in the totals." | Is a holder count a "total"? Read that way, the founders join Sunset's "count of holders", taking Already told from 4 to 7. This is weak: the count is by label, and founders have no row or label. No graded row moves. | None needed. To close it, add ", not in the count". |
| m5 | Robert's sign-off "Thanks\n[PERSON_NAME_0054]"; Sunset's signature block | Cosmetic only. Base Robert mostly writes "Thanks\n\n[PERSON_NAME_0054]", though the one-line form also occurs. Base Sunset blocks put a blank line between signature lines (1856675475513544349 /messages/8). | Add the blank lines if any rows are rebuilt anyway. |

## What passed, by item

**1. Notes doc (apart from M1, M2, m1, m4).**
- "besides the Sunset onboarding" matches #winddown /197 and /200.
- "that one is the vendor and termination papers" matches the Wind Down folder (d_e5caf6a8…): Task List, Termination Notices, Employee Termination Letters.
- The archive sentence matches /190 bullets 3 and 4.
- "Feb 12 Board position thread" picks out one thread: 1856958794180374704, PERSON_4337 (Senior Partner), Feb 12 22:05Z and 22:14Z.
- "from one of the three of us" is well defined:
  - #winddown's named members are exactly Robert, Arthur and Leonard. The other IDs (PERSON_6089, U04…) are unnamed.
  - The owner list's three 2,000,000 holders are Arthur Blake, [PERSON_NAME_0055] and Leonard Hayes.
  - The phrase correctly rules out the Carta notices sent to ES-14 and ES-18.
- "if they get one" closes ES-16's unanswered question.
- "One row per issue" settles 26 rows.

**2. Project description (apart from M1).**
- It settles the state of all 26 rows:
  - Canceled 6: ENG-2451, 2452, 2454, 2455, 2461, 2462.
  - Todo 14: six first notes including [PERSON_NAME_52949], six date notes, two full notes.
  - Done 6: the two Griffin funds, Segerstråle, Nebojsa, and the two Covered lines.
- "Canceled included, say why" covers the LC_* rows.
- "I'll pass it to Sunset myself" is consistent with Leonard's reply at 18:19:02Z, and the project was updated after it, at 18:21:46Z. No row grades a Sunset share.

**3. Family reply.**
- The thread is real, per the SQL: the replies carry thread_parent_id e3e198… and thread_ts_legacy 1770934638.035469, and the parent has reply_count 4 and latest_reply 1770949437.902269.
- The replies sit 02:21Z to 02:23Z: after the notes (01:05:41Z) and before the export end, so "the rest of my notes stands" is in order.
- It is fair and reachable: the notes name this parent twice ("where I left things today", "reply under my list").
- "Mark those lines Covered on the sheet in place of a label, and count them that way" settles three things:
  - Label: Covered.
  - Count: Covered 2, separate from Closing 6.
  - State: Done, through the project's "no own note" rule, with a reason comment.
- It does not clash with "at most one note per person": [PERSON_NAME_52949] gets one note, the brothers none.
- "One thing on the angels" fits bullet 2 of /197.
- There is only one family: the 2023 mail from PERSON_2260 (1770141224265557526) lists all three lines.

**4. KPMG item 2 and the follow-up: 243,757 is the only fair total.** The Carta notices give these as-of dates, vested figures and last days:
- Terminated Dec 31, 2025: ES-1, ES-4, ES-15.
- Terminated Oct 24, 2025: ES-3, ES-5, ES-16, ES-17 (last days Jan 24 and Jan 28, 2026).
- Terminated Nov 21, 2025: ES-14.
- Terminated Jan 30, 2026: ES-7, ES-12, ES-13, ES-18.
- Already lapsed: ES-2 (Nov 1, 2024) and ES-6 (Jul 16, 2025).

| Total | How it arises | Closed by |
|---|---|---|
| **243,757** | 81,702 (eight lines terminated on or before Dec 31, at vested) + 58,291 (four Jan 30 lines at full grant) + 103,764 (advisors) | (truth) |
| 266,436 | The Dec 31 terminations counted at full grant (+22,679) | The follow-up: "a termination effective on the as-of date itself counts as of that date" |
| 268,772 | The Jan 22 term-sheet figure, as recorded (ES-14 also at grant, +2,336) | "regardless of when recorded" |
| 214,235 | Jan 30 lines at vested (−29,522) | "each effective date as Carta shows it": Jan 30 is after Dec 31, and unvested options are outstanding |
| 189,228 | The Oct 24 lines dropped (−54,529) | Their last days (Jan 24 and 28, 2026) fall after Dec 31. "Last day has passed" is a today rule |
| 182,719 | Collins dropped (−61,038) | No Carta termination for ES-9; "as Carta shows it". This is fork M2, already kept; removing the "service ended" wording made it weaker, not stronger |
| 259,525 | ES-2 (3,052) and ES-6 (12,716) counted | "outstanding": both last days passed before Dec 31 |
| 162,055 | New test: "counts" read as "the line is gone at termination" | Not compelled. The notices show "Vested ... Last day to exercise", and "If a line's last day has passed, it holds nothing" implies the line holds something until then |

An honest reader does know that a terminated line counts at what vested. The Carta notices, the notes' last-day rule and Sunset's parenthetical all point there. A2 is 9,051,879 + 243,757 = 9,295,636.

**5. Sunset (apart from M3).**
- "(for options, what's vested)" agrees with the truth. The advisor agreements (gdocs 295, 490, 570) vest monthly over two years from Jul 21, 2023, so the advisor grants were fully vested before Feb 14, 2026, and 103,764 is right.
- "what each still needs to hear from you" maps onto the labels and no longer echoes Leonard's private word "owed".
- Leonard's "I'll get you the sheet next week" matches the project's "I'll pass it to Sunset myself".
- "Quick one from legal for the intake" fits Sunset's own Feb 11 mail ("we'll send over our onboarding intake", "our legal team will create your Plan of Dissolution").

**6. Robert's reply.**
- Greeting: "Hey [PERSON_NAME_0112]," is the base form (quoted in 1767975483498350973).
- The To header matches the base form.
- The quoted tail matches base message [0] exactly: "Fri, 11 Aug 2023 13:00:43 -0700", "Thanks!!!".
- "we've had to let the team go" is consistent with the Feb 11 letters, the Carta notices, and the work and all-hands still going on Feb 12 and 13.
- "backing us from the very start" fits the Aug 2023 wire and an advisor agreement dated Jul 21, 2023.

## Incidental, for the item 7 to 9 agent (not reviewed further)

- **ENG-2459:** "Last written contact I have before Feb: Nov 23, 2025, #dd-road-to-sub-250mb" is stale. Vincent posted in that same channel on Nov 25 and Nov 28, and in #god-bugs on Dec 2, 2025. Leonard is a member of both channels. No write moves.
- **ENG-2442:** the comment's locator (1836075678772806708, Jun 27, 2025) is a mail from patrick@harmonygames.co. The 2023 family list gives that address to Patrick Lewis (ENG-2444), whose comment says May 18, 2024. This is the known address collision, and the comment makes it more visible.
- **ENG-2440:** "Jan 30, 2026, DM" now points straight at Segerstråle's DM. TOLD on Segerstråle is close to free, so re-estimate its catch rate.
