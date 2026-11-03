"""Solver for the Frederick Q4 update send-list task (tools/oracle_kit.py contract).

rev7: the job is the bridge part of the Q4 investor update send list (the board pre-read job duplicated other
contributors' tasks). Each firm's state is worked out as before; the send list keeps New investor (signed SAFE, with
amount), In talks (incl. unsigned angels with their amount; build access for firms), Awaiting reply and Keep warm
(passed after a pitch call or meeting); email-only passes and firms not contacted stay off. Truth as of end of day
Tue Sep 30, 2025 (Pacific), from the base universe plus the
injection SQL (parsed with tools/base_check.parse_sql; never executed). One rule per mechanism_portfolio entry; each
rule has a natural-reading fallback that `disable` switches on, whole or per key set.

Base statuses for list firms the task does not hinge on come from BASE_STATUS (each with its deciding record ids).
rev4: every status is settled by a record or by a rule in the Oct 14 template (no two-reading firms remain), so
`accepted` stays empty; angels who said yes are In talks with Build access blank (template rule).
rev6: three corrections moved (Anton's amount -> Leonard's DM, SciPlay's pass -> a #executives thread reply, the Play
tester gap -> Arthur's #zombie-match3d post); each rule reads the rev6 record and keeps the rev5 record as a fallback so
the rev5 SQL still reproduces the rev5 truth (oracle_kit contract.regression).
rev9: Leonard's Sep 29 card comment adds a checklist per group on the Existing Investor Update card and an "F/up with"
card in To Do for everyone In talks or Awaiting reply (Follow-up field): NCsoft already has Leonard's open To Do card named
for its partner Anel (comment there, rule DUP); Dentsu (base Oct 1 meeting) and Makers (seeded Oct 8 call) are on Fred's
calendar after Sep 30 and get no card (rule BOOKED; the Makers call is titled by its partner, Michael Cheung).
rev11: Paul Heydon backs out on Sep 30 (mail to Leonard only); Leonard relays it in the thread under his Sep 19 #executives
angel post (S_LEO_PAUL_OUT), so Paul passed without a call and stays off the send list (rule DONE1, now a correction in a
thread reply). Arthur's Sep 30 answer to Karthic in the T-Accelerate thread (M_TACC_ARTHUR: the Play tester list for the
investor accounts was never attached) is a second record of the Play gap beside his #zombie-match3d reply (rule DONE2).
rev12 (rev11 baseline: Paul and the T-Accelerate mail were found by every run): Leonard's "Paul's out" moves to his 1:1 DM
with Frederick (S_LEO_PAUL_OUT_DM); the angel post has no replies again. Arthur's correction is his own #zombie-match3d root
post again (same record id as rev9/rev10/rev11, now a root) naming everyone on the investor tester list, and ZOM-567 logs
two more firms in talks (NCsoft, Brightwater), so the Play gap decides four Build access cells. The T-Accelerate mail
replies are gone.
"""
import collections
import json
from pathlib import Path

KEY_REGEX = r".+"
FIELDS = ["Firm", "Group", "Amount", "Build access", "Keep warm", "Follow-up"]
CLASS_FIELD, GROUPS_FIELD = "Group", "groups"

