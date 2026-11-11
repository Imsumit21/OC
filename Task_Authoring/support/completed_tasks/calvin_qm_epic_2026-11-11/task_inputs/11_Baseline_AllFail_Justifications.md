# Baseline All-Fail Justifications

All 6 baseline rollouts completed, so an all-fail rubric is one that failed in all 6. 24 rubrics failed in all 6, and 24 are valid.

## The Agent sets ZOM-571 (the report "Season pass icon animation restarts every time a panel closes") to the state Todo

ZOM-571 had to end in Todo, because its fix is not in pull request #472. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', sets Todo for a report waiting on a fix, and Arthur Blake's review comment on #472 says the season pass icon restart is not in that diff. All 6 runs read #472 only as a merged pull request named in the sheet's Fix column and never opened its review comments, so they took the fix as merged. Each run moved ZOM-571 under the Season Pass child without changing its state, so it stayed In Validation.

## The Agent sets ZOM-572 (the report "Season pass start popup shows again after every level until it is claimed") to the state In Validation

ZOM-572 had to end in In Validation, because its fix is in pull request #473, merged into main on Sep 30 2025. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', sets In Validation for a report waiting on QA, and Oliver Brooks's comment on #473 lists four flow fixes, this one among them (the pass start popup coming back after every level). The sheet's Fix cell for the row is blank and the note asks whether a fix is in main, so the merged pull requests had to be checked. All 6 runs read the #builds post that shows #473 merged into main, but none opened the comments on #473, so each took the blank cell as no fix. Each run moved ZOM-572 under the Season Pass child without changing its state, so it stayed Todo.

## The Agent sets ZOM-573 (the report "Season pass reward claim animation plays twice when coming back from the shop") to the state In Validation

ZOM-573 had to end in In Validation, because its fix is in pull request #473, merged into main on Sep 30 2025. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', sets In Validation for a report waiting on QA, and Oliver Brooks's comment on #473 lists four flow fixes, this one among them (the claim animation playing twice after the shop). The sheet's Fix cell for the row is blank and the note asks whether a fix is in main, so the merged pull requests had to be checked. All 6 runs read the #builds post that shows #473 merged into main, but none opened the comments on #473, so each took the blank cell as no fix. Each run moved ZOM-573 under the Season Pass child without changing its state, so it stayed Todo.

## The Agent sets ZOM-574 (the report "Event bar starts filling while the daily gift popup is still open") to the state Todo

ZOM-574 had to end in Todo, because its fix is not in pull request #472. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', sets Todo for a report waiting on a fix, and Arthur Blake's review comment on #472 says the event bar start is not in that diff. All 6 runs read #472 only as a merged pull request named in the sheet's Fix column and never opened its review comments, so they took the fix as merged. Each run moved ZOM-574 under the Collect & Win child without changing its state, so it stayed In Validation.

## The Agent sets ZOM-581 (the report "Pack opening sound keeps playing on the home screen after the pack closes") to the state Todo

ZOM-581 had to end in Todo, because its fix is not in pull request #475. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', sets Todo for a report waiting on a fix, and Arthur Blake's review comment on #475 says the pack sound stop is not anywhere in it. All 6 runs read #475 only as a merged pull request named in the sheet's Fix column and never opened its review comments, so they took the fix as merged. Each run moved ZOM-581 under the Card packs child without changing its state, so it stayed In Validation.

## The Agent sets ZOM-584 (the report "Win streak freezer popup opens behind the season pass popup") to the state In Validation

ZOM-584 had to end in In Validation, because its fix is in pull request #473, merged into main on Sep 30 2025. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', sets In Validation for a report waiting on QA, and Oliver Brooks's comment on #473 lists four flow fixes, this one among them (the freezer popup opening behind the pass popup). The sheet's Fix cell for the row is blank and the note asks whether a fix is in main, so the merged pull requests had to be checked. All 6 runs read the #builds post that shows #473 merged into main, but none opened the comments on #473, so each took the blank cell as no fix. Each run moved ZOM-584 under the Win Streak child without changing its state, so it stayed Todo.

## The Agent puts the sub-issue it creates for the report "Pass progress bar fills before the tokens arrive" in the state In Validation

The sub-issue for the report had to be in In Validation, because its fix is in pull request #473, merged into main on Sep 30 2025. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', gives a new sub-issue the state that matches its status, and Oliver Brooks's comment on #473 lists this fix (the pass bar filling before the tokens land). The sheet's Fix cell for the row is blank and the note asks whether a fix is in main, so the merged pull requests had to be checked. All 6 runs read the #builds post that shows #473 merged into main, but none opened the comments on #473, so each took the blank cell as no fix. Each run created the sub-issue in Todo.

## The Agent adds a comment on ZOM-571 that gives the status of the report "Season pass icon animation restarts every time a panel closes" as Waiting on a fix (any wording with that meaning: waits on a fix, needs a fix, fix pending)

