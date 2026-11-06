"""Apply the platform /rubric Fix List (report 6ae9909f7b5249d3148f3707_3_rubric.md) to 09_Rubrics.json.
Row numbers R# are the reviewed 70-row file (sha e898aefcbd72). Every edit asserts the old value first."""
import json, sys

P = sys.argv[1]
t = open(P).read()
d = json.loads(t)
assert len(d) == 70
R = {i: d[i - 1] for i in range(1, 71)}


def chk(i, frag):
    assert frag in R[i]["title"], (i, R[i]["title"][:80])


def swap(i, field, old, new):
    assert old in R[i][field], (i, field, old)
    R[i][field] = R[i][field].replace(old, new)


def prefix(i, new):
    j = R[i]["justification"]
    R[i]["justification"] = new + j[j.index(":"):]


# 1. R1
chk(1, "ends the run with exactly one new tab")
R[1].update(
    title="The Agent puts the gate register for Android Submission #135 / iOS Submission #50 in a new tab it adds to "
          "Vincent's ZM3D Release Gate spreadsheet (f_0ebfccf33076f9dbf086bc)",
    justification="Lookup: the prompt says 'Put the gate register in a new tab of my release gate sheet', and Vincent's "
                  "release gate sheet is the ZM3D Release Gate spreadsheet.",
    evidence="Sources: the prompt ('Put the gate register in a new tab of my release gate sheet'); Vincent's spreadsheet "
             "ZM3D Release Gate f_0ebfccf33076f9dbf086bc (tabs before the run: 'How we gate' and 'Sep 22 - Android #127 / "
             "iOS #40'). Accept: the gate register sits in a tab the Agent added to that spreadsheet; a register written "
             "into the Sep 22 tab or the How we gate tab, or only into another spreadsheet, fails.")

# 2. new tab-name row after R1
tab_name = {
    "title": "The Agent names its new register tab in Vincent's ZM3D Release Gate spreadsheet after both candidate builds, "
             "Android #135 and iOS #50 (a date prefix and the word 'Submission' optional)",
    "category": "Outcome",
    "weight": 1,
    "justification": "Lookup: the How we gate tab says 'One tab per gate, named after the candidate builds.', and the "
                     "candidates are Android Submission #135 and iOS Submission #50.",
    "evidence": "Sources: How we gate tab of ZM3D Release Gate f_0ebfccf33076f9dbf086bc ('One tab per gate, named after "
                "the candidate builds.'); the previous gate's tab 'Sep 22 - Android #127 / iOS #40'; Arthur Blake's post "
                "C08R27X0EAH/1759263900.484190 ('Android Submission #135 and iOS Submission #50'). Accept: the new "
                "register tab's name carries both candidate builds, Android #135 and iOS #50, with or without a date "
                "prefix and the word 'Submission'; a name that leaves out either build, or pairs 135 with iOS and 50 with "
                "Android, fails.",
}

# 3. R2
chk(2, "delivers the gate register")
R[2].update(
    title="The Agent ends the run with the values it wrote in exactly one tab of Vincent's ZM3D Release Gate spreadsheet "
          "(f_0ebfccf33076f9dbf086bc)",
    justification="Lookup: the prompt asks for the register in 'a new tab of my release gate sheet' and the How we gate "
                  "tab says 'One tab per gate'; the Sep 22 tab is the previous gate's register, a decoy for this gate's "
                  "values.",
    evidence="Sources: the prompt ('Put the gate register in a new tab of my release gate sheet'); How we gate tab of "
             "f_0ebfccf33076f9dbf086bc ('One tab per gate, named after the candidate builds. One row per ticket.'); the "
             "previous gate's tab 'Sep 22 - Android #127 / iOS #40'. Accept: at the end of the run every value the Agent "
             "wrote in that spreadsheet sits in one tab, whichever tab holds them; a deleted draft tab and an empty tab "
             "don't count. Values the Agent left in two or more tabs fail.")

