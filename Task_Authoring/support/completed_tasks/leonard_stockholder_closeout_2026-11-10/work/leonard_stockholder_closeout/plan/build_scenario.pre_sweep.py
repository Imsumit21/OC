#!/usr/bin/env python3
"""Single source of truth for the Leonard stockholder close-out design.
Writes 01_Hardness_Manifest.draft.json and 01_Gradable_Surface.json. assemble_design.py builds the dossier from the same data.
Design only: no prompt, Oracle Event or criterion text. Seeded ids come from research/s4_carrier_formats.md (collision-checked)."""
import hashlib, json, os

H = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(H)
CTX = json.load(open(os.path.join(WF, "00_Task_Context.json")))

MB = "leonard.hayes@harmonygames.co"
WD, DMS, DMR, DMA, DMT, GRP = "C0ADGSZKR3R", "D04UC0UEN2V", "D04UP2L3E3S", "D04UGG61DUM", "D09R59580EM", "C51ECE5102ED"
ADMIN, DMV = "C04UEQVDVB7", "D05PX3R13QF"
PROJECT = "ec2ea957-fc8e-4958-b809-0fb735b1e916"
FOLDER, DOC_NOTES, DOC_OLD = "d_601064334a0b493022fe83", "f_a37b403d5200d4f0a31d31", "f_762c60832854d3e7a7f7df"
SHEET, DECK = "f_5ecaa967db3adcfa440b09", "f_75dddccabb26eeea4842c8"
TH_KPMG, TH_SUNSET = f"{MB}/1857029474983245439", f"{MB}/1857034369525983506"
TH_ROBERT = f"{MB}/1857000911304835072"
EVT_HOLD = "evt_6f1a2c9e4b7d3a58c0e1d2"
TRELLO_CARD = "698e5a10c3f24b7e9d16a0e4"
SL_ORIGIN = f"{WD}/1770938120.410229"     # planned: Leonard says why the holders sit in Linear
SL_AMEND = f"{DMA}/1770949310.220519"     # planned: Leonard to Arthur, one change to the sharing

# Base Gmail messages, cited by RFC id because the gate reads a message's own timestamp
M_LIST = f"{MB}/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com>"
M_ES14 = f"{MB}/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv>"
M_ES13 = f"{MB}/<177093559600.10.6851662374290149851@notifications-email-sending-worker-5fc9459db-b2dtx>"
M_ES17 = f"{MB}/<176175429549.10.8466995912642267217@notifications-email-sending-worker-6b65bf6cf7-gcpxf>"
M_FRED = f"{MB}/<CAPBs_a6mwZj_4JRyPpidJCWgK9auo+34NVhirFGhKMHi3d5OmA@mail.gmail.com>"
M_MATT = f"{MB}/<CAMy0Hx1va3q4zH2HyPiqfm8Je2fm5A=JHKf8LrXWb12z2FHr6w@mail.gmail.com>"
M_PHIL = f"{MB}/<BYAPR02MB435880CCF501BE0AE906AFFDC460A@BYAPR02MB4358.namprd02.prod.outlook.com>"
M_TLAS = f"{MB}/<BY3PR13MB48333BC5C19C3EC4EC8B3F28A6F2A@BY3PR13MB4833.namprd13.prod.outlook.com>"
M_CLARK = f"{MB}/<BL0PR1501MB20995F0276101A153B2CC9DC99F7A@BL0PR1501MB2099.namprd15.prod.outlook.com>"
M_SIGN = f"{MB}/<CAPBs_a46H9SCR=PBn1EP4RvCL+HO3XqOma4mTNu0WdnWv17ZuA@mail.gmail.com>"
M_K24 = f"{MB}/<LV3PR19MB8524A7F34357829DDCA90153CA302@LV3PR19MB8524.namprd19.prod.outlook.com>"
M_ENES = f"{MB}/<A658306E-3D13-458C-A311-95454D575822@librasoftworks.com>"
M_BROS = f"{MB}/<0CDD5A07-0BE6-4909-8188-93E10FBF4E16@librasoftworks.com>"
M_VINC = f"{MB}/<CAEH8bLxfNq9vp7-VSMQdpetPWQxBhv2pcPE=xj=oX9c8MxNFtA@mail.gmail.com>"
M_BRIAN = f"{MB}/<CAPBs_a68Agj+37mZ6abeW5KEKTh00he+mgOpLP2FrpDjeO-37Q@mail.gmail.com>"
D_TERM, D_SIDE, D_SPA, D_DD = "gdocs:data.json /docs_documents/40", "gdocs:data.json /docs_documents/238", "gdocs:data.json /docs_documents/381", "gdocs:data.json /docs_documents/262"
D_CHARTER = "gdocs:data.json /docs_documents/360"
S_DRAFT, S_ONEBYONE, S_LETTERS, S_LIST, S_CARTA = (f"{WD}/1770664700.848759", f"{WD}/1770664924.520089", f"{WD}/1770841239.761999",
                                                  f"{WD}/1770934638.035469", f"{WD}/1770935621.095649")
S_PROMISE, S_SEG = f"{DMS}/1770665186.368229", f"{DMS}/1770664988.379119"
S_CLAIRE, S_TOR, S_VINC = f"{GRP}/1770903714.600249", f"{DMT}/1762285888.654689", f"{DMV}/1763665854.644329"
S_LISTSLACK = f"{ADMIN}/1732646280.941869"

# Holder project: one issue per non-founder holder. Rows are keyed by issue, because SSP-06/08 cannot be told apart on the record.
HOLDERS = [  # issue, holder (as the records show), id, class
 ("ENG-2438", "Griffin Gaming Partners II, L.P.", "SSP-01", "Already told"),
 ("ENG-2439", "Griffin Gaming Partners II Side Fund, L.P.", "SSP-02", "Already told"),
 ("ENG-2440", "Segerstrale", "SSP-03", "Already told"),
 ("ENG-2441", "Schaeppi", "SSP-04", "First note"),
 ("ENG-2442", "Bergmann", "SSP-05", "First note"),
 ("ENG-2443", "Enes Disli", "SSP-06/08", "First note"),
 ("ENG-2444", "Patrick Lewis", "SSP-06/08", "Covered"),
 ("ENG-2445", "Eren Disli", "SSP-07", "Covered"),
 ("ENG-2446", "Nebojsa", "SSP-09", "First note"),
 ("ENG-2447", "Matthew Collins", "SSP-10", "First note"),
 ("ENG-2448", "TOR Capital Limited", "SSP-11", "First note"),
 ("ENG-2449", "Deepak", "SSP-12", "Already told"),
 ("ENG-2450", "Julia Lawson", "ES-1", "Date note"),
 ("ENG-2451", "[PERSON_NAME_0100]", "ES-2", "Nothing"),
 ("ENG-2452", "Calvin Price", "ES-3", "Nothing"),
 ("ENG-2453", "Claire Morgan", "ES-4", "Date note"),
 ("ENG-2454", "Douglas", "ES-5", "Nothing"),
 ("ENG-2455", "Victor Barnes", "ES-6", "Nothing"),
 ("ENG-2456", "Marcus Bennett", "ES-7", "Date note"),
 ("ENG-2457", "Owen Baker", "ES-12", "Date note"),
 ("ENG-2458", "Martin Walsh", "ES-13", "Date note"),
 ("ENG-2459", "Vincent Parker", "ES-14", "Full note"),
 ("ENG-2460", "Brian Foster", "ES-15", "Date note"),
 ("ENG-2461", "[PERSON_NAME_2768] [PERSON_NAME_0011]", "ES-16", "Nothing"),
 ("ENG-2462", "Frederick Stone", "ES-17", "Nothing"),
 ("ENG-2463", "Oliver Brooks", "ES-18", "Full note"),
]
I = {h[2]: h[0] for h in HOLDERS if "/" not in h[2]}
I["ENES"], I["PAT"] = "ENG-2443", "ENG-2444"

