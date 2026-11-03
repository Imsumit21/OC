#!/usr/bin/env python3
"""Build 09_Rubrics.json, the V3 rubric_rows evidence and the 09 rubric writing plan for frederick_bridge_pipeline
(rev12). Every source value is read from its record here (seeded rows via base_check.parse_sql, base records via
hg.py get-many), never typed by hand. Run from the workspace root."""
import json, subprocess, sys
from pathlib import Path

WS = Path(__file__).resolve().parents[5]
TI = WS / "Task_Authoring/task_inputs"
sys.path.insert(0, str(WS / "Task_Authoring/tools"))
from base_check import parse_sql  # noqa: E402

SQL = parse_sql((TI / "01_Universe_Inject.sql").read_text())
ROOTS = json.loads((TI / "Working_Files/00_Task_Context.json").read_text())["source"]["paths"]
FRED = "frederick.stone@harmonygames.co"
REVIEWER = "Claude (model-drafted under GEN_EXECUTION §2; for the human author's review)"


def sql_row(table, identity):
    rows = [x["row"] for x in SQL if x["table"] == table and x["op"] == "insert"
            and all(x["row"].get(k) == v for k, v in identity.items())]
    assert len(rows) == 1, (table, identity, len(rows))
    return rows[0]


def get_json(service, rel, pointer):
    req = {"items": [{"service": service, "file": rel, "id": "v", "pointer": pointer, "max_chars": 65536}]}
    out = subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/hg.py"), "search", "get-many", "--request", "-",
                          "--task-dir", str(TI)], input=json.dumps(req), capture_output=True, text=True, cwd=WS)
    item = json.loads(out.stdout)["items"]["v"]
    assert item.get("encoding") == "rendered-json" and item.get("truncated") is False, (rel, pointer, item)
    return json.loads(item["text"])


HUB_T = ("gmail", f"{FRED}/1844724419788800011")
DOC = ("gdocs", "f_3b9e61c04d7a52e8f1a6c2")
FOLDER = ("gdrive", "d_5e8a1c3f9b07d2e64a1b93")
README = ("gdocs", "f_c61a0e93b7d24f58a2e917")
LIST = ("gsheets", "f_48247af79428823c3cac92")
CARD = ("trello", "68c5a49e8491a9d7faf869d0")
BOARD = ("trello", "640643a3fd8f3ca308d9318e")


def path(*hops):
    return [{"service": s, "id": i} for s, i in hops]


def review(ids, why):
    return {"reviewer": REVIEWER, "rationale": why, "evidence_ids": ids}


SNAP = ("The synth-cut snapshot is cut at the freeze (2025-09-30 23:59:59 PT); the record's own last-change time "
        "is before the freeze, so the exported body is its state at the freeze. ")


def S_sql(service, rid, table, identity, column, rec_col, hops, why, semantics="fact", mutable=False, rev=None):
    row = sql_row(table, identity)
    src = {"service": service, "id": rid, "source_file": "01_Universe_Inject.sql", "table": table,
           "identity": identity, "column": column, "source_value": row[column],
           "evidence_path": path(*hops), "reachability_rationale": why,
           "temporal_evidence": {"value_semantics": semantics, "mutable_state": mutable,
                                 "recorded_at_column": rec_col,
                                 "rationale": f"Seeded {table} row; {rec_col} = {row[rec_col]} (before the freeze)."}}
    if mutable:
        src["temporal_evidence"]["state_at_freeze_review"] = rev
    return src


def S_json(service, rid, rel, pointer, rec_pointer, hops, why, semantics="fact", mutable=False, rev=None):
    root = Path(ROOTS[service])
    value = get_json(service, rel, pointer)
    recorded = get_json(service, rel, rec_pointer)
    src = {"service": service, "id": rid, "source_file": str((root / rel).relative_to(WS)), "pointer": pointer,
           "source_value": value, "evidence_path": path(*hops), "reachability_rationale": why,
           "temporal_evidence": {"value_semantics": semantics, "mutable_state": mutable,
                                 "recorded_at_pointer": rec_pointer,
                                 "rationale": f"Base record; {rec_pointer} = {recorded} (before the freeze)."}}
    if mutable:
        src["temporal_evidence"]["state_at_freeze_review"] = rev
    return src


# ---- reusable sources --------------------------------------------------------------------------------------------
HUB_MSG = f"{FRED}/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>"
s_hub = S_sql("gmail", HUB_T[1], "gmail.gmail_messages", {"id": HUB_MSG}, "body_text", "date", [HUB_T],
              "The prompt names Leonard's Sep 30 email; it is the To copy in Frederick's inbox.")
s_doc = S_sql("gdocs", DOC[1], "gdocs.docs_documents", {"document_id": DOC[1]}, "body_text", "modified_time",
              [HUB_T, DOC], "Leonard's email asks for 'the groups and details in the Q4 update send list doc'; the doc is "
              "shared with Frederick.", mutable=True,
              rev=review([DOC[1], HUB_T[1]], SNAP + "Leonard's Sep 30 email (later than the doc's 2025-09-26T18:41Z "
                         "change) points to this doc as the rules in force."))
s_folder = S_sql("gdrive", FOLDER[1], "gdrive.drive_files", {"id": FOLDER[1]}, "name", "modified_time",
                 [HUB_T, FOLDER], "The prompt names 'my Q4 2025 investor update folder'; Frederick owns it.", mutable=True,
                 rev=review([FOLDER[1], HUB_T[1]], SNAP + "The Sep 30 email refers to 'your Q4 investor update folder'."))
s_readme = S_sql("gdocs", README[1], "gdocs.docs_documents", {"document_id": README[1]}, "body_text", "modified_time",
                 [HUB_T, FOLDER, README], "Leonard's email: 'the README in that folder says how to name it'; it sits "
                 "in Frederick's folder.", mutable=True,
                 rev=review([README[1], HUB_T[1]], SNAP + "The Sep 30 email points to this README for the name."))
s_card = S_json("trello", CARD[1], "data.json", "/cards/801/name", "/cards/801/dateLastActivity", [HUB_T, CARD],
                "The prompt names the Existing Investor Update card in Trello (unscoped).", mutable=True,
                rev=review([CARD[1], HUB_T[1]], SNAP + "The card's name is what the prompt and the Sep 30 email name."))
s_board = S_json("trello", BOARD[1], "data.json", "/boards/1/name", "/boards/1/dateLastActivity", [HUB_T, CARD, BOARD],
                 "The card's comments send the follow-up cards to 'To Do on this board' (Harmony Games).", mutable=True,
                 rev=review([BOARD[1], CARD[1]], SNAP + "Board name as exported at the freeze."))


def slack_seed(mid, chan_ts, why, extra_hops=()):
    return S_sql("slack", chan_ts, "slack.slack_messages", {"id": mid}, "text", "created_at",
                 [HUB_T, DOC, *extra_hops, ("slack", chan_ts)], why)


def gmail_seed(msg, thread, why, column="body_text", extra_hops=()):
    return S_sql("gmail", thread, "gmail.gmail_messages", {"id": msg}, column, "date",
                 [HUB_T, DOC, *extra_hops, ("gmail", thread)], why)


def gcal_seed(evt, column, why, semantics="fact"):
    return S_sql("gcal", evt, "gcal.gcal_events", {"event_id": evt, "calendar_id": FRED}, column, "created",
                 [HUB_T, DOC, ("gcal", evt)], why, semantics=semantics, mutable=True,
                 rev=review([evt, DOC[1]], SNAP + "Calendar entry on Frederick's own calendar, created before the freeze."))


def gcal_base(evt, idx, why, semantics="fact"):
    return S_json("gcal", evt, "data.json", f"/events/{idx}/summary", f"/events/{idx}/created",
                  [HUB_T, DOC, ("gcal", evt)], why, semantics=semantics, mutable=True,
                  rev=review([evt, DOC[1]], SNAP + "Calendar entry on Frederick's own calendar; the doc counts calls "
                             "'on Fred's calendar'."))


