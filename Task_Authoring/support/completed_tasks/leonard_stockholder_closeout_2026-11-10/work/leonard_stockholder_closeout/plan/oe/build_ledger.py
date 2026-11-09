#!/usr/bin/env python3
"""Write Working_Files/08_OE_Writing_Ledger.md from the verified facts. Run build_events.py first."""
import json
import os
import re
import subprocess
import sys

import build_events as E
import oe_data as D
import oe_lib as L
sys.path.insert(0, os.path.join(L.TA, "tools"))
import stage_gate as G  # noqa: E402

FACT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/private/tmp/claude-501/-Users-sumit-Source-OC/a5960dc6-a30f-407f-987d-df678279dab2/scratchpad/oe"
DEF = {f["key"]: f for f in json.load(open(os.path.join(FACT_DIR, "facts_winddown.json"))) if f["key"].startswith("defer")}
PROMPT = open(os.path.join(L.TI, "04_Prompt.txt")).read()
MB = "leonard.hayes@harmonygames.co"
th = lambda x: f"{MB}/{x}"
tf = lambda x: f"threads/leonard@harmonygames.co_{x}.json"
EXP = dict((i + 1, re.sub(r"<(PERSON_\d+_EMAIL)>", r"(\1)", e.replace("{DM}", str(E.OE_DM))).replace("|", "/")) for i, (_, e) in enumerate(E.EV))

B = []


def F(fact, service, tools, locator, origin, oe, result, deps, pointer, extra=""):
    fid = f"F{len(B) + 1}"
    expected = (EXP[oe] if isinstance(oe, int) else oe) + extra
    B.append([fid, fact, service, tools, locator, origin, expected, result, "see proof below" if re.search(r"Gmail|Slack|Drive|Docs|Sheets|Slides", service) else "unscoped service; natural pointer in the Locator origin column",
              ", ".join(deps) or "none", pointer])
    return fid


CENSUS_RESULT = open(os.path.join(L.HERE, "census_result.txt")).read().strip()
P1 = F("The holder project: scope, states, what to send", "Linear", "linear_list_projects", "the Linear project whose name has the word holder", 'prompt ("the holder project in Linear"); search "holder"', E.OE_PROJECT,
       "VERIFIED: every quote cut from the project row's description", [], "SQL L136, ec2ea957-fc8e-4958-b809-0fb735b1e916")
P2 = F("The 26 holder issues and their addresses", "Linear", "linear_list_issues", "the issues of the project named in F1", "F1", E.OE_ISSUES,
       "VERIFIED: 26 issue rows, each title and description line asserted against the SQL", [P1], "SQL L139 to L289, ENG-2438 to ENG-2463")
P3 = F("Two comments per issue, with the Nov 2024 owner-list figure", "Linear", "linear_list_comments", "the comments of each issue listed in F2", "F2", E.OE_COMMENTS,
       "VERIFIED: 52 comment rows; the 26 owner-list lines quoted", [P2], "SQL L141 to L293, ENG-2438")
P4 = F("The close-out notes: the asks and the handling rules", "Docs (Drive)", "gdrive_search, gdocs_get_document_text", "the Doc titled Stockholder close-out notes", 'prompt ("my close-out notes doc"); search "close-out"', E.OE_NOTES,
       "VERIFIED: every quote cut from the document body", [], "SQL L17, f_a37b403d5200d4f0a31d31")
P5 = F("The close-out folder and its files", "Drive", "gdrive_list_folder", "the folder that holds the notes in F4", "F4", E.OE_FOLDER,
       "VERIFIED: the three drive rows whose parent is the folder", [P4], "SQL L6 to L15, d_601064334a0b493022fe83, f_5ecaa967db3adcfa440b09, f_75dddccabb26eeea4842c8")
P6 = F("The draft holder sheet", "Sheets (Drive)", "gsheets_values_get", "the spreadsheet Holder list (draft) in the folder of F5", "F5", E.OE_DRAFT,
       "VERIFIED: grid cut from the sheet row", [P5], "SQL L25, f_5ecaa967db3adcfa440b09")
P7 = F("The update outline", "Slides (Drive)", "gslides_get_presentation_text", "the presentation in the folder of F5", "F5", E.OE_OUTLINE,
       "VERIFIED: text of the five slides", [P5], "SQL L32 to L48, f_75dddccabb26eeea4842c8")
P8 = F("#winddown: the investor email draft, the list and the done lines", "Slack", "slack_read_channel, slack_search_public_and_private", "#winddown, Leonard's posts of Feb 9 to Feb 12 2026", 'prompt ("my investor email draft in #winddown")', E.OE_WIND,
       "VERIFIED: every quote re-read through hg.py", [], "C0ADGSZKR3R/1770664700.848759, C0ADGSZKR3R/1770789534.434749, C0ADGSZKR3R/1770841239.761999, C0ADGSZKR3R/1770924424.711879, C0ADGSZKR3R/1770931777.561519, C0ADGSZKR3R/1770932147.282819, C0ADGSZKR3R/1770934638.035469, C0ADGSZKR3R/1770935621.095649, messages/C0ADGSZKR3R/2026-02.json /7 /57 /81 /163 /172 /174 /197 /198")
