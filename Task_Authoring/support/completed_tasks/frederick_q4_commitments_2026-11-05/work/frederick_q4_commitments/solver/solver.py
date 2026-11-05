"""Solver for frederick_q4_commitments (tools/oracle_kit.py contract), rev4 (rules NOTE and WIN added; rev1-rev3 truth reproduced).

Truth = the Q4 commitments log Frederick should write as of the end of Tue Sep 30, 2025 (Pacific), from the base universe
plus the injection SQL (parsed with tools/base_check.parse_sql; never executed). Each company's decision follows Leonard's
runway guardrails doc top to bottom (already answered -> cash test, except Arthur's keep-running list -> signing -> park),
with the Sep 29 #executives change (partner-booked travel counts as cash) and ESG's signing note (only Leonard or Arthur
accept terms; auto-renewal, exclusivity, IP licence or a term over 12 months also goes to ESG's intake).

Per-company facts that do not depend on a designed mechanism come from the cohort table M of
Working_Files/plan/build_scenario.py (each row's deciding records are in the SQL or the base). One rule per
mechanism_portfolio entry; each reads its deciding record and falls back to its natural reading when `disable` switches
it off (whole or per key set) or the record is absent. Over-application operators act on the rule's declared controls.
"""
import collections
import contextlib
import io
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "plan"))
with contextlib.redirect_stdout(io.StringIO()):     # the builder prints its census on import; keep solver output clean
    import build_scenario as B  # noqa: E402  (the cohort table; writes nothing unless BUILD_SCENARIO_WRITE=1)

KEY_REGEX = r".+"
FIELDS = ["Company", "Contact", "What's waiting", "Decision", "Answered by", "What we told them", "Next date"]
CLASS_FIELD, GROUPS_FIELD = "Decision", "groups"
I = B.IDS
REVIEW = "2026-01-05"
IDS = json.loads((HERE.parent / "plan" / "sql_ids.json").read_text())["ids"]
SL = IDS["slack_mid"]
M_ESG_ACK = IDS["msg"]["esg_ack"]
M_NOTICE = IDS["msg"]["clipforge_notice"]
KEEP_PAGER_ITEM = IDS["keep_items"][2]       # "the night pager for backend outages (whatever wakes me up at 3am)"