FRED = "frederick.stone@harmonygames.co"
# seeded deciding records (ids as written by Working_Files/plan/build_sql.py)
S_ROB_SCI = "229090ba6b316b667d1a6451b0297a47"          # rev6 C07C2866011/1759248360.377105, Robert (thread reply): Sciplay out
S_ROB_SCI_REV5 = "cf10d4f7f88143dc7ab976df27513790"     # rev5 C096HFA5Z8W/1759184040.552871 (removed in rev6)
S_DM_ANTON = "99b22482ddd77dd01b451afb39014839"         # rev6 D05S58U4SAK/1758731100.281734, Leonard: Anton down to 25, re-sending
S_DM_ANTON_SIGNED = "f7261dd1b05eb2da3b81fe7d8cde2854"  # rev6 D05S58U4SAK/1758914100.640218, Leonard: Anton signed the 25 one
S_ZM_ARTHUR = "3cddf83c394676d8b72c0c20ed58f520"        # rev6 C0880U9751A/1759274400.518306, Arthur: Play tester list never attached
S_ANGELS = "4921f321db5d08f936aac24a6a1d2af8"           # C07C2866011/1758303600.418207, Leonard: angels "in"
S_LEO_PAUL_OUT = "7fe55f3086c1b6bcdb5dec66b00cff56"     # rev11 C07C2866011/1759251900.863415, Leonard (reply under S_ANGELS): Paul's out
S_LEO_PAUL_OUT_DM = "c5657466a4af062ceef9f7c3285aeb74"  # rev12 D05S58U4SAK/1759251900.863415, Leonard (1:1 DM): Paul's out
CT_EDITH, CT_ILSE, CT_KARTHIC = "e3a91c07d5b48f26a0c7e314", "b72f0d6e19c3a84e5d21f9a0", "5d0e8b31f7a29c64e1b0d3a8"
EVT_BRIGHT = "evt_2f86b0d4c9e17a35b64e0d"
LIN_DENTSU, LIN_TACC = "lc_b549f3057640a5eb08f7581e", "lc_94eb35d962cfbdd31e1bd496"
LIN_NCSOFT, LIN_BRIGHT = "lc_4369758f577612cdb63b3457", "lc_5e2ff140afff06e3a78e2fe1"   # rev12 ZOM-567 comments
TR_KW_CMT = "68c64270d660c977c4696986"
TR_Q4_CMT = "68db03b86054eff7e8e92474"                 # rev9 Leonard Sep 29 card comment: checklist per group + follow-up cards
TR_FU_ANEL = "68c99e98737744bd966aed24"                # rev9 Leonard Sep 16 To Do card "F/up with Anel after the engine deep dive" (NCsoft)
EVT_MAKERS = "evt_6b2e94d0c17a3f58e9d2b1"              # rev9 Fred's copy: Michael Cheung and Leonard Hayes (Makers Fund), Wed Oct 8
B_EVT_DENTSU = "evt_3671b9a924ccba550e51fa"            # base Fred's copy: Harmony Games & Dentsu, Wed Oct 1 (created Sep 30 PT)
FOLLOWUP_GROUPS = ("In talks", "Awaiting reply")
S_LEO_1AM = "1a68c2da0f36fc25489d3d9bbe9ccc32"         # C096HFA5Z8W/1757365500.384216, Leonard: 1AM Gaming = March Gaming Fund, passed
S_LEO_PLAY = "c183280a284440a6ca6cdbb5270c9139"        # C096HFA5Z8W/1758817200.730591, Leonard: Play's no went to Griffin, still a no
S_LEO_TREO = "19e1e65d5952f075e8492867c6bcd472"        # C096HFA5Z8W/1756942260.617302, Leonard: Treo pinged him Sep 3, deck sent
S_LEO_INITIAL = "800870c56bda852a57dfa06cb4fd63e6"     # C096HFA5Z8W/1757442000.492583, Leonard: pinged Initial Capital on LinkedIn, they answered
S_LEO_MATTEL = "398502c0596e5347cc297f61eaefbd50"      # C096HFA5Z8W/1758927000.205874, Leonard: Mattel was RFP only, not pitched the bridge

# deciding message rows (Frederick's copies; ids as written by build_sql.py)
M_ANTON = "frederick.stone@harmonygames.co/<CACJhvEE55qdWXuKC3BWlscoxBKrLUWavLQ3cpTJ@mail.gmail.com>"   # rev5 only
M_DS_ANTON = "frederick.stone@harmonygames.co/<CAiKDPIoVSAFUBccUSRRBTi6dsmJdhof2EzteoIx@mail.gmail.com>"
M_PAUL = "frederick.stone@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com>"
M_HIRO = "frederick.stone@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>"
M_DENTSU = "frederick.stone@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>"
M_BRIGHT = "frederick.stone@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>"
M_BRIGHT_RE = "frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>"
M_TACC_ARTHUR = "frederick.stone@harmonygames.co/<CAU8zEO-shvUXQVk4-lQPDj5ihq08pcABtHRrtUv@mail.gmail.com>"   # rev11 Arthur to Karthic: Play tester list never attached

