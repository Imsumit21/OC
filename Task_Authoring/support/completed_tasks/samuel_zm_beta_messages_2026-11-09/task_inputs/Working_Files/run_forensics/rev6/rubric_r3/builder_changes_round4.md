# Builder changes for /rubric round 4

Base: the reviewed file, sha 5bf50637b0a1 (152 rows). Result: `09_Rubrics.json`, 153 rows, weight 583.

140 rows are byte-identical to the reviewed file. Remove 12 rows and add 13. Row numbers below are the new positions.

## Remove

- old R21: The Agent names Lapsed 7 days as the covering message in the What's missing column of the DES-344 (Lapsed 14 days) row of its calls sheet (the bare name passes, with or without "covered by", and so does DES-317, the PN sheet's "Has not played in seven days.", the client's "Weekly reminder batch" (WeeklyReminderTitle), Leonard's "the weekly one", its line "They’ve Taken Over… Can You Stop Them?" or "Your Squad Is Waiting", or any other wording that identifies Lapsed 7 days; a cell naming only the Weekly Leaderboard batch, DES-320 or "Weekly Rankings Reset!" fails)
- old R105: The Agent changes the state of exactly 30 existing tickets
- old R106: The Agent clears the assignee on exactly 24 existing tickets
- old R116: The Agent files its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) in Backlog
- old R117: The Agent files its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) unassigned
- old R118: The Agent files its new ticket for the ask on ZOM-556 (Daily gift about to reset) in Backlog
- old R119: The Agent files its new ticket for the ask on ZOM-556 (Daily gift about to reset) unassigned
- old R120: The Agent files its new ticket for the ask on ZOM-563 (Teammate sent lives) in Backlog
- old R121: The Agent files its new ticket for the ask on ZOM-563 (Teammate sent lives) unassigned
- old R122: The Agent files its new ticket for the ask on ZOM-483 (Infinite lives ending) in Backlog
- old R123: The Agent files its new ticket for the ask on ZOM-483 (Infinite lives ending) unassigned
- old R125: The Agent adds Lapsed 7 days (named by DES-317, Lapsed 7 days, the client's "Weekly reminder batch" (WeeklyReminderTitle), the PN sheet's "Has not played in seven days.", Your Squad Is Waiting or They’ve Taken Over… Can You Stop Them?) as an item on a checklist on the Push Notifications card on ZM ROADMAP (6851a769c65dc0017a227bb7)

## Add

### R21 · Outcome · weight 5

**Title:** The Agent names Lapsed 7 days as the covering message in the What's missing or Call cell of the DES-344 (Lapsed 14 days) row of its calls sheet (a bare name passes: Lapsed 7 days, DES-317, the PN sheet's "7 Days Lapsed", "Has not played in seven days." or "7d lapse since last session", the client's "Weekly reminder batch" (WeeklyReminderTitle, WeeklyReminderMessage, BatchScheduleWeeklyNotifications, Notification_WeeklyReminder), Leonard's "the weekly one", "the 7 day one" or "the 'taken over' push", "They’ve Taken Over… Can You Stop Them?", "It’s been a while, survivor.", "Your Squad Is Waiting" or "Your Squad Needs You Back"; a cell naming the Weekly Leaderboard batch, DES-320 or "Weekly Rankings Reset!" as covering it fails, even alongside Lapsed 7 days)

**Justification:** Multi-source: the weekly batch's four runs in the code, read with Leonard's cancellation note, show day 14 is covered, and the rule says to name the message.

