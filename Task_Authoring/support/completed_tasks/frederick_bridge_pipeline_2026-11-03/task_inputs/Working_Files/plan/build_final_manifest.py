#!/usr/bin/env python3
"""Final manifest (injection rev7) from the draft + what only the SQL settles. Keeps every draft id or lists the change
in design_delta."""
import hashlib, json
from pathlib import Path

WF = Path(__file__).resolve().parents[1]
m = json.loads((WF / "01_Hardness_Manifest.draft.json").read_text())
ids = json.loads((WF / "plan/sql_ids.json").read_text())["ids"]
FRED = "frederick.stone@harmonygames.co"
SHA = {"C07C2866011/1758303600.418207": "4921f321db5d08f936aac24a6a1d2af8",
       "C07C2866011/1758911700.336170": __import__("hashlib").sha256("C07C2866011|1758911700.336170".encode()).hexdigest()[:32],
       "C07C2866011/1759168800.117903": "7fef94264090696760180223fc8265e7",
       "C07C2866011/1759248360.377105": "229090ba6b316b667d1a6451b0297a47",
       "D05S58U4SAK/1758731100.281734": "99b22482ddd77dd01b451afb39014839",
       "D05S58U4SAK/1758914100.640218": "f7261dd1b05eb2da3b81fe7d8cde2854",
       "C0880U9751A/1759274400.518306": "3cddf83c394676d8b72c0c20ed58f520",
       "C0880U9751A/1759276080.094417": "301ad67f082965686f35a9484aa25b0a",
       "C07C2866011/1759251900.863415": "7fe55f3086c1b6bcdb5dec66b00cff56",      # rev11 Leonard: Paul's out (removed in rev12)
       "D05S58U4SAK/1759251900.863415": "c5657466a4af062ceef9f7c3285aeb74"}      # rev12 Leonard (1:1 DM): Paul's out
OLD_KW, NEW_KW = "68c6b2a4f19e03d7c5a81b2e", ids["TR_KW_CMT"]
SHEET_ANG = ids["SHEET_ANGELS"]


def sub(x):
    if isinstance(x, str):
        return SHA.get(x, NEW_KW if x == OLD_KW else x)
    if isinstance(x, list):
        return [sub(y) for y in x]
    if isinstance(x, dict):
        return {k: (sub(v) if k not in ("locator", "record", "container", "base_pointers") else
                    ([NEW_KW if y == OLD_KW else y for y in v] if isinstance(v, list) else
                     (v.replace(OLD_KW, NEW_KW) if isinstance(v, str) else v))) for k, v in x.items()}
    return x


m = sub(m)
m["_note"] = "final manifest (/create-injection rev7); every draft id kept or listed in design_delta"
# exact delegation words as written in the seeded records (case-exact substrings)
Q = {"K15": "Arthur tracks the tester adds",
     "K9": "do what I put on the Existing Investor Update card in Trello",
     "K18": "do what I put on the Existing Investor Update card in Trello",
     "K11": "The draft update deck shows what each group gets",
     "K17": "see my note in #executives on what counts as signed",
     "K14": "Arthur tracks the tester adds"}
for f in m["ask_fragments"]:
    if f["id"] in Q:
        f["delegation_quote"] = Q[f["id"]]
    for na in f.get("names_authorities", []):
        if na["id"] == "H2":
            na["quote"] = "what I put on the Existing Investor Update card"
    if f["id"] == "K9":
        f["seeded_ids"] = [NEW_KW]
