#!/usr/bin/env python3
"""Writes Working_Files/04_Prompt_Check.md for the current 04_Prompt.txt (word count and sha256 bound) and verifies
every quoted span is an exact substring of the prompt. Run from the workspace root:
    python3 -B Task_Authoring/task_inputs/Working_Files/scenario_gen/build_check.py
"""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
IDS = json.loads((HERE / "ids.json").read_text())
PROMPT = (TASK / "04_Prompt.txt").read_text()
WC, SHA = len(PROMPT.split()), hashlib.sha256(PROMPT.encode()).hexdigest()[:12]
G, H1, H2, LOG, MX = IDS["gate_sheet"], IDS["doc_h1"], IDS["doc_h2"], IDS["update_log"], IDS["matrix_sheet"]

DOC = f'''# Prompt Check — vincent-zm3d-release-gate
> Prompt: 04_Prompt.txt · {WC} words · sha256 {SHA} · checked 2026-11-04 against 04_Prompt_Writing_Brief.md (2026-11-04) · release task-quality-v1
> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## Summary

**Fail 0 · Non-fail 0 · Advisory 1 · UNVERIFIED 0** · checks clean: C1, C2, C3, C4, C5, C6, C7, C8, C9, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C22, C23, C24 · advisory: C10 · predicted /prompt band: PASS · Status: READY FOR /prompt

The prompt is a {WC}-word request in Vincent's first person. It names the work (the QA gate on Arthur's two candidates), the starting place (the store release ticket) and the four places the work lands: a new tab of his release gate sheet, the release ticket's description, a new ZM ticket in Linear for unfiled failures, and a reply in Arthur's candidates thread before Friday's go/no-go. Every rule, exception and correction stays in the records (the two Drive docs `{H2}` and `{H1}`, the runbook, the Trello card, the DMs).

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
| --- | --- | --- | --- | --- | --- |
| 1 | C10 | Discovery order · Advisory | "Reply in Arthur's candidates thread in #zombie-bugs" | brief §5 row 27 (`cmt_zom570_1`) and Eval 1 §2.7 hidden-destination row | Naming the thread settles Leonard's push note before the agent meets it; kept because Vincent knows the thread and hiding it would be a hidden destination (prompt_qc_cases `control-named-destination`). |

No fail and no non-fail findings were raised.

## Fair readings (accepted outcomes)

| Deliverable | Reading A | Reading B | Resolution and evidence |
| --- | --- | --- | --- |
| 1 · Register | One row per ticket in Leonard's scope (132 keys, `solver/truth.json`), each with build status, latest QA result and call | Only the Bug-labelled ZOM tickets, as the Sep 22 tab did (`{G}`) | Reading A only: `{H2}` (Sep 23) covers "every open ZM ticket, whatever team, label or state" and post-dates the Sep 22 tab; Vincent's own Sep 22 post `C08R27X0EAH/1758563100.005758` says "Bug tickets only this time". |
| 2 · Blocker list | Every BLOCKER by its existing key in the `ZOM-570` description | The same keys in a comment on `ZOM-570` | Reading A only: the prompt asks for "the release ticket's description"; a comment is a different write (outcome review). |
| 3 · New ticket | One new ZM ticket for the update from 1.3.24 to iOS Submission #50 (device, OS, source build) | Also a new ticket for the vendor's boss-fight report | Reading A only: the report maps to the existing `ZOM-562` and the reuse rule `68dc3ef455344e471b1d2ea9` says "no duplicate tickets"; the prompt asks for failures "nobody has filed yet". |
| 4 · Sign-off | A reply in `C08R27X0EAH/1759263900.484190` calling the candidates not ready / no-go | A top-level #zombie-bugs post | Reading A only: the prompt names "Arthur's candidates thread"; Leonard's note `cmt_zom570_1` asks for the reply too. |

## Verification log

| Span | Type | Universe record (locator) | Result |
| --- | --- | --- | --- |
| "Can you run the QA gate" | persona | `page_qa_runbook` owner line, `ZOM-570` assignee `usr_65c76e0b87aa7e9b` | Vincent owns QA (vincent.parker@harmonygames.co); the release ticket assigns him. |
| "the ZM store candidates" | object | `C08R27X0EAH/1759263900.484190` | Arthur: "ZM store candidates are up". |
| "Arthur cut yesterday" | event and date | `C05433XK267/1759257812.041449`, `C05433XK267/1759257934.076209` | Both jobs "Started by user Arthur Blake" on 2025-09-30 (11:43 / 11:45 PT); yesterday for Wed 1 Oct. |
| "Android Submission #135" | build | `C05433XK267/1759263189.219529` | "Match3D Android Submission - #135 - main"; the Jan 31 "DD Android Submission - #135" is another game (brief §10). |
| "iOS Submission #50" | build | `C05433XK267/1759259749.259909` | "Match 3D iOS Submission - #50 - main". |
| "The store release ticket" | ticket | `ZOM-570` | "ZM store push - Android Submission #135 / iOS Submission #50", the only store push ticket (persona_view base search "store push": 0 hits, the seeded one is unique; hg.py). |
| "has the background" | content | `ZOM-570` | Names the candidates, Leonard's rules, Arthur's build note, the reuse card and the #zombie-bugs post. |
| "my release gate sheet" | file | `{G}` | "ZM3D Release Gate", owner vincent.parker@harmonygames.co. |
| "a new tab" | write | `{G}` | Vincent owns the sheet; tabs "How we gate" and the Sep 22 gate exist. |
| "the release ticket's description" | write target | `ZOM-570` | Linear issue description, writable through linear_update_issue (catalog). |
| "a new ZM ticket in Linear" | write | team_ZOM | The ZOM team holds ZM tickets (`ZOM-562`, `ZOM-570`). |
| "the checks in the QA regression runbook" | doc | `page_qa_runbook` | "QA Regression Runbook", owned by QA (Vincent Parker); includes the update rows. |
| "that nobody has filed yet" | state | `68dc3ef455344e471b1d2ea9` | Matches Arthur's reuse comment ("only open a new one if nobody filed it yet"); hypothesis-free. |
| "Arthur's candidates thread in #zombie-bugs" | channel / thread | `C08R27X0EAH/1759263900.484190` | Arthur's top-level post in #zombie-bugs `C08R27X0EAH`; Vincent is a member (check-sql YES). |
| "the QA call" | output | `page_release_checklist` | "QA sign-off is a hard gate"; a go / no-go call is a new output, not a premise. |
| "before Friday's go/no-go" | event and date | `evt_81e6dc4dbfd331f1a6a317` | "ZM store push - go/no-go", Fri 3 Oct 2025 16:00Z (9:00 PT), on Vincent's calendar; a future meeting, created before the freeze. |

## Brief coverage

| Brief item | Present in the prompt (quoted span, or "absent") |
| --- | --- |
| §4 D1 · Register | "Put the gate register in a new tab of my release gate sheet" |
| §4 D2 · Blocker list | "add the blockers to the release ticket's description" |
| §4 D3 · New ticket | "file a new ZM ticket in Linear for anything the checks in the QA regression runbook turn up that nobody has filed yet" |
| §4 D4 · Sign-off | "Reply in Arthur's candidates thread in #zombie-bugs with the QA call" |
| §6 R1–R5 · scope, build status, QA result, liveness, calls | "The store release ticket has the background" |
| §6 R6 · matrix verdict | "the checks in the QA regression runbook" |
| §6 R7 · blockers on the ticket | "add the blockers to the release ticket's description" |
| §6 R8 · sign-off reply | "Reply in Arthur's candidates thread in #zombie-bugs" |
| §6 R9 · new ticket | "file a new ZM ticket in Linear" |
| §6 R10 · register format | "my release gate sheet" |
| §6 A1 · the store release ticket | "The store release ticket" |
| §6 A2 · the QA regression runbook | "the QA regression runbook" |
| §6 A3 · my release gate sheet | "my release gate sheet" |
| §7 · deadline | "before Friday's go/no-go" |
| §9 · tools, ids, rules, findings, vendor, old app name, call vocabulary | absent |

## Calibration cases (prompt_qc_cases.json)

| Case | Rule | Expected | Matched here? |
| --- | --- | --- | --- |
| K11-staged-errors · K11-control-spelled-correctly | staged_errors | FAIL · PASS | Matches the control: clean spelling and punctuation, no planted slip. |
| K31-trap-hint · control-symptom | trap_hint_or_riddle | FAIL · PASS | Matches neither failing quote; the prompt names the work and destinations, not a hidden problem. |
| K42, K47, K44 hidden-destination · control-named-destination | hidden_destination | FAIL · PASS | Matches the control: every destination Vincent knows is named (the sheet, the ticket's description, Linear, the thread). |
| K1-audit-form, K43-audit-form · control-plain-request | audit_form | FAIL · PASS | Matches the control: one plain request, no reconcile-classify-rank chain. |
| K44-if-chain | if_chain | FAIL | Not matched: one relative clause ("that nobody has filed yet"), no if / but-not / then-also chain. |
| K43-departed-person-premise | false_state_premise | FAIL | Not matched: Arthur is active through 2025-09-30 (activity.json active_sep_2025_quiet_in_oct). |
| K50-both-fair-figure · K49-newer-source | ugt_both_fair_figure | PASS · PASS | Not applicable: no figure is reported. |

## Self-review

| Check | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |
| --- | --- | --- | --- |
| C1 · word count and digest | The header could go stale after an edit. | len(text.split()) = {WC}, sha256 {SHA} recomputed by the gate; within 20–4,000 words. | clean |
| C2 · eight V3 fields | The prompt could sit under another persona, freeze or mode. | 00_Task_Context.json: Engineering, vincent_parker, Engineering Ops, Analysis and synthesis, Long Horizon, easy, freeze_utc 2025-10-01T00:00:00Z, synth-cut; roster vincent.parker@harmonygames.co. | clean |
| C3 · persona and voice | Arthur (CTO) could own a store gate better. | QA sign-off is Vincent's gate (page_release_checklist "Owner: Vincent Parker (QA)"); `ZOM-570` assigns him; a better-fitting colleague alone is not a Fail. | clean |
| C4 · competency, skill, function | The work could read as Retrieval, not Analysis and synthesis. | Each call combines the ticket, QA notes, the build cut and two rule docs (`{H2}`, `{H1}`); the sign-off synthesises 132 rows. | clean |
| C5 · complexity and seeding | An 88-word prompt could be under-specified. | brief §8: ambiguity (rules in Drive docs named only by description in `ZOM-570`), dynamic change (`68dc63484a5b2d0a869e758f`, `C08R6BF4ENN/1759261800.335275`, `{LOG}`), multi-source (11 services); RULE_IN_PROMPT clean (hardness_v2_check). | clean |
| C6 · fair outcomes | A comment-based blocker list or a new vendor ticket could be fair. | Settled by the prompt ("the release ticket's description", "nobody has filed yet") and `68dc3ef455344e471b1d2ea9`; recorded in the outcome review. | clean |
| C7 · clarity | "the QA call" leaves the form open. | One write (a thread reply); go / no-go wording is representational (brief §4b); no competing write. | clean |
| C8 · incorporation | The release ticket's pointers might not lead to one record each. | "Leonard's submission rules" → `{H2}`, "my note on how we cut submissions" → `{H1}`, "tech-issues card" → `68d1eb90bef538c7c5c5599d`; each shared with or unscoped for Vincent and states rules, not answers. | clean |
| C9 · pre-solved | Naming the runbook might hand over the update-path failure. | The runbook states the rule; the failing row is only in `{LOG}`; no ticket, blocker or count is named. | clean |
| C10 · discovery collapse | Naming the thread settles Leonard's destination note `cmt_zom570_1`. | Advisory finding 1; the thread is Vincent's known destination (control-named-destination). | advisory |
| C11 · investigation → action | The writes might not depend on findings. | The register needs each call, the description needs the BLOCKER set, the new ticket needs the matrix check (`{LOG}`), the reply needs the blocker list. | clean |
| C12 · tool use and cross-service | Two services might suffice. | Linear, Slack, Drive / Docs / Sheets, GitHub, Trello, Gmail, Contacts, GCal, Confluence carry weight; dossier pastes HARDNESS GATE (extreme): PASS. | clean |
| C13 · coherence | The new ticket could be a bolt-on. | All four writes serve the one gate before the go/no-go (`evt_81e6dc4dbfd331f1a6a317`). | clean |
| C14 · tool mention | "in Linear" could count as a tool mention. | A natural product name (prompt_qc_examples row 103); no function or server name. | clean |
| C15 · command list | "Put…, add…, and file…. Reply…" could be a scripted method. | It is the deliverables and who to tell (screen-24 skeleton), not which sources to read in which order; no First / Then / Finally word (common_errors §3 search hits clean after the local review removed "Then"). | clean |
| C16 · ordinary request | The runbook mention could hint at the trap. | Vincent owns the runbook (`page_qa_runbook`); the prompt names its checks generally, not the update path; no riddle, hedge, audit form or if-chain. | clean |
| C17 · truthfulness | "Arthur cut yesterday" or "Arthur's candidates thread" could be false. | `C05433XK267/1759257934.076209` (Arthur, Sep 30) and `C08R27X0EAH/1759263900.484190` (Arthur's post, seeded, check-sql YES). | clean |
| C18 · feasibility | Adding a tab or editing a description may not be cataloged. | gsheets_batch_update + gsheets_values_update, linear_update_issue, linear_create_issue, slack_send_message (catalog.json); Vincent owns `{G}`. | clean |
| C19 · persona ACL | The DM re-test and #zombie-ops note are scoped. | Vincent is in `C08R6BF4ENN` and `D0770ET1HV2`; the docs are shared with him; check-sql PASS. | clean |
| C20 · today's date | "yesterday" or "Friday" might resolve wrongly. | Persona today Wed 1 Oct 2025: yesterday Tue 30 Sep (job starts), Friday 3 Oct (`evt_81e6dc4dbfd331f1a6a317`). | clean |
| C21 · injected friction | A failure or wait could be announced. | 03_Error_Async_Config.txt Friction: none. | clean |
| C22 · universe coherence | Touched records could be inconsistent. | Injection gate PASS on this SQL (base_check, base_claims, fact_check, hg.py lint 0 FAIL); the static review findings (ZOM-481 wording, PR timing after `D079SNE2TL4/1759256193.859279`, invite timing) were fixed in rev1. | clean |
| C23 · originality | The scenario could copy a supplied sample. | No sample supplied with the task; differs from the guideline examples (store gate, not a close-out or wind-down). | clean |
| C24 · diversity | Could be investigate plus one Slack post. | Four writes over Sheets, Linear (two) and Slack. | clean |

Unresolved: none.

## Route

No Fail: paste `04_Prompt.txt` exactly as saved into `/prompt`, paired with `/injection` on the same SQL, answering the task date with Oct 1, 2025 (synth-cut). The C10 advisory is the human's call.
'''


def main():
    spans = re.findall(r'"([^"]+)"', DOC[DOC.index("## Findings"):DOC.index("## Fair readings")]) + \
        re.findall(r'\| "([^"]+)" \|', DOC[DOC.index("## Brief coverage"):DOC.index("## Calibration")])
    bad = [s for s in spans if s not in PROMPT]
    assert not bad, bad
    (WF / "04_Prompt_Check.md").write_text(DOC)
    print(f"check written · {WC} words · sha256 {SHA}")


if __name__ == "__main__":
    main()
