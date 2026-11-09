#!/usr/bin/env python3
"""Scenario builder (design stage) for Samuel Turner · Zombie Match beta player messages.

Writes Working_Files/01_Hardness_Manifest.draft.json, Working_Files/01_Gradable_Surface.json and plan/ids.json.
Design only: the seeded texts quoted here are the planned wording /create-injection must use verbatim.
Ids are minted deterministically (sha256 of a label). No prompt, Oracle Event or criterion text lives here.
"""
import hashlib, json, os
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
CTX = json.load(open(os.path.join(WF, "00_Task_Context.json")))
SAM = "samuel.turner@harmonygames.co"
SALT = "hg-samuel-zm-beta-messages|"


def hx(label, n):
    return hashlib.sha256((SALT + label).encode()).hexdigest()[:n]


def ts(iso):
    return int(datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp())


def drive(label):
    return "f_" + hx(label, 22)


def evt(label):
    return "evt_" + hx(label, 22)


def trello(label, iso):
    return "%08x" % ts(iso) + hx(label, 16)


def thread(label, iso):
    return str(((ts(iso) * 1000) << 20) + (int(hx(label, 8), 16) & 0xFFFFF))


def slack_ts(label, iso):
    return f"{ts(iso)}.{int(hx(label, 8), 16) % 1000000:06d}"


def gm(tid):
    return f"{SAM}/{tid}"


def cmt(label):
    return "cmt_" + hx(label, 20)


# ---------------------------------------------------------------- base records (all read through hg.py)
DM_LEONARD = "D06L58XCVKK"
DM_VINCENT = "D06UFE81RF0"
DM_ROBERT = "D06KPMDV2JZ"
DM_ARTHUR = "D06KV30TPL4"
ZM3D = "C0880U9751A"
ZBUGS = "C08R27X0EAH"
ZART = "C08R8CHB0QL"
INTERNAL = "C05KNDCHAAG"
BOARD = "6851a6569f3bf818760632ab"
BASE = {
    "folder": "d_caafeec2804b3a67ce46aa",
    "pn_sheet": "f_a325dd4af80afc5994d5dc",
    "pn_card": "6851a769c65dc0017a227bb7",
    "tech_card": "68d1eb90bef538c7c5c5599d",
    "minor_bugs_card": "68c451141c69fb8af1b4568e",
    "hourly_card": "68c45bba5d2c25a3a5c26a8c",
    "axe_card": "6851a7a6c31a93809acded72",
    "gtm_beta_doc": "f_ffbe775ff72a994c5d6b7c",
    "pr248": "harmonygames-Games/match3d#248",
    "pr292": "harmonygames-Games/match3d#292",
    "cr_strings": "harmonygames-Games/match3d#248#rc_10",
    "pns_sent": f"{DM_LEONARD}/1750138057.452159",
    "same_as_dd": f"{DM_LEONARD}/1750138076.953689",
    "shove_to_20": f"{DM_ROBERT}/1752162738.497679",
    "variant_c_13": f"{ZBUGS}/1755084279.518809",
    "pushed_back": f"{ZBUGS}/1758238811.686629",
    "all_local": f"{ZBUGS}/1758239520.618939",
    "at_the_beginning": f"{ZBUGS}/1758291802.756889",
    "no_push_yet": f"{DM_ARTHUR}/1750979784.704799",
    "push_vs_local": f"{DM_ARTHUR}/1750979856.324639",
    "beta_scope": f"{INTERNAL}/1757704290.799329",
    "axe_postponed": f"{INTERNAL}/1758558164.541689",
    "martin_root": f"{ZART}/1759159849.386619",
    "android_2007_root": f"{DM_VINCENT}/1759163970.141449",
    "liveops_page": "page_liveops_calendar",
    "release_page": "page_release_checklist",
    "gdd_page": "page_zm3d_gdd",
    "pr248_mail": gm("1836006988541924555"),
}

T = {   # seeded timestamps (UTC), all before the seed bound 2025-10-01T00:00:00Z
    "wc_ticket": "2025-09-17T15:20:00Z",
    "parent": "2025-09-23T16:40:00Z",
    "qa_note": "2025-09-15T13:05:00Z",
    "deck": "2025-09-19T18:30:00Z",
    "rule_doc": "2025-09-26T17:10:00Z",
    "copy_pass": "2025-09-25T15:00:00Z",
    "brian_opinion": "2025-09-26T18:02:00Z",
    "ask_decision": "2025-09-29T17:40:00Z",
    "boss_ask": "2025-09-24T13:10:00Z",
    "gift_ask": "2025-09-25T11:45:00Z",
    "corr_reply": "2025-09-29T18:05:00Z",
    "qa_reply": "2025-09-29T19:40:00Z",
    "freeze": "2025-09-29T20:15:00Z",
    "hub": "2025-09-30T20:40:00Z",
    "arthur_inline": "2025-06-26T20:58:00Z",
}

NEW_LINE = "Your Squad Needs You Back"

# ---------------------------------------------------------------- the 40 messages
M = []
_n = [313]


def member(key, title, source, asker, call, missing="", built=False, ticket=True, role="control", note=""):
    m = dict(key=key, title=title, source=source, asker=asker, call=call, missing=missing, built=built, role=role, note=note)
    if ticket:
        m["ticket"] = f"DES-{_n[0]}"
        _n[0] += 1
    else:
        m["ticket"] = None
    M.append(m)
    return m