RULES = {
    "DONE": {"mechanism": "A24", "requirement": "R6", "nodes": ["T1", "C1"], "decides": ["Decision", "Next date"],
             "natural_reading": "Nintendo needs nothing: registration completed", "family": "done_gap",
             "source": "linear-comment", "signature": "Nintendo ZOM-567 comment officer accepts",
             "controls": ["Orbit Store", "Playfuse", "Retainly"], "over_application": "done_over"},
    "CORR": {"mechanism": "A11", "requirement": "R2", "nodes": ["T2", "C2"], "decides": ["Decision", "Next date"],
             "natural_reading": "Framewell End: paid from Nov 1", "family": "superseding",
             "source": "slack-thread-reply-alias", "signature": "Maren Pro plan no charge until Feb 1",
             "controls": ["Brightlane Studio", "Quillcraft"], "over_application": "corr_over"},
    "COMPL": {"mechanism": "A25", "requirement": "R4", "nodes": ["T3", "C3"], "decides": ["Decision", "Answered by"],
              "natural_reading": "Lanternfly gets a Park reply", "family": "completion_elsewhere", "source": "slack-dm-thread-reply",
              "signature": "rang Wen back Southeast Asia after the raise",
              "controls": ["Balancy", "Motive Forge", "Glyphworks"], "over_application": "compl_over"},
    "EXC": {"mechanism": "A15", "requirement": "R3", "nodes": ["T4", "C4"], "decides": ["Decision", "Next date"],
            "natural_reading": "Pingwise End: paid from Nov 1", "family": "authority", "source": "trello-checklist",
            "signature": "keep-running night pager backend outages",
            "controls": ["Vaultline", "Certwell", "Reviewly"], "over_application": "exc_over"},
    "DATE": {"mechanism": "A4", "requirement": "R2", "nodes": ["T5", "C5"], "decides": ["Decision", "Next date"],
             "natural_reading": "Clipforge Park: pilot free through Jan 15", "family": "superseding",
             "source": "processor-notice", "signature": "workspace HG-2291 pilot ends Oct 15",
             "controls": ["Retainly", "Reviewly"], "over_application": "date_over"},
    "FILT": {"mechanism": "A17", "requirement": "R1", "nodes": ["T6", "C6"], "decides": ["groups"],
             "natural_reading": "Pixel Harbor not on the log", "family": "exact_predicate", "source": "mail-date-window",
             "signature": "Pixel Harbor deposit Oct 10 June quote",
             "controls": ["Glyphworks", "Nova Rewards", "Playable Factory"], "over_application": "filt_over"},
    "SIGN": {"mechanism": "A12", "requirement": "R6", "nodes": ["T7"], "decides": ["Decision"],
             "natural_reading": "Frederick accepts Markward's free click-through himself (July note): no card",
             "family": "superseding", "source": "hub-path", "signature": "ESG only Leonard or Arthur accept terms",
             "controls": ["Kinetic Arcade", "Echohall"], "over_application": "sign_over"},
    "AMEND": {"mechanism": "A15", "requirement": "R2", "nodes": ["T9"], "decides": ["Decision"],
              "natural_reading": "Wishwave Park: travel is booked by the partner", "family": "superseding",
              "source": "hub-path", "signature": "travel counts as cash partner books",
              "controls": ["Pressbeam"], "over_application": "amend_over"},
    "NOTE": {"mechanism": "A25", "requirement": "R4", "nodes": ["T19", "C8"], "decides": ["Decision", "Answered by"],
             "natural_reading": "Spotlight Fest End: say no to the $750 stand fee", "family": "completion_elsewhere",
             "source": "slack-root-alias", "signature": "Dec 5 indie showcase sitting this one out Rina",
             "controls": ["Motive Forge", "Wishwave"], "over_application": "note_over"},
    "WIN": {"mechanism": "A17", "requirement": "R1", "nodes": ["T20", "C7"], "decides": ["groups"],
            "natural_reading": "Hootline not on the log", "family": "exact_predicate", "source": "mail-window-and-folder",
            "signature": "Hootline promo keep the scheduler after Jan 31",
            "controls": ["Quillcraft", "Gamesforum SF"], "over_application": "win_over"},
}
DEGRADES = {
    "done_over": "routes Retainly's trial sign-up to a signature card although its paper needs no acceptance",
    "corr_over": "parks Brightlane too, as if every paid quote were waived",
    "compl_over": "treats Glyphworks as answered because Leonard mentioned fonts in #executives",
    "exc_over": "keeps Reviewly as live-game tooling",
    "date_over": "ends Retainly as well, as if its trial converted inside the window",
    "filt_over": "pulls Playable Factory's cold pitch onto the log",
    "sign_over": "cards Echohall although nothing needs accepting",
    "note_over": "treats Wishwave's showcase push as already answered by Robert's note",
    "win_over": "pulls Gamesforum SF's unanswered August invite onto the log",
    "amend_over": "ends Pressbeam as if it carried travel",
    "ch_miss": "a channel member's deciding record is not found: the member takes its natural reading",
}
CHANNELS = {
    "CH-DONE": {"kind": "scale", "degrade": "ch_miss", "members": ["Nintendo"], "latent": "member", "family": "done_gap",
                "rule": "DONE", "source": "linear-comment",
                "description": "ZOM-567's comment is not read: Nintendo looks done"},
    "CH-CORR": {"kind": "scale", "degrade": "ch_miss", "members": ["Framewell"], "latent": "member",
                "family": "superseding", "rule": "CORR", "source": "slack-thread-reply",
                "description": "Leonard's waiver reply (names Maren, not Framewell) under the Playtestcloud post is not found: Framewell ends"},
    "CH-COMPL": {"kind": "scale", "degrade": "ch_miss", "members": ["Lanternfly Publishing"], "latent": "member",
                 "family": "completion_elsewhere", "rule": "COMPL", "source": "slack-dm-thread-reply",
                 "description": "Leonard's DM thread reply (names Wen) is not opened: Lanternfly is answered again"},
    "CH-EXC": {"kind": "scale", "degrade": "ch_miss", "members": ["Pingwise"], "latent": "member", "family": "authority",
               "rule": "EXC", "source": "trello-checklist",
               "description": "the night-pager item is not joined to Pingwise: it ends"},
    "CH-DATE": {"kind": "scale", "degrade": "ch_miss", "members": ["Clipforge"], "latent": "member",
                "family": "superseding", "rule": "DATE", "source": "processor-notice",
                "description": "the HG-2291 notice is not joined to Clipforge: it parks"},
    "CH-FILT": {"kind": "scale", "degrade": "ch_miss", "members": ["Pixel Harbor Events"], "latent": "member",
                "family": "exact_predicate", "rule": "FILT", "source": "mail-date-window",
                "description": "the June quote is outside the run's search window: Pixel Harbor is missed"},
    "CH-NOTE": {"kind": "scale", "degrade": "ch_miss", "members": ["Spotlight Fest"], "latent": "member",
                "family": "completion_elsewhere", "rule": "NOTE", "source": "slack-root-alias",
                "description": "Robert's note (names the Dec 5 indie showcase and Rina) is not found: Spotlight ends and gets a second answer"},
    "CH-WIN": {"kind": "scale", "degrade": "ch_miss", "members": ["Hootline"], "latent": "member",
               "family": "exact_predicate", "rule": "WIN", "source": "mail-window-and-folder",
               "description": "Hootline's August-only thread (no filed paper) is outside the run's cohort sweep: Hootline is missed"},
    "CH-SLIP": {"kind": "scale", "degrade": None, "members": [], "latent": "member", "family": "slip",
                "slots": ["C1", "C2", "C5", "C6", "C7", "C9"],
                "description": "a base slip on a control row (who answered, what we told them, a card or a contact)"},
}
CHANNEL_RULE = {c["members"][0]: c["rule"] for c in CHANNELS.values() if c.get("rule")}