REQS = {
 "R1": "holder schedule: one row per project issue with holder, instrument and shares held now",
 "R2": "live or lapsed state and last day of every option line, from Carta",
 "R3": "stock apart from advisor options on merged lines, and the Series Seed total",
 "R4": "told column: who has already had a personal written message about the closing",
 "R5": "what is owed to each holder under the closed rule",
 "R6": "personal notes by class, with the earliest last day going first",
 "R7": "notice route for each holder, including side letter terms",
 "R8": "KPMG confirmation: share counts and options outstanding at the as-of date, plus later events",
 "R9": "directors in office and the preferred vote, with a heads-up to Griffin",
 "R10": "investor letter updated from the draft",
 "R11": "project issue states by what is owed, and a reason comment where no note goes",
 "R12": "an answer to any open written equity question on a live line",
 "R13": "destination, sharing and the founders' thread reply",
}

def surf(service, tool, per, rec, req, decides, nb, sc, seeded=False, ids=None):
    d = {"service": service, "tool": tool, "per_record_calls": per, "records": rec, "seeded": seeded, "requirement": req, "decides": decides,
         "why_no_bulk": nb, "short_circuit": sc}
    if ids: d["seeded_ids"] = ids
    return d

def vr(service, ref, at, container, seeded=False):
    d = {"service": service, "seeded": seeded, "at": at, "container": container}
    d["id" if seeded else "base_pointer"] = ref
    return d

def trap(id_, family, services, req, wrong, resolver, seeded=(), base=(), disc=None, versions=None, dtype=None):
    d = {"id": id_, "family": family, "services": list(services), "seeded_ids": list(seeded), "base_pointers": list(base), "requirement": req,
         "expected_wrong_reading": wrong, "resolver": resolver}
    if disc: d["discovery_order"] = disc
    if versions: d["version_records"] = versions
    if dtype: d["distractor_type"] = dtype
    return d

TRAPS = [
 trap("T1", "exact_predicate", ["gmail", "gdocs"], "R3",
      "the owner list's 86,470, 81,383 and 31,536 lines are stock, so Series Seed sums too high or the difference goes unnoticed",
      "Due Diligence Disclosures' advisor table: four angels also hold advisor options, 103,764 in all, and only the subtraction ties to the term sheet's 3,051,879",
      base=[M_LIST, D_DD], disc="the owner list is one read and carries every line; the advisor table is a 2023 doc with no holder word in its title"),
 trap("T2", "stale_summary", ["gmail", "slack"], "R1",
      "the Nov 2024 owner list is the current holder list, with option grants as shares and Griffin as one line",
      "Carta's certificates and awards: option lines are not stock, and Griffin is two fund lines", base=[M_LIST, S_LISTSLACK],
      disc="a search on any holder figure returns the owner list first"),
 trap("T3", "superseding", ["gdocs", "gmail"], "R2",
      "options outstanding are the term sheet's 268,772",
      "Carta's Feb 12 entries move the count after the Jan 22 snapshot: 159,706 live at the clock",
      base=[D_TERM, M_ES14], versions=[vr("gdocs", D_TERM, "2026-01-23T00:09:05Z", "file:f_11040fe5d66821bd6951aa"),
                                       vr("gmail", M_ES14, "2026-02-12T22:31:54Z", "gmail:1856960478782792748")]),
 trap("T4", "done_gap", ["slack", "gmail"], "R5",
      "'All termination letters are sent' means every Carta termination has a letter, so ES-14 and ES-18 were told like the others",
      "Six letters exist against eight Feb 12 Carta entries; matching letter recipients to Carta addresses leaves ES-14 and ES-18 with no letter",
      base=[S_LETTERS, M_ES14, M_BRIAN], disc="Leonard's own #winddown line says the letters are done; the gap shows only by joining recipients to Carta"),
 trap("T5", "conclusion_stop", ["slack", "gmail"], "R6",
      "'Carta terminations are done' closes the option side, so nothing more is owed to live holders",
      "The letters only promise a Carta mail; no holder-facing record gives any live holder a last day, so a date note is still owed",
      base=[S_CARTA, M_BRIAN]),
 trap("T6", "completion_elsewhere", ["slack"], "R4",
      "Leonard's Feb 12 list says the angels are still to do, so Segerstrale gets a first note",
      "Leonard's Feb 9 DM told him personally", base=[S_LIST, S_SEG], disc="#winddown is read first; the DM is off every channel listing"),
 trap("T7", "completion_elsewhere", ["slack", "gmail"], "R4",
      "no angel but Segerstrale has been told, so Deepak gets a first note",
      "NEW Robert's Feb 13 mail to Deepak, Leonard copied, tells him about the closing",
      seeded=[TH_ROBERT], base=[S_LIST], disc="a mail with no holder word in its subject, found only by reading recent mail or searching his address",
      versions=[vr("slack", S_LIST, "2026-02-12T22:17:18Z", f"slack:{S_LIST}"), vr("gmail", TH_ROBERT, "2026-02-13T05:12:00Z", "gmail:1857000911304835072", True)]),
 trap("T8", "near_miss_mention", ["slack"], "R5",
      "Tor was told in November, so he needs nothing",
      "The Nov 4 DM warned of about three months of runway; nothing says the company is closing, so Tor still gets a first note", base=[S_TOR]),
 trap("T9", "superseding", ["gdocs", "gmail"], "R7",
      "the side letter in Drive binds Tor alone",
      "The 2023 mail chain adds Segerstrale as a party and he signed it, so both lines carry the side letter route",
      base=[D_SIDE, M_TLAS, M_CLARK, M_SIGN],
      versions=[vr("gdocs", D_SIDE, "2023-08-28T22:12:51Z", "file:f_6201c7027d02997bfb2c84"), vr("gmail", M_TLAS, "2023-09-11T22:49:35Z", "gmail:1775602109531090463"),
                vr("gmail", M_CLARK, "2023-09-14T18:56:10Z", "gmail:1775602109531090463"), vr("gmail", M_SIGN, "2023-09-20T20:03:08Z", "gmail:1777052222643175480")]),
 trap("T10", "superseding", ["gdocs", "gmail"], "R9",
      "the board is the four named in the financing documents",
      "Matthew's May 1, 2025 mail and Phil's Feb 12, 2026 mail leave Leonard and Robert",
      base=[D_SPA, M_MATT, M_PHIL],
      versions=[vr("gdocs", D_SPA, "2023-06-21T15:53:29Z", "file:f_966445655f653d26dc8537"), vr("gmail", M_MATT, "2025-05-01T22:42:49Z", "gmail:1830959847543474636"),
                vr("gmail", M_PHIL, "2026-02-12T22:05:07Z", "gmail:1856958794180374704")]),
 trap("T11", "authority", ["gmail", "gdocs"], "R9",
      "Griffin's director resigned, so Griffin has nothing left to sign",
      "The charter's protective provision is a vote of the preferred, not a board seat; Griffin holds 90.0 % of the preferred",
      base=[M_PHIL, D_CHARTER]),
 trap("T12", "effective_date", ["gmail"], "R8",
      "KPMG gets today's holdings, or last year's as-of date",
      "NEW FY25 request fixes Dec 31, 2025 and asks that terminations effective by then be reflected; entries made in February carry earlier effective dates",
      seeded=[TH_KPMG], base=[M_K24, M_ES14],
      versions=[vr("gmail", M_K24, "2024-12-05T00:22:55Z", "gmail:1817557789846606177"), vr("gmail", TH_KPMG, "2026-02-13T16:48:33Z", "gmail:1857029474983245439", True)]),
 trap("T13", "entity_collision", ["gmail", "slack"], "R6",
      "three record holders mean three separate first notes",
      "Enes has handled everything for the three Disli lines; NEW the close-out notes say one note to the person who speaks for a family covers its lines",
      seeded=[DOC_NOTES], base=[M_ENES, M_BROS], disc="the owner list shows no shared surname: 'Patrick Lewis' reads as unrelated"),
 trap("T14", "scope_alias", ["gmail", "slack"], "R1",
      "'Patrick' is one person",
      "The wires and owner list separate Bergmann from the Disli line", base=[M_LIST]),
 trap("T15", "distractor", ["gmail", "slack"], "R2",
      "the roster's co-founder holds a founder's stake",
      "ES-17 is an option line that lapsed; Frederick Stone holds nothing at the clock", base=[M_ES17], dtype="lookalike_entity"),
 trap("T16", "distractor", ["gmail"], "R2",
      "ES-17's letter figures (34,409, Jan 22) are the record",
      "The letter itself says Carta shows the exact numbers: 34,439 and Jan 28, both before the clock", base=[M_FRED, M_ES17], dtype="near_duplicate_record"),
 trap("T17", "synthesis_omission", ["slack", "gmail"], "R12",
      "Claire's note only needs her date",
      "Her Feb 12 group-DM question about equity was never answered, and the closed rule says an open question on a live line is answered in the note",
      base=[S_CLAIRE], disc="the group DM is not a channel; Leonard's reply in it answers a different question"),
 trap("T18", "superseding", ["gdocs"], "R5",
      "the earlier notes doc still governs",
      "NEW the later close-out notes replace it", seeded=[DOC_OLD, DOC_NOTES],
      versions=[vr("gdocs", DOC_OLD, "2026-02-10T17:40:00Z", f"file:{DOC_OLD}", True), vr("gdocs", DOC_NOTES, "2026-02-13T01:05:00Z", f"file:{DOC_NOTES}", True)]),
 trap("T19", "distractor", ["gslides"], "R10", "the outline deck's numbers are current", "NEW deck dated before the Feb 12 entries carries the term sheet's count",
      seeded=[DECK], dtype="stale_summary"),
 trap("T20", "distractor", ["gsheets"], "R1", "the draft sheet is the holder list", "NEW partial sheet dated before the Carta entries", seeded=[SHEET], dtype="partial_listing"),
 trap("T21", "distractor", ["trello"], "R10", "the investor update is done because its card sits in Done", "the card has no description and no update followed it",
      base=["68c5a49e8491a9d7faf869d0"], dtype="already_done"),
 trap("T22", "distractor", ["gmail"], "R8", "last year's as-of date applies", "FY24 was Sep 30, 2024; the FY25 request names its own date", base=[M_K24], dtype="scope_adjacent"),
]

