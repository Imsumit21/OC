# Narrative half of the dossier, exec'd by assemble_dossier.py (shares its names).
A("## Findability and discovery-order proofs")
A("")
A(f"- Hub (A1) {MSG['hub']} in {I['hub_thread']}: Leonard → Frederick, Sep 30 23:10Z; a gmail search for 'DD publishing' or 'Monday' returns it first (newest). First link.")
A(f"- Ground rules H1 {I['rule_doc']}: the hub names 'the ground rules doc'; a Drive or Docs search for 'ground rules' returns it; the competing hit is Frederick's co-dev doc {I['codev_doc']} (decoy, co-dev only, not DD). Shared with Frederick directly; Leonard's parent folder isn't needed.")
A(f"- Rights H2: the rule doc names 'the position from the August sync'; a search for 'non-mobile' or 'rights' returns the sync doc {BASE['sync_doc']} and Leonard's post {BASE['rights_post']}.")
A(f"- Card H3 {I['dd_card']}: the hub names 'the DD publishing card on the UA/BD board'; a board read lists it on BD Follow Up.")
A(f"- T1 DONE: claim met first — Marek's mail {MSG['Oakline Games:2']} (wire sent Sep 29) and Frederick's card comment {I['oakline_card_comment']}; overturned by Arthur's reply {SL['arthur_cash']} (Sep 30) under the Sep 8 banker root, found by a Slack search on 'SVB', 'first-look' or a read of the #executives thread.")
A(f"- T2 CORR: claim met first — Tallwater's term sheet {term('Tallwater Games')} ($60,000); overturned by the note past the agenda on {I['pb_event']}, read with the event's full description.")
A(f"- T3 ALIAS: claim met first — Moonrail's term sheet {term('Moonrail Studios')}; overturned by Robert's post {SL['kestrel_post']} ('Kestrel' only), joined through Anika's signature in {IDS['threads']['Moonrail Studios']} and contact {I['anika_contact']}.")
A(f"- T4 FILT: Copperleaf's offer sits in Robert's reply {SL['copperleaf_relay']} under the Sep 24 70 % D1 root; it isn't on the sheet or in Frederick's inbox; a Slack search for 'publisher', 'advance' or 'installs' or a read of that thread finds it.")
A(f"- T5 FILT: Redwood's offer sits in the comment {I['eng2362_comment']} on ENG-2362, behind Arthur's #analytics pointer {SL['arthur_analytics']}, which says 'a publisher' and names the ticket.")
A(f"- T6, T14 EXC: Northglow's and Pinegrove's term sheets {term('Northglow Publishing')}, {term('Pinegrove Games')} take non-mobile rights or the code; the rule doc's 'Out on rights' line points at the August position.")
A(f"- T7 INPUT: claim met first — Sunfold's term sheet {term('Sunfold Mobile')} (50,000); overturned by Frederick's comment {I['sunfold_comment']} on the card 'F/up with Lena' {I['sunfold_card']}, reached by reading the list and joining Lena to Sunfold through the sheet.")
A(f"- T8 FOLLOW: Leonard's reply {SL['standing_line']} under the Sep 17 Matthew root in #bridge-pitch; the rule doc's last line carries it; the outreach sheet's 'What we sent' column picks the recipients.")
A(f"- T9 DATE: the rule doc says Oct 31 unless the lawyers give a later date; ESG's mail {MSG['esg_note']} and Leonard's reply {MSG['esg_leo']} ('License paper timing') set Nov 14.")
A(f"- T10: the two existing cards {I['oakline_card']}, {I['sunfold_card']} are named for people. T11: Summit's auto-ack sits in {IDS['threads']['Summit Mobile']}. T12: Frederick's Sep 4 Rayking message in {BASE['rayking_thread']} is an unsent draft; his seeded DM {SL['rayking_dm']} says they still owe an answer.")
A("")
A("## Self-validation")
A("")
A("| QC category | Tool-enforced (result) | Manual (evidence) |")
A("|---|---|---|")
A(f"| Missing Universe Data | check-sql PASS (1.E) | every deciding fact is persona-readable: {SL['arthur_cash']}, {I['pb_event']}, {SL['kestrel_post']}, {SL['copperleaf_relay']}, {I['eng2362_comment']}, {I['sunfold_comment']}, {MSG['esg_note']}, {SL['standing_line']} |")
A(f"| Temporal Field | sql_lint 0 errors; base_check Check C PASS | text dates agree: the rule doc (Mon Sep 29) says Monday's talk = Oct 6, the event {I['monday_event']}; Arthur's Sep 30 'next week' is Oct 6–10; ESG's Nov 14 follows its Nov 7 arbitration |")
A(f"| Cross-service Referential | base_check Check A PASS | one name and amount per publisher across thread, term sheet and sheet; Lena Fischer and Anika Rao match their Contacts rows |")
A("| Quantitative | reply counters updated on the three base roots; Trello badges match comments | every value comes from solver/truth.json; keep value re-read from the warehouse by the blind reviewer |")
A(f"| State / Lifecycle | ENG-2362 stays Todo with Arthur | the comment is a note on his own open ticket; {I['dd_card']} is an open card |")
A("| Identifier / Format | eval lint FAIL 0 CHECK 0 | ids follow base schemes (1.A); roster addresses in every seeded row (I03) |")
A(f"| Semantic / Category | — | titles match content ({I['rule_doc']}, {I['dd_card']}, {I['codev_doc']}) |")
A("| Other | — | voice per 1.C; no record states a decision, a total or the model |")
A("")
A("## Integrations and companions")
A("")
A("| Service | INT id | Companion | Decision |")
A("|---|---|---|---|")
A(f"| gcal | INT-11 | invitation mails | seeded: the Monday execs event (Frederick, Robert, Arthur; Leonard organizes) and the Tallwater call (Frederick). Frederick organized the Harbor Lane and Wavecrest calls himself with one outside guest, so no invitation lands in a HarmonyGames mailbox: declared in integration_exceptions (no_notify), the same shape the base shows |")
A("| linear | INT-03, INT-04, INT-05 | linear[bot] PR comment / Slack DM / mail digest | none: ENG-2362 has no PR; Arthur comments on his own issue (no notification to Frederick) |")
A(f"| gdrive | INT-13 | Drive Slack app share DM | none: the term sheets and {I['rule_doc']} are shared by name; the base share DMs are not universal, and no fact rests on one |")
A("| slack | INT-22 | Slack e-mail notifications | none: Frederick's base mailbox holds almost no such threads |")
A(f"| trello | INT-21 | no Trello→Slack integration | none ({I['dd_card']} posts nowhere) |")
A("| gmail, gdocs, gsheets, gslides, contacts | not integration sources | — | none |")
A("")
A("## Touched-data census and coherence hazards")
A("")
A(f"Touched data: the hub {I['hub_thread']} and copies; the rule doc {I['rule_doc']} and decoy {I['codev_doc']}; the DD publishing folder {I['dd_folder']} with the outreach sheet {I['outreach_sheet']} and eight term sheets; the one-pager {I['onepager_deck']}; the UA/BD board {B.UABD_BOARD} (list {B.BD_LIST}, cards {I['dd_card']}, {I['oakline_card']}, {I['sunfold_card']}); "
  f"#executives (roots {BASE['banker_root']}, {BASE['seventy_root']}, posts {BASE['rights_post']}, {BASE['rights_agenda']}, {BASE['ncsoft_question']}, {BASE['apple_arcade']}); #bridge-pitch (root {BASE['matthew_root']}, posts {BASE['positioned']}, {BASE['homa_codev']}); #analytics; DM D05S58U4SAK ({BASE['organic_arpi']}, {BASE['numbers_question']}, {BASE['tranche']}, {BASE['lead']}, {BASE['rayking_linkedin']}); "
  f"ENG-2362; the warehouse table ANALYTICS.MONETIZATION.REVENUE_DAILY; the sync doc {BASE['sync_doc']}; Frederick's Publishing Partners {BASE['partners_doc']} and Biz Dev Notes {BASE['bizdev_doc']}; the Appodeal and Rayking threads {BASE['appodeal_thread']}, {BASE['rayking_thread']}; Tilting Point's ack {BASE['tilting_ack']}; the board note {BASE['board_followup']}; every publisher thread.")