TOLD = {"End": "declined", "Park": "we'll pick it up in January", "Keep": "staying on",
        "Sign": "with Leonard or Arthur to sign", "SignCounsel": "with our counsel (ESG) first, then Leonard or Arthur signs"}
ANSWERED_TOLD = {
    "Lanternfly Publishing": "no new publishing deals before the raise; talk again in January (Leonard, Sep 27 call)",
    "Balancy": "we'll circle back when we have bandwidth (Leonard, Sep 11)",
    "Motive Forge": "keeping art in-house this quarter, pass for now (Arthur, Sep 19)",
    "Spotlight Fest": "skipping this year's showcase (Robert, Sep 17 call)"}
LATER = {"Lanternfly Publishing", "Balancy"}          # answers that said "later": they get the January review too
EXISTING_CONTACT = {"Kinetic Arcade", "Lumencloud", "Markward"}


def load_state(sql_text, revision=None):
    from base_check import parse_sql
    by_id = {}
    for x in parse_sql(sql_text):
        if x["op"] != "insert":
            continue
        r = x["row"]
        for k in ("id", "identifier", "contact_id", "spreadsheet_id", "document_id", "presentation_id"):
            if r.get(k):
                by_id[str(r[k])] = r
    return {"by_id": by_id, "revision": revision or "rev1"}


def _hit(spec, name, key):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and key in d[1]) for d in spec)


