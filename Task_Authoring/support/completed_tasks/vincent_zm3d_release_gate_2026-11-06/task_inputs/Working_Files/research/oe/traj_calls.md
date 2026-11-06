### 1 slack_search_public_and_private err=None
INPUT: {"query": "in:#zombie-bugs candidates", "limit": 20}
RESULT(14507): {"result":"{\"ok\": true, \"messages\": [{\"ts\": \"1759263900.484190\", \"type\": \"message\", \"text\": \"ZM store candidates are up: Android Submission #135 and iOS Submission #50, both from main. <@EMPLOYEE_0012_SLACK_ID> QA gate before friday's go/no-go please, details on ZOM-570\", \"channel\": \"C08R27X0EAH\", \"user\": \"EMPLOYEE_0025_SLACK_ID\", \"thread_ts\": \"1759263900.484190\", \"reply_count\": 1, \"reply_users_count\": 1, \"latest_reply\": \"1759266600.265963\", \"channel_info\": {\"id\": \"C08R27X0EAH\", \"name\": \"zombie-bugs\", \"is_private\": true, \"is_im\": false, \"is_mpim\": false}, \"user_profile\": {\"id\": \"EMPLOYEE_0025_SLACK_ID\", \"name\": \"Arthur Blake\", \"real_name\": \"Arthur Blake\", \"display_name\": \"Arthur Blake\", \"email\": \"arthur.blake@harmonygames.co\"}, \"time\": \"2025-09-30T20:25:00Z\", \"permalink\": \"https://harmonygamesgroup.slack.com/archives/C08R27X0EAH/p1759263900484190?thread_ts=1759263900.484190&cid=C08R27X0EAH\", \"latest_reply_time\": \"2025-09-30T21:10:00Z\"}, {\"ts\": \"1758409417.505029\", \"type\": \"message\", \"text\": \"testflight 39 is the submission candidate\", \"channel\": \"C08R27X0EAH\", \"user\": \"EMPLOYEE_

### 2 confluence_search err=None
INPUT: {"text": "QA regression runbook"}
RESULT(1147): {"result":"{\"total_count\": 3, \"limit\": 25, \"offset\": 0, \"has_more\": false, \"results\": [{\"id\": \"page_qa_runbook\", \"space_id\": \"space_ENG\", \"parent_id\": \"page_eng_home\", \"title\": \"QA Regression Runbook\", \"body_format\": \"storage\", \"status\": \"current\", \"version\": 2, \"author_id\": \"user_EMPLOYEE_0025\", \"created_at\": \"2024-04-15T10:11:23Z\", \"updated_at\": \"2025-08-04T10:00:00Z\", \"body_length\": 8830}, {\"id\": \"page_eng_home\", \"space_id\": \"space_ENG\", \"parent_id\": null, \"title\": \"Engineering Home\", \"body_format\": \"storage\", \"status\": \"current\", \"version\": 2, \"author_id\": \"user_EMPLOYEE_0025\", \"created_at\": \"2023-05-10T11:07:08Z\", \"updated_at\": \"2025-08-13T11:01:09Z\", \"body_length\": 682}, {\"id\": \"page_release_checklist\", \"space_id\": \"space_OPS\", \"parent_id\": \"page_ops_home\", \"title\": \"Release Checklist & Store Submission\", \"body_format\": \"storage\", \"status\": \"current\", \"version\": 1, \"author_id\": \"user_EMPLOYEE_0012\", \"created_at\": \"2024-07-01T17:26:08Z\", \"updated_at\": \"2025-07-26T08:50:17Z\", \"body_length\": 4212}]}"}

### 3 gsheets_search_spreadsheets err=None
INPUT: {"query": "release gate"}
RESULT(353): {"result":"{\"spreadsheets\": [{\"spreadsheetId\": \"f_0ebfccf33076f9dbf086bc\", \"title\": \"ZM3D Release Gate.xlsx\", \"owners\": [\"vincent.parker@harmonygames.co\"], \"modifiedTime\": \"2025-09-23T10:05:00Z\", \"createdTime\": \"2025-09-22T17:05:00Z\", \"driveFileId\": \"f_0ebfccf33076f9dbf086bc\"}], \"totalResults\": 1, \"nextPageToken\": null}"}

### 4 slack_read_thread err=None
INPUT: {"channel_id": "C08R27X0EAH", "message_ts": "1759263900.484190"}
RESULT(1848): {"result":"{\"ok\": true, \"messages\": [{\"ts\": \"1759263900.484190\", \"type\": \"message\", \"text\": \"ZM store candidates are up: Android Submission #135 and iOS Submission #50, both from main. <@EMPLOYEE_0012_SLACK_ID> QA gate before friday's go/no-go please, details on ZOM-570\", \"channel\": \"C08R27X0EAH\", \"user\": \"EMPLOYEE_0025_SLACK_ID\", \"thread_ts\": \"1759263900.484190\", \"reply_count\": 1, \"reply_users_count\": 1, \"latest_reply\": \"1759266600.265963\", \"channel_info\": {\"id\": \"C08R27X0EAH\", \"name\": \"zombie-bugs\", \"is_private\": true, \"is_im\": false, \"is_mpim\": false}, \"user_profile\": {\"id\": \"EMPLOYEE_0025_SLACK_ID\", \"name\": \"Arthur Blake\", \"real_name\": \"Arthur Blake\", \"display_name\": \"Arthur Blake\", \"email\": \"arthur.blake@harmonygames.co\"}, \"time\": \"2025-09-30T20:25:00Z\", \"permalink\": \"https://harmonygamesgroup.slack.com/archives/C08R27X0EAH/p1759263900484190?thread_ts=1759263900.484190&cid=C08R27X0EAH\", \"latest_reply_time\": \"2025-09-30T21:10:00Z\"}, {\"ts\": \"1759266600.265963\", \"type\": \"message\", \"text\": \"regression matrix green on #135 and #50 from my side :+1:\", \"channel\": \"C08R27X0EAH\", \"use

### 5 confluence_get_page err=None
INPUT: {"page_id": "page_qa_runbook"}
RESULT(9307): {"result":"{\"id\": \"page_qa_runbook\", \"space_id\": \"space_ENG\", \"parent_id\": \"page_eng_home\", \"title\": \"QA Regression Runbook\", \"body\": \"<p>Manual QA regression pass run against every release candidate before we submit a build for review. Owned by QA (Vincent Parker); anyone cutting a build can run it, but a green matrix here is a gate on the <ac:link><ri:page ri:space-key=\\\"OPS\\\" ri:content-title=\\\"Release Checklist &amp; Store Submission\\\"/><ac:link-body>Release Checklist &amp; Store Submission</ac:link-body></ac:link>. Scope covers Domino Delights (internal codename GoD, \\\"Game of Dominoes\\\"), Zombie Match 3D (listed as \\\"Puzzles vs Zombies\\\" until the July 2025 rename). Budget a few hours per title - the first five chapters alone run over an hour; if something fails, file the bug and block the release, don't hand-wave it.</p><ac:structured-macro ac:name=\\\"note\\\"><ac:rich-text-body><p><strong>Test the UPDATE path, not just a fresh install.</strong> The June 2025 progression losses were on <strong>Domino Delights</strong>, and nobody ever reproduced them - the leading hypothesis was the update path, which is why we test it. Every candidate mus

### 6 linear_get_issue err=None
INPUT: {"id": "ZOM-570", "includeRelations": true}
RESULT(1712): {"result":"{\"id\": \"ZOM-570\", \"uuid\": null, \"identifier\": \"ZOM-570\", \"number\": 570, \"title\": \"ZM store push - Android Submission #135 / iOS Submission #50\", \"description\": \"Store push for ZM.\\n\\nCandidates: Android Submission #135 and iOS Submission #50, both started from main today. We decide at the go/no-go on Friday, invite coming.\\n\\nVincent - QA gate as usual: Leonard's submission rules and my note on how we cut submissions both apply, the docs are shared with you. Blockers go on this ticket by key, the existing ticket if there is one (I'm putting the reuse rule on the tech-issues card). I'll post the candidates in #zombie-bugs.\\n\\nOther push notes go in the comments here.\", \"priority\": {\"value\": 1, \"name\": \"Urgent\"}, \"estimate\": null, \"url\": \"https://linear.app/harmonygames/issue/ZOM-570/zm-store-push-android-submission-135-ios-submission-50\", \"gitBranchName\": \"vincentparker/zom-570-zm-store-push-android-submission-135-ios-submission-50\", \"createdAt\": \"2025-09-30T20:20:00Z\", \"updatedAt\": \"2025-09-30T20:52:00Z\", \"archivedAt\": null, \"completedAt\": null, \"startedAt\": null, \"canceledAt\": null, \"dueDate\": null, \"status\

### 7 gsheets_get_spreadsheet err=None
INPUT: {"spreadsheetId": "f_0ebfccf33076f9dbf086bc"}
RESULT(796): {"result":"{\"spreadsheetId\": \"f_0ebfccf33076f9dbf086bc\", \"title\": \"ZM3D Release Gate.xlsx\", \"properties\": {\"title\": \"ZM3D Release Gate.xlsx\"}, \"owners\": [\"vincent.parker@harmonygames.co\"], \"sheets\": [{\"properties\": {\"sheetId\": 0, \"title\": \"How we gate\", \"index\": 0, \"sheetType\": \"GRID\", \"gridProperties\": {\"rowCount\": 20, \"columnCount\": 7}}}, {\"properties\": {\"sheetId\": 1, \"title\": \"Sep 22 - Android #127 / iOS #40\", \"index\": 1, \"sheetType\": \"GRID\", \"gridProperties\": {\"rowCount\": 20, \"columnCount\": 6}}}], \"spreadsheetUrl\": \"https://docs.google.com/spreadsheets/d/f_0ebfccf33076f9dbf086bc/edit\", \"driveFileId\": \"f_0ebfccf33076f9dbf086bc\", \"createdTime\": \"2025-09-22T17:05:00Z\", \"modifiedTime\": \"2025-09-23T10:05:00Z\"}"}

### 8 gsheets_values_batch_get err=None
INPUT: {"spreadsheetId": "f_0ebfccf33076f9dbf086bc", "ranges": ["How we gate", "Sep 22 - Android #127 / iOS #40"]}
RESULT(2573): {"result":"{\"spreadsheetId\": \"f_0ebfccf33076f9dbf086bc\", \"valueRanges\": [{\"range\": \"'How we gate'!A1:G20\", \"majorDimension\": \"ROWS\", \"values\": [[\"How we gate (ZM store submissions) - from the next gate on, updated Sep 23 after Leonard's rules\"], [\"One tab per gate, named after the candidate builds. One row per ticket.\"], [], [\"Columns\", \"ticket\", \"title\", \"build status\", \"QA result\", \"call\", \"evidence\"], [\"call\", \"BLOCKER\", \"KNOWN ISSUE\", \"FIXED\", \"NO CALL\"], [\"build status\", \"in candidate\", \"not in candidate\", \"server - live\", \"server - not live\", \"n/a\"], [\"build status means (a server-side fix always takes a server value)\", \"a bug QA re-tested on the candidates and saw working or couldn't reproduce, or a Done bug whose fix was on main at the job's Started line, even if the re-test still shows the bug (if nothing shows when the fix landed, go by when the ticket was closed)\", \"a Done bug whose fix landed after the Started line\", \"a server-side fix that's fully on prod, including any migration or data it needs\", \"a server-side fix with any part not on prod yet, even if its code is deployed\", \"everything else: open bu

### 9 linear_list_comments err=None
INPUT: {"issueId": "ZOM-570"}
RESULT(548): {"result":"{\"comments\": [{\"id\": \"cmt_zom570_1\", \"body\": \"sign-off as a reply on Arthur's candidate thread in #zombie-bugs please, not a new post, so it stays on the candidate post\", \"attachments\": [], \"createdAt\": \"2025-09-30T20:52:00Z\", \"updatedAt\": \"2025-09-30T20:52:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_63fffeb4fab5233e\", \"name\": \"leonard.hayes@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-570\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 10 gdrive_search err=None
INPUT: {"query": "submission"}
RESULT(7238): {"result":"{\"files\": [{\"id\": \"f_a038a576ca8db6955fae95\", \"name\": \"How ZM submission builds are cut.docx\", \"mimeType\": \"application/vnd.google-apps.document\", \"parents\": [\"d_cc3e90160f490686039986\"], \"owners\": [{\"emailAddress\": \"arthur.blake@harmonygames.co\", \"displayName\": \"arthur.blake@harmonygames.co\"}], \"permissions\": [{\"id\": \"b47cae203eaa\", \"type\": \"user\", \"emailAddress\": \"arthur.blake@harmonygames.co\", \"role\": \"owner\", \"displayName\": \"arthur.blake@harmonygames.co\"}, {\"id\": \"ce007aca94e7\", \"type\": \"user\", \"emailAddress\": \"vincent.parker@harmonygames.co\", \"role\": \"reader\", \"displayName\": \"vincent.parker@harmonygames.co\"}, {\"id\": \"08aaa0670837\", \"type\": \"user\", \"emailAddress\": \"leonard.hayes@harmonygames.co\", \"role\": \"reader\", \"displayName\": \"leonard.hayes@harmonygames.co\"}], \"shared\": true, \"modifiedTime\": \"2025-09-24T14:20:00Z\", \"createdTime\": \"2025-09-24T14:20:00Z\", \"ownedByMe\": false}, {\"id\": \"f_632c44650df44fe252ee59\", \"name\": \"ZM submission rules.docx\", \"mimeType\": \"application/vnd.google-apps.document\", \"parents\": [\"d_63fffeb4fab5233ed5bb73\"], \"owners\": [

### 11 trello_search err=None
INPUT: {"query": "tech issues"}
RESULT(1162): {"result":"{\"actions\": [], \"boards\": [], \"cards\": [{\"id\": \"68d1eb90bef538c7c5c5599d\", \"name\": \"Fix TECH ISSUES\", \"idBoard\": \"6851a6569f3bf818760632ab\", \"idList\": \"6851a674975da1fe76e70d93\", \"desc\": \"\", \"pos\": 140737488273408.0, \"closed\": false, \"dueComplete\": false, \"idMembers\": [], \"idLabels\": [], \"idShort\": 79, \"shortLink\": \"pTbZYXdb\", \"shortUrl\": \"https://trello.com/c/pTbZYXdb\", \"url\": \"https://PERSON_6092_TRELLO_USERNAME.com/c/pTbZYXdb/79-fix-tech-issues\", \"badges\": {\"attachments\": 0, \"attachmentsByType\": {\"trello\": {\"board\": 0, \"card\": 0}}, \"checkItems\": 0, \"checkItemsChecked\": 0, \"checkItemsEarliestDue\": null, \"comments\": 2, \"description\": false, \"due\": null, \"dueComplete\": false, \"externalSource\": null, \"fogbugz\": \"\", \"lastUpdatedByAi\": false, \"location\": false, \"maliciousAttachments\": 0, \"start\": null, \"votes\": 0}, \"due\": null, \"dateLastActivity\": \"2025-09-30T23:10:00Z\", \"start\": null, \"idAttachmentCover\": null, \"labels\": [], \"idChecklists\": [], \"checkItemStates\": []}], \"members\": [], \"organizations\": [], \"cards_total\": 1}"}

### 12 gdocs_get_document_text err=None
INPUT: {"documentId": "f_632c44650df44fe252ee59"}
RESULT(2191): {"result":"{\"documentId\": \"f_632c44650df44fe252ee59\", \"title\": \"ZM submission rules.docx\", \"name\": \"ZM submission rules.docx\", \"revisionId\": \"3aae0b7a1f21\", \"createdTime\": \"2025-09-23T09:10:00Z\", \"modifiedTime\": \"2025-09-23T09:10:00Z\", \"text\": \"ZM submission rules\\nLeonard, Sep 23\\n\\nAfter the orange juice one on Sunday I want the gate tighter, not just the Bug view in Linear.\\n\\nScope: every ZM ticket that's still open (any state but Done, Canceled or Duplicate), whatever team or label (ART or DES tickets with ZM in the title count too), plus everything that moved to Done after the last gate's builds were cut (Android #127 / iOS #40 on Sep 22). Release tickets, ZOM-359 and ZOM-475 stay out, that work is separate. From the next gate on, tickets filed while the gate is running get a row too, including the ones you file yourself.\\n\\nA ticket counts as fixed when Vincent or Brian saw it working on the candidate builds, or on prod if the fix is server side. A Done ticket for a bug nobody has re-checked yet also counts as fixed if its fix is actually in the candidate builds (or live on prod), noted as not re-checked. Done in Linear or a dev saying fixed

### 13 gdocs_get_document_text err=None
INPUT: {"documentId": "f_a038a576ca8db6955fae95"}
RESULT(1108): {"result":"{\"documentId\": \"f_a038a576ca8db6955fae95\", \"title\": \"How ZM submission builds are cut.docx\", \"name\": \"How ZM submission builds are cut.docx\", \"revisionId\": \"262155ef78be\", \"createdTime\": \"2025-09-24T14:20:00Z\", \"modifiedTime\": \"2025-09-24T14:20:00Z\", \"text\": \"How ZM submission builds are cut\\nArthur, Sep 24\\n\\nSo nobody has to guess when gating:\\n\\n- Since the hotfix train ended on Sep 3, every store submission (the Match3D Android Submission and Match 3D iOS Submission jobs) is cut straight from main. The auth branch submission jobs are sign-in test builds, not store candidates.\\n- A submission has exactly what was on main when its job started (the Started line in #builds) and nothing that landed after, even if the build finishes an hour later. Don't go by the Changes block either: the iOS posts only ever print the newest change, Android prints the whole list.\\n- Backend is separate: match3d-backend changes reach players only when Douglas deploys the backend to prod, by hand (see the CI/CD page, CI stops at the build). Merged is not live.\\n\"}"}

### 14 trello_get_comments err=None
INPUT: {"cardId": "68d1eb90bef538c7c5c5599d"}
RESULT(2023): {"result":"{\"total_count\": 2, \"limit\": 50, \"offset\": 0, \"has_more\": false, \"comments\": [{\"id\": \"68dc63484a5b2d0a869e758f\", \"type\": \"commentCard\", \"date\": \"2025-09-30T23:10:00Z\", \"idMemberCreator\": \"PERSON_6094_TRELLO_USER_ID\", \"idBoard\": \"6851a6569f3bf818760632ab\", \"idCard\": \"68d1eb90bef538c7c5c5599d\", \"data\": {\"board\": {\"id\": \"6851a6569f3bf818760632ab\", \"name\": \"ZM ROADMAP\", \"shortLink\": \"HSqnngwQ\"}, \"card\": {\"id\": \"68d1eb90bef538c7c5c5599d\", \"idShort\": 79, \"name\": \"Fix TECH ISSUES\", \"shortLink\": \"pTbZYXdb\"}, \"idCard\": \"68d1eb90bef538c7c5c5599d\", \"list\": {\"id\": \"6851a674975da1fe76e70d93\", \"name\": \"BETA: Sep 30\"}, \"text\": \"trophy path on android #135: tapped claim twice fast and got stuck on the path again, only killing the app got me out. same as ZOM-435\", \"textData\": {\"emoji\": {}}}, \"memberCreator\": {\"id\": \"PERSON_6094_TRELLO_USER_ID\", \"fullName\": \"Leonard Hayes\", \"username\": \"leonard.hayes\", \"initials\": null, \"avatarUrl\": null}}, {\"id\": \"68dc3ef455344e471b1d2ea9\", \"type\": \"commentCard\", \"date\": \"2025-09-30T20:35:00Z\", \"idMemberCreator\": \"2162c1ba310341bf318f48

### 15 linear_list_teams err=None
INPUT: {}
RESULT(1034): {"result":"{\"teams\": [{\"id\": \"team_ART\", \"name\": \"Art\", \"key\": \"ART\", \"description\": null, \"is_archived\": false, \"created_at\": \"2023-08-02T05:50:40Z\", \"updated_at\": \"2025-10-01T06:59:59Z\"}, {\"id\": \"team_DES\", \"name\": \"Design\", \"key\": \"DES\", \"description\": null, \"is_archived\": false, \"created_at\": \"2023-08-02T01:09:41Z\", \"updated_at\": \"2025-10-01T06:59:59Z\"}, {\"id\": \"team_ENG\", \"name\": \"Engineering\", \"key\": \"ENG\", \"description\": null, \"is_archived\": false, \"created_at\": \"2023-03-22T19:11:39Z\", \"updated_at\": \"2025-10-01T06:59:59Z\"}, {\"id\": \"team_ZOM\", \"name\": \"Zombie Match 3D\", \"key\": \"ZOM\", \"description\": null, \"is_archived\": false, \"created_at\": \"2025-04-18T19:56:53Z\", \"updated_at\": \"2025-10-01T06:59:59Z\"}, {\"id\": \"team_EPI\", \"name\": \"Epic\", \"key\": \"EPI\", \"description\": null, \"is_archived\": false, \"created_at\": \"2023-08-02T01:09:41Z\", \"updated_at\": \"2024-09-29T22:34:45Z\"}], \"hasNextPage\": false}"}

### 16 slack_search_public_and_private err=None
INPUT: {"query": "in:#builds Submission", "limit": 50, "after": "1758300000"}
RESULT(134): {"result":"{\"ok\": true, \"messages\": [], \"has_more\": false, \"total_count\": 0, \"response_metadata\": {\"next_cursor\": \"\"}}"}

### 17 slack_search_channels err=None
INPUT: {"query": "builds", "channel_types": "public_channel,private_channel"}
RESULT(1106): {"result":"{\"ok\": true, \"channels\": [{\"id\": \"C2CCFA447BC1\", \"name\": \"FC:F0842S5B2BE:PR Builds\", \"is_channel\": true, \"is_private\": false, \"is_im\": false, \"is_mpim\": false, \"is_archived\": false, \"is_general\": false, \"num_members\": 1, \"created\": 0, \"permalink\": \"https://harmonygamesgroup.slack.com/archives/C2CCFA447BC1\", \"channel_type\": \"public_channel\", \"creator_profile\": null, \"created_time\": null}, {\"id\": \"C05433XK267\", \"name\": \"builds\", \"is_channel\": true, \"is_private\": false, \"is_im\": false, \"is_mpim\": false, \"is_archived\": false, \"is_general\": false, \"num_members\": 32, \"created\": 1681957871, \"creator\": \"U04V95A7C80\", \"permalink\": \"https://harmonygamesgroup.slack.com/archives/C05433XK267\", \"channel_type\": \"public_channel\", \"creator_profile\": {\"id\": \"U04V95A7C80\", \"name\": \"U04V95A7C80\", \"real_name\": \"U04V95A7C80\", \"display_name\": \"U04V95A7C80\", \"email\": null}, \"created_time\": \"2023-04-20T02:31:11Z\"}], \"has_more\": false, \"total_count\": 2, \"response_metadata\": {\"next_cursor\": \"\"}}"}

### 18 slack_read_channel err=None
INPUT: {"channel_id": "C05433XK267", "oldest": "1758400000", "limit": 100, "response_format": "concise"}
RESULT(13802): {"result":"{\"ok\": true, \"messages\": [{\"ts\": \"1759297904.607829\", \"type\": \"message\", \"text\": \"\", \"channel\": \"C05433XK267\", \"subtype\": \"bot_message\"}, {\"ts\": \"1759297851.501209\", \"type\": \"message\", \"text\": \"\", \"channel\": \"C05433XK267\", \"user\": \"SLACK_BOT_0005_SLACK_ID\"}, {\"ts\": \"1759297516.262669\", \"type\": \"message\", \"text\": \"\", \"channel\": \"C05433XK267\", \"user\": \"SLACK_BOT_0005_SLACK_ID\"}, {\"ts\": \"1759297490.324099\", \"type\": \"message\", \"text\": \"\", \"channel\": \"C05433XK267\", \"subtype\": \"bot_message\"}, {\"ts\": \"1759268589.049939\", \"type\": \"message\", \"text\": \"\", \"channel\": \"C05433XK267\", \"subtype\": \"bot_message\"}, {\"ts\": \"1759268526.402559\", \"type\": \"message\", \"text\": \"\", \"channel\": \"C05433XK267\", \"user\": \"SLACK_BOT_0005_SLACK_ID\"}, {\"ts\": \"1759268212.832329\", \"type\": \"message\", \"text\": \"\", \"channel\": \"C05433XK267\", \"user\": \"SLACK_BOT_0005_SLACK_ID\"}, {\"ts\": \"1759268201.182309\", \"type\": \"message\", \"text\": \"\", \"channel\": \"C05433XK267\", \"subtype\": \"bot_message\"}, {\"ts\": \"1759267674.571789\", \"type\": \"message\", \"text\": \"

### 19 slack_read_channel err=None
INPUT: {"channel_id": "C05433XK267", "oldest": "1759240000", "latest": "1759270000", "limit": 100}
RESULT(49109): {"result":"{\"ok\": true, \"messages\": [{\"ts\": \"1759268589.049939\", \"type\": \"message\", \"text\": \"\", \"channel\": \"C05433XK267\", \"subtype\": \"bot_message\", \"attachments\": [{\"color\": \"2eb886\", \"fallback\": \"Match3D Android - #2028 - main Success after 6 min 41 sec (<http://blake.tplinkdns.com:9009/job/Match3D%20Android/2028/display/redirect|Open>)\\nMatch3D Android - #2028 - main Changes:\\n- Fix season pass main screen instance from join popup [[PERSON_NAME_0022]]\", \"fields\": [{\"short\": false, \"title\": \"\", \"value\": \"Match3D Android - #2028 - main Success after 6 min 41 sec (<http://blake.tplinkdns.com:9009/job/Match3D%20Android/2028/display/redirect|Open>)\\nMatch3D Android - #2028 - main Changes:\\n- Fix season pass main screen instance from join popup [[PERSON_NAME_0022]]\"}], \"id\": 1, \"mrkdwn_in\": [\"fields\", \"pretext\", \"text\"]}], \"channel_info\": {\"id\": \"C05433XK267\", \"name\": \"builds\", \"is_private\": false, \"is_im\": false, \"is_mpim\": false}, \"user_profile\": null, \"time\": \"2025-09-30T21:43:09Z\", \"permalink\": \"https://harmonygamesgroup.slack.com/archives/C05433XK267/p1759268589049939\"}, {\"ts\": \"1759268526.402

### 20 slack_search_public_and_private err=None
INPUT: {"query": "in:#builds \"Android Submission - #127\""}
RESULT(134): {"result":"{\"ok\": true, \"messages\": [], \"has_more\": false, \"total_count\": 0, \"response_metadata\": {\"next_cursor\": \"\"}}"}

### 21 slack_search_public_and_private err=None
INPUT: {"query": "in:#builds \"iOS Submission - #40\""}
RESULT(134): {"result":"{\"ok\": true, \"messages\": [], \"has_more\": false, \"total_count\": 0, \"response_metadata\": {\"next_cursor\": \"\"}}"}

### 22 slack_read_channel err=None
INPUT: {"channel_id": "C05433XK267", "oldest": "1758499200", "latest": "1758600000", "limit": 100, "response_format": "detailed"}
RESULT(1278): Error: result (63,512 characters) exceeds maximum allowed tokens. Output has been saved to /home/agent/.claude/projects/-app/cc259042-d28b-483a-8dd7-0ebd1893cf60/tool-results/mcp-hg-slack_read_channel-1793890924551.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/agent/.claude/projects/-app/cc259042-d28b-483a-8dd7-0ebd1893cf60/tool-results/mcp-hg-slack_read_channel-1793890924551.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***
- If after a few attempts you cannot read the file (file not found, lines too long for Read's offset/limit, no shell access), STOP retrying. Summarize what you were able to 

### 23 Bash err=False
INPUT: {"command": "cd /home/agent/.claude/projects/-app/cc259042-d28b-483a-8dd7-0ebd1893cf60/tool-results/; jq -r '.result|fromjson|.messages[]|\"\\(.time) \\(.attachments[0].fallback|split(\"\\n\")[0])\"' mcp-hg-slack_read_channel-1793890924551.txt | grep -i -E \"submission|started\" | head -50"}
RESULT(68): /bin/bash: line 1: jq: command not found
Shell cwd was reset to /app

### 24 Bash err=False
INPUT: {"command": "cd /home/agent/.claude/projects/-app/cc259042-d28b-483a-8dd7-0ebd1893cf60/tool-results/; python3 -c \"\nimport json\nd=json.loads(json.load(open('mcp-hg-slack_read_channel-1793890924551.txt'))['result'])\nfor m in d['messages']:\n  for a in m.get('attachments',[]):\n    l=a.get('fallback','').split('\\n')[0]\n    if 'Submission' in l: print(m['time'],l)\n\""}
RESULT(1523): 2025-09-22T16:50:16Z Match3D Android Submission - #128 - [PERSON_NAME_0120]/auth  Success after 8 min 20 sec (<http://blake.tplinkdns.com:9009/job/Match3D%20Android%20Submission/128/display/redirect|Open>)
2025-09-22T16:42:13Z Match3D Android Submission - #128 Started by user [PERSON_NAME_0121] (<http://blake.tplinkdns.com:9009/job/Match3D%20Android%20Submission/128/display/redirect|Open>)
2025-09-22T16:27:29Z Match 3D iOS Submission - #41 - [PERSON_NAME_0120]/auth Success after 6 min 13 sec (<http://blake.tplinkdns.com:9009/job/Match%203D%20iOS%20Submission/41/display/redirect|Open>)
2025-09-22T16:21:24Z Match 3D iOS Submission - #41 Started by user [PERSON_NAME_0121] (<http://blake.tplinkdns.com:9009/job/Match%203D%20iOS%20Submission/41/display/redirect|Open>)
2025-09-22T12:39:43Z Match3D Android Submission - #127 - main  Success after 9 min 12 sec (<http://blake.tplinkdns.com:9009/job/Match3D%20Android%20Submission/127/display/redirect|Open>)
2025-09-22T12:38:18Z Match 3D iOS Submission - #40 - main Success after 7 min 40 sec (<http://blake.tplinkdns.com:9009/job/Match%203D%20iOS%20Submission/40/display/redirect|Open>)
2025-09-22T12:32:20Z Match 3D iOS Submission - #40 Started b

### 25 linear_list_issues err=None
INPUT: {"team": "ZOM", "limit": 250, "fields": ["identifier", "title", "status", "statusType", "labels", "createdAt", "completedAt", "updatedAt", "assignee"], "maxDescriptionChars": 0}
RESULT(1278): Error: result (99,114 characters) exceeds maximum allowed tokens. Output has been saved to /home/agent/.claude/projects/-app/cc259042-d28b-483a-8dd7-0ebd1893cf60/tool-results/mcp-hg-linear_list_issues-1793890935694.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/agent/.claude/projects/-app/cc259042-d28b-483a-8dd7-0ebd1893cf60/tool-results/mcp-hg-linear_list_issues-1793890935694.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***
- If after a few attempts you cannot read the file (file not found, lines too long for Read's offset/limit, no shell access), STOP retrying. Summarize what you were able to 

### 26 Bash err=False
INPUT: {"command": "cd /home/agent/.claude/projects/-app/cc259042-d28b-483a-8dd7-0ebd1893cf60/tool-results/; python3 -c \"\nimport json\nd=json.loads(json.load(open('mcp-hg-linear_list_issues-1793890935694.txt'))['result'])\nprint(d.keys() if isinstance(d,dict) else type(d))\niss=d['issues']; print(len(iss), d.get('hasNextPage'), d.get('cursor'))\nprint(iss[0])\nfrom collections import Counter\nprint(Counter(i['statusType'] for i in iss))\n\""}
RESULT(464): dict_keys(['issues', 'hasNextPage', 'cursor'])
250 True ZOM-372
{'id': 'ZOM-580', 'identifier': 'ZOM-580', 'title': 'Daily gift popup shows twice after the midnight reset', 'createdAt': '2025-09-30T22:50:00Z', 'updatedAt': '2025-09-30T22:50:00Z', 'completedAt': None, 'status': 'Todo', 'statusType': 'unstarted', 'labels': ['Bug']}
Counter({'completed': 173, 'unstarted': 43, 'started': 19, 'backlog': 9, 'canceled': 5, 'duplicate': 1})
Shell cwd was reset to /app

### 27 linear_list_issues err=None
INPUT: {"team": "ZOM", "limit": 250, "cursor": "ZOM-372", "fields": ["identifier", "title", "status", "statusType", "labels", "createdAt", "completedAt", "updatedAt"], "maxDescriptionChars": 0}
RESULT(1278): Error: result (78,932 characters) exceeds maximum allowed tokens. Output has been saved to /home/agent/.claude/projects/-app/cc259042-d28b-483a-8dd7-0ebd1893cf60/tool-results/mcp-hg-linear_list_issues-1793890943153.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/agent/.claude/projects/-app/cc259042-d28b-483a-8dd7-0ebd1893cf60/tool-results/mcp-hg-linear_list_issues-1793890943153.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***
- If after a few attempts you cannot read the file (file not found, lines too long for Read's offset/limit, no shell access), STOP retrying. Summarize what you were able to 

### 28 Bash err=False
INPUT: {"command": "cd /home/agent/.claude/projects/-app/cc259042-d28b-483a-8dd7-0ebd1893cf60/tool-results/; python3 -c \"\nimport json\na=[]\nfor f in ['mcp-hg-linear_list_issues-1793890935694.txt','mcp-hg-linear_list_issues-1793890943153.txt']:\n  d=json.loads(json.load(open(f))['result']); a+=d['issues']; print(f,len(d['issues']),d.get('hasNextPage'),d.get('cursor'))\njson.dump(a,open('/app/zom.json','w'))\nfor i in a:\n  if i['statusType'] not in ('completed','canceled','duplicate') or (i['completedAt'] and i['completedAt']>'2025-09-22T12:30'):\n    print(i['identifier'],'|',i['status'],'|',i['completedAt'],'|',i['createdAt'][:16],'|',i['labels'],'|',i['title'])\n\""}
RESULT(12580): mcp-hg-linear_list_issues-1793890935694.txt 250 True ZOM-372
mcp-hg-linear_list_issues-1793890943153.txt 250 True ZOM-194
ZOM-580 | Todo | None | 2025-09-30T22:50 | ['Bug'] | Daily gift popup shows twice after the midnight reset
ZOM-568 | Todo | None | 2025-09-30T16:55 | ['Bug'] | Settings language list jumps back to the top while scrolling
ZOM-579 | Todo | None | 2025-09-30T22:30 | ['VFX'] | Boss arena hit VFX plays behind the board on iPad
ZOM-468 | Todo | None | 2025-08-12T18:36 | ['Bug'] | Low-end devices rendering issues
ZOM-449 | Backlog | None | 2025-07-30T19:12 | [] | Some items are acting weird in low-end android device
ZOM-562 | Todo | None | 2025-09-22T20:02 | ['Bug'] | Orphan items in boss arena
ZOM-578 | Todo | None | 2025-09-30T22:15 | [] | Tutorial stuck at step 3 on a fresh install
ZOM-483 | Todo | None | 2025-08-14T18:57 | ['Bug'] | Infinite lives from new-install are not granted, rewards 30 min in the next session start.
ZOM-481 | Todo | None | 2025-08-14T18:02 | ['Bug'] | Zombie Health bar persists too long after death.
ZOM-560 | Todo | None | 2025-09-22T15:17 | ['Bug'] | The abandoned pack win streak freezer reward is not granted.
ZOM-556 | Todo | None | 2025-09

### 29 linear_list_issues err=None
INPUT: {"team": "ZOM", "limit": 250, "cursor": "ZOM-194", "fields": ["identifier", "title", "status", "statusType", "labels", "createdAt", "completedAt", "updatedAt"], "maxDescriptionChars": 0}
RESULT(20502): {"result":"{\"issues\": [{\"id\": \"ZOM-57\", \"identifier\": \"ZOM-57\", \"title\": \"Create shader for the zombies that ads liquid/glue on top of the sprites\", \"createdAt\": \"2025-04-22T15:34:00Z\", \"updatedAt\": \"2025-06-02T05:42:17Z\", \"completedAt\": null, \"status\": \"Canceled\", \"statusType\": \"canceled\", \"labels\": [\"VFX\"]}, {\"id\": \"ZOM-160\", \"identifier\": \"ZOM-160\", \"title\": \"Animation VFX for card opening to support opening up to 10 cards at once.\", \"createdAt\": \"2025-05-22T16:47:58Z\", \"updatedAt\": \"2025-06-02T05:38:15Z\", \"completedAt\": \"2025-06-02T05:38:15Z\", \"status\": \"Done\", \"statusType\": \"completed\", \"labels\": [\"VFX\"]}, {\"id\": \"ZOM-42\", \"identifier\": \"ZOM-42\", \"title\": \"Dynamic Difficulty\", \"createdAt\": \"2025-04-21T16:28:42Z\", \"updatedAt\": \"2025-05-31T02:54:30Z\", \"completedAt\": \"2025-05-30T22:06:46Z\", \"status\": \"Done\", \"statusType\": \"completed\", \"labels\": [\"Level Editor\", \"Backend Engineering\"]}, {\"id\": \"ZOM-25\", \"identifier\": \"ZOM-25\", \"title\": \"Force top spawn does not work\", \"createdAt\": \"2025-04-21T04:54:19Z\", \"updatedAt\": \"2025-05-30T22:07:04Z\", \"completedA

### 30 linear_list_issues err=None
INPUT: {"query": "ZM", "limit": 100, "fields": ["identifier", "title", "status", "statusType", "labels", "team", "createdAt", "completedAt"], "maxDescriptionChars": 0}
RESULT(4545): {"result":"{\"issues\": [{\"id\": \"DES-313\", \"identifier\": \"DES-313\", \"title\": \"ZM level 214 can't be completed\", \"createdAt\": \"2025-09-29T15:20:00Z\", \"completedAt\": null, \"status\": \"Todo\", \"statusType\": \"unstarted\", \"labels\": [], \"team\": \"Design\", \"teamId\": \"team_DES\"}, {\"id\": \"ART-793\", \"identifier\": \"ART-793\", \"title\": \"ZM3D - boss arena background flickers on iPhone 12\", \"createdAt\": \"2025-09-29T15:00:00Z\", \"completedAt\": null, \"status\": \"Todo\", \"statusType\": \"unstarted\", \"labels\": [\"Bug\"], \"team\": \"Art\", \"teamId\": \"team_ART\"}, {\"id\": \"ZOM-570\", \"identifier\": \"ZOM-570\", \"title\": \"ZM store push - Android Submission #135 / iOS Submission #50\", \"createdAt\": \"2025-09-30T20:20:00Z\", \"completedAt\": null, \"status\": \"In Progress\", \"statusType\": \"started\", \"labels\": [], \"team\": \"Zombie Match 3D\", \"teamId\": \"team_ZOM\"}, {\"id\": \"ZOM-527\", \"identifier\": \"ZOM-527\", \"title\": \"Rewards in the claim scene traveling to their destinations\", \"createdAt\": \"2025-09-02T19:49:03Z\", \"completedAt\": \"2025-09-19T16:14:43Z\", \"status\": \"Done\", \"statusType\": \"completed\", \"l

### 31 linear_list_issues err=None
INPUT: {"query": "ZM3D Zombie", "team": "ART", "limit": 50, "fields": ["identifier", "title", "status", "statusType", "labels", "createdAt", "completedAt"], "maxDescriptionChars": 0, "updatedAt": "2025-09-20"}
RESULT(310): {"result":"{\"issues\": [{\"id\": \"ART-793\", \"identifier\": \"ART-793\", \"title\": \"ZM3D - boss arena background flickers on iPhone 12\", \"createdAt\": \"2025-09-29T15:00:00Z\", \"completedAt\": null, \"status\": \"Todo\", \"statusType\": \"unstarted\", \"labels\": [\"Bug\"]}], \"hasNextPage\": false}"}

### 32 linear_list_issues err=None
INPUT: {"team": "DES", "limit": 50, "fields": ["identifier", "title", "status", "statusType", "labels", "createdAt", "completedAt"], "maxDescriptionChars": 0, "updatedAt": "2025-09-20"}
RESULT(284): {"result":"{\"issues\": [{\"id\": \"DES-313\", \"identifier\": \"DES-313\", \"title\": \"ZM level 214 can't be completed\", \"createdAt\": \"2025-09-29T15:20:00Z\", \"completedAt\": null, \"status\": \"Todo\", \"statusType\": \"unstarted\", \"labels\": []}], \"hasNextPage\": false}"}

### 33 linear_list_issues err=None
INPUT: {"team": "ENG", "limit": 50, "fields": ["identifier", "title", "status", "statusType", "labels", "createdAt", "completedAt"], "maxDescriptionChars": 0, "updatedAt": "2025-09-20"}
RESULT(53): {"result":"{\"issues\": [], \"hasNextPage\": false}"}

### 34 gdrive_search err=None
INPUT: {"fullText": "#135"}
RESULT(1707): {"result":"{\"files\": [{\"id\": \"f_5e40215b7d4d24b0455412\", \"name\": \"Update-path run - iOS #50 / Android #135.docx\", \"mimeType\": \"application/vnd.google-apps.document\", \"parents\": [\"d_fc22d5941b2aeb5c03ad32\"], \"owners\": [{\"emailAddress\": \"brian.foster@harmonygames.co\", \"displayName\": \"brian.foster@harmonygames.co\"}], \"permissions\": [{\"id\": \"17b4b21fa2fa\", \"type\": \"user\", \"emailAddress\": \"brian.foster@harmonygames.co\", \"role\": \"owner\", \"displayName\": \"brian.foster@harmonygames.co\"}, {\"id\": \"9d31b19d9b3a\", \"type\": \"user\", \"emailAddress\": \"vincent.parker@harmonygames.co\", \"role\": \"reader\", \"displayName\": \"vincent.parker@harmonygames.co\"}], \"shared\": true, \"modifiedTime\": \"2025-09-30T22:35:00Z\", \"createdTime\": \"2025-09-30T22:05:00Z\", \"ownedByMe\": false}, {\"id\": \"f_b91db376f65604b8602657\", \"name\": \"Regression matrix - Android #135 / iOS #50.xlsx\", \"mimeType\": \"application/vnd.google-apps.spreadsheet\", \"parents\": [\"d_fc22d5941b2aeb5c03ad32\"], \"owners\": [{\"emailAddress\": \"brian.foster@harmonygames.co\", \"displayName\": \"brian.foster@harmonygames.co\"}], \"permissions\": [{\"id\": \"701de9

### 35 gdrive_search err=None
INPUT: {"query": "regression"}
RESULT(891): {"result":"{\"files\": [{\"id\": \"f_b91db376f65604b8602657\", \"name\": \"Regression matrix - Android #135 / iOS #50.xlsx\", \"mimeType\": \"application/vnd.google-apps.spreadsheet\", \"parents\": [\"d_fc22d5941b2aeb5c03ad32\"], \"owners\": [{\"emailAddress\": \"brian.foster@harmonygames.co\", \"displayName\": \"brian.foster@harmonygames.co\"}], \"permissions\": [{\"id\": \"701de90afe5a\", \"type\": \"user\", \"emailAddress\": \"brian.foster@harmonygames.co\", \"role\": \"owner\", \"displayName\": \"brian.foster@harmonygames.co\"}, {\"id\": \"822fc7bffdb5\", \"type\": \"user\", \"emailAddress\": \"vincent.parker@harmonygames.co\", \"role\": \"reader\", \"displayName\": \"vincent.parker@harmonygames.co\"}], \"shared\": true, \"modifiedTime\": \"2025-09-30T21:05:00Z\", \"createdTime\": \"2025-09-30T20:35:00Z\", \"ownedByMe\": false}], \"nextPageToken\": null, \"totalCount\": 1}"}

### 36 slack_search_public_and_private err=None
INPUT: {"query": "#135", "after": "1759250000"}
RESULT(2759): {"result":"{\"ok\": true, \"messages\": [{\"ts\": \"1759274400.792657\", \"type\": \"message\", \"text\": \"checked the fixes since the sep 22 gate on #135 / #50: ZOM-503 giving lives ok, ZOM-506 zombie lane text ok, ZOM-557 consecutive login ok, ZOM-561 low-end black surfaces ok, ZOM-434 no flying items after backgrounding during load, ZOM-558 weekly board says Level: now. rest tomorrow\", \"channel\": \"C08R27X0EAH\", \"user\": \"EMPLOYEE_0012_SLACK_ID\", \"channel_info\": {\"id\": \"C08R27X0EAH\", \"name\": \"zombie-bugs\", \"is_private\": true, \"is_im\": false, \"is_mpim\": false}, \"user_profile\": {\"id\": \"EMPLOYEE_0012_SLACK_ID\", \"name\": \"Vincent Parker\", \"real_name\": \"Vincent Parker\", \"display_name\": \"Vincent Parker\", \"email\": \"vincent.parker@harmonygames.co\"}, \"time\": \"2025-09-30T23:20:00Z\", \"permalink\": \"https://harmonygamesgroup.slack.com/archives/C08R27X0EAH/p1759274400792657\"}, {\"ts\": \"1759266600.265963\", \"type\": \"message\", \"text\": \"regression matrix green on #135 and #50 from my side :+1:\", \"channel\": \"C08R27X0EAH\", \"user\": \"EMPLOYEE_0026_SLACK_ID\", \"thread_ts\": \"1759263900.484190\", \"channel_info\": {\"id\": \"C08R2

### 37 gdocs_get_document_text err=None
INPUT: {"documentId": "f_5e40215b7d4d24b0455412"}
RESULT(1215): {"result":"{\"documentId\": \"f_5e40215b7d4d24b0455412\", \"title\": \"Update-path run - iOS #50 / Android #135.docx\", \"name\": \"Update-path run - iOS #50 / Android #135.docx\", \"revisionId\": \"c2c99e34c7c3\", \"createdTime\": \"2025-09-30T22:05:00Z\", \"modifiedTime\": \"2025-09-30T22:35:00Z\", \"text\": \"Update-path run - iOS #50 / Android #135\\nBrian Foster, Sep 30 2025 (after the fresh-install pass)\\n\\nUpdate rows from the QA regression runbook. Fresh-install rows are in my regression matrix sheet.\\n\\nDevice | OS | Installed from store | Updated to | Result | Notes\\niPhone 13 | iOS 18.6 | N-1 | iOS Submission #50 | FAIL | After the update the save came back at level 1 with 500 coins; the account was on level 212 with 18,400 coins before. Relaunching didn't bring it back.\\niPhone 13 | iOS 18.6 | N-2 | iOS Submission #50 | Pass | Level, coins and unlocks kept.\\nPixel 6 | Android 14 | N-1 | Android Submission #135 | Pass | Level, coins and unlocks kept.\\nPixel 6 | Android 14 | N-2 | Android Submission #135 | Pass | Level, coins and unlocks kept.\\n\\nRepro for the iOS row: install the N-1 build from the App Store, play past level 200, install TestFlight 50 over it, 

### 38 gdrive_list_sheets err=None
INPUT: {"spreadsheetId": "f_b91db376f65604b8602657"}
RESULT(216): {"result":"{\"sheets\": [{\"spreadsheetId\": \"f_b91db376f65604b8602657\", \"sheetId\": 0, \"title\": \"Matrix\", \"index\": 0, \"sheetType\": \"GRID\", \"gridProperties\": {\"rowCount\": 20, \"columnCount\": 6}}]}"}

### 39 gdrive_read_sheet_range err=None
INPUT: {"spreadsheetId": "f_b91db376f65604b8602657"}
RESULT(548): {"result":"{\"spreadsheetId\": \"f_b91db376f65604b8602657\", \"sheetIndex\": 0, \"mimeType\": \"text/csv\", \"text\": \"Area,Fresh install - iOS #50 (iPhone 13),Fresh install - Android #135 (Pixel 6),Update from N-1,Update from N-2,Notes\\r\\nSplash / asset load,Pass,Pass,,,throttled 3G + cleared cache\\r\\nSave / progression,Pass,Pass,,,\\r\\nLives & scheduler,Pass,Pass,,,\\\"clock moved +3h, lives refilled\\\"\\r\\nQuests populate / reset,Pass,Pass,,,\\r\\nPurchase / restore,Pass,Pass,,,\\\"sandbox, grants checked client side\\\"\\r\\n\"}"}

### 40 linear_list_issues err=None
INPUT: {"query": "save progress level 1 update reset coins", "limit": 15, "createdAt": "2025-09-15", "fields": ["identifier", "title", "status", "team", "createdAt"]}
RESULT(4084): {"result":"{\"issues\": [{\"id\": \"ZOM-544\", \"identifier\": \"ZOM-544\", \"title\": \"Implement Google Apple Login\", \"createdAt\": \"2025-09-15T15:28:14Z\", \"status\": \"In Progress\", \"statusType\": \"started\", \"team\": \"Zombie Match 3D\", \"teamId\": \"team_ZOM\"}, {\"id\": \"ZOM-580\", \"identifier\": \"ZOM-580\", \"title\": \"Daily gift popup shows twice after the midnight reset\", \"createdAt\": \"2025-09-30T22:50:00Z\", \"status\": \"Todo\", \"statusType\": \"unstarted\", \"team\": \"Zombie Match 3D\", \"teamId\": \"team_ZOM\"}, {\"id\": \"DES-313\", \"identifier\": \"DES-313\", \"title\": \"ZM level 214 can't be completed\", \"createdAt\": \"2025-09-29T15:20:00Z\", \"status\": \"Todo\", \"statusType\": \"unstarted\", \"team\": \"Design\", \"teamId\": \"team_DES\"}, {\"id\": \"ZOM-556\", \"identifier\": \"ZOM-556\", \"title\": \"When the daily gift is skipped, it doesn't reset to 0.\", \"createdAt\": \"2025-09-22T14:44:06Z\", \"status\": \"Todo\", \"statusType\": \"unstarted\", \"team\": \"Zombie Match 3D\", \"teamId\": \"team_ZOM\"}, {\"id\": \"ZOM-577\", \"identifier\": \"ZOM-577\", \"title\": \"level_fail event is missing the booster_used param\", \"createdAt\": 

### 41 linear_list_issues err=None
INPUT: {"team": "ZOM", "updatedAt": "2025-09-22T00:00:00Z", "limit": 100, "maxDescriptionChars": 1500, "fields": ["identifier", "title", "description", "status", "labels", "createdAt", "completedAt", "createdBy", "stateHistory"]}
RESULT(1278): Error: result (54,505 characters) exceeds maximum allowed tokens. Output has been saved to /home/agent/.claude/projects/-app/cc259042-d28b-483a-8dd7-0ebd1893cf60/tool-results/mcp-hg-linear_list_issues-1793890985713.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/agent/.claude/projects/-app/cc259042-d28b-483a-8dd7-0ebd1893cf60/tool-results/mcp-hg-linear_list_issues-1793890985713.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***
- If after a few attempts you cannot read the file (file not found, lines too long for Read's offset/limit, no shell access), STOP retrying. Summarize what you were able to 

### 42 Bash err=False
INPUT: {"command": "cd /home/agent/.claude/projects/-app/cc259042-d28b-483a-8dd7-0ebd1893cf60/tool-results/; python3 -c \"\nimport json\nd=json.loads(json.load(open('mcp-hg-linear_list_issues-1793890985713.txt'))['result'])\nprint(len(d['issues']),d.get('hasNextPage'))\nfor i in d['issues']:\n  print('=====',i['identifier'],'|',i['status'],'|',i.get('completedAt'),'|',i['labels'],'|',i.get('createdBy'),'|',i['title'])\n  print((i.get('description') or '').strip())\n  sh=i.get('stateHistory')\n  if sh: print('HIST',sh[-3:])\n\" > /app/recent.txt; wc -c /app/recent.txt; head -c 25000 /app/recent.txt"}
RESULT(25027): 34574 /app/recent.txt
69 False
===== ZOM-580 | Todo | None | ['Bug'] | brian.foster@harmonygames.co | Daily gift popup shows twice after the midnight reset
After the daily reset the daily gift popup opens, I claim it, and it opens again empty right after. Android #135.
===== ZOM-568 | Todo | None | ['Bug'] | vincent.parker@harmonygames.co | Settings language list jumps back to the top while scrolling
Settings > Language: the list jumps back to the top after every scroll on Android #133. You can still pick a language, it just takes a few tries.
===== ZOM-579 | Todo | None | ['VFX'] | vincent.parker@harmonygames.co | Boss arena hit VFX plays behind the board on iPad
On iPad (iOS #50) the boss hit VFX renders behind the board, so you only see it at the edges. Damage numbers are fine.
===== ZOM-468 | Todo | None | ['Bug'] | vincent.parker@harmonygames.co | Low-end devices rendering issues
* Sometimes, the boss buster item isn't fully visible.

![Screenshot_[CREDIT_CARD_NUMBER_6334]-44_232bce8c0fd071e3b7a1963a264fccd2.jpg]([URL_52782])

![Screenshot_[CREDIT_CARD_NUMBER_6333]-24_232bce8c0fd071e3b7a1963a264fccd2.jpg]([URL_52781])

* Sometimes, the objects cannot be rendered while opening 

### 43 Bash err=False
INPUT: {"command": "tail -c 9600 /app/recent.txt"}
RESULT(9595): ��3 seconds, randomized height
3. **Entry Effect (only once when state activates):**
   * When Infinite Lives turns on, the **heart icon could spin in**, **scale up**, or even flash once with a sound cue
   * This draws attention and makes the state change feel like a reward
4. **Banner (top left):**
   * If the Infinite Lives icon in the top-left (next to Full) is used:
     * Consider animating the **infinity loop** in the icon (it can rotate or pulse)
     * Optional: show a **faint timer bar** if lives are time-limited
===== ZOM-465 | In Progress | None | ['VFX'] | vincent.parker@harmonygames.co | Endless Mode Master VFX Ticket
* ~~Multiplier VFX at the end of level~~

You have already done the animation Marcus. No further comment on it thanks. 

## Event Animations

* ~~Idle Icon Animation~~ 

For all event icons we some need slight animations at the idle.  The idle animation should be subtle so whatever will be easier for you would be great because the image is not divided into different parts. But maybe the infinite symbol on the shirt of zombie can loop. 

![icn - endless horde.png]([URL_52777])

[[CREDIT_CARD_NUMBER_6331].3085654.mp4]([URL_52776])

* ~~Progress bar animati

### 44 slack_read_channel err=None
INPUT: {"channel_id": "C08R27X0EAH", "oldest": "1758500000", "limit": 100, "response_format": "concise"}
RESULT(22409): {"result":"{\"ok\": true, \"messages\": [{\"ts\": \"1759274400.792657\", \"type\": \"message\", \"text\": \"checked the fixes since the sep 22 gate on #135 / #50: ZOM-503 giving lives ok, ZOM-506 zombie lane text ok, ZOM-557 consecutive login ok, ZOM-561 low-end black surfaces ok, ZOM-434 no flying items after backgrounding during load, ZOM-558 weekly board says Level: now. rest tomorrow\", \"channel\": \"C08R27X0EAH\", \"user\": \"EMPLOYEE_0012_SLACK_ID\"}, {\"ts\": \"1759263900.484190\", \"type\": \"message\", \"text\": \"ZM store candidates are up: Android Submission #135 and iOS Submission #50, both from main. <@EMPLOYEE_0012_SLACK_ID> QA gate before friday's go/no-go please, details on ZOM-570\", \"channel\": \"C08R27X0EAH\", \"user\": \"EMPLOYEE_0025_SLACK_ID\", \"thread_ts\": \"1759263900.484190\"}, {\"ts\": \"1759249488.495439\", \"type\": \"message\", \"text\": \"i think we should squeeze in the fix for that issue if it's an easy fix. annoying and players can see that for 10 times in a day if they make it that far.\", \"channel\": \"C08R27X0EAH\", \"user\": \"EMPLOYEE_0012_SLACK_ID\", \"thread_ts\": \"1759249488.495439\"}, {\"ts\": \"1759140300.935009\", \"type\": \"messag

### 45 slack_read_thread err=None
INPUT: {"channel_id": "C08R27X0EAH", "message_ts": "1759249488.495439"}
RESULT(5839): {"result":"{\"ok\": true, \"messages\": [{\"ts\": \"1759249488.495439\", \"type\": \"message\", \"text\": \"i think we should squeeze in the fix for that issue if it's an easy fix. annoying and players can see that for 10 times in a day if they make it that far.\", \"channel\": \"C08R27X0EAH\", \"user\": \"EMPLOYEE_0012_SLACK_ID\", \"thread_ts\": \"1759249488.495439\", \"reply_count\": 4, \"reply_users_count\": 3, \"latest_reply\": \"1759254162.721499\", \"reactions\": [{\"count\": 1, \"name\": \"100\", \"users\": [\"EMPLOYEE_0002_SLACK_ID\"]}], \"files\": [{\"created\": 1759249152, \"filetype\": \"png\", \"id\": \"F09J3AU9YQL\", \"is_public\": false, \"mimetype\": \"image/png\", \"name\": \"image.png\", \"permalink\": \"https://harmonygamesgroup.slack.com/files/EMPLOYEE_0038_SLACK_ID/F09J3AU9YQL/image.png\", \"size\": 63490, \"timestamp\": 1759249152, \"title\": \"image.png\", \"url_private\": \"https://files.slack.com/files-pri/T04RZ2JAMM0-F09J3AU9YQL/image.png?token=xoxb-REDACTED\", \"user\": \"EMPLOYEE_0012_SLACK_ID\"}], \"channel_info\": {\"id\": \"C08R27X0EAH\", \"name\": \"zombie-bugs\", \"is_private\": true, \"is_im\": false, \"is_mpim\": false}, \"user_profile\": {\"id\": 

### 46 slack_read_thread err=None
INPUT: {"channel_id": "C08R27X0EAH", "message_ts": "1758903616.346579"}
RESULT(6429): {"result":"{\"ok\": true, \"messages\": [{\"ts\": \"1758903616.346579\", \"type\": \"message\", \"text\": \"After I skipped the zombie lane tutorial, \\u0131 got the exception and skipping couldn\\u2019t claim the ice cream. <@EMPLOYEE_0003_SLACK_ID>   \", \"channel\": \"C08R27X0EAH\", \"user\": \"EMPLOYEE_0012_SLACK_ID\", \"thread_ts\": \"1758903616.346579\", \"reply_count\": 6, \"reply_users_count\": 2, \"latest_reply\": \"1758917074.996069\", \"reactions\": [{\"count\": 1, \"name\": \"+1\", \"users\": [\"EMPLOYEE_0003_SLACK_ID\"]}], \"files\": [{\"created\": 1758903545, \"filetype\": \"png\", \"id\": \"F09HCV1PYKU\", \"is_public\": false, \"mimetype\": \"image/png\", \"name\": \"IMG_4696.png\", \"permalink\": \"https://harmonygamesgroup.slack.com/files/EMPLOYEE_0038_SLACK_ID/F09HCV1PYKU/img_4696.png\", \"size\": 291508, \"timestamp\": 1758903545, \"title\": \"IMG_4696\", \"url_private\": \"https://files.slack.com/files-pri/T04RZ2JAMM0-F09HCV1PYKU/img_4696.png?token=xoxb-REDACTED\", \"user\": \"EMPLOYEE_0012_SLACK_ID\"}, {\"created\": 1758903545, \"filetype\": \"png\", \"id\": \"F09H9DCENA1\", \"is_public\": false, \"mimetype\": \"image/png\", \"name\": \"IMG_4695.png\", \"permal

### 47 slack_read_thread err=None
INPUT: {"channel_id": "C08R27X0EAH", "message_ts": "1758751463.920129"}
RESULT(4194): {"result":"{\"ok\": true, \"messages\": [{\"ts\": \"1758751463.920129\", \"type\": \"message\", \"text\": \"it\\u2019s a known thing that some event packs get dropped for some users occasioanlly, it happens to every game every user. It\\u2019s supposed to be a small percent but it happens - just a reminder on this\", \"channel\": \"C08R27X0EAH\", \"user\": \"EMPLOYEE_0038_SLACK_ID\", \"thread_ts\": \"1758751463.920129\", \"reply_count\": 4, \"reply_users_count\": 2, \"latest_reply\": \"1758764698.653049\", \"channel_info\": {\"id\": \"C08R27X0EAH\", \"name\": \"zombie-bugs\", \"is_private\": true, \"is_im\": false, \"is_mpim\": false}, \"user_profile\": {\"id\": \"EMPLOYEE_0038_SLACK_ID\", \"name\": \"Leonard Hayes\", \"real_name\": \"Leonard Hayes\", \"display_name\": \"Leonard Hayes\", \"email\": \"leonard.hayes@harmonygames.co\"}, \"time\": \"2025-09-24T22:04:23Z\", \"permalink\": \"https://harmonygamesgroup.slack.com/archives/C08R27X0EAH/p1758751463920129?thread_ts=1758751463.920129&cid=C08R27X0EAH\", \"latest_reply_time\": \"2025-09-25T01:44:58Z\"}, {\"ts\": \"1758751516.822929\", \"type\": \"message\", \"text\": \"the question is does it happen more often when users are in tr

### 48 linear_list_comments err=None
INPUT: {"issueId": "ZOM-567"}
RESULT(494): {"result":"{\"comments\": [{\"id\": \"cmt_zom567_1\", \"body\": \"it was the grant job on the backend, fix is in match3d-backend #36, merged\", \"attachments\": [], \"createdAt\": \"2025-09-30T18:55:00Z\", \"updatedAt\": \"2025-09-30T18:55:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_cd7849ec043ab3da\", \"name\": \"douglas@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-567\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 49 linear_list_comments err=None
INPUT: {"issueId": "ZOM-563"}
RESULT(55): {"result":"{\"comments\": [], \"hasNextPage\": false}"}

### 50 linear_list_comments err=None
INPUT: {"issueId": "ZOM-534"}
RESULT(1555): {"result":"{\"comments\": [{\"id\": \"cmt_zom534_2\", \"body\": \"Against prod with #135: quest points still stuck at 5/5 until a restart, rewards fine.\", \"attachments\": [], \"createdAt\": \"2025-09-30T21:36:00Z\", \"updatedAt\": \"2025-09-30T21:36:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-534\", \"isEdited\": false}, {\"id\": \"cmt_zom534_1\", \"body\": \"#133 / #49 against prod: completed the daily quest and stayed in the quest panel; the points stayed at 5/5 and the chest stayed locked until the app was force-quit and reopened, then it reset. No quest rewards were lost.\", \"attachments\": [], \"createdAt\": \"2025-09-29T13:10:00Z\", \"updatedAt\": \"2025-09-29T13:10:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-534\", \"isEdited\": false}, {\"id\": \"cmt_zom534_0\", \"body\": \"Prod with the #127 client: quest points still don't reset until a restart.\", \"

### 51 linear_list_comments err=None
INPUT: {"issueId": "ZOM-569"}
RESULT(489): {"result":"{\"comments\": [{\"id\": \"cmt_zom569_1\", \"body\": \"fixed on my branch, the join popup only opens one SP screen now\", \"attachments\": [], \"createdAt\": \"2025-09-30T18:02:00Z\", \"updatedAt\": \"2025-09-30T18:02:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_bdf01b53c6a92c5e\", \"name\": \"oliver.brooks@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-569\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 52 linear_list_comments err=None
INPUT: {"issueId": "ZOM-435"}
RESULT(55): {"result":"{\"comments\": [], \"hasNextPage\": false}"}

### 53 linear_list_comments err=None
INPUT: {"issueId": "ZOM-573"}
RESULT(55): {"result":"{\"comments\": [], \"hasNextPage\": false}"}

### 54 linear_list_comments err=None
INPUT: {"issueId": "ZOM-578"}
RESULT(55): {"result":"{\"comments\": [], \"hasNextPage\": false}"}

### 55 linear_list_comments err=None
INPUT: {"issueId": "ZOM-576"}
RESULT(55): {"result":"{\"comments\": [], \"hasNextPage\": false}"}

### 56 linear_get_issue err=None
INPUT: {"id": "DES-313"}
RESULT(1106): {"result":"{\"id\": \"DES-313\", \"uuid\": null, \"identifier\": \"DES-313\", \"number\": 313, \"title\": \"ZM level 214 can't be completed\", \"description\": \"Level 214 asks for 3 jars but only 2 jars ever spawn, so the goal can't be reached and the level can't be finished. Tried 4 times on Android #133. Looks like the level data, not the code.\", \"priority\": {\"value\": 2, \"name\": \"High\"}, \"estimate\": null, \"url\": \"https://linear.app/harmonygames/issue/DES-313/zm-level-214-can-t-be-completed\", \"gitBranchName\": \"vincentparker/des-313-zm-level-214-can-t-be-completed\", \"createdAt\": \"2025-09-29T15:20:00Z\", \"updatedAt\": \"2025-09-30T22:38:00Z\", \"archivedAt\": null, \"completedAt\": null, \"startedAt\": null, \"canceledAt\": null, \"dueDate\": null, \"status\": \"Todo\", \"statusType\": \"unstarted\", \"labels\": [], \"links\": [], \"attachments\": [], \"createdBy\": \"vincent.parker@harmonygames.co\", \"createdById\": \"usr_65c76e0b87aa7e9b\", \"team\": \"Design\", \"teamId\": \"team_DES\", \"timeInStatusMinutes\": 2382, \"isArchived\": false, \"stateHistory\": []}"}

### 57 linear_get_issue err=None
INPUT: {"id": "ART-793"}
RESULT(1131): {"result":"{\"id\": \"ART-793\", \"uuid\": null, \"identifier\": \"ART-793\", \"number\": 793, \"title\": \"ZM3D - boss arena background flickers on iPhone 12\", \"description\": \"The boss arena backdrop flickers between the day and the night texture every few seconds on iPhone 12 (iOS #49). Gameplay is fine, it's just distracting.\", \"priority\": {\"value\": 3, \"name\": \"Medium\"}, \"estimate\": null, \"url\": \"https://linear.app/harmonygames/issue/ART-793/zm3d-boss-arena-background-flickers-on-iphone-12\", \"gitBranchName\": \"vincentparker/art-793-zm3d-boss-arena-background-flickers-on-iphone-12\", \"createdAt\": \"2025-09-29T15:00:00Z\", \"updatedAt\": \"2025-09-30T22:34:00Z\", \"archivedAt\": null, \"completedAt\": null, \"startedAt\": null, \"canceledAt\": null, \"dueDate\": null, \"status\": \"Todo\", \"statusType\": \"unstarted\", \"labels\": [\"Bug\"], \"links\": [], \"attachments\": [], \"createdBy\": \"vincent.parker@harmonygames.co\", \"createdById\": \"usr_65c76e0b87aa7e9b\", \"team\": \"Art\", \"teamId\": \"team_ART\", \"timeInStatusMinutes\": 2402, \"isArchived\": false, \"stateHistory\": []}"}

### 58 linear_list_comments err=None
INPUT: {"issueId": "DES-313"}
RESULT(485): {"result":"{\"comments\": [{\"id\": \"cmt_des313_1\", \"body\": \"#135: level 214 still only spawns 2 jars, can't finish it.\", \"attachments\": [], \"createdAt\": \"2025-09-30T22:38:00Z\", \"updatedAt\": \"2025-09-30T22:38:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"DES-313\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 59 linear_list_comments err=None
INPUT: {"issueId": "ART-793"}
RESULT(495): {"result":"{\"comments\": [{\"id\": \"cmt_art793_1\", \"body\": \"#50 on the iPhone 12: the backdrop still flickers in the boss arena.\", \"attachments\": [], \"createdAt\": \"2025-09-30T22:34:00Z\", \"updatedAt\": \"2025-09-30T22:34:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ART-793\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 60 linear_list_comments err=None
INPUT: {"issueId": "ZOM-559"}
RESULT(1230): {"result":"{\"comments\": [{\"id\": \"cmt_zom559_1\", \"body\": \"Android Submission #133 on a Samsung S22: home out mid-level, come back, then finish the level. SFX were silent for the rest of the level and the victory screen froze with the reward panel half drawn for about 20 seconds; only a force-quit got me out, the level reward was there after relaunch.\", \"attachments\": [], \"createdAt\": \"2025-09-29T15:20:00Z\", \"updatedAt\": \"2025-09-29T15:20:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_fc22d5941b2aeb5c\", \"name\": \"brian.foster@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-559\", \"isEdited\": false}, {\"id\": \"cmt_zom559_0\", \"body\": \"Tried on #127 on a Pixel 6: homed out and back three times, sound and the victory screen were fine. Can't reproduce here, need a Samsung.\", \"attachments\": [], \"createdAt\": \"2025-09-22T16:30:00Z\", \"updatedAt\": \"2025-09-22T16:30:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-559\", \"isEdited\": fals

### 61 linear_list_comments err=None
INPUT: {"issueId": "ZOM-546"}
RESULT(1014): {"result":"{\"comments\": [{\"id\": \"cmt_zom546_1\", \"body\": \"#135 / #50 endless: the board drains again after about 8 refills, down to 5 items with no match possible, the run can't go on.\", \"attachments\": [], \"createdAt\": \"2025-09-30T21:48:00Z\", \"updatedAt\": \"2025-09-30T21:48:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-546\", \"isEdited\": false}, {\"id\": \"cmt_zom546_0\", \"body\": \"#127: the refill still drains the board in endless after a few refills, same as before.\", \"attachments\": [], \"createdAt\": \"2025-09-22T13:10:00Z\", \"updatedAt\": \"2025-09-22T13:10:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-546\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 62 linear_list_comments err=None
INPUT: {"issueId": "ZOM-554"}
RESULT(1170): {"result":"{\"comments\": [{\"id\": \"cmt_zom554_2\", \"body\": \"#50: quitting mid tornado still leaves the next level's objects floating, had to force-quit again.\", \"attachments\": [], \"createdAt\": \"2025-09-30T21:54:00Z\", \"updatedAt\": \"2025-09-30T21:54:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-554\", \"isEdited\": false}, {\"id\": \"cmt_zom554_1\", \"body\": \"Android Submission #133: quit level 41 with the tornado booster mid-spin. On the next level the objects hung above their cells and drifted; matches didn't register on the floating pieces and the level couldn't be played until I force-quit and relaunched. Same on iOS #49.\", \"attachments\": [], \"createdAt\": \"2025-09-29T13:35:00Z\", \"updatedAt\": \"2025-09-29T13:35:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-554\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 63 linear_list_comments err=None
INPUT: {"issueId": "ZOM-564"}
RESULT(641): {"result":"{\"comments\": [{\"id\": \"cmt_zom564_1\", \"body\": \"Checked on iOS #50 and Android #135: finished the tutorial, went back into level 6, no free label on the boosters and the inventory count stayed the same when I didn't use one. Used one and it took one, as it should.\", \"attachments\": [], \"createdAt\": \"2025-09-30T21:20:00Z\", \"updatedAt\": \"2025-09-30T21:20:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_fc22d5941b2aeb5c\", \"name\": \"brian.foster@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-564\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 64 linear_list_comments err=None
INPUT: {"issueId": "ZOM-483"}
RESULT(603): {"result":"{\"comments\": [{\"id\": \"cmt_zom483_1\", \"body\": \"#135 fresh install: killed the app with 50 min of the new-install infinite lives left, after relaunch the banner says 30 min and it counts down from there. The 20 min are gone.\", \"attachments\": [], \"createdAt\": \"2025-09-30T22:14:00Z\", \"updatedAt\": \"2025-09-30T22:14:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-483\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 65 linear_list_comments err=None
INPUT: {"issueId": "ZOM-560"}
RESULT(545): {"result":"{\"comments\": [{\"id\": \"cmt_zom560_1\", \"body\": \"#135 sandbox account: bought the abandoned pack, coins and boosters came in, the win streak freezer time still didn't.\", \"attachments\": [], \"createdAt\": \"2025-09-30T22:06:00Z\", \"updatedAt\": \"2025-09-30T22:06:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-560\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 66 linear_list_comments err=None
INPUT: {"issueId": "ZOM-556"}
RESULT(1049): {"result":"{\"comments\": [{\"id\": \"cmt_zom556_2\", \"body\": \"#135: a skipped day still doesn't reset the daily gift.\", \"attachments\": [], \"createdAt\": \"2025-09-30T22:00:00Z\", \"updatedAt\": \"2025-09-30T22:00:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-556\", \"isEdited\": false}, {\"id\": \"cmt_zom556_1\", \"body\": \"#133 / #49: claimed day 3, then skipped a day. On the next launch the panel still highlighted day 4 instead of going back to day 1, and claiming it moved the streak on instead of restarting it.\", \"attachments\": [], \"createdAt\": \"2025-09-29T14:05:00Z\", \"updatedAt\": \"2025-09-29T14:05:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-556\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 67 linear_list_comments err=None
INPUT: {"issueId": "ZOM-505"}
RESULT(1191): {"result":"{\"comments\": [{\"id\": \"cmt_zom505_2\", \"body\": \"#135: tutorial panel still reopens on every level 19 retry, level is playable after tapping through.\", \"attachments\": [], \"createdAt\": \"2025-09-30T21:18:00Z\", \"updatedAt\": \"2025-09-30T21:18:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-505\", \"isEdited\": false}, {\"id\": \"cmt_zom505_1\", \"body\": \"Android Submission #133: failed level 19 three times on purpose. Each retry reopened the tutorial panel over the pre-level screen; after tapping through all four steps the level started and could be played and finished. Same on a second install, never a case where the level couldn't start.\", \"attachments\": [], \"createdAt\": \"2025-09-29T12:40:00Z\", \"updatedAt\": \"2025-09-29T12:40:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-505\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 68 linear_list_comments err=None
INPUT: {"issueId": "ZOM-580"}
RESULT(55): {"result":"{\"comments\": [], \"hasNextPage\": false}"}

### 69 linear_list_comments err=None
INPUT: {"issueId": "ZOM-571"}
RESULT(55): {"result":"{\"comments\": [], \"hasNextPage\": false}"}

### 70 linear_list_comments err=None
INPUT: {"issueId": "ZOM-572"}
RESULT(55): {"result":"{\"comments\": [], \"hasNextPage\": false}"}

### 71 linear_list_comments err=None
INPUT: {"issueId": "ZOM-574"}
RESULT(55): {"result":"{\"comments\": [], \"hasNextPage\": false}"}

### 72 linear_list_comments err=None
INPUT: {"issueId": "ZOM-568"}
RESULT(495): {"result":"{\"comments\": [{\"id\": \"cmt_zom568_1\", \"body\": \"#135: the language list still jumps back to the top while scrolling.\", \"attachments\": [], \"createdAt\": \"2025-09-30T22:30:00Z\", \"updatedAt\": \"2025-09-30T22:30:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-568\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 73 linear_list_comments err=None
INPUT: {"issueId": "ZOM-579"}
RESULT(55): {"result":"{\"comments\": [], \"hasNextPage\": false}"}

### 74 linear_list_comments err=None
INPUT: {"issueId": "ZOM-562"}
RESULT(504): {"result":"{\"comments\": [{\"id\": \"cmt_zom562_1\", \"body\": \"#135: still happens, saw single items after 2 of 8 refills in the boss arena.\", \"attachments\": [], \"createdAt\": \"2025-09-30T22:18:00Z\", \"updatedAt\": \"2025-09-30T22:18:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-562\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 75 linear_list_comments err=None
INPUT: {"issueId": "ZOM-520"}
RESULT(957): {"result":"{\"comments\": [{\"id\": \"cmt_zom520_1\", \"body\": \"#135, level 21: the first loss still doesn't reset the win streak, the counter stays at 3.\", \"attachments\": [], \"createdAt\": \"2025-09-30T21:30:00Z\", \"updatedAt\": \"2025-09-30T21:30:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-520\", \"isEdited\": false}, {\"id\": \"cmt_zom520_0\", \"body\": \"#127, level 21: the first loss still doesn't reset the win streak.\", \"attachments\": [], \"createdAt\": \"2025-09-22T13:20:00Z\", \"updatedAt\": \"2025-09-22T13:20:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-520\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 76 linear_list_comments err=None
INPUT: {"issueId": "ZOM-535"}
RESULT(960): {"result":"{\"comments\": [{\"id\": \"cmt_zom535_1\", \"body\": \"#135: fast matching still sends items at a zombie that just died, same as Brian found on #133.\", \"attachments\": [], \"createdAt\": \"2025-09-30T21:42:00Z\", \"updatedAt\": \"2025-09-30T21:42:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-535\", \"isEdited\": false}, {\"id\": \"cmt_zom535_0\", \"body\": \"#127: fast matching still sends items at a zombie that just died.\", \"attachments\": [], \"createdAt\": \"2025-09-22T14:10:00Z\", \"updatedAt\": \"2025-09-22T14:10:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-535\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 77 linear_list_comments err=None
INPUT: {"issueId": "ZOM-517"}
RESULT(987): {"result":"{\"comments\": [{\"id\": \"cmt_zom517_1\", \"body\": \"Can't reproduce on #135 or #50 any more: the monster kept its enrage through 6 refills in endless, 4 runs on each.\", \"attachments\": [], \"createdAt\": \"2025-09-30T21:24:00Z\", \"updatedAt\": \"2025-09-30T21:24:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-517\", \"isEdited\": false}, {\"id\": \"cmt_zom517_0\", \"body\": \"#127 endless: the monster still drops its enrage during the item refill.\", \"attachments\": [], \"createdAt\": \"2025-09-22T14:25:00Z\", \"updatedAt\": \"2025-09-22T14:25:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-517\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 78 linear_list_comments err=None
INPUT: {"issueId": "ZOM-429"}
RESULT(1075): {"result":"{\"comments\": [{\"id\": \"cmt_zom429_1\", \"body\": \"Couldn't reproduce on #135 or #50: let the weekly leaderboard end with the app open, the new one started and the rewards were claimable without killing the app, 3 tries on each.\", \"attachments\": [], \"createdAt\": \"2025-09-30T20:48:00Z\", \"updatedAt\": \"2025-09-30T20:48:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-429\", \"isEdited\": false}, {\"id\": \"cmt_zom429_0\", \"body\": \"#40: weekly leaderboard ended with the app open, the new one didn't start until I killed the app.\", \"attachments\": [], \"createdAt\": \"2025-09-22T13:40:00Z\", \"updatedAt\": \"2025-09-22T13:40:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-429\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 79 linear_list_comments err=None
INPUT: {"issueId": "ZOM-481"}
RESULT(1071): {"result":"{\"comments\": [{\"id\": \"cmt_zom481_2\", \"body\": \"#135: the health bar still hangs around for a second after the death animation. Level finishes.\", \"attachments\": [], \"createdAt\": \"2025-09-30T22:10:00Z\", \"updatedAt\": \"2025-09-30T22:10:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-481\", \"isEdited\": false}, {\"id\": \"cmt_zom481_1\", \"body\": \"At 120 CPM on #133 / #49 the health bar stayed about a second after the death animation, then disappeared. Nothing else was affected, the board cleared and the level finished.\", \"attachments\": [], \"createdAt\": \"2025-09-29T11:30:00Z\", \"updatedAt\": \"2025-09-29T11:30:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-481\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 80 linear_list_comments err=None
INPUT: {"issueId": "ZOM-504"}
RESULT(1065): {"result":"{\"comments\": [{\"id\": \"cmt_zom504_2\", \"body\": \"#50: matched item still lingers on its old cell for a refill in endless horde, the cell still works.\", \"attachments\": [], \"createdAt\": \"2025-09-30T21:12:00Z\", \"updatedAt\": \"2025-09-30T21:12:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-504\", \"isEdited\": false}, {\"id\": \"cmt_zom504_1\", \"body\": \"Endless horde on #133 / #49: a matched item stayed drawn on its old cell for two refills before disappearing; the cell still accepted matches and no input was lost.\", \"attachments\": [], \"createdAt\": \"2025-09-29T11:55:00Z\", \"updatedAt\": \"2025-09-29T11:55:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-504\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 81 linear_list_comments err=None
INPUT: {"issueId": "ZOM-458"}
RESULT(575): {"result":"{\"comments\": [{\"id\": \"cmt_zom458_1\", \"body\": \"Still there on #135 / #50: quit an algo level without passing and the home screen plays the level-pass animation, same as Brian found on #133 / #49.\", \"attachments\": [], \"createdAt\": \"2025-09-30T21:06:00Z\", \"updatedAt\": \"2025-09-30T21:06:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-458\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 82 linear_list_comments err=None
INPUT: {"issueId": "ZOM-443"}
RESULT(1058): {"result":"{\"comments\": [{\"id\": \"cmt_zom443_2\", \"body\": \"#135: same column pattern on streak bonus levels, no effect on play.\", \"attachments\": [], \"createdAt\": \"2025-09-30T21:00:00Z\", \"updatedAt\": \"2025-09-30T21:00:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-443\", \"isEdited\": false}, {\"id\": \"cmt_zom443_1\", \"body\": \"On a win-streak bonus level (#133 / #49) the removed items came from the same three columns on four streaks in a row, while an off-streak level removed a mixed set. Play continued normally.\", \"attachments\": [], \"createdAt\": \"2025-09-29T10:45:00Z\", \"updatedAt\": \"2025-09-29T10:45:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-443\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 83 linear_list_comments err=None
INPUT: {"issueId": "ZOM-438"}
RESULT(1046): {"result":"{\"comments\": [{\"id\": \"cmt_zom438_2\", \"body\": \"#135: C_0120 still ends with 11-13 zombies, level completes.\", \"attachments\": [], \"createdAt\": \"2025-09-30T20:54:00Z\", \"updatedAt\": \"2025-09-30T20:54:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-438\", \"isEdited\": false}, {\"id\": \"cmt_zom438_1\", \"body\": \"Ran C_0120 five times on Android #133 / iOS #49. Monster count at level end was 12, 13, 11, 14, 12; the missing zombies never appeared, but the level still completed normally every run.\", \"attachments\": [], \"createdAt\": \"2025-09-29T10:20:00Z\", \"updatedAt\": \"2025-09-29T10:20:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-438\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 84 linear_list_comments err=None
INPUT: {"issueId": "ZOM-468"}
RESULT(1101): {"result":"{\"comments\": [{\"id\": \"cmt_zom468_2\", \"body\": \"#135 low-end: boss buster still half missing, pack slots fine this time after one reopen.\", \"attachments\": [], \"createdAt\": \"2025-09-30T22:26:00Z\", \"updatedAt\": \"2025-09-30T22:26:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_fc22d5941b2aeb5c\", \"name\": \"brian.foster@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-468\", \"isEdited\": false}, {\"id\": \"cmt_zom468_1\", \"body\": \"Android Submission #133, same low-end device: boss buster rendered with half its body missing; opening a 3-card pack showed two empty card slots until the pack was closed and reopened. Gameplay and claims were fine.\", \"attachments\": [], \"createdAt\": \"2025-09-29T09:40:00Z\", \"updatedAt\": \"2025-09-29T09:40:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_fc22d5941b2aeb5c\", \"name\": \"brian.foster@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-468\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 85 linear_list_comments err=None
INPUT: {"issueId": "ZOM-449"}
RESULT(1238): {"result":"{\"comments\": [{\"id\": \"cmt_zom449_2\", \"body\": \"Android #135 on the same low-end device: cold start into level 3 froze again, taps did nothing until I force-quit.\", \"attachments\": [], \"createdAt\": \"2025-09-30T22:20:00Z\", \"updatedAt\": \"2025-09-30T22:20:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_fc22d5941b2aeb5c\", \"name\": \"brian.foster@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-449\", \"isEdited\": false}, {\"id\": \"cmt_zom449_1\", \"body\": \"Android Submission #133 on a low-end Android device: cold start into level 3, the tutorial highlight drew over the loading screen before the board appeared and the device stopped responding to taps for about 40 seconds; force-quit and relaunch got past it. MF11 microwave and MF12 controller still render with missing surfaces.\", \"attachments\": [], \"createdAt\": \"2025-09-29T09:15:00Z\", \"updatedAt\": \"2025-09-29T09:15:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_fc22d5941b2aeb5c\", \"name\": \"brian.foster@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-449\", \"isEdited

### 86 linear_list_comments err=None
INPUT: {"issueId": "ZOM-427"}
RESULT(517): {"result":"{\"comments\": [{\"id\": \"cmt_zom427_1\", \"body\": \"Android #135: launcher icon is still zoomed in, the zombie's head is cut off at the edges.\", \"attachments\": [], \"createdAt\": \"2025-09-30T20:42:00Z\", \"updatedAt\": \"2025-09-30T20:42:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-427\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 87 linear_list_comments err=None
INPUT: {"issueId": "ZOM-348"}
RESULT(1252): {"result":"{\"comments\": [{\"id\": \"cmt_zom348_2\", \"body\": \"Same on #135: catapult offer still shows -25% against the 100-gem list price, the other ribbons are still missing. Purchase goes through at the shown price.\", \"attachments\": [], \"createdAt\": \"2025-09-30T20:36:00Z\", \"updatedAt\": \"2025-09-30T20:36:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-348\", \"isEdited\": false}, {\"id\": \"cmt_zom348_1\", \"body\": \"Tested on Android Submission #133 / iOS #49: the 1000-coin common pack showed no discount ribbon, the 80-bone pack showed none either, and the catapult offer showed -25% against a 100-gem list price. Tapping buy opened the store sheet with the price that was shown and the purchase went through.\", \"attachments\": [], \"createdAt\": \"2025-09-29T09:50:00Z\", \"updatedAt\": \"2025-09-29T09:50:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-348

### 88 linear_list_comments err=None
INPUT: {"issueId": "ZOM-237"}
RESULT(1214): {"result":"{\"comments\": [{\"id\": \"cmt_zom237_2\", \"body\": \"#135 / #50: the NEW banner still replays on the second card and the SFX still fires on the wrong cards. Claims fine.\", \"attachments\": [], \"createdAt\": \"2025-09-30T20:30:00Z\", \"updatedAt\": \"2025-09-30T20:30:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-237\", \"isEdited\": false}, {\"id\": \"cmt_zom237_1\", \"body\": \"Tested on Android Submission #133 / iOS #49: opened a 10-card pack from the shop. On the second card the red NEW banner was already visible when the card flipped and then replayed its pop-in; the banner SFX fired on the 4th and 7th cards where no banner was shown. No effect on claiming the cards.\", \"attachments\": [], \"createdAt\": \"2025-09-29T09:05:00Z\", \"updatedAt\": \"2025-09-29T09:05:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-237\", \"isEdited\": false}], \"hasNextPa

### 89 linear_list_comments err=None
INPUT: {"issueId": "ZOM-477"}
RESULT(636): {"result":"{\"comments\": [{\"id\": \"cmt_zom477_1\", \"body\": \"Still want the poison kill cam sped up, it\\u2019s a bad experience. But it\\u2019s the kill cam doing what we built it to do, so this is a tuning ask for after the push, not a bug. No call for the store gates.\", \"attachments\": [], \"createdAt\": \"2025-09-24T09:20:00Z\", \"updatedAt\": \"2025-09-24T09:20:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_63fffeb4fab5233e\", \"name\": \"leonard.hayes@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-477\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 90 linear_list_comments err=None
INPUT: {"issueId": "ZOM-555"}
RESULT(497): {"result":"{\"comments\": [{\"id\": \"cmt_zom555_1\", \"body\": \"switched it to the fade out when no cards are given, like Vincent asked\", \"attachments\": [], \"createdAt\": \"2025-09-23T19:00:00Z\", \"updatedAt\": \"2025-09-23T19:00:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_bdf01b53c6a92c5e\", \"name\": \"oliver.brooks@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-555\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 91 linear_list_comments err=None
INPUT: {"issueId": "ZOM-536"}
RESULT(508): {"result":"{\"comments\": [{\"id\": \"cmt_zom536_1\", \"body\": \"updated the trampoline icon and the model, it's in #471 with the home screen fixes\", \"attachments\": [], \"createdAt\": \"2025-09-30T12:35:00Z\", \"updatedAt\": \"2025-09-30T12:35:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_caafeec2804b3a67\", \"name\": \"samuel.turner@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-536\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 92 linear_list_comments err=None
INPUT: {"issueId": "ZOM-473"}
RESULT(495): {"result":"{\"comments\": [{\"id\": \"cmt_zom473_0\", \"body\": \"#127: the endless end screen can still be tapped away before the x2.\", \"attachments\": [], \"createdAt\": \"2025-09-22T13:30:00Z\", \"updatedAt\": \"2025-09-22T13:30:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-473\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 93 linear_list_comments err=None
INPUT: {"issueId": "ZOM-419"}
RESULT(55): {"result":"{\"comments\": [], \"hasNextPage\": false}"}

### 94 linear_list_comments err=None
INPUT: {"issueId": "ZOM-506"}
RESULT(55): {"result":"{\"comments\": [], \"hasNextPage\": false}"}

### 95 linear_list_comments err=None
INPUT: {"issueId": "ZOM-503"}
RESULT(500): {"result":"{\"comments\": [{\"id\": \"cmt_zom503_0\", \"body\": \"#127: giving lives in teams updates right away now, no tab change needed.\", \"attachments\": [], \"createdAt\": \"2025-09-22T14:40:00Z\", \"updatedAt\": \"2025-09-22T14:40:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_65c76e0b87aa7e9b\", \"name\": \"vincent.parker@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-503\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 96 linear_list_comments err=None
INPUT: {"issueId": "ZOM-557"}
RESULT(504): {"result":"{\"comments\": [{\"id\": \"cmt_zom557_1\", \"body\": \"pushed the fix for the ConsecutiveLogins json mapping, it was always reading 0\", \"attachments\": [], \"createdAt\": \"2025-09-22T18:40:00Z\", \"updatedAt\": \"2025-09-22T18:40:00Z\", \"parentId\": null, \"resolvedAt\": null, \"quotedText\": null, \"author\": {\"id\": \"usr_bdf01b53c6a92c5e\", \"name\": \"oliver.brooks@harmonygames.co\"}, \"onBehalfOf\": null, \"issueId\": \"ZOM-557\", \"isEdited\": false}], \"hasNextPage\": false}"}

### 97 linear_list_comments err=None
INPUT: {"issueId": "ZOM-561"}
RESULT(55): {"result":"{\"comments\": [], \"hasNextPage\": false}"}

### 98 github_search_repositories err=None
INPUT: {"query": "match3d"}
RESULT(3013): {"result":"{\"total_count\": 4, \"incomplete_results\": false, \"unpopulated_fields\": [], \"items\": [{\"id\": \"harmonygames-Games/match3d\", \"name\": \"match3d\", \"full_name\": \"harmonygames-Games/match3d\", \"owner\": {\"login\": \"harmonygames-Games\", \"type\": \"Organization\"}, \"private\": true, \"default_branch\": \"main\", \"topics\": [], \"visibility\": \"private\", \"archived\": false, \"disabled\": false, \"is_template\": false, \"fork\": false, \"size\": 0, \"stargazers_count\": 0, \"watchers_count\": 0, \"forks_count\": 0, \"open_issues_count\": 2, \"created_at\": null, \"updated_at\": \"2025-10-01T05:44:17Z\", \"pushed_at\": \"2025-10-01T05:44:17Z\", \"html_url\": \"https://github.com/harmonygames-Games/match3d\", \"url\": \"https://api.github.com/repos/harmonygames-Games/match3d\"}, {\"id\": \"harmonygames-Games/match3d-backend\", \"name\": \"match3d-backend\", \"full_name\": \"harmonygames-Games/match3d-backend\", \"owner\": {\"login\": \"harmonygames-Games\", \"type\": \"Organization\"}, \"private\": true, \"default_branch\": \"main\", \"topics\": [], \"visibility\": \"private\", \"archived\": false, \"disabled\": false, \"is_template\": false, \"fork\": fals

### 99 github_list_pull_requests err=None
INPUT: {"owner": "harmonygames-Games", "repo": "match3d", "state": "all", "sort": "updated", "direction": "desc", "perPage": 50, "fields": ["number", "title", "state", "merged", "merged_at", "head", "created_at"]}
RESULT(18049): {"result":"{\"total_count\": 477, \"page\": 1, \"perPage\": 50, \"has_more\": true, \"truncated\": false, \"items\": [{\"number\": 477, \"title\": \"Collect And Win Analytics and title change\", \"state\": \"open\", \"merged\": false, \"head\": {\"ref\": \"[PERSON_NAME_0067]/collectAndWinAnalytics\", \"sha\": \"0dfd4a414f34166043d3a01b6217e78108701dce\", \"repo\": {\"full_name\": \"harmonygames-Games/match3d\"}}, \"created_at\": \"2025-09-30T22:26:30Z\", \"merged_at\": null}, {\"number\": 476, \"title\": \"Vision bot\", \"state\": \"open\", \"merged\": false, \"head\": {\"ref\": \"Blake/visionBot\", \"sha\": \"077e1ccfa22de4346c16360441bd35badaaeea46\", \"repo\": {\"full_name\": \"harmonygames-Games/match3d\"}}, \"created_at\": \"2025-09-30T18:54:32Z\", \"merged_at\": null}, {\"number\": 475, \"title\": \"[PERSON_NAME_0029]/animated icons\", \"state\": \"closed\", \"merged\": true, \"head\": {\"ref\": \"[PERSON_NAME_0029]/AnimatedIcons\", \"sha\": \"5dbf89b38aea5f709af274d351d7a61579d731b6\", \"repo\": {\"full_name\": \"harmonygames-Games/match3d\"}}, \"created_at\": \"2025-09-30T15:59:05Z\", \"merged_at\": \"2025-09-30T16:09:15Z\"}, {\"number\": 472, \"title\": \"Implement Win&Col

### 100 github_list_pull_requests err=None
INPUT: {"owner": "harmonygames-Games", "repo": "match3d-backend", "state": "all", "sort": "updated", "direction": "desc", "perPage": 20, "fields": ["number", "title", "state", "merged", "merged_at", "body", "created_at"]}
RESULT(17276): {"result":"{\"total_count\": 36, \"page\": 1, \"perPage\": 20, \"has_more\": true, \"truncated\": false, \"items\": [{\"number\": 36, \"title\": \"Fix Zombie Lane chest grant after the daily reset\", \"state\": \"closed\", \"merged\": true, \"body\": \"Chest claims were acknowledged but the grant job skipped them when the claim landed after the daily reset. ZOM-567\", \"created_at\": \"2025-09-30T18:30:00Z\", \"merged_at\": \"2025-09-30T18:50:00Z\"}, {\"number\": 35, \"title\": \"Other players profile\", \"state\": \"closed\", \"merged\": false, \"body\": \"\\n\\n<!-- This is an auto-generated comment: release notes by coderabbit.ai -->\\n\\n## Summary by CodeRabbit\\n\\n- New Features\\n  - Added GET /api/player/{player_id} to retrieve a player\\u2019s profile with inventory and key stats in a single response.\\n  - Returns clear errors for invalid IDs (400) and missing players (404).\\n\\n- Documentation\\n  - Updated API documentation to include the new endpoint, parameters, and responses.\\n  - Added an example request in the HTTP collection with authorization and sample player_id for quick testing.\\n\\n<!-- end of auto-generated comment: release notes by coderabbit.ai -->\", 

### 101 slack_search_public_and_private err=None
INPUT: {"query": "deploy", "after": "1758500000", "limit": 30}
RESULT(11792): {"result":"{\"ok\": true, \"messages\": [{\"ts\": \"1759164463.327349\", \"type\": \"message\", \"text\": \"Ok, the deployment is done, I will inform [PERSON_NAME_0120] and Blake as well\", \"channel\": \"D079SNE2TL4\", \"user\": \"EMPLOYEE_0031_SLACK_ID\", \"channel_info\": {\"id\": \"D079SNE2TL4\", \"name\": null, \"is_private\": false, \"is_im\": true, \"is_mpim\": false}, \"user_profile\": {\"id\": \"EMPLOYEE_0031_SLACK_ID\", \"name\": \"Douglas\", \"real_name\": \"Douglas\", \"display_name\": \"Douglas\", \"email\": \"douglas@harmonygames.co\"}, \"time\": \"2025-09-29T16:47:43Z\", \"permalink\": \"https://harmonygamesgroup.slack.com/archives/D079SNE2TL4/p1759164463327349\", \"participants\": [{\"id\": \"EMPLOYEE_0012_SLACK_ID\", \"name\": \"Vincent Parker\", \"real_name\": \"Vincent Parker\", \"display_name\": \"Vincent Parker\", \"email\": \"vincent.parker@harmonygames.co\"}, {\"id\": \"EMPLOYEE_0031_SLACK_ID\", \"name\": \"Douglas\", \"real_name\": \"Douglas\", \"display_name\": \"Douglas\", \"email\": \"douglas@harmonygames.co\"}, {\"id\": \"PERSON_6089_SLACK_ID\", \"name\": \"PERSON_6089_SLACK_ID\", \"real_name\": \"PERSON_6089_SLACK_ID\", \"display_name\": \"PERSON_6089_S

### 102 slack_read_channel err=None
INPUT: {"channel_id": "D079SNE2TL4", "oldest": "1758600000", "response_format": "concise"}
RESULT(10915): {"result":"{\"ok\": true, \"messages\": [{\"ts\": \"1759269903.971719\", \"type\": \"message\", \"text\": \"Go to sleep [PERSON_NAME_0050] :sleeping:\", \"channel\": \"D079SNE2TL4\", \"user\": \"EMPLOYEE_0031_SLACK_ID\"}, {\"ts\": \"1759269712.483915\", \"type\": \"message\", \"text\": \"fyi #36 is rolled out to prod too, the container is up. that's the code side\", \"channel\": \"D079SNE2TL4\", \"user\": \"EMPLOYEE_0031_SLACK_ID\"}, {\"ts\": \"1759269524.769369\", \"type\": \"message\", \"text\": \"Yep it works as expected \", \"channel\": \"D079SNE2TL4\", \"user\": \"EMPLOYEE_0012_SLACK_ID\"}, {\"ts\": \"1759256806.682939\", \"type\": \"message\", \"text\": \" Thankss will return to you\", \"channel\": \"D079SNE2TL4\", \"user\": \"EMPLOYEE_0012_SLACK_ID\"}, {\"ts\": \"1759256193.859279\", \"type\": \"message\", \"text\": \"Ok, I updated the prod environment with the latest teams/social changes, let me know if you are still getting those issues\", \"channel\": \"D079SNE2TL4\", \"user\": \"EMPLOYEE_0031_SLACK_ID\"}, {\"ts\": \"1759250957.169129\", \"type\": \"message\", \"text\": \"[USERNAME_35317]\", \"channel\": \"D079SNE2TL4\", \"user\": \"EMPLOYEE_0012_SLACK_ID\"}, {\"ts\": \"1

### 103 github_get_pull_request err=None
INPUT: {"owner": "harmonygames-Games", "repo": "match3d-backend", "pullNumber": 36}
RESULT(2051): {"result":"{\"id\": \"harmonygames-Games/match3d-backend#36\", \"number\": 36, \"title\": \"Fix Zombie Lane chest grant after the daily reset\", \"state\": \"closed\", \"merged\": true, \"draft\": false, \"locked\": false, \"maintainer_can_modify\": false, \"user\": {\"login\": \"PERSON_5760_GITHUB_USERNAME\", \"id\": \"PERSON_5760_GITHUB_ID\", \"node_id\": \"PERSON_5760_GITHUB_NODE_ID\", \"type\": \"User\", \"site_admin\": false, \"html_url\": \"https://github.com/PERSON_5760_GITHUB_USERNAME\"}, \"merged_by\": {\"login\": \"PERSON_5760_GITHUB_USERNAME\", \"id\": \"PERSON_5760_GITHUB_ID\", \"node_id\": \"PERSON_5760_GITHUB_NODE_ID\", \"type\": \"User\", \"site_admin\": false, \"html_url\": \"https://github.com/PERSON_5760_GITHUB_USERNAME\"}, \"body\": \"Chest claims were acknowledged but the grant job skipped them when the claim landed after the daily reset. ZOM-567\", \"base\": {\"ref\": \"main\", \"sha\": \"a0e4a218082ccfd2d20486fed1dba5772183e0d4\", \"repo\": {\"full_name\": \"harmonygames-Games/match3d-backend\"}}, \"head\": {\"ref\": \"zombie-lane-chest-grant\", \"sha\": \"5fa55c7a2d2f25fe75b576c00061000610669d3c\", \"repo\": {\"full_name\": \"harmonygames-Games/match3d-backen

### 104 github_get_issue_comments err=None
INPUT: {"owner": "harmonygames-Games", "repo": "match3d-backend", "issue_number": 36}
RESULT(102): {"result":"{\"total_count\": 0, \"limit\": 30, \"offset\": 0, \"has_more\": false, \"comments\": []}"}

### 105 github_get_pull_request_files err=True
INPUT: {"owner": "harmonygames-Games", "repo": "match3d-backend", "pullNumber": 36}
RESULT(845): {"message": "Cannot compute the file list for pull request #36: No commit or ref found for 5fa55c7a2d2f25fe75b576c00061000610669d3c in harmonygames-Games/match3d-backend. The commit is not in this repository's commit map. The pull request records 3 changed file(s) (+34/-9), so this is a missing object in this environment, not an empty diff.", "documentation_url": "https://docs.github.com/rest", "status": "503", "error": {"code": "unavailable", "message": "Cannot compute the file list for pull request #36: No commit or ref found for 5fa55c7a2d2f25fe75b576c00061000610669d3c in harmonygames-Games/match3d-backend. The commit is not in this repository's commit map. The pull request records 3 changed file(s) (+34/-9), so this is a missing object in this environment, not an empty diff."}, "changed_files": 3, "additions": 34, "deletions": 9}

### 106 github_get_pull_request_comments err=None
INPUT: {"owner": "harmonygames-Games", "repo": "match3d-backend", "pullNumber": 36}
RESULT(1786): {"result":"[{\"id\": \"harmonygames-Games/match3d-backend#36#rc_1\", \"user\": {\"login\": \"EMPLOYEE_0025_GITHUB_USERNAME\", \"id\": \"EMPLOYEE_0025_GITHUB_ID\", \"node_id\": \"EMPLOYEE_0025_GITHUB_NODE_ID\", \"type\": \"User\", \"site_admin\": false, \"html_url\": \"https://github.com/EMPLOYEE_0025_GITHUB_USERNAME\"}, \"body\": \"checked prod after Douglas rolled this out: claimed a chest on my prod account and nothing landed. the migration only creates the empty zombie_lane_chest_rows table, the rows the grant reads come from this load, which runs by hand per environment and hasn't been run on prod. so the new grant path does nothing on prod yet. I'm holding the prod load until after the store push\", \"path\": \"priv/repo/data/load_zombie_lane_chest_rows.exs\", \"diff_hunk\": \"@@ -0,0 +1,14 @@\\n+# Loads the chest rows the Zombie Lane grant reads. Run by hand per environment:\\n+#   bin/zombies_game eval 'Code.eval_file(\\\"priv/repo/data/load_zombie_lane_chest_rows.exs\\\")'\", \"line\": 2, \"commit_id\": \"5fa55c7a2d2f25fe75b576c00061000610669d3c\", \"pull_request_review_id\": null, \"side\": null, \"start_line\": null, \"start_side\": null, \"subject_type\": null, \"created

### 107 github_get_pull_request_reviews err=None
INPUT: {"owner": "harmonygames-Games", "repo": "match3d-backend", "pullNumber": 36}
RESULT(1300): {"result":"[{\"id\": \"harmonygames-Games/match3d-backend#36#rev_1\", \"user\": {\"login\": \"EMPLOYEE_0025_GITHUB_USERNAME\", \"id\": \"EMPLOYEE_0025_GITHUB_ID\", \"node_id\": \"EMPLOYEE_0025_GITHUB_NODE_ID\", \"type\": \"User\", \"site_admin\": false, \"html_url\": \"https://github.com/EMPLOYEE_0025_GITHUB_USERNAME\"}, \"state\": \"APPROVED\", \"body\": \"\", \"submitted_at\": \"2025-09-30T18:42:00Z\", \"commit_id\": null, \"html_url\": \"https://github.com/harmonygames-Games/match3d-backend/pull/36#pullrequestreview-rev_1\", \"pull_request_url\": \"https://api.github.com/repos/harmonygames-Games/match3d-backend/pulls/36\"}, {\"id\": \"harmonygames-Games/match3d-backend#36#rev_2\", \"user\": {\"login\": \"EMPLOYEE_0025_GITHUB_USERNAME\", \"id\": \"EMPLOYEE_0025_GITHUB_ID\", \"node_id\": \"EMPLOYEE_0025_GITHUB_NODE_ID\", \"type\": \"User\", \"site_admin\": false, \"html_url\": \"https://github.com/EMPLOYEE_0025_GITHUB_USERNAME\"}, \"state\": \"COMMENTED\", \"body\": \"\", \"submitted_at\": \"2025-09-30T22:40:00Z\", \"commit_id\": \"5fa55c7a2d2f25fe75b576c00061000610669d3c\", \"html_url\": \"https://github.com/harmonygames-Games/match3d-backend/pull/36#pullrequestreview-rev_2\", \"

### 108 github_get_pull_request_timeline err=None
INPUT: {"owner": "harmonygames-Games", "repo": "match3d-backend", "pullNumber": 36}
RESULT(2481): {"result":"[{\"id\": \"harmonygames-Games/match3d-backend#36#ev_1\", \"event\": \"review_requested\", \"actor\": {\"login\": \"PERSON_5760_GITHUB_USERNAME\", \"id\": \"PERSON_5760_GITHUB_ID\", \"node_id\": \"PERSON_5760_GITHUB_NODE_ID\", \"type\": \"User\", \"site_admin\": false, \"html_url\": \"https://github.com/PERSON_5760_GITHUB_USERNAME\"}, \"created_at\": \"2025-09-30T18:30:00Z\", \"requested_reviewer\": {\"github_id\": \"EMPLOYEE_0025_GITHUB_ID\", \"login\": \"EMPLOYEE_0025_GITHUB_USERNAME\", \"node_id\": \"EMPLOYEE_0025_GITHUB_NODE_ID\", \"type\": \"User\"}}, {\"id\": \"harmonygames-Games/match3d-backend#36#ev_2\", \"event\": \"commented\", \"actor\": {\"login\": \"SVC_0321_GITHUB_USERNAME\", \"id\": \"SVC_0321_GITHUB_ID\", \"node_id\": \"SVC_0321_GITHUB_NODE_ID\", \"type\": \"Bot\", \"site_admin\": false, \"html_url\": \"https://github.com/SVC_0321_GITHUB_USERNAME\"}, \"created_at\": \"2025-09-30T18:30:06Z\"}, {\"id\": \"harmonygames-Games/match3d-backend#36#ev_3\", \"event\": \"reviewed\", \"actor\": {\"login\": \"EMPLOYEE_0025_GITHUB_USERNAME\", \"id\": \"EMPLOYEE_0025_GITHUB_ID\", \"node_id\": \"EMPLOYEE_0025_GITHUB_NODE_ID\", \"type\": \"User\", \"site_admin\": false, 

### 109 github_search_commits err=None
INPUT: {"query": "repo:harmonygames-Games/match3d ZOM-473"}
RESULT(130): {"result":"{\"total_count\": 0, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": []}"}

### 110 github_search_pull_requests err=None
INPUT: {"query": "repo:harmonygames-Games/match3d endless", "fields": ["number", "title", "merged_at", "body"]}
RESULT(21854): {"result":"{\"total_count\": 28, \"incomplete_results\": false, \"has_more\": false, \"page\": 1, \"perPage\": 30, \"items\": [{\"number\": 470, \"title\": \"Collect And Win minor bugs fixes\", \"body\": \"Fixes:\\r\\n* When the page opened, it shows placeholder images at first.\\r\\n* After level completion, it first shows placeholder icon and progress for the event, then shows the correct one\\r\\n* In every level, I got two errors both backend and client. \\r\\n* In Boss arena and endless mode, the c&w UI is visible. \\n\\n<!-- This is an auto-generated comment: release notes by coderabbit.ai -->\\n## Summary by CodeRabbit\\n\\n- Refactor\\n  - Collect & Win screens now use pooled UI items for faster loading, smoother scrolling, reduced flicker, improved ordering and cleanup when refreshing content.\\n- New Features\\n  - Auto-scrolls to the first unclaimed reward/grand prize when opening the screen.\\n  - Reward and grand-prize items now reflect claimed state (labels hidden for claimed stages).\\n- Bug Fixes\\n  - Next Reward icon visibility corrected based on event lock.\\n  - Token counter/panel shown only when relevant (avoids Endless/Infinite Boss modes).\\n  - UI elements 

### 111 linear_get_issue err=None
INPUT: {"id": "ZOM-473"}
RESULT(1585): {"result":"{\"id\": \"ZOM-473\", \"uuid\": null, \"identifier\": \"ZOM-473\", \"number\": 473, \"title\": \"Endless mode ending screen can be skipped after death\", \"description\": \"When the endless mode is over, players can still try to match items with urgency but as soon as the level is over, the ending screen is visible.\\n\\nHowever that screen has no input blocker whatsoever. So it might be skipped at once while trying to match objects. \\n\\nHere is the expected outcome:\\n\\n* When the level ends, block the input until the x2 multiplication happens. So that players won't skip it accidentally. \\n\\n[[CREDIT_CARD_NUMBER_6336].8623973.mp4]([URL_52789])\", \"priority\": {\"value\": 3, \"name\": \"Medium\"}, \"estimate\": null, \"url\": \"https://linear.app/harmonygames/issue/ZOM-473/endless-mode-ending-screen-can-be-skipped-after-death\", \"gitBranchName\": \"vincentparker/zom-473-endless-mode-ending-screen-can-be-skipped-after-death\", \"createdAt\": \"2025-08-14T08:24:51Z\", \"updatedAt\": \"2025-09-22T15:11:51Z\", \"archivedAt\": null, \"completedAt\": \"2025-09-22T15:11:51Z\", \"startedAt\": null, \"canceledAt\": null, \"dueDate\": null, \"status\": \"Done\", \"statusTyp

### 112 linear_get_issue err=None
INPUT: {"id": "ZOM-453", "maxDescriptionChars": 600}
RESULT(1242): {"result":"{\"id\": \"ZOM-453\", \"uuid\": null, \"identifier\": \"ZOM-453\", \"number\": 453, \"title\": \"Fix text inconsistency\", \"description\": \"[PERSON_NAME_0040] to make a list of all uppercase, lowercase text placement \\nAnd we need to standardize the infographic screens.\", \"priority\": {\"value\": 3, \"name\": \"Medium\"}, \"estimate\": null, \"url\": \"https://linear.app/harmonygames/issue/ZOM-453/fix-text-inconsistency\", \"gitBranchName\": \"vincentparker/zom-453-fix-text-inconsistency\", \"createdAt\": \"2025-08-01T17:29:49Z\", \"updatedAt\": \"2025-08-01T17:31:09Z\", \"archivedAt\": null, \"completedAt\": null, \"startedAt\": null, \"canceledAt\": null, \"dueDate\": null, \"status\": \"Todo\", \"statusType\": \"unstarted\", \"labels\": [], \"links\": [], \"attachments\": [], \"createdBy\": \"julia.lawson@harmonygames.co\", \"createdById\": \"usr_8140f09bf9f1b94c\", \"assignee\": \"samuel.turner@harmonygames.co\", \"assigneeId\": \"usr_caafeec2804b3a67\", \"project\": \"Zombie Match 3D\", \"projectId\": \"dbab77c7-f871-4888-abf8-d98b52a41624\", \"parentId\": \"ZOM-450\", \"team\": \"Zombie Match 3D\", \"teamId\": \"team_ZOM\", \"timeInStatusMinutes\": 87214, \"is

### 113 linear_get_issue err=None
INPUT: {"id": "ZOM-293", "maxDescriptionChars": 600}
RESULT(1160): {"result":"{\"id\": \"ZOM-293\", \"uuid\": null, \"identifier\": \"ZOM-293\", \"number\": 293, \"title\": \"Dynamic Difficulty Tiering Down Issue\", \"description\": \"Dynamic Difficulty Tiering\", \"priority\": {\"value\": 4, \"name\": \"Low\"}, \"estimate\": null, \"url\": \"https://linear.app/harmonygames/issue/ZOM-293/dynamic-difficulty-tiering-down-issue\", \"gitBranchName\": \"vincentparker/zom-293-dynamic-difficulty-tiering-down-issue\", \"createdAt\": \"2025-06-23T18:19:40Z\", \"updatedAt\": \"2025-07-03T17:42:00Z\", \"archivedAt\": null, \"completedAt\": null, \"startedAt\": null, \"canceledAt\": null, \"dueDate\": null, \"status\": \"Todo\", \"statusType\": \"unstarted\", \"labels\": [\"30 June\"], \"links\": [], \"attachments\": [], \"createdBy\": \"vincent.parker@harmonygames.co\", \"createdById\": \"usr_65c76e0b87aa7e9b\", \"assignee\": \"Robert\", \"assigneeId\": \"usr_Robert\", \"project\": \"Zombie Match 3D\", \"projectId\": \"dbab77c7-f871-4888-abf8-d98b52a41624\", \"parentId\": \"ZOM-201\", \"team\": \"Zombie Match 3D\", \"teamId\": \"team_ZOM\", \"timeInStatusMinutes\": 143324, \"isArchived\": false, \"stateHistory\": []}"}

### 114 linear_list_issues err=None
INPUT: {"query": "progress wiped update level 1 save lost", "limit": 10, "fields": ["identifier", "title", "status", "createdAt"], "includeArchived": true}
RESULT(2164): {"result":"{\"issues\": [{\"id\": \"ENG-2109\", \"identifier\": \"ENG-2109\", \"title\": \"Quest In\\u0131t Issue Persist on some users\", \"createdAt\": \"2025-01-24T15:25:59Z\", \"status\": \"Backlog\", \"statusType\": \"backlog\"}, {\"id\": \"ENG-1116\", \"identifier\": \"ENG-1116\", \"title\": \"Quest goals are not updated before the quest gets populated on iOS\", \"createdAt\": \"2024-07-22T16:59:46Z\", \"status\": \"Canceled\", \"statusType\": \"canceled\"}, {\"id\": \"ENG-2363\", \"identifier\": \"ENG-2363\", \"title\": \"After signing-in, the game stuck at splash screen-\", \"createdAt\": \"2025-06-03T14:29:58Z\", \"status\": \"Todo\", \"statusType\": \"unstarted\"}, {\"id\": \"ENG-2313\", \"identifier\": \"ENG-2313\", \"title\": \"Retry Prelevel Dialogue Error\", \"createdAt\": \"2025-04-28T17:41:12Z\", \"status\": \"Done\", \"statusType\": \"completed\"}, {\"id\": \"ENG-1614\", \"identifier\": \"ENG-1614\", \"title\": \"The Win & Collect Event Pop up UI & VFX Issues\", \"createdAt\": \"2024-10-02T14:43:41Z\", \"status\": \"Done\", \"statusType\": \"completed\"}, {\"id\": \"ENG-1727\", \"identifier\": \"ENG-1727\", \"title\": \"UPDATED LIST OF COLLECT & WIN ISSUES\", \"cre

### 115 linear_create_issue err=None
INPUT: {"team": "ZOM", "title": "iOS: updating from the N-1 store build to iOS Submission #50 resets the save to level 1", "description": "Found by the update-path row of the QA regression runbook during the store gate for Android Submission #135 / iOS Submission #50 (ZOM-570).\n\n**Device / OS:** iPhone 13, iOS 18.6\n**Source build:** N-1 store build (App Store), updated to iOS Submission #50 (TestFlight 50)\n\n**What goes wrong:** After the update the save comes back at level 1 with 500 coins. Before the update the account was on level 212 with 18,400 coins. Relaunching doesn't bring the progress back.\n\n**Repro:**\n1. Install the N-1 build from the App Store.\n2. Play past level 200.\n3. Install TestFlight 50 (iOS Submission #50) over it.\n4. Launch. The save is back at level 1 / 500 coins.\n\n**Other update rows passed:** iOS N-2 → #50, Android N-1 → #135 and Android N-2 → #135 all kept level, coins and unlocks.\n\nSource: Brian's \"Update-path run - iOS #50 / Android #135\" doc (Sep 30). The runbook says a failure in any UPDATE column blocks the release, and lost progress/coins is a blocker under the ZM submission rules.", "labels": ["Bug"], "priority": 1, "blocks": ["ZOM-570"]}
RESULT(2232): {"result":"{\"id\": \"ZOM-581\", \"uuid\": null, \"identifier\": \"ZOM-581\", \"number\": 581, \"title\": \"iOS: updating from the N-1 store build to iOS Submission #50 resets the save to level 1\", \"description\": \"Found by the update-path row of the QA regression runbook during the store gate for Android Submission #135 / iOS Submission #50 (ZOM-570).\\n\\n**Device / OS:** iPhone 13, iOS 18.6\\n**Source build:** N-1 store build (App Store), updated to iOS Submission #50 (TestFlight 50)\\n\\n**What goes wrong:** After the update the save comes back at level 1 with 500 coins. Before the update the account was on level 212 with 18,400 coins. Relaunching doesn't bring the progress back.\\n\\n**Repro:**\\n1. Install the N-1 build from the App Store.\\n2. Play past level 200.\\n3. Install TestFlight 50 (iOS Submission #50) over it.\\n4. Launch. The save is back at level 1 / 500 coins.\\n\\n**Other update rows passed:** iOS N-2 \\u2192 #50, Android N-1 \\u2192 #135 and Android N-2 \\u2192 #135 all kept level, coins and unlocks.\\n\\nSource: Brian's \\\"Update-path run - iOS #50 / Android #135\\\" doc (Sep 30). The runbook says a failure in any UPDATE column blocks the release, and los

### 116 Bash err=False
INPUT: {"command": "cat > gate.py <<'EOF'\nimport json\na=json.load(open('zom.json'))\npage3_open={'ZOM-184':'11.Curling Iron (Maybe Drop the item)','ZOM-182':'9. Bagel','ZOM-181':'8. Vaious Solid color Plates/cups/mugs/egg on plates','ZOM-168':'5th In-game Boost Double Damage','ZOM-56':'Glued VFX','ZOM-137':'FOOD ITEMS','ZOM-155':'Squash','ZOM-151':'Cucumbers','ZOM-150':'Cherries','ZOM-148':'Plum','ZOM-147':'Peach','ZOM-130':'Create an out of moves screen flow with offers','ZOM-104':'Gas Can improvement','ZOM-78':'Event Calendar For Zombie Match 3D','ZOM-70':'Rewards system','ZOM-69':'Bot system','ZOM-66':'Stats endpoints','ZOM-65':'Profile page endpoints','ZOM-48':'Reward Animations'}\nrows={}\norder=[]\nexcl={'ZOM-570','ZOM-359','ZOM-475'}\nfor i in a:\n  k=i['identifier']\n  if k in excl: continue\n  openst = i['statusType'] not in ('completed','canceled','duplicate')\n  done_after = i['statusType']=='completed' and i['completedAt'] and i['completedAt']>'2025-09-22T12:30'\n  if openst or done_after:\n    rows[k]=i['title']; order.append(k)\nfor k,t in page3_open.items(): rows[k]=t; order.append(k)\nextra={'DES-313':\"ZM level 214 can't be completed\",'ART-793':'ZM3D - boss arena background flickers on iPhone 12','ART-792':'ZM3D - Marketing Screenshots round 3','ART-790':'Updated ZM Marketing Screenshots','ZOM-581':'iOS: updating from the N-1 store build to iOS Submission #50 resets the save to level 1'}\nfor k,t in extra.items(): rows[k]=t; order.append(k)\nSL='https://harmonyga
RESULT(2151): 133 Counter({'NO CALL': 86, 'KNOWN ISSUE': 22, 'BLOCKER': 14, 'FIXED': 11})
ZOM-449 BLOCKER n/a
ZOM-578 BLOCKER n/a
ZOM-483 BLOCKER n/a
ZOM-560 BLOCKER n/a
ZOM-554 BLOCKER n/a
ZOM-546 BLOCKER n/a
ZOM-576 BLOCKER n/a
ZOM-573 BLOCKER n/a
ZOM-567 BLOCKER server - not live
ZOM-569 BLOCKER not in candidate
ZOM-559 BLOCKER n/a
ZOM-435 BLOCKER in candidate
DES-313 BLOCKER n/a
ZOM-581 BLOCKER n/a
ZOM-580 KNOWN ISSUE n/a
ZOM-568 KNOWN ISSUE n/a
ZOM-579 KNOWN ISSUE n/a
ZOM-468 KNOWN ISSUE n/a
ZOM-562 KNOWN ISSUE n/a
ZOM-481 KNOWN ISSUE n/a
ZOM-556 KNOWN ISSUE n/a
ZOM-535 KNOWN ISSUE n/a
ZOM-534 KNOWN ISSUE n/a
ZOM-520 KNOWN ISSUE n/a
ZOM-505 KNOWN ISSUE n/a
ZOM-574 KNOWN ISSUE n/a
ZOM-504 KNOWN ISSUE n/a
ZOM-458 KNOWN ISSUE n/a
ZOM-443 KNOWN ISSUE n/a
ZOM-572 KNOWN ISSUE n/a
ZOM-438 KNOWN ISSUE n/a
ZOM-427 KNOWN ISSUE n/a
ZOM-571 KNOWN ISSUE n/a
ZOM-348 KNOWN ISSUE n/a
ZOM-237 KNOWN ISSUE n/a
ART-793 KNOWN ISSUE n/a
ZOM-517 FIXED in candidate
ZOM-564 FIXED in candidate
ZOM-429 FIXED in candidate
ZOM-563 FIXED server - live
ZOM-561 FIXED in candidate
ZOM-557 FIXED in candidate
ZOM-558 FIXED in candidate
ZOM-506 FIXED in candidate
ZOM-473 FIXED in candidate
ZOM-503 FIXED in candidate
ZOM-434 F

### 117 gsheets_batch_update err=None
INPUT: {"spreadsheetId": "f_0ebfccf33076f9dbf086bc", "requests": [{"addSheet": {"properties": {"title": "Sep 30 - Android #135 / iOS #50", "index": 2, "gridProperties": {"rowCount": 150, "columnCount": 6}}}}]}
RESULT(377): {"result":"{\"spreadsheetId\": \"f_0ebfccf33076f9dbf086bc\", \"driveFileId\": \"f_0ebfccf33076f9dbf086bc\", \"replies\": [{\"addSheet\": {\"properties\": {\"sheetId\": 1418000307, \"title\": \"Sep 30 - Android #135 / iOS #50\", \"index\": 2, \"sheetType\": \"GRID\", \"gridProperties\": {\"rowCount\": 150, \"columnCount\": 6}}}}], \"modifiedTime\": \"2025-10-01T07:05:12Z\"}"}

### 118 Bash err=False
INPUT: {"command": "python3 -c \"import json;print(json.dumps(json.load(open('rows.json'))))\""}
RESULT(22439): [["ticket", "title", "build status", "QA result", "call", "evidence"], ["ZOM-449", "Some items are acting weird in low-end android device", "n/a", "repro on #135 low-end Android (Brian): cold start into level 3 freezes until force-quit", "BLOCKER", "ZOM-449 comment cmt_zom449_2"], ["ZOM-578", "Tutorial stuck at step 3 on a fresh install", "n/a", "repro on #135 fresh install (Leonard): tutorial step 3 booster tap does nothing, stuck after relaunch", "BLOCKER", "ZOM-578"], ["ZOM-483", "Infinite lives from new-install are not granted, rewards 30 min in the next session start.", "n/a", "repro on #135 fresh install: relaunch resets new-install infinite lives from 50 to 30 min (20 min lost)", "BLOCKER", "ZOM-483 comment cmt_zom483_1"], ["ZOM-560", "The abandoned pack win streak freezer reward is not granted.", "n/a", "repro on #135 (sandbox purchase): abandoned pack does not deliver win streak freezer time", "BLOCKER", "ZOM-560 comment cmt_zom560_1"], ["ZOM-554", "Quiting level mid tornado boost breaks the object physics", "n/a", "repro on #50: quit mid tornado -> next level objects float, unplayable until force-quit", "BLOCKER", "ZOM-554 comment cmt_zom554_2"], ["ZOM-546", "Bug: refill 

### 119 Bash err=False
INPUT: {"command": "python3 -c \"\nimport json;r=json.load(open('rows.json'));print(len(r))\""}
RESULT(3): 134

### 120 gsheets_values_update err=None
INPUT: {"spreadsheetId": "f_0ebfccf33076f9dbf086bc", "range": "'Sep 30 - Android #135 / iOS #50'!A1", "valueInputOption": "RAW", "values": [["ticket", "title", "build status", "QA result", "call", "evidence"], ["ZOM-449", "Some items are acting weird in low-end android device", "n/a", "repro on #135 low-end Android (Brian): cold start into level 3 freezes until force-quit", "BLOCKER", "ZOM-449 comment cmt_zom449_2"], ["ZOM-578", "Tutorial stuck at step 3 on a fresh install", "n/a", "repro on #135 fresh install (Leonard): tutorial step 3 booster tap does nothing, stuck after relaunch", "BLOCKER", "ZOM-578"], ["ZOM-483", "Infinite lives from new-install are not granted, rewards 30 min in the next session start.", "n/a", "repro on #135 fresh install: relaunch resets new-install infinite lives from 50 to 30 min (20 min lost)", "BLOCKER", "ZOM-483 comment cmt_zom483_1"], ["ZOM-560", "The abandoned pack win streak freezer reward is not granted.", "n/a", "repro on #135 (sandbox purchase): abandoned pack does not deliver win streak freezer time", "BLOCKER", "ZOM-560 comment cmt_zom560_1"], ["ZOM-554", "Quiting level mid tornado boost breaks the object physics", "n/a", "repro on #50: quit mid tornado -> next level objects float, unplayable until force-quit", "BLOCKER", "ZOM-554 comment cmt_zom554_2"], ["ZOM-546", "Bug: refill algorithm spawns fewer items over time", "n/a", "repro on #135/#50: endless board drains to 5 items after ~8 refills, run cannot go on", "BLOCKER", "ZOM-546 comment cmt
RESULT(286): {"result":"{\"spreadsheetId\": \"f_0ebfccf33076f9dbf086bc\", \"driveFileId\": \"f_0ebfccf33076f9dbf086bc\", \"updatedRange\": \"'Sep 30 - Android #135 / iOS #50'!A1:F134\", \"updatedRows\": 134, \"updatedColumns\": 6, \"updatedCells\": 804, \"modifiedTime\": \"2025-10-01T07:06:30Z\"}"}

### 121 linear_update_issue err=None
INPUT: {"id": "ZOM-570", "patch": [{"op": "append", "text": "\n\n## QA gate blockers - Android Submission #135 / iOS Submission #50 (Oct 1)\n\nQA call: **NO-GO** until these are resolved. Full register: ZM3D Release Gate sheet, tab \"Sep 30 - Android #135 / iOS #50\".\n\n- ZOM-581 - iOS update from the N-1 store build to #50 resets the save to level 1 / 500 coins (runbook update-path row, newly filed)\n- ZOM-567 - Zombie Lane chests claimed on prod don't land in the inventory (server - not live: match3d-backend #36 is rolled out but the chest-row data load hasn't been run on prod)\n- ZOM-569 - Season Pass opens twice from the join popup, empty screen, kill app to exit (fix landed on main after the #135/#50 Started lines, so it isn't in the candidates)\n- ZOM-435 - Stuck on the trophy path after fast claim taps (repro on #135)\n- DES-313 - Level 214 can't be completed (only 2 of 3 jars spawn)\n- ZOM-546 - Endless refill drains the board, run can't continue\n- ZOM-554 - Quitting mid tornado leaves the next level unplayable until force-quit\n- ZOM-573 - Collect&Win: claiming the 5th chest crashes\n- ZOM-578 - Tutorial stuck at step 3 on a fresh install\n- ZOM-576 - Season Pass premium tier claim drops the booster bundle\n- ZOM-560 - Abandoned pack doesn't deliver the win streak freezer time\n- ZOM-483 - New-install infinite lives reset to 30 min on relaunch (lost time)\n- ZOM-449 - Low-end Android: cold start into level 3 freezes until force-quit\n- ZOM-559 - Samsung: sound lost after 
RESULT(3150): {"result":"{\"id\": \"ZOM-570\", \"uuid\": null, \"identifier\": \"ZOM-570\", \"number\": 570, \"title\": \"ZM store push - Android Submission #135 / iOS Submission #50\", \"description\": \"Store push for ZM.\\n\\nCandidates: Android Submission #135 and iOS Submission #50, both started from main today. We decide at the go/no-go on Friday, invite coming.\\n\\nVincent - QA gate as usual: Leonard's submission rules and my note on how we cut submissions both apply, the docs are shared with you. Blockers go on this ticket by key, the existing ticket if there is one (I'm putting the reuse rule on the tech-issues card). I'll post the candidates in #zombie-bugs.\\n\\nOther push notes go in the comments here.\\n\\n## QA gate blockers - Android Submission #135 / iOS Submission #50 (Oct 1)\\n\\nQA call: **NO-GO** until these are resolved. Full register: ZM3D Release Gate sheet, tab \\\"Sep 30 - Android #135 / iOS #50\\\".\\n\\n- ZOM-581 - iOS update from the N-1 store build to #50 resets the save to level 1 / 500 coins (runbook update-path row, newly filed)\\n- ZOM-567 - Zombie Lane chests claimed on prod don't land in the inventory (server - not live: match3d-backend #36 is rolled out but t

### 122 slack_send_message err=None
INPUT: {"channel_id": "C08R27X0EAH", "thread_ts": "1759263900.484190", "message": "QA gate for Android Submission #135 / iOS Submission #50: **NO-GO** from QA as it stands.\n\nBrian's fresh-install matrix is green, but one update-path row failed. On iOS, updating from the N-1 store build to #50 resets the save to level 1 / 500 coins (iPhone 13, iOS 18.6). Nobody had filed it, so it's now **ZOM-581**. Per the runbook, a failure in any update column blocks on its own.\n\n14 blockers in total, all listed by key on ZOM-570:\n• ZOM-581: update from N-1 to #50 wipes progress (iOS)\n• ZOM-567: Zombie Lane chests don't land on prod. Backend #36 is rolled out, but the chest data load hasn't run on prod, so it's not live\n• ZOM-569: Season Pass empty screen. The fix landed on main after the #135/#50 Started lines, so it isn't in these builds\n• ZOM-435: stuck on the trophy path again on #135\n• DES-313: level 214 can't be completed\n• ZOM-546: endless refill drains the board\n• ZOM-554: quitting mid-tornado leaves the next level unplayable until a force-quit\n• ZOM-573: crash on the 5th Collect&Win chest\n• ZOM-578: tutorial stuck at step 3 on a fresh install\n• ZOM-576: Season Pass premium claim drops the booster bundle\n• ZOM-560: abandoned pack doesn't deliver the freezer time\n• ZOM-483: new-install infinite lives get cut to 30 min\n• ZOM-449: low-end Android freezes on level 3\n• ZOM-559: Samsung victory-screen freeze (last seen on #133, not re-tested on the candidates yet)\n\nAlso: 22 k
RESULT(2183): {"result":"{\"ok\": true, \"ts\": \"1759302407.000000\", \"channel\": \"C08R27X0EAH\", \"message\": {\"text\": \"QA gate for Android Submission #135 / iOS Submission #50: **NO-GO** from QA as it stands.\\n\\nBrian's fresh-install matrix is green, but one update-path row failed. On iOS, updating from the N-1 store build to #50 resets the save to level 1 / 500 coins (iPhone 13, iOS 18.6). Nobody had filed it, so it's now **ZOM-581**. Per the runbook, a failure in any update column blocks on its own.\\n\\n14 blockers in total, all listed by key on ZOM-570:\\n\\u2022 ZOM-581: update from N-1 to #50 wipes progress (iOS)\\n\\u2022 ZOM-567: Zombie Lane chests don't land on prod. Backend #36 is rolled out, but the chest data load hasn't run on prod, so it's not live\\n\\u2022 ZOM-569: Season Pass empty screen. The fix landed on main after the #135/#50 Started lines, so it isn't in these builds\\n\\u2022 ZOM-435: stuck on the trophy path again on #135\\n\\u2022 DES-313: level 214 can't be completed\\n\\u2022 ZOM-546: endless refill drains the board\\n\\u2022 ZOM-554: quitting mid-tornado leaves the next level unplayable until a force-quit\\n\\u2022 ZOM-573: crash on the 5th Collect&Win ches
