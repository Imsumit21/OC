#!/usr/bin/env python3
"""Scenario builder (design stage) for Frederick Stone · Q4 vendor and partner commitments.

Writes Working_Files/01_Hardness_Manifest.draft.json, Working_Files/01_Gradable_Surface.json and
Working_Files/plan/ids.json + plan/tables/*.md (tables pasted into 01_Scenario_Design.md).
Design only: the seeded texts quoted here are the planned wording /create-injection must use verbatim.
Ids are minted deterministically (sha256 of a label) and checked against the base by plan/check_ids.py.
"""
import hashlib, json, os
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
CTX = json.load(open(os.path.join(WF, "00_Task_Context.json")))
FRED = "frederick.stone@harmonygames.co"
SALT = "hg-fred-q4-commitments|"


def hx(label, n):
    return hashlib.sha256((SALT + label).encode()).hexdigest()[:n]


def ts(iso):
    return int(datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp())


def drive(label, folder=False):
    return ("d_" if folder else "f_") + hx(label, 22)


def evt(label):
    return "evt_" + hx(label, 22)


def trello(label, iso):
    return "%08x" % ts(iso) + hx(label, 16)


def contact(label):
    return hx(label, 24)


def thread(label, iso):
    ms = ts(iso) * 1000
    return str((ms << 20) + (int(hx(label, 8), 16) & 0xFFFFF))


def slack_ts(label, iso):
    return f"{ts(iso)}.{int(hx(label, 8), 16) % 1000000:06d}"


def gm(tid):
    return f"{FRED}/{tid}"


# ---------------------------------------------------------------- planned base-anchored and seeded records
EXEC = "C07C2866011"          # #executives (YES)
DM = "D05S58U4SAK"            # Fred-Leonard DM (YES)
ZM3D = "C0880U9751A"          # #zombie-match3d (YES)
BOARD = "640643a3fd8f3ca308d9318e"   # founders' Trello board "Harmony Games"
TODO_LIST = "640643a3fd8f3ca308d93195"
BASE = {
    "rayking_thread": gm("1842348778705877030"),          # Fwd: Chinese Local Game publishing (Sep 4): boundary, never reached Rayking
    "balancy_thread": gm("1840501641217286806"),          # Leonard: priorities shifted, circle back (Sep 11)
    "google_thread": gm("1817715521687421486"),           # Google partner check-in (ad network: excluded)
    "playable_factory_thread": gm("1843000993076735547"),  # cold pitch, unanswered (excluded)
    "gamesforum_thread": gm("1842890197572292911"),        # speaker invite, unanswered (excluded)
    "nintendo_ndareq": gm("1842358947604469113"),         # Global ToS & NDA Acceptance Required (Sep 4)
    "nintendo_regdone": gm("1842359398719557772"),        # Registration Completed (Sep 4)
    "singular_renewal": gm("1837914783244638008"),        # Jul 17 payment-plan request (SC-39, excluded)
    "esg_engagement": gm("1841636073974841484"),          # ESG Law engagement (Aug 27)
    "ncsoft_report": gm("1842898562278009736"),           # NCsoft meeting report (strategic, excluded)
    "interco_thread": gm("1841620870486605150"),          # cold "call with Zynga?" pitch (excluded)
    "dentsu_thread": gm("1843473831194478743"),           # Griffin AGM || Dentsu (investor, excluded)
    "fred_nintendo_post": f"{EXEC}/1757011358.730529",     # "I registered an account for harmonygames."
    "fred_switch_steps": f"{EXEC}/1757011319.449149",      # Switch publishing steps
    "mattel_rfp_post": f"{EXEC}/1756832039.396149",        # Mattel RFP (Leonard keeps it: excluded)
    "two_buckets": f"{EXEC}/1757961037.465799",            # Fred's Sep 15 UA buckets framing (decoy scope)
    "playtestcloud_root": f"{EXEC}/1758513190.847889",     # Leonard, Sep 22: Playtestcloud results (root CORR hides under)
    "browserstack_card": "688c4fa78031638f0804a994",       # base card "cancel browsestack if not used" (H3 decoy)
    "fred_root": "d_175c0d7bc72ed244b944cb",
    "dm_localization_root": f"{DM}/1758151772.570449",  # Leonard, Sep 17: "we have no localization though" (rev4 COMPL root)
    "july_board_doc": "f_af99b76ff4da59a710edba",
}

T = {   # seeded timestamps (UTC), all before the seed bound 2025-10-01T00:00:00Z
    "july_sign_note": "2025-07-22T18:10:00Z",
    "keep_card": "2025-08-12T16:05:00Z",
    "ua_buckets_doc": "2025-09-16T17:00:00Z",
    "esg_note": "2025-09-24T20:05:00Z",
    "esg_ack": "2025-09-25T16:30:00Z",
    "esg_checklist": "2025-09-24T19:40:00Z",
    "zom567": "2025-09-23T17:00:00Z",
    "zom567_cmt": "2025-09-25T18:20:00Z",
    "framewell_quote": "2025-09-18T16:00:00Z",
    "framewell_waiver": "2025-09-26T21:02:00Z",
    "lanternfly_proposal": "2025-09-09T15:30:00Z",
    "lanternfly_reply": "2025-09-10T17:05:00Z",
    "lanternfly_followup": "2025-09-22T08:40:00Z",
    "lanternfly_dm": "2025-09-29T19:31:00Z",
    "pingwise_notice": "2025-09-24T15:00:00Z",
    "clipforge_welcome": "2025-07-08T18:00:00Z",
    "clipforge_kickoff": "2025-07-14T16:00:00Z",
    "clipforge_notice": "2025-09-12T14:10:00Z",
    "pixel_quote": "2025-06-18T17:30:00Z",
    "robert_cancel_all": "2025-09-25T17:04:00Z",
    "guardrails": "2025-09-26T16:00:00Z",
    "amendment": "2025-09-29T17:15:00Z",
    "review_event": "2025-09-29T18:00:00Z",
    "folder": "2025-09-29T20:00:00Z",
    "readme": "2025-09-30T22:40:00Z",
    "template": "2025-09-30T22:45:00Z",
    "hub": "2025-09-30T23:20:00Z",
    "tracker": "2025-07-31T21:00:00Z",
    "nova_withdraw": "2025-09-23T16:00:00Z",
    "spotlight_call": "2025-09-17T18:00:00Z",
    "motive_decline": "2025-09-19T17:45:00Z",
    "spotlight_note": "2025-09-17T18:41:00Z",   # Robert's #executives note (rev4: no company name)
    "hootline_signup": "2025-08-05T16:00:00Z",
    "hootline_ask": "2025-08-12T16:30:00Z",     # rev4: moved from Sep 24 to before mid-August (WIN)
}

IDS = {
    "hub_thread": gm(thread("hub", T["hub"])),
    "esg_thread": gm(thread("esg_note", T["esg_note"])),
    "guardrails_doc": drive("guardrails"),
    "ua_buckets_doc": drive("ua_buckets"),
    "esg_checklist_doc": drive("esg_checklist"),
    "readme_doc": drive("readme"),
    "template_sheet": drive("template_sheet"),
    "tracker_sheet": drive("july_tracker"),
    "q4_folder": drive("q4_folder", folder=True),
    "keep_card": trello("keep_card", T["keep_card"]),
    "review_event": evt("review_event"),
    "clipforge_kickoff": evt("clipforge_kickoff"),
    "spotlight_call": evt("spotlight_call"),
    "esg_intake_contact": contact("esg_intake"),
    "july_sign_note": f"{EXEC}/{slack_ts('july_sign_note', T['july_sign_note'])}",
    "robert_cancel_all": f"{EXEC}/{slack_ts('robert_cancel_all', T['robert_cancel_all'])}",
    "amendment_root": f"{EXEC}/{slack_ts('amendment', T['amendment'])}",
    "framewell_waiver_reply": f"{EXEC}/{slack_ts('framewell_waiver', T['framewell_waiver'])}",
    "lanternfly_dm": f"{DM}/{slack_ts('lanternfly_dm', T['lanternfly_dm'])}",
    "zom567": "ZOM-567",
    "zom567_cmt": "cmt_" + hx("zom567_cmt", 20),
    "lanternfly_thread": gm(thread("lanternfly", T["lanternfly_proposal"])),
    "lanternfly_deck": drive("lanternfly_deck"),
    "framewell_thread": gm(thread("framewell", T["framewell_quote"])),
    "pingwise_thread": gm(thread("pingwise", T["pingwise_notice"])),
    "clipforge_thread": gm(thread("clipforge", T["clipforge_welcome"])),
    "clipforge_notice_thread": gm(thread("clipforge_notice", T["clipforge_notice"])),
    "pixel_thread": gm(thread("pixel", T["pixel_quote"])),
    "nova_thread": gm(thread("nova", "2025-09-03T15:00:00Z")),
    "motive_thread": gm(thread("motive", "2025-09-15T16:00:00Z")),
    "spotlight_thread": gm(thread("spotlight", "2025-09-08T16:00:00Z")),
    "spotlight_note": f"{EXEC}/{slack_ts('spotlight_note', T['spotlight_note'])}",
    "hootline_thread": gm("1839631800730308867"),
}

# ---------------------------------------------------------------- the cohort (46 candidates; 36 in scope)
# decision: Answered / End / Keep / Sign / Park (the guardrails' closed set); out = off the log by the hub's scope rule
M = []


def member(key, decision, kind, paper, person, first_at, deciding, writes, role="control", channel=None, cost=None,
           next_date=None, answered_by=None, counsel=False, base=False, out_reason=None):
    M.append(dict(key=key, decision=decision, kind=kind, paper=paper, person=person, first_at=first_at,
                  deciding=deciding, writes=writes, role=role, channel=channel, cost=cost, next_date=next_date,
                  answered_by=answered_by, counsel=counsel, base=base, out_reason=out_reason))


R, RV, C, K, S, E = "reply", "revisit", "contact", "card", "esg", "cancel"
# --- traps
member("Nintendo", "Sign", "platform developer terms", None, None, "2025-09-04",
       "registration completed (base Sep 4) but Arthur's ZOM-567 comment (Sep 25): org account limited until an officer "
       "accepts the Global ToS and NDA (the request lapses Oct 15); ESG: only Leonard or Arthur accept terms", [K], role="trap",
       channel="DONE", next_date="2025-10-15", base=True)
