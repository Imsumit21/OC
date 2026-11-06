#!/usr/bin/env python3
"""Write selfreview.md (the plan's Self-review) from rows.json."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
rows = json.loads((HERE / "rows.json").read_text())
tw = sum(r["w"] for r in rows)
T = {r["tag"]: f"P{i + 1}" for i, r in enumerate(rows)}


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


out = ["## Self-review", "", "Prep self-review (playbook §Self-review, GEN_EXECUTION §6a):", "",
       "1. Re-read as /rubric (3_Rubrics_Eval.md 1.4 and 3.1): every prompt requirement (ledger R1 to R7, R7 timing by " + T["s_time"] + ") has a row on "
       "the correct artifact: the new tab (" + T["tab"] + ", " + T["tabname"] + "), the register's rows (" + T["count133"] +
       ") and its six How we gate columns (call: BLOCKER and FIXED classes in full, G1 samples; build status G2; QA result G3; "
       "evidence G4; title G5; ticket keys through every per-ticket row; register rows only in the new tab, " + T["regonly"] + "), the ZOM-570 description (" + T["z_keep"] + ", " +
       T["z_only"] + ", " + T["z_count"] + ", 19 member rows), the new issue (" + T["new_issue"] + " to " + T["new_one"] + ") and the thread reply ("
       + T["s_thread"] + ", " + T["s_call"] + "). Exclusions are exact counts or scopes on required writes (" + T["tab"] + ", "
       + T["count133"] + ", " + T["z_count"] + ", " + T["new_one"] + ", " + T["s_thread"] + "), never leave-alone rows. "
       "Runbook text the prompt does not assign (link the bug on the runbook page, mirror symptoms to the Customer Support "
       "Playbook, post the matrix) is not graded: the prompt incorporates the runbook's checks and asks for a Linear ticket; "
       "the OE (PASS) performs none of them, and the platform /prompt report records 'The QA Regression Runbook's checks "
       "are incorporated only for the new-ticket ask' (round-1 findings F2-08 to F2-12 rejected on that basis).",
       "2. Counter-readings per row (a = could a valid answer fail; b = could a wrong answer pass):", "",
       "| Row | Counter-reading | Resolution (evidence) |", "|---|---|---|"]
for k, r in enumerate(rows, 1):
    out.append(f"| P{k} | (a) a valid run writes {cell(r['valid'])}; the title accepts {cell('; '.join(r['acc']))}. (b) "
               f"strongest wrong answer: {cell(r['alt'])} | Rejected by the title's value {r['vals']}; deciding records "
               f"{r['fids']} re-verified in this run by build_rubric.py ({', '.join(r['oe'][:3])}) |")
out += ["",
        "3. Re-verify: every quoted value in 09_Rubrics.json and every source value in 00_V3_Authoring_Evidence.json "
        "rubric_rows was re-read in this run by Working_Files/rubric/build_rubric.py: seeded rows through "
        "base_check.parse_sql of 01_Universe_Inject.sql (each quote asserted verbatim in its record: Linear comments, issue "
        "descriptions, the Trello actions, the GitHub review comment rc_1, the Slack and Gmail rows, the Docs and the How we "
        "gate grid), base records through `hg.py search get-many` (Linear /issues/3347 to /issues/3641, #builds "
        "C05433XK267/2025-09.json /1120, /1122, /1129, Douglas DM /263, /265, Confluence /pages/7, Trello /cards/802). The "
        "population was recounted from linear data.json plus the 16 seeded issues: 112 open in scope, 20 Done after "
        "2025-09-22T12:30:43Z (no Done ticket between Sep 21 and the cut, so the cut time and the date read the same), no "
        "other open release ticket, no other team with a ZM title open. The 12 Opus 5.5 baseline runs in the slot (two "
        "batches) agree with every non-trap call graded here.",
        "4. Predicted all-fail re-check: 0 rows on the four bases. Every scoped record behind the cited F-ids has a "
        "persona_view YES line (pasted under §E); every write maps to a cataloged tool (gsheets_batch_update addSheet, "
        "gsheets_values_update / gsheets_values_append, linear_update_issue, linear_create_issue, slack_send_message with "
        "thread_ts); Friction: none, so no rate-1.0 retry; no row needs evidence outside Vincent's view (Linear, Trello, "
        "GitHub, Contacts and Confluence are unscoped). Rows that the earlier batches failed in every run (ZOM-293's call, "
        "the 19-blocker count) are hard, not impossible: the deciding records are visible and reachable from ZOM-570.",
        "5. Shortcut and diversity: the §F probe reports 58 hits and 2 incomplete Snowflake scans, all dispositioned. "
        "Most hits are generic words ('blocker', 'fixed', 'level 3') in older records about other builds or games. The "
        "rest are records the gate must read anyway: the rules doc and How we gate tab (vocabulary, no ticket values), "
        "the ask (ZOM-570, Arthur's post, the go/no-go invites), per-ticket comments (one or two tickets each) and Brian's "
        "update-path doc (the new-ticket rows only). The largest holder, the Sep 22 tab, covers 8 of 133 tickets and is "
        "stale on 4 of them (ZOM-559, ZOM-535, ZOM-429, ZOM-517). For the two incomplete scans, a direct read found no "
        "Snowflake row with 133 or 135 among the 7,736 rows holding any other value. None of these records answers the "
        "register. Diversity: Leonard's rules doc F6 sits in the Depends-on closure of most rows (structural, see "
        "Unresolved).",
        "6. Surface dispositions: 27 of 33 slots of 01_Gradable_Surface.json are covered by a row; S24 to S29 (ZOM-564, "
        "ZOM-506, ZOM-557, ZOM-561, ZOM-513, ZOM-387) are sampled out because G1 holds five samples plus two direct "
        "exceptions. Strongest case for a row: the independent review (F2-14, R4-1) counted the register's non-blocker "
        "calls as one sampled group over the cap (rubric_sampling.md: 'Each group covers one repeated property on one "
        "output'); resolution: none of the six is core (no prompt span names it) or an authority-decided exception, and "
        "each has a graded twin (" + T["fix_429"] + ", " + T["fix_563"] + ", " + T["smp_536"] + ").",
        "7. Weights by kind of work (1 lookup · 3 interpretation, comparison or limited reconciliation · 5 multi-source "
        "reconciliation across services): a call is 5 when a record in another service overrides or completes what the "
        "ticket shows (Trello re-test, Slack DMs, the vendor mail plus Contacts, the GitHub review comment, #builds, the DM "
        "with Douglas); 3 when the ticket's own description or comment is read against Leonard's severity rule or a Done "
        "ticket is matched to Vincent's re-check post; 1 when a ruling or label states the call. The same ticket keeps the "
        f"same weight on the register and on ZOM-570. Total {tw}.",
        "8. No-criterion-text scan: criterion titles live in 09_Rubrics.json (draft mode); the plan carries them only as "
        "the do_nothing_case quotes in §A3. 09_Rubrics.json has no em or en dash and no local file reference (asserted by "
        "the builder).", "",
        "Unresolved: (1) diversity.authority_share: Leonard's rules doc (F6) decides most of the weight by construction "
        "(its scope sentence defines the population and its severity rule decides every call); a design finding for the "
        "human to accept, as on the Robert, Douglas, Julia and Frederick tasks. (2) The human-time worksheet is not written "
        "yet (/create-humantime); it does not change any row."]
(HERE / "selfreview.md").write_text("\n".join(out) + "\n")
print("selfreview rows", len(rows))
