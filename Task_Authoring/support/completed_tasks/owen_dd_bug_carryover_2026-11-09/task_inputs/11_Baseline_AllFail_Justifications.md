# Baseline All-Fail Justifications

All 6 baseline rollouts completed, so an all-fail rubric is one that failed in all 6. Nine rubrics failed in all 6, and all nine are valid.

## The Agent files exactly 68 new issues for the DD bug carry-over, each in the Engineering team with the Bug label, parent ENG-2401, no assignee, an empty description and a title starting [2231]

The expected count is exactly 68 new issues: 63 canvas lines plus 7 later bug posts, minus the 2 lines that open tickets already cover. The prompt asks for everything Arthur asked the way he lays it out, and his carry-over notes say a line an open ticket already covers gets a note on that ticket instead of a new one, and that Vincent tied a few lines to tickets before he left; Vincent's email in Owen's inbox (Nov 20, 2025) ties the Apple sync line to ENG-2073, which is still open in Bugs. All six runs found Vincent's other tie, a comment on ENG-2363, yet filed 69 issues (ENG-2438 to ENG-2506), adding ENG-2440 for the Apple sync line, because none of them opened Vincent's email: their only Gmail searches were for Brian's mail, the build number or the UI work. Every other part of the template held in all six runs, so the count of 69 alone fails the row.

## The Agent files the issue for canvas line "Tavern buttons lost its frame." (it ends with a mention of Owen Baker) in the Bugs state

The expected state for the Tavern buttons issue is Bugs, because Marcus's Dec 11, 2025 DM to Owen says the frame was lost again on the Android build and Brian's fix didn't hold. The carry-over notes say a tick on the canvas stands unless a later record about that bug says otherwise, and anything not fixed, gone or covered is Broken and filed as Bugs; Marcus's message sits in Owen's own DMs and a Slack search for Tavern reaches it. All six runs filed the issue for the ticked Tavern line in Done, relying on the tick and Brian's Nov 20 fix in the line's thread, and none of them searched Slack for Tavern or opened the DM with Marcus.

## The Agent comments on ENG-2073 with the canvas line "In general, I cannot sync and sign in with my Apple account"

The expected write is a new comment on ENG-2073 carrying the canvas line In general, I cannot sync and sign in with my Apple account. The carry-over notes say a line an open ticket already covers gets a note on that ticket with the canvas wording and no new ticket, and Vincent's Nov 20, 2025 email in Owen's inbox says the Apple sync line comes down to the same sync problem as ENG-2073, no need for anything new; ENG-2073 is still open in Bugs. No run left any comment on ENG-2073: all six filed a new issue for the line (ENG-2440) instead, and none opened Vincent's email. The same runs did add the canvas wording to ENG-2363 for the other line Vincent tied, so the miss is the email, not the comment step.

## The Agent records the Tavern buttons lost its frame line as Broken (or Bugs) in the DD carry-over sheet

The expected Outcome for the Tavern buttons lost its frame row in the carry-over sheet is Broken (or Bugs), because Marcus's Dec 11, 2025 DM says Brian's fix didn't hold. The notes set the sheet columns Bug, Outcome, Ticket and Why and say a tick stands only until a later record about that bug says otherwise; Marcus's message sits in Owen's own DMs. All six runs wrote Fixed for the Tavern row, with a Why citing the tick or Brian's Nov 20 fix, because none of them opened the DM with Marcus or searched Slack for Tavern.

## The Agent records ENG-2073 as the ticket of the Apple sync line (In general, I cannot sync and sign in with my Apple account) in the DD carry-over sheet

The expected Ticket for the Apple sync line in the carry-over sheet is ENG-2073, the open ticket Vincent tied the line to in his Nov 20, 2025 email. The notes say a covered line gets no new ticket, that Vincent tied a few lines to tickets before he left, and give the sheet a Ticket column, so the row should point at the ticket that covers it; Vincent's email is in Owen's inbox and ENG-2073, titled Sign-In Account Synchronization Issues, is open in Bugs. All six runs put ENG-2440, the new issue they had filed for the line, in the Ticket cell; two of them judged from ENG-2073's own description that it was a different issue, because none of them opened the email that ties the line to it.

## The Agent records the Apple sync line (In general, I cannot sync and sign in with my Apple account) as Covered in the DD carry-over sheet

The expected Outcome for the Apple sync line in the carry-over sheet is Covered, because Vincent's Nov 20, 2025 email ties it to ENG-2073 (Sign-In Account Synchronization Issues), which is still open. The notes define Covered as a line that isn't fixed and that an open ticket already covers, and say Vincent tied a few lines to tickets before he left; his email is in Owen's inbox. All six runs recorded the line as Broken with their own new issue ENG-2440, since none of them opened the email; they found only the ENG-2363 tie, which Vincent left as a Linear comment.

## The Agent states in the Why cell of the Tavern buttons lost its frame line in the DD carry-over sheet that the buttons lost their frame again after Brian's fix

The expected Why for the Tavern buttons lost its frame row is that the buttons lost their frame again after Brian's fix, as Marcus's Dec 11, 2025 DM to Owen says. The notes give the sheet a Why column and say a tick stands only until a later record about that bug says otherwise; the DM is in Owen's own messages and a Slack search for Tavern reaches it. All six runs gave a Why built on the stale record instead, either that the line is ticked with nothing later or that Brian sent the fix, because none of them opened the DM with Marcus.

## The Agent tells Arthur in its reply to Arthur in his Feb 12 DM (D05S1S2AB5M) that 9 bugs are still broken

The expected figure is 9 still broken: 7 Broken items filed as Bugs plus the 2 Covered lines, which the notes say count as still broken when reporting back. Arthur's DM asks how many are still broken; the 7 Broken items include the Tavern line, which Marcus's Dec 11, 2025 DM reopens, while the Apple sync line is Covered by ENG-2073 per Vincent's Nov 20, 2025 email. Every run replied Still broken: 8, made of 7 issues in Bugs (with the Apple line in place of the Tavern line) plus 1 Covered line, ENG-2363, because each run missed both Marcus's DM and Vincent's email.

## The Agent tells Arthur in its reply to Arthur in his Feb 12 DM (D05S1S2AB5M) that it filed 68 new tickets

The expected figure is 68 new tickets: 63 canvas lines plus 7 later bug posts, minus the 2 lines that open tickets already cover. Arthur's DM asks how many new tickets were filed, and the notes say a covered line gets a note on its ticket, not a new one; Vincent's Nov 20, 2025 email ties the Apple sync line to ENG-2073. Every run replied New tickets filed: 69, counting the extra ENG-2440 it filed for the Apple sync line after missing Vincent's email, so the told figure is wrong by the same one ticket as the Linear count.