FRAGS = [
 ("K1", "slack", S_DRAFT, "requirement", ["AN1"], [], [S_DRAFT], S_DRAFT, "I will send periodic updates as we complete the major steps", ["R10"], []),
 ("K2", "slack", S_ONEBYONE, "requirement", ["AN2", "K6", "K7"], [], [S_ONEBYONE], DOC_NOTES, "the reach-out I promised", ["R6"], []),
 ("K3", "slack", S_PROMISE, "requirement", ["AN2", "K6", "K7"], [], [S_PROMISE], DOC_NOTES, "every angel investor", ["R6"], []),
 ("K4", "slack", S_LIST, "requirement", ["AN2", "K6", "K7"], [], [S_LIST], DOC_NOTES, "where I left things on Thursday", ["R4"], []),
 ("K5", "gsheets", "f_31115ddb6ed866f2b10d60", "requirement", ["AN2", "K6", "K7"], [], ["gsheets:data.json /sheets_spreadsheets/76/sheets/0/grid/2/1"],
  DOC_NOTES, "the investor email on the Task List", ["R10"], []),
 ("K6", "linear", f"linear:project/{PROJECT}", "delegation", ["AN2"], [PROJECT], [], PROJECT, "one issue per holder on Carta, live or lapsed", ["R1", "R11"],
  [{"id": "H1", "quote": "my close-out notes"}]),
 ("K7", "gdocs", DOC_NOTES, "requirement", ["AN2", "K6"], [DOC_NOTES], [], PROJECT, "my close-out notes have how each holder gets handled", ["R4", "R5", "R12"],
  [{"id": "H2", "quote": "Carta is the record"}]),
 ("K8", "gmail", TH_SUNSET, "requirement", ["AN2", "K6"], [TH_SUNSET], [], PROJECT, "what Sunset asked for", ["R1", "R2", "R3", "R7", "R9"],
  [{"id": "H3", "quote": "any side letter terms"}]),
 ("K9", "gmail", TH_KPMG, "requirement", ["AN3"], [TH_KPMG], [], TH_KPMG, "as of December 31, 2025", ["R8"], [{"id": "H4", "quote": "2025 Audit Request"}]),
 ("K10", "trello", TRELLO_CARD, "destination", ["AN2", "K6", "K7"], [TRELLO_CARD], [], DOC_NOTES, "the holder sheet comes first", ["R13"], []),
 ("K11", "gcal", EVT_HOLD, "requirement", ["AN2", "K6", "K7"], [EVT_HOLD], [], DOC_NOTES, "notes ready for me by Tuesday", ["R6"], []),
 ("K12", "gslides", DECK, "format", ["AN2", "K6", "K7"], [DECK], [], DOC_NOTES, "the update outline", ["R10"], []),
 ("K13", "gdrive", FOLDER, "destination", ["AN2", "K6", "K7"], [FOLDER], [], DOC_NOTES, "everything goes in the close-out folder", ["R13"], []),
 ("K14", "slack", SL_AMEND, "amendment", ["AN2", "K6", "K7"], [SL_AMEND], [], DOC_NOTES, "if the sharing changes I'll say in the DM", ["R13"], []),
 ("K15", "slack", SL_ORIGIN, "delegation", ["AN2", "K6"], [SL_ORIGIN], [], PROJECT, "as I said in #winddown", ["R11"], []),
]
def frag(t):
    id_, svc, cont, kind, via, seeded, base, by, quote, reqs, names = t
    d = {"id": id_, "service": svc, "container": cont, "locator": cont, "kind": kind, "incorporated_via": via, "seeded_ids": seeded, "base_pointers": base,
         "delegated_by_record": by, "delegation_quote": quote, "requirement_ids": reqs}
    if names: d["names_authorities"] = names
    return d

