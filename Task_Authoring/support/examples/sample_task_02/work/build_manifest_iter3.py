#!/usr/bin/env python3
"""Build 01_Hardness_Manifest.json (iteration 2) from the minted ids and the retest plan."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
I = json.loads((HERE / "ids.json").read_text())
RID = json.loads((HERE / "retest_ids.json").read_text())
PLAN = {p["key"]: p for p in json.loads((HERE / "retest_plan.json").read_text())}
A = "arthur.blake@harmonygames.co/"
G = "harmonygames-Games/"


def sid(ch, ts):
    return hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]


AB = {"ENG-1411", "ENG-1877"}
ios_records = sum(1 for k in RID["ios"] if k not in AB)
and_records = sum(1 for k in RID["android"] if k not in AB)
RT = "C0AE7RTQ2LK"
lives_ack = sid("D04UGG61DUM", "1770779905.660219")
oliver_dm = sid("D07H86MU8JC", "1770996671.284519")
brian = sid("C05V5FNLB9V", "1760973540.207889")
inv_A = A + I["msg_inv"]


SL = {k: sid(*v) for k, v in {
    "kickoff": ("C05V5FNLB9V", "1770940961.204551"), "z611_report": ("C08R27X0EAH", "1761064228.774519"),
    "z359_ptr": ("C08R27X0EAH", "1753088702.205119"), "z359_rep": ("C08R27X0EAH", "1753171206.312449"),
    "z608_ptr": ("C08R27X0EAH", "1760477048.551029"), "z608_rep": ("C08R27X0EAH", "1760637845.902769"),
    "z610_ptr": ("C08R27X0EAH", "1760735031.118839"), "e2345_ptr": ("C05V5FNLB9V", "1763997012.448319")}.items()}
ios = lambda k: RID["ios"][k]
andr = lambda k: RID["android"][k]["comments"]
COND_SLACK = "slack_conversations_search_messages with channel/author/date filters does not return thread replies (unverified)"
COND_LINC = "no bulk path returns Linear comments (linear_show_data / list_issues / get_issue) (unverified; base has 0 comments)"
COND_PARENT = "linear_list_issues does not return each issue's parent (unverified)"
COND_IDSEARCH = "no single broad id-prefix search (GitHub PR search or Slack search) returns the comment-only references (unverified)"

M = {
 "persona": "arthur_blake", "horizon": "Long Horizon",
 "requirements": {
  "R1": "cohort membership (ENG/ZOM, Bugs/Regression state or Bug label, open, no Acceptable Behavior, created before the cut-off)",
  "R2": "lot vs Not-in-lot-Web assignment and listing",
  "R3": "tier per row (house rule + accepted amendment)",
  "R4": "fix status per row (code-history rule incl. latest-merge rule and comment-only references)",
  "R5": "exact totals per lot x tier over rows that still reproduce",
  "R6": "destination folder, file name and tabs",
  "R7": "sharing + recipient + cc + link-only",
  "R8": "cut-off (current invite) and snapshot-at-send",
  "R9": "ENG-2439 end state (link in description, In Review)",
  "R10": "known-issues slide shows the per-lot totals by tier",
  "R11": "hub-thread reply with totals",
  "R12": "Confluence checklist disagreement reported",
  "R13": "per-platform retest results and current-build status per row",
  "R14": "row grouping: sub-issues folded into the parent's row; folded tier / fix / retest aggregation"},
 "services": {
  "slack": {"role": "hub; claim + partial retraction; reproduction report; decoy scale; iOS retest threads in each game's bug channel; write W6",
            "weight_reason": "A1 delegations; the iOS retest result per ticket (its own column) exists only in thread replies in #god-bugs / #zombie-bugs; written reports that decide REPRODUCED"},
  "gmail": {"role": "hidden authority H1 + amendment; stale cut-off versions; write W3",
            "weight_reason": "membership, fix-status (incl. latest-merge), per-platform retest and totals rules, the Web amendment and the snapshot rule exist only in Leonard's forwarded intake thread"},
  "gcal": {"role": "hidden authority H4", "weight_reason": "the current cut-off (Mon Feb 16 17:00Z) exists only on Sunset's calendar event; decides ENG-2440 and the file-name date"},
  "gdrive": {"role": "destination folder (Arthur-owned 04 Technical) + same-named decoy folder; writes W2/W7", "weight_reason": "the folder the schedule must be moved into and the file-level share"},
  "gdocs": {"role": "asset schedule", "weight_reason": "lot = Linear team, repos per lot (fix-evidence scope), web build in no lot"},
  "gsheets": {"role": "hidden authority H3 + write target W1", "weight_reason": "folder, file name, tab names, sharing and notify rules live only in Leonard's data room sheet"},
  "gslides": {"role": "slide to update (W5)", "weight_reason": "the known-issues slide must show the per-lot totals by tier"},
  "contacts": {"role": "alternate identity path only (the forward already carries Sunset's onboarding lead)"},
  "github": {"role": "fix evidence", "weight_reason": "merged PRs referencing ticket ids (titles/branches, and comment-only references on 8 PRs) and their merge order decide fix status"},
  "linear": {"role": "cohort + Android retest comments + reuse ticket", "weight_reason": "the 75 candidates, their state/priority/labels/parents, the Android result per ticket (its own column), and ENG-2439"},
  "trello": {"role": "hidden authority H2", "weight_reason": "severity tiers, the accepted amendment and the row-grouping rules exist only on Arthur's founders'-board card"},
  "confluence": {"role": "same-purpose checklist whose disagreement must be reported", "weight_reason": "R12: its engineering definition must be compared and the difference flagged"}},
 "anchors": [{"id": "A1", "prompt_reference": "the known-defects schedule Leonard asked me for in the wind-down channel", "service": "slack",
              "locator": "C0ADGSZKR3R ts " + I["ts_hub"]}],
 "ask_fragments": [
  {"id": "K1", "service": "slack", "container": "C0ADGSZKR3R:" + I["ts_hub"], "locator": "hub thread parent", "kind": "delegation", "incorporated_via": ["A1"], "seeded_ids": [I["slack_hub"]]},
  {"id": "K2", "service": "gmail", "container": A + I["thr_fwd_A"], "locator": "message 1 (Sunset intake rules 1-6)", "kind": "requirement", "incorporated_via": ["A1"], "seeded_ids": [A + I["msg_fwd"]]},
  {"id": "K3", "service": "gmail", "container": A + I["thr_fwd_A"], "locator": "message 2 (Sunset follow-up)", "kind": "amendment", "incorporated_via": ["A1", "K2"], "seeded_ids": [A + I["msg_fwd2"]], "supersedes": "K2 (adds Web list; rest stands)"},
  {"id": "K4", "service": "trello", "container": I["card"], "locator": "card desc (tiers + rows)", "kind": "requirement", "incorporated_via": ["A1", "K2"], "seeded_ids": [I["card"]]},
  {"id": "K5", "service": "trello", "container": I["card"], "locator": "commentCard Robert + Arthur", "kind": "amendment", "incorporated_via": ["A1", "K4"], "seeded_ids": [I["act_c1"], I["act_c2"]], "supersedes": "K4 hot-fix clause"},
  {"id": "K6", "service": "gsheets", "container": I["f_index"], "locator": "Index tab, row 'Known defects schedule'", "kind": "destination", "incorporated_via": ["A1"], "seeded_ids": [I["f_index"]]},
  {"id": "K7", "service": "gsheets", "container": I["f_index"] + ":Notes", "locator": "Notes tab (share, notify, date rule)", "kind": "recipient", "incorporated_via": ["A1", "K6"], "seeded_ids": [I["f_index"]]},
  {"id": "K8", "service": "gcal", "container": I["ical"], "locator": "event copies (current time)", "kind": "requirement", "incorporated_via": ["A1"], "seeded_ids": [I["evt_A"], I["evt_L"], I["evt_R"]]},
  {"id": "K9", "service": "gdocs", "container": I["f_assets"], "locator": "lots section", "kind": "requirement", "incorporated_via": ["A1"], "seeded_ids": [I["f_assets"]]},
  {"id": "K10", "service": "linear", "container": "ENG-2439", "locator": "tracking ticket description (end state)", "kind": "destination", "incorporated_via": ["A1"], "seeded_ids": ["ENG-2439"]},
  {"id": "K11", "service": "gslides", "container": I["f_deck"], "locator": "slide 5 (index 4) element", "kind": "destination", "incorporated_via": ["A1"], "seeded_ids": [I["f_deck"], I["el4"]]},
  {"id": "K12", "service": "confluence", "container": "page_ip_sale_data_room", "locator": "Engineering section", "kind": "requirement", "incorporated_via": ["A1"], "seeded_ids": ["page_ip_sale_data_room"]},
  {"id": "K13", "service": "slack", "container": "C05V5FNLB9V:1770940961.204551", "locator": "retest kickoff (builds per game, where each platform's result lives)", "kind": "requirement", "incorporated_via": ["A1", "K2"], "seeded_ids": [SL["kickoff"]]}],
 "authorities": [
  {"id": "H1", "name": "Sunset's intake list (issuer: Sunset)", "home_service": "gmail", "decoy_service": "confluence", "governs": ["R1", "R4", "R13"],
   "findable_query": "Sunset intake", "seeded_ids": [A + I["msg_fwd"], A + I["msg_fwd2"]], "decoy_seeded_ids": ["page_ip_sale_data_room"]},
  {"id": "H2", "name": "Arthur's severity tiers (issuer: Arthur)", "home_service": "trello", "decoy_service": "slack", "governs": ["R3", "R14"],
   "findable_query": "severity tiers", "seeded_ids": [I["card"], I["act_c1"], I["act_c2"]], "decoy_seeded_ids": [I["slack_decoy"], brian]},
  {"id": "H3", "name": "Leonard's data room sheet (issuer: Leonard)", "home_service": "gsheets", "decoy_service": "gdrive", "governs": ["R6", "R7"],
   "findable_query": "IP Sale Data Room", "seeded_ids": [I["f_index"]], "decoy_seeded_ids": [I["d_decoy"], I["d_decoy_eng"]]},
  {"id": "H4", "name": "Sunset's invite as it stands (issuer: Sunset)", "home_service": "gcal", "decoy_service": "gmail", "governs": ["R8"],
   "findable_query": "technical intake cut-off", "seeded_ids": [I["evt_A"], I["evt_L"], I["evt_R"]], "decoy_seeded_ids": [inv_A]}],
 "cohort": {"definition_source": "H1", "key": "Linear identifier", "size": 75,
  "evidence_surfaces": [
   {"service": "slack", "tool": "slack_conversations_replies", "per_record_calls": 1, "records": ios_records, "seeded": True,
    "why_no_bulk": "Oliver's iOS result is a thread reply under one parent per ticket in #god-bugs (DD) / #zombie-bugs (ZM), interleaved with base traffic; channel history returns parents only",
    "short_circuit": "the iOS result is its own column per row (rule 4): no other surface decides it, so it cannot be skipped for any retested ticket. Sweep risk: if a channel/author/date-filtered search returns thread replies, ~3 search pages replace these reads -> budget row is conditional_on"},
   {"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1, "records": 73, "seeded": True,
    "why_no_bulk": "Robert's Android result is a Linear comment; list_issues/get_issue do not return comments; absence (not retested) also needs the per-ticket call",
    "short_circuit": "the Android result is its own column per row, including 'not retested' for the 10 cohort tickets without a comment, so every cohort ticket (73) needs the call; sweep risk: linear_show_data may dump comments -> conditional_on"},
   {"service": "linear", "tool": "linear_get_issue", "per_record_calls": 1, "records": 75,
    "why_no_bulk": "the sub-issue parent drives row grouping (R14)",
    "short_circuit": "grouping cannot be known for a ticket without its parent field; skippable only if linear_list_issues returns parent -> conditional_on"},
   {"service": "github", "tool": "github_search_pull_requests", "per_record_calls": 1, "records": 75,
    "why_no_bulk": "8 PRs reference cohort tickets only in conversation comments, which PR listings never return",
    "short_circuit": "which ticket has a comment-only reference is unpredictable (7 tickets incl. a folded child), so each id must be searched; sweep risk: one broad id-prefix search may return them if comment bodies are indexed -> conditional_on"},
   {"service": "github", "tool": "github_get_pull_request_comments", "per_record_calls": 1, "records": 13,
    "why_no_bulk": "fix vs near-miss wording is only in the comment body",
    "short_circuit": "needed only for PRs whose reference is in a comment (8 fix refs + 5 near-miss mentions); title/branch references are decided by the listing"},
   {"service": "slack", "tool": "slack_conversations_search_messages", "per_record_calls": 1, "records": 4,
    "why_no_bulk": "a later written report can sit in any channel or DM",
    "short_circuit": "skipped where Regression state or a still-happens retest already decides REPRODUCED; needed for the 4 merged-fix tickets still UNVERIFIED after the retest (ENG-2400, ZOM-610, ZOM-611, ZOM-614) — checked absence, and ZOM-611's Oct-21 report must be dated against the latest merge"}]},
 "chains": [
  {"id": "C1", "root_cause": "human fix claims vs code-history rule (no stated conclusion)", "ends_in": "R4", "hops": [
   {"service": "slack", "record": I["slack_claim"], "finding": "Leonard: sign-in bugs fixed before xmas (claim)"},
   {"service": "slack", "record": I["slack_claim_r2"], "finding": "Leonard narrows it to the splash hang; 'dunno about the rest'"},
   {"service": "slack", "record": oliver_dm, "finding": "Oliver: splash hang fixed in the fix/login race PR"},
   {"service": "github", "record": "GameOfDominoes#1876 (base) names no ticket", "finding": "no fix evidence for ENG-2363 / ENG-2280 group"},
   {"service": "linear", "record": "ENG-2363, ENG-2280 (+2073/2114/2281)", "finding": "open; NO FIX"}]},
  {"id": "C2", "root_cause": "persona's own fix claim, later written reproduction", "ends_in": "R4", "hops": [
   {"service": "github", "record": G + "game-of-dominoes-backend#79#c_2", "finding": "server-side part of ENG-2277 / ENG-2400"},
   {"service": "slack", "record": I["slack_lives"], "finding": "Leonard Feb 11: 2277 back on 309"},
   {"service": "linear", "record": "ENG-2277 REPRODUCED; ENG-2400 retest unfinished on both -> UNVERIFIED", "finding": "R4"}]},
  {"id": "C3", "root_cause": "issuer-named house rule with an accepted partial amendment", "ends_in": "R3", "hops": [
   {"service": "slack", "record": I["slack_hub"], "finding": "hub: use your severity tiers"},
   {"service": "trello", "record": I["card"], "finding": "tiers + order + row rules"},
   {"service": "trello", "record": I["act_c1"], "finding": "hot-fix clause narrowed; accepted in " + I["act_c2"]},
   {"service": "linear", "record": "ZOM-616 (T2 not T1)", "finding": "priority/state/labels"}]},
  {"id": "C4", "root_cause": "scope amendment in a later email", "ends_in": "R2", "hops": [
   {"service": "gmail", "record": A + I["msg_fwd"], "finding": "intake rules"},
   {"service": "gmail", "record": A + I["msg_fwd2"], "finding": "web build not in a lot; separate list, not counted"},
   {"service": "linear", "record": "ENG-2406, ENG-2407, ENG-2408", "finding": "WebGL label"}]},
  {"id": "C5", "root_cause": "cut-off moved after the written statements; current invite governs", "ends_in": "R8", "hops": [
   {"service": "gmail", "record": A + I["msg_fwd"], "finding": "Sunset: Fri 12:00 PT"},
   {"service": "gmail", "record": inv_A, "finding": "invitation Fri 12pm PST"},
   {"service": "gcal", "record": I["evt_A"], "finding": "event now Mon 09:00 PT (no update email)"},
   {"service": "linear", "record": "ENG-2440", "finding": "created Fri 20:31Z: in"}]},
  {"id": "C6", "root_cause": "deck count replaced by computed totals", "ends_in": "R10", "hops": [
   {"service": "gslides", "record": I["f_deck"], "finding": "19 open bugs (13/6)"},
   {"service": "linear", "record": "cohort", "finding": "67 rows"},
   {"service": "slack", "record": "retest threads", "finding": "13 rows leave the totals"}]},
  {"id": "C7", "root_cause": "fix evidence only in PR conversation comments", "ends_in": "R4", "hops": [
   {"service": "slack", "record": SL["z608_ptr"], "finding": "pointer naming ZOM-608"},
   {"service": "github", "record": "match3d#520#c_2, #316#c_2, #528#c_2, #527#c_3, #542#c_3, GameOfDominoes#1912#c_2, #1832#c_1", "finding": "comments say they fix/address the tickets"},
   {"service": "linear", "record": "ZOM-359, ZOM-608, ZOM-610, ZOM-611, ENG-2345, ENG-2242", "finding": "state"}]},
  {"id": "C8", "root_cause": "per-platform retest results in two services, each a column", "ends_in": "R13", "hops": [
   {"service": "gmail", "record": A + I["msg_fwd"], "finding": "rule 4: per-platform results + current-build rule"},
   {"service": "slack", "record": SL["kickoff"], "finding": "builds named (DD 0.3.309, ZM 0.3.157); where results live"},
   {"service": "slack", "record": ios("ENG-1762")["replies"][0], "finding": "iOS: could not make it happen"},
   {"service": "linear", "record": andr("ENG-1762")[0], "finding": "Android: still happens -> REPRODUCES"}]},
  {"id": "C9", "root_cause": "latest-merge rule with a report between two merged fixes", "ends_in": "R4", "hops": [
   {"service": "github", "record": G + "match3d#527#c_3", "finding": "first half of ZOM-611 (merged Oct 18)"},
   {"service": "slack", "record": SL["z611_report"], "finding": "Oct 21: still resets"},
   {"service": "github", "record": G + "match3d#542#c_3", "finding": "more of ZOM-611 (merged Oct 24) = latest fix"},
   {"service": "linear", "record": andr("ZOM-611")[0], "finding": "Feb 13 retests both negative -> UNVERIFIED, NOT REPRODUCED"}]}],
 "traps": [
  {"id": "T1", "family": "exact_predicate", "independent": True, "services": ["linear", "gmail"], "seeded_ids": [ios("ENG-1411")["parent"], ios("ENG-1877")["parent"]],
   "base_pointers": ["linear:data.json /issues ENG-1411", "linear:data.json /issues ENG-1877", "linear:data.json /issues ART-695", "linear:data.json /issues ENG-1866 (Regression, no Bug label)"],
   "requirement": "R1", "expected_wrong_reading": "AB tickets listed / ART tickets added / Regression-without-Bug-label tickets missed", "resolver": "H1 rule 1"},
  {"id": "T1a", "family": "distractor", "distractor_type": "near_duplicate_record", "independent": False, "merged_into": "T1", "services": ["confluence"], "seeded_ids": ["page_ip_sale_data_room"],
   "requirement": "R1", "expected_wrong_reading": "Bugs column only", "resolver": "H1 governs; Confluence only to be compared (R12)"},
  {"id": "T1b", "family": "distractor", "distractor_type": "partial_listing", "independent": False, "merged_into": "T1", "services": ["slack"], "seeded_ids": [SL["kickoff"]],
   "requirement": "R1", "expected_wrong_reading": "retest list used as the cohort (adds 2 AB, misses ENG-1866, ZOM-542, 3 WebGL, ENG-2440)", "resolver": "Linear enumeration under H1"},
  {"id": "T1c", "family": "distractor", "distractor_type": "scope_adjacent", "independent": False, "merged_into": "T1", "services": ["linear"], "base_pointers": ["linear:data.json /issues ART-696", "linear:data.json /issues EPI-25"],
   "requirement": "R1", "expected_wrong_reading": "DD art bugs in Lot A", "resolver": "H1: ENG/ZOM teams"},
  {"id": "T2", "family": "conclusion_stop", "independent": True, "services": ["linear", "trello", "github"], "seeded_ids": [G + "GameOfDominoes#1832#c_1", I["card"]],
   "base_pointers": ["linear:data.json /issues ENG-2242 parent ENG-2128", "linear:data.json /issues ENG-2073 parent ENG-2280"],
   "requirement": "R14", "expected_wrong_reading": "73 flat rows; or the ENG-2128 row marked FIX MERGED because child ENG-2242 has a fix; or the row dropped because child ENG-2130 is NOT REPRODUCED",
   "resolver": "H2 rows clause: parent's fix status; most severe tier; NOT REPRODUCED only if every member is"},
  {"id": "T3", "family": "superseding", "independent": True, "services": ["trello", "slack"], "seeded_ids": [I["act_c1"], I["act_c2"]], "requirement": "R3",
   "expected_wrong_reading": "every Hot-Fix ticket T1 (ZOM-616 T1; Lot B 11/3/3/1) or the Slack launch scale used", "resolver": "Arthur's card + accepted amendment",
   "discovery_order": "card desc is returned first; the amendment is in the comments; the Slack scale shares the search term",
   "version_records": [{"service": "trello", "id": I["card"], "seeded": True, "at": "2026-02-12T22:20:47Z"},
                       {"service": "trello", "id": I["act_c1"], "seeded": True, "at": "2026-02-13T10:12:44Z"},
                       {"service": "trello", "id": I["act_c2"], "seeded": True, "at": "2026-02-13T10:40:07Z"}]},
  {"id": "T3a", "family": "distractor", "distractor_type": "non_authoritative_instruction", "independent": False, "merged_into": "T3", "services": ["slack"], "seeded_ids": [I["slack_decoy"], brian],
   "requirement": "R3", "expected_wrong_reading": "3-level launch scale; no-priority skipped", "resolver": "hub: 'your' tiers = Arthur's card"},
  {"id": "T4", "family": "tool_surface", "independent": True, "services": ["github", "slack"],
   "seeded_ids": [G + "game-of-dominoes-backend#79#c_2", G + "match3d#316#c_2", G + "match3d#520#c_2", G + "match3d#528#c_2", G + "match3d#527#c_3", G + "match3d#542#c_3", G + "GameOfDominoes#1912#c_2", G + "GameOfDominoes#1832#c_1"],
   "requirement": "R4", "expected_wrong_reading": "ENG-2277, ENG-2400, ENG-2345, ZOM-359, ZOM-608, ZOM-610, ZOM-611 = NO FIX (title/branch matching only)", "resolver": "PR conversation comments"},
  {"id": "T5", "family": "near_miss_mention", "independent": True, "services": ["github", "slack"],
   "seeded_ids": [G + "match3d#521#c_3", G + "GameOfDominoes#1886#c_2", G + "GameOfDominoes#1882#c_3", G + "match3d#529#c_3", G + "GameOfDominoes#1888#c_3", oliver_dm, I["slack_claim"]],
   "base_pointers": ["github:data.json /branches GameOfDominoes:owen.baker/ENG-2363", "github:data.json /pull_requests GameOfDominoes#1876"],
   "requirement": "R4", "expected_wrong_reading": "ZOM-591, ENG-2042, ENG-1838, ZOM-599, ENG-2094, ENG-2149, ENG-2363 or the sign-in group marked fixed (mention, branch, chat claim or unnamed PR)",
   "resolver": "H1 rule 3: a merged PR must itself say it fixes or addresses the ticket id"},
  {"id": "T6", "family": "superseding", "independent": True, "services": ["github", "slack"], "seeded_ids": [G + "game-of-dominoes-backend#79#c_2", I["slack_lives"]], "requirement": "R4",
   "expected_wrong_reading": "ENG-2277 UNVERIFIED (later DM report not found)", "resolver": "written report after the latest merge",
   "discovery_order": "the PR comment is found from the code side; the report sits in a DM",
   "version_records": [{"service": "github", "id": G + "game-of-dominoes-backend#79#c_2", "seeded": True, "at": "2025-12-04T16:20:00Z"},
                       {"service": "slack", "id": I["slack_lives"], "seeded": True, "at": "2026-02-11T03:10:32Z"}]},
  {"id": "T7", "family": "effective_date", "independent": True, "services": ["github", "slack"], "seeded_ids": [G + "match3d#527#c_3", SL["z611_report"], G + "match3d#542#c_3"], "requirement": "R4",
   "expected_wrong_reading": "ZOM-611 FIX MERGED - REPRODUCED (Oct 21 report counted against the first merge)", "resolver": "H1 rule 3: only reports after the latest merged fix count",
   "discovery_order": "the Oct 21 report is dated after the first fix and found by id search",
   "version_records": [{"service": "github", "id": G + "match3d#527#c_3", "seeded": True, "at": "2025-10-18T02:09:52Z"},
                       {"service": "slack", "id": SL["z611_report"], "seeded": True, "at": "2025-10-21T16:30:28Z"},
                       {"service": "github", "id": G + "match3d#542#c_3", "seeded": True, "at": "2025-10-24T13:20:41Z"}]},
  {"id": "T8", "family": "synthesis_omission", "independent": True, "services": ["slack", "linear"],
   "seeded_ids": [ios(k)["replies"][0] for k in ("ENG-1762", "ENG-1839", "ZOM-559", "ZOM-458", "ZOM-616", "ENG-2109", "ENG-2350")] + [andr(k)[0] for k in ("ENG-1762", "ZOM-616", "ZOM-546", "ENG-2274")],
   "requirement": "R13", "expected_wrong_reading": "one platform's column missing or wrong; 11 rows wrongly dropped by an iOS-only reader; first reply taken where a later one corrects it",
   "resolver": "rule 4: both platforms are columns; read each thread/comment list in full"},
  {"id": "T9", "family": "exact_predicate", "independent": True, "services": ["slack", "linear"],
   "seeded_ids": [ios("ENG-1854")["replies"][0], ios("ZOM-483")["replies"][0]] + [andr(k)[0] for k in ("ENG-2190", "ZOM-517", "ZOM-535")] + ios("ENG-2400")["replies"] + andr("ENG-2400"),
   "requirement": "R13", "expected_wrong_reading": "an unfinished retest or one on another build (ENG-1854, 0.3.307) treated as 'could not make it happen'; ENG-2400's unfinished retest treated as a written reproduction",
   "resolver": "rule 4: other build = not retested; unfinished = could not finish; neither is a report"},
  {"id": "T10", "family": "superseding", "independent": True, "services": ["gmail", "gcal"], "seeded_ids": [A + I["msg_fwd"], inv_A, I["evt_A"]], "requirement": "R8",
   "expected_wrong_reading": "cut-off Fri Feb 13; ENG-2440 dropped; file dated 2026-02-13", "resolver": "hub: the invite as it stands when you send; event now Mon Feb 16",
   "discovery_order": "both written statements say Friday and are in Gmail; only the event's current time says Monday",
   "version_records": [{"service": "gmail", "id": A + I["msg_fwd"], "seeded": True, "at": "2026-02-12T21:48:36Z"},
                       {"service": "gmail", "id": inv_A, "seeded": True, "at": "2026-02-12T22:05:19Z"},
                       {"service": "gcal", "id": I["evt_A"], "seeded": True, "at": "2026-02-13T16:05:33Z"}]},
  {"id": "T10a", "family": "distractor", "distractor_type": "already_done", "independent": False, "merged_into": "T10", "services": ["gdrive", "gcal"],
   "seeded_ids": ["f_3e8b0d27c4a91f56e2d7b0", "f_b61f4c0e9a2d73e85c1a4f", "f_07d9e2a5c8b41f36d0e9a7", "evt_c90d3a6e41f72b85e0a1f7"], "requirement": "R8",
   "expected_wrong_reading": "file name dated 2026-02-13 copied from Leonard's filed PDFs / Friday review block", "resolver": "current invite"},
  {"id": "T11", "family": "superseding", "independent": True, "services": ["gmail", "gdocs"], "seeded_ids": [A + I["msg_fwd2"]], "requirement": "R2",
   "expected_wrong_reading": "WebGL tickets counted in Lot A, or dropped entirely (the asset schedule says the web build is in no lot)", "resolver": "Sunset follow-up: separate list, not counted",
   "version_records": [{"service": "gmail", "id": A + I["msg_fwd"], "seeded": True, "at": "2026-02-12T23:12:40Z"},
                       {"service": "gmail", "id": A + I["msg_fwd2"], "seeded": True, "at": "2026-02-13T15:41:07Z"}]},
  {"id": "T12", "family": "distractor", "distractor_type": "lookalike_entity", "independent": True, "services": ["gdrive", "gsheets"], "seeded_ids": [I["d_decoy"], I["d_decoy_eng"]], "requirement": "R6",
   "expected_wrong_reading": "filed in Robert's same-named 'IP Sale Data Room / Technical'", "resolver": "H3: Leonard's folder, subfolder 04 Technical"},
  {"id": "T13", "family": "exact_predicate", "independent": True, "services": ["gsheets", "gdrive", "gmail"], "seeded_ids": [I["f_index"]], "requirement": "R7",
   "expected_wrong_reading": "folder shared instead of file, attachment sent, cc missing, or link sent without sharing", "resolver": "H3 Notes"},
  {"id": "T13a", "family": "distractor", "distractor_type": "lookalike_entity", "independent": False, "merged_into": "T13", "services": ["contacts"], "seeded_ids": [I["cnt_1674"]],
   "requirement": "R7", "expected_wrong_reading": "email to Sunset's CEO", "resolver": "the forward's sender = onboarding lead"},
  {"id": "T14", "family": "reuse_exclusion", "independent": True, "services": ["linear"], "seeded_ids": ["ENG-2439"], "requirement": "R9",
   "expected_wrong_reading": "new ticket created, or ENG-2439 moved to Done", "resolver": "ENG-2439 description: link + In Review"},
  {"id": "T15", "family": "distractor", "distractor_type": "partial_listing", "independent": False, "merged_into": "T8", "services": ["gslides"], "seeded_ids": [I["f_deck"]], "requirement": "R10",
   "expected_wrong_reading": "slide keeps 19 / 13 / 6 or shows listed instead of counted totals", "resolver": "hub: per-lot totals by tier you send Sunset"}],
 "call_budget": [
  {"phase": "discovery", "service": "slack", "calls": 7, "reason": "hub + thread, #winddown window, two DMs + claim thread, retest kickoff"},
  {"phase": "discovery", "service": "gmail", "calls": 3, "reason": "intake thread (both messages in one fetch) + invitation"},
  {"phase": "discovery", "service": "trello", "calls": 3, "reason": "search 'severity tiers' (card + Slack decoy share the term), card, comments"},
  {"phase": "discovery", "service": "gsheets", "calls": 2, "reason": "find Leonard's data room sheet, read both tabs"},
  {"phase": "discovery", "service": "gcal", "calls": 2, "reason": "find Sunset's event, read its current time"},
  {"phase": "discovery", "service": "gdocs", "calls": 2, "reason": "asset schedule"},
  {"phase": "discovery", "service": "gslides", "calls": 2, "reason": "overview deck + slide element id"},
  {"phase": "discovery", "service": "confluence", "calls": 2, "reason": "checklist page to compare (R12)"},
  {"phase": "discovery", "service": "gdrive", "calls": 2, "reason": "two same-named 'IP Sale Data Room' folders; list Leonard's subfolders"},
  {"phase": "enumeration", "service": "linear", "calls": 6, "reason": "ENG/ZOM open issues, paged (~244 open)"},
  {"phase": "enumeration", "service": "slack", "calls": 3, "reason": "#god-bugs / #zombie-bugs history to map each ticket to Oliver's thread parent"},
  {"phase": "enumeration", "service": "github", "calls": 28, "reason": "PR listings across the lot repos to index title/branch references and merge times"},
  {"phase": "per-record", "service": "slack", "calls": ios_records, "reason": "iOS retest thread per retested ticket (its own column)", "conditional_on": COND_SLACK},
  {"phase": "per-record", "service": "linear", "calls": 73, "reason": "Android comments per cohort ticket incl. checked absence (its own column)", "conditional_on": COND_LINC},
  {"phase": "per-record", "service": "linear", "calls": 75, "reason": "get_issue per candidate for the parent (row grouping)", "conditional_on": COND_PARENT},
  {"phase": "per-record", "service": "github", "calls": 75, "reason": "id search per ticket for comment-only references", "conditional_on": COND_IDSEARCH},
  {"phase": "per-record", "service": "github", "calls": 13, "reason": "comment bodies of the 13 PRs whose reference is in a comment (fix vs near-miss)"},
  {"phase": "per-record", "service": "slack", "calls": 4, "reason": "later-report search for the 4 merged-fix tickets still unresolved after the retest"},
  {"phase": "reconciliation", "service": "linear", "calls": 2, "reason": "parents ENG-2280 / ENG-2128"},
  {"phase": "reads-before-writes", "service": "linear", "calls": 1, "reason": "ENG-2439 current description"},
  {"phase": "reads-before-writes", "service": "slack", "calls": 1, "reason": "hub thread ts for the reply"},
  {"phase": "writes", "service": "gsheets", "calls": 5, "reason": "create (first tab) + add 2 tabs + 3 tab writes, minus one batched"},
  {"phase": "writes", "service": "gdrive", "calls": 2, "reason": "move into 04 Technical + share file with Sunset's lead (viewer)"},
  {"phase": "writes", "service": "gmail", "calls": 1, "reason": "email link to Sunset's lead, cc Leonard"},
  {"phase": "writes", "service": "linear", "calls": 1, "reason": "ENG-2439 link + In Review"},
  {"phase": "writes", "service": "gslides", "calls": 1, "reason": "known-issues slide totals"},
  {"phase": "writes", "service": "slack", "calls": 1, "reason": "hub-thread reply"},
  {"phase": "verification", "service": "gsheets", "calls": 1, "reason": "read back the three tabs"},
  {"phase": "verification", "service": "gdrive", "calls": 1, "reason": "confirm parent + share"}],
 "writes": [
  {"service": "gsheets", "tool": "gsheets_create_spreadsheet + gsheets_batch_update (addSheet) + gsheets_values_update", "count": 1, "depends_on": ["C1", "C2", "C3", "C4", "C5", "C7", "C8", "C9", "K6"]},
  {"service": "gdrive", "tool": "gdrive_move_file", "count": 1, "depends_on": ["K6", "T12"]},
  {"service": "gdrive", "tool": "gdrive_share_file", "count": 1, "depends_on": ["K7", "T13"]},
  {"service": "gmail", "tool": "gmail_send_message", "count": 1, "depends_on": ["K7", "T13", "C5"]},
  {"service": "linear", "tool": "linear_update_issue", "count": 1, "depends_on": ["K10", "T14"]},
  {"service": "gslides", "tool": "gslides_batch_update", "count": 1, "depends_on": ["K11", "C6", "C8"]},
  {"service": "slack", "tool": "slack_send_message", "count": 1, "depends_on": ["K1", "K12", "C3", "C8"]}]}
(ROOT / "01_Hardness_Manifest.json").write_text(json.dumps(M, indent=1, ensure_ascii=False))
tot = sum(b["calls"] for b in M["call_budget"]); cond = sum(b["calls"] for b in M["call_budget"] if b.get("conditional_on"))
print("budget", tot, "conditional", cond, "floor", tot - cond, "ios", ios_records,
      "per-record", sum(s["per_record_calls"] * s.get("records", 75) for s in M["cohort"]["evidence_surfaces"]),
      "independent traps", sum(1 for t in M["traps"] if t.get("independent")))