CLIENT, SERVER = "not scheduled in the client", "needs a server send"
# the existing ticket outside the parent comes first: it predates the parent (ALIAS)
member("Win & Collect start", "Ping when a Collect & Win window opens", "PNs Beta row 7", "calvin.price", "Hold", CLIENT, role="ALIAS")
PARENT = f"DES-{_n[0]}"
_n[0] += 1
# sheet rows
member("Lives recharged", "PN: Lives recharged", "PNs Beta row 3", "leonard", "Go", built=True)
member("Lapsed 1 day", "PN: Lapsed 1 day", "PNs Beta row 4", "leonard", "Go", built=True, role="BUILT")
member("Lapsed 7 days", "PN: Lapsed 7 days (week-away ping)", "PNs Beta row 5", "leonard", "Go", built=True, role="CORR")
member("Finish first mission", "PN: Finish first mission", "PNs Beta row 6", "leonard", "Hold", "cannot reach its players", built=True, role="DEP")
member("Plague Race", "PN: Plague Race (race reminder)", "PNs Beta row 9", "leonard", "Hold", "not seen on both platforms", built=True, role="QA")
member("Weekly Leaderboard reset", "PN: Weekly Leaderboard reset", "PNs Beta row 14", "leonard", "Hold", "fires on the wrong day", built=True, role="DONE")
member("Quests rollover", "PN: Quests rollover", "PNs Beta row 1", "leonard", "Hold", CLIENT)
member("Login Calendar update", "PN: Login Calendar update", "PNs Beta row 12", "leonard", "Hold", CLIENT)
member("Season Pass start", "PN: Season Pass start or reward", "PNs Beta row 13", "leonard", "Hold", CLIENT)
member("Hourly Coins", "PN: Hourly Coins", "PNs Beta row 2", "leonard", "Drop")
member("Nathan's Treasure Hunt", "PN: Nathan's Treasure Hunt start", "PNs Beta row 8", "leonard", "Drop")
member("Streak Fever", "PN: Streak Fever start", "PNs Beta row 10", "leonard", "Drop")
member("Axe Arena", "PN: Axe Arena start", "PNs Beta row 11", "leonard", "Drop")
# asks filed as tickets under the parent
for key, title, asker, call, miss in [
    ("Endless entries back", "PN ask: Endless entries are back", "brian.foster", "Hold", CLIENT),
    ("Endless weekly result", "PN ask: Endless weekly result", "brian.foster", "Hold", SERVER),
    ("Boss Arena open", "PN ask: Boss Arena is open", "robert", "Hold", CLIENT),
    ("Boss Arena last hours", "PN ask: Boss Arena last hours", "robert", "Hold", CLIENT),
    ("Season Pass last 48 hours", "PN ask: Season Pass last 48 hours", "oliver.brooks", "Hold", CLIENT),
    ("Season Pass premium nudge", "PN ask: Season Pass premium nudge", "brian.foster", "Hold", SERVER),
    ("Plague Race last hour", "PN ask: Plague Race last hour", "julia.lawson", "Hold", CLIENT),
    ("Plague Race result", "PN ask: Plague Race result", "julia.lawson", "Hold", SERVER),
    ("Zombie Lane reward ready", "PN ask: Zombie Lane reward ready", "owen.baker", "Hold", CLIENT),
    ("Trophy Path reward waiting", "PN ask: Trophy Path reward waiting", "owen.baker", "Hold", CLIENT),
    ("Daily chest ready", "PN ask: Daily chest ready", "calvin.price", "Hold", CLIENT),
    ("Free shop coins ready", "PN ask: Free shop coins ready", "martin.walsh", "Hold", CLIENT),
    ("Support reply waiting", "PN ask: Support reply waiting", "owen.baker", "Hold", SERVER),
    ("New levels added", "PN ask: New levels added", "julia.lawson", "Hold", SERVER),
    ("Lapsed 3 days", "PN ask: Lapsed 3 days", "leonard", "Hold", CLIENT),
    ("Lapsed 14 days", "PN ask: Lapsed 14 days", "leonard", "Hold", CLIENT),
    ("Comeback gift", "PN ask: Comeback gift on tap", "brian.foster", "Drop", ""),
    ("Rewarded ad ready", "PN ask: Rewarded ad ready", "robert", "Drop", ""),
    ("Pop-up offer live", "PN ask: Pop-up offer live", "brian.foster", "Drop", ""),
    ("Lava Event start", "PN ask: Lava Event start", "robert", "Drop", ""),
    ("PvP Event start", "PN ask: PvP Event start", "robert", "Drop", ""),
    ("Wild card ready", "PN ask: Wild card ready", "robert", "Drop", ""),
    ("Team battle start", "PN ask: Team battle start", "brian.foster", "Drop", ""),
    ("Bones mode reward", "PN ask: Bones mode reward", "robert", "Drop", ""),
]:
    member(key, title, "ask under the parent", asker, call, miss)
# asks outside the parent: comments on base tickets (FILT)
member("Boss Arena attempts refilled", "", "comment on ZOM-542", "brian.foster", "Hold", CLIENT, ticket=False, role="FILT")
member("Daily gift about to reset", "", "comment on ZOM-556", "julia.lawson", "Hold", CLIENT, ticket=False, role="FILT")

K = {m["key"]: m for m in M}
COUNTS = {c: sum(1 for m in M if m["call"] == c) for c in ("Go", "Hold", "Drop")}
TICKETED = [m for m in M if m["ticket"]]
N_NOTES = len(TICKETED)
N_UPDATES = sum(1 for m in TICKETED if m["call"] in ("Hold", "Drop"))
N_NEW = sum(1 for m in M if not m["ticket"]) + 1          # two asks + one string ticket
TK = {m["key"]: m["ticket"] for m in TICKETED}
LAST_TICKET = _n[0] - 1

IDS = {
    "hub": f"{DM_LEONARD}/" + slack_ts("hub", T["hub"]),
    "rule_doc": drive("rule-doc"),
    "deck": drive("beta-deck"),
    "qa_thread": gm(thread("qa-note", T["qa_note"])),
    "arthur_inline": BASE["pr248"] + "#rc_18",
    "arthur_mail": gm(thread("arthur-inline-mail", T["arthur_inline"])),
    "ask_decision": f"{ZM3D}/" + slack_ts("ask-decision", T["ask_decision"]),
    "brian_opinion": f"{ZM3D}/" + slack_ts("brian-opinion", T["brian_opinion"]),
    "corr_reply": f"{ZART}/" + slack_ts("corr-reply", T["corr_reply"]),
    "qa_reply": f"{DM_VINCENT}/" + slack_ts("qa-reply", T["qa_reply"]),
    "freeze_comment": trello("freeze-comment", T["freeze"]),
    "copy_pass": evt("copy-pass"),
    "boss_ask": cmt("boss-ask"),
    "gift_ask": cmt("gift-ask"),
    "race_qa": cmt("race-qa"),
    "weekly_qa": cmt("weekly-qa"),
    "ftue_qa": cmt("ftue-qa"),
    "parent": PARENT,
}

Q = {  # planned wording; every delegation quote is a verbatim span of these records
    "hub": ("Samuel, before beta goes out I want one straight answer on player messages. The PN sheet says six are Ready and I don't trust that. "
            "Take every row on the PNs Beta tab plus every ask for a new phone message that's been filed on a ticket or a card up to today, and make a call on each one using the message rule doc. "
            "Put it in one sheet in your Drive folder, one row per message: Message, Ticket, Call, What's missing, Fires as built, Final headline, String change. "
            f"I made a ticket per message under {PARENT}, leave the call as a comment on each ticket and move the ticket to match. "
            "Anything with no ticket gets one, but don't make a second one for something that already has a ticket under whatever name. "
            "Every Go goes on a checklist on our push notifications card so Vincent can tick it off. "
            "When it's done tell me here how many Go, Hold and Drop."),
    "rule": ("Beta message rule. A message is anything the game puts on a player's phone while the game is closed. "
             "Go: the feature behind it is in the beta, the client already schedules it, it fires on the right day, it can reach the players it is written for, and Vincent has seen it arrive on both iOS and Android. "
             "Hold: the feature is in the beta but one of those is missing. Name the one thing missing. "
             "Drop: the feature behind it is not in the beta. "
             "In the beta means live today or on the BETA list of the ZM ROADMAP board. The hour doesn't matter for beta, the day does. "
             "Neither status column on the sheet decides anything. "
             "What Vincent counts as seen is in his QA note. The permission ask is Robert's call. "
             "The final headline is the latest line Leonard has called. A line that differs from what the client ships needs a string ticket, because the strings are hard-coded. "
             "Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise."),
    "qa": ("How I'm checking the phone messages for beta. Seen only counts on a store-signed build, on a real iOS device and a real Android device. "
           "A build with the debug timer doesn't count, it only proves the code path."),
    "ask_decision": ("Permission ask for beta: it stays after level 20 and nothing asks before that, I don't want to lose people earlier. Arthur is switching off the startup one."),
    "corr_reply": f"random one while I'm here: for the week-away ping drop the 'taken over' line and use \"{NEW_LINE}\". body stays.",
    "qa_reply": ("also the race reminder I passed on the ticket: the iPhone pass was the build with the debug timer. on the store build it never came through. Android is fine."),
    "arthur_inline": ("This counts seven days from the day they last left the game, so it isn't tied to the rollover. Fine to merge, but it isn't a reset message until it's anchored to the real reset."),
    "freeze": ("Until the beta build is out nothing new lands in anyone's Todo. Held work sits in Backlog, unassigned."),
    "copy_pass": ("Cancelled, not needed. The game name in the notification strings already went in with the rename."),
    "boss_ask": ("while someone's in here, can we get a phone reminder once Boss Arena attempts refill? Arthur says a local timer is enough."),
    "gift_ask": ("could we also send a phone reminder the evening before the daily gift resets? local timer per Arthur."),
    "brian_opinion": ("honestly just send all the Ready ones at beta and fix copy after"),
    "deck": ("Beta readiness. Player messages: 6 Ready on the PN sheet."),
    "parent": ("One ticket per player message for beta. Rows from the PNs Beta tab plus anything the team wants added. Anyone can add an ask here."),
    "card": ("Vincent ticks these as he checks them on the store builds."),
}


