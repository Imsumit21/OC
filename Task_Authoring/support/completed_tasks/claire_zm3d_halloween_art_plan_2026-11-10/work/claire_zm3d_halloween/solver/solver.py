"""solver.py - truth owner for the ZM3D Halloween art plan (Claire Morgan, synth-cut Oct 1 2025).

One row per ZM3D marketing surface (the sheet's Store and Unity rows, the serving library tickets the sheet omits, and
the four archived creatives as out-of-scope rows with no call): its Halloween call, owner, due date and a reason. Every
value is derived from the injected records, parsed from the SQL as data (tools/base_check.parse_sql; never executed):
the sheet tabs, each ticket's comments (campaigns, newest capture build, master audio), the deck's threshold, the
Store / UA masters folder listings, Marcus's DM reply, Frederick's changes mail, Arthur's calendar and the Trello
comment. The one base fact used (the 30 s cut's master has the music baked in, Frederick's Aug 13 thread) is declared in
BASE_FACTS.

Revision rev3 moves the deciding facts off the swept path: Frederick's fake-installs thread reply (due date), Marcus's
#zm-animations note (re-captures), Robert's #zombie-art review (Marcus's test), Martin's #company-internal post with
Leonard's reply (statics), Frederick's restart mail (campaigns) and his Trello comment (old pack art).

Rules mirror the manifest's mechanism_portfolio one to one. Disabling a rule (whole, or for a key set) or removing its
deciding record gives the rule's natural (wrong) reading for those keys; degrade operators over-apply a rule to its
control members. Key-local: a row depends only on switches applied to its own key.
"""
from __future__ import annotations

import collections
import hashlib
import json
import pathlib
import re

KEY_REGEX = r"[A-Za-z0-9][A-Za-z0-9 _:.,'\"()/&+-]{1,60}"
FIELDS = ["surface", "call", "owner", "due", "notes"]
CLASS_FIELD = "call"
GROUPS_FIELD = "groups"
REVISIONS = ("rev1", "rev2", "rev3")

HV, RF, REUSE, SKIP = "HALLOWEEN VERSION", "REFRESH FIRST", "REUSE", "SKIP"
SHEET = "f_02b1968f5e882366fbb883"
DOC = "f_fdd6d2d2f4a4d2f5b908fb"
DECK = "f_5ebf55ad29e815d46243c8"
STORE_FOLDER = "d_74a7c95c28097dd9777e01"
UA_FOLDER = "d_6c2e4339e5d58108799ac8"
PLAN_MAIL = "claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>"
DM_REPLY = hashlib.sha256(b"D05V2N6PZNU|1759166437.080255").hexdigest()[:32]
TRELLO_COMMENT = "68dc65a0f2d7fb28743f5860"
# rev3: the deciding facts that left the swept path. Ids come from scenario_gen/ids.json through the SQL text.
_IDS = json.loads((pathlib.Path(__file__).resolve().parents[1] / "scenario_gen" / "ids.json").read_text())["ids"]
REVIEW_REPLY = _IDS["slack_fred_review_reply"]["row_id"]      # Frederick, fake-installs thread: Android US phone by Fri Oct 10
RECAP_NOTE = _IDS["slack_marcus_recapture"]["row_id"]         # Marcus, #zm-animations: the three re-captures
TEST_REVIEW = _IDS["slack_robert_test_reply"]["row_id"]       # Robert, #zombie-art thread: the test cannot ship
LEAVE_POST = _IDS["slack_martin_leave"]["row_id"]             # Martin, #company-internal: Julia takes the ad statics
LEAVE_REPLY = _IDS["slack_leonard_leave_reply"]["row_id"]     # Leonard's reply: works for me
RESTART_MAIL = _IDS["gmail_fred_restart"]["msg"]              # Frederick, Sep 29: two cuts left off iOS UK tablet
LOGO_COMMENT = _IDS["trello_logo_comment"]                    # Frederick, Marketing Video Refresh card: old zombies on the packs
TRIM_CUTS = ("squirrelfail landscape", "mrfluffernot landscape")
LOGO_CUTS = {"end card 001": "end card 001", "end card 16:9 from 001": "16:9", "end card 1:1 from 001": "1:1",
             "end card 4:5 from 001": "4:5"}
