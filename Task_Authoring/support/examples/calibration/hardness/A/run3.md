# Ledger: NF1 (V1 QC non-fail task 1) · trajectory-run-3 (1).json
model(init)=claude-opus-4-8 assistant-models={'claude-opus-4-8': 119}
tool_calls=84 errored_results=3 turns=85 duration_ms=659009 result_subtype=success is_error=False
subagents=0 subagent_models=[] post_final_result_events=0 compaction=no
tool counts: mcp__mcp_43c92cc9__github_get_pull_request_reviews=31, mcp__mcp_43c92cc9__github_get_pull_request_comments=9, mcp__mcp_43c92cc9__github_get_file_contents=8, mcp__mcp_43c92cc9__github_get_user=5, mcp__mcp_43c92cc9__github_get_issue_comments=4, mcp__mcp_43c92cc9__github_add_issue_comment=4, mcp__mcp_43c92cc9__linear_create_issue=3, mcp__mcp_43c92cc9__slack_search_channels=2, mcp__mcp_43c92cc9__github_search_repositories=2, mcp__mcp_43c92cc9__gdocs_search_documents=2, mcp__mcp_43c92cc9__gdrive_search=2, mcp__mcp_43c92cc9__github_add_reply_to_pull_request_comment=2, mcp__mcp_43c92cc9__slack_read_channel=1, mcp__mcp_43c92cc9__slack_read_user_profile=1, mcp__mcp_43c92cc9__github_list_pull_requests=1, Bash=1, mcp__mcp_43c92cc9__gdrive_read_file=1, mcp__mcp_43c92cc9__gdrive_list_sheets=1, mcp__mcp_43c92cc9__gdrive_read_sheet_range=1, mcp__mcp_43c92cc9__linear_list_teams=1, mcp__mcp_43c92cc9__linear_get_user=1, mcp__mcp_43c92cc9__slack_send_message=1

> [main] I'll start by finding the prototype channel and reading Arthur's message.
   1 [main] mcp__mcp_43c92cc9__slack_search_channels {"query": "prototype"}
      => {"result":"{\"ok\": true, \"channels\": [{\"id\": \"C072LATR10Q\", \"name\": \"tile_dozer_prototype\", \"is_channel\": true, \"is_private\": true, \"is_im\": false, \"is_mpim\": false, \"is_archived\": true, \"is_general\": false, \"num_members\": 23, \"created\": 1714756844, \"creator\": \"U04TWDMD …[+534]
   2 [main] mcp__mcp_43c92cc9__slack_search_channels {"query": "combo fighter"}
      => {"result":"{\"ok\": true, \"channels\": []}"}
> [main] The `prototype` channel (C09UHHN6PFZ) is the active one. Let me read it.
   3 [main] mcp__mcp_43c92cc9__slack_read_channel {"channel": "C09UHHN6PFZ", "limit": 30}
      => {"result":"{\"ok\": true, \"messages\": [{\"ts\": \"1772210520.000000\", \"type\": \"message\", \"text\": \"and don't just take the review status at face value. go look at what actually landed on the branch after the reviewer complained. if the code got fixed anyway then the ticket should say so, an …[+14490]
> [main] Now let me find the Combo Fighter repo and identify the people involved.
   4 [main] mcp__mcp_43c92cc9__github_search_repositories {"query": "combo fighter"}
      => {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"items\": []}"}
   5 [main] mcp__mcp_43c92cc9__github_search_repositories {"query": "combo"}
      => {"result":"{\"total_count\": 1, \"incomplete_results\": false, \"items\": [{\"id\": \"harmonygames-Games/Combo-Fighters\", \"name\": \"Combo-Fighters\", \"full_name\": \"harmonygames-Games/Combo-Fighters\", \"owner\": {\"login\": \"harmonygames-Games\", \"type\": \"Organization\"}, \"private\": true …[+353]
   6 [main] mcp__mcp_43c92cc9__slack_read_user_profile {"user": "EMPLOYEE_0025_SLACK_ID"}
      => {"result":"{\"ok\": true, \"user\": {\"id\": \"EMPLOYEE_0025_SLACK_ID\", \"name\": \"Arthur Blake\", \"real_name\": \"Arthur Blake\", \"display_name\": \"Arthur Blake\", \"profile\": {\"email\": \"arthur.blake@harmonygames.co\", \"image_72\": null, \"display_name\": \"Arthur Blake\", \"real_name\":  …[+114]
> [main] Repo confirmed: `harmonygames-Games/Combo-Fighters`, Arthur Blake = EMPLOYEE_0025. Let me pull all PRs.
   7 [main] mcp__mcp_43c92cc9__github_list_pull_requests {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "state": "all", "perPage": 100}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#37\", \"number\": 37, \"title\": \"Combo Definition Updates\", \"state\": \"closed\", \"merged\": true, \"draft\": false, \"locked\": false, \"user\": {\"login\": \"PERSON_5877_GITHUB_USERNAME\"}, \"merged_by\": {\"login\": \"EMPLOYEE_0003_GIT …[+48251]
> [main] This is a large PR history. Let me pull reviews and comments for the substantive merged PRs to find review pushback. I'll batch the reviews first.
   8 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 37}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#37#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0003_GITHUB_USERNAME\"}, \"state\": \"CHANGES_REQUESTED\", \"body\": \"\", \"submitted_at\": \"2026-02-12T14:24:40Z\"}, {\"id\": \"harmonygames-Games/Combo-Fighters#37#rev_2\", \"user\": {\"login\": …[+523]
   9 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 36}
      => {"result":"[]"}
  10 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 34}
      => {"result":"[]"}
  11 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 33}
      => {"result":"[]"}
  12 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 28}
      => {"result":"[]"}
  13 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 27}
      => {"result":"[]"}
  14 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 26}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#26#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0003_GITHUB_USERNAME\"}, \"state\": \"CHANGES_REQUESTED\", \"body\": \"I think we should try a solution that uses time. If the player watches an ad to level up one of the attributes, he has to wait  …[+877]
  15 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 24}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#24#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0003_GITHUB_USERNAME\"}, \"state\": \"CHANGES_REQUESTED\", \"body\": \"\", \"submitted_at\": \"2026-01-13T18:58:07Z\"}, {\"id\": \"harmonygames-Games/Combo-Fighters#24#rev_2\", \"user\": {\"login\": …[+734]
  16 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 21}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#21#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0003_GITHUB_USERNAME\"}, \"state\": \"APPROVED\", \"body\": \"\", \"submitted_at\": \"2026-01-02T09:49:12Z\"}]"}
  17 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 8}
      => {"result":"[]"}
  18 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 3}
      => {"result":"[]"}
  19 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 23}
      => {"result":"[]"}
