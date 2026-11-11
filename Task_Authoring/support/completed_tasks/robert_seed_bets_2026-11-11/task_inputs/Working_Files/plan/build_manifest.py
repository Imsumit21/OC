# exec'd by build_scenario.py: manifest, surface, tables
def s_at(ptr):
    return dt.datetime.fromtimestamp(float(ptr.split("/")[1]), dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
SENT = {}
for n in NOT:
    SENT.setdefault(n["thread"], n["sent"])
def sent(f):
    return SENT[f].replace("+00:00", "Z")
H = IDS; B = BASE
ctx = {k: CTX[k] for k in ("context_hash", "assignment_hash", "policy_hash", "freeze_utc", "difficulty_mode")}
REQ = {
 "R1": "per-payee figure: what each payee on the bank was paid, from the Payment Processed notices, one sheet row per payee (paid figure)",
 "R2": "money that left and stayed out: a returned wire does not count, money moved between the company's own accounts is not spending (paid figure, left-out rows)",
 "R3": "a contractor paid some other way goes in only if a receipt for it reached Robert's mail, at the amount sent (paid figure)",
 "R4": "buckets: Build, Marketing, Company; Marketing stays out of build cost and Company sits on its own line (bucket per payee)",
 "R5": "which bet: the notice's Transaction Date against the bet calendar, each payment whole to one bet (bet columns, build cost per bet)",
 "R6": "anything not paid in dollars stays in its own currency next to the line and out of dollar totals (company line)",
 "R7": "what each game brought in: lifetime revenue from the warehouse's daily revenue table, as recorded, with Combo Fighter's left off for now (revenue per game)",
 "R8": "the sheet in Robert's Drive with the working sheet's layout, shared with Leonard and Arthur",
 "R9": "the Payee history project: each issue moved to Done once its line is right; a reason on the issue where the figure differs from the notices",
 "R10": "a reply to Leonard in #winddown with what each bet cost and brought in, what changes on the draft deck, and the sheet's link",
}
services = {
 "slack": {"role": "the ask in #winddown (anchor); #admin_foundersonly Apr 2024 wire notes; Robert's company card note; #leapblock statement; #playablex, #executives game ties", "weight_reason": "the ask, the returned wire, the off-bank route and Leapblock's statement"},
 "gmail": {"role": "132 Payment Processed notices and the Awaiting and Recipient notices; five Western Union receipts; Node Media's mail; Arthur's Chase mail; the Angel calls invitation", "weight_reason": "the record every figure starts from, plus the deciding receipts and the correction"},
 "linear": {"role": "the Payee history project (anchor), 22 issues with what Leonard and Arthur remember; closes and reason comments", "weight_reason": "the cohort, the per-payee notes and the follow-through writes"},
 "gdocs": {"role": "Leonard's method doc (H1); the Leapblock MSA", "weight_reason": "what counts, buckets, bet calendar and the exception"},
 "gdrive": {"role": "Robert's root (write home); Drive rows of the seeded doc, sheet and deck", "weight_reason": "the sheet must sit in Robert's own Drive and be shared"},
 "gsheets": {"role": "Leonard's working sheet (layout source, quick pass by date); the P&L costs tab; the sheet Robert writes", "weight_reason": "the layout the ask names and the graded register"},
 "gslides": {"role": "Leonard's draft deck with the quick figures", "weight_reason": "the ask wants what changes on it, so its figures are compared with the result"},
 "snowflake": {"role": "ANALYTICS.MONETIZATION.REVENUE_DAILY (H2), base only", "weight_reason": "lifetime revenue per game"},
 "trello": {"role": "Leonard's older quick plan on the Harmony Games board, replaced by the method; read only", "weight_reason": "a superseded plan the method names"},
 "contacts": {"role": "the contact row that spells the Telegram contractor's name", "weight_reason": "a name the notices token out; the contract search needs it"},
 "gcal": {"role": "the Angel calls hold on Leonard's and Robert's calendars", "weight_reason": "when the figures are needed; context, holds no graded fact"},
}
anchors = [
 {"id": "AN1", "service": "slack", "locator": H["ask"], "prompt_reference": "Leonard's ask in #winddown", "requirement_ids": ["R8", "R9", "R10"]},
 {"id": "AN2", "service": "linear", "locator": f"linear:project/{H['project']}", "prompt_reference": "the Payee history project", "requirement_ids": ["R9"]},
]
def frag(fid, service, container, kind, via, seeded, by, quote, reqs, names=None, base=None):
    return {"id": fid, "service": service, "container": container, "locator": container, "kind": kind, "incorporated_via": via, "seeded_ids": seeded,
            "base_pointers": base or [], "delegated_by_record": by, "delegation_quote": cur(quote), "requirement_ids": reqs, "names_authorities": [dict(n, quote=cur(n["quote"])) for n in (names or [])]}
fragments = [
 frag("K1", "slack", H["ask"], "delegation", ["AN1"], [H["ask"]], H["ask"], "can you own it", ["R8", "R10"], [{"id": "H1", "quote": "Angel note: how to count the money"}]),
 frag("K2", "gdocs", H["method"], "requirement", ["AN1", "K1"], [H["method"]], H["ask"], "how I want it counted is in the doc I just wrote", ["R1", "R2", "R3", "R4", "R5", "R6"],
      [{"id": "H2", "quote": "the warehouse's daily revenue table"}, {"id": "H3", "quote": "SVB's Payment Processed notices"}]),
 frag("K16", "slack", H["ask2"], "delegation", ["AN1", "K1"], [H["ask2"]], H["ask"], "more below", ["R8", "R9", "R10"]),
 frag("K3", "linear", f"linear:project/{H['project']}", "requirement", ["AN1", "K1", "K16"], [H["project"]], H["ask2"], "I put everyone on the SVB notices into the Payee history project in linear", ["R1", "R9"]),
 frag("K4", "gsheets", H["sheet"], "format", ["AN1", "K1", "K16"], [H["sheet"]], H["ask2"], "use the layout of my Angel note working sheet", ["R8"]),
 frag("K5", "gslides", H["deck"], "requirement", ["AN1", "K1", "K16"], [H["deck"]], H["ask2"], "my quick numbers are on that sheet and on the draft deck", ["R10"]),
 frag("K6", "gcal", H["hold_rob"], "destination", ["AN1", "K1"], [H["hold_rob"]], H["ask"], "before I start the angel calls on tuesday", ["R10"]),
 frag("K7", "trello", H["trello"], "amendment", ["AN1", "K1", "K2"], [H["trello"]], H["method"], "It replaces the quick plan I left on our board", ["R1"]),
 frag("K8", "gmail", B["n_ban_first"], "requirement", ["AN1", "K1", "K2"], [], H["method"], "SVB's Payment Processed notices are the one place I know with a line per payment", ["R1"], base=[B["n_ban_first"]]),
 frag("K9", "gmail", B["wu1"], "requirement", ["AN1", "K1", "K2"], [], H["method"], "it goes in only if a receipt for it reached your mail", ["R3"], base=[B["wu1"]]),
 frag("K10", "snowflake", B["revenue"], "requirement", ["AN1", "K1", "K2"], [], H["method"], "the warehouse's daily revenue table", ["R7"], base=[B["revenue"]]),
 frag("K11", "slack", H["statement"], "requirement", ["AN1", "K1", "K2"], [H["statement"]], H["method"], "A notice is where you start, not the last word", ["R1", "R2"]),
 frag("K12", "gmail", H["arthur_mail"], "requirement", ["AN1", "K1", "K2"], [H["arthur_mail"]], H["method"], "Money we moved between our own accounts isn't spending", ["R2"]),
 frag("K13", "slack", B["returned"], "requirement", ["AN1", "K1", "K2"], [], H["method"], "What counts is money that left the company and stayed out", ["R2"], base=[B["returned"]]),
 frag("K14", "contacts", H["c_brooks"], "requirement", ["AN1", "K1", "K2"], [H["c_brooks"]], H["method"], "Marketing is anything made or bought to get installs", ["R4"]),
 frag("K15", "gdocs", B["brooks_contract"], "requirement", ["AN1", "K1", "K2"], [], H["method"], "Marketing is anything made or bought to get installs", ["R4"], base=[B["brooks_contract"]]),
]
authorities = [
 {"id": "H1", "name": "the angel note method doc", "home_service": "gdocs", "decoy_service": "trello", "governs": ["R2", "R3", "R4", "R5", "R6"], "findable_query": "Angel note how to count",
  "seeded_ids": [H["method"]], "base_pointers": [], "decoy_seeded_ids": [H["trello"]], "decoy_base_pointers": []},
 {"id": "H2", "name": "the warehouse's daily revenue table", "home_service": "snowflake", "decoy_service": "snowflake", "governs": ["R7"], "findable_query": "REVENUE_DAILY", "seeded_ids": [], "base_pointers": [B["revenue"]],
  "decoy_seeded_ids": [], "decoy_base_pointers": [B["store_tx"]], "decoy_scope": {"dimension": "issuer", "decoy": "the stores' own transaction rows, gross of refunds, no ad revenue", "task": "each game's revenue as the company's daily table records it, ads included"}},
 {"id": "H3", "name": "SVB's Payment Processed notices", "home_service": "gmail", "decoy_service": "gsheets", "governs": ["R1"], "findable_query": "SVB Payment Notification Payment Processed", "seeded_ids": [], "base_pointers": [B["n_ban_first"]],
  "decoy_seeded_ids": [], "decoy_base_pointers": [B["pl_costs"]], "decoy_scope": {"dimension": "issuer", "decoy": "the company's own monthly P&L cost lines by category", "task": "the bank's own line per payment"}},
]
surfaces = [
 {"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1.0, "records": 22, "seeded": True, "seeded_ids": [ISS[k] for k in ("Deel", "MotMot", "JPMorgan", "Lucas", "Lauren Brooks")], "requirement": "R4", "decides": "bucket per payee",
  "why_no_bulk": "linear_list_issues returns descriptions and states but no comments; each payee's notes need its own linear_list_comments",
  "short_circuit": "the notes are the only place that says what a payee on the bank's spelling was for; no other record lists all 22, so skipping a read leaves that row's bucket unsourced"},
 {"service": "gmail", "tool": "gmail_get_messages_batch (format full, 10 ids a call)", "per_record_calls": 0.65, "records": 22, "requirement": "R1", "decides": "paid figure",
  "why_no_bulk": "gmail_search_messages returns ids only and the default snippet stops before payee and amount; format full is capped at 10 ids a call, so 132 notices need at least 14 reads",
  "short_circuit": "no sheet or table carries payee-level payments: the ledger has no vendor names and the P&L is monthly by category"},
 {"service": "slack", "tool": "slack_conversations_search_messages (per payee name)", "per_record_calls": 0.5, "records": 22, "requirement": "R5", "decides": "bet columns, build cost per bet",
  "why_no_bulk": "no channel holds every payee; the ties sit in several private channels and one search needs the payee's own name",
  "short_circuit": "a payee's return, re-send or game tie exists only in the channel where it was discussed"},
 {"service": "gmail", "tool": "gmail_search_messages (per payee name)", "per_record_calls": 0.5, "records": 22, "requirement": "R3", "decides": "paid figure",
  "why_no_bulk": "gmail_search returns ids only and the notices are one sender; receipts and vendor mail come back only by the payee's own name",
  "short_circuit": "payments the notices don't show exist only as a vendor or transfer mail"},
]
cohort = {"definition": "every payee the bank shows on the Payment Processed notices since Sep 2023, one issue each in the Payee history project (22 real payees, 24 spellings, 132 notices)",
          "definition_source": [H["ask"], H["project"], H["method"]], "key": "payee", "size": 22, "evidence_surfaces": surfaces}
chains = [
 {"id": "C1", "root_cause": "A24", "ends_in": "R2", "hops": [
  {"service": "gmail", "record": B["n_ban_first"], "finding": "Payment Processed, BANCO DE AMERICA ***8605, $4,032, Transaction Date Apr 2, 2024"},
  {"service": "slack", "record": B["wire_fail"], "finding": "Leonard Apr 5: this wire didn't go through"},
  {"service": "slack", "record": B["wrong_acct"], "finding": "Arthur Apr 5: I messed up the bank account number, fixed up and resubmitted"},
  {"service": "gmail", "record": B["n_ban_mod"], "finding": "Recipient Modified to ***3341, then Processed again (Apr 5)"},
  {"service": "slack", "record": B["returned"], "finding": "Leonard Apr 12: money returned to us, the bank returned our money"},
  {"service": "slack", "record": H["return_note"], "finding": "Leonard Feb 13: the Apr 2024 wire to the account ending 8605 came back; re-sent to 3341"}]},
 {"id": "C2", "root_cause": "A17", "ends_in": "R3", "hops": [
  {"service": "linear", "record": ISS["Lucas"], "finding": "Leonard's note: that's Lucas, mini games dev"},
  {"service": "slack", "record": B["lucas_card"], "finding": "Robert Jun 2024: sending Lucas's pay via company card"},
  {"service": "gmail", "record": B["wu1"], "finding": "five Western Union receipts, $7,525 received, Jun 3 to Aug 23, 2024"}]},
 {"id": "C3", "root_cause": "A13", "ends_in": "R1", "hops": [
  {"service": "gmail", "record": B["lb_await"], "finding": "Payment Awaiting Approval, Leapblock $33,290, Sep 13, 2023; no Processed notice in any mailbox"},
  {"service": "slack", "record": B["lb_done"], "finding": "Arthur Sep 13, 2023 on Leonard's approval request: Done!"},
  {"service": "slack", "record": H["statement"], "finding": "Leapblock's closing statement: 30 wires, 407,944, first one 33,290 on 13 Sep 2023"}]},
 {"id": "C4", "root_cause": "A11", "ends_in": "R2", "hops": [
  {"service": "gmail", "record": B["jpm_notice"], "finding": "Payment Processed, JPMorgan ***3203, $4,000, Aug 19, 2024"},
  {"service": "linear", "record": ISS["JPMorgan"], "finding": "Leonard's note: approved it, thinks it was a contractor advance, cannot place which"},
  {"service": "gmail", "record": H["arthur_mail"], "finding": "Arthur Feb 13: that was our own Chase account, money put back after Carta's renewal; it never left the company"}]},
 {"id": "C5", "root_cause": "A7", "ends_in": "R4", "hops": [
  {"service": "linear", "record": ISS["Node Media"], "finding": "the bank shows an LLC; Leonard's note: one payment when we closed the account"},
  {"service": "slack", "record": B["node_close"], "finding": "Leonard Jan 2, 2025: closing our account with Node Media LLC"},
  {"service": "gmail", "record": B["node_mail"], "finding": "the agency's invoice note: Sept $1,428.57, Oct $5,000, Nov $5,000 behind the $16,428.57; UA agency, so Marketing"}]},
 {"id": "C6", "root_cause": "A15", "ends_in": "R4", "hops": [
  {"service": "linear", "record": ISS["Lauren Brooks"], "finding": "Leonard's note: the contract sent out in Oct, $500 a month"},
  {"service": "contacts", "record": H["c_brooks"], "finding": "the contact row spells the name the notices token out"},
  {"service": "gdocs", "record": B["brooks_contract"], "finding": "her contract's Exhibit A: run and optimize paid UA on Telegram, so Marketing under the method's bucket sentence"}]},
]
def trap(tid, family, svcs, seeded, base, req, wrong, resolver, order=None, versions=None, dtype=None):
    t = {"id": tid, "family": family, "services": svcs, "seeded_ids": seeded, "base_pointers": base, "requirement": req, "expected_wrong_reading": wrong, "resolver": resolver}
    if dtype: t["distractor_type"] = dtype
    if order: t["discovery_order"] = order
    if versions: t["version_records"] = sorted(versions, key=lambda r: r["at"])
    return t
def v(service, rid, seeded, at, container=None):
    r = {"service": service, ("id" if seeded else "base_pointer"): rid, "seeded": seeded, "at": at}
    if container: r["container"] = container
    return r
def vs(ptr):
    return v("slack", ptr, False, s_at(ptr), f"slack:{ptr}")
def vg(ptr, f):
    return v("gmail", ptr, False, sent(f), f"gmail:{ptr.split('/')[1]}")
JPM_F = next(n["thread"] for n in NOT if "JPMorgan" in n["to"])
BAN1_F, BAN2_F = "threads/00004088.json", "threads/00004124.json"
traps = [
 trap("T1", "done_gap", ["gmail", "slack"], [H["return_note"]], [B["n_ban_first"], B["wire_fail"], B["wrong_acct"], B["returned"]], "R2",
      "the Processed notice means $4,032 went to MotMot on the wrong account, so the payee's total is $41,088", "the wire went to a bad account number and the bank returned it (#admin_foundersonly Apr 5 and Apr 12, 2024), so MotMot's net is $37,056",
      order="the Processed notice is read first in every run; the return is in a founders' channel, two years back and in a Feb 13 note that names the account endings, neither on the doc or issue path",
      versions=[vg(B["n_ban_first"], BAN1_F), vs(B["wire_fail"]), vs(B["wrong_acct"]), vs(B["returned"]), v("slack", H["return_note"], True, "2026-02-13T01:52:13Z", f"slack:{H['return_note']}")]),
 trap("T2", "exact_predicate", ["gmail", "slack", "linear"], [ISS["Lucas"]], [B["lucas_card"], B["wu1"], B["wu2"], B["wu3"], B["wu4"], B["wu5"]], "R3",
      "the notices hold every payment to Lucas, so he cost $6,450", "five Western Union receipts in the founders' mail add $7,525; the method brings a receipted contractor in, so he cost $13,975",
      order="the notices and Leonard's note come first; the receipts share no sender or subject with the notices"),
 trap("T3", "superseding", ["gmail", "slack"], [H["statement"]], [B["lb_await"], B["lb_done"]], "R1",
      "no Processed notice means the $33,290 never left, so Leapblock's total is $374,654", "Leapblock's own closing statement counts it among 30 wires, $407,944, and Arthur's Sep 2023 Done agrees",
      order="a Processed-only read never sees the Awaiting notice; the statement is a Feb 13 post in a channel runs read only by name",
      versions=[vg(B["lb_await"], "threads/00001577.json") if False else v("gmail", B["lb_await"], False, "2023-09-13T14:50:58Z", f"gmail:{B['lb_await'].split('/')[1]}"), vs(B["lb_done"]),
                v("slack", H["statement"], True, T["statement"], f"slack:{H['statement']}")]),
 trap("T4", "superseding", ["gmail", "linear"], [ISS["JPMorgan"], H["arthur_mail"]], [], "R2",
      "the $4,000 to JPMorgan in Aug 2024 is a cost of the bet running that month", "Arthur's Feb 13 mail: that account is the company's own Chase, so the money never left and is left out",
      order="the notice and Leonard's hedged note that it was a contractor advance come first; Arthur's later mail is about Chase records, not the project",
      versions=[v("gmail", B["jpm_notice"], False, sent(JPM_F), "gmail:1807851044809802572"), v("linear", ISS["JPMorgan"], True, T["issue0"], f"linear:{ISS['JPMorgan']}"),
                v("gmail", H["arthur_mail"], True, T["arthur"], f"gmail:{H['arthur_mail'].split('/')[1]}")]),
 trap("T5", "scope_alias", ["gmail", "slack", "linear"], [ISS["Node Media"]], [B["node_close"], B["node_mail"]], "R4",
      "the $16,428.57 LLC is a build vendor of the bet running that day", "the LLC is Node Media, a UA agency (its own invoice note gives the exact amounts), so it is Marketing and outside build cost",
      order="the bank shows only a token LLC; the name appears in a founders' channel and the agency's mail"),
 trap("T6", "authority", ["gdocs", "contacts", "linear"], [H["method"], H["c_brooks"], ISS["Lauren Brooks"]], [B["brooks_contract"]], "R4",
      "a monthly contractor on a contract is build cost, so her $1,500 falls in ZM and Combo Fighter by date", "her contract's Exhibit A is paid UA work on Telegram, so the method's bucket sentence makes it Marketing, outside build cost",
      order="the note and the contact read as a contractor; only the contract says what the work was"),
 trap("T7", "unit_or_timezone", ["gmail", "slack"], [ISS["Martin Walsh"]], [B["bgn_notice"], B["laptop"]], "R6",
      "Martin's Oct 30, 2025 payment is $1,999 of build cost", "the notice is in BGN and #admin_foundersonly says it was his laptop: a Company line kept in its own currency, out of dollar totals",
      order="a parser built for USD drops or mis-adds it"),
 trap("T8", "stale_summary", ["gsheets", "gslides"], [H["sheet"], H["deck"]], [], "R5",
      "Leonard's quick numbers ($985K, $609K, $74K) are the bets' build cost", "they are every notice added up by date; the method's buckets, exception and adjustments change all three",
      dtype="stale_summary", order="both records are named in the ask and read before the notices"),
 trap("T9", "superseding", ["trello", "gdocs"], [H["trello"], H["method"]], [], "R1",
      "the quick plan on the board (add up the notices by date and round) is the whole method", "the method says it replaces the plan: buckets, adjustments and the bet calendar apply",
      versions=[v("trello", H["trello"], True, T["trello"], f"trello:{H['trello']}"), v("gdocs", H["method"], True, T["method"], f"file:{H['method']}")]),
 trap("T10", "superseding", ["gmail", "slack"], [], [B["n_ban_mod"], B["n_ban_resend"], B["motmot_one"]], "R1",
      "the Apr 5 $4,032 is a duplicate of the Apr 3 wire, so one of them should be dropped as a mistake and the account stays as it was", "the Apr 5 wire to the corrected account is the real payment; it stands",
      versions=[vs(B["motmot_one"]), vg(B["n_ban_resend"], BAN2_F)]),
 trap("T11", "distractor", ["gmail"], [], [B["n_ban_first"]], "R1", "two same-amount Leapblock wires in Aug 2025 are a duplicate", "they pay separate months; both stand", dtype="near_duplicate_record"),
 trap("T12", "distractor", ["gmail"], [], [B["lb_await"]], "R1", "Awaiting Approval and Scheduled notices are payments too", "only processed payments count; 130 Awaiting and 40 Scheduled notices repeat them", dtype="keyword_collision"),
 trap("T13", "distractor", ["slack"], [], [B["lucas_send"]], "R3", "the ZM animator paid on a card ($5,400 agreed) goes in like Lucas", "no receipt reached the mail, so the method leaves it out", dtype="scope_adjacent"),
 trap("T14", "distractor", ["linear"], [ISS["4X helper"]], [], "R4", "the $500 proposal helper is a Domino Delights or ZM cost", "the 4X proposal is not one of the three games; a Company line", dtype="other_title"),
 trap("T15", "distractor", ["slack"], [], [B["pl_accurate"]], "R1", "Leonard's Aug 2025 note that the P&L is accurate makes the P&L the record to use", "that note is about balances; the method goes by the bank's line-per-payment notices", dtype="non_authoritative_instruction"),
 trap("T16", "distractor", ["gmail"], [], [B["deel_recipient"]], "R1", "the second spelling on ***8380 is another payee", "same account as Deel, one payee", dtype="lookalike_entity"),
 trap("T17", "distractor", ["snowflake", "gdocs"], [H["method"]], [B["store_tx"]], "R7", "store transactions are each game's revenue", "the method names the daily revenue table, ads included", dtype="partial_listing"),
]
PRI = json.load(open(os.path.join(HERE, "priors.json")))
def prior(f):
    e = PRI.get(f)
    return {"alpha": e["alpha"], "beta": e["beta"], "record_ids": e["record_ids"]} if e else {"alpha": 1.0, "beta": 1.0, "record_ids": []}
portfolio = [
 {"id": "RET", "mechanism": "A24", "prior_family": "A24", "prior_family_reason": "same mechanism: a done source and the missing piece in another service", "nodes": ["T1", "C1", "T10"], "requirement": "R2", "natural_reading": "every Processed notice is money that stayed out",
  "controls": ["Leapblock"], "over_application": "ret_over: treats the two Leapblock $3,700 wires of Aug 2025 as one returned and one re-sent", "source": "founders-channel-by-name", "signature": "thats the motmot one"},
 {"id": "OFF", "mechanism": "A17", "prior_family": "A17", "prior_family_reason": "same mechanism: in-scope payments outside the obvious search", "nodes": ["T2", "C2", "T13"], "requirement": "R3", "natural_reading": "the notices are the whole population",
  "controls": ["Graham Porter"], "over_application": "off_over: adds the card-paid ZM animator with no receipt", "source": "mail-by-name", "signature": "Western Union Lucas"},
 {"id": "ORPH", "mechanism": "A13", "prior_family": "A11", "prior_family_reason": "closest measured family: a later record elsewhere changes a figure", "nodes": ["T3", "C3", "T12"], "requirement": "R1", "natural_reading": "no Processed notice means no payment",
  "controls": ["Eveline Art"], "over_application": "orph_over: counts Awaiting and Scheduled notices as payments for other payees", "source": "channel-by-name", "signature": "407,944 over 30 wires"},
 {"id": "CORR", "mechanism": "A11", "prior_family": "A11", "prior_family_reason": "same mechanism: a dated correction in another service", "nodes": ["T4", "C4"], "requirement": "R2", "natural_reading": "every wire is a cost",
  "controls": ["Singular"], "over_application": "corr_over: drops another one-off wire as an internal transfer", "source": "recent-mail", "signature": "our own Chase account"},
 {"id": "ALIAS", "mechanism": "A7", "prior_family": "A17", "prior_family_reason": "closest measured family: the item hides from the obvious name", "nodes": ["T5", "C5"], "requirement": "R4", "natural_reading": "the bank's payee name tells you what the payee is",
  "controls": ["Adjoe"], "over_application": "alias_over: moves a studio such as Leapblock into Marketing", "source": "mail-by-token", "signature": "Sept $1,428.57"},
 {"id": "CLASS", "mechanism": "A15", "prior_family": "A15", "prior_family_reason": "same mechanism: a house definition overrides the natural reading of a contractor", "nodes": ["T6", "C6"], "requirement": "R4", "natural_reading": "a monthly contractor is build cost",
  "controls": ["Graham Porter"], "over_application": "class_over: moves a build contractor such as Graham Porter into Marketing", "source": "contract-doc", "signature": "run and optimize paid UA"},
 {"id": "CURR", "mechanism": "A10", "prior_family": "A15", "prior_family_reason": "closest measured family: one rule on one line, no Opus 5.5 prior for A10", "nodes": ["T7"], "requirement": "R6", "natural_reading": "every notice is USD and every person paid is build cost",
  "controls": ["Lauren Brooks"], "over_application": "curr_over: treats a dollar wire as foreign", "source": "notice-field", "signature": "1,999.00 BGN"},
]
for p in portfolio:
    p["prior"] = prior(p["prior_family"])
channels = [
 {"id": "CH-RET", "kind": "scale", "rule": "RET", "degrade": "ch_miss", "latent": "member", "family": "A24", "source": "founders-channel-by-name", "members": ["MotMot"], "description": "the Apr 2024 wire notes are not found: MotMot stays at $41,088"},
 {"id": "CH-OFF", "kind": "scale", "rule": "OFF", "degrade": "ch_miss", "latent": "member", "family": "A17", "source": "mail-by-name", "members": ["Lucas"], "description": "the Western Union receipts are not found: Lucas stays at $6,450"},
 {"id": "CH-ORPH", "kind": "scale", "rule": "ORPH", "degrade": "ch_miss", "latent": "member", "family": "A11", "source": "channel-by-name", "members": ["Leapblock"], "description": "the statement is not read: Leapblock stays at $374,654"},
 {"id": "CH-CORR", "kind": "scale", "rule": "CORR", "degrade": "ch_miss", "latent": "member", "family": "A11", "source": "recent-mail", "members": ["JPMorgan"], "description": "Arthur's mail is not found: $4,000 stays a cost"},
 {"id": "CH-ALIAS", "kind": "scale", "rule": "ALIAS", "degrade": "ch_miss", "latent": "member", "family": "A17", "source": "mail-by-token", "members": ["Node Media"], "description": "the LLC is not identified: $16,428.57 stays in Domino Delights build cost"},
 {"id": "CH-CLASS", "kind": "scale", "rule": "CLASS", "degrade": "ch_miss", "latent": "member", "family": "A15", "source": "contract-doc", "members": ["Lauren Brooks"], "description": "the contract is not read: her $1,500 stays in build cost by date"},
 {"id": "CH-CURR", "kind": "scale", "rule": "CURR", "degrade": "ch_miss", "latent": "member", "family": "A15", "source": "notice-field", "members": ["Martin Walsh"], "description": "the BGN payment is added as dollars or as build cost"},
]
budget = [
 ("discovery", "slack", 10, "the ask, #winddown pages, Feb #executives, the channels a payee's note points at"),
 ("rules", "gdocs", 2, "the method doc and the Leapblock MSA"), ("rules", "gsheets", 2, "the working sheet's layout and quick figures"), ("rules", "gslides", 1, "the draft deck whose figures the reply compares"),
 ("rules", "trello", 2, "the board card the method replaces"), ("rules", "gcal", 1, "when the angel calls start"), ("rules", "linear", 3, "the project and its 22 issues"), ("rules", "snowflake", 4, "list, describe and the lifetime revenue query"),
 ("per-record", "gmail", 16, "search pages and 14+ full-format reads over the 132 notices (10 ids a call)"), ("per-record", "linear", 22, "each payee's notes (no bulk comment read)"),
 ("per-record", "slack", 11, "a name search per payee with an open question: returns, re-sends, game ties"), ("per-record", "gmail", 11, "a name search per payee for receipts and vendor mail"),
 ("reconciliation", "gdrive", 3, "Robert's root, the working sheet and the deck by title"), ("reconciliation", "contacts", 2, "the names the notices token out"), ("reconciliation", "gsheets", 2, "the P&L costs tab for lines the notices don't name"),
 ("per-record", "linear", 22, "closing each payee's issue, as the method asks (no batch write)"), ("writes", "linear", 4, "a reason comment on each payee whose figure differs from the notices"),
 ("writes", "gsheets", 4, "create the sheet and write its rows"), ("writes", "gdrive", 3, "move it to Robert's root and share it with Leonard and Arthur"), ("writes", "slack", 1, "the reply to Leonard"), ("read-back", "gsheets", 1, "read the sheet back before replying"),
]
call_budget = [{"phase": a, "service": b, "calls": c, "reason": d} for a, b, c, d in budget]
TOTAL_BUDGET = sum(c for _, _, c, _ in budget)
writes = [
 {"service": "gsheets", "tool": "gsheets_create_spreadsheet+gsheets_values_update", "count": 4, "depends_on": ["C1", "C2", "C3", "C4", "C5", "C6", "T3"], "requirements": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]},
 {"service": "gdrive", "tool": "gdrive_move_file+gdrive_share_file", "count": 3, "depends_on": ["K4"], "requirements": ["R8"]},
 {"service": "linear", "tool": "linear_update_issue", "count": 22, "depends_on": ["C1", "C2", "C3", "C4", "C5", "C6"], "requirements": ["R9"]},
 {"service": "linear", "tool": "linear_create_comment", "count": 4, "depends_on": ["C1", "C2", "C3", "C4"], "requirements": ["R9"]},
 {"service": "slack", "tool": "slack_send_message", "count": 1, "depends_on": ["C1", "C2", "C3", "C4", "C5", "C6", "T8"], "requirements": ["R10"]},
]
hazards = [
 {"hazard_id": "R04", "resolution": "excluded", "why_safe": "no Slack Drive link is cited; files are named by title"},
 {"hazard_id": "R08", "resolution": "excluded", "why_safe": "no invitation mail is relied on; the hold's invite is context only"},
 {"hazard_id": "L08", "resolution": "excluded", "why_safe": "no base open issue is modified or cited; seeded payee issues go to active people only"},
 {"hazard_id": "L13", "resolution": "excluded", "why_safe": "the design never asserts that work stopped at the shutdown"},
]
EXC_WHO = "requester, Claude Code chat 2026-11-07: 'go with the best one that aligns with task requirement and the goal' on the §10 proposals of 00_Pre_Scenario_Analysis.md"
manifest = {
 "_note": "DRAFT manifest (scenario stage). Seeded ids are planned (minted in research/minted_ids.json, collision-checked across the base); /create-injection writes the final manifest.",
 "persona": "robert", "assignment_context": ctx, "horizon": "Long Horizon", "effective_profile": "extreme",
 "volume_exception": {"reason": "22 real payees; the 132 notices collapse to about 16 reads because a full read takes 10 ids; the per-payee notes, lookups and closes give about 130 honest calls per run; reaching 500 would need padding, which fails on its own",
                      "requester_confirmation": EXC_WHO, "call_budget_floor": 120, "per_record_floor": 40},
 "cohort_exception": {"reason": "no natural cohort of 40 or more records has three no-bulk surfaces here: the 132 notices share one sender and are read in batches, so the honest unit is the 22 payees", "requester_confirmation": EXC_WHO, "cohort_floor": 22},
 "requirements": REQ, "services": services, "anchors": anchors, "ask_fragments": fragments, "authorities": authorities, "cohort": cohort, "chains": chains, "traps": traps,
 "mechanism_portfolio": portfolio, "channels": channels, "call_budget": call_budget, "writes": writes, "hazard_acknowledgements": hazards, "denied_probes": [], "gradable_surface": "01_Gradable_Surface.json",
}
# ---------------------------------------------------------------- gradable surface
MS, CA, IN, LK, CO = "multi_source_reconciliation", "calculation", "interpretation", "lookup", "comparison"
def slot(sid, title, weight, kind, reason, cls, selector, role="core", group=None, mechs=(), fact=None, **kw):
    s = {"id": sid, "title": title, "weight": weight, "work_kind": kind, "work_reason": reason, "class": cls, "selector": selector, "role": role, "mechanisms": list(mechs)}
    if group: s["group"] = group
    if fact: s["fact_id"] = fact
    s.update(kw); return s
