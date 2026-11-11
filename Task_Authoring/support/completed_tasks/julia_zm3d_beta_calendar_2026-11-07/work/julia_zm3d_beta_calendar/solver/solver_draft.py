"""julia-zm3d-beta-liveops-calendar solver - DRAFT SCAFFOLDING (the build session fills `solve()`).

Truth owner for Julia Lawson's ZM3D beta live-ops + push calendar (Product / Marketing and GTM / Planning and
decision support, Long Horizon): one row per beat of the four buy weeks (Mon Oct 6 - Sun Nov 2, 2025) with its first
window, its weeks running, its Status (Run/Hold) and what is still to do before it runs (owner, due), plus one row per
beta push with Send-or-hold and what is missing. Parses the injection SQL as data through tools/base_check.parse_sql;
never executes SQL.

WHAT THIS FILE IS
  The scaffolding only. `RULES` mirrors the manifest's fourteen mechanism-portfolio entries verbatim (ids,
  mechanism, requirement, nodes, natural_reading, controls, over_application, source, signature, decides). The
  judgment - which window opens first, which beat is held, what is still to do, which push is sendable - is NOT
  written here: every value is a `TODO_<key>_<field>` placeholder and `solve()` carries a per-key/per-field comment
  block naming the seeded records and the rules that decide it. The build session replaces the placeholders with the
  rule logic and keeps the wiring (RULES, DEGRADES, CHANNELS, load_state, keys, aggregates, evidence, base_route).

WIRING ALREADY IN PLACE
  * disable/degrade plumbing: a placeholder grows a `[<rule>:natural]` / `[<operator>]` marker exactly where a rule
    or an over-application operator reaches that key+field, so a dead rule or a dead operator shows up empty in
    contract.controls before any real value exists.
  * `_off` / `_has` follow the exemplar: a rule is off for a key whole (the id in `disable`) or per key
    ((id, {keys})) and is also off when its deciding records are missing from the parsed SQL (base records excepted).
  * `base_route` routes every base deciding record (the push sheet, the base PRs, review comments and issues) so
    contract.golden can read them through tools/hg.py records.

TWO MISMATCHES THE BUILD SESSION MUST RECONCILE (contract.controls and contract.slots are blocking)
  1. `decides` / `controls` are the MANIFEST's prose and labels, verbatim. oracle_kit reads `decides` as ROW FIELD
     NAMES and `controls` as SOLVER KEYS, so both must be rewritten before the contract can pass: `decides_fields`
     and `control_keys` on each rule are the mechanical replacement (see DECIDES_FIELDS / CONTROL_KEYS below).
  2. Six surface slots are `class: "direct"` with a `reason_matches` selector (S06, S08, S09, S10, S11, P06).
     gradable_surface.solver_value() has no `reason_matches` branch, so those slots read NOT_SOLVER and
     contract.slots FAILs no matter what solve() returns. They are graded from the calendar text the run writes,
     so those slots need `class: "write_content"` (or a `field`/`sole_reason` selector) in 01_Gradable_Surface.json.
  Also: CLASS_FIELD is "Status" (the beats' column). The push deliverable's class column is "Send or hold", so a
  push rule's `decides` must name "Send or hold" - the module-level class field alone cannot cover both tables.
"""
import collections
import hashlib
import re

REVISIONS = ("rev1",)
CLASS_FIELD = "Status"
GROUPS_FIELD = "groups"

# The solver's row fields (column names of the two table deliverables).
STATUS = "Status"                                    # Run / Held
FIRST_WINDOW = "First window (UTC)"
WEEKS = "Weeks running"
TODO_FIELD = "Still to do (owner, due)"
SEND_HOLD = "Send or hold"                           # Send / Held
MISSING = "What is missing (owner)"                  # the held push's reason
FIELDS = [STATUS, FIRST_WINDOW, WEEKS, TODO_FIELD, SEND_HOLD, MISSING]
BEAT_FIELDS = [STATUS, FIRST_WINDOW, WEEKS, TODO_FIELD]
PUSH_FIELDS = [SEND_HOLD, MISSING]

# ---------------------------------------------------------------- the keys
BEATS = [
    "Plague Race",
    "Collect & Win",
    "Season Pass",
    "Endless Monster Mode",
    "Weekly Leagues",
    "Zombie Lane",
    "Quests",
    "Daily Login",
]
# The "PNs Beta" tab's Ready rows the calendar carries a push for (the fifth, "Weekly Leaderboard reset", and the
# Not-Ready "Win & Collect event start" row are the open question - see PUSH_KEYS_TODO).
PUSHES = [
    "1-day lapse",
    "D0-1 FTUE",
    "Plague Race start",
    "Lives recharged",
    "7-day lapse",
    "Win & Collect event start",
]
# TODO(build): the base push sheet f_a325dd4af80afc5994d5dc "PNs Beta" holds 14 rows. Ready: lives recharged,
# 1-day lapse, 7-day lapse, D0-1 FTUE, Plague Race, Weekly Leaderboard reset. Not Ready: Quests, Hourly Coins,
# Win & Collect, Nathan's Treasure Hunt, Streak Fever, Axe Arena, Login Calendar, Season Pass. Decide whether the
# sixth key is "Win & Collect event start" (Not Ready -> held) or "Weekly Leaderboard reset" (Ready, and the beat it
# belongs to is held); 01_Gradable_Surface.json's pushes key_regex names neither.