member("Framewell", "Park", "creative asset subscription", "gdocs", ("Maren", "Holt", "maren@framewell.io"),
       T["framewell_quote"], "order form: Pro plan billed from Nov 1 at $149/month; Leonard's Sep 26 thread reply under "
       "the Playtestcloud post (rev4: names Maren and the Pro plan, not Framewell): no charge until Feb 1 -> nothing before January",
       [R, RV, C], role="trap", channel="CORR", next_date="2026-01-05")
member("Lanternfly Publishing", "Answered", "Southeast Asia publishing proposal", "gslides", ("Wen", "Halvorsen", "wen@lanternfly.games"),
       T["lanternfly_proposal"], "Frederick replied Sep 10 ('thanks, we'll take a look'); Lanternfly's Sep 22 'any news?' sits unanswered "
       "in the thread; Leonard's Sep 29 reply in the DM thread under his Sep 17 'we have no localization though' (rev4: names Wen "
       "and the Southeast Asia deal, not Lanternfly): he rang Wen back on Saturday, Southeast Asia waits until after the raise, talk again in January", [RV, C], role="trap", channel="COMPL", answered_by="Leonard", next_date="2026-01-05")
member("Pingwise", "Keep", "uptime monitoring and on-call paging", "gdocs", ("Dana", "Whitfield", "dana@pingwise.io"),
       T["pingwise_notice"], "free tier ends Oct 31, Team $29/month from Nov 1 (cash in window); Arthur's keep-running "
       "list names 'the night pager for backend outages' -> Pingwise's on-call paging -> Keep", [R, C], role="trap",
       channel="EXC", cost="$29/month from Nov 1", next_date="2025-11-01")
member("Clipforge", "End", "UGC video ad pilot", "gdocs", ("Priya", "Raman", "priya@clipforge.co"),
       T["clipforge_welcome"], "pilot agreement (Jul 14): free through Jan 15, 2026; processor notice (Sep 12) for "
       "workspace HG-2291 'UGC Studio': pilot cap reached, pilot ends Oct 15, $1,800/month from Oct 16 unless cancelled "
       "in writing to the address in the notice -> End, cancel by Oct 15", [E, C], role="trap", channel="DATE",
       cost="$1,800/month from Oct 16", next_date="2025-10-15")
member("Pixel Harbor Events", "End", "booth at the Oct 24 indie showcase", "gdocs",
       ("Teodor", "Lind", "teodor@pixelharbor.events"), T["pixel_quote"], "June 18 quote (outside the September window): "
       "booth hold needs a $2,400 deposit by Oct 10 -> cash in window -> End", [R, C], role="trap", channel="FILT",
       cost="$2,400 deposit by Oct 10", next_date="2025-10-10")
# --- End controls
for k, kind, nm, cost, nd in [
        ("Brightlane Studio", "creative agency retainer", ("Ines", "Varga", "ines@brightlane.studio"), "$3,500/month from Oct 1", "2025-10-01"),
        ("Soundvault", "music licence (annual)", ("Rafael", "Moreno", "rafael@soundvault.fm"), "$1,188 prepaid on signature; quote valid to Oct 15", "2025-10-15"),
        ("Reviewly", "store-review management trial", ("Hana", "Kobayashi", "hana@reviewly.app"), "trial converts Oct 20 at $79/month", "2025-10-19"),
        ("Streamcast Talent", "influencer campaign", ("Kofi", "Mensah", "kofi@streamcast.tv"), "50% deposit on booking for a November campaign", "2025-10-31"),
        ("Lingora", "store-listing localization sprint", ("Elena", "Petrova", "elena@lingora.com"), "$2,640 invoiced on delivery; quote valid until Oct 3", "2025-10-03"),
        ("Panelpulse", "player research panel", ("Arjun", "Shah", "arjun@panelpulse.io"), "$1,200 prepaid for an Oct 14 panel; confirm by Oct 6", "2025-10-06"),
        ("Ascendo", "ASO agency retainer", ("Lucia", "Ferrer", "lucia@ascendo.agency"), "$900/month from Oct 1", "2025-10-01"),
        ("Wishwave", "pre-registration push at a partner showcase", ("Sven", "Aalto", "sven@wishwave.gg"), "partner-booked travel for two (counts under the Sep 29 amendment); confirm by Oct 17", "2025-10-17")]:
    member(k, "End", kind, "gdocs", nm, "2025-08-01..2025-09-28", f"paper: {cost}", [R, C], cost=cost, next_date=nd)
# --- Keep controls (named on Arthur's list)
member("Vaultline", "Keep", "nightly database backups", "gdocs", ("Mila", "Novak", "mila@vaultline.io"), "2025-09-22",
       "renews Oct 12 at $19/month; on Arthur's keep-running list by name", [R, C], cost="$19/month", next_date="2025-10-12")
member("Certwell", "Keep", "SSL certificate for the API domain", "gdocs", ("Jonas", "Weber", "jonas@certwell.com"),
       "2025-09-23", "renews Oct 20 at $89/year; on Arthur's keep-running list by name", [R, C], cost="$89/year", next_date="2025-10-20")
# --- Sign controls
member("Kinetic Arcade", "Sign", "publishing LOI (12-month exclusivity)", "gdocs", ("Noor", "Haddad", "noor@kineticarcade.com"),
       "2025-09-10", "free in window; exclusivity -> ESG first; officer signs", [R, K, S], counsel=True, next_date="2025-10-20")
member("Lumencloud", "Sign", "cloud credits programme (36-month term)", "gdocs", ("Aiden", "Clarke", "aiden@lumencloud.dev"),
       "2025-09-11", "free; 36-month term -> ESG first", [R, K, S], counsel=True, next_date="2025-10-31")
member("Bundlehouse", "Sign", "co-marketing bundle (licenses our game IP)", "gslides", ("Freya", "Olsen", "freya@bundlehouse.gg"),
       "2025-09-16", "free; licence of our IP -> ESG first", [R, K, S, C], counsel=True, next_date="2025-11-01")
member("Orbit Store", "Sign", "store featuring agreement", "gdocs", ("Mateo", "Rossi", "mateo@orbitstore.games"),
       "2025-09-19", "free; needs an officer's acceptance", [R, K, C], next_date="2025-10-24")
member("Markward", "Sign", "brand-monitoring free tier (click-through terms)", "gdocs", ("Leah", "Brennan", "leah@markward.io"),
       "2025-09-09", "free; click-through terms = an officer accepts (ESG overrides Leonard's July note)", [R, K])
member("Playfuse", "Sign", "bundle partnership NDA (ESG mutual template)", "gdocs", ("Iris", "Navarro", "iris@playfuse.gg"),
       "2025-09-25", "mutual NDA on ESG's template: an officer signs, no counsel review", [R, K, C], next_date="2025-10-08")
# --- Park controls
for k, kind, nm, why in [
        ("Hootline", "social scheduler", ("Gemma", "Doyle", "gemma@hootline.co"), "promo: free until Jan 31"),
        ("Glyphworks", "font licence quote", ("Tomas", "Novotny", "tomas@glyphworks.type"), "quote valid to Jan 31, nothing owed until ordered"),
        ("Cloudlark", "startup credits offer", ("Yara", "Nasser", "yara@cloudlark.io"), "credits, no term, start any time"),
        ("Echohall", "community platform upgrade proposal", ("Bruno", "Costa", "bruno@echohall.chat"), "free plan continues"),
        ("Pressbeam", "PR distribution package for 2026", ("Ava", "Lindqvist", "ava@pressbeam.news"), "booked later; no travel"),
        ("Retainly", "analytics trial", ("Omar", "Farouk", "omar@retainly.io"), "trial converts Jan 12, 2026 (outside the window)"),
        ("Quillcraft", "AI copywriting tool beta", ("Nadia", "Petrov", "nadia@quillcraft.ai"), "free beta through January"),
        ("Tilecast", "website playable-preview widget", ("Kenji", "Mori", "kenji@tilecast.io"), "free pilot slot in February"),
        ("Benchmarkly", "benchmark report subscription", ("Clara", "Weiss", "clara@benchmarkly.com"), "free sample now, paid from February"),
        ("Loopnote", "meeting-notes tool trial", ("Pavel", "Sokol", "pavel@loopnote.app"), "trial free until Feb 1"),
        ("Driftwood Audio", "voice-over studio quote", ("Sofia", "Marin", "sofia@driftwood.audio"), "quote valid until Feb 28")]:
    member(k, "Park", kind, "gdocs", nm, "2025-08-05..2025-09-27", f"paper: {why}", [R, RV, C], next_date="2026-01-05")
# rev4 (WIN): Hootline moves outside the obvious filter - no filed paper (terms in the mail body) and both messages before mid-August
_h = next(x for x in M if x["key"] == "Hootline")
_h.update(paper=None, first_at=T["hootline_signup"], role="trap", channel="WIN",
          deciding="Frederick signed up Aug 5 (promo keeps the scheduler free until Jan 31, then $39/month); Gemma's Aug 12 question whether "
                   "to keep it after Jan 31 is unanswered; no filed paper and nothing after Aug 12 -> in scope by the hub's undated rule, Park")
# --- Answered controls
member("Balancy", "Answered", "live-ops tool trial", None, ("Balancy", "rep", "PERSON_0527_EMAIL"), "2025-09-11",
       "Leonard answered in-thread on Sep 11 ('company priorities have shifted … we'll circle back') -> later -> revisit",
       [RV, C], answered_by="Leonard", next_date="2026-01-05", base=True)
member("Motive Forge", "Answered", "outsourced art quote", "gdocs", ("Hugo", "Lambert", "hugo@motiveforge.art"), "2025-09-15",
       "Arthur declined in-thread on Sep 19 (cc Frederick)", [C], answered_by="Arthur")
member("Spotlight Fest", "Answered", "showcase slot invitation", "gdocs", ("Rina", "Takeda", "rina@spotlightfest.events"),
       "2025-09-08", "Robert's Sep 17 #executives note (rev4: names the Dec 5 indie showcase and Rina, not Spotlight Fest; the call's "
       "calendar description no longer carries the answer): sitting this one out, he let Rina know", [C],
       role="trap", channel="NOTE", answered_by="Robert")
