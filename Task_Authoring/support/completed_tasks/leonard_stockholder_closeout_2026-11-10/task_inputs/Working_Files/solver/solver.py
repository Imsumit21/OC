"""Solver for Leonard's stockholder close-out (tools/oracle_kit.py contract), rev2.

Truth = the holder schedule Leonard should have at the clock (2026-02-14 00:00 UTC, normal universe): one row per project
issue, ENG-2438 to ENG-2463, plus SUMMARY for the company-wide figures. Built from the base facts below (re-read through
tools/hg.py; research/s2_option_notice_state.md, 00_PreScenario/verified_anchors.txt) and the injection SQL (parsed with
tools/base_check.parse_sql; never executed).

One rule per mechanism_portfolio entry. Each reads its deciding record where that record is seeded, and falls back to its
natural reading when `disable` switches it off (whole or per key set), when its channel degrade hits the key, or when the
record is absent. Over-application operators act on the declared controls. SUMMARY reads only its own rule state, so the
solver stays key-local.
"""
import collections

KEY_REGEX = r"ENG-\d{4}|SUMMARY"
FIELDS = ["Issue", "Holder", "Instrument", "Shares held now", "Last day", "Told", "Owed", "State",
          "Options now", "Options at Dec 31", "Open question"]
CLASS_FIELD, GROUPS_FIELD = "Owed", "groups"
CLOCK, AS_OF = "2026-02-14", "2025-12-31"

MB = "leonard.hayes@harmonygames.co"
R_NOTES = "f_a37b403d5200d4f0a31d31"                  # Leonard's close-out notes (the closed rule)
R_KPMG = f"{MB}/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com>"   # KPMG's FY25 request
R_ROBERT = f"{MB}/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com>"           # Robert's reply to Nebojsa

def _slack_id(channel, ts):
    import hashlib
    return hashlib.sha256(f"{channel}|{ts}".encode()).hexdigest()[:32]

R_FAMILY = _slack_id("C0ADGSZKR3R", "1770949310.220519")      # Leonard's reply under his Feb 12 list
R_BOARD = f"{MB}/<CAGkro_Tn7wQ2xLp9VbR4mYc8KsHd3EjUf6ZaNi1oGqX5tBe0Rw@mail.gmail.com>"   # Robert: Leonard and me on the board
R_BOUNCE = f"{MB}/<698ce305.050a0220.3b7f1c.9d2e.GMR@mx.google.com>"    # rev2: Owen's Feb 11 letter bounced (in its own thread)
R_EXT = f"{MB}/<CAJr7mPx2QwF8nVb4LtK9sYd3HcE6uZaR1oGiN5tMeBq0WsXkQz@mail.gmail.com>"   # rev2: Calvin forwards Carta's Jan 23 update (ES-3 to Feb 20)
EXT_LAST = {"ENG-2452": "2026-02-20"}
BOUNCED = {"ENG-2457"}
R_AKIN = f"{MB}/<CAPBs_aLeDrdRoqOb0LrQ1AfGvbpmR-YdoG8A6PGmPay5Sc-ng=@mail.gmail.com>"   # rev2: Leonard tells "Akin" (Matthew Collins) about the closing, Feb 12