def gmail_base(tid, msg_idx, field, why):
    rel = f"threads/frederick@harmonygames.co_{tid}.json"
    return S_json("gmail", f"{FRED}/{tid}", rel, f"/messages/{msg_idx}/{field}", f"/messages/{msg_idx}/date_parsed",
                  [HUB_T, DOC, ("gmail", f"{FRED}/{tid}")], why)


def slack_base(chan, idx, ts, why):
    return S_json("slack", f"{chan}/{ts}", f"messages/{chan}/2025-09.json", f"/{idx}/text", f"/{idx}/ts",
                  [HUB_T, DOC, ("slack", f"{chan}/{ts}")], why)


def grid(r, c, why):
    return S_json("gsheets", LIST[1], "data.json", f"/sheets_spreadsheets/96/sheets/0/grid/{r}/{c}",
                  "/sheets_spreadsheets/96/modified_time", [HUB_T, DOC, LIST], why, mutable=True,
                  rev=review([LIST[1], DOC[1]], SNAP + "The doc reads the list 'as of 09/11'; the sheet was last changed "
                             "2025-09-15; the injected one-cell edit touches only the LVP row."))


s_robert = slack_seed("229090ba6b316b667d1a6451b0297a47", "C07C2866011/1759248360.377105",
                      "Reply in #executives (Frederick is a member) under Leonard's Sep 29 post; Slack search 'Sciplay' "
                      "finds it.")
s_paul = slack_seed("c5657466a4af062ceef9f7c3285aeb74", "D05S58U4SAK/1759251900.863415",
                    "Leonard's 1:1 DM with Frederick; Slack search 'Paul' finds it.")
s_angelpost = slack_seed("4921f321db5d08f936aac24a6a1d2af8", "C07C2866011/1758303600.418207",
                         "#executives post 'angel update' (member).")
s_anton25 = slack_seed("99b22482ddd77dd01b451afb39014839", "D05S58U4SAK/1758731100.281734",
                       "Leonard's 1:1 DM with Frederick; Slack search 'Anton' finds it.")
s_anton_signed = slack_seed("f7261dd1b05eb2da3b81fe7d8cde2854", "D05S58U4SAK/1758914100.640218",
                            "Same DM, Sep 26.")
s_signed_rule = slack_seed("20924cc7f5176991d8a97a8eafb291d0", "C07C2866011/1758911700.336170",
                           "The doc points to 'my note in #executives on what counts as signed'.")
s_arthur = slack_seed("3cddf83c394676d8b72c0c20ed58f520", "C0880U9751A/1759274400.518306",
                      "Root post in #zombie-match3d (member) by Arthur, whom the doc names as tracking the tester adds; "
                      "Slack search 'tester' finds it.")
s_completed = gmail_seed(f"{FRED}/<CAiKDPIoVSAFUBccUSRRBTi6dsmJdhof2EzteoIx@mail.gmail.com>", f"{FRED}/1844354293432320031",
                         "DocuSign Completed notice in Frederick's inbox; the signed rule requires it.", column="subject",
                         extra_hops=[("slack", "C07C2866011/1758911700.336170")])
s_edith = gmail_seed(f"{FRED}/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>", f"{FRED}/1844318935449600041",
                     "Edith Vane's pass, cc Frederick; subject 'Harmony Games bridge'.")
s_ilse = gmail_seed(f"{FRED}/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>", f"{FRED}/1844276782694400053",
                    "Ilse Marrow's reply in the 'Harmony Games - follow up' thread, cc Frederick.")
s_hiro_evt = gcal_seed("evt_7d3e19b04a6c25f8e1b9a0", "attendees_json",
                       "The Tue Sep 23 call on Frederick's calendar; its guest PERSON_9903_EMAIL is Edith Vane's address.")
s_bw_evt = gcal_seed("evt_2f86b0d4c9e17a35b64e0d", "summary", "The Sep 25 call 'Ilse Marrow and Leonard Hayes' on "
                     "Frederick's calendar.")
s_makers_evt = gcal_seed("evt_6b2e94d0c17a3f58e9d2b1", "summary", "The Oct 8 call on Frederick's calendar (a future "
                         "meeting at the clock; created Sep 29).", semantics="scheduled_event")
s_sciplay_call = gcal_base("evt_25c9ee60d4b6c8f6d39a74", 1525, "The Sep 15 SciPlay call on Frederick's calendar.")
s_lvp_call = gcal_base("evt_e59dc0a675d0c407b79acf", 9289, "The Sep 9 LVP call on Frederick's calendar.")
s_homa_call = gcal_base("evt_89381fe5a15b802c5652a9", 5523, "The Sep 18 Homa call on Frederick's calendar.")
s_a16z_call = gcal_base("evt_e802a3583ee79ff6087f76", 9414, "The Sep 18 speedrun interview on Frederick's calendar.")
s_gfr_call = gcal_base("evt_2204ffea306847eea6e5b0", 1368, "The Sep 30 GFR call on Frederick's calendar.")
s_ncsoft_call = gcal_base("evt_d2044af06de4e892ce1d0a", 8468, "The Sep 10 NCsoft call on Frederick's calendar.")
s_dentsu_mail = gmail_base("1843473831194478743", 0, "body", "Leonard's Sep 25 Dentsu mail confirming the Oct 1 1:30pm "
                           "meeting, cc Frederick; Gmail search 'Dentsu' finds it. The evidence also names the calendar entry "
                           "evt_3671b9a924ccba550e51fa (the deciding record per /rubric round 1); that entry was created "
                           "2025-10-01T00:02:03Z, after the 2025-10-01T00:00:00Z seed bound, so this pre-bound mail is the "
                           "dated source for the same booked meeting.")
s_lvp_mail = gmail_base("1842277743427687737", 1, "body", "LVP's Sep 25 answer in the 're-intros: Are (LVP)' thread, "
                        "cc Frederick; Gmail search 'LVP' finds it.")
s_homa_note = slack_base("C096HFA5Z8W", 252, "1758210489.170809", "Frederick's own #bridge-pitch note naming Homa.")
s_ih = slack_base("C096HFA5Z8W", 159, "1757716998.377299", "Leonard's #bridge-pitch post on outreach made on our behalf.")
s_bbq = slack_base("C096HFA5Z8W", 89, "1757345124.546449", "Leonard's Sep 8 #bridge-pitch status post, 'BBQ Capital (sent, no update)'.")
s_anel = gmail_base("1832208184829815962", 1, "body", "Anel's Sep 30 message in the NCsoft thread (sender shown as '(anel)'), cc Frederick; Gmail search '45min' finds it.")

DOC_SPAN = "His email lays out what he's after."
SORT_SPAN = "sort out who from the bridge round gets the Q4 investor update"
FOLDER_SPAN = "Please put the send list in my Q4 2025 investor update folder"
CARD_SPAN = "do what he asked on the Existing Investor Update card in Trello"
REPLY_SPAN = "reply on his thread with how many ended up in each group"

# ---- rows ------------------------------------------------------------------------------------------------------
# keys: t title, w weight, kind, why (kind reason), fact, span, oe, fids, vals, verify, final, acc, alt, srcs,
#       just, ev, dist, amb, dec, grp, ovl, valid, idle
R = []


def row(**k):
    R.append(k)


row(tag="folder", t="The Agent puts the bridge-round send list in Frederick's Drive folder \"Q4 2025 investor update\" "
      "(created there or moved there)", w=1, kind="lookup",
    why="direct: the prompt names the folder", fact="sheet_location",
    span=FOLDER_SPAN, oe=["OE 29", "OE 30", "OE 31"], fids="F4", vals="`Q4 2025 investor update` `d_5e8a1c3f9b07d2e64a1b93`",
    verify="Send list file in Frederick's folder", final="Drive file parent d_5e8a1c3f9b07d2e64a1b93",
    acc=["a send list file whose parent is the Q4 2025 investor update folder",
         "created in place or created elsewhere and moved"], alt="A file left in My Drive or in another folder fails. "
    "Creating the file in My Drive and moving it is the same end state.", srcs=[s_folder],
    just="Lookup: the prompt names the folder ('Please put the send list in my Q4 2025 investor update folder').",
    ev="Source: folder 'Q4 2025 investor update' d_5e8a1c3f9b07d2e64a1b93. Accept: a send list file whose final parent is "
       "that folder, created there or moved there.",
    dist="—", amb="—", dec="F4", grp="—", ovl="—", valid="A Sheet created in My Drive, then moved into the folder",
    idle="No file in 'Q4 2025 investor update' (an idle Agent creates nothing)")