def _off(rule, key, disable, degrade):
    return _hit(disable, rule, key) or (CHANNEL_RULE.get(key) == rule and _hit(degrade, "ch_miss", key))


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    b = state["by_id"]
    have = lambda i: i in b          # noqa: E731
    out = {}
    for m in B.M:
        k = m["key"]
        if keys_ is not None and k not in keys_:
            continue
        dec, nd, by = m["decision"], m["next_date"], m["answered_by"]
        if dec == "out":
            dec = None
        # ---- designed mechanisms (each falls back to its natural reading)
        if k == "Nintendo" and (_off("DONE", k, disable, degrade) or not have(I["zom567_cmt"])):
            dec, nd = "Answered", None                    # registration completed: looks like nothing is waiting
        if k == "Framewell" and (_off("CORR", k, disable, degrade) or not have(SL["framewell_waiver_reply"])):
            dec, nd = "End", "2025-10-31"                 # Pro billed from Nov 1: say no before then
        if k == "Lanternfly Publishing" and (_off("COMPL", k, disable, degrade) or not have(SL["lanternfly_dm"])):
            dec, by, nd = "Park", None, REVIEW
        if k == "Pingwise" and (_off("EXC", k, disable, degrade) or not have(KEEP_PAGER_ITEM)):
            dec, nd = "End", "2025-10-31"                 # Team plan from Nov 1: downgrade before Oct 31
        if k == "Clipforge" and (_off("DATE", k, disable, degrade) or not have(M_NOTICE)):
            dec, nd = "Park", REVIEW                      # pilot agreement: free through Jan 15
        if k == "Pixel Harbor Events" and (_off("FILT", k, disable, degrade) or not have(I["pixel_thread"])):
            dec, nd = None, None
        if k == "Markward" and (_hit(disable, "SIGN", k) or not have(M_ESG_ACK)):
            dec, nd = "Park", REVIEW                      # July note: Frederick accepts it himself, nothing to sign
        if k == "Wishwave" and (_hit(disable, "AMEND", k) or not have(SL["amendment_root"])):
            dec, nd = "Park", REVIEW                      # the partner books the travel
        if k == "Spotlight Fest" and (_off("NOTE", k, disable, degrade) or not have(SL["spotlight_note"])):
            dec, by, nd = "End", None, None               # the invitation looks open: say no to the $750 stand fee
        if k == "Hootline" and (_off("WIN", k, disable, degrade) or not have(IDS["threads"]["Hootline"])):
            dec, nd = None, None                          # outside the run's cohort sweep: not on the log
        # ---- over-application operators on control members
        if k == "Retainly" and _hit(degrade, "done_over", k):
            dec, nd = "Sign", None
        if k == "Brightlane Studio" and _hit(degrade, "corr_over", k):
            dec, nd = "Park", REVIEW
        if k == "Glyphworks" and _hit(degrade, "compl_over", k):
            dec, by = "Answered", "Leonard"
        if k == "Reviewly" and _hit(degrade, "exc_over", k):
            dec, nd = "Keep", "2025-10-20"
        if k == "Retainly" and _hit(degrade, "date_over", k):
            dec, nd = "End", "2026-01-11"
        if k == "Playable Factory" and _hit(degrade, "filt_over", k):
            dec, nd = "End", None
        if k == "Echohall" and _hit(degrade, "sign_over", k):
            dec, nd = "Sign", None
        if k == "Wishwave" and _hit(degrade, "note_over", k):
            dec, by, nd = "Answered", "Robert", None
        if k == "Gamesforum SF" and _hit(degrade, "win_over", k):
            dec, nd = "Park", REVIEW
        if k == "Pressbeam" and _hit(degrade, "amend_over", k):
            dec, nd = "End", None
        # ---- derived fields and writes
        if dec is None:
            out[k] = {"Company": k, "Contact": None, "What's waiting": None, "Decision": None, "Answered by": None,
                      "What we told them": None, "Next date": None, "groups": [], "evidence": {"Company": []}}
            continue
        if dec != "Answered":
            by = None
        if dec == "Answered":
            told = ANSWERED_TOLD.get(k, "nothing waiting")
            if k == "Lanternfly Publishing" and "Southeast Asia has to wait" in str(b.get(SL["lanternfly_dm"], {}).get("text")):
                told = "Southeast Asia waits until after the raise; talk again in January (Leonard, Sep 27 call)"
        else:
            told = TOLD["SignCounsel"] if dec == "Sign" and m["counsel"] else TOLD[dec]
        person = m["person"]
        groups = ["log"]
        if dec != "Answered" and person:
            groups.append("written_answer")
        if dec == "Park" or (dec == "Answered" and k in LATER):
            groups.append("revisit")
            nd = REVIEW
        if dec == "Sign":
            groups.append("card")
            if m["counsel"]:
                groups.append("esg")
        if person and k not in EXISTING_CONTACT:
            groups.append("contact_add")
        ev = [x for x in (IDS["threads"].get(k), IDS["papers"].get(k)) if x and have(x)]
        if k == "Nintendo":
            ev = [x for x in (I["zom567"], I["zom567_cmt"]) if have(x)]
        if k == "Balancy":
            ev = [B.BASE["balancy_thread"]]
        contact = ("PERSON_0527_NAME" if k == "Balancy" else f"{person[0]} {person[1]}" if person else None)
        waiting = m["kind"]
        if k == "Tilecast" and "Interactive demo widget" in str(b.get(IDS["papers"]["Tilecast"], {}).get("body_text")):
            waiting = "website interactive demo widget"      # rev3 wording of Tilecast's offer
        out[k] = {"Company": k, "Contact": contact, "What's waiting": waiting, "Decision": dec, "Answered by": by,
                  "What we told them": told, "Next date": nd, "groups": sorted(groups), "evidence": {"Company": ev}}
    return out