KEYS = BEATS + PUSHES


def keys():
    return list(KEYS)


# ---------------------------------------------------------------- the rules (manifest mirror)
# The fourteen entries of 01_Hardness_Manifest.draft.json mechanism_portfolio, field for field. `family` repeats
# `mechanism` (the exemplar's idiom; oracle_kit pools channel rates by it). `authority` is derived mechanically from
# the manifest's authorities[].governs (H1 governs R1/R3/R4/R6, H2 R8, H3 R2); a requirement governs no authority for
# R5. `decides_fields` and `control_keys` are the reconciled, machine-readable form of the prose (see the docstring).
RULES = {
    "R_DONE_DEPLOY": {
        "mechanism": "A24", "family": "A24", "requirement": "R2", "nodes": ["T1", "CH1"],
        "natural_reading": "merged client PRs + 'feature completed' = starts with the first beta window",
        "decides": ["Collect & Win first window", "Collect & Win still to do"],
        "decides_fields": [FIRST_WINDOW, TODO_FIELD],
        "controls": ["Plague Race", "Endless"],
        "control_keys": ["Plague Race", "Endless Monster Mode"],
        "over_application": "over:every-beat-waits-for-a-release",
        "source": "inline-470", "signature": "merged-not-deployed", "authority": ["H3"],
    },
    "R_WITHDRAWN": {
        "mechanism": "A11", "family": "A11", "requirement": "R4", "nodes": ["T2", "CH2"],
        "natural_reading": "the Product owner's approval in the art thread stands",
        "decides": ["Plague Race weeks running", "Halloween one-off in the reply"],
        "decides_fields": [WEEKS],
        "controls": ["Endless", "Season Pass"],
        "control_keys": ["Endless Monster Mode", "Season Pass"],
        "over_application": "over:every-one-off-dropped",
        "source": "robert-dm-thread", "signature": "approval-taken-back", "authority": ["H1"],
    },
    "R_SCOPE_BEATS": {
        "mechanism": "A17", "family": "A17", "requirement": "R1", "nodes": ["T3"],
        "natural_reading": "the beats are the events everyone lists",
        "decides": ["Quests row", "Login calendar row"],
        "decides_fields": [STATUS, TODO_FIELD],
        "controls": ["Plague Race", "Endless"],
        "control_keys": ["Plague Race", "Endless Monster Mode"],
        "over_application": "over:every-push-row-is-a-beat",
        "source": "brief-scope", "signature": "resets-are-beats", "authority": ["H1"],
    },
    "R_COPY_CURRENT": {
        "mechanism": "A15", "family": "A15", "requirement": "R6", "nodes": ["T4"],
        "natural_reading": "Ready in the push sheet = sendable",
        "decides": ["1-day lapse push", "D0-1 FTUE push"],
        "decides_fields": [SEND_HOLD, MISSING],
        "controls": ["7-day lapse", "Lives recharged"],
        "control_keys": ["7-day lapse", "Lives recharged"],
        "over_application": "over:every-zombie-copy-held",
        "source": "brief-copy", "signature": "old-title-held", "authority": ["H1"],
    },
    "R_WIRED": {
        "mechanism": "A15", "family": "A15", "requirement": "R6", "nodes": ["T5"],
        "natural_reading": "Ready = wired",
        "decides": ["Plague Race start push"],
        "decides_fields": [SEND_HOLD, MISSING],
        "controls": ["7-day lapse", "Lives recharged"],
        "control_keys": ["7-day lapse", "Lives recharged"],
        "over_application": "over:every-push-held",
        "source": "brief-wiring", "signature": "ready-but-wip", "authority": ["H1"],
    },
    "R_TECH_HOLD": {
        "mechanism": "A1", "family": "A1", "requirement": "R3", "nodes": ["T7", "CH4"],
        "natural_reading": "the owner note and the Sep 22 fix settle it: a restart gets players in",
        "decides": ["Weekly leagues status", "ZOM-429 hold note"],
        "decides_fields": [STATUS],
        "controls": ["Quests", "Daily login"],
        "control_keys": ["Quests", "Daily Login"],
        "over_application": "over:every-restart-fault-held",
        "source": "retest-reply", "signature": "fails-after-restart", "authority": ["H1"],
    },
    "R_HANDOFF_SLIP": {
        "mechanism": "A14", "family": "A14", "requirement": "R8", "nodes": ["T8", "CH3"],
        "natural_reading": "the handoff thread's date is the date",
        "decides": ["Season Pass November config deadline", "reply to Brian"],
        "decides_fields": [TODO_FIELD],
        "controls": ["Endless", "Zombie Lane"],
        "control_keys": ["Endless Monster Mode", "Zombie Lane"],
        "over_application": None,
        "source": "brian-slip-mail", "signature": "date-moved-in-other-thread", "authority": ["H2"],
    },
    "R_LOCK_BOUNDARY": {
        "mechanism": "A19", "family": "A19", "requirement": "R8", "nodes": ["T9"],
        "natural_reading": "a delivery on the lock day is on time",
        "decides": ["Season Pass November config deadline", "reply to Brian"],
        "decides_fields": [TODO_FIELD],
        "controls": ["Collect & Win"],
        "control_keys": ["Collect & Win"],
        "over_application": None,
        "source": "lock-instant", "signature": "lock-day-late", "authority": ["H2"],
    },
    "R_DONE_ELSEWHERE": {
        "mechanism": "A25", "family": "A25", "requirement": "R5", "nodes": ["T10", "CH5"],
        "natural_reading": "an open ticket is still to do",
        "decides": ["Daily login still to do"],
        "decides_fields": [TODO_FIELD],
        # manifest labels are records (the *issues* the rule must leave alone), not solver keys: they must be
        # re-pointed to the beat whose still-to-do they protect (ZOM-344 -> Quests, ZOM-556 -> Daily Login).
        "controls": ["ZOM-344", "ZOM-556"],
        "control_keys": ["Quests", "Daily Login"],
        "over_application": "over:every-open-ticket-done",
        "source": "pr-471", "signature": "shipped-ticket-open", "authority": ["H1"],
    },
    "R_REVIEW_FLAGS": {
        "mechanism": "A3", "family": "A3", "requirement": "R5", "nodes": ["T11", "CH6"],
        "natural_reading": "approved or bot-only PRs leave nothing to do",
        "decides": ["Collect & Win still to do", "Season Pass still to do"],
        "decides_fields": [TODO_FIELD],
        # same shape: the manifest names the two PRs (#420, #364) that must add no task; contract.controls needs
        # solver keys, so the build session re-points each to the beat it protects.
        "controls": ["harmonygames-Games/match3d#420", "harmonygames-Games/match3d#364"],
        "control_keys": [],                       # TODO(build): two solver keys (beat rows the PRs leave untouched)
        "over_application": "over:every-pr-adds-a-task",
        "source": "post-merge-pass", "signature": "flag-in-inline-note", "authority": ["H1"],
    },
    "R_QUEST_SET": {
        "mechanism": "A13", "family": "A13", "requirement": "R5", "nodes": ["T12"],
        "natural_reading": "the quests rollover runs its new set from week 1",
        "decides": ["Quests still to do"],
        "decides_fields": [TODO_FIELD],
        "controls": ["Login calendar"],
        "control_keys": ["Daily Login"],
        "over_application": None,
        "source": "trello-quests", "signature": "new-set-later", "authority": ["H1"],
    },
    "R_HOLD_SCOPE": {
        "mechanism": "A17", "family": "A17", "requirement": "R3", "nodes": ["D7", "D8", "D9"],
        "natural_reading": "an open or diagnosed fault thread means the beat is held",
        "decides": ["Endless runs", "Zombie Lane runs", "Season Pass runs"],
        "decides_fields": [STATUS],
        "controls": ["Plague Race", "Daily Login"],
        "control_keys": ["Plague Race", "Daily Login"],
        "over_application": "over:every-open-fault-holds-the-beat",
        "source": "fault-threads", "signature": "cosmetic-fault-not-a-hold", "authority": ["H1"],
    },
    "R_ICON_SCOPE": {
        "mechanism": "A17", "family": "A17", "requirement": "R5", "nodes": ["T14"],
        "natural_reading": "the master VFX ticket struck 'all event icons' as done, so every icon is animated",
        "decides": ["Collect & Win still to do (icon)"],
        "decides_fields": [TODO_FIELD],
        "controls": ["Season Pass", "Zombie Lane"],
        "control_keys": ["Season Pass", "Zombie Lane"],
        "over_application": "over:all-event-icons-done",
        "source": "icon-master-vs-prs", "signature": "cw-icon-absent", "authority": ["H1"],
    },
    "R_INFRA_SCOPE": {
        "mechanism": "A17", "family": "A17", "requirement": "R3", "nodes": ["D10"],
        "natural_reading": ("the in-progress queue manager, whose flow list does not yet order the Plague Race "
                            "panel, holds Plague Race"),
        "decides": ["Plague Race runs"],
        "decides_fields": [STATUS],
        "controls": ["Plague Race"],
        "control_keys": ["Plague Race"],
        "over_application": "over:an-unqueued-panel-holds-the-beat",
        "source": "queue-manager", "signature": "unqueued-panel-not-a-hold", "authority": ["H1"],
    },
}

