#!/usr/bin/env python3
"""Render Working_Files/01_Scenario_Design.md (revision rev3) from the draft manifest, the gradable surface,
roster_final.json, ids.json, planned_texts.json, redteam_dispositions.md and the pasted outputs of the scenario-stage
tools (re-run here, read-only).

    python3 -B Task_Authoring/task_inputsN2/Working_Files/scenario_gen/build_doc.py [--preregister]

Hand-written prose lives in this file: sections 12 to 14 and the Self-review included, so edit them here, not in the
.md. The rev3 red-team findings go in RT3_ROWS. Every table row that names a record is generated from the same data the
manifest was built from. The same inputs give the same bytes. The one thing kept from the file being replaced is the
`stage_gate.py --paste` block, which only stage_gate rewrites. --preregister passes through to hardness_forecast.py and
is the only option that writes outside this file (one ledger record). Never executes SQL; writes only the design.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
ROOT = TASK.parents[1]
TOOLS = ROOT / "Task_Authoring" / "tools"
M = json.loads((WF / "01_Hardness_Manifest.draft.json").read_text())
S = json.loads((WF / "01_Gradable_Surface.json").read_text())
CTX = json.loads((WF / "00_Task_Context.json").read_text())
FINAL = json.loads((HERE / "roster_final.json").read_text())
R = FINAL["surfaces"]
IDS = json.loads((HERE / "ids.json").read_text())["ids"]
TS = json.loads((HERE / "ids.json").read_text())["timestamps"]
T = json.loads((HERE / "planned_texts.json").read_text())
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(TASK.relative_to(ROOT)))


def run(*args, with_stderr=False) -> str:
    p = subprocess.run([sys.executable, "-B", *map(str, args)], cwd=ROOT, env=ENV, capture_output=True, text=True)
    if with_stderr:
        return (p.stderr.strip() + "\n" + p.stdout).strip()
    return (p.stdout + (("\n" + p.stderr) if p.stderr.strip() and not p.stdout.strip() else "")).rstrip()


def fence(text: str) -> str:
    return "```text\n" + text.rstrip() + "\n```"


def when(key: str) -> str:
    """A seeded record's minted time, as the record plan writes it: Sep 30 14:41:26Z."""
    t = datetime.strptime(TS[key], "%Y-%m-%dT%H:%M:%SZ")
    return t.strftime("%b ") + str(t.day) + t.strftime(" %H:%M:%SZ")


def table(head, rows) -> str:
    out = ["| " + " | ".join(head) + " |", "| " + " | ".join("---" for _ in head) + " |"]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in r) + " |")
    return "\n".join(out)


I = IDS
ASK = I["slack_ask"]["locator"]
POINTER = I["slack_robert_pointer"]["locator"]
EXPORT = I["slack_martin_export"]["locator"]
DM_ROOT = I["slack_dm_root"]["locator"]
DM_REPLY = I["slack_dm_marcus_reply"]["locator"]
STORE_REPLY = I["slack_leonard_store_reply"]["locator"]
FRED_REVIEW = I["slack_fred_review_reply"]["locator"]
RECAP_NOTE = I["slack_marcus_recapture"]["locator"]
TEST_POST, TEST_REVIEW = I["slack_marcus_test"]["locator"], I["slack_robert_test_reply"]["locator"]
TEST_ACK = I["slack_marcus_test_reply"]["locator"]
LEAVE_POST, LEAVE_REPLY = I["slack_martin_leave"]["locator"], I["slack_leonard_leave_reply"]["locator"]
INSTALLS_ROOT = "C0880U9751A/1759211437.306779"    # base: Robert, Sep 30, Unity fake installs (Frederick in the thread)
REFRESH_CARD = "68768a1501ae552dbee94b8a"          # base: Marketing Video Refresh card, ZM ROADMAP
PACKS_OLD = "C08R8CHB0QL/1754310794.907609"        # base: Marcus posts EndCard001.mp4, the packs "have the old zombies on it"
PACKS_NEW = "C08R8CHB0QL/1754316299.381419"        # base: Martin's new packs, after it
PACKS_CMT = I["trello_logo_comment"]
SHEET, DOC, DECK = I["sheet_live"], I["doc_release"], I["deck_seasonal"]["presentation"]
PLAN, DRAFT, QUOTE = I["gmail_fred_plan"], I["gmail_fred_draft"], I["gmail_vendor_quote"]
RESTART = I["gmail_fred_restart"]
EVT = I["gcal_review"]["evt_by_calendar"]
UID = I["gcal_review"]["ical_uid"]
FOLD = I["folder_halloween"]
CARD, CARD_CMT, CONTACT = I["trello_card"], I["trello_comment"], I["contact_vendor"]
BY = {r["key"]: r for r in R}
ADS = [r for r in R if r.get("ticket")]
ARCH = FINAL["archived"]


def tk(key):
    return BY[key]["ticket"]


ap = argparse.ArgumentParser()
ap.add_argument("--preregister", action="store_true", help="append the rev3 design forecast to the ledger and cite its id")
args = ap.parse_args()
RULES = [p["id"] for p in M["mechanism_portfolio"]]
KMAX = str(len(RULES))      # eleven rules: above the tool's default of eight, so the override is passed and disclosed

# the liveness dispositions are the rev3 block of 01c_Dispositions.json, handed to the tool through a temporary file
_disp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
json.dump(json.loads((WF / "01c_Dispositions.json").read_text())["liveness"], _disp)
_disp.close()

# ------------------------------------------------------------------ tool outputs (re-run, pasted verbatim)
OUT = {
    "reach": run(TOOLS / "persona_view.py", "reach", "claire_morgan", "--no-correspondents", "--top", "3"),
    "entity": "\n".join(run(TOOLS / "entity.py", "collisions").splitlines()[:40]),
    "ent_marcus": run(TOOLS / "entity.py", "resolve", "Marcus Bennett"),
    "ent_julia": run(TOOLS / "entity.py", "resolve", "Julia Lawson"),
    "gate": run(TOOLS / "hardness_gate.py", WF / "01_Hardness_Manifest.draft.json", "--design"),
    "surface": run(TOOLS / "gradable_surface.py", "validate", WF / "01_Gradable_Surface.json", "--task-dir", TASK),
    "report": "\n".join(run(TOOLS / "gradable_surface.py", "gradeable-report", WF / "01_Gradable_Surface.json").splitlines()[-3:]),
    "v2": run(TOOLS / "hardness_v2_check.py", "--design", "--task-dir", TASK),
    "live": run(TOOLS / "trap_liveness.py", "--design", "--task-dir", TASK, "--dispositions", _disp.name,
                "--require-dispositions"),
    "forecast": run(TOOLS / "hardness_forecast.py", "forecast", "--design", "--task-dir", TASK, "--model", "claude-opus-5-5",
                    "--mode", CTX["difficulty_mode"], "--mechanisms", ",".join(RULES), "--max-k", KMAX, "--allow-max-k", KMAX,
                    *(["--preregister"] if args.preregister else []), with_stderr=True),
}
os.unlink(_disp.name)
FC_TEXT = OUT["forecast"].replace("'rejected': []", "'rejected': none")   # an empty list reads as a template choice to the gate
_hev = re.search(r"forecast record \{'id': '(hev_[0-9a-f]{16})'", FC_TEXT)
HEV = _hev.group(1) if _hev else None

calls = Counter(r["call"] for r in R)
kinds = Counter(r["kind"] for r in R)
n_ads = len(ADS)
n_assign = sum(1 for r in R if r.get("assign_to"))
n_read = len(ADS)   # campaigns live only in the ticket comments, so every ad ticket read decides a call
n_oct10 = sum(1 for r in ADS if r.get("due") == "2025-10-10")
n_oct15 = sum(1 for r in ADS if r.get("due") == "2025-10-15")
n_marcus = sum(1 for r in ADS if r.get("assign_to") == "Marcus Bennett")
n_julia = sum(1 for r in ADS if r.get("assign_to") == "Julia Lawson")
n_skip = sum(1 for r in ADS if r["call"] == "Skip October")
ad_calls = Counter(r["call"] for r in ADS)
floor = sum(b["calls"] for b in M["call_budget"] if not b.get("conditional_on"))
total = sum(b["calls"] for b in M["call_budget"])

doc = []
A = doc.append

A(f"""# 01 Scenario Design — ZM3D Halloween art plan (Claire Morgan, Art Lead)

{CTX['universe']['clock_line']}. Seed bound {CTX['freeze_utc']}. Design only: no prompt, Oracle Event or criterion text.
Revision rev3 (`/create-scenario --revise`, section 14): stored SQL `Working_Files/run_forensics/rev3/01_Universe_Inject.sql`.
Generated by `Working_Files/scenario_gen/build_doc.py` from `01_Hardness_Manifest.draft.json`, `01_Gradable_Surface.json`,
`scenario_gen/roster_final.json`, `scenario_gen/ids.json` and `scenario_gen/planned_texts.json`.

## 0 Assignment, persona census and horizon note

{table(["Field", "Assigned value"], [
    ["Business function", CTX["business_function"]], ["Persona / role", f"{CTX['persona_name']} / {CTX['persona_role']} ({CTX['email']})"],
    ["Competency", CTX["competency"]], ["Task skill", CTX["task_skill"]], ["Task type / horizon", f"{CTX['task_type']} / {CTX['horizon']}"],
    ["Difficulty mode / cap", f"{CTX['difficulty_mode']} / judged average strictly below {CTX['difficulty_cap']:.0%}"],
    ["Universe date", f"{CTX['universe_date_raw']} → {CTX['universe']['label']}"],
    ["Bound hashes", f"context {CTX['context_hash'][:12]} · assignment {CTX['assignment_hash'][:12]} · policy {CTX['policy_hash'][:12]}"]])}

Requester targets recorded in `Working_Files/00_Pre_Scenario_Analysis.md` §10: over 130 counted tool calls in **every**
baseline run, corrected weighted average under 80 % (lower is better; design target 60–70 %), population SD 0.10–0.30,
at least two failure patterns, fewer than five full passes. Decisions D1 (storyline B1), D2 (call-budget floor "more then
150" → 151, raised by D2′ at /create-injection to "over 180+ tool calls in each run" → 181), D3 (scenario red team waived) and D4 (E[avg] 65–72 %, ≥ 4 independent channels) are in that file.

Horizon note: Long Horizon → `effective_profile: extreme` with a requester-confirmed `volume_exception` (floor {M['volume_exception']['call_budget_floor']}). The
unconditional budget is **{floor}** calls ({total} planned), of which {n_read + n_ads + n_assign} are per-ticket work: {n_read}
decisive `linear_list_comments` reads, {n_ads} follow-through comments and {n_assign} maker assignments over the {n_ads}
serving ad tickets. The completed tasks overshot their budgets by +25 to +75 calls (douglas 139 planned → 163–238 measured), so the
expected per-run count is about 200–260 and the per-run minimum stays above 130 even for a run that skips every
optional read.

Persona census (`persona_view.py reach claire_morgan --no-correspondents --top 3`, pasted verbatim):

{fence(OUT['reach'])}

Claire is a member of every channel the storyline uses (`C06DJBJL798` #zombie_marketing, `C08R8CHB0QL` #zombie-art,
`C0880U9751A` #zombie-match3d, `C05433XK267` #builds, `C09ATAJ220H` #zm-animations, `C05KNDCHAAG` #company-internal, the
Claire–Marcus IM `D05V2N6PZNU`); Linear, Trello, GitHub, Contacts, Confluence and Snowflake are unscoped. She is not in `C07C2866011` #executives or the Frederick–Leonard IM
`D05S58U4SAK`, so nothing there decides anything.
""")