# 4. R3
chk(3, "exactly 133 ticket rows")
R[3].update(
    title="The Agent writes exactly 132 rows naming existing tickets below the header row in its new tab of the ZM3D "
          "Release Gate spreadsheet, each naming a different ticket (rows for tickets it files during the run not counted)",
    justification="Multi-source: Leonard's scope ('every ZM ticket that's still open ..., whatever team or label ..., plus "
                  "everything that moved to Done after the last gate's builds were cut', release tickets, ZOM-359 and "
                  "ZOM-475 out) gives 112 open tickets plus 20 moved to Done after the Android #127 cut "
                  "(2025-09-22 12:30:43 UTC): 132 existing tickets.",
    evidence="Sources: Leonard's 'ZM submission rules' doc f_632c44650df44fe252ee59 (scope sentence); #builds "
             "C05433XK267/1758544243.280239 (Android #127 Started 2025-09-22 12:30:43 UTC); Linear teams ZOM, ART and "
             "DES. Accept: exactly 132 rows below the header row that each name a different ticket that existed before "
             "the run; rows for tickets the Agent files during the run, blank rows and rows naming no ticket are not "
             "counted. Any other count fails.")

# 5. R22 evidence
chk(22, "BLOCKER for the new ticket")
swap(22, "evidence", "Accept: the row for the new update-path ticket, by its new ZOM key, has the call BLOCKER.",
     "Accept: the register row for the new update-path ticket (identified by its new ZOM key, its Linear link or its "
     "title) has the call BLOCKER.")

# 7. weights
chk(25, "FIXED for ZOM-563"); assert R[25]["weight"] == 3; R[25]["weight"] = 5; prefix(25, "Multi-source")
chk(32, "server - live for ZOM-563"); assert R[32]["weight"] == 3; R[32]["weight"] = 5; prefix(32, "Multi-source")
chk(33, "in candidate for ZOM-473"); assert R[33]["weight"] == 3; R[33]["weight"] = 5; prefix(33, "Multi-source")
chk(34, "n/a for ZOM-477"); assert R[34]["weight"] == 3; R[34]["weight"] = 1; prefix(34, "Lookup")

# 8. R38
chk(38, "Trello card Fix TECH ISSUES")
swap(38, "title", "(68d1eb90bef538c7c5c5599d, link trello.com/c/pTbZYXdb)",
     "(68d1eb90bef538c7c5c5599d, or a link containing /c/pTbZYXdb)")
swap(38, "evidence", "or a link to the card (short link pTbZYXdb)", "or a link containing /c/pTbZYXdb")

# 9. R39 (and weight from 7)
chk(39, "DM with Douglas that settles ZOM-563"); assert R[39]["weight"] == 3
R[39]["title"] = ("The Agent puts the record of Vincent's Sep 30 DM with Douglas that settles ZOM-563 (channel D079SNE2TL4 "
                  "with Douglas's prod update ts 1759256193.859279 or Vincent's confirmation ts 1759269524.769369, or a "
                  "Slack link to either message) in ZOM-563's evidence cell of its new tab of the ZM3D Release Gate "
                  "spreadsheet")
R[39]["weight"] = 5
prefix(39, "Multi-source")

# 11. R42
chk(42, "exactly 19 tickets as blockers")
R[42].update(
    title="The Agent lists exactly 18 existing tickets as blockers in the description of the release ticket ZOM-570 "
          "(a ticket it files during the run not counted)",
    justification="Multi-source: the BLOCKER calls of the register's existing tickets (18, besides the new update-path "
                  "ticket) are the list Arthur asks for 'by key, the existing ticket if there is one'.")
swap(42, "evidence", "Accept: exactly 19 distinct tickets listed as blockers in ZOM-570's description.",
     "Accept: exactly 18 distinct tickets that existed before the run listed as blockers in ZOM-570's description; a "
     "ticket the Agent files during the run is not counted. Any other count fails.")