# The reconciled machine form of the manifest's prose (see the module docstring mismatch 1). contract.controls reads
# `RULES[r]["decides"]` as row field names and `RULES[r]["controls"]` as solver output keys; the build session flips
# RULES onto these two maps (a two-line comprehension) once it agrees with them.
DECIDES_FIELDS = {r: list(v.get("decides_fields") or []) for r, v in RULES.items()}
CONTROL_KEYS = {r: list(v.get("control_keys") or []) for r, v in RULES.items()}

DEGRADES = {
    "over:every-beat-waits-for-a-release":
        "start every beat only after the backend release, not at its own first opening window",
    "over:every-one-off-dropped":
        "treat every one-off as dropped because the Halloween one-off was taken back",
    "over:every-push-row-is-a-beat":
        "put every push row on the calendar as a beat of its own",
    "over:every-zombie-copy-held":
        "hold every push whose row is Ready because one row still carries the old game name",
    "over:every-push-held":
        "hold every push because its wiring column reads WIP",
    "over:every-restart-fault-held":
        "hold every beat whose thread mentions a fault, restart or not",
    "over:every-open-ticket-done":
        "treat every open ticket as already shipped",
    "over:every-pr-adds-a-task":
        "give every merged PR a still-to-do line, approved or bot-only included",
    "over:every-open-fault-holds-the-beat":
        "hold every beat with an open cosmetic, VFX, performance or analytics fault",
    "over:all-event-icons-done":
        "treat the master icon ticket's 'all event icons' as covering Collect & Win",
    "over:an-unqueued-panel-holds-the-beat":
        "hold Plague Race because the queue manager has not ordered its panel",
}
CHANNELS = {}      # no async waits or forced errors in this task (03_Error_Async_Config.txt: Friction none)