RULES = {
    "DONE1": {"mechanism": "A14", "requirement": "R3", "nodes": ["T1", "C1"], "decides": ["Group", "Amount"],
              "natural_reading": "Paul Heydon In talks at $50,000: he said yes and the SAFE is still waiting on him",
              "family": "superseding", "source": "leonard_dm_relay", "controls": ["Anton Bernstein"], "over_application": "done1_over"},
    "INPUT": {"mechanism": "A11", "requirement": "R3", "nodes": ["T4"], "decides": ["Amount"],
              "natural_reading": "Anton at the $40K posted in #executives and on the Bridge angels sheet",
              "family": "superseding", "source": "leonard_dm", "controls": ["GFR Fund"], "over_application": "input_over"},
    "DONE2": {"mechanism": "A24", "requirement": "R4", "nodes": ["T2"], "decides": ["Build access"],
              "natural_reading": "T-Accelerate, Dentsu, NCsoft and Brightwater on both platforms because ZOM-567 logs both tracks",
              "family": "done_gap", "source": "arthur_root_post", "controls": ["GFR Fund"], "over_application": "done2_over"},
    "CORR": {"mechanism": "A14", "requirement": "R2", "nodes": ["T3", "C2"], "decides": ["Group", "Keep warm"],
             "natural_reading": "Sciplay In talks from its own mail thread",
             "family": "superseding", "source": "exec_thread_reply", "controls": ["Dentsu Ventures"], "over_application": "corr_over"},
    "ALIAS": {"mechanism": "A7", "requirement": "R2", "nodes": ["T5", "C3"], "decides": ["Group", "Keep warm"],
              "natural_reading": "Hiro Capital Awaiting reply from the list row",
              "family": "scope_alias", "source": "contacts", "controls": ["Makers Fund"], "over_application": "alias_over"},
    "FILT": {"mechanism": "A17", "requirement": "R1", "nodes": ["T6", "T7", "C4"], "decides": ["groups"],
             "natural_reading": "the send list looks only at the 2025 list rows",
             "family": "exact_predicate", "source": "calendar", "controls": ["T-accelerate"], "over_application": "filt_over"},
    "FOLLOW": {"mechanism": "A15", "requirement": "R6", "nodes": ["T8", "C5"], "decides": ["Keep warm"],
               "natural_reading": "no keep-warm checklist items",
               "family": "authority", "source": "card_rule", "controls": ["Dentsu Ventures"], "over_application": "follow_over"},
    "DUP": {"mechanism": "A7", "requirement": "R8", "nodes": ["T12", "C6"], "decides": ["Follow-up"],
            "natural_reading": "a new F/up card for NCsoft: the open To Do card names only Anel",
            "family": "scope_alias", "source": "trello_todo", "controls": ["GFR Fund"], "over_application": "dup_over"},
    "BOOKED": {"mechanism": "A17", "requirement": "R8", "nodes": ["T13", "C7"], "decides": ["Follow-up"],
               "natural_reading": "follow-up cards for Dentsu and Makers: the calendar is read only through Sep 30, or the person-titled Oct 8 call is not tied to Makers",
               "family": "exact_predicate", "source": "calendar_october", "controls": ["BBQ Capital"],
               "over_application": "booked_over"},
}
DEGRADES = {
    "done1_over": "drop the signed angel (Anton) from the send list too, as if he had backed out",
    "input_over": "put an amount on a firm in talks (GFR Fund) as if a 1:1 note had given one",
    "done2_over": "give GFR Fund iOS access as if it had been added to TestFlight (it never was)",
    "corr_over": "read Dentsu (in talks) as passed after a pitch (Keep warm)",
    "alias_over": "map an unrelated partner reply onto Makers Fund (passed, off the list)",
    "filt_over": "split PXLite off T-Accelerate as its own off-list firm",
    "follow_over": "add every firm in talks (Dentsu) to keep-warm",
    "dup_over": "comment on another open To Do card for GFR Fund instead of giving it its own follow-up card",
    "booked_over": "skip BBQ Capital's follow-up card as if it had a call booked after Sep 30",
    "filt_miss": "a member of the off-list population is not found (calendar-call channel)",
}
CHANNELS = {
    "CH-FILT-HOMA": {"kind": "scale", "degrade": "filt_miss", "members": ["Homa"], "latent": "member",
                     "family": "exact_predicate", "rule": "FILT", "source": "calendar",
                     "description": "Homa's call (person-titled event; HOMA only in the invitation body) is not found"},
    "CH-FILT-BRIGHT": {"kind": "scale", "degrade": "filt_miss", "members": ["Brightwater Games Fund"], "latent": "member",
                       "family": "exact_predicate", "rule": "FILT", "source": "calendar",
                       "description": "the Sep 25 'Ilse Marrow and Leonard Hayes' call is not mapped to Brightwater"},
}