PORTFOLIO = [
 {"id": "ADV", "mechanism": "A17", "prior_family": "A17", "prior_family_reason": "in-scope grants sit inside merged lines and outside the obvious Carta search", "nodes": ["T1", "T2", "C1"], "requirement": "R3",
  "natural_reading": "the owner list's figure is the holder's stock", "decides": ["K1", "K4", "K5", "K6", "K7", "K8", "P1", "NC_Collins", "NC_Nebojsa"],
  "controls": ["Schaeppi", "Bergmann"], "over_application": "adv_over: subtracts an advisor grant from a plain $25,000 line", "source": "doc-table", "signature": "Due Diligence advisor table 103,764"},
 {"id": "LETTER", "mechanism": "A24", "prior_family": "A24", "prior_family_reason": "a founder's done statement with a missing piece shown only by joining two records", "nodes": ["T4", "T5", "C2"], "requirement": "R5",
  "natural_reading": "every Carta termination had a letter, so every live option holder has been told", "decides": ["C_ES14", "C_ES18", "C_DATE", "N_Vincent", "N_Oliver", "D6"],
  "controls": ["Julia Lawson", "Brian Foster"], "over_application": "letter_over: treats a holder with a real letter as untold", "source": "founder-claim", "signature": "six letters against eight entries"},
 {"id": "TOLD", "mechanism": "A25", "prior_family": "A25", "prior_family_reason": "a completion record sits away from the list that says the work is open", "nodes": ["T6", "T7", "T8", "C3"], "requirement": "R4",
  "natural_reading": "the Feb 12 list means no angel has been told", "decides": ["C_SEG", "C_DEEPAK", "C_TOR", "C_FIRST", "LC_Seg", "LC_Deepak"],
  "controls": ["TOR Capital Limited"], "over_application": "told_over: treats Tor's November runway warning as being told", "source": "dm-and-mail", "signature": "Feb 9 DM; Robert's Feb 13 mail"},
 {"id": "ASOF", "mechanism": "A19", "prior_family": "A19", "prior_family_reason": "the deciding figure must be derived from effective dates, not read off a record", "nodes": ["T12", "C4"], "requirement": "R8",
  "natural_reading": "the confirmation reports today's option count or the term sheet's", "decides": ["A1", "A2"],
  "controls": ["Series Seed share count"], "over_application": "asof_over: back-dates the stock lines", "source": "derived", "signature": "243,757 options at Dec 31, 2025"},
 {"id": "FAM", "mechanism": "A7", "prior_family": "A7", "prior_family_reason": "one person speaks for lines whose names do not show the link", "nodes": ["T13", "T14", "C7"], "requirement": "R6",
  "natural_reading": "three record holders get three notes", "decides": ["F1", "F2", "F3", "N_COUNT"],
  "controls": ["Schaeppi and Bergmann, who share a company but each answer for themselves"], "over_application": "fam_over: folds the Solsten pair into one note", "source": "old-mail", "signature": "all three brothers"},
 {"id": "SIDE", "mechanism": "A15", "prior_family": "A15", "prior_family_reason": "a signed term overrides the Drive copy for a second holder", "nodes": ["T9", "C6"], "requirement": "R7",
  "natural_reading": "the side letter binds Tor alone", "decides": ["S3", "S1", "S2"],
  "controls": ["Matthew Collins, an ordinary line"], "over_application": "side_over: gives an ordinary holder the side letter route", "source": "old-mail", "signature": "Segerstrale signed the side letter"},
 {"id": "BOARD", "mechanism": "A11", "prior_family": "A11", "prior_family_reason": "a dated resignation in mail overrides board lists in documents", "nodes": ["T10", "T11", "C5"], "requirement": "R9",
  "natural_reading": "the document board list stands and Griffin has nothing left to do", "decides": ["B1", "B2", "L6", "G2"],
  "controls": ["Robert, who stays on the board"], "over_application": "board_over: drops Robert with the outside directors", "source": "mail", "signature": "May 1, 2025 resignation"},
 {"id": "ASK", "mechanism": "A9", "prior_family": "A9", "prior_family_reason": "a written question with no matching reply", "nodes": ["T17", "C8"], "requirement": "R12",
  "natural_reading": "Claire's note only needs her date", "decides": ["Q1", "Q2"],
  "controls": ["ES-16's exercise thread, on a lapsed line"], "over_application": "ask_over: writes to a lapsed holder because they once asked", "source": "group-dm", "signature": "Claire's equity question"},
]
CHANNELS = [
 {"id": "CH-LIVE", "kind": "scale", "degrade": "ch_miss", "latent": "member", "family": "exact_predicate", "source": "carta-notices",
  "members": [h[2] for h in HOLDERS if h[2].startswith("ES-")], "slots": ["P_lapsed_ES2", "P_lapsed_ES3", "P_lapsed_ES5", "P_lapsed_ES6", "P_lapsed_ES16", "P_FRED"],
  "description": "a complexity channel, not a rule: Leonard's list names Carta, so a run reads the notices; a line is misread one at a time"},
] + [{"id": f"CH-{p['id']}", "kind": "scale", "rule": p["id"], "degrade": "ch_miss", "latent": "member", "family": p["prior_family"], "source": p["source"], "members": p["controls"],
      "description": p["natural_reading"]} for p in PORTFOLIO]

CHAINS = [
 {"id": "C1", "root_cause": "A17", "ends_in": "R3", "hops": [{"service": "gmail", "record": M_LIST, "finding": "owner list: 86,470, 81,383, 31,536 twice"},
   {"service": "gdocs", "record": "f_6a37227593d0977fdbdd7a", "finding": "advisor table: 61,038, 30,518, 6,104, 6,104"}, {"service": "gdocs", "record": "f_11040fe5d66821bd6951aa", "finding": "term sheet total 3,051,879 ties only after subtracting"}]},
 {"id": "C2", "root_cause": "A24", "ends_in": "R5", "hops": [{"service": "slack", "record": S_LETTERS, "finding": "Leonard: all termination letters are sent"},
   {"service": "gmail", "record": M_BRIAN, "finding": "six letters to six recipients"}, {"service": "gmail", "record": M_ES14, "finding": "eight Carta entries on Feb 12"},
   {"service": "gmail", "record": M_VINC, "finding": "ES-14 resigned in November, before any letter"}]},
 {"id": "C3", "root_cause": "A25", "ends_in": "R4", "hops": [{"service": "slack", "record": S_LIST, "finding": "angels still to do on Feb 12"},
   {"service": "slack", "record": S_SEG, "finding": "Feb 9 DM told Segerstrale"}, {"service": "gmail", "record": TH_ROBERT, "finding": "NEW Robert told Deepak on Feb 13"}]},
 {"id": "C4", "root_cause": "A19", "ends_in": "R8", "hops": [{"service": "gmail", "record": TH_KPMG, "finding": "NEW as-of date Dec 31, 2025"},
   {"service": "gmail", "record": M_ES14, "finding": "effective Nov 21, entered Feb 12"}, {"service": "gmail", "record": M_ES13, "finding": "effective Jan 30: full grant still held at Dec 31"},
   {"service": "gdocs", "record": "f_6a37227593d0977fdbdd7a", "finding": "advisor grants count at every date"}]},
 {"id": "C5", "root_cause": "A11", "ends_in": "R9", "hops": [{"service": "gdocs", "record": "f_966445655f653d26dc8537", "finding": "board of four in the financing documents"},
   {"service": "gmail", "record": M_MATT, "finding": "Matthew resigned May 1, 2025"}, {"service": "gmail", "record": M_PHIL, "finding": "Griffin's director resigned Feb 12, 2026"}]},
 {"id": "C6", "root_cause": "A15", "ends_in": "R7", "hops": [{"service": "gdocs", "record": "f_6201c7027d02997bfb2c84", "finding": "Drive draft: Tor only"},
   {"service": "gmail", "record": M_CLARK, "finding": "revised letter"}, {"service": "gmail", "record": M_SIGN, "finding": "signed with Segerstrale's signature as well"}]},
 {"id": "C7", "root_cause": "A7", "ends_in": "R6", "hops": [{"service": "gmail", "record": M_LIST, "finding": "three lines, no shared surname"},
   {"service": "gmail", "record": M_ENES, "finding": "Enes supplies all three addresses"}, {"service": "gmail", "record": M_BROS, "finding": "all three brothers wired"},
   {"service": "linear", "record": "ENG-2444", "finding": "the project shows a name with no link to the family"}]},
 {"id": "C8", "root_cause": "A9", "ends_in": "R12", "hops": [{"service": "slack", "record": S_CLAIRE, "finding": "Claire asks about equity"},
   {"service": "slack", "record": f"{GRP}/1770903714.600249", "finding": "Leonard's replies answer the deletion question only"}, {"service": "gmail", "record": M_BRIAN, "finding": "the letter's equity paragraph gives no date"}]},
]