def write(path, obj):
    with open(path, "w") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)
        f.write("\n")


# ---------------------------------------------------------------- requirements
REQ = {
    "R1": "plan population: every row on the PNs Beta tab plus every ask for a new phone message filed on a ticket or a card by Sep 30 - 40 messages; in-game prompts, red dots and Domino-only tabs stay off",
    "R2": "a Call per message (Go, Hold, Drop) under the message rule: the feature in the beta, the client schedules it, the right day, it can reach its players, seen on both platforms",
    "R3": "What's missing for each Hold: the one thing the rule test fails on",
    "R4": "Final headline for each Go: the latest line Leonard has called, and a String change value that says whether the client ships a different line",
    "R5": "Fires as built for each Go, from what the client actually schedules",
    "R6": "the call as a comment on every message's ticket, reusing an existing ticket under whatever name, and a new ticket only for a message with none",
    "R7": "each ticket moved to match its call: Drop to Canceled, Hold parked as the roadmap's freeze says",
    "R8": "a string ticket for each line the client must change, and none for a line already right",
    "R9": "the plan sheet in Samuel's Drive folder, every Go on a checklist on the push notifications card, and the Go, Hold and Drop counts back to Leonard in his DM",
}

# ---------------------------------------------------------------- anchors and fragments
anchors = [
    {"id": "A1", "service": "slack", "record": IDS["hub"], "locator": IDS["hub"], "prompt_reference": "Leonard's DM from yesterday", "requirement_ids": ["R1", "R6", "R9"]},
    {"id": "A2", "service": "gsheets", "record": BASE["pn_sheet"], "locator": BASE["pn_sheet"], "prompt_reference": "the Zombie Match PN sheet", "requirement_ids": ["R1"]},
    {"id": "A3", "service": "gdrive", "record": BASE["folder"], "locator": BASE["folder"], "prompt_reference": "my Drive folder", "requirement_ids": ["R9"]},
]


def frag(fid, service, container, kind, via, seeded, by, quote, reqs, names=None, base=None):
    return {"id": fid, "service": service, "container": container, "locator": container, "kind": kind, "incorporated_via": via,
            "seeded_ids": seeded, "base_pointers": base or [], "delegated_by_record": by, "delegation_quote": quote,
            "requirement_ids": reqs, "names_authorities": names or []}


H = IDS
fragments = [
    frag("K1", "slack", H["hub"], "requirement", ["A1"], [H["hub"]], H["hub"],
         "every row on the PNs Beta tab plus every ask for a new phone message that's been filed on a ticket or a card up to today",
         ["R1", "R6", "R9"], [{"id": "H1", "quote": "the message rule doc"}]),
    frag("K2", "gdocs", H["rule_doc"], "delegation", ["A1", "K1"], [H["rule_doc"]], H["hub"], "using the message rule doc", ["R2", "R3", "R4", "R8"],
         [{"id": "H2", "quote": "his QA note"}, {"id": "H3", "quote": "unless the roadmap says otherwise"}]),
    frag("K3", "gsheets", BASE["pn_sheet"], "requirement", ["A2"], [], BASE["pn_sheet"], "the Zombie Match PN sheet", ["R1"], base=[BASE["pn_sheet"]]),
    frag("K4", "linear", PARENT, "delegation", ["A1", "K1"], [PARENT], H["hub"], f"I made a ticket per message under {PARENT}", ["R6", "R7"]),
    frag("K5", "gdrive", BASE["folder"], "destination", ["A1", "K1"], [], H["hub"], "Put it in one sheet in your Drive folder", ["R9"], base=[BASE["folder"]]),
    frag("K6", "trello", BASE["pn_card"], "destination", ["A1", "K1"], [], H["hub"], "Every Go goes on a checklist on our push notifications card", ["R9"], base=[BASE["pn_card"]]),
    frag("K7", "trello", BOARD, "requirement", ["A1", "K1", "K2"], [], H["rule_doc"], "on the BETA list of the ZM ROADMAP board", ["R2"], base=[BOARD]),
    frag("K8", "gmail", H["qa_thread"], "requirement", ["A1", "K1", "K2"], [H["qa_thread"]], H["rule_doc"], "What Vincent counts as seen is in his QA note", ["R2", "R3"]),
    frag("K9", "slack", H["ask_decision"], "requirement", ["A1", "K1", "K2"], [H["ask_decision"]], H["rule_doc"], "The permission ask is Robert's call", ["R2", "R3"]),
    frag("K10", "trello", BASE["tech_card"], "amendment", ["A1", "K1", "K2"], [H["freeze_comment"]], H["rule_doc"], "unless the roadmap says otherwise", ["R7"], base=[BASE["tech_card"]]),
    frag("K11", "slack", H["corr_reply"], "amendment", ["A1", "K1", "K2"], [H["corr_reply"]], H["rule_doc"], "the latest line Leonard has called", ["R4"]),
    frag("K12", "github", BASE["pr248"], "requirement", ["A1", "K1", "K2"], [H["arthur_inline"]], H["rule_doc"], "the client already schedules it", ["R5", "R8"], base=[BASE["pr248"]]),
    frag("K13", "linear", "ZOM-542", "requirement", ["A1", "K1"], [H["boss_ask"]], H["hub"], "filed on a ticket or a card up to today", ["R1"], base=["ZOM-542"]),
    frag("K14", "linear", "ZOM-556", "requirement", ["A1", "K1"], [H["gift_ask"]], H["hub"], "filed on a ticket or a card up to today", ["R1"], base=["ZOM-556"]),
    frag("K15", "confluence", BASE["liveops_page"], "requirement", ["A1", "K1"], [], H["hub"], "under whatever name", ["R6"], base=[BASE["liveops_page"]]),
    frag("K16", "gcal", H["copy_pass"], "requirement", ["A1", "K1", "K2"], [H["copy_pass"]], H["rule_doc"], "A line that differs from what the client ships needs a string ticket", ["R8"]),
]

authorities = [
    {"id": "H1", "name": "the message rule doc", "home_service": "gdocs", "decoy_service": "gdocs", "governs": ["R2", "R4"], "findable_query": "message rule",
     "seeded_ids": [H["rule_doc"]], "base_pointers": [], "decoy_seeded_ids": [], "decoy_base_pointers": [BASE["gtm_beta_doc"]],
     "decoy_scope": {"dimension": "game", "decoy": "Domino Delights beta launch plan, 2024", "task": "Zombie Match 3D beta player messages"}},
    {"id": "H2", "name": "Vincent's QA note", "home_service": "gmail", "decoy_service": "confluence", "governs": ["R3"], "findable_query": "checking the phone messages",
     "seeded_ids": [H["qa_thread"]], "base_pointers": [], "decoy_seeded_ids": [], "decoy_base_pointers": [BASE["release_page"]],
     "decoy_scope": {"dimension": "team", "decoy": "whole-build store submission checklist", "task": "phone message checks"}},
    {"id": "H3", "name": "the roadmap freeze", "home_service": "trello", "decoy_service": "trello", "governs": ["R7"], "findable_query": "Held work",
     "seeded_ids": [H["freeze_comment"]], "base_pointers": [BASE["tech_card"]], "decoy_seeded_ids": [], "decoy_base_pointers": [BASE["minor_bugs_card"]],
     "decoy_scope": {"dimension": "team", "decoy": "the Minor Bugs to Fix card, for bug tickets", "task": "held message tickets"}},
]