# Fixed application order: which rows exist, then what holds a beat, then what a beat still needs (window -> config
# -> shipped-elsewhere/flagged), then the one-off, then the push sheet last (a push reads the beat's call).
RULES_ORDER = (
    "R_SCOPE_BEATS",
    "R_HOLD_SCOPE",
    "R_INFRA_SCOPE",
    "R_TECH_HOLD",
    "R_DONE_DEPLOY",
    "R_LOCK_BOUNDARY",
    "R_HANDOFF_SLIP",
    "R_QUEST_SET",
    "R_DONE_ELSEWHERE",
    "R_REVIEW_FLAGS",
    "R_ICON_SCOPE",
    "R_WITHDRAWN",
    "R_COPY_CURRENT",
    "R_WIRED",
)

# ---------------------------------------------------------------- records
# Seeded by 01_Universe_Inject.sql (parsed, never executed).
SLACK_APPROVAL = "C08R8CHB0QL/1758213600.552913"          # Robert approves the Halloween one-off (sid 2e75e232...)
SLACK_WITHDRAW = "D05GU6L0XFH/1759270200.638114"          # Robert takes it back in his DM thread (sid 58d06bd5...)
SLACK_RETEST = "C0880U9751A/1759265412.481907"            # Vincent re-tests the weekly leaderboard (fa3eee2c...)
SLACK_ASK = "D05SD5QLG94/1759263600.418207"               # Frederick's ask: the calendar of the four buy weeks
BRIEF = "f_7c3e91a4d2b85f60e1a9c4"                        # Frederick's working rules (docs)
UA_PLAN = "f_2b9d4e7a1c63f08d5e7b21"                      # the four buy weeks (slides)
CALENDAR_SHEET = "f_e4a17c90b3d25f6a8c1d73"               # Julia's calendar sheet (Calendar + Pushes tabs)
EVT_RELEASE = "evt_9a4c2e7f1b3d58e06c7a2f"                # Douglas: backend release, Oct 8 15:00-16:00 UTC
MAIL_0922 = "julia.lawson@harmonygames.co/<CAH4q9Zb2fK7xQe1M8sPnL3vT6wR0yDc@mail.gmail.com>"   # config: Fri Oct 29
MAIL_0926 = "julia.lawson@harmonygames.co/<CAH4q9Zc8uV1nE5kJ2mRtP7aW3xQ9bLs@mail.gmail.com>"  # slip: Fri Oct 31
CMT_ZOM429 = "cmt_zom429_1"        # restart gets players into the new week
CMT_ZOM556 = "cmt_zom556_1"        # the streak pays out; the counter is cosmetic
CMT_ZOM565 = "cmt_zom565_1"        # endless start-screen VFX live
CMT_ZOM543 = "cmt_zom543_1"        # queue manager: the panel order list
CMT_ZOM526 = "cmt_zom526_1"        # token-to-live-ops travel, VFX paths
CMT_ZOM552 = "cmt_zom552_1"        # season pass redeem events
CMT_ZOM534 = "cmt_zom534_1"        # quest points rollover syncs now
CMT_ZOM432 = "cmt_zom432_1"        # daily gift frame still owed (superseded by #471@c_18)
CMT_ZOM78 = "cmt_zom78_1"          # use ZOM-78 for the calendar ticket
CMT_ZOM465 = "cmt_zom465_1"        # 'all event icons animate' claim
CMT_ZOM344 = "cmt_zom344_1"
CMT_ZOM471 = "cmt_zom471_1"
CMT_ZOM504 = "cmt_zom504_1"        # endless visual-only clear
CMT_ZOM517 = "cmt_zom517_1"        # enrage state, test board only
CMT_ZOM521 = "cmt_zom521_1"        # master VFX checklist
CMT_ZOM542 = "cmt_zom542_1"        # endless/boss arena layouts
CMT_ZOM546 = "cmt_zom546_1"        # refill counts hold
CMT_ZOM549 = "cmt_zom549_1"        # analytics payloads
CMT_ZOM566 = "cmt_zom566_1"        # C&W event list mapped to the sheet
PR470_RC = "harmonygames-Games/match3d#470#rc_10"         # Arthur: C&W server windows are DEV-only
PR370_RC = "harmonygames-Games/match3d#370#rc_1"          # Arthur: final vial sprites still missing
PR438_RC = "harmonygames-Games/match3d#438#rc_74"         # Arthur: premium strip moves to November
PR454_C = "harmonygames-Games/match3d#454#c_4"            # Marcus: the C&W event icon is still to do
PR471_C = "harmonygames-Games/match3d#471#c_18"           # Samuel: the daily-gift frame shipped in #135
TRELLO_QUESTS = "68dac8204f1e9a3b7c2d5e61"               # Brian: the new quest set lands with the Mon Oct 13 rollover

