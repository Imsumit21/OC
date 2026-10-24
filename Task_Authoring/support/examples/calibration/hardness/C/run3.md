# Ledger: V7-T1 (V1 HarmonyGames task 1) · trajectory-run-3.json
model(init)=claude-opus-4-8 assistant-models={'claude-opus-4-8': 426}
tool_calls=348 errored_results=0 turns=349 duration_ms=1911755 result_subtype=success is_error=False
subagents=0 subagent_models=[] post_final_result_events=0 compaction=no
tool counts: mcp__mcp_4981f6c7__github_search_pull_requests=82, mcp__mcp_4981f6c7__linear_create_comment=79, mcp__mcp_4981f6c7__github_search_commits=71, mcp__mcp_4981f6c7__linear_get_issue=40, mcp__mcp_4981f6c7__linear_update_issue=12, mcp__mcp_4981f6c7__github_get_pull_request_reviews=9, TaskUpdate=7, Bash=6, TaskCreate=6, mcp__mcp_4981f6c7__gdrive_search=5, mcp__mcp_4981f6c7__linear_list_issues=4, mcp__mcp_4981f6c7__gdocs_get_document_text=3, mcp__mcp_4981f6c7__linear_list_users=2, mcp__mcp_4981f6c7__slack_search_channels=2, mcp__mcp_4981f6c7__slack_read_channel=2, mcp__mcp_4981f6c7__gdocs_search_documents=2, mcp__mcp_4981f6c7__gdrive_read_file=2, mcp__mcp_4981f6c7__gmail_get_thread=2, mcp__mcp_4981f6c7__gmail_send_message=2, mcp__mcp_4981f6c7__github_get_me=1, mcp__mcp_4981f6c7__linear_get_user=1, mcp__mcp_4981f6c7__get_time=1, mcp__mcp_4981f6c7__trello_list_boards=1, mcp__mcp_4981f6c7__gsheets_search_spreadsheets=1, mcp__mcp_4981f6c7__gmail_search_messages=1, mcp__mcp_4981f6c7__github_search_repositories=1, mcp__mcp_4981f6c7__contacts_search_contacts=1, mcp__mcp_4981f6c7__gdocs_batch_update=1, mcp__mcp_4981f6c7__slack_send_message=1

