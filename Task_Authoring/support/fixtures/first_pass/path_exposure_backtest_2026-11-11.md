| case | outcome | found | path_exposure | reasons | hardness_v2_check | trap_liveness |
|---|---|---|---|---|---|---|
| BRIDGE-rev10-CORR | mixed | 2/7 runs opened it (pre-check: 'pass' search call 75 + thread call 76; baseline r4: 'pass' search call 92 + thread call 94); r1, r2, r3, r5, r6 did not | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| BRIDGE-rev10-DONE2 | landed | 0/7 runs opened it (pre-check + baseline r1-r6; no tool output contains the message) | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| BRIDGE-rev11-CORR | landed | 1/7 runs opened it (baseline r6 only: slack_read_thread on the a16z post call 87); pre-check and r1-r5 did not | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| BRIDGE-rev11-DONE1 | leaked | 7/7 runs opened it (slack_read_thread on the angel post C07C2866011/1758303600.418207: pre-check call 20, r1 19, r2 22, r3 20, r4 35, r5 32, r6 85) | EXPOSED | keyword,thin_search | no node | no node |
| BRIDGE-rev11-DONE2 | leaked | 7/7 runs opened it (body decoded from the T-Accelerate thread: pre-check calls 100 sub + 126 main, r1 40, r2 110, r3 37, r4 45, r5 54, r6 64; snippet also in mailbox listings) | EXPOSED | keyword,sweep_window | no node | no node |
| BRIDGE-rev12-ALIAS | leaked | 13/13 runs opened it (pre-check + baseline r1-r6 + baseline2 r1-r6; returned by each run's Sep mailbox listing or batch read) | EXPOSED | sweep_window | CLEAN | CLEAN |
| BRIDGE-rev12-BOOKED | leaked | 13/13 runs opened it (pre-check + baseline r1-r6 + baseline2 r1-r6; each run's calendar listing ran past Sep 30 and returned the Oct 8 'Michael Cheung and Leonard Hayes' event) | EXPOSED | pointer | CLEAN | FLAG breadcrumb |
| BRIDGE-rev12-CORR | mixed | 5/13 runs opened it (pre-check 'passed' search call 73 + thread call 75; baseline r4 'pass' call 95 + thread 97; baseline2 r2 'pass' call 99; baseline2 r5 'sciplay' call 58 + thread 59; baseline2 r6 call 82); the other 8 did not | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| BRIDGE-rev12-DONE1 | mixed | 5/13 runs opened it (pre-check calls 69-70 DM read; baseline r4 'Paul' search call 86 + DM call 87; baseline2 r3 DM call 60; baseline2 r4 'Paul' search call 75 + DM call 76; baseline2 r6 call 95); the other 8 did not | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| BRIDGE-rev12-DONE2 | mixed | 8/13 runs opened it (baseline r1, r2, r4, r5 via 'tester'; baseline r6 via 'internal test'; baseline2 r1, r3 via 'tester'; baseline2 r6 via 'internal test'); pre-check, baseline r3, baseline2 r2, r4, r5 did not | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| BRIDGE-rev12-DUP | leaked | 13/13 runs opened it (pre-check + baseline r1-r6 + baseline2 r1-r6; trello_get_lists cards=open or trello_get_cards_in_list on To Do) | EXPOSED | pointer | CLEAN | FLAG breadcrumb |
| BRIDGE-rev12-FOLLOW | leaked | 13/13 runs opened it (pre-check + baseline r1-r6 + baseline2 r1-r6; trello_get_comments / trello_get_card actions=all on card 68c5a49e8491a9d7faf869d0, calls 10-21) | EXPOSED | named_container,pointer,root_or_self | CLEAN | FLAG breadcrumb |
| BRIDGE-rev12-INPUT | leaked | 11/13 runs opened it (returned by Slack 'SAFE', 'docusign' or 'Anton' searches in the pre-check, baseline r3-r6 and baseline2 r1-r6); baseline r1 and r2 did not and wrote $40K | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| BRIDGE-rev5-CORR | leaked | 1/1 runs opened it (rev5 pre-check: slack_conversations_search_messages call 34, filter_in_channel #bridge-pitch + filter_threads_only) | EXPOSED | keyword,thin_search | no node | no node |
| BRIDGE-rev5-DONE2 | leaked | 1/1 runs opened it (rev5 pre-check: linear_list_issues call 93 'tester TestFlight internal test', linear_list_comments ZOM-567 call 94) | EXPOSED | root_or_self | CLEAN | CLEAN |
| BRIDGE-rev5-FILT | leaked | 1/1 runs opened it (rev5 pre-check: one gcal listing Sep 3-30 at call 27, output read back by Bash calls 28-29) | EXPOSED | pointer | CLEAN | FLAG breadcrumb,order |
| BRIDGE-rev5-INPUT | leaked | 1/1 runs opened it (rev5 pre-check: gmail_list_threads call 40 returned its snippet; gmail_get_thread call 61 opened the 'SAFE amount' thread) | EXPOSED | keyword,sweep_window | no node | no node |
| BRIDGE-rev9-CORR | leaked | 1/1 runs opened it (rev9 pre-check: slack_read_thread on the a16z post C07C2866011/1759196326.309469 call 76; 'pass' search call 77) | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| BRIDGE-rev9-DONE2 | leaked | 1/1 runs opened it (rev9 pre-check: slack_search_public_and_private 'tester' call 72, 'testflight' call 73, slack_read_thread call 74) | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| CLAIRE-rev2-T1STOREFOLDER | leaked | 1/1 (rev2 pre-check: gdrive_list_folder on the Store folder, call 231, result 232; the folder also came back in gdrive_search 'halloween' at result 216) | EXPOSED | pointer | CLEAN | FLAG breadcrumb |
| CLAIRE-rev2-T2CALENDAR | leaked | 1/1 (rev2 pre-check: gdrive_search 'release calendar' result 16; gdocs_get_document_text call 25) | EXPOSED | keyword | CLEAN | FLAG breadcrumb |
| CLAIRE-rev2-T3DMREPLY | leaked | 1/1 (rev2 pre-check, Working_Files/archive/rev3_slot/06_PreCheck_Trajectory/trajectory.json sha 8ef0af2a: slack_search_public_and_private 'halloween', call event 217, result 218) | EXPOSED | keyword,thin_search | CLEAN | FLAG breadcrumb,order |
| CLAIRE-rev2-T4SEP30MAIL | leaked | 1/1 (rev2 pre-check: gmail_search_messages 'october UA plan' call 17 returned it with the Sep 12 draft; gmail_get_message call 27) | EXPOSED | keyword,sweep_window,thin_search | FLAG SAME_PLACE/on_delegation_path | FLAG breadcrumb,order,self-advertising |
| CLAIRE-rev2-T6ART831 | leaked | 1/1 (rev2 pre-check: linear_get_issue ART-831 call 54; its comment cmt_art831_2 'Not on the live creatives sheet yet.' (SQL L117) read by linear_list_comments, result event 165) | EXPOSED | keyword,pointer | CLEAN | FLAG breadcrumb |
| CLAIRE-rev2-T9CMT795 | leaked | 1/1 (rev2 pre-check: linear_list_comments ART-795, result event 70, one of the 58-call comment sweep) | EXPOSED | pointer | CLEAN | FLAG breadcrumb |
| CLAIRE-rev3-T20FREDOCT10 | landed | 0/7 (7 rev3 runs = P (Working_Files/archive/rev3_slot/06_PreCheck_Trajectory/trajectory-run-1 (1).json, the attempt-1 /hardness r2 run) + B1-B6 (Working_Files/archive/rev3_slot/07_Baseline_Trajectories/trajectory-run-1..6.json)). rev4, same row at L25: 0/7 | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| CLAIRE-rev3-T21MARTINLEAVE | landed | 0/7 (7 rev3 runs = P (Working_Files/archive/rev3_slot/06_PreCheck_Trajectory/trajectory-run-1 (1).json, the attempt-1 /hardness r2 run) + B1-B6 (Working_Files/archive/rev3_slot/07_Baseline_Trajectories/trajectory-run-1..6.json)). rev4, same row at L7: 1/7 (B1: slack_search 'store' result 254, then slack_read_thread result 264) | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| CLAIRE-rev3-T22SEP29MAIL | mixed | 5/7 (B1 gmail_get_thread result 58; B3 gmail_get_message result 58; B4 gmail_get_message result 37; B5 gmail_get_messages_batch result 34; B6 gmail_get_thread result 46; not P, B2). rev4, same row at L245: 5/7 (P, B1, B4, B5, B6) | EXPOSED | keyword,sweep_window,thin_search | CLEAN | FLAG breadcrumb |
| CLAIRE-rev3-T23TRELLOENDCARD | landed | 0/7 (7 rev3 runs = P (Working_Files/archive/rev3_slot/06_PreCheck_Trajectory/trajectory-run-1 (1).json, the attempt-1 /hardness r2 run) + B1-B6 (Working_Files/archive/rev3_slot/07_Baseline_Trajectories/trajectory-run-1..6.json)). rev4, same row at L316: 0/7 | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| CLAIRE-rev3-T3ROBERTREJECT | mixed | 2/7 (B4 slack_read_thread result 253; B5 slack_conversations_replies result 222; not P, B1, B2, B3, B6). rev4, same row at L5: 4/7 (B1, B2 via search 'in:#zombie-art', B4, B6) | OFF-PATH | - | CLEAN | FLAG breadcrumb,order |
| CLAIRE-rev3-T6TRELLO826 | leaked | 7/7 (P trello_get_comments result 69; B1 trello_search 'halloween' result 35; B2 result 43; B3 trello_get_comments result 62; B4 result 53; B5 result 43; B6 result 55). rev4 (L314): 7/7; rev2 (L294): 1/1 at call 43 | EXPOSED | pointer | CLEAN | FLAG breadcrumb |
| CLAIRE-rev3-T9MARCUSPOST | landed | 0/7 (7 rev3 runs = P (Working_Files/archive/rev3_slot/06_PreCheck_Trajectory/trajectory-run-1 (1).json, the attempt-1 /hardness r2 run) + B1-B6 (Working_Files/archive/rev3_slot/07_Baseline_Trajectories/trajectory-run-1..6.json)). rev4, same post at L2: 0/7 | EXPOSED | keyword,thin_search | CLEAN | FLAG breadcrumb |
| CLAIRE-rev4-T9MARCUSREPLY | landed | 0/7 (7 rev4 runs = P (06_PreCheck_Trajectory/trajectory-run-1 (8).json) + B1-B6 (07_Baseline_Trajectories/trajectory-run-N (k).json)) | EXPOSED | keyword | CLEAN | FLAG breadcrumb |
| DOUG-final-PAGEC2 | mixed | 3/6 (B1 confluence_list_comments result 29; B4 result 30; B5 result 31) | EXPOSED | pointer | CLEAN | CLEAN |
| DOUG-final-PR38RC1 | landed | 1/6 (B3 github_get_pull_request_comments #38, result 152) | OFF-PATH | - | CLEAN | CLEAN |
| DOUG-final-PR39RC1 | landed | 1/6 (B3 github_get_pull_request_comments #39, result 191) | OFF-PATH | - | CLEAN | CLEAN |
| DOUG-final-PR46RC1 | landed | 0/6 | OFF-PATH | - | CLEAN | CLEAN |
| DOUG-final-REPLYALL | mixed | 2/6 (B2 gmail_get_thread result 332; B5 gmail_get_thread result 576). 6 final-baseline runs = B1 (07_Baseline_Trajectories/trajectory-run-1 (7).json), B2-B6 (trajectory-run-N.json) | EXPOSED | named_container,sweep_window,thin_search | FLAG SAME_PLACE/first_read | FLAG breadcrumb |
| DOUG-final-ZOM336CMT | leaked | 6/6 (linear_list_comments ZOM-336: B1 result 484; B2 196; B3 529; B4 332; B5 346 and 517; B6 403) | OFF-PATH | - | CLEAN | CLEAN |
| FQ4-rev3-FRAMEWELL | leaked | 1/1 run opened it: the pre-check (06_PreCheck_Trajectory/trajectory.json, sha d5dc726b6150). It is first in a result at tool call 150 (slack_search 'Framewell'); the report gives events 444, 455 and 480. | EXPOSED | keyword,thin_search | CLEAN | FLAG breadcrumb |
| FQ4-rev3-LANTERNFLY | leaked | 1/1 run opened it: the pre-check, first at tool call 129 (slack_search 'Lanternfly'). The report gives events 387, 426 and 428/430: a name search, a 'told' search and the DM history read. | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| FQ4-rev3-NINTENDO | landed | 0/1 runs opened it. The pre-check made 0 Linear calls and has 0 hits for the comment text or for ZOM-567's title. | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| FQ4-rev3-PAYLANE | leaked | 1/1 run opened it: the pre-check. Its snippet appeared in the after:2025/08/15 gmail_list_threads result (tool call 26) and the thread was opened at call 61. The report gives events 66 and 187. | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| FQ4-rev3-SPOTLIGHT | leaked | 1/1 run opened it: the pre-check, first at tool call 128 (slack_search 'Spotlight'). | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| FQ4-rev4-BALANCY | landed | 0/7 runs read Leonard's Sep 11 reply: the scan finds 0 hits for 'as soon as we get some bandwidth'. The thread id appears in every run's inbox listing. Baseline run-2 alone opened the thread, in minimal format with 100-character snippets. | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| FQ4-rev4-FRAMEWELL | landed | 0/7 runs opened it: the pre-check (Run1_trajectory.json, sha 637c04535a86) and baselines 1-6 (07_Baseline_Trajectories). The scan finds 0 hits for 'Maren called me back about the Pro plan'. The tool proposal in run_forensics/rev4/baseline/node_verdicts.json, 'CORR LEAKED 6', is wrong. | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| FQ4-rev4-HOOTLINE | leaked | 6/7 runs opened it. By tool call:
- pre-check: gmail_get_messages_batch, call 33
- run-1: list_threads after:2025/07/01, call 28; get_thread, call 67
- run-2: get_thread, call 39
- run-3: Bash read of a listing, call 25
- run-4: batch read, call 40
- run-5: batch read, call 29

Baseline run-6 never did: it listed only after:2025/08/15, has no Hootline text in any result, and fails every Hootline row. | EXPOSED | keyword,thin_search | CLEAN | FLAG breadcrumb,order |
| FQ4-rev4-LANTERNFLY | landed | 0/7 runs opened it (pre-check and baselines 1-6): the scan finds 0 hits for 'I rang Wen back on Saturday'. | OFF-PATH | - | CLEAN | CLEAN |
| FQ4-rev4-NINTENDO | landed | 0/7 runs opened it (pre-check and baselines 1-6). There were 0 Linear calls in any run, and the scan finds 0 hits for the comment text or for ZOM-567's title. | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| FQ4-rev4-SPOTLIGHT | landed | 0/7 runs opened it (pre-check and baselines 1-6): the scan finds 0 hits for 'had the call about the Dec 5 indie showcase'. | OFF-PATH | - | CLEAN | CLEAN |
| LEO-rev1p-ADV | landed | 0/1 (the pre-check run never opened it) | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| LEO-rev1p-ASOF | leaked | 1/1 (the pre-check run opened it, first in the result at event 61 of gmail_get_thread) | EXPOSED | keyword,named_container,thin_search | CLEAN | CLEAN |
| LEO-rev1p-FAM | leaked | 1/1 (the pre-check run opened it, first in the result at event 28 of slack_read_thread) | EXPOSED | named_container,pointer | CLEAN | CLEAN |
| LEO-rev1p-TOLD2446 | leaked | 1/1 (the pre-check run opened it, first in the result at event 314 of gmail_get_thread) | OFF-PATH | - | CLEAN | CLEAN |
| LEO-rev2-ADV | landed | 0/6 baseline runs opened it (none); the /hardness run on this revision (06_PreCheck_Trajectory/trajectory-run-1.json): not opened | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| LEO-rev2-ALIAS | leaked | 6/6 baseline runs opened it (run-1, run-2, run-3, run-4, run-5, run-6); the /hardness run on this revision (06_PreCheck_Trajectory/trajectory-run-1.json): opened | OFF-PATH | - | CLEAN | CLEAN |
| LEO-rev2-ASOF | leaked | 5/6 baseline runs opened it (run-1, run-2, run-3, run-4, run-6); the /hardness run on this revision (06_PreCheck_Trajectory/trajectory-run-1.json): opened | EXPOSED | keyword,named_container,thin_search | CLEAN | CLEAN |
| LEO-rev2-BOUNCE | leaked | 6/6 baseline runs opened it (run-1, run-2, run-3, run-4, run-5, run-6); the /hardness run on this revision (06_PreCheck_Trajectory/trajectory-run-1.json): opened | OFF-PATH | - | CLEAN | CLEAN |
| LEO-rev2-EXT | mixed | 4/6 baseline runs opened it (run-1, run-2, run-3, run-6); the /hardness run on this revision (06_PreCheck_Trajectory/trajectory-run-1.json): opened | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| LEO-rev2-TOLD2440 | mixed | 4/6 baseline runs opened it (run-3, run-4, run-5, run-6); the /hardness run on this revision (06_PreCheck_Trajectory/trajectory-run-1.json): not opened | OFF-PATH | - | CLEAN | CLEAN |
| LEO-rev2-TOLD2446 | mixed | 4/6 baseline runs opened it (run-1, run-2, run-4, run-6); the /hardness run on this revision (06_PreCheck_Trajectory/trajectory-run-1.json): not opened | OFF-PATH | - | CLEAN | CLEAN |
| LLC-rev3-COMPLETE | leaked | 1/1 (pre-check) | EXPOSED | keyword | CLEAN | FLAG breadcrumb |
| LLC-rev3-CORR | leaked | 1/1 (pre-check) | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| LLC-rev3-DONE | landed | 0/1 opened the body (listed, snippet only) | EXPOSED | keyword | CLEAN | CLEAN |
| LLC-rev3-FILT | leaked | 1/1 (pre-check) | EXPOSED | keyword | CLEAN | FLAG breadcrumb,order |
| LLC-rev4-CORR | leaked | 5/6 (baseline; b5 wrong) | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| LLC-rev4-DATE | landed | 1/6 (baseline b3) | EXPOSED | keyword | CLEAN | CLEAN |
| LLC-rev4-DONE | mixed | 3/6 (b2,b3,b6 state right) | EXPOSED | keyword | CLEAN | CLEAN |
| LLC-rev4-FILT | landed | 1/6 (baseline b3) | OFF-PATH | - | CLEAN | FLAG breadcrumb,order |
| LLC-rev4-STACKS | leaked | 5/6 (baseline; b5 wrong) | EXPOSED | keyword | CLEAN | CLEAN |
| OWEN-rev5-APPLE_MAIL | landed | 0/13 runs opened it. Checked by scanning tool results for 'comes down to the same sync problem' and the subject 'sign in lines on my list': the pre-check (06_PreCheck_Trajectory/trajectory.json, sha 27fb0c6d) and baseline batch 2 r1-r6 (Working_Files/run_forensics/rev5/baseline2/) have 0 hits. Baseline batch 1 r1-r6 is not stored; summary.md says 'Gmail never searched for it'. | OFF-PATH | - | CLEAN | CLEAN |
| OWEN-rev5-INLINE_TD | landed | 0/13 runs opened it. The pre-check and batch 2 r1-r6 have 0 hits for 'in this PR. That has to be swapped'. That probe also matches the injected #engineering-bots copy (C050WGU41HR/1763557535.436659, line 131), so neither carrier was read. Batch 1 is not stored; its summary says 'no run called the PR reviews/comments tools'. | OFF-PATH | - | CLEAN | CLEAN |
| OWEN-rev5-SHOP_REPLY | mixed | 5/7 stored runs opened it: batch 2 r1, r2, r3, r5 and r6, through a from:Brian listing of C09Q4S613CN or a Bash read-back of one. The pre-check and batch 2 r4 never did. Batch 2 r2 had it in a result (call 101) but still filed the ticket Done. Batch 1 (not stored) filed the ticket right in 5/6 runs, all but r3. | OFF-PATH | - | CLEAN | CLEAN |
| OWEN-rev7-BRIAN_APPLE | leaked | 1/1 run opened it: the pre-check (Working_Files/run_forensics/rev7/precheck/trajectory.json, sha b0a1d4db). It is first in a result at tool call 62 (slack_search 'from:<@Brian> PR', after 1761000000), then at call 63 (slack_read_channel D07E9PSQB6W, oldest 1764900000), and again in the keyword-less from:Brian Nov 1-Dec 15 listing at calls 218-219. Vincent's email (line 287) was never opened. | EXPOSED | root_or_self,sweep_window | CLEAN | CLEAN |
| OWEN-rev8-BRIAN_TAVERN | leaked | 1/1 run opened it: the rev8 pre-check (sha f5dc1d4e). That trajectory is not stored in the archive; the /hardness report confirms the line in its tool results and that the Tavern decision was right. | EXPOSED | root_or_self,sweep_window | CLEAN | CLEAN |
| OWEN-rev9-BRIAN_POPUPS | mixed | 9/13 runs opened it:
- the pre-check (call 94, from:Brian search; call 96, DM read)
- batch 1 r2-r6, per the summary (r1 read the DM only for Nov 13-24)
- batch 2 r3, r4 and r5, by scan

It was not opened by batch 1 r1 or batch 2 r1, r2 and r6. Each of those four runs moved ENG-2426 and ENG-2434 to Done. The original inline comments #1905#rc_1 and #1908#rc_1 were opened by 0/13: batch 2 r4 called github_get_pull_request_reviews twice, and that call does not return inline comments. | EXPOSED | root_or_self,sweep_window | CLEAN | CLEAN |
| OWEN-rev9-TAVERN_DM | landed | 0/13 runs opened it. The pre-check (Run1_trajectory.json, sha d8b88c21) and batch 2 r1-r6 (Working_Files/run_forensics/rev9/baseline2/, the same sessions as the 07_Baseline_Trajectories verifier batch) have 0 hits for 'I looked at the prefab and Brian'. Batch 1 is not stored; its summary says 'Marcus DM never opened' for every run. | OFF-PATH | - | CLEAN | CLEAN |
| ROBERT-rev6-ALIAS | leaked | 1/1 (rev6 pre-check: Slack search 'close after:2024-12-01 before:2025-01-20' result 400; '"Node Media"' search result 409) | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| ROBERT-rev6-CORR | leaked | 1/1 (rev6 pre-check: Gmail search '3203' result 381, gmail_get_thread result 387 after one ECONNRESET) | EXPOSED | keyword | CLEAN | CLEAN |
| ROBERT-rev6-OFF | leaked | 1/1 (rev6 pre-check: date-window Gmail search result 292 listed it, opened in gmail_get_messages_batch result 294 and gmail_get_message result 299; all five receipts by result 321) | EXPOSED | named_container | CLEAN | CLEAN |
| ROBERT-rev6-ORPH | leaked | 1/1 (rev6 pre-check: first Slack search 'received after:2026-01-01' returned it as the top hit, result 244; thread read result 258) | EXPOSED | keyword | CLEAN | CLEAN |
| ROBERT-rev6-RET | landed | 0/1 (rev6 pre-check 06_PreCheck_Trajectory/trajectory.json sha fc4e4ed2; the Apr 5 sibling C04UEQVDVB7/1712331718.859679 also 0/1) | OFF-PATH | - | CLEAN | CLEAN |
| ROBERT-rev7-ALIAS | leaked | 6/7 (P gmail_get_messages_batch result 260; B1 get_thread 524 and get_message 531; B2 370/372; B3 292; B4 337; B6 629-634; not B5) | OFF-PATH | - | CLEAN | CLEAN |
| ROBERT-rev7-CORR | leaked | 7/7 (P gmail_get_thread result 169; B1 255; B2 gmail_get_messages_batch result 164; B3 302; B4 158; B5 240; B6 batch 247 and get_thread 289) | EXPOSED | keyword | CLEAN | CLEAN |
| ROBERT-rev7-OFF | landed | 1/7 (B1 only: gmail_get_thread call 483, result spilled, decoded by script at result 500; P and B2-B6 never opened any of the five receipt threads) | EXPOSED | named_container | CLEAN | CLEAN |
| ROBERT-rev7-ORPH | leaked | 7/7 (P result 201/213; B1 402; B2 343/350; B3 181; B4 307/316; B5 257; B6 417/433) | EXPOSED | keyword | CLEAN | CLEAN |
| ROBERT-rev7-RET | mixed | 5/7 (P 'came back' search result 190; B3 'wire came back' result 259; B4 'wires' result 344; B5 'wires' result 267; B6 '"came back"' result 458; not B1, B2). 7 rev7 runs with stored results = P (06_PreCheck_Trajectory/trajectory-run-1-5.json) + B1-B6 (07_Baseline_Trajectories/trajectory-run-N (1).json); the first rev7 batch keeps call ledgers only and is not counted | EXPOSED | root_or_self | CLEAN | CLEAN |
| SAM-rev5-ALIAS | leaked | 1/1 (the pre-check run opened it, first in the result at event 143 of linear_list_issues) | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| SAM-rev5-CORR | leaked | 1/1 (the pre-check run opened it, first in the result at event 227 of slack_search_public_and_private) | OFF-PATH | - | CLEAN | CLEAN |
| SAM-rev5-FILT542 | landed | 0/1 (the pre-check run never opened it) | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| SAM-rev5-FILT556 | landed | 0/1 (the pre-check run never opened it) | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| SAM-rev5-FOLLOW | leaked | 1/1 (the pre-check run opened it, first in the result at event 114 of trello_get_board_actions) | OFF-PATH | - | CLEAN | CLEAN |
| SAM-rev5-QA | leaked | 1/1 (the pre-check run opened it, first in the result at event 208 of slack_search_public_and_private) | OFF-PATH | - | CLEAN | CLEAN |
| SAM-rev6-CORR | mixed | 2/6 baseline runs opened it (run-4, run-5); the /hardness run on this revision (Run1_trajectory.json): not opened | EXPOSED | pointer | CLEAN | CLEAN |
| SAM-rev6-FILT563 | landed | 0/6 baseline runs opened it (none); the /hardness run on this revision (Run1_trajectory.json): not opened | OFF-PATH | - | CLEAN | FLAG breadcrumb |
| SAM-rev6-FOLLOW | leaked | 6/6 baseline runs opened it (run-1, run-2, run-3, run-4, run-5, run-6); the /hardness run on this revision (Run1_trajectory.json): opened | EXPOSED | pointer | CLEAN | CLEAN |
| SAM-rev6-PULL | leaked | 5/6 baseline runs opened it (run-1, run-2, run-4, run-5, run-6); the /hardness run on this revision (Run1_trajectory.json): opened | EXPOSED | keyword,root_or_self | CLEAN | CLEAN |
| SAM-rev6-QA | leaked | 5/6 baseline runs opened it (run-1, run-2, run-4, run-5, run-6); the /hardness run on this revision (Run1_trajectory.json): not opened | OFF-PATH | - | CLEAN | CLEAN |
| VIN-rev1-T12 | leaked | 1/1 (the pre-check run opened it, first in the result at event 245 of linear_list_comments) | EXPOSED | pointer,root_or_self | CLEAN | CLEAN |
| VIN-rev1-T2 | leaked | 1/1 (the pre-check run opened it, first in the result at event 295 of slack_search_public_and_private) | OFF-PATH | - | CLEAN | CLEAN |
| VIN-rev1-T3 | leaked | 1/1 (the pre-check run opened it, first in the result at event 39 of trello_get_comments) | EXPOSED | root_or_self | CLEAN | CLEAN |
| VIN-rev1-T3b | leaked | 1/1 (the pre-check run opened it, first in the result at event 386 of slack_search_public_and_private) | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| VIN-rev1-T5 | leaked | 1/1 (the pre-check run opened it, first in the result at event 336 of gmail_get_messages_batch) | OFF-PATH | - | CLEAN | CLEAN |
| VIN-rev2-R1 | leaked | 6/6 baseline runs opened it (run-1, run-2, run-3, run-4, run-5, run-6); the /hardness run on this revision (06_PreCheck_Trajectory/trajectory-run-1.json): opened | OFF-PATH | - | CLEAN | CLEAN |
| VIN-rev2-R3a | landed | 1/6 baseline runs opened it (run-5); the /hardness run on this revision (06_PreCheck_Trajectory/trajectory-run-1.json): not opened | EXPOSED | keyword,thin_search | CLEAN | FLAG breadcrumb |
| VIN-rev2-R3b | landed | 1/6 baseline runs opened it (run-1); the /hardness run on this revision (06_PreCheck_Trajectory/trajectory-run-1.json): not opened | EXPOSED | root_or_self | CLEAN | FLAG breadcrumb |
| VIN-rev2-T3b | landed | 1/6 baseline runs opened it (run-5); the /hardness run on this revision (06_PreCheck_Trajectory/trajectory-run-1.json): not opened | EXPOSED | keyword,thin_search | CLEAN | CLEAN |
| VIN-rev2-T5 | landed | 1/6 baseline runs opened it (run-6); the /hardness run on this revision (06_PreCheck_Trajectory/trajectory-run-1.json): not opened | OFF-PATH | - | CLEAN | CLEAN |

| tool | leaked: flagged | leaked: missed | landed: clear | landed: flagged (false alarm) | mixed: flagged/clear | not judged |
|---|---|---|---|---|---|---|
| either_old_tool | 19 | 36 | 17 | 16 | 4/12 | 4 |
| hardness_v2_check | 1 | 54 | 33 | 0 | 1/15 | 4 |
| path_exposure | 43 | 16 | 22 | 11 | 11/5 | 0 |
| trap_liveness | 19 | 36 | 17 | 16 | 4/12 | 4 |