OFFLIST = ["Homa", "Brightwater Games Fund"]
PASS_AFTER_PITCH = ["London Venture Partners"]          # base: call Sep 9 (evt_e59dc0a675d0c407b79acf), pass Sep 25
IN_TALKS = ["Dentsu Ventures", "NCsoft", "GFR Fund", "T-accelerate", "Homa", "Brightwater Games Fund"]
BASE_STATUS = {   # rev4 template rules + Leonard's notes: firm -> (status, alternatives, deciding evidence)
    "London Venture Partners": ("Passed", [], [f"{FRED}/1842277743427687737"]),
    "Grishin Robotics": ("Passed", [], [f"{FRED}/1842278603974731778"]),
    "Lakestar Ventures": ("Passed", [], [f"{FRED}/1842279175401495849"]),
    "Play Ventures": ("Passed", [], ["C096HFA5Z8W/1757955553.793529", S_LEO_PLAY]),
    "March Gaming Fund": ("Passed", [], [f"{FRED}/1842278301421016623", S_LEO_1AM]),
    "Andreessen Horowitz": ("In talks", [], [f"{FRED}/1842277213140775733", "evt_e802a3583ee79ff6087f76"]),
    "Dentsu Ventures": ("In talks", [], [f"{FRED}/1843473831194478743"]),
    "NCsoft": ("In talks", [], [f"{FRED}/1832208184829815962"]),
    "GFR Fund": ("In talks", [], [f"{FRED}/1843547312959065138"]),
    "T-accelerate": ("In talks", [], [f"{FRED}/1842283406259093714"]),
    "Sciplay": ("In talks", [], [f"{FRED}/1842285743246816270"]),          # overturned by CORR
    "Hiro Capital": ("Awaiting reply", [], ["f_48247af79428823c3cac92"]),  # overturned by ALIAS
    "Anton Bernstein": ("In talks", [], [S_ANGELS]),                       # angel who said yes (template rule)
    "Paul Heydon": ("In talks", [], [S_ANGELS]),
    "Makers Fund": ("Awaiting reply", [], [f"{FRED}/1842277859335386393"]),
    "Raine Ventures": ("Awaiting reply", [], [f"{FRED}/1842279098258817066"]),
    "BBQ Capital": ("Awaiting reply", [], ["C096HFA5Z8W/1757345124.546449"]),
    "General Catalyst": ("Awaiting reply", [], ["C096HFA5Z8W/1757716998.377299"]),   # outreach by IH counts as ours
    "Sony Mobile": ("Awaiting reply", [], ["f_48247af79428823c3cac92"]),
    "Revo Capital": ("Awaiting reply", [], ["C096HFA5Z8W/1757345124.546449"]),
    "e2vc": ("Awaiting reply", [], ["C096HFA5Z8W/1757345124.546449"]),
    "Superplay": ("Awaiting reply", [], ["f_48247af79428823c3cac92", f"{FRED}/1842285179768836773"]),
    "Treo VC": ("Awaiting reply", [], ["C096HFA5Z8W/1756941551.539229", S_LEO_TREO]),
    "Initial Capital": ("Awaiting reply", [], ["f_48247af79428823c3cac92", S_LEO_INITIAL]),   # Latest Status: they answered, no call, no no
    "[PERSON_NAME_5402]": ("Passed", [], ["f_48247af79428823c3cac92"]),       # Latest Status "They don't do bridge" counts as written
    "BITKRAFT Ventures": ("Awaiting reply", [], ["C096HFA5Z8W/1758563861.649039", f"{FRED}/1843988506059556678"]),
    "Triptyq": ("Awaiting reply", [], ["C096HFA5Z8W/1757716998.377299"]),
    "Turkven": ("Awaiting reply", [], ["C096HFA5Z8W/1757716998.377299"]),
    "Harlem Capital": ("Awaiting reply", [], ["C096HFA5Z8W/1757716998.377299"]),
    "Mattel": ("Not contacted this round", [], [S_LEO_MATTEL]),            # RFP / partnership only (template rule)
    "Transcend Fund": ("Not contacted this round", [], ["f_48247af79428823c3cac92"]),   # a plan to reach out only
    "Acterra": ("Not contacted this round", [], ["f_48247af79428823c3cac92"]),
    "Index Ventures": ("Not contacted this round", [], ["C096HFA5Z8W/1757345124.546449"]),   # earlier-round answer
}
BASE_STATUS_REV3 = {   # rev1-rev3 template: firm -> (status, accepted alternatives, base evidence)
    "London Venture Partners": ("Passed", [], [f"{FRED}/1842277743427687737"]),
    "Grishin Robotics": ("Passed", [], [f"{FRED}/1842278603974731778"]),
    "Lakestar Ventures": ("Passed", [], ["C096HFA5Z8W/1757345124.546449"]),
    "Play Ventures": ("Passed", ["Awaiting reply"], ["C096HFA5Z8W/1757955553.793529", "C096HFA5Z8W/1758671737.632949"]),
    "Andreessen Horowitz": ("In talks", ["Passed"], [f"{FRED}/1842277213140775733", f"{FRED}/1844748127814183717"]),
    "Dentsu Ventures": ("In talks", [], [f"{FRED}/1843473831194478743"]),
    "NCsoft": ("In talks", [], [f"{FRED}/1832208184829815962"]),
    "GFR Fund": ("In talks", [], [f"{FRED}/1843547312959065138"]),
    "T-accelerate": ("In talks", [], [f"{FRED}/1842283406259093714"]),
    "Sciplay": ("In talks", [], [f"{FRED}/1842285743246816270"]),          # overturned by CORR
    "Hiro Capital": ("Awaiting reply", [], ["f_48247af79428823c3cac92"]),  # overturned by ALIAS
    "Makers Fund": ("Awaiting reply", [], ["C096HFA5Z8W/1757345124.546449"]),
    "Raine Ventures": ("Awaiting reply", [], ["C096HFA5Z8W/1757345124.546449"]),
    "BBQ Capital": ("Awaiting reply", [], ["C096HFA5Z8W/1757345124.546449"]),
    "General Catalyst": ("Awaiting reply", ["Not contacted this round"], ["f_48247af79428823c3cac92"]),
    "Sony Mobile": ("Awaiting reply", [], ["f_48247af79428823c3cac92"]),
    "Revo Capital": ("Awaiting reply", [], ["C096HFA5Z8W/1757345124.546449"]),
    "e2vc": ("Awaiting reply", [], ["C096HFA5Z8W/1757345124.546449"]),
    "Superplay": ("Awaiting reply", ["Not contacted this round"], ["f_48247af79428823c3cac92"]),
    "Mattel": ("Awaiting reply", ["In talks"], ["C096HFA5Z8W/1756941551.539229"]),
    "Treo VC": ("Awaiting reply", ["In talks"], ["C096HFA5Z8W/1757345124.546449"]),
    "BITKRAFT Ventures": ("Awaiting reply", ["Not contacted this round"], ["C096HFA5Z8W/1758563861.649039"]),
    "Triptyq": ("Awaiting reply", ["Not contacted this round"], ["C096HFA5Z8W/1757716998.377299"]),
    "Turkven": ("Awaiting reply", ["Not contacted this round"], ["C096HFA5Z8W/1757716998.377299"]),
    "Harlem Capital": ("Awaiting reply", ["Not contacted this round"], ["C096HFA5Z8W/1757716998.377299"]),
    "Transcend Fund": ("Not contacted this round", ["Awaiting reply"], ["f_48247af79428823c3cac92"]),
    "Acterra": ("Not contacted this round", ["Awaiting reply"], ["f_48247af79428823c3cac92"]),
    "March Gaming Fund": ("Not contacted this round", ["Passed"], ["f_48247af79428823c3cac92"]),
    "Index Ventures": ("Not contacted this round", ["Passed"], ["C096HFA5Z8W/1757345124.546449"]),
}
REV4_RULES = "Angels who've said yes this round go under In talks"   # the rev4-rev6 template wording
REV7_RULES = "Angels who've said yes but haven't signed go here too"  # the rev7 send-list doc wording
REV4_NOTES = {"Play Ventures": S_LEO_PLAY, "March Gaming Fund": S_LEO_1AM, "Mattel": S_LEO_MATTEL, "Treo VC": S_LEO_TREO, "Initial Capital": S_LEO_INITIAL}
ANGELS = {"Paul Heydon": 50000, "Anton Bernstein": 40000}   # as posted in #executives (S_ANGELS)