surfaces = [
    {"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1.0, "records": N_NOTES, "requirement": "R2", "seeded": True,
     "seeded_ids": [PARENT], "decides": "a Call per message",
     "why_no_bulk": "linear_list_issues returns descriptions but no comments; comments come one issue at a time",
     "short_circuit": "the build, QA and client-or-server notes live only in each ticket's comments, and no sheet column or list carries them, so a correct run cannot skip a ticket"},
    {"service": "slack", "tool": "slack_search_public_and_private", "per_record_calls": 0.6, "records": 40, "requirement": "R2", "decides": "a Call per message",
     "why_no_bulk": "no channel read covers DMs, threads and every project channel at once; a search is keyed to one feature name",
     "short_circuit": "a feature can be cut, moved or re-judged in chat after its ticket was written, so each feature needs its own look before its call stands"},
    {"service": "trello", "tool": "trello_get_cards_in_list", "per_record_calls": 0.25, "records": 40, "requirement": "R2", "decides": "a Call per message",
     "why_no_bulk": "cards_in_list returns one list; the feature-to-card match is a name join per message",
     "short_circuit": "whether a feature is in the beta depends on which list its card sits in, and the ticket does not say"},
    {"service": "github", "tool": "github_get_pull_request_comments + github_get_file_contents", "per_record_calls": 3.0, "records": 6, "requirement": "R5", "decides": "Fires as built",
     "why_no_bulk": "review comments come one PR at a time and the schedule is only in the client source; github_search_pull_requests carries neither",
     "short_circuit": "the six built messages are the only Go candidates, and when each really fires is not on the sheet or the ticket"},
]

chains = [
    {"id": "C1", "root_cause": "A24", "ends_in": "R3", "hops": [
        {"service": "gsheets", "record": BASE["pn_sheet"], "finding": "Weekly Leaderboard reset: Status Ready"},
        {"service": "linear", "record": TK["Weekly Leaderboard reset"], "finding": "ticket Done; Vincent saw it arrive on both"},
        {"service": "github", "record": H["arthur_inline"], "finding": "Arthur, Jun 26: counts seven days from the last leave, not tied to the rollover"},
        {"service": "github", "record": BASE["pr248"], "finding": "the merged schedule still adds i * 7 days to today"}]},
    {"id": "C2", "root_cause": "A11", "ends_in": "R4", "hops": [
        {"service": "gsheets", "record": BASE["pn_sheet"], "finding": "Lapsed 7 days headline from June"},
        {"service": "linear", "record": TK["Lapsed 7 days"], "finding": "ticket repeats the June line and carries the week-away name"},
        {"service": "slack", "record": H["corr_reply"], "finding": f"Leonard's later thread reply replaces the line with {NEW_LINE}"}]},
    {"id": "C3", "root_cause": "A4", "ends_in": "R3", "hops": [
        {"service": "gsheets", "record": BASE["pn_sheet"], "finding": "first-session message: level 20 not completed, 12 hours"},
        {"service": "slack", "record": BASE["shove_to_20"], "finding": "Robert, Jul 10: shove the ask to level 20"},
        {"service": "slack", "record": H["ask_decision"], "finding": "Robert, Sep 29: nothing asks before level 20 at beta"},
        {"service": "github", "record": BASE["pr292"], "finding": "permission asked only after that progress"}]},
    {"id": "C4", "root_cause": "A14", "ends_in": "R3", "hops": [
        {"service": "linear", "record": H["race_qa"], "finding": "Vincent, Sep 24: seen on both"},
        {"service": "gmail", "record": H["qa_thread"], "finding": "a debug-timer build does not count"},
        {"service": "slack", "record": H["qa_reply"], "finding": "Vincent, Sep 29: the iPhone pass was the debug-timer build"}]},
    {"id": "C5", "root_cause": "A7", "ends_in": "R6", "hops": [
        {"service": "gsheets", "record": BASE["pn_sheet"], "finding": "row says Win & Collect event start"},
        {"service": "confluence", "record": BASE["liveops_page"], "finding": "Collect & Win is the same feature under a different name"},
        {"service": "linear", "record": TK["Win & Collect start"], "finding": "an existing ticket outside the parent carries the work"}]},
    {"id": "C6", "root_cause": "A17", "ends_in": "R1", "hops": [
        {"service": "slack", "record": H["hub"], "finding": "asks filed on any ticket or card count"},
        {"service": "linear", "record": "ZOM-542", "finding": "a home-screen ticket, not a notification ticket"},
        {"service": "linear", "record": H["boss_ask"], "finding": "Brian's ask for an attempts reminder sits in a comment"}]},
    {"id": "C7", "root_cause": "A25", "ends_in": "R8", "hops": [
        {"service": "gsheets", "record": BASE["pn_sheet"], "finding": "the 1-day body still says Puzzles vs Zombies"},
        {"service": "gcal", "record": H["copy_pass"], "finding": "cancelled copy pass: the name already went in with the rename"},
        {"service": "github", "record": BASE["pr248"], "finding": "the client strings already say Zombie Match 3D"}]},
    {"id": "C8", "root_cause": "A15", "ends_in": "R7", "hops": [
        {"service": "gdocs", "record": H["rule_doc"], "finding": "Hold tickets go back to Todo unless the roadmap says otherwise"},
        {"service": "trello", "record": BASE["tech_card"], "finding": "the tech issues card on the BETA list"},
        {"service": "trello", "record": H["freeze_comment"], "finding": "Leonard, Sep 29: held work sits in Backlog, unassigned"}]},
]


def trap(tid, family, services_, seeded, base, req, wrong, resolver, order=None, versions=None, dtype=None):
    t = {"id": tid, "family": family, "services": services_, "seeded_ids": seeded, "base_pointers": base, "requirement": req,
         "expected_wrong_reading": wrong, "resolver": resolver}
    if order:
        t["discovery_order"] = order
    if versions:
        t["version_records"] = versions
    if dtype:
        t["distractor_type"] = dtype
    return t


def v(service, rid, at, seeded=True, container=None, base=False):
    r = {"service": service, "seeded": seeded, "at": at}
    r["base_pointer" if base else "id"] = rid
    if container:
        r["container"] = container
    return r