ENDCARD_TICKET = "ART-831"
OFFSHEET = {"julia 4:5": "ART-826", "marcus portrait UA end card": ENDCARD_TICKET}   # serving, not on the sheet
BASE_THREAD_30S = "C06DJBJL798/1755114007.441789"
BASE_FACTS = {BASE_THREAD_30S: "music_baked"}   # Frederick's Aug 13 30 s UA cut: "the background music is baked in"
SWAP_DATE = "2025-07-29"                        # the Jul 29 zombie swap the deck names (Android #1452 / iOS 1232)
MONTHS = {m: i + 1 for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}

RULES = {
    "R_BUILD_CUT": {"mechanism": "2.6.7", "family": "2.6.7", "requirement": "R4", "nodes": ["T2", "CH6", "T16", "T13"],
                    "decides": ["due"], "controls": ['iPhone 6.5" set', "Google Play phone set"],
                    "over_application": "over:every-store-piece-due-oct16", "source": "release-calendar",
                    "authority": ["H2"], "natural_reading": "the icon swaps around Oct 24 as Leonard suggests"},
    "R_DONE_EXPORT": {"mechanism": "A24", "family": "A24", "requirement": "R2", "nodes": ["T1", "CH1"],
                      "decides": ["call"], "controls": ['iPhone 6.5" set', "Google Play phone set"],
                      "over_application": "over:every-store-set-missing", "source": "store-folder",
                      "natural_reading": "'exported' means every store set has its Halloween version"},
    "R_TEST_TURNED_DOWN": {"mechanism": "A24", "family": "A24", "requirement": "R7", "nodes": ["T3", "CH4", "T19"],
                           "decides": ["call"], "controls": ["cheer fastcouch 4:5", "marcus.bennett 4:5", "couch alpha 50"],
                           "over_application": "over:every-current-cut-reused", "source": "robert-test-review",
                           "natural_reading": "Marcus's DM and the two files mean the cheer fastcouch cuts are done, so they are reused"},
    "R_FLIGHT_CHANGE": {"mechanism": "A11", "family": "A11", "requirement": "R5", "nodes": ["T4", "CH3", "T18"],
                        "decides": ["due", "call"], "controls": ["couch alpha 50 16:9", "balloons alpha 50 (1) 16:9"],
                        "over_application": "over:every-tablet-cut-skipped", "source": "fred-plan-mail", "authority": ["H4"],
                        "natural_reading": "the Sep 12 draft: ads due Oct 17, all four campaigns"},
    "R_SCOPE_SERVING": {"mechanism": "A17", "family": "A17", "requirement": "R1", "nodes": ["T6", "CH7", "T5", "T10", "T14"],
                        "decides": ["call"], "controls": ["GreenCouch 001", "Professional Mode 9x16 test"],
                        "over_application": "over:archive-rows-serving", "source": "sheet-scope", "authority": ["H1"],
                        "natural_reading": "the sheet's rows are the scope"},
    "R_ART_CURRENT": {"mechanism": "A15", "family": "A15", "requirement": "R2", "nodes": ["T8", "CH2", "T17", "T11", "T12"],
                      "decides": ["call"], "controls": ["couch alpha 50", "barrel marketing2 4:5", "marcus.bennett 4:5"],
                      "over_application": "over:every-pre-august-post-refreshed", "source": "robert-deck", "authority": ["H3"],
                      "natural_reading": "any serving cut takes a Halloween overlay as it is"},
    "R_REVIEW_WINDOW": {"mechanism": "A14", "family": "A14", "requirement": "R5", "nodes": ["T20", "CH8"], "decides": ["due"],
                        "controls": ["marcus.bennett 4:5", "cheer fastcouch 4:5"], "over_application": "over:every-ad-due-oct10",
                        "source": "fred-review-reply", "natural_reading": "every working ad is due with Frederick on Wed Oct 15"},
    "R_RECAPTURE_NOTE": {"mechanism": "A25", "family": "A25", "requirement": "R2", "nodes": ["T9", "CH9"], "decides": ["call"],
                         "controls": ["couch alpha 30", "couch boss 30"], "over_application": "over:every-april-cut-recaptured",
                         "source": "marcus-recapture-note",
                         "natural_reading": "the ticket's April capture is the newest, so the cut is refreshed first"},
    "R_STATICS_COVER": {"mechanism": "A18", "family": "A18", "requirement": "R8", "nodes": ["T21", "CH10"], "decides": ["owner"],
                        "controls": ["app icon", 'iPad 12.9" set'], "over_application": "over:every-martin-piece-to-julia",
                        "source": "martin-leave-post", "natural_reading": "Martin has the stills, as Leonard's split says"},
    "R_TABLET_TRIM": {"mechanism": "A13", "family": "A13", "requirement": "R6", "nodes": ["T22", "CH11"], "decides": ["call"],
                      "controls": ["boris alin2 16:9", "couch boss 30 16:9"], "over_application": "over:every-landscape-cut-skipped",
                      "source": "fred-restart-mail", "natural_reading": "the ticket's campaign note is current, so the cut stays on iOS UK tablet"},
    "R_OLD_PACKS": {"mechanism": "A12", "family": "A12", "requirement": "R2", "nodes": ["T23", "CH12"], "decides": ["call"],
                    "controls": ["marcus.bennett 4:5", "marcus.bennett 1:1"], "over_application": "over:every-august-render-refreshed",
                    "source": "fred-packs-comment", "natural_reading": "a render from a current build takes a Halloween version as it is"},
}
RULES_ORDER = tuple(RULES)
DEGRADES = {
    "over:every-store-piece-due-oct16": "put every store piece, the Google Play set included, on the Oct 16 build cut",
    "over:every-store-set-missing": "treat every store set as missing its Halloween version",
    "over:every-current-cut-reused": "reuse every current-build cut as if Marcus had already dressed it",
    "over:every-tablet-cut-skipped": "skip every cut that runs on the Android US tablet campaign, even one that also runs on iOS UK tablet",
    "over:archive-rows-serving": "treat the Archive tab's paused creatives as serving",
    "over:every-pre-august-post-refreshed": "refresh every cut whose sheet 'live since' is before the Jul 29 swap, re-captures included",
    "over:every-ad-due-oct10": "move every working ad to Fri Oct 10, iOS-only ads included",
    "over:every-april-cut-recaptured": "treat every April capture as re-captured on a current build",
    "over:every-martin-piece-to-julia": "give Julia everything Martin had, store art included",
    "over:every-landscape-cut-skipped": "skip every cut that shares the tablet campaigns, even one still on iOS UK tablet",
    "over:every-august-render-refreshed": "refresh every August capture or render, not only the flagged end cards",
}
CHANNELS = {}
REUSE_NAMED = {DM_REPLY: ("cheer fastcouch", ("9:16", "16:9"))}   # what Marcus's reply names: "both 9:16 and 16:9"