for t in m["traps"]:
    if t["id"] == "T3":
        t["version_records"] = [
            {"service": "gmail", "base_pointer": f"{FRED}/1842285743246816270", "seeded": False,
             "at": "2025-09-18T03:27:31Z", "container": f"gmail:{FRED}/1842285743246816270"},
            {"service": "slack", "id": SHA["C07C2866011/1759248360.377105"], "seeded": True, "at": "2025-09-30T16:06:00Z",
             "container": "slack:C07C2866011/1759196326.309469"}]
    if t["id"] == "T4":
        t["seeded_ids"] = [SHA["C07C2866011/1758303600.418207"], SHEET_ANG, SHA["D05S58U4SAK/1758731100.281734"],
                           SHA["D05S58U4SAK/1758914100.640218"]]
        t["version_records"] = [
            {"service": "slack", "id": SHA["C07C2866011/1758303600.418207"], "seeded": True, "at": "2025-09-19T17:40:00Z",
             "container": "slack:C07C2866011/1758303600.418207"},
            {"service": "gsheets", "id": SHEET_ANG, "seeded": True, "at": "2025-09-20T03:15:00Z", "container": f"file:{SHEET_ANG}"},
            {"service": "slack", "id": SHA["D05S58U4SAK/1758731100.281734"], "seeded": True, "at": "2025-09-24T16:25:00Z",
             "container": "slack:D05S58U4SAK/1758731100.281734"}]
        t["services"] = ["slack", "gsheets"]
    if t["id"] == "T2":
        t["version_records"] = [
            {"service": "gmail", "id": f"{FRED}/{ids['MSGIDS']['g_dentsu']}", "seeded": True, "at": "2025-09-26T17:20:00Z",
             "container": f"gmail:{ids['G_DENTSU']}"},
            {"service": "linear", "id": ids["LIN_C_DENTSU"], "seeded": True, "at": "2025-09-30T18:40:00Z",
             "container": "linear:ZOM-567"},
            {"service": "slack", "id": SHA["C0880U9751A/1759274400.518306"], "seeded": True, "at": "2025-09-30T23:20:00Z",
             "container": "slack:C0880U9751A/1759274400.518306"}]
        t["seeded_ids"] = [ids["G_DENTSU"], "ZOM-567", ids["LIN_C_TACC"], ids["LIN_C_NCSOFT"], ids["LIN_C_BRIGHT"],
                           ids["LIN_C_DENTSU"], SHA["C0880U9751A/1759274400.518306"], SHA["C0880U9751A/1759276080.094417"]]
    if t["id"] == "T1":
        t["seeded_ids"] = [SHA["C07C2866011/1758303600.418207"], SHEET_ANG, ids["G_DS_PAUL"], SHA["D05S58U4SAK/1759251900.863415"]]
        t["resolver"] = ("Leonard's Sep 30 10:05 AM PT message in his 1:1 DM with Frederick: Paul's out, he can't put money "
                         "in this year after all (Paul's mail went to Leonard only). A no for this round with no call or meeting: "
                         "Paul stays off the send list")
    if t["id"] == "T1":      # rev11: the nudge is dated by its message row (a thread row carries no date)
        t["version_records"] = [
            {"service": "slack", "id": SHA["C07C2866011/1758303600.418207"], "seeded": True, "at": "2025-09-19T17:40:00Z",
             "container": "slack:C07C2866011/1758303600.418207"},
            {"service": "gmail", "id": f"{FRED}/{ids['MSGIDS']['g_paul_nudge']}", "seeded": True, "at": "2025-09-29T15:00:00Z",
             "container": f"gmail:{ids['G_DS_PAUL']}"},
            {"service": "slack", "id": SHA["D05S58U4SAK/1759251900.863415"], "seeded": True, "at": "2025-09-30T17:05:00Z",
             "container": "slack:D05S58U4SAK"}]
    if t["id"] == "T8":
        t["seeded_ids"] = [NEW_KW, ids["TR_Q4_CMT"]]
    for v in t.get("version_records", []):
        if v.get("id") in SHA:
            v["id"] = SHA[v["id"]]
for c in m["chains"]:
    for hp in c["hops"]:
        hp["record"] = SHA.get(hp["record"], NEW_KW if hp["record"] == OLD_KW else hp["record"])
m["authorities"][1]["seeded_ids"] = [NEW_KW, ids["TR_Q4_CMT"]]
# channels as the solver declares them (kinds from the oracle_kit vocabulary)
m["channels"] = [
    {"id": "CH-FILT-HOMA", "kind": "scale", "rule": "FILT", "degrade": "filt_miss", "members": ["Homa"], "latent": "member",
     "family": "exact_predicate"},
    {"id": "CH-FILT-BRIGHT", "kind": "scale", "rule": "FILT", "degrade": "filt_miss", "members": ["Brightwater Games Fund"],
     "latent": "member", "family": "exact_predicate"}]
