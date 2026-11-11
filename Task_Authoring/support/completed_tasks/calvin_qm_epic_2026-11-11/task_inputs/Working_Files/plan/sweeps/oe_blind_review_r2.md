# Oracle Events blind review, round 2

Scope: 04_Prompt.txt, 08_Oracle_Events.md (104 events), 01_Universe_Inject.sql (read, never executed), the OE eval rules, catalog.json, and base data through `hg.py search` only. Clock: 2025-10-01 00:00 PT (07:00 UTC), Oct 1, 2025 (synth-cut).

## Verdict

- CRITICAL: none found.
- MAJOR: 2 (OE 4 search term; OE 12 count boundary).
- MINOR: 6.
- Everything else in OE 1 to OE 104 checked out against the records.

## MAJOR

### M1. OE 4: the search term does not occur in the record
- Span: `search "pass sheet legend", from the note in OE 3`
- Problem: the doc is named "How to read my pass sheets" and its body never contains the word "legend" (SQL gdocs row `f_d3a1aa5976285aac98ffda`). Only the sheet's own footnote contains "pass sheet legend". A name or full-text search for that phrase returns the sheet at most, not the doc. catalog.json gives no matching semantics for `gdrive_search`, so this cannot be shown to work.
- Fix: `OE 4  Find and read the legend of Vincent's pass sheets in Drive (the note in OE 3 names it; search "pass sheets", or list the folder that holds the flow pass sheet)`. Both files share parent `d_65c76e0b87aa7e9b84d1df`.

### M2. OE 12: "Eight merged pull requests" depends on the time zone
- Span: `List the match3d pull requests merged since Vincent started his pass on Sep 26 2025` / `Eight merged pull requests are not on the sheet`
- Problem: PR #463 "FPS and Force Kill Tracking" (github data.json `/pull_requests/2367`) has `merged_at` 2025-09-26T00:08:03Z, base main. That is Sep 25 5:08 PM PT, but Sep 26 in UTC, and the OE gives this list's merge times in UTC only. A list filtered on the record's own date returns nine PRs off the sheet, not eight. #463 changes no decision (performance tracking, one bot comment, one approval).
- Fix: state the boundary. For example: `...merged since Vincent started his sheet (created Sep 26 2025 3:12 AM PT, 10:12 UTC)...` and add to Expected: `#463 merged Sep 25 5:08 PM PT (Sep 26 00:08 UTC), before the pass started, and is not counted.` Alternatively count nine and list #463.
- Confirmed otherwise: #466, #467, #468, #469, #470, #471, #473, #474 are the only other merges into main up to the clock; #476 and #477 are open; #465, #472, #475 are the only PRs on the sheet.

## MINOR

### m1. OE 12: wrong or ambiguous merge time for #473 in the list
- Span: `#473 and #474 (Sep 30 15:48 UTC)`
- Problem: #473 merged 15:41:20 UTC (`/pull_requests/2378`); only #474 merged 15:48:10 UTC (`/pull_requests/2379`). The same Expected line later gives 15:41 UTC for #473, so the line contradicts itself.
- Fix: `#473 (Sep 30 15:41 UTC), #474 (Sep 30 15:48 UTC)`.

### m2. OE 8: each build has two posts in #builds
- Span: `Fifteen posts, oldest first`
- Problem: every named build has a "Started by ..." post (no branch) and a result post "... - <branch> Success after ..." (messages/C05433XK267/2025-09.json). The fifteen titles and times are the result posts; all fifteen times and branches are correct.
- Fix: `Fifteen result posts (the "Success" post of each build, which carries the branch), oldest first`.

### m3. OE 16: the two other DMs are not named
- Span: `his two other DMs with messages since Sep 26 carry no other bug seen in a build`
- Problem: true, but not checkable as written. The two are Calvin's DM with Owen Baker (D05S1S2H55M, 16 messages Sep 26 to 29, Spanish) and with EMPLOYEE_0032 (D07GJJBK789, 7 messages Sep 29). Owen's "Se ve un poco mas lento todo" (Sep 29 22:14 UTC) is a remark on Calvin's video, not a bug seen in a build; worth calling out as the near miss.
- Fix: name both DMs and add `Owen's Sep 29 remark that everything looks a little slower is about Calvin's video, not a build.`