A("")
A("Hazards from coherence_hazards.json:")
A(f"- temporal: T02 — seeded threads run in date order (base_check Check C); the base Rayking thread keeps its own order and no seed is appended to it.")
A("- semantic: S04 (Frederick's GitHub 'Ryan') avoided — no GitHub record touched; other semantic hazards: none in scope.")
A("- cross-service referential: R04 avoided — seeded Slack names documents by title, never by link; R08 — seeded meetings carry invitation copies, except the two declared no_notify calls.")
A("- quantitative: Q01, Q03 — the three seeded replies update reply_count, reply_users_count and latest_reply on their roots (hazard_acknowledgements dated_claim); Q09 — the rule doc names one table, and V2 mirrors it; Q10 — one identical body per mailbox copy.")
A("- state/lifecycle: L08 — ENG-2362 is assigned to Arthur, active at the clock; other lifecycle hazards: none in scope.")
A(f"- identifier/format: I03 — seeded rows use the roster address {FRED}; I04 — RFC-2822 dates; I15 — seeded docs keep one title in Drive and Docs; I16 — Trello ids encode their action time.")
A("")
A("Known data issues (references/known_data_issues/synthcut.md, read for every touched record; no load-bearing fact, trap or graded slot rests on a card's 'Don't grade' value):")
A("- SC-1 (installs in the warehouse): excluded; monthly installs are publisher commitments.")
A(f"- SC-35, SC-3 (warehouse revenue against P&L workbooks): excluded; Frederick can open none of the P&L workbooks, and the keep value reads one named table.")
A("- SC-17 (ad-revenue payouts per network): excluded; keep value uses total_revenue_usd, never a network figure.")
A("- SC-3, SC-5, SC-73 (runway, burn, cash balance): excluded; no deliverable asks for them.")
A(f"- SC-39, SC-63 (Singular and Griffin lines in the sync doc): excluded; only the rights line of {BASE['sync_doc']} is cited.")
A("- SC-6 (vendor mail from brian.foster@): excluded; no vendor mail is on the path.")
A("- SC-49, SC-54 (Frederick's founder status and pay): no row grades either.")
A("- SC-9, SC-10, SC-33, SC-34 (investor sheet rows): investor work is out of scope.")
A("")
A("## Intended disagreements")
A("")
A("| Claim met first | Overturning record | Why realistic | Resolution |")
A("|---|---|---|---|")
DIS = [
 (f"Marek's mail {MSG['Oakline Games:2']} and card comment {I['oakline_card_comment']}: the $10,000 went out Sep 29", f"Arthur's reply {SL['arthur_cash']} (Sep 30): it never hit the account", "a wire can bounce on a wrong beneficiary; the sender reports sending, the bank reports receipt", "Banked means in the SVB account (rule doc): $0; the resend lands in October"),
 (f"Tallwater's term sheet {term('Tallwater Games')}: $60,000", f"note on {I['pb_event']}: $40,000 now", "publishers revise terms on calls and nobody reissues the paper at once", "use the latest terms, wherever they are (rule doc)"),
 (f"Sunfold's term sheet {term('Sunfold Mobile')}: 50,000 installs", f"Frederick's comment {I['sunfold_comment']}: 30,000", "a budget cut told by phone lands on a follow-up card", "use the latest terms"),
 (f"Moonrail's term sheet {term('Moonrail Studios')}", f"Robert's post {SL['kestrel_post']}: Kestrel froze signings", "a parent's call reaches one founder, who names the parent", "Withdrawn (first that fits); Anika's signature and Contacts join the names"),
 (f"the rule doc {I['rule_doc']}: sign Oct 31", f"ESG's note {MSG['esg_note']} and Leonard {MSG['esg_leo']}: Nov 14", "counsel's calendar moves a planning date", "the rule doc says use the lawyers' date"),
 (f"Northglow's and Pinegrove's offers have the highest 12-month values", f"the August position {BASE['rights_post']}, {BASE['sync_doc']}", "publishers ask for more than a founder has said they'd give", "Out on rights sits above Live in the rule doc"),
 (f"the Apr 30 board note {BASE['board_followup']}: paid-traffic numbers", f"Leonard's Sep 24 organic figure {BASE['organic_arpi']}", "a founder picks the planning figure", "the rule doc sets $0.50"),
 (f"Frederick's Sep 4 message in {BASE['rayking_thread']} looks like a reply", f"its Drafts label; his DM {SL['rayking_dm']}: we still owe them an answer", "drafts sit unsent", "Waiting on us"),
 (f"Summit's mail in {IDS['threads']['Summit Mobile']} looks like an answer", "the rule doc's No reply line", "auto-acks are common", "No reply"),
]
for d in DIS:
    A("| " + " | ".join(d) + " |")
