"""Brief §5 and §5a share this fact list: (fid, label, value, locator, met first / overturned by, search risk, service, query, want).
Design facts only. Imported by brief_searches.py and assemble_brief.py."""
import contextlib, io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import build_scenario as B
IDS = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
I, BASE, SL, MSG = B.IDS, B.BASE, IDS["slack_mid"], IDS["msg"]
TH = IDS["threads"]
term = B.term
F = [
 ("F1", "hub ask", "the model, the card, Contacts, the reply; leave the Sep 24 lead out", MSG["hub"], "first link (A1)", "—", "gmail", "DD publishing", I["hub_thread"]),
 ("F2", "ground rules doc", "who's in, status order, value, Q4 cash, keep value, first pick, reminders, layout", I["rule_doc"], "named by the hub; met second", "first-framing latch on F3", "gdocs", "ground rules", I["rule_doc"]),
 ("F3", "co-dev doc (decoy)", "co-dev terms, not DD", I["codev_doc"], "competing hit on a 'what we'd take' or 'terms' search", "decoy", "gdocs", "Co-dev", I["codev_doc"]),
 ("F4", "DD publishing card", "checklists, follow-up cards, nudges", I["dd_card"], "named by the hub", "—", "trello", "DD publishing", I["dd_card"]),
 ("F5", "DD publishing folder", "term sheets and the outreach sheet; the model's home", I["dd_folder"], "named by the hub", "—", "gdrive", "DD publishing", I["dd_folder"]),
 ("F6", "outreach sheet", "24 publishers, what each got", I["outreach_sheet"], "named by the rule doc", "stops here for the population", "gsheets", "outreach", I["outreach_sheet"]),
 ("F7", "May one-pager", "paid-traffic numbers only", I["onepager_deck"], "named by the standing line", "—", "gslides", "one-pager", I["onepager_deck"]),
 ("F8", "organic figure", "$0.50 D30 ARPI", BASE["organic_arpi"], "named by the rule doc; overturns the paid numbers in F27", "—", "slack", "D30 ARPI", BASE["organic_arpi"]),
 ("F9", "rights position", "retain code, IP and non-mobile distribution rights", BASE["rights_post"], "named by the rule doc as the August sync position", "value-first reading of Northglow", "slack", "non-mobile", BASE["rights_post"]),
 ("F10", "August sync doc", "same sentence on the agenda", BASE["sync_doc"], "named by the rule doc", "—", "gdocs", "Executives Biweekly Sync", BASE["sync_doc"]),
 ("F11", "Copperleaf's offer", "28 %, $32,000 net 30, 40,000 installs, respond by Oct 17", I["copperleaf_relay"], "off the sheet and off the inbox; a reply under the Sep 24 root", "rarely opens a thread under an unrelated post", "slack", "advance", I["copperleaf_relay"]),
 ("F12", "#analytics pointer", "a tech lead at a publisher, notes on ENG-2362", I["arthur_analytics"], "leads to F13", "no publisher name in the line", "slack", "deep links", I["arthur_analytics"]),
 ("F13", "Redwood's offer on ENG-2362", "24 %, $25,000 net 45, 40,000 installs, respond by Oct 31", "ENG-2362 comment " + I["eng2362_comment"], "behind F12", "prefers mail and Drive over Linear comments", "linear", "ENG-2362", "ENG-2362"),
 ("F14", "Kestrel post", "frozen every outside signing; anything on the table is off", I["kestrel_post"], "overturns Moonrail's term sheet", "says Kestrel only", "slack", "Kestrel", I["kestrel_post"]),
 ("F15", "Anika's contact", "Partnerships, Kestrel Group", I["anika_contact"], "joins Kestrel to Moonrail", "—", "contacts", "Anika", I["anika_contact"]),
 ("F16", "Arthur's SVB reply", "the first-look never hit the account; resent next week, lands in October", I["arthur_cash"], "overturns F25 and F26", "stops at 'went out today'", "slack", "first-look", I["arthur_cash"]),
 ("F17", "banker root", "Sep 8 post the reply sits under", BASE["banker_root"], "container of F16", "—", "slack", "banker", BASE["banker_root"]),
 ("F18", "70 % D1 root", "Sep 24 post the relay sits under", BASE["seventy_root"], "container of F11", "—", "slack", "70% D1", BASE["seventy_root"]),
 ("F19", "Matthew root", "Sep 17 post the standing line sits under", BASE["matthew_root"], "container of F20", "—", "slack", "talked to Matthew", BASE["matthew_root"]),
 ("F20", "standing line", "anyone who got the one-pager and still has an offer in hears $0.50 D30 ARPI; notes in Gmail drafts", I["standing_line"], "carried by the rule doc's last line", "reply under an unrelated root", "slack", "one-pager", I["standing_line"]),
 ("F21", "Tallwater note", "the advance is $40,000 now", I["pb_event"], "overturns Tallwater's term sheet", "description past the first lines", "gcal", "Tallwater", I["pb_event"]),
 ("F22", "F/up with Lena card", "comment: 30,000 installs, not 50,000", I["sunfold_card"], "overturns Sunfold's term sheet; comment " + I["sunfold_comment"], "card named for a person", "trello", "F/up with Lena", I["sunfold_card"]),
 ("F23", "F/up with Marek card", "comment: the $10K went out", I["oakline_card"], "claim met first (T1); comment " + I["oakline_card_comment"], "card named for a person", "trello", "F/up with Marek", I["oakline_card"]),
 ("F24", "ESG thread", "earliest signature Nov 14; Leonard confirms", I["esg_thread"], "overturns the rule doc's Oct 31, as the doc allows", "names no publisher", "gmail", "License paper timing", I["esg_thread"]),
 ("F25", "Oakline's paid mail", "$10,000 sent by wire Sep 29, ref OAK-2291", MSG["Oakline Games:2"], "claim met first (T1)", "stops here", "gmail", "first-look", TH["Oakline Games"]),
 ("F26", "Appodeal thread", "no terms; last message theirs", BASE["appodeal_thread"], "base cohort member", "—", "gmail", "Appodeal publishing Program", BASE["appodeal_thread"]),
 ("F27", "board note", "paid-traffic numbers, Apr 30", BASE["board_followup"], "claim met first (T13)", "—", "gmail", "Board Follow-Up", BASE["board_followup"]),
 ("F28", "Rayking thread", "Frederick's Sep 4 message is an unsent draft", BASE["rayking_thread"], "base cohort member", "reads the draft as a reply", "gmail", "Rayking", BASE["rayking_thread"]),
 ("F29", "Rayking DM", "we still owe them an answer", I["rayking_dm"], "settles F28", "—", "slack", "Rayking", I["rayking_dm"]),
 ("F30", "Homa talk", "co-dev path, out of scope", BASE["homa_codev"], "named out by the rule doc", "—", "slack", "focus Homa", BASE["homa_codev"]),
 ("F31", "NCsoft talk", "engine talks, out of scope", BASE["ncsoft_question"], "named out by the rule doc", "—", "slack", "NCsoft", BASE["ncsoft_question"]),
 ("F32", "Tilting Point ack", "UA funding form, out of scope", BASE["tilting_ack"], "named out by the rule doc", "—", "gmail", "Tilting Point", BASE["tilting_ack"]),
 ("F33", "Publishing Partners doc", "candidate list, not the population", BASE["partners_doc"], "decoy for the population", "—", "gdocs", "Publishing Partners", BASE["partners_doc"]),
 ("F34", "Biz Dev Notes", "April candidate list with a template", BASE["bizdev_doc"], "decoy for the population", "—", "gdocs", "Biz Dev Notes", BASE["bizdev_doc"]),
 ("F35", "Monday event", "Oct 6 17:00Z, the four execs", I["monday_event"], "context", "—", "gcal", "DD publishing", I["monday_event"]),
 ("F36", "Lena's contact", "already in Contacts", I["lena_contact"], "skip", "—", "contacts", "Lena", I["lena_contact"]),
 ("F37", "revenue table", "ANALYTICS.MONETIZATION.REVENUE_DAILY total_revenue_usd: Jul 2,078.33, Aug 721.55, Sep 381.11", "snowflake.wh_analytics__monetization__revenue_daily", "named by the rule doc", "the agent's system prompt doesn't advertise Snowflake; the doc names it", "snowflake", "REVENUE_DAILY", "REVENUE_DAILY"),
 ("F38", "the Sep 24 lead", "left out by the hub", BASE["lead"], "named out by the hub", "—", "slack", "looking for games", BASE["lead"]),
 ("F39", "Tamatem mention", "a name passed along, not in scope", BASE["tamatem"], "named out by the rule doc's passed-along sentence", "—", "slack", "Tamatem", BASE["tamatem"]),
 ("F40", "Apple Arcade post", "a dominoes lead nobody took", BASE["apple_arcade"], "not on the sheet, nobody came to us", "—", "slack", "signed someone for dominoes", BASE["apple_arcade"]),
]
PLAIN = {"Northglow Publishing": "Out on rights", "Pinegrove Games": "Out on rights", "Moonrail Studios": "Withdrawn"}
for m in B.M:
    k = m["key"]
    if m.get("base") or k in ("Copperleaf Games", "Redwood Arcade"):
        continue
    F.append((f"C:{k}", f"{k} thread", m["status"], TH[k], "cohort member", "per-record read", "gmail", k.split(" ")[0], TH[k]))
for k in B.TERM_DOCS:
    F.append((f"T:{k}", f"{k} term sheet", B.TERM_DOCS[k][:60], term(k), "named by the folder", "stale value on three sheets" if k in ("Oakline Games", "Tallwater Games", "Sunfold Mobile") else "per-record read", "gdocs", k + " - term sheet", term(k)))
