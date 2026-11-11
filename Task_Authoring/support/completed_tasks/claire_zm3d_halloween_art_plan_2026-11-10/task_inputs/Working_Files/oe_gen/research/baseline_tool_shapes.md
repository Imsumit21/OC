# Baseline tool shapes: seven Opus runs, mined for Oracle Events

Source of truth for tool routes, parameters and rendered values on the Halloween task (`task_inputsN2`). Every excerpt below is copied by script from the trajectories, not retyped.

## How to read this

| Convention | Meaning |
|---|---|
| B1 to B6 | `07_Baseline_Trajectories/trajectory-run-1.json` to `-6.json` |
| PC | `06_PreCheck_Trajectory/trajectory-run-1 (1).json` |
| `B3#16` | Tool call 16 (zero-based, in order) in run B3, as numbered by `traj_lib.py` |
| Tool names | Every task tool is on server `hg`. Raw name is `mcp__hg__<name>`; the short name is used below |
| Output excerpts | Shown with the `{"result":"..."}` wrapper removed. `\uXXXX` escapes are left as the tool returned them |
| Counts | Out of 7 runs unless stated |
| Clock | `get_time` with `{}` returned `"current_time": "2025-10-01T07:00:15Z"` in 7/7 |

Scripts are in this folder: `traj_lib.py` (loader) and `s1_*.py` to `s31_*.py` (one per check). `build_report.py` regenerates this file. `06_PreCheck_Trajectory/` also holds an older `trajectory-run-1.json` and `trajectory.json`; those were not used.

## What changes how you write the Oracle Events

1. **Four of the six deciding-record groups were never read by any run.** Frederick's "Fri Oct 10" reply, Marcus's re-record note, Martin's vacation post with Leonard's reply, and Frederick's end card 001 comment are all 0/7. So there is no observed natural route for them. Item 9 offers candidates, each marked UNTESTED. Only Robert's reply (2/7) and the Unity retention mail (5/7) have a real route to cite.
2. **"Fri Oct 10" in B1, B2 and B3 is not Frederick's deadline.** It is the runs' own internal date (refresh target in B1 and B2, icon concept date in B3). All 329 `linear_update_issue` calls used `dueDate: "2025-10-15"`, and no call ever assigned `julia.lawson@harmonygames.co`.
3. **Slack names never render inside message text.** `<@EMPLOYEE_0005_SLACK_ID>` stays raw. The author's name comes only from the `user_profile` block, which `response_format: "concise"` removes.
4. **`slack_read_channel` never returned a thread reply** (0 reply rows in 11 reads). Replies need `slack_read_thread` or search. Concise mode also drops `reply_count`, so a parent looks reply-less.
5. **`gmail_search_messages` returns only `id` and `threadId`, with no subject or snippet.** Message bodies are base64 in `payload.body.data`. The decoded wording does not appear literally in the tool output, apart from a truncated snippet.
6. **Linear's best library filter is `{"team":"Art","createdAt":"2025-09-01","limit":100}`.** It returned exactly the 62 issues ART-793 to ART-854 with `hasNextPage: false` (B2#88). Only 1/7 used it. Add `fields` to keep the output small.
7. **Linear input is `state`; output is `status` plus `statusType`.** Assignee is an email string, and the key is absent when unset. Linear shows no display names for these people.
8. **`gdocs_create_document` returns no URL.** `gsheets_create_spreadsheet` does (`spreadsheetUrl`). The doc URL comes from `gdrive_share_file` (`file.webViewLink`) or `gdrive_get_file_metadata` (`webViewLink`).
9. **`gsheets_get_spreadsheet`, `trello_get_board_actions` and `gsheets_values_get` on the source sheet were called by 0/7.** The first two appear only in the init roster, and the trajectories carry no tool schemas, so their parameters and output cannot be taken from these runs.
10. **Sheet formulas do not evaluate.** All three runs that wrote `COUNTIF`/`COUNTIFS` read back `#NAME?`. The write itself reported success.
11. **Large outputs spill to a file.** `gcal_list_events` (196,590 chars) and 3 of the 4 `linear_list_issues` calls at `limit: 250` came back as an `Error: result (...)` message, not data. `jq` is not installed in the runner; `python3` is.
12. **Run-specific values must be placeholders.** Doc and sheet ids differ per run. ART-855 and ART-856 follow creation order, which flipped in B4.

## 1. Finding Leonard's message, and how Slack renders

### Route

