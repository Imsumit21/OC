# Deep Recheck P4 · Wording (blind)

Pass: P4 (prompt). Task date Oct 1, 2025 (synth-cut), clock 2025-10-01 00:00 PT.
Inputs read: R/inputs/04_Prompt.txt, 00_Task_Assigned_Inputs.md (platform block), 02_Universe_Date.txt, 01_Universe_Inject.sql (read only, not executed).

## Findings

none

Sentences checked: 6 (100 words, 2 paragraphs). Every sentence was checked against every P4 topic.

1. "Frederick messaged me yesterday asking for the live-ops and push calendar for the Zombie Match 3D beta, the four buy weeks that start Monday the 6th."
2. "Can you take it on for me?"
3. "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me."
4. "It goes in my live-ops calendar sheet."
5. "If a beat ends up held, leave a note on its ticket so the owner picks it up."
6. "Once the sheet's done, link it on the calendar ticket and send Frederick the recommendation he asked for."

## Per-topic results (common_errors §3 search hits and named cause, §6.6, §6.7; Eval 1 §1.2, §1.3, §1.5 Ambiguity, §2.7)

- **Search hits / catalog tool names / MCP / "tool"** — no finding. A case-insensitive scan for `linear_`, `gmail_`, `slack_`, `MCP`, `tool`, `First`, `Then`, `Finally` returned no hits. None of the 298 operation names in `Evals/references/tools/catalog.json` appears, and no server prefix appears either (`slack`, `linear`, `gdrive`, `gsheets`, `github`, `trello` and the rest). No parameter names appear. "sheet", "ticket", "message" and "brief" are plain business references.
- **First / then / finally step list** — no finding. There is no enumerated or numbered sequence. S6's "Once the sheet's done, link it … and send Frederick …" is one natural dependency clause, the same shape as the passing control "can you check what's still open and close it out?". It repeats the order Frederick himself gave in slack D05SD5QLG94 msg 8b090dec472117f4598b9ad84318272e: "Put it in the calendar sheet in your ZM Live Ops folder, link it on the calendar ticket, and send me the recommendation back here."
- **Bolt-on** — no finding. Every sentence feeds the deliverable. S5, the ticket note on a held beat, is the only ask that is not in Frederick's DM. It depends on the hold decision the calendar has to make, and it ties to the brief's "Still to do … who owns it", so it is not an unrelated add-on.
- **Opaque id / exact timestamp** — no finding. The prompt has no ids, filenames or clock times. "Monday the 6th" is the scope start a person would type, and it matches the UA plan slide "W1 Mon Oct 6 - Sun Oct 12".
- **Named cause (§6.7)** — no finding (named cause: none stated). The prompt states no cause for any hold, slip or late start. "If a beat ends up held" names a possible outcome, not why it happens.
- **Trap hint or riddle** — no finding. No phrase points at a planted trap: the leaderboard retest that contradicts the ZOM-429 comment, the Halloween approval that was later pulled, Collect & Win staying on DEV until the Oct 8 release, the Brian config date moving from Oct 29 to Oct 31, the daily-gift frame conflict, or the push naming rule. S5's conditional fits either answer, held or not held. S3 only says where the requirements live, like the passing control "Arthur posted how he wants each kind handled."
- **Hidden destination the persona would know** — no finding. Each place a write goes is named in the prompt or settled by a persona-visible record:
  - S4 "my live-ops calendar sheet" is named, and Julia owns it: gsheets `f_e4a17c90b3d25f6a8c1d73` "ZM3D Beta Live-Ops Calendar" in Julia's folder `d_5f2c8e1b7a94d03c6e2b58` "ZM Live Ops". The only base look-alike is gdrive `/drive_files/44292` "LiveOps Event Calendar.xlsx", a Domino Delights resource file that Julia does not own.
  - S6 "the calendar ticket" uses Frederick's own words. Linear `cmt_zom78_1` on ZOM-78 "Event Calendar For Zombie Match 3D", written by usr_175c0d7bc72ed244 (frederick.stone@), says: "Let us use this ticket for the ZM3D beta live-ops calendar instead of opening a new one. Link the sheet here when it is ready."
  - S6 "send Frederick" names the recipient. The channel is set by his message "send me the recommendation back here", in IM D05SD5QLG94, whose members include EMPLOYEE_0005_SLACK_ID (Julia Lawson) and EMPLOYEE_0008_SLACK_ID (Frederick Stone).
  - S5 "its ticket" is a plain reference to the beat's own ticket, not a pointer phrase like #42/#47/#44. For the leaderboard the ticket can be found: Linear ZOM-429 "Leaderboard next session doesn't start without killing the app" (Backlog).
- **Audit / compliance-form wording** — no finding. The prompt has none of the forms seen in #1/#43, such as "reconcile", "governing control", "complete the decision record / handoff it requires" or "classify". It reads as a person handing off a request.
- **Long if / but-not / then-also chain** — no finding. S5 is one short conditional, comparable to the passing §6.5 control "If a bill is missing from those, say it is missing". Per-case rules (holds, push gating, one-offs, config locks) stay in the brief gdocs `f_7c3e91a4d2b85f60e1a9c4` and in Frederick's thread reply `097c95c6e043ada8294b60f13e1656ba`, not in the prompt.
- **Staged typos / made-up emoji / broken punctuation** — no finding. The prompt is spelled correctly, uses ASCII only (straight apostrophe in "sheet's") and contains no emoji. Clean typing is not a defect.
- **Naturalness / spec-like or polished LLM voice (§1.2, §2.7)** — no finding. There is no document formatting and none of the polished connectives ("Additionally", "Please ensure"). Sentence lengths are uneven (26/7/24/7/18/18) and contractions are used. Spec-sheet register triggers: 0 of 4. Deliverable contents are not enumerated (they are left to Frederick's message), there are no preservation or format rules, no prescribed reply format, and the length is not driven by listing contents. Read as a plain request, it sounds like a PM handing a co-founder's ask to an assistant.

Platform defects: none.