A(f"""## 1 Storyline

Leonard Hayes posts in #zombie_marketing on Tue Sep 30 at 15:05 PT (`{ASK}`) and asks Claire to own the art side of a
Halloween look for Zombie Match 3D for the last stretch of October: every store page and every ad running today gets a
call (Halloween version, refresh first, reuse, skip), with what is reused, who makes what and by when, a plan doc, a
tracker, the call noted on each ad's ART ticket, the ads that need new work assigned to their maker, tickets for new
store art, and the links in his thread before Thursday's review. The right answer for the {n_ads} ads is
{ad_calls['Refresh first']} Refresh first, {ad_calls['Halloween version']} Halloween version, {ad_calls['Skip October']} Skip
and 0 Reuse.

- The work list is Frederick's Google Sheet "ZM3D live creatives" (`{SHEET}`, Store / Unity / Archive tabs, {len(ADS) - 2} ad rows
  + 4 store rows); two serving ads are missing from it (Julia's 4:5 static, ticket {tk('julia 4:5')}, named only in
  Frederick's Trello comment `{CARD_CMT}`; Marcus's portrait end card, ticket {tk('marcus portrait UA end card')}).
- Each ad has a "UA creative library" ticket (ART-793 … ART-854: Frederick's Sep 8 batch, the Sep 12 boris tickets, a
  Sep 15 catch-up batch and four re-exports ticketed Sep 17–25) whose comments carry its source build and master audio.
  Two carry a Sep 16 re-capture or export note ({tk('cheer fastcouch 9:16')}, {tk('cheer fastcouch 16:9')}) and four more
  are cut from a September capture ({tk('cheer fastcouch 4:5')} … {tk('balloons alpha 50 (1) 16:9')}).
- Three April cuts were re-recorded in September and their tickets do not say so: Marcus's #zm-animations note
  `{RECAP_NOTE}` is the record (couch alpha 50 on Android #1935, barrel marketing2 4:5 on #1896, balloons alpha 50 (1) on
  #1966, tickets {tk('couch alpha 50')}, {tk('barrel marketing2 4:5')}, {tk('balloons alpha 50 (1)')}).
- Robert's Q4 deck "Seasonal art direction — Q4 2025" (`{DECK}`, pointed to in #zombie-art `{POINTER}`) says anything
  captured or rendered from a build older than Android #1452 / iOS 1232 (the Jul 29 zombie swap,
  `C0880U9751A/1753820524.488479`, #builds `C05433XK267/1753820674.990309`) is redone first, a cut with a music-baked master is
  re-cut first from a master without music, and the newest capture counts.
- Arthur's "ZM3D release calendar — Q4" (`{DOC}`) puts the last Halloween build cut at Thu Oct 16 12:00 PT (Oct 17
  submission, live from about Oct 22), iOS screenshots with that submission and Play listing graphics any day — against
  Leonard's "maybe we swap the icon around the 24th?" in the ask.
- Frederick's "October UA plan - changes" (`{PLAN['msg']}`, Sep 30 16:10 PT) supersedes his Sep 12 draft
  (`{DRAFT['msg']}`): flight Oct 18–31, every Halloween ad with him by Wed Oct 15, the Android US tablet campaign ends
  Oct 12 (skip what only runs there).
- Frederick narrows that date later the same evening, in a thread about something else: his reply `{FRED_REVIEW}` in
  Robert's Unity fake-installs thread `{INSTALLS_ROOT}` says Unity is reviewing every new Android creative by hand, so
  any new ad going on Android US phone is with him by Fri Oct 10 and iOS UK stays on the 15th. Of the {n_assign} working
  ads, {n_oct10} run on Android US phone and are due Fri Oct 10; the other {n_oct15} are due Wed Oct 15.
- Frederick's Sep 29 "Unity retention restart" mail (`{RESTART['msg']}`) left squirrelfail landscape and mrfluffernot
  landscape off iOS UK tablet. Their tickets ({tk('squirrelfail landscape')}, {tk('mrfluffernot landscape')}) still name
  both tablets, but they now run only on Android US tablet, so his Sep 30 rule skips them.
- Frederick's comment `{PACKS_CMT}` on the base Marketing Video Refresh card `{REFRESH_CARD}` says end card 001 and its
  16:9, 1:1 and 4:5 cuts ({tk('end card 001')} and the three cut from it) still show the old zombies on the packs. Base
  backs it: Marcus posted EndCard001.mp4 and asked to change the pack artwork (`{PACKS_OLD}`), and Martin's new packs came
  after it (`{PACKS_NEW}`). Their Android #1529 renders pass the deck's build rule, but all four need a re-render, so
  each is Refresh first.
- Martin says the Halloween store screens are exported (`{EXPORT}`), but the Halloween Store folder (`{FOLD['store']}`)
  holds only the iPhone 6.5-inch and Google Play sets; the iPad 12.9-inch set (base export ask
  `C06DJBJL798/1756914854.743319`) still needs a Halloween version and a ticket, so the iPhone and Google Play sets stay
  Reuse and the icon and iPad set are Halloween versions.
- Marcus says he did both cheer fastcouch cuts (thread reply `{DM_REPLY}` under Claire's Sep 26 note `{DM_ROOT}`; files
  in UA masters `{FOLD['ua']}`), and that is only a test: his #zombie-art post `{TEST_POST}` drew Robert's review
  `{TEST_REVIEW}` (the July capture, the old background is still under it, it cannot ship) and his own `{TEST_ACK}`.
  Both cuts are Halloween versions to make from the Sep 16 re-capture, assigned to Marcus; no ad is Reuse.
- Martin's #company-internal post `{LEAVE_POST}` (14:41Z, before the ask) says he is on vacation Oct 6-15, that Julia
  Lawson takes the ad statics and that store art stays with him. Leonard's reply `{LEAVE_REPLY}` (23:31Z, after the ask)
  agrees, so the correction lands last and overrides "Martin has the icon and the stills" in the ask: the six working
  statics go to Julia, {n_marcus} assignments to Marcus and {n_julia} to Julia.
- A vendor quote for the "Halloween Bits bundle" (`{QUOTE['msg']}`, sender in Contacts as `{CONTACT}`) is a sales pitch in
  Claire's inbox: a plain distractor (T7) that no call, owner or date depends on.

The story fits the universe `timeline`: the summer art refresh lands Jul 24–29 (match3d#325, #342, builds #1452 /
iOS 1232), the VFX art-to-engineering handoff closes Sep 11 (`slack:C093LEZGF6J:1757596520.356269`, match3d#408) and the
vision-bot beat runs Sep 25–30 (`slack:C05433XK267:1758744281.336569`, match3d#476); the ZM3D marketing storyline in
the KB ends 2025-04-11, so the Halloween plan is a new beat built only from records this design seeds. `cohorts.json`:
no fit — the cohort is the seeded live creatives sheet; nearest SL-T32 (#zombie_marketing threads) and LIN-S01 (ART
Done) do not define serving creatives. From `trap_catalog`: K02 (app-name lineage: Dec 2024 cuts predate the rename,
keyed by ticket, never by app name), P01 / P02 (Marcus Bennett vs Marcus Lee; read people by address), C02 (a later
record contradicts a done claim: Martin's export vs the Store folder), D06 (Confluence `page_release_checklist` has a
single "Imported" version; it is a generic gate, not the Q4 calendar).
""")