P9 = F("The four replies under the list: family rule, Covered, Arthur on the sheet", "Slack", "slack_read_thread", "the thread under Leonard's list in F8", "F8", E.OE_THREAD,
       "VERIFIED: four seeded replies", [P8], "C0ADGSZKR3R/1770949310.220519, C0ADGSZKR3R/1770949322.640149, C0ADGSZKR3R/1770949351.317729, C0ADGSZKR3R/1770949437.902269, SQL L60 to L66")
P10 = F("What Sunset asked for", "Gmail", "gmail_search_messages, gmail_get_thread", "Leonard's mail from Sunset about the stockholder intake", 'F1 ("what Sunset asked for"); search "Sunset stockholder"', E.OE_SUNSET,
        "VERIFIED: every quote cut from the message", [P1], f"{th('1857034369525983506')}, SQL L90")
P11 = F("KPMG's request and clarification", "Gmail", "gmail_search_messages, gmail_get_thread", "the FY2025 audit request thread in Leonard's mailbox", 'prompt ("KPMG\'s audit request"); search "Audit Request"', E.OE_KPMG,
        "VERIFIED: every quote cut from the three messages", [], f"{th('1857029474983245439')}, SQL L80 to L86")
NOTICE = {}
for r in D.OPTION:
    k, cid, tid = r[0], r[3], r[4]
    NOTICE[cid] = F(f"Carta notice for {cid} ({k})", "Gmail", "gmail_search_messages, gmail_get_message", f"Carta's termination notice for {cid} in Leonard's mailbox", 'F8 ("Carta terminations are done"); search "has been terminated"',
                    f"{cid} {r[5]}: granted {D.n(r[6])}, vested {D.n(r[7])}, terminated as of {r[8]} (effective date), last day to exercise {r[9]} (semantic date).",
                    "VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise)", [P8], f"{th(tid)}, {tf(tid)} /messages/0/body")
PC = F("Calvin's forward of Carta's Jan 23 update: ES-3 extended", "Gmail", "gmail_search_messages, gmail_get_message", "mail from the address on ENG-2452", "F2", E.OE_CALVIN,
       "VERIFIED: quoted from the seeded message", [P2, NOTICE["ES-3"]], f"{th('1856121753612004097')}, SQL L115")
LET = ["1856858053929740799", "1856860994291529096", "1856861229984402233", "1856861323365646598", "1856861400116562076", "1856861462411533365"]
PL = F("The six Feb 11 letters, and no closing message to ES-3, ES-12 (by DM), ES-14, ES-18 since Feb 1", "Gmail and Slack", "gmail_search_messages, gmail_get_thread, slack_read_channel", "mail and DMs with the nine live noticed holders since Feb 1 2026", "F2, F3", E.OE_LETTERS,
       'VERIFIED letters; ABSENCE evidence_check: search "terminating our independent" over all 88,728 gmail thread files, scan complete, 18 matches = 6 letters in 3 mailboxes, no seventh letter; addresses [EMAIL_0801], PERSON_2684_EMAIL and PERSON_1174_EMAIL over all 17,635 of Leonard\'s thread files, scan complete, none in 2026; positive control: PERSON_3140_EMAIL returns the Feb 11 letter; Slack: 39 DMs and group DMs with Leonard and those four holders, one February 2026 file (D05SDEQEK61), all four messages read',
       [P2, P3] + [NOTICE["ES-1"]], ", ".join(th(x) for x in LET) + ", D05SDEQEK61/1770827705.815759")
PB = F("The bounce on the ES-12 letter", "Gmail", "gmail_get_thread", "the thread of the ES-12 letter in F" + PL[1:], PL, E.OE_BOUNCE,
       'VERIFIED: quoted from the seeded message; ABSENCE evidence_check: Delivery Status mails in Leonard\'s 17,635 thread files, scan complete, none in Feb 2026 other than this seeded one',
       [PL], f"{th('1856860994291529096')}, SQL L111")
PT = F("Tie of the ES-15 name to ENG-2460", "Gmail", "gmail_search_messages, gmail_get_message", "mail with the address on ENG-2460", "F2", E.OE_ES15,
       "VERIFIED: both lines quoted from the option list", [P2], f"{th('1782034095239486005')}, {tf('1782034095239486005')} /messages/3/body")
PQ = F("Holder questions about their holding: one open for a holder who gets a note", "Gmail and Slack", "gmail_search_messages, gmail_get_thread, slack_search_public_and_private, slack_read_channel", "mail from the 26 issue addresses and Leonard's Slack DMs and group DMs, about options, shares, equity, vesting or exercise, no date limit", "F2", E.OE_CLAIRE,
       CENSUS_RESULT, [P2], f"C51ECE5102ED/1770903714.600249, C51ECE5102ED/1770906363.694689, {th('1847333990408253969')}, messages/C51ECE5102ED/2026-02.json /1 /4")
PG = F("The four advisor grants and who holds each", "Gmail", "gmail_search_messages, gmail_get_message", "Carta digests that name ES-8 to ES-11", 'search "ES-9"; F12 (the numbers the notices skip)', E.OE_GRANTS,
       "VERIFIED: quoted from the two digests", [NOTICE["ES-1"]], f"{th('1782897835407336831')}, {th('1783169549554193375')}, SQL L119")