> [main] I'll start by establishing my identity and finding the cleanup ticket Vincent assigned to me. Let me investigate across the relevant systems.
   1 [main] mcp__mcp_4981f6c7__github_get_me {}
      => {"result":"{\"login\": \"agent\", \"id\": \"0\", \"type\": \"User\", \"site_admin\": false, \"name\": \"Agent\"}"}
   2 [main] mcp__mcp_4981f6c7__linear_get_user {"query": "me"}
      => {"result":"{\"id\": \"usr_49b9dfa5208d400d\", \"email\": \"calvin.price@harmonygames.co\", \"name\": \"calvin.price@harmonygames.co\", \"display_name\": \"calvin.price@harmonygames.co\", \"avatar_url\": null, \"is_active\": true, \"created_at\": \"2023-03-22T19:13:25Z\", \"updated_at\": \"2026-01-01 …[+15]
   3 [main] mcp__mcp_4981f6c7__get_time {}
      => {   "current_time": "2026-02-13T12:00:00Z" }
> [main] Today is Friday, Feb 13, 2026; planning is Monday Feb 16. Let me find the cleanup ticket Vincent assigned to me and locate Vincent. I'll search Linear and Trello.
   4 [main] mcp__mcp_4981f6c7__linear_list_issues {"assignee": "me", "limit": 50}
      => Error: result (53,253 characters) exceeds maximum allowed tokens. Output has been saved to /root/.claude/projects/-app/7a2780c2-0286-412b-a257-bb48c4fe2743/tool-results/mcp-mcp_4981f6c7-linear_list_issues-1788504142670.txt. Format: JSON with schema: {result: string} Use offset and limit parameters t …[+986]
   5 [main] mcp__mcp_4981f6c7__linear_list_users {"query": "Vincent"}
      => {"result":"{\"users\": [{\"id\": \"usr_65c76e0b87aa7e9b\", \"email\": \"vincent.parker@harmonygames.co\", \"name\": \"vincent.parker@harmonygames.co\", \"display_name\": \"vincent.parker@harmonygames.co\", \"avatar_url\": null, \"is_active\": true, \"created_at\": \"2024-04-15T21:29:22Z\", \"updated …[+59]
   6 [main] mcp__mcp_4981f6c7__trello_list_boards {}
      => {"result":"[{\"id\": \"65eb4ec525346c8070ca638f\", \"name\": \"DD Product Roadmap\", \"desc\": \"- Track product development and feature requests with stakeholders and product owners.\ \ - Prioritize feature requests for upcoming sprints and create a transparent development process with your agile t …[+21050]
> [main] The Linear issue list is large. Let me query the saved file directly for the cleanup ticket and Vincent's authored issues.
   7 [main] Bash {"command": "cd /root/.claude/projects/-app/7a2780c2-0286-412b-a257-bb48c4fe2743/tool-results/ && python3 -c \" import json d=json.load(open('mcp-mcp_4981f6c7-linear_list_issues-1788504142670.txt')) s=d['result'] data=json.loads(s) issues=data.get('issues',data) if isinstance(data,dict) else data print(type(data)) print(list(data.keys()) if isinstance(data,dict) else len(data)) \" "}
      => <class 'dict'> ['issues', 'next_cursor'] Shell cwd was reset to /app
   8 [main] Bash {"command": "cd /root/.claude/projects/-app/7a2780c2-0286-412b-a257-bb48c4fe2743/tool-results/ && python3 -c \" import json d=json.load(open('mcp-mcp_4981f6c7-linear_list_issues-1788504142670.txt')) data=json.loads(d['result']) issues=data['issues'] print('count',len(issues),'next',data['next_cursor']) for i in issues:     t=i.get('title','')     print(i.get('identifier'), '|', i.get('state',{}).g …[+85]
      => count 50 next NTA ENG-2439 | None | Fire symbol vfx still wrong on the boss camera path ENG-2438 | None | Board cleanup before planning ENG-2428 | None | Season Pass - UI Optimization ENG-2426 | None | Axe Arena - UI Optimization ENG-2415 | None | Quest UI Optimization ENG-2414 | None | Leaderboard  …[+2692]
> [main] Found **ENG-2438 "Board cleanup before planning"**. Let me get the full ticket.
   9 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-2438"}
      => {"result":"{\"id\": \"ENG-2438\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_65c76e0b87aa7e9b\", \"state_id\": \"Todo\", \"cycle_id\": null, \"identifier\": \"ENG-2438\", \"number\": 2438, \"title\": \"Board  …[+729]
> [main] The ticket points to the **board-cleanup** Slack channel. The task says the authoritative write-up is a document, and where write-up and channel differ, the write-up wins. Let me find the channel and read it.
  10 [main] mcp__mcp_4981f6c7__slack_search_channels {"query": "board-cleanup"}
      => {"result":"{\"ok\": true, \"channels\": [{\"id\": \"C09XK4M2QT7\", \"name\": \"board-cleanup\", \"is_channel\": true, \"is_private\": true, \"is_im\": false, \"is_mpim\": false, \"is_archived\": false, \"is_general\": false, \"num_members\": 3, \"created\": 1770649800}], \"has_more\": false, \"total …[+14]
  11 [main] mcp__mcp_4981f6c7__slack_read_channel {"channel": "C09XK4M2QT7", "limit": 100}
      => {"result":"{\"ok\": true, \"messages\": [{\"ts\": \"1770739260.002400\", \"type\": \"message\", \"text\": \"will do, ill sort marco once ive worked out what actually went where\", \"channel\": \"C09XK4M2QT7\", \"user\": \"EMPLOYEE_0006_SLACK_ID\"}, {\"ts\": \"1770739200.002300\", \"type\": \"message …[+7137]
> [main] This is a rich thread. Vincent (EMPLOYEE_0012) is the manager. The authoritative document is the **"board hygiene runbook"** — "where it disagrees with what I've said in this channel, go with the runbook." There are 79 tickets listed. Let me locate the runbook and supporting sources (version tracker sheet, streak fever schedule doc, the December-cut mail, and the dd-vfx-triage channel).  Let me set up task tracking and start gathering the authoritative sources.
  12 [main] mcp__mcp_4981f6c7__gdrive_search {"fullText": "board hygiene runbook"}
      => {"result":"{\"files\": [{\"id\": \"f_7b1e4c90a3d25f8614ac37\", \"name\": \"Board Hygiene Runbook\", \"mimeType\": \"application/vnd.google-apps.document\", \"owners\": [{\"emailAddress\": \"vincent.parker@harmonygames.co\", \"displayName\": \"vincent.parker@harmonygames.co\"}], \"permissions\": [{\" …[+847]
  13 [main] mcp__mcp_4981f6c7__gdocs_search_documents {"fullText": "board hygiene"}
      => {"result":"{\"documents\": [{\"documentId\": \"f_7b1e4c90a3d25f8614ac37\", \"title\": \"Board Hygiene Runbook\", \"name\": \"Board Hygiene Runbook\", \"revisionId\": \"1\", \"owners\": [\"vincent.parker@harmonygames.co\"], \"modifiedTime\": \"2026-01-19T11:04:00Z\", \"createdTime\": \"2026-01-19T11: …[+106]
  14 [main] mcp__mcp_4981f6c7__gdrive_search {"query": "runbook"}
      => {"result":"{\"files\": [{\"id\": \"f_7b1e4c90a3d25f8614ac37\", \"name\": \"Board Hygiene Runbook\", \"mimeType\": \"application/vnd.google-apps.document\", \"owners\": [{\"emailAddress\": \"vincent.parker@harmonygames.co\", \"displayName\": \"vincent.parker@harmonygames.co\"}], \"permissions\": [{\" …[+847]
> [main] Let me read the authoritative runbook in full.
  15 [main] mcp__mcp_4981f6c7__gdocs_get_document_text {"documentId": "f_7b1e4c90a3d25f8614ac37"}
      => {"result":"{\"documentId\": \"f_7b1e4c90a3d25f8614ac37\", \"title\": \"Board Hygiene Runbook\", \"name\": \"Board Hygiene Runbook\", \"revisionId\": \"1\", \"text\": \"Board Hygiene Runbook\ \ Engineering Ops. Written up after the last planning round went badly. If anything in chat contradicts this  …[+6756]
> [main] I have the authoritative runbook. Key rules I'll apply (runbook overrides chat where they differ):  - **State authority**: repo decides. Check **both merged PRs (body names ticket) AND commit history (messages naming ticket), across every repo the title could touch** — not PR-title, not a single repo. - **PO exception**: if the ticket was raised by that title's product owner AND updated within **120 days**, leave the state, comment the repo finding, and flag for planning. Owners: Zombie Match 3D → Julia Lawson; Domino Delights → Marcus Bennett; Combo Fighters → engineering (no exception). Check the 120-day window per ticket. - **Ship line** (from chat, not contradicted): merged to ship branch → Done; merged to a non-ship branch → In Progress. DD ships off `develop`, Zombie off `main`. - **Reverted** work doesn't count. **Sign-off**: if changes were requested but it merged anyway, flag it …[+619]
  16 [main] mcp__mcp_4981f6c7__linear_list_issues {"limit": 250, "maxDescriptionChars": 0}
      => Error: result (199,049 characters) exceeds maximum allowed tokens. Output has been saved to /root/.claude/projects/-app/7a2780c2-0286-412b-a257-bb48c4fe2743/tool-results/mcp-mcp_4981f6c7-linear_list_issues-1788504383590.txt. Format: JSON with schema: {result: string} Use offset and limit parameters  …[+987]
  17 [main] mcp__mcp_4981f6c7__gdrive_search {"fullText": "version tracker"}
      => {"result":"{\"files\": [{\"id\": \"f_13a1e5c4375d15711187dd\", \"name\": \"App Version Tracker.xlsx\", \"mimeType\": \"application/vnd.google-apps.spreadsheet\", \"parents\": [\"d_4b624c684850e238958446\"], \"owners\": [{\"emailAddress\": \"Resource: -6481757892984311338\", \"displayName\": \"Resour …[+4562]
  18 [main] mcp__mcp_4981f6c7__gsheets_search_spreadsheets {"query": "version"}
      => {"result":"{\"spreadsheets\": [{\"spreadsheetId\": \"f_13a1e5c4375d15711187dd\", \"title\": \"App Version Tracker\", \"owners\": [\"Resource: -6481757892984311338\"], \"modifiedTime\": \"2024-12-18T16:26:03Z\", \"createdTime\": \"2024-02-22T18:53:02Z\", \"driveFileId\": \"f_13a1e5c4375d15711187dd\"} …[+50]
  19 [main] mcp__mcp_4981f6c7__gdrive_search {"fullText": "LiveOps Event Calendar"}
      => {"result":"{\"files\": [{\"id\": \"f_b04156e116437611a5014a\", \"name\": \"LiveOps Event Calendar.xlsx\", \"mimeType\": \"application/vnd.google-apps.spreadsheet\", \"parents\": [\"d_ab884a308d722f3285420c\"], \"owners\": [{\"emailAddress\": \"Resource: -6481757892984311338\", \"displayName\": \"Res …[+3958]
  20 [main] mcp__mcp_4981f6c7__slack_search_channels {"query": "dd-vfx-triage"}
      => {"result":"{\"ok\": true, \"channels\": [{\"id\": \"C09VF7X3TQM\", \"name\": \"dd-vfx-triage\", \"is_channel\": true, \"is_private\": true, \"is_im\": false, \"is_mpim\": false, \"is_archived\": false, \"is_general\": false, \"num_members\": 3, \"created\": 1767621600}], \"has_more\": false, \"total …[+14]
  21 [main] mcp__mcp_4981f6c7__gmail_search_messages {"query": "december cut"}
      => {"result":"{\"messages\": [{\"id\": \"calvin.price@harmonygames.co/<CAOb2rk8fZ1mQpV7xL3nT9dY4wRj@mail.gmail.com>\", \"threadId\": \"calvin.price@harmonygames.co/1821553094412667181\"}, {\"id\": \"calvin.price@harmonygames.co/<CAJm7q2v8xNf3PkR5wLdT9hYbQ1sZ4eGmail@mail.gmail.com>\", \"threadId\": \"ca …[+105]
> [main] Let me read the tracker, the event calendar, the VFX-triage channel, the December-cut mail, and parse the full ticket list.
  22 [main] mcp__mcp_4981f6c7__gdrive_read_file {"fileId": "f_13a1e5c4375d15711187dd"}
      => {"result":"{\"mimeType\": \"text/csv\", \"text\": \"App Version,Android Release Date,Major Release,Content,Learning,Notes,,\\r\ 0.1.18,2024-01-13 00:00:00,No,UA Candidate,,,,\\r\ 0.1.24,2024-01-22 00:00:00,Yes,UA Build,,,,\\r\ 0.1.25,2024-01-23 00:00:00,No,Character [PERSON_NAME_47383] Fix,,,,\\r\ 0 …[+22639]
  23 [main] mcp__mcp_4981f6c7__gdrive_read_file {"fileId": "f_b04156e116437611a5014a"}
      => {"result":"{\"mimeType\": \"text/csv\", \"text\": \"MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY,,,,,,,,,,,,,,,,,,,\\r\ Win Streak,Win Streak,Win Streak,Win Streak,Win Streak,Win Streak,Win Streak,,,,,,,,,,,,,,,,,,,\\r\ Nathan's Booty,Nathan's Booty,Nathan's Booty,Nathan's Booty,Nathan's …[+1341]
  24 [main] mcp__mcp_4981f6c7__slack_read_channel {"channel": "C09VF7X3TQM", "limit": 50}
      => {"result":"{\"ok\": true, \"messages\": [{\"ts\": \"1770733320.000500\", \"type\": \"message\", \"text\": \"ive raised ENG-2439 so it doesnt get lost\", \"channel\": \"C09VF7X3TQM\", \"user\": \"EMPLOYEE_0002_SLACK_ID\"}, {\"ts\": \"1767720600.000400\", \"type\": \"message\", \"text\": \"yeah. dont  …[+839]
  25 [main] mcp__mcp_4981f6c7__gmail_get_thread {"thread_id": "calvin.price@harmonygames.co/1821553094412667181"}
      => {"result":"{\"total_count\": 1, \"limit\": 50, \"offset\": 0, \"has_more\": false, \"messages\": [{\"id\": \"calvin.price@harmonygames.co/<CAOb2rk8fZ1mQpV7xL3nT9dY4wRj@mail.gmail.com>\", \"threadId\": \"calvin.price@harmonygames.co/1821553094412667181\", \"labelIds\": [\"INBOX\", \"CATEGORY_PERSONAL …[+1224]
  26 [main] mcp__mcp_4981f6c7__gmail_get_thread {"thread_id": "calvin.price@harmonygames.co/1817402993551128470"}
      => {"result":"{\"total_count\": 1, \"limit\": 50, \"offset\": 0, \"has_more\": false, \"messages\": [{\"id\": \"calvin.price@harmonygames.co/<CAJm7q2v8xNf3PkR5wLdT9hYbQ1sZ4eGmail@mail.gmail.com>\", \"threadId\": \"calvin.price@harmonygames.co/1817402993551128470\", \"labelIds\": [\"INBOX\", \"CATEGORY_ …[+1987]
> [main] Now let me decode the key facts and parse all 79 tickets' metadata. Two important emails: - **Oliver Brooks**: nothing has gone out to players since the December build — publisher never opened a window after the December cut; everything since sits on internal tracks. - **Priya Nair (Northgate Publishing, publisher)**: last Android build pushed live was **0.2.82** (tracker date 2024-12-03); **0.2.85 was staged for December and held — not released, no date**. She wants which recent fixes reached players (live builds + platforms only).  And **dd-vfx-triage**: the fire-symbol VFX fix merged but was **pulled back out** (reverted with the camera pass) — "don't trust the ticket, it never got moved back"; ENG-2439 was raised to track it. That's ENG-2200 → a revert case.  Let me parse the 79 tickets' states/creators/dates and map Linear users.
  27 [main] mcp__mcp_4981f6c7__linear_list_users {"limit": 250}
      => {"result":"{\"users\": [{\"id\": \"usr_PERSON_3138\", \"email\": \"PERSON_3138_EMAIL\", \"name\": \"PERSON_3138_NAME\", \"display_name\": \"PERSON_3138_NAME\", \"avatar_url\": null, \"is_active\": true, \"created_at\": \"2025-03-10T19:40:46Z\", \"updated_at\": \"2025-12-16T22:28:24Z\"}, {\"id\": \"u …[+12100]
  28 [main] Bash {"command": "cd /root/.claude/projects/-app/7a2780c2-0286-412b-a257-bb48c4fe2743/tool-results/ && python3 -c \" import json d=json.load(open('mcp-mcp_4981f6c7-linear_list_issues-1788504383590.txt')) data=json.loads(d['result']) issues=data['issues'] print('total issues in file:', len(issues), 'next:', data['next_cursor']) want='''ART-384 ART-385 ART-424 ART-425 ART-426 ART-444 ART-542 ART-585 ART- …[+780]
      => total issues in file: 250 next: MjUw want count 79 MISSING from file: ['ART-384', 'ART-385', 'ART-424', 'ART-425', 'ART-426', 'ART-444', 'ART-542', 'ART-585', 'ART-605', 'ART-620', 'ART-705', 'ART-723', 'ART-760', 'ENG-233', 'ENG-1355', 'ENG-1387', 'ENG-1411', 'ENG-1444', 'ENG-1448', 'ENG-1452', 'EN …[+278]
> [main] The file has 250 issues but is missing 42 older ones. Let me extract the metadata for the 37 present and fetch the 42 missing directly. First, extract present ones.
  29 [main] Bash {"command": "cd /root/.claude/projects/-app/7a2780c2-0286-412b-a257-bb48c4fe2743/tool-results/ && python3 -c \" import json d=json.load(open('mcp-mcp_4981f6c7-linear_list_issues-1788504383590.txt')) issues=json.loads(d['result'])['issues'] want='ART-384 ART-385 ART-424 ART-425 ART-426 ART-444 ART-542 ART-585 ART-605 ART-620 ART-705 ART-723 ART-760 ENG-233 ENG-1355 ENG-1387 ENG-1411 ENG-1444 ENG-14 …[+962]
      => ENG-2022 |st= Todo |cr= marcus.bennett |upd= 2025-10-27T14:14:52Z |par= None | Streak Bar Cinematic Implementation ENG-2094 |st= Todo |cr= vincent |upd= 2025-10-27T14:16:02Z |par= None | Fast click on char unlock screen creates FPS  ENG-2149 |st= Todo |cr= vincent |upd= 2025-10-27T14:16:08Z |par= No …[+4100]
> [main] I now have 37 tickets' metadata and confirmed the product owners: **Julia Lawson** (Zombie, `usr_8140f09b…`) and **Marcus Bennett** (Domino Delights, `usr_c77c50cc…`).   Key date reasoning: `get_time` = **2026-02-13** (Friday before Monday's planning — consistent with the narrative). The 120-day PO-exception cutoff is therefore **2025-10-16** (updated_at ≥ that = protected; earlier = stale). This boundary is exactly what separates the Julia-Lawson ZOM tickets, which is the intended nuance.  Let me get the remaining 42 tickets (page 2), the parent tickets' states, and discover the GitHub repos.
  30 [main] mcp__mcp_4981f6c7__linear_list_issues {"limit": 250, "maxDescriptionChars": 0, "cursor": "MjUw"}
      => Error: result (202,825 characters) exceeds maximum allowed tokens. Output has been saved to /root/.claude/projects/-app/7a2780c2-0286-412b-a257-bb48c4fe2743/tool-results/mcp-mcp_4981f6c7-linear_list_issues-1788504564627.txt. Format: JSON with schema: {result: string} Use offset and limit parameters  …[+987]
  31 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2022"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
  32 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2200"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1917\", \"number\": 1917, \"title\": \"Fire symbol vfx after camera change\", \"state\": \"closed\", \"merged\": true, \"draft\": …[+1123]
> [main] Repo confirmed: **harmonygames-Games/GameOfDominoes** (Domino Delights, ships off `develop`). PR #1917 names ENG-2200, merged to develop 2026-01-05 — but dd-vfx-triage says it was pulled back out. I'll verify the revert. Let me discover all repos and extract the remaining 42 tickets + parent states from page 2.
  33 [main] mcp__mcp_4981f6c7__github_search_repositories {"query": "org:harmonygames-Games", "perPage": 100}
      => {"result":"{\"total_count\": 16, \"incomplete_results\": false, \"unpopulated_fields\": [], \"items\": [{\"id\": \"harmonygames-Games/Combo-Fighters\", \"name\": \"Combo-Fighters\", \"full_name\": \"harmonygames-Games/Combo-Fighters\", \"owner\": {\"login\": \"harmonygames-Games\", \"type\": \"Organ …[+8412]
  34 [main] Bash {"command": "cd /root/.claude/projects/-app/7a2780c2-0286-412b-a257-bb48c4fe2743/tool-results/ && python3 -c \" import json d=json.load(open('mcp-mcp_4981f6c7-linear_list_issues-1788504564627.txt')) data=json.loads(d['result']) issues=data['issues'] print('count',len(issues),'next',data['next_cursor']) want='ART-384 ART-385 ART-424 ART-425 ART-426 ART-444 ART-542 ART-585 ART-605 ART-620 ART-705 AR …[+1287]
      => count 250 next NTAw --- WANT (missing 42) --- ENG-2258 |st= Todo |cr= brian.foster |upd= 2025-08-14T19:14:19Z |par= None |comp= None | Infographic Tutorial Animations ZOM-390 |st= Backlog |cr= vincent |upd= 2025-07-15T17:24:27Z |par= None |comp= None | Icon and Event Visual for Win Streak Event ZOM- …[+897]
> [main] Repos identified. Global GitHub search spans all repos, so I'll search PRs + commits per ticket. Let me confirm `search_commits` works (test ENG-2200 + its revert), fetch page 3 for the remaining 38 tickets, and pull parent states from page 1.
  35 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2200"}
      => {"result":"{\"total_count\": 2, \"incomplete_results\": false, \"items\": [{\"sha\": \"6b204e9fa71c38d05e8213b4c7096fd5a8e31207\", \"commit\": {\"message\": \"Revert \\\"Fire symbol vfx after camera change ENG-2200\\\" - it fights the boss cam path, putting ENG-2200 back to open until we redo it\",  …[+760]
  36 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "camera pass boss"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
  37 [main] mcp__mcp_4981f6c7__linear_list_issues {"limit": 250, "maxDescriptionChars": 0, "cursor": "NTAw"}
      => Error: result (205,379 characters) exceeds maximum allowed tokens. Output has been saved to /root/.claude/projects/-app/7a2780c2-0286-412b-a257-bb48c4fe2743/tool-results/mcp-mcp_4981f6c7-linear_list_issues-1788504619578.txt. Format: JSON with schema: {result: string} Use offset and limit parameters  …[+987]
> [main] `search_commits` works and confirms the **ENG-2200 revert** (2026-01-06, "putting ENG-2200 back to open"). So ENG-2200 stays put. Let me parse page 3 for the remaining 38 tickets and pull all parent states from page 1.
  38 [main] Bash {"command": "cd /root/.claude/projects/-app/7a2780c2-0286-412b-a257-bb48c4fe2743/tool-results/ && python3 -c \" import json,glob files=['mcp-mcp_4981f6c7-linear_list_issues-1788504383590.txt','mcp-mcp_4981f6c7-linear_list_issues-1788504564627.txt','mcp-mcp_4981f6c7-linear_list_issues-1788504619578.txt'] byid={} for f in files:     d=json.load(open(f));      for i in json.loads(d['result'])['issues …[+1448]
      => total unique issues loaded: 750 ENG-1685 |st= Backlog |cr= vincent |upd= 2025-05-05T19:26:09Z |par= None |comp= None | River Tile End Game Screen Visual Impair ENG-2190 |st= Backlog |cr= vincent |upd= 2025-05-05T19:34:50Z |par= None |comp= None | Players' names are not visible in the fi ENG-2191 |st …[+1798]
> [main] `search_commits`/`search_pull_requests` are reliable global searches across all repos. Now let me fetch the 33 remaining tickets' metadata (older/archived ones), plus ZOM-118 (a parent).  Note: **ZOM-457 "Algo Level Issues" is Done but its child ZOM-458 is Todo** — a candidate "parent closed over unfinished child." I'll verify ZOM-458's repo status before flagging.
  39 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-384", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-384\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ART\", \"parent_id\": \"ART-360\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_c77c50cc15c5342d\", \"state_id\": \"Todo\", \"cycle_id\": null, \"identifier\": \"ART-384 …[+461]
  40 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-385", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-385\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ART\", \"parent_id\": \"ART-360\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_c77c50cc15c5342d\", \"state_id\": \"Todo\", \"cycle_id\": null, \"identifier\": \"ART-385 …[+565]
  41 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-424", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-424\", \"project_id\": null, \"team_id\": \"team_ART\", \"parent_id\": \"ART-386\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_Victor Barnes\", \"state_id\": \"In Review\", \"cycle_id\": null, \"identifier\": \"ART-424\", \"number\": 424, \"title\": \" …[+443]
  42 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-425", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-425\", \"project_id\": null, \"team_id\": \"team_ART\", \"parent_id\": \"ART-424\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_Victor Barnes\", \"state_id\": \"In Review\", \"cycle_id\": null, \"identifier\": \"ART-425\", \"number\": 425, \"title\": \" …[+451]
  43 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-426", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-426\", \"project_id\": null, \"team_id\": \"team_ART\", \"parent_id\": \"ART-424\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_Victor Barnes\", \"state_id\": \"In Review\", \"cycle_id\": null, \"identifier\": \"ART-426\", \"number\": 426, \"title\": \" …[+434]
  44 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-444", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-444\", \"project_id\": null, \"team_id\": \"team_ART\", \"parent_id\": \"ART-424\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_Victor Barnes\", \"state_id\": \"In Review\", \"cycle_id\": null, \"identifier\": \"ART-444\", \"number\": 444, \"title\": \" …[+452]
  45 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-542", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-542\", \"project_id\": null, \"team_id\": \"team_ART\", \"parent_id\": \"ART-386\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_Victor Barnes\", \"state_id\": \"In Review\", \"cycle_id\": null, \"identifier\": \"ART-542\", \"number\": 542, \"title\": \" …[+501]
  46 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-585", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-585\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ART\", \"parent_id\": \"ART-584\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_Robert\", \"state_id\": \"Todo\", \"cycle_id\": null, \"identifier\": \"ART-585\", \"numb …[+503]
  47 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-605", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-605\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ART\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_c77c50cc15c5342d\", \"state_id\": \"Todo\", \"cycle_id\": null, \"identifier\": \"ART-605\", \"n …[+511]
  48 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-620", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-620\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ART\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_c77c50cc15c5342d\", \"state_id\": \"Todo\", \"cycle_id\": null, \"identifier\": \"ART-620\", \"n …[+500]
  49 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-705", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-705\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ART\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_Robert\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"ART-705\", \"number\" …[+535]
  50 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-723", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-723\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ART\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_65c76e0b87aa7e9b\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"ART-723\",  …[+549]
  51 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-760", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-760\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ART\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_c77c50cc15c5342d\", \"state_id\": \"In Review\", \"cycle_id\": null, \"identifier\": \"ART-760\" …[+596]
  52 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-233", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-233\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_cc3e90160f490686\", \"state_id\": \"Canceled\", \"cycle_id\": null, \"identifier\": \"ENG-233\", \"number\": 233, \"title\": \"New H …[+470]
  53 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-1355", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-1355\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_63fffeb4fab5233e\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-1355\", \"number\": 1355, \"title\": \"Map no …[+615]
  54 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-1387", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-1387\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_Robert\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"ENG-1387\", \"number …[+540]
  55 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-1411", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-1411\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_65c76e0b87aa7e9b\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"ENG-1411\" …[+598]
  56 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-1444", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-1444\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_63fffeb4fab5233e\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-1444\", \"number\": 1444, \"title\": \"Allow  …[+608]
  57 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-1448", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-1448\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_Robert\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-1448\", \"number\": …[+642]
  58 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-1452", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-1452\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_Robert\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-1452\", \"number\": …[+630]
  59 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-1486", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-1486\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_65c76e0b87aa7e9b\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"ENG-1486\" …[+556]
  60 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-1669", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-1669\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_65c76e0b87aa7e9b\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"ENG-1669\" …[+560]
  61 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-1730", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-1730\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_c77c50cc15c5342d\", \"state_id\": \"Canceled\", \"cycle_id\": null, \"identifier\": \"ENG-1730\ …[+576]
  62 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-1731", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-1731\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_c77c50cc15c5342d\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"ENG-1731\" …[+515]
  63 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-1878", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-1878\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_65c76e0b87aa7e9b\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"ENG-1878\" …[+533]
  64 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-1882", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-1882\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": \"ENG-1806\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_65c76e0b87aa7e9b\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"EN …[+563]
  65 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-1976", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-1976\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_Robert\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"ENG-1976\", \"number …[+515]
  66 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-2017", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-2017\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_65c76e0b87aa7e9b\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"ENG-2017\" …[+510]
  67 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-2042", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-2042\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_65c76e0b87aa7e9b\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"ENG-2042\" …[+555]
  68 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-2076", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-2076\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": \"ENG-2072\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_65c76e0b87aa7e9b\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"EN …[+519]
  69 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-2154", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-2154\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_65c76e0b87aa7e9b\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"ENG-2154\" …[+518]
  70 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "EPI-5", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"EPI-5\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_EPI\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_Robert\", \"state_id\": \"In Progress\", \"cycle_id\": null, \"identifier\": \"EPI-5\", \"number\" …[+504]
  71 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ZOM-48", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ZOM-48\", \"project_id\": \"dbab77c7-f871-4888-abf8-d98b52a41624\", \"team_id\": \"team_ZOM\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_fc22d5941b2aeb5c\", \"state_id\": \"Backlog\", \"cycle_id\": null, \"identifier\": \"ZOM-48\", \" …[+519]
  72 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ZOM-118", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ZOM-118\", \"project_id\": \"dbab77c7-f871-4888-abf8-d98b52a41624\", \"team_id\": \"team_ZOM\", \"parent_id\": null, \"assignee_id\": \"usr_c77c50cc15c5342d\", \"creator_id\": \"usr_8140f09bf9f1b94c\", \"state_id\": \"Todo\", \"cycle_id\": null, \"identifier\": \"ZOM-118\", \"n …[+494]
> [main] I now have all 79 tickets' full metadata. Let me set up tracking and begin the GitHub verification phase (PR body + commit message, across all repos, per the runbook).
  73 [main] TaskCreate {"subject": "Verify all 79 tickets against repos (PRs + commits, all repos)", "description": "For each of the 79 flagged tickets, search merged PRs (body names ticket) and commit messages (all repos) to determine what actually landed. Record findings.", "activeForm": "Verifying tickets against repos"}
      => Task #1 created successfully: Verify all 79 tickets against repos (PRs + commits, all repos)
  74 [main] TaskCreate {"subject": "Apply states + comment every ticket per runbook rules", "description": "Update states per ship-line/revert/sign-off rules; apply PO 120-day exception (Julia Lawson ZOM, Marcus Bennett DD); comment repo+PR number, reached-players, no names. Comment even clean ones.", "activeForm": "Applying states and comments"}
      => Task #2 created successfully: Apply states + comment every ticket per runbook rules
  75 [main] TaskCreate {"subject": "Fix Streak Fever schedule (ENG-2274) from LiveOps Event Calendar", "description": "Establish what days Streak Fever runs from the LiveOps Event Calendar (not backend cron), correct the schedule doc, note correction on ticket.", "activeForm": "Fixing Streak Fever schedule"}
      => Task #3 created successfully: Fix Streak Fever schedule (ENG-2274) from LiveOps Event Calendar
  76 [main] TaskCreate {"subject": "Flag parents closed over unfinished children", "description": "ZOM-457 (Done) has open child ZOM-458; check others. Flag on tickets.", "activeForm": "Flagging closed parents"}
      => Task #4 created successfully: Flag parents closed over unfinished children
  77 [main] TaskCreate {"subject": "Email Priya (publisher) and Marco (cert partner) per disclosure rules", "description": "Priya: live builds/platforms only (which recent fixes reached players). Marco: staged Dec build number + platform only. No tickets/PRs/names.", "activeForm": "Emailing external partners"}
      => Task #5 created successfully: Email Priya (publisher) and Marco (cert partner) per disclosure rules
  78 [main] TaskCreate {"subject": "Post summary to board-cleanup channel", "description": "One message, exceptions + near-misses only, ticket IDs only, no PR numbers/branches/names.", "activeForm": "Posting channel summary"}
      => Task #6 created successfully: Post summary to board-cleanup channel
  79 [main] TaskUpdate {"taskId": "1", "status": "in_progress"}
      => Updated task #1 status
> [main] Now the verification phase. I'll search PRs (body) and commits (messages, all repos) for each ticket. Starting with the recent bug/feature cluster.
  80 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2022"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
  81 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2022"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
  82 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2094"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
  83 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2094"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
  84 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2149"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
  85 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2149"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
  86 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2181"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
  87 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2181"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
  88 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2274"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
  89 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2274"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
  90 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2344"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
  91 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2344"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
  92 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2384"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
  93 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2384"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
> [main] No merged work for that batch. Continuing with the UI-optimization cluster (Oliver flagged these as having merged).
  94 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2402"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
  95 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2402"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
  96 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2405"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1905\", \"number\": 1905, \"title\": \"ENG-2405: Mini-Games UI Optimization\", \"state\": \"closed\", \"merged\": true, \"draft\" …[+1763]
  97 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2405"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
  98 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2406"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
  99 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2406"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 100 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2410"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 101 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2410"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"items\": [{\"sha\": \"ada49ce996d749cf652249dd9ca2ed20fc517870\", \"commit\": {\"message\": \"Merge branch 'develop' into [PERSON_NAME_0092]/ENG-2410\ \ # Conflicts:\ #\\tAssets/AddressableAssetsData/link.xml.meta\ #\\tAssets/GoD/Conve …[+8481]
 102 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2414"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 103 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2414"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 104 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2415"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 105 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2415"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 106 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2417"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1901\", \"number\": 1901, \"title\": \"ENG-2417: Settings UI Optimization\", \"state\": \"closed\", \"merged\": true, \"draft\":  …[+1343]
 107 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2417"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
> [main] Key finding: **PR #1905** (title "ENG-2405") merged to `develop` but its **body names ENG-2432/2433/2434/2435** (the mini-game children), not 2405 — a title-vs-body distinction the runbook cares about. **ENG-2417** merged to develop (#1901). **ENG-2410** only has a "merge develop into feature-branch" commit — not landed on develop (near-miss).  Let me sweep the rest of the UI-optimization cluster via PR-body search.
 108 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2418"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1902\", \"number\": 1902, \"title\": \"ENG-2418: Level - win UI Optimization\", \"state\": \"closed\", \"merged\": true, \"draft\ …[+949]
 109 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2419"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1903\", \"number\": 1903, \"title\": \"ENG-2419: Level Lose - Out-of-moves Screens UI Optimization\", \"state\": \"closed\", \"me …[+1384]
 110 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2424"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 111 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2425"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1895\", \"number\": 1895, \"title\": \"ENG-2425: Nathan's Treasure - UI Optimization\", \"state\": \"closed\", \"merged\": true,  …[+1251]
 112 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2426"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1908\", \"number\": 1908, \"title\": \"ENG-2426: Axe Arena - UI Optimization\", \"state\": \"closed\", \"merged\": true, \"draft\ …[+951]
 113 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2427"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 114 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2428"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 115 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2429"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 116 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2430"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 117 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2431"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 118 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2432"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1905\", \"number\": 1905, \"title\": \"ENG-2405: Mini-Games UI Optimization\", \"state\": \"closed\", \"merged\": true, \"draft\" …[+1763]
 119 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2433"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1905\", \"number\": 1905, \"title\": \"ENG-2405: Mini-Games UI Optimization\", \"state\": \"closed\", \"merged\": true, \"draft\" …[+1763]
 120 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2434"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1905\", \"number\": 1905, \"title\": \"ENG-2405: Mini-Games UI Optimization\", \"state\": \"closed\", \"merged\": true, \"draft\" …[+1763]
 121 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2435"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1905\", \"number\": 1905, \"title\": \"ENG-2405: Mini-Games UI Optimization\", \"state\": \"closed\", \"merged\": true, \"draft\" …[+1763]
 122 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2437"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
> [main] UI cluster so far: **merged to develop** = ENG-2417(#1901), 2418(#1902), 2419(#1903), 2425(#1895), 2426(#1908), and 2432/2433/2434/2435(#1905, body-named). No PR-body hit yet for 2410, 2414, 2415, 2424, 2427, 2428, 2429, 2430, 2431, 2437. Let me check the parent umbrella PRs (ENG-2403, ENG-2404) and commit-search the no-hit children.
 123 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2403"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 124 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2404"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 125 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2414"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 126 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2415"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 127 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2424"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 128 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2427"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 129 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2431"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 130 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2437"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
> [main] UI children 2414, 2415, 2424, 2427, 2431, 2437 and the umbrella parents 2403/2404 have **nothing merged**. Now checking the remaining "Validation" UI tickets via commits and starting the ZOM/EPI sweep.
 131 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2428"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 132 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2429"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 133 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2430"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 134 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ZOM-631"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 135 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ZOM-631"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 136 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ZOM-637"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 137 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ZOM-637"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 138 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ZOM-638"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 139 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ZOM-638"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 140 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ZOM-642"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/match3d#540\", \"number\": 540, \"title\": \"[PERSON_NAME_0029]/remove game modes\", \"state\": \"closed\", \"merged\": true, \"draft\": false,  …[+1192]
 141 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ZOM-642"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 142 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ZOM-666"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/match3d#540\", \"number\": 540, \"title\": \"[PERSON_NAME_0029]/remove game modes\", \"state\": \"closed\", \"merged\": true, \"draft\": false,  …[+1192]
 143 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ZOM-666"}
      => {"result":"{\"total_count\": 2, \"incomplete_results\": false, \"items\": [{\"sha\": \"102aa4f0d881086c8e648d6c66680b5cde1d8279\", \"commit\": {\"message\": \"Remove zombie related feats of strength from the leaderboards.  ZOM-666\ \ Remove zombie related feats of strength from the leaderboards.  ZO …[+1051]
> [main] Critical ZOM finding: **PR #540 (match3d) names both ZOM-642 and ZOM-666, merged to base `lite` — NOT `main`** (Zombie's ship line). So this landed on a non-ship branch. Applying the PO 120-day rule: **ZOM-642** (Julia, moved 2025-10-20 → protected) vs **ZOM-666** (Julia, moved 2025-10-10 → stale → repo decides). That's the intended "who raised it / how recently it moved" split. ZOM-631/637/638 have nothing merged.  Let me PR-sweep the remaining ZOM/EPI/ART/old-ENG tickets.
 144 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ZOM-344"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 145 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ZOM-458"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 146 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ZOM-483"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 147 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ZOM-613"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 148 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ZOM-48"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/match3d#500\", \"number\": 500, \"title\": \"ZOM-481: Zombie Health bar persists too long after death\", \"state\": \"closed\", \"merged\": true …[+1533]
 149 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ZOM-121"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 150 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ZOM-243"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 151 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ZOM-390"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 152 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "EPI-5"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 153 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ZOM-344"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 154 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ZOM-458"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 155 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ZOM-483"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 156 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ZOM-613"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 157 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ZOM-48"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 158 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ZOM-121"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 159 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ZOM-243"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 160 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ZOM-390"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 161 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "EPI-5"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
> [main] Noted a false substring match: query "ZOM-48" hit PR #500 which is actually **ZOM-481** (body names ZOM-481, not ZOM-48) — a near-miss; ZOM-48 has nothing. I'll verify exact IDs carefully. ZOM-344/458/483/613/121/243/390 and EPI-5: nothing merged.  Now sweeping the ART and older-ENG tickets (PR-body search).
 162 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ART-384"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 163 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ART-385"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 164 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ART-424"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 165 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ART-425"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 166 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ART-426"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 167 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ART-444"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 168 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ART-542"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 169 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ART-585"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 170 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ART-605"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 171 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ART-620"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 172 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ART-705"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 173 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ART-723"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 174 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ART-760"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1636\", \"number\": 1636, \"title\": \"Sagamap Unlock Features/Buttons Vfx\", \"state\": \"closed\", \"merged\": true, \"draft\": …[+1195]
 175 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ART-760"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 176 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ART-585"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 177 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ART-605"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 178 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ART-620"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
> [main] **ART-760** merged to `develop` (PR #1636, body names ART-760, 2025-01-17) — currently "In Review", stale creator → repo decides → Done (but not shipped: no release after Dec cut). Other ART tickets: nothing merged. Now the older-ENG sweep.
 179 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-233 "}
      => {"result":"{\"total_count\": 4, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1882\", \"number\": 1882, \"title\": \"ENG-2331: After win&collect is completed, the null reference creates buzzing sound.\", \"s …[+5901]
 180 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-1355"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1081\", \"number\": 1081, \"title\": \"harmonygames/[PERSON_NAME_0029]/scroll saga map\", \"state\": \"closed\", \"merged\": true …[+1224]
 181 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-1387"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 182 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-1411"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 183 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-1444"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1081\", \"number\": 1081, \"title\": \"harmonygames/[PERSON_NAME_0029]/scroll saga map\", \"state\": \"closed\", \"merged\": true …[+1224]
 184 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-1448"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1081\", \"number\": 1081, \"title\": \"harmonygames/[PERSON_NAME_0029]/scroll saga map\", \"state\": \"closed\", \"merged\": true …[+1224]
 185 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-1452"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1081\", \"number\": 1081, \"title\": \"harmonygames/[PERSON_NAME_0029]/scroll saga map\", \"state\": \"closed\", \"merged\": true …[+1224]
 186 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-1486"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 187 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-1669"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 188 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-1730"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"id\": \"harmonygames-Games/GameOfDominoes#1324\", \"number\": 1324, \"title\": \"Marcus/strake bar cinematic\", \"state\": \"closed\", \"merged\": true, \"draft\": false,  …[+1074]
 189 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-1731"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 190 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-1878"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 191 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-1882"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 192 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-1976"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 193 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2017"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 194 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2042"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 195 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2076"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 196 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2154"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 197 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-1685"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 198 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2190"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 199 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2191"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
 200 [main] mcp__mcp_4981f6c7__github_search_pull_requests {"query": "ENG-2258"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}
> [main] **ENG-1355/1444/1448/1452** all landed via PR #1081 to develop (2024-09-27) — already Done, repo confirms. **ENG-1730** (currently Canceled) has PR #1324 (body names ENG-1730) merged to develop 2024-10-18 — a disagreement I'll investigate for a revert. The "ENG-233" hits were substring false-matches (ENG-2330/2331/2337/2339). Now commit-searching the remaining older-ENG tickets and checking ENG-1730 for a revert.
 201 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-1730"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 202 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "strake bar"}
      => {"result":"{\"total_count\": 2, \"incomplete_results\": false, \"items\": [{\"sha\": \"c537f57b6893fdb9ef6b8e5ffa0a9ec6ce3fb6d1\", \"commit\": {\"message\": \"Strake bar powerup vfx\", \"author\": {\"name\": \"marcus\", \"email\": \"marcus@harmonygames.co\", \"date\": \"2024-10-17T11:01:24Z\"}, \"co …[+778]
 203 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-1387"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 204 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-1411"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 205 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-1486"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 206 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-1669"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 207 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-1731"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 208 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-1878"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 209 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-1882"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 210 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-1976"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 211 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2017"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 212 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2042"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 213 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2076"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 214 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2154"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 215 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-1685"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 216 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2190"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 217 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2191"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 218 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2258"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
> [main] ENG-1730 confirmed: PR #1324 merged to develop (2024-10-18), streak-bar VFX commits present, **no revert** — yet the ticket is Canceled. Repo disagrees; creator is stale → repo decides. All other older-ENG tickets: nothing merged. Let me finish coverage with the ART commit checks.
 219 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ART-384"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 220 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ART-385"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 221 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ART-424"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 222 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ART-425"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 223 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ART-426"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 224 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ART-444"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 225 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ART-542"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 226 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ART-705"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 227 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ART-723"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
 228 [main] mcp__mcp_4981f6c7__github_search_commits {"query": "ENG-2200"}
      => {"result":"{\"total_count\": 2, \"incomplete_results\": false, \"items\": [{\"sha\": \"6b204e9fa71c38d05e8213b4c7096fd5a8e31207\", \"commit\": {\"message\": \"Revert \\\"Fire symbol vfx after camera change ENG-2200\\\" - it fights the boss cam path, putting ENG-2200 back to open until we redo it\",  …[+760]
> [main] Full repo verification complete for all 79. Now the sign-off check (runbook §3: an ignored review is a process finding). Let me pull reviews on the PRs that actually landed.
 229 [main] mcp__mcp_4981f6c7__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "GameOfDominoes", "pullNumber": 1901}
      => {"result":"[{\"id\": \"harmonygames-Games/GameOfDominoes#1901#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0025_GITHUB_USERNAME\"}, \"state\": \"APPROVED\", \"body\": \"\", \"submitted_at\": \"2025-11-19T13:04:11Z\", \"commit_id\": null}]"}
 230 [main] mcp__mcp_4981f6c7__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "GameOfDominoes", "pullNumber": 1902}
      => {"result":"[{\"id\": \"harmonygames-Games/GameOfDominoes#1902#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0025_GITHUB_USERNAME\"}, \"state\": \"APPROVED\", \"body\": \"\", \"submitted_at\": \"2025-11-19T13:04:36Z\", \"commit_id\": null}]"}
 231 [main] mcp__mcp_4981f6c7__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "GameOfDominoes", "pullNumber": 1903}
      => {"result":"[{\"id\": \"harmonygames-Games/GameOfDominoes#1903#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0025_GITHUB_USERNAME\"}, \"state\": \"APPROVED\", \"body\": \"\", \"submitted_at\": \"2025-11-19T13:04:58Z\", \"commit_id\": null}]"}
 232 [main] mcp__mcp_4981f6c7__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "GameOfDominoes", "pullNumber": 1895}
      => {"result":"[{\"id\": \"harmonygames-Games/GameOfDominoes#1895#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0025_GITHUB_USERNAME\"}, \"state\": \"APPROVED\", \"body\": \"\", \"submitted_at\": \"2025-11-13T23:41:19Z\", \"commit_id\": null}]"}
 233 [main] mcp__mcp_4981f6c7__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "GameOfDominoes", "pullNumber": 1908}
      => {"result":"[{\"id\": \"harmonygames-Games/GameOfDominoes#1908#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0025_GITHUB_USERNAME\"}, \"state\": \"APPROVED\", \"body\": \"\", \"submitted_at\": \"2025-11-20T01:51:51Z\", \"commit_id\": null}]"}
 234 [main] mcp__mcp_4981f6c7__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "GameOfDominoes", "pullNumber": 1905}
      => {"result":"[{\"id\": \"harmonygames-Games/GameOfDominoes#1905#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0025_GITHUB_USERNAME\"}, \"state\": \"APPROVED\", \"body\": \"\", \"submitted_at\": \"2025-11-19T13:05:32Z\", \"commit_id\": null}]"}
 235 [main] mcp__mcp_4981f6c7__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "GameOfDominoes", "pullNumber": 1636}
      => {"result":"[{\"id\": \"harmonygames-Games/GameOfDominoes#1636#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0003_GITHUB_USERNAME\"}, \"state\": \"APPROVED\", \"body\": \"\", \"submitted_at\": \"2025-01-17T22:16:26Z\", \"commit_id\": null}]"}
 236 [main] mcp__mcp_4981f6c7__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "GameOfDominoes", "pullNumber": 1324}
      => {"result":"[{\"id\": \"harmonygames-Games/GameOfDominoes#1324#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0032_GITHUB_USERNAME\"}, \"state\": \"APPROVED\", \"body\": \"\", \"submitted_at\": \"2024-10-18T10:41:23Z\", \"commit_id\": null}]"}
 237 [main] mcp__mcp_4981f6c7__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "match3d", "pullNumber": 540}
      => {"result":"[{\"id\": \"harmonygames-Games/match3d#540#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0003_GITHUB_USERNAME\"}, \"state\": \"CHANGES_REQUESTED\", \"body\": \"Always avoid string comparison and changing enums' order. Nice Work!\", \"submitted_at\": \"2025-10-22T21:31:27Z\", \"commit_id\": nu …[+6]
> [main] Sign-off finding: **PR #540 (ZOM-642/ZOM-666) was merged over a CHANGES_REQUESTED review** with no re-approval — a process finding to flag on both. All DD develop PRs were approved.  I now have complete verification. Let me finish a few dependencies before writing: check remaining parent states (for closed-over-open-children), locate the Streak Fever schedule doc, and find Marco/certline's contact.
 238 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-360", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-360\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ART\", \"parent_id\": null, \"assignee_id\": \"usr_c77c50cc15c5342d\", \"creator_id\": \"usr_Robert\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ART-360\", \"number\": 3 …[+595]
 239 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-386", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-386\", \"project_id\": null, \"team_id\": \"team_ART\", \"parent_id\": null, \"assignee_id\": null, \"creator_id\": \"usr_Victor Barnes\", \"state_id\": \"Canceled\", \"cycle_id\": null, \"identifier\": \"ART-386\", \"number\": 386, \"title\": \"GAMEPLAY BETA\", \"descripti …[+407]
 240 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ART-584", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ART-584\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ART\", \"parent_id\": null, \"assignee_id\": \"usr_51f5f16d46e8cf55\", \"creator_id\": \"usr_Robert\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ART-584\", \"number\": 5 …[+629]
 241 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-1806", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-1806\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_c77c50cc15c5342d\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-1806\", \ …[+665]
 242 [main] mcp__mcp_4981f6c7__linear_get_issue {"id": "ENG-2072", "maxDescriptionChars": 0}
      => {"result":"{\"id\": \"ENG-2072\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_cd7849ec043ab3da\", \"creator_id\": \"usr_65c76e0b87aa7e9b\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-2072\", \ …[+454]
 243 [main] mcp__mcp_4981f6c7__gdrive_search {"fullText": "Streak Fever"}
      => {"result":"{\"files\": [{\"id\": \"f_948768f5a462e7037d17c9\", \"name\": \"Economy Changes for Domino Delights.docx\", \"mimeType\": \"application/vnd.google-apps.document\", \"parents\": [\"d_63fffeb4fab5233ed5bb73\"], \"owners\": [{\"emailAddress\": \"leonard.hayes@harmonygames.co\", \"displayName …[+16967]
 244 [main] mcp__mcp_4981f6c7__gdocs_search_documents {"fullText": "Streak Fever"}
      => {"result":"{\"documents\": [{\"documentId\": \"f_948768f5a462e7037d17c9\", \"title\": \"Economy Changes for Domino Delights\", \"name\": \"Economy Changes for Domino Delights\", \"revisionId\": \"c909f275b1\", \"owners\": [\"leonard.hayes@harmonygames.co\"], \"modifiedTime\": \"2025-12-12T21:47:11Z\ …[+1515]
 245 [main] mcp__mcp_4981f6c7__contacts_search_contacts {"query": "Marco"}
      => {"result":"{\"contacts\": [{\"contact_id\": \"c8a1d4f70b23e59c6a4f21e3\", \"first_name\": \"Marco\", \"last_name\": \"Reyes\", \"is_user\": false, \"gender\": \"Unknown\", \"age\": null, \"nationality\": null, \"city_living\": null, \"country\": null, \"status\": \"active\", \"job\": null, \"descrip …[+154]
> [main] Marco = **marco@certline.io** (Marco Reyes, cert partner). Streak Fever docs: the shared spec `[LiveOps] Streak Fever` (product-owned, I can only read) and my own editable `[LiveOps] Streak Fever Overview`. The LiveOps Event Calendar (source of truth) shows **Streak Fever runs Tuesday only**.  Also found several **closed parents over unfinished children**: ZOM-457→ZOM-458, ART-360→ART-384/385, ART-584→ART-585, ENG-1806→ENG-1882, ENG-2072→ENG-2076.  Let me read both Streak Fever docs to locate the schedule claim to correct.
 246 [main] mcp__mcp_4981f6c7__gdocs_get_document_text {"documentId": "f_cccfcf7859b52dae552a09"}
      => {"result":"{\"documentId\": \"f_cccfcf7859b52dae552a09\", \"title\": \"[LiveOps] Streak Fever Overview\", \"name\": \"[LiveOps] Streak Fever Overview\", \"revisionId\": \"35cf02b7c0\", \"text\": \"Streak Fever Overview\ Objectives:\ For HARMONY GAMES:\ Increases playtime and engagement.\ Encourages  …[+1179]
 247 [main] mcp__mcp_4981f6c7__gdocs_get_document_text {"documentId": "f_97bbbdbf4a6078fa98e7a0"}
      => {"result":"{\"documentId\": \"f_97bbbdbf4a6078fa98e7a0\", \"title\": \"[LiveOps] Streak Fever\", \"name\": \"[LiveOps] Streak Fever\", \"revisionId\": \"97bbbdbf4a\", \"text\": \"Domino Delights Streak Fever v1.0\ How to read this doc\ Black text means description/explanation\ Most feature specs wil …[+19090]
> [main] Both Streak Fever docs state the schedule as "Monday, Thursday, Saturday, Sunday," but the **LiveOps Event Calendar (source of truth) shows Streak Fever runs Tuesday only**. The product spec is product-owned (read-only for me); my own `[LiveOps] Streak Fever Overview` is the editable "doc we've got." Let me correct it to Tuesday.
 248 [main] mcp__mcp_4981f6c7__gdocs_batch_update {"documentId": "f_cccfcf7859b52dae552a09", "requests": [{"replaceAllText": {"containsText": {"text": "Event runs on Monday, Thursday, Saturday, and Sunday, resetting at UTC midnight.", "matchCase": true}, "replaceText": "Event runs on Tuesday, resetting at UTC midnight. (Corrected 2026-02-13 to match the LiveOps Event Calendar, the source of truth for live event days; the previous Mon/Thu/Sat/Sun  …[+65]
      => {"result":"{\"documentId\": \"f_cccfcf7859b52dae552a09\", \"replies\": [{\"occurrencesChanged\": 1}], \"writeControl\": {\"requiredRevisionId\": \"17b23bf4c5edde4315c0\"}}"}
> [main] Doc corrected. Now executing Linear updates. **Group 1 — DD UI tickets that merged to `develop` (ship line) → Done** (not yet shipped: no release since the December cut). Comment then set state, per ticket.
 249 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2417", "body": "Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1901; PR body names this ticket, review approved, not reverted. develop is the DD ship line, so this is Done. Reached players: no — no store release has gone out since the December cut (last live build 0.2.82, Android), so no build has carried it and it is live on no platform."}
      => {"result":"{\"id\": \"comment_e39b7a960ec94b74b08c253d30d42d30\", \"issue_id\": \"ENG-2417\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1901; PR body names this ticket, review approved,  …[+344]
 250 [main] mcp__mcp_4981f6c7__linear_update_issue {"id": "ENG-2417", "state": "Done"}
      => {"result":"{\"id\": \"ENG-2417\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": \"ENG-2403\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_fc22d5941b2aeb5c\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-2417\", \"number\": 2417, \"title\":  …[+556]
 251 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2418", "body": "Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1902; PR body names this ticket, review approved, not reverted. develop is the DD ship line, so this is Done. Reached players: no — no store release has gone out since the December cut (last live build 0.2.82, Android), so no build has carried it and it is live on no platform."}
      => {"result":"{\"id\": \"comment_54b245c51b1649d9986da0d4646ec60f\", \"issue_id\": \"ENG-2418\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1902; PR body names this ticket, review approved,  …[+344]
 252 [main] mcp__mcp_4981f6c7__linear_update_issue {"id": "ENG-2418", "state": "Done"}
      => {"result":"{\"id\": \"ENG-2418\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": \"ENG-2403\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_fc22d5941b2aeb5c\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-2418\", \"number\": 2418, \"title\":  …[+474]
 253 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2419", "body": "Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1903; PR body names this ticket, review approved, not reverted. develop is the DD ship line, so this is Done. Reached players: no — no store release has gone out since the December cut (last live build 0.2.82, Android), so no build has carried it and it is live on no platform."}
      => {"result":"{\"id\": \"comment_dcd8ee34c5e94a5b88b0eab93432198f\", \"issue_id\": \"ENG-2419\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1903; PR body names this ticket, review approved,  …[+344]
 254 [main] mcp__mcp_4981f6c7__linear_update_issue {"id": "ENG-2419", "state": "Done"}
      => {"result":"{\"id\": \"ENG-2419\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": \"ENG-2403\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_fc22d5941b2aeb5c\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-2419\", \"number\": 2419, \"title\":  …[+521]
 255 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2425", "body": "Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1895; PR body names this ticket, review approved, not reverted. develop is the DD ship line, so this is Done. Reached players: no — no store release has gone out since the December cut (last live build 0.2.82, Android), so no build has carried it and it is live on no platform."}
      => {"result":"{\"id\": \"comment_fe49482dc96b4922bd9c7bca284a507d\", \"issue_id\": \"ENG-2425\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1895; PR body names this ticket, review approved,  …[+344]
 256 [main] mcp__mcp_4981f6c7__linear_update_issue {"id": "ENG-2425", "state": "Done"}
      => {"result":"{\"id\": \"ENG-2425\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": \"ENG-2404\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_fc22d5941b2aeb5c\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-2425\", \"number\": 2425, \"title\":  …[+483]
 257 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2426", "body": "Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1908; PR body names this ticket, review approved, not reverted. develop is the DD ship line, so this is Done. Reached players: no — no store release has gone out since the December cut (last live build 0.2.82, Android), so no build has carried it and it is live on no platform."}
      => {"result":"{\"id\": \"comment_b776255489df41cfac833c5f2336e59b\", \"issue_id\": \"ENG-2426\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1908; PR body names this ticket, review approved,  …[+344]
 258 [main] mcp__mcp_4981f6c7__linear_update_issue {"id": "ENG-2426", "state": "Done"}
      => {"result":"{\"id\": \"ENG-2426\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": \"ENG-2404\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_fc22d5941b2aeb5c\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-2426\", \"number\": 2426, \"title\":  …[+474]
 259 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2432", "body": "Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1905; this ticket is named in the PR body (the PR is titled after parent ENG-2405 but its body lists ENG-2432/2433/2434/2435), review approved, not reverted. develop is the DD ship line, so this is Done. Reached players: no — no store release has gone out since the December cut (last  …[+88]
      => {"result":"{\"id\": \"comment_e167a48de46c4828b766fcb2fd0e1f27\", \"issue_id\": \"ENG-2432\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1905; this ticket is named in the PR body (the PR  …[+438]
 260 [main] mcp__mcp_4981f6c7__linear_update_issue {"id": "ENG-2432", "state": "Done"}
      => {"result":"{\"id\": \"ENG-2432\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": \"ENG-2405\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_fc22d5941b2aeb5c\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-2432\", \"number\": 2432, \"title\":  …[+436]
 261 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2433", "body": "Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1905; this ticket is named in the PR body (PR titled after parent ENG-2405; body lists ENG-2432/2433/2434/2435), review approved, not reverted. develop is the DD ship line, so this is Done. Reached players: no — no store release has gone out since the December cut (last live build 0.2 …[+74]
      => {"result":"{\"id\": \"comment_41319d63bbd04a5087ff692b26d58411\", \"issue_id\": \"ENG-2433\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1905; this ticket is named in the PR body (PR titl …[+424]
 262 [main] mcp__mcp_4981f6c7__linear_update_issue {"id": "ENG-2433", "state": "Done"}
      => {"result":"{\"id\": \"ENG-2433\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": \"ENG-2405\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_fc22d5941b2aeb5c\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-2433\", \"number\": 2433, \"title\":  …[+437]
 263 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2434", "body": "Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1905; this ticket is named in the PR body (PR titled after parent ENG-2405; body lists ENG-2432/2433/2434/2435), review approved, not reverted. develop is the DD ship line, so this is Done. Reached players: no — no store release has gone out since the December cut (last live build 0.2 …[+74]
      => {"result":"{\"id\": \"comment_6a687e7321a746288af32c42fb80de3d\", \"issue_id\": \"ENG-2434\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1905; this ticket is named in the PR body (PR titl …[+424]
 264 [main] mcp__mcp_4981f6c7__linear_update_issue {"id": "ENG-2434", "state": "Done"}
      => {"result":"{\"id\": \"ENG-2434\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": \"ENG-2405\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_fc22d5941b2aeb5c\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-2434\", \"number\": 2434, \"title\":  …[+436]
 265 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2435", "body": "Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1905; this ticket is named in the PR body (PR titled after parent ENG-2405; body lists ENG-2432/2433/2434/2435), review approved, not reverted. develop is the DD ship line, so this is Done. Reached players: no — no store release has gone out since the December cut (last live build 0.2 …[+74]
      => {"result":"{\"id\": \"comment_71a05388dfd74a5984b46b5c18603198\", \"issue_id\": \"ENG-2435\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1905; this ticket is named in the PR body (PR titl …[+424]
 266 [main] mcp__mcp_4981f6c7__linear_update_issue {"id": "ENG-2435", "state": "Done"}
      => {"result":"{\"id\": \"ENG-2435\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": \"ENG-2405\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_fc22d5941b2aeb5c\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-2435\", \"number\": 2435, \"title\":  …[+436]
> [main] **Group 2 — remaining exceptions**: ART-760 & ENG-1730 → Done; ZOM-666 → In Progress (merged to non-ship `lite`); ZOM-642 protected (leave + flag); ENG-2200 reverted (leave + flag); and confirm the four saga-map tickets that shipped in 0.2.46.
 267 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ART-760", "body": "Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1636; PR body names this ticket, review approved, not reverted. develop is the DD ship line, so this is Done (was In Review). Reached players: no — the merge (Jan 2025) has no store release dated on or after it; nothing has gone out since the December cut (last live build 0.2.82, Andro …[+64]
      => {"result":"{\"id\": \"comment_f39440f0ca44402bb3e18270ee481e9a\", \"issue_id\": \"ART-760\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Merged to develop in GameOfDominoes #1636; PR body names this ticket, review approved, n …[+414]
 268 [main] mcp__mcp_4981f6c7__linear_update_issue {"id": "ART-760", "state": "Done"}
      => {"result":"{\"id\": \"ART-760\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ART\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_c77c50cc15c5342d\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ART-760\", \"n …[+1414]
 269 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-1730", "body": "Board cleanup (pre-planning, repo-verified). Disagreement flagged: this ticket is Canceled, but the streak-bar powering VFX was merged to develop in GameOfDominoes #1324, review approved, and was not reverted. develop is the DD ship line, so per repo this is Done, not Canceled — moving it and flagging for planning to confirm the intent. Reached players: yes — carri …[+101]
      => {"result":"{\"id\": \"comment_dfd4f6f4baf842b4bcbd1d220e5fb3c8\", \"issue_id\": \"ENG-1730\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Disagreement flagged: this ticket is Canceled, but the streak-bar powering VFX was merg …[+457]
 270 [main] mcp__mcp_4981f6c7__linear_update_issue {"id": "ENG-1730", "state": "Done"}
      => {"result":"{\"id\": \"ENG-1730\", \"project_id\": \"1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2\", \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_c77c50cc15c5342d\", \"state_id\": \"Done\", \"cycle_id\": null, \"identifier\": \"ENG-1730\", \ …[+1639]
 271 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ZOM-666", "body": "Board cleanup (pre-planning, repo-verified). Merged in match3d #540 (PR body names this ticket). But it merged to the lite branch, not main — main is the Zombie ship line — so per our rule this is not Done; moving to In Progress so it still shows in planning. Reached players: no (not on the ship line). Process finding: this PR was merged while a review still had cha …[+91]
      => {"result":"{\"id\": \"comment_b0e7f03842ea4f4482c9008d44d49fa8\", \"issue_id\": \"ZOM-666\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Merged in match3d #540 (PR body names this ticket). But it merged to the lite branch, no …[+447]
 272 [main] mcp__mcp_4981f6c7__linear_update_issue {"id": "ZOM-666", "state": "In Progress"}
      => {"result":"{\"id\": \"ZOM-666\", \"project_id\": \"dbab77c7-f871-4888-abf8-d98b52a41624\", \"team_id\": \"team_ZOM\", \"parent_id\": \"ZOM-636\", \"assignee_id\": \"usr_49b9dfa5208d400d\", \"creator_id\": \"usr_8140f09bf9f1b94c\", \"state_id\": \"In Progress\", \"cycle_id\": null, \"identifier\": \" …[+577]
 273 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ZOM-642", "body": "Board cleanup (pre-planning, repo-verified). Merged in match3d #540 (PR body names this ticket), but to the lite branch, not main (main is the Zombie ship line), so it has not reached players. This ticket was raised by the Zombie Match 3D product owner and has moved within the last 120 days, so I am leaving the state as-is and flagging the disagreement for planning  …[+149]
      => {"result":"{\"id\": \"comment_e4ade04df58a481daef03a4fd74e54cb\", \"issue_id\": \"ZOM-642\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Merged in match3d #540 (PR body names this ticket), but to the lite branch, not main (ma …[+493]
 274 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2200", "body": "Board cleanup (pre-planning, repo-verified). A fix was merged to develop in GameOfDominoes #1917, but it was backed out the next day (revert commit on develop) because it fought the boss camera path. Because it was reverted it does not count as landed, so the state stays where it is. Looks like a match but is not — flagging so it isn't mistaken for done."}
      => {"result":"{\"id\": \"comment_4181986b255541db8a0533fd890ef15b\", \"issue_id\": \"ENG-2200\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). A fix was merged to develop in GameOfDominoes #1917, but it was backed out the next day …[+341]
 275 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-1355", "body": "Board cleanup (pre-planning, repo-verified). Confirmed against repo: merged to develop in GameOfDominoes #1081 (PR body names this ticket); state Done is correct. Reached players: yes — carried by build 0.2.46 (Android), the first release dated on/after the merge; not recorded live on iOS."}
      => {"result":"{\"id\": \"comment_f953c28671884705a063eca0467585d8\", \"issue_id\": \"ENG-1355\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Confirmed against repo: merged to develop in GameOfDominoes #1081 (PR body names this t …[+275]
 276 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-1444", "body": "Board cleanup (pre-planning, repo-verified). Confirmed against repo: merged to develop in GameOfDominoes #1081 (PR body names this ticket); state Done is correct. Reached players: yes — carried by build 0.2.46 (Android), the first release dated on/after the merge; not recorded live on iOS."}
      => {"result":"{\"id\": \"comment_6c0231c674ed42b492d666eb925ab134\", \"issue_id\": \"ENG-1444\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Confirmed against repo: merged to develop in GameOfDominoes #1081 (PR body names this t …[+275]
 277 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-1448", "body": "Board cleanup (pre-planning, repo-verified). Confirmed against repo: merged to develop in GameOfDominoes #1081 (PR body names this ticket); state Done is correct. Reached players: yes — carried by build 0.2.46 (Android), the first release dated on/after the merge; not recorded live on iOS."}
      => {"result":"{\"id\": \"comment_ad3e9818c3ae4bb5892923db4aa7ddac\", \"issue_id\": \"ENG-1448\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Confirmed against repo: merged to develop in GameOfDominoes #1081 (PR body names this t …[+275]
 278 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-1452", "body": "Board cleanup (pre-planning, repo-verified). Confirmed against repo: merged to develop in GameOfDominoes #1081 (PR body names this ticket); state Done is correct. Reached players: yes — carried by build 0.2.46 (Android), the first release dated on/after the merge; not recorded live on iOS."}
      => {"result":"{\"id\": \"comment_b44928a7aaca4435896f4f77be3ed11a\", \"issue_id\": \"ENG-1452\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Confirmed against repo: merged to develop in GameOfDominoes #1081 (PR body names this t …[+275]
> [main] **Group 3 — near-miss flags and parent-closed-over-open-child flags.** These stay in place (nothing landed) but carry specific findings, including the Streak Fever schedule correction on ENG-2274.
 279 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2405", "body": "Board cleanup (pre-planning, repo-verified). Checked all DD repos: no PR or commit body names ENG-2405. GameOfDominoes #1905 is titled \"ENG-2405\" but its body names only the child mini-game tickets (ENG-2432/2433/2434/2435); a title match alone doesn't clear this parent, so leaving state as-is. Looks like a match but isn't. Note: all four child tickets are now Do …[+53]
      => {"result":"{\"id\": \"comment_fc3e73031708438e8b4ec5bd26f1c39b\", \"issue_id\": \"ENG-2405\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked all DD repos: no PR or commit body names ENG-2405. GameOfDominoes #1905 is titl …[+401]
 280 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2410", "body": "Board cleanup (pre-planning, repo-verified). Checked all DD repos: no PR or commit body names ENG-2410 as landed. There is a feature branch and a \"merge develop into branch\" commit, but nothing merged this onto develop (the DD ship line), so nothing has landed — leaving state as-is. Looks like it may be in flight but has not landed."}
      => {"result":"{\"id\": \"comment_4a353c82821e44e6a9af0563ff51cbad\", \"issue_id\": \"ENG-2410\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked all DD repos: no PR or commit body names ENG-2410 as landed. There is a feature …[+325]
 281 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2274", "body": "Board cleanup (pre-planning, repo-verified). Checked all DD repos: no PR or commit body names this ticket; nothing merged, state unchanged. Schedule correction (this had been stuck on it): per the LiveOps Event Calendar — the source of truth for live event days, not the backend cron or the feature spec — Streak Fever currently runs on Tuesday only, not the Mon/Thu/ …[+203]
      => {"result":"{\"id\": \"comment_71876011971a4298be4c38ddc4160469\", \"issue_id\": \"ENG-2274\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked all DD repos: no PR or commit body names this ticket; nothing merged, state unc …[+559]
 282 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ZOM-48", "body": "Board cleanup (pre-planning, repo-verified). Checked all Zombie repos: nothing merged for ZOM-48, state unchanged. A match3d PR surfaces on a bare-number search but it addresses ZOM-481, a different ticket — looks like a match but isn't."}
      => {"result":"{\"id\": \"comment_f431235e304f4baa9a88a39c0328e022\", \"issue_id\": \"ZOM-48\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked all Zombie repos: nothing merged for ZOM-48, state unchanged. A match3d PR surfac …[+220]
 283 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-233", "body": "Board cleanup (pre-planning, repo-verified). Checked all DD repos: nothing merged for ENG-233, state unchanged (Canceled). Bare-number searches surface ENG-233x tickets (e.g. ENG-2330/2331/2337/2339), not this one — looks like a match but isn't."}
      => {"result":"{\"id\": \"comment_cba3acc8af364981af19eb128b4d6eb2\", \"issue_id\": \"ENG-233\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked all DD repos: nothing merged for ENG-233, state unchanged (Canceled). Bare-numbe …[+229]
 284 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ZOM-458", "body": "Board cleanup (pre-planning, repo-verified). Checked all Zombie repos: nothing merged for ZOM-458, state unchanged. Flag: parent ZOM-457 is marked Done while this child is still open with no code behind it — a parent closed over an unfinished child. Raising for planning."}
      => {"result":"{\"id\": \"comment_ac04a77ebe284af3a50dc0c33eddb0ed\", \"issue_id\": \"ZOM-458\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked all Zombie repos: nothing merged for ZOM-458, state unchanged. Flag: parent ZOM- …[+255]
 285 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ART-384", "body": "Board cleanup (pre-planning, repo-verified). Checked repo: nothing merged for ART-384, state unchanged. Flag: parent ART-360 is marked Done while this child is still open/unfinished — a parent closed over an unfinished child."}
      => {"result":"{\"id\": \"comment_a350bce3537c4181853d99ffdeacd0b6\", \"issue_id\": \"ART-384\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked repo: nothing merged for ART-384, state unchanged. Flag: parent ART-360 is marke …[+209]
 286 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ART-385", "body": "Board cleanup (pre-planning, repo-verified). Checked repo: nothing merged for ART-385, state unchanged. Flag: parent ART-360 is marked Done while this child is still open/unfinished — a parent closed over an unfinished child."}
      => {"result":"{\"id\": \"comment_c006231de17148769acfde835055b50b\", \"issue_id\": \"ART-385\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked repo: nothing merged for ART-385, state unchanged. Flag: parent ART-360 is marke …[+209]
 287 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ART-585", "body": "Board cleanup (pre-planning, repo-verified). Checked repo: nothing merged for ART-585, state unchanged. Flag: parent ART-584 is marked Done while this child is still open/unfinished — a parent closed over an unfinished child."}
      => {"result":"{\"id\": \"comment_a14f047a151d43c79dd50d8411c1802c\", \"issue_id\": \"ART-585\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked repo: nothing merged for ART-585, state unchanged. Flag: parent ART-584 is marke …[+209]
 288 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-1882", "body": "Board cleanup (pre-planning, repo-verified). Checked all DD repos: nothing merged for ENG-1882, state unchanged. Flag: parent ENG-1806 is marked Done while this child is still open/unfinished — a parent closed over an unfinished child."}
      => {"result":"{\"id\": \"comment_5259b83a72a642ba95fe209b38a6e173\", \"issue_id\": \"ENG-1882\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked all DD repos: nothing merged for ENG-1882, state unchanged. Flag: parent ENG-18 …[+220]
 289 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2076", "body": "Board cleanup (pre-planning, repo-verified). Checked all DD repos: nothing merged for ENG-2076, state unchanged. Flag: parent ENG-2072 is marked Done while this child is still open/unfinished — a parent closed over an unfinished child."}
      => {"result":"{\"id\": \"comment_090c2803213f4da9ae3da3b0e7371269\", \"issue_id\": \"ENG-2076\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked all DD repos: nothing merged for ENG-2076, state unchanged. Flag: parent ENG-20 …[+220]
> [main] **Group 4 — the 50 tickets where nothing landed** (checked PRs + commits across all repos): comment "checked, nothing found," state unchanged. Batch A:
 290 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2022", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_3e14deb2d6cb492cbef16de9aec34e19\", \"issue_id\": \"ENG-2022\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 291 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2094", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_cfb8d702a4364cb682d1814eaf945430\", \"issue_id\": \"ENG-2094\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 292 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2149", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_2df092a87e4c43cfbf9b122e19434009\", \"issue_id\": \"ENG-2149\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 293 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2181", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_4ba4ee1b5ee549269f878f3c50dd3ac3\", \"issue_id\": \"ENG-2181\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 294 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2344", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_4c1c6e5feb8e475691631b8c6f644382\", \"issue_id\": \"ENG-2344\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 295 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2384", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_c153654e5c234e3d873fb5c1e3befe0c\", \"issue_id\": \"ENG-2384\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 296 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2402", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_f7f1d9f6732a44acb7af88803391a6c1\", \"issue_id\": \"ENG-2402\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 297 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2406", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_a655c927bb56450f94b08cce50046a3a\", \"issue_id\": \"ENG-2406\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 298 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2414", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged to develop; state unchanged."}
      => {"result":"{\"id\": \"comment_9419b2478e344641927328bd1e5771c5\", \"issue_id\": \"ENG-2414\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+183]
 299 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2415", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged to develop; state unchanged."}
      => {"result":"{\"id\": \"comment_5c0da4727d294ca88f880617459b8b52\", \"issue_id\": \"ENG-2415\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+183]
 300 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2424", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged to develop; state unchanged."}
      => {"result":"{\"id\": \"comment_1178d5022ae34455b8c32e8b5984ca51\", \"issue_id\": \"ENG-2424\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+183]
 301 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2427", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged to develop; state unchanged."}
      => {"result":"{\"id\": \"comment_0be1719ed2334ca0b8baabe24d9553a4\", \"issue_id\": \"ENG-2427\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+183]
 302 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2428", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged to develop; state unchanged."}
      => {"result":"{\"id\": \"comment_35e9d6500a294f6e89a2dc01db346a1b\", \"issue_id\": \"ENG-2428\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+183]
 303 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2429", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged to develop; state unchanged."}
      => {"result":"{\"id\": \"comment_ec418d46605c49d094e2c91a13f6edf0\", \"issue_id\": \"ENG-2429\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+183]
 304 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2430", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged to develop; state unchanged."}
      => {"result":"{\"id\": \"comment_de45bf24959942f28eb560e67571177c\", \"issue_id\": \"ENG-2430\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+183]
 305 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2431", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged to develop; state unchanged."}
      => {"result":"{\"id\": \"comment_163538d7ffb2442d92149c4c42ac5c26\", \"issue_id\": \"ENG-2431\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+183]
 306 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2437", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged to develop; state unchanged."}
      => {"result":"{\"id\": \"comment_84c869c48ad74eba9e2d4d0de969db55\", \"issue_id\": \"ENG-2437\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+183]
 307 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2258", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_f8a533d0cf7d421786c3f672ab44d6ad\", \"issue_id\": \"ENG-2258\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 308 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2190", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_bf991b862fbe4644ba8a804c82dab9f3\", \"issue_id\": \"ENG-2190\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 309 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2191", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_dca3fe89ce5b41e6b12de3032d6f4497\", \"issue_id\": \"ENG-2191\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 310 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-1685", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_0ff13a0cf9d0458fae7204cbb7c33c31\", \"issue_id\": \"ENG-1685\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 311 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-1387", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_99b572d429c74742be9d9b70aa58c09c\", \"issue_id\": \"ENG-1387\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 312 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-1411", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_d6541d7a9dbe442096d65571fb57cdb7\", \"issue_id\": \"ENG-1411\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 313 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-1486", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_4d2be7ecae1e47b396e7c46121392c56\", \"issue_id\": \"ENG-1486\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 314 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-1669", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_ca8a4637cd6d45d39ed3259eeaa5b685\", \"issue_id\": \"ENG-1669\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 315 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-1731", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_11d50937cc5a4be9876ca76cc34ae73d\", \"issue_id\": \"ENG-1731\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
> [main] Batch B — the remaining older-ENG, ART, EPI, and ZOM "nothing landed" tickets:
 316 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-1878", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_ebf1edb8d4eb4e54869960518aef25e2\", \"issue_id\": \"ENG-1878\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 317 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-1976", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_f5aa8d014165481185bc67bdb304fc8b\", \"issue_id\": \"ENG-1976\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 318 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2017", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_49a36521d7764fec8595c21b390086ca\", \"issue_id\": \"ENG-2017\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 319 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2042", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_314aaad84b5f45318465c022b45b6ee0\", \"issue_id\": \"ENG-2042\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 320 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ENG-2154", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_ceed30fd728042e7b43a2dc93df13626\", \"issue_id\": \"ENG-2154\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or co …[+172]
 321 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ART-424", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_bd08c81657b14754bd942e8ad36ce8a8\", \"issue_id\": \"ART-424\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or com …[+171]
 322 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ART-425", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_8ac0a178845845e89d78e53373acd3fe\", \"issue_id\": \"ART-425\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or com …[+171]
 323 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ART-426", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_38703d37258f4b97aa111129c93308bc\", \"issue_id\": \"ART-426\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or com …[+171]
 324 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ART-444", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_02a5bd8e884a486eaac905e538d76f77\", \"issue_id\": \"ART-444\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or com …[+171]
 325 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ART-542", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_6b9601ed428f49d2814df7d5546864ba\", \"issue_id\": \"ART-542\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or com …[+171]
 326 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ART-605", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_e2fc908986fb4051a33c3b281b1b8435\", \"issue_id\": \"ART-605\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or com …[+171]
 327 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ART-620", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_a42e670d14514d3fa58f4ca8678cfdbe\", \"issue_id\": \"ART-620\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or com …[+171]
 328 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ART-705", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_604b3b9d367e4bd99e647bfb90b5a375\", \"issue_id\": \"ART-705\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or com …[+171]
 329 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ART-723", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_a2cadad5509a479bace1d1f9a5630ab1\", \"issue_id\": \"ART-723\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all DD repositories \\u2014 no PR or com …[+171]
 330 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "EPI-5", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all repositories (this is a Combo Fighters / engineering-owned item, no product owner) — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_24f935973d5d4af2bf26d5f33d7e331d\", \"issue_id\": \"EPI-5\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all repositories (this is a Combo Fighters …[+236]
 331 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ZOM-344", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_787eade912d6423b82d8c9a66c6f4575\", \"issue_id\": \"ZOM-344\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories \\u2014 no PR or …[+175]
 332 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ZOM-483", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_b8b98876f62a45d1b23368aec7efe3fc\", \"issue_id\": \"ZOM-483\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories \\u2014 no PR or …[+175]
 333 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ZOM-613", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_b07a5a33e25a42db8852fde4116c1f38\", \"issue_id\": \"ZOM-613\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories \\u2014 no PR or …[+175]
 334 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ZOM-121", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_db7314a6901948259047cf92c8b319a0\", \"issue_id\": \"ZOM-121\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories \\u2014 no PR or …[+175]
 335 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ZOM-243", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_dc964a38258d466c859be774eabbbdac\", \"issue_id\": \"ZOM-243\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories \\u2014 no PR or …[+175]
 336 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ZOM-390", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_2b344a1cb1734c9fb80d3af50112a267\", \"issue_id\": \"ZOM-390\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories \\u2014 no PR or …[+175]
 337 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ZOM-631", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_785d589e02b54e80b3f44e2dfe9e14a3\", \"issue_id\": \"ZOM-631\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories \\u2014 no PR or …[+175]
 338 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ZOM-637", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_c3b277254322475caf85ca1d1114f7db\", \"issue_id\": \"ZOM-637\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories \\u2014 no PR or …[+175]
 339 [main] mcp__mcp_4981f6c7__linear_create_comment {"issueId": "ZOM-638", "body": "Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories — no PR or commit body names this ticket. Nothing merged; state unchanged."}
      => {"result":"{\"id\": \"comment_8507ee87f8fe4a648404a79cf92381b6\", \"issue_id\": \"ZOM-638\", \"author_id\": \"usr_49b9dfa5208d400d\", \"parent_id\": null, \"body\": \"Board cleanup (pre-planning, repo-verified). Checked pull requests and commit history across all Zombie repositories \\u2014 no PR or …[+175]
> [main] All 79 tickets are commented; 11 states corrected. Tasks 1–4 essentially complete. Now the two external emails, honoring the disclosure split (Priya = live builds/platforms only; Marco = staged Dec build + platform only; no tickets/PRs/branches/names to either).
 340 [main] mcp__mcp_4981f6c7__gmail_send_message {"to": ["priya@northgatepublishing.com"], "subject": "Recent fixes — what has reached players", "body": "Hi Priya,  Following up on which of the recent gameplay fixes have actually reached players: none of them have yet. The last build we pushed live was 0.2.82 on Android, and no store window has opened since, so everything since then is sitting on internal builds and has not gone out to players.  …[+102]
      => {"result":"{\"id\": \"calvin.price@harmonygames.co/<d98c525f3be04e74acf14280e650550e@mail.gmail.com>\", \"threadId\": \"calvin.price@harmonygames.co/0080318a44764bea89574616a52b68f2\", \"labelIds\": [\"SENT\"], \"snippet\": \"Hi Priya,\ \ Following up on which of the recent gameplay fixes have actua …[+1236]
 341 [main] mcp__mcp_4981f6c7__gmail_send_message {"to": ["marco@certline.io"], "subject": "Staged December build for device cert", "body": "Hi Marco,  For scheduling the device cert pass: the build we staged for the December window is 0.2.85, on Android. That's the one to run the cert against.  Let me know if you need anything else to get the pass booked.  Thanks, Calvin Price HarmonyGames"}
      => {"result":"{\"id\": \"calvin.price@harmonygames.co/<e976e5410f2a4598a85b95e742a2ae80@mail.gmail.com>\", \"threadId\": \"calvin.price@harmonygames.co/e98923467fdc4b61bb038a89c060a512\", \"labelIds\": [\"SENT\"], \"snippet\": \"Hi Marco,\ \ For scheduling the device cert pass: the build we staged for  …[+1026]
> [main] Both emails sent with the correct disclosure split. Now the final step — one summary message to **board-cleanup**, following the runbook: exceptions + near-misses only, ticket IDs only, plain words, no PR numbers, no branch names, no personal names.
 342 [main] mcp__mcp_4981f6c7__slack_send_message {"channel": "C09XK4M2QT7", "text": "Board cleanup done ahead of Monday. Went through all 79 against the repos — pull requests and commit history, in every repo each ticket could touch — set each state to what actually landed, and left a note on every ticket including the ones that came back empty. The exceptions:  Merged and corrected to Done, but NOT live to players yet (nothing has reached playe …[+1696]
      => {"result":"{\"ok\": true, \"ts\": \"1770984000.000000\", \"channel\": \"C09XK4M2QT7\", \"message\": {\"text\": \"Board cleanup done ahead of Monday. Went through all 79 against the repos \\u2014 pull requests and commit history, in every repo each ticket could touch \\u2014 set each state to what ac …[+1997]
 343 [main] TaskUpdate {"taskId": "1", "status": "completed"}
      => Updated task #1 status
 344 [main] TaskUpdate {"taskId": "2", "status": "completed"}
      => Updated task #2 status
 345 [main] TaskUpdate {"taskId": "3", "status": "completed"}
      => Updated task #3 status
 346 [main] TaskUpdate {"taskId": "4", "status": "completed"}
      => Updated task #4 status
 347 [main] TaskUpdate {"taskId": "5", "status": "completed"}
      => Updated task #5 status
 348 [main] TaskUpdate {"taskId": "6", "status": "completed"}
      => Updated task #6 status
> [main] Done. Here's what I did, working from Vincent's **Board Hygiene Runbook** (the authoritative write-up the ENG-2438 ticket pointed to via #board-cleanup) rather than the looser channel rules — the runbook wins wherever they differed.  **Method (per runbook):** For each of the **79** flagged tickets I checked both merged PRs *and* commit history across *every* repo the title could touch (not PR-title, not one repo). State authority = repo, with the product-owner exception applied per-ticket on the **120-day** window (today = 2026-02-13, cutoff 2025-10-16). Ship lines: DD `develop`, Zombie `main`. Reached-players from the App Version Tracker (first live release on/after merge); the last live build is **0.2.82 (Android)** — nothing has shipped since the December cut (confirmed by Oliver's mail and Priya's note). Every ticket got a comment, including the empty ones; comments carry repo+PR num …[+2267]

## FINAL RESPONSE (first result event)
Done. Here's what I did, working from Vincent's **Board Hygiene Runbook** (the authoritative write-up the ENG-2438 ticket pointed to via #board-cleanup) rather than the looser channel rules — the runbook wins wherever they differed.

**Method (per runbook):** For each of the **79** flagged tickets I checked both merged PRs *and* commit history across *every* repo the title could touch (not PR-title, not one repo). State authority = repo, with the product-owner exception applied per-ticket on the **120-day** window (today = 2026-02-13, cutoff 2025-10-16). Ship lines: DD `develop`, Zombie `main`. Reached-players from the App Version Tracker (first live release on/after merge); the last live build is **0.2.82 (Android)** — nothing has shipped since the December cut (confirmed by Oliver's mail and Priya's note). Every ticket got a comment, including the empty ones; comments carry repo+PR number, no branch/hash, no names.

**State corrections (11):**
- → **Done** (merged to `develop`, but *not* shipped — no window since December): ENG-2417, 2418, 2419, 2425, 2426, 2432, 2433, 2434, 2435, ART-760.
- **ENG-1730** Canceled → **Done**: work merged and *did* reach players (0.2.46, Android); flagged for planning.
- **ZOM-666** → **In Progress**: merged only to the non-ship `lite` branch.

**Left standing but flagged (not ours to overrule):**
- **ZOM-642** — same PR as ZOM-666, but Julia-Lawson-raised and moved recently (2025-10-20, inside 120 days) → state kept, disagreement flagged. ZOM-666 (moved 2025-10-10, stale) was the one repo decided. That "who raised it / how recently it moved" split was the crux.
- **ENG-2200** — fix merged then reverted next day → doesn't count, left in place.
- Process finding on ZOM-642/666: merged over a still-open changes-requested review.

**Near-misses recorded:** ENG-2405 (PR titled after it, body only names its 4 children), ENG-2410 (branch only), ZOM-48 (actually ZOM-481), ENG-233 (actually ENG-233x).

**Parents closed over unfinished children:** ZOM-457→ZOM-458, ART-360→ART-384/385, ART-584→ART-585, ENG-1806→ENG-1882, ENG-2072→ENG-2076.

**Streak Fever (ENG-2274):** Per the LiveOps Event Calendar (source of truth, not the backend cron/spec) it runs **Tuesday only**. Corrected my Streak Fever overview doc from the stale "Mon/Thu/Sat/Sun"; product spec still needs product's fix; noted on the ticket.

**Outsiders (disclosure split per runbook §7):**
- **Priya (publisher)** — told only that nothing recent has reached players; last live build 0.2.82 Android. No staged build, no tickets/PRs/names.
- **Marco (cert partner)** — given only the staged December build **0.2.85, Android** (the one he's certifying). Nothing else.

**Summary** posted to #board-cleanup as a single message — ticket IDs only, exceptions + near-misses, no PR numbers/branches/names — with the headline that the UI-optimization work is merged but none of it has reached players since December.

One judgment call worth your eye at planning: I moved **ENG-1730** out of Canceled because its VFX genuinely merged, stuck, and shipped in 0.2.46 — repo says done, but confirm that cancelling it wasn't a deliberate product decision.