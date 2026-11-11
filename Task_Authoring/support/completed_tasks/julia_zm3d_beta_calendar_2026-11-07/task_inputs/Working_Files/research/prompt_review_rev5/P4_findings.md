# Deep Recheck P4 · Wording

Stage: /prompt (Eval 1 Phase 5). Pass P4, blind to the main review and other passes.
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Inputs read: R/inputs/04_Prompt.txt, 00_Task_Assigned_Inputs.md (platform block), 02_Universe_Date.txt, 01_Universe_Inject.sql (read only, never executed).

## Findings

none. Sentences checked: 6 (all of them; 100 words, 2 paragraphs).

| # | Sentence |
|---|---|
| S1 | "Frederick messaged me yesterday asking for the live-ops and push calendar for the Zombie Match 3D beta, the four buy weeks that start Monday the 6th." |
| S2 | "Can you take it on for me?" |
| S3 | "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me." |
| S4 | "It goes in my live-ops calendar sheet." |
| S5 | "If a beat ends up held, leave a note on its ticket so the owner picks it up." |
| S6 | "Once the sheet's done, link it on the calendar ticket and send Frederick the recommendation he asked for." |

## Topic lines

- **Search hits (common_errors §3).** No finding. Case-insensitive counts on the prompt text: `linear_` 0, `gmail_` 0, `slack_` 0, `MCP` 0, `tool` 0, `First` 0, `Then` 0, `Finally` 0. The prompt has no non-ASCII characters.
- **Catalog tool names, MCP or "tool" wording (§6.6, Eval 1 §1.3.4).** No finding. The services are referred to only by natural business nouns: "messaged", "message", "brief", "sheet", "ticket". There are no parameter names and no MCP server names.
- **First / then / finally step list (§6.6, Eval 1 §1.3.1).** No finding. There are no sequencing words and no numbered steps. S6's "Once the sheet's done, link it…" states a real dependency: the link needs the sheet to exist. It does not prescribe a procedure. Frederick's own ask (SQL line 11, slack `bca784379e7dbca9e64e79a64dfefbba`) sets the same order: "Put it in the calendar sheet … and link it on the calendar ticket. Then send me your recommendation back here".
- **Bolt-on sentence (§6.6, Eval 1 §1.3.2).** No finding. S1–S4 frame the one deliverable. S5's ticket notes depend on the calendar's held status. S6's link and recommendation are both in Frederick's ask. No sentence is an unrelated ask. S2 is the delegation line, not an added task.
- **Opaque id or exact timestamp the task does not need (§6.6, Eval 1 §2.7).** No finding. There are no ids, filenames or clock times. "Monday the 6th" and "yesterday" are natural dates. They resolve to Oct 6 and Sep 30 against Wed Oct 1, and they match Frederick's "Mon Oct 6 through Sun Nov 2".
- **Named cause (§6.7, Investigation).** No finding. The prompt states no cause for any hold, slip or still-to-do. S5 is conditional ("If a beat ends up held") and names no beat and no reason. The leaderboard failure (ZOM-429, plus the restart re-test in #zombie-match3d, SQL line 19 `b5f2955c2e154efc6835946ecfe1758e`) and the Collect & Win DEV-stack delay (SQL line 138 `match3d#470#rc_10`) are left for discovery.
- **Trap hint or riddle (Eval 1 §2.7, Riddles override).** No finding. I checked every trap seeded in the SQL against each sentence. None is pointed at:
  - Robert's Halloween approval and later pull-back (SQL lines 15 and 17).
  - Brian's Oct 29 to Oct 31 handoff change (SQL lines 23–80).
  - Douglas's "not blocking" on ZOM-429 against Vincent's failed re-test after restart (SQL lines 165 and 19).
  - The Collect & Win window pre-empted by the Oct 8 release (SQL lines 82–88 and 138).
  - The ZOM-432 frame already shipped (SQL line 187).
  - The four push rows to leave off and Zombie Lane (SQL line 13).
  - The Mon Oct 13 quest set (SQL line 237).

  "ends up held" is a plain conditional. It does not hint that a ticket's own status is wrong, or which beat is affected.
- **Hidden destination the persona would know (Eval 1 §1.5 Ambiguity, §2.7).** No finding. Each place the output goes is either named naturally, or left to the data only where finding it is the task and a persona-visible record names it.
  - S4 "my live-ops calendar sheet": the SQL sheet `f_e4a17c90b3d25f6a8c1d73` "ZM3D Beta Live-Ops Calendar" (lines 130–133) is owned by julia.lawson and sits in her folder `d_5f2c8e1b7a94d03c6e2b58` "ZM Live Ops". Frederick's DM names it: "the calendar sheet in your ZM Live Ops folder". The only other live-ops calendar sheet in the base, gdrive/data.json `drive_files` `f_b04156e116437611a5014a` "LiveOps Event Calendar.xlsx", is owned by "Resource: -6481757892984311338" and only shared with Julia, so it is not "my".
  - S6 "the calendar ticket": linear/data.json ZOM-78 is "Event Calendar For Zombie Match 3D" (Backlog). Frederick (`usr_175c0d7bc72ed244` = frederick.stone) commented on it at SQL line 190, `cmt_zom78_1`: "Let us use this ticket for the ZM3D beta live-ops calendar instead of opening a new one. Link the sheet here when it is ready." The other calendar-titled issues are ENG-2240 "Web interface for the liveops calendar", ENG-2238, ENG-2261 and ENG-2311. None of them is the ZM3D calendar ticket. "The calendar ticket" is Frederick's own wording and a natural business name.
  - S6 "send Frederick the recommendation he asked for": the recipient is named. The place is named in his message, slack `bca784379e7dbca9e64e79a64dfefbba` in D05SD5QLG94, whose members per slack/channels.json are Julia Lawson and Frederick Stone: "send me your recommendation back here". That message is the one S1 points at. This is not the #44 "answer him there too" pattern, where nothing led to the place.
  - S5 "its ticket": which beats are held is the finding itself, so the prompt cannot name the ticket without pre-solving. For the beat the records show failing after a restart, the place is named in Linear (unscoped): ZOM-429 "Leaderboard next session doesn't start without killing the app" (Backlog, assignee douglas). The GitHub data.json `reviews` collection has no CHANGES_REQUESTED review on a match3d PR after 2025-07-16. The only ones are match3d#303 on 2025-07-16 and match3d-backend#4 in June 2025. So the brief's change-request hold path adds no held beat without a ticket.
  - The brief's own write (SQL lines 92–111, `f_7c3e91a4d2b85f60e1a9c4`, "its owner is told in a reply on the mail where they committed to it") names its place. Brian's Sep 26 mail (SQL lines 65–72) adds "If the new date is a problem on your side, reply on this mail."
- **Audit or compliance-form wording (Eval 1 §2.7).** No finding. There is no audit or compliance vocabulary: no "reconcile", "governing", "remediation", "handoff it requires", "in-scope cohort" or "classify". The prompt reads as a PM handing off one deliverable, unlike #1 and #43.
- **Long if / but-not / then-also chains (Eval 1 §2.7, §6.2).** No finding. The only conditional is S5, a single "if X, do Y" with no but-not, unless or then-also clause. Per-case rules (hold criteria, push rules, one-off approval, config locks) are in the seeded brief, not in the prompt.
- **Staged typos, made-up emoji or broken punctuation (Eval 1 §1.2, Typing override).** No finding. There are no misspellings, no emoji, and the apostrophe and punctuation are correct. The writing is clean, which raises no flag.
- **Plain natural request / spec-like or polished LLM voice (Eval 1 §1.2, §2.7).** No finding. The prompt is first person and conversational ("Can you take it on for me?", "Once the sheet's done"). Sentence lengths vary (26, 7, 24, 7, 18 and 18 words). There are no polished connectives, no document formatting and no enumerated deliverable contents, preservation rules or reply format (zero spec-sheet register triggers). Pointing to "his message" and "the brief he shared with me" instead of restating them is the natural delegation Eval 1 §1.2 allows. "Beat" and "buy weeks" are the brief's and the UA plan's own terms, and fit a live-ops PM.

## Boundary notes (not P4, not scored here)

P4 left two questions open because they belong to other topics:
- Whether S5's "its ticket" resolves to ZOM-429 alone or could also mean the leaderboard feature tickets ZOM-71 "Weekly leaderboard system" (Done, no assignee) or ZOM-36 "Leaderboards" (Done). This is destination uniqueness, a UGT question.
- Whether any record defines the config lock that would trigger the brief's reply to Brian. Slack 2025 has no "config lock" hit, and neither does gdocs. My Gmail scan did not finish.

Platform defects: none.