def _list_keys():
    import ast
    here = Path(__file__).resolve()
    data = here.parents[4] / "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gsheets/data.json"
    d = json.loads(data.read_text())
    sp = next(x for x in d["sheets_spreadsheets"] if x["spreadsheet_id"] == "f_48247af79428823c3cac92")
    sh = ast.literal_eval(sp["sheets"]) if isinstance(sp["sheets"], str) else sp["sheets"]
    seen, keys = set(), []
    for r in sh[0]["grid"][1:]:
        f = (r[1] if len(r) > 1 else "").strip()
        if f and f.lower() not in seen:
            seen.add(f.lower())
            keys.append(f)
    return keys


def load_state(sql_text, revision=None):
    from base_check import parse_sql
    rows = [x for x in parse_sql(sql_text) if x["op"] == "insert"]
    by_id = {}
    for x in rows:
        r = x["row"]
        for k in ("id", "contact_id", "event_id", "spreadsheet_id"):
            if r.get(k):
                by_id[str(r[k])] = r
    texts = " ".join(json.dumps(x["row"], ensure_ascii=False) for x in rows)
    return {"by_id": by_id, "text": texts, "list_keys": _list_keys(), "revision": revision or "rev1"}


def _hit(spec, name, key):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and key in d[1]) for d in spec)