**Evidence:** Sources: Gmail samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> ('The weekly one repeats for four weeks, so day 14 is already covered.'), match3d Assets/Scripts/Notifications/NotificationManager.cs ('// Schedule Weekly reminder batch'; 'BatchScheduleWeeklyNotifications(WeeklyReminderTitle, WeeklyReminderMessage, 4, serverToday);'; title 'They’ve Taken Over… Can You Stop Them?'; message 'It’s been a while, survivor.'), PN sheet f_a325dd4af80afc5994d5dc row 6 in the sheet, export grid index 5 (When '7 Days Lapsed', Details 'Has not played in seven days.', Segmentation '7d lapse since last session'), GitHub harmonygames-Games/match3d#248#rc_8 ('LocalizationManager.GetTranslation("Notification_WeeklyReminder")'), Calendar evt_f2c03e69f50acf62c9d1c3 ('Final for the 7 day one is "Your Squad Is Waiting", body stays. That replaces what I said in the art thread.'), Slack C08R8CHB0QL/1759169129.445834 ('the 'taken over' push'; 'make it "Your Squad Needs You Back", body stays'); the Weekly Leaderboard batch is a separate call for DES-320 ('BatchScheduleWeeklyLeaderboardNotifications(WeeklyLeaderboardTitle, WeeklyLeaderboardMessage, 4, serverToday);'); rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop: it fails test 1, or the client already covers it under another message, then name that message.'). Accept: the Agent names Lapsed 7 days as the covering message in the What's missing or Call cell of the DES-344 (Lapsed 14 days) row of its calls sheet (a bare name passes: Lapsed 7 days, DES-317, the PN sheet's "7 Days Lapsed", "Has not played in seven days." or "7d lapse since last session", the client's "Weekly reminder batch" (WeeklyReminderTitle, WeeklyReminderMessage, BatchScheduleWeeklyNotifications, Notification_WeeklyReminder), Leonard's "the weekly one", "the 7 day one" or "the 'taken over' push", "They’ve Taken Over… Can You Stop Them?", "It’s been a while, survivor.", "Your Squad Is Waiting" or "Your Squad Needs You Back"; a cell naming the Weekly Leaderboard batch, DES-320 or "Weekly Rankings Reset!" as covering it fails, even alongside Lapsed 7 days).

### R105 · Outcome · weight 5

**Title:** The Agent moves exactly 24 pre-existing tickets to Backlog (its new tickets not counted)

**Justification:** Multi-source: the count comes out of all the calls, and the card overrides Todo.

**Evidence:** Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise.'). Accept: the Agent moves exactly 24 pre-existing tickets to Backlog (its new tickets not counted).

### R106 · Outcome · weight 5

**Title:** The Agent moves exactly 6 pre-existing tickets to Canceled

**Justification:** Multi-source: the count comes out of test 1 and the covered Lapsed 14 days.

**Evidence:** Source: rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise.'). Accept: the Agent moves exactly 6 pre-existing tickets to Canceled.

### R107 · Outcome · weight 5

**Title:** The Agent clears the assignee on exactly 24 pre-existing tickets (its new tickets not counted)

**Justification:** Multi-source: the count comes out of all the calls, read with the roadmap card's 'unassigned'.

**Evidence:** Source: Trello card 68d1eb90bef538c7c5c5599d 'Fix TECH ISSUES' ('Held tickets sit in Backlog, unassigned.'; action 68dae8c7d95e24b55b69bf80). Accept: the Agent clears the assignee on exactly 24 pre-existing tickets (its new tickets not counted).

### R117 · Outcome · weight 5

**Title:** The Agent has its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) in Backlog when it finishes, whether filed there or moved there

**Justification:** Tracing: the ask sits in a comment on ZOM-542, off DES-314's children; it is a Hold, and the later roadmap card puts held tickets in Backlog over the rule doc's Todo.

**Evidence:** Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise.'); Linear ZOM-542 comment cmt_f1b8a109dfa70cdc4565 ('can we get a phone reminder once the daily Boss Arena attempts refill?'). Accept: the Agent has its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) in Backlog when it finishes, whether filed there or moved there.

### R118 · Outcome · weight 5

**Title:** The Agent has its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) unassigned when it finishes, whether filed that way or cleared later

