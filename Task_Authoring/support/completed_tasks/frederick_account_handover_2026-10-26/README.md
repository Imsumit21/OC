# Frederick Stone: marketing & UA account handover register (submitted 2026-10-26)

Persona Frederick Stone (Co-founder) · Normal Horizon · Executive / Corporate Ops / Analysis and synthesis · difficulty mode medium · env hg4-with-gsuite-bundle-1174 · universe hg4-2026-08-31 · universe date Oct 1, 2025 07:00.

`task_inputs/` is the full slot folder as submitted. `work/fs_account_custody/` holds the local helper scripts (ID minting, SQL/design/dossier/manifest builders and their revision backups).

## Final state
- Injection SQL `01_Universe_Inject.sql` sha256 8d54ed2b4c0c (after three hardening rounds; earlier versions in `Working_Files/pre_hardening_r1..r3`).
- Friction: none (`03_Error_Async_Config.txt` left empty).
- Oracle Events: `08_Oracle_Events.md`; /oe reached PASS after fixing two MINOR accuracy issues from a NON-FAIL 3 run.
- Rubric: 37 rows (35 Outcome, 2 Process), weight 119.
- Baselines (6 of 6 completed): weighted pass 72.3 / 59.7 / 63.9 / 93.3 / 100 / 95.8, average 80.8%, pass@1 1/6, SD 0.161, 4 failure patterns (largest 40%), golden run-5 88 calls, no all-fail rows (no 11_AF_Justification needed). Average missed the <75% author target but passed the V3 medium cap (<85%); the task was accepted.

## Key answers
- Register: Google Sheet in Drive "Company Ops" (d_21f9e11d43739eaef26b38), 13 accounts; deactivated AdMob pub-2341961509332343 excluded.
- REVOKE (outsider Node Media LLC): Meta Domino Delights 907669287942378, Unity, YouTube, TikTok @harmonygames.
- TRANSFER: X @harmonygames only (1). KEEP: Instagram, Google Ads 569-350-5790 (Arthur's email override), AppLovin, LinkedIn, Discord. CLOSE: Google Ads 449-481-1590 (Calm Play), adjoe, AdMob pub-3556282811018998.
- Reply in Slack DM D05S58U4SAK: TRANSFER count 1 and the four outsider-access accounts.
- Trello checklist on Fred's "Lock up social handles and domain?" card (UA/BD board) naming only X.

## Lessons carried forward
- Hidden authorities that worked: Trello rules card + its comment (socials never CLOSE), Arthur's follow-up email (569 KEEP), Leonard's thread reply (<$100 ad revenue doesn't count), Gmail partner notices + Partners tabs for outsider access.
- Runs that found all Gmail partner notices passed nearly everything; to push the average under 75%, add a second independent hidden authority on rows the strong runs pass, not just more notices.
- When fixing /oe findings, sweep the whole defect class, not only the cited event.
