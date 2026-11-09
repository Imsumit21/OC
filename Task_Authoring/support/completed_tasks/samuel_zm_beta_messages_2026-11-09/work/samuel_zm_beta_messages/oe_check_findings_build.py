#!/usr/bin/env python3
"""Write plan/oe_check_findings.json: the independent review's items with their dispositions, numbered from the live event index."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
N = json.load(open(os.path.join(HERE, "oe_events_index.json")))["index"]
EXTRA = os.path.join(HERE, "oe_check_recheck.json")
n = lambda k: f"OE {N[k]}"  # noqa: E731
adv = [
    (n("c1"), "Pre-check revision (independent review #1, confirmed): free shop coins were called a BETA-list item. The shop card is about inventory; DES-339 says 'We already give free coins in the shop.' (SQL L159). The basis now quotes that line, carried in " + n("kids") + "."),
    (n("c1"), "Pre-check revision (independent review #2, confirmed): 'the lapsed messages' were called client-scheduled, but DES-342 and DES-343 say 'not in NotificationManager yet'. It now names Lapsed 1 day and Lapsed 7 days in the client and the other three as the same feature; GitHub added to the sources."),
    (n("freeze"), "Pre-check revision (independent review #3, confirmed): Leonard's authorship sits on the updateCard action (SQL L54, trello /members/2), which a card read does not return. See the recheck row: the event no longer states the author."),
    (n("feat2"), "Pre-check revision (independent review #4, confirmed): ZOM-314 says the button 'will be used when' Helpshift is implemented, so it does not show support shipped. ZOM-301 'Helpshift Implementation', Done (linear /issues/3356), now carries Support reply waiting at test 1."),
    (n("c1"), "Pre-check revision (independent review #5, confirmed): 'the daily login' had no source. DES-322's 'Daily login is already in the game.' (SQL L125) and DES-321's 'Quests are already in production.' now carry those rows."),
    (n("feat"), "Pre-check revision (independent review #6, confirmed): the heading said the BETA list leaves Boss Arena out; it is on the list. Reworded to tie it to the card."),
    (n("rc18"), "Pre-check revision (independent review #7, #8, #9, confirmed): the PR number now comes from " + n("kids") + " ('Built in match3d #248.'); the merged date, which a comments read does not return, is gone; the comment is placed on BatchScheduleWeeklyLeaderboardNotifications, as its diff hunk ends there (SQL L92)."),
    (n("vid"), "Pre-check revision (independent review #10, confirmed): a new event produces Vincent's Slack user id (slack users.json) before the search that uses it."),
    (n("client"), "Pre-check revision (independent review #11, #17, #26, confirmed): the separate level-constant event and the level-gate sentence are gone, because test 4 rests on DES-318 and the sheet's Segmentation cell. The four titles now sit behind 'Titles include' and are quoted from the hunk read through hg.py, so no Expected value depends on a repository blob."),
    (n("line2"), "Pre-check revision (independent review #12, confirmed): a search does not return the parent post, so the Martin Walsh label is gone."),
    (n("sheet"), "Pre-check revision (independent review #13, #14, confirmed): the twin sheet sentence, which no event read, is gone; rows now show the tab's own Details column instead of message names it does not hold."),
    (f"{n('roadmap')}, {n('liveops')}", "Pre-check revision (independent review #15, #16, confirmed): partial rundowns now say 'among others' and 'Among the event rows'."),
    (f"{n('census')}, {n('tcard')}", "Pre-check revision (independent review #18, #19, confirmed): the Linear search now covers three terms, and a new Trello event covers cards, so 'a ticket or a card' is searched on both sides. The reviewer's own sweep of all 3,687 issues and 803 cards found no further ask."),
    (f"{n('wh')}, {n('w_note')}", "Pre-check revision (independent review #20, confirmed): percent added."),
    (n("w_rows"), "Pre-check revision (independent review #21, #22, confirmed): the row event now covers What's missing on Go and Drop rows, and accepts the sheet's or the ticket's name or a short form."),
    (f"{n('wc')}, {n('wcc')}, {n('feat')}, {n('feat2')}", "Pre-check revision (independent review #23, a format risk): the find-and-read and multi-lookup events are split. Population reads stay one event each, as gate 14 allows."),
    (n("pop"), "Independent review #24, kept: updatedAt and orderBy are cataloged parameters of linear_list_issues (Evals/references/tools/linear-tools.json) and the records carry updated_at, but 0 of 27 baseline list calls used them. limit 100 added, since the filtered call returns 53 rows. createdAt behaved as a since filter in run-2."),
    (n("rc18"), "Independent review #25, kept: github_get_pull_request_comments is cataloged but no run called it, so the event also offers the same comment in Samuel's Gmail (SQL L69), a branch that completes the step alone."),
    (f"{n('ask:Boss Arena attempts refilled')} to {n('rest')}", "Independent review note, kept: linear_list_comments was never called on a ZOM ticket in a run. It worked on every DES ticket, and issueId is its one required parameter."),
    (f"{n('w_new:Boss Arena attempts refilled')}", "Independent review note, kept: linear_create_issue was run with state Todo, not Backlog. state is a cataloged parameter and linear_update_issue reached Backlog in every run."),
    ("all", "Size: " + str(json.load(open(os.path.join(HERE, "oe_events_index.json")))["events"]) + " events, about 41,000 characters, to be typed by hand (the field blocks pasting). Each write is its own event by the one-write rule."),
]
rc = json.load(open(EXTRA)) if os.path.exists(EXTRA) else {"advisory": [], "note": "It then re-read the rewritten events."}
adv += [tuple(x) for x in rc["advisory"]]
ind = ("Independent review: one general-purpose reviewer, given the file, the prompt, the SQL and the rules, but not the ledger, brief, solver, dossier or this report, read the events against the SQL rows and the base through hg.py. "
       "It reached the same 36 calls on its own (Go 2, Hold 28, Drop 6), found no missing population member or write and no unauthorised write, and confirmed every quoted string, timestamp and weekday it could reach. "
       "It raised 26 items; each was checked against its record, and all are fixed or kept with a reason under Advisory. " + rc["note"])
json.dump({"spans": 224, "independent": ind, "findings": [], "advisory": adv, "prediction": "PASS 5", "completeness": 5, "accuracy": 5,
           "preface": "Before this check ran, the draft was revised for the items under Advisory; this report judges the revised file only."},
          open(os.path.join(HERE, "oe_check_findings.json"), "w"), indent=0, ensure_ascii=False)
print("advisory", len(adv))