# --- out of scope (boundary records)
for k, why, base in [("Playable Factory", "cold pitch nobody answered", True), ("Gamesforum SF", "speaker invite nobody answered", True),
                     ("InterCo Digital", "cold pitch nobody answered", True), ("Rayking Game", "cold pitch only forwarded around internally (Frederick's Sep 4 reply went to Leonard)", True),
                     ("Google partner check-in", "ad network: stays on the UA budget call", True), ("Singular", "UA stack, named in the hub's exclusion (SC-39)", True),
                     ("NCsoft", "strategic / investor talks (bridge work)", True), ("Dentsu", "investor (bridge work)", True),
                     ("Mattel", "Leonard keeps it", True), ("Nova Rewards", "offer withdrawn on Sep 23", False)]:
    member(k, "out", "boundary", None, None, None, why, [], role="boundary", base=base, out_reason=why)

IN = [m for m in M if m["decision"] != "out"]
assert len(IN) == 36 and len(M) == 46, (len(IN), len(M))
COUNTS = {d: sum(1 for m in IN if m["decision"] == d) for d in ("Answered", "End", "Keep", "Sign", "Park")}
assert COUNTS == {"Answered": 4, "End": 10, "Keep": 3, "Sign": 7, "Park": 12}, COUNTS
N_REPLY = sum(1 for m in IN if R in m["writes"] or E in m["writes"])
N_REVISIT = sum(1 for m in IN if RV in m["writes"])
N_CARD = sum(1 for m in IN if K in m["writes"])
N_ESG = sum(1 for m in IN if S in m["writes"])
# contacts: every member with a person, minus the three already in Contacts (Kinetic, Lumencloud, Markward)
EXISTING_CONTACTS = {"Kinetic Arcade", "Lumencloud", "Markward"}
N_CONTACT = sum(1 for m in IN if m["person"] and m["key"] not in EXISTING_CONTACTS)
N_PAPER = sum(1 for m in IN if m["paper"])
assert (N_REPLY, N_REVISIT, N_CARD, N_ESG, N_CONTACT) == (31, 14, 7, 3, 32), (N_REPLY, N_REVISIT, N_CARD, N_ESG, N_CONTACT)

# ---------------------------------------------------------------- planned wording (verbatim for /create-injection)
Q = {
    "hub_scope": "anyone outside the investor work who has an offer, a trial, a quote, terms or an ask in front of us and that one of us has actually engaged with",
    "hub_cold": "Cold pitches nobody answered, including ones we only forwarded around internally, stay off it",
    "hub_guardrails": "Go by the runway guardrails doc for what we do with each one",
    "hub_amend": "plus the one change I posted in #executives on Monday",
    "hub_esg": "Anything that needs signing goes the way ESG's note about signing says",
    "hub_answer": "Everyone who is waiting to hear from us should get a written answer this week",
    "hub_contacts": "Get each company's contact into Contacts so we're not digging through mail next time",
    "hub_readme": "the README in the folder has the columns",
    "hub_report": "reply here with what we're keeping and what's waiting on Arthur or me to sign",
    "doc_keep": "anything on Arthur's keep-running list on our board stays",
    "doc_review": "comes back at the January commitments review on our calendars",
    "readme_template": "copy the header row from the template sheet",
    "esg_intake": "our intake address (it's in your Contacts as ESG Law intake)",
    "esg_checklist": "what to include is in the intake checklist I shared",
    "esg_board": "put it on your founders' board To Do list with the company's name in the card title",
    "framewell_waiver_v4": "side note, Maren called me back about the Pro plan. they'll hold it at no charge until Feb 1 with nothing to sign before then, so nothing from them lands before January. treat them like the other free ones",
    "lanternfly_note_v4": "on localization: I rang Wen back on Saturday about their Southeast Asia deal and let them know Southeast Asia has to wait until after the raise. we'll pick it up again in January",
    "spotlight_note_v4": "had the call about the Dec 5 indie showcase. we're sitting this one out this year, I let Rina know",
    "spotlight_desc_v4": "Showcase slot call with Rina.",
    "hootline_ask_v4": "Hi Frederick, now that your profiles are set up, a quick planning question: when the startup promo ends on Jan 31, would you like to keep the scheduler after that? Gemma",
}


def write(path, obj):
    with open(path, "w") as f:
        json.dump(obj, f, indent=1)
        f.write("\n")


# ---------------------------------------------------------------- manifest
ctx = {k: CTX[k] for k in ("context_hash", "assignment_hash", "policy_hash", "freeze_utc", "difficulty_mode")}
REQ = {
    "R1": "log population: every outside company with an offer, a trial, a quote, terms or an ask waiting on us that one of us engaged with (a call, a reply, a sign-up or paper) - 36 companies; cold pitches nobody answered (including ones only forwarded around internally), ad networks and Singular, investors, Mattel and withdrawn offers stay off",
    "R2": "decision per company under the runway guardrails' cash test and park rule (End / Park), with the Sep 29 #executives change that travel and event costs count as cash even when a partner books them",
    "R3": "live-game exemption: anything on Arthur's keep-running list stays (Keep) even when it costs money",
    "R4": "already answered: no second answer; the log records who answered (Answered by) and a revisit when the answer was 'later'",
    "R5": "a written answer to every company waiting to hear from us, on its own thread or to the address its paper or notice names",
    "R6": "signing: only Leonard or Arthur accept terms; anything waiting on a signature gets a founders' board To Do card named for the company; auto-renewal, exclusivity, IP licence or a term over 12 months also goes to ESG's intake address, one email per agreement (Sign)",
    "R7": "revisit reminder on Frederick's calendar on the January commitments review date (Mon Jan 5, 2026) for each parked company and each 'later' answer (Next date)",
    "R8": "a contact for every company's person in Contacts, company in the job field, added only when missing",
    "R9": "the log sheet in Frederick's Q4 commitments folder with the README's columns (Company, Contact, What's waiting, Decision, Answered by, What we told them, Next date)",
    "R10": "reply on Leonard's thread with what we're keeping (Keep) and what's waiting on Arthur or Leonard to sign (Sign)",
}
services = {
    "gmail": {"role": "hub ask and report destination; ESG's signing note and intake emails; every counterparty's offer thread (36 in scope, 10 boundary); Clipforge's processor notice; replies and cancellations", "weight_reason": "the ask, the signing rule, every offer's state and every written answer live in mail"},
    "gdocs": {"role": "runway guardrails doc (H1) and its UA-buckets decoy; the folder README; ESG's intake checklist; 28 counterparties' papers (order forms, terms, quotes)", "weight_reason": "the decision rules and each paper's cost, dates and terms (auto-renewal, exclusivity, IP, term) decide the decision"},
    "gdrive": {"role": "Frederick's Q4 commitments folder (destination, owned by Frederick) holding the README and template; papers shared by counterparties", "weight_reason": "the log must be created in the owned folder"},
    "gsheets": {"role": "log template header row; Frederick's stale July vendor tracker (decoy); the log itself", "weight_reason": "the log is the graded register"},
    "gslides": {"role": "partners' proposal decks as their papers (Lanternfly, Bundlehouse)", "weight_reason": "Bundlehouse's IP-licence term (counsel route) and Lanternfly's proposal live only in the deck"},
    "slack": {"role": "Leonard's Sep 29 #executives amendment; Leonard's Sep 26 thread reply (Framewell waiver, names Maren) under the Sep 22 Playtestcloud root; Leonard's Sep 29 DM thread reply under his Sep 17 localization message (Lanternfly answered, names Wen); Robert's Sep 17 note (Spotlight answered, names the Dec 5 indie showcase); Leonard's July 'sign small stuff' note (superseded); Robert's 'cancel everything' post (non-authoritative); Frederick's Sep 4 Nintendo post (base)", "weight_reason": "Framewell's decision, Lanternfly's answered state and the travel amendment exist only in Slack"},
    "gcal": {"role": "Leonard's Jan 5, 2026 commitments review (revisit date); Clipforge's Jul 14 kickoff; Spotlight's Sep 17 call (no answer in its description); revisit writes", "weight_reason": "the revisit date lives in the calendar; the revisit reminders are writes"},
    "trello": {"role": "Arthur's keep-running list card (H3) on the founders' board; signature cards in To Do (writes); base BrowserStack card (decoy)", "weight_reason": "the Keep exemption is decided by the card's checklist; routed signatures are cards"},
    "contacts": {"role": "ESG Law intake entry (recipient); three counterparties already present; contact writes", "weight_reason": "ESG's intake address and the dedupe check live in Contacts; contacts are writes"},
    "linear": {"role": "ZOM-567 'Switch dev kit' and Arthur's Sep 25 comment (the Nintendo done-gap)", "weight_reason": "the missing piece of Nintendo's 'done' lives only in the Linear comment"},
}
anchors = [
    {"id": "A1", "service": "gmail", "record": IDS["hub_thread"], "locator": IDS["hub_thread"], "prompt_reference": "Leonard's vendor and partner email", "requirement_ids": ["R1", "R5", "R10"]},
    {"id": "A2", "service": "gdrive", "record": IDS["q4_folder"], "locator": IDS["q4_folder"], "prompt_reference": "my Q4 commitments folder", "requirement_ids": ["R9"]},
]


def frag(fid, service, container, kind, via, seeded, by, quote, reqs, names=None, base=None):
    return {"id": fid, "service": service, "container": container, "locator": container, "kind": kind,
            "incorporated_via": via, "seeded_ids": seeded, "base_pointers": base or [], "delegated_by_record": by,
            "delegation_quote": quote, "requirement_ids": reqs, "names_authorities": names or []}