zart_root = BASE["martin_root"].split("/")[1]
dmv_root = BASE["android_2007_root"].split("/")[1]
traps = [
    trap("T1", "done_gap", ["gsheets", "linear", "github"], [H["arthur_inline"], H["weekly_qa"]], [BASE["pn_sheet"], BASE["pr248"]], "R3",
         "the weekly leaderboard message is finished: the sheet says Ready, its ticket is Done, Vincent saw it arrive and PR #248 merged approved",
         "Arthur's inline comment on PR #248 and the schedule in the client: it counts seven days from the last leave, so it is not on the rollover day: Hold, fires on the wrong day",
         "the sheet, the ticket and the approval come back first; the comment needs github_get_pull_request_comments or the source file"),
    trap("T2", "superseding", ["gsheets", "linear", "slack"], [H["corr_reply"], TK["Lapsed 7 days"]], [BASE["pn_sheet"], BASE["martin_root"]], "R4",
         "the June line on the sheet and the ticket is the final headline",
         f"Leonard's Sep 29 thread reply under Martin's Endless theme post replaces it with {NEW_LINE}; the client still ships the old line, so a string ticket follows",
         "the sheet and ticket are read first; the reply needs the thread open or a search for the ticket's week-away name",
         [v("gsheets", BASE["pn_sheet"], "2025-06-23T07:02:43Z", False, "file:" + BASE["pn_sheet"], True),
          v("linear", TK["Lapsed 7 days"], T["parent"], True, "linear:" + TK["Lapsed 7 days"]),
          v("slack", H["corr_reply"], T["corr_reply"], True, f"slack:{ZART}/{zart_root}")]),
    trap("T3", "cross_reference_gap", ["gsheets", "slack", "github"], [H["ask_decision"], H["ftue_qa"]], [BASE["pn_sheet"], BASE["shove_to_20"], BASE["pr292"]], "R3",
         "the first-session message is Ready and LIVE with a level 20 trigger, Vincent saw it arrive, so it goes",
         "its trigger selects players below level 20, and the only ask is after level 20: nobody it is written for has been asked: Hold, cannot reach its players",
         "each record is plain on its own; only the join shows it"),
    trap("T4", "superseding", ["linear", "gmail", "slack"], [H["race_qa"], H["qa_thread"], H["qa_reply"]], [BASE["android_2007_root"]], "R3",
         "Vincent passed the race reminder on both platforms on its ticket",
         "Vincent's later thread reply in his DM with Samuel: the iPhone pass was the debug-timer build, which his QA note says does not count: Hold, not seen on both platforms",
         "the ticket comment is read per ticket; the reply sits in a DM thread under a build request and names the race reminder, not Plague Race",
         [v("linear", H["race_qa"], "2025-09-24T14:30:00Z", True, "linear:" + TK["Plague Race"]),
          v("slack", H["qa_reply"], T["qa_reply"], True, f"slack:{DM_VINCENT}/{dmv_root}")]),
    trap("T5", "scope_alias", ["gsheets", "confluence", "linear"], [TK["Win & Collect start"]], [BASE["pn_sheet"], BASE["liveops_page"]], "R6",
         "the Win & Collect row has no ticket under the parent, so it needs a new one",
         f"the live-ops page says Collect & Win is the same feature under another name, and {TK['Win & Collect start']} already carries it: reuse it",
         "the parent's children and a Win & Collect search both miss it; the ticket predates the parent"),
    trap("T6", "exact_predicate", ["linear", "gsheets"], [H["boss_ask"], H["gift_ask"]], ["ZOM-542", "ZOM-556", BASE["pn_sheet"]], "R1",
         "the sheet rows and the parent's children are the whole list",
         "Leonard's scope takes in asks on any ticket or card: Brian's on ZOM-542 and Julia's on ZOM-556 are comments on tickets about other things",
         "neither ticket title mentions a phone message, so a notification search and the children listing both miss them"),
    trap("T7", "completion_elsewhere", ["gsheets", "gcal", "github"], [H["copy_pass"]], [BASE["pn_sheet"], BASE["pr248"]], "R8",
         "the 1-day body still says Puzzles vs Zombies, so it needs a string ticket",
         "the client strings already say Zombie Match 3D (a cancelled copy pass says so and the source confirms it): no string ticket for it",
         "the sheet is read first and looks stale; the source file or the cancelled invite settles it"),
    trap("T8", "superseding", ["gdocs", "trello"], [H["rule_doc"], H["freeze_comment"]], [BASE["tech_card"]], "R7",
         "the rule doc says Hold tickets go back to Todo",
         "Leonard's later comment on the tech issues card: held work sits in Backlog, unassigned",
         "the doc is read first; the comment is on a card read only for its list position",
         [v("gdocs", H["rule_doc"], T["rule_doc"], True, "file:" + H["rule_doc"]),
          v("trello", H["freeze_comment"], T["freeze"], True, "trello:" + BASE["tech_card"])]),
    trap("T9", "superseding", ["slack"], [H["ask_decision"]], [BASE["shove_to_20"], BASE["variant_c_13"]], "R3",
         "the permission ask is at level 13 on variant C or at the start of the game",
         "Robert's Sep 29 post settles it for beta: after level 20, nothing before it",
         "older DM and bug-channel records come back first",
         [v("slack", BASE["shove_to_20"], "2025-07-10T15:52:18Z", False, f"slack:{DM_ROBERT}/1752162738.497679", True),
          v("slack", BASE["variant_c_13"], "2025-08-13T11:24:39Z", False, f"slack:{ZBUGS}/1755084066.905699", True),
          v("slack", H["ask_decision"], T["ask_decision"], True, f"slack:{ZM3D}/" + H["ask_decision"].split("/")[1])]),
    trap("T10", "distractor", ["gslides"], [H["deck"]], [], "R2", "the beta readiness deck says six messages are Ready, so six go",
         "the deck repeats the June sheet flags; the rule says neither flag decides", dtype="stale_summary"),
    trap("T11", "distractor", ["gsheets"], [], [BASE["pn_sheet"]], "R1", "the PN BETA Translated tab and the older PNs tab are part of the list",
         "both hold Domino copy; Leonard's scope is the PNs Beta tab", dtype="near_duplicate_record"),
    trap("T12", "distractor", ["slack"], [H["brian_opinion"]], [], "R2", "Brian's 'send all the Ready ones' settles the calls",
         "Brian does not own the rule; the rule doc decides", dtype="non_authoritative_instruction"),
    trap("T13", "distractor", ["linear"], [], ["ENG-2311"], "R2", "ENG-2311 is Done, so event start messages are built",
         "that ticket is Domino Delights; the Zombie Match client schedules six messages", dtype="other_title"),
    trap("T14", "distractor", ["linear"], [], ["ZOM-471", "ZOM-539"], "R1", "red-dot tickets are asks for notifications",
         "a red dot is in the game; the rule covers what reaches a closed phone", dtype="keyword_collision"),
    trap("T15", "distractor", ["trello", "linear"], [], ["6874409dfe0decf6f8fca64f", "ZOM-397"], "R1", "Rate Us and the permission popup are messages on the plan",
         "both show inside the game; the rule covers a closed game", dtype="scope_adjacent"),
]

