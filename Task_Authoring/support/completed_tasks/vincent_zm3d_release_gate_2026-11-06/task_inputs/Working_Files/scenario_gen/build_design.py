#!/usr/bin/env python3
"""Generator for the scenario-stage artifacts of the Vincent Parker release-gate task (design only, no SQL).

Writes Working_Files/01_Hardness_Manifest.draft.json and Working_Files/01_Gradable_Surface.json from the data below,
so every id, count and weight lives in one place. Read-only on the universe; run from the workspace root:
    python3 -B Task_Authoring/task_inputs/Working_Files/scenario_gen/build_design.py
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path

TASK = Path(__file__).resolve().parents[2]
WF = TASK / "Working_Files"
CTX = json.loads((WF / "00_Task_Context.json").read_text())
IDS = json.loads((Path(__file__).with_name("ids.json")).read_text())


def ep(ts: str) -> int:
    return int(dt.datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp())


# ------------------------------------------------------------------ planned seeded records (ids from ids.json)
GATE_SHEET = IDS["gate_sheet"]            # Vincent-owned 'ZM3D Release Gate'
UPDATE_LOG = IDS["update_log"]            # Brian's update-path test log (Docs)
GONOGO = IDS["gonogo_event_vincent"]      # Vincent's copy of the go/no-go event
H2_MSG = IDS["doc_h2"]                    # Leonard doc, Sep 23: ZM submission rules
H1_MSG = IDS["doc_h1"]                    # Arthur doc, Sep 24: how ZM submission builds are cut
H1_DECOY = IDS["doc_h1_decoy"]            # Arthur doc, Sep 2: 1.3.24 hotfix submissions
H2_DECOY = IDS["doc_h2_decoy"]            # Leonard doc, Jul 27: what blocks a ZM TestFlight beta drop
VENDOR = IDS["gmail_vendor"]              # playtest vendor session notes, Sep 30
CONTACT = IDS["contact_vendor"]
ANNOUNCE = IDS["slack_announce"]          # C08R27X0EAH/<ts> Arthur's candidate post
GREEN = IDS["slack_green"]                # Brian's 'regression green' reply in that thread
PASS133 = IDS["slack_pass133"]            # Vincent's Sep 26 re-test note (#zombie-bugs)
INLINE36 = IDS["review36_inline"]         # Arthur inline review comment on match3d-backend#36 after the rollout: the chest rows are dev-only
DOUG36 = IDS["slack_dm_doug36"]           # Douglas -> Vincent DM: #36 rolled out to prod, code side only (22:01Z)
REVIEW36 = IDS["review36"]                 # Arthur APPROVED review on match3d-backend#36 (GitHub)
DM_DOC = IDS["slack_dm_doc"]              # Brian -> Vincent DM pointing at the update-path doc (no result)
DM_BRIAN = IDS["slack_dm_brian"]          # Brian -> Vincent DM: endless end screen
TRELLO_REUSE = IDS["trello_arthur"]       # Arthur commentCard on 68d1eb90bef538c7c5c5599d
TRELLO_CORR = IDS["trello_leonard"]       # Leonard commentCard on the same card
REL = "ZOM-570"                           # release ticket (Arthur)
SYMPTOM_293 = "cmt_zom293_1"              # Vincent's Jul 3 note on ZOM-293: what goes wrong (lost boosters)
BRIAN29 = IDS["slack_dm_brian29"]         # Brian -> Vincent group DM, Sep 29: ZOM-458 and ZOM-535 are worse than they look
SELF_FILED = "ZOM-581"                    # the update-path bug the run files (rev1 pre-check: opus event 462)
X2, NEUTRAL1, X1 = "ZOM-567", "ZOM-568", "ZOM-569"
NEW_OPEN = [f"ZOM-{n}" for n in range(571, 581)]   # Sep 30 QA-pass tickets; ZOM-578 = Leonard's unlabeled tutorial lock
ART_NEW, DES_NEW, LEO_NEW = "ART-793", "DES-313", "ZOM-578"
BACKEND_PR = "harmonygames-Games/match3d-backend#36"
SETTLE_559 = "cmt_zom559_1"                 # Brian's Sep 28 re-test comment on ZOM-559 (Android Submission #133)

# base anchors / records
RUNBOOK, CHECKLIST, CICD = "page_qa_runbook", "page_release_checklist", "page_cicd_pipeline"
B135 = "C05433XK267/1759263189.219529"         # Android Submission #135 success post (job start 18:45:34Z)
B135_START = "C05433XK267/1759257934.076209"
I50 = "C05433XK267/1759259749.259909"          # iOS Submission #50 success post (job start 18:43:32Z)
B2028 = "C05433XK267/1759268589.049939"        # Android #2028 'Fix season pass main screen instance from join popup'
B107 = "C05433XK267/1756826078.213299"         # Android Submission #107 from release/1.3.24_HotFix (Sep 2)
TF39 = "C08R27X0EAH/1758409417.505029"         # 'testflight 39 is the submission candidate' (Sep 20)
OJ_BLOCKER = "C08R27X0EAH/1758485492.586459"   # Leonard: orange juice 'Submission blocker' (Sep 21)
DOUG_PROD = "D079SNE2TL4/1759256193.859279"    # Douglas: prod updated with teams/social changes (Sep 30 18:16Z)
VINC_OK = "D079SNE2TL4/1759269524.769369"      # Vincent: 'Yep it works as expected' (21:58Z)
TECH_CARD = "68d1eb90bef538c7c5c5599d"         # ZM ROADMAP 'Fix TECH ISSUES'
MINOR_CARD = "68c451141c69fb8af1b4568e"        # ZM ROADMAP 'Minor Bugs to Fix - [Vincent]' (stale list)

# ------------------------------------------------------------------ requirements
REQ = {
    "R1": "Gate scope in the register: one row for every open Zombie Match 3D ticket (the ZOM team in any state or label, plus other teams' tickets with ZM in the title) and every ticket moved to Done since the Sep 22 gate; release tickets and the perf-pass tickets stay out",
    "R2": "Build status column for every ticket moved to Done since the Sep 22 gate: in the Sep 30 candidate builds or not, by the submission build rule",
    "R3": "QA result column: the latest QA result on the candidate builds (or on prod for a server fix), not a developer's fixed note or an older build's pass",
    "R4": "Live status for fixes that need a backend change: live only once deployed to prod; merged (even with an approval) is not live",
    "R5": "Launch call for every register ticket in the call column: blocker, known issue, fixed or no call, by the severity rule and what is true on the candidates (not the Linear state)",
    "R6": "Regression matrix verdict under the runbook update-path rule: a failed update column blocks the release",
    "R7": "Blockers listed on the store release ticket, each by its existing ticket key (reuse, no duplicate tickets)",
    "R8": "QA sign-off posted as a reply in Arthur's #zombie-bugs candidate thread before Friday's go/no-go",
    "R9": "A bug filed for the failed update-path check with device, OS and source build",
    "R10": "Register written as a new tab in Vincent's release gate sheet with the sheet's columns and call vocabulary",
}

SERVICES = {
    "slack": {"role": "candidate builds, re-test reports, sign-off destination",
              "weight_reason": "#builds Submission #135/#50 and #2028 posts decide build membership (R2); the #zombie-bugs candidate thread is the sign-off destination (R8); Brian's DM decides R3 for ZOM-473 and Douglas's DM that #36 is rolled out (code only) is the done source for ZOM-567 (R4)"},
    "linear": {"role": "cohort, per-ticket QA notes, release ticket writes",
               "weight_reason": "every open ZM ticket and every Done-since-gate ticket is a register row (R1); per-ticket comments carry the QA observations that decide the call (R5); the release ticket carries the blocker list (R7) and the filed bug (R9)"},
    "github": {"role": "fix provenance",
               "weight_reason": "match3d PR merge times place each Done fix before or after the 18:43Z cut (R2); match3d-backend#36 shows the chest fix merged with Arthur's approval, and only its inline review comment says the chest rows are still dev-only (R4)"},
    "confluence": {"role": "QA rules (base pages, not injected)",
                   "weight_reason": "the runbook's update-path rule decides R6 and its sign-off channel R8; the checklist decides the filed bug's content R9; the CI/CD page defines a backend deploy as manual (R4)"},
    "gmail": {"role": "external report",
              "weight_reason": "the playtest vendor's Sep 30 session notes are the only record that the boss-arena orphans leave players unable to finish the fight, which escalates ZOM-562 (R5)"},
    "gsheets": {"role": "destination and format",
                "weight_reason": "Vincent's 'ZM3D Release Gate' sheet fixes the register columns and call vocabulary (R10) and is the write target"},
    "gdocs": {"role": "hidden authorities and update-path evidence",
              "weight_reason": "Leonard's Sep 23 rules doc decides scope, verification and severity (R1, R3, R5); Arthur's Sep 24 doc decides build membership and backend liveness (R2, R4); Brian's test log is the only record of the update from the N-1 store build failing on iOS #50 with device and OS (R6, R9)"},
    "gdrive": {"role": "discovery and ownership",
               "weight_reason": "Drive search is how the rule docs and their older look-alikes are found (R1-R5); the gate sheet's Drive row makes Vincent its owner (write access for R10); the test log's Drive row shares it with him"},
    "gcal": {"role": "deadline",
             "weight_reason": "the Friday Oct 3 go/no-go on Vincent's calendar is the deadline the sign-off serves (R8)"},
    "trello": {"role": "reuse instruction and an off-path correction",
               "weight_reason": "Arthur's comment on the ZM tech-issues card sets the reuse rule (R7); Leonard's later comment there is the only record that ZOM-435 is back on #135 (R3)"},
    "contacts": {"role": "identity of the external reporter",
                 "weight_reason": "maps the vendor sender to the ZM playtest vendor, so the session report is a report against the candidate (R5)"},
}

ANCHORS = [
    {"id": "A1", "prompt_reference": "the store release ticket", "service": "linear", "locator": REL,
     "seeded_ids": [REL], "requirement_ids": ["R7"]},
    {"id": "A2", "prompt_reference": "the QA regression runbook", "service": "confluence", "locator": RUNBOOK,
     "base_pointers": [RUNBOOK], "requirement_ids": ["R6", "R8"]},
    {"id": "A3", "prompt_reference": "my release gate sheet", "service": "gsheets", "locator": GATE_SHEET,
     "seeded_ids": [GATE_SHEET], "requirement_ids": ["R10"]},
]


def frag(fid, service, container, kind, via, seeded=None, base=None, by=None, quote=None, reqs=(), names=None):
    f = {"id": fid, "service": service, "container": container, "locator": (seeded or base)[0], "kind": kind,
         "incorporated_via": via, "seeded_ids": list(seeded or []), "base_pointers": list(base or []),
         "delegated_by_record": by, "delegation_quote": quote, "requirement_ids": list(reqs)}
    if names:
        f["names_authorities"] = names
    return f


FRAGMENTS = [
    frag("K1", "gdocs", f"file:{H2_MSG}", "requirement", ["A1"], seeded=[H2_MSG], by=REL,
         quote="Leonard's submission rules", reqs=["R1", "R5"],
         names=[{"id": "H2", "quote": "every ZM ticket that's still open"}]),
    frag("K1b", "gdocs", f"file:{H2_MSG}", "requirement", ["A1"], seeded=[H2_MSG], by=REL,
         quote="Leonard's submission rules", reqs=["R3"]),
    frag("K2", "gdocs", f"file:{H1_MSG}", "requirement", ["A1"], seeded=[H1_MSG], by=REL,
         quote="my note on how we cut submissions", reqs=["R2"],
         names=[{"id": "H1", "quote": "exactly what was on main when its job started"}]),
    frag("K2b", "gdocs", f"file:{H1_MSG}", "requirement", ["A1"], seeded=[H1_MSG], by=REL,
         quote="my note on how we cut submissions", reqs=["R4"]),
    frag("K3", "confluence", f"confluence:{CICD}", "requirement", ["A1", "K2b"], base=[CICD], by=H1_MSG,
         quote="CI/CD page", reqs=["R4"]),
    frag("K4", "confluence", f"confluence:{CHECKLIST}", "format", ["A2"], base=[CHECKLIST], by=RUNBOOK,
         quote="tick the QA sign-off on the", reqs=["R9"]),
    frag("K6", "gsheets", f"file:{GATE_SHEET}", "format", ["A3"], seeded=[GATE_SHEET], by=GATE_SHEET,
         quote="How we gate", reqs=["R10"]),
    frag("K7", "gcal", f"gcal:{IDS['gonogo_ical']}", "deadline", ["A1"], seeded=[GONOGO], by=REL,
         quote="go/no-go on Friday", reqs=["R8"]),
    frag("K8", "trello", f"trello:{TECH_CARD}", "reuse", ["A1"], seeded=[TRELLO_REUSE], by=REL,
         quote="tech-issues card", reqs=["R7"]),
    frag("K9", "slack", f"slack:{ANNOUNCE}", "destination", ["A1"], seeded=[ANNOUNCE], by=REL,
         quote="post the candidates in #zombie-bugs", reqs=["R8"]),
    frag("K10", "linear", f"linear:{REL}#comment", "amendment", ["A1"], seeded=[IDS["linear_leonard_comment"]], by=REL,
         quote="push notes go in the comments here", reqs=["R8"]),
    frag("K11", "slack", f"slack:{OJ_BLOCKER}", "requirement", ["A1", "K1"], base=[OJ_BLOCKER], by=H2_MSG,
         quote="like the orange juice one", reqs=["R5"]),
]
# K10's own container is the release ticket's comment thread: keep it distinct from the ticket key for the count,
# but the hardness_v2 container key is linear:ZOM-570 (an anchor container) — a destination amendment meant to be read.
FRAGMENTS[9]["container"] = f"linear:{REL}"

AUTHORITIES = [
    {"id": "H1", "name": "Arthur's submission build rules", "home_service": "gdocs", "decoy_service": "gdocs",
     "governs": ["R2", "R4"], "findable_query": "submission builds", "seeded_ids": [H1_MSG],
     "decoy_seeded_ids": [H1_DECOY]},
    {"id": "H2", "name": "Leonard's ZM submission rules", "home_service": "gdocs", "decoy_service": "gdocs",
     "governs": ["R1", "R3", "R5"], "findable_query": "submission rules", "seeded_ids": [H2_MSG],
     "decoy_seeded_ids": [H2_DECOY],
     "decoy_scope": {"dimension": "lot", "decoy": "ZM TestFlight beta drops",
                     "task": "ZM store submission builds"}},
]

OPEN_BASE = 99 + 2          # ZOM open at the clock + ART-790/ART-792 (ZM marketing art)
OPEN_NEW = 1 + len(NEW_OPEN) + 2   # ZOM-568, ZOM-571..580, ART-793, DES-313
DONE_SINCE = 18 + 2         # base Done since 2025-09-22T12:30Z + ZOM-567, ZOM-569
COHORT = OPEN_BASE + OPEN_NEW + DONE_SINCE - 2   # ZOM-359 / ZOM-475 perf exclusions stay out

COHORT_SPEC = {
    "definition_source": "K1", "key": "ticket id", "size": COHORT,
    "evidence_surfaces": [
        {"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1.0, "records": COHORT, "seeded": True,
         "seeded_ids": [X2, NEUTRAL1, X1, REL] + NEW_OPEN + [ART_NEW, DES_NEW],
         "why_no_bulk": "linear_list_issues returns state, labels and a truncated description but never comments; the QA observations that decide the call live only in each ticket's comments (Ask_Carriers §6b)",
         "short_circuit": "labels and state never decide the call: a VFX- or Improvement-labelled ticket can carry a freeze in its comments and a Bug-labelled one can be cosmetic, so a run that skips a ticket's comments mis-calls the unpredictable subset; no filtered search returns comment text",
         "requirement": "R5", "decides": "call column"},
        {"service": "github", "tool": "github_get_pull_request", "per_record_calls": 0.75, "records": DONE_SINCE,
         "seeded": True, "seeded_ids": [BACKEND_PR],
         "why_no_bulk": "PR search returns merged_at only for PRs whose title or branch names the ticket; half the Done fixes are PRs without the key or direct commits, so each Done ticket's fix has to be traced (branch, PR body, #builds change line) one ticket at a time",
         "short_circuit": "the ticket's Done state never decides build status: a fix merged after the 18:43Z cut or only in the backend repo is not in the candidate builds, so the trace is needed even when the ticket is Done",
         "requirement": "R2", "decides": "Build status column"},
        {"service": "slack", "tool": "slack_conversations_search_messages", "per_record_calls": 0.1, "records": COHORT,
         "seeded": True, "seeded_ids": [PASS133, DM_BRIAN],
         "why_no_bulk": "re-test reports are spread over #zombie-bugs threads, DMs and #zombie-ops; a channel sweep returns them but not which ticket each refers to, so each ticket's latest result must be matched (counted at 0.1 per ticket: the sweep pages are shared)",
         "short_circuit": "a developer's fixed note or Done state never decides the QA result column; the latest re-test on the candidate does",
         "requirement": "R3", "decides": "QA result column"},
    ],
}


def vrec(service, rid, at, seeded, container=None):
    v = {"service": service, ("id" if seeded else "base_pointer"): rid, "seeded": seeded, "at": at}
    if container:
        v["container"] = container
    return v


TRAPS = [
    {"id": "T1", "family": "done_gap", "services": ["linear", "slack", "gdocs"], "seeded_ids": [X1], "base_pointers": [B2028, B135_START],
     "requirement": "R2", "expected_wrong_reading": "ZOM-569 was closed at 18:05Z, before both jobs started, with Oliver's 'fixed' note, so the fix ships in #135/#50",
     "resolver": "H1: a submission has exactly what was on main when its job started; Oliver fixed it on his branch, and the change only reaches main in Android #2028 / iOS Internal #1759 (21:36Z), after both jobs started (18:43Z/18:45Z); How we gate goes by the close time only when nothing shows when the fix landed",
     "discovery_order": "the Done state, the pre-cut close time and the fix note are on the ticket; when the fix landed on main is only in #builds (and GitHub's commit list); PR #473 'Addressables/sp' (merged 15:41Z) is season-pass work that does not fix it"},
    {"id": "T2", "family": "done_gap", "services": ["linear", "github", "slack", "confluence"], "seeded_ids": [X2, BACKEND_PR, REVIEW36, INLINE36, DOUG36], "base_pointers": [CICD],
     "requirement": "R4", "expected_wrong_reading": "ZOM-567 is Done, match3d-backend#36 is approved and merged, and Douglas says #36 is rolled out to prod, so players get their chests (fixed, not re-checked)",
     "resolver": "Arthur's inline review comment on #36 (22:35Z, after Douglas's rollout): he claimed a chest on his prod account and nothing landed; the migration only creates the empty zombie_lane_chest_rows table, and the rows the grant reads come from the PR's load script, which runs by hand per environment and hasn't been run on prod (he is holding it until after the store push); so part of the fix isn't on prod (How we gate: server - not live, 'any part not on prod yet, even if its code is deployed'; H1: merged is not live) and the chests still don't land",
     "discovery_order": "the Done ticket, the approved merged PR and Douglas's 'rolled out' DM are met first; the missing piece is only in the PR's inline review comment (match3d-backend has no Slack mirror)",
     "version_records": [vrec("linear", X2, "2025-09-30T19:00:00Z", True, f"linear:{X2}"),
                         vrec("slack", DOUG36, "2025-09-30T22:01:52Z", True, "slack:D079SNE2TL4"),
                         vrec("github", INLINE36, "2025-09-30T22:35:00Z", True, f"github:{BACKEND_PR}")]},
    {"id": "T3", "family": "superseding", "services": ["linear", "slack", "trello"], "seeded_ids": [PASS133, TRELLO_CORR], "base_pointers": ["ZOM-435"],
     "requirement": "R3", "expected_wrong_reading": "ZOM-435 is Done and passed Vincent's #133 re-test, so it ships fixed",
     "resolver": "H2: the latest QA result on the candidate counts; Leonard's Sep 30 Trello comment reproduces the trophy-path lock on #135",
     "discovery_order": "the Done ticket and the #zombie-bugs pass are on the obvious path; the re-test on #135 is a comment on a roadmap card",
     "version_records": [vrec("linear", "ZOM-435", "2025-07-25T00:00:00Z", False, "linear:ZOM-435"),
                         vrec("slack", PASS133, "2025-09-29T10:05:00Z", True, f"slack:{PASS133}"),
                         vrec("trello", TRELLO_CORR, "2025-09-30T23:10:00Z", True, f"trello:{TECH_CARD}")]},
    {"id": "T3b", "family": "superseding", "services": ["linear", "slack"], "seeded_ids": [DM_BRIAN], "base_pointers": ["ZOM-473"],
     "requirement": "R3", "expected_wrong_reading": "ZOM-473 is Done (Sep 22), so the endless end screen ships fixed",
     "resolver": "H2: Brian's re-test on iOS #50 (DM, Sep 30) shows the end screen can still be tapped away",
     "discovery_order": "the Done state is in the list view; the re-test is in a DM",
     "version_records": [vrec("linear", "ZOM-473", "2025-08-14T08:24:51Z", False, "linear:ZOM-473"),
                         vrec("slack", DM_BRIAN, "2025-09-30T21:30:00Z", True, f"slack:{DM_BRIAN}")]},
    {"id": "T4", "family": "authority", "services": ["gdocs", "slack", "confluence", "gsheets"], "seeded_ids": [UPDATE_LOG, GREEN], "base_pointers": [RUNBOOK],
     "requirement": "R6", "expected_wrong_reading": "Brian's 'regression green' reply and the passing fresh-install and N-1 rows clear the gate",
     "resolver": "the runbook: both update rows are mandatory and a failure in any UPDATE column blocks; the test log's update from the N-1 store build to iOS #50 resets progress",
     "discovery_order": "the green summary is in the sign-off thread every run reads; the failing row is in Brian's test log"},
    {"id": "T5", "family": "scope_alias", "services": ["gmail", "contacts", "linear"], "seeded_ids": [VENDOR, CONTACT], "base_pointers": ["ZOM-562"],
     "requirement": "R5", "expected_wrong_reading": "the vendor's 'Puzzles vs Zombies' boss-fight report is a new or unrelated issue, and ZOM-562 (orphan items after refill) is cosmetic",
     "resolver": "the report's boss-arena refill leaving single items that never form a set is ZOM-562; the player could not finish and lost a life, so H2 makes it a blocker",
     "discovery_order": "ZOM-562's own text reads as cosmetic; the consequence is only in an external sender's mail under the game's old name"},
    {"id": "T6", "family": "exact_predicate", "services": ["linear", "gdocs"], "seeded_ids": [ART_NEW, DES_NEW, LEO_NEW],
     "requirement": "R1", "expected_wrong_reading": "the gate covers ZOM-team tickets labelled Bug",
     "resolver": "H2: every ZM ticket still open (any state but Done, Canceled or Duplicate) whatever team or label; ART-793 and DES-313 are ZM defects in other teams and ZOM-578 has no label",
     "discovery_order": "the obvious filter is team ZOM + label Bug"},
    {"id": "T7", "family": "completion_elsewhere", "services": ["linear", "slack"], "base_pointers": ["ZOM-563", DOUG_PROD, VINC_OK],
     "requirement": "R3", "expected_wrong_reading": "ZOM-563 is still In Progress and its lives/frames symptom on prod makes it a blocker",
     "resolver": "H2 (server fixes count once QA confirms on prod after the deploy): Douglas updated prod at 18:16Z and Vincent confirmed it works at 21:58Z in their DM",
     "discovery_order": "the ticket state is open; the confirmation is in a DM"},
    {"id": "T8", "family": "superseding", "services": ["gdocs", "slack"], "seeded_ids": [H1_DECOY, H1_MSG], "base_pointers": [B107],
     "requirement": "R2", "expected_wrong_reading": "submissions are built from a release branch, so main commits before the cut may not be in #135",
     "resolver": "Arthur's Sep 24 doc: since the hotfix train ended every ZM store submission is cut straight from main",
     "discovery_order": "the Sep 2 doc matches the same Drive search and the release-branch submissions in #builds are met in history first",
     "version_records": [vrec("slack", B107, "2025-09-02T15:14:38Z", False, "slack:C05433XK267"),
                         vrec("gdocs", H1_DECOY, "2025-09-02T15:40:00Z", True, f"file:{H1_DECOY}"),
                         vrec("gdocs", H1_MSG, "2025-09-24T14:20:00Z", True, f"file:{H1_MSG}")]},
    {"id": "T9", "family": "distractor", "distractor_type": "lookalike_entity", "services": ["slack", "linear"], "seeded_ids": [REL], "base_pointers": [TF39],
     "requirement": "R2", "expected_wrong_reading": "the submission candidate is TestFlight 39 (the last 'submission candidate' post)",
     "resolver": "the release ticket names Android Submission #135 and iOS Submission #50",
     "discovery_order": "a search for 'submission candidate' returns the Sep 20 post first"},
    {"id": "T10", "family": "distractor", "distractor_type": "stale_summary", "services": ["slack"], "seeded_ids": [GREEN],
     "requirement": "R6", "expected_wrong_reading": "regression is green, good to go", "resolver": "the runbook update-path rule and the test log",
     "discovery_order": "the summary is a reply in the sign-off thread"},
    {"id": "T11", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["gdocs"], "seeded_ids": [H2_DECOY],
     "requirement": "R5", "expected_wrong_reading": "only crashes and progress wipes block (the July beta-drop rule)",
     "resolver": "H2 governs store submission builds; the July note covers TestFlight beta drops only"},
    {"id": "T12", "family": "superseding", "services": ["gsheets", "linear"], "seeded_ids": [GATE_SHEET, SETTLE_559], "base_pointers": ["ZOM-559"],
     "requirement": "R5", "expected_wrong_reading": "carry the Sep 22 tab's calls forward (ZOM-559 known issue)",
     "resolver": "each call is made on the current evidence; Brian's Sep 29 re-test on Android Submission #133 records the victory screen freezing, which H2 makes a blocker",
     "discovery_order": "the previous gate tab is the first tab of the destination sheet; the re-test is a comment on the ticket",
     "version_records": [vrec("gsheets", GATE_SHEET, "2025-09-22T17:05:00Z", True, f"file:{GATE_SHEET}"),
                         vrec("linear", SETTLE_559, "2025-09-29T15:20:00Z", True, "linear:ZOM-559")]},
    {"id": "T13", "family": "distractor", "distractor_type": "keyword_collision", "services": ["linear"], "base_pointers": ["ZOM-516"],
     "requirement": "R5", "expected_wrong_reading": "the refill report maps to ZOM-516 (endless mode refills one item less)",
     "resolver": "ZOM-516 is a closed Duplicate about endless mode; the report is boss arena orphan items (ZOM-562)"},
    {"id": "T14", "family": "distractor", "distractor_type": "partial_listing", "services": ["trello"], "base_pointers": [MINOR_CARD],
     "requirement": "R1", "expected_wrong_reading": "the 'Minor Bugs to Fix' card is the list to gate",
     "resolver": "H2's scope is every open ZM ticket; the card is a September to-do list"},
    {"id": "T15", "family": "distractor", "distractor_type": "already_done", "services": ["linear", "github"], "base_pointers": ["ZOM-564", "harmonygames-Games/match3d#466"],
     "requirement": "R3", "expected_wrong_reading": "ZOM-564 is Todo, so the free label still eats boosters",
     "resolver": "PR #466 (merged Sep 26) is in the candidates and Brian's re-test on iOS #50 is on the ticket"},
    {"id": "T16", "family": "cross_reference_gap", "services": ["linear", "slack", "gdocs"], "seeded_ids": [BRIAN29, "cmt_zom458_1", "cmt_zom535_1"], "base_pointers": ["ZOM-458", "ZOM-535"],
     "requirement": "R5", "expected_wrong_reading": "ZOM-458 is a wrong animation and ZOM-535 a fast-matching inefficiency, both still there on #135 / #50: known issues",
     "resolver": "H2 ('call it on how bad it is whatever the ticket says'): Brian's Sep 29 check on #133 / #49 (D0770ET1HV2) shows ZOM-458 marks the quit level passed and its chest claimed with nothing in the inventory (lost items) and ZOM-535 leaves the boss arena unfinishable (can't finish a level); Vincent's #135 / #50 notes confirm both still happen 'same as Brian found', so both are blockers",
     "discovery_order": "the tickets' own text and Vincent's Sep 30 notes read like the cosmetic symptom; how bad it is sits only in an older message of the QA group DM, outside the post-candidate window"},
    {"id": "T17", "family": "exact_predicate", "services": ["linear", "gdocs"], "seeded_ids": [SYMPTOM_293], "base_pointers": ["ZOM-293"],
     "requirement": "R5", "expected_wrong_reading": "ZOM-293's description is just 'Dynamic Difficulty Tiering' and it carries no Bug label, so it doesn't say what goes wrong: no call",
     "resolver": "H2 (lost boosters / coins = blocker; 'a ticket that doesn't say what goes wrong' is no call): the reporter's own Jul 3 comment says what goes wrong, the pre-level boosters picked for the retry are charged and gone after the tier-change reload, so it is a blocker (build status n/a: open, nobody re-tested)",
     "discovery_order": "the list view and the issue read show a bare description; what goes wrong is only in the ticket's comments, which a run that reads comments only on bug-looking tickets never opens"},
]

CHAINS = [
    {"id": "CH1", "root_cause": "A24", "ends_in": "R2", "hops": [
        {"service": "linear", "record": X1, "finding": "closed at 18:05Z with a fixed-on-my-branch note"},
        {"service": "slack", "record": B135_START, "finding": "Android Submission #135 job started 18:45:34Z"},
        {"service": "slack", "record": B2028, "finding": "the season pass fix lands in Android #2028 at 21:36Z"},
        {"service": "gdocs", "record": H1_MSG, "finding": "a submission has what was on main when its job started"}]},
    {"id": "CH2", "root_cause": "A11", "ends_in": "R3", "hops": [
        {"service": "linear", "record": "ZOM-435", "finding": "Done Sep 22 with Oliver's fix note"},
        {"service": "slack", "record": PASS133, "finding": "Vincent's pass on Submission #133"},
        {"service": "trello", "record": TRELLO_CORR, "finding": "Leonard reproduces the trophy-path lock on #135"}]},
    {"id": "CH3", "root_cause": "A15", "ends_in": "R6", "hops": [
        {"service": "slack", "record": GREEN, "finding": "Brian calls regression green"},
        {"service": "gdocs", "record": UPDATE_LOG, "finding": "update from the N-1 store build to iOS #50 resets progress"},
        {"service": "confluence", "record": RUNBOOK, "finding": "any failed update column blocks"}]},
    {"id": "CH4", "root_cause": "A7", "ends_in": "R5", "hops": [
        {"service": "gmail", "record": VENDOR, "finding": "boss fight stuck after refill, life lost (Puzzles vs Zombies)"},
        {"service": "contacts", "record": CONTACT, "finding": "sender is the ZM playtest vendor"},
        {"service": "linear", "record": "ZOM-562", "finding": "orphan items after refill"}]},
    {"id": "CH5", "root_cause": "A25", "ends_in": "R3", "hops": [
        {"service": "linear", "record": "ZOM-563", "finding": "In Progress: works on dev, not prod"},
        {"service": "slack", "record": DOUG_PROD, "finding": "Douglas updates prod with the teams/social changes"},
        {"service": "slack", "record": VINC_OK, "finding": "Vincent confirms it works"}]},
    {"id": "CH6", "root_cause": "A17", "ends_in": "R1", "hops": [
        {"service": "linear", "record": ART_NEW, "finding": "ZM defect filed in the ART team"},
        {"service": "linear", "record": DES_NEW, "finding": "ZM defect filed in the DES team"},
        {"service": "gdocs", "record": H2_MSG, "finding": "every ZM ticket that's still open, whatever team or label"}]},
]

PORTFOLIO = [
    {"id": "R_DONE_BUILD", "mechanism": "A24", "prior_family": "A24", "prior_family_reason": "same mechanism id; no Opus 5.5 ledger record yet (Beta(1,1), UNCALIBRATED)",
     "nodes": ["T1", "CH1"], "requirement": "R2", "natural_reading": "a Done ticket with a merged fix is in the candidate builds",
     "decides": ["Build status column", "call column"], "source": "build-cut", "signature": "fix-after-job-start",
     "controls": ["ZOM-506", "ZOM-557", "ZOM-561"], "over_application": "over:every-done-not-in-build"},
    {"id": "R_DONE_SERVER", "mechanism": "A24", "prior_family": "A24", "prior_family_reason": "same mechanism id (done source vs missing deploy); no Opus 5.5 record yet",
     "nodes": ["T2"], "requirement": "R4", "natural_reading": "an approved, merged backend PR = live",
     "decides": ["call column"], "source": "backend-deploy", "signature": "merged-not-deployed",
     "controls": ["ZOM-563", "ZOM-503"], "over_application": "over:every-server-fix-not-live"},
    {"id": "R_CORRECTION", "mechanism": "A11", "prior_family": "wrong summary + thread past its conclusion (A1)",
     "prior_family_reason": "closest library family with Opus 5.5 records: a claim met first and overturned by a later record elsewhere (hev_0e23d0e0b6b029a5, hev_e0e5f73b1cee8d3d, hev_6b560d035cdf9211); differs in that the overturning record is a re-test in another service",
     "nodes": ["T3", "T3b", "CH2"], "requirement": "R3", "natural_reading": "Done (and an older pass) = fixed",
     "decides": ["QA result column", "call column"], "source": "retests", "signature": "latest-retest-on-candidate",
     "controls": ["ZOM-506", "ZOM-557"], "over_application": "over:every-done-came-back"},
    {"id": "R_ALIAS", "mechanism": "A7", "prior_family": "A7", "prior_family_reason": "same mechanism id (scope/alias boundary; hev_83d7b0972f87a2ec)",
     "nodes": ["T5", "CH4"], "requirement": "R5", "natural_reading": "ZOM-562 is cosmetic; the vendor report is unrelated or a new ticket",
     "decides": ["call column", "blocker list"], "source": "vendor-report", "signature": "boss-arena-orphans",
     "controls": ["ZOM-546", "ZOM-504"], "over_application": "over:map-every-refill-report-to-562"},
    {"id": "R_FILTER", "mechanism": "A17", "prior_family": "A17", "prior_family_reason": "same mechanism id (cohort boundary; hev_971c5e5fdb2d2c1a)",
     "nodes": ["T6", "CH6"], "requirement": "R1", "natural_reading": "scope = team ZOM, label Bug",
     "decides": ["register rows", "call column"], "source": "scope-rule", "signature": "any-team-any-label",
     "controls": ["ZOM-565", "ZOM-566", "ART-790"], "over_application": "over:every-non-bug-is-defect"},
    {"id": "R_COMPLETION", "mechanism": "A25", "prior_family": "A25", "prior_family_reason": "same mechanism id; no Opus 5.5 ledger record yet (Beta(1,1), UNCALIBRATED)",
     "nodes": ["T7", "CH5"], "requirement": "R3", "natural_reading": "an open ticket is still broken",
     "decides": ["QA result column", "call column"], "source": "server-confirm", "signature": "confirmed-on-prod",
     "controls": ["ZOM-534", "ZOM-544"], "over_application": "over:every-in-progress-ships"},
    {"id": "R_OLD_NOTE", "mechanism": "A14", "prior_family": "A14",
     "prior_family_reason": "same mechanism id (history outside the window the run reads; hev_ee2fa6cd86df8050, hev_0aea2ae9c00e83c2; UNCALIBRATED)",
     "nodes": ["T16"], "requirement": "R5", "natural_reading": "a ticket whose text and latest check read cosmetic is a known issue",
     "decides": ["call column", "blocker list"], "source": "older-dm", "signature": "worse-than-it-looks",
     "controls": ["ZOM-481", "ZOM-427"], "over_application": "over:every-cosmetic-is-worse"},
    {"id": "R_SYMPTOM_NOTE", "mechanism": "A17", "prior_family": "A17",
     "prior_family_reason": "same mechanism id (an in-scope item outside the obvious filter; hev_95fae459cc9d282a, hev_971c5e5fdb2d2c1a; UNCALIBRATED)",
     "nodes": ["T17"], "requirement": "R5", "natural_reading": "a ticket whose description doesn't say what goes wrong is no call",
     "decides": ["call column", "blocker list"], "source": "reporter-note", "signature": "what-goes-wrong-in-a-comment",
     "controls": ["ZOM-311", "ZOM-130"], "over_application": "over:every-vague-ticket-is-a-bug"},
]

WRITES = [
    {"service": "gsheets", "tool": "gsheets_values_update", "count": 1, "depends_on": ["R_DONE_BUILD", "R_DONE_SERVER", "R_CORRECTION", "R_ALIAS", "R_FILTER", "R_COMPLETION", "K1", "K6"],
     "requirements": ["R1", "R2", "R3", "R4", "R5", "R10"]},
    {"service": "linear", "tool": "linear_update_issue", "count": 1, "depends_on": ["R_DONE_BUILD", "R_DONE_SERVER", "R_CORRECTION", "R_ALIAS", "R_FILTER", "K8"],
     "requirements": ["R7"]},
    {"service": "linear", "tool": "linear_create_issue", "count": 1, "depends_on": ["T4", "K4"], "requirements": ["R6", "R9"]},
    {"service": "slack", "tool": "slack_send_message", "count": 1, "depends_on": ["T4", "K9", "K10"], "requirements": ["R8"]},
]


def B(phase, service, calls, reason):
    return {"phase": phase, "service": service, "calls": calls, "reason": reason}


BUDGET = [
    B("discovery", "linear", 3, "open the release ticket, its comments (Leonard's push notes) and its description history"),
    B("discovery", "slack", 3, "find Arthur's candidate post in #zombie-bugs and read its thread (destination, Brian's summary)"),
    B("discovery", "confluence", 6, "read the runbook, the release checklist and the CI/CD page the rules point to, plus the runbook's and checklist's comments"),
    B("rules", "gdrive", 2, "search Drive for the rule docs ZOM-570 names; the same searches return the two older look-alike docs"),
    B("rules", "gdocs", 4, "read Leonard's and Arthur's rule docs and the two older look-alike docs, one read each"),
    B("rules", "gmail", 1, "read the playtest vendor's session notes"),
    B("rules", "gsheets", 3, "read the gate sheet's metadata, its 'How we gate' tab and the Sep 22 tab"),
    B("rules", "gdrive", 2, "locate the gate sheet and the test log by title and confirm the owner"),
    B("rules", "gcal", 2, "find the go/no-go event and read its time"),
    B("rules", "trello", 3, "read the tech-issues card and its comments, and the minor-bugs card it sits beside"),
    B("rules", "contacts", 2, "look up the vendor sender of the session report"),
    B("rules", "gdocs", 1, "read Brian's update-path test log"),
    B("enumeration", "linear", 8, "list open ZOM issues (~110, 2 pages), Done since Sep 22, the ZM project view across teams, and ART/DES open issues"),
    B("enumeration", "slack", 26, "page #builds Sep 22-30 (~450 Jenkins posts, 9 pages), #zombie-bugs Sep 22-30 (~450, 9 pages), #zombie-match3d (3), #zombie-ops (1), the Brian and Douglas DMs (2) and the two bug canvases' channels (2) for re-test reports"),
    B("enumeration", "github", 4, "list match3d PRs merged Sep 22-30 and the backend repo's recent PRs"),
    B("enumeration", "gmail", 3, "search the mailbox for session reports and build notices since Sep 22"),
    B("per-record", "linear", COHORT, "one linear_list_comments per register ticket: the QA observation deciding the call lives only in comments"),
    B("per-record", "github", 15, "trace the fix of each Done-since-gate ticket whose PR does not name it (branch, PR body, backend PR)"),
    B("per-record", "slack", 13, "match re-test reports to tickets (thread reads beyond the shared sweep pages)"),
    B("reconciliation", "github", 3, "read the post-cut commit (a61cb2b9, #2028) and match3d-backend#36's merge state"),
    B("reconciliation", "linear", 3, "check the existing tickets the vendor report and the filter members map to before writing"),
    B("reconciliation", "slack", 3, "open the full change lists of Android Submission #135, iOS Submission #50 and Android #2028 (attachment text) to place each Done fix before or after the cut"),
    B("writes", "gsheets", 3, "add the gate tab and write the register (two value updates)"),
    B("writes", "linear", 2, "update the release ticket's blocker list and create the update-path bug"),
    B("writes", "slack", 1, "reply in Arthur's candidate thread with the QA call"),
    B("read-back", "gsheets", 1, "read the register back"),
    B("read-back", "linear", 2, "read the release ticket and the new bug back"),
]


def build_manifest() -> dict:
    return {
        "assignment_context": {k: CTX[k] for k in ("context_hash", "assignment_hash", "policy_hash", "freeze_utc", "difficulty_mode")},
        "persona": "vincent_parker",
        "horizon": "Long Horizon",
        "effective_profile": "extreme",
        "volume_exception": {
            "reason": "Honest necessary calls top out near 260 (about 155 per record): only Linear comments are a per-record surface here (GitHub reviews and comments are mirrored to #zombie-prs, Slack threads are search-sweepable, closed tickets take no new comments), and the widest natural gate scope is every open ZM ticket plus everything Done since the Sep 22 gate (~139 tickets). Reaching 500/300 would need padding, a failing error.",
            "requester_confirmation": "The requester (task owner) chose floors 250 / 150 with the widest scope in this session on 2026-11-04 ('go with this'), after first confirming 280 / 170 on 2026-11-04 and being shown that 280 / 170 is unreachable without padding",
            "call_budget_floor": 250, "per_record_floor": 150},
        "requirements": REQ,
        "services": SERVICES,
        "anchors": ANCHORS,
        "ask_fragments": FRAGMENTS,
        "authorities": AUTHORITIES,
        "cohort": COHORT_SPEC,
        "chains": CHAINS,
        "traps": TRAPS,
        "call_budget": BUDGET,
        "writes": WRITES,
        "mechanism_portfolio": PORTFOLIO,
        "gradable_surface": {"path": "01_Gradable_Surface.json"},
    }


# ------------------------------------------------------------------ gradable surface
def slot(sid, title, w, kind, reason, cls, role, sel, fact, mech=None, group=None, by=None, **kw):
    s = {"id": sid, "title": title, "weight": w, "work_kind": kind, "work_reason": reason, "class": cls, "role": role,
         "selector": sel, "fact_id": fact}
    if group:
        s["group"] = group
    if mech:
        s["mechanisms"] = mech
    if by:
        s["singled_out_by"] = by
    s.update(kw)
    return s


MSR = "multi_source_reconciliation"
SLOTS = [
    slot("S01", "ZOM-569 call", 5, MSR, "the Done state, the fix commit's time in #builds, both candidate job starts and Arthur's build rule must be reconciled", "direct", "exception", ["field", X1, "call"], f"{X1}.call", ["R_DONE_BUILD"], "exception", "H1"),
    slot("T01", "Release ticket lists ZOM-569 as a blocker", 5, MSR, "the same reconciliation decides the blocker list write", "write_content", "exception", ["tracker_lists", "blocker", X1], f"{X1}.call", ["R_DONE_BUILD"], "blockers", "H1"),
    slot("S03", "ZOM-567 call", 5, MSR, "the Done ticket, the approved and merged backend PR, Douglas's rollout DM, Arthur's inline review comment and the How we gate server definitions must be reconciled", "direct", "exception", ["field", X2, "call"], f"{X2}.call", ["R_DONE_SERVER"], "exception", "H1"),
    slot("T02", "Release ticket lists ZOM-567 as a blocker", 5, MSR, "the same reconciliation decides the blocker list write", "write_content", "exception", ["tracker_lists", "blocker", X2], f"{X2}.call", ["R_DONE_SERVER"], "blockers", "H1"),
    slot("S05", "ZOM-435 call", 5, MSR, "the Done ticket, the #133 pass and Leonard's #135 re-test on Trello must be ordered and weighed under Leonard's rule", "direct", "exception", ["field", "ZOM-435", "call"], "ZOM-435.call", ["R_CORRECTION"], "exception", "H2"),
    slot("T03", "Release ticket lists ZOM-435 as a blocker", 5, MSR, "the same reconciliation decides the blocker list write", "write_content", "exception", ["tracker_lists", "blocker", "ZOM-435"], "ZOM-435.call", ["R_CORRECTION"], "blockers", "H2"),
    slot("S07", "ZOM-473 call", 5, MSR, "the Done ticket and Brian's iOS #50 re-test in a DM must be reconciled, then the severity rule applied", "direct", "exception", ["field", "ZOM-473", "call"], "ZOM-473.call", ["R_CORRECTION"], "exception", "H2"),
    slot("T05", "Release ticket lists ZOM-473 as a blocker", 5, MSR, "the same reconciliation (Brian's iOS #50 re-test in the Turkish DM against the Done ticket) decides the blocker list write", "write_content", "exception", ["tracker_lists", "blocker", "ZOM-473"], "ZOM-473.call", ["R_CORRECTION"], "blockers", "H2"),
    slot("B01", "Filed bug covers the update from the N-1 store build to iOS Submission #50", 5, MSR, "the test log's failing row, the runbook's update rule and the checklist's bug-content rule must be combined", "write_content", "core", ["text", "newbug", "N-1|0\\.3\\.49|1\\.3\\.49|store (build|version)|App Store"], "updatepath.bug"),
    slot("S09", "ZOM-562 call", 5, MSR, "an external report under the old game name must be mapped to ZOM-562 and the consequence weighed under the severity rule", "direct", "exception", ["field", "ZOM-562", "call"], "ZOM-562.call", ["R_ALIAS"], "exception", "H2"),
    slot("T04", "Release ticket lists ZOM-562 as a blocker", 5, MSR, "the alias mapping decides which existing ticket the blocker list reuses", "write_content", "exception", ["tracker_lists", "blocker", "ZOM-562"], "ZOM-562.call", ["R_ALIAS"], "blockers", "H2"),
    slot("S11", "ART-793 call", 5, MSR, "a ZM defect in the ART team is brought into scope by Leonard's rule and called by its report", "direct", "exception", ["field", ART_NEW, "call"], f"{ART_NEW}.call", ["R_FILTER"], "exception", "H2"),
    slot("S12", "DES-313 call", 5, MSR, "a ZM defect in the DES team is brought into scope by Leonard's rule and called by its report", "direct", "exception", ["field", DES_NEW, "call"], f"{DES_NEW}.call", ["R_FILTER"], "exception", "H2"),
    slot("S13", "ZOM-578 call", 5, MSR, "an unlabeled ZOM ticket outside the Bug view is brought into scope and called by its report", "direct", "exception", ["field", LEO_NEW, "call"], f"{LEO_NEW}.call", ["R_FILTER"], "exception", "H2"),
    slot("S14", "ZOM-563 call", 5, MSR, "the open ticket, Douglas's prod deploy and Vincent's confirmation in a DM must be reconciled", "direct", "exception", ["field", "ZOM-563", "call"], "ZOM-563.call", ["R_COMPLETION"], "exception", "H2"),
    slot("S31", "ZOM-458 call", 5, MSR, "the ticket's cosmetic text and Vincent's #135 note are read with Brian's older #133 check in the QA group DM and called on how bad it is", "direct", "exception", ["field", "ZOM-458", "call"], "ZOM-458.call", ["R_OLD_NOTE"], "exception", "H2"),
    slot("T06", "Release ticket lists ZOM-458 as a blocker", 5, MSR, "the same reconciliation decides the blocker list write", "write_content", "exception", ["tracker_lists", "blocker", "ZOM-458"], "ZOM-458.call", ["R_OLD_NOTE"], "blockers", "H2"),
    slot("S32", "ZOM-535 call", 5, MSR, "the ticket's matching-inefficiency text and Vincent's #135 note are read with Brian's older boss-arena check and called on how bad it is", "direct", "exception", ["field", "ZOM-535", "call"], "ZOM-535.call", ["R_OLD_NOTE"], "exception", "H2"),
    slot("T08", "Release ticket lists ZOM-535 as a blocker", 5, MSR, "the same reconciliation decides the blocker list write", "write_content", "exception", ["tracker_lists", "blocker", "ZOM-535"], "ZOM-535.call", ["R_OLD_NOTE"], "blockers", "H2"),
    slot("S30", "ZOM-293 call", 5, MSR, "a bare ticket outside the Bug view is read with its reporter's note on what goes wrong and called under the severity rule", "direct", "exception", ["field", "ZOM-293", "call"], "ZOM-293.call", ["R_SYMPTOM_NOTE"], "exception", "H2"),
    slot("T07", "Release ticket lists ZOM-293 as a blocker", 5, MSR, "the same reading decides the blocker list write", "write_content", "exception", ["tracker_lists", "blocker", "ZOM-293"], "ZOM-293.call", ["R_SYMPTOM_NOTE"], "blockers", "H2"),
    slot("S20", "ZOM-559 call", 3, "interpretation", "the ticket's own report (hard freeze at the victory screen) is read against the severity rule", "direct", "sample", ["field", "ZOM-559", "call"], "ZOM-559.call", group="open"),
    slot("S21", "ZOM-560 call", 3, "interpretation", "a purchased pack's missing reward is read against the severity rule", "direct", "sample", ["field", "ZOM-560", "call"], "ZOM-560.call", group="open"),
    slot("S22", "ZOM-481 call", 3, "interpretation", "the QA observation in the comments (a lingering health bar, play unaffected) is read against the severity rule", "direct", "sample", ["field", "ZOM-481", "call"], "ZOM-481.call", group="open"),
    slot("S24", "ZOM-564 call", 3, "limited_reconciliation", "the merged PR and the re-test note on the ticket are reconciled with its Todo state", "direct", "sample", ["field", "ZOM-564", "call"], "ZOM-564.call", group="open"),
    slot("S25", "ZOM-506 call", 3, "comparison", "the fix commit in PR #471 (merged 15:52Z) is compared with the 18:43Z cut", "direct", "sample", ["field", "ZOM-506", "call"], "ZOM-506.call", group="done"),
    slot("S26", "ZOM-557 call", 3, "comparison", "the fix's #builds change line is compared with the cut", "direct", "sample", ["field", "ZOM-557", "call"], "ZOM-557.call", group="done"),
    slot("S27", "ZOM-561 call", 3, "comparison", "the fix PR #469 (merged Sep 30 01:50Z) is compared with the cut", "direct", "sample", ["field", "ZOM-561", "call"], "ZOM-561.call", group="done"),
    slot("S28", "ZOM-513 call", 1, "lookup", "an art task's label decides no call", "direct", "sample", ["field", "ZOM-513", "call"], "ZOM-513.call", group="nocall"),
    slot("S29", "ZOM-387 call", 1, "lookup", "an analytics task's label decides no call", "direct", "sample", ["field", "ZOM-387", "call"], "ZOM-387.call", group="nocall"),
    slot("V01", "Register has a row for every in-scope ticket and no other existing ticket", 3, "limited_reconciliation", "the scope rule applied to the open and Done-since-gate sets fixes the key set", "delivery", "volume", ["delivery", "register_keys_exact"], "register.keys", ["R_FILTER"], volume_for=["open", "done", "nocall", "exception"]),
    slot("D01", "Sign-off posted in Arthur's candidate thread", 1, "lookup", "delivery into the named thread is a direct check", "delivery", "core", ["delivery", "slack_thread", ANNOUNCE.split("/")[1]], "signoff.thread"),
    slot("D02", "Sign-off calls the candidates not ready to ship", 3, "interpretation", "the call follows from the blocker list, which already holds clear base blockers (ZOM-546, ZOM-560) whatever the traps decide", "write_content", "core", ["text", "slack", "no[- ]?go|not (?:ready|shipping)|hold|block"], "signoff.call"),
]


def build_surface(keys: list[str]) -> dict:
    return {
        "kind": "GRADABLE_SURFACE", "version": 1, "task": "vincent-zm3d-release-gate", "revision": "scenario-01",
        "classes": ["BLOCKER", "KNOWN ISSUE", "FIXED", "NO CALL"],
        "truth_fields": {"class": "call", "groups": "groups"},
        "truth_keys": keys,
        "deliverables": {
            "register": {"kind": "table", "name_regex": "(?:#135|#50|gate|sep 30)", "key_column": "ticket",
                         "key_regex": "(?:ZOM|ART|DES)-[0-9]{1,4}",
                         "columns": ["ticket", "title", "build status", "QA result", "call", "evidence"],
                         "class_column": "call", "reason_column": "evidence",
                         "comparators": {"call": "norm", "build status": "norm"}, "missing_values": ["", "-", "n/a"]},
            "tracker": {"kind": "text", "tool": "linear_update_issue", "issue": REL, "key_regex": "(?:ZOM|ART|DES)-[0-9]{1,4}",
                        "groups": [["blocker", "blocker"]]},
            "newbug": {"kind": "json_text", "tool": "linear_create_issue"},
            "slack": {"kind": "json_text", "tool": "slack_send_message"},
        },
        "slots": [dict(s, expected_keys=keys + [SELF_FILED],
                       note=f"{SELF_FILED} is the first ticket the run files (Linear numbers the next ZOM key after ZOM-580); "
                            "Leonard's rules give tickets filed while the gate runs a row, including the ones Vincent files")
                  if s["id"] == "V01" else s for s in SLOTS],
    }


def main() -> None:
    keys = json.loads((Path(__file__).with_name("scope_keys.json")).read_text())
    m = build_manifest()
    (WF / "01_Hardness_Manifest.draft.json").write_text(json.dumps(m, indent=1, ensure_ascii=False) + "\n")
    (WF / "01_Gradable_Surface.json").write_text(json.dumps(build_surface(keys), indent=1, ensure_ascii=False) + "\n")
    total = sum(b["calls"] for b in BUDGET)
    per = sum(s["per_record_calls"] * s["records"] for s in COHORT_SPEC["evidence_surfaces"])
    print(f"manifest + surface written; cohort {COHORT}; budget {total}; per-record {per:.0f}; slots {len(SLOTS)} "
          f"weight {sum(s['weight'] for s in SLOTS)}; keys {len(keys)}")


if __name__ == "__main__":
    main()