H = IDS
fragments = [
    frag("K1", "gmail", H["hub_thread"], "requirement", ["A1"], [H["hub_thread"]], H["hub_thread"], Q["hub_scope"], ["R1", "R5", "R8", "R10"],
         [{"id": "H1", "quote": "the runway guardrails doc"}, {"id": "H2", "quote": "ESG's note about signing"}]),
    frag("K2", "gdocs", H["guardrails_doc"], "delegation", ["A1", "K1"], [H["guardrails_doc"]], H["hub_thread"], Q["hub_guardrails"], ["R2"]),
    frag("K3", "gdocs", H["guardrails_doc"], "requirement", ["A1", "K1"], [H["guardrails_doc"]], H["hub_thread"], Q["hub_guardrails"], ["R4"]),
    frag("K4", "gdocs", H["guardrails_doc"], "requirement", ["A1", "K1"], [H["guardrails_doc"]], H["hub_thread"], Q["hub_guardrails"], ["R3"],
         [{"id": "H3", "quote": "Arthur's keep-running list on our board"}]),
    frag("K5", "gmail", H["esg_thread"], "requirement", ["A1", "K1"], [H["esg_thread"]], H["hub_thread"], Q["hub_esg"], ["R6"]),
    frag("K6", "trello", H["keep_card"], "requirement", ["A1", "K1", "K4"], [H["keep_card"]], H["guardrails_doc"], Q["doc_keep"], ["R3"]),
    frag("K7", "gcal", H["review_event"], "amendment", ["A1", "K1", "K2"], [H["review_event"]], H["guardrails_doc"], Q["doc_review"], ["R7"]),
    frag("K8", "gdocs", H["readme_doc"], "format", ["A1", "K1"], [H["readme_doc"]], H["hub_thread"], Q["hub_readme"], ["R9", "R8"]),
    frag("K9", "gsheets", H["template_sheet"], "format", ["A1", "K1", "K8"], [H["template_sheet"]], H["readme_doc"], Q["readme_template"], ["R9"]),
    frag("K10", "slack", H["amendment_root"], "amendment", ["A1", "K1"], [H["amendment_root"]], H["hub_thread"], Q["hub_amend"], ["R2"]),
    frag("K11", "contacts", H["esg_intake_contact"], "recipient", ["A1", "K1", "K5"], [H["esg_intake_contact"]], H["esg_thread"], Q["esg_intake"], ["R6"]),
    frag("K12", "gdocs", H["esg_checklist_doc"], "format", ["A1", "K1", "K5"], [H["esg_checklist_doc"]], H["esg_thread"], Q["esg_checklist"], ["R6"]),
    frag("K13", "gmail", H["hub_thread"], "destination", ["A1"], [H["hub_thread"]], H["hub_thread"], Q["hub_report"], ["R10"]),
    frag("K14", "gmail", H["hub_thread"], "requirement", ["A1"], [H["hub_thread"]], H["hub_thread"], Q["hub_answer"], ["R5"]),
]
authorities = [
    {"id": "H1", "name": "the runway guardrails doc", "home_service": "gdocs", "decoy_service": "gdocs", "governs": ["R2", "R4", "R7"],
     "findable_query": "runway guardrails", "seeded_ids": [H["guardrails_doc"]], "base_pointers": [],
     "decoy_seeded_ids": [H["ua_buckets_doc"]], "decoy_base_pointers": [BASE["two_buckets"]],
     "decoy_scope": {"dimension": "team", "decoy": "UA ad-network spend (fundraising bucket vs real UA bucket, Sep 15-16)", "task": "vendor and partner commitments outside UA"}},
    {"id": "H2", "name": "ESG's note about signing", "home_service": "gmail", "decoy_service": "slack", "governs": ["R6"],
     "findable_query": "ESG signing", "seeded_ids": [H["esg_thread"]], "base_pointers": [], "decoy_seeded_ids": [H["july_sign_note"]],
     "decoy_base_pointers": []},
    {"id": "H3", "name": "Arthur's keep-running list", "home_service": "trello", "decoy_service": "trello", "governs": ["R3"],
     "findable_query": "keep-running", "seeded_ids": [H["keep_card"]], "base_pointers": [], "decoy_seeded_ids": [],
     "decoy_base_pointers": [f"trello:{BASE['browserstack_card']}"],
     "decoy_scope": {"dimension": "team", "decoy": "tools Leonard cancelled in his August cleanup", "task": "what the live game needs to keep running"}},
]
surfaces = [
    {"service": "gmail", "tool": "gmail_search_messages+gmail_get_thread", "per_record_calls": 0.5, "records": 46, "requirement": "R1",
     "decides": "every outside company with an offer, a trial, a quote, terms or an ask waiting on us",
     "why_no_bulk": "gmail_search returns ids only; gmail_get_messages_batch reads bodies in bulk, so only half a call per company is counted",
     "short_circuit": "whether a company is in scope (engaged, not cold, not withdrawn) and what it is waiting on is only in its own thread; no list names the 36"},
    {"service": "gdocs", "tool": "gdocs_get_document / gslides_get_presentation", "per_record_calls": 1.0, "records": 32, "requirement": "R2", "seeded": True,
     "decides": "decision per company", "why_no_bulk": "each paper is its own document; no call returns the body of more than one document",
     "short_circuit": "cost, conversion dates and terms (auto-renewal, exclusivity, IP, term length) decide 13 of 32 papers and the mail never states them, so every paper must be read"},
    {"service": "contacts", "tool": "contacts_search_contacts", "per_record_calls": 1.0, "records": 35, "requirement": "R8",
     "decides": "a contact for every company's person in Contacts, company in the job field, added only when missing",
     "why_no_bulk": "three counterparties already have contacts; a per-company lookup is the dedupe check before each add (contacts_get_contacts pages 170+ internal entries)",
     "short_circuit": "adding without the lookup duplicates Kinetic Arcade, Lumencloud and Markward"},
    {"service": "gcal", "tool": "gcal_list_events (Jun-Jan window)", "per_record_calls": 0.2, "records": 46, "requirement": "R4",
     "decides": "already answered: no second answer; the log records who answered (Answered by)",
     "why_no_bulk": "one listing covers many companies (counted at 0.2 per company)", "short_circuit": "Clipforge's workspace id appears only on its kickoff call and paper; Spotlight's call is the only calendar trace of its answer, which is in Robert's note"},
]
cohort = {"definition": "every outside company with an offer, trial, quote, terms or ask to HG in Frederick's view since June 2025 (46 looked at); 36 pass the hub's scope rule",
          "definition_source": [H["hub_thread"], H["guardrails_doc"]], "key": "company", "size": 46, "evidence_surfaces": surfaces}

chains = [
    {"id": "C1", "root_cause": "A24", "ends_in": "R6", "hops": [
        {"service": "gmail", "record": BASE["nintendo_regdone"], "finding": "Nintendo Developer Portal: Registration Completed (Sep 4)"},
        {"service": "slack", "record": BASE["fred_nintendo_post"], "finding": "Frederick: I registered an account for harmonygames"},
        {"service": "linear", "record": "ZOM-567", "finding": "Arthur, Sep 25 comment: org account limited until an officer accepts the Global ToS and NDA"},
        {"service": "gmail", "record": H["esg_thread"], "finding": "ESG: only Leonard or Arthur accept terms; waiting on a signature -> founders' board card"}]},
    {"id": "C2", "root_cause": "A11", "ends_in": "R7", "hops": [
        {"service": "gmail", "record": H["framewell_thread"], "finding": "Framewell: Pro plan from Nov 1 at $149/month"},
        {"service": "gdocs", "record": "framewell order form", "finding": "billing starts Nov 1 (cash in window)"},
        {"service": "slack", "record": H["framewell_waiver_reply"], "finding": "Leonard (thread reply under the Sep 22 Playtestcloud post): no charge until Feb 1"},
        {"service": "gcal", "record": H["review_event"], "finding": "parked -> revisit at the Jan 5 review"}]},
    {"id": "C3", "root_cause": "A25", "ends_in": "R4", "hops": [
        {"service": "gmail", "record": H["lanternfly_thread"], "finding": "Lanternfly proposal (Sep 9); Frederick: 'we'll take a look' (Sep 10); Sep 22 'any news?' unanswered in the thread"},
        {"service": "gslides", "record": H["lanternfly_deck"], "finding": "Southeast Asia publishing proposal deck"},
        {"service": "slack", "record": BASE["dm_localization_root"], "finding": "Leonard (DM root, Sep 17): 'we have no localization though'"},
        {"service": "slack", "record": H["lanternfly_dm"], "finding": "Leonard (DM thread reply, Sep 29): rang Wen back Saturday, Southeast Asia waits until after the raise, talk in January"}]},
    {"id": "C4", "root_cause": "A15", "ends_in": "R3", "hops": [
        {"service": "gmail", "record": H["pingwise_thread"], "finding": "free tier ends Oct 31; Team $29/month from Nov 1 unless you downgrade"},
        {"service": "gdocs", "record": "pingwise terms", "finding": "uptime monitoring and on-call paging for the backend endpoints"},
        {"service": "gdocs", "record": H["guardrails_doc"], "finding": "exemption: anything on Arthur's keep-running list stays"},
        {"service": "trello", "record": H["keep_card"], "finding": "checklist item 'the night pager for backend outages'"}]},
    {"id": "C5", "root_cause": "A4", "ends_in": "R2", "hops": [
        {"service": "gdocs", "record": "clipforge pilot agreement", "finding": "pilot free through Jan 15, 2026; workspace HG-2291"},
        {"service": "gmail", "record": H["clipforge_notice_thread"], "finding": "processor notice for workspace HG-2291: pilot ends Oct 15, $1,800/month from Oct 16"},
        {"service": "gcal", "record": H["clipforge_kickoff"], "finding": "Jul 14 kickoff (UGC Studio) ties the workspace to Clipforge"}]},
    {"id": "C6", "root_cause": "A17", "ends_in": "R1", "hops": [
        {"service": "gmail", "record": H["pixel_thread"], "finding": "June 18 quote: booth hold needs a $2,400 deposit by Oct 10"},
        {"service": "gdocs", "record": "pixel harbor quote", "finding": "deposit terms; showcase Oct 24"},
        {"service": "gmail", "record": H["hub_thread"], "finding": "scope: anyone with an offer in front of us that one of us engaged with (no date limit)"}]},
    {"id": "C7", "root_cause": "A17", "ends_in": "R1", "hops": [
        {"service": "gmail", "record": H["hootline_thread"], "finding": "Aug 5 sign-up (free until Jan 31) and Gemma's Aug 12 'keep it after Jan 31?', nothing later, no filed paper"},
        {"service": "gmail", "record": H["hub_thread"], "finding": "scope: an offer in front of us that one of us engaged with (a sign-up), no date limit"},
        {"service": "gcal", "record": H["review_event"], "finding": "parked -> revisit at the Jan 5 review"}]},
    {"id": "C8", "root_cause": "A25", "ends_in": "R4", "hops": [
        {"service": "gmail", "record": H["spotlight_thread"], "finding": "Rina's Sep 8 invitation: Dec 5 indie showcase, $750 stand fee, 'could we set up a call?'"},
        {"service": "gcal", "record": H["spotlight_call"], "finding": "Sep 17 showcase call, Robert organizer (no answer in the description)"},
        {"service": "slack", "record": H["spotlight_note"], "finding": "Robert (Sep 17, #executives): sitting the Dec 5 indie showcase out, let Rina know"}]},
]