**Justification:** Tracing: the ask sits in a comment on ZOM-542, off DES-314's children; it is a Hold, and the roadmap card says held tickets sit unassigned.

**Evidence:** Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-542 comment cmt_f1b8a109dfa70cdc4565 ('can we get a phone reminder once the daily Boss Arena attempts refill?'). Accept: the Agent has its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) unassigned when it finishes, whether filed that way or cleared later.

### R119 · Outcome · weight 5

**Title:** The Agent has its new ticket for the ask on ZOM-556 (Daily gift about to reset) in Backlog when it finishes, whether filed there or moved there

**Justification:** Tracing: the ask sits in a comment on ZOM-556, off DES-314's children; it is a Hold, and the later roadmap card puts held tickets in Backlog over the rule doc's Todo.

**Evidence:** Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise.'); Linear ZOM-556 comment cmt_2b519285937e7fa79453 ('could we also send a phone reminder the evening before the daily gift streak resets?'). Accept: the Agent has its new ticket for the ask on ZOM-556 (Daily gift about to reset) in Backlog when it finishes, whether filed there or moved there.

### R120 · Outcome · weight 5

**Title:** The Agent has its new ticket for the ask on ZOM-556 (Daily gift about to reset) unassigned when it finishes, whether filed that way or cleared later

**Justification:** Tracing: the ask sits in a comment on ZOM-556, off DES-314's children; it is a Hold, and the roadmap card says held tickets sit unassigned.

**Evidence:** Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-556 comment cmt_2b519285937e7fa79453 ('could we also send a phone reminder the evening before the daily gift streak resets?'). Accept: the Agent has its new ticket for the ask on ZOM-556 (Daily gift about to reset) unassigned when it finishes, whether filed that way or cleared later.

### R121 · Outcome · weight 5

**Title:** The Agent has its new ticket for the ask on ZOM-563 (Teammate sent lives) in Backlog when it finishes, whether filed there or moved there

**Justification:** Tracing: the ask sits in a comment on ZOM-563, off DES-314's children; it is a Hold, and the later roadmap card puts held tickets in Backlog over the rule doc's Todo.

**Evidence:** Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise.'); Linear ZOM-563 comment cmt_eabac5435f2b3a575aad ('could we get a phone message when a teammate sends you lives?'). Accept: the Agent has its new ticket for the ask on ZOM-563 (Teammate sent lives) in Backlog when it finishes, whether filed there or moved there.

### R122 · Outcome · weight 5

**Title:** The Agent has its new ticket for the ask on ZOM-563 (Teammate sent lives) unassigned when it finishes, whether filed that way or cleared later

**Justification:** Tracing: the ask sits in a comment on ZOM-563, off DES-314's children; it is a Hold, and the roadmap card says held tickets sit unassigned.

**Evidence:** Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-563 comment cmt_eabac5435f2b3a575aad ('could we get a phone message when a teammate sends you lives?'). Accept: the Agent has its new ticket for the ask on ZOM-563 (Teammate sent lives) unassigned when it finishes, whether filed that way or cleared later.

### R123 · Outcome · weight 5

**Title:** The Agent has its new ticket for the ask on ZOM-483 (Infinite lives ending) in Backlog when it finishes, whether filed there or moved there

**Justification:** Tracing: the ask sits in a comment on ZOM-483, off DES-314's children; it is a Hold, and the later roadmap card puts held tickets in Backlog over the rule doc's Todo.

**Evidence:** Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise.'); Linear ZOM-483 comment cmt_e2e2926a2080ca53c4ea ('could we also remind players on their phone when their infinite lives are about to run out?'). Accept: the Agent has its new ticket for the ask on ZOM-483 (Infinite lives ending) in Backlog when it finishes, whether filed there or moved there.

### R124 · Outcome · weight 5

**Title:** The Agent has its new ticket for the ask on ZOM-483 (Infinite lives ending) unassigned when it finishes, whether filed that way or cleared later

