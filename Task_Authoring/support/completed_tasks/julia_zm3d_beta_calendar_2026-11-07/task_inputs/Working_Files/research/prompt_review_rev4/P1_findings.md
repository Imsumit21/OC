# Deep recheck P1 (Unique Ground Truth, Clarity): findings

Task date: Oct 1, 2025 (synth-cut). Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC). Inputs read verbatim: 00_Task_Assigned_Inputs.md (platform block), 02_Universe_Date.txt, 04_Prompt.txt, 01_Universe_Inject.sql (all 262 lines, never executed). Base data was read through the wrapper (`hg.py search …`) and directly with python3.12.

## Checked

- Prompt: all 6 of 6 sentences.
- Sources the prompt brings in, which I read sentence by sentence:
  - Frederick's DM (D05SD5QLG94 `8b090dec…`): 6 sentences.
  - His thread reply (`097c95c6…`): 5 sentences.
  - The brief "ZM3D beta live-ops calendar - working rules" (gdocs `f_7c3e91a4d2b85f60e1a9c4`): 36 sentences or lines (27 rule sentences plus the title, byline and 8 headings).
  - The UA plan deck that the brief points to as "my UA plan" (gslides `f_2b9d4e7a1c63f08d5e7b21`): 3 slides, 13 lines.
- Records each answer depends on, also read in full:
  - PNs Beta tab: 14 rows.
  - Brian's two mails: 10 sentences.
  - Robert's approval and pull messages: 5 sentences.
  - Vincent's re-test: 3 sentences.
  - The Oct 8 release event: 2 sentences.
  - 31 sentences of injected PR, Linear and Trello comments.
  - Confluence pages 6, 16, 20 and 27.

## Findings

DR1 | P1 | common_errors §2 "Which number, if two amounts or dates exist" / Eval 1 §2.1 both-fair figure | Prompt S3: "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me." The brief ("Config locks") says: "Every config a beat needs lands before its lock, read in server time (UTC). A committed date that misses the lock moves earlier and its owner is told in a reply on the mail where they committed to it." | See records below | Unique Ground Truth (one reported date) | BOTH_FAIR_FIGURE / acceptance range: not a UGT fail as long as the rubric accepts Wed Oct 29 or any handoff before Fri Oct 31 00:00 UTC

**Records:**

- **Confluence `pages[20]` `page_season_pass_spec` (persona-visible).** It says "Season config (tiers, rewards, theme) is authored in the live-ops tool and locked 24h before each season opens" and "production seasons reset monthly on the 1st at 00:00 UTC". So the lock is Fri Oct 31 00:00 UTC.
- **Brian's Sep 22 mail, Julia's inbox** (gmail `julia.lawson@harmonygames.co/<CAH4q9Zb2fK7xQe1M8sPnL3vT6wR0yDc@mail.gmail.com>`). It says "The config handoff we agreed with Product is for Wed Oct 29".
- **Brian's Sep 26 mail, Julia's inbox** (gmail `julia.lawson@harmonygames.co/<CAH4q9Zc8uV1nE5kJ2mRtP7aW3xQ9bLs@mail.gmail.com>`). It says:
  - "the November Season Pass config handoff moves from Wed Oct 29 to Fri Oct 31, 10:00 Istanbul time"
  - "Treat Fri Oct 31 as the date I am committing to and drop the Oct 29 one"
  - "If the new date is a problem on your side, reply on this mail."