def trap(tid, family, services_, seeded, base, req, wrong, resolver, order=None, versions=None, dtype=None):
    t = {"id": tid, "family": family, "services": services_, "seeded_ids": seeded, "base_pointers": base, "requirement": req,
         "expected_wrong_reading": wrong, "resolver": resolver}
    if dtype:
        t["distractor_type"] = dtype
    if order:
        t["discovery_order"] = order
    if versions:
        t["version_records"] = versions
    return t


traps = [
    trap("T1", "done_gap", ["gmail", "slack", "linear", "trello"], ["ZOM-567", H["zom567_cmt"]], [BASE["nintendo_regdone"], BASE["fred_nintendo_post"]], "R6",
         "Nintendo is done: Frederick registered and the portal sent Registration Completed, so nothing is waiting",
         "Arthur's Sep 25 comment on ZOM-567: the org account stays limited until an officer accepts the Global ToS and NDA; with ESG's rule it is Sign with a founders' board card",
         order="the two Sep 4 portal mails and Frederick's #executives post come back from any Nintendo search; the comment needs linear_list_comments on ZOM-567"),
    trap("T2", "superseding", ["gmail", "gdocs", "slack"], [H["framewell_thread"], H["framewell_waiver_reply"]], [BASE["playtestcloud_root"]], "R2",
         "Framewell is paid from Nov 1, so it fails the cash test: End with a cancellation",
         "Leonard's Sep 26 reply under his Sep 22 Playtestcloud post: Maren (Framewell's account manager on the order-form mail) holds the Pro plan at no charge until Feb 1 -> free until January -> Park, revisit Jan 5",
         order="the quote thread and order form are read first; the reply sits under a root about another vendor, #executives history shows roots only, and the reply names neither Framewell nor 'vendor', so a company-name search misses it (rev3 pre-check found it by 'Framewell', event 444)",
         versions=[{"service": "gmail", "id": H["framewell_thread"], "seeded": True, "at": T["framewell_quote"], "container": f"gmail:{H['framewell_thread'].split('/')[1]}"},
                   {"service": "slack", "id": H["framewell_waiver_reply"], "seeded": True, "at": T["framewell_waiver"], "container": f"slack:{EXEC}/1758513190.847889"}]),
    trap("T3", "completion_elsewhere", ["gmail", "gslides", "slack"], [H["lanternfly_thread"], H["lanternfly_dm"]], [BASE["dm_localization_root"]], "R4",
         "Lanternfly's Sep 22 follow-up is unanswered, so it gets a Park reply",
         "Leonard's Sep 29 reply in the DM thread under his Sep 17 localization message: he rang Wen back (Southeast Asia waits until after the raise, talk in January) -> Answered by Leonard, revisit Jan 5, no second answer",
         order="the thread with the unanswered follow-up is the natural read; the answer is a thread reply in the 1:1 DM (history shows roots only) naming Wen and the Southeast Asia deal, so neither a 'Lanternfly' nor a 'told' search returns it (rev3 found the DM root at events 387, 426, 428)"),
    trap("T4", "authority", ["gmail", "gdocs", "trello"], [H["pingwise_thread"], H["keep_card"]], [], "R3",
         "Pingwise bills $29/month from Nov 1, so it fails the cash test: End (ask to downgrade)",
         "the guardrails exempt Arthur's keep-running list; its checklist item 'the night pager for backend outages' is Pingwise's on-call paging -> Keep, confirm staying",
         order="the cash test is read before the exemption is joined to a checklist item that does not name the vendor"),
    trap("T5", "superseding", ["gdocs", "gmail", "gcal"], [H["clipforge_notice_thread"], H["clipforge_kickoff"]], [], "R2",
         "Clipforge's pilot is free through Jan 15, 2026 (its agreement), so Park",
         "the processor notice for workspace HG-2291 (UGC Studio, tied to Clipforge by the paper and the Jul 14 kickoff) moves the pilot end to Oct 15 and starts $1,800/month on Oct 16 -> End, cancel in writing by Oct 15",
         order="the agreement and the rep's thread name Clipforge; the notice names only the workspace and product, so a name search misses it",
         versions=[{"service": "gdocs", "id": "clipforge-pilot-agreement", "seeded": True, "at": "2025-07-08T18:30:00Z", "container": "file:clipforge-pilot-agreement"},
                   {"service": "gmail", "id": H["clipforge_notice_thread"], "seeded": True, "at": T["clipforge_notice"], "container": f"gmail:{H['clipforge_notice_thread'].split('/')[1]}"}]),
    trap("T6", "exact_predicate", ["gmail", "gdocs"], [H["pixel_thread"]], [], "R1",
         "the backlog is what came in during September, so Pixel Harbor's June quote is missed",
         "the hub's scope has no date limit (an offer in front of us that we engaged with); the June quote still needs a deposit by Oct 10 -> on the log, End",
         order="date-windowed mail searches (after Sep 1) do not return a June 18 thread"),
    trap("T7", "superseding", ["slack", "gmail"], [H["july_sign_note"], H["esg_thread"]], [], "R6",
         "Leonard's July note lets Frederick accept small terms himself, so Markward's click-through needs no card",
         "ESG's Sep 24 note (only Leonard or Arthur accept terms, whatever the amount) and Leonard's Sep 25 reply ('this replaces what I said in July')",
         versions=[{"service": "slack", "id": H["july_sign_note"], "seeded": True, "at": T["july_sign_note"], "container": f"slack:{H['july_sign_note']}"},
                   {"service": "gmail", "id": H["esg_thread"], "seeded": True, "at": T["esg_note"], "container": f"gmail:{H['esg_thread'].split('/')[1]}"},
                   {"service": "gmail", "id": H["esg_thread"] + "#ack", "seeded": True, "at": T["esg_ack"], "container": f"gmail:{H['esg_thread'].split('/')[1]}"}]),
    trap("T8", "superseding", ["gdocs", "gcal"], [H["guardrails_doc"], H["review_event"]], [], "R7",
         "revisit 'in the first week of January' (the guardrails' wording), dated by guess",
         "Leonard's commitments review on Mon Jan 5, 2026 (created Sep 29) is the revisit date",
         versions=[{"service": "gdocs", "id": H["guardrails_doc"], "seeded": True, "at": T["guardrails"], "container": f"file:{H['guardrails_doc']}"},
                   {"service": "gcal", "id": H["review_event"], "seeded": True, "at": T["review_event"], "container": f"gcal:{H['review_event']}"}]),
    trap("T9", "superseding", ["gdocs", "slack"], [H["guardrails_doc"], H["amendment_root"]], [], "R2",
         "travel and event costs count only when we book them, so Wishwave (partner-booked travel) parks",
         "Leonard's Sep 29 #executives change: travel and event costs count as cash even when a partner books them -> Wishwave End",
         versions=[{"service": "gdocs", "id": H["guardrails_doc"], "seeded": True, "at": T["guardrails"], "container": f"file:{H['guardrails_doc']}"},
                   {"service": "slack", "id": H["amendment_root"], "seeded": True, "at": T["amendment"], "container": f"slack:{H['amendment_root']}"}]),
    trap("T10", "distractor", ["slack"], [H["robert_cancel_all"]], [], "R2", "Robert's 'just cancel every marketing tool' settles every decision as End",
         "Robert is not the owner of the guardrails; Leonard's doc decides", dtype="non_authoritative_instruction"),
    trap("T11", "distractor", ["gmail"], [], [BASE["playable_factory_thread"]], "R1", "Playable Factory's unanswered follow-up is a company waiting on us",
         "a cold pitch nobody engaged with is off the log", dtype="scope_adjacent"),
    trap("T12", "distractor", ["gmail"], [], [BASE["google_thread"]], "R1", "the Google partner check-in is a partner waiting on timing",
         "the hub keeps ad networks off the log (UA budget call)", dtype="scope_adjacent"),
    trap("T13", "distractor", ["gmail"], [], [BASE["balancy_thread"]], "R4", "Balancy's trial offer needs an answer",
         "Leonard answered in-thread on Sep 11 ('we'll circle back') -> Answered by Leonard, revisit", dtype="already_done"),
    trap("T14", "stale_summary", ["gsheets"], [H["tracker_sheet"]], [], "R1", "Frederick's July 31 vendor tracker is the population",
         "the tracker predates most offers and lists ended ones; the hub's scope rule over the mail decides", dtype="stale_summary"),
    trap("T15", "distractor", ["gmail"], [], [BASE["ncsoft_report"]], "R1", "NCsoft's engine demo and 'pilot' talk is a partner offer",
         "NCsoft is strategic / investor talks (bridge work), off the log", dtype="keyword_collision"),
    trap("T16", "distractor", ["gmail"], [H["nova_thread"]], [], "R1", "Nova Rewards' offer is waiting on us",
         "Nova withdrew it on Sep 23", dtype="withdrawn_ask"),
    trap("T18", "distractor", ["gmail"], [], [BASE["rayking_thread"]], "R1", "Rayking's pitch is engaged: Frederick wrote 'Hi …, Leonard forwarded me your email'",
         "that reply went to Leonard (To: leonard.hayes), so nothing from us reached Rayking: a pitch only forwarded around internally stays off the log", dtype="scope_adjacent"),
    trap("T17", "distractor", ["gmail", "gdocs"], ["retainly-terms"], [], "R2", "Retainly's trial converts to paid like Reviewly's, so End",
         "Retainly converts Jan 12, 2026, outside the cash window -> Park", dtype="near_duplicate_record"),
    trap("T19", "completion_elsewhere", ["gmail", "gcal", "slack"], [H["spotlight_thread"], H["spotlight_note"]], [], "R4",
         "Spotlight Fest's Dec 5 invitation ($750 stand fee) is still open, so the cash test ends it with a written no",
         "Robert's Sep 17 #executives note: he had the call about the Dec 5 indie showcase and let Rina know we're sitting it out -> Answered by Robert, no second answer",
         order="the invitation thread and the Sep 17 call event are the natural reads; the note names neither the fest nor 'told', and sits before the late-September #executives window (rev3 found the old wording by 'Spotlight' and 'told', events 386, 426)"),
    trap("T20", "exact_predicate", ["gmail"], [H["hootline_thread"]], [], "R1",
         "the backlog is what is live in recent mail and the filed papers, so Hootline (nothing after Aug 12, no paper) is missed",
         "the hub's scope has no date limit: Frederick signed up (engaged) and Gemma's Aug 12 question is unanswered -> on the log, Park, revisit Jan 5",
         order="a mailbox listing from mid-August, the paperwork folder and the July tracker all miss it (rev3's cohort came from exactly those, events 66, 282, 284); an undated mail search or a June-onward listing finds it"),
]

