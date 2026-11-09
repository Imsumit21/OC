# Builder changes for /rubric round 2

From the reviewed JSON (sha 3911b7d5f4de, 143 rows) to 09_Rubrics.json (sha d1cbadf710e9, 149 rows). Row numbers in section 1 are the old rows; in sections 2 and 3 they are the new rows.

## 1 · Remove these 24 old rows

- R15: The Agent records in the What's missing column of the DES-315 (Lives recharged) row of its calls sheet that it fails test 6, seen on both iOS and Android (naming test 6, or saying Vincent Parker's tick is off or it failed to arrive on iOS 0.3.49)
- R16: The Agent records in the What's missing column of the DES-319 (Plague Race) row of its calls sheet that it fails test 6, seen on both iOS and Android (naming test 6, or saying the iOS pass was on the 5-minute timers build or it never showed up on the real iOS build)
- R19: The Agent records in the What's missing column of the DES-344 (Lapsed 14 days) row of its calls sheet that another message already covers it (naming Lapsed 7 days, DES-317 or the weekly batch)
- R25: The Agent records in the What's missing column of the DES-322 (Login Calendar update) row of its calls sheet that the client has yet to schedule it (naming test 3, or saying it isn't scheduled in the client yet)
- R38: The Agent fills the Final headline column on exactly two rows of its calls sheet
- R39: The Agent fills the String change column on exactly two rows of its calls sheet
- R41: The Agent enters Hold in the Call column of exactly 28 rows of its calls sheet
- R42: The Agent enters Drop in the Call column of exactly 6 rows of its calls sheet
- R51: The Agent gives the reason Lives recharged (or Full Ammo Reloaded!) is still a Hold in its one-page note: it fails test 6, seen on both iOS and Android (naming test 6, or saying Vincent Parker's tick is off or it failed to arrive on iOS 0.3.49)
- R52: The Agent gives the reason Plague Race (or Plague Race Is On!) is still a Hold in its one-page note: it fails test 6, seen on both iOS and Android (naming test 6, or saying the iOS pass was on the 5-minute timers build or it never showed up on the real iOS build)
- R53: The Agent gives the reason Weekly Leaderboard reset (or Weekly Rankings Reset!) is still a Hold in its one-page note: it fires on the wrong day (naming test 5, or saying it counts from the last session and misses the weekly reset)
- R54: The Agent gives the reason Finish first mission (or Finish Your First Mission!) is still a Hold in its one-page note: it can't reach its players (naming test 4, or saying its players below level 20 haven't had our own ask, which runs after level 20)
- R92: The Agent leaves call comments on exactly 32 existing Design tickets, DES-313 and DES-315 to DES-345 (a comment on a ZOM ticket aside)
- R94: The Agent moves DES-319 (Plague Race) from Done to Backlog
- R99: The Agent moves DES-321 (Quests rollover) from In Review to Backlog
- R100: The Agent moves DES-323 (Season Pass start) from In Review to Backlog
- R104: The Agent moves exactly 24 existing tickets to Backlog (the Hold tickets among DES-313 and DES-315 to DES-345)
- R105: The Agent moves exactly 6 existing tickets to Canceled (the Drop tickets among DES-315 to DES-345)
- R106: The Agent changes the state of exactly 30 of the tickets DES-313 and DES-315 to DES-345
- R107: The Agent clears the assignee on exactly 24 of the tickets DES-313 and DES-315 to DES-345
- R114: The Agent files exactly four new ask tickets in Backlog, unassigned
- R116: The Agent adds Lapsed 7 days (named by DES-317, Lapsed 7 days, the PN sheet's "Has not played in seven days." or Your Squad Is Waiting) as an item on a checklist on the Push Notifications card on ZM ROADMAP (6851a769c65dc0017a227bb7)
- R139: The Agent sends its emails about the asks to exactly eight people, the askers apart from Leonard Hayes
- R143: The Agent posts the counts in Leonard's DM after all of its other writes for the job (the calls sheet, the note, the ticket comments, the ticket moves, the new tickets, the checklist and the emails), with none of them after the post

## 2 · Add these 30 rows (new or retitled), at these positions

### C4
- Title: The Agent enters Lapsed 1 day (or the PN sheet's "Has not played in 24 hours", any wording naming that message) in the Message column of the DES-316 row of its calls sheet
- Category: Outcome · Weight: 1
- Justification: Lookup: the name is read from the sheet row or the ticket.
- Evidence: Sources: PN sheet f_a325dd4af80afc5994d5dc row 4 'Has not played in 24 hours', Linear DES-316 'PN: Lapsed 1 day'; Leonard's DM ('Put it in one sheet in your Drive folder, one row per message: Message, Ticket, Call, What's missing, Audience, Final headline, String change.'). Accept: the Agent enters Lapsed 1 day (or the PN sheet's "Has not played in 24 hours", any wording naming that message) in the Message column of the DES-316 row of its calls sheet.

### C14
- Title: The Agent enters Drop in the Call column of the DES-344 (Lapsed 14 days) row of its calls sheet
- Category: Outcome · Weight: 5
- Justification: Multi-source: the weekly batch's four runs in the code, read with Leonard's cancellation note, show day 14 is covered, and the rule makes that a Drop.
- Evidence: Sources: Gmail samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> ('The weekly one repeats for four weeks, so day 14 is already covered.'), NotificationManager.cs ('BatchScheduleWeeklyNotifications(WeeklyReminderTitle, WeeklyReminderMessage, 4, serverToday);'); rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop: it fails test 1, or the client already covers it under another message, then name that message.'). Accept: the Agent enters Drop in the Call column of the DES-344 (Lapsed 14 days) row of its calls sheet.

### C17
- Title: The Agent records in the What's missing column of the DES-315 (Lives recharged) row of its calls sheet that it fails test 6, as Vincent has yet to see it arrive on both iOS and Android (naming test 6, or saying Vincent Parker's tick is off or it failed to arrive on iOS 0.3.49)
- Category: Outcome · Weight: 5
- Justification: Multi-source: Vincent's Sep 30 post names the headline Full Ammo, so it has to be tied to the row and set against his Sep 24 pass.
- Evidence: Sources: Slack C0880U9751A/1759245146.720608 ('taking my tick off Full Ammo until I've seen it land'), Linear DES-315 Vincent's Sep 24 pass cmt_51e018b23e18c2f680cd, Gmail QA note; rule doc f_dc45e0e5a8b8635c1b82b2 ('6. Vincent has seen it arrive on both iOS and Android.'). Accept: the Agent records in the What's missing column of the DES-315 (Lives recharged) row of its calls sheet that it fails test 6, as Vincent has yet to see it arrive on both iOS and Android (naming test 6, or saying Vincent Parker's tick is off or it failed to arrive on iOS 0.3.49).

### C18
- Title: The Agent records in the What's missing column of the DES-319 (Plague Race) row of its calls sheet that it fails test 6, as Vincent has yet to see it arrive on both iOS and Android (naming test 6, or saying the iOS pass was on the 5-minute timers build or it never showed up on the real iOS build)
- Category: Outcome · Weight: 5
- Justification: Multi-source: Vincent's reply in Samuel's DM withdraws a pass the checks sheet still shows, and the QA note says a shortened-timer build doesn't count.
- Evidence: Sources: Slack D06UFE81RF0/1759174846.723833 ('that iPhone was still on the 5-minute timers build when I ticked it, so scratch iOS.'), Gmail QA note ('A build with shortened timers doesn't count, it only proves the code path.'); rule doc f_dc45e0e5a8b8635c1b82b2 ('6. Vincent has seen it arrive on both iOS and Android.'). Accept: the Agent records in the What's missing column of the DES-319 (Plague Race) row of its calls sheet that it fails test 6, as Vincent has yet to see it arrive on both iOS and Android (naming test 6, or saying the iOS pass was on the 5-minute timers build or it never showed up on the real iOS build).

### C21
- Title: The Agent records in the What's missing column of the DES-344 (Lapsed 14 days) row of its calls sheet that another message already covers it (naming Lapsed 7 days, DES-317, the weekly batch, the PN sheet's "Has not played in seven days.", or its line "They’ve Taken Over… Can You Stop Them?" or "Your Squad Is Waiting")
- Category: Outcome · Weight: 5
- Justification: Multi-source: the weekly batch's four runs in the code, read with Leonard's cancellation note, show day 14 is covered, and the rule says to name the message.
- Evidence: Sources: Gmail samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> ('The weekly one repeats for four weeks, so day 14 is already covered.'), NotificationManager.cs ('BatchScheduleWeeklyNotifications(WeeklyReminderTitle, WeeklyReminderMessage, 4, serverToday);'); rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop: it fails test 1, or the client already covers it under another message, then name that message.'). Accept: the Agent records in the What's missing column of the DES-344 (Lapsed 14 days) row of its calls sheet that another message already covers it (naming Lapsed 7 days, DES-317, the weekly batch, the PN sheet's "Has not played in seven days.", or its line "They’ve Taken Over… Can You Stop Them?" or "Your Squad Is Waiting").

### C39
- Title: The Agent keeps its Final headline entries to the rows it calls Go in its calls sheet (a blank cell, a dash or N/A on the other rows counts as no entry)
- Category: Outcome · Weight: 1
- Justification: Lookup: the rule keeps the column to Go rows, read across the sheet's own Call column.
- Evidence: Source: rule doc f_dc45e0e5a8b8635c1b82b2 ('Final headline and String change are only for Go rows.'). Accept: the Agent keeps its Final headline entries to the rows it calls Go in its calls sheet (a blank cell, a dash or N/A on the other rows counts as no entry).

### C40
- Title: The Agent keeps its String change entries to the rows it calls Go in its calls sheet (a blank cell, a dash or N/A on the other rows counts as no entry)
- Category: Outcome · Weight: 1
- Justification: Lookup: the rule keeps the column to Go rows, read across the sheet's own Call column.
- Evidence: Source: rule doc f_dc45e0e5a8b8635c1b82b2 ('Final headline and String change are only for Go rows.'). Accept: the Agent keeps its String change entries to the rows it calls Go in its calls sheet (a blank cell, a dash or N/A on the other rows counts as no entry).

### C50
- Title: The Agent names Lives recharged (or DES-315, When lives are recharged, or Full Ammo Reloaded!) in its one-page note as a message the client already schedules that is still a Hold
- Category: Outcome · Weight: 5
- Justification: Multi-source: the message is one of the client's six scheduling calls, and its Hold joins records in other services.
- Evidence: Sources: NotificationManager.cs (six scheduling calls), Slack C0880U9751A/1759245146.720608 ('taking my tick off Full Ammo until I've seen it land'), Linear DES-315 Vincent's Sep 24 pass cmt_51e018b23e18c2f680cd, Gmail QA note; Leonard's DM ('anything the client already schedules that's still a Hold and why'). Accept: the Agent names Lives recharged (or DES-315, When lives are recharged, or Full Ammo Reloaded!) in its one-page note as a message the client already schedules that is still a Hold.

### C51
- Title: The Agent gives test 6 as the reason Lives recharged (or DES-315, When lives are recharged, or Full Ammo Reloaded!) is held in its one-page note (naming test 6, or saying Vincent has yet to see it arrive on both iOS and Android, that Vincent Parker's tick is off, or that it failed to arrive on iOS 0.3.49)
- Category: Outcome · Weight: 5
- Justification: Multi-source: the reason joins the same records as the call.
- Evidence: Sources: Slack C0880U9751A/1759245146.720608 ('taking my tick off Full Ammo until I've seen it land'), Linear DES-315 Vincent's Sep 24 pass cmt_51e018b23e18c2f680cd, Gmail QA note; rule doc f_dc45e0e5a8b8635c1b82b2 ('6. Vincent has seen it arrive on both iOS and Android.'). Accept: the Agent gives test 6 as the reason Lives recharged (or DES-315, When lives are recharged, or Full Ammo Reloaded!) is held in its one-page note (naming test 6, or saying Vincent has yet to see it arrive on both iOS and Android, that Vincent Parker's tick is off, or that it failed to arrive on iOS 0.3.49).

### C52
- Title: The Agent names Plague Race (or DES-319, or Plague Race Is On!) in its one-page note as a message the client already schedules that is still a Hold
- Category: Outcome · Weight: 5
- Justification: Multi-source: the message is one of the client's six scheduling calls, and its Hold joins records in other services.
- Evidence: Sources: NotificationManager.cs (six scheduling calls), Slack D06UFE81RF0/1759174846.723833 ('that iPhone was still on the 5-minute timers build when I ticked it, so scratch iOS.'), Gmail QA note ('A build with shortened timers doesn't count, it only proves the code path.'); Leonard's DM ('anything the client already schedules that's still a Hold and why'). Accept: the Agent names Plague Race (or DES-319, or Plague Race Is On!) in its one-page note as a message the client already schedules that is still a Hold.

### C53
- Title: The Agent gives test 6 as the reason Plague Race (or DES-319, or Plague Race Is On!) is held in its one-page note (naming test 6, or saying Vincent has yet to see it arrive on both iOS and Android, that the iOS pass was on the 5-minute timers build, or that it never showed up on the real iOS build)
- Category: Outcome · Weight: 5
- Justification: Multi-source: the reason joins the same records as the call.
- Evidence: Sources: Slack D06UFE81RF0/1759174846.723833 ('that iPhone was still on the 5-minute timers build when I ticked it, so scratch iOS.'), Gmail QA note ('A build with shortened timers doesn't count, it only proves the code path.'); rule doc f_dc45e0e5a8b8635c1b82b2 ('6. Vincent has seen it arrive on both iOS and Android.'). Accept: the Agent gives test 6 as the reason Plague Race (or DES-319, or Plague Race Is On!) is held in its one-page note (naming test 6, or saying Vincent has yet to see it arrive on both iOS and Android, that the iOS pass was on the 5-minute timers build, or that it never showed up on the real iOS build).

### C54
- Title: The Agent names Weekly Leaderboard reset (or DES-320, or Weekly Rankings Reset!) in its one-page note as a message the client already schedules that is still a Hold
- Category: Outcome · Weight: 5
- Justification: Multi-source: the message is one of the client's six scheduling calls, and its Hold joins records in other services.
- Evidence: Sources: NotificationManager.cs (six scheduling calls), GitHub PR #248 review comment rc_18 ('This counts seven days from the day they last left the game, so it isn't tied to the rollover.'), NotificationManager.cs ('DateTime fireTime = referenceDate.AddDays(i * 7);'); Leonard's DM ('anything the client already schedules that's still a Hold and why'). Accept: the Agent names Weekly Leaderboard reset (or DES-320, or Weekly Rankings Reset!) in its one-page note as a message the client already schedules that is still a Hold.

### C55
- Title: The Agent gives test 5 as the reason Weekly Leaderboard reset (or DES-320, or Weekly Rankings Reset!) is held in its one-page note (naming test 5, or saying it fires on the wrong day, or that it counts from the last session and misses the weekly reset)
- Category: Outcome · Weight: 5
- Justification: Multi-source: the reason joins the same records as the call.
- Evidence: Sources: GitHub PR #248 review comment rc_18 ('This counts seven days from the day they last left the game, so it isn't tied to the rollover.'), NotificationManager.cs ('DateTime fireTime = referenceDate.AddDays(i * 7);'); rule doc f_dc45e0e5a8b8635c1b82b2 ('5. It fires on the right day.'). Accept: the Agent gives test 5 as the reason Weekly Leaderboard reset (or DES-320, or Weekly Rankings Reset!) is held in its one-page note (naming test 5, or saying it fires on the wrong day, or that it counts from the last session and misses the weekly reset).

### C56
- Title: The Agent names Finish first mission (or DES-318, Finish first tutorial, or Finish Your First Mission!) in its one-page note as a message the client already schedules that is still a Hold
- Category: Outcome · Weight: 5
- Justification: Multi-source: the message is one of the client's six scheduling calls, and its Hold joins records in other services.
- Evidence: Sources: NotificationManager.cs (six scheduling calls), Slack C0880U9751A/1759167608.326578 ('leaving our own ask after level 20'), reply C0880U9751A/1759170096.924778 ('NotificationManager only schedules once our own ask has run or they switch it on from settings'), Linear DES-318 audience comment cmt_886fb8b04e3b6ba66b57 ('Who it's for: new players below level 20'), rule doc f_dc45e0e5a8b8635c1b82b2 ('A player only counts once our own permission ask has happened, the settings toggle doesn't count.'); Leonard's DM ('anything the client already schedules that's still a Hold and why'). Accept: the Agent names Finish first mission (or DES-318, Finish first tutorial, or Finish Your First Mission!) in its one-page note as a message the client already schedules that is still a Hold.

### C57
- Title: The Agent gives test 4 as the reason Finish first mission (or DES-318, Finish first tutorial, or Finish Your First Mission!) is held in its one-page note (naming test 4, or saying it can't reach its players, or that its players below level 20 haven't had our own ask, which runs after level 20)
- Category: Outcome · Weight: 5
- Justification: Multi-source: the reason joins the same records as the call.
- Evidence: Sources: Slack C0880U9751A/1759167608.326578 ('leaving our own ask after level 20'), reply C0880U9751A/1759170096.924778 ('NotificationManager only schedules once our own ask has run or they switch it on from settings'), Linear DES-318 audience comment cmt_886fb8b04e3b6ba66b57 ('Who it's for: new players below level 20'), rule doc f_dc45e0e5a8b8635c1b82b2 ('A player only counts once our own permission ask has happened, the settings toggle doesn't count.'). Accept: the Agent gives test 4 as the reason Finish first mission (or DES-318, Finish first tutorial, or Finish Your First Mission!) is held in its one-page note (naming test 4, or saying it can't reach its players, or that its players below level 20 haven't had our own ask, which runs after level 20).

### C95
- Title: The Agent leaves call comments on exactly 32 existing Design tickets
- Category: Outcome · Weight: 5
- Justification: Tracing: DES-313 has to be added to the 31 children of DES-314, and DES-314 itself and the ZOM tickets stay out.
- Evidence: Sources: Linear DES-314 (31 children), DES-313; Leonard's DM ('Leave the call as a comment on each ticket and move the ticket to match.'). Accept: the Agent leaves call comments on exactly 32 existing Design tickets.

### C104
- Title: The Agent moves exactly 24 existing tickets to Backlog
- Category: Outcome · Weight: 5
- Justification: Multi-source: the count comes out of all the calls, and the card overrides Todo.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise.'). Accept: the Agent moves exactly 24 existing tickets to Backlog.

### C105
- Title: The Agent moves exactly 6 existing tickets to Canceled
- Category: Outcome · Weight: 5
- Justification: Multi-source: the count comes out of test 1 and the covered Lapsed 14 days.
- Evidence: Source: rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise.'). Accept: the Agent moves exactly 6 existing tickets to Canceled.

### C106
- Title: The Agent changes the state of exactly 30 existing tickets
- Category: Outcome · Weight: 5
- Justification: Multi-source: Go tickets stay as they are, so the count is the 32 tickets less the two Go.
- Evidence: Source: rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise.'). Accept: the Agent changes the state of exactly 30 existing tickets.

### C107
- Title: The Agent clears the assignee on exactly 24 existing tickets
- Category: Outcome · Weight: 5
- Justification: Multi-source: the count comes out of all the calls, read with the roadmap card's 'unassigned'.
- Evidence: Source: Trello card 68d1eb90bef538c7c5c5599d 'Fix TECH ISSUES' ('Held tickets sit in Backlog, unassigned.'; action 68dae8c7d95e24b55b69bf80). Accept: the Agent clears the assignee on exactly 24 existing tickets.

### C108
- Title: The Agent clears the assignee on DES-313 (Win & Collect start)
- Category: Outcome · Weight: 5
- Justification: Tracing: the ticket is found through the live-ops page, it carries Calvin Price, and the roadmap card's 'unassigned' applies.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d 'Fix TECH ISSUES' ('Held tickets sit in Backlog, unassigned.'; action 68dae8c7d95e24b55b69bf80); Linear DES-313 assignee Calvin Price. Accept: the Agent clears the assignee on DES-313 (Win & Collect start).

### C109
- Title: The Agent clears the assignee on DES-315 (Lives recharged)
- Category: Outcome · Weight: 5
- Justification: Multi-source: the clear rests on the test 6 failure and the roadmap card's 'unassigned'.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d 'Fix TECH ISSUES' ('Held tickets sit in Backlog, unassigned.'; action 68dae8c7d95e24b55b69bf80); Linear DES-315 assignee Samuel Turner. Accept: the Agent clears the assignee on DES-315 (Lives recharged).

### C110
- Title: The Agent clears the assignee on DES-329 (Endless weekly result)
- Category: Outcome · Weight: 3
- Justification: Comparison: the rule's Todo is compared with the later roadmap card, which says unassigned.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d 'Fix TECH ISSUES' ('Held tickets sit in Backlog, unassigned.'; action 68dae8c7d95e24b55b69bf80); Linear DES-329 assignee Samuel Turner. Accept: the Agent clears the assignee on DES-329 (Endless weekly result).

### C117
- Title: The Agent files its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) in Backlog with no assignee
- Category: Outcome · Weight: 3
- Justification: Comparison: the ask is a Hold, and the roadmap card puts held tickets in Backlog, unassigned.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-542 comment cmt_f1b8a109dfa70cdc4565. Accept: the Agent files its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) in Backlog with no assignee.

### C118
- Title: The Agent files its new ticket for the ask on ZOM-556 (Daily gift about to reset) in Backlog with no assignee
- Category: Outcome · Weight: 3
- Justification: Comparison: the ask is a Hold, and the roadmap card puts held tickets in Backlog, unassigned.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-556 comment cmt_2b519285937e7fa79453. Accept: the Agent files its new ticket for the ask on ZOM-556 (Daily gift about to reset) in Backlog with no assignee.

### C119
- Title: The Agent files its new ticket for the ask on ZOM-563 (Teammate sent lives) in Backlog with no assignee
- Category: Outcome · Weight: 3
- Justification: Comparison: the ask is a Hold, and the roadmap card puts held tickets in Backlog, unassigned.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-563 comment cmt_eabac5435f2b3a575aad. Accept: the Agent files its new ticket for the ask on ZOM-563 (Teammate sent lives) in Backlog with no assignee.

### C120
- Title: The Agent files its new ticket for the ask on ZOM-483 (Infinite lives ending) in Backlog with no assignee
- Category: Outcome · Weight: 3
- Justification: Comparison: the ask is a Hold, and the roadmap card puts held tickets in Backlog, unassigned.
- Evidence: Sources: Trello card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.'); Linear ZOM-483 comment cmt_e2e2926a2080ca53c4ea. Accept: the Agent files its new ticket for the ask on ZOM-483 (Infinite lives ending) in Backlog with no assignee.

### C122
- Title: The Agent adds Lapsed 7 days (named by DES-317, Lapsed 7 days, the PN sheet's "Has not played in seven days.", Your Squad Is Waiting or They’ve Taken Over… Can You Stop Them?) as an item on a checklist on the Push Notifications card on ZM ROADMAP (6851a769c65dc0017a227bb7)
- Category: Outcome · Weight: 5
- Justification: Multi-source: the item is a Go, which only the six tests produce, and the card is named by the prompt.
- Evidence: Sources: Trello card 6851a769c65dc0017a227bb7 (Leonard's comment 68d415a716abcb84070a8e2a), NotificationManager.cs ('DailyNotifications(OneDayLapsedTitle, OneDayLapsedMessage, serverToday);'; 'BatchScheduleWeeklyNotifications(WeeklyReminderTitle, WeeklyReminderMessage, 4, serverToday);'), Gmail QA note ('Seen only counts on a store build, on a real iOS device and a real Android device.'), Phone message checks sheet f_8eb8c04713ff6a6ef4a265 (Sep 24 pass), Slack C0880U9751A/1759245146.720608 ('the lapsed ones are still coming through'); Leonard's DM ('Every Go goes on a checklist on our push notifications card so Vincent can tick it off.'). Accept: the Agent adds Lapsed 7 days (named by DES-317, Lapsed 7 days, the PN sheet's "Has not played in seven days.", Your Squad Is Waiting or They’ve Taken Over… Can You Stop Them?) as an item on a checklist on the Push Notifications card on ZM ROADMAP (6851a769c65dc0017a227bb7).

### C145
- Title: The Agent sends its emails about the asks to exactly eight people
- Category: Outcome · Weight: 5
- Justification: Multi-source: the askers come from the ticket creators, and Douglas only from a comment on ZOM-563.
- Evidence: Sources: Contacts for the eight askers, Linear ZOM-563 comment cmt_eabac5435f2b3a575aad; Leonard's DM ('Email each person who asked for something, apart from me, to say what happened to their asks.'). Accept: the Agent sends its emails about the asks to exactly eight people.

### C149
- Title: The Agent posts the counts in Leonard's DM after all of its other writes for the job (the calls sheet, the note, the ticket comments, the ticket moves, the assignee clears, the new tickets, the checklist and the emails), with none of them after the post
- Category: Process · Weight: 1
- Justification: Lookup: the prompt says 'When it's all finished tell him the counts in that same DM'; no Outcome row can show the order.
- Evidence: Source: the prompt ('When it's all finished tell him the counts in that same DM'); Leonard's DM D06L58XCVKK/1759264851.763895. Accept: the Agent posts the counts in Leonard's DM after all of its other writes for the job (the calls sheet, the note, the ticket comments, the ticket moves, the assignee clears, the new tickets, the checklist and the emails), with none of them after the post.

## 3 · Change these 6 rows (same title, other fields)

### C7: The Agent enters Hold in the Call column of the DES-320 (Weekly Leaderboard reset) row of its calls sheet
- Justification: Multi-source: the test 5 failure joins Arthur's PR #248 review comment and the code loop against the ticket and the sheet's Ready status.

### C8: The Agent enters Hold in the Call column of the DES-318 (Finish first mission) row of its calls sheet
- Justification: Multi-source: the test 4 failure joins Robert's Slack post and Arthur's reply against the ticket's audience and the rule.

### C34: The Agent enters the key of its new ticket for the ask on ZOM-563 (Teammate sent lives) in the Ticket column of that ask's row of its calls sheet
- Weight: 1
- Justification: Lookup: the key of the Agent's own new ticket for this ask (not ZOM-563).

### C100: The Agent moves DES-344 (Lapsed 14 days) from In Review to Canceled
- Evidence: Sources: Gmail samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> ('The weekly one repeats for four weeks, so day 14 is already covered.'), match3d Assets/Scripts/Notifications/NotificationManager.cs ('BatchScheduleWeeklyNotifications(WeeklyReminderTitle, WeeklyReminderMessage, 4, serverToday);'); rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise.'); DES-344 state In Review. Accept: the Agent moves DES-344 (Lapsed 14 days) from In Review to Canceled.

### C102: The Agent moves DES-324 (Hourly Coins) from In Review to Canceled
- Evidence: Sources: ZM ROADMAP Backlog list card 68c45bba5d2c25a3a5c26a8c ('Hourly Collection'); rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise.'); DES-324 state In Review. Accept: the Agent moves DES-324 (Hourly Coins) from In Review to Canceled.

### C103: The Agent moves DES-345 (Comeback gift) from In Review to Canceled
- Evidence: Sources: Linear DES-345 comment cmt_13477aa8d1468ae11c9d ('A reward on tap is a version 2 idea, it isn't in the beta.'); rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise.'); DES-345 state In Review. Accept: the Agent moves DES-345 (Comeback gift) from In Review to Canceled.