row(tag="native", t="The Agent creates the bridge-round send list as a native Google Sheet or Google Doc", w=1,
    kind="lookup", why="direct: one line in the folder README", fact="sheet_type", span=FOLDER_SPAN,
    oe=["OE 29", "OE 30"], fids="F5", vals="`Google Sheets or Docs only`", verify="Send list file type",
    final="Drive file mimeType", acc=["a native Google Sheet", "a native Google Doc"],
    alt="An uploaded xlsx, csv or other file fails: the README says 'no uploads'.", srcs=[s_readme],
    just="Lookup: the README in the folder says 'Google Sheets or Docs only, no uploads'.",
    ev="Source: README f_c61a0e93b7d24f58a2e917 ('Google Sheets or Docs only, no uploads'). Accept: a native Google Sheet "
       "or Google Doc; an uploaded xlsx, csv or other file fails.",
    dist="—", amb="—", dec="F5", grp="—", ovl="—", valid="A Google Sheet 'Q4 update - send list'",
    idle="No send list file exists (an idle Agent creates nothing)")
row(tag="name", t="The Agent names the send list file \"Q4 update - send list\" (any letter case, spacing or dash style)", w=1,
    kind="lookup", why="direct: one line in the folder README", fact="sheet_name", span=FOLDER_SPAN, oe=["OE 29", "OE 30"],
    fids="F5", vals="`Q4 update - send list`", verify="Send list file name", final="Drive file name",
    acc=["Q4 update - send list", "Q4 Update - Send List", "Q4 update – send list", "Q4 update-send list"],
    alt="The README fixes the name, so other names fail; case, spacing and dash style are representational.",
    srcs=[s_readme], just="Lookup: the README says 'Name the send list \"Q4 update - send list\"'.",
    ev="Source: README f_c61a0e93b7d24f58a2e917. Accept: Q4 update - send list in any letter case, spacing or dash style.",
    dist="T1 (Q3 doc title 'Q3 investor update - send list') → the Q4 name", amb="—", dec="F5", grp="—", ovl="—",
    valid="File titled 'Q4 Update - Send List'", idle="No file named 'Q4 update - send list' exists")
row(tag="count25", t="The Agent lists exactly 25 recipients on the bridge-round send list, one row per firm or angel (header rows excluded "
      "from the count)", w=5, kind="multi-source", why="the count only follows from the full audit of 77 list names plus "
    "off-list calls, passes, signatures and Paul's back-out", fact="send_list_size", span=SORT_SPAN,
    oe=["OE 5", "OE 6", "OE 7", "OE 8", "OE 9", "OE 11", "OE 28", "OE 32"], fids="F6 F15 F39 F40 F13",
    vals="`25`", verify="Send list volume — number of recipient rows", final="Send list rows",
    acc=["25 recipient rows under any header", "rows in any order"], alt="26 (Paul Heydon added), 24 or any count other than "
    "25 fails; a separate tab or note of people kept off adds rows the doc says stay out of the sheet.",
    srcs=[s_doc, s_paul], just="Multi-source: 25 is what is left after reading every list name's Latest Status, Fred's "
    "calendar, #bridge-pitch, the outreach mail, the signed rule and Leonard's Sep 30 DM that Paul is out.",
    ev="Sources: send-list doc f_3b9e61c04d7a52e8f1a6c2 (who to look at; 'The ones who stay off don't go in the sheet'); "
       "Leonard's DM D05S58U4SAK/1759251900.863415 (Paul out). Accept: exactly 25 recipient rows.",
    dist="T2, T9, T10 (Paul post, send-to-everyone mail) → grade the count", amb="—", dec="DONE1 FILT C1 C4",
    grp="sheet (volume)", ovl="—", valid="A sheet with a header and 25 recipient rows", idle="No send list rows at all")
row(tag="sciplay", t="The Agent puts Sciplay in the Keep warm group on the bridge-round send list", w=5, kind="multi-source",
    why="SciPlay's own mail thread shows no pass; the pass is a phone call relayed in a #executives thread reply under "
    "another post, after the Sep 15 call", fact="group_sciplay", span=DOC_SPAN, oe=["OE 6", "OE 13", "OE 14", "OE 28", "OE 32"],
    fids="F18 F19", vals="`Sciplay` `Keep warm`", verify="Sciplay's group on the send list", final="Send list row for Sciplay",
    acc=["Keep warm", "keep warm", "Sciplay or SciPlay as the name"], alt="In talks (from the mail thread) fails; the "
    "Sep 30 reply is later and is a pass after a pitch call.", srcs=[s_robert, s_sciplay_call],
    just="Multi-source: the Sep 15 call on Fred's calendar plus Robert's Sep 30 reply 'Sciplay's out too ... passing on "
         "this round', which overrides the mail thread.",
    ev="Sources: Robert's reply C07C2866011/1759248360.377105; SciPlay call evt_25c9ee60d4b6c8f6d39a74. Accept: Keep warm.",
    dist="T5 (mail thread, list note) → grade Keep warm", amb="—", dec="CORR T3 C2", grp="group sample (hard)", ovl="—",
    valid="Row 'SciPlay | Keep warm'", idle="No Sciplay row exists")
row(tag="hiro", t="The Agent puts Hiro Capital in the Keep warm group on the bridge-round send list", w=5, kind="multi-source",
    why="the pass names no firm; Contacts maps Edith Vane to Hiro Capital and the Sep 23 call lists her as a guest",
    fact="group_hiro", span=DOC_SPAN, oe=["OE 6", "OE 16", "OE 17", "OE 28", "OE 32"], fids="F17",
    vals="`Hiro Capital` `Keep warm`", verify="Hiro Capital's group", final="Send list row for Hiro Capital",
    acc=["Keep warm"], alt="Awaiting reply (from the list's 09/11 note) fails: the Sep 26 pass after the Sep 23 call is later.",
    srcs=[s_edith, s_hiro_evt], just="Multi-source: Edith Vane's unnamed pass, her contact 'Partner, Hiro Capital' and the "
    "Sep 23 call that lists her address.", ev="Sources: Edith's mail frederick.stone@harmonygames.co/1844318935449600041; "
    "call evt_7d3e19b04a6c25f8e1b9a0; contact e3a91c07d5b48f26a0c7e314. Accept: Keep warm.",
    dist="T6 → grade Keep warm", amb="—", dec="ALIAS T5 C3", grp="group sample (hard)", ovl="—",
    valid="Row 'Hiro Capital | Keep warm'", idle="No Hiro Capital row exists")
s_treo = slack_seed("19e1e65d5952f075e8492867c6bcd472", "C096HFA5Z8W/1756942260.617302",
                    "Leonard's #bridge-pitch post on Treo VC (member); Slack search 'Treo' finds it.")
