# P4 · Wording (deep recheck, /prompt Phase 5)

Pass: P4, blind and independent. Task date Oct 1, 2025 (synth-cut), clock 2025-10-01 00:00 PT.
Inputs read: R/inputs/04_Prompt.txt, 00_Task_Assigned_Inputs.md (platform block), 02_Universe_Date.txt, 01_Universe_Inject.sql (read only, not executed). Base exports read directly (gdrive, linear, github data.json) and through the wrapper (slack, confluence, linear, gdocs, gmail).

## Findings

none

Sentences checked: 6 (100 words, 2 paragraphs). Every sentence was checked against every P4 topic.

| S# | Words | Sentence |
|---|---|---|
| S1 | 26 | "Frederick messaged me yesterday asking for the live-ops and push calendar for the Zombie Match 3D beta, the four buy weeks that start Monday the 6th." |
| S2 | 7 | "Can you take it on for me?" |
| S3 | 24 | "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me." |
| S4 | 7 | "It goes in my live-ops calendar sheet." |
| S5 | 18 | "If a beat ends up held, leave a note on its ticket so the owner picks it up." |
| S6 | 18 | "Once the sheet's done, link it on the calendar ticket and send Frederick the recommendation he asked for." |

## Topic results (each one clean)

- **Catalog tool names, MCP or "tool" wording (common_errors §3 search hits, §6.6; Eval 1 §1.3.4): no finding.** I scanned the prompt for all 298 operation names in `Evals/references/tools/catalog.json`: 0 hits. The terms `linear_`, `gmail_`, `slack_`, `MCP`, `tool`, `First`, `Then`, `Finally` also get 0 hits. No parameter names, underscores, backticks or system-called-a-tool wording. "messaged", "sheet", "ticket" and "brief" are natural service nouns ("the Linear ticket" stays, per §3).
- **Step list (first / then / finally; Eval 1 §1.3.1): no finding.** The prompt has no sequence words and no numbered steps. The only ordering is "Once the sheet's done, link it on the calendar ticket" (S6), which is a real dependency: you cannot link a sheet before it is filled. It does not prescribe a procedure. S5 is a conditional, not a step.
- **Bolt-on sentence (§6.6; Eval 1 §1.3.2): no finding.** S1 sets the object and the span. S2 is the delegation itself. S3 points to the two governing sources. S4 names the destination. S5 adds the held-beat ticket notes, which come out of the calendar analysis. S6 adds the ticket link and the reply to the requester. None is an unrelated extra ask. Deleting S4, S5 or S6 removes a destination or a graded write.
- **Opaque id or exact timestamp (§6.6; Eval 1 §2.7): no finding.** The prompt has no ids, filenames, agent ids or clock times. "Monday the 6th" is a natural date: Oct 6, 2025 is a Monday, and the brief f_7c3e91a4d2b85f60e1a9c4 says "Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC".
- **Named cause (§3 line 2, §6.7; Eval 1 §1.3.3): no finding.** Named cause: none stated. The prompt gives no reason why any beat is held, late or ready, and no cause for any record conflict. S5 states only a possible outcome ("If a beat ends up held") and leaves which beats and why to the records.
- **Trap hint or riddle (Eval 1 §2.7, Riddles override; calibration #31): no finding.** I checked the prompt against each trap the records hold. These are: the Halloween one-off approval being pulled (slack 58d06bd55ea4129eaadb726291967d5a, D05GU6L0XFH: "pulling my ok ... my later word on this one is the one that counts"); the leaderboard "not blocking" comment (linear cmt_zom429_1) against the Sep 30 re-test (slack fa3eee2c614b0741aeb240275f86abf7, C0880U9751A: "it still does not start a new week. I killed the app and reopened it twice"); Collect & Win windows still on DEV until the Oct 8 release (github harmonygames-Games/match3d#470#rc_10; gcal evt_5c1e83a7d94b02f6c8e31a); Brian's handoff moving from Oct 29 to Oct 31 (gmail julia.lawson@harmonygames.co/1844835127305531392); the four non-beta push rows and Zombie Lane (slack 097c95c6e043ada8294b60f13e1656ba); and Boss Arena being off the calendar (brief). No prompt sentence alludes to any of them. Nothing in the prompt reads like "not on anybody's list". The brief's own "Not only the events everyone lists" is in a seeded record, not the prompt.
- **Hidden destination the persona would know (Eval 1 §1.5 Ambiguity, §2.7; calibration #42/#47/#44): no finding.** Every destination is named, or is left to the data with a persona-visible record that names it:
  - S4 "my live-ops calendar sheet". Injected gdrive f_e4a17c90b3d25f6a8c1d73 "ZM3D Beta Live-Ops Calendar.xlsx" (owner julia.lawson, parent d_5f2c8e1b7a94d03c6e2b58 "ZM Live Ops"). Frederick's DM (slack 8b090dec472117f4598b9ad84318272e) says "Put it in the calendar sheet in your ZM Live Ops folder". Julia owns 12 base spreadsheets, and none has "calendar" or "live-ops" in its name. Base "LiveOps Event Calendar.xlsx" (f_b04156e116437611a5014a) is owned by a Resource account, not Julia, so "my" excludes it.
  - S6 "the calendar ticket". Base linear ZOM-78 is titled "Event Calendar For Zombie Match 3D" and was created by usr_8140f09bf9f1b94c (julia.lawson). On it, injected comment cmt_zom78_1 by usr_175c0d7bc72ed244 (frederick.stone) says: "Let us use this ticket for the ZM3D beta live-ops calendar instead of opening a new one. Link the sheet here when it is ready." The phrase is the same one Frederick uses ("link it on the calendar ticket"). It is a plain descriptive name, not a riddle. ENG-2240 "Web interface for the liveops calendar" is an engineering item and does not compete.
  - S6 "send Frederick". The recipient is named. His DM says "send me your recommendation back here", so the channel is in the request record the prompt points to.
  - S5 "its ticket". Which beats are held is the finding, so the persona cannot name the tickets in advance. Each beat's ticket is in Linear. The held candidate visible in the records, the weekly leaderboard, has one open ticket: ZOM-429 "Leaderboard next session doesn't start without killing the app" (Backlog, assignee douglas). Its other leaderboard tickets are all Done.
  - A further write is not named in the prompt: the brief's "Config locks" rule (f_7c3e91a4d2b85f60e1a9c4: "its owner is told in a reply on the mail where they committed to it"). Its place is named by that persona-visible record, and the prompt does not hide or riddle it. Whether that write is in scope belongs to P1/R3, not P4.
- **Audit or compliance-form wording (Eval 1 §2.7; calibration #1/#43): no finding.** The prompt has no "reconcile / classify / complete the ... handoff it requires" register and no deliverable form. It reads as a PM handing a co-founder's request to an assistant.
- **Long if / but-not / then-also chains (Eval 1 §2.7; calibration #44): no finding.** The only conditional is S5: one condition ("If a beat ends up held") with one action and a purpose clause. It has no but-not, then-also or nested exceptions. The per-case rules (held vs late vs still-to-do, push readiness, one-off approval) are in the seeded brief and Frederick's DM thread, not in the prompt.
- **Staged typos, made-up emoji or broken punctuation (Eval 1 §1.2, Typing override; calibration #11): no finding.** The prompt is spelled correctly, has no emoji, and its punctuation is normal. The contraction "sheet's" is natural.
- **Plain natural request; spec-like or polished LLM voice (Eval 1 §1.2, §2.7, Spec-Sheet Register hard gate): no finding.** No headings, bullets, numbering or bold. No polished connectives ("Additionally", "Please ensure"). No enumerated deliverable contents, no preservation or format rules, no prescribed reply format, and the length is not driven by listing contents (0 of 4 register triggers). Sentence lengths are uneven (26 / 7 / 24 / 7 / 18 / 18 words), with natural shortcuts ("Can you take it on for me?", "Once the sheet's done"). The terms "beat", "buy weeks" and "live-ops and push calendar" come from the requester's own records and suit a ZM3D product manager.

Platform defects: none.