PDM = F("ENG-2440 told, and the 0.5% grant tied to the holder", "Slack", "slack_search_public_and_private, slack_read_channel", "the DM where the address on ENG-2440 appears", 'F2; search "PERSON_3336_EMAIL"', E.OE_DM,
        "VERIFIED: every quote re-read through hg.py; link: the other person gives the ENG-2440 address in the DM", [P2], "D04UC0UEN2V/1770664988.379119, D04UC0UEN2V/1770669799.913739, D04UC0UEN2V/1694674255.630849, D04UC0UEN2V/1706113754.132409, D04UC0UEN2V/1693245806.221449, D04UC0UEN2V/1693246524.896449")
PA = F("Size of each advisor grant, by name", "Gmail", "gmail_search_messages, gmail_get_message", "the mail with the disclosure schedule table", 'F' + PDM[1:] + ' ("103764 shares for advisors"); search "103,764"', E.OE_ADVISOR,
       "VERIFIED: rows quoted from the message body (name, role, percent and shares on separate lines)", [PDM, PG], f"{th('1773160163779741845')}, {tf('1773160163779741845')} /messages/1/body")
PV = F("How the four grants vest", "Gmail", "gmail_get_thread, gmail_get_attachment, contacts_search_contacts", "the Nov 10 2023 board consent attached in Leonard's Option Issuances thread, and the ENG-2447 Contacts row", 'search "Option Issuances"; F2 (the address to look up in Contacts)', E.OE_VEST,
       "VERIFIED: Exhibit A quoted from the attachment as gmail_get_attachment returned it (baseline run 2, consent_nov10_2023_exhibit_a.txt); all four grants 1/24th monthly/no cliff; the Contacts row updated at SQL L133; recorded calculation: Nov 2023 plus 24 monthly steps", [PDM, PG, PA, NOTICE["ES-1"]], f"{th('1782034095239486005')}, message <IA1PR15MB5917E8BDC461FB37F1D957F08AAEA@IA1PR15MB5917.namprd15.prod.outlook.com>, att_0001; db57e559500151d6b3991b62 (Contacts), SQL L133")
PLG = F("The share ledger figures", "Docs (Drive)", "gdrive_search, gdocs_get_document_text", "the term sheet Doc with Inputs from ledger", 'search "ledger"', E.OE_LEDGER,
        "VERIFIED: quoted from the document body (gdocs data.json /docs_documents/40/body_text)", [], "f_11040fe5d66821bd6951aa")
PFIN = F("No new financing since Dec 31, 2025", "Gmail", "gmail_search_messages, gmail_get_thread", "Leonard's Jan 23 recap mail and Feb 9 wind-down request", 'F' + PLG[1:] + ' (the doc title has "Recap"); search "recap"; search "out of funds"', E.OE_RECAP,
          'VERIFIED: quoted from both mails; ABSENCE evidence_check: Slack messages/*/2026-0*.json for term sheet, financing, bridge, recap, funding (scan complete, none closing a round); Leonard\'s mailbox "certificate SSP-" in thread ids from Nov 2025, scan complete, 0; repeats the records\' own words "We are out of funds"',
          [PLG], f"{th('1855133803855213163')}, {th('1856688113228112603')}, f_11040fe5d66821bd6951aa")
PS = F("Griffin's split between its two funds", "Gmail", "gmail_search_messages, gmail_get_message", "the mail with the Series Seed purchaser schedule", 'search "Series Seed Preferred Shares"', E.OE_SPLIT,
       "VERIFIED: quoted from the message body", [PLG], f"{th('1771880236343640719')}, {tf('1771880236343640719')} /messages/0/body")
PBD = F("The Board position thread: partner's mail, recipients, board now", "Gmail", "gmail_search_messages, gmail_get_thread", "the thread named Board position", 'F4 ("their own Board position mail"); search "Board position"', E.OE_BOARD,
        "VERIFIED: quoted from the two base messages and the seeded reply", [P4], f"{th('1856958794180374704')}, SQL L96")
PCH = F("Who votes on a dissolution", "Docs (Drive)", "gdrive_search, gdocs_get_document_text", "the charter Doc with the protective provisions", 'search "dissolve"', E.OE_CHARTER,
        "VERIFIED: quoted from the document body (gdocs data.json /docs_documents/360/body_text)", [], "f_90c029015fc474199cf736")
PGT = F("Griffin's partner told", "Gmail", "gmail_search_messages, gmail_get_thread", "mail to the address on ENG-2438 since Feb 1 2026", "F2", E.OE_GTOLD,
        "VERIFIED: quoted from the messages", [P2], f"{th('1856675475513544349')}, {tf('1856675475513544349')} /messages/13/body /messages/12/body")
PR = F("ENG-2446 told by Robert", "Gmail", "gmail_search_messages, gmail_get_message", "mail to the address on ENG-2446 since Feb 1 2026", "F2", E.OE_ROBERT,
       "VERIFIED: quoted from the seeded message; no delivery failure (ABSENCE: Delivery Status mails over all 17,635 of Leonard's thread files, none on this address)", [P2], f"{th('1773963101399472184')}, SQL L105")