s_sep3 = slack_base("C096HFA5Z8W", 33, "1756941551.539229", "Leonard's Sep 3 #bridge-pitch outreach list ('Treeo VC').")
row(tag="treo", t="The Agent puts Treo VC (or Treo, Treeo VC) in the Awaiting reply group on the bridge-round send list", w=5,
    kind="multi-source", why="two Sep 3 #bridge-pitch posts (one spells it Treeo) read against the doc's 'that day "
    "included', with no call on Fred's calendar and no no", fact="group_treo", span=DOC_SPAN, oe=["OE 5", "OE 7", "OE 28", "OE 32"], fids="F28 F27",
    vals="`Treo VC` `Awaiting reply`", verify="Treo VC's group", final="Send list row for Treo VC",
    acc=["Awaiting reply", "Treo VC, Treo or Treeo VC as the name"], alt="Off the list (no Latest Status note, or the Sep 3 "
    "outreach read as before the kickoff) fails: the doc counts 'since the Sep 3 kickoff, that day included'.",
    srcs=[s_treo, s_sep3], just="Multi-source: Leonard's two Sep 3 #bridge-pitch posts (LinkedIn ping answered with the "
    "deck), the doc's 'that day included', and no call on Fred's calendar and no no.",
    ev="Sources: #bridge-pitch C096HFA5Z8W/1756942260.617302 and C096HFA5Z8W/1756941551.539229; doc f_3b9e61c04d7a52e8f1a6c2. "
       "Accept: Awaiting reply (Treo VC, Treo or Treeo VC as the name).",
    dist="T13-type spelling (Treeo) → grade the group", amb="—", dec="F28", grp="group sample (edge, ordinary member)",
    ovl="—", valid="Row 'Treo VC | Awaiting reply'", idle="No Treo VC row exists")
row(tag="homa", t="The Agent adds Homa (or HOMA, Homa Games, [PERSON_NAME_0854] as it appears in mail) to the bridge-round "
      "send list in the In talks group", w=5, kind="multi-source", why="off the 2025 list; found only through the Sep 18 call on Fred's calendar, "
    "and counted as investment talks through Fred's co-dev investment note", fact="group_homa", span=SORT_SPAN,
    oe=["OE 6", "OE 7", "OE 19", "OE 28", "OE 32"], fids="F20", vals="`Homa` `In talks`",
    verify="Homa on the send list and its group", final="Send list row for Homa",
    acc=["Homa", "HOMA", "Homa Games", "[PERSON_NAME_0854]"], alt="Leaving Homa off (the list read as the whole population) "
    "fails; a co-dev-only reading is overruled by Frederick's own note.", srcs=[s_homa_call, s_homa_note],
    just="Multi-source: the Sep 18 call on Fred's calendar, Frederick's #bridge-pitch note 'focus Homa on the co-dev "
         "investment path' and the follow-up mail.",
    ev="Sources: call evt_89381fe5a15b802c5652a9; #bridge-pitch C096HFA5Z8W/1758210489.170809; follow-up "
       "frederick.stone@harmonygames.co/1843552279434086285. Accept: Homa, HOMA, Homa Games or [PERSON_NAME_0854], In talks.",
    dist="T10 → grade inclusion", amb="—", dec="FILT T6 C4", grp="group sample (hard)", ovl="—",
    valid="Row 'HOMA | In talks'", idle="No Homa row exists")
row(tag="brightwater", t="The Agent adds Brightwater Games Fund (or Brightwater) to the bridge-round send list in the In "
      "talks group", w=5,
    kind="multi-source", why="off the 2025 list; the Sep 25 call, Ilse Marrow's signature and her non-pass reply",
    fact="group_brightwater", span=SORT_SPAN, oe=["OE 6", "OE 18", "OE 28", "OE 32"], fids="F21",
    vals="`Brightwater Games Fund` `In talks`", verify="Brightwater on the send list and its group",
    final="Send list row for Brightwater Games Fund", acc=["Brightwater Games Fund", "Brightwater"],
    alt="Leaving Brightwater off fails; 'come back to you next week' is not a pass.", srcs=[s_bw_evt, s_ilse],
    just="Multi-source: the Sep 25 call on Fred's calendar and Ilse Marrow's reply signed 'Principal, Brightwater Games Fund'.",
    ev="Sources: call evt_2f86b0d4c9e17a35b64e0d; thread frederick.stone@harmonygames.co/1844276782694400053. Accept: "
       "Brightwater or Brightwater Games Fund, In talks.", dist="T10 → grade inclusion", amb="—", dec="FILT T7 C4",
    grp="group sample (hard)", ovl="—", valid="Row 'Brightwater | In talks'", idle="No Brightwater row exists")
row(tag="a16z", t="The Agent puts Andreessen Horowitz (a16z) in the In talks group on the bridge-round send list", w=5,
    kind="multi-source", why="the Sep 18 speedrun interview on Fred's calendar, the doc's accelerator rule and the "
    "speedrun decline mail, which the rule sets aside as no bridge answer", fact="group_a16z", span=DOC_SPAN, oe=["OE 2", "OE 6", "OE 21", "OE 28", "OE 32"],
    fids="F2 F23", vals="`Andreessen Horowitz` `In talks`", verify="a16z's group", final="Send list row for a16z",
    acc=["Andreessen Horowitz", "a16z"], alt="Keep warm or off on the speedrun decline fails: the doc says the program's "
    "decision is not their answer on the bridge.", srcs=[s_a16z_call, s_doc],
    just="Multi-source: the Sep 18 speedrun interview on Fred's calendar, the doc's accelerator rule and the speedrun "
         "decline mail in Gmail, which the rule says is not their answer on the bridge.",
    ev="Sources: interview evt_e802a3583ee79ff6087f76; doc f_3b9e61c04d7a52e8f1a6c2 (accelerator rule). Accept: In talks.",
    dist="T8 → grade In talks", amb="—", dec="F23", grp="direct exception (named in the doc)", ovl="—",
    valid="Row 'a16z | In talks'", idle="No a16z row exists")
row(tag="anton_group", t="The Agent puts Anton Bernstein in the New investor group on the bridge-round send list", w=5,
    kind="multi-source", why="the #executives rule (Slack) joined with the DocuSign Completed notice (Gmail): new investor "
    "only once the notice is in",
    fact="anton_group", span=DOC_SPAN, oe=["OE 4", "OE 12", "OE 28", "OE 32"], fids="F7 F11",
    vals="`Anton Bernstein` `New investor`", verify="Anton's group", final="Send list row for Anton Bernstein",
    acc=["New investor"], alt="In talks fails: his Completed notice came in Sep 26.", srcs=[s_completed, s_signed_rule],
    just="Multi-source: Leonard's #executives rule on what counts as signed, joined with the Sep 26 DocuSign Completed "
         "notice in Gmail.",
    ev="Sources: Completed notice frederick.stone@harmonygames.co/1844354293432320031; rule C07C2866011/1758911700.336170. "
       "Accept: New investor.", dist="—", amb="—", dec="F11", grp="direct exception (core)", ovl="—",
    valid="Row 'Anton Bernstein | New investor | 25,000'", idle="No Anton Bernstein row exists")
row(tag="anton_amount", t="The Agent records 25,000 as Anton Bernstein's amount on the bridge-round send list (25000, $25,000, $25K or 25k "
      "also pass)", w=5, kind="multi-source", why="the post and the angels sheet say 40; a later DM cuts it to 25 and a "
    "second DM says the 25 SAFE was signed", fact="anton_amount", span=DOC_SPAN, oe=["OE 10", "OE 11", "OE 12", "OE 32"],
    fids="F8 F9 F10", vals="`25,000`", verify="Anton's amount", final="Amount cell of Anton's row",
    acc=["25,000", "25000", "$25,000", "$25K", "25k", "USD 25,000"], alt="40,000 (post and sheet) fails.",
    srcs=[s_anton25, s_anton_signed], just="Multi-source: Leonard's Sep 19 post ($40K) is overtaken by his Sep 24 DM "
    "('only do 25 this time, not the 40') and Sep 26 DM ('Anton signed the 25 one').",
    ev="Sources: DM D05S58U4SAK/1758731100.281734; DM D05S58U4SAK/1758914100.640218. Accept: 25,000 in any of those forms.",
    dist="T2 → grade 25,000", amb="—", dec="INPUT T4", grp="direct exception (core)", ovl="—",
    valid="Amount '$25K'", idle="No amount for Anton Bernstein exists")