BUDGET = [
 ("discovery", "slack", 8, "the draft, #winddown pages, the Feb 12 list, the founder DMs"),
 ("discovery", "gmail", 6, "Sunset's request, KPMG's request and recent mail"),
 ("discovery", "linear", 3, "project, issue list, status list"),
 ("discovery", "gdrive", 3, "the close-out folder and Leonard's Drive listing"),
 ("rules", "gdocs", 6, "close-out notes, earlier notes, charter, IRA, side letter draft, term sheet"),
 ("rules", "gsheets", 2, "Task List and the draft holder sheet"),
 ("rules", "gslides", 1, "the update outline deck"),
 ("rules", "trello", 2, "the founders' close-out card and its comment"),
 ("rules", "gcal", 1, "the Tuesday hold, found by a keyword search because lists spill"),
 ("rules", "contacts", 2, "holders with no name in the mail: Bergmann and Eren"),
 ("per-record", "linear", 26, "each holder's issue notes need their own linear_list_comments; list_issues returns no comments"),
 ("per-record", "gmail", 26, "one search per holder address for the told column; search returns ids only"),
 ("per-record", "gmail", 14, "termination notices and letters read per option line; a batch at full format is capped at 10 ids"),
 ("per-record", "slack", 13, "name search per stock holder across DMs for any message about the closing"),
 ("reconciliation", "snowflake", 2, "FINANCE_LEDGER financing rows: dollars and no new money since 2023"),
 ("reconciliation", "gdocs", 2, "Due Diligence advisor table and the term sheet tie-out"),
 ("reconciliation", "gmail", 4, "side letter chain and the board resignations"),
 ("writes", "gsheets", 4, "create the schedule, fill it, read it back"),
 ("writes", "gdocs", 3, "the letter"),
 ("writes", "gdrive", 6, "move both files, share each with Robert and Arthur"),
 ("writes", "linear", 26, "one state move per holder issue; no bulk form"),
 ("writes", "linear", 10, "a reason comment on each issue where no note goes"),
 ("writes", "gmail", 2, "Griffin heads-up and the KPMG reply"),
 ("writes", "slack", 1, "the founders' thread reply"),
]
BUDGET_COND = [("writes", "gmail", 14, "one personal note per target", "gmail_create_draft has never run in a stored baseline; prove it in the pre-check")]

WRITES = [
 {"service": "gsheets", "tool": "gsheets_create_spreadsheet+gsheets_values_update", "count": 3, "depends_on": ["C1", "C2", "C3", "C6", "T3", "T14"], "requirements": ["R1", "R2", "R3", "R4", "R5", "R7"]},
 {"service": "gdocs", "tool": "gdocs_create_document", "count": 1, "depends_on": ["C5", "K1"], "requirements": ["R10"]},
 {"service": "gdrive", "tool": "gdrive_move_file+gdrive_share_file", "count": 6, "depends_on": ["K13", "K14"], "requirements": ["R13"]},
 {"service": "gmail", "tool": "gmail_create_draft", "count": 14, "depends_on": ["C2", "C3", "C7", "C8"], "requirements": ["R6", "R12"]},
 {"service": "gmail", "tool": "gmail_reply_to_message", "count": 2, "depends_on": ["C4", "C5"], "requirements": ["R8", "R9"]},
 {"service": "linear", "tool": "linear_update_issue", "count": 26, "depends_on": ["C2", "C3", "T15"], "requirements": ["R11"]},
 {"service": "linear", "tool": "linear_create_comment", "count": 10, "depends_on": ["C3", "T3"], "requirements": ["R11"]},
 {"service": "slack", "tool": "slack_send_message", "count": 1, "depends_on": ["C2"], "requirements": ["R13"]},
]

SERVICES = {
 "slack": ("the draft, Leonard's promise and list, the done claims, DMs that decide who was told", "the ask, the wrong sources and the records that beat them; the founders' reply"),
 "gmail": ("Carta notices, letters, the owner list, side letter chain, resignations, KPMG and Sunset requests", "every line's live state and the as-of date live here; notes and replies go here"),
 "gcal": ("the Tuesday hold", "the date the notes are due"),
 "gdrive": ("the close-out folder", "the destination of both files"),
 "gdocs": ("close-out notes, advisor table, term sheet, charter and side letter drafts", "the closed rule and the subtraction that ties the stock lines"),
 "gsheets": ("Task List, draft holder sheet, the deliverable", "the schedule itself"),
 "gslides": ("the update outline", "the letter's section order, supporting only"),
 "contacts": ("Bergmann and Eren name-to-address rows", "ties two token-only holders to a name"),
 "linear": ("the holder project", "the cohort, per-holder notes, states and reason comments"),
 "trello": ("the founders' close-out card", "the order: the holder sheet comes first"),
 "snowflake": ("FINANCE_LEDGER financing rows", "confirms no new financing since 2023 for the KPMG reply, and Segerstrale's $50,000"),
}