PAK = F("Leonard's Feb 12 mail to Husnu Akin", "Gmail", "gmail_search_messages, gmail_get_message", "Leonard's sent mail since Feb 1 2026 about shutting down", 'search "shutting down"', E.OE_AKIN,
        "VERIFIED: quoted from the seeded message", [PL], f"{th('1856961760270377901')}, SQL L123")
PAK2 = F("Akin is the ENG-2447 holder", "Gmail", "gmail_search_messages, gmail_get_message", "a mail that addresses or signs as Akin", 'search "and Akin"', E.OE_AKIN2,
         "VERIFIED: quoted; ABSENCE evidence_check: Delivery Status mails over Leonard's 17,635 thread files, none on PERSON_8862_EMAIL", [P2, PAK], f"{th('1776432843811839680')}, {tf('1776432843811839680')} /messages/0/body")
PF = F("The family: who handles it", "Gmail", "gmail_search_messages, gmail_get_thread", "mail with the address on ENG-2445", "F2", E.OE_FAM,
       "VERIFIED: quoted from the two threads", [P2, P9], f"{th('1770141224265557526')}, {th('1774211155651873582')}")
PTOR = F("TOR's partner: a runway warning only", "Slack", "slack_search_public_and_private, slack_read_channel", "Leonard's DM with TOR Capital's partner", 'search "months of runway"', E.OE_TOR,
         "VERIFIED: quoted; the DM's only month file is 2025-11, three messages read", [], "D09R59580EM/1762285888.654689, messages/D09R59580EM/2025-11.json /1")
PABS = F("No closing message to the other angels", "Gmail and Slack", "gmail_search_messages, slack_search_public_and_private", "mail and DMs with the addresses on ENG-2441 to ENG-2445, ENG-2448, ENG-2449", "F2", E.OE_ABS,
         'ABSENCE evidence_check: each address in to, cc and bcc over all 17,635 of Leonard\'s thread files, scan complete, intersected with the 470 messages dated Jan 31 to Feb 2026: 0 hits; 40 founder-sent February messages read one by one; Slack: 161 DMs with Leonard, 10 with February 2026 files read in full, none with these holders; positive control: PERSON_4337_EMAIL returns the two February mails in F' + PGT[1:] + '; the same Slack scan returns D04UC0UEN2V/1770664988.379119',
         [P2, P8, PGT], f"{th('1856675475513544349')}, D04UC0UEN2V/1770664988.379119, C0ADGSZKR3R/1770934638.035469")
C1 = F("Stock line holdings and the Series Seed total", "Calculation (no tool)", "none", "figures in F3, F" + PG[1:] + ", F" + PA[1:] + ", F" + PS[1:], "F3", E.OE_CALC1,
       "VERIFIED by recorded calculation: each line equals the owner-list figure less its grant; the 12 lines sum to 3,051,879, the ledger figure", [P3, PG, PA, PV, PLG, PS, PDM], "F3, solver/truth.json, ENG-2438")
C2 = F("Live option lines, last days, options today", "Calculation (no tool)", "none", "notices F12 to F25 and the update in F" + PC[1:], "F12", E.OE_CALC2,
       "VERIFIED by recorded calculation against the clock", [NOTICE["ES-1"], PC, P4, PV], "F12, solver/truth.json, ENG-2450")
C3 = F("Labels, notes and states", "Calculation (no tool)", "none", "rules in F1, F4, F9 and the told facts", "F1", E.OE_CALC3,
       "VERIFIED by recorded calculation; not_a_claim on the wording", [P1, P4, P9, PL, PB, PQ, PGT, PDM, PR, PAK2, PF, PTOR, PABS, C1, C2], "F1, solver/truth.json, ENG-2438")
C4 = F("Board, preferred vote, who goes first", "Calculation (no tool)", "none", "F" + PBD[1:] + ", F" + PCH[1:] + ", F" + PS[1:], PBD, E.OE_CALC4,
       "VERIFIED by recorded calculation: 2,746,693 / 3,051,879 = 90.0%", [PBD, PCH, PS, C2, C3], "F" + PBD[1:] + ", solver/truth.json, ENG-2452")
C5 = F("KPMG's figures at Dec 31, 2025", "Calculation (no tool)", "none", "F11, the notices, the grants", "F11", E.OE_CALC5,
       "VERIFIED by recorded calculation: sixteen lines sum to 243,757", [P11, NOTICE["ES-1"], PG, PA, PDM, C1, PFIN], "F11, solver/truth.json, ENG-2450")