row(tag="angels", t="The Agent lists exactly one angel (an individual investor, not a firm) on the bridge-round send list",
    w=5, kind="multi-source",
    why="Paul Heydon said yes in the post, is unsigned in the nudge, and backed out in a later 1:1 DM; the other list "
    "angels had no outreach", fact="angel_scope", span=SORT_SPAN, oe=["OE 5", "OE 10", "OE 11", "OE 12", "OE 28", "OE 32"],
    fids="F6 F8 F12 F13", vals="`1`", verify="Angel scope of the send list (Paul Heydon's back-out)",
    final="Angel rows of the send list", acc=["exactly one row for an individual investor"],
    alt="Two angel rows (Anton Bernstein plus Paul Heydon In talks at $50,000, from the post and the unsigned SAFE) fail: "
    "Leonard's Sep 30 DM says Paul is out.",
    srcs=[s_paul, s_angelpost], just="Multi-source: Leonard's Sep 19 post (two angels said yes), the Sep 29 nudge and the "
    "Sep 30 DM 'Paul's out'.",
    ev="Sources: DM D05S58U4SAK/1759251900.863415 (Paul out); post C07C2866011/1758303600.418207 (Paul and Anton said "
       "yes); list f_48247af79428823c3cac92 (angels No. 1–5). Accept: exactly one row for an individual investor.",
    dist="T2 → grade the angel scope", amb="—", dec="DONE1 T1 C1",
    grp="direct exception (Paul)", ovl="—", valid="One angel row, Anton Bernstein", idle="No angel rows at all")
for firm, shown, oe_n, accept_name in [
        ("Dentsu Ventures", "Dentsu Ventures (or Dentsu)", "OE 25", "Dentsu Ventures or Dentsu"),
        ("T-accelerate", "T-accelerate (or T-Accelerate, T-Accelerate Capital)", "OE 23",
         "T-accelerate, T-Accelerate or T-Accelerate Capital"),
        ("NCsoft", "NCsoft", "OE 22", "NCsoft"),
        ("Brightwater Games Fund", "Brightwater Games Fund (or Brightwater)", "OE 18", "Brightwater Games Fund or Brightwater")]:
    key = firm.split()[0].lower().replace("-", "_")
    row(tag=f"ba_{key}", t=f"The Agent records the build access for {shown} on the bridge-round send list as iOS only "
          f"(\"TestFlight only\" also passes)", w=5, kind="multi-source", why="ZOM-567 logs TestFlight and Play adds; Arthur's later Sep 30 post "
        "says the Play tester list never reached the internal track, and Leonard's reply shows Android still not live",
        fact=f"build_{key}", span=DOC_SPAN, oe=["OE 26", "OE 27", oe_n, "OE 28", "OE 32"], fids="F41 F42 F43 F44",
        vals="`iOS only`", verify=f"{firm} build access", final=f"Build access cell of {firm}'s row",
        acc=["iOS only", "TestFlight only", "iOS (TestFlight) only"], alt="iOS and Android (from ZOM-567) fails; "
        "none fails (TestFlight was added).", srcs=[s_arthur, s_doc],
        just="Multi-source: ZOM-567's add log against Arthur's later #zombie-match3d post naming this firm's testers.",
        ev="Sources: Arthur's post C0880U9751A/1759274400.518306; Leonard's reply C0880U9751A/1759276080.094417; ZOM-567 "
           f"(comments); doc f_3b9e61c04d7a52e8f1a6c2 (build access values). Accept: iOS only or TestFlight only for {accept_name}.",
        dist="T3, T4 → grade iOS only", amb="—", dec="DONE2 T2", grp="direct exception (Arthur's post names it)",
        ovl="—", valid=f"{firm} 'iOS only'", idle=f"No build access value for {firm} exists")
row(tag="ba_homa", t="The Agent records the build access for Homa (or HOMA, Homa Games, [PERSON_NAME_0854]) on the "
      "bridge-round send list as none", w=5, kind="multi-source",
    why="Homa is in talks only through the Sep 18 call; ZOM-567's add log and Arthur's later post name no Homa tester, so "
    "the doc's value for it is none", fact="build_homa", span=DOC_SPAN, oe=["OE 19", "OE 26", "OE 27", "OE 28", "OE 32"],
    fids="F20 F41 F42 F44", vals="`none`", verify="Homa build access", final="Build access cell of Homa's row",
    acc=["none", "None", "NONE"], alt="iOS only, Android only or iOS and Android fails (no tester add for Homa); a blank "
    "cell fails (blank is for angels).", srcs=[s_arthur, s_homa_call, s_doc],
    just="Multi-source: Homa is in talks only through the Sep 18 call on Fred's calendar; ZOM-567's add log and Arthur's "
         "later #zombie-match3d post name no Homa tester, so the doc's value is none.",
    ev="Sources: ZOM-567 (comments; no Homa tester add); Arthur's post C0880U9751A/1759274400.518306 (names four other "
       "firms); call evt_89381fe5a15b802c5652a9; doc f_3b9e61c04d7a52e8f1a6c2 ('Write iOS only, Android only, iOS and "
       "Android, or none'). Accept: none in any letter case for Homa, HOMA, Homa Games or [PERSON_NAME_0854]; a blank cell "
       "fails.", dist="T10 → grade none", amb="—", dec="FILT DONE2", grp="direct exception (no tester add; the 'none' value)",
    ovl="—", valid="HOMA 'none'", idle="No build access value for Homa exists")