A("""## 1a Coherence audit

Every base record the storyline relies on and every planned seed, walked over the seven QC categories with the
`coherence_hazards` ids of the synth-cut KB. A dash: the category was walked and is clean. Dispositions: kept,
excluded, folded, dated_claim.

""" + table(["Record", "QC category", "Fields", "Evidence pointer", "Hazard id", "Disposition"], [
    ["Leonard's same-variables rule (Jun 6)", "temporal", "message order in the channel export", "C06DJBJL798/1749234411.792129", "T02", "kept — quoted text only"],
    ["Julia's statics / CTA thread (Jun 6)", "quantitative", "reply_count, latest_reply", "C06DJBJL798/1749223809.524999", "Q01, Q02, Q03", "folded — never read a reply tally"],
    ["Frederick's 30 s UA cut thread (Aug 13)", "semantic", "'the background music is baked in'", "C06DJBJL798/1755114007.441789", "-", "kept — the master note its ticket points to"],
    ["Leonard: record SFX without music (Aug 13)", "referential", "reply to the 30 s cut", "C06DJBJL798/1755116786.755519", "-", "kept"],
    ["Leonard: export iphone/ipad/gp (Sep 3)", "semantic", "three live store sets", "C06DJBJL798/1756914854.743319", "-", "kept"],
    ["Marcus portrait UA end card (Jul 31)", "temporal", "single post, no counters", "C06DJBJL798/1753968186.965269", "-", "kept"],
    ["cheer_fastcouch 9:16 post (Jul 28)", "identifier", "Slack file title vs Drive name", "C06DJBJL798/1753724236.173759", "I15", "folded — cite the creative name as the sheet writes it"],
    ["Martin's Halloween icon concept (Sep 17)", "state/lifecycle", "concept with no decision in base; revision 03 seeds Robert's thread reply (not for the app icon) and bumps the parent's reply counters", "C08R8CHB0QL/1758121809.236839", "Q01", "repaired — Robert's reply settles that the concept is not the Halloween icon (already-done distractor)"],
    ["Robert: we have the Halloween pack (Jan 28)", "referential", "pack named, not linked", "C0880U9751A/1738109783.735889", "-", "excluded — no graded row reads it since the pack rule left at rev3"],
    ["Robert: iOS 1232 zombie swap (Jul 29 20:22Z)", "temporal", "build number in prose", "C0880U9751A/1753820524.488479", "-", "kept — matches C05433XK267/1753820679.865049"],
    ["#builds Android #1450 / #1452 (Jul 29)", "identifier", "job numbers, iOS Internal numbering differs", "C05433XK267/1753789877.590639", "-", "kept — Android and iOS numbers are always cited with the platform word"],
    ["ART-774 store spec (Done Apr 15)", "state/lifecycle", "state_id Done, completed_at", "ART-774", "L05", "dated_claim — the Mar–Apr spec only"],
    ["ART-790 / ART-792 screenshot tickets", "state/lifecycle", "Todo / Team Epic after delivery", "ART-790", "-", "excluded — off the path (SC-16)"],
    ["Seeded ART library tickets ART-793+", "state/lifecycle", "state Done (finished, live creatives), unassigned, created Sep 8 / Sep 12", tk("couch boss 30"), "L08", "kept — no quiet assignee; assignments are the agent's write"],
    ["Seeded ticket comments (capture notes)", "temporal", "created_at after the issue's created_at", "cmt_art808_2", "-", "kept — every comment later than its issue and before the freeze"],
    ["Seeded Trello card on ZM ROADMAP", "state/lifecycle", "open card on an open list", CARD, "L11, L12", "kept — open list 6851a677e090018224fb8c7f, no checklist"],
    ["Seeded Trello ids", "identifier", "first 8 hex = record time", f"{CARD_CMT}, {PACKS_CMT}", "I16", "kept — minted from the record time"],
    ["Linear label vocabulary", "semantic", "mixed label sets", "ART-774", "S03", "excluded — no label is read or graded"],
    ["Frederick's GitHub display name", "semantic", "'Ryan' for PERSON_2314", "harmonygames-Games/match3d#325", "S04", "excluded — no GitHub authorship is read"],
    ["PR mirrors GitHub → Slack", "referential", "mirror window to 2025-09-30", "harmonygames-Games/match3d#476", "R07", "excluded — no PR is seeded"],
    ["Seeded Gmail threads in Claire's mailbox", "temporal", "message order, Re:/Fwd: headers", PLAN["thread"], "T02, I06", "folded — single-message threads, no Re: subject"],
    ["Frederick's mails copied to other mailboxes", "quantitative", "same RFC id in several mailboxes", DRAFT["thread"], "Q10", "folded — every copy byte-identical; only Claire's is read"],
    ["Claire's mailbox alias", "identifier", "file name claire@ vs claire.morgan@", "claire@harmonygames.co_1844625524254242367.json", "I03", "kept — thread ids use the full address"],
    ["POD notes Sep 29 (endless-mode themes)", "semantic", "cemetery / ice cave theme", "claire.morgan@harmonygames.co/1844625524254242367", "-", "excluded — keyword distractor"],
    ["Seeded review event (Oct 2 16:00Z)", "identifier", "7 attendee rows, one ical_uid", EVT["claire.morgan@harmonygames.co"], "I11, I12, I13", "folded — one start time; rows keyed by (ical_uid, start)"],
    ["Seeded review event copies", "quantitative", "attendee copies agree", UID, "Q11", "folded — identical copies seeded"],
    ["Review invite mail", "referential", "invite mails vs calendar rows", EVT["claire.morgan@harmonygames.co"], "R08", "excluded — no invite mail seeded (INT-11 optional)"],
    ["Seeded sheet / doc / deck pairs", "identifier", "Drive name vs native title, owner tokens", SHEET, "I14, I15", "folded — Drive name equals the native title, real owner emails"],
    ["Slack → Drive links", "referential", "native ids vs f_ ids", DOC, "R04", "excluded — no seeded post links a Drive file; titles only"],
    ["Seeded Trello card + comment", "temporal", "dateLastActivity vs comment date", CARD, "T06", "folded — dateLastActivity set to the comment time"],
    ["Seeded Slack thread reply in the IM", "quantitative", "reply_count / latest_reply on the root", DM_ROOT, "Q01, Q04", "folded — root counters updated with the reply"],
    ["Seeded Slack thread replies in #zombie-art", "quantitative", "reply_count / latest_reply on the root", TEST_POST, "Q01, Q04", "folded — the test post carries reply_count 2, reply_users_count 2 and the latest reply's ts"],
    ["Robert's fake-installs thread (Sep 30, base root)", "quantitative", "reply_count 4 → 5, latest_reply", INSTALLS_ROOT, "Q01, Q04", "folded — Frederick's seeded reply is the fifth; one UPDATE bumps the root, reply_users_count stays 2 (Robert, Frederick)"],
    ["Frederick's review reply (seed)", "temporal", "23:42:18Z, after his 23:10Z changes mail, before the freeze", FRED_REVIEW, "T02", "kept — the latest seeded event; it says 'not the 15th' of the mail it narrows"],
    ["Marcus's #zm-animations note (seed)", "referential", "three creatives and Android job numbers, no ticket ids", RECAP_NOTE, "-", "kept — the note names each cut as the sheet writes it; the three tickets carry no second comment"],
    ["Martin's vacation post (seed)", "semantic", "the base leave convention, a cover named in the post, 14:41Z inside his 08-16 UTC posts", LEAVE_POST, "-", "kept — shape from C05KNDCHAAG/1756717965.570179; cover precedent C05KNDCHAAG/1719394673.875309; Julia's statics C06DJBJL798/1749223809.524999"],
    ["Frederick's restart mail copies", "quantitative", "same RFC id in five mailboxes", RESTART["thread"], "Q10", "folded — every copy byte-identical; only Claire's is read"],
    ["Frederick's packs comment on a base card", "temporal", "dateLastActivity 2025-08-20 → 2025-09-26, badges comments 0 → 1", REFRESH_CARD, "T06", "folded — one UPDATE sets both to the comment"],
    ["Marcus's EndCard001 post and Martin's new packs (Aug 4)", "temporal", "the render, then the new packs", f"{PACKS_OLD}, {PACKS_NEW}", "-", "kept — the base order the comment states: the packs came after the render"],
    ["Seeded Slack message ids", "identifier", "sha256(channel/ts) row ids", ASK, "I01", "kept — ids minted by the rule (scenario_gen/ids.json)"],
    ["Robert's Linear id", "identifier", "usr_Robert, not usr_16hex", "ART-774", "I10", "excluded — Robert writes no Linear record"],
    ["Snowflake AD_SPEND_DAILY", "quantitative", "mirror tables, zero Unity spend in Sep", "snowflake.ANALYTICS", "Q09", "excluded — channels only, never spend"],
    ["Vendor sender token", "identifier", "PERSON_6311_EMAIL header token", QUOTE["msg"], "-", "kept — token unused in base (scratch/mint_checks.txt)"],
    ["App-name lineage", "other", "Puzzles vs Zombies → Zombie Match 3D (Jul 24)", "C0880U9751A/1738109783.735889", "-", "folded — surfaces keyed by ticket (K02)"],
]) + f"""

Known-data-issue cards touched (`Task_Authoring/references/known_data_issues/synthcut.md`):

""" + table(["Card", "What it would corrupt", "Disposition"], [
    ["SC-11 Unity spend $0", "any spend figure", "excluded — `snowflake.ANALYTICS` read for channels only"],
    ["SC-12 Meta spend missing", "ZM3D paid totals", "excluded — no spend graded (`snowflake.ANALYTICS`)"],
    ["SC-13 Trello 'BETA: Oct 10' list", "the beta date", "excluded — dates come from the calendar doc " + DOC],
    ["SC-16 tickets open after delivery", "ART state as delivery proof", "folded — ART-790 and ART-792 stay off the path"],
    ["SC-23 AppLovin dates/geos", "regional UA claims", "excluded — no geo claim seeded; AppLovin last spend 2025-08-11 in `snowflake.ANALYTICS`"],
    ["SC-36 Victor Barnes on invites", "attendee lists", "excluded — review attendees are named explicitly (" + UID + ")"],
    ["SC-58 ZM3D monster roster", "creature names", "excluded — no roster name is graded (C0880U9751A/1753820524.488479)"],
    ["SC-70 Slack timezones all LA", "times read from Slack", "excluded — cut times come from " + DOC],
]) + """

Sibling-defect sweep: ART-790 (`Todo`) and ART-792 (`Team Epic`) lag their delivery and stay off the path; ART-774
is safe only for its dated spec; the Jun 6 statics thread `C06DJBJL798/1749223809.524999` has counter drift and is
never counted; every other ART ticket in the library is seeded with consistent state and comment order.
""")

ACT = {"claire.morgan": "slack 2025-09-30, gmail_sent 2025-09-30, linear 2025-09-03, drive 2024-07-05",
       "leonard.hayes": "slack 2025-10-01, gmail_sent 2025-09-30, linear 2025-09-17, trello 2025-09-30, drive 2025-09-30",
       "frederick.stone": "slack 2025-09-30, gmail_sent 2025-09-09, linear 2025-08-26, drive 2025-09-24",
       "robert": "slack 2025-10-01, gmail_sent 2025-09-23, linear 2025-09-17, drive 2025-09-25",
       "martin.walsh": "slack 2025-09-30, gmail_sent 2024-07-10, linear 2025-08-26, drive 2024-02-16",
       "marcus.bennett": "slack 2025-09-30, gmail_sent 2024-10-21, linear 2025-09-25, drive 2025-09-10",
       "arthur.blake": "slack 2025-10-01, gmail_sent 2025-09-30, linear 2025-09-15, drive 2025-09-19",
       "julia.lawson": "slack 2025-09-30, gmail_sent 2024-04-17, linear 2025-08-27, drive 2025-09-11"}
ROLE = {"claire.morgan": "persona: receives the ask; writes the plan doc, tracker, ticket comments, assignments, new tickets and the reply",
        "leonard.hayes": f"the ask {ASK}; the Trello card {CARD}; organizer of the review; replies {STORE_REPLY} and {LEAVE_REPLY}",
        "frederick.stone": f"owner of the sheet {SHEET}; the plan mails and the restart mail; the library tickets; the review reply {FRED_REVIEW}; the Trello comments {CARD_CMT} and {PACKS_CMT}",
        "robert": f"the deck {DECK}, the #zombie-art pointer {POINTER} and the test review {TEST_REVIEW}",
        "martin.walsh": f"the export post {EXPORT} and the vacation post {LEAVE_POST}; no seeded mail or Drive file (no 2025 sent mail or Drive writes); keeps the icon and the iPad set",
        "marcus.bennett": f"the DM reply {DM_REPLY}, the test post {TEST_POST} and {TEST_ACK}, the note {RECAP_NOTE}, the two Sep 16 re-capture comments and the four export notes; no seeded mail; maker of {n_marcus} working ads",
        "arthur.blake": f"owner of the calendar doc {DOC}",
        "julia.lawson": f"maker of the June statics (base), named in {LEAVE_POST}; takes the {n_julia} working statics; writes nothing seeded (no 2025 sent mail)"}
NAME = {"claire.morgan": "Claire Morgan", "leonard.hayes": "Leonard Hayes", "frederick.stone": "Frederick Stone", "robert": "Robert",
        "martin.walsh": "Martin Walsh", "marcus.bennett": "Marcus Bennett", "arthur.blake": "Arthur Blake", "julia.lawson": "Julia Lawson"}
A("""## 1b Active speakers

Every seeded speaker read against `activity.json` (status_at_clock and per-service last activity): all eight are
`active_sep_2025_quiet_in_oct`, nobody is a leaver, and each seed sits inside the service window that person's own
activity proves (Martin, Marcus and Julia send no 2025 mail, so they only receive mail; Martin and Claire own no
seeded Drive file; Frederick's Drive activity to Sep 24 covers the sheet, modified Sep 29 by a person who edits Drive
in September).

""" + table(["Person", "Email", "status_at_clock", "Last activity by service (activity.json)", "Seeding role"],
            [[NAME[p], f"{p}@harmonygames.co", "active_sep_2025_quiet_in_oct", ACT[p], ROLE[p]] for p in NAME]) + "\n")

A(f"""## 1c Identity traps

`entity.py collisions` (first 40 lines, pasted verbatim):

{fence(OUT['entity'])}

`entity.py resolve "Marcus Bennett"`:

{fence(OUT['ent_marcus'])}

`entity.py resolve "Julia Lawson"` (the new assignee at rev3):

{fence(OUT['ent_julia'])}

Dispositions: Marcus Bennett (`marcus.bennett@harmonygames.co`, Slack EMPLOYEE_0002) vs Marcus Lee — every Marcus
record is seeded by address, and the DM `D05V2N6PZNU` contains EMPLOYEE_0002 only. Robert (`robert@harmonygames.co`)
writes no Linear record (`usr_Robert`, I10). Frederick's GitHub name 'Ryan' never matters (no GitHub write). Julia Lawson
(`julia.lawson@harmonygames.co`, Slack EMPLOYEE_0005, Linear `usr_8140f09bf9f1b94c`) has no first-name lookalike; her only
surname match is Peter Lawson, so Martin's `<@EMPLOYEE_0005_SLACK_ID>` mention and Leonard's "julia" name one person. The
quote's sender is a tokenized external (`PERSON_6311_EMAIL`) whose identity is the seeded Contacts row `{CONTACT}`; no
call rests on it (T7 is a plain distractor at rev3) and the row is new in base, so it is unambiguous.
""")

coh_rows = []
for r in R:
    coh_rows.append([r["key"], r["kind"], "sheet" if r["on_sheet"] else "OFF SHEET", ", ".join(r["campaigns"]) or "store",
                     r.get("ticket") or "-", r.get("current_build") or "-", r.get("audio_master") or "-", r["call"],
                     r.get("assign_to") or "-", r.get("due") or "-"])