ROW = r"[ -~ -￿]"
def row(name, pat, n=220):
    return ["text", "ledger", f"{name}{ROW}{{0,{n}}}{pat}"]
ask_ts = H["ask"].split("/")[1]
def _money(v):
    whole = f"{v:,.2f}"
    return [whole, whole.removesuffix(".00"), "$" + whole, "$" + whole.removesuffix(".00"), str(v)]
MONEY_ALIASES = {str(float(v)): _money(float(v)) for v in (28128, 13975, 337594, 530736.14, 45941.5, 5000, 7175)}
slots = [
 slot("X1", "MotMot net of the returned wire", 5, MS, "the bank's Processed notice against the founders' Apr 2024 notes and the re-sent wire", "direct", ["field", "MotMot", "Domino Delights"], "exception", None, ["RET"], "motmot_net", singled_out_by="H1"),
 slot("X3", "Lucas with the card-paid transfers", 5, MS, "three notices joined to five Western Union receipts under the method's receipt sentence", "direct", ["field", "Lucas", "Domino Delights"], "exception", None, ["OFF"], "lucas_total", singled_out_by="H1"),
 slot("X4", "Leapblock including the Sep 2023 wire", 5, MS, "29 notices against the orphan Awaiting notice, Arthur's Done and Leapblock's statement", "direct", ["field", "Leapblock", "Domino Delights"], "exception", None, ["ORPH"], "leapblock_total", singled_out_by="H1"),
 slot("X5", "the Aug 2024 $4,000 kept out of cost", 5, MS, "the notice and Leonard's note against Arthur's Chase mail", "direct", ["field", "JPMorgan", "Bucket"], "exception", None, ["CORR"], "jpm_out", singled_out_by="H1"),
 slot("X6", "Node Media identified and kept out of build cost", 5, MS, "a token LLC on the bank joined to the founders' note and the agency's invoice mail, then the bucket sentence", "direct", ["field", "Node Media", "Bucket"], "exception", None, ["ALIAS"], "node_marketing", singled_out_by="H1"),
 slot("X8", "Telegram contractor kept out of build cost", 5, MS, "the notices and Leonard's note joined through the contact row to her contract's scope, under the bucket sentence", "direct", ["field", "Lauren Brooks", "Bucket"], "exception", None, ["CLASS"], "brooks_marketing", singled_out_by="H1"),
 slot("X9", "Martin's payment kept in BGN on the company line", 3, IN, "the notice's currency read with the laptop note under the method's currency sentence", "direct", ["field", "Martin Walsh", "Company"], "exception", None, ["CURR"], "martin_bgn", singled_out_by="H1"),
 slot("B1", "Domino Delights build cost", 5, MS, "notices by date with the return, the receipts, the statement and the bucket calls", "write_content", ["text", "ledger", r"959,?342(\.64)?"], "core", None, ["RET", "OFF", "ORPH", "CORR", "ALIAS"], "dd_build"),
 slot("B2", "ZM build cost", 5, MS, "notices by date with the bucket calls", "write_content", ["text", "ledger", r"544,?433(\.44)?"], "core", None, ["CLASS", "CURR"], "zm_build"),
 slot("B3", "Combo Fighter build cost", 5, MS, "notices by date with the bucket call on the contractor", "write_content", ["text", "ledger", r"72,?685(\.61)?"], "core", None, ["CLASS"], "cf_build"),
 slot("B4", "Company line", 3, CA, "legal, tools, website and the proposal helper in dollars, with the laptop in its own currency", "write_content", ["text", "ledger", r"49,?625\b"], "core", None, [], "company_line"),
 slot("V1", "Domino Delights lifetime revenue", 3, CA, "a sum over the warehouse's daily revenue table", "write_content", ["text", "ledger", r"12,?331(\.25)?"], "core", None, [], "dd_rev"),
 slot("V2", "ZM lifetime revenue", 3, CA, "a sum over the warehouse's daily revenue table", "write_content", ["text", "ledger", r"\b11\.99\b"], "core", None, [], "zm_rev"),
 slot("S1", "Deel across both spellings", 3, CA, "35 notices summed over two spellings of one account", "direct", ["field", "Deel", "Domino Delights"], "sample", "payees"),
 slot("S2", "Eveline Art", 3, CA, "28 notices summed", "direct", ["field", "Eveline Art", "Domino Delights"], "sample", "payees"),
 slot("S3", "Graham Porter", 1, LK, "one notice", "direct", ["field", "Graham Porter", "ZM"], "sample", "payees"),
 slot("S4", "Adjoe kept out of build cost", 1, LK, "a UA network under the bucket sentence", "direct", ["field", "Adjoe", "Bucket"], "sample", "payees"),
 slot("S5", "Trademark lawyer on the company line", 3, CA, "four notices summed", "direct", ["field", "Trademark lawyer", "Company"], "sample", "payees"),
 slot("S6", "number of Build rows", 1, LK, "the output-volume row for the payee rows: 9 payees in Build", "aggregate", ["total", "Build"], "volume", None, ["CLASS"], volume_for=["payees"]),
 slot("C1", "reason on the MotMot issue", 3, IN, "the method's follow-through on a figure that differs from the notices", "write_content", ["text", "comments", r"([Rr]eturn|wrong account|bounced|came back|didn.t go through)"], "core", None, ["RET"], "c_motmot"),
 slot("C2", "reason on the Lucas issue", 3, IN, "the method's follow-through", "write_content", ["text", "comments", r"(Western Union|money transfer|company card)"], "core", None, ["OFF"], "c_lucas"),
 slot("C3", "reason on the Leapblock issue", 3, IN, "the method's follow-through", "write_content", ["text", "comments", r"(33,?290|[Ss]tatement)"], "core", None, ["ORPH"], "c_leapblock"),
 slot("C4", "reason on the JPMorgan issue", 3, IN, "the method's follow-through", "write_content", ["text", "comments", r"(Chase|own account|[Tt]ransfer)"], "core", None, ["CORR"], "c_jpm"),
 slot("R1", "reply gives Domino Delights build cost", 3, IN, "the headline the ask wants", "write_content", ["text", "reply", r"959,?342|\$?959K|\$?0?\.96 ?M"], "core", None, ["RET", "OFF", "ORPH", "CORR", "ALIAS"], "dd_build"),
 slot("R2", "reply says the deck's figures change", 3, IN, "the ask: what changes on the deck", "write_content", ["text", "reply", r"[Dd]eck"], "core", None, [], "deck_change"),
 slot("D1", "sheet in Robert's Drive", 1, LK, "the ask: keep yours in your drive", "delivery", ["delivery", "register_parent", B["robert_root"]]),
 slot("D2", "shared with Leonard", 1, LK, "the ask", "delivery", ["delivery", "share_reader"]),
 slot("D3", "reply links the sheet", 1, LK, "the ask", "delivery", ["link", "reply"]),
 slot("D4", "reply in #winddown on Leonard's ask", 1, LK, "the ask: tell me here", "delivery", ["delivery", "slack_thread", ask_ts]),
]
surface = {
 "kind": "GRADABLE_SURFACE", "version": 1, "task": "robert_seed_bets", "revision": "design-1", "truth_keys": [p[0] for p in PAYEES], "classes": ["Build", "Marketing", "Company", "Not a cost"],
 "truth_fields": {"class": "Bucket", "groups": "groups"},
 "known_gaps": ["Issue closes are template-identical writes on 22 issues: the rubric covers them, and the surface grades no close, because a tracker_state slot binds one issue. /create-rubric-writing plans rows per the platform's one-row-per-write reading.", "Combo Fighter revenue is not graded: the method leaves it off for now, and the warehouse figure conflicts with base chat (NB-26). B1-B4, V1-V2, C1-C4 and R1-R2 are text slots: the solver forecast cannot see them, so it reports loss only on the field slots and overstates E[avg]. The --design forecast, which reads declared mechanisms, is the wider view."],
 "deliverables": {
  "ledger": {"kind": "table", "name_regex": r"(?i).*(angel|seed|bet|money|payee).*", "key_column": "Payee", "key_regex": r"(?:Payee 1|[A-Za-z0-9][A-Za-z0-9 .()&/-]*)", "columns": Q["sheet_header"], "class_column": "Bucket", "reason_column": "Note",
             "comparators": {"Bucket": "yes_no", "Domino Delights": "yes_no", "ZM": "yes_no", "Company": "yes_no"}, "yes_no": {"Build": ["Build", "Build cost"], "Marketing": ["Marketing", "UA", "Marketing / UA"], "Company": ["Company", "Company costs"], "Not a cost": ["Not a cost", "Left out", "Transfer", "Internal transfer", "Own account", "Own transfer", "Excluded", "None", "n/a", "No bucket", "", "-"],
              **MONEY_ALIASES, "1,999.00 BGN": ["1,999.00 BGN", "1,999 BGN", "BGN 1,999", "BGN 1,999.00", "1999 BGN"]}},
  "reply": {"kind": "json_text", "tool": "slack_send_message"},
  "comments": {"kind": "json_text", "tool": "linear_create_comment"},
 },
 "slots": slots,
}
_by = {}
for s_ in slots:
    for m_ in s_["mechanisms"]:
        _by.setdefault(m_, []).append(s_["id"])
for e_ in portfolio:
    e_["decides"] = _by.get(e_["id"], [])
write(os.path.join(WF, "01_Gradable_Surface.json"), surface)
write(os.path.join(WF, "01_Hardness_Manifest.draft.json"), manifest)
write(os.path.join(HERE, "ids.json"), {"IDS": IDS, "BASE": BASE, "T": T, "issues": ISS, "gmail_threads": {"arthur": MINT["gmail"]["arthur_chase"]["threads"], "invite": MINT["gmail"]["hold_invite"]["threads"]}})
write(os.path.join(HERE, "wording.json"), Q)
write(os.path.join(HERE, "cohort.json"), PAYEES)
print(json.dumps({"payees": len(PAYEES), "budget": TOTAL_BUDGET, "slots": len(slots), "weight": sum(s["weight"] for s in slots), "traps": len(traps)}))