for name, n, oe_items, fids, src2, why in [
        ("Keep warm", 3, "OE 37, OE 38, OE 39, OE 40", "F45 F40 F19", s_robert,
         "passes after a pitch call: LVP, Hiro (alias) and SciPlay (thread reply)"),
        ("New investor", 1, "OE 41, OE 42", "F46 F40 F11", s_completed, "the signed rule applied to both angels"),
        ("In talks", 7, "OE 43, OE 44, OE 45, OE 46, OE 47, OE 48, OE 49, OE 50", "F46 F40 F13", s_paul,
         "calls on Fred's calendar without a pass, minus SciPlay's pass and Paul's back-out, plus the two off-list firms"),
        ("Awaiting reply", 14, "OE 51, OE 52, OE 53, OE 54, OE 55, OE 56, OE 57, OE 58, OE 59, OE 60, OE 61, OE 62, OE 63, "
         "OE 64, OE 65", "F46 F34 F40", s_ih, "outreach since Sep 3 across the list, #bridge-pitch and mail with no call "
         "and no no")]:
    key = name.lower().replace(" ", "_")
    item_word = "item" if n == 1 else "items"
    art = "an" if name[0] in "AEIOU" else "a"
    title = (f"The Agent creates {art} {name} checklist on the Existing Investor Update Trello card holding exactly {n} "
             f"{item_word}")
    accept = (f"a checklist whose name contains the group name {name} (any letter case, spacing or plural; other words "
              f"around it are allowed) with exactly {n} {item_word}")
    row(tag=f"cl_{key}", t=title, w=5, kind="multi-source", why=f"the count follows only from the full group audit ({why})",
        fact=f"{key}_count", span=CARD_SPAN, oe=["OE 28", "OE 33"] + oe_items.split(", "), fids=fids, vals=f"`{n}`",
        verify=f"{name} checklist volume", final=f"{name} checklist on card 68c5a49e8491a9d7faf869d0",
        acc=[accept],
        alt=f"Any other count fails (e.g. {n + 1}).", srcs=[s_card, src2],
        just=f"Multi-source: Leonard's card comments ask for one checklist per group, one item per firm or angel; {n} is "
             f"the {name} group after the full audit.",
        ev=f"Sources: card 68c5a49e8491a9d7faf869d0 (comments 68c64270d660c977c4696986, 68db03b86054eff7e8e92474). "
           f"Accept: {accept}.",
        dist="—", amb="—", dec={"Keep warm": "CORR ALIAS C2 C3", "New investor": "INPUT F11",
                                 "In talks": "DONE1 CORR FILT C1", "Awaiting reply": "F34"}[name],
        grp=f"{name} checklist (volume)", ovl="—", valid=f"{name} checklist with {n} {item_word}",
        idle=f"No {name} checklist on the card")
    if name == "New investor":
        row(tag="item_anton", t="The Agent adds Anton Bernstein as an item on the New investor checklist of the Existing "
              "Investor Update Trello card", w=5, kind="multi-source",
            why="the card's one-item-per-firm-or-angel rule applied to the signed rule (Slack) and Anton's DocuSign "
            "Completed notice (Gmail)", fact="anton_group", span=CARD_SPAN, oe=["OE 33", "OE 41", "OE 42"],
            fids="F46 F11", vals="`Anton Bernstein`", verify="Anton item placement", final="New investor checklist item",
            acc=["Anton Bernstein"], alt="Paul Heydon as the New investor item fails: his SAFE has no Completed notice.",
            srcs=[s_card, s_completed, s_signed_rule],
            just="Multi-source: the Sep 29 card comment's one item per firm or angel, applied to Leonard's #executives "
                 "signed rule and Anton's Sep 26 DocuSign Completed notice.",
            ev="Sources: card 68c5a49e8491a9d7faf869d0 (comment 68db03b86054eff7e8e92474); Completed notice "
               "frederick.stone@harmonygames.co/1844354293432320031; rule C07C2866011/1758911700.336170. Accept: Anton "
               "Bernstein as an item on the New investor checklist.", dist="T2", amb="—", dec="INPUT F11",
            grp="New investor checklist (its one member)", ovl="—", valid="New investor item 'Anton Bernstein'",
            idle="No New investor checklist item 'Anton Bernstein'")
    if name == "Awaiting reply":
        row(tag="item_sony", t="The Agent adds Sony Mobile (or Sony) as an item on the Awaiting reply checklist of the "
              "Existing Investor Update Trello card", w=5, kind="multi-source",
            why="the list's Latest Status shows our outreach; the Sep 8 #bridge-pitch post adds an advisor's read that "
            "they aren't investing, which the doc says is not the firm's answer", fact="group_sony", span=CARD_SPAN,
            oe=["OE 33", "OE 51", "OE 60"], fids="F6 F29 F34 T17", vals="`Sony Mobile`", verify="Sony Mobile item placement",
            final="Awaiting reply checklist item", acc=["Sony Mobile", "Sony"],
            alt="Leaving Sony off (the advisor's read taken as a pass) fails: the doc says an advisor's own read isn't the "
            "firm's answer.", srcs=[s_card, s_bbq, s_doc],
            just="Multi-source: the list's Latest Status 'Reached out - no response as of 09/11', Leonard's Sep 8 "
                 "#bridge-pitch post with an advisor's read, and the doc's rule that an advisor's read isn't the firm's answer.",
            ev="Sources: list f_48247af79428823c3cac92 (No. 83 Sony Mobile, Latest Status 'Reached out - no response as of "
               "09/11'); #bridge-pitch C096HFA5Z8W/1757345124.546449 (Sony line: 'they are not investing in content right now "
               "according IH'); doc f_3b9e61c04d7a52e8f1a6c2 ('An advisor's own read on whether a "
               "firm invests isn't the firm's answer.'); card comment 68db03b86054eff7e8e92474. Accept: Sony Mobile or "
               "Sony on the Awaiting reply checklist.", dist="T17", amb="—", dec="F34 T17",
            grp="Awaiting reply checklist sample (edge: advisor's read)", ovl="—", valid="Awaiting reply item 'Sony Mobile'",
            idle="No Awaiting reply checklist item for Sony Mobile")
row(tag="item_sciplay", t="The Agent adds Sciplay as an item on the Keep warm checklist of the Existing Investor Update "
      "Trello card", w=5,
    kind="multi-source", why="the card's Keep warm rule joined with Robert's Sep 30 #executives reply, which overrides "
    "SciPlay's mail thread", fact="group_sciplay",
    span=CARD_SPAN, oe=["OE 33", "OE 37", "OE 40"], fids="F45 F19", vals="`Sciplay`", verify="SciPlay item placement",
    final="Keep warm checklist item", acc=["Sciplay", "SciPlay"], alt="Sciplay on the In talks checklist fails.",
    srcs=[s_card, s_robert], just="Multi-source: the Keep warm rule comment on the card, Robert's Sep 30 #executives reply "
    "('Sciplay's out too') and the Sep 15 call on Fred's calendar, which override SciPlay's mail thread.",
    ev="Sources: card 68c5a49e8491a9d7faf869d0 (comment 68c64270d660c977c4696986); reply C07C2866011/1759248360.377105. "
       "Accept: Sciplay or SciPlay on the Keep warm checklist.", dist="T5", amb="—", dec="CORR T3 C2",
    grp="Keep warm checklist sample (hard)", ovl="—", valid="Keep warm item 'SciPlay'", idle="No Keep warm checklist item 'Sciplay'")
row(tag="item_homa", t="The Agent adds Homa (or HOMA, Homa Games, [PERSON_NAME_0854]) as an item on the In talks checklist "
      "of the Existing Investor Update Trello card", w=5, kind="multi-source", why="the Sep 29 checklist rule applied to "
    "an off-list firm found only through the Sep 18 call on Fred's calendar and Fred's co-dev investment note", fact="group_homa", span=CARD_SPAN, oe=["OE 33", "OE 43", "OE 49"], fids="F46 F20",
    vals="`Homa`", verify="Homa item placement", final="In talks checklist item", acc=["Homa", "HOMA", "Homa Games",
    "[PERSON_NAME_0854]"], alt="No Homa item (the list treated as the whole population) fails.", srcs=[s_card, s_homa_call],
    just="Multi-source: the Sep 29 comment's one item per firm, applied to an off-list firm found only through the Sep 18 "
         "call on Fred's calendar and Fred's #bridge-pitch note on the co-dev investment path.",
    ev="Sources: card 68c5a49e8491a9d7faf869d0 (comment 68db03b86054eff7e8e92474); call evt_89381fe5a15b802c5652a9. "
       "Accept: Homa, HOMA, Homa Games or [PERSON_NAME_0854] on the In talks checklist.", dist="T10", amb="—",
    dec="FOLLOW FILT T8 C5", grp="In talks checklist sample (hard)", ovl="—", valid="In talks item 'HOMA'",
    idle="No In talks checklist item for Homa")
row(tag="cards18", t="The Agent creates exactly 18 new follow-up cards (named \"F/up with\" and a firm or contact name) in the To Do "
      "list of the Harmony Games Trello board", w=5, kind="multi-source", why="In talks plus Awaiting reply (21), minus "
    "NCsoft's existing Anel card and Dentsu and Makers, who have meetings on Fred's calendar after Sep 30",
    fact="followup_card_count", span=CARD_SPAN, oe=["OE 34", "OE 35", "OE 36", "OE 66", "OE 83"], fids="F46 F47 F48 F49 F50",
    vals="`18`", verify="Follow-up card volume", final="New open cards in To Do 640643a3fd8f3ca308d93195",
    acc=["18 new cards named 'F/up with' plus a firm or contact name"], alt="19 (a Dentsu, Makers, NCsoft or SciPlay card) "
    "or 20 fails; 21 (no exceptions) fails.", srcs=[s_board, s_makers_evt, s_dentsu_mail],
    just="Multi-source: the Sep 29 card comment's rules applied to the groups, the To Do list (the Anel card) and Fred's "
         "calendar after Sep 30 (Dentsu Oct 1, Michael Cheung of Makers Fund Oct 8).",
    ev="Sources: board 640643a3fd8f3ca308d9318e (list To Do 640643a3fd8f3ca308d93195); Makers call "
       "evt_6b2e94d0c17a3f58e9d2b1 (Oct 8); Dentsu meeting evt_3671b9a924ccba550e51fa (Oct 1 1:30pm PT; confirmed in Leonard's "
       "Sep 25 mail frederick.stone@harmonygames.co/1843473831194478743). Accept: exactly 18 new "
       "cards in To Do named 'F/up with' and a firm or contact name.", dist="T11, T12 → grade the count", amb="—", dec="DUP BOOKED T12 T13 C6 C7",
    grp="cards (volume)", ovl="—", valid="18 cards 'F/up with GFR Fund' etc.", idle="No new cards in To Do")