# Base records: they live in the exports, never in the injection SQL, so _has() treats them as always present.
PUSH_SHEET = "f_a325dd4af80afc5994d5dc"                   # the PNs Beta push sheet (base, gsheets)
PAGE_LIVEOPS = "page_liveops_calendar"                    # confluence: 'same feature as Win & Collect'
PR470 = "harmonygames-Games/match3d#470"
PR370 = "harmonygames-Games/match3d#370"
PR438 = "harmonygames-Games/match3d#438"
PR454 = "harmonygames-Games/match3d#454"
PR456 = "harmonygames-Games/match3d#456"
PR471 = "harmonygames-Games/match3d#471"
PR475 = "harmonygames-Games/match3d#475"
PR459 = "harmonygames-Games/match3d#459"
PR472 = "harmonygames-Games/match3d#472"
ZOM_429 = "ZOM-429"
ZOM_432 = "ZOM-432"
ZOM_465 = "ZOM-465"
ZOM_543 = "ZOM-543"
ZOM_556 = "ZOM-556"
ZOM_534 = "ZOM-534"
ZOM_344 = "ZOM-344"
ZOM_78 = "ZOM-78"
BASE = frozenset({PUSH_SHEET, PAGE_LIVEOPS, PR470, PR370, PR438, PR454, PR456, PR471, PR475, PR459, PR472,
                  ZOM_429, ZOM_432, ZOM_465, ZOM_543, ZOM_556, ZOM_534, ZOM_344, ZOM_78})

# ---------------------------------------------------------------- deciding records (CANDIDATE)
# TODO(build): confirm every id below against the record before it becomes the evidence of a graded value. The pairs
# are the ones the manifest's traps and sources name; none of them asserts a value yet.
DECIDING = {
    ("R_DONE_DEPLOY", "Collect & Win"): [PR470_RC, EVT_RELEASE, BRIEF],
    ("R_WITHDRAWN", "Plague Race"): [SLACK_APPROVAL, SLACK_WITHDRAW, BRIEF],
    ("R_SCOPE_BEATS", "Quests"): [BRIEF, TRELLO_QUESTS],
    ("R_SCOPE_BEATS", "Daily Login"): [BRIEF, CMT_ZOM432, CMT_ZOM556],
    ("R_COPY_CURRENT", "1-day lapse"): [BRIEF, PUSH_SHEET],
    ("R_COPY_CURRENT", "D0-1 FTUE"): [BRIEF, PUSH_SHEET],
    ("R_WIRED", "Plague Race start"): [BRIEF, PUSH_SHEET],
    ("R_TECH_HOLD", "Weekly Leagues"): [CMT_ZOM429, SLACK_RETEST, BRIEF],
    ("R_HANDOFF_SLIP", "Season Pass"): [MAIL_0922, MAIL_0926, BRIEF],
    ("R_LOCK_BOUNDARY", "Season Pass"): [MAIL_0926, BRIEF],
    ("R_DONE_ELSEWHERE", "Daily Login"): [PR471_C, CMT_ZOM432, BRIEF],
    ("R_REVIEW_FLAGS", "Collect & Win"): [PR370_RC, BRIEF],
    ("R_REVIEW_FLAGS", "Season Pass"): [PR438_RC, BRIEF],
    ("R_QUEST_SET", "Quests"): [TRELLO_QUESTS, BRIEF],
    ("R_HOLD_SCOPE", "Endless Monster Mode"): [CMT_ZOM504, CMT_ZOM565, CMT_ZOM521, BRIEF],
    ("R_HOLD_SCOPE", "Zombie Lane"): [CMT_ZOM526, CMT_ZOM542, BRIEF],
    ("R_HOLD_SCOPE", "Season Pass"): [CMT_ZOM552, BRIEF],
    ("R_ICON_SCOPE", "Collect & Win"): [CMT_ZOM465, PR454_C, PR454, PR456, PR475, BRIEF],
    ("R_INFRA_SCOPE", "Plague Race"): [CMT_ZOM543, PR459, PR472, BRIEF],
}