def keys_of(state):
    return state["list_keys"] + OFFLIST


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    b = state["by_id"]
    have = lambda i: i in b
    posted = have(S_ANGELS)                       # the #executives post is the only record of the angels' amounts
    paul_completed = "Completed: Complete with docusign: Harmony Games SAFE - Paul Heydon" in state["text"]
    anton_completed = have(M_DS_ANTON)
    anton_latest = 25000 if (have(S_DM_ANTON) or have(M_ANTON)) else ANGELS["Anton Bernstein"]
    play_gap = have(S_ZM_ARTHUR) or have(M_TACC_ARTHUR)   # rev6/rev11/rev12: no investor tester can get the Android build
    dentsu_play_missing = play_gap or "Play internal track not added" in state["text"]   # rev5: ticket caveat
    out = {}
    universe = list(keys_ or keys_of(state))
    if _hit(degrade, "filt_over", "T-accelerate") and "T-accelerate" in universe:
        universe.append("PXLite")
    for k in universe:
        missed = k in OFFLIST and (_hit(disable, "FILT", k) or _hit(degrade, "filt_miss", k))
        if k in OFFLIST:
            ok = have(M_BRIGHT) and have(M_BRIGHT_RE) if k == "Brightwater Games Fund" else True
            if not ok:
                missed = True
        rev4 = REV4_RULES in state["text"] or REV7_RULES in state["text"]
        table = BASE_STATUS if rev4 and (k not in REV4_NOTES or have(REV4_NOTES[k])) else BASE_STATUS_REV3
        status, accepted, ev = table.get(k, ("Not contacted this round", [], ["f_48247af79428823c3cac92"]))
        if k in OFFLIST or k == "PXLite":
            status, accepted, ev = "In talks", [], [EVT_BRIGHT] if k == "Brightwater Games Fund" else ["evt_89381fe5a15b802c5652a9"]
        if k == "Sciplay" and (have(S_ROB_SCI) or have(S_ROB_SCI_REV5)) and not _hit(disable, "CORR", k):
            status, ev = "Passed", [S_ROB_SCI]
        if k == "Hiro Capital" and have(M_HIRO) and have(CT_EDITH) and not _hit(disable, "ALIAS", k):
            status, ev = "Passed", [CT_EDITH]
        paul_out = S_LEO_PAUL_OUT_DM if have(S_LEO_PAUL_OUT_DM) else (S_LEO_PAUL_OUT if have(S_LEO_PAUL_OUT) else None)
        if k == "Paul Heydon" and paul_out and not _hit(disable, "DONE1", k):
            status, ev = "Passed", [paul_out]                # rev11/rev12: backed out, no call: off the send list
        if k == "Anton Bernstein" and _hit(degrade, "done1_over", k):
            status = "Passed"
        if k == "T-accelerate" and _hit(degrade, "filt_over", k):
            status = "Not contacted this round"
        if k == "Dentsu Ventures" and _hit(degrade, "corr_over", k):
            status = "Passed"
        if k == "Makers Fund" and _hit(degrade, "alias_over", k):
            status = "Passed"
        access = None
        if status == "In talks" and k not in ANGELS:      # template: leave Build access blank for angels
            access = "none"
            if k == "Dentsu Ventures":
                access = "iOS and Android" if (_hit(disable, "DONE2", k) or not have(LIN_DENTSU) or not dentsu_play_missing) else "iOS only"
            if k == "T-accelerate":
                access = "iOS only" if (play_gap and not _hit(disable, "DONE2", k)) else "iOS and Android"
            if k in ("NCsoft", "Brightwater Games Fund") and have({"NCsoft": LIN_NCSOFT, "Brightwater Games Fund": LIN_BRIGHT}[k]):
                access = "iOS only" if (play_gap and not _hit(disable, "DONE2", k)) else "iOS and Android"   # rev12
            if k == "GFR Fund" and _hit(degrade, "done2_over", k):
                access = "iOS only"
        committed = soft = None
        if (k in ANGELS and not posted) or status == "Passed":
            pass
        elif k == "Paul Heydon":
            if paul_completed:
                committed = ANGELS[k]
            else:
                soft = ANGELS[k]
        elif k == "Anton Bernstein":
            amount = ANGELS[k] if _hit(disable, "INPUT", k) else anton_latest
            if _hit(degrade, "done1_over", k) or not anton_completed:
                soft = amount
            else:
                committed = amount
        pitched_pass = status == "Passed" and (k in PASS_AFTER_PITCH or k in ("Sciplay", "Hiro Capital"))
        keep = "yes" if (pitched_pass and have(TR_KW_CMT) and not _hit(disable, "FOLLOW", k)) else "no"
        if k == "Dentsu Ventures" and _hit(degrade, "follow_over", k):
            keep = "yes"
        # rev7 send-list groups
        if committed:
            group, amount = "New investor", committed
        elif status == "In talks":
            group, amount = "In talks", soft
        elif status == "Awaiting reply":
            group, amount = "Awaiting reply", None
        elif status == "Passed" and (pitched_pass or (k == "Dentsu Ventures" and _hit(degrade, "corr_over", k))):
            group, amount = "Keep warm", None
        else:
            group, amount = None, None
        if group != "In talks":
            access = None
        if k == "GFR Fund" and _hit(degrade, "input_over", k) and group == "In talks":
            amount = 25000
        groups = (["register"] if group else []) + (["keepwarm"] if keep == "yes" else []) + \
                 (["in_talks"] if group == "In talks" else []) + (["new_investor"] if group == "New investor" else [])
        # rev9 follow-up cards (Leonard's Sep 29 card comment): everyone In talks or Awaiting reply gets an "F/up with" card in
        # To Do; one that already has a To Do card gets a comment on it; one with a call or meeting on Fred's calendar
        # after Sep 30 gets nothing
        follow = None
        if have(TR_Q4_CMT) and group in FOLLOWUP_GROUPS and not missed:
            follow = "card"
            if k == "NCsoft" and have(TR_FU_ANEL) and not _hit(disable, "DUP", k):
                follow = "comment"
            if k == "GFR Fund" and _hit(degrade, "dup_over", k):
                follow = "comment"
            booked = k == "Dentsu Ventures" or (k == "Makers Fund" and have(EVT_MAKERS))
            if booked and not _hit(disable, "BOOKED", k):
                follow = "none"
            if k == "BBQ Capital" and _hit(degrade, "booked_over", k):
                follow = "none"
        if follow == "card":
            groups = groups + ["followup_card"]
        elif follow == "comment":
            groups = groups + ["followup_comment"]
        if missed:      # the firm is left off the send list: no row is written for it
            group, amount, access, groups, accepted, follow = None, None, None, [], [], None
        firm_ev = [x for x in ev if x in b]
        out[k] = {"Firm": k, "Group": group, "Status": status, "accepted_status": accepted, "Amount": amount,
                  "Build access": access, "Keep warm": keep, "Follow-up": follow, "groups": groups,
                  "evidence": {"Group": ev, "Firm": firm_ev}}
    return out