m["hazard_acknowledgements"] = []
m["integration_exceptions"] = []
m["facts"] = [
    {"key": "Paul", "value": "out", "kind": "name", "must_appear_in": [SHA["D05S58U4SAK/1759251900.863415"]]},
    {"key": "Arthur's Play correction", "value": "Play console", "kind": "name", "must_appear_in": [SHA["C0880U9751A/1759274400.518306"]]},
    {"key": "Anton Bernstein", "value": "25", "kind": "amount",
     "home_ids": [SHA["D05S58U4SAK/1758731100.281734"], SHA["D05S58U4SAK/1758914100.640218"]],
     "version_records": [SHA["C07C2866011/1758303600.418207"], SHEET_ANG]},
    {"key": "keep-warm rule", "value": "Keep warm", "kind": "name", "must_appear_in": [NEW_KW]},
]
MSG = ids["MSGIDS"]
HUB_MSG = f"{FRED}/{MSG['g_hub']}"
m["anchors"][0]["record"] = m["anchors"][0]["locator"] = HUB_MSG
for f in m["ask_fragments"]:
    if f["delegated_by_record"] == ids["G_HUB"]:
        f["delegated_by_record"] = HUB_MSG
    if f["id"] in ("K1", "K2", "K3"):
        f["seeded_ids"] = [HUB_MSG, ids["G_HUB"]]
        f["locator"] = HUB_MSG
    if f["id"] == "K9":
        f["names_authorities"] = [{"id": "H2", "quote": "a Keep warm checklist on this card"}]
for t in m["traps"]:
    for v in t.get("version_records", []):
        if v.get("base_pointer") == f"{FRED}/1842285743246816270":
            v["base_pointer"] = "gmail:threads/frederick@harmonygames.co_1842285743246816270.json /messages/1"
    if t["id"] == "T10":
        t["version_records"] = [
            {"service": "gsheets", "base_pointer": "gsheets:data.json /sheets_spreadsheets/96", "seeded": False,
             "at": "2025-09-15T19:27:01Z", "container": "file:f_48247af79428823c3cac92"},
            {"service": "gmail", "base_pointer": "gmail:threads/frederick@harmonygames.co_1842283406259093714.json /messages/0",
             "seeded": False, "at": "2025-09-22T17:40:07Z", "container": f"gmail:{FRED}/1842283406259093714"}]
OLD_DENTSU = f"{FRED}/1844347876147200047"
EVT_HIRO = ids["EVT_HIRO"][FRED]
for t in m["traps"]:
    t["seeded_ids"] = [ids["G_DENTSU"] if x == OLD_DENTSU else x for x in t.get("seeded_ids", [])]
    if t["id"] == "T5":
        t["seeded_ids"] = list(dict.fromkeys(t["seeded_ids"] + [EVT_HIRO]))
        t["resolver"] = ("Edith Vane's Sep 26 pass (no firm name; cc the Investment Director from the Sep 3 Hiro thread) after the "
                         "Sep 23 Hiro pitch call on the calendar; Contacts: Partner, Hiro Capital")
for c in m["chains"]:
    for hp in c["hops"]:
        if hp["record"] == OLD_DENTSU:
            hp["record"] = ids["G_DENTSU"]
    if c["id"] == "C3" and not any(h["record"] == EVT_HIRO for h in c["hops"]):
        c["hops"].insert(1, {"service": "gcal", "record": EVT_HIRO,
                             "finding": "Tue Sep 23 call 'PERSON_5487_NAME and Leonard Hayes' (Hiro partner + Edith)"})
for w in m.get("writes", []):
    w["depends_on"] = [ids["G_DENTSU"] if x == OLD_DENTSU else x for x in w["depends_on"]]