- **GCal `evt_5c1e83a7d94b02f6c8e31a` (Julia's calendar).** It says "release window 18:00-19:00 Istanbul time", with start_ts 15:00Z. That confirms Istanbul is UTC+3, so Brian's handoff is Fri Oct 31 07:00 UTC. It misses the lock by 7 hours.

**The two readings:**

- **Reading A.**
  - Reply on the Sep 26 thread to Brian.
  - Move the handoff to the latest point that still lands before the lock: by the end of Thu Oct 30 UTC, which is before Fri Oct 31 00:00 UTC (03:00 Istanbul). This keeps as much of the "two extra days" he asked for as possible.
  - The Season Pass "Still to do" cell carries that date.
- **Reading B.**
  - Same reply, same thread, same recipient.
  - Move the handoff back to Wed Oct 29, the date Brian himself calls "agreed with Product". His Sep 26 mail invites a reply "If the new date is a problem".
  - The Still-to-do cell carries Oct 29.
- **What is the same.** Both make the same decision: the date misses the lock and moves earlier. Both make the same write (a reply on the Sep 26 mail), to the same destination and recipient (Brian, with Frederick possibly cc'd as on the thread). Both complete every explicit ask. The figure does not change what the agent does next.
- **What differs.** Only the new handoff date.

**Settled by: nothing.**

- The brief says only "moves earlier" and "lands before its lock". It names no target date.
- Brian's "drop the Oct 29 one" ranks his own two commitments. It does not say where a lock-driven move should land.
- Both values sit on persona-visible records: Oct 29 is stated in the Sep 22 mail, and the lock instant comes from the spec's two numbers.
- None of the five checks (newer source, authority, source identity, scope, same result) separates them.

**What would settle it:** a brief sentence or a dated record naming the target, such as "move it to the lock" or "back to the agreed Oct 29". Without one, the rubric must accept Wed Oct 29, or any handoff instant before Fri Oct 31 00:00 UTC. A row that pins a single date is overly specific.

## Edge values computed (no further finding)

- **Collect & Win first window.**
  - The release is Oct 8 at 15:00Z (start) or 16:00Z (end).
  - Either way it pre-empts the Wed-Thu window that opened Oct 8 00:00 UTC. Brief: "a window the release instant pre-empts does not count".
  - So the first window is Fri Oct 10 00:00 UTC (Thu Oct 9 17:00 PDT, which the brief allows as the same instant).
  - That gives 10 windows: Oct 10–12, 13–14, 15–16, 17–19, 20–21, 22–23, 24–26, 27–28, 29–30, and Oct 31–Nov 2 23:59 UTC.
  - Status is "starts late", not held. Brief: "A beat that is only waiting on that release starts late, it is not held."
- **Season Pass.**
  - The October season runs Oct 1 00:00 UTC to Nov 1 00:00 UTC.
  - The November season opens Sat Nov 1 00:00 UTC (Oct 31 17:00 PDT).
  - Whether the "First window" cell shows the running October season or Nov 1 is presentation only; both seasons are listed either way.
- **Lock edge, UTC vs PT.**
  - Brian's 10:00 Istanbul is exactly Fri Oct 31 00:00 PDT. Read against a PT "day before" freeze, the handoff would sit exactly on the lock instead of missing it.
  - That PT reading is ruled out by the brief: "read in server time (UTC)".
  - The UTC+2 misreading (08:00Z) also still misses.
- **Endless resets.**
  - Daily resets at 00:00 UTC: 28 in the span.
  - Weekly resets Monday 00:00 UTC: Oct 6, 13, 20 and 27, so 4.
  - Oct 6 00:00 is included because the brief says the span "covers Mon Oct 6 00:00 UTC".
  - Source: Confluence `pages[27]`.
- **Pushes.** The PNs Beta tab of "Push Notifications Zombie Match" (gsheets `sheets_spreadsheets[220]`) has 14 rows. Leaving off the four Frederick names gives 10 lines.
  - **2 go out:** "When lives are recharged" and "7 Days Lapsed". Both are Ready and LIVE, and neither copy names the game.
  - **8 are held:**
    - Quests: Not Ready.
    - "1 Days Lapsed" and FTUE: copy says "Puzzles vs Zombies". The brief says "names the game only as Zombie Match 3D", and Confluence `pages[6]` says the game was "listed as 'Puzzles vs Zombies' until the July 2025 store rename".
    - Win & Collect: Not Ready, WIP, and a non-ZM3D event name.
    - Plague Race: WIP.
    - Login Calendar: Not Ready, WIP.
    - Season Pass: Not Ready, WIP.
    - Weekly Leaderboard: WIP.

## Candidates checked and settled (no finding)

- **Push sheet identity.** Only the ZM sheet's PNs Beta has the Ready/Not Ready "Status" column that the brief's "Ready and LIVE" rule needs. The Domino sheet (`sheets_spreadsheets[73]`) has no such column and no Plague Race row. The brief's "the translated tab is the old Domino set" describes the ZM sheet's "PN BETA Translated" tab.
- **Calendar sheet.** Frederick says "Put it in the calendar sheet in your ZM Live Ops folder". That is `f_e4a17c90b3d25f6a8c1d73`, Julia-owned, in `d_5f2c8e1b7a94d03c6e2b58` "ZM Live Ops". The domain-visible "LiveOps Event Calendar.xlsx" is not Julia's and is not in that folder.
- **Calendar ticket.** It is ZOM-78 "Event Calendar For Zombie Match 3D". Frederick's comment `cmt_zom78_1` on it says "Let us use this ticket for the ZM3D beta live-ops calendar instead of opening a new one. Link the sheet here when it is ready." ENG-2240 "Web interface for the liveops calendar" is not it.
- **"His message" includes the thread reply.** It has the same author and thread and says "Two things the brief does not spell out."
- **Halloween one-off is off.**
  - The brief says the approval comes "from Product … his later word is the one that counts".
  - Robert is Product: the Season Pass spec says "Owner: Robert (Product)", and so does the ZM3D GDD (`pages[16]`).
  - Robert's later DM (D05GU6L0XFH `58d06bd5…`, Sep 30) says "pulling my ok. Take it off the beta calendar". This supersedes his Sep 18 approval in #zombie-art.
- **Weekly leaderboard is held.**
  - Vincent, Sep 30 in #zombie-match3d, where Julia is a member: "it still does not start a new week. I killed the app and reopened it twice … Same on the second device."
  - This is newer than Douglas's Sep 23 ZOM-429 comment "they land in the new week fine".
  - ZOM-429 itself says it "doesn't start the new one or let me claim my rewards", and ZM-Liveops-Docs/Leaderboards.md says "Claim weekly reward (triggers new session)".
  - That meets the brief: "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart. An established failure holds it".
- **"Its ticket" for the hold note is ZOM-429** (assignee douglas@). ZOM-71 "Weekly leaderboard system" is Done with no assignee, so it fails the prompt's "so the owner picks it up".
- **Leagues are the weekly leaderboard, not a separate running beat.**
  - match3d-backend#16 is titled "Leaderboards: Weekly leagues fixes".
  - ENG-2076 says "isn't reflected on weekly league. It needs to wait for the new weekly session".
  - Confluence `pages[27]` lists "Weekly Leaderboards" in its table and "Leagues" in its overlap note for the same game.
- **No "Hold until" date exists on any record.** Hold-until stays "no fix date on record, held through the span". The Oct 8 release does not cover it: Arthur's #470 comment says "leagues … schedules are already running on prod", and the release only moves windows "still on the DEV stack". The rubric must not require a specific instant.
- **Change-request hold clause holds nothing.** No CHANGES_REQUESTED review exists on any Aug–Sep 2025 PR in match3d, match3d-backend or liveops. The only ones on these repos are match3d#303 (Jul 16, later approved and merged) and match3d-backend#4 (Jun, merged). No human review comment from Aug–Sep requests an unresolved change. This holds under any definition of "the Aug-Sep live-ops cohort", which no record defines.
- **Held pushes are not held beats (no extra ticket notes).** The brief says "Hold a beat only when players provably cannot enter, score or claim…". The push rule is separate: "Anything else is held, with what is missing."
- **The reply to Brian is required.** Prompt S3 adopts the brief's working rules, and the brief names the write: "its owner is told in a reply on the mail where they committed to it". The thread is the Sep 26 mail, where Oct 31 was committed: "reply on this mail".
- **Still-to-do inclusions.** Newer records settle each one:
  - The daily-gift frame shipped: Samuel's #471 comment, and ZOM-432 is Done.
  - ZOM-526 Season Pass polish is out: Brian, Sep 26, "does not have to land".
  - The Collect & Win icon animation is in: Marcus, ZOM-465, Sep 30, "still to do on my side".
  - Analytics tickets are out: ZOM-566, ZOM-552, ZOM-549 and ZOM-442.
- **The quest set on Mon Oct 13 does not trigger the lock rule.** It is a Trello commitment by Brian, not a mail commitment. Confluence `pages[27]` says "There is no technical content lock … The 24h season-pass freeze … is a process control". The brief asks only whether the quest beat is in and whether its push is ready.
- **Boss Arena and Infinite Boss are off.** ZOM-487 is titled "Infinite HP Boss Arena", and the brief says "Boss Arena is off this calendar". Zombie Lane is off per Frederick's reply.
- **No window dates for Plague Race, quests or daily gift.** The brief governs: "put down whether the beat is in and whether its push is ready, not its window dates."

## Topic results

- **Unique Ground Truth:** one fork (DR1). I propose it as BOTH_FAIR_FIGURE / acceptance range, so it is not a fail as long as the rubric accepts Oct 29 or any handoff before Fri Oct 31 00:00 UTC. No other UGT finding.
- **Clarity:** no finding. No two readings lead to different write actions. DR1 changes only the date inside the same reply. Under §2.1 a both-fair figure is not scored again under Clarity. The prompt has no "I'll" statements.

Fork list line:
- F1: Brian's November Season Pass handoff, moved earlier | Reading A: by the Fri Oct 31 00:00 UTC lock (end of Thu Oct 30 UTC) | Reading B: back to Wed Oct 29 ("agreed with Product", Sep 22 mail) | Both fair: Oct 29 or any handoff before Oct 31 00:00 UTC (BOTH_FAIR_FIGURE / range); the rubric must accept either.

Platform defects: none observed in the records P1 relied on.