> [main] PRs #37 and #26 merged with CHANGES_REQUESTED and no later approval. #24 and #21 were approved before merge. Let me get the inline comments and issue comments for the candidates and the other substantive PRs to catch informal pushback and see what was actually asked.
  20 [main] mcp__mcp_43c92cc9__github_get_pull_request_comments {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 37}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#37#rc_1\", \"user\": {\"login\": \"EMPLOYEE_0003_GITHUB_USERNAME\"}, \"body\": \"The scriptable object can't store if it is locked, this shouldn't exist here as a field.\ \ What you can do instead is something like this:\ \ `public bool IsAvai …[+8426]
  21 [main] mcp__mcp_43c92cc9__github_get_issue_comments {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "issue_number": 37}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#37#c_1\", \"user\": {\"login\": \"PERSON_6026_GITHUB_USERNAME\"}, \"body\": \"<!-- This is an auto-generated comment: summarize by coderabbit.ai -->\ <!-- walkthrough_start -->\ \ <details>\ <summary>\\ud83d\\udcdd Walkthrough</summary>\ \ ##  …[+14818]
  22 [main] mcp__mcp_43c92cc9__github_get_pull_request_comments {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 26}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#26#rc_1\", \"user\": {\"login\": \"EMPLOYEE_0003_GITHUB_USERNAME\"}, \"body\": \"We should probably move both of this Memory lines to WinScreen\", \"path\": \"Assets/Scripts/Managers/GameController.cs\", \"diff_hunk\": \"@@ -174,6 +174,7 @@ pr …[+7202]
  23 [main] mcp__mcp_43c92cc9__github_get_issue_comments {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "issue_number": 26}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#26#c_1\", \"user\": {\"login\": \"PERSON_6026_GITHUB_USERNAME\"}, \"body\": \"<!-- This is an auto-generated comment: summarize by coderabbit.ai -->\ <!-- walkthrough_start -->\ \ <details>\ <summary>\\ud83d\\udcdd Walkthrough</summary>\ \ ##  …[+7318]
  24 [main] mcp__mcp_43c92cc9__github_get_pull_request_comments {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 24}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#24#rc_1\", \"user\": {\"login\": \"EMPLOYEE_0003_GITHUB_USERNAME\"}, \"body\": \"Slot is never null, unless it receives a wierd index, which would cause an Index Out Of Range Exception. I guess this check isn't needed.\", \"path\": \"Assets/Sc …[+13074]
  25 [main] mcp__mcp_43c92cc9__github_get_pull_request_comments {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 36}
      => {"result":"[]"}
  26 [main] mcp__mcp_43c92cc9__github_get_issue_comments {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "issue_number": 36}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#36#c_1\", \"user\": {\"login\": \"PERSON_6026_GITHUB_USERNAME\"}, \"body\": \"<!-- This is an auto-generated comment: summarize by coderabbit.ai -->\ <!-- This is an auto-generated comment: skip review by coderabbit.ai -->\ \ > [!IMPORTANT]\ > …[+1775]
  27 [main] mcp__mcp_43c92cc9__github_get_pull_request_comments {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 33}
      => {"result":"[]"}
  28 [main] mcp__mcp_43c92cc9__github_get_pull_request_comments {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 28}
      => {"result":"[]"}
  29 [main] mcp__mcp_43c92cc9__github_get_pull_request_comments {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 34}
      => {"result":"[]"}
  30 [main] mcp__mcp_43c92cc9__github_get_issue_comments {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "issue_number": 34}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#34#c_1\", \"user\": {\"login\": \"PERSON_6026_GITHUB_USERNAME\"}, \"body\": \"<!-- This is an auto-generated comment: summarize by coderabbit.ai -->\ <!-- walkthrough_start -->\ \ <details>\ <summary>\\ud83d\\udcdd Walkthrough</summary>\ \ ##  …[+36010]
  31 [main] mcp__mcp_43c92cc9__github_get_pull_request_comments {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 3}
      => {"result":"[]"}