AR = [
    ("R1", "the holder project in Linear", "Discovery: the project, its 26 issues and comments", "Explicit", [P1, P2, P3]),
    ("R2", "my close-out notes doc has how each holder gets handled and what still needs doing", "Discovery: the handling rules and the asks, plus the replies under the list that change them", "Explicit", [P4, P9]),
    ("R3", "take care of all of it the way those lay it out", "Discovery: what each holder holds, last days, who has been told, the family, the open question, the board and vote", "Implicit (through R1, R2)", list(NOTICE.values()) + [PC, PL, PB, PT, PQ, PG, PA, PV, PLG, PS, PBD, PCH, PGT, PDM, PR, PAK, PAK2, PF, PTOR, PABS, C1, C2, C3, C4]),
    ("R4", "the holder sheet and the investor letter in my close-out folder", "Write: finish the draft holder sheet in the folder, share it with Robert and Arthur", "Explicit", [P5, P6, P10, C1, C2, C3, C4, PBD, P9]),
    ("R5", "with the letter worked up from my investor email draft in #winddown", "Write: the letter as a Doc in the folder, shared with Robert", "Explicit", [P7, P8, P5, PBD]),
    ("R6", "the messages to holders as drafts in my Gmail", "Write: 14 drafts, unsent", "Explicit", [P2, C1, C2, C3, PQ, PF]),
    ("R7", "the Linear issues", "Write: 26 state moves and 12 reason comments", "Explicit", [P1, C3]),
    ("R8", "the heads-up to Griffin", "Write: reply to all on the partner's Board position mail, sent", "Explicit", [PBD, P4]),
    ("R9", "the reply in #winddown", "Write: thread reply saying who goes first, sent", "Explicit", [P8, C4]),
    ("R10", "an answer to KPMG's audit request for Griffin from yesterday", "Write: reply to all with items 1 to 4, sent", "Explicit", [P11, C1, C5, PFIN, PS]),
    ("R11", "Send the replies yourself, no need to check with me", "Constraint: the Griffin, KPMG and #winddown replies are sent", "Explicit", [P11, PBD, P8]),
    ("R12", "only the holder messages wait for me", "Constraint: the 14 notes stay drafts", "Explicit", [P4]),
]
for r in AR:
    assert r[1] in PROMPT, r[1]


def defer(key, extra=""):
    d = DEF[key]
    return (f"slack · gmail · linear · trello · gcal · drive · docs; population {d['population']} records, pagination complete; governing version: {d['governing_version']}; result: {d['result'].split('Scope:')[0].strip()} "
            f"Pointers f_a37b403d5200d4f0a31d31, 698e5a10c3f24b7e9d16a0e4, evt_6f1a2c9e4b7d3a58c0e1d2. Bounded by unsearched file contents (Gmail attachments, Slack files).{extra}").replace("|", "/")


CR = [
    ("R4", "Finish the holder sheet", '"That\'s the holder sheet and the investor letter in my close-out folder"', "gsheets_values_update (exists)", "spreadsheetId, range, values", P6, "26 rows, totals, counts, directors and vote in f_5ecaa967db3adcfa440b09", "what each holds, last days, labels, totals, counts, directors, vote", "W1"),
    ("R4", "Share the sheet with Robert and Arthur", '"Share it and the letter with Robert" (notes); "the sheet goes to you as well as Robert" (thread)', "gdrive_share_file (exists)", "fileId, emailAddress, role", PBD, "both addresses hold a permission on the sheet", "none", "W1"),
    ("R5", "Create the letter, move it, share it", '"with the letter worked up from my investor email draft in #winddown"', "gdocs_create_document, gdrive_move_file, gdrive_share_file (exist)", "title, bodyText; fileId, newParentId; fileId, emailAddress, role", P8, "a Doc in d_601064334a0b493022fe83, shared with robert@harmonygames.co", "the draft brought up to date with the outline's sections", "W2"),
    ("R6", "Save 14 holder notes as drafts", '"the messages to holders as drafts in my Gmail"', "gmail_create_draft (exists)", "to, subject, body", C3, "14 drafts in Leonard's mailbox, none sent", "closing where not told, last day where there is one, what they hold, Claire's answer, the family's three holdings", "W3"),
    ("R7", "Move the 26 issues", '"the Linear issues"', "linear_update_issue (exists)", "id, state", C3, "Canceled 5, Todo 14, Done 7", "state only", "W4"),
    ("R7", "Comment on the 12 issues with no note", '"the Linear issues"; "On every issue with no note of its own, Canceled included, say why." (project)', "linear_create_comment (exists)", "issueId, body", C3, "12 comments", "why the issue has no note", "W4"),
    ("R10", "Send the KPMG confirmation", '"an answer to KPMG\'s audit request for Griffin from yesterday"; "Send the replies yourself, no need to check with me"', "gmail_send_message with thread_id, or gmail_reply_to_message with reply_all (exist)", "thread_id, to, cc, subject, body", P11, "sent in the thread to the four addresses", "items 1 to 4 as of Dec 31, 2025", "W5"),
    ("R8", "Send the Griffin heads-up", '"the heads-up to Griffin"; "Send the replies yourself, no need to check with me"', "gmail_reply_to_message (exists)", "message_id, reply_all, body", PBD, "sent on the partner's own mail to PERSON_4337_EMAIL, cc PERSON_2847_EMAIL", "a request for the preferred vote on the dissolution", "W6"),
    ("R9", "Reply under the list in #winddown", '"the reply in #winddown"; "Send the replies yourself, no need to check with me"', "slack_send_message (exists)", "channel, text, thread_ts", P8, "a reply in the thread of C0ADGSZKR3R/1770934638.035469", "who goes first", "W7"),
]
CAT = {t["name"] for t in json.load(open(os.path.join(L.WS, "Evals", "references", "tools", "catalog.json")))}
for r in CR:
    for t in re.findall(r"\b(?:gsheets|gdrive|gdocs|gmail|linear|slack)_[a-z_]+", r[3]):
        assert t in CAT, t

