# Mutation matrix — sql_lint + base_check

Clean fixture: after: 0 fail-level findings, 2 warnings


Y = the targeted rule fired at FAIL level · Y* = caught at FAIL level only by another rule · warn = warning only · N = missed

| # | Defect class | Mutation | after | First new finding (latest version) |
|---|---|---|---|---|
| 1 | broken reference | Linear comment on a nonexistent issue | Y | B:issue ENG-999999 does not exist |
| 2 | broken reference | Slack <@mention> of a nonexistent user | Y | B:text mentions <@UNOBODY000>, which is not a Slack user |
| 3 | broken reference | Text cites a nonexistent Linear ticket | Y | B:text references Linear ENG-2989, which exists neither in the base nor in the SQL (Cross-service Referential: dangling reference) |
| 4 | broken reference | Slack text links a PR missing from GitHub | Y | B:text links PR harmonygames-Games/Combo-Fighters#99999, which does not exist in GitHub (base or SQL) — Cross-service Referential |
| 5 | broken reference | Gmail in_reply_to resolves to nothing | Y | B:in_reply_to <nope@harmonygames.co> does not resolve to a message in mailbox oliver.brooks@harmonygames.co (base thread or SQL) |
| 6 | broken reference | Confluence link to a missing page title | Y | B:page link ri:content-title="Arch Overview v9" does not resolve to any page title |
| 7 | broken reference | Trello checklist on a missing card | Y | B:checklist 69651abca1b2c3d4e5f6a7b9 points to card 0000000000000000000000ff, which does not exist |
| 8 | ID-contract break | Slack id is not sha256(channel|ts) | Y | B:id 0123456789abcdef0123456789abcdef breaks the Slack id contract sha256('C09R0KXFX71/1768231200.000100')[:32] |
| 9 | ID-contract break | Gmail message id not <mailbox>/<Message-ID> | Y | L:gmail message id 'oliver.brooks@harmonygames.co/handoff-2' breaks the <mailbox>/<RFC Message-ID> scheme (104,476/104,480 base ids) |
| 10 | ID-contract break | Drive id not f_ + 22 hex | Y | L:gdrive.drive_files.id 'f_0a1b2c3d4e5f60718293a49' breaks the service ID format (53,866/53,866 base files are f_/d_ + 22 hex) |
| 11 | ID-contract break | GitHub comment id outside <pr>#c_<n> | Y | L:github.github_pr_comments.id 'harmonygames-Games/Combo-Fighters#1#c_extra' breaks the GitHub id scheme <pr_id>#c_<n> (100% of base rows) |
| 12 | ID-contract break | GCal ical_uid not 32hex@hg4 | Y | L:gcal ical_uid 'f1e2d3c4b5a69788796a5b4c3d2e1f0@hg4' breaks the 32-hex@hg4 scheme (11,233/11,233 base events) |
| 13 | ID-contract break | Trello id not minted from its time | Y | L:trello.trello_actions.id 9a1b2c3d4e5f6a7b8c9d0e1f encodes creation 2051-12-06 — Trello ids start with the record's Unix seconds (100% of base cards/ |
| 14 | ID-contract break | Linear id differs from identifier | Y | L:linear id iss_handoff differs from identifier ENG-2990 (base: id = identifier) |
| 15 | chronology inversion | Slack reply before its parent | Y | B:reply ts 1768226400.000100 is not after its parent 1768230000.000100 |
| 16 | chronology inversion | Gmail reply dated before the message it answers | Y | B:reply oliver.brooks@harmonygames.co/<handoff-2@harmonygames.co> is dated before the message it answers |
| 17 | chronology inversion | GCal event ends before it starts | Y | B:event evt_0a1b2c3d4e5f60718293a4 ends before it starts |
| 18 | chronology inversion | Linear comment before its issue exists | Y | B:comment cmt_0a1b2c3d4e5f60718293 predates its issue ENG-2990 |
| 19 | chronology inversion | Slack message before the channel existed | Y | B:message ts 1736694000.000100 (2025-01-12) predates channel C09R0KXFX71's creation (2025-11-07) — Temporal |
| 20 | status/activity mismatch | Linear Done without completed_at | Y | L:ENG-2990: State/Lifecycle — state Done without completed_at (base: every Done issue has completed_at) |
| 21 | status/activity mismatch | Linear comment newer than issue updated_at | Y | B:comment cmt_0a1b2c3d4e5f60718293 (2026-01-13) is newer than issue ENG-2990 updated_at 2026-01-12T19:00:00Z — UPDATE the issue's updated_at (a commen |
| 22 | status/activity mismatch | PR comment newer than PR updated_at | Y | B:harmonygames-Games/Combo-Fighters#1#c_900 (2026-02-01) is newer than PR harmonygames-Games/Combo-Fighters#1 updated_at 2026-01-21T13:30:50Z — UPDATE |
| 23 | status/activity mismatch | Trello badges disagree with checklist/comments | Y | B:card 69651a80a1b2c3d4e5f6a7b8 badges {'comments': 1, 'checkItems': 0, 'checkItemsChecked': 0} disagree with its SQL comments/check items {'comments' |
| 24 | status/activity mismatch | Slack parent reply_count disagrees with replies | Y | B:thread counters reply_count/latest_reply/reply_users_count = ('3', '1768231200.000100', '1') but its SQL replies give (1, '1768231200.000100', 1) (b |
| 25 | status/activity mismatch | Confluence version gap / page.version stale | Y | B:page page_eng_home versions [4] do not continue the base history 1..2 contiguously |
| 26 | status/activity mismatch | PR comment without its 'commented' timeline event | Y | B:harmonygames-Games/Combo-Fighters#1#c_900 has no matching 'commented' timeline event (same pr_id and created_at) — base pairs 884/884 |
| 27 | malformed JSON in a JSON column | attendees_json not valid JSON | Y | L:gcal.gcal_events.attendees_json: malformed JSON in a JSON column (Expecting property name enclosed in double quotes at char 108) |
| 28 | malformed JSON in a JSON column | badges_json not valid JSON | Y | L:trello.trello_cards.badges_json: malformed JSON in a JSON column (Expecting ',' delimiter at char 321) |
| 29 | non-member poster | Slack poster not in channel members | Y | B:user EMPLOYEE_0004_SLACK_ID posts in C09R0KXFX71 but is not a channel member |
| 30 | mailbox mismatch | Copy in a mailbox that is neither sender nor recipient | Y | L:gmail copy in oliver.brooks@harmonygames.co's mailbox: oliver.brooks@harmonygames.co is neither the sender (brian.foster@harmonygames.co) nor in To/ |
| 31 | mailbox mismatch | Own sent copy not labelled SENT | Y | L:gmail copy in oliver.brooks@harmonygames.co's own mailbox is from oliver.brooks@harmonygames.co but not labelled SENT (base: 100% of own copies are  |
| 32 | attendee-copy gap | Organizer's calendar has no copy | Y | B:event 0f1e2d3c4b5a69788796a5b4c3d2e1f0@hg4: brian.foster@harmonygames.co is an attendee/organizer with a calendar but has no copy of the event (base |
| 33 | attendee-copy gap | Drive share to an unknown person | Y | B:owner/share entry nobody.here@harmonygames.co is not a known HarmonyGames identity (Drive users, mailboxes, Slack/Linear users, contacts) |
| 34 | attendee-copy gap | Sheets row sharing differs from its Drive row | Y | B:f_0a1b2c3d4e5f60718293a4: owner/sharing differ from its drive_files row (base: Docs/Sheets/Slides mirror Drive sharing, 633/633 docs) |
| 35 | duplicate keys | Same Slack row inserted twice | Y | B:slack.slack_messages id 5a5d2bddf92fd7fe0d04f78c518283c4 inserted twice |
| 36 | duplicate keys | New Linear issue collides with the base | Y | B:issue ENG-2022 collides with the base |
| 37 | duplicate keys | Trello idShort already used on the board | Y | B:card idShort 80 is already used on board 65eb4ec525346c8070ca638f |
| 38 | generated-column write | INSERT writes slack text_fts | Y | L:slack.slack_messages: INSERT writes generated column(s) ['text_fts'] — the database computes them; drop them from the column list |
| 39 | missing NOT NULL | INSERT omits Linear is_archived | Y | L:linear.linear_issues: INSERT omits NOT NULL column(s) ['is_archived'] |

after: targeted rule fired 39/39; caught only by a side-effect rule 0; any FAIL-level catch 39/39, 0 warning-only, 0 missed