**Justification:** Tracing: the ask sits in a comment on ZOM-483, off DES-314's children; it is a Hold, and the roadmap card says held tickets sit unassigned.

**Evidence:** Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-483 comment cmt_e2e2926a2080ca53c4ea ('could we also remind players on their phone when their infinite lives are about to run out?'). Accept: the Agent has its new ticket for the ask on ZOM-483 (Infinite lives ending) unassigned when it finishes, whether filed that way or cleared later.

### R126 · Outcome · weight 5

**Title:** The Agent adds Lapsed 7 days (named by Lapsed 7 days, DES-317, the PN sheet's "7 Days Lapsed", "Has not played in seven days." or "7d lapse since last session", the client's "Weekly reminder batch" (WeeklyReminderTitle, WeeklyReminderMessage, BatchScheduleWeeklyNotifications, Notification_WeeklyReminder), Leonard's "the weekly one", "the 7 day one" or "the 'taken over' push", "They’ve Taken Over… Can You Stop Them?", "It’s been a while, survivor.", "Your Squad Is Waiting" or "Your Squad Needs You Back") as an item on a checklist on the Push Notifications card on ZM ROADMAP (6851a769c65dc0017a227bb7)

**Justification:** Multi-source: the item is a Go, which only the six tests produce, and the card is named by the prompt.

**Evidence:** Sources: match3d Assets/Scripts/Notifications/NotificationManager.cs call site ('// Schedule Weekly reminder batch'; 'BatchScheduleWeeklyNotifications(WeeklyReminderTitle, WeeklyReminderMessage, 4, serverToday);', lines 173–174; title 'They’ve Taken Over… Can You Stop Them?'; message 'It’s been a while, survivor.'), Gmail samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> ('The weekly one repeats for four weeks, so day 14 is already covered.'), PN sheet f_a325dd4af80afc5994d5dc row 6 in the sheet, export grid index 5 (When '7 Days Lapsed', Details 'Has not played in seven days.', Segmentation '7d lapse since last session'), GitHub harmonygames-Games/match3d#248#rc_8 ('LocalizationManager.GetTranslation("Notification_WeeklyReminder")'), Calendar evt_f2c03e69f50acf62c9d1c3 ('Final for the 7 day one is "Your Squad Is Waiting", body stays. That replaces what I said in the art thread.'), Slack C08R8CHB0QL/1759169129.445834 ('the 'taken over' push'; 'make it "Your Squad Needs You Back", body stays'), Trello card 6851a769c65dc0017a227bb7 (Leonard's comment 68d415a716abcb84070a8e2a), NotificationManager.cs ('DailyNotifications(OneDayLapsedTitle, OneDayLapsedMessage, serverToday);'; 'BatchScheduleWeeklyNotifications(WeeklyReminderTitle, WeeklyReminderMessage, 4, serverToday);'), Gmail QA note ('Seen only counts on a store build, on a real iOS device and a real Android device.'), Phone message checks sheet f_8eb8c04713ff6a6ef4a265 (Sep 24 pass), Slack C0880U9751A/1759245146.720608 ('the lapsed ones are still coming through'); Leonard's DM ('Every Go goes on a checklist on our push notifications card so Vincent can tick it off.'). Accept: the Agent adds Lapsed 7 days (named by Lapsed 7 days, DES-317, the PN sheet's "7 Days Lapsed", "Has not played in seven days." or "7d lapse since last session", the client's "Weekly reminder batch" (WeeklyReminderTitle, WeeklyReminderMessage, BatchScheduleWeeklyNotifications, Notification_WeeklyReminder), Leonard's "the weekly one", "the 7 day one" or "the 'taken over' push", "They’ve Taken Over… Can You Stop Them?", "It’s been a while, survivor.", "Your Squad Is Waiting" or "Your Squad Needs You Back") as an item on a checklist on the Push Notifications card on ZM ROADMAP (6851a769c65dc0017a227bb7).