# ------------------------------------------------------------------ state
def load_state(sql_text, revision=None):
    try:
        from base_check import parse_sql
    except ImportError:  # direct use outside the tool bundle
        import pathlib
        import sys
        sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[4] / "tools"))
        from base_check import parse_sql
    ids, issues, comments, tabs, files, texts = set(), {}, collections.defaultdict(list), {}, [], {}
    for x in parse_sql(sql_text or ""):
        if x["op"] != "insert":
            continue
        t, r = x["table"], x["row"]
        for c in ("id", "identifier", "document_id", "spreadsheet_id", "presentation_id", "event_id", "contact_id"):
            if r.get(c):
                ids.add(str(r[c]))
        if t == "linear.linear_issues":
            issues[r["id"]] = {"title": r.get("title") or "", "description": r.get("description") or "",
                               "state": r.get("state_id")}
        elif t == "linear.linear_comments":
            comments[r["issue_id"]].append((r["created_at"], r["body"]))
        elif t == "gsheets.sheets_sheets" and r.get("spreadsheet_id") == SHEET:
            tabs[r["title"]] = json.loads(r["grid_json"])
        elif t == "gdrive.drive_files":
            files.append({"id": r["id"], "name": r["name"], "parents": json.loads(r.get("parents_json") or "[]")})
        elif t == "slack.slack_messages":
            texts[r["id"]] = r.get("text") or ""
        elif t == "gmail.gmail_messages":
            texts[r["id"]] = r.get("body_text") or ""
        elif t == "gdocs.docs_documents":
            texts[r["document_id"]] = r.get("body_text") or ""
        elif t == "gslides.slides_page_elements":
            texts[r["presentation_id"]] = texts.get(r["presentation_id"], "") + "\n" + (r.get("text") or "")
        elif t == "trello.trello_actions":
            texts[r["id"]] = (json.loads(r.get("data_json") or "{}")).get("text") or ""
    for k in comments:
        comments[k].sort()
    return {"ids": ids, "issues": issues, "comments": dict(comments), "tabs": tabs, "files": files, "texts": texts,
            "revision": revision or REVISIONS[-1]}