A("")
A("## Constraints for the prompt brief")
A("")
A("| Anchor | May be named (noun phrases only) | Record |")
A("|---|---|---|")
A(f"| A1 | Leonard's email from yesterday | {MSG['hub']} |")
A(f"| A2 | the DD publishing card | {I['dd_card']} |")
A(f"| A3 | my DD publishing folder | {I['dd_folder']} |")
A("")
A("Never name in the prompt: the rule doc's rules, the rights position, any publisher, Copperleaf's or Redwood's route, ENG-2362, Kestrel, the SVB reply, the Tallwater note, the Sunfold comment, the Nov 14 date, the organic figure or Leonard's standing line.")
A("")
A("## Fact sheet")
A("")
A("| Key | Value | Kind | Home / must appear in |")
A("|---|---|---|---|")
for f in MAN["facts"]:
    A(f"| {f['key']} | {f['value']} | {f['kind']} | {', '.join((f.get('home_ids') or []) + (f.get('must_appear_in') or []))} |")
A("")
L.extend(fence(rd("fact_check.txt")))
A("")
A("fact_check drift warnings: each compares different publishers' amounts or the two dated signing dates; both are intended (a per-publisher value, and a superseded date declared in T9). No fix needed.")
A("")
tot = AGG.get("totals") or {}
A(f"Solver totals (`solver/truth.json`): {tot.get('publishers')} publishers; {AGG.get('classes')}; first pick {tot.get('first_pick')}, {tot.get('first_pick_value')} over 12 months, {tot.get('first_pick_q4')} in Q4; banked {tot.get('banked')}; keep value {tot.get('keep_value')}; contacts to add {tot.get('contacts_added')}; new cards {tot.get('cards_new')}, card comments {tot.get('card_comments')}, reminders {tot.get('reminders')}, organic notes {tot.get('organic_notes')}, nudges {tot.get('nudges')}.")
A("")
A("## Facts for the human")
A("")
A("| Locator | Base/seeded | Fact | Reach | Role |")
A("|---|---|---|---|---|")
RH = [
 (MSG["hub"], "seeded", "Leonard → Frederick, 2025-09-30T23:10Z, 'DD publishing: what I need for Monday': the model, the card, Contacts, the reply", "Frederick's mailbox", "first link (A1)"),
 (I["rule_doc"], "seeded", "Leonard, Sep 29: who's in, status order, valuing, Q4 cash, keep value, first pick, reminders, layout", "shared with Frederick", "authority H1"),
 (I["codev_doc"], "seeded", "Frederick, Sep 19: co-dev terms, not DD", "Frederick owns", "decoy"),
 (I["dd_card"], "seeded", "Leonard, Sep 29: checklists, follow-up cards, nudges", "unscoped", "authority H3"),
 (I["outreach_sheet"], "seeded", "Frederick, Sep 24: 24 publishers with what each got", "Frederick owns", "population"),
 (I["onepager_deck"], "seeded", "May one-pager with paid-traffic numbers", "Frederick owns", "evidence (T8)"),
 (I["dd_folder"], "seeded", "Frederick's DD publishing folder", "Frederick owns", "write target (A3)"),
 (SL["arthur_cash"], "seeded", "Arthur, Sep 30, reply under the banker root: the first-look never hit the account", "#executives member", "overturning (T1)"),
 (SL["copperleaf_relay"], "seeded", "Robert, Sep 26, reply under the 70 % D1 root: Copperleaf's offer", "#executives member", "cohort (T4)"),
 (SL["kestrel_post"], "seeded", "Robert, Sep 29: Kestrel froze outside signings", "#executives member", "overturning (T3)"),
 (SL["standing_line"], "seeded", "Leonard, Sep 26, reply under the Matthew root: the organic figure note", "#bridge-pitch member", "standing rule (T8)"),
 (SL["arthur_analytics"], "seeded", "Arthur, Sep 26: a publisher's tech lead, notes on ENG-2362", "#analytics member", "pointer (T5)"),
 (SL["rayking_dm"], "seeded", "Frederick → Leonard, Sep 5: we still owe them an answer", "DM member", "evidence (T12)"),
 (I["eng2362_comment"], "seeded", "Arthur, Sep 26: Redwood's offer pasted on ENG-2362", "unscoped", "cohort (T5)"),
 (I["sunfold_comment"], "seeded", "Frederick, Sep 30: Sunfold commits 30,000", "unscoped", "overturning (T7)"),
 (I["oakline_card_comment"], "seeded", "Frederick, Sep 29: Marek says the money went out", "unscoped", "claim met first (T1)"),
 (I["pb_event"], "seeded", "Sep 29 Tallwater call, note: advance is $40,000 now", "Frederick's calendar", "overturning (T2)"),
 (I["harbor_event"], "seeded", "Sep 26 Harbor Lane call, no change", "Frederick's calendar", "control"),
 (I["wavecrest_event"], "seeded", "Sep 25 Wavecrest call, terms as sent", "Frederick's calendar", "control"),
 (I["monday_event"], "seeded", "Oct 6 execs event", "Frederick's calendar", "context"),
 (MSG["esg_note"], "seeded", "ESG partner, Sep 29: earliest signature Nov 14", "Frederick's mailbox", "overturning (T9)"),
 (MSG["esg_leo"], "seeded", "Leonard, Sep 30: Nov 14 is the signing date", "Frederick's mailbox", "overturning (T9)"),
 (I["anika_contact"], "seeded", "Contacts: Anika Rao, Partnerships, Kestrel Group", "unscoped", "alias join (T3)"),
 (I["lena_contact"], "seeded", "Contacts: Lena Fischer, Sunfold Mobile", "unscoped", "skip (R10)"),
 (BASE["rights_post"], "base", "Leonard, Aug 25: keep code, IP and non-mobile rights", "#executives member", "authority H2"),
 (BASE["sync_doc"], "base", "Executives Biweekly Sync, Aug 28: the same sentence", "shared with Frederick", "authority H2"),
 (BASE["organic_arpi"], "base", "Sep 24: $0.50 D30 ARPI", "DM member", "input (R4)"),
 (BASE["appodeal_thread"], "base", "Appodeal's last message, May 21, no terms", "Frederick's mailbox", "cohort: Waiting on us"),
 (BASE["rayking_thread"], "base", "Rayking's mail with Frederick's unsent draft", "Frederick's mailbox", "cohort: Waiting on us"),
 ("snowflake.wh_analytics__monetization__revenue_daily", "base", f"DD total_revenue_usd: {B.KEEP_MONTHS}", "unscoped", "input (keep value)"),
]
for k in M:
    if M[k].get("base") or k in ("Copperleaf Games", "Redwood Arcade"):
        continue
    t = ROWS.get(k) or {}
    RH.append((IDS["threads"][k], "seeded", f"{k} thread: {t.get('Status')}", "Frederick's mailbox", "evidence (cohort)"))
    if k in B.TERM_DOCS:
        RH.append((term(k), "seeded", f"{k} term sheet: {B.TERM_DOCS[k][:70]}", "shared with Frederick", "evidence (cohort terms)"))