### m4. OE 7: Expected leaves out the comment that decides row 19
- Span: `Later notes: on ZOM-585 ... On ZOM-582 ...`
- Problem: Owen Baker's comment on ZOM-577 (Sep 30 18:26 UTC), "I have a fix locally, need to test it before I open the PR", is why row 19 is Waiting on a fix and not Waiting on QA. It is read by the step but not listed.
- Fix: append `On ZOM-577, Owen Baker, Tue Sep 30 2025 11:26 AM PT (Sep 30 18:26 UTC): "I have a fix locally, need to test it before I open the PR" The fix is not in main.`

### m5. OE 10 and OE 11: tool reach for inline review comments not shown
- Span: `Read the review comments on pull request #472 in GitHub`
- Problem: Arthur's two comments are inline review comments (`github_review_comments`). catalog.json lists `github_get_pull_request_comments` and `github_get_pull_request_reviews` with no descriptions, so it is unverified that either returns inline comments. The same text is in Calvin's inbox (two GitHub mails, Sep 30 15:53:59Z and 16:10:09Z) and in the #zombie-prs thread replies.
- Fix: add the fallback, e.g. `(also in the #zombie-prs thread under the #472 post and in Calvin's GitHub mail)`.

### m6. OE 17: the search also returns the superseded invitation
- Span: `Find the review invite in Gmail (search "flow review"...)`
- Problem: Calvin's inbox also holds the Sep 29 invitation "Invitation: ZM home screen flow review @ Fri Oct 3, 2025", whose body says "Collect & Win and Daily Gift this time". Not wrong, but the trap is not called out.
- Fix: add `The Sep 29 invitation for Fri Oct 3 (agenda "Collect & Win and Daily Gift") is the earlier version.`

## Verified without findings

- Cross-references: every "OE n" in OE 2 to OE 104 points to an earlier event that contains what is attributed to it. No forward references.
- OE 1: ts 1759264805.214409, Tue Sep 30 1:40 PM PT, all five quotes.
- OE 2: ZOM-543 title, team, state, no parent; Brian's comment 20:25:37Z; all quotes. No base comments on ZOM-543.
- OE 3: all 38 rows match the sheet cell for cell; columns, owner, tab, footnote. 18 blank Ticket cells, 20 ticket keys.
- OE 5, OE 6: quotes and times (Calvin 16:29:04Z, Vincent 17:15:44Z and 17:15:51Z, Thu Sep 25).
- OE 7: all 20 states; four quoted notes, authors and times.
- OE 8: fifteen builds, times, branches; twelve main, three feature (#1698, #1718, #1746); #135 after #1745, #1750, #1757.
- OE 9 to OE 11: titles, base, merge times, #472 description, Arthur's login, name and both comments.
- OE 12: #473 title, merge time, Oliver's login, name, comment and time; rows 13, 38, 14, 37. No other merged PR carries a human statement about the flow list (#470's four fixes are different bugs).
- OE 13: ZOM-556 and ZOM-560 titles, states, Vincent's comments and times. All 553 ZOM tickets checked by each row's key words: no ticket holds the other sixteen rows. Base Linear has no comments.
- OE 14: both replies, thread dates, authors, times, channel #zombie-bugs.
- OE 15: Robert's message, channel #zombie-match3d, time; #2006 posted before #1745. Every message since Sep 26 in Calvin's team channels and all injected Slack rows read: no later sighting for the other nine rows.
- OE 16: Marcus's two messages and times; no ZOM ticket for "icon glow"; four DMs besides Marcus's have messages since Sep 26 (Brian, Vincent, Owen Baker, EMPLOYEE_0032), none with another bug seen in a build.
- OE 17 to OE 20: mail sender, time, subject, note; event start and five attendees; card name, description, Leonard's two edits at 17:22Z, earlier description; folder and deck owner. No base name collisions in Drive, Gmail, Calendar or Trello.
- OE 21: all 39 decisions recomputed from the rules: 10 Passed, 9 Waiting on QA, 20 Waiting on a fix; per-area counts; 0 Clear; review rows 6, 8, 15, 17, 18, 19, 36.
- OE 22 to OE 104: 10 children, 17 new sub-issues, 22 moves, 22 notes, each with the right parent, title, state change and reason; sheet, two tabs, move, five shares, slide, DM. No missing, duplicated or doubled-up write.
- No statement of what the agent does not do, no final-answer wording, no redundant event.