CONTROLS_OF = {v["over_application"]: set(v["controls"]) for v in RULES.values() if v.get("over_application")}


def _over(degrade, op, key):
    """An over-application operator acts on its rule's control members only (a control trial, never a landing)."""
    return key in CONTROLS_OF.get(op, ()) and _off(degrade, op, key)


def _present(state, rid):
    return rid in state["ids"]


def _off(spec, name, key):
    for d in spec or ():
        if isinstance(d, (tuple, list)):
            if d and d[0] == name and (len(d) < 2 or d[1] is None or key in d[1]):
                return True
        elif d == name:
            return True
    return False


# ------------------------------------------------------------------ the cohort, read from the sheet and the library
def _cohort(state):
    """{key: {kind, ticket, live_since, section}} for the Store and Unity rows, the off-sheet serving tickets and the
    Archive rows."""
    out = {}
    tabs = state["tabs"]
    for row in (tabs.get("Store") or [])[1:]:
        out[row[0]] = {"section": "store", "ticket": None, "live": row[2]}
    for row in (tabs.get("Unity") or [])[1:]:
        out[row[0]] = {"section": "unity", "ticket": row[3], "live": row[2], "format": row[1]}
    on_sheet = {v["ticket"] for v in out.values() if v["ticket"]}
    for row in (tabs.get("Archive") or [])[1:]:
        out[row[0]] = {"section": "archive", "ticket": row[3], "live": None, "format": row[1]}
        on_sheet.add(row[3])
    for iid, iss in sorted(state["issues"].items()):
        if iid in on_sheet or not iid.startswith("ART-") or iss["state"] == "Canceled":
            continue
        key = iss["title"].rsplit(" (", 1)[0]
        out[key] = {"section": "offsheet", "ticket": iid, "live": None, "format": iss["title"].rsplit(" (", 1)[-1].rstrip(")")}
    for key, iid in OFFSHEET.items():   # a serving ad the sheet omits keeps its row even when its record is gone
        out.setdefault(key, {"section": "offsheet", "ticket": iid, "live": None, "format": ""})
    return out