# stock lines: issue, name, Carta id, owner-list line, advisor grant inside that line, told, how
STOCK = [
 ("ENG-2438", "Griffin Gaming Partners II, L.P.", "SSP-01", 2662255, 0, True, "Griffin's partner, Feb 12 mail"),
 ("ENG-2439", "Griffin Gaming Partners II Side Fund, L.P.", "SSP-02", 84438, 0, True, "Griffin's partner, Feb 12 mail"),
 ("ENG-2440", "Segerstrale", "SSP-03", 81383, 30518, True, "Leonard's Feb 9 DM"),
 ("ENG-2441", "Schaeppi", "SSP-04", 25432, 0, False, None),
 ("ENG-2442", "Bergmann", "SSP-05", 25432, 0, False, None),
 ("ENG-2443", "Enes", "SSP-06/08", 25432, 0, False, None),
 ("ENG-2444", "Patrick Lewis", "SSP-06/08", 25432, 0, False, None),
 ("ENG-2445", "Eren", "SSP-07", 25432, 0, False, None),
 ("ENG-2446", "Nebojsa", "SSP-09", 31536, 6104, True, "Robert's Feb 12 reply"),
 ("ENG-2447", "Matthew Collins", "SSP-10", 86470, 61038, False, None),
 ("ENG-2448", "TOR Capital Limited", "SSP-11", 50865, 0, False, None),
 ("ENG-2449", "Deepak", "SSP-12", 31536, 6104, False, None),
]
# option lines: issue, name, Carta id, granted, vested, effective, last day, had a Feb 11 letter
OPTION = [
 ("ENG-2450", "Julia Lawson", "ES-1", 30519, 17802, "2025-12-31", "2026-03-31", True),
 ("ENG-2451", "ES-2", "ES-2", 12208, 3052, "2024-08-01", "2024-11-01", False),
 ("ENG-2452", "Calvin Price", "ES-3", 8138, 4408, "2025-10-24", "2026-01-24", False),
 ("ENG-2453", "Claire Morgan", "ES-4", 7630, 4450, "2025-12-31", "2026-03-31", True),
 ("ENG-2454", "Douglas", "ES-5", 10173, 5298, "2025-10-24", "2026-01-24", False),
 ("ENG-2455", "Victor Barnes", "ES-6", 30519, 12716, "2025-04-16", "2025-07-16", False),
 ("ENG-2456", "Marcus Bennett", "ES-7", 22889, 12875, "2026-01-30", "2026-04-30", True),
 ("ENG-2457", "Owen Baker", "ES-12", 16277, 8477, "2026-01-30", "2026-04-30", True),
 ("ENG-2458", "Martin Walsh", "ES-13", 3866, 2013, "2026-01-30", "2026-04-30", True),
 ("ENG-2459", "Vincent Parker", "ES-14", 3866, 1530, "2025-11-21", "2026-02-21", False),
 ("ENG-2460", "Brian Foster", "ES-15", 10173, 3391, "2025-12-31", "2026-03-31", True),
 ("ENG-2461", "ES-16", "ES-16", 35605, 10384, "2025-10-24", "2026-01-24", False),
 ("ENG-2462", "Frederick Stone", "ES-17", 127162, 34439, "2025-10-24", "2026-01-28", False),
 ("ENG-2463", "Oliver Brooks", "ES-18", 15259, 5404, "2026-01-30", "2026-04-30", False),
]
COMMON = 6000000
FAMILY_COVERED = {"ENG-2444", "ENG-2445"}             # the note to Enes (ENG-2443) covers these lines
NO_LETTER = {"ENG-2459", "ENG-2463"}
TOLD_ELSEWHERE = {"ENG-2440", "ENG-2446"}
ADVISOR = {k for k, _, _, _, adv, _, _ in STOCK if adv}
KEYS = [s[0] for s in STOCK] + [o[0] for o in OPTION] + ["SUMMARY"]