mechs = [
    ("DONE", "A24", "done_gap", "v2 trap 1: Ready, Done and an approved merge against a review comment and the schedule in the source", ["T1", "C1"], "R3",
     "Weekly Leaderboard reset Go: Ready, Done, seen on both", ["X1", "X2", "X2b"], ["Lives recharged (right day: Go)", "Lapsed 7 days (seven days is the right day: Go)"],
     "over-application holds Lapsed 1 day for not being exactly 24 hours", "pr-inline", "Arthur inline rollover", 0.55),
    ("CORR", "A11", "superseding", "v2 trap 2: a line on a sheet and ticket replaced by a thread reply under another topic in another service", ["T2", "C2"], "R4",
     "Lapsed 7 days keeps the June line", ["X3", "X4", "X16"], ["Lives recharged (line unchanged)", "Lapsed 1 day (line unchanged)"],
     "over-application rewrites another lapsed headline", "channel-thread", "week-away ping new line", 0.55),
    ("DEP", "A4", "authority", "v2 trap 4 (no ledger family for dependencies): closest is a stated rule applied through a join; here the permission ask gates the trigger", ["T3", "C3"], "R3",
     "Finish first mission Go: Ready, LIVE, seen on both", ["X5", "X6", "X6b"], ["Lapsed 1 day (players past the ask: Go)"],
     "over-application holds every message for players who declined", "join", "level 20 ask vs level 20 trigger", 0.30),
    ("QA", "A14", "superseding", "v2 trap 2 on a status: Vincent's own later DM thread reply withdraws his ticket comment", ["T4", "C4"], "R3",
     "Plague Race Go: Vincent passed it on the ticket", ["X7", "X8", "X8b"], ["Lives recharged (store builds on both: Go)"],
     "over-application doubts every QA comment", "dm-thread", "race reminder debug timer", 0.60),
    ("ALIAS", "A7", "scope_alias", "v2 trap 6: an existing ticket under another name; the page maps the two names", ["T5", "C5"], "R6",
     "a new ticket for the Win & Collect row", ["X9", "X10"], ["Login Calendar update (ticket under its own name)"],
     "over-application merges Season Pass start into Season Pass last 48 hours", "linear-name", "Collect and Win ping", 0.40),
    ("FILT", "A17", "exact_predicate", "v2 trap 7: in-scope asks outside the sheet and the parent, in comments on tickets about other things", ["T6", "C6"], "R1",
     "the plan stops at the sheet rows and the parent's children", ["X11", "X12", "X13"], ["ZOM-471 red dot (in the game: off the plan)"],
     "over-application adds red dots and in-game prompts", "linear-offlist", "phone reminder comment", 0.50),
    ("BUILT", "A25", "completion_elsewhere", "v2 trap 9: a line looks stale on the sheet but the work is already in the client", ["T7", "C7"], "R8",
     "Lapsed 1 day needs a string change for the old game name", ["X14", "X15", "X17"], ["Lapsed 7 days (a real string change)"],
     "over-application clears the real string change", "code-read", "NotificationManager strings", 0.50),
    ("FOLLOW", "A15", "superseding", "v2 trap 3: a follow-through rule amended on a card the prompt never names", ["T8", "C8"], "R7",
     "Hold tickets go back to Todo", ["X18", "X19", "X19b"], ["Axe Arena (Drop: Canceled either way)"],
     "over-application parks Drop tickets too", "trello-comment", "held work Backlog", 0.45),
]
portfolio, channels, RATES = [], [], {}
for mid, mech, fam, why, nodes, req, nat, dec, ctrl, over, src, sig, rate in mechs:
    portfolio.append({"id": mid, "mechanism": mech, "prior_family": fam, "prior_family_reason": why, "nodes": nodes, "requirement": req,
                      "natural_reading": nat, "decides": dec, "controls": ctrl, "over_application": over, "source": src, "signature": sig})
    RATES[mid] = rate
    who = {"DONE": ["Weekly Leaderboard reset"], "CORR": ["Lapsed 7 days"], "DEP": ["Finish first mission"], "QA": ["Plague Race"], "ALIAS": ["Win & Collect start"],
           "FILT": ["Boss Arena attempts refilled", "Daily gift about to reset"], "BUILT": ["Lapsed 1 day"], "FOLLOW": ["Quests rollover", "Login Calendar update"]}[mid]
    channels.append({"id": "CH-" + mid, "kind": "member", "rule": mid, "degrade": nat, "members": who, "latent": src, "family": fam})
channels.append({"id": "CH-SLIP", "kind": "slip", "degrade": "base slip on control rows", "slots": ["K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9"]})

budget = [
    ("discovery", "slack", 4, "read the hub; read the DM history around it; find the PN thread in #zombie-bugs"),
    ("discovery", "gdocs", 2, "read the rule doc; reject the 2024 GTM - Beta doc on scope"),
    ("discovery", "gsheets", 4, "list the tabs; read PNs Beta; read the older PNs tab; read PN BETA Translated to rule it out"),
    ("discovery", "trello", 5, "board lists; BETA, Oct 21 and Backlog lists for beta scope; the push notifications card"),
    ("discovery", "confluence", 3, "live-ops page for feature state and names; GDD; release checklist"),
    ("discovery", "gslides", 1, "read the beta readiness deck the search returns and reject it"),
    ("discovery", "gdrive", 2, "confirm the folder; find the rule doc"),
    ("discovery", "gcal", 2, "list the window for copy and QA sessions"),
    ("discovery", "gmail", 3, "find Vincent's QA note; open it; search for message mail"),
    ("discovery", "linear", 4, "read the parent; its comments; page its children; search for notification asks"),
    ("per-record", "linear", N_NOTES, "one linear_list_comments per message ticket: build, QA and client-or-server notes exist nowhere else"),
    ("per-record", "slack", 24, "a search per feature family (the stored Frederick run made 39 for 36 members): a feature can be cut or re-judged in chat after its ticket was written"),
    ("per-record", "trello", 10, "a card check per feature: which list it sits on decides In the beta"),
    ("per-record", "github", 18, "PR reviews, inline comments and source for the six built messages"),
    ("per-record", "linear", N_NOTES, "one linear_create_comment per ticket: the call lands on each ticket, no batch form exists"),
    ("per-record", "linear", N_UPDATES, "one linear_update_issue per Hold and Drop ticket: the state follows the call, no batch form exists"),
    ("per-record", "linear", N_NEW, "new tickets for the two off-parent asks and the one string change"),
    ("per-record", "trello", 1 + COUNTS["Go"], "the checklist and one trello_create_check_item per Go message"),
    ("writes", "gsheets", 3, "create the plan sheet; write the rows; check it"),
    ("writes", "gdrive", 1, "move the sheet into the folder"),
    ("writes", "slack", 1, "report the counts to Leonard"),
    ("readback", "gsheets", 1, "read the plan back"),
    ("readback", "linear", 2, "spot-check ticket states"),
    ("readback", "trello", 1, "read the checklist back"),
]
TOTAL_BUDGET = sum(c for _, _, c, _ in budget)
PER_RECORD = round(sum(s["per_record_calls"] * s["records"] for s in surfaces))

writes = [
    {"service": "gsheets", "tool": "gsheets_create_spreadsheet+gsheets_values_update", "count": 3, "depends_on": ["K1", "K2", "C1", "C2", "C3", "C4", "C5", "C6", "C7"], "requirements": ["R1", "R2", "R3", "R4", "R5", "R9"]},
    {"service": "gdrive", "tool": "gdrive_move_file", "count": 1, "depends_on": ["K5"], "requirements": ["R9"]},
    {"service": "linear", "tool": "linear_create_comment", "count": N_NOTES, "depends_on": ["K4", "C1", "C3", "C4", "C5"], "requirements": ["R6"]},
    {"service": "linear", "tool": "linear_update_issue", "count": N_UPDATES, "depends_on": ["K4", "K10", "C8"], "requirements": ["R7"]},
    {"service": "linear", "tool": "linear_create_issue", "count": N_NEW, "depends_on": ["K13", "K14", "C2", "C6", "C7"], "requirements": ["R6", "R8"]},
    {"service": "trello", "tool": "trello_create_checklist+trello_create_check_item", "count": 1 + COUNTS["Go"], "depends_on": ["K6", "C1", "C3", "C4"], "requirements": ["R9"]},
    {"service": "slack", "tool": "slack_send_message", "count": 1, "depends_on": ["K1"], "requirements": ["R9"]},
]

services = {
    "slack": {"role": "hub DM; Robert's ask decision; Leonard's line change; Vincent's DM reply; feature talk", "weight_reason": "the ask, the ask point, the final line and the withdrawn QA pass live here"},
    "gsheets": {"role": "the PN sheet (population, June flags and copy); the plan sheet", "weight_reason": "the population and the deliverable"},
    "gdocs": {"role": "the message rule doc", "weight_reason": "the Go, Hold and Drop tests"},
    "gdrive": {"role": "Samuel's folder, owner of the plan", "weight_reason": "the destination the plan must land in"},
    "linear": {"role": "one ticket per message, its notes and comments, off-parent asks, new tickets", "weight_reason": "per-message build, QA and client-or-server facts, and the ticket writes"},
    "trello": {"role": "ZM ROADMAP lists for beta scope, the push notifications card, the freeze comment", "weight_reason": "In the beta, the Go checklist and the Hold parking rule"},
    "github": {"role": "match3d#248, Arthur's inline comment, the client source", "weight_reason": "what the client schedules and when"},
    "gmail": {"role": "Vincent's QA note; the GitHub mail for Arthur's comment", "weight_reason": "what counts as seen"},
    "gcal": {"role": "the cancelled copy pass", "weight_reason": "the completion note that clears the old-name string"},
    "gslides": {"role": "beta readiness deck, a stale summary", "weight_reason": "the convincing wrong count of six"},
    "confluence": {"role": "live-ops page and release checklist, base only", "weight_reason": "the Collect & Win name map and feature state"},
}