ctx = CTX
manifest = {
 "_note": "Draft manifest for the stockholder close-out. Generated by plan/build_scenario.py.",
 "persona": "leonard_hayes",
 "assignment_context": {k: ctx[k] for k in ("context_hash", "assignment_hash", "policy_hash", "freeze_utc", "difficulty_mode")},
 "horizon": "Long Horizon", "effective_profile": "extreme",
 "author_targets": {"counted_calls_every_run_gt": 130, "average_lt": 0.70, "design_E_avg_le": 0.62, "platform_cap": 0.85,
                    "source": "requester chat 2026-11-07: 'assignemt is medium but we have to target hard difficulty'; 'go with your recommendations on all six' (aim under 70 %, 62 % a stretch)"},
 "volume_exception": {"reason": "26 non-founder holders; mail reads batch, so about 145 honest calls per run; reaching 500 would need padding, which fails on its own",
                      "requester_confirmation": "requester, Claude Code chat 2026-11-07: 'go with your recommendations on all six' (00_Pre_Scenario_Analysis.md §10 decision 3)",
                      "call_budget_floor": 130, "per_record_floor": 85},
 "cohort_exception": {"reason": "the company has 29 holders on Carta, 26 of them non-founders; no honest cohort of 40 exists and padding one fails on its own",
                      "requester_confirmation": "requester, Claude Code chat 2026-11-07: 'go with your recommendations on all six' (00_Pre_Scenario_Analysis.md §10 decision 3)",
                      "cohort_floor": 26},
 "requirements": REQS,
 "services": {k: {"role": v[0], "weight_reason": v[1]} for k, v in SERVICES.items()},
 "anchors": [
  {"id": "AN1", "service": "slack", "locator": S_DRAFT, "prompt_reference": "the investor email draft in #winddown", "requirement_ids": ["R10"]},
  {"id": "AN2", "service": "linear", "locator": PROJECT, "prompt_reference": "the holder project in Linear", "requirement_ids": ["R1", "R5", "R11"]},
  {"id": "AN3", "service": "gmail", "locator": TH_KPMG, "prompt_reference": "KPMG's audit request for Griffin", "requirement_ids": ["R8"]},
 ],
 "ask_fragments": [frag(t) for t in FRAGS],
 "authorities": [
  {"id": "H1", "name": "my close-out notes", "home_service": "gdocs", "decoy_service": "gdocs", "governs": ["R4", "R5", "R12"], "findable_query": "close-out notes", "seeded_ids": [DOC_NOTES], "base_pointers": [], "decoy_seeded_ids": [DOC_OLD], "decoy_base_pointers": []},
  {"id": "H2", "name": "Carta's termination details", "home_service": "gmail", "decoy_service": "gdocs", "governs": ["R2"], "findable_query": "Termination details", "seeded_ids": [], "base_pointers": [M_ES14], "decoy_seeded_ids": [], "decoy_base_pointers": [D_TERM]},
  {"id": "H3", "name": "the signed side letter", "home_service": "gmail", "decoy_service": "gdocs", "governs": ["R7"], "findable_query": "side letter", "seeded_ids": [], "base_pointers": [M_SIGN], "decoy_seeded_ids": [], "decoy_base_pointers": [D_SIDE]},
  {"id": "H4", "name": "KPMG's FY25 request", "home_service": "gmail", "decoy_service": "gmail", "governs": ["R8"], "findable_query": "Audit Request", "seeded_ids": [TH_KPMG], "base_pointers": [], "decoy_seeded_ids": [], "decoy_base_pointers": [M_K24],
   "decoy_scope": {"dimension": "fiscal year", "decoy": "FY24 request, as of September 30, 2024", "task": "FY25 request, as of December 31, 2025"}},
 ],
 "cohort": {"definition": "every holder on a Carta record, live or lapsed, other than the three founders: 12 Series Seed lines and 14 option-only lines, one project issue each",
            "definition_source": [PROJECT, DOC_NOTES], "key": "holder issue", "size": 26, "evidence_surfaces": [
   surf("linear", "linear_list_comments", 1.0, 26, "R5", "what is owed", "linear_list_issues returns titles and states but no comments; each issue's notes need their own read",
        "each issue's notes carry that holder's own contact history; skipping the read leaves the row's last contact and any stale claim unchecked", True, ["ENG-2438", "ENG-2439", "ENG-2440", "ENG-2441", "ENG-2442"]),
   surf("gmail", "gmail_search_messages (per holder address)", 1.0, 26, "R4", "told", "gmail_search_messages returns ids only and no mail lists who was told; each address needs its own search",
        "only a per-address search finds a personal message; the Feb 12 list and the letters cover different people"),
   surf("gmail", "gmail_get_thread (notice, letter, last contact)", 0.75, 26, "R2", "last day", "the notices are one per thread and the date is only in the body; the owner list has no dates",
        "the last day exists nowhere else, so the notice cannot be skipped for an option line"),
   surf("slack", "slack_search_public_and_private (per holder name)", 0.5, 26, "R4", "told", "no channel holds every holder's contact; DMs need a name search",
        "a personal DM counts as told and shows up nowhere else"),
   surf("gdocs", "gdocs_get_document_text (agreement or consent)", 0.5, 14, "R3", "stock apart from advisor options", "agreements and consents are separate documents with no index",
        "the grant size on an agreement separates a holder's stock from options where the owner list merges them"),
 ]},
 "chains": CHAINS, "traps": TRAPS, "mechanism_portfolio": PORTFOLIO, "channels": CHANNELS,
 "call_budget": [{"phase": p, "service": s, "calls": c, "reason": r} for p, s, c, r in BUDGET] +
                [{"phase": p, "service": s, "calls": c, "reason": r, "conditional_on": k} for p, s, c, r, k in BUDGET_COND],
 "writes": WRITES,
 "hazard_acknowledgements": [
  {"hazard_id": "L13", "resolution": "excluded", "why_safe": "neither Combo-Fighters#37 nor the #company-internal repo post is cited; no row claims work stopped"},
  {"hazard_id": "L08", "resolution": "excluded", "why_safe": "seeded issues are assigned only to the three founders, never to a holder"},
  {"hazard_id": "R04", "resolution": "excluded", "why_safe": "neither the Slack folder link nor the dead 'Harmony Games Cap Table' link is cited; no row needs that sheet"},
  {"hazard_id": "R08", "resolution": "excluded", "why_safe": "no base invitation is cited; the one seeded event has Leonard as its only attendee"},
 ],
 "denied_probes": [],
 "gradable_surface": "01_Gradable_Surface.json",
}

# ------------------------------------------------------------ gradable surface
S = []
def slot(id_, title, w, kind, reason, cls, sel, mech=(), role="core", group=None, fact=None, singled=None, volume_for=None):
    d = {"id": id_, "title": title, "weight": w, "work_kind": kind, "work_reason": reason, "class": cls, "selector": sel, "role": role, "mechanisms": list(mech)}
    if group: d["group"] = group
    if fact: d["fact_id"] = fact
    if singled: d["singled_out_by"] = singled
    if volume_for: d["volume_for"] = volume_for
    S.append(d)
W = "[ -~\\u00a0-\\uffff]{0,160}"
def near(a, b): return f"({a}){W}{b}"
SCH = "schedule"
# stock
slot("K1", "Series Seed total", 5, "multi_source_reconciliation", "the lines tie only after advisor options come out", "aggregate", ["text", SCH, "3,?051,?879"], ["ADV"])
slot("K2", "Griffin II shares", 3, "limited_reconciliation", "the owner list merges the two funds", "direct", ["text", SCH, near("Griffin[^\\n]{0,40}II(?! Side)", "2,?662,?255")], ["ADV"])
slot("K3", "Side Fund shares", 3, "limited_reconciliation", "the owner list merges the two funds", "direct", ["text", SCH, near("Side Fund", "84,?438")], ["ADV"])
for k, n, v in [("K4", "Collins|ENG-2447", "25,?432"), ("K5", "Segerstr|ENG-2440", "50,?865"), ("K6", "Nebojsa|ENG-2446", "25,?432"), ("K7", "Deepak|ENG-2449", "25,?432")]:
    slot(k, f"stock for {n.split('|')[0]}", 5, "multi_source_reconciliation", "owner list less the advisor table, tied to the total", "direct", ["text", SCH, near(n, v)], ["ADV"])
slot("K8", "advisor options", 3, "calculation", "the four grants sum from the advisor table", "aggregate", ["text", SCH, "103,?764"], ["ADV"])
for i, (n, v) in enumerate([("TOR|ENG-2448", "50,?865"), ("Schaeppi|ENG-2441", "25,?432"), ("Bergmann|ENG-2442", "25,?432")], 13):
    slot(f"K{i}", f"stock line {n.split('|')[0]}", 1, "lookup", "one line on the owner list", "direct", ["text", SCH, near(n, v)], role="sample", group="stock")
slot("K16", "every project issue on the sheet", 1, "lookup", "output volume", "delivery", ["delivery", "register_keys_exact", SCH], role="volume", volume_for=["stock", "live"])
# options
slot("P1", "live options at the clock", 5, "multi_source_reconciliation", "vested live lines plus advisor grants, across notices and the advisor table", "aggregate", ["text", SCH, "159,?706"], ["ADV"])
for e, k in [("ES2", I["ES-2"]), ("ES3", I["ES-3"]), ("ES5", I["ES-5"]), ("ES6", I["ES-6"]), ("ES16", I["ES-16"])]:
    slot(f"P_lapsed_{e}", f"{e} holds nothing", 3, "comparison", "the last day against the clock", "direct", ["field", k, "Owed"], role="exception", singled="H2")