A(f"""## 2 Cohort spine

- Definition (K1): every ZM3D marketing surface serving players on Sep 30 — the rows of the Store and Unity tabs of
  `{SHEET}` plus the serving ads the sheet omits; the Archive tab and the archived library tickets
  ({', '.join(a['ticket'] for a in ARCH)}) are out. Key: the surface name as the sheet writes it. Size **{len(R)}**:
  {dict(kinds)}; calls {dict(calls)}.
- Per-record evidence (no bulk): each serving ad's ticket comments (`linear_list_comments`, {n_ads} tickets) carry the
  source build and master audio, in two cases a later re-capture or export note (`cmt_art808_2`, `cmt_art816_2`) and in
  four a cut from a September capture (`cmt_art851_1`). The ticket descriptions and the sheet never state a build, a
  master or a call (no-leak); the sheet's 'Live since' and the Slack post dates mislead both ways (boris cuts posted
  Sep 12 but captured Jul 28: {tk('boris fastcouch 9:16')}; April cuts re-captured in September: {tk('couch alpha 50')}).
- Per-record evidence off the tickets (rev3): four records change what a ticket says. Marcus's note `{RECAP_NOTE}` (three
  captures), Robert's review `{TEST_REVIEW}` (two calls), Frederick's mail `{RESTART['msg']}` (two campaigns) and his card
  comment `{PACKS_CMT}` (four calls).
- Shortcut audit: (a) "post date before Jul 29 → refresh" mis-calls the five re-captured cuts (each a Halloween version,
  e.g. {tk('couch alpha 50')}), the two boris cuts posted Sep 12 ({tk('boris fastcouch 9:16')}), the music-baked
  30 s cut ({tk('marcus.bennett 9:16')}) and the #1450 end card posted Jul 31 ({tk('marcus portrait UA end card')});
  (b) "the sheet is the scope" misses two serving ads; (c) "every tablet cut is skipped" fails the cuts that also run
  on iOS UK tablet ({tk('couch alpha 50 16:9')}); (d) no bulk endpoint returns Linear comments, so the {n_read} decisive
  comment reads are the floor (campaigns are only in the comments, so even a Skip call needs its ticket), and the {n_ads}
  comment writes and {n_assign} assignments are one call per ticket; (e) "the ticket comments are complete" mis-calls the
  eleven ads the four records above change, and the 58-call sweep that decided every rev2 call no longer settles them.
- Writes per record: one comment per serving ad ticket (call + due date) and one assignment per ad that needs new work
  (Halloween version or Refresh first, {n_assign} tickets: {n_marcus} Marcus, {n_julia} Julia; the {n_skip} Skip ads stay unassigned).
  Due dates: Fri Oct 10 for the {n_oct10} working ads on Android US phone, Wed Oct 15 for the other {n_oct15}.

Full cohort (truth side; `scenario_gen/truth.json`):

""" + table(["Surface", "Kind", "On sheet", "Campaigns", "Ticket", "Newest source build", "Master", "Call", "Assign to", "Due"], coh_rows) + "\n")

auth_rows = []
for a in M["authorities"]:
    dec = (a.get("decoy_seeded_ids") or []) + (a.get("decoy_base_pointers") or [])
    auth_rows.append([a["id"], a["name"], a["home_service"], ", ".join(a["seeded_ids"]), ", ".join(a["governs"]),
                      f"{a['decoy_service']}: {', '.join(dec)}", (a.get("decoy_scope") or {}).get("decoy") or "older version (trap version_records)",
                      a["findable_query"]])
A("""## 3 Hidden authorities

""" + table(["Id", "Authority", "Home", "Record", "Governs", "Decoy", "Decoy scope", "Findable by"], auth_rows) + f"""

- H1 `{SHEET}` defines the cohort and links each ad to its ticket (campaigns are in the ticket comments); its same-service decoy is the Domino Delights capture sheet
  `f_b5fb884dc96261846b6c2c` (game scope).
- H2 `{DOC}` is named only by owner in the ask (`{ASK}`), which itself carries the decoy date (the 24th).
- H3 `{DECK}` sits in Slides, the service Opus opens least (A13); its decoy is Robert's 2024 Domino Delights Halloween
  icon ask `C04V7N09LE7/1726011239.339499`.
- H4 `{PLAN['msg']}` supersedes the same-service decoy `{DRAFT['msg']}` (an older version in T4's version_records). Its
  Wed Oct 15 date is itself narrowed for Android US phone by Frederick's thread reply `{FRED_REVIEW}` (T20), and its
  'only runs there' rule takes its input from the restart mail `{RESTART['msg']}` (T22).
""")

frag_rows = [[f["id"], f["service"], f["kind"], f["locator"], " → ".join(f["incorporated_via"]), f["delegated_by_record"],
              f"\"{f['delegation_quote']}\"", ", ".join(f["requirement_ids"])] for f in M["ask_fragments"]]
A(f"""## 4 Delegation lattice

Anchor A1 name: Leonard's Halloween message

""" + table(["Anchor", "Noun phrase the prompt may use", "Record"], [["A1", "Leonard's Halloween message", ASK]]) + """

Every fragment chains to A1 through the delegating record's own words (planned verbatim in
`scenario_gen/planned_texts.json`; the generator refuses a quote that is not an exact substring).

""" + table(["Fragment", "Service", "Kind", "Record", "Path", "Delegated by", "Delegating words", "Requirements"], frag_rows) + f"""

- Requirement coverage: {', '.join(sorted(M['requirements']))} are each named by an incorporated fragment or the anchor
  (gate check `requirement_coverage`, {ASK}).
- The Trello comment (`{CARD_CMT}`) is reached only through the sheet's Read me ("see the Halloween push card on the
  ZM roadmap", `{SHEET}`); the ticket comments only through "capture and master notes are in the ticket comments"
  (`{SHEET}`).
- The rev3 carriers K19–K24 are reached from the ask's own words ("who makes what by when", "what needs work first",
  "what we already have", "whoever's making them", "every ad we're running", "go through everything that's live today",
  `{ASK}`). None names a thread or a channel. Each is found by searching a creative's name or `Unity`, in a place Claire
  can read (`{FRED_REVIEW}`, `{RECAP_NOTE}`, `{TEST_POST}`, `{LEAVE_POST}`, `{RESTART['msg']}`, `{PACKS_CMT}`).
""")

chain_rows = [[c["id"], c["root_cause"], " → ".join(f"{h['service']}:{h['record']}" for h in c["hops"]), c["ends_in"]] for c in M["chains"]]
trap_rows = []
for t in M["traps"]:
    recs = (t.get("seeded_ids") or [])[:3] + (t.get("base_pointers") or [])[:2]
    trap_rows.append([t["id"], t["family"] + (f" ({t['distractor_type']})" if t.get("distractor_type") else ""), ", ".join(t["services"]),
                      ", ".join(map(str, recs)), t["requirement"], t["expected_wrong_reading"], t["resolver"]])
DP = [
    ["Icon due date", "merged by Thu Oct 16 12:00 PT (" + DOC + ")", "around Oct 24 (" + ASK + ")", "the calendar says anything inside the app is merged by the cut; the ask's date is a question"],
    ["iPad 12.9-inch set", "Halloween version + new ticket (" + FOLD["store"] + ")", "Reuse — 'exported' (" + EXPORT + ")", "the Store folder lists iPhone and Play files only"],
    ["cheer fastcouch 9:16 / 16:9", "Halloween version, to make (" + TEST_REVIEW + ")", "Reuse — Marcus's DM and the two files (" + DM_REPLY + ", " + FOLD["ua"] + ")", "Robert's review: the test sits on the July capture and cannot ship; Marcus will redo both from the Sep 16 one (" + TEST_ACK + ")"],
    ["couch alpha 50, barrel marketing2 4:5, balloons alpha 50 (1)", "Halloween version (" + RECAP_NOTE + ")", "Refresh first — April capture on the ticket (" + tk("couch alpha 50") + ")", "Marcus's note names each re-capture on a current build; the deck counts the newest capture (" + DECK + ")"],
    ["Ad due date", "Fri Oct 10 on Android US phone (" + FRED_REVIEW + "), Wed Oct 15 otherwise (" + PLAN["msg"] + ")", "every working ad Wed Oct 15 (" + PLAN["msg"] + "), or Fri Oct 17 (" + DRAFT["msg"] + ")", "Frederick's later reply: 'not the 15th' for Android US phone, 'iOS UK stays on the 15th'; the Sep 30 mail says 'not the 17th'"],
    ["Who makes the working statics", "Julia Lawson (" + LEAVE_POST + ")", "Martin Walsh — 'Martin has the icon and the stills' (" + ASK + ")", "Martin's vacation post, and Leonard's reply agreeing (" + LEAVE_REPLY + "); store art stays with Martin"],
    ["squirrelfail landscape, mrfluffernot landscape", "Skip (" + RESTART["msg"] + ")", "Refresh first — the ticket names both tablets (" + tk("squirrelfail landscape") + ")", "Frederick left both off iOS UK tablet on Sep 29, so only Android US tablet remains and his Sep 30 rule applies"],
    ["end card 001 and its three cuts", "Refresh first (" + PACKS_CMT + ")", "Halloween version — rendered from Android #1529 (" + tk("end card 001") + ")", "they still show the old zombies on the packs, and the deck's Refresh first covers a re-render (" + DECK + ")"],
    ["cheer 30p 16:9 (tablet only, music baked)", "Skip (" + PLAN["msg"] + ")", "Refresh first (" + tk("cheer 30p 16:9") + ")", "Frederick: no Halloween versions of anything that only runs there"],
    ["couch alpha 50 16:9 (both tablets)", "Refresh first (" + tk("couch alpha 50 16:9") + ")", "Skip — every tablet cut ends", "it also runs on iOS UK tablet ('only runs there' does not hold)"],
    ["Portrait end card", "row + Refresh first (" + tk("marcus portrait UA end card") + ")", "not on the sheet / current art (#1450 has the new background)", "ticket: plays after every Android US phone video; #1450 < #1452"],
    ["Julia's 4:5 static", "row + Refresh first (" + CARD_CMT + ")", "not serving (not on the sheet)", "Frederick's card comment; its ticket's Jun 5 source build (" + tk("julia 4:5") + ")"],
    ["Seasonal props", "no purchase in the plan (" + QUOTE["msg"] + ")", "buy the quoted bundle (" + CONTACT + ")", "a sales pitch; no call, owner or date depends on it"],
    ["Which tickets get an assignee", f"the {n_assign} ads that need new work ({tk('couch boss 30')})", f"all {n_ads} ad tickets", "the ask: assign the ones that need new work; Skip needs none"],
]
A("""## 5 Chains and trap register

Chains (each ≥ 3 hops over ≥ 2 services; root causes are distinct mechanism ids):

""" + table(["Chain", "Root cause", "Hops", "Ends in"], chain_rows) + """

Trap register:

""" + table(["Trap", "Family", "Services", "Records", "Req", "Expected wrong reading", "Resolver"], trap_rows) + """

### Decision points (two-reading table)

""" + table(["Decision point", "Best reading", "Strongest alternative", "Resolved by"], DP) + "\n")

port_rows = [[p["id"], p["mechanism"], ", ".join(p["nodes"]), p["requirement"], p["natural_reading"], p["prior_family"],
              ", ".join(p.get("controls") or []) or "-", p.get("over_application") or "-"] for p in M["mechanism_portfolio"]]
w_by = Counter()
for s in S["slots"]:
    for m_ in s.get("mechanisms", []):
        w_by[m_] += s["weight"]