def aggregates(rows):
    groups = collections.defaultdict(list)
    for k in sorted(rows):
        for g in rows[k]["groups"]:
            groups[g].append(k)
    listed = [v for v in rows.values() if v["Decision"]]
    return {"classes": dict(sorted(collections.Counter(v["Decision"] for v in listed).items())),
            "groups": {g: groups[g] for g in sorted(groups)},
            "totals": {"log_size": len(listed), "written_answers": len(groups.get("written_answer", [])),
                       "revisits": len(groups.get("revisit", [])), "cards": len(groups.get("card", [])),
                       "esg_emails": len(groups.get("esg", [])), "contacts_added": len(groups.get("contact_add", []))}}


def evidence(rows, key, field):
    if field == "Company":
        return list(rows[key]["evidence"]["Company"])
    return []


def touched(state, rule):
    return {"DONE": {"Nintendo"}, "CORR": {"Framewell"}, "COMPL": {"Lanternfly Publishing"}, "EXC": {"Pingwise"},
            "DATE": {"Clipforge"}, "FILT": {"Pixel Harbor Events"}, "SIGN": {"Markward"}, "AMEND": {"Wishwave"},
            "NOTE": {"Spotlight Fest"}, "WIN": {"Hootline"}}[rule]


def deciding(state, rule, key):
    return {"DONE": [I["zom567_cmt"]], "CORR": [SL["framewell_waiver_reply"]], "COMPL": [SL["lanternfly_dm"]],
            "EXC": [KEEP_PAGER_ITEM], "DATE": [M_NOTICE], "FILT": [I["pixel_thread"]], "SIGN": [M_ESG_ACK],
            "AMEND": [SL["amendment_root"]], "NOTE": [SL["spotlight_note"]], "WIN": [IDS["threads"]["Hootline"]]}[rule]


def base_route(record_id):
    if record_id == B.BASE["balancy_thread"]:
        return {"service": "gmail", "file": "threads/frederick@harmonygames.co_1840501641217286806.json",
                "pointer": "/messages", "field": "thread_id"}
    return None