# The keys a rule can act on (derived from DECIDING, so a rule with no deciding key acts on nothing).
TOUCHED = {}
for _rule, _key in DECIDING:
    TOUCHED.setdefault(_rule, set()).add(_key)


def _sid(ref):
    """The id a seeded Slack message row carries: sha256("<channel>|<ts>")[:32]."""
    ch, ts = ref.split("/")
    return hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]


def _has(state, *ids):
    """Every deciding record is present in the SQL; base records live in the exports and are always present."""
    have = state.get("ids") if isinstance(state, dict) else None
    if have is None:
        return True
    return all(i in have for i in ids if i not in BASE)


def _off(spec, name, key):
    """True when `name` is disabled/applied for `key` (whole, or via a (name, key set) pair)."""
    for d in spec:
        if isinstance(d, tuple):
            if d[0] == name and key in d[1]:
                return True
        elif d == name:
            return True
    return False


def _uniq(seq):
    out, seen = [], set()
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def load_state(sql_text, revision=None):
    """The injected records, parsed as data (never executed), indexed by id and by table."""
    try:
        from base_check import parse_sql
    except ImportError:                                   # direct use outside the tool bundle
        import pathlib
        import sys
        for parent in pathlib.Path(__file__).resolve().parents:
            if (parent / "tools" / "base_check.py").is_file():
                sys.path.insert(0, str(parent / "tools"))
                break
        from base_check import parse_sql
    inserts = [x for x in parse_sql(sql_text) if x["op"] == "insert"]
    ids, by_id, tables = set(), {}, {}
    for x in inserts:
        r = x["row"]
        tables.setdefault(x["table"], []).append(r)
        found = []
        for c in ("id", "identifier", "document_id", "spreadsheet_id", "presentation_id", "event_id", "thread_id",
                  "card_id", "issue_id", "commit_id", "comment_id"):
            if r.get(c):
                found.append(str(r[c]))
        if r.get("ts") and (r.get("channel_id") or r.get("channel")):   # a Slack row is also reachable as channel|ts
            ref = f"{r.get('channel_id') or r.get('channel')}/{r['ts']}"
            found.append(ref)
            found.append(_sid(ref))                                      # the row id, sha256 of the same ref
        for v in found:
            ids.add(v)
            by_id.setdefault(v, []).append((x["table"], r))
    return {"ids": ids, "by_id": by_id, "tables": tables, "revision": revision or REVISIONS[-1],
            "rows": len(inserts), "counts": {t: len(v) for t, v in tables.items()}}


def _groups(key):
    """TODO(build): the row's groups (the exemplar's idiom: the deliverable plus the class, lower-cased, plus any
    deliverable-specific group such as a held beat's ticket). Empty until the class values exist."""
    return []


