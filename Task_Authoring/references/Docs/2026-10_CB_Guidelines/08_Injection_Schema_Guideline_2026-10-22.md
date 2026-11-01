<!-- Source: CB guideline PDF (watermarked copy) (Archive 6.zip, received 2026-11-01). Text extracted with pdftotext; watermark lines removed; two-column pages may interleave. -->

Injection Schema Guideline
HarmonyGames · Universe date: October 1, 2025 or February 14, 2026, 00:00 UTC · Updated October 22, 2026
How to add or change HarmonyGames records with a SQL file, then run /injection on that file. You do not need to be a database
expert. Follow the six steps, then copy the table you need.
Updates
Change log
Plain-language injection guide. 64 tables you can write, including Confluence. Snowflake is listed only so you do not write
SQL for it.
New section 01: create an injection with the web portal and run it in the universe. Second universe date added: October 1,
2025. Sections renumbered.
How to create an injection
01 · Create and run your injection
Save the file as 01_Universe_Inject.sql.
3. Save it
Copy real ids from the data files (section 04), use the column names from this guide (section 05), fill every Required
column, and date anything that already happened on or before your universe date. Nothing in the SQL may state the
answer the agent is supposed to find.
2. Check every line
In the Eval Portal chat, describe what has to exist in the universe for your task: who says what, where, and when. Ask
it to write the injection SQL for that scenario.
1. Describe your
scenario
What to do
The quickest way to start is to let the web portal draft the SQL from your scenario. You are still responsible for every line.
Run it in the universe and confirm it in _changelog, as shown below.
5. Inject it
Run /injection in the Eval Portal and fix the SQL until it passes.
4. Run /injection
EXAMPLE REQUEST
Inject it in the universe
Write the injection SQL for this scenario: on February 10, 2026, Leonard posts in the ua-spend Slack channel that the Adjoe test
starts on February 12, and Robert replies in the same thread asking for the final numbers.
Every change you made to the universe has a row here, with its table, the operation (INSERT, UPDATE or DELETE)
and the id of the row. If your change is not listed, it did not go in. Fix the SQL and run it again.
In the left panel, open Tables and click _changelog.
7. Confirm your changes
SQL that inserts or updates data usually returns No records found. That is the expected result. Only a statement
that looks something up returns rows.
6. Open the change log
Paste the whole file into the editor.
Click Run Query.
3. Paste your SQL
5. Read the result
Click the Query tab.
2. Open the editor
In the universe, open the Database tab.
1. Open the database
What to do
Run your SQL in the universe's database, then open the change log to confirm that every change went in.
An insert or an update changes data and returns no rows. To confirm the injection, check _changelog, not the result panel.
Your SQL pasted into the editor (3), ready to run with Run Query (4).
The Database tab (1) with the Query tab open (2).
NO RECORDS FOUND IS NOT AN ERROR
After Run Query, an insert or update shows No records found (5).
Your SQL pasted into the editor (3), ready to run with Run Query (4).
An injection is a text file of SQL statements. It adds a Slack message, an email, a ticket, or another record before the agent starts the
task. You save it as 01_Universe_Inject.sql and run /injection on it.
02 · What you are doing
The _changelog table under Tables (6), with one row for each change you made (7).
Write your SQL from these. There are 64 tables you can use, including Confluence.
Snowflake
Do not write injection SQL for Snowflake. It is a separate analytics database, and the injection file cannot change it.
something that should already be there.
Open them to copy an id that already exists, such as a channel, a user, or a repository. Do not invent an id for
section 04
The data files in
What to do
Find it in section 06. Use the full name, such as slack.slack_messages . The data file name is not the table name.
Open the data file from section 04. If your new row points at a channel, user, thread, or repository, copy an id that is
already there. For the new row itself, make an id that is not already used.
2. Copy real ids
1. Pick the table
03 · Write the SQL in six steps
Required = Yes means the copy-ready statement must include that column. Required = No means you can leave it out. Text
goes in single quotes. Numbers, TRUE, and FALSE do not. A column ending in _json is text that holds a list or a group of fields,
written as '[]' or '{}'.
HOW TO READ A COLUMN TABLE
The tables in section
What to do with it
What you have
Each record lives in a table. The table name always has two parts: the service, then the table, with a dot between them. A GitHub
issue is github.github_issues. An email is gmail.gmail_messages. A Slack message is slack.slack_messages.
do not put it in the SQL.
The data file sometimes uses a different name. Section 05 lists those differences. If a name is not in the Column list,
names from this guide
3. Use the column
What to do
Required = No column only when you need it, and add its value in the same position.
The copy-ready statement under each table already includes those columns. Replace every replace-me. Add a
4. Fill every Required =
Yes column
Put BEGIN; before the statements and COMMIT; after them. Save the file as 01_Universe_Inject.sql. Run
6. Save and check
Today is your universe date: October 1, 2025 or February 14, 2026, 00:00 UTC. Anything that already happened
is dated on or before it; a deadline may come after it. Write a timestamp as '2026-02-13 12:00:00+00'. Use a
date that fits your universe.
5. Keep the date in the
/injection on it. To make a second run safe, delete only the new id first, then insert it again.
-- Add the email. The thread id must already exist in the data.
INSERT INTO gmail.gmail_messages (
thread_id,
user_email,
subject,
body_text
) VALUES (
'new-message-id',
'existing-thread-id',
'person@harmonygames.co',
'Subject line',
'Body of the email'
An empty list. Use this for a _json column when there is nothing to put in it.
Leave the field empty. Only for a Required = No column.
A number. No quotes.
Yes or no. No quotes.
Text. A quote inside the text is written twice: 'it''s fine'.
TRUE or FALSE
It means
COMMIT;
'some text'
-- Running the file twice should not create two copies, so remove this id first.
DELETE FROM gmail.gmail_messages
WHERE id = 'new-message-id';
This example adds one email. The words after -- are notes. They are not part of the command.
You type
04 · Where to look up an existing id
UPDATE slack.slack_messages
SET text = 'Updated text'
WHERE id = 'existing-message-id';
change that existing row.
To change a row that is already there, copy its id from the data file and use UPDATE. Do this only when the task is supposed to
Open the data file for the service, find a record like the one you need, and copy its id. Paths start at New_Evals/. GitHub and Gmail
also store attachments next to these files. An attachment is not an extra table.
Tables
HarmonyGames_Gmail/Services_Data/gmail/users.json, labels.json, threads/*.json
HarmonyGames_Other_Services
HarmonyGames_Other_Services/Services_Data/slack/channels.json, users.json,
files.json, emojis.json, messages/<channel>/<month>.json
HarmonyGames_Other_Services/Services_Data/gcal/data.json
Google
HarmonyGames_Other_Services
Google
HarmonyGames_Other_Services
HarmonyGames_Other_Services/Services_Data/gdocs/data.json
HarmonyGames_Other_Services
HarmonyGames_Other_Services/Services_Data/gsheets/data.json. The row file is
not unpacked here; use the column list.
HarmonyGames_Other_Services
HarmonyGames_Other_Services/Services_Data/gslides/data.json
HarmonyGames_Other_Services/Services_Data/contacts/contacts.json
No service export
HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json
05 · When the data file uses a different name
— skip for
a normal
Changelog
HarmonyGames_Other_Services
Confluence
HarmonyGames_Other_Services/Services_Data/trello/data.json
HarmonyGames_Other_Services
Contacts
HarmonyGames_Other_Services
HarmonyGames_Other_Services/Services_Data/gdrive/data.json
Trello
HarmonyGames_Other_Services
Google
Calendar
HarmonyGames_Other_Services/Services_Data/linear/data.json
HarmonyGames_Other_Services
Google
Slides
Linear
Google
Sheets
HarmonyGames_Gmail
HarmonyGames_GitHub/Services_Data/github/data.json
Open this file
HarmonyGames_GitHub
GitHub
Folder
Service
THE USUAL PATTERN
A data file and the SQL column list usually use the same names. When they do not, use the name in the right column below. If a
name from the file is not in that column and not in the Column list, leave it out.
A list in the file often becomes a column ending in _json. Write it in quotes: '[]' when it is empty, or '["bug"]' when it has
rrule_json
start_json
shared_with_emails_json
shared_with_emails
gdocs.docs_documents
end_json
gcal.gcal_events
attendees_json
gcal.gcal_events
attendees
gcal.gcal_events
shared_with_emails_json
shared_with_emails
Name to write in SQL
gcal.gcal_events
style_runs_json
style_runs
gdocs.docs_documents
shared_with_emails_json
shared_with_emails
parents_json
parents
owners_json
owners
gdrive.drive_files
Name in the data file
gcal.gcal_calendars
gdrive.drive_files
gdrive.drive_files
one item. Gmail files use capitals, such as emailAddress. SQL uses underscores, such as email_address.
Name to write in SQL
parent_shas
parent_shas_json
labels_json
labels
github.github_pull_requests
assignee_logins_json
assignee_logins
github.github_pull_requests
Name in the data file
github.github_commits
github.github_repositories
topics
topics_json
github.github_timeline_events
gmail.gmail_labels
labelListVisibility
threads_total
email_address
emailAddress
gmail.gmail_users
to_json
gmail.gmail_messages
reply_to_json
reply_to
label_ids_json
labelIds
gmail.gmail_messages
headers_json
headers
gmail.gmail_messages
gmail.gmail_messages
cc_json
gmail.gmail_messages
bcc_json
gmail.gmail_messages
threads_unread
threadsUnread
messages_unread
threadsTotal
gmail.gmail_labels
messagesTotal
messages_total
gmail.gmail_users
history_id
historyId
gmail.gmail_users
labels_json
labels
creator_id
creator
slack.slack_channels
created_ts
created
slack.slack_channels
user_id
slack.slack_messages
slack.slack_files
members_json
members
slack.slack_channels
attachments
attachments_json
user_id
data_json
reactions_json
reactions
trello.trello_actions
slack.slack_messages
files_json
slack.slack_messages
channel_id
channel
slack.slack_messages
slack.slack_messages
relations_json
relations
linear.linear_projects
linear.linear_issues
links_json
labels_json
labels
linear.linear_issues
shared_with_emails_json
shared_with_emails
gslides.slides_presentations
threads_total
threadsTotal
gmail.gmail_users
linear.linear_issues
messages_total
messagesUnread
gmail.gmail_labels
messagesTotal
gmail.gmail_labels
message_list_visibility
gmail.gmail_labels
label_list_visibility
messageListVisibility
data_json
gmail.gmail_labels
requested_reviewer_logins_json
requested_reviewer_logins
github.github_pull_requests
Name to write in SQL
labelNames
labelNames_json
idLabels_json
idMembers_json
boardIds_json
06 · The tables you can write
memberIds_json
memberIds
boardIds
idMembers
trello.trello_cards
cover_json
idLabels
trello.trello_cards
trello.trello_organizations
badges_json
trello.trello_cards
badges
trello.trello_organizations
trello.trello_cards
prefs_json
trello.trello_boards
Name in the data file
trello.trello_boards
Repositories, issues, pull requests, reviews, commits, and releases.
Mailboxes, labels, threads, messages, and attachments.
Channels, users, messages, and files.
Teams, projects, issues, comments, and attachments.
Calendars and events.
Drive users, files, and sheet files stored on Drive.
Presentations, pages, and page elements.
Organizations, boards, lists, cards, checklists, and actions.
Contact records.
Spaces, pages, versions, comments, labels, and attachments.
A log of changes. Skip it unless the task tells you to edit the changelog.
github.github_branches
SQL name: github. Repositories, issues, pull requests, reviews, commits, and releases.
GitHub
Changelog — skip for a normal task
Confluence
Contacts
Trello
Google Slides
Google Sheets
Spreadsheets and sheet grids.
Document bodies.
Google Docs
Google Drive
Google Calendar
Linear
What the rows are
Tables
GitHub
Service
Find the service, open its page, and copy the statement under the table. Confluence is written in the same file as the other services.
Skip the changelog unless the task tells you to edit it.
head_sha
protected
is_default
Yes or no
Yes or no
repo_id
Required
Column
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under branches. 6 columns. 3 must be filled.
INSERT INTO github.github_branches (
repo_id,
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
github.github_commit_map
Add a Required = No column only when you need it. Put its name and its value in the same position.
new_sha
old_sha
repo_id
Required
Column
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under commit_map. 3 columns. 3 must be filled.
INSERT INTO github.github_commit_map (
repo_id,
old_sha,
new_sha
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
github.github_commits
Add a Required = No column only when you need it. Put its name and its value in the same position.
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under commits. 12 columns. 2 must be filled.
committed_date
Date and time
Date and time
authored_date
message
repo_id
Required
Column
The data file says parent_shas. Write parent_shas_json.
Write this in quotes, such as '[]' or '{}'.
parent_shas_json
committer_email
committer_name
committer_login
author_email
author_name
author_login
INSERT INTO github.github_commits (
repo_id
) VALUES (
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
Add a Required = No column only when you need it. Put its name and its value in the same position.
github.github_issues
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under issues. 13 columns. 3 must be filled.
number
Number
author_login
labels_json
assignee_logins_json
pull_request_id
created_at
Date and time
updated_at
Date and time
Write this in quotes, such as '[]' or '{}'.
Write this in quotes, such as '[]' or '{}'.
Copy this, then replace every replace-me
Date and time
closed_at
repo_id
Required
Column
INSERT INTO github.github_issues (
repo_id,
number
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
0 -- required. A number, with no quotes
github.github_labels
Add a Required = No column only when you need it. Put its name and its value in the same position.
repo_id
Required
Column
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under labels. 5 columns. 3 must be filled.
Copy this, then replace every replace-me
description
Required
Column
INSERT INTO github.github_labels (
repo_id,
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Add a Required = No column only when you need it. Put its name and its value in the same position.
github.github_pr_comments
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under pull_request_comments. 6 columns. 2 must be
created_at
Date and time
updated_at
Date and time
author_login
Required
Column
-- required. Replace this text
INSERT INTO github.github_pr_comments (
) VALUES (
'replace-me', -- required. Replace this text
Copy this, then replace every replace-me
'replace-me'
filled.
Add a Required = No column only when you need it. Put its name and its value in the same position.
Number
position
commit_sha
Required
Column
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under pull_request_commits. 4 columns. 3 must be
filled.
github.github_pull_request_commits
Copy this, then replace every replace-me
INSERT INTO github.github_pull_request_commits (
commit_sha
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
github.github_pull_requests
Add a Required = No column only when you need it. Put its name and its value in the same position.
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under pull_requests. 27 columns. 3 must be filled.
The data file says assignee_logins. Write assignee_logins_json.
repo_id
number
merged
Yes or no
locked
Yes or no
author_login
merged_by_login
base_ref
head_ref
base_sha
head_sha
merge_commit_sha
additions
Number
deletions
Number
changed_files
Number
labels_json
Yes or no
Number
Write this in quotes, such as '[]' or '{}'.
Write this in quotes, such as '[]' or '{}'.
Date and time
Date and time
Date and time
Date and time
closed_at
merged_at
updated_at
created_at
Write this in quotes, such as '[]' or '{}'.
logins_json
requested_reviewer_
assignee_logins_json
Required
Column
The data file says labels. Write labels_json.
The data file says requested_reviewer_logins. Write requested_reviewer_logins_json.
Copy this, then replace every replace-me
html_url
Required
Column
INSERT INTO github.github_pull_requests (
repo_id,
number
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
0 -- required. A number, with no quotes
Add a Required = No column only when you need it. Put its name and its value in the same position.
github.github_releases
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under releases. 11 columns. 3 must be filled.
Yes or no
prerelease
Yes or no
author_login
created_at
Date and time
published_at
target_commitish
Copy this, then replace every replace-me
Date and time
tag_name
repo_id
Required
Column
INSERT INTO github.github_releases (
repo_id,
tag_name
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
github.github_repositories
Add a Required = No column only when you need it. Put its name and its value in the same position.
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under repositories. 24 columns. 4 must be filled.
The data file says topics. Write topics_json.
Add a Required = No column only when you need it. Put its name and its value in the same position.
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under review_comments. 11 columns. 2 must be filled.
github.github_review_comments
INSERT INTO github.github_repositories (
full_name,
owner_login
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
html_url
pushed_at
updated_at
Date and time
created_at
Number
open_issues_count
Number
forks_count
Number
watchers_count
stargazers_count
parent_full_name
Number
Copy this, then replace every replace-me
Date and time
Date and time
is_template
Yes or no
topics_json
language
default_branch
Yes or no
disabled
description
owner_login
full_name
Write this in quotes, such as '[]' or '{}'.
Yes or no
archived
license_key
Required
Column
Column
Yes or no
Number
visibility
Required
Add a Required = No column only when you need it. Put its name and its value in the same position.
commit_id
submitted_at
Date and time
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under reviews. 7 columns. 2 must be filled.
author_login
INSERT INTO github.github_reviews (
) VALUES (
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Add a Required = No column only when you need it. Put its name and its value in the same position.
Copy this, then replace every replace-me
commit_id
position
diff_hunk
author_login
github.github_reviews
Number
Date and time
Number
created_at
INSERT INTO github.github_review_comments (
) VALUES (
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Column
Required
Column
Copy this, then replace every replace-me
in_reply_to_id
Required
github.github_tags
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under tags. 9 columns. 4 must be filled.
tag_sha
message
tagger_name
tagger_email
tagger_date
Date and time
Copy this, then replace every replace-me
repo_id
Required
Column
INSERT INTO github.github_tags (
repo_id,
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
github.github_timeline_events
Add a Required = No column only when you need it. Put its name and its value in the same position.
Write this in quotes, such as '[]' or '{}'.
data_json
Date and time
created_at
actor_login
Required
Column
The data file says data. Write data_json.
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under timeline_events. 6 columns. 3 must be filled.
INSERT INTO github.github_timeline_events (
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
html_url
Date and time
Add a Required = No column only when you need it. Put its name and its value in the same position.
avatar_url
Date and time
updated_at
Number
created_at
following
followers
Copy an existing id from HarmonyGames_Gmail/Services_Data/gmail/threads/*.json, under messages, then attachments. 6 columns.
mime_type
public_gists
Number
filename
message_id
Number
public_repos
SQL name: gmail. Mailboxes, labels, threads, messages, and attachments.
Number
Number
site_admin
Yes or no
node_id
github_id
Copy an existing id from HarmonyGames_GitHub/Services_Data/github/data.json, under users. 15 columns. 1 must be filled.
2 must be filled.
gmail.gmail_attachments
INSERT INTO github.github_users (
) VALUES (
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
Column
Required
Column
github.github_users
Required
Add a Required = No column only when you need it. Put its name and its value in the same position.
INSERT INTO gmail.gmail_attachments (
message_id
) VALUES (
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
Add a Required = No column only when you need it. Put its name and its value in the same position.
messages_total
Number
messages_unread
threads_total
threads_unread
Number
user_email
label_id
Required
Column
6 columns. 2 must be filled.
gmail.gmail_label_user_counters
INSERT INTO gmail.gmail_label_user_counters (
label_id,
user_email
) VALUES (
'replace-me', -- required. Replace this text
'name@harmonygames.co' -- required. Replace this text
Copy this, then replace every replace-me
Number
Number
gmail.gmail_labels
Add a Required = No column only when you need it. Put its name and its value in the same position.
Copy an existing id from HarmonyGames_Gmail/Services_Data/gmail/labels.json. 11 columns. 2 must be filled.
The data file says labelListVisibility. Write label_list_visibility.
The data file says messageListVisibility. Write message_list_visibility.
The data file says messagesTotal. Write messages_total.
The data file says messagesUnread. Write messages_unread.
The data file says threadsTotal. Write threads_total.
Number
Number
messages_unread
messages_total
label_list_visibility
visibility
message_list_
Required
Column
The data file says threadsUnread. Write threads_unread.
INSERT INTO gmail.gmail_labels (
) VALUES (
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
color_background
color_text
Number
threads_unread
Number
threads_total
Required
Column
Add a Required = No column only when you need it. Put its name and its value in the same position.
gmail.gmail_messages
Copy an existing id from HarmonyGames_Gmail/Services_Data/gmail/threads/*.json, under messages. 27 columns. 3 must be filled.
The data file says to. Write to_json.
The data file says labelIds. Write label_ids_json.
The data file says reply_to. Write reply_to_json.
The data file says cc. Write cc_json.
The data file says headers. Write headers_json.
The data file says bcc. Write bcc_json.
Write this in quotes, such as '[]' or '{}'.
Write this in quotes, such as '[]' or '{}'.
from_email
from_name
to_json
cc_json
bcc_json
reply_to_json
subject
Number
size_estimate
Date and time
Number
internal_date
history_id
snippet
trash_removed_labels_
label_ids_json
user_email
Required
thread_id
Column
Write this in quotes, such as '[]' or '{}'.
Write this in quotes, such as '[]' or '{}'.
Write this in quotes, such as '[]' or '{}'.
Write this in quotes, such as '[]' or '{}'.
body_html
headers_json
payload_json
in_reply_to
references
mbox_from
date_parsed_source
Write this in quotes, such as '[]' or '{}'.
Leave this blank.
Write this in quotes, such as '[]' or '{}'.
Leave blank
body_text_fts
Write this in quotes, such as '[]' or '{}'.
attachments_meta_json
Required
body_text
Column
Copy this, then replace every replace-me
INSERT INTO gmail.gmail_messages (
thread_id,
user_email
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'name@harmonygames.co' -- required. Replace this text
gmail.gmail_threads
Add a Required = No column only when you need it. Put its name and its value in the same position.
Copy this, then replace every replace-me
history_id
snippet
Required
user_email
Column
Copy an existing id from HarmonyGames_Gmail/Services_Data/gmail/threads/*.json, under (thread object). 4 columns. 2 must be
filled.
INSERT INTO gmail.gmail_threads (
user_email
) VALUES (
'replace-me', -- required. Replace this text
'name@harmonygames.co' -- required. Replace this text
Add a Required = No column only when you need it. Put its name and its value in the same position.
gmail.gmail_users
The data file says historyId. Write history_id.
The data file says emailAddress. Write email_address.
Copy an existing id from HarmonyGames_Gmail/Services_Data/gmail/users.json. 6 columns. 1 must be filled.
Date and time
created_at
members_json
creator_id
Write this in quotes, such as '[]' or '{}'.
Number
created_ts
Yes or no
is_general
Yes or no
is_archived
Yes or no
is_mpim
Number
purpose
Yes or no
Add a Required = No column only when you need it. Put its name and its value in the same position.
num_members
is_private
history_id
Number
threads_total
Number
messages_total
Yes or no
is_channel
The data file says members. Write members_json.
Yes or no
INSERT INTO gmail.gmail_users (
email_address
) VALUES (
'name@harmonygames.co' -- required. Replace this text
Copy an existing id from HarmonyGames_Other_Services/Services_Data/slack/channels.json. 14 columns. 10 must be filled.
email_address
SQL name: slack. Channels, users, messages, and files.
Column
Required
The data file says threadsTotal. Write threads_total.
The data file says created. Write created_ts.
The data file says creator. Write creator_id.
Column
Copy this, then replace every replace-me
Required
slack.slack_channels
The data file says messagesTotal. Write messages_total.
INSERT INTO slack.slack_channels (
is_channel,
is_private,
is_mpim,
is_archived,
is_general,
num_members,
created_ts,
members_json
) VALUES (
'replace-me', -- required. Replace this text
FALSE, -- required. TRUE or FALSE, with no quotes
FALSE, -- required. TRUE or FALSE, with no quotes
FALSE, -- required. TRUE or FALSE, with no quotes
FALSE, -- required. TRUE or FALSE, with no quotes
FALSE, -- required. TRUE or FALSE, with no quotes
FALSE, -- required. TRUE or FALSE, with no quotes
0, -- required. A number, with no quotes
0, -- required. A number, with no quotes
'[]' -- required. Write this in quotes, such as '[]' or '{}'
Copy this, then replace every replace-me
thread_ts
created
updated
channel_id
user_id
Required
Column
7 columns. 5 must be filled.
slack.slack_drafts
Add a Required = No column only when you need it. Put its name and its value in the same position.
Number
INSERT INTO slack.slack_drafts (
user_id,
created,
updated
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
0, -- required. A number, with no quotes
0 -- required. A number, with no quotes
Copy this, then replace every replace-me
Number
Add a Required = No column only when you need it. Put its name and its value in the same position.
permalink
url_private
Yes or no
is_public
Number
created
message_ts
channel_id
user_id
filetype
Copy an existing id from HarmonyGames_Other_Services/Services_Data/slack/files.json. 16 columns. 4 must be filled.
mimetype
Add a Required = No column only when you need it. Put its name and its value in the same position.
INSERT INTO slack.slack_files (
Copy this, then replace every replace-me
content_inline
INSERT INTO slack.slack_emojis (
) VALUES (
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
The data file says user. Write user_id.
content_path
created
preview
user_id
Copy an existing id from HarmonyGames_Other_Services/Services_Data/slack/emojis.json. 5 columns. 1 must be filled.
alias_for
Number
Number
Column
Required
Column
slack.slack_files
Required
slack.slack_emojis
is_public
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
0, -- required. A number, with no quotes
FALSE -- required. TRUE or FALSE, with no quotes
slack.slack_messages
Add a Required = No column only when you need it. Put its name and its value in the same position.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/slack/messages/<channel>/<month>.json. 24 columns. 13 must
be filled.
The data file says user. Write user_id.
user_id
thread_parent_id
thread_ts_legacy
reply_count
Number
reply_users_count
latest_reply
is_activity_message
subtype
reactions_json
files_json
attachments_json
created_at
Date and time
edited_ts
edited_user
client_msg_id
permalink
metadata_json
text_fts
channel_id
Required
Write this in quotes, such as '[]' or '{}'.
Write this in quotes, such as '[]' or '{}'.
Write this in quotes, such as '[]' or '{}'.
Yes or no
Number
Column
The data file says files. Write files_json.
The data file says reactions. Write reactions_json.
The data file says attachments. Write attachments_json.
The data file says channel. Write channel_id.
Leave this blank.
Write this in quotes, such as '[]' or '{}'.
Leave blank
INSERT INTO slack.slack_messages (
channel_id,
reply_count,
reply_users_count,
is_activity_message,
reactions_json,
files_json,
attachments_json,
created_at,
metadata_json
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
0, -- required. A number, with no quotes
0, -- required. A number, with no quotes
FALSE, -- required. TRUE or FALSE, with no quotes
'[]', -- required. Write this in quotes, such as '[]' or '{}'
'[]', -- required. Write this in quotes, such as '[]' or '{}'
'[]', -- required. Write this in quotes, such as '[]' or '{}'
'2026-02-13 12:00:00+00', -- required. Put the date in quotes
'[]' -- required. Write this in quotes, such as '[]' or '{}'
Copy this, then replace every replace-me
INSERT INTO slack.slack_scheduled_messages (
channel_id,
user_id,
post_at,
created
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
0, -- required. A number, with no quotes
0 -- required. A number, with no quotes
Copy this, then replace every replace-me
Number
Number
thread_ts
created
post_at
user_id
channel_id
Required
7 columns. 6 must be filled.
Column
slack.slack_scheduled_messages
Add a Required = No column only when you need it. Put its name and its value in the same position.
Add a Required = No column only when you need it. Put its name and its value in the same position.
slack.slack_users
avatar_url
Yes or no
is_admin
Yes or no
deleted
timezone
Yes or no
display_name
real_name
Required
Column
is_admin,
deleted,
timezone
) VALUES (
'replace-me', -- required. Replace this text
FALSE, -- required. TRUE or FALSE, with no quotes
FALSE, -- required. TRUE or FALSE, with no quotes
FALSE, -- required. TRUE or FALSE, with no quotes
'replace-me' -- required. Replace this text
INSERT INTO slack.slack_users (
Copy this, then replace every replace-me
SQL name: linear. Teams, projects, issues, comments, and attachments.
linear.linear_attachments
Add a Required = No column only when you need it. Put its name and its value in the same position.
Linear
Copy an existing id from HarmonyGames_Other_Services/Services_Data/slack/users.json. 10 columns. 5 must be filled.
Number
rel_path
surface
mime_type
filename
issue_identifier
Required
Column
filled.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/linear/data.json, under attachments. 8 columns. 4 must be
INSERT INTO linear.linear_attachments (
issue_identifier,
filename
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
Add a Required = No column only when you need it. Put its name and its value in the same position.
linear.linear_comments
Copy an existing id from HarmonyGames_Other_Services/Services_Data/linear/data.json, under comments. 8 columns. 7 must be filled.
author_id
parent_id
is_edited
created_at
updated_at
issue_id
Required
Column
Yes or no
author_id,
is_edited,
created_at,
updated_at
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
FALSE, -- required. TRUE or FALSE, with no quotes
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
INSERT INTO linear.linear_comments (
issue_id,
Copy this, then replace every replace-me
linear.linear_issues
Add a Required = No column only when you need it. Put its name and its value in the same position.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/linear/data.json, under issues. 26 columns. 9 must be filled.
The data file says labels. Write labels_json.
The data file says links. Write links_json.
The data file says relations. Write relations_json.
Copy this, then replace every replace-me
Yes or no
Number
time_in_status_
archived_at
canceled_at
completed_at
INSERT INTO linear.linear_issues (
priority,
labels_json,
links_json,
relations_json,
is_archived,
created_at,
updated_at
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
0, -- required. A number, with no quotes
'[]', -- required. Write this in quotes, such as '[]' or '{}'
'[]', -- required. Write this in quotes, such as '[]' or '{}'
'[]', -- required. Write this in quotes, such as '[]' or '{}'
started_at
due_date
estimate
priority
Write this in quotes, such as '[]' or '{}'.
description
Number
number
Write this in quotes, such as '[]' or '{}'.
cycle_id
state_id
updated_at
creator_id
Write this in quotes, such as '[]' or '{}'.
created_at
assignee_id
is_archived
parent_id
relations_json
team_id
links_json
project_id
labels_json
minutes
identifier
Number
Column
Number
Required
FALSE, -- required. TRUE or FALSE, with no quotes
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Add a Required = No column only when you need it. Put its name and its value in the same position.
linear.linear_projects
Copy an existing id from HarmonyGames_Other_Services/Services_Data/linear/data.json, under projects. 14 columns. 8 must be
filled.
summary
description
lead_id
priority
start_date
target_date
labels_json
is_archived
Yes or no
created_at
updated_at
Write this in quotes, such as '[]' or '{}'.
Number
INSERT INTO linear.linear_projects (
team_id,
priority,
labels_json,
is_archived,
created_at,
updated_at
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
0, -- required. A number, with no quotes
'[]', -- required. Write this in quotes, such as '[]' or '{}'
FALSE, -- required. TRUE or FALSE, with no quotes
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
team_id
Required
Column
The data file says labels. Write labels_json.
Add a Required = No column only when you need it. Put its name and its value in the same position.
linear.linear_team_memberships
Copy an existing id from HarmonyGames_Other_Services/Services_Data/linear/data.json, under team_memberships. 4 columns. 4 must
be filled.
created_at
user_id
Required
team_id
Column
INSERT INTO linear.linear_team_memberships (
team_id,
user_id,
created_at
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
linear.linear_teams
Add a Required = No column only when you need it. Put its name and its value in the same position.
updated_at
created_at
is_archived
description
Required
Column
Copy an existing id from HarmonyGames_Other_Services/Services_Data/linear/data.json, under teams. 7 columns. 6 must be filled.
Yes or no
INSERT INTO linear.linear_teams (
is_archived,
created_at,
updated_at
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
FALSE, -- required. TRUE or FALSE, with no quotes
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
Add a Required = No column only when you need it. Put its name and its value in the same position.
linear.linear_users
Copy an existing id from HarmonyGames_Other_Services/Services_Data/linear/data.json, under users. 8 columns. 6 must be filled.
display_name
avatar_url
is_active
created_at
updated_at
Yes or no
Copy this, then replace every replace-me
Required
Column
INSERT INTO linear.linear_users (
is_active,
created_at,
updated_at
) VALUES (
'replace-me', -- required. Replace this text
'name@harmonygames.co', -- required. Replace this text
'replace-me', -- required. Replace this text
FALSE, -- required. TRUE or FALSE, with no quotes
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
gcal.gcal_calendars
SQL name: gcal. Calendars and events.
Google Calendar
Add a Required = No column only when you need it. Put its name and its value in the same position.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/gcal/data.json, under calendars. 9 columns. 2 must be filled.
Write this in quotes, such as '[]' or '{}'.
Yes or no
primary
time_zone
description
visibility
shared_with_emails_
owner_email
summary
calendar_id
Required
Column
The data file says shared_with_emails. Write shared_with_emails_json.
Copy this, then replace every replace-me
access_role
Required
Column
INSERT INTO gcal.gcal_calendars (
calendar_id,
summary
) VALUES (
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
gcal.gcal_events
Add a Required = No column only when you need it. Put its name and its value in the same position.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/gcal/data.json, under events. 23 columns. 2 must be filled.
calendar_id
summary
description
location
start_ts
Date and time
Required
event_id
Column
transparency
rrule_json
recurring_event_id
original_start_json
sequence
created
updated
hangout_link
visibility
status
Write this in quotes, such as '[]' or '{}'.
Write this in quotes, such as '[]' or '{}'.
attendees_json
creator_email
organizer_email
end_json
start_json
Date and time
Write this in quotes, such as '[]' or '{}'.
Write this in quotes, such as '[]' or '{}'.
Date and time
Date and time
Number
Write this in quotes, such as '[]' or '{}'.
The data file says rrule. Write rrule_json.
The data file says start. Write start_json.
The data file says attendees. Write attendees_json.
The data file says end. Write end_json.
Copy this, then replace every replace-me
ical_uid
Required
Column
INSERT INTO gcal.gcal_events (
event_id,
calendar_id
) VALUES (
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
SQL name: gdrive. Drive users, files, and sheet files stored on Drive.
gdrive.drive_files
Google Drive
Add a Required = No column only when you need it. Put its name and its value in the same position.
The data file says owners. Write owners_json.
filled.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/gdrive/data.json, under drive_files. 20 columns. 3 must be
owners_json
Write this in quotes, such as '[]' or '{}'.
modified_time
Date and time
created_time
Date and time
Number
trashed
starred
Yes or no
content_path
web_view_link
icon_link
description
visibility
Write this in quotes, such as '[]' or '{}'.
visibility_role
shared_roles_json
Write this in quotes, such as '[]' or '{}'.
Yes or no
shared_with_emails_
Write this in quotes, such as '[]' or '{}'.
owner_email
parents_json
mime_type
Required
Column
The data file says parents. Write parents_json.
The data file says shared_with_emails. Write shared_with_emails_json.
INSERT INTO gdrive.drive_files (
mime_type
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
content_text
Required
Column
gdrive.drive_sheets
Add a Required = No column only when you need it. Put its name and its value in the same position.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/gdrive/data.json, under drive_sheets. 6 columns. 3 must be
filled.
Number
INSERT INTO gdrive.drive_sheets (
spreadsheet_id,
sheet_id,
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
Number
Number
column_count
row_count
Required
sheet_id
spreadsheet_id
Column
gdrive.drive_users
Add a Required = No column only when you need it. Put its name and its value in the same position.
Copy this, then replace every replace-me
INSERT INTO gdrive.drive_users (
display_name
photo_link
display_name
Required
Column
filled.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/gdrive/data.json, under drive_users. 4 columns. 3 must be
) VALUES (
'replace-me', -- required. Replace this text
'name@harmonygames.co', -- required. Replace this text
'replace-me' -- required. Replace this text
Add a Required = No column only when you need it. Put its name and its value in the same position.
SQL name: gdocs. Document bodies.
gdocs.docs_documents
Google Docs
Copy an existing id from HarmonyGames_Other_Services/Services_Data/gdocs/data.json, under docs_documents. 11 columns. 2 must
The data file says style_runs. Write style_runs_json.
Date and time
modified_time
created_time
drive_file_id
Write this in quotes, such as '[]' or '{}'.
revision_id
style_runs_json
body_text
visibility
Write this in quotes, such as '[]' or '{}'.
shared_with_emails_
owner_email
Required
document_id
Column
The data file says shared_with_emails. Write shared_with_emails_json.
be filled.
Copy this, then replace every replace-me
Date and time
INSERT INTO gdocs.docs_documents (
document_id,
) VALUES (
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
SQL name: gsheets. Spreadsheets and sheet grids.
Google Sheets
Add a Required = No column only when you need it. Put its name and its value in the same position.
gsheets.sheets_sheets
The file is HarmonyGames_Other_Services/Services_Data/gsheets/data.json. It is not unpacked here, so use the column list. 7 columns. 3
must be filled.
grid_json
Number
column_count
Write this in quotes, such as '[]' or '{}'.
INSERT INTO gsheets.sheets_sheets (
spreadsheet_id,
sheet_id,
) VALUES (
'replace-me', -- required. Replace this text
0, -- required. A number, with no quotes
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
Number
Number
row_count
Number
sheet_id
Required
spreadsheet_id
Column
Date and time
modified_time
Date and time
created_time
drive_file_id
INSERT INTO gsheets.sheets_spreadsheets (
spreadsheet_id,
) VALUES (
'replace-me', -- required. Replace this text
Copy this, then replace every replace-me
-- required. Replace this text
'replace-me'
visibility
Write this in quotes, such as '[]' or '{}'.
shared_with_emails_
owner_email
spreadsheet_id
Required
Column
must be filled.
The file is HarmonyGames_Other_Services/Services_Data/gsheets/data.json. It is not unpacked here, so use the column list. 8 columns. 2
gsheets.sheets_spreadsheets
Add a Required = No column only when you need it. Put its name and its value in the same position.
Add a Required = No column only when you need it. Put its name and its value in the same position.
SQL name: gslides. Presentations, pages, and page elements.
gslides.slides_page_elements
Google Slides
Copy an existing id from HarmonyGames_Other_Services/Services_Data/gslides/data.json, under slides_presentations, then
Number
width_emu
height_emu
Number
placeholder_type
object_id
page_object_id
Required
presentation_id
Column
pages, then elements. 10 columns. 3 must be filled.
INSERT INTO gslides.slides_page_elements (
presentation_id,
page_object_id,
object_id
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
Number
Number
Add a Required = No column only when you need it. Put its name and its value in the same position.
gslides.slides_pages
pages. 4 columns. 2 must be filled.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/gslides/data.json, under slides_presentations, then
Number
layout
object_id
Required
presentation_id
Column
INSERT INTO gslides.slides_pages (
presentation_id,
object_id
) VALUES (
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
Add a Required = No column only when you need it. Put its name and its value in the same position.
gslides.slides_presentations
Copy an existing id from HarmonyGames_Other_Services/Services_Data/gslides/data.json, under slides_presentations. 9 columns.
2 must be filled.
owner_email
shared_with_emails_
Write this in quotes, such as '[]' or '{}'.
INSERT INTO gslides.slides_presentations (
presentation_id,
) VALUES (
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Date and time
Copy this, then replace every replace-me
Add a Required = No column only when you need it. Put its name and its value in the same position.
Trello
Date and time
modified_time
created_time
revision_id
drive_file_id
visibility
presentation_id
Required
Column
The data file says shared_with_emails. Write shared_with_emails_json.
trello.trello_actions
SQL name: trello. Organizations, boards, lists, cards, checklists, and actions.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/trello/data.json, under actions. 7 columns. 3 must be filled.
Date and time
idMemberCreator
idBoard
idCard
data_json
Required
Column
The data file says data. Write data_json.
Write this in quotes, such as '[]' or '{}'.
INSERT INTO trello.trello_actions (
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'2026-02-13 12:00:00+00' -- required. Put the date in quotes
Copy this, then replace every replace-me
trello.trello_attachments
Add a Required = No column only when you need it. Put its name and its value in the same position.
idCard
mimeType
Date and time
idMember
isUpload
Yes or no
rel_path
Number
INSERT INTO trello.trello_attachments (
idCard
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
Required
Column
filled.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/trello/data.json, under attachments. 10 columns. 3 must be
trello.trello_boards
Add a Required = No column only when you need it. Put its name and its value in the same position.
Yes or no
Required
closed
Column
The data file says prefs. Write prefs_json.
The data file says labelNames. Write labelNames_json.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/trello/data.json, under boards. 13 columns. 2 must be filled.
nodeId
shortUrl
idOrganization
Required
Column
dateLastView
Date and time
prefs_json
Write this in quotes, such as '[]' or '{}'.
labelNames_json
Write this in quotes, such as '[]' or '{}'.
Write this in quotes, such as '[]' or '{}'.
INSERT INTO trello.trello_boards (
) VALUES (
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
memberIds_json
Date and time
dateLastActivity
trello.trello_cards
Add a Required = No column only when you need it. Put its name and its value in the same position.
idBoard
idList
Number
closed
Yes or no
Date and time
dueComplete
idMembers_json
idLabels_json
idShort
shortLink
shortUrl
Write this in quotes, such as '[]' or '{}'.
Number
Required
Column
The data file says idMembers. Write idMembers_json.
The data file says cover. Write cover_json.
The data file says idLabels. Write idLabels_json.
The data file says badges. Write badges_json.
Yes or no
Copy an existing id from HarmonyGames_Other_Services/Services_Data/trello/data.json, under cards. 18 columns. 4 must be filled.
Write this in quotes, such as '[]' or '{}'.
Write this in quotes, such as '[]' or '{}'.
Copy this, then replace every replace-me
Write this in quotes, such as '[]' or '{}'.
INSERT INTO trello.trello_cards (
idBoard,
idList
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
badges_json
cover_json
Date and time
dateLastActivity
Required
Column
Add a Required = No column only when you need it. Put its name and its value in the same position.
trello.trello_check_items
idChecklist
Required
Column
filled.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/trello/data.json, under check_items. 7 columns. 3 must be
Copy this, then replace every replace-me
Date and time
idMember
Number
INSERT INTO trello.trello_check_items (
idChecklist
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
trello.trello_checklists
Add a Required = No column only when you need it. Put its name and its value in the same position.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/trello/data.json, under checklists. 5 columns. 4 must be
filled.
Required
Column
Number
Required
idBoard
idCard
Column
INSERT INTO trello.trello_checklists (
idCard,
idBoard
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
Add a Required = No column only when you need it. Put its name and its value in the same position.
trello.trello_labels
idBoard
Required
Column
Copy an existing id from HarmonyGames_Other_Services/Services_Data/trello/data.json, under labels. 4 columns. 2 must be filled.
idBoard
) VALUES (
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
INSERT INTO trello.trello_labels (
Copy this, then replace every replace-me
Yes or no
Number
Yes or no
softLimit
subscribed
Number
closed
idBoard
Required
Column
Copy an existing id from HarmonyGames_Other_Services/Services_Data/trello/data.json, under lists. 7 columns. 3 must be filled.
trello.trello_lists
Add a Required = No column only when you need it. Put its name and its value in the same position.
INSERT INTO trello.trello_lists (
idBoard
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
username
fullName
avatarUrl
memberType
confirmed
Yes or no
Required
Column
Copy an existing id from HarmonyGames_Other_Services/Services_Data/trello/data.json, under members. 9 columns. 3 must be filled.
initials
fullName
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
INSERT INTO trello.trello_members (
username,
Copy this, then replace every replace-me
Add a Required = No column only when you need it. Put its name and its value in the same position.
displayName
Required
Column
The data file says memberIds. Write memberIds_json.
The data file says boardIds. Write boardIds_json.
filled.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/trello/data.json, under organizations. 7 columns. 3 must be
trello.trello_organizations
trello.trello_members
Add a Required = No column only when you need it. Put its name and its value in the same position.
Date and time
Copy this, then replace every replace-me
description
status
Date and time
country
city_living
nationality
updated_at
Copy an existing id from HarmonyGames_Other_Services/Services_Data/contacts/contacts.json, under contacts. 17 columns. 3 must
created_at
gender
SQL name: contacts. Contact records.
Yes or no
Copy this, then replace every replace-me
Number
is_user
address
last_name
Add a Required = No column only when you need it. Put its name and its value in the same position.
INSERT INTO contacts.contacts (
contact_id,
first_name
boardIds_json
Write this in quotes, such as '[]' or '{}'.
memberIds_json
contact_id
Write this in quotes, such as '[]' or '{}'.
website
Column
Required
INSERT INTO trello.trello_organizations (
displayName
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
be filled.
Column
contacts.contacts
Contacts
Required
first_name,
last_name
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Confluence
Add a Required = No column only when you need it. Put its name and its value in the same position.
SQL name: confluence. Spaces, pages, versions, comments, labels, and attachments.
SAME FILE AS THE OTHER SERVICES
A Confluence page, comment, or label goes in 01_Universe_Inject.sql with the rest of your SQL. Copy the statement under
the table and replace every replace-me.
confluence.confluence_attachments
columns. 8 must be filled.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json, under attachments. 9
media_type
file_size
Number
version
Number
author_id
created_at
updated_at
page_id
Required
Column
INSERT INTO confluence.confluence_attachments (
page_id,
media_type,
file_size,
version,
created_at,
updated_at
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
0, -- required. A number, with no quotes
0, -- required. A number, with no quotes
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
Add a Required = No column only when you need it. Put its name and its value in the same position.
confluence.confluence_comments
Copy an existing id from HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json, under comments. 7
columns. 6 must be filled.
Add a Required = No column only when you need it. Put its name and its value in the same position.
confluence.confluence_labels
INSERT INTO confluence.confluence_comments (
page_id,
author_id,
created_at,
updated_at
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
updated_at
created_at
parent_id
author_id
Required
page_id
Column
columns. 5 must be filled.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json, under labels. 5
prefix
created_at
page_id
Required
Column
INSERT INTO confluence.confluence_labels (
page_id,
prefix,
created_at
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
Copy this, then replace every replace-me
Add a Required = No column only when you need it. Put its name and its value in the same position.
-- required. Replace this text
confluence.confluence_page_versions
'replace-me'
Number
created_at
message
author_id
number
Required
page_id
Column
Copy an existing id from HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json, under page_versions.
8 columns. 6 must be filled.
INSERT INTO confluence.confluence_page_versions (
page_id,
number,
created_at
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
0, -- required. A number, with no quotes
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
confluence.confluence_pages
Add a Required = No column only when you need it. Put its name and its value in the same position.
Number
version
status
body_format
parent_id
space_id
Required
Column
columns. 9 must be filled.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json, under pages. 11
updated_at
Required
created_at
author_id
Column
INSERT INTO confluence.confluence_pages (
space_id,
body_format,
status,
version,
created_at,
updated_at
) VALUES (
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
0, -- required. A number, with no quotes
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
status
description
homepage_id
created_at
updated_at
INSERT INTO confluence.confluence_spaces (
status,
created_at,
updated_at
) VALUES (
'replace-me', -- required. Replace this text
Copy this, then replace every replace-me
Required
Column
columns. 7 must be filled.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json, under spaces. 9
confluence.confluence_spaces
Add a Required = No column only when you need it. Put its name and its value in the same position.
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
confluence.confluence_users
Add a Required = No column only when you need it. Put its name and its value in the same position.
display_name
is_active
created_at
updated_at
Yes or no
account_id
Required
Column
columns. 6 must be filled.
Copy an existing id from HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json, under users. 7
INSERT INTO confluence.confluence_users (
display_name,
is_active,
created_at,
updated_at
) VALUES (
'replace-me', -- required. Replace this text
'name@harmonygames.co', -- required. Replace this text
'replace-me', -- required. Replace this text
FALSE, -- required. TRUE or FALSE, with no quotes
'replace-me', -- required. Replace this text
'replace-me' -- required. Replace this text
Copy this, then replace every replace-me
Changelog — skip for a normal task
Add a Required = No column only when you need it. Put its name and its value in the same position.
8 columns. 4 must be filled.
public._changelog
SQL name: public. A log of changes. Skip it unless the task tells you to edit the changelog.
Filled in for you. Leave it out.
Filled in for you. Leave it out.
Number
Required
Date and time
timestamp
Column
This table records changes. Do not add a row here unless the task tells you to edit the changelog.
SKIP THIS FOR A NORMAL TASK
changed_fields
summary
operation
Required
table_name
schema_name
Column
Write this in quotes, such as '[]' or '{}'.
06 · Snowflake — do not inject
DO NOT PUT THESE TABLES IN AN INJECTION FILE
Snowflake is the analytics database. A task may ask the agent to read it. Do not add, edit, or delete these rows in an injection
file. The lists below are only so you can recognize a table name.
Daily active users, retention cohorts, level performance · 10 tables
ANALYTICS.GAME_EVENTS
ANALYTICS.GAME_EVENTS.PLAYER_DAILY_PROGRESS
Per-player daily snapshot: level reached, sessions, coins, boosters, levels attempted/completed, purchase flag. coins_earned is what play paid
out; coins bought from the store arrive as iap_grant rows in RESOURCE_FLOW_EVENTS and are not counted here. coins_spent and
boosters_used count purchases at each game's shipped booster prices, so a player-day with no affordable purchase reads zero, and
boosters_used is zero throughout for Combo Fighter, which ships none. made_purchase is reconciled against IAP_TRANSACTIONS at the gamedate grain. Holds 183,033 player-days over 31,210 distinct players, against 31,210 installs lifetime -- a player appears here only on days they
total_session_minutes
Number
coins_earned
Number
Number
sessions_count
Number
current_level
Highest level unlocked
Date and time
Number
made_purchase
levels_completed
levels_attempted
Number
boosters_used
coins_spent
country
platform
game_id
renamed player key; joins to
PLAYER_DAILY_PROGRESS.player_id
Comment
player_id
Required
Column
actually played. Aggregated upstream of the retained event tables. RAW_GAME_EVENTS and STG_EVENTS_ENRICHED retain a 1:8 session
sample, and PROGRESSION_EVENTS, SESSION_LEVEL_EVENTS and AD_IMPRESSION_EVENTS a 1:16 sample, so a recount from those tables
will not match these totals.
Yes or no
Number
Number
ANALYTICS.GAME_EVENTS.DAILY_ACTIVE_USERS
Daily aggregated user metrics per game and platform. Includes DAU, new/returning split, session counts, average session length, and D1/D7/D30
retention percentages. combo_fighter from 2025-12-27, domino_delights from 2023-11-01. Zombie Match 3D is ABSENT BY DESIGN and its
absence is a fact about the company, not a gap: it never had a DAU instrument. Derive ZM3D volume from
ANALYTICS.MARKETING.INSTALL_EVENTS and ANALYTICS.GAME_EVENTS.USER_COHORT_RETENTION instead. Do not synthesise a ZM3D
Calendar date (UTC)
ios | android
Daily active users. GRAIN: one row per game x platform x date -
d30_retention_pct
Number
d7_retention_pct
d1_retention_pct
avg_session_minutes
First-time users that day
total_sessions
- SUM the platform rows to get a game's DAU for a day.
AVG(dau) averages PLATFORM ROWS, not days, and halves the
answer for any two-platform game.
returning_users
Number
new_users
Number
combo_fighter | domino_delights -- zombie_match_3d is absent
by design, see the table comment
Date and time
platform
Comment
game_id
Required
Column
DAU series. Aggregated upstream of the retained event tables. RAW_GAME_EVENTS and STG_EVENTS_ENRICHED retain a 1:8 session sample,
and PROGRESSION_EVENTS, SESSION_LEVEL_EVENTS and AD_IMPRESSION_EVENTS a 1:16 sample, so a recount from those tables will not
match these totals.
Number
Number
Number
NULL until the 7-day window closes
NULL until the 30-day window closes
ANALYTICS.GAME_EVENTS.LEVEL_PERFORMANCE
Number
% of Day-0 cohort returning on Day 1
Number
Per-level aggregates, 5,497 rows. Level ranges present: combo_fighter 1-442, domino_delights 1-4755, zombie_match_3d 1-300. fail_reason_top
is the modal failure for that level and uses each title's OWN fail vocabulary -- the three games do not share one. Aggregated upstream of the
retained event tables. RAW_GAME_EVENTS and STG_EVENTS_ENRICHED retain a 1:8 session sample, and PROGRESSION_EVENTS,
avg_attempts
completion_rate_pct
Number
avg_time_seconds
Number
boosters_used_per_
Number
Average attempts to complete (1.0 = first try always)
% of players who complete level on a given attempt
Most common failure reason
Number
Date and time
created_date
fail_reason_top
tutorial | standard | hard | boss
attempt
Number
level_type
level_number
game_id
Comment
Required
Column
SESSION_LEVEL_EVENTS and AD_IMPRESSION_EVENTS a 1:16 sample, so a recount from those tables will not match these totals.
ANALYTICS.GAME_EVENTS.USER_COHORT_RETENTION
Number
Number
% returning on Day 1
Number
NULL until the 7-day window closes
Number
NULL until the 14-day window closes
Number
NULL until the 30-day window closes
NULL until the 60-day window closes
avg_iap_per_user
pct_ever_paid
Week of install (Monday)
Date and time
Number
ANALYTICS.GAME_EVENTS.DIM_PLAYER
% of cohort who ever made an IAP
Average IAP spend per install in the cohort
Number
Number
installs
platform
Comment
game_id
Required
cohort_week
Column
a 1:16 sample, so a recount from those tables will not match these totals.
Weekly install cohorts with Day 1 through Day 60 retention, 333 cohort rows. D1 across cohorts ranges 0.0%-75.0%, unweighted mean 24.4%
over all 333 cohorts. Per-cohort scatter is wide. Aggregated upstream of the retained event tables. RAW_GAME_EVENTS and
STG_EVENTS_ENRICHED retain a 1:8 session sample, and PROGRESSION_EVENTS, SESSION_LEVEL_EVENTS and AD_IMPRESSION_EVENTS
Player dimension for the install universe, 31,210 rows. Acquisition channels are derived from INSTALL_EVENTS and match AD_SPEND_DAILY.
Channel mix: adjoe 8,730, applovin 699, google_uac 256, meta 1,455, organic 15,610, unity_ads 4,460.
last_seen_date
primary_game_id
platform
country_code
acquisition_channel
lifecycle_bucket
is_payer
Yes or no
max_level_seen
Number
total_sessions_est
Number
player_traits
object
Date and time
renamed player key; joins to
PLAYER_DAILY_PROGRESS.player_id
Date and time
first_seen_date
Comment
player_id
Required
Column
ANALYTICS.GAME_EVENTS.DAILY_METRICS_AGG
Daily metrics mart derived from the DAU and revenue tables. Aggregated upstream of the retained event tables. RAW_GAME_EVENTS and
STG_EVENTS_ENRICHED retain a 1:8 session sample, and PROGRESSION_EVENTS, SESSION_LEVEL_EVENTS and AD_IMPRESSION_EVENTS
a 1:16 sample, so a recount from those tables will not match these totals.
Date and time
Comment
Required
title_id
metric_date
Column
total_sessions
Number
iap_revenue_usd
Number
ad_revenue_usd
Number
total_revenue_usd
Number
arpu_usd
Number
Number
new_users
Number
Comment
platform
Required
Column
ANALYTICS.GAME_EVENTS.SESSION_LEVEL_EVENTS
metric_flag
Number
source_rows
Derived from RAW_EVENTS and retained at a 1:16 session sample; sampling is by session, so every event of a retained session is present. Raw
level attempt events (sampled). Each row = one player action: level_started, level_completed, level_failed, booster_used, or tutorial_step.
LEVEL_PERFORMANCE is aggregated from the full upstream event stream before sampling, not from this table, so a recount here will not
player_id
renamed player key; joins to
PLAYER_DAILY_PROGRESS.player_id
game_id
level_number
Number
event_type
level_started | level_completed | level_failed | booster_used
Comment
Required
Date and time
Date and time
Number
quarter
week_start
date_key
win | out_of_moves | time_limit | board_stuck (domino_delights) |
hp_depleted | out_of_space (zombie_match_3d) | knocked_out
Calendar dimension over the active warehouse period.
(combo_fighter)
ANALYTICS.GAME_EVENTS.DIM_DATE
Column
Number
Number
attempt_number
result
booster_type
duration_seconds
country
platform
Date and time
event_timestamp
Comment
event_id
Required
Column
reproduce it.
company_phase
is_revenue_country
is_ua_country
primary_market_tier
currency_code
gdpr_region
first_seen_date
Yes or no
Yes or no
region
country_name
Comment
Required
country_code
Country dimension distinguishing revenue countries from UA-only countries.
ANALYTICS.GAME_EVENTS.DIM_COUNTRY
Number
fiscal_month
Yes or no
is_weekend
day_of_week
Number
Comment
Required
Column
Column
ANALYTICS.GAME_EVENTS.DIM_DEVICE
Date and time
Yes or no
Number
Consumer marketing name for the hardware code, e.g.
iPhone11,6 = iPhone XS Max; joins
INSTALL_EVENTS.device_model. NULL for tablets (no installtable equivalent).
phone | tablet
Estimated retail value used for LTV/segmentation
Number
Date and time
Yes or no
est_market_value_usd
first_seen_date
is_tablet
ios | android
form_factor
os_version
platform
S23+ (joins RAW_GAME_EVENTS.device.model,
CLIENT_ERROR_EVENTS.device_model)
Canonical hardware code, e.g. iPhone14,5 / Samsung Galaxy
device_model_generic
Comment
device_model
device_id
Required
Column
Device dimension: the phone/tablet models seen across HG4 titles with platform, OS version, form factor, and an estimated market value.
Anchored to the device deep-dive device space (iPhone/iPad + Samsung/Pixel/Oppo/OnePlus). Domino Delights install sample skews ~77% iOS.
Ad spend, install attribution, ROAS · 8 tables
ANALYTICS.MARKETING.AD_SPEND_DAILY
ANALYTICS.MARKETING
Daily marketing spend by game, channel, and country. Channels present: adjoe, applovin, google_uac, meta, unity_ads. By game -combo_fighter: meta; domino_delights: adjoe, applovin, google_uac, meta, unity_ads; zombie_match_3d: applovin, meta, unity_ads. Spend runs
Comment
Date and time
channel
country
spend_usd
impressions
clicks
installs
cpi_usd
day1_roas
meta | google_uac | unity_ads | applovin | adjoe
Number
Number
ANALYTICS.MARKETING.INSTALL_EVENTS
Revenue / spend ratio on Day 1 post-install
Number
Number
Number
Number
game_id
Required
Column
2024-09-01 to 2026-02-09 (attribution MMP = Singular). No blended CPI is quoted: compute it from these rows for the window you care about,
because a single blended figure hides a 3x spread across channels and months.
Individual install events, 31,210 rows: Domino Delights 22,980, Zombie Match 3D 7,329, Combo Fighter 901. Lifetime distinct players are in
DIM_PLAYER. Combo Fighter runs 2025-12-27 to 2026-02-09 (615 paid / 286 organic); no IAP sales recorded for this title, though a store is
present - see IAP_TRANSACTIONS. Domino Delights spans three phases: closed alpha from 2023-11-01 (internal testers, pre-launch),
device_model_generic
marketing name; device_model holds the canonical hardware
is_organic
cpi_usd
attributed_campaign
os_version
device_model
platform
country
Date and time
channel
PLAYER_DAILY_PROGRESS.player_id
game_id
renamed player key; joins to
player_id
Comment
install_id
Required
Column
unannounced Google Play availability from ~2024-08, and the US soft launch 2025-04-11. 3,784 of its installs predate the US soft launch, so the
earliest install date for this title is not its launch date.
Yes or no
Number
0.0 for organic
ANALYTICS.MARKETING.SINGULAR_INSTALLS_RAW
Singular MMP landing table derived from INSTALL_EVENTS. singular_id equals INSTALL_EVENTS.install_id for joinability; install_meta and
event_value are nested raw payloads. Singular was HG's operational MMP (AppsFlyer was historical/referenced only).
media_source
campaign_key
country_code
platform
customer_user_id
renamed player key; joins to
PLAYER_DAILY_PROGRESS.player_id
cost_usd
install_meta
event_value
Date and time
Comment
install_time
Required
singular_id
Column
ANALYTICS.MARKETING.UA_SPEND_UNIFIED_V2
variant
object
Number
installs_current
Number
cpi_current
Number
source_count
Number
source_meta
Number
Number
Comment
Required
Date and time
review_date
review_id
App-store review stream with one-star spikes aligned to incidents.
Column
object
ANALYTICS.MARKETING.APP_STORE_REVIEWS
Number
clicks_current
impressions_current
spend_current
country_code
campaign_key
network_name
title_id
Comment
Date and time
Required
report_date
Column
Versioned paid-UA spend mart for all titles (includes 152 combo_fighter rows), reconciled from AD_SPEND_DAILY and carrying source_meta for
the versioned calculation.
PLAYER_DAILY_PROGRESS.player_id
Number
Date and time
mmp_reported_at
Yes or no
is_organic
cost_usd
campaign_key
media_source
ANALYTICS.MARKETING.INSTALL_ATTRIBUTION
os_version
device_model_generic
spend_usd
marketing name, joins DIM_DEVICE.device_model_generic
Comment
country
Required
Date and time
canonical HARDWARE code, joins DIM_DEVICE.device_model
device_model
What we paid the networks (as the MMP reported it).
country
ANALYTICS.MARKETING.AD_SPEND
incident_related
sentiment_score
platform
campaign_key
app_version
network
review_text
game_id
Number
game_id
rating
Yes or no
country_code
organic | meta | google_uac | unity_ads | applovin | adjoe
Column
platform
Number
install_ts
player_id
Date and time
title_id
renamed player key; joins to
install_id
object
review_meta
Comment
Column
Column
Required
Installs, carrying player_id.
topic_bucket
Comment
Number
Required
country
rating
app_version
topic_bucket
ANALYTICS.MONETIZATION.IAP_TRANSACTIONS
IAP transactions and daily revenue · 6 tables
ANALYTICS.MONETIZATION
Number
platform
game_id
Date and time
Comment
Required
review_id
Player-submitted review text from the app stores.
Column
ANALYTICS.MARKETING.STORE_REVIEWS
Number
installs_reported
Number
clicks
Number
Comment
impressions
Required
Column
Individual in-app purchase records, 977 rows (2024-02-23 to 2026-02-09). By game: domino_delights 976, zombie_match_3d 1. SKUs present:
bundle.tier2.abandoned_backpack, dd_coins_large, dd_coins_medium, dd_coins_mega, dd_coins_small, dd_remove_ads, dd_starter_pack. Titles
absent from this table recorded no purchases; absence here means no sales, not the absence of a store. NET of refunds:
ANALYTICS.MONETIZATION.STORE_TRANSACTIONS holds 993 gross receipts = 977 completed + 16 refunded ($125.84); the refunded ones are
excluded here. The two tables share transaction_id, so this is a strict subset - use that table for receipt counts and this one for revenue.
Date and time
game_id
platform
country
product_sku
product_name
price_usd
is_subscription
player_id
Comment
Required
transaction_id
Column
ANALYTICS.MONETIZATION.REVENUE_DAILY
renamed player key; joins to
PLAYER_DAILY_PROGRESS.player_id
Yes or no
Number
Daily revenue aggregated by game, platform, and top country. Includes both IAP and ad revenue. Best single day by game -- combo_fighter peaks
at $0.73 on 2026-01-28; domino_delights peaks at $159.03 on 2025-06-28; zombie_match_3d peaks at $1.99 on 2025-07-31. Aggregated
upstream of the retained event tables. RAW_GAME_EVENTS and STG_EVENTS_ENRICHED retain a 1:8 session sample, and
PROGRESSION_EVENTS, SESSION_LEVEL_EVENTS and AD_IMPRESSION_EVENTS a 1:16 sample, so a recount from those tables will not
match these totals.
Number
Number
Total revenue for the day. GRAIN: one row per game x platform
x country_top -- SUM before comparing to any daily figure; an
average over these rows is not a daily average.
Average revenue per user (total revenue / DAU)
ANALYTICS.MONETIZATION.REVENUE_DAILY_V2
Average revenue per paying user
Number
Number
arppu_usd
arpu_usd
Number
paying_users
Number
total_revenue_usd
ad_revenue_usd
iap_revenue_usd
country_top
Comment
platform
Date and time
Required
game_id
Column
Versioned all-title (includes 90 combo_fighter) revenue mart. Includes Combo Fighter (90 rows) and keeps a calc_metadata payload explaining the
scope. Aggregated upstream of the retained event tables. RAW_GAME_EVENTS and STG_EVENTS_ENRICHED retain a 1:8 session sample, and
PROGRESSION_EVENTS, SESSION_LEVEL_EVENTS and AD_IMPRESSION_EVENTS a 1:16 sample, so a recount from those tables will not
match these totals.
country_code
iap_revenue_current
ad_revenue_current
total_revenue_current
paying_users_current
arpu_current
Number
source_table
calc_metadata
object
platform
title_id
Date and time
Comment
report_date
Required
Column
Number
Number
Number
Number
ANALYTICS.MONETIZATION.VIRTUAL_CURRENCY_LEDGER
Date and time
event_date
Comment
Required
ledger_id
Column
Virtual-currency ledger, a 1:1 projection of RESOURCE_FLOW_EVENTS keyed by ledger_meta.source_event_id, preserving the Apr 2025 coincrisis economy version. Amounts and running balances are the source row's, not recomputed.
renamed player key; joins to
PLAYER_DAILY_PROGRESS.player_id
item_id
balance_after
economy_version
ledger_meta
object
Number
Required
Comment
ANALYTICS.MONETIZATION.AD_REVENUE
network
placement
impressions
Number
BILLABLE impressions as reported by the ad network - what the
network paid on, not what the client fired. Legitimately much
paid | accrued_unpaid
Number
counts, and do not truncate either side to make them agree
accrued_vs_paid
reach this column. The two tables reconcile on MONEY, not on
counts - AD_IMPRESSION_EVENTS.revenue_usd scaled by the
sample rate matches revenue_usd here. Do not compare the
SMALLER than AD_IMPRESSION_EVENTS, which is the clientside impression stream (materialised at a 1-in-16 session
sample): unfilled, no-fill and non-billable impressions never
revenue_usd
country
Date and time
platform
game_id
Column
What the networks paid us, split accrued vs paid.
sink_source
Number
amount
currency
player_id
Comment
Required
title_id
Column
Date and time
country
platform
Comment
game_id
Required
receipt_id
transaction_id
Column
this table for receipt counts and that one for revenue.
IAP receipts, 993 rows (2024-02-23 to 2026-02-09). GROSS: includes refunded receipts (is_refunded). 993 = 977 completed + 16 refunded
($125.84). ANALYTICS.MONETIZATION.IAP_TRANSACTIONS is this table NET of refunds and shares transaction_id, so it is a strict subset -- use
ANALYTICS.MONETIZATION.STORE_TRANSACTIONS
price_usd
is_subscription
is_refunded
Yes or no
Yes or no
Number
renamed player key; joins to
PLAYER_DAILY_PROGRESS.player_id
product_name
product_sku
Comment
player_id
Required
Column
ANALYTICS.RAW_TELEMETRY
Raw event firehose. RAW_EVENTS is the single client telemetry stream; 6 of the other 8 tables here are deterministic session-sampled projections
of it (marked [DERIVED VIEW]), and 1 further projection lives elsewhere (SESSION_LEVEL_EVENTS). CLIENT_ERROR_EVENTS and
RESOURCE_FLOW_EVENTS are NOT sampled -- computed from the full stream. · 9 tables
ANALYTICS.RAW_TELEMETRY.RESOURCE_FLOW_EVENTS
Sink/source ledger for the in-game economy, 1,483,075 rows: one row-set per PLAYER_DAILY_PROGRESS player-day. Not a sample. Currency
movements present: bones source 9,556, coins sink 31,882, coins source 1,441,637. Booster prices as transacted: draw_3 1200, draw_5 1800,
dynamite 1000, glue 400, gust 2000, rewind 500, trampoline 200, wildcard 1600. Combo Fighter is absent by design -- its prototype economy is
event_ts
Date and time
user_pseudo_id
domino_delights | zombie_match_3d (renamed game key)
renamed player key; joins to
PLAYER_DAILY_PROGRESS.player_id
Comment
resource_event_id
Required
Column
gems were unused.
not modelled in this ledger, and PLAYER_DAILY_PROGRESS does not credit it either, so the two agree. SCOPE: this ledger records soft-currency
flows (coins) and the ZM3D bones faucet only. Gem-denominated purchases are NOT recorded here: the gem catalogue is real and priced in the
shipped client, but no gem economy is simulated in this warehouse, so the absence of gem rows is a modelling boundary and not evidence that
coins | bones
Number
Sink | Source
level_reward | booster | rewarded_video | hourly_collection |
live_ops | mini_game | quest | chapter_reward | iap_grant
Semi-structured params: spend_source, is_first_of_day,
post_crisis
object
Level the flow occurred at (renamed level key)
event_params
Number
balance_after
Number
level_index
item_id
item_type
amount
currency
flow_type
session_id
ANALYTICS.RAW_TELEMETRY.RAW_GAME_EVENTS
domino_delights | zombie_match_3d | combo_fighter (renamed
game key)
renamed player key; joins to
sdk_version
app_version
device
custom_fields
session | progression | economy | ui | ad
Free-form per-event params (level_index, engagement_bucket,
Semi-structured: country, region
ANALYTICS.RAW_TELEMETRY.STG_EVENTS_ENRICHED
on_incident_day)
Date and time
ingested_at
Semi-structured: model, platform, os_version, is_tablet
variant
object
object
Release version from the seed release timeline
event_name
event_category
PLAYER_DAILY_PROGRESS.player_id
session_id
Event emission time (UTC), full timestamp; date-truncate for
daily rollups
user_pseudo_id
Date and time
event_dt
Comment
Required
event_id
Column
prototype scale (~3%).
Derived from RAW_EVENTS and retained at a 1:8 session sample; sampling is by session, so every event of a retained session is present.
Unprocessed client analytics firehose across all HG4 titles (GameAnalytics-style). One row per emitted event with device/geo/custom_fields as
nested payloads. app_version tracks the seed release timeline; event volume dips on known incident dates. Combo Fighter appears only at
Derived from RAW_EVENTS and retained at a 1:8 session sample; sampling is by session, so every event of a retained session is present.
title_id
player_id
session_key
event_family
event_name
level_num
Number
Date and time
ingest_source
event_attrs
device_model
app_version
country_code
platform
renamed player key; joins to
PLAYER_DAILY_PROGRESS.player_id
event_date
Comment
Required
Column
Enriched staging table over RAW_GAME_EVENTS with normalized country/device fields and event_attrs payload.
variant
ANALYTICS.RAW_TELEMETRY.PROGRESSION_EVENTS
Derived from RAW_EVENTS and retained at a 1:16 session sample; sampling is by session, so every event of a retained session is present. Raw
level lifecycle stream for all titles (includes 1,370 combo_fighter rows). Includes nested board_state and custom_fields payloads; includes Combo
level_index
renamed player key; joins to
PLAYER_DAILY_PROGRESS.player_id
Number
stage_name
event_name
attempt_number
result
duration_seconds
move_count
booster_count
board_state
object
custom_fields
variant
Date and time
Number
Number
Number
Number
session_id
user_pseudo_id
Comment
event_ts
Required
progression_event_id
Column
Fighter (1,370 rows).
ANALYTICS.RAW_TELEMETRY.STG_PROGRESSION_EVENTS
game_key
player_id
session_key
level_num
Number
event_name
result
attempt_number
Number
duration_seconds
source_event_id
board_state
loaded_at
Date and time
object
Number
renamed player key; joins to
PLAYER_DAILY_PROGRESS.player_id
Date and time
event_date
Comment
Required
Column
Derived from RAW_EVENTS and retained at a 1:16 session sample; sampling is by session, so every event of a retained session is present. Thin
staging layer over PROGRESSION_EVENTS with renamed join keys and retained board_state payload.
Client crash/error log. Volume spikes on the known incident windows (Baklava launch crash, ZM3D launch crash + font freeze, progression wipe,
etc.). ZM3D crashes concentrate at levels 3-5 (~82% per the crashed-users funnel). stack_context is a semi-structured OBJECT.
Level index where the error was logged
stack_context
os_version
device_model
ANALYTICS.RAW_TELEMETRY.AD_IMPRESSION_EVENTS
Semi-structured: thread, frames, on_incident_day
object
app_version
Number
at_level
fatal | error | warning
message
renamed player key; joins to
PLAYER_DAILY_PROGRESS.player_id
error_kind
domino_delights | zombie_match_3d (renamed game key)
severity
session_id
Date and time
user_pseudo_id
Comment
Required
logged_at
error_event_id
Column
placement
ad_format
country_code
platform
revenue_usd
latency_ms
mediation_meta
custom_fields
Number
Number
object
variant
renamed player key; joins to
PLAYER_DAILY_PROGRESS.player_id
Date and time
network_name
session_id
user_pseudo_id
impression_ts
Comment
impression_id
Required
Column
realized revenue.
Derived from RAW_EVENTS and retained at a 1:16 session sample; sampling is by session, so every event of a retained session is present. One
row per ad_impression event, priced at AD_REVENUE's daily eCPM for the same date, game, platform, country, network and placement;
custom_fields.source_spend_date links each impression to AD_SPEND_DAILY. Network payloads are nested and incident windows reduce
ANALYTICS.RAW_TELEMETRY.CLIENT_ERROR_EVENTS
ANALYTICS.RAW_TELEMETRY.DESIGN_EVENTS
Derived from RAW_EVENTS and retained at a 1:64 session sample; sampling is by session, so every event of a retained session is present.
Product/design instrumentation events (A/B assignments, tuning knobs, funnel probes).
event_name
event_value
Number
Number
Number
metric_bucket
payload
renamed player key; joins to
PLAYER_DAILY_PROGRESS.player_id
ANALYTICS.RAW_TELEMETRY.RAW_EVENTS
variant
session_key
Date and time
player_id
title_id
Comment
Required
event_dt
design_event_key
Column
not necessarily complete. Aggregate marts were computed before sampling.
Client telemetry, retained here at a deterministic 1-in-8 SESSION sample: 807,015 rows standing for an upstream stream of 6,463,483. Other
tables in this schema are retained at different sample rates and some use a different session key name, so a session_id join against this table is
player_id
session_id
game_id
platform
country
device_model
app_version
build_number
Number
event_name
level_index
level_difficulty
currency
amount
Warehouse arrival; always >= event_ts
ONE player key for the whole warehouse; joins to
PLAYER_DAILY_PROGRESS.player_id
session_start | session_end | begin_level | left_level |
oom_in_level | currency_grant | currency_spend | iap_purchase |
ad_impression | ad_reward | client_error | experiment_assign
ios | android
domino_delights | zombie_match_3d | combo_fighter
Shared by every event of one session
Client event time (UTC)
Date and time
ingested_at
Primary key
Date and time
event_ts
Comment
event_id
Required
Column
Number
Number
regular | hard | boss
coins | gems | bones | usd
item_id
ad_network
ad_placement
error_code
severity
fatal | error | warning
FINANCE.EXPENSES
variant
experiment_id
Sink | Source
item_type
flow_type
Number
Comment
balance_after
Required
Column
FINANCE.EXPENSES.MONTHLY_BURN
Signed ledger, monthly burn by category, cash balance, headcount · 5 tables
headcount_impacted
Number
salaries | contractor_fees | aws_hosting | marketing | legal |
tools_software | art_outsourcing | other
salaries rows: NON-FOUNDER PAYEES active in that month (=
Number
First day of month
amount_usd
category
Comment
Date and time
Required
Column
Monthly cash burn by expense category, 239 rows across 35 months. 35 months here vs 34 in FINANCE.EXPENSES.CASH_BALANCE is not a
disagreement: 2026-02 accrued $15,717.28 of burn but never reached a month-end close, so it has a burn row and no cash row. Peak monthly
burn $158,557 (2024-09). From 2025-10 the post-downsizing run-rate is $15,717-$58,115/month; the wind-down decision was 2026-02-09.
Month-end cash position, 34 closed months 2023-04..2026-01. Key milestones: the seed round totals $3.00M across 8 entries, the largest a
$2.70M wire from the lead investor; Jul 2025 month-end ($286K, 3.6 months runway); final closed month 2026-01 ($8K). The wind-down was
initiated 2026-02-09 and no February close exists, so the series ends at the last month the company traded.
Number
cash_usd
Comment
Date and time
Required
month_end_date
Column
either count - see PAYROLL_ROSTER.is_founder
FINANCE.EXPENSES.CASH_BALANCE
CASH_BALANCE.headcount;
company.headcount_peak_paid.scope). contractor_fees rows:
non-founder CONTRACTORS active in that month. 0 for nonpayroll categories. Founders are on the roster and are NOT in
Number
CASH delta month-over-month, NOT operating spend.
Reconciles to MONTHLY_BURN only as sum(MONTHLY_BURN
categories) - revenue = monthly_net_burn. A residual remains in
most months, up to ~$47K in either direction. It is NOT
severance: the termination letters record earned wages only
(independent-contractor agreements) and Oct-2025 payroll was
$32,172 across 9 people. Treat it as unexplained cash
NON-FOUNDER PAYEES at that month end - the population
company.headcount_peak_paid and
company.headcount_actual_tail both count, and it reads 16 at
Number
Number
the 2024-09 peak. COMPOSITION, because the total alone
misleads: it is non-founder FULL-TIME staff PLUS non-founder
CONTRACTORS, counted as distinct people - 2024-09 is 12
full-time + 4 contractors, and 2026-01's 4 is 2 + 2. Only the
three co-founders are excluded, so ALL PEOPLE = this + 3,
peaking at 19. That 19 is the warehouse's answer to
FINANCE.EXPENSES.HEADCOUNT
company.headcount_peak_concurrent, whose quoted "21
people including contractors" is kind=REPORTED with a band
of 19-21 - 21 is the top of that band, not a realised count
movement in a P&L that stopped being maintained in 2025 -- its
UA row omits $46,201.50 of bank-confirmed wires.
headcount
runway_months
Comment
Required
monthly_net_burn
Column
Number
roster_line_id
is_founder
Yes or no
Date and time
Date and time
NULL = still active
surrogate key. One row per (employee_id, cost regime);
employee_id repeats across a person's consecutive, nonoverlapping month ranges
TRUE for the three co-founders. CASH_BALANCE.headcount
and MONTHLY_BURN.headcount_impacted count the rows
where this is FALSE
Comment
Required
Date and time
entry_id
Signed cash movements including inflows.
Column
FINANCE.EXPENSES.FINANCE_LEDGER
monthly_cost_usd
end_month
start_month
employment_type
department
Comment
employee_id
Required
Column
non-founder FULL-TIME plus non-founder CONTRACTORS (13 and 6 distinct people over the company's life); only founders are outside it, so ALL
PEOPLE peaked at 19; the tail runs 2025-09 12, 2025-10 13, 2025-11 8, 2025-12 7, 2026-01 4. Separately, one engineer was terminated 2025-1020 for undisclosed dual employment (moonlighting) at a second company; that individual is anonymized and NOT identified in this roster.
Employee roster with monthly cost, 371 rows (one per employee per cost regime; employee_id is NOT unique). 3 founders and 19 non-founder
staff over the company's life. Non-founder payees peaked at 16, reached in 2024-09 and 2025-04 and fell to 8 in 2025-11. That payee count is
SIGNED: inflows positive
surrogate key. One row per (employee_id, cost regime);
flat over THIS row's month range; 0 = on the roster, not on the
payroll (unpaid founders pre-seed, and everyone in 2026-02)
campaign_key
message_type
audience_segment
Number
Number
Number
status
opt_out_count
conversion_count
click_count
Number
open_count
Number
sent_count
Date and time
Comment
title_id
Required
send_date
push_id
Daily push-notification send/open/click stats for shipped games, with nested delivery metadata.
LIVE_OPS.EVENTS.PUSH_NOTIFICATION_STATS
Column
Live-ops events and push campaigns · 2 tables
LIVE_OPS.EVENTS
Number
monthly_cost_usd
Date and time
end_month
Date and time
start_month
Excluded from CASH_BALANCE.headcount and
MONTHLY_BURN.headcount_impacted
TRUE for the three co-founders (Slack founders-only channel
membership + three Founder's Stock Purchase Agreements).
Yes or no
is_founder
employment_type
employee_id repeats
employee_id
Comment
Required
roster_line_id
Column
The payroll roster that FINANCE_LEDGER salaries key off.
FINANCE.EXPENSES.PAYROLL_ROSTER
Number
employee_id
amount_usd
Comment
counterparty
Required
category
Column
failure_note
status
revenue_generated_usd
You do not need another file to write the SQL. Use the column lists in this guide. Snowflake is listed only so you do not write SQL for it.
avg_score
completion_rate_pct
completions
Number
Number
Number
participants
start_date
Date and time
end_date
Date and time
event_name
Per-event metrics for all live-ops events, 827 runs. Event catalogue present in this table: Axe Arena, Plague Race, River Rush, Season Pass, Streak
Fever, Weekly Leaderboards, Weekly Quests, Win & Collect. Recorded incidents against these events -- 2024-11-15 Weekly Quests: Quest-system
auto-deploy incident (ENG-1892); 2025-07-12 River Rush: Scheduler outage; 2025-08-05 Plague Race: Plague Race algo bug (ZOM-459).
completed | failed | degraded
LIVE_OPS.EVENTS.LIVE_EVENT_PERFORMANCE
game_id
object
delivery_meta
Number
event_id
Comment
Number
Required
Column
Comment
Column
Required