for firm, names, oe_n, src2, dec, fid, why, just, extra in [
        ("GFR Fund", ["GFR Fund", "GFR", "PERSON_0787_NAME", "[PERSON_NAME_2306]"], "OE 66", s_gfr_call, "DUP F22",
         "card_gfr", "IH's Sep 12 outreach and the Sep 30 call on Fred's calendar with no pass put GFR In talks; no open "
         "To Do card exists for it",
         "Multi-source: IH's Sep 12 #bridge-pitch outreach, the Sep 30 call on Fred's calendar with no pass, and the Sep 29 "
         "card rule for In talks firms without an open card.",
         " (call title 'Leonard Hayes and PERSON_0787_NAME'); list f_48247af79428823c3cac92 (No. 7 GFR Fund, Partner "
         "[PERSON_NAME_2306])"),
        ("BBQ Capital", ["BBQ Capital", "BBQ"], "OE 75", s_bbq, "BOOKED F34", "card_bbq",
         "outreach in the Sep 3 and Sep 8 #bridge-pitch posts, no call on Fred's calendar and no pass put BBQ in Awaiting "
         "reply; no open To Do card and no call after Sep 30",
         "Multi-source: Leonard's Sep 3 #bridge-pitch post ('BBQ Capital (sent)') and Sep 8 post ('BBQ Capital (sent, no "
         "update)'), no call on "
         "Fred's calendar, no open To Do card, and the Sep 29 card rule.", " ('BBQ Capital (sent, no update)')"),
        ("Brightwater Games Fund", ["Brightwater Games Fund", "Brightwater", "Ilse Marrow", "Ilse"], "OE 70", s_bw_evt,
         "FILT F21", "card_brightwater", "the Sep 25 call and Ilse Marrow's signed non-pass reply put this off-list firm "
         "In talks; no open To Do card and no call after Sep 30",
         "Multi-source: the Sep 25 call on Fred's calendar, Ilse Marrow's reply signed 'Principal, Brightwater Games Fund', "
         "no open To Do card and no call after Sep 30, under the Sep 29 card rule.",
         " (call 'Ilse Marrow and Leonard Hayes'); thread frederick.stone@harmonygames.co/1844276782694400053 (Ilse "
         "Marrow, Principal, Brightwater Games Fund)")]:
    shown = ", ".join(names[:-1]) + " or " + names[-1]
    row(tag=fid, t=f"The Agent creates a follow-up card for {firm} in the To Do list of the Harmony Games Trello board (named "
          f"\"F/up with\" and {shown})", w=5, kind="multi-source",
        why=why, fact=fid, span=CARD_SPAN,
        oe=["OE 36", oe_n], fids="F46 F50", vals=f"`{firm}`", verify=f"{firm} follow-up card", final="Card in To Do",
        acc=[f"F/up with {x}" for x in names],
        alt="A card in another list fails.", srcs=[s_board, src2],
        just=just,
        ev=f"Sources: board 640643a3fd8f3ca308d9318e (To Do 640643a3fd8f3ca308d93195); comment 68db03b86054eff7e8e92474; "
           f"{firm} evidence {src2['id']}{extra}. Accept: a card in To Do named 'F/up with' and {shown}.",
        dist="—", amb="—", dec=dec,
        grp="cards sample", ovl="—", valid=f"Card 'F/up with {firm}'", idle=f"No card for {firm} in To Do")
row(tag="ncsoft_comment", t="The Agent adds a new comment for NCsoft's Q4 follow-up on the existing To Do card \"F/up with Anel after the "
      "engine deep dive\"", w=5, kind="multi-source", why="the open card names only a first name; the 2025 list's Partner "
    "column maps Anel Ceman to NCsoft, and the rule says comment instead of a second card", fact="ncsoft_comment",
    span=CARD_SPAN, oe=["OE 5", "OE 34", "OE 84"], fids="F47 F48", vals="`F/up with Anel after the engine deep dive`",
    verify="NCsoft comment on the Anel card", final="Comment on card 68c99e98737744bd966aed24",
    acc=["any new comment text that marks NCsoft's Q4 follow-up"], alt="A new 'F/up with NCsoft' card instead fails.",
    srcs=[s_anel, s_ncsoft_call], just="Multi-source: the To Do card's partner name, the list's Partner column (and Anel's NCsoft thread) and the "
    "Sep 29 rule to comment on an existing card.", ev="Sources: list f_48247af79428823c3cac92 (NCsoft Partner Anel Ceman); NCsoft thread frederick.stone@harmonygames.co/1832208184829815962 (Anel); "
    "Anel card 68c99e98737744bd966aed24; rule comment 68db03b86054eff7e8e92474. Accept: any new comment on that card about "
    "NCsoft's Q4 follow-up.", dist="T11", amb="—", dec="DUP T12 C6", grp="direct exception (existing card)", ovl="—",
    valid="Comment 'NCsoft is In talks for the Q4 update'", idle="No new comment on the Anel card")
row(tag="reply", t="The Agent sends a reply on Leonard Hayes's Sep 30 email \"Q4 investor update - send list\" to "
      "leonard.hayes@harmonygames.co (reply-all also passes)", w=1, kind="lookup", why="direct: the thread is the one the "
    "prompt names", fact="reply_sent", span=REPLY_SPAN, oe=["OE 1", "OE 86"], fids="F1",
    vals="`leonard.hayes@harmonygames.co`", verify="Reply delivery", final="Sent message in thread 1844724419788800011",
    acc=["a sent reply to Leonard", "a reply-all to Leonard, Robert and Arthur"], alt="A draft fails; a new thread fails.",
    srcs=[s_hub], just="Lookup: the prompt says to reply on Leonard's thread.",
    ev="Source: Leonard's email frederick.stone@harmonygames.co/1844724419788800011. Accept: a sent reply or reply-all on "
       "that thread.", dist="—", amb="—", dec="F1", grp="—", ovl="—", valid="Reply-all on the thread",
    idle="No reply on the thread")
for name, n, split, src2, dec, fids in [("New investor", 1, "1 angel and 0 firms", s_completed, "INPUT F11", "F40 F51"),
                                        ("In talks", 7, "7 firms and 0 angels", s_paul, "DONE1 FILT CORR", "F40 F51"),
                                        ("Awaiting reply", 14, "14 firms and 0 angels", s_ih, "F34", "F40 F51"),
                                        ("Keep warm", 3, "3 firms and 0 angels", s_robert, "CORR ALIAS", "F40 F51")]:
    key = name.lower().replace(" ", "_")
    row(tag=f"cnt_{key}", t=f"The Agent states in its reply to Leonard that the {name} group has {n} ({split}; {n} as one number also "
          f"passes)", w=5, kind="multi-source", why="the count follows only from the full group audit",
        fact=f"{key}_count", span=REPLY_SPAN, oe=["OE 85", "OE 86"], fids=fids, vals=f"`{n}`",
        verify=f"{name} count in the reply", final="Reply body", acc=[f"{n}", split, f"{split.split(' and ')[0]}"],
        alt=f"Any other {name} total fails (e.g. {n + 1}).", srcs=[s_hub, src2],
        just=f"Multi-source: Leonard asks for 'how many firms and angels are in each group'; {n} is the {name} group after "
             f"the full audit.",
        ev=f"Sources: Leonard's email frederick.stone@harmonygames.co/1844724419788800011; groups per the send list. "
           f"Accept: {n} for {name}, as one number or split as {split}.", dist="—", amb="—", dec=dec,
        grp="told fact", ovl="—", valid=f"'{name}: {split.replace(' and ', ', ')}'", idle="No reply sent")