def _placeholder(state, key, field, disable, degrade):
    """A clearly-marked stand-in value plus the rules/operators that reach this key+field.

    The marker is the wiring proof, not the answer: `[R_X:natural]` says the rule is off for this key (or lost its
    deciding records) on a field it decides, `[over:...]` says that over-application operator reaches this key (as a
    decided key or a control member). Deterministic: markers are sorted.
    """
    marks = []
    for rule in RULES_ORDER:
        fields = DECIDES_FIELDS.get(rule, [])
        if field not in fields:
            continue
        if key in TOUCHED.get(rule, ()) and (_off(disable, rule, key)
                                             or not _has(state, *DECIDING.get((rule, key), []))):
            marks.append(f"{rule}:natural")
        op = RULES[rule].get("over_application")
        members = set(TOUCHED.get(rule, ())) | set(CONTROL_KEYS.get(rule, []))
        if op and key in members and _off(degrade, op, key):
            marks.append(op)
    base = f"TODO_{key}_{field}"
    marks = _uniq(marks)
    return base if not marks else base + " [" + " ".join(sorted(marks)) + "]"


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    """The expected value of every row (SKELETON - the build session owns the judgment).

    Per key and field, this is what decides it (manifest `decides` + `controls` + the surface selectors). Records are
    the DECIDING ids above; the rule order is RULES_ORDER.

    "Plague Race"
      Status            R_INFRA_SCOPE (D10): the queue manager (CMT_ZOM543, #459, #472) does not order the Plague
                        Race panel, yet players still enter, score and claim -> Runs. Over-apply:
                        over:an-unqueued-panel-holds-the-beat -> Held.  Surface C01 (accepted: Runs/Run/Go/Live).
      Weeks running     R_WITHDRAWN (T2/CH2): Robert's approval (SLACK_APPROVAL) vs his later DM withdrawal
                        (SLACK_WITHDRAW, "my later word ... counts") -> All four weeks. Over-apply:
                        over:every-one-off-dropped.  Surface S02.
      Still to do       none raised: "nothing left" (an empty cell). Surface S07-style missing_values apply.
    "Collect & Win"
      First window      R_DONE_DEPLOY (T1/CH1): server windows are DEV-only until EVT_RELEASE (Oct 8 15:00-16:00 UTC)
                        and the brief's Mon-Tue/Wed-Thu/Fri-Sun 00:00 UTC cadence pre-empts the window the release
                        opens inside -> Fri Oct 10 00:00 UTC. Over-apply: over:every-beat-waits-for-a-release.
                        Surface S01 (accepted outcomes list the allowed renderings).
      Status            C05: a live beat once its prod windows open; the queue/addressables gaps do not hold it -> Runs.
      Still to do       three owners, one cell: R_REVIEW_FLAGS (PR370_RC: vial sprites, Claire) + R_ICON_SCOPE
                        (CMT_ZOM465 vs #454/#456/#475: the C&W event icon is absent, Marcus) + R_DONE_DEPLOY.
                        Surfaces S08 (vial|sprite) and S11 (icon).
      Weeks running     n/a (the event runs to the end of the buy weeks).
    "Season Pass"
      Status            R_HOLD_SCOPE (D7-D9): the open issues are analytics -> Runs.  Surface C04.
      Still to do       R_HANDOFF_SLIP (T8/CH3: MAIL_0926 moves Oct 29 -> Fri Oct 31 10:00 Istanbul) +
                        R_LOCK_BOUNDARY (T9: the 24 h lock before the Nov 1 00:00 UTC opening makes it late; state
                        Oct 31 00:00 UTC / Oct 30 17:00 PDT) + R_REVIEW_FLAGS (PR438_RC: premium strip -> November,
                        Oliver).  Surfaces S09 (premium|strip|banner) and S10 (the lock regex).
      Weeks running     n/a.
    "Endless Monster Mode"
      Status            R_HOLD_SCOPE: its faults are VFX/analytics (CMT_ZOM504, CMT_ZOM565, CMT_ZOM521) -> Runs.
                        Surface C02.
    "Weekly Leagues"
      Status            R_TECH_HOLD (T7/CH4): the Sep 22 "working fine" note (CMT_ZOM429) is overturned by Vincent's
                        Sep 30 re-test (SLACK_RETEST: no new week even after two restarts) -> Held. Over-apply:
                        over:every-restart-fault-held.  Surface S03 + the ZOM-429 note (W05).
      Still to do       the restart fix, owner from the league ticket (surface W05 writes it).
    "Zombie Lane"
      Status            R_HOLD_SCOPE: no fault stops enter/score/claim -> Runs.  Surface C03.
    "Quests"
      Status            R_SCOPE_BEATS (T3/R1): the rollover is a reset the brief puts on the calendar -> in and Runs;
                        the ZOM-534 restart-clearing fault is a known issue, not a hold.  Surface S04.
      Still to do       R_QUEST_SET (T12): TRELLO_QUESTS puts the new set with the Mon Oct 13 rollover (Brian).
                        Surface S06 (regex wants Oct 13 / week 2 / "new quest").
    "Daily Login"
      Status            R_SCOPE_BEATS -> in and Runs (ZOM-556: claiming works, the counter is cosmetic). Surface S05.
      Still to do       R_DONE_ELSEWHERE (T10/CH5): ZOM-432 is still Todo but PR471_C says the frame shipped in
                        #135 -> nothing left (empty cell).  Surface S07.
    "1-day lapse"       R_COPY_CURRENT (T4): Ready, but the English copy still says "Puzzles vs Zombies" -> Held.
                        What is missing: the old-title copy fix. Surfaces P01 + P06.
    "D0-1 FTUE"         R_COPY_CURRENT: same old title -> Held. Surface P02.
    "Plague Race start" R_WIRED (T5): Ready but "Status (NA, WIP, LIVE)" reads WIP -> Held (not wired). Surface P03.
    "Lives recharged"   Ready + LIVE + its own copy -> Send.  Surface P04.
    "7-day lapse"       Ready + LIVE + its own copy -> Send.  Surface P05.
    "Win & Collect event start"  TODO(build): the Not-Ready row; decide whether it is a calendar push at all (the
                        brief scopes pushes to English PNs Beta) and whether its name is the ZM3D one.
    """
    out = {}
    for k in (keys_ or keys()):
        row = {}
        row["Beat" if k in BEATS else "Push"] = k
        for f in (BEAT_FIELDS if k in BEATS else PUSH_FIELDS):
            row[f] = _placeholder(state, k, f, disable, degrade)
        # TODO(build): apply the rules in RULES_ORDER for this key (each rule's natural reading when it is off for
        # the key or its deciding records are missing), then the over-application operators of its control members,
        # then set "groups" (deliverable + lower-cased class + any ticket group) and "evidence".
        fields = BEAT_FIELDS if k in BEATS else PUSH_FIELDS
        row["groups"] = _groups(k)
        row["evidence"] = _uniq([i for f in fields for i in evidence({}, k, f)])
        out[k] = row
    return out