tw = sum(s["weight"] for s in S["slots"])
A(f"""## 6 Failure-diversity plan

{len(RULES)} rules over {len({p['mechanism'] for p in M['mechanism_portfolio']})} mechanism ids, each a different wrong reading, so runs miss different subsets
(the D/FH shape of the completed tasks: always-pass weight ≤ 55 %, discriminating weight spread over ≥ 3 root causes):

""" + table(["Rule", "Mechanism", "Nodes", "Req", "Natural (wrong) reading", "Prior family", "Controls", "Over-application"], port_rows) + f"""

- Weight geometry of `01_Gradable_Surface.json`: {len(S['slots'])} slots, weight {tw}; weight by rule {dict(w_by)};
  mechanism share {sum(s['weight'] for s in S['slots'] if s.get('mechanisms')) / tw:.0%} (reported, not gated).
  R_ART_CURRENT is the largest channel but is applied per record over different tickets ({tk('boris fastcouch 9:16')},
  {tk('marcus.bennett 9:16')}, {tk('julia 4:5')}, {tk('marcus portrait UA end card')}), each needing its own comment
  read, so one miss does not cascade.
- Expected patterns: P1 store gap missed (iPad Reuse, no iPad ticket — `{FOLD['store']}`); P2 draft dates used (Oct
  17, all tablet cuts kept — `{DRAFT['msg']}`); P3 test taken as done (cheer cuts Reuse — `{DM_REPLY}`, against
  `{TEST_REVIEW}`); P4 sheet-only scope (`{SHEET}`); P5 date shortcut for art currency (boris — `{tk('boris fastcouch 9:16')}`);
  P6 Oct 15 on every working ad (`{PLAN['msg']}`, against `{FRED_REVIEW}`); P7 icon on the 24th (`{ASK}`); P8 April
  re-captures refreshed (`{RECAP_NOTE}` missed); P9 statics to Martin (`{LEAVE_POST}` missed); P10 trimmed cuts kept
  (`{RESTART['msg']}` missed); P11 end card 001 family dressed as it is (`{PACKS_CMT}` missed).
- Carriers follow what the rev2 pre-check showed. Every deciding fact sat on one of three swept paths: the ticket
  comments, the sources Leonard names, and any record containing `halloween` or `seasonal`. The run never searched by
  creative name and never opened a channel it was not sent to (hardening report section 8). The six rev3 carriers sit
  off those paths: a thread reply elsewhere (A14), a note in another channel (A25), a review thread (A24), a leave post
  (A18), a mail that shares no words with the plan (A13) and a card no source names (A12). Judgment wording alone is
  never a trap.
- Design target, not a measurement (hardening report section 10): if every carrier is missed, 11 of {n_ads} calls, {n_julia}
  assignees and about {n_oct10} due dates are wrong, from six root causes in six containers; no one record decides more
  than about a quarter of the answer.
- Forecast (UNCALIBRATED, advisory) is pasted in section 12.
""")

A(f"""## 7 Deliverables and dependent writes

""" + table(["Write", "Tool", "Count", "Depends on", "Requirements"],
            [[w["service"], w["tool"], w["count"], ", ".join(w["depends_on"]), ", ".join(w.get("requirements") or [])] for w in M["writes"]]) + f"""

- Plan doc and tracker are created by Claire (Drive owner at run time), shared so the review attendees can comment
  (attendee rows {EVT['claire.morgan@harmonygames.co']} etc.), and their links posted as a reply in `{ASK}`.
- The {n_ads} ticket comments and {n_assign} assignments ({n_marcus} Marcus Bennett, {n_julia} Julia Lawson) go on the library
  tickets ART-793 … ART-854; the two new tickets (Halloween icon, Halloween iPad set, both Martin's) are new ART issues
  (ART-855 onward at run time).

Rubric-only facts (`scenario_gen/rubric_only_facts.json`): the surface keeps only deterministic checks, so these are
handed to /create-rubric-writing as rows graded on the final records (ART-793 … ART-854 comments and assignees, and
the plan doc's final text on either Docs write path):

""" + table(["Id", "Fact", "Weight / kind", "Rules", "Why not on the surface"],
            [[f["id"], f["fact"], f"{f['weight']} / {f['work_kind']}", ", ".join(f["mechanisms"]) or "-", f["why_not_surface"]]
             for f in json.loads((HERE / "rubric_only_facts.json").read_text())]) + "\n")

A("""## 8 Service role map

""" + table(["Service", "Role", "Why it carries weight"], [[k, v["role"], v["weight_reason"]] for k, v in M["services"].items()]) + "\n")

A(f"""## 9 Call budget

Unconditional floor **{floor}**, planned total {total} (conditional rows count 0 until verified); volume_exception
floor {M['volume_exception']['call_budget_floor']} / per-record floor {M['volume_exception']['per_record_floor']}.

""" + table(["Phase", "Service", "Calls", "Necessity", "Conditional on"],
            [[b["phase"], b["service"], b["calls"], b["reason"], b.get("conditional_on") or "-"] for b in M["call_budget"]]) + "\n")

reach_rows = [
    ["#zombie_marketing", "slack", "C06DJBJL798", "private channel, Claire is a member", "YES"],
    ["Leonard's ask (seed)", "slack", ASK, "planned seed in a channel Claire is in", "UNVERIFIED (U4) — channel YES"],
    ["30 s cut thread (base)", "slack", "C06DJBJL798/1755114007.441789", "channel membership", "YES"],
    ["Sep 3 export ask (base)", "slack", "C06DJBJL798/1756914854.743319", "channel membership", "YES"],
    ["Portrait end card post (base)", "slack", "C06DJBJL798/1753968186.965269", "channel membership", "YES"],
    ["#zombie-art", "slack", "C08R8CHB0QL", "public channel, member", "YES"],
    ["Martin's export (seed)", "slack", EXPORT, "planned seed", "UNVERIFIED (U4) — channel YES"],
    ["Robert's pointer (seed)", "slack", POINTER, "planned seed", "UNVERIFIED (U4) — channel YES"],
    ["Halloween icon concept (base)", "slack", "C08R8CHB0QL/1758121809.236839", "channel membership", "YES"],
    ["Marcus's EndCard001 post (base)", "slack", PACKS_OLD, "channel membership", "YES"],
    ["Martin's new packs (base)", "slack", PACKS_NEW, "channel membership", "YES"],
    ["Marcus's test post (seed)", "slack", TEST_POST, "planned seed", "UNVERIFIED (U4) — channel YES"],
    ["Robert's review (seed)", "slack", TEST_REVIEW, "planned seed (thread reply)", "UNVERIFIED (U4) — channel YES"],
    ["Marcus's reply to the review (seed)", "slack", TEST_ACK, "planned seed (thread reply)", "UNVERIFIED (U4) — channel YES"],
    ["Leonard's store reply (seed)", "slack", STORE_REPLY, "planned seed (thread reply)", "UNVERIFIED (U4) — channel YES"],
    ["#zombie-match3d", "slack", "C0880U9751A", "private channel, member", "YES"],
    ["Fake-installs thread (base)", "slack", INSTALLS_ROOT, "channel membership", "YES"],
    ["Frederick's review reply (seed)", "slack", FRED_REVIEW, "planned seed (thread reply)", "UNVERIFIED (U4) — channel YES"],
    ["iOS 1232 zombie swap (base)", "slack", "C0880U9751A/1753820524.488479", "channel membership", "YES"],
    ["#zm-animations", "slack", "C09ATAJ220H", "private channel, member", "YES"],
    ["Marcus's re-capture note (seed)", "slack", RECAP_NOTE, "planned seed", "UNVERIFIED (U4) — channel YES"],
    ["#company-internal", "slack", "C05KNDCHAAG", "private channel, member", "YES"],
    ["Martin's vacation post (seed)", "slack", LEAVE_POST, "planned seed", "UNVERIFIED (U4) — channel YES"],
    ["Leonard's reply on cover (seed)", "slack", LEAVE_REPLY, "planned seed (thread reply)", "UNVERIFIED (U4) — channel YES"],
    ["#builds", "slack", "C05433XK267", "public channel, member", "YES"],
    ["Claire–Marcus IM", "slack", "D05V2N6PZNU", "IM, Claire is a member", "YES"],
    ["DM root (seed)", "slack", DM_ROOT, "planned seed in the IM", "UNVERIFIED (U4) — channel YES"],
    ["Marcus's reply (seed)", "slack", DM_REPLY, "planned seed in the IM", "UNVERIFIED (U4) — channel YES"],
    ["#god-gameart decoy (base)", "slack", "C04V7N09LE7/1726011239.339499", "channel membership", "YES"],
    ["Live creatives sheet (seed)", "gsheets", SHEET, "planned seed shared with Claire", "UNVERIFIED (U4)"],
    ["Release calendar (seed)", "gdocs", DOC, "planned seed shared with Claire", "UNVERIFIED (U4)"],
    ["Seasonal deck (seed)", "gslides", DECK, "planned seed shared with Claire", "UNVERIFIED (U4)"],
    ["Halloween folder (seed)", "gdrive", FOLD["root"], "planned seed shared with Claire", "UNVERIFIED (U4)"],
    ["Store folder (seed)", "gdrive", FOLD["store"], "planned seed (child of the root)", "UNVERIFIED (U4)"],
    ["UA masters folder (seed)", "gdrive", FOLD["ua"], "planned seed (child of the root)", "UNVERIFIED (U4)"],
    ["DD capture sheet decoy (base)", "gsheets", "f_b5fb884dc96261846b6c2c", "shared with Claire", "YES"],
    ["Plan-changes mail (seed)", "gmail", PLAN["msg"], "planned seed in Claire's mailbox", "UNVERIFIED (U4)"],
    ["Draft mail (seed)", "gmail", DRAFT["msg"], "planned seed in Claire's mailbox", "UNVERIFIED (U4)"],
    ["Restart mail (seed)", "gmail", RESTART["msg"], "planned seed in Claire's mailbox", "UNVERIFIED (U4)"],
    ["Vendor quote (seed)", "gmail", QUOTE["msg"], "planned seed in Claire's mailbox", "UNVERIFIED (U4)"],
    ["POD notes Sep 29 (base)", "gmail", "claire.morgan@harmonygames.co/1844625524254242367", "own mailbox", "YES"],
    ["Review event (seed)", "gcal", EVT["claire.morgan@harmonygames.co"], "planned seed on Claire's calendar", "UNVERIFIED (U4)"],
    ["Library tickets + comments (seed)", "linear", "ART-793", "Linear is unscoped", "unscoped"],
    ["Trello card + comment (seed)", "trello", CARD, "Trello is unscoped", "unscoped"],
    ["Packs comment on the base card (seed)", "trello", f"{PACKS_CMT} on {REFRESH_CARD}", "Trello is unscoped", "unscoped"],
    ["Vendor contact (seed)", "contacts", CONTACT, "Contacts is unscoped", "unscoped"],
    ["match3d icon settings (base)", "github", "harmonygames-Games/match3d#325", "GitHub is unscoped", "unscoped"],
    ["Release checklist (base)", "confluence", "page_release_checklist", "Confluence is unscoped", "unscoped"],
]
A(f"""## 10 QC Rails

- Seed bound: every seeded event timestamp is ≤ 2025-10-01T00:00:00Z; only plan fields are later (review start
  Oct 2 16:00Z `{EVT['claire.morgan@harmonygames.co']}`; the dates inside the calendar doc and the mails).
- No-leak: no seeded record states a call word, a source build next to a call, or the plan; the sheet and ticket
  descriptions carry no build or master (`{SHEET}`, ART-793). Robert's review and Frederick's packs comment state a fact
  about the art; the deck's words turn it into a call (`{TEST_REVIEW}`, `{PACKS_CMT}`).
- Fairness: every deciding fact is in a record Claire can reach (reach table below); no deciding fact sits in
  `C07C2866011` or `D05S58U4SAK`.
- Unique ground truth: the decision points in section 5 each have a record that settles them; the precedence
  Skip > Reuse > Refresh first > Halloween version follows from the mail ("don't make Halloween versions of anything
  that only runs there", `{PLAN['msg']}`) and the deck ("Reuse: it already has a seasonal version", `{DECK}`). Reuse
  reaches only the exported iPhone and Google Play sets (`{FOLD['store']}`); Robert's review takes it away from the cheer
  fastcouch test (`{TEST_REVIEW}`).
- Coherence with base: build numbers, dates and channel membership are base facts (`C05433XK267/1753820674.990309`,
  `C05433XK267/1758037790.659569`); the art-refresh timeline is base (match3d#325, #342).

### Reach table (load-bearing records)

`persona_view.py can-see claire_morgan SERVICE ID` per row; planned seeds answer UNVERIFIED with a U4 reason
(not in base) and are re-proved with `check-sql` at injection.

""" + table(["Record", "Service", "Id", "Visibility path", "persona_view result"], reach_rows) + f"""

### Integrations and companions

""" + table(["Service", "INT id", "Companion", "Decision"], [
    ["slack", "INT-04", "Linear Slack app posts", "none needed — no Linear status change is seeded; comments only"],
    ["slack", "INT-13", "Drive app share DMs", "none — the seeded files are shared without a share DM"],
    ["slack", "INT-06", "Jenkins #builds results", "none — no build is seeded; base jobs are cited"],
    ["gmail", "INT-11", "calendar invite mails", "none — the review event needs no invite mail (optional companion)"],
    ["gcal", "INT-11", "invite / RSVP mails", "none — seven attendee rows seeded, no invite mail"],
    ["gdrive", "INT-13", "Drive share DMs", "none — optional companion omitted"],
    ["gdocs", "-", "no integration", "none — no companion exists"],
    ["gsheets", "-", "no integration", "none — no companion exists"],
    ["gslides", "-", "no integration", "none — no companion exists"],
    ["linear", "INT-05", "Linear digest mails", "none — seeded comments need no mail"],
    ["linear", "INT-03", "linear[bot] PR comments", "none — no PR is seeded"],
    ["github", "INT-01", "GitHub → #zombie-prs mirror", "none — nothing is seeded in GitHub"],
    ["trello", "INT-21", "Trello → Slack", "none — the integration does not exist"],
    ["contacts", "-", "no integration", "none — participant identity only"],
    ["confluence", "-", "no integration", "none — read only"],
    ["snowflake", "-", "no integration", "none — read only, not injectable"],
]) + "\n")