RULES = {
 "ADV": {"mechanism": "A17", "requirement": "R3", "nodes": ["T1", "T2", "C1"], "family": "A17", "source": "doc-table",
         "decides": ["Shares held now", "Instrument", "Options now", "Options at Dec 31", "Series Seed total",
                     "Options outstanding now", "Options outstanding at Dec 31", "Issued plus options at Dec 31"],
         "natural_reading": "the owner list's figure is the holder's stock", "signature": "Due Diligence advisor table 103,764",
         "controls": ["ENG-2441", "ENG-2442"], "over_application": "adv_over"},
 "LETTER": {"mechanism": "A24", "requirement": "R5", "nodes": ["T4", "T5", "C2"], "family": "A24", "source": "founder-claim",
            "decides": ["Told", "Owed", "State"],
            "natural_reading": "every Carta termination had a letter, so every live option holder has been told",
            "signature": "six letters against eight entries", "controls": ["ENG-2450", "ENG-2460"], "over_application": "letter_over"},
 "TOLD": {"mechanism": "A25", "requirement": "R4", "nodes": ["T6", "T7", "T8", "C3"], "family": "A25", "source": "dm-and-mail",
          "decides": ["Told", "Owed", "State"], "natural_reading": "the Feb 12 list means no angel has been told",
          "signature": "Feb 9 DM; Robert's Feb 12 reply", "controls": ["ENG-2448"], "over_application": "told_over"},
 "ASOF": {"mechanism": "A19", "requirement": "R8", "nodes": ["T12", "C4"], "family": "A19", "source": "derived",
          "decides": ["Options at Dec 31", "Options outstanding at Dec 31", "Issued plus options at Dec 31"],
          "natural_reading": "the confirmation reports today's option count or the term sheet's",
          "signature": "243,757 options at Dec 31, 2025", "controls": ["ENG-2455"], "over_application": "asof_over"},
 "FAM": {"mechanism": "A7", "requirement": "R6", "nodes": ["T13", "T14", "C7"], "family": "A7", "source": "dm-and-old-mail",
         "decides": ["Owed", "State"], "natural_reading": "three record holders get three notes", "signature": "all three brothers",
         "controls": ["ENG-2441", "ENG-2442"], "over_application": "fam_over"},
 "BOARD": {"mechanism": "A11", "requirement": "R9", "nodes": ["T10", "T11", "C5"], "family": "A11", "source": "mail",
           "decides": ["Directors"], "natural_reading": "the document board list stands and Griffin has nothing left to do",
           "signature": "May 1, 2025 resignation", "controls": ["SUMMARY"], "over_application": "board_over"},
 "ASK": {"mechanism": "A9", "requirement": "R12", "nodes": ["T17", "C8"], "family": "A9", "source": "group-dm",
         "decides": ["Open question"], "natural_reading": "Claire's note only needs her date", "signature": "Claire's equity question",
         "controls": ["ENG-2461"], "over_application": "ask_over"},
 "BOUNCE": {"mechanism": "A24", "requirement": "R4", "nodes": ["T23", "C9"], "family": "A24", "source": "mail-bounce",
            "decides": ["Told", "Owed"], "natural_reading": "a sent letter told its holder, so Owen gets his date only",
            "signature": "delivery failure on Owen's Feb 11 letter", "controls": ["ENG-2456"], "over_application": "bounce_over"},
 "ALIAS": {"mechanism": "A7", "requirement": "R4", "nodes": ["T25", "C11"], "family": "A7", "source": "alias-mail",
           "decides": ["Told", "Owed", "State"], "natural_reading": "no mail to Collins's address after the closing, so he is untold and gets a first note",
           "signature": "Leonard's Feb 12 mail to Akin", "controls": ["ENG-2449"], "over_application": "alias_over"},
 "EXT": {"mechanism": "A11", "requirement": "R2", "nodes": ["T24", "C10"], "family": "A11", "source": "holder-forward",
         "decides": ["Last day", "Told", "Owed", "State", "Options now", "Options outstanding now"],
         "natural_reading": "Carta's Oct 29 termination notice gives ES-3's last day, Jan 24, so the line holds nothing",
         "signature": "Carta's Jan 23 update forwarded by Calvin", "controls": ["ENG-2454"], "over_application": "ext_over"},
}
DEGRADES = {
 "adv_over": "subtracts an advisor grant from a plain $25,000 line",
 "letter_over": "treats a holder with a real letter as untold",
 "told_over": "treats Tor's November runway warning as being told",
 "asof_over": "counts a line that lapsed before the as-of date as still open at it",
 "fam_over": "folds the Solsten pair into one note",
 "board_over": "drops Robert with the outside directors",
 "ask_over": "writes to a lapsed holder because they once asked",
 "bounce_over": "treats Marcus's delivered letter as bounced",
 "ext_over": "extends ES-5's window with Calvin's",
 "alias_over": "takes the Akin mail as telling Deepak too",
 "live_miss": "a lapsed line is misread as live at its grant",
 "ch_adv": "a member's advisor grant is not found: the owner-list figure stands",
 "ch_letter": "a member's missing letter is not noticed: the member counts as told",
 "ch_told": "a member's message is not found: the member counts as untold",
 "ch_asof": "a member's effective date is not applied: it reports what the line holds today",
 "ch_fam": "a member's family link is not found: the member gets its own note",
 "ch_board": "the resignations are not found: the document board stands",
 "ch_ask": "the group-DM question is not found: the note carries the date only",
 "ch_bounce": "the delivery failure is not found: the letter counts as telling Owen",
 "ch_ext": "the forwarded Carta update is not found: ES-3 stays lapsed at Jan 24",
 "ch_alias": "Akin is not tied to Collins: he stays untold and gets a first note",
}
MEMBERS = {
 "ADV": ["ENG-2440", "ENG-2446", "ENG-2447", "ENG-2449", "SUMMARY"],
 "LETTER": ["ENG-2459", "ENG-2463"],
 "TOLD": ["ENG-2440", "ENG-2446"],
 "ASOF": ["ENG-2452", "ENG-2454", "ENG-2456", "ENG-2457", "ENG-2458", "ENG-2461", "ENG-2462", "ENG-2463", "SUMMARY"],
 "FAM": ["ENG-2444", "ENG-2445"],
 "BOARD": ["SUMMARY"],
 "ASK": ["ENG-2453"],
 "BOUNCE": ["ENG-2457"],
 "EXT": ["ENG-2452", "SUMMARY"],
 "ALIAS": ["ENG-2447"],
}
CHANNELS = {"CH-LIVE": {"kind": "scale", "degrade": "live_miss", "latent": "member", "family": "exact_predicate", "source": "carta-notices",
                        "members": ["ENG-2451", "ENG-2454", "ENG-2455", "ENG-2461", "ENG-2462"],
                        "description": "a complexity channel, not a rule: a line is misread one at a time and stays live at its grant"}}