row(tag="order_file", t="The Agent sends its reply on Leonard's thread only once its writes to the send list file "
      "(creating, moving, renaming or editing it) are finished (at least one such write comes before the reply and none "
      "after it)", w=1, cat="Process",
    kind="lookup", why="one ordering condition read from Leonard's 'Please put it in your Q4 investor update folder ... "
    "Once it's done reply here'", fact="reply_order_file", span=REPLY_SPAN,
    oe=["OE 30", "OE 32", "OE 86"], fids="F1", vals="`Once it's done reply here`", verify="Order: reply after the send list writes",
    final="Order of the reply and the send list file writes (creating, moving, renaming or editing it)",
    acc=["at least one send list file write (creating, moving, renaming or editing it) before the reply and none after it"],
    alt="A reply sent before the send list exists, or a send list write after the reply, fails.", srcs=[s_hub],
    just="Lookup: Leonard's email asks for the send list in the folder, then says 'Once it's done reply here', so the "
         "reply follows the send list writes; no Outcome row can show the order.",
    ev="Source: Leonard's email frederick.stone@harmonygames.co/1844724419788800011 ('Please put it in your Q4 investor "
       "update folder ... Once it's done reply here with how many firms and angels are in each group'). Accept: at least "
       "one write to the send list file (creating, moving, renaming or editing it) comes before the reply, and none of "
       "those writes comes after it.",
    dist="—", amb="—", dec="F1", grp="—", ovl="—", valid="Send list created, moved and filled, then the reply",
    idle="No reply sent")
row(tag="order_checklists", t="The Agent sends its reply on Leonard's thread only once its checklist writes on the "
      "Existing Investor Update Trello card are finished (at least one checklist write on that card comes before the reply "
      "and none after it)", w=1, cat="Process",
    kind="lookup", why="one ordering condition read from Leonard's 'Then do what I put on the Existing Investor Update "
    "card in Trello. Once it's done reply here'; the reply's group counts are the checklists' sizes",
    fact="reply_order_checklists", span=REPLY_SPAN,
    oe=["OE 37", "OE 65", "OE 86"], fids="F1 F46", vals="`Once it's done reply here`",
    verify="Order: reply after the checklist writes on the card",
    final="Order of the reply and the checklist and checklist-item writes on card 68c5a49e8491a9d7faf869d0",
    acc=["at least one checklist write on the card before the reply and no checklist write of any kind on it after"],
    alt="A reply sent before any checklist exists, or any checklist write on the card (adding, renaming, ticking or "
        "deleting a checklist or item) after the reply, fails.",
    srcs=[s_hub, s_card],
    just="Lookup: Leonard's email says 'Then do what I put on the Existing Investor Update card in Trello. Once it's done "
         "reply here', and the reply reports the group counts the checklists hold; no Outcome row can show the order.",
    ev="Sources: Leonard's email frederick.stone@harmonygames.co/1844724419788800011 ('Then do what I put on the Existing "
       "Investor Update card in Trello. Once it's done reply here with how many firms and angels are in each group'); card "
       "68c5a49e8491a9d7faf869d0. Accept: at least one checklist write on that card comes before the reply, and no "
       "checklist write of any kind on that card (adding, renaming, ticking or deleting a checklist or item) comes after it.",
    dist="—", amb="—", dec="F1", grp="—", ovl="—", valid="Four checklists and their items first, then the reply",
    idle="No reply sent")

row(tag="order_cards", t="The Agent sends its reply on Leonard's thread only once its new follow-up cards in the To Do "
      "list of the Harmony Games Trello board are created (at least one new card comes before the reply and none after it)",
    w=1, cat="Process", kind="lookup", why="one ordering condition read from Leonard's 'Then do what I put on the Existing "
    "Investor Update card in Trello. Once it's done reply here'; the cards are a separate write action from the checklists",
    fact="reply_order_cards", span=REPLY_SPAN, oe=["OE 36", "OE 83", "OE 86"], fids="F1 F46 F50",
    vals="`Once it's done reply here`", verify="Order: reply after the follow-up cards",
    final="Order of the reply and the new cards in To Do 640643a3fd8f3ca308d93195",
    acc=["at least one new card in To Do before the reply and no new card in that list after it"],
    alt="A reply sent before any follow-up card exists, or a new To Do card created after the reply, fails.",
    srcs=[s_hub, s_board],
    just="Lookup: Leonard's email says 'Then do what I put on the Existing Investor Update card in Trello. Once it's done "
         "reply here', and the Sep 29 card comment asks for the follow-up cards in To Do; no Outcome row can show the order.",
    ev="Sources: Leonard's email frederick.stone@harmonygames.co/1844724419788800011 ('Once it's done reply here'); comment "
       "68db03b86054eff7e8e92474 on card 68c5a49e8491a9d7faf869d0 ('everyone In talks or Awaiting reply gets a follow-up "
       "card in To Do on this board'). Accept: at least one new card created in the To Do list of board "
       "640643a3fd8f3ca308d9318e before the reply, and no new card created in that list after it.",
    dist="—", amb="—", dec="F1", grp="—", ovl="—", valid="18 follow-up cards in To Do first, then the reply",
    idle="No reply sent")
row(tag="order_comment", t="The Agent sends its reply on Leonard's thread only after it adds its new comment on the existing "
      "To Do card \"F/up with Anel after the engine deep dive\"", w=1, cat="Process", kind="lookup",
    why="one ordering condition read from Leonard's 'Once it's done reply here'; the comment is a separate write action "
    "from the cards and checklists", fact="reply_order_comment", span=REPLY_SPAN, oe=["OE 84", "OE 86"], fids="F1 F47 F48",
    vals="`Once it's done reply here`", verify="Order: reply after the Anel card comment",
    final="Order of the reply and the new comment on card 68c99e98737744bd966aed24",
    acc=["the new comment on the Anel card is added before the reply is sent"],
    alt="A reply sent before the comment, or no comment at all, fails.", srcs=[s_hub, s_card],
    just="Lookup: Leonard's email says 'Once it's done reply here', and the Sep 29 card comment says to comment on an "
         "existing To Do card instead of adding another; no Outcome row can show the order.",
    ev="Sources: Leonard's email frederick.stone@harmonygames.co/1844724419788800011 ('Once it's done reply here'); comment "
       "68db03b86054eff7e8e92474 ('If one of them already has a card in To Do, comment on that card instead of adding "
       "another'); Anel card 68c99e98737744bd966aed24. Accept: the new comment on that card is added before the reply is sent.",
    dist="—", amb="—", dec="F1", grp="—", ovl="—", valid="Comment on the Anel card, then the reply",
    idle="No reply sent")

# ---- outputs ---------------------------------------------------------------------------------------------------
rubric = [{"title": r["t"], "category": r.get("cat", "Outcome"), "weight": r["w"], "justification": r["just"], "evidence": r["ev"]}
          for r in R]
(TI / "09_Rubrics.json").write_text(json.dumps(rubric, indent=1, ensure_ascii=False) + "\n")


def ahash(p):
    return subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/stage_gate.py"), "--artifact-hash", str(p)],
                          capture_output=True, text=True, cwd=WS).stdout.strip()


ev_path = TI / "Working_Files/00_V3_Authoring_Evidence.json"
ev = json.loads(ev_path.read_text())
ev["rubric_hash"] = ahash(TI / "09_Rubrics.json")
ev["prompt_hash"] = ahash(TI / "04_Prompt.txt")
ev["rubric_rows"] = [{"criterion_id": f"C{i + 1}", "fact_id": r["fact"], "prompt_span": r["span"],
                      "accepted_outcomes": r["acc"], "alternatives_review": r["alt"], "source_records": r["srcs"]}
                     for i, r in enumerate(R)]
ev_path.write_text(json.dumps(ev, indent=1, ensure_ascii=False) + "\n")
json.dump([{k: v for k, v in r.items() if k != "srcs"} for r in R], open(Path(__file__).with_name("rows.json"), "w"),
          indent=1, ensure_ascii=False)
print(len(R), "rows; weight", sum(r["w"] for r in R), "; rubric_hash", ev["rubric_hash"])
