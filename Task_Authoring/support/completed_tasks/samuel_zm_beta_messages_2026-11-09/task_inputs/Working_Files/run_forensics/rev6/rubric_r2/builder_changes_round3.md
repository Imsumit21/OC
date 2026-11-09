# Builder changes for /rubric round 3

From the reviewed JSON (sha d1cbadf710e9, 149 rows) to 09_Rubrics.json (sha 5bf50637b0a1, 152 rows). Section 1 uses the old row numbers; sections 2 and 3 use the new ones.

## 1 · Remove these 8 old rows

- R21: The Agent records in the What's missing column of the DES-344 (Lapsed 14 days) row of its calls sheet that another message already covers it (naming Lapsed 7 days, DES-317, the weekly batch, the PN sheet's "Has not played in seven days.", or its line "They’ve Taken Over… Can You Stop Them?" or "Your Squad Is Waiting")
- R104: The Agent moves exactly 24 existing tickets to Backlog
- R105: The Agent moves exactly 6 existing tickets to Canceled
- R117: The Agent files its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) in Backlog with no assignee
- R118: The Agent files its new ticket for the ask on ZOM-556 (Daily gift about to reset) in Backlog with no assignee
- R119: The Agent files its new ticket for the ask on ZOM-563 (Teammate sent lives) in Backlog with no assignee
- R120: The Agent files its new ticket for the ask on ZOM-483 (Infinite lives ending) in Backlog with no assignee
- R122: The Agent adds Lapsed 7 days (named by DES-317, Lapsed 7 days, the PN sheet's "Has not played in seven days.", Your Squad Is Waiting or They’ve Taken Over… Can You Stop Them?) as an item on a checklist on the Push Notifications card on ZM ROADMAP (6851a769c65dc0017a227bb7)

## 2 · Add these 11 rows, at these positions

### C21
- Title: The Agent names Lapsed 7 days as the covering message in the What's missing column of the DES-344 (Lapsed 14 days) row of its calls sheet (the bare name passes, with or without "covered by", and so does DES-317, the PN sheet's "Has not played in seven days.", the client's "Weekly reminder batch" (WeeklyReminderTitle), Leonard's "the weekly one", its line "They’ve Taken Over… Can You Stop Them?" or "Your Squad Is Waiting", or any other wording that identifies Lapsed 7 days; a cell naming only the Weekly Leaderboard batch, DES-320 or "Weekly Rankings Reset!" fails)
- Category: Outcome · Weight: 5
- Justification: Multi-source: the weekly batch's four runs in the code, read with Leonard's cancellation note, show day 14 is covered, and the rule says to name the message.
- Evidence: Sources: Gmail samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> ('The weekly one repeats for four weeks, so day 14 is already covered.'), match3d Assets/Scripts/Notifications/NotificationManager.cs ('// Schedule Weekly reminder batch'; 'BatchScheduleWeeklyNotifications(WeeklyReminderTitle, WeeklyReminderMessage, 4, serverToday);'; title 'They’ve Taken Over… Can You Stop Them?'), PN sheet f_a325dd4af80afc5994d5dc row 'Has not played in seven days.'; the Weekly Leaderboard batch is a separate call for DES-320 ('BatchScheduleWeeklyLeaderboardNotifications(WeeklyLeaderboardTitle, WeeklyLeaderboardMessage, 4, serverToday);'); rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop: it fails test 1, or the client already covers it under another message, then name that message.'). Accept: the Agent names Lapsed 7 days as the covering message in the What's missing column of the DES-344 (Lapsed 14 days) row of its calls sheet (the bare name passes, with or without "covered by", and so does DES-317, the PN sheet's "Has not played in seven days.", the client's "Weekly reminder batch" (WeeklyReminderTitle), Leonard's "the weekly one", its line "They’ve Taken Over… Can You Stop Them?" or "Your Squad Is Waiting", or any other wording that identifies Lapsed 7 days; a cell naming only the Weekly Leaderboard batch, DES-320 or "Weekly Rankings Reset!" fails).

### C99
- Title: The Agent moves DES-319 (Plague Race) from Done to Backlog
- Category: Outcome · Weight: 5
- Justification: Multi-source: the move rests on the test 6 failure and on the roadmap card that overrides Todo.
- Evidence: Sources: Slack D06UFE81RF0/1759174846.723833 ('that iPhone was still on the 5-minute timers build when I ticked it, so scratch iOS.'), Trello card 68d1eb90bef538c7c5c5599d 'Fix TECH ISSUES' ('Held tickets sit in Backlog, unassigned.'; action 68dae8c7d95e24b55b69bf80); rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise.'); DES-319 state Done. Accept: the Agent moves DES-319 (Plague Race) from Done to Backlog.

### C116
- Title: The Agent files its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) in Backlog
- Category: Outcome · Weight: 3
- Justification: Comparison: the ask is a Hold, and the later roadmap card puts held tickets in Backlog over the rule doc's Todo.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-542 comment cmt_f1b8a109dfa70cdc4565. Accept: the Agent files its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) in Backlog.

### C117
- Title: The Agent files its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) unassigned
- Category: Outcome · Weight: 3
- Justification: Comparison: the ask is a Hold, and the roadmap card says held tickets sit unassigned.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-542 comment cmt_f1b8a109dfa70cdc4565. Accept: the Agent files its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) unassigned.