E_TRAPS = [
    ("T1", "Owner-list figures on the comments and the draft sheet merge stock with advisor grants (ENG-2440, SQL L155)", "F" + C1[1:], "the Carta digests and the advisor table: 30,518, 61,038, 6,104, 6,104; f_6a37227593d0977fdbdd7a"),
    ("T2", "ES-3 notice with last day Jan. 24, 2026 (" + th("1847333347700620793") + ")", PC, f"Calvin's forward Tue Feb 3 2026 of Carta's Jan 23 update, later than the Oct 29 2025 notice; SQL L115"),
    ("T3", '"All termination letters are sent" (C0ADGSZKR3R/1770841239.761999)', PL, "six letters against nine live lines; none to ES-3, ES-14, ES-18"),
    ("T4", "The ES-12 letter looks delivered (" + th("1856860994291529096") + ")", PB, "the Delivery Status message in the same thread, SQL L111"),
    ("T5", "Feb 12 list shows the angels open (C0ADGSZKR3R/1770934638.035469)", PDM, "the Feb 9 DM D04UC0UEN2V/1770664988.379119 and Robert's Feb 12 mail, SQL L105"),
    ("T6", "The Feb 12 mail goes to a personal address and a name unlike the issue title (" + th("1856961760270377901") + ")", PAK2, "Collins signs 'akin' on " + th("1776432843811839680")),
    ("T7", "TOR DM mentions runway (D09R59580EM/1762285888.654689)", PTOR, "a cash warning, Nov 2025; the told rule needs the closing"),
    ("T8", "Term sheet options 268,772 (f_11040fe5d66821bd6951aa)", C2, "dated Jan 22 2026, before the Feb 12 Carta entries"),
    ("T9", "ChatGPT cap-table figures 3,051,881 in #executives (C07C2866011/1768417784.194359) and 3,051,882 in Aug 2023 mail", C1, "Leonard's reply C07C2866011/1768418331.402719: go by the ledger, 3,051,879 in f_11040fe5d66821bd6951aa"),
    ("T10", "Earlier outreach notes: one BCC mail (f_762c60832854d3e7a7f7df)", P4, "the later notes f_a37b403d5200d4f0a31d31: 'These replace my earlier outreach notes.'"),
    ("T11", "ES-17 letter: 34,409 vested, window Jan 22 (" + th("1847335165884050330") + ")", NOTICE["ES-17"], "Carta: 34,439, Jan. 28, 2026; the notes make Carta the record"),
    ("T12", "Outline line 'Holders, per the Nov 2024 owner list' (f_75dddccabb26eeea4842c8)", C1, "the notes: 'Carta is the record'"),
    ("T13", "Replying to Leonard's or Robert's later mail in the Board thread would add Robert and Arthur (" + th("1856958794180374704") + ")", PBD, "the notes name the partner's own mail, <BYAPR02MB435880CCF501BE0AE906AFFDC460A@BYAPR02MB4358.namprd02.prod.outlook.com>"),
    ("T14", "Bastian Bergmann and Patrick Lewis share the name Patrick (ENG-2442, ENG-2444; " + th("1799418746420547240") + ")", PF, "Leonard's May 2024 update bcc lists both addresses; only Patrick Lewis is in the family list"),
]
RISKS = [
    (1, "The KPMG reply-all tool dropped the copies on seeded mail in the pre-check (trajectory-run-1 event 891)", P11, "OE accuracy", "the OE names the four recipients and no tool"),
    (2, "ENG-2440 told rests on the DM's other party being the holder: Slack users.json has no name for that user", PDM, "UGT", "the address given in the DM and the 0.5% grant message tie it; platform /prompt F5 settled it Already told"),
    (3, "Advisor options: Sunset asks for what's vested, and vesting start dates are in Carta", PV, "rubric", "the consent's Exhibit A gives all four grants 1/24th monthly/no cliff, and the Nov 2023 grants ran out by Nov 2025; /prompt DR4 settled it the same way"),
    (4, "Letter sections 'Distributions' and 'tax papers' have no quotable figure", P7, "OE accuracy / rubric", "narrative content, not_a_claim; grade the sections and the updates"),
    (5, "Leonard cannot see Robert's or Arthur's own sent mail beyond copies to him; a direct message outside Leonard's view could exist", PABS, "UGT", "persona-visible bound; Arthur's mailbox checked clean"),
    (6, "Gmail attachments are readable through gmail_get_attachment", PV, "OE accuracy", f"OE {E.OE_VEST} reads the one attachment the path needs; the absence sweeps cover message text, not file contents"),
    (7, "The ES-12 letter's year slip (January 31, 2025) in the base", PB, "OE accuracy", "no step cites that date; Carta governs"),
]


def row(cells):
    return "| " + " | ".join(str(c).replace("\n", " ").replace("|", "/") for c in cells) + " |"