# 12. R62 + new source-build row
chk(62, "files a new Linear issue in the ZOM")
R[62]["title"] = ("The Agent files a new Linear issue in the ZOM (Zombie Match 3D) team for the save reset found on the "
                  "runbook's update path: after the update the save comes back at level 1")
swap(62, "evidence", "Accept: a new issue in team ZOM describing that update and the save coming back at level 1.",
     "Accept: a new issue in team ZOM whose title or description says that after the update the save comes back at "
     "level 1.")
source_build = {
    "title": "The Agent names the source build N-1 (the previous App Store version) in its new update-path save-reset "
             "issue in Linear (in the issue's title or description or in a comment it adds on that issue)",
    "category": "Outcome",
    "weight": 1,
    "justification": "Lookup: the runbook says 'File the bug with device, OS version, source build and repro steps', and "
                     "the failing row's source build is N-1.",
    "evidence": "Sources: QA Regression Runbook page_qa_runbook ('File the bug with device, OS version, source build and "
                "repro steps'); Brian Foster's doc f_5e40215b7d4d24b0455412 ('iPhone 13 | iOS 18.6 | N-1 | iOS "
                "Submission #50 | FAIL'). Accept: the new issue's title or description, or a comment the Agent adds on "
                "it, names N-1 or the previous App Store version as the build the update started from.",
}

# 13. R63, R64
SUFFIX = " (in the issue's title or description or in a comment it adds on that issue)"
chk(63, "names the device iPhone 13"); R[63]["title"] += SUFFIX
chk(64, "names the OS version iOS 18.6"); R[64]["title"] += SUFFIX

# 14. R65
chk(65, "gives repro steps")
R[65]["title"] = ("The Agent gives repro steps in its new update-path save-reset issue in Linear (in the issue's description "
                  "or in a comment it adds on that issue) that install an earlier App Store build, play past level 200, "
                  "install TestFlight 50 (iOS Submission #50) over it and launch the game")
swap(65, "evidence", "Accept: those four steps in the new issue's title, description or a comment the Agent adds on it, "
                     "in any wording, numbered or in one sentence.",
     "Accept: those four steps in the new issue's description or a comment the Agent adds on it, in any wording, "
     "numbered or in one sentence; the first step may name the N-1 build or say an earlier App Store build.")

# 16. R68
chk(68, "posts its QA call in Slack only")
R[68].update(
    title="The Agent posts exactly one message in #zombie-bugs (channel C08R27X0EAH) during the run",
    justification="Lookup: Leonard's ZOM-570 comment asks for the sign-off 'as a reply on Arthur's candidate thread in "
                  "#zombie-bugs please, not a new post', so the run's one #zombie-bugs message is that reply.",
    evidence="Sources: Leonard Hayes's ZOM-570 comment cmt_zom570_1 ('sign-off as a reply on Arthur's candidate thread "
             "in #zombie-bugs please, not a new post'); Arthur Blake's post C08R27X0EAH/1759263900.484190. Accept: "
             "exactly one message the Agent sends in C08R27X0EAH during the run, top-level posts and thread replies "
             "counted alike (a thread reply also sent to the channel counts once); no message, or two or more, fails.")

# deletions (6, 10, 15, 17) and insertions (2, 12)
chk(23, "FIXED for ZOM-429"); chk(27, "KNOWN ISSUE for ZOM-481"); chk(41, "into no other Linear issue")
chk(67, "QA Regression Runbook Confluence page"); chk(69, "before the go/no-go")
DROP = {23, 27, 41, 67, 69}
out = []
for i in range(1, 71):
    if i in DROP:
        continue
    out.append(R[i])
    if i == 1:
        out.append(tab_name)
    if i == 62:
        out.append(source_build)
assert len(out) == 67, len(out)
open(P, "w").write(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print("rows", len(out), "weight", sum(r["weight"] for r in out))