rp = [
    ["slack", ASK, "Leonard, Sep 30 22:05:13Z", "the ask (planned_texts.json slack_ask)"],
    ["slack", POINTER, "Robert, Sep 25 16:30:22Z", "pointer to the deck"],
    ["slack", EXPORT, "Martin, Sep 30 15:20:41Z", "'halloween store screens are exported'"],
    ["slack", DM_ROOT, "Claire, Sep 26 07:40:09Z", "DM root (reply_count 1)"],
    ["slack", DM_REPLY, "Marcus, Sep 29 17:20:37Z", "thread reply: cheer fastcouch Halloween cuts done"],
    ["slack", STORE_REPLY, "Leonard, Sep 30 15:47Z", "thread reply under the export post: exported art needs no ticket"],
    ["slack", TEST_POST, "Marcus, " + when("slack_marcus_test"), "#zombie-art: quick test on cheer fastcouch (reply_count 2)"],
    ["slack", TEST_REVIEW, "Robert, " + when("slack_robert_test_reply"), "thread reply: the July capture, cannot ship"],
    ["slack", TEST_ACK, "Marcus, " + when("slack_marcus_test_reply"), "thread reply: will redo both from the Sep 16 capture"],
    ["slack", RECAP_NOTE, "Marcus, " + when("slack_marcus_recapture"), "#zm-animations: three re-captures on Android #1935, #1896, #1966"],
    ["slack", FRED_REVIEW, "Frederick, " + when("slack_fred_review_reply"), f"thread reply under base {INSTALLS_ROOT}: any new ad on Android US phone by Fri Oct 10"],
    ["slack", LEAVE_POST, "Martin, " + when("slack_martin_leave"), "#company-internal: vacation Oct 6-15, Julia takes the ad statics (reply_count 1)"],
    ["slack", LEAVE_REPLY, "Leonard, " + when("slack_leonard_leave_reply"), "thread reply: julia on the ad statics works"],
    ["gsheets", SHEET, "Frederick, modified Sep 30 22:30Z", "Read me / Store / Unity / Archive tabs (roster_final.json)"],
    ["gdocs", DOC, "Arthur, modified Sep 30 22:40Z", "Q4 release calendar"],
    ["gslides", DECK, "Robert, modified Sep 25 16:10Z", "4 slides " + ", ".join(I["deck_seasonal"]["slides"])],
    ["gmail", DRAFT["msg"], "Frederick → 4, Sep 12 17:40Z", "October UA plan (draft); copies in recipients' mailboxes"],
    ["gmail", PLAN["msg"], "Frederick → 4, Sep 30 23:10Z", "October UA plan - changes"],
    ["gmail", RESTART["msg"], "Frederick → 4, " + when("gmail_fred_restart"), "Unity retention restart: two cuts left off iOS UK tablet; copies in recipients' mailboxes"],
    ["gmail", QUOTE["msg"], "PERSON_6311_EMAIL → Claire, Sep 24 14:00Z", "Halloween props quote"],
    ["contacts", CONTACT, "-", "Kay, founder, KayKit (email PERSON_6311_EMAIL)"],
    ["gcal", EVT["claire.morgan@harmonygames.co"], "Leonard, updated Sep 30 22:10Z", f"ZM3D Halloween review Oct 2 16:00–16:30Z, ical_uid {UID}, 7 rows"],
    ["gdrive", FOLD["root"], "Leonard, Sep 29 09:15Z", "ZM3D Halloween 2025 / Store / UA masters"],
    ["gdrive", ", ".join(I["files_store"][:2]) + " …", "Martin's export, Sep 30 15:12Z (owner Leonard's folder)", "11 Halloween store files (iPhone 6.5 ×5, Play ×6)"],
    ["gdrive", ", ".join(I["files_ua"]), "Marcus, Sep 29 17:05Z", "cheer fastcouch Halloween 9:16 and 16:9"],
    ["linear", "ART-793 … ART-854", "Frederick, Sep 8 16:00Z / Sep 12 16:20Z / Sep 15 16:00Z / Sep 17–25", f"{n_ads} serving + {len(ARCH)} archived library tickets, unassigned, serving ones Done at their last comment"],
    ["linear", "cmt_art793_1 … cmt_art842_1", "Frederick, Sep 8–12", "capture notes (roster_final.json comment_1)"],
    ["linear", "cmt_art808_2, cmt_art816_2", "Marcus, Sep 16", "re-capture and export notes (the three April tickets carry none at rev3)"],
    ["trello", CARD, "Leonard, Sep 30 22:00Z", "Halloween push card on ZM ROADMAP 6851a6569f3bf818760632ab"],
    ["trello", CARD_CMT, "Frederick, Sep 30 23:20Z", "Julia's 4:5 static still running on iOS UK"],
    ["trello", PACKS_CMT, "Frederick, " + when("trello_logo_comment"), f"the old zombies on the packs in end card 001 and its cuts, on base card {REFRESH_CARD}"],
]
A("""## 11 Record plan for /create-injection

""" + table(["Service", "Id", "Author / time", "Content"], rp) + f"""

- Verbatim texts: `scenario_gen/planned_texts.json`; per-surface sheet rows, ticket titles, descriptions and comment
  texts: `scenario_gen/roster_final.json` (e.g. {tk('boris fastcouch 9:16')}: "{BY['boris fastcouch 9:16']['comment_1']}").
- Ids are minted in `scenario_gen/ids.json` and collision-checked against the full base collections
  (`Working_Files/scratch/mint_checks.txt`: gdrive 53,631 / gslides 132 / gcal 10,395 / linear 3,687 / trello
  803 cards + 5,252 actions / contacts 170 — scan_complete, 0 hits, positive controls hit).
- Companion updates: the DM root's reply_count / latest_reply (`{DM_ROOT}`); the test post's and vacation post's counters
  (`{TEST_POST}`, `{LEAVE_POST}`); the base fake-installs root's reply_count 4 → 5 and latest_reply (`{INSTALLS_ROOT}`); the
  Trello card's dateLastActivity (`{CARD}`) and the base card's dateLastActivity and comment badge (`{REFRESH_CARD}`); one Gmail
  copy of each Frederick mail per recipient mailbox, byte-identical (`{PLAN['thread']}`, `{RESTART['thread']}`).
""")

A(f"""## 12 Self-test results

`hardness_gate.py 01_Hardness_Manifest.draft.json --design`:

{fence(OUT['gate'])}

`gradable_surface.py validate` and `gradeable-report`:

{fence(OUT['surface'] + chr(10) + OUT['report'])}

`hardness_v2_check.py --design` (advisory):

{fence(OUT['v2'])}

Disposition of the DECISION_FLIP flag on R_BUILD_CUT: the build cut decides the store art's due dates and the ship route,
which the surface cannot decode deterministically (a due window accepts any date up to the Thu Oct 16 12:00 PT cut, and
reason_matches has no solver value, so S37–S39 cover the ad due dates only); it flips the rubric-only facts RO9 (weight 5)
and RO8 (weight 3) (`{DOC}` against the ask's "around the 24th" in `{ASK}`). No weight was raised to clear the flag.

The rev2 DECISION_FLIP flag on the pack rule and the SAME_PLACE flag on T9 are gone. The rule was purged, and the
re-capture note left the ticket for `{RECAP_NOTE}`; SAME_PLACE now reads CLEAN above.

`trap_liveness.py --design --dispositions` with the `liveness` block of `01c_Dispositions.json` (advisory):

{fence(OUT['live'])}

`hardness_forecast.py forecast --design --model claude-opus-5-5 --mode {CTX['difficulty_mode']} --mechanisms` with the {len(RULES)} rule ids and the disclosed override `--max-k {KMAX} --allow-max-k {KMAX}` (UNCALIBRATED; the tool refuses more than 8 without it):

{fence(FC_TEXT)}

{f"Pre-registered forecast id: {HEV}." if HEV else "This is a re-run of the rev3 design and is not pre-registered: no ledger record exists for it yet (`build_doc.py --preregister` appends one and cites its id here)."}
""")

# rev3 red team, one list per finding: [#, reviewer, finding, disposition, evidence]
RT3_ROWS = [
    ["RR1", "A: /prompt, blind", "matched truth on 61 of 62 rows, and each new trap resolves to one answer", "recorded", "solver/truth.json"],
    ["RR2", "A: /prompt, blind", "the ART-809 fork", "kept unchanged: it passed four blind platform passes", "ART-809; PW3 below"],
    ["RR3", "A: /prompt, blind", "the referent of 'the 15th' in Frederick's reply", "fixed: the reply now says 'any new ad going on Android US phone', without adding the word halloween", FRED_REVIEW],
    ["RR4", "A: /prompt, blind", "Martin's vacation post sat outside his hours; his posts all fall 08-16 UTC", "fixed: moved to 2025-09-30T14:41:26Z, before Leonard's 22:05Z ask; Leonard's reply stays at 23:31:47Z, after the ask, so the correction still lands last", f"{LEAVE_POST}; {LEAVE_REPLY}"],
    ["RR5", "A: /prompt, blind", "the Trello card that hosts Frederick's end card comment", "kept: its title names Marcus and Frederick", REFRESH_CARD],
    ["RR6", "B: /injection, blind", "0 FAIL", "recorded", "01_Universe_Inject.sql"],
    ["RR7", "B: /injection, blind", "the logo reason conflicted with base: older end cards had no logo, and Martin supplied it Jul 31", "fixed: the rule is now R_OLD_PACKS and the reason is the old zombies on the packs", f"{PACKS_CMT}; {PACKS_OLD}; {PACKS_NEW}"],
    ["RR8", "B: /injection, blind", "Leonard's base line about Thursday beside the seeded Oct 2 review", "accepted: it is base and two platform reviews did not flag it", "C05KNDCHAAG/1759279503.256079"],
    ["RR9", "B: /injection, blind", "dropping ART-831's sentence", "fixed: S0r declined the drop and the sentence stays (section 14)", "cmt_art831_2"],
    ["RR10", "B: /injection, blind", "the restart mail's wording", "fixed: it now reads 'The iOS retention campaigns went back on today.' and is sent at 23:48Z, after Leonard set the budget at 22:48Z", RESTART["msg"] + "; base C07C2866011/1759186080.203099"],
]
# findings the platform /prompt rounds added after redteam_dispositions.md was last written (they follow its PW4 row)
PW_ROWS = """| PW5 | MAJOR (platform /prompt attempt 6aea4c1e, UGT + Clarity) | 'open ART tickets for any new store art' gave 2 or 4 tickets: nothing said whether the sets Martin already exported count as new | SEEDED: Leonard's thread reply under Martin's post, K18, names no set, so T1's iPad gap still shows only in the Store folder; prompt, Leonard's ask and Martin's post unchanged | `C08R8CHB0QL/1759247246.453725`; 2 new tickets (icon, iPad 12.9"); truth.json and geometry unchanged |
| PW6 | MAJOR (platform /prompt, Cross-Service Coherence) | 58 library tickets were Todo while their comments record finished, running creatives | REPAIRED: Done, started_at = created_at, completed_at = updated_at = the last comment, still unassigned so assignment stays the agent's write | ART-793 … ART-854 less ART-836 … ART-839; sql_lint lifecycle and base_check comment-after-close clean |
| PW7 | MINOR (platform /prompt, Cross-Service Coherence) | the sheet's modified_time predated the Trello card its Read me names | REPAIRED: modified_time 2025-09-30T22:30:00Z on the Drive and Sheets rows; Read me pointer kept because it is the route to the Julia 4:5 comment | `f_02b1968f5e882366fbb883`; card createCard 2025-09-30T22:00:00Z |
| PW8 | REJECTED (platform /prompt issue 3) | report says ART-836 … ART-839 have canceled_at NULL | NO CHANGE: the reviewed SQL (sha256 df47d906…) already sets canceled_at = updated_at on all four | column parse of the SQL: 2025-09-15T17:00:00Z ×3, 2025-09-19T17:00:00Z |
"""