def visibility_block(text):
    scoped = sorted(set(G.scoped_ids(text)), key=lambda x: x[1])
    ids = sorted({i for _, i in scoped})
    lb = os.path.join(L.HERE, "oe_lb_ids.txt")
    open(lb, "w").write("\n".join(ids) + "\n")
    r = L.run([L.PY, "-B", "Task_Authoring/tools/persona_view.py", "check-sql", "leonard_hayes", "Task_Authoring/task_inputs/01_Universe_Inject.sql", "--load-bearing", lb])
    out = r.stdout.splitlines()
    want = set(ids)
    yes_lb = [x for x in out if x.startswith("[YES LB]") and "<" not in x and any(i in want for _, i in G.scoped_ids(x))]
    bad = [x for x in out if x.startswith(("[NO", "[UNVERIFIED"))]
    verdict = [x for x in out if x.startswith("verdict")]
    r2 = L.run([L.PY, "-B", "Task_Authoring/tools/persona_view.py", "check-sql", "leonard_hayes", "Task_Authoring/task_inputs/01_Universe_Inject.sql", "--load-bearing", lb, "--json"])
    d = json.loads(r2.stdout)
    in_sql = set()
    for rw in d["rows"]:
        in_sql.update(rw.get("keys", []))
    base = [(s, i) for s, i in scoped if i not in in_sql]
    lines, no = [], []
    for s, i in base:
        ln = L.persona_can_see(s, i)
        lines.append(ln)
        if not ln.endswith(": YES"):
            no.append(ln)
    L._save()
    return yes_lb, verdict, lines, no, bad