portfolio = [
    {"id": "DONE", "mechanism": "A24", "prior_family": "done_gap", "prior_family_reason": "v2 trap 1: a done source (registration completed) with the missing piece (officer acceptance) in another service (Linear comment)",
     "nodes": ["T1", "C1"], "requirement": "R6", "natural_reading": "Nintendo needs nothing: registration completed", "decides": ["X1", "X2"],
     "controls": ["Orbit Store (needs an officer's acceptance, no done claim: Sign)", "Playfuse (NDA: Sign)"],
     "over_application": "over-application routes Retainly's trial sign-up to a signature card although its paper needs no acceptance",
     "prior": {"alpha": 1.0, "beta": 2.0, "record_ids": ["hev_7f44d83eaad625e9", "hev_522f1ca2bc9062de"]}, "source": "linear-comment", "signature": "Nintendo ZOM-567 comment officer accepts"},
    {"id": "CORR", "mechanism": "A11", "prior_family": "superseding", "prior_family_reason": "v2 trap 2: the waiver is a thread reply under a root about another vendor and (rev4) names the contact and plan, not the company; rev3's named reply leaked to a 'Framewell' search (hev_ebc012c844829411); bridge SciPlay reply under an unrelated root: 2/8 then 3/6 caught",
     "nodes": ["T2", "C2"], "requirement": "R2", "natural_reading": "Framewell End: paid from Nov 1", "decides": ["X3", "X4"],
     "controls": ["Brightlane Studio (paid from Oct 1, no waiver: End)", "Quillcraft (free beta through January: Park)"],
     "over_application": "over-application parks Brightlane too, as if every paid quote were waived",
     "prior": {"alpha": 1.0, "beta": 3.0, "record_ids": ["hev_1ceea0e7e912f48b", "hev_ebc012c844829411"]}, "source": "slack-thread-reply-alias", "signature": "Maren Pro plan no charge until Feb 1"},
    {"id": "COMPL", "mechanism": "A25", "prior_family": "completion_elsewhere", "prior_family_reason": "v2 trap 9: the answer was given by phone and (rev4) recorded as a thread reply in Leonard's 1:1 DM naming Wen, not the company; rev3's named DM root leaked (hev_13d86dcf23442708); bridge Paul DM placement: 3/6 caught",
     "nodes": ["T3", "C3"], "requirement": "R4", "natural_reading": "Lanternfly gets a reply (Park or Sign)", "decides": ["X5", "X6", "X15", "X19"],
     "controls": ["Balancy (answered in its own thread: Answered)", "Motive Forge (Arthur declined in-thread: Answered)"],
     "over_application": "over-application treats Glyphworks as answered because Leonard mentioned fonts in #executives",
     "prior": {"alpha": 1.0, "beta": 2.0, "record_ids": ["hev_13d86dcf23442708"]}, "source": "slack-dm-thread-reply", "signature": "rang Wen back Southeast Asia after the raise"},
    {"id": "EXC", "mechanism": "A15", "prior_family": "authority", "prior_family_reason": "v2 trap 5: an exception in an older record (Arthur's August list) overrides the cash test; the item is named by function, not vendor",
     "nodes": ["T4", "C4"], "requirement": "R3", "natural_reading": "Pingwise End: paid from Nov 1", "decides": ["X16", "P1"],
     "controls": ["Vaultline and Certwell (named on the list: Keep)", "Reviewly (paid, not on the list: End)"],
     "over_application": "over-application keeps Reviewly as live-game tooling",
     "prior": {"alpha": 1.0, "beta": 3.0, "record_ids": ["hev_d17e4abe74f0e7e0", "hev_1de494f0682754d6"]}, "source": "trello-checklist", "signature": "keep-running night pager backend outages"},
    {"id": "DATE", "mechanism": "A4", "prior_family": "superseding", "prior_family_reason": "v2 trap 4: a moved end date changes which side of the Dec 31 window the pilot falls on; the notice is keyed by workspace id (handover publisher-id notice: 5/6 missed)",
     "nodes": ["T5", "C5"], "requirement": "R2", "natural_reading": "Clipforge Park: pilot free through Jan 15", "decides": ["X9", "X10", "X11"],
     "controls": ["Retainly (converts Jan 12: Park)", "Reviewly (converts Oct 20 by its own terms: End)"],
     "over_application": "over-application ends Retainly as well",
     "prior": {"alpha": 1.0, "beta": 2.0, "record_ids": ["hev_e61e07235eadbd24", "hev_1ceea0e7e912f48b"]}, "source": "processor-notice", "signature": "workspace HG-2291 pilot ends Oct 15"},
    {"id": "FILT", "mechanism": "A17", "prior_family": "exact_predicate", "prior_family_reason": "v2 trap 7: one in-scope company sits outside the September date window runs search (handover Arthur email outside the window: 2/6 missed)",
     "nodes": ["T6", "C6"], "requirement": "R1", "natural_reading": "Pixel Harbor not on the log", "decides": ["X12", "X13", "V1"],
     "controls": ["Glyphworks (August thread with a filed paper: on the log)", "Nova Rewards (withdrawn: off)"],
     "over_application": "over-application pulls Playable Factory's cold pitch onto the log",
     "prior": {"alpha": 1.0, "beta": 3.0, "record_ids": ["hev_9c403cae42eb4df8", "hev_c2297d21ba5cbc7b"]}, "source": "mail-date-window", "signature": "Pixel Harbor deposit Oct 10 June quote"},
    {"id": "SIGN", "mechanism": "A12", "prior_family": "superseding", "prior_family_reason": "the governing signing rule (ESG, Gmail) supersedes Leonard's July Slack note; on the delegation path, so expected mostly caught",
     "nodes": ["T7"], "requirement": "R6", "natural_reading": "Frederick accepts Markward's free click-through himself (July note): no card", "decides": ["C10"],
     "controls": ["Kinetic Arcade (counsel + card either way)"], "over_application": "over-application cards Echohall although nothing needs accepting",
     "prior": {"alpha": 1.0, "beta": 2.0, "record_ids": ["hev_e61e07235eadbd24"]}, "source": "hub-path", "signature": "ESG only Leonard or Arthur accept terms"},
    {"id": "AMEND", "mechanism": "A15", "prior_family": "superseding", "prior_family_reason": "the Sep 29 #executives change to the cash test; named by the hub, so expected mostly caught",
     "nodes": ["T9"], "requirement": "R2", "natural_reading": "Wishwave Park: travel is booked by the partner", "decides": ["C11"],
     "controls": ["Pressbeam (no travel: Park)"], "over_application": "over-application ends Pressbeam",
     "prior": {"alpha": 1.0, "beta": 2.0, "record_ids": ["hev_1ceea0e7e912f48b"]}, "source": "hub-path", "signature": "travel counts as cash partner books"},
    {"id": "NOTE", "mechanism": "A25", "prior_family": "completion_elsewhere", "prior_family_reason": "v2 trap 9 (rev4): Spotlight's answer was given on a call by Robert and recorded only in his #executives note, which names the Dec 5 indie showcase and Rina, not the fest; rev3's named note leaked to 'Spotlight' and 'told' searches (precheck events 386, 426)",
     "nodes": ["T19", "C8"], "requirement": "R4", "natural_reading": "Spotlight Fest End: say no to the $750 stand fee", "decides": ["X20", "C3"],
     "controls": ["Motive Forge (Arthur declined in-thread: Answered)", "Wishwave (partner showcase push, nobody answered: End)"],
     "over_application": "over-application treats Wishwave's showcase push as already answered by Robert's note",
     "prior": {"alpha": 1.0, "beta": 2.0, "record_ids": ["hev_13d86dcf23442708"]}, "source": "slack-root-alias", "signature": "Dec 5 indie showcase sitting this one out Rina"},
    {"id": "WIN", "mechanism": "A17", "prior_family": "exact_predicate", "prior_family_reason": "v2 trap 7 (rev4): one in-scope company sits outside every obvious filter - no filed paper, not in the July tracker, nothing after Aug 12 - while rev3's pre-check built the cohort from an after:Aug-15 listing, the paperwork folder and the tracker (events 66, 282, 284)",
     "nodes": ["T20", "C7"], "requirement": "R1", "natural_reading": "Hootline not on the log", "decides": ["X18", "X21", "V1"],
     "controls": ["Quillcraft (August thread with a filed paper: on the log)", "Gamesforum SF (August invite nobody answered: off)"],
     "over_application": "over-application pulls Gamesforum SF's unanswered August invite onto the log",
     "prior": {"alpha": 1.0, "beta": 3.0, "record_ids": ["hev_9c403cae42eb4df8", "hev_c2297d21ba5cbc7b"]}, "source": "mail-window-and-folder", "signature": "Hootline promo keep the scheduler after Jan 31"},
]
for p in portfolio:
    if p["prior"] is None:
        p.pop("prior")