The comment on ZOM-571 had to give the status Waiting on a fix, because pull request #472 does not hold its fix. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', asks for a note with the status and why on each moved ticket, and Arthur Blake's review comment on #472 says the season pass icon restart is not in that diff. All 6 runs read #472 only as a merged pull request named in the sheet's Fix column and never opened its review comments, so they took the fix as merged. Each run's comment on ZOM-571 gives Waiting on QA.

## The Agent gives, in its comment on ZOM-571, the reason that pull request #472 does not hold its fix (any wording with that meaning)

The comment on ZOM-571 had to say that pull request #472 does not hold its fix. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', asks for a note with the status and why on each moved ticket, and Arthur Blake's review comment on #472 says the season pass icon restart is not in that diff. All 6 runs read #472 only as a merged pull request named in the sheet's Fix column and never opened its review comments, so they took the fix as merged. Each run's comment on ZOM-571 gives the opposite reason, that the fix is in main through #472.

## The Agent adds a comment on ZOM-572 that gives the status of the report "Season pass start popup shows again after every level until it is claimed" as Waiting on QA (any wording with that meaning: waits on QA, ready for QA, to re-test)

The comment on ZOM-572 had to give the status Waiting on QA, because its fix is in pull request #473, merged into main on Sep 30 2025. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', asks for a note with the status and why on each moved ticket, and Oliver Brooks's comment on #473 lists this fix (the pass start popup coming back after every level). The sheet's Fix cell for the row is blank and the note asks whether a fix is in main, so the merged pull requests had to be checked. All 6 runs read the #builds post that shows #473 merged into main, but none opened the comments on #473, so each took the blank cell as no fix. Each run's comment on ZOM-572 gives Waiting on a fix.

## The Agent gives, in its comment on ZOM-572, the reason that its fix is in pull request #473, which is merged into main (any wording with that meaning)

The comment on ZOM-572 had to say that its fix is in pull request #473, which is merged into main. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', asks for a note with the status and why on each moved ticket, and Oliver Brooks's comment on #473 lists this fix (the pass start popup coming back after every level). The sheet's Fix cell for the row is blank and the note asks whether a fix is in main, so the merged pull requests had to be checked. All 6 runs read the #builds post that shows #473 merged into main, but none opened the comments on #473, so each took the blank cell as no fix. Each run's comment on ZOM-572 says no fix is in main, and none names #473.

## The Agent adds a comment on ZOM-573 that gives the status of the report "Season pass reward claim animation plays twice when coming back from the shop" as Waiting on QA (any wording with that meaning: waits on QA, ready for QA, to re-test)

The comment on ZOM-573 had to give the status Waiting on QA, because its fix is in pull request #473, merged into main on Sep 30 2025. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', asks for a note with the status and why on each moved ticket, and Oliver Brooks's comment on #473 lists this fix (the claim animation playing twice after the shop). The sheet's Fix cell for the row is blank and the note asks whether a fix is in main, so the merged pull requests had to be checked. All 6 runs read the #builds post that shows #473 merged into main, but none opened the comments on #473, so each took the blank cell as no fix. Each run's comment on ZOM-573 gives Waiting on a fix.

## The Agent gives, in its comment on ZOM-573, the reason that its fix is in pull request #473, which is merged into main (any wording with that meaning)

The comment on ZOM-573 had to say that its fix is in pull request #473, which is merged into main. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', asks for a note with the status and why on each moved ticket, and Oliver Brooks's comment on #473 lists this fix (the claim animation playing twice after the shop). The sheet's Fix cell for the row is blank and the note asks whether a fix is in main, so the merged pull requests had to be checked. All 6 runs read the #builds post that shows #473 merged into main, but none opened the comments on #473, so each took the blank cell as no fix. Each run's comment on ZOM-573 says no fix is in main, and none names #473.

## The Agent adds a comment on ZOM-574 that gives the status of the report "Event bar starts filling while the daily gift popup is still open" as Waiting on a fix (any wording with that meaning: waits on a fix, needs a fix, fix pending)

The comment on ZOM-574 had to give the status Waiting on a fix, because pull request #472 does not hold its fix. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', asks for a note with the status and why on each moved ticket, and Arthur Blake's review comment on #472 says the event bar start is not in that diff. All 6 runs read #472 only as a merged pull request named in the sheet's Fix column and never opened its review comments, so they took the fix as merged. Each run's comment on ZOM-574 gives Waiting on QA.

## The Agent gives, in its comment on ZOM-574, the reason that pull request #472 does not hold its fix (any wording with that meaning)

The comment on ZOM-574 had to say that pull request #472 does not hold its fix. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', asks for a note with the status and why on each moved ticket, and Arthur Blake's review comment on #472 says the event bar start is not in that diff. All 6 runs read #472 only as a merged pull request named in the sheet's Fix column and never opened its review comments, so they took the fix as merged. Each run's comment on ZOM-574 gives the opposite reason, that the fix is in main through #472.

## The Agent adds a comment on ZOM-581 that gives the status of the report "Pack opening sound keeps playing on the home screen after the pack closes" as Waiting on a fix (any wording with that meaning: waits on a fix, needs a fix, fix pending)