def _date(text):
    """'Apr 7' / 'Dec 6, 2024' -> 'YYYY-MM-DD'."""
    m = re.match(r"([A-Z][a-z]{2}) (\d{1,2})(?:, (\d{4}))?", text or "")
    if not m:
        return None
    return f"{m.group(3) or '2025'}-{MONTHS[m.group(1)]:02d}-{int(m.group(2)):02d}"


def _threshold(state):
    m = re.search(r"Android #(\d+) / iOS (\d+)", state["texts"].get(DECK, ""))
    return int(m.group(1)) if m else None


def _ticket_facts(state, ticket):
    """campaigns, newest source (build number, 'prototype' or a capture date) and master audio from the comments."""
    camp, build, cap_date, proto, master = None, None, None, False, None
    for _, body in state["comments"].get(ticket, []):
        m = (re.search(r"(?:^|\. )Unity: ([^.]+)\.", body) or re.search(r"Uploaded to Unity [A-Z][a-z]{2} \d+: ([^.]+)\.", body)
             or re.search(r"Still running on Unity: ([^(]+) \(checked", body))
        if m:
            camp = tuple(c.strip() for c in m.group(1).split(","))
        b = re.search(r"Android #(\d+)", body)
        if b:
            build, cap_date, proto = int(b.group(1)), None, False
        elif "from the prototype" in body:
            build, cap_date, proto = None, None, True
        else:
            d = re.match(r"Captured ([A-Z][a-z]{2} \d{1,2}(?:, \d{4})?)", body)
            if d:
                build, cap_date, proto = None, _date(d.group(1)), False
        if "music baked into the master" in body:
            master = "music_baked"
        elif "SFX only" in body:
            master = "sfx_only"
        elif "Master notes are in Frederick's Aug 13 thread" in body:
            master = BASE_FACTS[BASE_THREAD_30S]
    return {"campaigns": camp or (), "build": build, "cap_date": cap_date, "proto": proto, "master": master}


def _reuse_named(state, key):
    for rid, (name, aspects) in REUSE_NAMED.items():
        text = state["texts"].get(rid, "")
        if _present(state, rid) and name in text and all(a in text for a in aspects) and key.startswith(name):
            if any(key.endswith(a) for a in aspects):
                return rid
    return None


def _store_has(state, key):
    marks = {'iPhone 6.5" set': "iPhone65", "Google Play phone set": "GooglePlay_phone", 'iPad 12.9" set': "iPad"}
    if not _present(state, STORE_FOLDER) or key not in marks:
        return False
    return any(STORE_FOLDER in f["parents"] and marks[key] in f["name"] and "Halloween" in f["name"] for f in state["files"])