for r in RH:
    A("| " + " | ".join(str(x).replace("|", "/") for x in r) + " |")
A("")
A("## Blind sweeps")
A("")
L.extend(rd("sweep/dispositions.md").splitlines())
A("")
A("## Platform /injection review of rev1")
A("")
A("Attempt 6aed99b31c89eba1436ef322 (`injection-static-v2`, stored in `run_forensics/rev1/platform_injection_review.md`) reviewed rev1 (sha256 e6aa859bea5f, the SQL here byte for byte): FINAL VERDICT: PASS. Lint 0 FAIL, 0 CHECK, 0 INFO; Checks A, B and C PASS; no demonstrated defects. No advisory changes the SQL, because any SQL edit voids this PASS:")
A("- Advisory 1 (slides_pages.notes, slides_page_elements.table_json and ordinal, linear_comments.sequence not in the unverified snapshot): kept. The same four columns loaded on the frederick_q4_commitments rev2 platform changelog.")
A("- Advisory 2 (external term sheets with a parent in Frederick's private folder): kept as a simplification; check-sql shows each is shared with him (1.E). Whether a run finds them is checked at /prompt and the pre-check.")
A("- Advisory 3 (publisher thread numbers decode to Sep 1): information only; thread ids have no listed contract.")
A("- Advisory 4 (Robert's and Arthur's cited mail and Robert's call have no record of their own): deliberate, the offers are Slack-only and Linear-only; visibility is a /prompt question.")
A("- Advisory 5 (Robert's and Arthur's invite copies say PDT): cosmetic, kept.")
A("")
A("## Platform /prompt review of rev1 and the rev2 change")
A("")
A("Attempt 6aed99b31c89eba1436ef322 (`run_forensics/rev1/platform_prompt_review.md`) reviewed prompt bed2b497fa1e on rev1: FINAL VERDICT: FAIL, Score 2. Unique Ground Truth 2 and Clarity 2 came from one fork; every other dimension scored 5, the dataset gate was distinct at 0.599, and Cross-Service Coherence was 5. The fork: the rule doc's last line said what Leonard had said about what goes out to publishers 'still applies', which could be read as a limit on content rather than as three notes owed in this job.")
A(f"- Fixed in rev2: the last line of {I['rule_doc']} now says 'Fred, the notes I asked you for on what goes out to publishers still aren't done, so do those as part of this too.' The doc (Sep 29) follows the ask ({SL['standing_line']}, Sep 26), and nothing else in Leonard's Slack with Frederick asks for notes to publishers (hg.py searches of D05S58U4SAK and C096HFA5Z8W), so the line has one referent. Recipients and wording stay in the Slack line.")
A(f"- Also in rev2: the outreach sheet's note moved from a row under the table to a cell beside the header of {I['outreach_sheet']}. The platform reports counted it as a 25th sheet row and said 27 publishers, though their own lists name 26.")
A("- Not taken (optional, no score effect): removing the four unsnapshotted columns, which loaded on the Q4 platform changelog; emptying the term sheets' parents_json, which would change where a run finds them.")
A("- The prompt text doesn't change. Truth doesn't change in any field (oracle_kit regression against the rev1 SQL and truth). Rev2 needs /injection, then /prompt, then /hardness again.")
A("")
A("## Platform follow-ups")
A("")
A(f"- ○ carrier: the Tallwater note is on a calendar description ({I['pb_event']}), past 150 characters. L6 stays open: the Opus pre-check must show a run can read it with a full event read. Linear comment {I['eng2362_comment']} is ● (Ask_Carriers §6b).")
A(f"- `trello_create_card` on the UA/BD board and the checklist writes on {I['dd_card']} are unproven until the pre-check.")
A("- Warehouse revenue isn't compared cell by cell with the P&L: Frederick can't open those workbooks, so no deliverable rests on that comparison.")
A("- The forecast's exact mode doesn't fail write-content slots; read its E[avg] as an upper view.")
A("- No independent red team ran (REDTEAM_* unset; fallback recorded in the scenario design §13).")
A("")
A("## Self-review")
A("")
A("### Tool outputs (final SQL, verbatim)")
A("")
A("`tools/sql_lint.py`:")
L.extend(fence(rd("sql_lint.txt")))
A("")
A("sql_lint warning disposition (8 warnings, one class — on/after the clock): the four copies of the Oct 6 'DD publishing: execs' event carry future start and end plan fields, a not-yet-happened meeting created Sep 30; nothing after the seed bound is treated as completed.")
A("")
A("`tools/base_check.py`:")
L.extend(fence(rd("base_check.txt")))
A("")
A("base_check (run with the final manifest): the INT-11 exceptions for the Harbor Lane and Wavecrest calls are declared notes (no_notify: Frederick organized both; the only other attendee is external). The note lines for gsheets and gslides say those tables have no base-reference rules; sql_lint covers them.")
A("")
A("`tools/base_claims.py`:")
L.extend(fence(rd("base_claims.txt")))
A("")
A("`tools/hardness_gate.py` (final manifest + SQL):")
L.extend(fence(rd("hardness_gate.txt").replace("\nexit 0", "")))
A("")
hgl = json.loads(rd("hg_lint.txt"))
A(f"`tools/hg.py lint` (the eval's hg_injection_lint, base data): counts {hgl.get('counts')}. LINT: no CHECK flag to disposition; no INFO.")
A("")
A("### Preflight (S4b–S5e)")
A("")
L.extend(fence(rd("oracle_kit.txt")))
A("")
L.extend(fence(rd("mutation.txt").replace("missing []", "missing: none")))
A("")
L.extend(fence(rd("geometry.txt").replace("missing []", "missing: none")))
A("")
L.extend(fence(rd("liveness.txt")))
A("")
L.extend(rd("preflight_note.md").splitlines())
A("")
L.extend(fence("\n".join(l[:230].replace("[]", "none") for l in rd("forecast_injection.txt").splitlines() if "V3 E[avg]" in l or "V3: P(all" in l or "ledger: forecast record" in l)))
A("")
A("`tools/preflight_report.py --forecast 01c_Forecast.json`:")
L.extend(fence(rd("preflight.txt").replace("[]", "none")))
A("")
A("### Changes made at this stage (and why)")
A("")
L.extend(rd("sweep/changes.md").splitlines())
A("")
A("### /injection Checks A–C walk")
A("")
A(f"- Inventory: {n_ins} INSERT, {n_upd} UPDATE, 0 DELETE, no upserts; tables {dict(sorted(by_table.items()))}. PASS.")
A("- Check A (references and IDs): every channel, user, issue, thread, calendar, board, list and folder resolves (base_check Check A PASS); in_reply_to and references point at earlier seeded messages; every minted id has 0 base hits (1.F); owners and shares are roster addresses or the publisher's own address. PASS.")
A("- Check B (structure): sql_lint 0 errors; every *_json column is literal JSON; NOT NULL columns supplied; generated columns never written; camelCase Trello columns quoted. PASS.")
A("- Check C (dates, parents, statuses, counts): all seeded timestamps ≤ 2025-10-01T00:00Z except the Oct 6 event's plan fields; replies after their parents; root counters match; statuses unchanged. PASS.")
A("")
A("### Touched-data census")
A("")
A("See 'Touched-data census and coherence hazards' above: six hazard categories covered, each with cited hazards or 'none in scope', and the cards SC-1, SC-3, SC-5, SC-6, SC-9, SC-10, SC-17, SC-33, SC-34, SC-35, SC-39, SC-49, SC-54, SC-63, SC-73 dispositioned.")
A("")
A("### Counter-readings")
A("")
A("| Category | Counter-reading (strongest argument it FAILS) | Evidence that resolves it | Verdict |")
A("|---|---|---|---|")
exec(open(os.path.join(HERE, "dossier_counter.py")).read())
for c in CR:
    A("| " + " | ".join(c) + " |")
A("")
A("People status: everyone a rule depends on is active at the clock (Leonard, Robert, Arthur, Frederick per activity.json; ESG Law is external); no Snowflake roster or Confluence headcount line is used.")
A("")
A("Unresolved: no independent red-team review (fallback recorded); channel landing rates are analogs from completed Frederick tasks (UNCALIBRATED); the calendar-description route and writes on the UA/BD board await the pre-check.")
A("")
