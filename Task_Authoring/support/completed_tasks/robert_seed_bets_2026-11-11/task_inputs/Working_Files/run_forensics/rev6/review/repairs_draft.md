# Draft repair moves for rev7 (proposal only; S0r decides)

Prompt stays byte-identical. No new payees, issues, rows, steps or writes. Each move changes where a deciding fact lives or what a seeded note claims.

## M1. RET (MotMot return): keep the trap, give it a record a reviewer can see
Now: the only evidence is base data, two-year-old messages in #admin_foundersonly (C04UEQVDVB7/1712331718.859679 and /1712901800.684259). LANDED in the run. The platform /hardness reviewer checked Gmail and Linear for returns, never Slack, and scored the wrong total as correct.
Proposal: seed one dated record close to the clock, from a founder, that says the April 2024 wire to the engineer came back and was re-sent, using the engineer's name rather than "MotMot", in Slack but not in #winddown's top level. No amount. Candidates: a thread reply under a related existing post, or a recent message in a channel Robert is in.
Aim: catch rate of a third to two thirds rather than about zero, and a carrier the /hardness reviewer can read in the SQL.
Slots: X1, B1, R1, C1.

## M2. CORR (JPMorgan $4,000): swap the neutral note for a convincing wrong source
Now: ENG-2450 comment_10121682aae484f81a11f3f8b3e0ee94 (Leonard, 2026-02-13T00:26:36Z) "I approved this one in Aug 2024 but I can't remember what it was for". It is the only unknown note of 22, so it works as a beacon.
Proposal: Leonard's note gives a hedged wrong recollection that puts the money in Build by date, for example that it was an advance to a contractor. Arthur's existing mail "Chase records" (2026-02-13T16:26:44Z, to Leonard and Robert) stays as is and beats it: he made the transfer, it is later, and it states the fact.
Slots: X5, B1, R1, C4.

## M3. CLASS (Lauren Brooks): take the conclusion out of the note, keep a settling record
Now: ENG-2455 comment_990674712ad0127e26f780eadb5418ea "her contract had her running our paid UA on telegram, so she's marketing, not build", added in rev6 to answer a rev4 /prompt UGT 2 / Clarity 1 where the reviewer never opened the contract. FALSE in the run: the contract was never opened.
Proposal: delete that comment, and make the first note name the deal so a reader knows where to look ("the Telegram deal I sent out in Oct, $500 a month"), leaving the Drive contract f_20a0df3860bb5731d22f07 and the Slack offer thread C07C2866011 (Oct 2025) to settle the bucket under the doc's "Marketing is anything made or bought to get installs".
This is the only trap on ZM and CF: X8, B2, B3, S6.
Known risk: rev4 failed here; Exhibit A has five services including product advice.

## M4. ORPH (Leapblock): drop the free year split and the named wire
Now: seeded C05URGU759U/1770971846.479179 "2023 (from 13 Sep, the first one 33,290) 104,868; 2024 232,726; 2025 62,950; 2026 7,400. Total 407,944 over 30 wires." The run reconciled by year in one step.
Proposal: the post gives the total and wire count only, so a run must work out which wire is missing to assign it to a bet, using the Sep 13, 2023 Awaiting Approval notice for 33,290 and Arthur's "Done!" (C04UEQVDVB7/1694616951.239909).
Slots: X4, B1, C3.

## M5. ALIAS (Node Media): take the search key out of the note
Now: ENG-2444 comment_7453d8e60a3625923294c54e36a8667d "one payment when we closed the account, Jan 2025" supplies the word and window that find "closing our account with Node Media LLC".
Proposal: reduce it to the date, leaving the founders' message and the UA Sync invite to resolve the name.
Slots: X6, B1, R1.

## Left alone on purpose
- Doc rule sentences (close-out, receipt, own accounts, currency). Blind sweeps forced them to close forks; difficulty should come from facts to establish, not from removing the rules.
- OFF (Lucas, Western Union): live. The run's deliberate hunt missed; a date window aimed at another trap found it.
- CURR, T8, T9, T12-T17: FALSE as difficulty. Not rebuilt; not counted as loss channels.

## Rubric-stage surface fixes (not difficulty)
D1 any folder Robert owns; D2 either role and bind the recipient; D4 any reply in #winddown; X5 accept a none/own-accounts bucket; C1-C4 bind to their issue; S6 exclude total rows.