# ------------------------------------------------------------------ one row
def _row(key, info, state, disable, degrade):
    on = lambda rule, rid=None: not _off(disable, rule, key) and (rid is None or _present(state, rid))  # noqa: E731
    sect = info["section"]
    row = {"surface": key, "call": None, "owner": None, "due": None, "notes": "", "groups": ["calls"]}
    if sect == "archive":
        if _over(degrade, "over:archive-rows-serving", key):
            row.update(call=HV, owner="Marcus Bennett", notes="over-applied: a paused creative treated as serving")
        else:
            row.update(groups=["archive"], notes="paused: Archive tab, out of scope")
        return row
    if sect == "offsheet":
        rid = TRELLO_COMMENT if "julia" in key else ENDCARD_TICKET
        named = rid in state["ids"] and (("4:5 static" in state["texts"].get(TRELLO_COMMENT, "") and "julia" in key)
                                         or "Plays after every" in state["issues"].get(info["ticket"], {}).get("description", ""))
        if not (on("R_SCOPE_SERVING", rid) and named):
            row.update(groups=["calls"], notes="not on the sheet: left out")
            return row
    if sect == "store":
        if key == "app icon":
            row.update(call=HV, owner="Julia Lawson" if _over(degrade, "over:every-martin-piece-to-julia", key) else "Martin Walsh",
                       notes="new seasonal piece (Robert turned the Sep 17 concept down for the icon)")
            row["due"] = "Thu Oct 16" if on("R_BUILD_CUT", DOC) else "Fri Oct 24"
            return row
        made = _store_has(state, key) if on("R_DONE_EXPORT", STORE_FOLDER) else True
        if _over(degrade, "over:every-store-set-missing", key):
            made = False
        row.update(call=REUSE if made else HV,
                   owner="Julia Lawson" if _over(degrade, "over:every-martin-piece-to-julia", key) else "Martin Walsh",
                   notes="Halloween store export already made" if made else "no Halloween export in the Store folder")
        if key == "Google Play phone set":
            row["due"] = "Thu Oct 16" if _over(degrade, "over:every-store-piece-due-oct16", key) else None
        else:
            row["due"] = "Thu Oct 16" if on("R_BUILD_CUT", DOC) else "Fri Oct 17"
        return row
    # an ad: its own ticket decides it, unless a later record elsewhere changes one of its facts
    f = _ticket_facts(state, info["ticket"])
    static = (info.get("format") or "").endswith("static")
    cover = static and on("R_STATICS_COVER", LEAVE_POST) and "ad statics" in state["texts"].get(LEAVE_POST, "")
    maker = "Julia Lawson" if cover else ("Martin Walsh" if static else "Marcus Bennett")
    plan = on("R_FLIGHT_CHANGE", PLAN_MAIL)
    if on("R_TABLET_TRIM", RESTART_MAIL) and key in TRIM_CUTS and key in state["texts"].get(RESTART_MAIL, ""):
        f["campaigns"] = tuple(c for c in f["campaigns"] if c != "iOS UK tablet")
    if plan and f["campaigns"] == ("Android US tablet",):
        row.update(call=SKIP, notes="runs only on Android US tablet, which ends Oct 12")
        return row
    if _over(degrade, "over:every-landscape-cut-skipped", key):
        row.update(call=SKIP, notes="over-applied: a cut on the tablet campaigns")
        return row
    if _over(degrade, "over:every-tablet-cut-skipped", key) and "Android US tablet" in f["campaigns"]:
        row.update(call=SKIP, notes="over-applied: a tablet cut")
        return row
    due = "Wed Oct 15" if plan else "Fri Oct 17"
    if plan and on("R_REVIEW_WINDOW", REVIEW_REPLY) and "Android US phone" in f["campaigns"]:
        due = "Fri Oct 10"
    if plan and _over(degrade, "over:every-ad-due-oct10", key):
        due = "Fri Oct 10"
    # Marcus's DM and the two files are the done source; Robert's review in another channel is the missing piece
    turned_down = on("R_TEST_TURNED_DOWN", TEST_REVIEW) and "can't ship" in state["texts"].get(TEST_REVIEW, "")
    if _reuse_named(state, key) and not turned_down:
        row.update(call=REUSE, owner="Marcus Bennett", due=due, notes="Halloween version already in UA masters")
        return row
    if on("R_RECAPTURE_NOTE", RECAP_NOTE):
        m = re.search(re.escape(key) + r" on (?:android )?#(\d+)", state["texts"].get(RECAP_NOTE, ""))
        if m:
            f.update(build=int(m.group(1)), cap_date=None, proto=False)
    if _over(degrade, "over:every-april-cut-recaptured", key):
        f.update(build=9999, cap_date=None, proto=False)
    thr = _threshold(state) if on("R_ART_CURRENT", DECK) else None
    old = thr is not None and (f["proto"] or (f["build"] is not None and f["build"] < thr)
                                or (f["cap_date"] is not None and f["cap_date"] < SWAP_DATE))
    music = thr is not None and f["master"] == "music_baked"
    flagged = (on("R_OLD_PACKS", LOGO_COMMENT) and key in LOGO_CUTS and LOGO_CUTS[key] in state["texts"].get(LOGO_COMMENT, ""))
    call = RF if (old or music or flagged) else HV
    if _over(degrade, "over:every-pre-august-post-refreshed", key) and (_date(info.get("live")) or "9999") < SWAP_DATE:
        call = RF
    if _over(degrade, "over:every-august-render-refreshed", key):
        call = RF
    if call == HV and _over(degrade, "over:every-current-cut-reused", key):
        call = REUSE
    why = ("source predates the Jul 29 swap" if old else ("old zombies on the packs: re-render first" if flagged else "music baked into the master")) \
        if call == RF else ("current source" if call == HV else "over-applied reuse")
    row.update(call=call, owner=maker, due=due, notes=why)
    return row


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    co = _cohort(state)
    keys = sorted(co) if keys_ is None else [k for k in keys_ if k in co]
    return {k: _row(k, co[k], state, disable, degrade) for k in sorted(keys)}


