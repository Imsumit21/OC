#!/usr/bin/env python3
"""Assemble Working_Files/04_Prompt_Writing_Brief.md from prompt_gen/brief_template.md, the discovery-map rows below and
the verbatim research outputs of prompt_gen/run_research.py (research/sap_raw.txt, sap_rows.json, entity_raw.txt). The rev3
counts are asserted against solver/truth.json, and the must-not-appear words are scanned against 04_Prompt.txt, so neither can
drift. Never executes SQL.

    python3 -B Task_Authoring/task_inputsN2/Working_Files/prompt_gen/run_research.py
    python3 -B Task_Authoring/task_inputsN2/Working_Files/prompt_gen/build_brief.py
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
R = HERE / "research"

PLAN = "claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>"
DRAFT = "claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>"
QUOTE = "claire.morgan@harmonygames.co/<CAJec750be2c45f33a4016dbe77be0056@mail.gmail.com>"
RESTART = "claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>"

# Fact · Value · Locator · Persona-readable · Met first / overturned by · Search risk · Name in prompt?
DM = [
    ("1 · Leonard's Halloween ask", "scope (everything live, store pages and every ad), sources, owner split, follow-through, deadline; 'maybe … around the 24th?'", "`C06DJBJL798/1759269913.882683`", "YES (#zombie_marketing member)", "met first (the prompt's anchor); its icon question is overturned by row 3, its stills owner by row 34", "agents latch onto the requester's date and owner split", "Yes — anchor A1, as 'his message' in #zombie_marketing (the persona knows it)"),
    ("2 · Live creatives sheet", "Store tab (4 surfaces), Unity tab (56 ads, each with its ART ticket), Archive (4 paused); Read me: campaigns, capture and master notes are in the ticket comments", "`f_02b1968f5e882366fbb883`", "YES (shared reader)", "met first as the list; overturned for scope by rows 27 and 30", "agents treat the sheet's rows as the whole scope", "No (the ask names it; the prompt does not)"),
    ("3 · Arthur's release calendar", "merge cut Thu Oct 16 12:00 PT; iOS screenshots with the Oct 17 submission; Play graphics any day; Nov 6 clean-up incl. the icon", "`f_fdd6d2d2f4a4d2f5b908fb`", "YES (shared reader)", "overturns the ask's 'around the 24th'", "found by title only; agents stop at the requester's suggestion", "No"),
    ("4 · Robert's pointer", "the seasonal direction is in his deck, for all marketing art", "`C08R8CHB0QL/1758817822.269981`", "YES (#zombie-art member)", "connecting", "a Slack search for 'seasonal' also returns 2024 Domino Delights posts", "No"),
    ("5 · Robert's seasonal deck", "pre-swap captures (older than Android #1452 / iOS 1232) refresh first; newest capture counts; a cut whose master has the music baked in is re-cut first from a master without music; the four calls", "`f_5ebf55ad29e815d46243c8`", "YES (shared reader)", "the governing rule (hidden authority H3)", "deck text is read once; the per-ticket application is where runs slip", "No (root cause)"),
    ("6 · Frederick's Sep 30 changes mail", "Android US tablet ends Oct 12 (skip what only runs there); flight Oct 18–31; ads with him by Wed Oct 15", f"`{PLAN}`", "YES (own mailbox)", "met second, after the draft; overturns row 7; overturned for Android US phone by row 31", "a search for 'October UA plan' returns both; it reads as the last word", "No"),
    ("7 · Frederick's Sep 12 draft", "Oct 20–31 on four campaigns; due Fri Oct 17", f"`{DRAFT}`", "YES (own mailbox)", "met first; superseded by row 6", "stale value met first", "No"),
    ("8 · Martin's export claim", "'halloween store screens are exported to the halloween folder'", "`C08R8CHB0QL/1759245641.309714`", "YES (#zombie-art member)", "claim met first; overturned by row 9", "agents stop at a message that sounds done", "No"),
    ("9 · Halloween Store folder", "Halloween iPhone 6.5 ×5 and Google Play ×6, no iPad set", "`d_74a7c95c28097dd9777e01` (in `d_272d849cde40c35980a433`)", "YES (shared writer)", "overturns row 8", "base 'Halloween' Drive hits are all hidden by ACL; the seeded tree is the only visible one", "No"),
    ("10 · UA masters files", "cheer_fastcouch_halloween 9x16 and 16x9: Marcus's test, turned down", "`f_dc5cf9e4250d433c1511ec`, `f_bcd34f98925e3f20d846ce` in `d_6c2e4339e5d58108799ac8`", "YES (shared)", "decoy with row 11; overturned by row 33", "the files look finished", "No"),
    ("11 · Marcus's IM reply", "'did the cheer fastcouch one, both 9:16 and 16:9': a done claim, no longer the answer", "`D05V2N6PZNU/1759166437.080255`", "YES (Claire's IM)", "met first (a `halloween` or `cheer fastcouch` search returns it); overturned by row 33", "agents stop at a message that sounds done", "No"),
    ("12 · Halloween push card", "Leonard's card on the roadmap (named by the sheet's Read me)", "Trello `68dc52e015f87c50c441d1a9`", "YES (Trello unscoped)", "connecting", "a board-wide search floods (ZM ROADMAP)", "No"),
    ("13 · UA creative library tickets", "one ticket per ad; comments carry campaigns, capture build, master audio", "`ART-793` … `ART-854` (team_ART)", "YES (Linear unscoped)", "per-record evidence and the write target", "no bulk comment read; one call per ticket", "No ('each ad's ART ticket' only)"),
    ("14 · April capture notes on the three re-captured cuts", "Android #456 / #633, April; rev3 removed the ticket's second comment, so these now read as final", "`cmt_art795_1`, `cmt_art797_1`, `cmt_art805_1`", "YES (Linear unscoped)", "met first; overturned by row 32", "the only comment on the ticket reads as final", "No"),
    ("15 · Vendor quote", "a Halloween Bits bundle, 39 USD, reply by Oct 3", f"`{QUOTE}`", "YES (own mailbox)", "plain distractor since rev3 (R_PACK_ALIAS purged, no graded row)", "a 'Halloween' mail search returns it first", "No"),
    ("16 · Vendor contact", "PERSON_6311 — Founder, KayKit", "Contacts `6b350edd259a8b4499a9e625`", "YES (unscoped)", "conditional read; no graded row", "agents skip Contacts", "No"),
    ("17 · KayKit Halloween Bits pack owned", "already in the match3d repo (Robert: 'we have the Halloween pack', `C0880U9751A/1738109783.735889`)", "GitHub `/reviews/2166/body` (path `Assets/ThirdParty/3D Characters/KayKit/Packs/Bits/KayKit - Halloween Bits (For Unity)`); `C0880U9751A/1738109783.735889`", "YES (unscoped)", "conditional read; no graded row", "found only by the pack name", "No"),
    ("18 · Halloween review", "Thu Oct 2 16:00–16:30Z (9:00 PT); attendees Leonard (dialling in from LA), Frederick, Martin, Marcus, Robert, Arthur, Claire (not Julia)", "`evt_d947bf7cd910549b674b1f`", "YES (own calendar copy)", "deadline and audience", "none", "Yes — 'Thursday's review' (the persona's own meeting; the ask names it)"),
    ("19 · 30 s cut master thread", "Frederick: 'the background music is baked in'", "`C06DJBJL798/1755114007.441789`", "YES (#zombie_marketing member)", "evidence for the marcus.bennett cuts' tickets", "reached only from the ticket's note", "No"),
    ("20 · #builds Android #1452", "Match3D Android #1452 ZombieSwap, Jul 29 20:24Z", "`C05433XK267/1753820674.990309`", "YES (#builds member)", "dates the deck's threshold", "near miss #1450 at 11:51Z", "No"),
    ("21 · Robert's iOS 1232 post", "zombie swap completed with new background", "`C0880U9751A/1753820524.488479`", "YES (#zombie-match3d member)", "dates the threshold", "none", "No"),
    ("22 · Leonard's Sep 3 export ask", "export app store assets for iphone / ipad / gp", "`C06DJBJL798/1756914854.743319`", "YES (#zombie_marketing member)", "confirms the three live sets", "rank 3 behind older noise", "No"),
    ("23 · ART-774", "Mar–Apr store screenshot spec (Done)", "`ART-774`", "YES (unscoped)", "decoy (older spec)", "deep in a 'screenshot' search", "No"),
    ("24 · Robert's Halloween pack mention", "'we have the Halloween pack'", "`C0880U9751A/1738109783.735889`", "YES (#zombie-match3d member)", "conditional read; no graded row", "none", "No"),
    ("25 · Martin's Sep 17 icon concept", "'*Halloween theme* for an app icon or an event' + AppIconHalloween.png", "`C08R8CHB0QL/1758121809.236839`", "YES (#zombie-art member)", "claim met first; overturned by row 29", "the image reads as a finished icon", "No"),
    ("26 · 1.3.38 release", "'1.3.38 is out!' (the Store tab's 'Live since Sep 17')", "`C0880U9751A/1758141269.804779`", "YES (#zombie-match3d member)", "grounds the store sets' dates", "none", "No"),
    ("27 · Julia's 4:5 static", "still running on iOS UK, never made the sheet, count it in", "Trello `68dc65a0f2d7fb28743f5860` on `68dc52e015f87c50c441d1a9`", "YES (unscoped)", "overturns the sheet as scope", "a card comment, not the card", "No"),
    ("28 · Portrait end card ticket", "plays after every Android US phone video (rendered from Android #1450)", "`ART-831`", "YES (unscoped)", "off-sheet serving ad", "found only by listing the library", "No"),
    ("29 · Robert's icon reply", "'Nice for an event, but not for the app icon, it gets too busy at that size'", "`C08R8CHB0QL/1758127951.679146` (thread reply under `C08R8CHB0QL/1758121809.236839`)", "YES (#zombie-art member)", "overturns row 25", "agents rarely open thread replies", "No"),
    ("30 · Frederick's end-card note", "'Still running on Unity: Android US phone (checked Sep 29). Not on the live creatives sheet yet.'", "`cmt_art831_2` on `ART-831`", "YES (unscoped)", "settles row 28's scope", "second comment on the ticket", "No"),
    ("31 · Frederick's Android date reply (R_REVIEW_WINDOW)", "'any new ad going on Android US phone has to be with me by Fri Oct 10, not the 15th. iOS UK stays on the 15th.' Unity reviews new Android creatives by hand, about 5 days each", "`C0880U9751A/1759275738.984915` (thread reply under base `C0880U9751A/1759211437.306779`, #zombie-match3d, Sep 30 23:42Z)", "YES (#zombie-match3d member; check-sql YES)", "overturns row 6 for Android US phone; 30 of the 48 working ads", "a `halloween` or `October UA plan` search does not reach it (neither phrase is in the text); it sits in a thread about bot installs; natural searches: `Unity`, `fake installs`, or reading #zombie-match3d", "No (root cause, never in the prompt)"),
    ("32 · Marcus's re-capture note (R_RECAPTURE_NOTE)", "'re-recorded 3 of the old ua cuts for frederick, same edits, no music: couch alpha 50 on android #1935, barrel marketing2 4:5 on #1896, balloons alpha 50 (1) on #1966'", "`C09ATAJ220H/1758823964.738872` (#zm-animations, Sep 25 18:12Z)", "YES (#zm-animations member; check-sql YES)", "overturns row 14 under row 5's newest-capture rule; three calls become Halloween version", "a `halloween` search does not reach it; the ticket holds no pointer; natural searches: the creative's name (`couch alpha 50`, `barrel marketing2`, `balloons alpha 50 (1)`) or reading #zm-animations", "No (root cause, never in the prompt)"),
    ("33 · Robert's test review (R_TEST_TURNED_DOWN)", "Marcus's post: 'quick test on cheer fastcouch, 9:16 and 16:9, pumpkins and fog over the cut. files are in ua masters'; Robert: 'this is the July capture … We can't ship these, they need doing again from the Sep 16 one'; Marcus: 'ok, i will redo both from the sep 16 capture'", "`C08R8CHB0QL/1759167065.499092`, replies `C08R8CHB0QL/1759248337.170599`, `C08R8CHB0QL/1759249269.380507` (#zombie-art)", "YES (#zombie-art member; check-sql YES)", "overturns rows 10 and 11; cheer fastcouch 9:16 and 16:9 go from Reuse to Halloween version, assigned to Marcus", "a `halloween` search does not reach it (the post says pumpkins and fog); natural search: the creative's name `cheer fastcouch`, then the thread; agents rarely open replies", "No (root cause, never in the prompt)"),
    ("34 · Martin's vacation post and Leonard's reply (R_STATICS_COVER)", "'I'll be on vacation Oct 6-15. <@EMPLOYEE_0005_SLACK_ID> takes the ad statics while I'm out, store art stays with me.'; Leonard: 'thanks martin. julia on the ad statics works for me'", "`C05KNDCHAAG/1759243286.478812`, reply `C05KNDCHAAG/1759275107.322377` (#company-internal, Sep 30)", "YES (#company-internal member; check-sql YES)", "overturns row 1's 'Martin has … the stills' for the six working statics; Leonard's reply lands after the ask", "a `halloween` search does not reach it; a company channel, no creative named; natural searches: `vacation`, `ad statics`, or reading #company-internal, where Leonard's base post `C05KNDCHAAG/1759279503.256079` sits about an hour after his reply; the review's description covers it (§12)", "No (root cause, never in the prompt)"),
    ("35 · Frederick's restart mail (R_TABLET_TRIM)", "'I left squirrelfail landscape and mrfluffernot landscape off iOS UK tablet this time … Both stay on Android US tablet.'", f"`{RESTART}` (subject 'Unity retention restart', Sep 29 23:48Z)", "YES (own mailbox; check-sql YES)", "overturns the campaign notes `cmt_art811_1`, `cmt_art811_2`, `cmt_art813_1`; row 6's rule then makes both Skip", "a `halloween` or `October UA plan` search does not reach it; natural searches: the creative's name (`squirrelfail landscape`, `mrfluffernot`) or `Unity`", "No (root cause, never in the prompt)"),
    ("36 · Frederick's packs comment (R_OLD_PACKS)", "'end card 001 still has the old zombies on the packs, Martin's new packs came after Marcus rendered it. Same on the 16:9, 1:1 and 4:5 cut from it. They can keep serving for now but they need a re-render before anyone builds on them.'", "Trello `68d6cff0c6568da5d9c8e81f` on base card `68768a1501ae552dbee94b8a` (Marketing Video Refresh, ZM ROADMAP, Sep 26 17:40Z); base lineage `C08R8CHB0QL/1754310794.907609`, `C08R8CHB0QL/1754316299.381419`", "YES (Trello unscoped; present in the SQL)", "overturns 'Rendered from Android #1529' (`cmt_art833_1`, `cmt_art834_1`, `cmt_art835_1`, `cmt_art848_1`); four calls become Refresh first under row 5's call words", "a `Halloween` Trello search does not reach it; the build passes the deck's rule, so nothing prompts a second look; natural searches: `end card 001` (the creative's name), `Marketing Video Refresh`, or reading the ZM ROADMAP cards", "No (root cause, never in the prompt)"),
    ("37 · Leonard's store-ticket reply", "'whatever is already exported is done so no tickets needed for those, tickets are just for store art that still has to be made'", "`C08R8CHB0QL/1759247246.453725` (thread reply under `C08R8CHB0QL/1759245641.309714`)", "YES (#zombie-art member; check-sql YES)", "narrows row 1's 'open tickets for any new store art'; settles the iPhone and Play sets", "reached by opening row 8's thread", "No"),
]

def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "| " + " | ".join("---" for _ in head) + " |"]
    return "\n".join(out + ["| " + " | ".join(c.replace("|", "/") for c in r) + " |" for r in rows])


def fences(raw: str) -> str:
    """Split a research log into one fenced block per tool run, each opening on the tool's own header line (so the
    gate reads it as tool output); the '### n' labels stay outside the fences as plain text."""
    head = re.compile(r"^\s*(SEARCH \w+ |OVERLAY \w+ |SHARED_FIRST_NAMES|ENTITY |CHECK-SQL as |no exact match|[a-z_]+ (?:gmail|slack|gcal|gdrive|gdocs|gsheets|gslides) \S+: )")
    out, block, label = [], [], None
    def flush():
        if block and head.match(block[0]):
            out.extend(([f"Run {label}:", ""] if label else []) + ["```text"] + block + ["```", ""])
        elif block:   # a non-persona_view helper output (hg.py JSON, notes): kept in the research log, cited here
            out.extend([f"Run {label}: helper output kept verbatim in `Working_Files/prompt_gen/research/` (not a persona_view run).", ""])
    for line in raw.rstrip().splitlines():
        if line.startswith("### "):
            flush()
            block, label = [], line[4:].strip()
            continue
        if not block and not line.strip():
            continue
        block.append(line)
    flush()
    return "\n".join(out).rstrip()


MUST_NOT = ["turned down", "can't ship", "test", "July capture", "Sep 16", "fog", "pumpkins", "redo",
            "review window", "manual review", "Unity rep", "Unity", "fake installs", "Android", "Android US phone", "iOS UK", "Oct 10", "Fri Oct 10", "5 days",
            "re-capture", "recapture", "re-recorded", "re-record", "#zm-animations", "#1896", "#1935", "#1966", "couch alpha 50", "barrel marketing2", "balloons alpha 50",
            "vacation", "Julia", "Lawson", "statics", "static", "stills", "cover", "#company-internal", "Oct 6",
            "tablet", "tablet trim", "iOS UK tablet", "Android US tablet", "restart", "retention", "landscape", "squirrelfail", "mrfluffernot",
            "old zombies", "old packs", "packs", "re-render", "rerender", "Marketing Video Refresh", "end card", "end card 001",
            "R_TEST_TURNED_DOWN", "R_REVIEW_WINDOW", "R_RECAPTURE_NOTE", "R_STATICS_COVER", "R_TABLET_TRIM", "R_OLD_PACKS",
            "LA", "dial in", "investors", "Oct 15", "Oct 16", "Oct 17", "Oct 12", "Reuse", "Refresh first", "Skip", "Marcus", "Martin", "Frederick", "Robert", "Arthur", "#zombie-art", "#zombie-match3d"]


def must_not_line(prompt: str) -> str:
    hits = [w for w in MUST_NOT if re.search(r"(?<![\w-])" + re.escape(w) + r"(?![\w-])", prompt, re.I)]
    assert not hits, hits
    sha = hashlib.sha256(prompt.encode()).hexdigest()[:12]
    return (f"{len(MUST_NOT)} words and phrases (the rev3 rule words above, the six rule ids, the rest of the dates, call words and people) "
            f"scanned against `04_Prompt.txt` (sha256 {sha}) by `Working_Files/prompt_gen/build_brief.py`, whole word, any case: 0 found.")


def check_truth():
    t = json.loads((WF / "solver" / "truth.json").read_text())
    calls = [v for v in t.values() if "calls" in v.get("groups", [])]
    store = {"app icon", 'iPad 12.9" set', 'iPhone 6.5" set', "Google Play phone set"}
    ads = [v for k, v in t.items() if "calls" in v.get("groups", []) and k not in store]
    c, a = Counter(v["call"] for v in calls), Counter(v["call"] for v in ads)
    assert len(calls) == 62 and len(ads) == 58, (len(calls), len(ads))
    assert (c["HALLOWEEN VERSION"], c["REFRESH FIRST"], c["REUSE"], c["SKIP"]) == (14, 36, 2, 10), c
    assert (a["HALLOWEEN VERSION"], a["REFRESH FIRST"], a["REUSE"], a["SKIP"]) == (12, 36, 0, 10), a
    work = [v for v in ads if v["call"] in ("HALLOWEEN VERSION", "REFRESH FIRST")]
    assert Counter(v["owner"] for v in work) == {"Marcus Bennett": 42, "Julia Lawson": 6}
    assert Counter(v["due"] for v in work) == {"Fri Oct 10": 30, "Wed Oct 15": 18}


def sap_rows(data):
    head = ["Fact (§5 row)", "Service", "Natural query", "Visible hits", "Hidden by ACL", "First visible hit (id)", "Found?"]
    out = []
    for r in data["rows"]:
        runs = r["runs"]
        q = " · ".join(f'"{x["query"]}"' for x in runs)
        vis = " · ".join(f'{x["visible"]} (showing {x["showing"]})' for x in runs)
        hid = " · ".join("not scanned (--no-hidden)" if x["hidden"] == "None" else f'{x["hidden"]} in {x["hidden_c"]} containers' for x in runs)
        first = " · ".join(f'`{x["first"]}`' if x["first"] else "— (0 hits)" for x in runs)
        svc = r["service"] + ("" if r["service"] in ("slack", "gmail", "gdrive", "gslides", "gcal") else " — unscoped (not ACL-scoped)")
        tgt = ", ".join(f"`{t}`" for t in r["targets"])
        if r["origin"] == "seeded":
            over = sorted({t for x in runs for t in x["target_overlay"]}, key=r["targets"].index)
            assert over, r["n"]
            how = "check-sql YES" if r["service"] in ("slack", "gmail", "gdrive", "gslides", "gcal") else "unscoped service, present in the SQL"
            why = "seeded: persona_view reads base only, so the base run cannot return it"
            found = f"YES — {why}; overlay hit {', '.join(f'`{t}`' for t in over)} ({how})"
            found += f"; path: {r['path']}" if r["path"] else ""
        else:
            x = runs[0]
            assert x["target_rank"], r["n"]
            see = "; can-see YES" if r["service"] == "slack" else "; unscoped"
            found = f"YES — base record {tgt} (rank {x['target_rank']} of {x['visible']} visible{see})"
        out.append((f'{r["n"]} · {r["fact"]} {tgt}', svc, q, vis, hid, first, found))
    return table(head, out)


def sap_halloween(data):
    head = ["Carrier (§5 row)", "Service", "Query", "Visible base hits", "SQL rows the word hits", "Carrier in the results?"]
    rows = []
    for m in data["halloween"]:
        assert not m["target_hit"], m
        rows.append((f'{m["n"]} · {m["fact"]}', m["service"], '"halloween"', str(m["visible"]), str(m["overlay"]),
                     f'no: the word is not in {", ".join(f"`{t}`" for t in m["targets"])}'))
    return table(head, rows)


def main():
    t = (HERE / "brief_template.md").read_text()
    prompt = (TASK / "04_Prompt.txt").read_text()
    check_truth()
    data = json.loads((R / "sap_rows.json").read_text())
    assert len(data["rows"]) == len(DM), (len(data["rows"]), len(DM))
    assert data["check_sql"]["verdict"] == "PASS" and data["check_sql"]["failures"] == 0
    dm = table(["Fact", "Value", "Locator", "Persona-readable", "Met first / overturned by", "Search risk", "Name in prompt?"], DM)
    sql = (TASK / "01_Universe_Inject.sql").read_bytes()
    out = (t.replace("@@SQL_SHA@@", hashlib.sha256(sql).hexdigest()[:12])
            .replace("@@CHECK_SQL@@", data["check_sql"]["verdict"])
            .replace("@@DISCOVERY_MAP@@", dm).replace("@@SAP_TABLE@@", sap_rows(data))
            .replace("@@SAP_HALLOWEEN@@", sap_halloween(data)).replace("@@MUST_NOT@@", must_not_line(prompt))
            .replace("@@SAP_RAW@@", fences((R / "sap_raw.txt").read_text()))
            .replace("@@ENTITY_RAW@@", fences((R / "entity_raw.txt").read_text())))
    assert "@@" not in out
    (WF / "04_Prompt_Writing_Brief.md").write_text(out)
    print("wrote 04_Prompt_Writing_Brief.md", len(out.splitlines()), "lines;", len(DM), "discovery rows;",
          len(data["rows"]), "search rows;", len(data["halloween"]), "halloween rows")


if __name__ == "__main__":
    main()