hazards = [
    {"hazard_id": "Q01", "resolution": "dated_claim", "requirement": "R4", "why_safe": "Leonard's seeded reply under Martin's Sep 29 root changes that root's reply counters; the SQL updates them as companions and the text is an attributed, dated claim"},
    {"hazard_id": "Q01", "resolution": "dated_claim", "requirement": "R3", "why_safe": "Vincent's seeded DM reply under Samuel's Sep 29 root changes that root's counters; updated as companions"},
]

manifest = {
    "_note": "draft manifest (/create-scenario); /create-injection writes 01_Hardness_Manifest.json keeping every id or listing it in design_delta. Seeded texts quoted in delegation_quote are the planned wording.",
    "persona": "samuel_turner",
    "assignment_context": {k: CTX[k] for k in ("context_hash", "assignment_hash", "policy_hash", "freeze_utc", "difficulty_mode")},
    "horizon": "Long Horizon", "effective_profile": "extreme",
    "author_targets": {"min_calls_per_run": 130, "max_avg_weighted_pass": 0.8,
                       "requester_confirmation": "task author in chat on 2026-11-04: 'my task is a long horizon task soo i want over 130 tool calls in each runs and also i want difficulty pass rate under 80% and also have to folllow all other difficulty guidelines soo you can choose from your self which option is best fit for my requirements in this task'"},
    "volume_exception": {"reason": "40 real messages; mail, channels and sheets are bulk-readable, so honest necessary calls are about 240 and a lean correct run about 150; reaching 500 would need padding, which fails on its own",
                         "requester_confirmation": "task author in chat on 2026-11-04 set the horizon target at 'over 130 tool calls in each runs' and delegated the choice ('you can choose from your self which option is best fit for my requirements in this task'), after the pre-scenario analysis proposed this exception",
                         "call_budget_floor": 200, "per_record_floor": 90},
    "requirements": REQ, "services": services, "anchors": anchors, "ask_fragments": fragments, "authorities": authorities,
    "cohort": {"definition": "every row on the PNs Beta tab plus every ask for a new phone message filed on a ticket or a card by Sep 30: 40 messages",
               "definition_source": [H["hub"], BASE["pn_sheet"], PARENT], "key": "message", "size": len(M), "evidence_surfaces": surfaces},
    "chains": chains, "traps": traps, "mechanism_portfolio": portfolio, "channels": channels,
    "call_budget": [{"phase": p, "service": s, "calls": c, "reason": r} for p, s, c, r in budget],
    "writes": writes, "hazard_acknowledgements": hazards, "denied_probes": [], "gradable_surface": "01_Gradable_Surface.json",
}
write(os.path.join(WF, "01_Hardness_Manifest.draft.json"), manifest)

# ---------------------------------------------------------------- gradable surface
MS, LR, LK, CA = "multi_source_reconciliation", "limited_reconciliation", "lookup", "calculation"
W, F, R, L7 = TK["Weekly Leaderboard reset"], TK["Finish first mission"], TK["Plague Race"], TK["Lapsed 7 days"]
HELD1, HELD2, HELD3, DROP1 = TK["Quests rollover"], TK["Login Calendar update"], TK["Boss Arena open"], TK["Axe Arena"]


def slot(sid, title, weight, kind, reason, cls, selector, role="core", group=None, mechs_=(), fact=None, **kw):
    s = {"id": sid, "title": title, "weight": weight, "work_kind": kind, "work_reason": reason, "class": cls, "selector": selector, "role": role, "mechanisms": list(mechs_)}
    if group:
        s["group"] = group
    if fact:
        s["fact_id"] = fact
    s.update(kw)
    return s