def build():
    A = [row([r[0], f'"{r[1]}"', r[2], r[3], ", ".join(r[4])]) for r in AR]
    Brows = [row(b) for b in B]
    Crows = [row([r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], defer("defer." + r[8]), "yes"]) for r in CR]
    Erows = [row(t) for t in E_TRAPS]
    Frows = [row(x) for x in RISKS]
    body = "\n".join(Brows + Crows + Erows)
    yes_lb, verdict, cs, no, bad = visibility_block(body)
    assert not no, no
    n_abs = sum("ABSENCE" in b[7] for b in B)
    n_nc = sum("not_a_claim" in b[7] for b in B)
    prompt_sha = L.run(["shasum", "-a", "256", os.path.join(L.TI, "04_Prompt.txt")]).stdout[:12]
    sql_sha = L.run(["shasum", "-a", "256", L.SQL_PATH]).stdout[:12]
    hdr = f"""# 08 OE Writing Ledger: leonard_stockholder_closeout (injection rev2)
Generated 2026-11-08 · Clock 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) · seed bound 2026-02-14T00:00:00Z · Persona Leonard Hayes leonard.hayes@harmonygames.co (Co-founder & Creative Director) · Tier Long-Horizon · Mode Medium
Status: READY: every requirement has verified facts, every scoped fact is persona-visible (pasted proof below), all write families map to cataloged tools, friction is none
Inputs read: 04_Prompt.txt present (sha256 {prompt_sha}) · 00_Assigments.md present · 01_Universe_Inject.sql present (sha256 {sql_sha}; the platform reviewed the same statements without the 4 header comment lines, 9b02cc8f34a9) · 01_Grounding_Dossier.md present (leads only) · 01_Scenario_Design.md and 01_Hardness_Manifest.json present (leads only) · 03_Error_Async_Config.txt present (Friction: none) · 02_Reference_Files none · 04_Prompt_Writing_Brief.md present (leads only; its section 4b predates rev2, so solver/truth.json and the platform /prompt report govern)

Persona binding: roster entry leonard_hayes, Leonard Hayes, Co-founder & Creative Director, leonard.hayes@harmonygames.co. Scoped services: Gmail (own mailbox), Slack (member of #winddown and #executives, and party to the DMs cited), Calendar (own), Drive, Docs, Sheets and Slides (own or shared files). Unscoped: Linear, Trello, Contacts.

Dates: Pacific first, UTC beside it. 'sent', 'created', 'posted' mark record times, all at or before the seed bound. Semantic future dates: Carta's last days to exercise, KPMG's due date 2/27/2026, Tuesday's holder notes; none is expected as done.

Locators use names and natural searches; opaque ids sit in the Expected data and Source pointer columns.
"""
    doc = hdr + f"""
## A · Requirements (traced to the prompt)
| R | Prompt span (quoted) | Type (Discovery / Write / Tell / Constraint) | Explicit / implicit | Fact IDs |
|---|---|---|---|---|
""" + "\n".join(A) + """

## B · Facts
| F | Fact / value | Service | Tool family (catalog) | Locator | Locator origin (prompt · F-n · search "query") | Expected data (dates typed: created / starts / due) | Ledger result for the Expected line (VERIFIED quote · not_a_claim · ABSENCE evidence_check · UNRESOLVED) | Persona-visible? (proof) | Depends on | Source pointer |
|---|---|---|---|---|---|---|---|---|---|---|
""" + "\n".join(Brows) + """

Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)

`python3 Task_Authoring/tools/persona_view.py check-sql leonard_hayes Task_Authoring/task_inputs/01_Universe_Inject.sql --load-bearing plan/oe/oe_lb_ids.txt`:

""" + "\n".join(yes_lb + verdict) + """

`python3 Task_Authoring/tools/persona_view.py can-see leonard_hayes (service) (id)`, first line of each:

""" + "\n".join(cs) + """

## C · Write capability
| R | Required write | Prompt authority (quoted; agent, not user-reserved) | Catalog tool (exists?) | Required parameters | Target (fact ID) | Completing end state | Content the prompt requires | Defer search (services · population · pagination complete · governing version · result, or UNRESOLVED) | Feasible? |
|---|---|---|---|---|---|---|---|---|---|
""" + "\n".join(Crows) + """

## D · Friction facts
| Function (01_) | Mode / rate / wait | Facts blocked | Alternative path (service, locator) | Alternative facts | Visible? |
|---|---|---|---|---|---|
| none | Friction: none (03_Error_Async_Config.txt) | none | none | none | none |

## E · Traps and distractors
| T | What the agent meets (pointer) | Competes with (fact ID) | Discriminator (timestamp / author / ID) |
|---|---|---|---|
""" + "\n".join(Erows) + """

## F · Open risks
| # | Risk | Facts affected | Consequence (OE accuracy / rubric / UGT / feasibility) | Check needed |
|---|---|---|---|---|
""" + "\n".join(Frows) + f"""

## G · Tally
Requirements {len(AR)} · facts {len(B)} · writes {len(CR)} (feasible {len(CR)}) · friction items 0 · expected values {len(B)} (quoted {len(B) - n_nc} · not_a_claim {n_nc} · ABSENCE-checked {n_abs}) · unverified visibility 0 · blocking 0

## Self-review

Walked Evals/2_Oracle_Events_Eval.md 1.1, 2.1 to 2.6 and 3.1 to 3.5 against this ledger in order. Every requirement has facts; every write family has its prompt authority, a cataloged tool with its parameters, a completing end state and a defer search; friction is none; every scoped fact carries pasted visibility proof. Every §B value was re-verified in this run: seeded values from the parsed SQL rows, base values through tools/hg.py (plan/oe/verify_facts.py re-read 115 record fields and confirmed 504 quotes, and the spans added after the blind review were re-read the same way), and plan/oe/build_events.py refuses any quoted span or figure on an Expected line that is not in a record. No-event-text scan: §B holds facts and dependency edges, with event wording kept in 08_Oracle_Events.md.

| R | Counter-reading (strongest other reading of the span, or a competing location) | Evidence that resolves it | Result |
|---|---|---|---|
| R1 | 'the holder project' could be another Linear project | F1: 'Holder records' is the only project with 'holder', created by Leonard Feb 12, and SQL L136 says one issue per holder | holds |
| R2 | the earlier outreach notes could govern, or the notes alone | T10: F4 opens 'These replace my earlier outreach notes.'; F9's replies under the list add the family rule and Arthur | holds |
| R3 | 'all of it' could be only the angels on Leonard's list | F1: 'one issue per holder on Carta, live or lapsed'; F4 'Everyone still holding something' | holds (26 lines) |
| R4 | a new sheet could be made rather than finishing the draft; the sheet could go to Robert only | F4: 'Finish my draft one in the folder rather than starting another'; F9: 'the sheet goes to you as well as Robert' | holds |
| R5 | the letter could be sent or could stay in Slack | F4: 'bring it up to date as a letter I can send'; 'everything goes in the close-out folder' | holds (a Doc, unsent) |
| R6 | one note per issue (26), or notes to the Covered lines | F4 'At most one note per person'; F9: one note covers the family's lines | holds (14) |
| R7 | states without comments, or comments on every issue | F1: 'On every issue with no note of its own, Canceled included, say why.' | holds (26 moves, 12 comments) |
| R8 | a reply on Robert's later mail, or a new mail | F4: 'as a reply to all on their own Board position mail'; T13 | holds |
| R9 | a new top-level post in #winddown | F4: 'reply under my list in #winddown'; F8 gives the thread | holds |
| R10 | today's option count, or the term sheet's 268,772 | F11: 'as of December 31, 2025' and the vesting clarification; T8; F{C5[1:]} | holds (243,757) |
| R11 | the KPMG reply or heads-up left as drafts | prompt 'Send the replies yourself'; F1 'Send KPMG's confirmation as a reply to all' | holds (sent) |
| R12 | the notes could be sent because 'Send the replies yourself' | prompt 'only the holder messages wait for me'; F4 'I read and send each note myself' | holds (drafts) |

Unresolved: none blocking. Open risks §F 1 to 7 go to the draft and rubric stages. Upstream gate paste: the prompt-writing and injection PASS blocks predate the readiness framework added in another session (see the handoff note).
"""
    assert "—" not in doc, "em dash in ledger"
    out = os.path.join(L.WF, "08_OE_Writing_Ledger.md")
    open(out, "w").write(doc)
    print("ledger", len(doc), "facts", len(B), "reqs", len(AR), "writes", len(CR), "yesLB", len(yes_lb), "cansee", len(cs), "bad", bad[:5], verdict)


if __name__ == "__main__":
    build()