slot("P_FRED", "ES-17 holds nothing", 5, "tracing", "the largest non-Griffin line, traced across the owner list, Carta and the letter", "direct", ["field", I["ES-17"], "Owed"], role="exception", singled="H2")
for e in ["ES-1", "ES-4", "ES-7", "ES-12", "ES-13"]:
    v = {"ES-1": "17,?802", "ES-4": "4,?450", "ES-7": "12,?875", "ES-12": "8,?477", "ES-13": "2,?013"}[e]
    slot(f"P_live_{e}", f"{e} vested", 1, "lookup", "one notice", "direct", ["text", SCH, near(I[e], v)], role="sample", group="live")
slot("P_first", "ES-14 last day", 3, "comparison", "the earliest of the live dates", "direct", ["text", SCH, near(I["ES-14"], "Feb[a-z]*\\.? ?21|2026-02-21|2/21")])
# owed
slot("C_ES14", "ES-14 owed a full note", 5, "tracing", "no letter: six recipients joined to eight Carta entries", "direct", ["field", I["ES-14"], "Owed"], ["LETTER"], fact="owed_es14")
slot("C_ES18", "ES-18 owed a full note", 5, "tracing", "no letter: six recipients joined to eight Carta entries", "direct", ["field", I["ES-18"], "Owed"], ["LETTER"], fact="owed_es18")
slot("C_DATE", "date notes total", 3, "calculation", "live lines with a letter", "aggregate", ["text", SCH, near("[Dd]ate note", "(6|six)")], ["LETTER"])
slot("C_SEG", "Segerstrale already told", 5, "multi_source_reconciliation", "a DM against the list that says angels are open", "direct", ["field", "ENG-2440", "Owed"], ["TOLD"], fact="owed_seg")
slot("C_DEEPAK", "Deepak already told", 5, "multi_source_reconciliation", "Robert's mail against the same list", "direct", ["field", "ENG-2449", "Owed"], ["TOLD"], fact="owed_deepak")
slot("C_TOR", "Tor still owed a first note", 3, "interpretation", "a runway warning is not the closing", "direct", ["field", "ENG-2448", "Owed"], ["TOLD"], fact="owed_tor")
slot("C_FIRST", "first notes total", 3, "calculation", "stock lines not yet told", "aggregate", ["text", SCH, near("[Ff]irst note", "(6|six)")], ["TOLD"])
# told column (R4): the crossing itself, apart from what follows from it
slot("TC_ES14", "ES-14 not told", 3, "comparison", "resigned before the closing, outside every Feb 11 channel", "direct", ["field", I["ES-14"], "Told"], ["LETTER"], fact="told_es14")
slot("TC_ES18", "ES-18 not told personally", 3, "comparison", "a channel post is not a personal message", "direct", ["field", I["ES-18"], "Told"], ["LETTER"], fact="told_es18")
slot("TC_SEG", "Segerstrale told", 3, "comparison", "a personal DM", "direct", ["field", "ENG-2440", "Told"], ["TOLD"], fact="told_seg")
slot("TC_DEEPAK", "Deepak told", 3, "comparison", "Robert's mail", "direct", ["field", "ENG-2449", "Told"], ["TOLD"], fact="told_deepak")
slot("TC_TOR", "Tor not told", 3, "comparison", "a runway warning, not the closing", "direct", ["field", "ENG-2448", "Told"], ["TOLD"], fact="told_tor")
# route
slot("S1", "Tor's notice route", 3, "interpretation", "side letter notice terms", "write_content", ["text", SCH, near("TOR|ENG-2448", "(side letter|email|courier)")], ["SIDE"])
slot("S2", "copy to Tor's counsel", 3, "interpretation", "side letter notice terms", "write_content", ["text", SCH, near("TOR|ENG-2448", "(TLAS|Thompson)")], ["SIDE"])
slot("S3", "Segerstrale under the side letter", 5, "multi_source_reconciliation", "Drive draft against the signed mail chain", "write_content", ["text", SCH, near("Segerstr|ENG-2440", "side letter")], ["SIDE"])
# board
slot("B1", "directors in office", 5, "tracing", "two resignations traced across mail against the financing documents", "write_content", ["text", SCH, "director[ -~\\u00a0-\\uffff]{0,80}Leonard[ -~\\u00a0-\\uffff]{0,40}Robert"], ["BOARD"])
slot("B2", "Griffin carries the preferred vote", 3, "calculation", "share of preferred", "write_content", ["text", SCH, "90(\\.0)? ?%"], ["BOARD"])
# letter
for k, t, pat in [("L3", "no distribution promised", "(no|not expect)[ -~\\u00a0-\\uffff]{0,60}(distribut|return|proceeds)"), ("L4", "write-off papers", "(tax|write.?off)"), ("L5", "IP and code", "(IP|codebase)")]:
    slot(k, t, 1, "lookup", "from the draft", "write_content", ["text", "letter", pat])
slot("L2", "Sunset named as running the close", 3, "interpretation", "the draft predates the signing", "write_content", ["text", "letter", "sunset"])
slot("L6", "letter states the board", 3, "interpretation", "the draft predates the resignation", "write_content", ["text", "letter", "(board|director)[ -~\\u00a0-\\uffff]{0,120}(Robert|resign)"], ["BOARD"])
slot("L8", "letter's option paragraph", 3, "interpretation", "live and lapsed lines read differently", "write_content", ["text", "letter", "(option|exercise)"])
slot("G1", "heads-up drafted to Griffin", 1, "lookup", "one write", "delivery", ["link", "griffin"])
slot("G2", "heads-up names the holder vote", 3, "interpretation", "a vote of the preferred, not a board seat", "write_content", ["text", "griffin", "(consent|vote|preferred)"], ["BOARD"])
# notes
notes = [("Schaeppi", []), ("Bergmann", []), ("Nebojsa", ["ADV"]), ("Collins", ["ADV"]), ("Tor", ["TOLD"])]
for n, m in notes:
    slot(f"NC_{n}", f"note to {n} states the holding", 3, "interpretation", "the holder's own line", "write_content", ["text", "notes", near(n, "(25,?432|50,?865|shares)")], m)
slot("F4", "Patrick Lewis's line is covered", 3, "interpretation", "the family rule on a name with no surname link", "direct", ["field", "ENG-2444", "Owed"], ["FAM"], fact="owed_pat")
slot("F5", "Eren's line is covered", 3, "interpretation", "the family rule; he has no mail of his own", "direct", ["field", "ENG-2445", "Owed"], ["FAM"], fact="owed_eren")
slot("F1", "one note to Enes covers the family", 5, "tracing", "the link is in 2023 mail and the names show no shared surname", "write_content", ["text", "notes", near("Enes", "(brother|family|all three|Patrick|Eren)")], ["FAM"])
slot("F2", "that note covers three lines", 3, "calculation", "three holdings in one note", "write_content", ["text", "notes", "(76,?296|three[ -~\\u00a0-\\uffff]{0,40}25,?432)"], ["FAM"])
slot("F3", "reason comment on a covered line", 3, "interpretation", "the line is covered by Enes's note", "write_content", ["text", "comments", "(enes|family|brother)"], ["FAM"])
slot("N_COUNT", "bare count of notes", 3, "calculation", "first, date and full notes after the family rule", "aggregate", ["link", "notes"], ["FAM", "TOLD", "LETTER"], fact="note_count")
for e, k in [("ES-1", "Mar"), ("ES-7", "Apr"), ("ES-12", "Apr"), ("ES-13", "Apr"), ("ES-15", "Mar")]:
    n = {"ES-1": "Julia", "ES-7": "Marcus", "ES-12": "Owen", "ES-13": "Martin", "ES-15": "Brian"}[e]
    slot(f"ND_{e}", f"date note to {e}", 1, "lookup", "the date is on one notice", "write_content", ["text", "notes", near(n, k)], role="sample", group="date")
