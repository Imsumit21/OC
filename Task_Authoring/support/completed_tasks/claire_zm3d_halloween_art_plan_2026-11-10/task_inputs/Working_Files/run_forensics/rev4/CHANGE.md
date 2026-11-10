# rev4: settle the re-recorded cuts (2026-11-08)

Platform /prompt FAIL 2 on attempt 6aeed825ea17fab7311d0896 (Unique Ground Truth and Clarity): no record said whether
Marcus's #1935 / #1896 / #1966 re-recordings replaced the running cuts on ART-795, ART-797, ART-805 and ART-823.
The SQL body was the one that passed before (2175e44f is rev3 0a08dede minus 7 header comment lines).

SQL (6c143945fe3e): one new row, Marcus's thread reply under his Sep 25 #zm-animations post, id
6aecfa673deb24040a0d83058b4848d8, ts 1758825697.426919; the parent's thread_ts_legacy, reply_count, reply_users_count
and latest_reply set to match. Text:
"use these from now on, they replace the april captures on ART-795, ART-805 and ART-797. the couch 16:9 on ART-823 wasnt redone, thats still the apr 7 capture"

Key unchanged: truth.json reproduces byte for byte. Calls stay 12 / 36 / 10.
Also edited: OE 22 (action and quote); rubric rows 6, 22, 61, 65, 81, 111 (0-based), evidence field only;
load_bearing_ids, oe_lb_ids, rubric_lb_ids and 01_Hardness_Manifest.json (reply id added).

Why a thread reply: Frederick is not in #zm-animations; a Linear comment reaches 7 of 7 runs and is the shape the
manifest records as leaked in rev2. Replaying real rev3 queries, 0 of 7 runs would hit the reply.
Rejected wording: "in unity now" and "same slots" (the sheet's Live since equals upload dates; the claim also made
upload the test for replacing, which opens ART-808 and ART-816), "only those 3" (ART-852 to 854 use the same builds).

Not rebuilt: injection_gen/gen_sql.py, planned_texts.json and ids.json do not hold this reply, and the builders still
name task_inputsN2. Re-running gen_sql.py would drop the reply. solver.py reads only the parent's text.
Stale on purpose: dossier, preflight, ledgers and check reports still cite earlier SQL hashes.

Local cold review in ../../research/prompt_review_rev4/: P1 none, main UGT 5 and Clarity 5, injection PASS.
Main and P2 raised Coherence items in rows unchanged since the passing rounds; not edited, see p2.md and main.md.