| Step | Tool | Input | Runs |
|---|---|---|---|
| Find channel | `slack_search_channels` | `{"query": "zombie", "channel_types": "public_channel,private_channel"}` | 5/7 on the first call (B1, B2, B5, B6, PC) |
| Find channel, second try | `slack_search_channels` | `{"query": "marketing", "channel_types": "public_channel,private_channel"}` | 1/7 (B4, after `{"query":"zombie"}` showed only 3 public channels) |
| Find channel, fallback | `slack_channels_list` | `{"channel_types": "public_channel,private_channel", "limit": 200}` | 1/7 (B3, after `{"query":"zombie_marketing"}` returned 0). 111 channels |
| Read | `slack_read_channel` | `{"channel_id": "C06DJBJL798", "limit": 30}` | 6/7; B2 used `limit: 20`. Leonard's message is the first row |
| Optional | `slack_read_thread` | `{"channel_id": "C06DJBJL798", "message_ts": "1759269913.882683"}` | 3/7 (B1#4, B4#5, B6#4). It returned only the parent; there were no replies |

`#zombie_marketing` is private. Without `channel_types`, the search returned public channels only (B4#0: `zombie-art`, `zombie-prs`, `zombie-sfx`), which also fits B3's empty result for the exact name. With both types, `zombie` returned 7 channels: `zombie-art`, `zombie-bugs`, `zombie-match3d`, `zombie-ops`, `zombie-prs`, `zombie-sfx`, `zombie_marketing`.

slack_search_channels (B4#3)

Input:
```json
{"query": "marketing", "channel_types": "public_channel,private_channel"}
```

Output (complete):
```text
{"ok": true, "channels": [{"id": "C06DJBJL798", "name": "zombie_marketing", "is_channel": true, "is_private": true, "is_im": false, "is_mpim": false, "is_archived": false, "is_general": false, "num_members": 17, "created": 1705003525, "creator": "U04TWDMDT0V", "permalink": "https://harmonygamesgroup.slack.com/archives/C06DJBJL798", "channel_type": "private_channel", "creator_profile": {"id": "U04TWDMDT0V", "name": "U04TWDMDT0V", "real_name": "U04TWDMDT0V", "display_name": "U04TWDMDT0V", "email": null}, "created_time": "2024-01-11T20:05:25Z"}], "has_more": false, "total_count": 1, "response_metadata": {"next_cursor": ""}}
```

slack_read_channel (B1#3)

Input:
```json
{"channel_id": "C06DJBJL798", "limit": 30}
```

Output (chars 0-600 of 35596):
```text
{"ok": true, "messages": [{"ts": "1759269913.882683", "type": "message", "text": "<@EMPLOYEE_0009_SLACK_ID> halloween for ZM :jack_o_lantern: I'd like everything players see from us to look like halloween for the last stretch of october - store pages and every ad we're running. can you own the art side? go through everything that's live today and work out what gets a halloween version, what needs work first, what we already have, and who makes what by when\n\u2022 the live creatives sheet is what's running\n\u2022 Arthur's release calendar has the Q4 dates\n\u2022 Robert has direction for seas
```

Response envelope keys: `ok`, `messages`, `has_more`, `response_metadata.next_cursor`. Rows are newest first. No run passed a cursor to a Slack read.

### One message, full format

```json
{
 "ts": "1759269913.882683",
 "type": "message",
 "text": "<@EMPLOYEE_0009_SLACK_ID> halloween for ZM :jack_o_lantern: I'd like everything players se ...[truncated here]",
 "channel": "C06DJBJL798",
 "user": "EMPLOYEE_0038_SLACK_ID",
 "channel_info": {
  "id": "C06DJBJL798",
  "name": "zombie_marketing",
  "is_private": true,
  "is_im": false,
  "is_mpim": false
 },
 "user_profile": {
  "id": "EMPLOYEE_0038_SLACK_ID",
  "name": "Leonard Hayes",
  "real_name": "Leonard Hayes",
  "display_name": "Leonard Hayes",
  "email": "leonard.hayes@harmonygames.co"
 },
 "time": "2025-09-30T22:05:13Z",
 "permalink": "https://harmonygamesgroup.slack.com/archives/C06DJBJL798/p1759269913882683"
}
```

### How ids and mentions render

| Element | Full format | Concise (`response_format: "concise"`) |
|---|---|---|
| Author id | `"user": "EMPLOYEE_0038_SLACK_ID"` | Same |
| Author name | `user_profile.name` = `Leonard Hayes`, plus `real_name`, `display_name`, `email` | Absent |
| Mention in text | Raw, `<@EMPLOYEE_0009_SLACK_ID>`. Never replaced | Raw |
| Time | `ts` and `"time": "2025-09-30T22:05:13Z"` | `ts` only |
| Thread data | `thread_ts`, `reply_count`, `reply_users_count`, `latest_reply`, `latest_reply_time` | `thread_ts` only |
| Other | `channel_info`, `permalink`, `reactions`, `files`, `attachments` when present | Absent |

Masked names can appear inside text, for example `:[USERNAME_21162]:` and `[PERSON_NAME_3331]`.

Concise format example, slack_read_thread (B4#96)

Input:
```json
{"channel_id": "C08R8CHB0QL", "message_ts": "1759167065.499092", "response_format": "concise"}
```

Output (chars 0-600 of 838):
```text
{"ok": true, "messages": [{"ts": "1759167065.499092", "type": "message", "text": "quick test on cheer fastcouch, 9:16 and 16:9, pumpkins and fog over the cut. files are in ua masters", "channel": "C08R8CHB0QL", "user": "EMPLOYEE_0002_SLACK_ID", "thread_ts": "1759167065.499092"}, {"ts": "1759248337.170599", "type": "message", "text": "Fog reads well but this is the July capture, the old background is still under it. We can't ship these, they need doing again from the Sep 16 one", "channel": "C08R8CHB0QL", "user": "EMPLOYEE_0016_SLACK_ID", "thread_ts": "1759167065.499092"}, {"ts": "1759249269.38
```

### Resolving a person's name

`slack_read_user_profile` was called 7/7, always with `{}`, and only returned Claire. No run passed a user id, so these runs do not show whether it accepts one. `slack_search_users` is in the roster and was never called. Names of other people came only from `user_profile` on full-format messages.

slack_read_user_profile (B1#1)

Input:
```json
{}
```

Output (complete):
```text
{"ok": true, "user": {"id": "EMPLOYEE_0009_SLACK_ID", "name": "Claire Morgan", "real_name": "Claire Morgan", "display_name": "Claire Morgan", "profile": {"email": "claire.morgan@harmonygames.co", "image_72": null, "display_name": "Claire Morgan", "real_name": "Claire Morgan"}, "is_bot": false, "is_admin": false, "deleted": false, "tz": "America/Los_Angeles"}}
```

Token to person, from `user_profile` on messages those people wrote:

| Token | Name | Email |
|---|---|---|
| `EMPLOYEE_0002_SLACK_ID` | Marcus Bennett | marcus.bennett@harmonygames.co |
| `EMPLOYEE_0003_SLACK_ID` | Oliver Brooks | oliver.brooks@harmonygames.co |
| `EMPLOYEE_0005_SLACK_ID` | Julia Lawson | julia.lawson@harmonygames.co |
| `EMPLOYEE_0006_SLACK_ID` | Calvin Price | calvin.price@harmonygames.co |
| `EMPLOYEE_0008_SLACK_ID` | Frederick Stone | frederick.stone@harmonygames.co |
| `EMPLOYEE_0009_SLACK_ID` | Claire Morgan | claire.morgan@harmonygames.co |
| `EMPLOYEE_0016_SLACK_ID` | Robert | robert@harmonygames.co |
| `EMPLOYEE_0025_SLACK_ID` | Arthur Blake | arthur.blake@harmonygames.co |
| `EMPLOYEE_0026_SLACK_ID` | Brian Foster | brian.foster@harmonygames.co |
| `EMPLOYEE_0033_SLACK_ID` | Martin Walsh | martin.walsh@harmonygames.co |
| `EMPLOYEE_0038_SLACK_ID` | Leonard Hayes | leonard.hayes@harmonygames.co |

Not resolvable from these runs: `EMPLOYEE_0032_SLACK_ID` and `PERSON_6089_SLACK_ID` have `user_profile` names equal to the token and a null email. `EMPLOYEE_0012_SLACK_ID`, `EMPLOYEE_0030_SLACK_ID` and `PERSON_6072_SLACK_ID` appear only as mentions.

So `<@EMPLOYEE_0005_SLACK_ID>` in Martin's vacation post would render raw, and tying it to Julia needs a full-format message that she wrote.

## 2. Calendar route to the review event

| Route | Input | Runs | Result |
|---|---|---|---|
| `gcal_search_events` | `{"q": "review", "timeMin": "2025-10-01T00:00:00Z", "timeMax": "2025-10-04T00:00:00Z"}` | 4/7 (B1#7, B2#7, B4#21, B5#17) | 2 items, attendees included, one call |
| `gcal_list_events`, then Bash, then `gcal_get_event` | `{"calendarId": "primary", "timeMin": "2025-10-01T00:00:00Z", "timeMax": "2025-10-04T00:00:00Z", "singleEvents": true}` | 3/7 (B3#8, B6#8, PC#8) | Spill of 196,590 chars, file parsed with python3, then `{"calendarId": "primary", "eventId": "evt_d947bf7cd910549b674b1f"}` |

`gcal_search_events` is the route to cite. Its envelope is `kind`, `items`, `totalResults`. The items were `evt_90a596f305490fdee09edd` "Bug Review" (a weekly recurring event from 2024) and `evt_d947bf7cd910549b674b1f` "ZM3D Halloween review".

Halloween item inside the search output (B1#7):
```text
 {"kind": "calendar#event", "etag": "\"2690210106834954\"", "id": "evt_d947bf7cd910549b674b1f", "iCalUID": "83766dff00ea50972c41ba9f47db58c3@hg4", "htmlLink": "https://www.google.com/calendar/event?eid=ZXZ0X2Q5NDdiZjdjZDkxMDU0OWI2NzRiMWYgY2xhaXJlLm1vcmdhbkBoYXJtb255Z2FtZXMuY28", "status": "confirmed", "summary": "ZM3D Halloween review", "description": "Claire walks us through the Halloween plan and tracker. I'm in LA Thursday so I'll dial in for this one.", "location": null, "start": {"dateTime": "2025-10-02T16:00:00Z"}, "end": {"dateTime": "2025-10-02T16:30:00Z"}, "organizer": {"email": "leonard.hayes@harmonygames.co", "self": false, "displayName": "leonard.hayes@harmonygames.co"}, "creator": {"email": "leonard.hayes@harmonygames.co", "self": false, "displayName": "leonard.hayes@harmonygames.co"}, "attendees": [{"email": "claire.morgan@harmonygames.co", "responseStatus": "needsAction", "self": true}, {"email": "leonard.hayes@harmonygames.co", "responseStatus": "accepted", "organizer": true}, {"email": "frederick.stone@harmonygames.co", "responseStatus": "needsAction"}, {"email": "martin.walsh@harmonygames.co", "responseStatus": "needsAction"}, {"email": "marcus.bennett@harmonygames.co", "re
```

`gcal_get_event` (B3#11):

Input:
```json
{"calendarId": "primary", "eventId": "evt_d947bf7cd910549b674b1f"}
```

Output (first 600 chars):
```text
{"kind": "calendar#event", "etag": "\"2690210106834954\"", "id": "evt_d947bf7cd910549b674b1f", "iCalUID": "83766dff00ea50972c41ba9f47db58c3@hg4", "htmlLink": "https://www.google.com/calendar/event?eid=ZXZ0X2Q5NDdiZjdjZDkxMDU0OWI2NzRiMWYgY2xhaXJlLm1vcmdhbkBoYXJtb255Z2FtZXMuY28", "status": "confirmed", "summary": "ZM3D Halloween review", "description": "Claire walks us through the Halloween plan and tracker. I'm in LA Thursday so I'll dial in for this one.", "location": null, "start": {"dateTime": "2025-10-02T16:00:00Z"}, "end": {"dateTime": "2025-10-02T16:30:00Z"}, "organizer": {"email": "leona
```

### How attendees render

Each attendee is an object with `email` and `responseStatus`, plus `self: true` (Claire) or `organizer: true` (Leonard). Attendees have no display name. `organizer` and `creator` have `displayName`, which is just the email. Start and end are UTC: `2025-10-02T16:00:00Z` to `16:30:00Z`, which is 9:00 PT.

The 7 attendees are claire.morgan, leonard.hayes, frederick.stone, martin.walsh, marcus.bennett, robert and arthur.blake (all @harmonygames.co). All 7 runs shared with the 6 who are not Claire.

Note: in `gcal_list_events`, expanded recurring instances show `+00:00` and a suffixed id (`evt_..._20251001T160000Z`). The Halloween event shows `Z` and a plain id (B3#10).

## 3. Sheet route: ZM3D live creatives

| Step | Tool | Input | Runs |
|---|---|---|---|
| Find | `gdrive_search` | `{"query": "live creatives"}` | 6/7; B6 used `{"query": "creatives"}`. Both return 1 file |
| Tabs | `gdrive_list_sheets` | `{"spreadsheetId": "f_02b1968f5e882366fbb883"}` | 7/7 |
| All tabs | `gsheets_values_batch_get` | `{"spreadsheetId": "f_02b1968f5e882366fbb883", "ranges": ["Read me", "Store", "Unity", "Archive"]}` | 4/7 (B1, B2, B5, B6) |
| Three tabs | `gsheets_values_batch_get` | `ranges: ["Store", "Unity", "Archive"]` | 2/7 (B3, B4; Read me came from another call) |
| Per tab, CSV | `gdrive_read_sheet_range` | `{"spreadsheetId": "f_02b1968f5e882366fbb883", "sheetIndex": 1}` | 1/7 (PC, indexes 0 to 3) |
| `gsheets_get_spreadsheet` | Never called | | 0/7 |
| `gsheets_values_get` on this sheet | Never called | | 0/7 (used only on the runs' own trackers) |

Partial-read trap: `gdrive_read_file` on the sheet (B3#12) and `gdrive_read_sheet_range` with no `sheetIndex` (B4#9, PC#10) both returned only the first tab, Read me.

gdrive_search (B1#5)

Input:
```json
{"query": "live creatives"}
```

Output (chars 0-600 of 1364):
```text
{"files": [{"id": "f_02b1968f5e882366fbb883", "name": "ZM3D live creatives", "mimeType": "application/vnd.google-apps.spreadsheet", "parents": ["d_175c0d7bc72ed244b944cb"], "owners": [{"emailAddress": "frederick.stone@harmonygames.co", "displayName": "frederick.stone@harmonygames.co"}], "permissions": [{"id": "43c52407441e", "type": "user", "emailAddress": "frederick.stone@harmonygames.co", "role": "owner", "displayName": "frederick.stone@harmonygames.co"}, {"id": "a6810488bdb1", "type": "user", "emailAddress": "leonard.hayes@harmonygames.co", "role": "reader", "displayName": "leonard.hayes@ha
```

gdrive_list_sheets (B1#8)

Input:
```json
{"spreadsheetId": "f_02b1968f5e882366fbb883"}
```

Output (complete):
```text
{"sheets": [{"spreadsheetId": "f_02b1968f5e882366fbb883", "sheetId": 0, "title": "Read me", "index": 0, "sheetType": "GRID", "gridProperties": {"rowCount": 1000, "columnCount": 1}}, {"spreadsheetId": "f_02b1968f5e882366fbb883", "sheetId": 1, "title": "Store", "index": 1, "sheetType": "GRID", "gridProperties": {"rowCount": 1000, "columnCount": 4}}, {"spreadsheetId": "f_02b1968f5e882366fbb883", "sheetId": 2, "title": "Unity", "index": 2, "sheetType": "GRID", "gridProperties": {"rowCount": 1000, "columnCount": 4}}, {"spreadsheetId": "f_02b1968f5e882366fbb883", "sheetId": 3, "title": "Archive", "index": 3, "sheetType": "GRID", "gridProperties": {"rowCount": 1000, "columnCount": 4}}]}
```

gsheets_values_batch_get (B1#10)

Input:
```json
{"spreadsheetId": "f_02b1968f5e882366fbb883", "ranges": ["Read me", "Store", "Unity", "Archive"]}
```

Output (chars 0-600 of 4747):
```text
{"spreadsheetId": "f_02b1968f5e882366fbb883", "valueRanges": [{"range": "'Read me'!A1:A1000", "majorDimension": "ROWS", "values": [["One row per creative serving on our four Unity retention campaigns today (iOS UK phone, iOS UK tablet, Android US phone, Android US tablet) plus the store listing sets. Paused or retired creatives move to Archive. Each Unity row links its ART ticket; campaigns, capture and master notes are in the ticket comments. Store sets have no ART ticket. Halloween push: see the Halloween push card on the ZM roadmap."]]}, {"range": "Store!A1:D1000", "majorDimension": "ROWS",
```

Tail of the same output, showing the end of Unity and all of Archive:
```text
 alpha 50 4:5", "4:5 video", "Sep 23", "ART-853"], ["balloons alpha 50 (1) 16:9", "16:9 video", "Sep 25", "ART-854"]]}, {"range": "Archive!A1:D1000", "majorDimension": "ROWS", "values": [["Creative", "Format", "Paused on", "ART ticket"], ["GreenCouch 001", "9:16 video", "Sep 15", "ART-836"], ["Professional Mode 9x16 test", "9:16 video", "Sep 15", "ART-837"], ["sophie ocean portrait", "9:16 video", "Sep 15", "ART-838"], ["squirrelfail portrait text", "9:16 video", "Sep 19", "ART-839"]]}]}
```

### How the four tabs come back

| Tab | Returned range | Rows including header | Notes |
|---|---|---|---|
| Read me | `'Read me'!A1:A1000` (quoted) | 1 | One text cell, no header |
| Store | `Store!A1:D1000` | 5 | Header plus 4 surfaces. Empty `ART ticket` cells are dropped, so data rows have 3 values |
| Unity | `Unity!A1:D1000` | 57 | Header plus 56 creatives |
| Archive | `Archive!A1:D1000` | 5 | Header plus ART-836 to ART-839. Third column is `Paused on` |

`gdrive_read_sheet_range` returns the same data as CSV in a `text` field:
```text
{"spreadsheetId": "f_02b1968f5e882366fbb883", "sheetIndex": 1, "mimeType": "text/csv", "text": "Surface,Stores,Live since,ART ticket\r\napp icon,\"App Store, Google Play\",Sep 17,\r\n\"iPhone 6.5\"\" set\",App Store,Sep 17,\r\n\"iPad 12.9\"\" set\",App Store,Sep 17,\r\nGoogle Play phone set,Google Play,Sep 17,\r\n"}
```

## 4. Deck and doc routes

### Deck: Seasonal art direction — Q4 2025 (`f_5ebf55ad29e815d46243c8`)

Found by `gdrive_search` in three ways, and `gdrive_search` has two distinct modes:

| Input | Runs | Files returned |
|---|---|---|
| `{"query": "seasonal"}` | 2/7 (B3#24, PC#6) | 1, the deck |
| `{"fullText": "seasonal"}` | 4/7 (B1#21, B2#20, B5#6, B6#23) | 11, deck first |
| `{"fullText": "halloween"}` | 2/7 (B4#20, B6#92) | 19 |
| `{"query": "halloween"}` | 5/7 | 14 |

The counts indicate `query` matches names and `fullText` also matches content. `{"query": "iPad"}` returned 0 files in 4/7 runs, because no file name contains it.

`gslides_get_presentation_text` was the read in 7/7:

gslides_get_presentation_text (B1#23)

Input:
```json
{"presentationId": "f_5ebf55ad29e815d46243c8"}
```

Output (complete):
```text
{"presentationId": "f_5ebf55ad29e815d46243c8", "title": "Seasonal art direction \u2014 Q4 2025", "revisionId": "09590bf741", "slideCount": 4, "text": "Seasonal art direction \u2014 Q4 2025\nHalloween and the holidays, store and ads\n\nSeasonal dressing goes on top of the current art only. Anything captured or rendered from a build older than Android #1452 / iOS 1232 (the zombie swap with the new background, Jul 29) is redone on the current build first. If a later capture has replaced it, the newest capture is the one that counts.\nA video whose master has the music baked in is re-cut first from a master without music (re-export one from the project if there is none), so the seasonal pass can be edited.\nBefore any seasonal pass\n\nOnly the seasonal layer changes: pumpkins, fog, props, the title treatment. Same flat background, same pose, same zombie order, same CTA, so a seasonal variant still tests clean against its normal version.\nWhat changes\n\nCalls for the tracker\nHalloween version: dress it from the current art.\nRefresh first: re-capture, re-render or re-cut before any seasonal pass.\nReuse: it already has a seasonal version, use that one.\nSkip: no seasonal version this time."}
```

Flat `text`, with `slideCount: 4` and no per-slide markers. Slides are separated only by blank lines.

`gslides_get_presentation` was used by 1/7 (PC#25), with a `fields` mask aimed at speaker notes. All four notes pages were empty, so nothing depends on it:

gslides_get_presentation (PC#25)

Input:
```json
{"presentationId": "f_5ebf55ad29e815d46243c8", "fields": "slides(objectId,slideProperties(notesPage(pageElements(shape(text)))))"}
```

Output (chars 0-420 of 1116):
```text
{"slides": [{"objectId": "slide_3094f53a92b2", "slideProperties": {"notesPage": {"pageElements": [{"shape": {"text": {"textElements": [{"startIndex": 0, "endIndex": 1, "paragraphMarker": {"style": {}}}, {"startIndex": 0, "endIndex": 1, "textRun": {"content": "\n", "style": {}}}]}}}]}}}, {"objectId": "slide_2f543a88ea15", "slideProperties": {"notesPage": {"pageElements": [{"shape": {"text": {"textElements": [{"startIn
```

### Doc: ZM3D release calendar — Q4 (`f_fdd6d2d2f4a4d2f5b908fb`)

Found by `gdrive_search {"query": "release calendar"}` in 7/7. Read by `gdocs_get_document_text` in 4/7 (B3, B4, B5, PC) and by `gdrive_read_file` in 3/7 (B1, B2, B6).

gdocs_get_document_text (B3#13)

Input:
```json
{"documentId": "f_fdd6d2d2f4a4d2f5b908fb"}
```

Output (complete):
```text
{"documentId": "f_fdd6d2d2f4a4d2f5b908fb", "title": "ZM3D release calendar \u2014 Q4", "name": "ZM3D release calendar \u2014 Q4", "revisionId": "dc309c94e6", "createdTime": "2025-09-24T16:20:00Z", "modifiedTime": "2025-09-30T22:40:00Z", "text": "Zombie Match 3D store submissions, Q4 2025. Owner: Arthur.\nOct 17 submission: the last build that can carry Halloween changes. Merge cut is Thu Oct 16, 12:00 PT. Anything that ships in the build has to be merged by then. Submit Fri Oct 17.\niOS screenshots can only change with a new version, so new iOS screenshots go up with the Oct 17 submission and are due by the same Oct 16 12:00 PT cut.\nApple review has been taking up to 3 days, so plan on that build and its iOS store listing being live from Wed Oct 22.\nGoogle Play listing graphics are not tied to a build: upload any day and allow 1 day for review.\nNov 6 submission: post-Halloween clean-up (icon and screenshots back to normal).\n"}
```

`gdrive_read_file` returns the same text with `mimeType: "text/markdown"` and a leading `# `:
```text
{"mimeType": "text/markdown", "text": "# Zombie Match 3D store submissions, Q4 2025. Owner: Arthur.\nOct 17 submission: the last build that can carry Halloween changes. Merge cut is Thu Oct 16, 12:00 
```

## 5. Gmail

### Search queries, and which mails each surfaced

Every `gmail_search_messages` and `gmail_list_messages` call in the seven runs:

| Call | Query | Other params | Hits (`resultSizeEstimate`) | Draft (Sep 12) | Changes (Sep 30) | Unity retention |
|---|---|---|---|---|---|---|
| B1#11 | `october OR halloween OR UA` | `user_email: claire.morgan`, `max_results: 30` | 30 of 219 | yes | yes | no |
| B1#18 | `from:frederick.stone@harmonygames.co` | `user_email: claire.morgan`, `max_results: 20` | 3 of 3 | yes | yes | yes |
| B1#19 | `from:robert@harmonygames.co` | `user_email: claire.morgan`, `max_results: 20` | 20 of 167 | no | no | no |
| B2#6 | `october UA plan` | `user_email: me` | 5 of 5 | yes | yes | no |
| B3#7 | `newer_than:7d` | `user_email: me` | 12 of 12 | no | yes | yes |
| B3#21 | `from:frederick.stone@harmonygames.co` | `user_email: me` | 3 of 3 | yes | yes | yes |
| B4#8 | `newer_than:10d` | `user_email: claire.morgan` | 12 of 12 | no | yes | yes |
| B4#16 | `october UA plan` | `user_email: claire.morgan` | 5 of 5 | yes | yes | no |
| B5#7 | `october OR halloween OR seasonal` | `user_email: claire.morgan` | 81 of 81 | yes | yes | no |
| B5#11 (list) | `after:2025/09/20` | `user_email: claire.morgan`, `max_results: 30` | 13 of 13 | no | yes | yes |
| B5#14 | `from:frederick.stone@harmonygames.co` | `user_email: claire.morgan` | 3 of 3 | yes | yes | yes |
| B6#7 | `october OR halloween OR UA` | `user_email: claire.morgan`, `max_results: 30` | 30 of 219 | yes | yes | no |
| B6#15 | `from:frederick.stone@harmonygames.co` | `user_email: claire.morgan`, `max_results: 10` | 3 of 3 | yes | yes | yes |
| PC#7 | `october UA plan` | `user_email: me` | 5 of 5 | yes | yes | no |

Both "October UA plan" mails were read in 7/7. `{"query": "october UA plan"}` returns both, along with 3 Substack mails, and does **not** return the Unity retention mail.

`user_email` accepts `"me"` (B2, B3, PC) or the full address (B1, B4, B5, B6). Ids look like `claire.morgan@harmonygames.co/<CANf1Nx...@mail.gmail.com>` and thread ids like `claire.morgan@harmonygames.co/1844732284519287777`.

gmail_search_messages (B2#6)

Input:
```json
{"query": "october UA plan", "user_email": "me"}
```

Output (chars 0-600 of 869):
```text
{"messages": [{"id": "claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>", "threadId": "claire.morgan@harmonygames.co/1844732284519287777"}, {"id": "claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>", "threadId": "claire.morgan@harmonygames.co/1843080777036925215"}, {"id": "claire.morgan@harmonygames.co/<20250809120232.3.be5092890a65493a@mg-d0.substack.com>", "threadId": "claire.morgan@harmonygames.co/1839979713618546098"}, {"id": "claire.morgan@harmonygames.co/<20241005120107.3.b8d2038a21f5d86a@mg-d1.substack.com>", "threa
```

Search output has only `id` and `threadId` per message, plus `resultSizeEstimate` and `nextPageToken`. There is no subject, sender or snippet, so a run must open a mail to learn what it is.

### Did any run find "Unity retention restart"?

Yes, 5/7. B2 and PC never surfaced it. Route detail is in Item 9.

### `gmail_get_thread` shape

gmail_get_thread (B1#20)

Input:
```json
{"thread_id": "claire.morgan@harmonygames.co/1844644077950167516", "user_email": "claire.morgan@harmonygames.co"}
```

Output (complete):
```text
{"id": "claire.morgan@harmonygames.co/1844644077950167516", "snippet": "Hi all, The iOS retention campaigns went back on today. I left squirrelfail landscape and mrfluffernot landscape off iOS UK tablet this time", "messages": [{"id": "claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>", "threadId": "claire.morgan@harmonygames.co/1844644077950167516", "labelIds": ["INBOX", "CATEGORY_PERSONAL"], "snippet": "Hi all, The iOS retention campaigns went back on today. I left squirrelfail landscape and mrfluffern", "internalDate": "1759189680000", "sizeEstimate": 607, "payload": {"partId": "0", "mimeType": "text/plain", "filename": "", "headers": [{"name": "X-GM-THRID", "value": "1844644077950167516"}, {"name": "Delivered-To", "value": "claire.morgan@harmonygames.co"}, {"name": "MIME-Version", "value": "1.0"}, {"name": "Date", "value": "Mon, 29 Sep 2025 16:48:00 -0700"}, {"name": "Message-ID", "value": "<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>"}, {"name": "Subject", "value": "Unity retention restart"}, {"name": "From", "value": "frederick stone <frederick.stone@harmonygames.co>"}, {"name": "To", "value": "leonard hayes <leonard.hayes@harmonygames.co>, claire morgan <claire.morgan@harmonygames.co>, marcus bennett <marcus.bennett@harmonygames.co>, martin walsh <martin.walsh@harmonygames.co>"}], "body": {"size": 212, "data": "SGkgYWxsLApUaGUgaU9TIHJldGVudGlvbiBjYW1wYWlnbnMgd2VudCBiYWNrIG9uIHRvZGF5LiBJIGxlZnQgc3F1aXJyZWxmYWlsIGxhbmRzY2FwZSBhbmQgbXJmbHVmZmVybm90IGxhbmRzY2FwZSBvZmYgaU9TIFVLIHRhYmxldCB0aGlzIHRpbWUsIHRoZXkgd2VyZSB0aGUgd2Vha2VzdCB0aGVyZS4gQm90aCBzdGF5IG9uIEFuZHJvaWQgVVMgdGFibGV0LgpGcmVkZXJpY2s="}}}]}
```

| Field | Format | Example |
|---|---|---|
| Thread envelope | `id`, `snippet`, `messages` | |
| Subject, From, To | `payload.headers[]` as name/value pairs; there are no top-level fields | `{"name": "Subject", "value": "Unity retention restart"}` |
| Date header | RFC 2822 in Pacific offset | `Mon, 29 Sep 2025 16:48:00 -0700` |
| `internalDate` | Epoch milliseconds, as a string | `"1759189680000"` |
| Body | Base64 in `payload.body.data`, with `body.size` | |
| Snippet | About 140 chars at thread level, 100 at message level | |
| Names in From/To | Lowercase | `frederick stone <frederick.stone@harmonygames.co>` |

`gmail_get_message` (`{"user_email": "me", "message_id": "..."}`) returns the same message object without the thread wrapper.

`gmail_get_messages_batch` (`{"user_email": ..., "message_ids": [...]}`) returns `{"messages": [...], "not_found": []}`. By default it has **no body data**: `"body": {"size": 484}` (B3#16, B4#12), so both runs had to re-read with `gmail_get_message`. With `"format": "full"` the base64 data is included (B5#13).

### Decoded bodies

These are decoded from `payload.body.data`, which matters because the tool output itself is base64. B6 decoded with Bash at B6#19.

**October UA plan (draft)**, `Date: Fri, 12 Sep 2025 10:40:00 -0700`, thread `claire.morgan@harmonygames.co/1843080777036925215`
```text
Hi all,
Draft plan for October so art can plan around it. Unity only: iOS UK phone, iOS UK tablet, Android US phone, Android US tablet. Halloween flight Oct 20-31 on all four campaigns. Halloween creatives to me by Fri Oct 17 so I can upload them.
I'll confirm before the end of the month.
Frederick
```

**October UA plan - changes**, `Date: Tue, 30 Sep 2025 16:10:00 -0700`, thread `claire.morgan@harmonygames.co/1844732284519287777`
```text
Hi all,
Two changes to the October plan I sent on the 12th.
1. The Android US tablet campaign ends Sun Oct 12 and its budget moves to iOS UK, so don't make Halloween versions of anything that only runs there.
2. The Halloween flight now runs Sat Oct 18 - Fri Oct 31 on the other three campaigns. Unity needs new creatives uploaded and approved before a flight starts, so every Halloween ad needs to be with me by Wed Oct 15, not the 17th.
Everything else in the plan stands.
Frederick
```

**Unity retention restart**, `Date: Mon, 29 Sep 2025 16:48:00 -0700`, thread `claire.morgan@harmonygames.co/1844644077950167516`
```text
Hi all,
The iOS retention campaigns went back on today. I left squirrelfail landscape and mrfluffernot landscape off iOS UK tablet this time, they were the weakest there. Both stay on Android US tablet.
Frederick
```

## 6. Trello

| Tool | Input | Runs | Result |
|---|---|---|---|
| `trello_search` | `{"query": "halloween"}` | 3/7 (B1, B2 with capital H, B4) | Card and comment action. 2,401 chars |
| `trello_search` | `{"query": "halloween", "cards_filter": "all"}` | 2/7 (B5, B6) | Same output |
| `trello_search` | `{"query": "Halloween", "modelTypes": "cards", "cards_filter": "all"}` | 1/7 (B3) | Card only, `actions: []` |
| `trello_search` | `{"query": "Halloween push", "modelTypes": "cards"}` | 1/7 (PC) | Card only, `actions: []` |
| `trello_get_comments` | `{"cardId": "68dc52e015f87c50c441d1a9"}` | 2/7 (B3, PC) | 1 comment |
| `trello_get_card` | `{"cardId": "68dc52e015f87c50c441d1a9", "actions": "all", "checklists": "all"}` | 1/7 (B4#27, after an error) | Card, comment action and createCard action |
| `trello_get_board_actions` | Never called | 0/7 | |

Without `modelTypes`, `trello_search` returns the comment in `actions`, so no second call is needed. With `modelTypes: "cards"` it does not, which is why B3 and PC followed up with `trello_get_comments`.

`"attachments": "true"` as a string is rejected (B4#24, B6#25, B6#27). B4 dropped the parameter and succeeded. B6 repeated the same call and gave up, relying on its search output. Boolean `true` was never tried.

trello_search (B1#12)

Input:
```json
{"query": "halloween"}
```

Output (chars 0-1000 of 2176):
```text
{"actions": [{"id": "68dc65a0f2d7fb28743f5860", "type": "commentCard", "date": "2025-09-30T23:20:00Z", "idMemberCreator": "4b4a68fc0fec0b254e4f9d8e", "idBoard": "6851a6569f3bf818760632ab", "idCard": "68dc52e015f87c50c441d1a9", "data": {"board": {"id": "6851a6569f3bf818760632ab", "name": "ZM ROADMAP", "shortLink": "HSqnngwQ"}, "card": {"id": "68dc52e015f87c50c441d1a9", "idShort": 80, "name": "Halloween push - store + ads (Claire/Martin/Marcus)", "shortLink": "7979f6E4"}, "idCard": "68dc52e015f87c50c441d1a9", "list": {"id": "6851a677e090018224fb8c7f", "name": "Oct 21"}, "text": "Julia's 4:5 static (They're coming, stop them!) is still running on iOS UK and is still our best CPI there. It never made it onto the live creatives sheet, so count it in for Halloween.", "textData": {"emoji": {}}}, "memberCreator": {"id": "4b4a68fc0fec0b254e4f9d8e", "fullName": "Frederick Stone", "username": "frederick.stone", "initials": "FS", "avatarUrl": null}}], "boards": [], "cards": [{"id": "68dc52e015f87c
```

trello_get_comments (B3#22)

Input:
```json
{"cardId": "68dc52e015f87c50c441d1a9"}
```

Output (complete):
```text
{"total_count": 1, "limit": 50, "offset": 0, "has_more": false, "comments": [{"id": "68dc65a0f2d7fb28743f5860", "type": "commentCard", "date": "2025-09-30T23:20:00Z", "idMemberCreator": "4b4a68fc0fec0b254e4f9d8e", "idBoard": "6851a6569f3bf818760632ab", "idCard": "68dc52e015f87c50c441d1a9", "data": {"board": {"id": "6851a6569f3bf818760632ab", "name": "ZM ROADMAP", "shortLink": "HSqnngwQ"}, "card": {"id": "68dc52e015f87c50c441d1a9", "idShort": 80, "name": "Halloween push - store + ads (Claire/Martin/Marcus)", "shortLink": "7979f6E4"}, "idCard": "68dc52e015f87c50c441d1a9", "list": {"id": "6851a677e090018224fb8c7f", "name": "Oct 21"}, "text": "Julia's 4:5 static (They're coming, stop them!) is still running on iOS UK and is still our best CPI there. It never made it onto the live creatives sheet, so count it in for Halloween.", "textData": {"emoji": {}}}, "memberCreator": {"id": "4b4a68fc0fec0b254e4f9d8e", "fullName": "Frederick Stone", "username": "frederick.stone", "initials": "FS", "avatarUrl": null}}]}
```

Envelope: `total_count`, `limit`, `offset`, `has_more`, `comments`. The comment text is at `data.text`, and the author is `memberCreator.fullName`, which is a real display name here. Dates are ISO UTC.

Full-card extra, a `createCard` action from Leonard (B4#27):
```text
{"id": "68dc52e00c3711a8c59f3b0c", "type": "createCard", "date": "2025-09-30T22:00:00Z", "idMemberCreator": "PERSON_6094_TRELLO_USER_ID", "idBoard": "6851a6569f3bf818760632ab", "idCard": "68dc52e015f87c50c441d1a9", "data": {"board": {"id": "6851a6569f3bf818760632ab", "name": "ZM ROADMAP", "shortLink": "HSqnngwQ"}, "card": {"id": "68dc52e015f87c50c441d1a9", "idShort": 80, "name": "Halloween push - store + ads (Claire/Martin/Marcus)", "shortLink": "7979f6E4"}, "list": {"id": "6851a677e090018224fb8c7f", "name": "Oct 21"}}, "memberCreator": {"id": "PERSON_60
```

### Comment on "Marketing Video Refresh"

**0/7.** The strings `Marketing Video Refresh`, `68768a1501ae552dbee94b8a` and `old zombies` appear in no tool output in any run. Every Trello call targeted the Halloween card. The only other Trello fact any run saw is the board: `6851a6569f3bf818760632ab`, "ZM ROADMAP".

## 7. Linear

### Every `linear_list_issues` call

| Call | Input | Returned | `hasNextPage` / `cursor` | ART-826 | ART-831 |
|---|---|---|---|---|---|
| B1#27 | `{"team": "Art", "limit": 250, "fields": ["identifier", "title", "status", "assignee", "createdAt"], "includeArchived": true}` | SPILL, 64,342 chars. 250 rows once parsed | true | yes | yes |
| B2#24 | `{"team": "Art", "query": "julia", "limit": 20}` | 8 | false / - | yes | no |
| B2#88 | `{"team": "Art", "createdAt": "2025-09-01", "limit": 100, "fields": ["title", "status", "assignee", "createdAt"]}` | 62 | false / - | yes | yes |
| B2#91 | `{"query": "store screenshots icon", "limit": 20, "fields": ["title", "status", "assignee", "team", "createdAt"]}` | 20 | true / ZOM-521 | no | no |
| B3#96 | `{"team": "Art", "limit": 40, "orderBy": "createdAt", "fields": ["title", "status", "assignee", "createdAt"]}` | 40 | true / ART-815 | yes | yes |
| B3#233 | `{"team": "Art", "state": "Todo", "limit": 100, "fields": ["assignee", "dueDate"], "updatedAt": "2025-10-01T07:00:00Z"}` | 48 | false / - | yes | yes |
| B4#28 | `{"team": "ART", "limit": 100, "fields": ["title", "description", "status", "assignee", "labels", "createdAt"], "orderBy": "createdAt"}` | 100 | true / ART-709 | yes | yes |
| B4#151 | `{"team": "ART", "limit": 70, "orderBy": "createdAt", "fields": ["assignee", "dueDate"]}` | 70 | true / ART-777 | yes | yes |
| B5#20 | `{"team": "Art", "limit": 250, "fields": ["identifier", "title", "description", "status", "assignee", "createdBy", "updatedAt"], "includeArchived": true}` | SPILL, 122,653 chars. 250 rows once parsed | true | yes | yes |
| B5#23 | `{"team": "Art", "limit": 250, "cursor": "ART-450", "fields": ["identifier", "title", "status"], "includeArchived": true, "maxDescriptionChars": 0}` | 250 | true / ART-337 | no | no |
| B6#28 | `{"team": "ART", "limit": 250, "fields": ["identifier", "title", "status", "assignee", "createdAt", "labels"], "orderBy": "createdAt"}` | SPILL, 73,518 chars. 250 rows once parsed | true | yes | yes |
| B6#34 | `{"team": "ART", "limit": 62, "fields": ["identifier", "title", "description"], "orderBy": "createdAt"}` | 62 | true / ART-793 | yes | yes |
| B6#93 | `{"query": "halloween", "fields": ["identifier", "title", "status", "assignee", "team"]}` | 0 | false / - | no | no |
| PC#29 | `{"team": "Art", "query": "julia", "limit": 50, "fields": ["title", "status", "assignee", "createdAt"]}` | 8 | false / - | yes | no |

The spilled rows are marked from the Bash reads that followed (B1#28, B5#22, B6#29), which show the 250 rows and `hasNextPage`. All three reads contain both tickets. B1#28 and B5#22 show the cursor `ART-450`; B6#29 shows the `cursor` key.

### What reaches ART-826 and ART-831, and pagination

- **Best filter:** `{"team": "Art", "createdAt": "2025-09-01", "limit": 100, "fields": ["title", "status", "assignee", "createdAt"]}` (B2#88). It returned exactly 62 issues, the contiguous ART-793 to ART-854, with `hasNextPage: false`, so no pagination. ART-792 was created 2025-08-26, so the date cleanly splits the library. 10,413 chars, no spill. The 62 include the four archived ART-836 to ART-839 (status mix: {'Done': 58, 'Canceled': 4}). None has an assignee.
- **Also works:** `{"team": "ART", "limit": 62, "orderBy": "createdAt", ...}` (B6#34) returns the same 62, newest first, but `hasNextPage` is true because older issues exist.
- **Partial:** `query: "julia"` reaches ART-826 but not ART-831. It returns 8 issues: the 7 Julia statics and ART-749.
- **Not needed:** a cursor. Only B5 used one (`"cursor": "ART-450"`), which moved on to less recently updated, irrelevant issues. The cursor is an issue identifier, not an opaque token.
- `team` accepts `"Art"` or `"ART"`. Default sort is `updatedAt` descending (rows in B2#24 strictly descend), which puts ART-831 first in the library because it was updated Sep 29.
- Spill threshold: 41,314 chars passed (B4#28) and 64,342 spilled (B1#27). `limit: 250` spilled in 3 of 4 calls. B5#23 fit in 37,846 chars by asking only for `identifier`, `title` and `status` with `maxDescriptionChars: 0`.

### How each run actually reached the two tickets

| Run | ART-826 | ART-831 |
|---|---|---|
| B1 | Team list, spill, Bash (#28) | Same |
| B2 | `query: "julia"` (#24) | Walked ticket numbers: `linear_list_comments` #62, no listing first |
| B3 | Walked ticket numbers (#68), then `linear_get_issue` #79 | Walked ticket numbers (#73), then `linear_get_issue` #80 |
| B4 | Team list `limit: 100` (#28) | Same |
| B5 | Team list, spill, Bash (#22) | Same |
| B6 | Team list, spill, Bash (#29) | Same |
| PC | `query: "julia"` (#29) | **Never.** No read, no comment, no update on ART-831 |

linear_list_issues with fields (B2#88)

Input:
```json
{"team": "Art", "createdAt": "2025-09-01", "limit": 100, "fields": ["title", "status", "assignee", "createdAt"]}
```

Output (chars 0-480 of 9156):
```text
{"issues": [{"id": "ART-831", "title": "marcus portrait UA end card (9:16 end card)", "createdAt": "2025-09-08T16:38:00Z", "status": "Done", "statusType": "completed"}, {"id": "ART-854", "title": "balloons alpha 50 (1) 16:9 (16:9 video)", "createdAt": "2025-09-25T17:00:00Z", "status": "Done", "statusType": "completed"}, {"id": "ART-853", "title": "couch alpha 50 4:5 (4:5 video)", "createdAt": "2025-09-23T16:10:00Z", "status": "Done", "statusType": "completed"}, {"id": "ART-83
```

Without `fields`, each row is the full issue object (B2#24, first row):
```text
{"id": "ART-849", "uuid": null, "identifier": "ART-849", "number": 849, "title": "julia 1:1 android tablet (1:1 static)", "description": "UA creative library: julia 1:1 android tablet (1:1 static). Made by Julia Lawson. Capture notes in the comments.", "priority": {"value": 0, "name": "No priority"}, "estimate": null, "url": "https://linear.app/harmonygames/issue/ART-849/julia-1-1-android-tablet-1-1-static", "gitBranchName": "clairemorgan/art-849-julia-1-1-android-tablet-1-1-static", "createdAt": "2025-09-15T16:06:00Z", "updatedAt": "2025-09-15T16:07:00Z", "archivedAt": null, "completedAt": "2025-09-15T16:07:00Z", "startedAt": "2025-09-15T16:06:00Z", "canceledAt": null, "dueDate": null, "status": "Done", "statusType": "completed", "labels": [], "links": [], "createdBy": "frederick.stone@harmonygames.co", "createdById": "usr_175c0d7bc72ed244", "team": "Art", "teamId": "team_ART", "timeInStatusMinutes": 22494, "isArchived": false}
```

### How state and assignee render

| Thing | Rendering |
|---|---|
| State | `"status": "Done", "statusType": "completed"`. There is no `state` key in output, although the write input is `state` |
| Assignee, set | `"assignee": "marcus.bennett@harmonygames.co", "assigneeId": "usr_c77c50cc15c5342d"` |
| Assignee, unset | Both keys absent, not null |
| Assignee, masked person | `"assignee": "EMPLOYEE_0032_NAME", "assigneeId": "usr_EMPLOYEE_0032"` (B2#91) |
| Creator | `createdBy` email and `createdById` |
| Team | `"team": "Art", "teamId": "team_ART"` |
| Priority | `{"value": 0, "name": "No priority"}` |
| `fields` projection | `id` always comes back. Asking for `status` also returns `statusType`; `assignee` also returns `assigneeId` when set; `team` also returns `teamId` |

### `linear_get_issue`

11 calls in 6/7 (not B4). Input key is `id`. It adds `attachments` and `stateHistory` to the row shape.

linear_get_issue (B2#82)

Input:
```json
{"id": "ART-831"}
```

Output (complete):
```text
{"id": "ART-831", "uuid": null, "identifier": "ART-831", "number": 831, "title": "marcus portrait UA end card (9:16 end card)", "description": "UA creative library: portrait UA end card (Marcus, Jul 31). Plays after every Android US phone video. Capture and master notes in the comments.", "priority": {"value": 0, "name": "No priority"}, "estimate": null, "url": "https://linear.app/harmonygames/issue/ART-831/marcus-portrait-ua-end-card-9-16-end-card", "gitBranchName": "clairemorgan/art-831-marcus-portrait-ua-end-card-9-16-end-card", "createdAt": "2025-09-08T16:38:00Z", "updatedAt": "2025-09-29T17:40:00Z", "archivedAt": null, "completedAt": "2025-09-29T17:40:00Z", "startedAt": "2025-09-08T16:38:00Z", "canceledAt": null, "dueDate": null, "status": "Done", "statusType": "completed", "labels": [], "links": [], "attachments": [], "createdBy": "frederick.stone@harmonygames.co", "createdById": "usr_175c0d7bc72ed244", "team": "Art", "teamId": "team_ART", "timeInStatusMinutes": 2241, "isArchived": false, "stateHistory": []}
```

### `linear_list_comments`

415 calls, 7/7. Input is `{"issueId": "ART-793"}`; B4 twice added `limit: 3`. `hasNextPage` was false on every call and the most comments on one ticket was 2. **Newest comment first.** The author `name` is an email.

Coverage of the 58 live tickets: all in 6/7. PC read 57, missing ART-831. B2 alone also read the 4 archived tickets, which returned no comments.

linear_list_comments, ART-831 (B3#73)

Input:
```json
{"issueId": "ART-831"}
```

Output (complete):
```text
{"comments": [{"id": "cmt_art831_2", "body": "Still running on Unity: Android US phone (checked Sep 29). Not on the live creatives sheet yet.", "attachments": [], "createdAt": "2025-09-29T17:40:00Z", "updatedAt": "2025-09-29T17:40:00Z", "parentId": null, "resolvedAt": null, "quotedText": null, "author": {"id": "usr_175c0d7bc72ed244", "name": "frederick.stone@harmonygames.co"}, "onBehalfOf": null, "issueId": "ART-831", "isEdited": false}, {"id": "cmt_art831_1", "body": "Rendered from Android #1450 footage (Jul 29). Master: SFX only, no music. Unity: Android US phone.", "attachments": [], "createdAt": "2025-09-08T16:39:00Z", "updatedAt": "2025-09-08T16:39:00Z", "parentId": null, "resolvedAt": null, "quotedText": null, "author": {"id": "usr_175c0d7bc72ed244", "name": "frederick.stone@harmonygames.co"}, "onBehalfOf": null, "issueId": "ART-831", "isEdited": false}], "hasNextPage": false}
```

ART-826 (B3#68):
```text
{"comments": [{"id": "cmt_art826_1", "body": "Made from Android #852 captures (Jun 5). Unity: iOS UK phone.", "attachments": [], "createdAt": "2025-09-08T16:34:00Z", "updatedAt": "2025-09-08T16:34:00Z", "parentId": null, "resolvedAt": null, "quotedText": null, "author": {"id": "usr_175c0d7bc72ed244", "name": "frederick.stone@harmonygames.co"}, "onBehalfOf": null, "issueId": "ART-826", "isEdited": false}], "hasNextPage": false}
```

### Helpers

| Tool | Input | Runs | Output notes |
|---|---|---|---|
| `linear_list_issue_statuses` | `{"team": "Art"}` | 2/7 (B3, PC) | Backlog, Todo, Team Epic, In Review, Done, Canceled, Duplicate, with `id`, `type`, `issueCount` |
| `linear_list_users` | `{"query": "mar"}` (B3), `{"query": "ma"}` (PC), `{"query": "harmonygames", "limit": 100}` (B4) | 3/7 | `name`, `email` and `displayName` are all the email for these people |
| `linear_list_teams` | `{}` or `{"query": "art"}` | 2/7 (B4, B6) | Art `team_ART` key `ART`; also DES, ENG, ZOM, EPI |

User ids seen: Marcus `usr_c77c50cc15c5342d`, Martin `usr_51f5f16d46e8cf55`, Claire `usr_7fe31e7ec8199618`, Frederick `usr_175c0d7bc72ed244`. Julia `usr_8140f09bf9f1b94c` with email `julia.lawson@harmonygames.co` (B4#103). Note there is also a separate `marcus.lee@harmonygames.co`, `usr_b501f018a4c5319f`.

## 8. Writes

All ids below are from one run and differ per run. Use placeholders in the Oracle Events.

### Summary

| Tool | Calls | Runs | Input keys | Returns a URL? |
|---|---|---|---|---|
| `gdocs_create_document` | 7 | 7/7 | `title`, `bodyText` (6/7); `title` only (B4) | **No.** `documentId` and `driveFileId` only |
| `gsheets_create_spreadsheet` | 7 | 7/7 | `title`, `initialSheetTitle` | **Yes,** `spreadsheetUrl`, plus `spreadsheetId` and `driveFileId` |
| `gsheets_batch_update` | 7 | 7/7 | `spreadsheetId`, `requests` (`addSheet`) | No |
| `gsheets_values_update` | 27 | 7/7 | `spreadsheetId`, `range`, `valueInputOption`, `values` | No |
| `gdrive_share_file` | 84 | 7/7 | `fileId`, `emailAddress`, `role` | **Yes,** `file.webViewLink` |
| `linear_create_comment` | 406 | 7/7 | `issueId`, `body` | No |
| `linear_update_issue` | 329 | 7/7 | `id`, `assignee`, `dueDate`, sometimes `state` | Yes, `url` |
| `linear_create_issue` | 14 | 7/7 | `team`, `title`, `description`, `assignee`, `dueDate`, optional `state`, `priority` | Yes, `url` |
| `slack_send_message` | 7 | 7/7 | `channel_id`, `thread_ts`, `message` | Yes, `message_link` |

### `gdocs_create_document`

gdocs_create_document (B1#104)

Input:
```json
{"title": "ZM3D Halloween 2025 - art plan", "bodyText": "ZM3D Halloween 2025 - art plan\nOwner: Claire Morgan (Art). For the Halloween review, Thu Oct 2. Comments welcome.\nTracker (one row per surface and per ad, with call, make ...[truncated here, 7990 chars total]"}
```

Output (complete):
```text
{"documentId": "72c0c509b3fff09344e0698b", "title": "ZM3D Halloween 2025 - art plan", "name": "ZM3D Halloween 2025 - art plan", "revisionId": "56458fbb9f06066138a0", "driveFileId": "72c0c509b3fff09344e0698b", "driveVisible": true, "owners": ["claire.morgan@harmonygames.co"], "createdTime": "2025-10-01T07:05:59Z", "modifiedTime": "2025-10-01T07:05:59Z"}
```

Doc id is 24 hex characters. The URL pattern is `https://docs.google.com/document/d/<documentId>/edit`. Runs got it from `gdrive_get_file_metadata` (`{"fileId": "<documentId>"}`, 4/7: B1, B3, B4, PC) or from a `gdrive_share_file` response. Before sharing, metadata shows `"shared": false`, `"ownedByMe": true` and a single owner permission:
```text
{"id": "72c0c509b3fff09344e0698b", "name": "ZM3D Halloween 2025 - art plan", "mimeType": "application/vnd.google-apps.document", "parents": ["d_7fe31e7ec81996189e1f14"], "owners": [{"emailAddress": "claire.morgan@harmonygames.co", "displayName": "claire.morgan@harmonygames.co"}], "permissions": [{"id": "e367b9062d8a", "type": "user", "emailAddress": "claire.morgan@harmonygames.co", "role": "owner", "displayName": "claire.morgan@harmonygames.co"}], "shared": false, "modifiedTime": "2025-10-01T07:05:59Z", "createdTime": "2025-10-01T07:05:59Z", "ownedByMe": true, "webViewLink": "https://docs.google.com/document/d/72c0c509b3fff09344e0698b/edit"}
```

With `title` only (B4#108), the output also includes a `body.content` structure. B4 then filled it with `gdocs_batch_update` `insertText` at index 1 (B4#123). B2 and PC used `replaceAllText` to fix text after creation (B2#99, PC#108).

### `gsheets_create_spreadsheet`

gsheets_create_spreadsheet (B1#97)

Input:
```json
{"title": "ZM3D Halloween 2025 - art tracker", "initialSheetTitle": "Ads"}
```

Output (complete):
```text
{"spreadsheetId": "1hhsNIRs4oTen_AVqgDjRveIqyCI41QVCNUS_FwkQ94w", "title": "ZM3D Halloween 2025 - art tracker", "properties": {"title": "ZM3D Halloween 2025 - art tracker"}, "sheets": [{"properties": {"sheetId": 0, "title": "Ads", "index": 0, "sheetType": "GRID", "gridProperties": {"rowCount": 1000, "columnCount": 26}}}], "spreadsheetUrl": "https://docs.google.com/spreadsheets/d/1hhsNIRs4oTen_AVqgDjRveIqyCI41QVCNUS_FwkQ94w/edit", "driveFileId": "1hhsNIRs4oTen_AVqgDjRveIqyCI41QVCNUS_FwkQ94w", "owners": ["claire.morgan@harmonygames.co"], "createdTime": "2025-10-01T07:04:08Z", "modifiedTime": "2025-10-01T07:04:08Z"}
```

Spreadsheet id is 44 characters, for example `1hhsNIRs4oTen_AVqgDjRveIqyCI41QVCNUS_FwkQ94w`. Extra tabs were added with `gsheets_batch_update`:

gsheets_batch_update (B1#98)

Input:
```json
{"spreadsheetId": "1hhsNIRs4oTen_AVqgDjRveIqyCI41QVCNUS_FwkQ94w", "requests": [{"addSheet": {"properties": {"title": "Store", "index": 0}}}, {"addSheet": {"properties": {"title": "Key dates", "index": 2}}}]}
```

Output (complete):
```text
{"spreadsheetId": "1hhsNIRs4oTen_AVqgDjRveIqyCI41QVCNUS_FwkQ94w", "driveFileId": "1hhsNIRs4oTen_AVqgDjRveIqyCI41QVCNUS_FwkQ94w", "replies": [{"addSheet": {"properties": {"sheetId": 1387155845, "title": "Store", "index": 0, "sheetType": "GRID", "gridProperties": {"rowCount": 1000, "columnCount": 26}}}}, {"addSheet": {"properties": {"sheetId": 1227695172, "title": "Key dates", "index": 2, "sheetType": "GRID", "gridProperties": {"rowCount": 1000, "columnCount": 26}}}}], "modifiedTime": "2025-10-01T07:04:11Z"}
```

### `gsheets_values_update`

gsheets_values_update (B1#101)

Input:
```json
{"spreadsheetId": "1hhsNIRs4oTen_AVqgDjRveIqyCI41QVCNUS_FwkQ94w", "range": "Ads!A1", "valueInputOption": "RAW", "values": "[[\"ART ticket\", \"Creative\", \"Format\", \"Serving today\", \"Serving in Halloween flight (Oct 18-31)\", \"Current source\", \"Halloween call\", \"Maker\", \"Due\", \"Notes\", \"Status\"], [\"ART-793\", \"couch boss 30\", \" ...[truncated here, 59 items]"}
```

Output (complete):
```text
{"spreadsheetId": "1hhsNIRs4oTen_AVqgDjRveIqyCI41QVCNUS_FwkQ94w", "driveFileId": "1hhsNIRs4oTen_AVqgDjRveIqyCI41QVCNUS_FwkQ94w", "updatedRange": "Ads!A1:K59", "updatedRows": 59, "updatedColumns": 11, "updatedCells": 649, "modifiedTime": "2025-10-01T07:05:10Z"}
```

`valueInputOption`: RAW 21, USER_ENTERED 4, omitted 2 (B5#106 and B5#107 worked). Ranges with a space work quoted (`'Key dates'!A1`) or unquoted (`Key dates!A1`, B4#117); the response always quotes them.

### `gdrive_share_file`

gdrive_share_file (B1#106)

Input:
```json
{"fileId": "72c0c509b3fff09344e0698b", "emailAddress": "leonard.hayes@harmonygames.co", "role": "commenter"}
```

Output (complete):
```text
{"id": "31517f623007", "type": "user", "emailAddress": "leonard.hayes@harmonygames.co", "role": "commenter", "displayName": "leonard.hayes@harmonygames.co", "domain": null, "actor": "claire.morgan@harmonygames.co", "file": {"id": "72c0c509b3fff09344e0698b", "name": "ZM3D Halloween 2025 - art plan", "mimeType": "application/vnd.google-apps.document", "webViewLink": "https://docs.google.com/document/d/72c0c509b3fff09344e0698b/edit"}}
```

84 of 84 calls used `role: "commenter"`, 12 per run: 6 people on 2 files. The six were leonard.hayes, frederick.stone, martin.walsh, marcus.bennett, robert and arthur.blake (@harmonygames.co). `type` was never passed.

### `linear_create_comment`

linear_create_comment (B1#122)

Input:
```json
{"issueId": "ART-793", "body": "**Halloween call: Refresh first.** Current source: Android #440 (Apr 5), SFX-only master. This predates Robert's cutoff (Android #1452 / iOS 1232, the Jul 29 zombie swap with the new background), so it gets re-captured/re-rendered on the cu ...[truncated here, 715 chars total]"}
```

Output (chars 0-1050 of 1072):
```text
{"id": "comment_d9d3025303434612b6886310c8890f1b", "body": "**Halloween call: Refresh first.** Current source: Android #440 (Apr 5), SFX-only master. This predates Robert's cutoff (Android #1452 / iOS 1232, the Jul 29 zombie swap with the new background), so it gets re-captured/re-rendered on the current build before the seasonal pass. Then the Halloween pass: seasonal layer only, same background, pose, zombie order and CTA. Serves in the Halloween flight on: iOS UK phone, Android US phone. **Due:** refresh by Fri Oct 10; Halloween version to Frederick by **Wed Oct 15**. **Maker:** Marcus Bennett. Plan: https://docs.google.com/document/d/72c0c509b3fff09344e0698b/edit | Tracker: https://docs.google.com/spreadsheets/d/1hhsNIRs4oTen_AVqgDjRveIqyCI41QVCNUS_FwkQ94w/edit", "attachments": [], "createdAt": "2025-10-01T07:06:55Z", "updatedAt": "2025-10-01T07:06:55Z", "parentId": null, "resolvedAt": null, "quotedText": null, "author": {"id": "usr_7fe31e7ec8199618", "name": "claire.morgan@harmonygames.co"}, "onBehalfOf": null, "issueId": "ART-79
```

Comment ids are `comment_<32 hex>`. Markdown in `body` is stored verbatim. 58 per run in B1 to B6, covering ART-793 to ART-854 minus ART-836 to ART-839. PC made 57, missing ART-831.

### `linear_update_issue`

Without state (B2#171)

Input:
```json
{"id": "ART-793", "assignee": "marcus.bennett@harmonygames.co", "dueDate": "2025-10-15"}
```

Output (complete):
```text
{"id": "ART-793", "uuid": null, "identifier": "ART-793", "number": 793, "title": "couch boss 30 (9:16 video)", "description": "UA creative library: couch boss 30 (9:16 video). Made by Frederick Stone. Capture and master notes in the comments.", "priority": {"value": 0, "name": "No priority"}, "estimate": null, "url": "https://linear.app/harmonygames/issue/ART-793/couch-boss-30-9-16-video", "gitBranchName": "clairemorgan/art-793-couch-boss-30-9-16-video", "createdAt": "2025-09-08T16:00:00Z", "updatedAt": "2025-10-01T07:08:39Z", "archivedAt": null, "completedAt": "2025-09-09T17:30:00Z", "startedAt": "2025-09-08T16:00:00Z", "canceledAt": null, "dueDate": "2025-10-15", "status": "Done", "statusType": "completed", "labels": [], "links": [], "createdBy": "frederick.stone@harmonygames.co", "createdById": "usr_175c0d7bc72ed244", "assignee": "marcus.bennett@harmonygames.co", "assigneeId": "usr_c77c50cc15c5342d", "team": "Art", "teamId": "team_ART", "timeInStatusMinutes": 31058, "isArchived": false, "stateHistory": []}
```

With state (B1#180)

Input:
```json
{"id": "ART-825", "assignee": "martin.walsh@harmonygames.co", "dueDate": "2025-10-15", "state": "Todo"}
```

Output (complete):
```text
{"id": "ART-825", "uuid": null, "identifier": "ART-825", "number": 825, "title": "julia 1:1 (1:1 static)", "description": "UA creative library: julia 1:1 (1:1 static). Made by Julia Lawson. Capture notes in the comments.", "priority": {"value": 0, "name": "No priority"}, "estimate": null, "url": "https://linear.app/harmonygames/issue/ART-825/julia-1-1-1-1-static", "gitBranchName": "clairemorgan/art-825-julia-1-1-1-1-static", "createdAt": "2025-09-08T16:32:00Z", "updatedAt": "2025-10-01T07:10:08Z", "archivedAt": null, "completedAt": null, "startedAt": null, "canceledAt": null, "dueDate": "2025-10-15", "status": "Todo", "statusType": "unstarted", "labels": [], "links": [], "createdBy": "frederick.stone@harmonygames.co", "createdById": "usr_175c0d7bc72ed244", "assignee": "martin.walsh@harmonygames.co", "assigneeId": "usr_51f5f16d46e8cf55", "team": "Art", "teamId": "team_ART", "timeInStatusMinutes": 0, "isArchived": false, "stateHistory": [{"state": {"id": "state_adefefc54cfc5bc7", "name": "In Review", "type": "started"}, "startedAt": "2025-09-08T16:32:00Z", "endedAt": "2025-09-09T17:30:00Z"}, {"state": {"id": "state_164b3f7490cc5fd9", "name": "Done", "type": "completed"}, "startedAt": "2025-09-09T17:30:00Z", "endedAt": "2025-10-01T07:10:08Z"}, {"state": {"id": "state_6e9ebc9fea5453c0", "name": "Todo", "type": "unstarted"}, "startedAt": "2025-10-01T07:10:08Z", "endedAt": null}]}
```

| Question | Answer |
|---|---|
| How was assignee passed? | Email, 329/329. Never id or name |
| Assignee values | `marcus.bennett@harmonygames.co` 287, `martin.walsh@harmonygames.co` 42, Julia 0 |
| `dueDate` | `"2025-10-15"` in 329/329. Format is `YYYY-MM-DD` |
| `state` | `"Todo"` in 92 calls, all in B1 (46) and B3 (46). Omitted in 237 |
| Effect of omitting `state` | Ticket stays `Done`, `completed`, with `completedAt` kept. So 5/7 runs left assigned tickets showing Done |
| Effect of `state: "Todo"` | `status: Todo`, `statusType: unstarted`, `completedAt: null`, and `stateHistory` gains entries |
| Updates per run | B1 46, B2 48, B3 46, B4 48, B5 48, B6 46, PC 47 |

### `linear_create_issue`

With state (B1#95)

Input:
```json
{"team": "Art", "title": "ZM3D Halloween app icon (App Store + Google Play)", "assignee": "martin.walsh@harmonygames.co", "dueDate": "2025-10-13", "state": "Todo", "description": "Halloween version of the live app icon (live since Sep 17 on App Store + Google Play) for the ZM3D Halloween push.\n\n**Direction (Robert):** keep it as simple as the current icon - only the seasonal la ...[truncated here, 1144 chars total]"}
```

Output (chars 0-480 of 2218):
```text
{"id": "ART-855", "uuid": null, "identifier": "ART-855", "number": 855, "title": "ZM3D Halloween app icon (App Store + Google Play)", "description": "Halloween version of the live app icon (live since Sep 17 on App Store + Google Play) for the ZM3D Halloween push.\n\n**Direction (Robert):** keep it as simple as the current icon - only the seasonal layer changes (pumpkin / fog / prop / title treatment), same character, pose and flat background. The Sep 17 concept in #zombie-ar
```

Tail of that output:
```text
025-10-01T07:04:01Z", "updatedAt": "2025-10-01T07:04:01Z", "archivedAt": null, "completedAt": null, "startedAt": null, "canceledAt": null, "dueDate": "2025-10-13", "status": "Todo", "statusType": "unstarted", "labels": [], "links": [], "createdBy": "claire.morgan@harmonygames.co", "createdById": "usr_7fe31e7ec8199618", "assignee": "martin.walsh@harmonygames.co", "assigneeId": "usr_51f5f16d46e8cf55", "team": "Art", "teamId": "team_ART", "timeInStatusMinutes": 0, "isArchived": false, "stateHistory": [{"state": {"id": "state_6e9ebc9fea5453c0", "name": "Todo", "type": "unstarted"}, "startedAt": "2025-10-01T07:04:01Z", "endedAt": null}]}
```

| Run | `team` | `state` sent | Result status | `priority` sent | Result priority | `dueDate` (icon, iPad) | Ticket ids |
|---|---|---|---|---|---|---|---|
| B1 | `Art` | Todo | Todo | omitted | No priority | 2025-10-13, 2025-10-14 | icon ART-855, iPad ART-856 |
| B2 | `Art` | omitted | Backlog | 2 | High | 2025-10-16, 2025-10-16 | icon ART-855, iPad ART-856 |
| B3 | `Art` | Todo | Todo | omitted | No priority | 2025-10-14, 2025-10-14 | icon ART-855, iPad ART-856 |
| B4 | `ART` | Todo | Todo | 2 | High | 2025-10-16, 2025-10-16 | icon ART-856, iPad ART-855 |
| B5 | `Art` | Todo | Todo | 2 | High | 2025-10-16, 2025-10-16 | icon ART-855, iPad ART-856 |
| B6 | `ART` | omitted | Backlog | omitted | No priority | 2025-10-14, 2025-10-16 | icon ART-855, iPad ART-856 |
| PC | `Art` | Todo | Todo | 2 | High | 2025-10-14, 2025-10-15 | icon ART-855, iPad ART-856 |

`assignee` was `martin.walsh@harmonygames.co` in 14/14. Omitting `state` gives **Backlog** (B2, B6), not Todo. `team` accepts `Art` or `ART`, and output is always `"team": "Art"`. `priority: 2` renders as High. Numbers continue from ART-854, so the first created ticket is ART-855.

### `slack_send_message`

slack_send_message (B1#226)

Input:
```json
{"channel_id": "C06DJBJL798", "thread_ts": "1759269913.882683", "message": "Halloween plan and tracker are ready for Thursday's review. Both are shared with everyone on the invite so you can comment:\n• Plan: https://docs.google.com/document/d/72c0c509b3fff09344e0698b/edit\n• Tracker: https://docs.google.com/spreadsheets/d/1hhsNIRs4oTen_AVqgDjRveIqyCI41QVCNUS_FwkQ94w/edit\n\n** ...[truncated here, 1417 chars total]"}
```

Output (chars 0-500 of 1908):
```text
{"ok": true, "ts": "1759302668.000000", "channel": "C06DJBJL798", "message": {"text": "Halloween plan and tracker are ready for Thursday's review. Both are shared with everyone on the invite so you can comment:\n\u2022 Plan: https://docs.google.com/document/d/72c0c509b3fff09344e0698b/edit\n\u2022 Tracker: https://docs.google.com/spreadsheets/d/1hhsNIRs4oTen_AVqgDjRveIqyCI41QVCNUS_FwkQ94w/edit\n\n**Store**\n\u2022 iPhone 6.5\" and Google Play phone sets: reuse Martin's exports.\n\u2022 New store 
```

Tail of the output:
```text
d.", "user": "EMPLOYEE_0009_SLACK_ID", "thread_ts": "1759269913.882683"}, "message_link": "https://harmonygamesgroup.slack.com/archives/C06DJBJL798/p1759302668000000?thread_ts=1759269913.882683&cid=C06DJBJL798", "message_context": {"message_ts": "1759302668.000000", "channel_id": "C06DJBJL798"}, "thread_ts": "1759269913.882683"}
```

7/7 used `channel_id: "C06DJBJL798"` and `thread_ts: "1759269913.882683"`. The text key is `message`, not `text`. The response echoes `user: "EMPLOYEE_0009_SLACK_ID"`. Mention tokens stay raw in the echo. B1 and B4 used `<@EMPLOYEE_0008_SLACK_ID>` for Frederick; the rest used no mention.

### Failed writes

| Run | Call | What happened | Outcome |
|---|---|---|---|
| B3 | #164 `linear_create_comment` on ART-813 | `ECONNRESET` | Did not land: B3#182 `linear_list_comments` showed only the original comment. Retried at #183, succeeded |
| B4 | #118 `gsheets_values_update` with `COUNTIF`/`COUNTIFS`, USER_ENTERED | Reported success; #119 read `#NAME?` | #120 rewrote with literals but kept `=SUM(...)` totals, and that row was not read back |
| B5 | #102 same | Reported success; #104 read `#NAME?` | #105 `gsheets_values_batch_clear`, then #106 and #107 wrote numbers |
| PC | #104 same | Reported success; #105 read `#NAME?` | #106 rewrote with RAW values |
| B4 | #141, #143 `Agent` subagents for comment batches | Both died with an API error (Item 10) | Their tool calls were Bash only, so no Linear write happened. B4 then posted all 58 itself |

No other write failed. Every other write output was checked for `error`, `ok: false` and `success: false`.

Formula readback (PC#105):
```text
{"range": "Summary!A4:D9", "majorDimension": "ROWS", "values": [["Ads by call", "Count", "Marcus", "Martin"], ["Halloween version", "#NAME?", "#NAME?", "#NAME?"], ["Refresh first", "#NAME?", "#NAME?", "#NAME?"], ["Reuse", "#NAME?", "0", "0"], ["Skip", "#NAME?", "0", "0"], ["Total ads", "#NAME?", "#NAME?", "#NAME?"]]}
```

## 9. Deciding records: who read what

| Record | Runs that read it | Query or read that surfaced it |
|---|---|---|
| Frederick's reply, "Fri Oct 10" | **0/7** | None |
| Marcus's note, "re-recorded 3 of the old ua cuts" | **0/7** | None |
| Robert's reply, "We can't ship these" | **2/7** (B4, B5) | Channel read of #zombie-art, then thread read. No search query |
| Martin's vacation post | **0/7** | None |
| Leonard's "julia on the ad statics" | **0/7** | None |
| Frederick's "Unity retention restart" mail | **5/7** (B1, B3, B4, B5, B6) | `from:frederick.stone@harmonygames.co`, `newer_than:7d`, `newer_than:10d`, `after:2025/09/20` |
| Frederick's Trello comment, "end card 001 still has the old zombies" | **0/7** | None |

### Every Slack search any run made

All 10 searches, which is why nothing on these records surfaced:

| Run | Input |
|---|---|
| B1#13 | `slack_search_public_and_private` `{"query": "halloween", "limit": 40}` |
| B1#93 | `slack_search_public_and_private` `{"query": "ipad screenshots", "limit": 20}` |
| B2#16 | `slack_search_public_and_private` `{"query": "halloween", "limit": 50}` |
| B2#89 | `slack_search_public_and_private` `{"query": "ipad", "after": "1754000000"}` |
| B2#90 | `slack_search_public_and_private` `{"query": "screenshots", "after": "1754000000"}` |
| B3#18 | `slack_search_public_and_private` `{"query": "halloween", "limit": 40, "response_format": "concise"}` |
| B4#94 | `slack_search_public_and_private` `{"query": "halloween", "response_format": "concise"}` |
| B5#84 | `slack_search_public_and_private` `{"query": "halloween", "limit": 50, "response_format": "concise"}` |
| B6#91 | `slack_search_public_and_private` `{"query": "halloween", "limit": 50, "response_format": "concise"}` |
| PC#26 | `slack_conversations_search_messages` `{"search_query": "halloween", "limit": 50}` |

Channels read with `slack_read_channel` were only `C06DJBJL798` and `C08R8CHB0QL`. No run read `C0880U9751A`, `C09ATAJ220H` or `C05KNDCHAAG`, and no run read a thread in any of them.

### What the runs show about Slack search behaviour

These facts support the candidate routes below:

- **Replies are searchable.** B1#13 hit `1758127951.679146`, a reply with `thread_ts: 1758121809.236839`.
- **Multi-word queries behaved as all-words.** `{"query": "ipad screenshots"}` (B1#93) returned 7 messages, all containing both words. This is one sample.
- **Results are newest first** (B1#93 and B1#13), so recent records sit at the top.
- **Default limit is 20**: B4#94 returned 20 of `total_count: 26` with `has_more: true`.
- Search spans channels and DMs the persona can see, including `D05V2N6PZNU` and private channels.
- `after` takes an epoch string (`"after": "1754000000"`, B2#89).
- `slack_conversations_search_messages` takes `search_query` (PC#26) and returned the same 31,671 chars as the other tool with `query`. `slack_conversations_replies` takes `thread_ts` and matches `slack_read_thread`, which takes `message_ts` (B5#85 and B1#14 are both 1,892 chars).

### Frederick's reply, "Fri Oct 10"

Record: channel `C0880U9751A` (#zombie-match3d), reply ts `1759275738.984915`, `thread_ts` `1759211437.306779`.

**0/7.** The markers `manual review`, `Unity rep` and `1759211437.306779` appear in no tool output. `C0880U9751A` did appear, but only in channel listings (`slack_search_channels`, B3's `slack_channels_list`) and on unrelated search hits (Arthur's seasonal themes, Robert's early-2025 posts, Leonard's iPad note).

"Fri Oct 10" appears only in the runs' own writes: B1 (35 `linear_create_comment` echoes, 5 Bash), B2 (37 `linear_create_comment` echoes) and B3 (1 `linear_create_issue` echo). No read output in any run contains it, and neither does any read output contain "Oct 10". Examples:
B1#122 `body`:
```text
**Due:** refresh by Fri Oct 10; Halloween version to Frederick by **Wed Oct 15**.
```

B2#113 `body`:
```text
**Due:** refreshed by Fri Oct 10 · Halloween version to Frederick by **Wed Oct 15**.
```

B3#101 `description`:
```text
Concept for Robert's sign-off: Fri Oct 10
```

Candidate routes, UNTESTED:

- `slack_search_public_and_private {"query": "Unity"}`. The word is in the reply, and the Sep 30 23:42Z timestamp should rank near the top because results are newest first. Frederick's mail and the Read me both name Unity, so it is a natural term.
- `slack_search_public_and_private {"query": "manual review"}`, using words in the record, but less natural because nothing points to them.
- `slack_read_channel` on `C0880U9751A`, then `slack_read_thread {"channel_id": "C0880U9751A", "message_ts": "1759211437.306779"}`. The reply will not show in the channel read. Full format would show the parent's `reply_count`. Per `Working_Files/prompt_eval/evidence_pack.md` (not a trajectory), the parent is Robert's Unity fake-installs post, which does not look Halloween-related.

### Marcus's note, "re-recorded 3 of the old ua cuts"

Record: channel `C09ATAJ220H` (#zm-animations), ts `1758823964.738872`.

**0/7.** The phrase and the word `re-recorded` appear in no tool output. `#zm-animations` was visible only in B3's channel list (#3) and in one unrelated hit, Calvin's message in B2#89.

Caution: build numbers `#1935`, `#1896` and `#1966` do appear in `linear_list_comments`, but on **other tickets**: ART-853, ART-852 and ART-854. The tickets the note corrects still say April in every run:
ART-795 (B1#31):
```text
Captured from Android #456 on Apr 7. Master: SFX only, no music. Unity: iOS UK phone, Android US phone.
```

ART-805 (B1#41):
```text
Captured from Android #633 on Apr 29. Master: SFX only, no music. Unity: iOS UK phone.
```

ART-797 (B1#33):
```text
Captured from Android #456 on Apr 7. Master: SFX only, no music. Unity: iOS UK phone, Android US phone.
```

Candidate routes, UNTESTED: `slack_search_public_and_private {"query": "couch alpha 50"}`, a creative name that is in the note and on the sheet. Or `slack_read_channel {"channel_id": "C09ATAJ220H"}`, since it is not a thread reply; whether it falls within a given `limit` is unknown here. The hardening report calls this Marcus's busiest channel, with 73 posts in September.

### Robert's reply, "We can't ship these"

Record: channel `C08R8CHB0QL` (#zombie-art), reply ts `1759248337.170599`, `thread_ts` `1759167065.499092`.

**2/7.** No search surfaced it. The parent does not contain the word "halloween", so all the `halloween` searches miss the thread.

| Run | Surfaced by | Read by |
|---|---|---|
| B4 | #93 `slack_read_channel` `{"channel_id": "C08R8CHB0QL", "limit": 30, "response_format": "concise"}` | #96 `slack_read_thread` `{"channel_id": "C08R8CHB0QL", "message_ts": "1759167065.499092", "response_format": "concise"}` |
| B5 | #88, same channel read | #90 `slack_conversations_replies` `{"channel_id": "C08R8CHB0QL", "thread_ts": "1759167065.499092"}` |

B1 (#91) and B2 (#18) made the same concise channel read, saw the parent and did not open it. In concise format the parent shows no `reply_count`. B3, B6 and PC never read this channel. Natural route to cite: read #zombie-art, then open Marcus's test post thread.

B5#90 output, reply row:
```text
{"ts": "1759248337.170599", "type": "message", "text": "Fog reads well but this is the July capture, the old background is still under it. We can't ship these, they need doing again from the Sep 16 one", "channel": "C08R8CHB0QL", "user": "EMPLOYEE_0016_SLACK_ID", "thread_ts": "1759167065.499092", "channel_info": {"id": "C08R8CHB0QL", "name": "zombie-art", "is_private": false, "is_im": false, "is_mpim": false}, "user_profile": {"id": "EMPLOYEE_0016_SLACK_ID", "name": "Robert", "real_name": "Robert", "display_name": "Robert", "email": "robert@harmonygames.co"}, "time": "2025-09-30T16:05:37Z", "permalink": "https://harmonygamesgroup.sl
```

### Martin's vacation post and Leonard's reply

Records: channel `C05KNDCHAAG` (#company-internal), Martin ts `1759243286.478812`, Leonard reply ts `1759275107.322377`.

**0/7 for both.** The words `vacation` and `ad statics` appear in no tool output. `C05KNDCHAAG` appeared only on 2024 "Happy Halloween" and iPad hits, and in B3's channel list. Consequence: all 42 `linear_update_issue` calls for the six working Julia statics (ART-825 to ART-830, 6 per run) assigned Martin. None assigned Julia.

Candidate routes, UNTESTED: `slack_search_public_and_private {"query": "vacation"}` for Martin's post, then `slack_read_thread {"channel_id": "C05KNDCHAAG", "message_ts": "1759243286.478812"}` for Leonard's reply. Or `slack_read_channel {"channel_id": "C05KNDCHAAG"}`; the post is one day before the clock. The post's mention will render raw as `<@EMPLOYEE_0005_SLACK_ID>`.

### Frederick's "Unity retention restart" mail

Thread `claire.morgan@harmonygames.co/1844644077950167516`, message `claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>`.

| Run | First surfaced by | Body read by |
|---|---|---|
| B1 | #18 `from:frederick.stone@harmonygames.co` | #20 `gmail_get_thread` |
| B3 | #7 `newer_than:7d` | #20 `gmail_get_message` (#16 batch had headers only) |
| B4 | #8 `newer_than:10d` | #15 `gmail_get_message` (#12 batch had headers only) |
| B5 | #11 `gmail_list_messages` `after:2025/09/20` | #13 `gmail_get_messages_batch` with `format: full` |
| B6 | #15 `from:frederick.stone@harmonygames.co` | #18 `gmail_get_thread`, decoded in Bash at #19 |
| B2, PC | Never surfaced. Each ran only `october UA plan` | Not read |

Natural route to cite: `gmail_search_messages {"query": "from:frederick.stone@harmonygames.co", "user_email": "claire.morgan@harmonygames.co"}`, which returns exactly his 3 mails (B1#18), then `gmail_get_thread`. Keyword queries missed it: `october UA plan`, `october OR halloween OR UA` and `october OR halloween OR seasonal` all exclude it.

gmail_search_messages (B1#18)

Input:
```json
{"query": "from:frederick.stone@harmonygames.co", "user_email": "claire.morgan@harmonygames.co", "max_results": 20}
```

Output (complete):
```text
{"messages": [{"id": "claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>", "threadId": "claire.morgan@harmonygames.co/1844732284519287777"}, {"id": "claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>", "threadId": "claire.morgan@harmonygames.co/1844644077950167516"}, {"id": "claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>", "threadId": "claire.morgan@harmonygames.co/1843080777036925215"}], "resultSizeEstimate": 3, "nextPageToken": null}
```

### Frederick's Trello comment, "end card 001 still has the old zombies"

Record: card `68768a1501ae552dbee94b8a` (Marketing Video Refresh), action `68d6cff0c6568da5d9c8e81f`, list "Jul 24", board "ZM ROADMAP".

**0/7.** See Item 6. Candidate routes, UNTESTED:

- `trello_search {"query": "end card"}`. The default search returns `actions`. Caution: the only comment hit seen also sits on a card with "Halloween" in its name, so these runs do not prove the search matches comment text alone.
- `trello_get_comments {"cardId": "68768a1501ae552dbee94b8a"}`. This input form is proven, but no run saw this card id. A board-level call is needed first, and no run made one, so neither its parameters nor its output are evidenced.

### Related reads worth citing

| Thread or record | Runs | Note |
|---|---|---|
| Martin's store export post, `C08R8CHB0QL/1759245641.309714` | 7/7 | Surfaced by `halloween`. Leonard's reply says no tickets are needed for what is already exported |
| Frederick's Aug 13 music thread, `C06DJBJL798/1755114007.441789` | 7/7 | 16 messages. `reply_count: 15` |
| Martin's icon thread, `C08R8CHB0QL/1758121809.236839` | 4/7 (B3, B4, B5, B6) | Robert: icon stays simple. The reply text also surfaced in `halloween` search in all runs |
| Claire and Marcus DM, `D05V2N6PZNU/1758872409.023532` | 4/7 (B3, B4, B5, B6) | Marcus's cheer fastcouch test. Surfaced by `halloween` |
| Trello Julia 4:5 comment | 7/7 | Points to ART-826 |
| `confluence_search {"text": "seasonal"}` | 5/7 | B1 also read `confluence_get_page {"page_id": "page_liveops_calendar"}` |

## 10. Every tool error

`03_Error_Async_Config.txt` says `Friction: none`, so nothing below is injected.

### Flagged `is_error` (6)

| Call | Tool | Error text |
|---|---|---|
| B3#164 | `linear_create_comment` | `ECONNRESET: The socket connection was closed unexpectedly. For more information, pass `verbose: true` in the second argument to fetch()` |
| B4#24 | `trello_get_card` | `{"error": "attachments must be true, false, or \"cover\"", "code": "invalid_value"}` |
| B4#141 | `Agent` | `Agent terminated early due to an API error: Autocompact is thrashing: the context refilled to the limit within 3 turns of the previous compact, 3 times in a row. A file being read or a tool output is likely too large for the context window. Try reading in smaller chunks, or use /clear to start fresh. (error type invalid_request)` |
| B4#143 | `Agent` | `Agent terminated early due to an API error: Autocompact is thrashing: the context refilled to the limit within 3 turns of the previous compact, 3 times in a row. A file being read or a tool output is likely too large for the context window. Try reading in smaller chunks, or use /clear to start fresh. (error type invalid_request)` |
| B6#25 | `trello_get_card` | `{"error": "attachments must be true, false, or \"cover\"", "code": "invalid_value"}` |
| B6#27 | `trello_get_card` | `{"error": "attachments must be true, false, or \"cover\"", "code": "invalid_value"}` |

Inputs for the Trello errors: `{"cardId": "68dc52e015f87c50c441d1a9", "actions": "all", "checklists": "all", "attachments": "true"}`.

The B3 error is a transport fault, not a validation error, and is transient. The B4 errors are harness-level subagent failures, not `hg` tool errors.

### Spills (6), not flagged as errors

| Call | Tool | Size | Recovery |
|---|---|---|---|
| B1#27 | `linear_list_issues` | 64,342 | Bash python at #28 |
| B3#8 | `gcal_list_events` | 196,590 | `jq` failed at #9, python at #10 |
| B5#20 | `linear_list_issues` | 122,653 | `jq` failed at #21, python at #22 |
| B6#8 | `gcal_list_events` | 196,590 | `jq` failed at #9, then python |
| B6#28 | `linear_list_issues` | 73,518 | Bash python at #29 |
| PC#8 | `gcal_list_events` | 196,590 | `jq` failed at #9, python at #16 |

Message text (B3#8, first 330 chars):
```text
Error: result (196,590 characters) exceeds maximum allowed tokens. Output has been saved to /home/agent/.claude/projects/-app/51a9849a-3f9e-47c2-af9d-0cd15dd98694/tool-results/mcp-hg-gcal_list_events-1793918237209.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the fil
```

### Bash failures (6)

B3#9, B5#21, B6#9 and PC#9 all returned this (`jq` is not installed):
```text
/bin/bash: line 1: jq: command not found
/bin/bash: line 1: jq: command not found
Shell cwd was reset to /app
```

B4#140 and B6#29 ended with `BrokenPipeError: [Errno 32] Broken pipe` after their output was cut by a pipe. Both were harmless, and the data before the error was usable.

### Silent failure

Formulas read back `#NAME?` in B4#119, B5#104 and PC#105, with no error raised (Item 8).

### Empty results, not errors

| Call | Input | Why |
|---|---|---|
| B3#0 | `slack_search_channels {"query": "zombie_marketing"}` | Private channel, no `channel_types` |
| B1#92, B2#92, B4#100, B6#100 | `gdrive_search {"query": "iPad"}` | Name match only, and no file has iPad in its name. This is the signal that the iPad set is missing |
| B6#93 | `linear_list_issues {"query": "halloween", ...}` | No Linear issue matches, before the new tickets exist |
| B1, B5, B2 | `linear_list_comments` on ART-792, ART-790, ART-836 to ART-839 | Those tickets have no comments |