The comment on ZOM-581 had to give the status Waiting on a fix, because pull request #475 does not hold its fix. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', asks for a note with the status and why on each moved ticket, and Arthur Blake's review comment on #475 says the pack sound stop is not anywhere in it. All 6 runs read #475 only as a merged pull request named in the sheet's Fix column and never opened its review comments, so they took the fix as merged. Each run's comment on ZOM-581 gives Waiting on QA.

## The Agent gives, in its comment on ZOM-581, the reason that pull request #475 does not hold its fix (any wording with that meaning)

The comment on ZOM-581 had to say that pull request #475 does not hold its fix. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', asks for a note with the status and why on each moved ticket, and Arthur Blake's review comment on #475 says the pack sound stop is not anywhere in it. All 6 runs read #475 only as a merged pull request named in the sheet's Fix column and never opened its review comments, so they took the fix as merged. Each run's comment on ZOM-581 gives the opposite reason, that the fix is in main through #475.

## The Agent adds a comment on ZOM-584 that gives the status of the report "Win streak freezer popup opens behind the season pass popup" as Waiting on QA (any wording with that meaning: waits on QA, ready for QA, to re-test)

The comment on ZOM-584 had to give the status Waiting on QA, because its fix is in pull request #473, merged into main on Sep 30 2025. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', asks for a note with the status and why on each moved ticket, and Oliver Brooks's comment on #473 lists this fix (the freezer popup opening behind the pass popup). The sheet's Fix cell for the row is blank and the note asks whether a fix is in main, so the merged pull requests had to be checked. All 6 runs read the #builds post that shows #473 merged into main, but none opened the comments on #473, so each took the blank cell as no fix. Each run's comment on ZOM-584 gives Waiting on a fix.

## The Agent gives, in its comment on ZOM-584, the reason that its fix is in pull request #473, which is merged into main (any wording with that meaning)

The comment on ZOM-584 had to say that its fix is in pull request #473, which is merged into main. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', asks for a note with the status and why on each moved ticket, and Oliver Brooks's comment on #473 lists this fix (the freezer popup opening behind the pass popup). The sheet's Fix cell for the row is blank and the note asks whether a fix is in main, so the merged pull requests had to be checked. All 6 runs read the #builds post that shows #473 merged into main, but none opened the comments on #473, so each took the blank cell as no fix. Each run's comment on ZOM-584 says no fix is in main, and none names #473.

## The Agent gives the report "Pass progress bar fills before the tokens arrive" the Status Waiting on QA (any wording with that meaning: waits on QA, ready for QA, to re-test) in the Reports tab of the stock-take sheet

The Status cell of the report had to read Waiting on QA, because its fix is in pull request #473, merged into main on Sep 30 2025. Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', asks for a Status on every report row of the stock-take sheet, and Oliver Brooks's comment on #473 lists this fix (the pass bar filling before the tokens land). The sheet's Fix cell for the row is blank and the note asks whether a fix is in main, so the merged pull requests had to be checked. All 6 runs read the #builds post that shows #473 merged into main, but none opened the comments on #473, so each took the blank cell as no fix. Each run wrote Waiting on a fix in that cell.

## The Agent gives 9 as the number of reports waiting on QA in its message to Brian Foster in Calvin's Slack DM with him

The message to Brian had to give 9 reports waiting on QA. The count runs over the 39 reports under Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', and Brian's message asks for it. It needs the three reports whose fix Arthur Blake's review comments on #472 and #475 say is not in those pull requests, and the four reports whose fix Oliver Brooks's comment lists in the merged #473. No run opened those comments, so the six runs gave 7, 8, 8, 8, 7 and 8.

## The Agent gives 20 as the number of reports waiting on a fix in its message to Brian Foster in Calvin's Slack DM with him

The message to Brian had to give 20 reports waiting on a fix. The count runs over the 39 reports under Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', and Brian's message asks for it. It needs the three reports whose fix Arthur Blake's review comments on #472 and #475 say is not in those pull requests, and the four reports whose fix Oliver Brooks's comment lists in the merged #473. No run opened those comments, so the six runs gave 18, 21, 17, 19, 18 and 19.

## The Agent gives 9 as the number of reports waiting on QA on the slide it adds to Calvin's ZM queue manager presentation

The new slide had to give 9 reports waiting on QA. The count runs over the 39 reports under Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', and Brian's message asks for it. It needs the three reports whose fix Arthur Blake's review comments on #472 and #475 say is not in those pull requests, and the four reports whose fix Oliver Brooks's comment lists in the merged #473. No run opened those comments, so the six runs gave 7, 8, 8, 8, 7 and 8.

## The Agent gives 20 as the number of reports waiting on a fix on the slide it adds to Calvin's ZM queue manager presentation

The new slide had to give 20 reports waiting on a fix. The count runs over the 39 reports under Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', and Brian's message asks for it. It needs the three reports whose fix Arthur Blake's review comments on #472 and #475 say is not in those pull requests, and the four reports whose fix Oliver Brooks's comment lists in the merged #473. No run opened those comments, so the six runs gave 18, 21, 17, 19, 18 and 19.