channels = [
    {"id": "CH-DONE", "kind": "member", "rule": "DONE", "degrade": "Nintendo treated as done (no Sign, no card)", "members": ["Nintendo"], "latent": "linear-comment read", "family": "done_gap"},
    {"id": "CH-CORR", "kind": "member", "rule": "CORR", "degrade": "Framewell ended", "members": ["Framewell"], "latent": "contact-name search / thread open", "family": "superseding"},
    {"id": "CH-COMPL", "kind": "member", "rule": "COMPL", "degrade": "Lanternfly answered again (Sign or Park)", "members": ["Lanternfly Publishing"], "latent": "DM thread open", "family": "completion_elsewhere"},
    {"id": "CH-EXC", "kind": "member", "rule": "EXC", "degrade": "Pingwise ended", "members": ["Pingwise"], "latent": "trello checklist join", "family": "authority"},
    {"id": "CH-DATE", "kind": "member", "rule": "DATE", "degrade": "Clipforge parked", "members": ["Clipforge"], "latent": "workspace-id mail", "family": "superseding"},
    {"id": "CH-FILT", "kind": "member", "rule": "FILT", "degrade": "Pixel Harbor Events off the log", "members": ["Pixel Harbor Events"], "latent": "mail date window", "family": "exact_predicate"},
    {"id": "CH-NOTE", "kind": "member", "rule": "NOTE", "degrade": "Spotlight Fest ended and answered again", "members": ["Spotlight Fest"], "latent": "full #executives read / showcase search", "family": "completion_elsewhere"},
    {"id": "CH-WIN", "kind": "member", "rule": "WIN", "degrade": "Hootline off the log", "members": ["Hootline"], "latent": "undated mail search", "family": "exact_predicate"},
    {"id": "CH-SLIP", "kind": "slip", "degrade": "base slip on control rows", "slots": ["C1", "C2", "C5", "C6", "C7", "C9"]},
]
budget = [
    ("discovery", "gmail", 4, "read the hub; open ESG's signing thread with Leonard's reply; open the ESG engagement thread for the intake group"),
    ("discovery", "gdocs", 4, "read the guardrails doc, the folder README, ESG's intake checklist; reject the UA-buckets doc on scope"),
    ("discovery", "gsheets", 2, "read the template header row; reject the July tracker as stale"),
    ("discovery", "gdrive", 2, "list the Q4 commitments folder; locate papers shared by counterparties"),
    ("discovery", "slack", 4, "read Leonard's Sep 29 amendment; search #executives for the guardrails context and the July signing note"),
    ("discovery", "trello", 2, "read the founders' board lists and cards; read Arthur's keep-running checklist"),
    ("discovery", "gcal", 1, "read the Jan 5 commitments review"),
    ("discovery", "contacts", 1, "find ESG Law intake"),
    ("enumeration", "gmail", 8, "census of offer threads since June (dated and undated searches, vendor and partner terms); every company has its own thread"),
    ("enumeration", "gcal", 2, "list calls Jun 2025 to Jan 2026 (kickoffs, partner calls, the review)"),
    ("enumeration", "slack", 3, "search #executives and DMs for vendor and partner decisions Leonard or Arthur already made"),
    ("per-record", "gmail", 23, "each of 46 companies' thread read (bulk batch reads counted at half a call per company)"),
    ("per-record", "gdocs", 29, "each counterparty's paper (order form, terms, quote): cost, conversion dates, auto-renewal, exclusivity, IP, term"),
    ("per-record", "gslides", 3, "partners' proposal decks (Lanternfly, Bundlehouse) and one deck-only term"),
    ("per-record", "contacts", 35, "lookup before each add (three counterparties already exist; ESG intake)"),
    ("per-record", "slack", 8, "name, contact-name and topic searches for companies whose state may have moved off their thread (Framewell, Lanternfly, Spotlight and others), and opening the threads they land in"),
    ("per-record", "linear", 2, "ZOM-567 and its comments (Nintendo)"),
    ("per-record", "gcal", 9, "calls tied to a company (Clipforge kickoff, Spotlight, partner calls) read at 0.2 per company"),
    ("writes", "gmail", 31, "a written answer to each of 31 companies waiting to hear from us (replies on their threads; Clipforge's cancellation to the notice's address)"),
    ("writes", "gmail", 3, "one email per counsel agreement to ESG's intake address (Kinetic Arcade, Lumencloud, Bundlehouse)"),
    ("writes", "gcal", 14, "a revisit reminder on Jan 5 for each of 12 parked companies and 2 'later' answers"),
    ("writes", "contacts", 32, "a contact for each company's person not already in Contacts"),
    ("writes", "trello", 7, "a founders' board To Do card for each company waiting on a signature"),
    ("writes", "gsheets", 3, "create the log in the folder and write its rows"),
    ("writes", "gmail", 1, "reply on Leonard's thread with what stays and what waits on a signature"),
    ("read-back", "gsheets", 2, "read the log back against the README columns"),
    ("read-back", "trello", 1, "confirm the cards landed in To Do"),
]
call_budget = [{"phase": p, "service": s, "calls": c, "reason": r} for p, s, c, r in budget]
TOTAL_BUDGET = sum(c for _, _, c, _ in budget)
PER_RECORD = round(sum(s["per_record_calls"] * s["records"] for s in surfaces))
writes = [
    {"service": "gsheets", "tool": "gsheets_create_spreadsheet+gsheets_values_update", "count": 3, "depends_on": ["K8", "K9", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "T1", "T2", "T3", "T4", "T5", "T6", "T19", "T20"], "requirements": ["R1", "R2", "R3", "R4", "R9"]},
    {"service": "gmail", "tool": "gmail_reply_to_message+gmail_send_message", "count": 34, "depends_on": ["K1", "K14", "K5", "K11", "K12", "C2", "C3", "C4", "C5", "C6"], "requirements": ["R5", "R6"]},
    {"service": "gcal", "tool": "gcal_create_event", "count": 14, "depends_on": ["K7", "C2", "C3", "C7", "T8", "T20"], "requirements": ["R7"]},
    {"service": "contacts", "tool": "contacts_add_new_contact", "count": 32, "depends_on": ["K1", "K8", "C6"], "requirements": ["R8"]},
    {"service": "trello", "tool": "trello_create_card", "count": 7, "depends_on": ["K5", "C1", "T7"], "requirements": ["R6"]},
    {"service": "gmail", "tool": "gmail_reply_to_message (report)", "count": 1, "depends_on": ["K13", "C1", "C2", "C3", "C4", "C5", "C6"], "requirements": ["R10"]},
]
manifest = {
    "_note": "draft manifest (/create-scenario); /create-injection writes 01_Hardness_Manifest.json keeping every id or listing it in design_delta. Seeded texts quoted in delegation_quote are the planned wording.",
    "persona": "frederick_stone", "assignment_context": ctx, "horizon": "Long Horizon", "effective_profile": "extreme",
    "author_targets": {"min_calls_per_run": 130, "max_avg_weighted_pass": 0.8,
                       "requester_confirmation": "task author in chat on 2026-11-03: 'my task is a long horizon task soo i want over 130 tool calls in each runs and also i want difficulty pass rate under 80% and also have to folllow all other difficulty guidelines soo you can choose from your self which option is best fit for my needs for this task'"},
    "volume_exception": {"reason": "the cohort is 46 real companies (36 in scope); mail and calendar are bulk-readable, so honest necessary calls are about 225 (a lean correct run about 150) - reaching 500 would need padding, which fails on its own",
                         "requester_confirmation": "task author in chat on 2026-11-03 set the horizon target at 'over 130 tool calls in each runs' and delegated the choice ('you can choose from your self which option is best fit for my needs'); the pre-scenario analysis's volume-exception proposal was part of that choice",
                         "call_budget_floor": 200, "per_record_floor": 90},
    "requirements": REQ, "services": services, "anchors": anchors, "ask_fragments": fragments, "authorities": authorities,
    "cohort": cohort, "chains": chains, "traps": traps, "mechanism_portfolio": portfolio, "channels": channels,
    "call_budget": call_budget, "writes": writes,
    "hazard_acknowledgements": [
        {"hazard_id": "Q01", "resolution": "dated_claim", "requirement": "R2", "why_safe": "Leonard's seeded reply under his Sep 22 Playtestcloud root changes that root's reply_count/latest_reply; the SQL updates the counters as companions and the text is an attributed, dated claim"},
        {"hazard_id": "Q01", "resolution": "dated_claim", "requirement": "R4", "why_safe": "rev4: Leonard's seeded DM reply under his Sep 17 'we have no localization though' root (D05S58U4SAK/1758151772.570449) changes that root's reply_count/latest_reply; the SQL updates the counters as companions and the text is an attributed, dated claim"},
    ],
    "denied_probes": [], "gradable_surface": "01_Gradable_Surface.json",
    "design_delta": [
        {"id": "T2", "change": "rebuild", "why": "rev3 pre-check found the waiver by a 'Framewell' Slack search (precheck event 444) and 'vendor after:' (event 480); rev4 rewords the reply to name Maren and the Pro plan, not Framewell or vendors", "evidence": "run_forensics/rev3/precheck.node_verdicts.json"},
        {"id": "T3", "change": "rebuild", "why": "rev3 DM root was the newest DM message and named Lanternfly and 'told' (events 387, 426, 428); rev4 makes it a thread reply under Leonard's Sep 17 localization DM, naming Wen and the Southeast Asia deal", "evidence": "run_forensics/rev3/precheck.node_verdicts.json"},
        {"id": "T19", "change": "add", "why": "Spotlight's answer (Robert's note) leaked by 'Spotlight'/'told' (events 386, 426); rev4 de-names it, removes the answer from the call's description and gives it its own rule NOTE", "evidence": "01a_Hardening_Report.md §10 M3"},
        {"id": "T20", "change": "add", "why": "the only landed trap was a member outside the inbox-and-folder filter; rev4 moves Hootline outside it (no paper, ask moved to Aug 12) under rule WIN", "evidence": "01a_Hardening_Report.md §10 M4"},
        {"id": "C7", "change": "add", "why": "chain for WIN (Hootline)", "evidence": "01a_Hardening_Report.md §10 M4"},
        {"id": "C8", "change": "add", "why": "chain for NOTE (Spotlight)", "evidence": "01a_Hardening_Report.md §10 M3"},
        {"id": "X7", "change": "purge", "why": "surface: the Pingwise decision sample (EXC leaked, the guardrails name the card) is replaced in the decision group by X20 Spotlight decision; EXC keeps X16 and P1", "evidence": "run_forensics/rev3/precheck.surface_grades.json"},
        {"id": "surface", "change": "rebuild", "why": "the rev3 proxy under-reported a correct run by 27 points: Answered by and Next date now compare by word (issue_key), and the told patterns accept 'no', 'won't', 'said no', 'passed on'", "evidence": "01a_Hardening_Report.md §6"},
    ],
}
if os.environ.get("BUILD_SCENARIO_WRITE") == "1":
    write(os.path.join(WF, "01_Hardness_Manifest.draft.json"), manifest)

# ---------------------------------------------------------------- gradable surface
KEYS = [m["key"] for m in IN]
PROC = "billing@paylane.io"   # processor address named in Clipforge's notice (no 'clipforge' string)


def slot(sid, title, weight, kind, reason, cls, selector, role="core", group=None, mechs=(), fact=None, **kw):
    s = {"id": sid, "title": title, "weight": weight, "work_kind": kind, "work_reason": reason, "class": cls,
         "selector": selector, "role": role, "mechanisms": list(mechs)}
    if group:
        s["group"] = group
    if fact:
        s["fact_id"] = fact
    s.update(kw)
    return s