def aggregates(rows):
    classes = dict(collections.Counter(v.get(CLASS_FIELD) for v in rows.values() if v.get(CLASS_FIELD)))
    groups = {}
    for k in sorted(rows):
        for g in rows[k].get(GROUPS_FIELD) or []:
            groups.setdefault(g, []).append(k)
    return {"classes": classes, "groups": groups}


def evidence(rows, key, field):
    """The record(s) that decide one field of one row (the golden check's sample). CANDIDATE ids - see DECIDING."""
    if field in ("Beat", "Push"):
        return []
    ids = []
    for rule in RULES_ORDER:
        if key not in TOUCHED.get(rule, ()) or field not in DECIDES_FIELDS.get(rule, []):
            continue
        ids.extend(DECIDING.get((rule, key), []))
    return _uniq(ids)


def touched(state, rule):
    return set(TOUCHED.get(rule, ()))


def deciding(state, rule, key):
    return list(DECIDING.get((rule, key), []))


# (pattern, service, file, pointer, field) - the export location of a base record, read by tools/hg.py records.
# Base records the solver routes are checked; unrouted ones are reported unverified.
BASE_ROUTES = [
    (r"#rc_\d+$", "github", "data.json", "/review_comments", "id"),
    (r"#rev_\d+$", "github", "data.json", "/reviews", "id"),
    (r"#c_\d+$", "github", "data.json", "/pull_request_comments", "id"),
    (r"#ev_\d+$", "github", "data.json", "/timeline_events", "id"),
    (r"^harmonygames-Games/[A-Za-z0-9_.-]+#\d+$", "github", "data.json", "/pull_requests", "id"),
    (r"^ZOM-\d+$", "linear", "data.json", "/issues", "identifier"),
    (r"^cmt_[A-Za-z0-9_]+$", "linear", "data.json", "/comments", "id"),
    (r"^evt_[0-9a-f]+$", "gcal", "data.json", "/events", "event_id"),
    (r"^[a-z0-9._%+-]+@harmonygames\.co/<", "gmail", "threads/*.json", "/messages", "id"),
    (r"^[A-Z0-9]{8,}/[0-9]+\.[0-9]+$", "slack", "messages/*/*.json", "", "id"),
    (r"^[0-9a-f]{24}$", "trello", "data.json", "/actions", "id"),
    (r"^page_[a-z0-9_]+$", "confluence", "confluence_working.json", "/pages", "id"),
    (r"^d_[0-9a-f]{20,}$", "gdrive", "data.json", "/drive_files", "id"),
]
# The f_-prefixed ids are ambiguous by prefix (a doc, a deck and two sheets); route them by name.
F_ROUTES = {
    BRIEF: ("gdocs", "data.json", "/docs_documents", "document_id"),
    UA_PLAN: ("gslides", "data.json", "/slides_presentations", "presentation_id"),
    CALENDAR_SHEET: ("gsheets", "data.json", "/sheets_spreadsheets", "spreadsheet_id"),
    PUSH_SHEET: ("gsheets", "data.json", "/sheets_spreadsheets", "spreadsheet_id"),
}


def base_route(record_id):
    """Where a base deciding record lives in the exports (read through tools/hg.py records by the golden check)."""
    rid = str(record_id or "")
    if rid in F_ROUTES:
        service, file, pointer, field = F_ROUTES[rid]
        return {"service": service, "file": file, "pointer": pointer, "field": field}
    for pattern, service, file, pointer, field in BASE_ROUTES:
        if re.search(pattern, rid):
            return {"service": service, "file": file, "pointer": pointer, "field": field}
    return None