> [main] Let me verify the remaining merged PRs for any other CHANGES_REQUESTED, and map the GitHub identities.
  32 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 35}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#35#rev_1\", \"user\": {\"login\": \"PERSON_6026_GITHUB_USERNAME\"}, \"state\": \"COMMENTED\", \"body\": \"**Actionable comments posted: 7**\ \ <details>\ <summary>\\ud83e\\udd16 Fix all issues with AI agents</summary>\ \ ```\ In `@Assets/Art/T …[+22665]
  33 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 18}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#18#rev_1\", \"user\": {\"login\": \"PERSON_6026_GITHUB_USERNAME\"}, \"state\": \"COMMENTED\", \"body\": \"**Actionable comments posted: 1**\ \ <details>\ <summary>\\ud83d\\udcdc Review details</summary>\ \ **Configuration used**: defaults\ \ * …[+748]
  34 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 17}
      => {"result":"[]"}
  35 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 16}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#16#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0003_GITHUB_USERNAME\"}, \"state\": \"APPROVED\", \"body\": \"\", \"submitted_at\": \"2025-12-21T04:07:29Z\"}]"}
  36 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 15}
      => {"result":"[]"}
  37 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 14}
      => {"result":"[]"}
  38 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 9}
      => {"result":"[{\"id\": \"harmonygames-Games/Combo-Fighters#9#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0003_GITHUB_USERNAME\"}, \"state\": \"APPROVED\", \"body\": \"\", \"submitted_at\": \"2025-12-12T15:48:18Z\"}]"}
  39 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 31}
      => {"result":"[]"}
  40 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 13}
      => {"result":"[]"}
  41 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 6}
      => {"result":"[]"}
  42 [main] mcp__mcp_43c92cc9__github_get_user {"username": "EMPLOYEE_0003_GITHUB_USERNAME"}
      => {"result":"{\"login\": \"EMPLOYEE_0003_GITHUB_USERNAME\", \"id\": \"EMPLOYEE_0003_GITHUB_ID\", \"node_id\": \"EMPLOYEE_0003_GITHUB_NODE_ID\", \"type\": \"User\", \"site_admin\": false, \"name\": \"Oliver Brooks\", \"email\": \"oliver.brooks@harmonygames.co\", \"public_repos\": 0, \"public_gists\": 0 …[+123]
  43 [main] mcp__mcp_43c92cc9__github_get_user {"username": "PERSON_5877_GITHUB_USERNAME"}
      => {"result":"{\"login\": \"PERSON_5877_GITHUB_USERNAME\", \"id\": \"PERSON_5877_GITHUB_ID\", \"node_id\": \"PERSON_5877_GITHUB_NODE_ID\", \"type\": \"User\", \"site_admin\": false, \"name\": \"PERSON_5877_NAME\", \"email\": \"PERSON_5877_EMAIL\", \"public_repos\": 0, \"public_gists\": 0, \"followers\" …[+108]
  44 [main] mcp__mcp_43c92cc9__github_get_user {"username": "EMPLOYEE_0016_GITHUB_USERNAME"}
      => {"result":"{\"login\": \"EMPLOYEE_0016_GITHUB_USERNAME\", \"id\": \"EMPLOYEE_0016_GITHUB_ID\", \"node_id\": \"EMPLOYEE_0016_GITHUB_NODE_ID\", \"type\": \"User\", \"site_admin\": false, \"name\": \"Robert\", \"email\": \"robert@harmonygames.co\", \"public_repos\": 0, \"public_gists\": 0, \"followers\ …[+109]
  45 [main] mcp__mcp_43c92cc9__github_get_user {"username": "EMPLOYEE_0025_GITHUB_USERNAME"}
      => {"result":"{\"login\": \"EMPLOYEE_0025_GITHUB_USERNAME\", \"id\": \"EMPLOYEE_0025_GITHUB_ID\", \"node_id\": \"EMPLOYEE_0025_GITHUB_NODE_ID\", \"type\": \"User\", \"site_admin\": false, \"name\": \"Arthur Blake\", \"email\": \"arthur.blake@harmonygames.co\", \"public_repos\": 0, \"public_gists\": 0,  …[+121]
  46 [main] mcp__mcp_43c92cc9__github_get_user {"username": "PERSON_0396_GITHUB_USERNAME"}
      => {"result":"{\"login\": \"PERSON_0396_GITHUB_USERNAME\", \"id\": \"PERSON_0396_GITHUB_ID\", \"node_id\": \"PERSON_0396_GITHUB_NODE_ID\", \"type\": \"User\", \"site_admin\": false, \"name\": \"Marcus\", \"public_repos\": 0, \"public_gists\": 0, \"followers\": 0, \"following\": 1, \"created_at\": \"202 …[+64]
> [main] Oliver Brooks (EMPLOYEE_0003) is the lead reviewer; Arthur Blake (EMPLOYEE_0025) is the founder. I found three PRs merged over a standing `CHANGES_REQUESTED`: **#37**, **#26**, and **#35** (Arthur's own backend PR). Let me get #35's inline comments, verify what actually landed in the code, and locate the combo design spec.
  47 [main] mcp__mcp_43c92cc9__github_get_pull_request_comments {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 35}
      => Error: result (248,693 characters) exceeds maximum allowed tokens. Output has been saved to /root/.claude/projects/-app/ea74f797-0e04-4d20-937b-f9c2c40a916a/tool-results/mcp-mcp_43c92cc9-github_get_pull_request_comments-1785675884945.txt. Format: JSON with schema: {result: string} Use offset and lim …[+1015]
  48 [main] mcp__mcp_43c92cc9__github_get_file_contents {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "path": "Assets/Scripts/ScriptableObjects/ComboDefinition.cs", "ref": "bf4e630b9afd8147c7c86a6953a6a9e50cc3cf64"}
      => {"result":"{\"type\": \"file\", \"encoding\": \"base64\", \"name\": \"ComboDefinition.cs\", \"path\": \"Assets/Scripts/ScriptableObjects/ComboDefinition.cs\", \"size\": 5207, \"content\": \"dXNpbmcgU3lzdGVtOwp1c2luZyBTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYzsKdXNpbmcgU3lzdGVtLkdsb2JhbGl6YXRpb247CnVzaW5nIF …[+6839]
  49 [main] mcp__mcp_43c92cc9__github_get_file_contents {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "path": "Assets/Scripts/UI/ComboScreen.cs", "ref": "bf4e630b9afd8147c7c86a6953a6a9e50cc3cf64"}
      => {"result":"{\"type\": \"file\", \"encoding\": \"base64\", \"name\": \"ComboScreen.cs\", \"path\": \"Assets/Scripts/UI/ComboScreen.cs\", \"size\": 5487, \"content\": \"dXNpbmcgU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWM7CnVzaW5nIFN5c3RlbS5MaW5xOwp1c2luZyBOYXVnaHR5QXR0cmlidXRlczsKdXNpbmcgVW5pdHlFbmdpbmU7Cgpwd …[+7188]
  50 [main] mcp__mcp_43c92cc9__gdocs_search_documents {"fullText": "combo rarity"}
      => {"result":"{\"documents\": [], \"totalResults\": 0, \"nextPageToken\": null}"}
  51 [main] mcp__mcp_43c92cc9__gdrive_search {"query": "combo"}
      => {"result":"{\"files\": [{\"id\": \"f_e782531004d48b81f91e97\", \"name\": \"Combo Fighter Design Details.xlsx\", \"mimeType\": \"application/vnd.google-apps.spreadsheet\", \"parents\": [\"d_9f7ba94f7526d54d8482ba\"], \"owners\": [{\"emailAddress\": \"robert@harmonygames.co\", \"displayName\": \"rober …[+5559]
> [main] Critical finding on **#37**: the final merged `ComboDefinition.cs` shows Oliver's requested changes *were actually applied* — enum renamed to `ERarityEnum`, the `Locked` field removed and replaced with a computed `IsLocked => !ComboManager.Instance.IsComboUnlocked(Id)`, and `LevelMultiplierRow` gone. So the code got fixed even though no formal approval was ever recorded. Notably, the enum shipped as **4 tiers (Rare, Epic, Legendary, Mythic)** — `Common` was removed before merge.  Let me pull Oliver's actual review comments on #35, read the combo design docs, and verify #26's shipped code.
  52 [main] Bash {"command": "cd /root/.claude/projects/-app/ea74f797-0e04-4d20-937b-f9c2c40a916a/tool-results && python3 -c \" import json d=json.load(open('mcp-mcp_43c92cc9-github_get_pull_request_comments-1785675884945.txt')) import re arr=json.loads(d['result']) print('total comments:', len(arr)) for c in arr:     u=c.get('user',{}).get('login','')     if 'EMPLOYEE_0003' in u or 'EMPLOYEE_0025' in u or 'PERSON …[+176]
      => total comments: 27 ---- EMPLOYEE_0003_GITHUB_USERNAME Assets/Store/DominoPlayerPrefs.cs 2026-01-30T20:36:31Z Can we rename this to something else? ---- EMPLOYEE_0025_GITHUB_USERNAME Assets/Store/DominoPlayerPrefs.cs 2026-01-30T21:27:16Z Yes ---- EMPLOYEE_0003_GITHUB_USERNAME Assets/Scripts/UI/Profil …[+627]
  53 [main] mcp__mcp_43c92cc9__gdrive_read_file {"fileId": "f_8fb667cfb8d1e8dcc7a182"}
      => {"result":"{\"mimeType\": \"text/markdown\", \"text\": \"Overview\ \ ### 1. Game Overview\ Title: Combo Fighter\ Genre: Merge puzzle auto battler\ Platform: (iOS / Android)\ Core Loop Summary:\ Place fight-action tetris shaped pieces on a game board and watch the character fight hordes of enemies.\  …[+15482]
  54 [main] mcp__mcp_43c92cc9__gdrive_list_sheets {"spreadsheetId": "f_e782531004d48b81f91e97"}
      => {"result":"{\"sheets\": [{\"sheetId\": \"0\", \"title\": \"Combo Sheet\", \"index\": 0, \"gridProperties\": {\"rowCount\": 992, \"columnCount\": 16}}, {\"sheetId\": \"1\", \"title\": \"LevelObstacles\", \"index\": 1, \"gridProperties\": {\"rowCount\": 1000, \"columnCount\": 6}}, {\"sheetId\": \"2\", …[+2176]
  55 [main] mcp__mcp_43c92cc9__github_get_file_contents {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "path": "Assets/Scripts/Managers/GameController.cs", "ref": "9ecdc51faca08f3ebb237b63b5dbd792b4ea3bdd"}
      => {"result":"{\"type\": \"file\", \"encoding\": \"base64\", \"name\": \"GameController.cs\", \"path\": \"Assets/Scripts/Managers/GameController.cs\", \"size\": 8966, \"content\": \"dXNpbmcgU3lzdGVtLkNvbGxlY3Rpb25zOwp1c2luZyBTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYzsKdXNpbmcgQVllbGxvd3BhcGVyLlNlcmlhbGl6ZWRDb …[+11840]
> [main] Verified **#26**: the shipped `GameController.cs` still resets the ad cooldown on level finish (and `LoseScreen` on loss), so the exact exploit Oliver flagged — lose fast, return to menu, watch another ad — is live in production. Oliver's "move to WinScreen" suggestion also never landed.  Now verifying #35's fate and sweeping the remaining merged PRs for any missed objections.
  56 [main] mcp__mcp_43c92cc9__github_get_file_contents {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "path": "Assets/Store/DominoPlayerPrefs.cs", "ref": "f065d1ca18ef1bf25040aaafcd0be80915b56cf5"}
      => {"result":"{\"message\": \"Not Found\", \"documentation_url\": \"https://docs.github.com/rest\"}"}
  57 [main] mcp__mcp_43c92cc9__github_get_file_contents {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "path": "Assets/AWSGameSDK/AWSGameSDKClient.cs", "ref": "f065d1ca18ef1bf25040aaafcd0be80915b56cf5"}
      => {"result":"{\"type\": \"file\", \"encoding\": \"base64\", \"name\": \"AWSGameSDKClient.cs\", \"path\": \"Assets/AWSGameSDK/AWSGameSDKClient.cs\", \"size\": 25124, \"content\": \"Ly8gQ29weXJpZ2h0IEFtYXpvbi5jb20sIEluYy4gb3IgaXRzIGFmZmlsaWF0ZXMuIEFsbCBSaWdodHMgUmVzZXJ2ZWQuCi8vIFNQRFgtTGljZW5zZS1JZGVudG …[+33383]
  58 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 25}
      => {"result":"[]"}
  59 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 29}
      => {"result":"[]"}
  60 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 30}
      => {"result":"[]"}
  61 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 12}
      => {"result":"[]"}
  62 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 11}
      => {"result":"[]"}
  63 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 7}
      => {"result":"[]"}
  64 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 5}
      => {"result":"[]"}
  65 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 4}
      => {"result":"[]"}
  66 [main] mcp__mcp_43c92cc9__github_get_pull_request_reviews {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 2}
      => {"result":"[]"}
> [main] Sweep confirms **#37, #26, #35 are the only three PRs merged over a standing `CHANGES_REQUESTED`**. Key #35 verification: the shipped `AWSGameSDKClient.cs` *did* adopt some CodeRabbit fixes (login GET now URL-encodes via `Uri.EscapeDataString`, JSON escaping added) — but the **auth/refresh token still gets written to logs** in the error paths (`Debug.LogError(...RawResponse:{rawResponse})`), and `GetUserCountry()` still has no guard. So security concerns partially shipped unaddressed.  Now let me settle whether #35/#37 are actually in the live `main` build, and check the combo design spec for Owen's question.
  67 [main] mcp__mcp_43c92cc9__github_get_file_contents {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "path": "Assets/Scripts/ScriptableObjects/ComboDefinition.cs", "ref": "main"}
      => {"result":"{\"type\": \"file\", \"encoding\": \"base64\", \"name\": \"ComboDefinition.cs\", \"path\": \"Assets/Scripts/ScriptableObjects/ComboDefinition.cs\", \"size\": 5207, \"content\": \"dXNpbmcgU3lzdGVtOwp1c2luZyBTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYzsKdXNpbmcgU3lzdGVtLkdsb2JhbGl6YXRpb247CnVzaW5nIF …[+6839]
  68 [main] mcp__mcp_43c92cc9__github_get_file_contents {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "path": "Assets/AWSGameSDK/AWSGameSDKClient.cs", "ref": "main"}
      => {"result":"{\"type\": \"file\", \"encoding\": \"base64\", \"name\": \"AWSGameSDKClient.cs\", \"path\": \"Assets/AWSGameSDK/AWSGameSDKClient.cs\", \"size\": 25124, \"content\": \"Ly8gQ29weXJpZ2h0IEFtYXpvbi5jb20sIEluYy4gb3IgaXRzIGFmZmlsaWF0ZXMuIEFsbCBSaWdodHMgUmVzZXJ2ZWQuCi8vIFNQRFgtTGljZW5zZS1JZGVudG …[+33383]
  69 [main] mcp__mcp_43c92cc9__github_get_file_contents {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "path": "Assets/Scripts/Ads/UI/MainMenuAdsController.cs", "ref": "main"}
      => {"result":"{\"type\": \"file\", \"encoding\": \"base64\", \"name\": \"MainMenuAdsController.cs\", \"path\": \"Assets/Scripts/Ads/UI/MainMenuAdsController.cs\", \"size\": 10714, \"content\": \"dXNpbmcgQmFja2VuZC5BUElzOwp1c2luZyBTeXN0ZW07CnVzaW5nIFVuaXR5RW5naW5lOwp1c2luZyBVbml0eUVuZ2luZS5VSTsKCnB1Ymxp …[+14185]
  70 [main] mcp__mcp_43c92cc9__gdrive_read_sheet_range {"spreadsheetId": "f_e782531004d48b81f91e97", "sheetIndex": 10}
      => {"result":"{\"spreadsheetId\": \"f_e782531004d48b81f91e97\", \"sheetIndex\": 10, \"mimeType\": \"text/csv\", \"text\": \"Trigger Name,Combo,Combo Name,Combo Bonus Dmg Multiplier,Made?,In-Game Tested DPS,Pieces,DPS/Piece,Base DPS Damage,1/20/2026 Multiplier,New DPS,,Combo Hits,Avg DPS,Index to 2 Hit  …[+24535]
  71 [main] mcp__mcp_43c92cc9__gdocs_search_documents {"fullText": "unlock"}
      => {"result":"{\"documents\": [{\"documentId\": \"f_3f0cc30eb0c9dace70301c\", \"title\": \"Lucky Adventurer Thoughts\", \"revisionId\": \"3f0cc30eb0\", \"owners\": [\"robert@harmonygames.co\"], \"modifiedTime\": \"2025-11-05T22:42:40Z\", \"createdTime\": \"2025-11-05T22:33:35Z\", \"driveFileId\": \"f_3 …[+1278]
  72 [main] mcp__mcp_43c92cc9__gdrive_search {"query": "rarity"}
      => {"result":"{\"files\": [], \"nextPageToken\": null, \"totalCount\": 0}"}
> [main] I now have everything I need. Confirmed on `main` (the live build): all three flagged PRs' code is shipped — including #35's token-logging in error paths and #26's cooldown-reset exploit.  **Design-spec finding (Owen's question):** The combo rarity/unlock/leveling system that shipped in #37 (`ERarityEnum` Rare/Epic/Legendary/Mythic, 300 unlock cost, per-rarity level bonus) is **not** documented in the GDD or the "Combo Fighter Design Details" sheet — the GDD's combo section only covers bonus-damage multipliers (matching the "Combo List" tab), with no rarity/unlock/leveling. No "Combo Unlocking Specs" / rarity doc exists in Drive or Docs. The spec cited in the #37 review only ever lived in the Slack thread and the PR comments.  Let me set up the Linear tickets. First, find the engineering board.
  73 [main] mcp__mcp_43c92cc9__linear_list_teams {}
      => {"result":"{\"teams\": [{\"id\": \"team_ART\", \"name\": \"Art\", \"key\": \"ART\", \"description\": null, \"is_archived\": false, \"created_at\": \"2026-08-02T12:59:49Z\", \"updated_at\": \"2026-08-02T12:59:49Z\"}, {\"id\": \"team_DES\", \"name\": \"Design\", \"key\": \"DES\", \"description\": null …[+733]
  74 [main] mcp__mcp_43c92cc9__linear_get_user {"query": "me"}
      => {"result":"{\"id\": \"usr_4e13bd40cc73d0fc\", \"email\": \"owen.baker@harmonygames.co\", \"name\": \"owen.baker@harmonygames.co\", \"display_name\": \"owen.baker@harmonygames.co\", \"avatar_url\": null, \"is_active\": true, \"created_at\": \"2026-08-02T12:59:49Z\", \"updated_at\": \"2026-08-02T12:59 …[+9]
> [main] Engineering board = **ENG**. Creating the three tickets (one per PR, unassigned), then I'll comment on each PR and post the Slack summary.
  75 [main] mcp__mcp_43c92cc9__linear_create_issue {"team": "Engineering", "title": "Combo-Fighters PR #35 merged over standing CHANGES_REQUESTED — auth tokens logged in prod", "priority": 2, "description": "Record of review state at the Feb-2026 freeze (Combo Fighter is live/monetizing). Recording state only — not assigning.  **PR:** harmonygames-Games/Combo-Fighters #35 \"Blake/backend\" — author Arthur Blake (@EMPLOYEE_0025), merged by the auth …[+1773]
      => {"result":"{\"id\": \"issue_1d4792d3d0434e63a69c4afd110bc7d0\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": null, \"creator_id\": null, \"state_id\": \"Todo\", \"cycle_id\": null, \"identifier\": \"ENG-2438\", \"number\": 2438, \"title\": \"Combo-Fighters P …[+2566]
  76 [main] mcp__mcp_43c92cc9__linear_create_issue {"team": "Engineering", "title": "Combo-Fighters PR #26 merged over unresolved reviewer objection — ad-cooldown bypass is live", "priority": 2, "description": "Record of review state at the Feb-2026 freeze. Recording state only — not assigning.  **PR:** harmonygames-Games/Combo-Fighters #26 \"Added cooldown to main menu upgrade ad watch\" — author @PERSON_5877, merged by Oliver Brooks. **Review:** …[+1532]
      => {"result":"{\"id\": \"issue_1448bbe40440418c81a05ed15ede610e\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": null, \"creator_id\": null, \"state_id\": \"Todo\", \"cycle_id\": null, \"identifier\": \"ENG-2439\", \"number\": 2439, \"title\": \"Combo-Fighters P …[+2274]
  77 [main] mcp__mcp_43c92cc9__linear_create_issue {"team": "Engineering", "title": "Combo-Fighters PR #37 merged without formal sign-off (changes addressed in code, never re-approved) + combo rarity spec gap", "priority": 3, "description": "Record of review state at the Feb-2026 freeze. Recording state only — not assigning.  **PR:** harmonygames-Games/Combo-Fighters #37 \"Combo Definition Updates\" — author @PERSON_5877, merged by Oliver Brooks.  …[+2421]
      => {"result":"{\"id\": \"issue_5a471d95d211426eb62510b8488fe6ef\", \"project_id\": null, \"team_id\": \"team_ENG\", \"parent_id\": null, \"assignee_id\": null, \"creator_id\": null, \"state_id\": \"Todo\", \"cycle_id\": null, \"identifier\": \"ENG-2440\", \"number\": 2440, \"title\": \"Combo-Fighters P …[+3249]
> [main] Tickets created unassigned: **ENG-2438** (#35), **ENG-2439** (#26), **ENG-2440** (#37). Now the PR comments.
  78 [main] mcp__mcp_43c92cc9__github_add_issue_comment {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "issue_number": 35, "body": "**Review-state audit — recording pre-freeze state (per Arthur, Feb 2026).**  This PR carries a standing `CHANGES_REQUESTED` from @oliver.brooks (2026-01-30 20:36) and was merged by the author ~57 min later (21:33) with **no approving review**. The objection was never signed off.  Checked against what actually la …[+1003]
      => {"result":"{\"id\": \"1000001\", \"user\": {\"login\": \"agent\"}, \"body\": \"**Review-state audit \\u2014 recording pre-freeze state (per Arthur, Feb 2026).**\ \ This PR carries a standing `CHANGES_REQUESTED` from @oliver.brooks (2026-01-30 20:36) and was merged by the author ~57 min later (21:33) …[+1252]
  79 [main] mcp__mcp_43c92cc9__github_add_issue_comment {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "issue_number": 26, "body": "**Review-state audit — recording pre-freeze state (per Arthur, Feb 2026).**  Standing `CHANGES_REQUESTED` from @oliver.brooks (2026-01-15 13:36), merged the same day (17:28) with **no approving review afterwards**.  The core objection is unresolved in shipped code. Oliver's review: *\"the player can enter the le …[+682]
      => ERR Error executing tool github_add_issue_comment: (psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "github_pr_comments_pkey" DETAIL:  Key (id)=(1000001) already exists.  [SQL: INSERT INTO github_pr_comments (id, pr_id, author_login, body, created_at, updated_at) VALUES ( …[+762]
  80 [main] mcp__mcp_43c92cc9__github_add_issue_comment {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "issue_number": 37, "body": "**Review-state audit — recording pre-freeze state (per Arthur, Feb 2026).**  This PR has a standing `CHANGES_REQUESTED` from @oliver.brooks (2026-02-12) and was merged 2026-02-13 21:59 with **no subsequent approving review**, so GitHub still shows it unresolved. But checking what actually landed on the branch/`m …[+953]
      => ERR Error executing tool github_add_issue_comment: (psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "github_pr_comments_pkey" DETAIL:  Key (id)=(1000001) already exists.  [SQL: INSERT INTO github_pr_comments (id, pr_id, author_login, body, created_at, updated_at) VALUES ( …[+764]
> [main] The #35 comment posted; #26 and #37 collided on a key because they ran in the same instant. Retrying sequentially.
  81 [main] mcp__mcp_43c92cc9__github_add_issue_comment {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "issue_number": 26, "body": "**Review-state audit — recording pre-freeze state (per Arthur, Feb 2026).**  Standing `CHANGES_REQUESTED` from @oliver.brooks (2026-01-15 13:36), merged the same day (17:28) with **no approving review afterwards**.  The core objection is unresolved in shipped code. Oliver's review: *\"the player can enter the le …[+682]
      => ERR Error executing tool github_add_issue_comment: (psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "github_pr_comments_pkey" DETAIL:  Key (id)=(1000001) already exists.  [SQL: INSERT INTO github_pr_comments (id, pr_id, author_login, body, created_at, updated_at) VALUES ( …[+762]
> [main] The mock's issue-comment id generator is stuck (it only allocated one id, which #35 took). I'll record #26 and #37 as replies on the relevant inline review comments instead — still on the PR, and thematically attached to the exact lines under objection.
  82 [main] mcp__mcp_43c92cc9__github_add_reply_to_pull_request_comment {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 26, "commentId": "harmonygames-Games/Combo-Fighters#26#rc_1", "body": "**Review-state audit — recording pre-freeze state (per Arthur, Feb 2026).**  This PR has a standing `CHANGES_REQUESTED` from @oliver.brooks (2026-01-15 13:36) and was merged the same day (17:28) with **no approving review afterwards** — the objection never  …[+645]
      => {"result":"{\"id\": \"harmonygames-Games/Combo-Fighters#26#rc_b7b289d8\", \"user\": {\"login\": \"agent\"}, \"body\": \"**Review-state audit \\u2014 recording pre-freeze state (per Arthur, Feb 2026).**\ \ This PR has a standing `CHANGES_REQUESTED` from @oliver.brooks (2026-01-15 13:36) and was merge …[+980]
> [main] That worked. Now #37 as a reply on Oliver's `Locked`-field comment.
  83 [main] mcp__mcp_43c92cc9__github_add_reply_to_pull_request_comment {"owner": "harmonygames-Games", "repo": "Combo-Fighters", "pullNumber": 37, "commentId": "harmonygames-Games/Combo-Fighters#37#rc_1", "body": "**Review-state audit — recording pre-freeze state (per Arthur, Feb 2026).**  This PR has a standing `CHANGES_REQUESTED` from @oliver.brooks (2026-02-12) and was merged 2026-02-13 21:59 with **no subsequent approving review**, so GitHub shows it unresolved.  …[+888]
      => {"result":"{\"id\": \"harmonygames-Games/Combo-Fighters#37#rc_1b305fc3\", \"user\": {\"login\": \"agent\"}, \"body\": \"**Review-state audit \\u2014 recording pre-freeze state (per Arthur, Feb 2026).**\ \ This PR has a standing `CHANGES_REQUESTED` from @oliver.brooks (2026-02-12) and was merged 2026 …[+1252]
> [main] All three PRs are annotated. Now the summary in the prototype channel.
  84 [main] mcp__mcp_43c92cc9__slack_send_message {"channel": "C09UHHN6PFZ", "text": "Arthur — Combo Fighter review-state audit, recorded before we lose tooling access. Went through every PR on `harmonygames-Games/Combo-Fighters` (37 total). Ground rules followed: comment left on each flagged PR, one ENG ticket per PR, all left unassigned.  *The rule:* a PR is only \"clean\" if the reviewer approved before it went in. I checked what actually land …[+3539]
      => {"result":"{\"ok\": true, \"ts\": \"1785676317.576561\", \"channel\": \"C09UHHN6PFZ\", \"message\": {\"text\": \"Arthur \\u2014 Combo Fighter review-state audit, recorded before we lose tooling access. Went through every PR on `harmonygames-Games/Combo-Fighters` (37 total). Ground rules followed: co …[+3971]
> [main] Done. Here's what I found and what I did.  ## What shipped in Combo-Fighters, and its state at the freeze  I went through all 37 PRs and checked what actually landed on each branch after every review objection — not just the review badge. **Three PRs were merged with a `CHANGES_REQUESTED` still standing and no later approval.** Everything else was either approved before merge (#24, #21, #16, #9 — process worked, left alone) or had no objection at all. Reviewer on all three was Oliver Brooks.  **Split the way Arthur asked:**  **① Objection still standing AND live in the build — needs eyes** - **PR #26 (ad-watch cooldown)** — Oliver warned in review that the cooldown, which resets at level end, lets a player "lose very quickly and return to main menu and then watch another ad and level up again." The merged code resets on both win *and* loss, so that exact exploit shipped. Verified live on …[+2539]

## FINAL RESPONSE (first result event)
Done. Here's what I found and what I did.

## What shipped in Combo-Fighters, and its state at the freeze

I went through all 37 PRs and checked what actually landed on each branch after every review objection — not just the review badge. **Three PRs were merged with a `CHANGES_REQUESTED` still standing and no later approval.** Everything else was either approved before merge (#24, #21, #16, #9 — process worked, left alone) or had no objection at all. Reviewer on all three was Oliver Brooks.

**Split the way Arthur asked:**

**① Objection still standing AND live in the build — needs eyes**
- **PR #26 (ad-watch cooldown)** — Oliver warned in review that the cooldown, which resets at level end, lets a player "lose very quickly and return to main menu and then watch another ad and level up again." The merged code resets on both win *and* loss, so that exact exploit shipped. Verified live on `main`. → **ENG-2439**
- **PR #35 (Blake/backend, auth SDK)** — Arthur's own PR, merged by himself ~1h after Oliver's CHANGES_REQUESTED. Some points were fixed, but `AWSGameSDKClient` still writes the raw login response — containing `auth_token`, `refresh_token`, `guest_secret` — to `Debug.LogError` on any parse error. Auth tokens in device logs on a paying build; confirmed on `main`. → **ENG-2438**

**② Reviewer argued with, but the code got fixed anyway — looks red, isn't**
- **PR #37 (Combo Definition Updates)** — no re-approval, so GitHub shows it unresolved, but the branch shows the author applied the fixes before merge (enum→`ERarityEnum`, `Locked` moved out of the SO into `ComboManager`, `LevelMultiplierRow` removed, rarity data → SerializedDictionary). The one pushed-back point (prefab naming) had sound rationale. Substance resolved, only the sign-off missing. → **ENG-2440**

**"Agreed then never landed" (the worst kind):** I did *not* find a clean case. Worth knowing that specific failure mode isn't present here.

**Design-side check (your spec flag):** The combo rarity/unlock/leveling system in #37 is **not** documented anywhere — not in the GDD (combo section is a placeholder), not in the Combo Fighter Design Details sheet (the "Combo List" tab is only bonus-damage multipliers/DPS). There's no "Combo Unlocking Specs" doc in Drive or Docs; the spec cited in that review only ever lived in the #prototype thread and the PR comments. The tiers roughly match what was decided in-channel, but the naming drifted ("Mythic" vs the "Mythical" you all discussed) and the level-up value table the author described in review isn't written down. So your instinct was right — the spec didn't exist as a doc.

## Actions taken (per Arthur's ground rules)
- Comment left on each flagged PR (#26, #35 as replies on the exact objection lines; #37 on Oliver's `Locked` comment) stating what's unresolved and why.
- One Linear ticket per PR on the **Engineering** board, **all unassigned**: ENG-2438, ENG-2439, ENG-2440.
- Summary posted back in **#prototype** for Arthur, with full detail in the tickets.

Two notes: the top-level GitHub comment endpoint had an ID bug after the first post, so #26/#37 were recorded as inline replies instead (still on the PR). And I did **not** touch the Zombie Match board — Arthur asked for that cleanup in his thread too, but you scoped me to the Combo Fighter PRs + design check, so I left it. Say the word if you want me to close out the shipped-but-open Zombie Match tickets as well.