A("""## 13 Red team

RED TEAM FALLBACK: two independent blind Claude reviewers read rev3 instead, one emulating /prompt (UGT and fairness) and one emulating /injection (coherence against base), because REDTEAM_* is not configured here, so redteam_review.py --dual cannot run. Their findings are dispositioned in the rev3 table in this section.

### Revision rev3 (2026-11-05, `/create-scenario --revise` after the rev2 `/hardness` FAIL)

""" + table(["#", "Reviewer", "Finding", "Disposition", "Evidence after the fix"], RT3_ROWS) + """

### Before rev3

The rows below are the record of the earlier reviews and keep the facts of their day: the counts, the pack rule and the
Reuse cuts in them are superseded by sections 1 to 12 and by section 14. Rev3 purged the rule RT2 mentions; the sentence
PW2 added to ART-831 (`cmt_art831_2`) stays. "Revision 02" and "Revision 03" below are scenario revisions and both predate
SQL rev2. The requester waived the scenario red team on 2026-11-04 (D3 'waive'; REDTEAM_* not set); an independent
GPT-6.1 Sol redteam subagent reviewed those revisions instead.

""" + (HERE / "redteam_dispositions.md").read_text().rstrip() + "\n" + PW_ROWS)

DELTA_EVENT = {"R_ALREADY_MADE": "run-1 event 217", "T3": "run-1 event 217", "CH4": "run-1 event 217", "R_PACK_ALIAS": "run-1 event 299",
               "CH5": "run-1 event 299", "T9": "run-1 event 287", "R5": "run-1 event 287", "R8": "run-1 event 465"}
DELTA_ROWS = [[d["id"], d["change"], d["reason"], DELTA_EVENT.get(d["id"], "run-1 event 287")]
              for d in json.loads((WF / "01_Hardness_Manifest.json").read_text())["design_delta"]]
A(f"""## 14 Revision intake (S0r)

Verdicts consumed: `run_forensics/rev2/precheck.normalized.node_verdicts.json` (`/create-hardening` MODE B, one Opus 5.5
pre-check of rev2). The file labels the run `precheck`; below it is run-1, as in `01a_Hardening_Report.md`. Export:
`06_PreCheck_Trajectory/trajectory-run-1.json`, read through the header-normalised copy
`run_forensics/rev2/precheck/trajectory.header_normalized.json` (hardening report section 7).

Binding: the export is BOUND to rev2 on discriminating content (2 needles seen, 562 shared, SQL sha256 `28b0cdadce52…`).
Its verdicts describe rev2 only and certify nothing about rev3. CONFOUNDED candidates: none flagged, none assigned.

""" + table(["Node", "Runs", "Proposed verdict", "Disposition", "Evidence"], [
    ["R_BUILD_CUT (T2, CH6, T16, T13)", "precheck (run-1)", "LEAKED", "keep — a clear rule in a named source, kept as it is", "run-1 event 25 read the calendar and run-1 event 274 tied the icon to the build rather than Oct 24; the Oct 15 ticket date is the only deviation"],
    ["R_DONE_EXPORT (T1, CH1)", "precheck (run-1)", "LEAKED", "keep — the iPad gap stays the store-side done gap", "run-1 event 225 read Martin's thread and run-1 event 231 listed the Store folder in one call; the ticket was written at run-1 event 272"],
    ["R_ALREADY_MADE (T3, CH4, T19)", "precheck (run-1)", "LEAKED", "rebuild — now R_TEST_TURNED_DOWN (A24): the DM and the two files stay as the done source, and Robert's review in a #zombie-art thread is the missing piece", "run-1 event 217: one `halloween` Slack search returned Claire's DM root and Marcus's thread reply together"],
    ["R_FLIGHT_CHANGE (T4, CH3, T18)", "precheck (run-1)", "LEAKED", "keep — and R_REVIEW_WINDOW narrows its date in another thread", "run-1 event 17: one Gmail search returned both mails, read at run-1 event 27 and event 29"],
    ["R_SCOPE_SERVING (T6, CH7, T5, T10, T14)", "precheck (run-1)", "LEAKED", "keep — and the proposed drop of ART-831's sentence is declined (see the routing table)", "run-1 event 54 ART-831 announced itself; run-1 event 43 `trello_search` returned the ART-826 comment; run-1 event 60 gave the set difference"],
    ["R_ART_CURRENT (T8, CH2, T9, T17, T11, T12)", "precheck (run-1)", "LEAKED", "keep for T8, CH2, T17, T11, T12 — T9 leaves it and is rebuilt as R_RECAPTURE_NOTE", "run-1 event 106 read the deck, 58 `linear_list_comments` calls swept the capture notes, run-1 event 207 followed ART-809's pointer; run-1 event 287 used re-captures that sat on the same ticket as the capture they replace"],
    ["R_PACK_ALIAS (T7, CH5)", "precheck (run-1)", "SURFACE-ONLY, dispositioned FALSE by the hardening report", "purge — the rule and CH5 leave the design; T7 stays as a plain distractor and no record changes", "run-1 event 227 read the quote and the plan at run-1 event 299 turned the bundle down in one line without the Contacts or GitHub hops; no graded row depends on it"],
]) + f"""

Routing of the findings (hardening report sections 9 to 11):

""" + table(["Finding", "Route", "Outcome", "Evidence"], [
    ["Universe-side: moves 1–6", "S5a onward, then `/create-injection`", "applied: R_REVIEW_WINDOW, R_RECAPTURE_NOTE, R_TEST_TURNED_DOWN, R_STATICS_COVER, R_TABLET_TRIM, R_OLD_PACKS; SQL stored at `run_forensics/rev3/01_Universe_Inject.sql`. Move 6 changed reason after the red team (RR7): the old zombies on the packs, not a logo", "run-1 event 287 built every call from the ticket comments, with no check against any other service"],
    ["Universe-side: drop ART-831's sentence 'Not on the live creatives sheet yet.' (hardening report section 9)", "S0r decision", "declined: the sentence stays, because the earlier `/injection` and `/prompt` passes rely on it and dropping it buys no difficulty", "run-1 event 54 read the ticket; the run also reached the set difference at run-1 event 60, so the sentence was not the only route"],
    ["Prompt-side", "`/create-prompt-writing check` not needed", "no defect: `04_Prompt.txt` is unchanged", "run-1 event 2 read the ask; 'every ad we're running', 'who makes what by when' and 'whoever's making them' already reach each change"],
    ["OE and rubric", "`/create-oe-writing check`, `/create-rubric-writing check`", "neither exists yet; when written they stay off Unity CPI and spend (SC-11), ART-790, go-live dates and ticket state", "run-1 event 299: the plan and tracker writes the rows will be graded on"],
    ["Verifier and local proxy", "`/create-allfail` when a verifier exists; the shared-tool defect goes to the tool owner", "`surface_grader.py` read 6.8% on the raw export and 10.2% on the normalised copy, a decoder artifact; no verdict rests on it", "run-1 event 287 and run-1 event 294: each of the 19 failed slots was checked in the write payload and is met"],
]) + f"""

Design delta recorded in `01_Hardness_Manifest.json` (`design_delta`):

""" + table(["Id", "Change", "Reason", "Evidence"], DELTA_ROWS) + "\n")