def aggregates(rows):
    classes = dict(collections.Counter(v[CLASS_FIELD] for v in rows.values() if v.get(CLASS_FIELD)))
    groups = {}
    for k in sorted(rows):
        for g in rows[k].get(GROUPS_FIELD) or []:
            groups.setdefault(g, []).append(k)
    return {"classes": classes, "groups": groups}


_STATE = {}


def evidence(rows, key, field):
    """The records that decide one field of one row (the golden check reads them)."""
    row = rows.get(key) or {}
    if field == "due":
        if key in ("app icon", 'iPad 12.9" set', 'iPhone 6.5" set', "Google Play phone set"):
            return [DOC]
        return [REVIEW_REPLY] if (row.get("due") == "Fri Oct 10") else [PLAN_MAIL]
    if field == "surface":
        if '"' in key:
            return []          # a quoted key cannot be matched inside a JSON-escaped grid
        if key in ("julia 4:5", "marcus portrait UA end card"):
            return ["ART-826" if key == "julia 4:5" else ENDCARD_TICKET]
        return [SHEET]
    return []                  # owner / notes: unverified (decided by the ask's owner split and the rules)


def touched(state, rule):
    """Every key the rule can move alone or under any mix of the other rules (precedence: Skip > Reuse > the art rule),
    plus its over-application's control members."""
    others = frozenset(r for r in RULES if r != rule)
    moved = set()
    for ctx in (frozenset(), others):
        a, b = solve(state, disable=ctx), solve(state, disable=ctx | {rule})
        moved |= {k for k in a if a[k] != b.get(k)}
    op = RULES[rule].get("over_application")
    if op:
        base, d = solve(state), solve(state, degrade={op})
        moved |= {k for k in base if base[k] != d.get(k)}
    return sorted(moved)


def deciding(state, rule, key):
    if rule == "R_BUILD_CUT":
        return [DOC]
    if rule == "R_DONE_EXPORT":
        return [STORE_FOLDER]
    if rule == "R_TEST_TURNED_DOWN":
        return [TEST_REVIEW]
    if rule == "R_REVIEW_WINDOW":
        return [REVIEW_REPLY]
    if rule == "R_RECAPTURE_NOTE":
        return [RECAP_NOTE]
    if rule == "R_STATICS_COVER":
        return [LEAVE_POST, LEAVE_REPLY]
    if rule == "R_TABLET_TRIM":
        return [RESTART_MAIL]
    if rule == "R_OLD_PACKS":
        return [LOGO_COMMENT]
    if rule == "R_FLIGHT_CHANGE":
        return [PLAN_MAIL]
    if rule == "R_SCOPE_SERVING":
        return [TRELLO_COMMENT] if "julia" in key else [ENDCARD_TICKET]
    if rule == "R_ART_CURRENT":
        return [DECK]
    return []


def base_route(record_id):
    """Base records the truth rests on are Slack messages (Frederick's Aug 13 thread); they carry no hg.py records
    route, so the golden check reports them unverified and the dossier re-reads them through tools/hg.py."""
    return None