slot("ND_vol", "every date note", 1, "lookup", "output volume", "delivery", ["link", "notes"], role="volume", volume_for=["date"], fact="date_vol")
slot("N_Vincent", "ES-14's note covers the closing and Feb 21", 5, "tracing", "a holder outside every Feb 11 channel", "write_content", ["text", "notes", near("Vincent", "(clos|shut|wind)")], ["LETTER"])
slot("N_Oliver", "ES-18's note covers the closing", 3, "interpretation", "no letter on file", "write_content", ["text", "notes", near("Oliver", "(clos|shut|wind)")], ["LETTER"])
slot("Q1", "Claire's note answers her equity question", 5, "tracing", "a group-DM question joined to the letter's equity paragraph and her notice", "write_content", ["text", "notes", near("Claire", "(exercise|equity|option)")], ["ASK"])
slot("Q2", "Claire's last day", 3, "comparison", "her notice", "write_content", ["text", "notes", near("Claire", "Mar[a-z]*\\.? ?31")], ["ASK"])
# KPMG
slot("A1", "options at the as-of date", 5, "deeper_reasoning", "effective dates across every notice, not entry dates", "aggregate", ["text", "kpmg", "243,?757"], ["ASOF"])
slot("A2", "issued plus options at the as-of date", 5, "deeper_reasoning", "derived from the same dates", "aggregate", ["text", "kpmg", "9,?295,?636"], ["ASOF"])
for e, k, v, why in [("ES-7", "Marcus", "22,?889", "terminated after the as-of date: the full grant still counts"), ("ES-12", "Owen", "16,?277", "terminated after the as-of date: the full grant still counts"),
                     ("ES-1", "Julia", "17,?802", "terminated on the as-of date: vested only"), ("ES-14", "Vincent", "1,?530", "effective in November, entered in February"), ("ES-16", "ENG-2461", "10,?384", "lapsed since, but open at the as-of date")]:
    slot(f"AL_{e}", f"{e} at the as-of date", 3, "comparison", why, "write_content", ["text", "kpmg", near(k, v)], ["ASOF"], role="sample", group="asof", fact=f"asof_{e}")
slot("AL_vol", "every option line at the as-of date", 1, "lookup", "output volume", "delivery", ["link", "kpmg"], role="volume", volume_for=["asof"], fact="asof_vol")
slot("A3", "each fund's shares", 3, "limited_reconciliation", "two lines, not one", "write_content", ["text", "kpmg", "84,?438"], ["ADV"])
slot("A5", "later event disclosed", 3, "interpretation", "the closing falls after the as-of date", "write_content", ["text", "kpmg", "(clos|shut|wind)"])
slot("A7", "no new financing", 1, "lookup", "ledger and mail", "write_content", ["text", "kpmg", "(no new|since the seed|no (further|additional) financ)"])
slot("A8", "reply goes to all", 1, "lookup", "KPMG's own request", "delivery", ["link", "kpmg"], fact="kpmg_all")
# project
slot("LC_Seg", "reason comment on Segerstrale's issue", 3, "interpretation", "says who told him", "write_content", ["text", "comments", "(segerstr|kris)"], ["TOLD"])
slot("LC_Deepak", "reason comment on Deepak's issue", 3, "interpretation", "says who told him", "write_content", ["text", "comments", "(deepak|robert)"], ["TOLD"])
for e in ["ES-2", "ES-3", "ES-5"]:
    slot(f"LC_{e}", f"reason comment on {e}'s issue", 1, "lookup", "the last day is on one notice", "write_content", ["text", "comments", f"{I[e]}|lapsed"], role="sample", group="lc")
slot("LC_vol", "a reason comment wherever no note goes", 1, "lookup", "output volume", "delivery", ["link", "comments"], role="volume", volume_for=["lc"], fact="lc_vol")
for e in ["ES-3", "ES-6", "ES-12"]:
    slot(f"LS_{e}", f"state of {e}'s issue", 1, "lookup", "state by class", "delivery", ["link", "moves"], role="sample", group="st", fact=f"state_{e}")
slot("LS_vol", "every issue moved", 1, "lookup", "output volume", "delivery", ["link", "moves"], role="volume", volume_for=["st"], fact="state_vol")
# delivery
slot("D1", "schedule in the close-out folder", 1, "lookup", "named destination", "delivery", ["delivery", "register_parent", FOLDER])
slot("D2", "shared with Robert", 1, "lookup", "the notes", "delivery", ["delivery", "share_reader"])
slot("D3", "letter in the folder", 1, "lookup", "named destination", "delivery", ["link", "letter"])
slot("D5", "thread reply", 1, "lookup", "named destination", "delivery", ["link", "reply"], fact="reply_sent")
slot("D6", "reply names who goes first", 3, "interpretation", "the earliest last day among the untold", "write_content", ["text", "reply", "(vincent|ES-14|Feb[a-z]*\\.? ?21)"], ["LETTER"])

surface = {"kind": "GRADABLE_SURFACE", "version": 1, "task": "leonard_stockholder_closeout", "revision": "design-1",
           "classes": ["First note", "Covered", "Date note", "Full note", "Already told", "Nothing"],
           "truth_fields": {"class": "Owed", "groups": "groups"}, "truth_keys": [h[0] for h in HOLDERS],
           "deliverables": {
            SCH: {"kind": "table", "name_regex": ".*(holder|stockholder|close.?out|schedule).*", "key_column": "Issue", "key_regex": "ENG-\\d{4}",
                  "columns": ["Issue", "Holder", "Instrument", "Shares held now", "Last day", "Told", "Owed", "Route"], "class_column": "Owed", "reason_column": "Route",
                  "comparators": {"Issue": "issue_key", "Owed": "yes_no", "Told": "yes_no"},
                  "yes_no": {"First note": ["First note", "First"], "Covered": ["Covered", "Covered by Enes", "Family note"], "Date note": ["Date note", "Date"], "Full note": ["Full note", "Full"],
                             "Already told": ["Already told", "None, told"], "Nothing": ["Nothing", "None", "Lapsed", "Holds nothing"],
                             "Yes": ["Yes", "Told", "Y"], "No": ["No", "Not told", "N"]}},
            "letter": {"kind": "json_text", "tool": "gdocs_create_document"}, "notes": {"kind": "json_text", "tool": "gmail_create_draft"},
            "griffin": {"kind": "json_text", "tool": "gmail_reply_to_message"}, "kpmg": {"kind": "json_text", "tool": "gmail_reply_to_message"},
            "reply": {"kind": "json_text", "tool": "slack_send_message"}, "comments": {"kind": "json_text", "tool": "linear_create_comment"},
            "moves": {"kind": "json_text", "tool": "linear_update_issue"}},
           "slots": S}
json.dump(manifest, open(os.path.join(WF, "01_Hardness_Manifest.draft.json"), "w"), indent=1, ensure_ascii=False)
json.dump(surface, open(os.path.join(WF, "01_Gradable_Surface.json"), "w"), indent=1, ensure_ascii=False)
t = sum(s["weight"] for s in S); f = sum(s["weight"] for s in S if s["mechanisms"])
print(len(S), "slots, weight", t, "flippable", f, f"{f/t:.1%}", "weight-5", sum(1 for s in S if s["weight"] == 5))
for p in PORTFOLIO:
    w = sum(s["weight"] for s in S if p["id"] in s["mechanisms"]); print(f"  {p['id']:7} {w:3d} {w/t:5.1%}")
print("budget unconditional", sum(c for _, _, c, _ in BUDGET))