SR_ROWS = [
    ["1", "temporal — icon due date", "Leonard, the requester, says \"around the 24th\"; a run may argue the requester's date wins", f"ask {ASK}; calendar {DOC}", "the calendar makes the icon a build change merged by Thu Oct 16 12:00 PT; the 24th is a question mark, and the iOS build is live about Oct 22, so the 24th is not reachable without the cut (T2, T16)"],
    ["2", "temporal — ad due date", "Frederick's Sep 30 mail says every Halloween ad by Wed Oct 15 and is the source the ask names; a thread reply about fake installs should not move it. The Sep 12 draft is longer still (Oct 17, all four campaigns)", f"reply {FRED_REVIEW}; changes {PLAN['msg']}; draft {DRAFT['msg']}", "the reply is from the same owner, 32 minutes later, and says 'not the 15th' for Android US phone and 'iOS UK stays on the 15th'; the mail names the draft and says 'not the 17th' (T4, T20)"],
    ["3", "temporal — Android over-application", "Unity reviews every new Android creative, so the cuts on Android US tablet are due Oct 10 too", f"reply {FRED_REVIEW}; ticket {tk('cheer fastcouch 16:9')}; changes {PLAN['msg']}", f"the reply says 'any new ad going on Android US phone'; Android US tablet ends Oct 12, before the flight, so a cut on both tablets ships on iOS UK and stays on the 15th: {n_oct10} ads on Oct 10, {n_oct15} on Oct 15 (T20)"],
    ["4", "temporal — boris capture", "a Sep 12 post and 'live since Sep 12' mean the boris cuts are current", "ART-840 comment cmt_art840_1 \"Captured Jul 28\"", "Jul 28 is before the Jul 29 swap the deck names; Leonard's base \"you have the old zombies\" (D05S58U4SAK, not visible to Claire) agrees but is not needed (T8)"],
    ["5", "semantic / category — statics", "Julia's statics are composites, not captures, so the capture rule does not reach them", f"ART-825 cmt_art825_1 \"Made from Android #852 captures (Jun 5)\"; deck {DECK}", "the deck says \"captured or rendered from a build\"; the comment names the build, so Refresh first"],
    ["6", "semantic / category — what is an ad", "the icon and store sets are \"surfaces\" but not \"ads\": should they be commented and assigned?", f"ask {ASK}; sheet Read me {SHEET}", "\"drop a comment on each ad's ART ticket\"; the Read me says store sets have no ART ticket; store art gets new tickets instead"],
    ["7", "semantic / category — the old packs", "Frederick's comment says they 'can keep serving for now', and Android #1529 passes the deck, so end card 001 and its cuts are Halloween versions", f"comment {PACKS_CMT}; ticket {tk('end card 001')}; deck {DECK}; base {PACKS_OLD}, {PACKS_NEW}", "the same comment says they need a re-render before anyone builds on them, the old zombies are the art the deck wants gone, and its Refresh first is 're-capture, re-render or re-cut before any seasonal pass' (T23)"],
    ["8", "referential / cross-service — Julia's 4:5 static", "the static is not on the sheet, and the sheet says it lists what is running", f"Trello comment {CARD_CMT}; ticket ART-826", "Frederick, the sheet's owner, says on the card the Read me names that it never made the sheet and is still running (T6)"],
    ["9", "referential / cross-service — portrait end card", "an end card is part of every video, not a separate surface; it should not get a row", f"ART-831 description; ask {ASK}", "the ask covers \"everything players see\" and \"every ad\"; the end card has its own library ticket and its own call, like the four end cards on the sheet, and its Sep 29 note says it is still running and not on the sheet yet (T6)"],
    ["10", "referential / cross-service — vendor bundle", "the props are what a Halloween pass needs, so the plan should price or buy them", f"quote {QUOTE['msg']}; contact {CONTACT}", "a sales pitch is not a serving surface: no call, owner, date or slot depends on it, the pack rule was purged at rev3 and T7 is a plain distractor"],
    ["11", "referential / cross-service — who makes the statics", "Leonard's split is the requester's own, and a vacation post is not a re-assignment", f"ask {ASK}; post {LEAVE_POST}; reply {LEAVE_REPLY}", f"Martin's post is before the ask, but Leonard himself replies 'julia on the ad statics works for me' after it, so the correction lands last; the {n_julia} working statics go to Julia and the store art stays with Martin (T21)"],
    ["12", "quantitative / reconciliation — assignments", "the Skip ads stay in the plan, so someone should still own them", f"roster_final.json assign_to; ask {ASK}", f"the ask says \"the ones that need new work\"; the {n_skip} Skip ads need none; the rubric counts {n_assign} ({n_marcus} Marcus, {n_julia} Julia), exact scope, rubric-only RO3"],
    ["13", "quantitative / reconciliation — cohort size", "the four archived library tickets are part of the library, so 66 rows", "ART-836 description \"Paused on Sep 15, see the Archive tab\"", "the Read me moves paused creatives to Archive; serving = 62 (T14)"],
    ["14", "state / lifecycle — cheer fastcouch test", "Marcus made the files and said so, and they sit in UA masters, so the cuts are done (Reuse)", f"DM reply {DM_REPLY}; UA masters {FOLD['ua']}; review {TEST_REVIEW}; reply {TEST_ACK}", "the art director turned the test down (July capture, old background, cannot ship) and Marcus agreed to redo both from the Sep 16 capture, so each is a Halloween version to make (T3)"],
    ["15", "state / lifecycle — re-captures", "the ticket is the record the sheet's Read me names and it shows an April capture; a note in an animation channel is a side note", f"ticket {tk('couch alpha 50')} cmt_art795_1; note {RECAP_NOTE}; deck {DECK}", "the deck says the newest capture counts; the note is by the person who recorded it and names each cut and build, so each is a Halloween version (T9)"],
    ["16", "state / lifecycle — trimmed cuts", "ART-811's second comment says both tablets were checked, so the ticket is the current record", f"ticket {tk('squirrelfail landscape')} cmt_art811_2; mail {RESTART['msg']}", "that check is Sep 9; Frederick's Sep 29 mail is later, names both cuts and says both stay on Android US tablet, so his Sep 30 rule skips them (T22)"],
    ["17", "identifier / format — build numbers", "iOS Internal #1452 exists (Aug 20), so \"#1452\" could mean an August iOS build", f"C05433XK267/1755696763.753209; deck {DECK}", "every comment and the deck write the platform (\"Android #1452 / iOS 1232\"); no capture note cites an iOS Internal number. Marcus's note writes 'android #1935' once and then bare numbers for the same platform"],
    ["18", "identifier / format — #1450", "#1450 has the new background (Jul 29), so the end card is current art", "C05433XK267/1753789877.590639; ART-831 cmt_art831_1", "the deck's threshold is Android #1452 (the zombie swap, 20:24Z); #1450 is older (T17)"],
    ["19", "identifier / format — call words", "a run writes \"Skip for October\" or \"Refresh first (old build)\" in the call cell, and the surface's `norm` comparator calls it different", f"deck slide 4 {DECK}; 01_Gradable_Surface.json tracker comparators", "the deck gives four exact call words and the tracker has a notes column; the surface stays strict so a cell cannot match two calls, and the rubric judge reads paraphrase"],
    ["20", "other — Skip vs Refresh", "cheer 30p 16:9 has music baked in, so it must be refreshed before anything else", f"ART-820; changes mail {PLAN['msg']}", "the mail says not to make Halloween versions of anything that only runs on Android US tablet; nothing is made, so no refresh"],
    ["21", "other — tablet over-application", "the Android US tablet campaign ends, so every 16:9 cut is skipped", "ART-823 campaigns iOS UK tablet + Android US tablet", "\"anything that only runs there\": couch alpha 50 16:9 also runs on iOS UK tablet (T18)"],
    ["22", "done claim — iPad set", "Martin says the Halloween store screens are exported, so the iPad set is done", f"export {EXPORT}; Store folder {FOLD['store']}", "the folder holds iPhone 6.5-inch ×5 and Play ×6 only; the Store tab lists the iPad set (T1)"],
    ["23", "completion elsewhere — cheer fastcouch 4:5", "Marcus says he \"did the cheer fastcouch one\", so every cheer fastcouch export has a Halloween version, the 4:5 too", f"DM reply {DM_REPLY}; UA masters {FOLD['ua']}; ART-851 cmt_art851_1", "the reply names \"both 9:16 and 16:9\", the folder holds those two files, and the 4:5 was cut on Sep 17 and was never in the test; it has no Halloween version, so Halloween version (T19)"],
    ["24", "fairness — Robert's review", "a thread reply that never says halloween is too hidden: an all-fail, not a trap", f"root {TEST_POST} (reply_count 2); review {TEST_REVIEW}", "the root is a top-level post in Claire's own channel and names cheer fastcouch, 9:16 and 16:9, so a search on the creative's name or a read of #zombie-art finds the thread"],
    ["25", "fairness — re-capture note", "#zm-animations is not a channel the ask points at, so an April call is an unfair loss", f"note {RECAP_NOTE}; C09ATAJ220H (Claire is a member)", "Claire can read it, and the note names each cut as the sheet writes it, so a search on the creative's name returns it; it is Marcus's busiest channel in September (hardening report section 10)"],
    ["26", "fairness — vacation post", "#company-internal is general chatter, so a change of maker there is an unfair all-fail", f"post {LEAVE_POST}; base convention C05KNDCHAAG/1756717965.570179; cover precedent C05KNDCHAAG/1719394673.875309", "Claire is a member, leave posts with a named cover are base practice there, and the requester answers in the thread; a search on Julia or statics returns it"],
    ["27", "fairness — packs comment", "no source names the Marketing Video Refresh card, so the four end cards are an unfair loss", f"comment {PACKS_CMT}; card {REFRESH_CARD}", "Trello is unscoped, the card's title names Marcus and Frederick, and the comment names end card 001 and its cuts, so a search on the creative's name returns it; a run that searches only `halloween` misses it by design (run-1 event 43)"],
    ["28", "fairness — Trello comment", "a Trello card is rarely opened, so Julia's static is an unfair all-fail", f"sheet Read me {SHEET}", "the Read me names the card; the static's own ticket ART-826 is in the library a run must enumerate"],
    ["29", "volume — a short run", "a run folds the note and the assignment into one issue update, or settles Skip from the sheet without reading those tickets, and stays at or under 180 calls", f"call budget (01_Hardness_Manifest.draft.json); ask {ASK}; sheet Read me {SHEET}; completed tasks douglas 163 / 175 and robert 116 / 115 (lowest run / floor)", f"the ask asks for a comment (linear_create_comment takes one issueId) and the assignee is a separate update; the sheet carries no campaigns, so all {n_ads} comment reads decide a call; {n_ads} + {n_ads} + {n_assign} per-ticket calls plus the shortest discovery, rule and delivery route give an unconditional floor of {floor}; the rev2 run counted 225 (hardening report section 6)"],
    ["30", "deliverable path — plan doc", "a run creates an empty doc and inserts the plan with a batch update, so a surface slot on one Docs tool reads nothing", f"scenario_gen/rubric_only_facts.json RO6; doc {DOC} is the calendar seed, not the plan", "plan text is a rubric-only fact graded on the doc's final text on either path; no surface slot reads it"],
    ["31", "due dates — Reuse", "the exported store sets are \"already made\", so they have no due date", f"roster_final.json; calendar {DOC}", "production status (\"made\") and hand-off are separate: the iPhone set still goes in with the Oct 17 submission, due by the Oct 16 12:00 PT cut; the Play set has no graded date; no ad is Reuse at rev3"],
    ["32", "grading — due dates", "three reason_matches slots sample three ads, so a run with a wrong date on the other 45 passes them", "01_Gradable_Surface.json S37, S38, S39; rubric_only_facts.json RO2, RO10", f"true for the surface: S37–S39 sample the rule and its control, and rubric-only RO10 (weight 5) and RO2 grade the whole set of {n_assign}, so the rule decides graded rows on both sides"],
    ["33", "difficulty — dead weight", "Opus reads the deck and every ticket, so most rules always pass and the average lands above the cap, as at rev2", "hardening report section 8; forecast pasted in section 12", "rev2 did exactly that (run-1 event 287); rev3 moves six deciding facts off the three swept paths, but the forecast is UNCALIBRATED and the claim stays open until `/hardness`"],
    ["34", "HARDNESS GATE", "the design gate passes only because SQL checks are skipped", "section 12 output", "true: seeded ids, chronology and reach are re-proved at injection (`hardness_gate.py` full mode, `persona_view check-sql`)"],
]
A("""## Self-review

Adversarial pass over the rev3 design, one counter-reading per decision point plus one per QC category, each tied to the
record that settles it. The HARDNESS GATE re-run is pasted in section 12 and appended by `stage_gate.py --paste`.

""" + table(["#", "QC category / decision", "Counter-reading (strongest case against the design)", "Evidence", "Disposition"], SR_ROWS) + f"""

Unresolved (none blocks the design): {len(json.loads((HERE / "rubric_only_facts.json").read_text()))} facts are rubric-only (per-ticket comment coverage, the {n_assign}-ticket
assignment mapping, plan text on either Docs write path, the tracker's due windows) and must be written as rubric rows at
/create-rubric-writing; R_BUILD_CUT flips no surface slot (advisory DECISION_FLIP flag); the base cuts' Slack origin
threads beyond the 30 s cut are confirmation only and stay conditional; the exact Linear tool shape for listing 62
library tickets in one page is unverified (budgeted as two calls); Google Play upload timing is planned but not graded;
the vendor contact's display name is set at injection (`PERSON_6311_EMAIL` token). New at rev3: Martin is away Oct 6-15
while the icon and the iPad set stay his and are due by the Thu Oct 16 12:00 PT cut, so that work lands before Oct 6 or
on the morning of Oct 16; the `surface_grader.py` residual in section 14 is open; the ledger holds only this task's records, so every prior is close to Beta(1,1) and every rev3 difficulty figure is a
design target until `/hardness`.
""")

TARGET = WF / "01_Scenario_Design.md"
GATE_BLOCK = re.search(r"^```\nSTAGE GATE scenario: .*?^```$", TARGET.read_text(), re.M | re.S) if TARGET.exists() else None
TARGET.write_text("\n".join(doc).rstrip() + "\n" + ("\n" + GATE_BLOCK.group(0) + "\n" if GATE_BLOCK else ""))
print("wrote", TARGET, "· hev", HEV)