for _r, _v in RULES.items():
    CHANNELS[f"CH-{_r}"] = {"kind": "scale", "rule": _r, "degrade": f"ch_{_r.lower()}", "latent": "member", "family": _v["family"],
                            "source": _v["source"], "members": MEMBERS[_r], "description": _v["natural_reading"]}


def load_state(sql_text, revision=None):
    from base_check import parse_sql
    by_id = {}
    for x in parse_sql(sql_text):
        if x["op"] != "insert":
            continue
        r = x["row"]
        for k in ("id", "identifier", "document_id", "spreadsheet_id", "presentation_id", "event_id"):
            if r.get(k):
                by_id[str(r[k])] = r
    return {"by_id": by_id, "revision": revision or "rev2"}


def _hit(spec, name, key):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and key in d[1]) for d in spec)


def _off(rule, key, disable, degrade):
    return _hit(disable, rule, key) or (key in MEMBERS[rule] and _hit(degrade, f"ch_{rule.lower()}", key))


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    b = state["by_id"]
    have = lambda i: i in b                     # noqa: E731
    notes = have(R_NOTES)
    kpmg = have(R_KPMG) and "December 31, 2025" in str(b[R_KPMG].get("body_text") or "")
    robert = have(R_ROBERT) and "closing" in str(b[R_ROBERT].get("body_text") or "")
    family = have(R_FAMILY) and "for a family" in str(b[R_FAMILY].get("text") or "")

    def title(k, name):
        return str(b[k].get("title")) if have(k) else name

    def option_now(o, live):
        return o[4] if live else 0

    def as_of(o, on, live):
        if not on:
            return option_now(o, live)
        if o[6] <= AS_OF:
            return 0
        return o[3] if o[5] > AS_OF else o[4]

    def last_of(o, key):
        k = o[0]
        if k in EXT_LAST and have(R_EXT) and not _off("EXT", key, disable, degrade):
            return EXT_LAST[k]
        if k == "ENG-2454" and key == k and have(R_EXT) and _hit(degrade, "ext_over", k):
            return EXT_LAST["ENG-2452"]
        return o[6]

    out = {}
    for s in STOCK:
        k, name, cid, listed, adv, told, how = s
        if keys_ is not None and k not in keys_:
            continue
        adv_on = not _off("ADV", k, disable, degrade)
        shares = listed - adv if adv_on else listed
        if k in TOLD_ELSEWHERE:
            told = (notes and not _off("TOLD", k, disable, degrade)) and (k != "ENG-2446" or robert)
        if k == "ENG-2448" and _hit(degrade, "told_over", k):
            told = True
        if k == "ENG-2447" and have(R_AKIN) and not _off("ALIAS", k, disable, degrade):
            told = True
        if k == "ENG-2449" and have(R_AKIN) and _hit(degrade, "alias_over", k):
            told = True
        owed = "Already told" if told else "First note"
        if k in FAMILY_COVERED and family and not _off("FAM", k, disable, degrade):
            owed = "Covered"
        if k == "ENG-2442" and _hit(degrade, "fam_over", k):
            owed = "Covered"
        if k in ("ENG-2441", "ENG-2442") and _hit(degrade, "adv_over", k):
            shares -= 6104
        grant = adv if adv_on else 0
        ev = {"Issue": [k] if have(k) else [], "Holder": [k] if have(k) else []}
        out[k] = {"Issue": k, "Holder": title(k, name), "Instrument": "Series Seed and advisor options" if grant else "Series Seed",
                  "Shares held now": shares, "Last day": None, "Told": "Yes" if told else "No", "Owed": owed,
                  "State": "Todo" if owed == "First note" else "Done", "Options now": grant, "Options at Dec 31": grant,
                  "Open question": None, "groups": ["stock"], "evidence": ev}
    for o in OPTION:
        k, name, cid, granted, vested, eff, last, letter = o
        if keys_ is not None and k not in keys_:
            continue
        last = last_of(o, k)
        misread = k in CHANNELS["CH-LIVE"]["members"] and _hit(degrade, "live_miss", k) and last < CLOCK
        live = last >= CLOCK or misread
        told = letter
        if k in NO_LETTER and (not notes or _off("LETTER", k, disable, degrade)):
            told = True
        if k in ("ENG-2450", "ENG-2460") and _hit(degrade, "letter_over", k):
            told = False
        if k in BOUNCED and have(R_BOUNCE) and not _off("BOUNCE", k, disable, degrade):
            told = False
        if k == "ENG-2456" and have(R_BOUNCE) and _hit(degrade, "bounce_over", k):
            told = False
        owed = "Nothing"
        if live:
            owed = "Date note" if told else "Full note"
        ask = "equity" if k == "ENG-2453" and notes and not _off("ASK", k, disable, degrade) else None
        if k == "ENG-2461" and _hit(degrade, "ask_over", k):
            ask, owed = "exercise", "Date note"
        at = as_of(o[:6] + (last,) + o[7:], kpmg and not _off("ASOF", k, disable, degrade), last >= CLOCK)
        if k == "ENG-2455" and _hit(degrade, "asof_over", k):
            at = vested
        held = (granted if misread else vested) if live else 0
        ev = {"Issue": [k] if have(k) else [], "Holder": [k] if have(k) else []}
        out[k] = {"Issue": k, "Holder": title(k, name), "Instrument": "Option", "Shares held now": 0,
                  "Last day": last if live else None, "Told": ("Yes" if told else "No") if live else None, "Owed": owed,
                  "State": "Canceled" if owed == "Nothing" else "Todo",
                  "Options now": held, "Options at Dec 31": at, "Open question": ask, "groups": ["option"], "evidence": ev}
    if keys_ is None or "SUMMARY" in keys_:
        k = "SUMMARY"
        adv_on = not _off("ADV", k, disable, degrade)
        asof_on = kpmg and not _off("ASOF", k, disable, degrade)
        grants = sum(s[4] for s in STOCK)
        seed = sum(s[3] - s[4] if adv_on else s[3] for s in STOCK)
        lasts = {o[0]: last_of(o, k) for o in OPTION}
        now = sum(o[4] for o in OPTION if lasts[o[0]] >= CLOCK) + (grants if adv_on else 0)
        at = sum(as_of(o[:6] + (lasts[o[0]],) + o[7:], asof_on, lasts[o[0]] >= CLOCK) for o in OPTION) + (grants if adv_on else 0)
        directors = "Leonard Hayes, Robert"
        if _off("BOARD", k, disable, degrade) or not have(R_BOARD):
            directors = "Leonard Hayes, Robert, Matthew Collins, Griffin's director"
        if _hit(degrade, "board_over", k):
            directors = "Leonard Hayes"
        griffin = STOCK[0][3] + STOCK[1][3]
        out[k] = {"Issue": k, "Common": COMMON, "Series Seed total": seed, "Options outstanding now": now,
                  "Options outstanding at Dec 31": at, "Issued plus options at Dec 31": COMMON + seed + at, "Directors": directors,
                  "Griffin share of preferred": f"{100 * griffin / seed:.1f}%", "Owed": None, "groups": [], "evidence": {}}
    return out