m["design_delta"] = [
    {"id": "K9/H2/T8 trello comment", "change": f"comment id {OLD_KW} -> {NEW_KW}",
     "reason": "Trello ids carry the action's Unix seconds; the comment is dated 2025-09-14T04:20Z (Leonard's evening hours)"},
    {"id": "K10", "change": "container 67f446b4b0817af30d2d63f6 -> a new 'Board Deck - Oct 14' card (rev1-rev6; removed in rev7)",
     "reason": "the base Board Deck card is the April deck in Done; the Oct 14 note belongs on a new card"},
    {"id": "T1", "change": "the Paul record frederick.stone@harmonygames.co/1844610859008000037 is Leonard's Sep 29 nudge mail; Paul's state is shown by the absence of a DocuSign Completed notice beside Anton's",
     "reason": "the base DocuSign notices (SVC_1302) have Completed/request/viewed shapes but no reminder shape"},
    {"id": "T4", "change": f"added Leonard's 'Bridge angels' sheet {SHEET_ANG} as the middle version (3 versions)",
     "reason": "stale tracker in a third service; supplies the >= 3-version supersession"},
    {"id": "T3", "change": "version_records reduced to the SciPlay thread and Robert's reply",
     "reason": "both earlier entries were the same base thread (one timestamp per record)"},
    {"id": "ZOM-567", "change": "created 2025-09-30T17:10Z, comments 17:25Z and 18:40Z (design: Sep 24 / Sep 29)",
     "reason": "Linear numbers follow creation order: ZOM-566 was created 2025-09-30T16:26Z"},
    {"id": "channels", "change": "CH-SLIP dropped; FILT channels use kind 'scale'",
     "reason": "oracle_kit channel kinds; control rows are slips, not a complexity channel"},
    {"id": "hazard_acknowledgements", "change": "Q01 entry removed",
     "reason": "the SQL updates the root's reply counters (companion); Q hazards need no acknowledgement"},
    {"id": "companions", "change": "invitation mails for the Brightwater call (Frederick, Robert, Arthur) and the Oct 6 review (Frederick); Ilse's reply in the follow-up thread; deck-card Sections checklist",
     "reason": "INT-11 base rate; Brightwater's firm name in a reply signature; deck coordination record"},
]
m["design_delta"] += [
    {"id": "T5 / R6 (rev2)", "change": f"seeded the Hiro pitch call {EVT_HIRO} (Tue 2025-09-23 16:00-16:45Z, Leonard, the founders, "
     "PERSON_5487 and Edith Vane) on four calendars with invitation mails; Edith's pass now thanks Leonard for 'the session on Tuesday'",
     "reason": "platform /injection rev1 advisory 2: the Sep 3 Hiro thread is a re-intro email, not a call, so the base held no Hiro "
               "pitch call this round; the keep-warm rule (passes after a call or meeting) and Edith's wording need one"},
    {"id": "T2 Dentsu thread (rev2)", "change": f"thread {OLD_DENTSU} -> {ids['G_DENTSU']}: Ryo-san's Sep 26 03:10Z mail with the "
     "three tester addresses starts the thread; Leonard's 'invites are out' mail is its reply",
     "reason": "platform /injection rev1 advisory 4: Leonard's 'thank you for sending your emails' and Arthur's 'came in Fri' now "
               "point at a recorded message"},
    {"id": "H1 template population rule (rev2)", "change": "'one row per firm … a firm that shows up twice is one row' -> 'one row per name on the 2025 game investor list, angels included … a repeated name is still one row'",
     "reason": "known data issue SC-33 (watch): the list repeats Acterra, Progression Fund and BITKRAFT Ventures; the rule now settles the count and names the five angels' rows explicitly (the money rows sit on two of them)"},
    {"id": "Brightwater follow-up (rev2)", "change": "Leonard says he will send the deck and engine doc separately; Ilse will brief the partners",
     "reason": "platform /injection rev1 advisory 3: the mail claimed attachments that carry no attachment metadata"},
]
m["design_delta"] += [
    {"id": "K11 (rev3)", "change": "the register's columns moved from slide 9's speaker notes into its visible text; the Board Deck - Oct 14 card comment now reads 'Slide 9 of the draft deck lists the table's columns'",
     "reason": "platform /injection rev2 advisory 1: speaker-notes rendering is unverified (Ask_Carriers §5; no baseline trajectory shows notes), so the pointer could dangle"},
    {"id": "ZOM-567 Dentsu comment (rev3)", "change": "'came in Fri' -> 'came in Thursday night'",
     "reason": "platform /injection rev2 advisory 2: Ryo-san's mail is 2025-09-26T03:10Z = Thu Sep 25 20:10 PT"},
    {"id": "T6 Brightwater call (rev3)", "change": "2025-09-25 16:00-16:45Z -> 15:30-16:15Z (invitations 8:30-9:15am PDT)",
     "reason": "platform /injection rev2 advisory 3: clear of Leonard's base 1:1 evt_c6d85261f1e1dc58ddf1ad (16:30Z)"},
    {"id": "Trello board (rev3)", "change": "UPDATE trello_boards 640643a3fd8f3ca308d9318e dateLastActivity -> 2025-09-27T17:30:24Z",
     "reason": "platform /injection rev2 advisory 4: board activity follows the seeded card actions"},
]
m["design_delta"] += [
    {"id": "Initial Capital post (rev5)", "change": "Leonard root post C096HFA5Z8W/1757442000.492583 (Sep 9: pinged Initial Capital on LinkedIn about the bridge; they won't lead but might write a small check)",
     "reason": "platform /prompt review of rev4 (report 2) UGT fork F1: the list's 09/11 note implied contact but no Frederick-visible record showed our outreach; the row is now Awaiting reply"},
    {"id": "ZOM-567 comments and description (rev5)", "change": "T-Accelerate comment: TestFlight and Play internal track both added Sep 22 (was Play Sep 23; 'Rutik' and the unsupported 'Karthic confirmed it installs' dropped); Dentsu comment: TestFlight added Sep 26, Play not added because their work addresses aren't Google accounts (was 'no console owner rights'; matches Arthur's base Sep 23 'I have to add them by email for google play to work'); description reworded as a dated log",
     "reason": "platform /prompt review of rev4 DR2 (Cross-Service Coherence 3): base #executives Sep 22 16:30Z shows Arthur sending both invites himself; graded values unchanged (T-accelerate iOS and Android, Dentsu iOS only)"},
    {"id": "a16z speedrun feedback rule (rev5)", "change": "template: 'the program's decision and the feedback that comes with it aren't their answer on the bridge; that has to come on our bridge thread with them or in #bridge-pitch'",
     "reason": "author coherence sweep: the base Sep 30 speedrun feedback (frederick.stone@harmonygames.co/1844748127814183717) also discusses the bridge; the rule keeps a16z In talks with one reading (their bridge thread 1842277213140775733 has no answer)"},
    {"id": "Brightwater follow-up, deck agenda, Dentsu contact (rev5)", "change": "follow-up no longer promises a separate deck email; slide 2 agenda order matches the slides (Team, Runway and options, then Fundraising); new contact a4c2e9f07b31d85e6c0f1b29 Ryo Ishikawa, Dentsu Ventures (PERSON_5221_EMAIL)",
     "reason": "author coherence sweep: an unfulfilled promise, an agenda/slide order mismatch, and the Dentsu team (Ryo 石川 遼, PERSON_5221) not tied to the list row Dentsu Ventures in any record"},
    {"id": "Mattel post wording (rev5)", "change": "'that was only ever an RFP and partnership conversation' -> 'since the kickoff that's only been an RFP conversation, we haven't pitched them the bridge'",
     "reason": "platform /injection rev4 advisory 1: Leonard's Aug 26 email (before the kickoff) offered a small strategic investment"},
]
m["design_delta"] += [
    {"id": "H1 template status rules (rev4)", "change": "the Oct 14 template f_3b9e61c04d7a52e8f1a6c2 drops the 'Last two-way contact' column and adds the rules the platform /prompt review of rev3 found missing: only this round counts (the list's Status/comment columns, earlier-round answers and plans to reach out do not); a no to our pitch sent to Griffin or an advisor counts like a written phone pass; Awaiting reply holds even if they wrote back; outreach by someone introducing us counts and only bridge outreach counts (not RFP or partnership mail); angels who said yes are In talks with Build access blank; an accelerator decision (a16z speedrun) is not a bridge answer; soft-circled accepts a yes one of us wrote down; a call counts only when it is on Frederick's calendar (also for In talks); the list's Latest Status notes count as written (a note that they passed or don't do bridges is their no); a firm pitched the bridge or an investment alongside a co-dev deal counts even when co-dev or publishing was also on the table; banks (SVB), RFPs, publishing-only and engine-company calls are out; the kickoff day counts; one amount rule (latest amount the investor gave) for committed and soft-circled; build access is written iOS only / Android only / iOS and Android / none",
     "reason": "platform /prompt rev3 FAIL 2 (UGT forks F1-F9: Homa, Play Ventures, connector outreach, a16z, Paul's relayed yes, angel bucket, last-contact definition and window, 1AM Gaming); every status is now settled by a record or a template rule (solver accepted_status empty)"},
    {"id": "H2 keep-warm rule (rev4)", "change": "comment 68c64270d660c977c4696986: 'after we've actually pitched them (a call or meeting)' -> 'after we've actually pitched them on a call or meeting this round'",
     "reason": "earlier-round calls (Play Ventures 2023, Lakestar May 2025) would otherwise make a fourth keep-warm item defensible"},
    {"id": "K11 slide 9 (rev4)", "change": "slide 9's column list drops 'last two-way contact'; gradable surface register columns drop it too",
     "reason": "the column is ungraded and its definition forked twice in the platform review (our trailing reply; no window)"},
    {"id": "new #bridge-pitch posts (rev4)", "change": "three Leonard root posts in C096HFA5Z8W: 1757365500.384216 (Sep 8: 1AM Gaming is the March Gaming Fund row; they passed), 1758817200.730591 (Sep 25: Play's Sep 15 no was their reply to Griffin; still their no), 1758927000.205874 (Sep 26: Mattel was RFP/partnership only, not pitched the bridge)",
     "reason": "settle the 1AM Gaming mapping (fork F9), the Play Ventures contradiction (fork F2 and Cross-Service Coherence) and Mattel's hidden Sep 26/27 exchange (Cross-Service Coherence)"},
    {"id": "Treo VC post, Board Deck comment, Brightwater mail (rev4)", "change": "Leonard root post C096HFA5Z8W/1756942260.617302 (Sep 3: Treo pinged him on LinkedIn, deck sent); Board Deck - Oct 14 comment now reads 'how many firms are on it (every row, angels included)' and slide 9 'Firms on Fred's sheet'; Brightwater follow-up thanks Ilse for 'the questions on the bridge round'",
     "reason": "an author-run blind fork sweep of rev4 found Treo's contact date (Sep 2 warm-up vs Sep 3), the reply's firm count (79 / 77 / 74) and Brightwater's pitch as remaining two-reading points"},
]
m["design_delta"] += [
    {"id": "INPUT / T4 (rev6)", "change": "Anton's mail frederick.stone@harmonygames.co/1844162278195200023 removed from Frederick's mailbox (Anton's mail now goes to Leonard only, leonard.hayes@harmonygames.co copy); Leonard's DM to Frederick D05S58U4SAK/1758731100.281734 (Sep 24: Anton down to 25, voiding the 40 SAFE and re-sending at 25) and D05S58U4SAK/1758914100.640218 (Sep 26: Anton signed the 25 one) added; the template's 'For both, use the latest amount the investor gave us.' removed",
     "reason": "rev5 Opus pre-check (Platform_Report/hardness_report1, score 1): the trim was a top-level Sep mail the run's mailbox listing returned (01a_Hardening_Report.md, RB1); a DM is in no channel read"},
    {"id": "CORR / T3 / K8 (rev6)", "change": "Robert's #bridge-pitch root C096HFA5Z8W/1759161600.226431 and reply C096HFA5Z8W/1759184040.552871 removed (with the root counter update on C096HFA5Z8W/1757716998.377299); Robert's reply under Leonard's speedrun post C07C2866011/1759196326.309469 added as C07C2866011/1759248360.377105 (root counters updated); fragment K8 dropped; template Passed now 'they've told us no for this round' (phone-pass sentence and 'in writing' removed)",
     "reason": "rev5 pre-check: the template named #bridge-pitch and the run's threads-only search of that channel returned the reply (RB2)"},
    {"id": "DONE2 / T2 / K15 (rev6)", "change": "ZOM-567 Dentsu comment now logs the Play add (Sep 26) like T-Accelerate's; Arthur's #zombie-match3d post C0880U9751A/1759274400.518306 (the Play investor tester list was never attached to the internal testing track; TestFlight fine) and Leonard's thread reply C0880U9751A/1759276080.094417 ('ping me when it's live') added; Arthur will attach the list with his Oct 1 build push; build access definition now 'whether they can get the current internal build'; fragment K15 (Arthur's post, delegated by 'Arthur tracks the tester adds'); T-Accelerate build access iOS and Android -> iOS only",
     "reason": "rev5 pre-check: the ticket carried its own caveat, so the done source had no gap (RB3)"},
    {"id": "coherence sweep (rev6)", "change": "Arthur's post no longer claims he lacks Play console rights (he attaches the list with the Oct 1 build) and names ZOM-567; Treo post 'pinged me again'; Play correction acknowledges Robert's 'discussing' relay; template 'go only by the Latest Status notes'; Arthur's invitation copies in Eastern time; Board Deck card idShort 466 -> 456",
     "reason": "independent seeded-vs-base sweep: CD843DBC4C3E/1759244974.454399, D04UC0UEN2V/1756878703.235739, C096HFA5Z8W/1758764726.605039, list comment column, Arthur's base invitations (EDT), board max idShort 455"},
    {"id": "LVP list date (rev8)", "change": "UPDATE gsheets.sheets_sheets for f_48247af79428823c3cac92 sheet 0: the base grid with one cell changed, row No. 8 (London Venture Partners) Latest Status 'Pitch/Catch up on 09/07' -> '09/09'",
     "reason": "platform /prompt of rev7 (Platform_Report/prompt_report5): NON-FAIL 3 on Cross-Service Coherence only, the base list's 09/07 (a Sunday) against the Sep 9 call on the calendar, in #bridge-pitch and in Fred's Sep 12 mail (SC-10); the review's minimum fix"},
    {"id": "ALIAS (rev6)", "change": "template sentence 'A partner writing from their own address counts for their firm. If the name doesn't ring a bell, check contacts and the earlier threads.' removed",
     "reason": "rev5 pre-check: the hint sent the run to Contacts (RB4); the mapping stays in Contacts e3a91c07d5b48f26a0c7e314 and the cc of PERSON_5282"},
]
m["design_delta"] += [
    {"id": "job (rev7)", "change": "the task is now the bridge part of the Q4 investor update send list: hub subject 'Q4 investor update - send list'; the Oct 14 template f_3b9e61c04d7a52e8f1a6c2 becomes the 'Q4 investor update - send list' rules doc (groups New investor / In talks / Awaiting reply / Keep warm; email-only passes and uncontacted firms stay off; same population, status and build-access rules as rev6); the July template f_8d2c47a91e05b3f6d7c418 becomes the Q3 (July) send list decoy (new investor = a yes with an amount); folder d_5e8a1c3f9b07d2e64a1b93 renamed 'Q4 2025 investor update' with its README; the deck f_a47d0e2c95b18f63e2c0d5 becomes the draft Q4 update (bridge slide says what each group gets); the Board Deck card, its checklist and comment are removed (K10 dropped); Leonard's #executives note on what counts as signed added (K17, C07C2866011/1758911700.336170); Robert's mail and Arthur's aside re-aimed at the send list; the review event renamed",
     "reason": "platform /prompt of rev6 (Platform_Report/prompt_report4): every content dimension 5, FAIL only on the new STEP 0.6 dataset-duplicate gate (meaning 0.804 to another contributor's Frederick task on the Oct 14 board pre-read handoff); the request had to become a different job"},
]
m["design_delta"] += [
    {"id": "T2 correction placement (rev10)", "change": "Arthur's Sep 30 correction 3cddf83c394676d8b72c0c20ed58f520 and Leonard's "
     "reply move from their own #zombie-match3d thread into the thread under Leonard's base Sep 29 post 'I just released 0.3.49 "
     "on IOS' (c891232a8b395a701268cff14cffd883; root reply counters updated). The text now names the Play console group, the "
     "internal track, Karthic, the Dentsu folks and the Linear log, not tester, TestFlight or ZOM-567",
     "reason": "platform /hardness of rev9 (Platform_Report/hardness_report3): score 1; the run's Slack search for 'tester' "
               "returned the root post directly. Hardness v2 Part 3.2 and the reviewer's suggestion 1"},
    {"id": "T1 done claim (rev10; removed in rev11)", "change": "Paul's reply frederick.stone@harmonygames.co/<CAA_lm07dfuR9zTKG5Xh1lma8QW1_dNi4pJJcvpJ@mail.gmail.com> (Sep 30 8:40 AM PT, to Leonard, cc Frederick) on "
     "Leonard's Sep 29 nudge thread: 'Done, signed it last night'. No DocuSign Completed notice for Paul exists",
     "reason": "hardness_report3 suggestion 2 and Hardness v2 Part 3.1: the 'still sitting with you' nudge was a caveat Opus "
               "could see (Part 4). Leonard's #executives note (only a Completed notice counts; them telling us doesn't) "
               "settles Paul as In talks, so the truth is unchanged"},
]
m["design_delta"] += [
    {"id": "T1 / DONE1 Paul backs out (rev11; relay moved to the DM in rev12)", "change": f"Paul's rev10 'Done, signed it' reply removed. Paul writes Leonard only "
     f"({ids['G_PAUL_OUT_LEO']}, Sep 30 7:55 AM PT, reply on the nudge thread without Frederick) that he has to back out; Leonard "
     "replies under his own Sep 19 #executives angel post (C07C2866011/1759251900.863415, Sep 30 10:05 AM PT): 'Paul's out, he "
     "wrote me this morning that he can't put money in this year after all' (root reply counters set). Truth: Paul passed "
     "without a call and is off the send list (25 entries; In talks 7 firms, 0 angels; 18 follow-up cards). Rule DONE1 is now "
     "a correction in a thread reply (A14); INPUT's control moves to GFR Fund",
     "reason": "rev10 baseline (6 Opus 5.5 runs, run_forensics/rev10/baseline/baseline_review.md): Paul caught 7 of 7, so the "
               "trap added no variation; runs 1, 3, 5 and 6 failed the same values (signature over-concentrated, SD about "
               "0.04). A partly-caught trap landing on several rows (row, checklist item, card, counts) spreads the signatures"},
    {"id": "T2 / DONE2 T-Accelerate correction (rev11; removed in rev12)", "change": "Karthic's report frederick.stone@harmonygames.co/<CAz_RUxJqfvgfKAkYtz-r7Yoht-mPT7mOKAMrJNp@mail.gmail.com> (Sep 30 10:20Z) and "
     "Arthur's answer frederick.stone@harmonygames.co/<CAU8zEO-shvUXQVk4-lQPDj5ihq08pcABtHRrtUv@mail.gmail.com> (Sep 30 1:05 PM PT: the Play tester list the investor accounts are on was never "
     "attached to the internal test track, nobody on it has the Android build yet) added to the base T-Accelerate thread "
     "(four mailbox copies; thread snippets set to Arthur's reply). Arthur's #zombie-match3d reply now covers the 3 Dentsu "
     "folks only ('either'); Leonard's answer names Ryo-san only",
     "reason": "rev10 baseline: build access was missed 7 of 7 (one choke point shared by every run). A second, findable "
               "record in the investor's own thread lets some runs fix both cells and others neither; truth unchanged"},
]
m["design_delta"] += [
    {"id": "T1 / DONE1 Paul's out moves to the DM (rev12)", "change": "Leonard's 'Paul's out, he wrote me this morning that he "
     "can't put money in this year after all' moves from the reply under his Sep 19 #executives angel post "
     "(C07C2866011/1759251900.863415, removed; the angel post has no replies again) to his 1:1 DM with Frederick "
     "(D05S58U4SAK/1759251900.863415, same time). Truth unchanged: Paul is off the send list",
     "reason": "rev11 baseline (6 Opus 5.5 runs, run_forensics/rev11/baseline/baseline_review.md): every run reached the angel "
               "post through its own SAFE/DocuSign search and opened its thread (7 of 7). The DM was opened by 6 of 15 Opus "
               "runs across rev9-rev11, independently of the SciPlay thread (4 of 15)"},
    {"id": "T2 / DONE2 Arthur's root post, four firms (rev12)", "change": "the rev11 T-Accelerate mail replies (Karthic's report, "
     "Arthur's answer; eight mailbox rows and four thread-snippet updates) are removed, as is the rev11 reply placement under the "
     "0.3.49 release post (its counters are base again). Arthur's correction 3cddf83c394676d8b72c0c20ed58f520 is a root post in "
     "#zombie-match3d again (Sep 30 4:20 PM PT, one reply from Leonard), saying 'investor tester list' and naming Karthic, the 3 "
     "Dentsu folks, Anel's two at NCsoft and Ilse from Brightwater; no TestFlight, no ticket id. ZOM-567 logs NCsoft (Sep 22) "
     f"and Brightwater (Sep 26) too ({ids['LIN_C_NCSOFT']}, {ids['LIN_C_BRIGHT']}). Truth: NCsoft and Brightwater Build access "
     "iOS only (was none); DONE2's control moves to GFR Fund",
     "reason": "rev11 baseline: the T-Accelerate thread was read in full by 7 of 7 runs, so the cells never varied. A Slack search "
               "for 'tester' (the README's own word) was run by 5 of 15 Opus runs and returned nothing in rev10/rev11; firm-name "
               "searches add a few more. Four cells instead of two make the trap carry enough weight for the 0.1 spread floor"},
]
sp = WF / "solver/solver.py"
m["solver"] = {"path": "Working_Files/solver/solver.py", "digest": hashlib.sha256(sp.read_bytes()).hexdigest()}
m["gradable_surface"] = "01_Gradable_Surface.json"
(WF / "01_Hardness_Manifest.json").write_text(json.dumps(m, indent=1, ensure_ascii=False) + "\n")
print("final manifest written;", len(m["design_delta"]), "design_delta entries")