### C118
- Title: The Agent files its new ticket for the ask on ZOM-556 (Daily gift about to reset) in Backlog
- Category: Outcome · Weight: 3
- Justification: Comparison: the ask is a Hold, and the later roadmap card puts held tickets in Backlog over the rule doc's Todo.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-556 comment cmt_2b519285937e7fa79453. Accept: the Agent files its new ticket for the ask on ZOM-556 (Daily gift about to reset) in Backlog.

### C119
- Title: The Agent files its new ticket for the ask on ZOM-556 (Daily gift about to reset) unassigned
- Category: Outcome · Weight: 3
- Justification: Comparison: the ask is a Hold, and the roadmap card says held tickets sit unassigned.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-556 comment cmt_2b519285937e7fa79453. Accept: the Agent files its new ticket for the ask on ZOM-556 (Daily gift about to reset) unassigned.

### C120
- Title: The Agent files its new ticket for the ask on ZOM-563 (Teammate sent lives) in Backlog
- Category: Outcome · Weight: 3
- Justification: Comparison: the ask is a Hold, and the later roadmap card puts held tickets in Backlog over the rule doc's Todo.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-563 comment cmt_eabac5435f2b3a575aad. Accept: the Agent files its new ticket for the ask on ZOM-563 (Teammate sent lives) in Backlog.

### C121
- Title: The Agent files its new ticket for the ask on ZOM-563 (Teammate sent lives) unassigned
- Category: Outcome · Weight: 3
- Justification: Comparison: the ask is a Hold, and the roadmap card says held tickets sit unassigned.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-563 comment cmt_eabac5435f2b3a575aad. Accept: the Agent files its new ticket for the ask on ZOM-563 (Teammate sent lives) unassigned.

### C122
- Title: The Agent files its new ticket for the ask on ZOM-483 (Infinite lives ending) in Backlog
- Category: Outcome · Weight: 3
- Justification: Comparison: the ask is a Hold, and the later roadmap card puts held tickets in Backlog over the rule doc's Todo.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-483 comment cmt_e2e2926a2080ca53c4ea. Accept: the Agent files its new ticket for the ask on ZOM-483 (Infinite lives ending) in Backlog.

### C123
- Title: The Agent files its new ticket for the ask on ZOM-483 (Infinite lives ending) unassigned
- Category: Outcome · Weight: 3
- Justification: Comparison: the ask is a Hold, and the roadmap card says held tickets sit unassigned.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-483 comment cmt_e2e2926a2080ca53c4ea. Accept: the Agent files its new ticket for the ask on ZOM-483 (Infinite lives ending) unassigned.

### C125
- Title: The Agent adds Lapsed 7 days (named by DES-317, Lapsed 7 days, the client's "Weekly reminder batch" (WeeklyReminderTitle), the PN sheet's "Has not played in seven days.", Your Squad Is Waiting or They’ve Taken Over… Can You Stop Them?) as an item on a checklist on the Push Notifications card on ZM ROADMAP (6851a769c65dc0017a227bb7)
- Category: Outcome · Weight: 5
- Justification: Multi-source: the item is a Go, which only the six tests produce, and the card is named by the prompt.
- Evidence: Sources: match3d Assets/Scripts/Notifications/NotificationManager.cs call site ('// Schedule Weekly reminder batch'; 'BatchScheduleWeeklyNotifications(WeeklyReminderTitle, WeeklyReminderMessage, 4, serverToday);', line 173), Trello card 6851a769c65dc0017a227bb7 (Leonard's comment 68d415a716abcb84070a8e2a), NotificationManager.cs ('DailyNotifications(OneDayLapsedTitle, OneDayLapsedMessage, serverToday);'; 'BatchScheduleWeeklyNotifications(WeeklyReminderTitle, WeeklyReminderMessage, 4, serverToday);'), Gmail QA note ('Seen only counts on a store build, on a real iOS device and a real Android device.'), Phone message checks sheet f_8eb8c04713ff6a6ef4a265 (Sep 24 pass), Slack C0880U9751A/1759245146.720608 ('the lapsed ones are still coming through'); Leonard's DM ('Every Go goes on a checklist on our push notifications card so Vincent can tick it off.'). Accept: the Agent adds Lapsed 7 days (named by DES-317, Lapsed 7 days, the client's "Weekly reminder batch" (WeeklyReminderTitle), the PN sheet's "Has not played in seven days.", Your Squad Is Waiting or They’ve Taken Over… Can You Stop Them?) as an item on a checklist on the Push Notifications card on ZM ROADMAP (6851a769c65dc0017a227bb7).

## 3 · Change these 2 rows (same title, other fields)

### C4: The Agent enters Lapsed 1 day (or the PN sheet's "Has not played in 24 hours", any wording naming that message) in the Message column of the DES-316 row of its calls sheet
- Evidence: Sources: PN sheet f_a325dd4af80afc5994d5dc row 5 in the sheet, export grid index 4, 'Has not played in 24 hours', Linear DES-316 'PN: Lapsed 1 day'; Leonard's DM ('Put it in one sheet in your Drive folder, one row per message: Message, Ticket, Call, What's missing, Audience, Final headline, String change.'). Accept: the Agent enters Lapsed 1 day (or the PN sheet's "Has not played in 24 hours", any wording naming that message) in the Message column of the DES-316 row of its calls sheet.

### C24: The Agent records in the What's missing column of its row for the ask on ZOM-563 (Teammate sent lives) in its calls sheet that it needs a server send (naming test 2, or saying it needs a server)
- Weight: 3
- Justification: Interpretation: test 2 read against the asker's own note on ZOM-563 that it would have to go out from the server.