slots = [
    slot("X1", "Weekly Leaderboard reset call", 5, MS, "sheet, ticket and approved PR against Arthur's inline comment and the source", "direct", ["field", "Weekly Leaderboard reset", "Call"], "sample", "call_hold", ["DONE"]),
    slot("X2", "Weekly Leaderboard reset what's missing", 5, MS, "the gap is only in the inline comment and the source", "write_content", ["reason_matches", "Weekly Leaderboard reset", r".*([Ww]rong day|[Rr]ollover|[Rr]eset day|not tied|[Ss]even days from|last left).*"], "sample", "missing", ["DONE"], fact="weekly_gap"),
    slot("X2b", "Weekly Leaderboard reset note on its ticket", 5, MS, "the ticket says Done; the note must carry the gap from GitHub", "write_content", ["text", "comments", rf".*{W}.*([Ww]rong day|[Rr]ollover|[Rr]eset day|not tied).*"], mechs_=["DONE"], fact="weekly_gap"),
    slot("X3", "Lapsed 7 days final headline", 5, MS, "sheet and ticket against Leonard's thread reply under another topic", "direct", ["field", "Lapsed 7 days", "Final headline"], "sample", "headline", ["CORR"], fact="line7"),
    slot("X4", "Lapsed 7 days string ticket carries the line", 5, MS, "the line reaches Linear only through the Slack reply", "write_content", ["text", "tickets", rf".*{NEW_LINE}.*"], mechs_=["CORR"], fact="line7"),
    slot("X5", "Finish first mission call", 5, MS, "the trigger on the sheet joined to the ask point across DMs, a post and a PR", "direct", ["field", "Finish first mission", "Call"], "sample", "call_hold", ["DEP"]),
    slot("X6", "Finish first mission what's missing", 5, MS, "the join names the gap", "write_content", ["reason_matches", "Finish first mission", r".*([Pp]ermission|[Aa]sk|[Rr]each|level 20).*"], "sample", "missing", ["DEP"], fact="ftue_gap"),
    slot("X6b", "Finish first mission note on its ticket", 5, MS, "the ticket says Done; the note must carry the join", "write_content", ["text", "comments", rf".*{F}.*([Pp]ermission|[Aa]sk|[Rr]each|level 20).*"], mechs_=["DEP"], fact="ftue_gap"),
    slot("X7", "Plague Race call", 5, MS, "ticket pass against the QA note and Vincent's DM thread reply", "direct", ["field", "Plague Race", "Call"], "sample", "call_hold", ["QA"]),
    slot("X8", "Plague Race what's missing", 5, MS, "the withdrawn platform is only in the DM reply", "write_content", ["reason_matches", "Plague Race", r".*(i[Pp]hone|iOS|store build|both platforms).*"], "sample", "missing", ["QA"], fact="race_gap"),
    slot("X8b", "Plague Race note on its ticket", 5, MS, "the ticket says Done; the note must carry the DM reply", "write_content", ["text", "comments", rf".*{R}.*(i[Pp]hone|iOS|store build).*"], mechs_=["QA"], fact="race_gap"),
    slot("X9", "Win & Collect row points at the existing ticket", 5, MS, "row name joined to a ticket under another name through the live-ops page", "direct", ["field", "Win & Collect start", "Ticket"], "exception", mechs_=["ALIAS"], singled_out_by="K15"),
    slot("X10", "the call lands on the existing Collect & Win ticket", 5, MS, "the ticket is outside the parent and outside the sheet's name", "write_content", ["text", "comments", rf".*{TK['Win & Collect start']}.*"], mechs_=["ALIAS"]),
    slot("X11", "Boss Arena attempts refilled on the plan", 5, MS, "an ask in a comment on a home-screen ticket, under Leonard's scope", "direct", ["field", "Boss Arena attempts refilled", "Call"], "exception", mechs_=["FILT"], singled_out_by="K13"),
    slot("X12", "Daily gift about to reset on the plan", 5, MS, "an ask in a comment on a daily-gift bug, under Leonard's scope", "direct", ["field", "Daily gift about to reset", "Call"], "exception", mechs_=["FILT"], singled_out_by="K14"),
    slot("X13", "a new ticket for the Boss Arena ask", 3, LR, "no ticket exists for it", "write_content", ["text", "tickets", r".*[Bb]oss.*"], mechs_=["FILT"]),
    slot("X14", "Lapsed 1 day fires as built", 5, "cross_modal", "the sheet says 24 hours; the source schedules the next server day", "direct", ["field", "Lapsed 1 day", "Fires as built"], "sample", "fires", ["BUILT"]),
    slot("X15", "Lapsed 1 day string change", 5, "cross_modal", "sheet copy against the client strings", "direct", ["field", "Lapsed 1 day", "String change"], "sample", "string", ["BUILT"]),
    slot("X16", "Lapsed 7 days string change", 5, MS, "the client ships the June line; only Leonard's reply shows it must change", "direct", ["field", "Lapsed 7 days", "String change"], "sample", "string", ["CORR"]),
    slot("X17", "Lapsed 7 days fires as built", 5, "cross_modal", "a four-week batch in the source; the sheet says only 7 days lapsed", "direct", ["field", "Lapsed 7 days", "Fires as built"], "sample", "fires", ["BUILT"]),
    slot("X18", "a held ticket parked in Backlog", 5, MS, "rule doc amended on a card the prompt never names, applied to a Linear ticket", "write_content", ["text", "updates", rf".*{HELD1}.*[Bb]acklog.*"], "sample", "state", ["FOLLOW"]),
    slot("X19", "a second held ticket parked in Backlog", 5, MS, "same amendment on another ticket", "write_content", ["text", "updates", rf".*{HELD2}.*[Bb]acklog.*"], "sample", "state", ["FOLLOW"]),
    slot("X19b", "a held ask's ticket parked in Backlog", 5, MS, "same amendment on an ask's ticket", "write_content", ["text", "updates", rf".*{HELD3}.*[Bb]acklog.*"], "sample", "state", ["FOLLOW"]),
    slot("T1", "Go count back to Leonard", 5, MS, "the count follows every call across services", "aggregate", ["text", "dm", r".*(Go: 3|3 Go|Go 3).*"], mechs_=["DONE", "DEP", "QA"]),
    slot("T3", "Drop count back to Leonard", 3, CA, "count over the Drop rows", "aggregate", ["text", "dm", r".*(Drop: 12|12 Drop|Drop 12).*"]),
    slot("K1", "Lives recharged call", 3, LR, "ticket QA note and the source agree", "direct", ["field", "Lives recharged", "Call"], "sample", "call_go"),
    slot("K2", "Lapsed 1 day call", 3, LR, "the day is right and it reaches players past the ask", "direct", ["field", "Lapsed 1 day", "Call"], "sample", "call_go"),
    slot("K3", "Axe Arena call", 3, LR, "sheet row against the Sep 22 post and the Oct 21 list", "direct", ["field", "Axe Arena", "Call"], "sample", "call_drop"),
    slot("K4", "Streak Fever call", 3, LR, "a Domino event with no Zombie Match card", "direct", ["field", "Streak Fever", "Call"], "sample", "call_drop"),
    slot("K5", "Hourly Coins call", 3, LR, "sheet row against the Backlog card", "direct", ["field", "Hourly Coins", "Call"], "sample", "call_drop"),
    slot("K6", "Login Calendar update call", 3, LR, "feature live, nothing scheduled", "direct", ["field", "Login Calendar update", "Call"], "sample", "call_hold"),
    slot("K7", "Season Pass start call", 3, LR, "feature in the beta, nothing scheduled", "direct", ["field", "Season Pass start", "Call"], "sample", "call_hold"),
    slot("K8", "Quests rollover what's missing", 3, LR, "Arthur's note on the ticket", "write_content", ["reason_matches", "Quests rollover", r".*([Ss]chedul|[Cc]lient|[Ll]ocal).*"], "sample", "missing"),
    slot("K9", "Plague Race result what's missing", 3, LR, "Arthur's note on the ticket", "write_content", ["reason_matches", "Plague Race result", r".*([Ss]erver).*"], "sample", "missing"),
    slot("K10", "Lives recharged final headline", 1, LK, "unchanged from the sheet", "direct", ["field", "Lives recharged", "Final headline"], "sample", "headline"),
    slot("K11", "Lives recharged on the card's checklist", 3, LR, "a Go lands on the card", "write_content", ["text", "checks", r".*[Ll]ives.*"]),
    slot("K12", "a Drop ticket canceled", 3, LR, "the call decides the state", "write_content", ["text", "updates", rf".*{DROP1}.*[Cc]ancel.*"], "sample", "state"),
    slot("K13", "the call on an ordinary ticket", 1, LK, "one comment per ticket", "write_content", ["text", "comments", rf".*{TK['Hourly Coins']}.*"]),
    slot("V1", "every message on the plan, and no others", 3, LR, "the volume row for the population", "delivery", ["delivery", "register_keys_exact"], "volume", mechs_=["FILT"], volume_for=["call_go", "call_hold", "call_drop", "missing", "headline", "fires", "string", "state"]),
    slot("D1", "plan in Samuel's folder", 1, LK, "folder named in the prompt", "delivery", ["delivery", "register_parent", BASE["folder"]]),
    slot("D2", "counts back to Leonard", 1, LK, "reply in the DM", "delivery", ["delivery", "slack_channel_post", DM_LEONARD, r".*Go.*"]),
]
surface = {
    "kind": "GRADABLE_SURFACE", "version": 1, "task": "samuel_zm_beta_messages", "revision": "design-1",
    "truth_keys": [m["key"] for m in M], "classes": ["Go", "Hold", "Drop"],
    "truth_fields": {"class": "Call", "groups": "groups"},
    "deliverables": {
        "plan": {"kind": "table", "name_regex": r"(?i).*(beta|message|pn|player).*", "key_column": "Message", "key_regex": ".+",
                 "columns": ["Message", "Ticket", "Call", "What's missing", "Fires as built", "Final headline", "String change"],
                 "class_column": "Call", "reason_column": "What's missing",
                 "comparators": {"Call": "norm", "Ticket": "issue_key", "String change": "yes_no", "Final headline": "norm", "Fires as built": "norm"}},
        "comments": {"kind": "json_text", "tool": "linear_create_comment"},
        "updates": {"kind": "json_text", "tool": "linear_update_issue"},
        "tickets": {"kind": "json_text", "tool": "linear_create_issue"},
        "checks": {"kind": "json_text", "tool": "trello_create_check_item"},
        "dm": {"kind": "json_text", "tool": "slack_send_message"},
    },
    "slots": slots,
}
write(os.path.join(WF, "01_Gradable_Surface.json"), surface)
write(os.path.join(HERE, "ids.json"), {"ids": IDS, "base": BASE, "times": T, "quotes": Q, "counts": COUNTS, "tickets": TK, "parent": PARENT, "last_ticket": LAST_TICKET,
                                       "rates": RATES, "budget_total": TOTAL_BUDGET, "per_record_total": PER_RECORD, "members": M, "new_line": NEW_LINE})
if __name__ == "__main__":
    print("members", len(M), COUNTS, "tickets", len(TICKETED), "notes", N_NOTES, "updates", N_UPDATES, "new", N_NEW, "parent", PARENT, "last", LAST_TICKET)
    print("budget", TOTAL_BUDGET, "per-record", PER_RECORD, "slots", len(slots), "weight", sum(s["weight"] for s in slots), "flippable", sum(s["weight"] for s in slots if s["mechanisms"]))