MS = "multi_source_reconciliation"
slots = [
    # traps
    slot("X1", "Nintendo decision", 5, MS, "portal mails + Frederick's post vs Arthur's Linear comment + ESG's signing rule", "direct", ["field", "Nintendo", "Decision"], "sample", "decision", ["DONE"]),
    slot("X2", "Nintendo signature card", 5, MS, "the card exists only if the Linear comment and ESG's rule are joined", "write_content", ["text", "cards", r".*[Nn]intendo.*"], mechs=["DONE"], fact="nintendo_card"),
    slot("X3", "Framewell decision", 5, MS, "order form vs Leonard's thread reply under another vendor's post", "direct", ["field", "Framewell", "Decision"], "sample", "decision", ["CORR"]),
    slot("X4", "Framewell revisit reminder", 5, MS, "revisit exists only once the waiver parks it; date from the review event", "write_content", ["text", "events", r".*[Ff]ramewell.*"], mechs=["CORR"], fact="framewell_revisit"),
    slot("X5", "Lanternfly decision", 5, MS, "thread follow-up vs Leonard's DM", "direct", ["field", "Lanternfly Publishing", "Decision"], "sample", "decision", ["COMPL"]),
    slot("X6", "Lanternfly answered by", 5, MS, "who answered is only in the DM", "direct", ["field", "Lanternfly Publishing", "Answered by"], "sample", "answered_by", ["COMPL"]),
    slot("X20", "Spotlight Fest decision", 5, MS, "invitation thread vs Robert's note that names only the Dec 5 indie showcase and Rina", "direct", ["field", "Spotlight Fest", "Decision"], "sample", "decision", ["NOTE"]),
    slot("X9", "Clipforge decision", 5, MS, "pilot agreement vs processor notice keyed by workspace id + kickoff call", "direct", ["field", "Clipforge", "Decision"], "sample", "decision", ["DATE"]),
    slot("X10", "Clipforge next date", 5, MS, "cancel-by date from the moved pilot end", "direct", ["field", "Clipforge", "Next date"], "sample", "next_date", ["DATE"]),
    slot("X11", "Clipforge written cancellation", 5, MS, "the address is only in the processor notice", "write_content", ["text", "sends", r".*billing@paylane\.io.*"], mechs=["DATE"], fact="clipforge_cancel"),
    slot("X12", "Pixel Harbor next date", 5, MS, "June quote outside the window + hub scope + deposit date", "direct", ["field", "Pixel Harbor Events", "Next date"], "sample", "next_date", ["FILT"]),
    slot("X13", "Pixel Harbor told", 5, MS, "decline after finding the June quote and applying the cash test", "write_content", ["reason_matches", "Pixel Harbor Events", r".*(\\b[Nn]o\\b|[Dd]eclin|[Pp]ass(ed)? on|[Nn]ot (book|tak)|[Nn]o thanks|[Ss]aid no|[Ww]on'?t|[Nn]ot this).*"], "sample", "told", ["FILT"]),
    # volume and report
    slot("V1", "log membership", 3, "limited_reconciliation", "46 looked at, 36 kept by the scope rule", "delivery", ["delivery", "register_keys_exact"], "volume", None, ["FILT", "WIN"],
         fact="log_size", volume_for=["decision", "next_date", "answered_by", "told"], expected_keys=KEYS),
    slot("P1", "report names what stays", 5, MS, "kept list needs the exemption join (Pingwise) plus Vaultline and Certwell", "write_content", ["text", "replies", r".*[Pp]ingwise.*"], mechs=["EXC"], fact="kept_list"),
    slot("P2", "report names Markward as waiting to sign", 3, "interpretation", "ESG's note supersedes the July note for click-through terms", "write_content", ["text", "replies", r".*[Mm]arkward.*"], mechs=["SIGN"], fact="sign_list_markward"),
    slot("X14", "Framewell next date", 5, MS, "review date once the waiver parks it (order form says Nov 1)", "direct", ["field", "Framewell", "Next date"], "sample", "next_date", ["CORR"]),
    slot("X15", "Lanternfly told", 5, MS, "what Leonard told them is only in the DM", "write_content", ["reason_matches", "Lanternfly Publishing", r".*([Nn]o new (publishing|deals)|(before|after|until) the raise).*"], "sample", "told", ["COMPL"]),
    slot("X17", "Nintendo next date", 5, MS, "the portal request lapses Oct 15 unless an officer accepts - only in Arthur's ZOM-567 comment", "direct", ["field", "Nintendo", "Next date"], "sample", "next_date", ["DONE"]),
    slot("X16", "Pingwise next date", 5, MS, "Keep: next bill Nov 1 (End would be a cancel-by date)", "direct", ["field", "Pingwise", "Next date"], "sample", "next_date", ["EXC"]),
    slot("X18", "Hootline revisit reminder", 5, MS, "Hootline exists only in August mail with no paper; parked -> Jan 5 reminder", "write_content", ["text", "events", r".*[Hh]ootline.*"], mechs=["WIN"], fact="hootline_revisit"),
    slot("X19", "Lanternfly revisit reminder", 5, MS, "a 'later' answer found only in the DM thread reply -> Jan 5 reminder", "write_content", ["text", "events", r".*[Ll]anternfly.*"], mechs=["COMPL"], fact="lanternfly_revisit"),
    slot("X21", "Hootline contact", 3, "limited_reconciliation", "Gemma is reachable only from the August thread", "write_content", ["text", "contacts", r".*[Hh]ootline.*"], mechs=["WIN"], fact="hootline_contact"),
    # controls
    slot("C1", "Balancy answered by", 3, "interpretation", "Leonard's answer is in Balancy's own thread", "direct", ["field", "Balancy", "Answered by"], "sample", "answered_by"),
    slot("C2", "Motive Forge answered by", 3, "interpretation", "Arthur declined in-thread", "direct", ["field", "Motive Forge", "Answered by"], "sample", "answered_by"),
    slot("C3", "Spotlight Fest answered by", 5, MS, "Robert's answer is only in his Sep 17 note, which names the showcase and Rina, not the fest", "direct", ["field", "Spotlight Fest", "Answered by"], "sample", "answered_by", ["NOTE"]),
    slot("C5", "Soundvault told", 3, "interpretation", "paid on signature -> declined", "write_content", ["reason_matches", "Soundvault", r".*(\\b[Nn]o\\b|[Dd]eclin|[Pp]ass(ed)? on|[Nn]ot (book|tak)|[Nn]o thanks|[Ss]aid no|[Ww]on'?t|[Nn]ot this).*"], "sample", "told"),
    slot("C6", "Kinetic Arcade told", 3, "interpretation", "exclusivity -> with counsel", "write_content", ["reason_matches", "Kinetic Arcade", r".*([Cc]ounsel|[Ll]awyer|[Ll]egal|ESG).*"], "sample", "told"),
    slot("C7", "Kinetic Arcade card", 3, "interpretation", "waiting on a signature -> card", "write_content", ["text", "cards", r".*[Kk]inetic.*"], fact="kinetic_card"),
    slot("C8", "Lumencloud to ESG intake", 5, MS, "36-month term on the paper + ESG rule + intake address from Contacts", "write_content", ["text", "sends", r".*[Ll]umencloud.*"], fact="lumencloud_esg"),
    slot("C9", "Reviewly contact", 1, "lookup", "the person in Reviewly's thread", "write_content", ["text", "contacts", r".*[Rr]eviewly.*"], fact="reviewly_contact"),
    slot("C10", "Markward signature card", 3, "interpretation", "ESG's note supersedes the July note: click-through terms need an officer", "write_content", ["text", "cards", r".*[Mm]arkward.*"], mechs=["SIGN"], fact="markward_card"),
    slot("C11", "Wishwave told", 3, "interpretation", "the Sep 29 change counts partner-booked travel as cash", "write_content", ["reason_matches", "Wishwave", r".*(\\b[Nn]o\\b|[Dd]eclin|[Pp]ass(ed)? on|[Nn]ot (book|tak)|[Nn]o thanks|[Ss]aid no|[Ww]on'?t|[Nn]ot this).*"], "sample", "told", ["AMEND"]),
    # delivery
    slot("D1", "log in the Q4 commitments folder", 1, "lookup", "folder named in the prompt", "delivery", ["delivery", "register_parent", IDS["q4_folder"]]),
    slot("D2", "report on Leonard's thread", 1, "lookup", "reply on the hub", "delivery", ["delivery", "email_reply", "hub-message"]),
]
surface = {
    "kind": "GRADABLE_SURFACE", "version": 1, "task": "frederick_q4_commitments", "revision": "design-2",
    "truth_keys": KEYS, "classes": ["Answered", "End", "Keep", "Sign", "Park"],
    "truth_fields": {"class": "Decision", "groups": "groups"},
    "deliverables": {
        "log": {"kind": "table", "name_regex": r"(?i).*(commit|vendor|partner|q4).*", "key_column": "Company", "key_regex": ".+",
                "columns": ["Company", "Contact", "What's waiting", "Decision", "Answered by", "What we told them", "Next date"],
                "class_column": "Decision", "reason_column": "What we told them",
                "comparators": {"Decision": "norm", "Answered by": "issue_key", "Next date": "issue_key"}},
        "replies": {"kind": "json_text", "tool": "gmail_reply_to_message"},
        "sends": {"kind": "json_text", "tool": "gmail_send_message"},
        "events": {"kind": "json_text", "tool": "gcal_create_event"},
        "cards": {"kind": "json_text", "tool": "trello_create_card"},
        "contacts": {"kind": "json_text", "tool": "contacts_add_new_contact"},
    },
    "slots": slots,
}
if os.environ.get("BUILD_SCENARIO_WRITE") == "1":
    write(os.path.join(WF, "01_Gradable_Surface.json"), surface)
write(os.path.join(HERE, "ids.json"), {"ids": IDS, "base": BASE, "times": T, "quotes": Q, "counts": COUNTS,
                                       "writes": {"replies": N_REPLY, "revisits": N_REVISIT, "cards": N_CARD, "esg": N_ESG, "contacts": N_CONTACT, "papers": N_PAPER},
                                       "budget_total": TOTAL_BUDGET, "per_record_total": PER_RECORD,
                                       "members": M})
print("members", len(M), "in scope", len(IN), COUNTS, "writes", N_REPLY, N_REVISIT, N_CARD, N_ESG, N_CONTACT, "papers", N_PAPER)
print("budget", TOTAL_BUDGET, "per-record", PER_RECORD, "slots", len(slots), "weight", sum(s["weight"] for s in slots),
      "flippable", sum(s["weight"] for s in slots if s["mechanisms"]))
