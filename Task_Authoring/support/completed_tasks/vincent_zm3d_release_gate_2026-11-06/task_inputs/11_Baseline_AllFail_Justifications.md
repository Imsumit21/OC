# Baseline All-Fail Justifications

All 6 baseline rollouts completed, so an all-fail rubric is one that failed in all 6. 3 rubrics failed in all 6, and all 3 are valid.

## The Agent records the call BLOCKER for ZOM-293 in its new tab of the ZM3D Release Gate spreadsheet

ZOM-293's call has to be BLOCKER, because Vincent's own comment on the open ticket says the glue and trampoline taken for a retry were lost after the tier reload, 600 coins worth. Leonard's submission rules, which the release ticket ZOM-570 says apply, put every open ZM ticket in the gate, make lost boosters a blocker and give no call only to a ticket that doesn't say what goes wrong, and the comment opens with 'what goes wrong here:'. All six runs judged ZOM-293 from its one-line description, 'Dynamic Difficulty Tiering', and wrote NO CALL with the note that it doesn't say what goes wrong. Runs 2 to 6 never listed the ticket's comments, though each listed comments on dozens of other tickets, and in run 1 a sub-agent fetched the comment but the main agent re-read only the description before writing the row.

## The Agent lists exactly 18 existing tickets as blockers in the description of the release ticket ZOM-570 (a ticket it files during the run not counted)

The release ticket ZOM-570 has to list exactly 18 existing tickets as blockers, the BLOCKER calls of the register apart from the new update-path ticket. Arthur's ZOM-570 description asks for blockers on the ticket by key, and under Leonard's rules 18 existing tickets are blockers on the candidates, ZOM-293, ZOM-458, ZOM-473, ZOM-535 and ZOM-562 among them, each settled by a comment, DM, email or re-test beyond its description. The six runs listed 13, 13, 13, 13, 16 and 14 existing tickets besides the new ticket they filed: every run left out ZOM-293, five runs left out ZOM-458, ZOM-473 and ZOM-535, and five left out ZOM-562. No run reached 18, so the miss comes from the calls behind the list, not from how the list was written.

## The Agent lists ZOM-293 as a blocker in the description of the release ticket ZOM-570

ZOM-293 has to be on the blocker list in the description of the release ticket ZOM-570, since its lost boosters, 600 coins worth, make it a blocker under Leonard's rules. Arthur's ZOM-570 description asks for blockers on the ticket by key, and the call follows from Vincent's comment on the open ticket, which says the glue and trampoline taken for a retry were gone after the tier reload. Every run appended a blocker section to ZOM-570 built from the tickets it had called BLOCKER in its register, and because all six had called ZOM-293 NO CALL from its one-line description, none of the six lists includes it. This row grades the release ticket, while the register row grades the call the list came from.