def aggregates(rows):
    groups = collections.defaultdict(list)
    for k in sorted(rows):
        for g in rows[k]["groups"]:
            groups[g].append(k)
    listed = [v for v in rows.values() if v["Group"]]
    return {"classes": dict(sorted(collections.Counter(v["Group"] for v in listed).items())),
            "groups": {g: groups[g] for g in sorted(groups)},
            "totals": {"send_list_size": len(listed),
                       "new_investor_total": sum(v["Amount"] or 0 for v in listed if v["Group"] == "New investor"),
                       "keep_warm": len(groups.get("keepwarm", [])),
                       "followup_cards": len(groups.get("followup_card", [])),
                       "followup_comments": len(groups.get("followup_comment", []))}}


def evidence(rows, key, field):
    if field == "Firm":
        return list(rows[key]["evidence"]["Firm"])
    return []


def touched(state, rule):
    return {"DONE1": {"Paul Heydon"}, "INPUT": {"Anton Bernstein"}, "DONE2": {"Dentsu Ventures", "T-accelerate", "NCsoft", "Brightwater Games Fund"}, "CORR": {"Sciplay"},
            "ALIAS": {"Hiro Capital"}, "FILT": set(OFFLIST), "FOLLOW": {"London Venture Partners", "Sciplay", "Hiro Capital"},
            "DUP": {"NCsoft"}, "BOOKED": {"Dentsu Ventures", "Makers Fund"}}[rule]


def deciding(state, rule, key):
    return {"DONE1": [S_ANGELS, S_LEO_PAUL_OUT_DM], "INPUT": [S_DM_ANTON, S_DM_ANTON_SIGNED], "DONE2": [S_ZM_ARTHUR, LIN_TACC, LIN_DENTSU, LIN_NCSOFT, LIN_BRIGHT], "CORR": [S_ROB_SCI],
            "ALIAS": [M_HIRO], "FILT": [M_BRIGHT, M_BRIGHT_RE], "FOLLOW": [TR_KW_CMT],
            "DUP": [TR_FU_ANEL, TR_Q4_CMT], "BOOKED": [EVT_MAKERS, TR_Q4_CMT]}[rule]


def base_route(record_id):
    return None