def aggregates(rows):
    listed = {k: v for k, v in rows.items() if k != "SUMMARY"}
    classes = collections.Counter(v["Owed"] for v in listed.values())
    states = collections.Counter(v["State"] for v in listed.values())
    groups = collections.defaultdict(list)
    for k in sorted(listed):
        for g in listed[k]["groups"]:
            groups[g].append(k)
    notes = sum(classes.get(c, 0) for c in ("First note", "Date note", "Full note"))
    first = sorted((v["Last day"], k) for k, v in listed.items() if v["Last day"] and v["Told"] == "No")
    return {"classes": dict(sorted(classes.items())), "states": dict(sorted(states.items())), "notes": notes,
            "reason_comments": len(listed) - notes,
            "first_to_go": first[0][1] if first else None, "groups": {g: groups[g] for g in sorted(groups)},
            "summary": {f: v for f, v in rows.get("SUMMARY", {}).items() if f not in ("Issue", "Owed", "groups", "evidence")}}


def evidence(rows, key, field):
    return list((rows[key].get("evidence") or {}).get(field, []))


def touched(state, rule):
    return set(MEMBERS[rule])


def deciding(state, rule, key):
    seeded = {"LETTER": [R_NOTES], "TOLD": [R_NOTES, R_ROBERT] if key == "ENG-2446" else [R_NOTES], "ASOF": [R_KPMG], "BOARD": [R_BOARD],
              "FAM": [R_FAMILY], "ASK": [R_NOTES], "BOUNCE": [R_BOUNCE], "EXT": [R_EXT], "ALIAS": [R_AKIN]}
    return [i for i in seeded.get(rule, []) if i in state["by_id"]]


def base_route(record_id):
    return None
