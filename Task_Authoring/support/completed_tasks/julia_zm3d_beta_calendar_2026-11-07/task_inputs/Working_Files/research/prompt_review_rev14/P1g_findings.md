# Deep recheck P1 rerun on the rev14 SQL

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

SQL reviewed: sha256 edae63f3e83852f212c19892a9c9cf7304404b80db3178f92a470f301a598e13

**Result: `none`. F1 and F2 are both settled, and I could not break the changed text. Forks: none.**

Checked: 46 sentences (prompt 6, Frederick's message 6, thread reply 5, brief 29), 7 beats, 14 PNs Beta rows, 16 sheet columns, 6 writes.

## What changed

Only two sentences in Frederick's brief changed, plus the style offsets that follow from them. The prompt is identical, and every other SQL line is byte-identical to rev13.

- **Added to "Span and time base":** "Endless goes down as its weekly windows, with the daily reset noted."
- **Config locks, before:** "...moves to any time before it and its owner is told in a reply on the mail where they committed to it."
- **Config locks, after:** "...moves to any time before it and you tell its owner in a reply on the mail where they committed to it."
- **Offsets:** all 9 style runs land on their headings in the new body text.

## F1, reply to Brian: SETTLED

**Rule:** brief, Config locks: "A committed date that misses the lock moves to any time before it and you tell its owner in a reply on the mail where they committed to it."

Reading B was: no mail, flag it in the sheet only. It is now ruled out on each ground I gave:

| Rev13 ground for B | Status | Quote that kills it |
|---|---|---|
| The sentence was passive and named no sender | Gone | "you tell its owner" |
| Frederick, in copy, might be the one to tell him | Gone | "you" has one referent. The brief is shared only with julia.lawson@harmonygames.co; Frederick's message says "shared with you"; the only other second person is "the calls are yours". |
| Julia might keep this step for herself | Gone | Prompt: "Can you take it on for me?" |
| The prompt scopes the brief to "building it" | Gone | Prompt: "his working rules for building it are in the brief". The brief opens: "How I want the beta calendar built for the four buy weeks. The rules stay here". The reply is one of those rules, and nothing carves it out. |
| The prompt's list of writes omits it | Not a reading any more | The list has no "only". Eval 1 §2.1 check 2: "apply its instructions to the decisions it governs". |

- **Correction to my rev13 line:** I wrote "Missing: a prompt sentence". That was stricter than the standard, which accepts an incorporated rule, and the setup names the brief as a rule source. So the fix does not need a prompt change.
- **Basis:** RECORD (incorporated rule).
- **Clarity:** the write-action gate now passes.
- **What remains:** the reply is still absent from the prompt's own list. That argument rests on omission alone, with no text behind it.
- **Consequence downstream:** this is now a required write. OE and rubric must carry it and accept any date before the lock.

## F2, Endless Windows cell: SETTLED

**Rule:** brief, Span and time base: "Endless goes down as its weekly windows, with the daily reset noted."

- **Reading B (28 daily windows):** ruled out by "weekly windows".
- **Cell now:** Oct 6 00:00-Oct 12 23:59, Oct 13 00:00-Oct 19 23:59, Oct 20 00:00-Oct 26 23:59, Oct 27 00:00-Nov 2 23:59, with a note of the daily reset at 00:00 UTC.
- **Clipping:** none is needed, because Oct 6 is a Monday and Nov 2 is a Sunday.
- **Basis:** RECORD (incorporated rule).

## Attempts to break the changed text

All of these failed. The fork numbers continue from rev13.

**Endless sentence**

- F41: Weekly boundary | A: Mon 00:00 UTC | B: 12:00:01 AM Monday GMT, a different instant, from Robert's Endless doc f_9956263905ddb43d1500ff (domain-visible, Aug 14) | Settled by: calendar page, updated Sep 29: "weekly on Monday 00:00 UTC, both cron-scheduled in the CDK stack"; CDK ENDLESS_MONSTER_WEEKLY_SCHEDULE "0 0 * * 1"; brief "closing 23:59 UTC". The source is newer and it is the running config. [RECORD]
- F42: Does the hold reach Endless's weekly windows | A: no | B: yes, because Endless also has a weekly leaderboard and Vincent says only "the weekly leaderboard" | Settled by: Vincent in #zombie-bugs names modes when he means them: "Infinite boss leaderboard ... endless mode leaderboard" (Sep 15), and lists "Endless mode", "plague race" and "Leaderboard" separately (Aug 29). Rc_10 also lists "leagues, Endless" apart. [RECORD]
- F43: Leaderboard windows, now the one windowed beat with no cadence in the brief | A: 4 weekly | B: none stated, or reset instants only | Settled by: "A held beat keeps its usual windows and weeks"; CDK LEAGUES_SCHEDULE "0 0 * * 1", "PROD: every monday at 00:00 AM UTC". There is only one cadence, so no second set exists. [RECORD]
- F44: Endless on or off, as a permanent mode like Zombie Lane | A: on | B: off | Settled by the new sentence. Frederick's Zombie Lane reason is "no window or reset to plan", and Endless has both. [RECORD]
- F45: "Goes down" read as an outage | Not a real reading | The sentence sits in the time-base section, and the brief uses "put down" in the same sense. [RECORD]

**Reply sentence**

- F46: Whose owner | A: Brian | B: Robert, since the spec says "Owner: Robert (Product)" | Settled by: "the mail where they committed to it". Robert is not on that mail; Brian wrote "the date I am committing to". [RECORD]
- F47: Reply now or when the date passes | A: now | B: defer to Oct 31 | Settled by: "A committed date that misses the lock moves". The test is on the date, which already sits 7 hours after the lock, and the rule has no wait. Brian's Sep 26 mail: "If the new date is a problem on your side, reply on this mail." [RECORD]
- F48: More replies now that "you tell" is active | A: one, to Brian | B: other owners with dates | Settled by the sweep below: no other committed config date exists. Leonard's Oct 13 quests note says "if they are ready", which is not a commitment, and nothing ties it to a lock. [RECORD]

**Sweep behind F48:** 11,350 Aug-Sep messages in Julia-visible Slack channels and 304 messages in her mailbox export, searched for commitment, handoff, lock and freeze wording. Slack gave 22 hits, none a config date (they are mostly booster and win-streak "freeze" or "lock" talk). Mail gave none. Brian's two mails sit in the SQL and were read there.

## Reading A delta

- Endless row: as in F2 above.
- Write 6, the reply on Brian's Sep 26 mail, is now settled rather than open.
- Everything else in my rev13 Reading A stands.

## Carried forward

F3-F40 stand unchanged, because the universe did not change. I re-read the full brief and rechecked 19 injected quotes those forks rely on; all appear with the same counts in both SQL files. F28-F30 still rest on the same sentence: "moves to any time before it" is intact, so the rubric still must not pin a date.

## Edge values

Unchanged from rev13, except that Endless is now 4 windows only.

## Platform

Unchanged: the anonymized token in PNs Beta R7 and R14. No FD tags apply.

## Limits and disclosure

- I did not repeat the full universe scan. Only the two brief sentences changed, so this rerun covered the brief, the quote check, the sweep and the Endless boundary sources.
- My first command here read review_rev13's REVIEW_SETUP.md, 04_Prompt.txt and SQL for the diff, before I had read the setup that bars that folder. They were my own earlier inputs. I opened no other reviewer's work, and all later work used R14 paths and R14/work/p1g only.
