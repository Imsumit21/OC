"""Hand-written dossier sections for plan/assemble_dossier.py. Design text only: no prompt, Oracle Event or criterion wording."""
import json, re

ROLE = {"f_a37b403d5200d4f0a31d31": "authority", "f_762c60832854d3e7a7f7df": "decoy", "f_5ecaa967db3adcfa440b09": "claim met first",
        "f_75dddccabb26eeea4842c8": "format reference", "d_601064334a0b493022fe83": "destination",
        "C0ADGSZKR3R/1770949": "amendment", "C0ADGSZKR3R/1770938": "origin", "evt_6f1a2c9e4b7d3a58c0e1d2": "due date",
        "698e5a10c3f24b7e9d16a0e4": "order of work", "ec2ea957-fc8e-4958-b809-0fb735b1e916": "hub",
        "LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2": "as-of authority", "LV3PR19MB85246D2E9B14C7A03F5E8D12BC4A7": "boundary",
        "mlkq74xd": "ask", "CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw": "overturning",
        "CAPBs_a7Tq2LmV9xYcR4KdN8wUe3HsJ6oFbZ1gPiA5tGyQnE0Xw": "connecting", "CAPBs_a5Wn3RvK8yZtH2DqL7mJc9XeU4oGfB6sPiN1aTuYkEr0Q": "connecting"}


def tail(A, table, fence, rd, g1, G):
    MB, GM, TH, SUM, AGG, TRUTH, MAN = G["MB"], G["GM"], G["TH"], G["SUM"], G["AGG"], G["TRUTH"], G["MAN"]
    N, O, D, P = G["DOC_NOTES"], G["DOC_OLD"], G["DECK"], G["PROJECT"]
    SH, F, C, E, FAM, ORI = G["SHEET"], G["FOLDER"], G["CARD"], G["EVT"], "C0ADGSZKR3R/1770949310.220519", G["SL_ORIGIN"]
    LIST, SEG, TOR, CLAIRE, ONE, DRAFT = "C0ADGSZKR3R/1770934638.035469", "D04UC0UEN2V/1770664988.379119", "D09R59580EM/1762285888.654689", "C51ECE5102ED/1770903714.600249", "C0ADGSZKR3R/1770664924.520089", "C0ADGSZKR3R/1770664700.848759"
    LETTERS, CARTA = "C0ADGSZKR3R/1770841239.761999", "C0ADGSZKR3R/1770935621.095649"
    OWNER = f"{MB}/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com>"
    ES14, MATT, PHIL = f"{MB}/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv>", f"{MB}/<CAMy0Hx1va3q4zH2HyPiqfm8Je2fm5A=JHKf8LrXWb12z2FHr6w@mail.gmail.com>", f"{MB}/<BYAPR02MB435880CCF501BE0AE906AFFDC460A@BYAPR02MB4358.namprd02.prod.outlook.com>"
    SIGN, ENES, BROS = f"{MB}/<CAPBs_a46H9SCR=PBn1EP4RvCL+HO3XqOma4mTNu0WdnWv17ZuA@mail.gmail.com>", f"{MB}/<A658306E-3D13-458C-A311-95454D575822@librasoftworks.com>", f"{MB}/<0CDD5A07-0BE6-4909-8188-93E10FBF4E16@librasoftworks.com>"
    BRIAN, VINC = f"{MB}/<CAPBs_a68Agj+37mZ6abeW5KEKTh00he+mgOpLP2FrpDjeO-37Q@mail.gmail.com>", f"{MB}/<CAEH8bLxfNq9vp7-VSMQdpetPWQxBhv2pcPE=xj=oX9c8MxNFtA@mail.gmail.com>"
    ADVT, TERM, CHARTER, SIDE, SPA = "f_6a37227593d0977fdbdd7a", "f_11040fe5d66821bd6951aa", "f_90c029015fc474199cf736", "f_6201c7027d02997bfb2c84", "f_966445655f653d26dc8537"
    KPMG, FOLLOW, SUNSET, ROBERT, ACK = GM["kpmg"], GM["kpmg_follow"], GM["sunset"], GM["robert_leo"], GM["kpmg_ack"]

    A("## Findability and discovery-order proofs")
    A("")
    for t in [
        f"- Hub (AN2) {P} 'Holder records': a Linear project list returns it; its 26 issues come from one list call, with titles and states but no comments. The description names the close-out notes and Sunset's ask.",
        f"- Close-out notes H1 {N}: the project description says 'my close-out notes'; a Drive search for 'close-out' or 'notes', or a listing of the folder {F}, returns it. 'close-out' has 0 base hits (research/g1_grounding.md 1.D), so the seeded name is the only hit. The older {O} is found by 'notes' or 'outreach'.",
        f"- Investor email draft (AN1) {DRAFT}: named by the Task List row and H1; first post of its kind in #winddown.",
        f"- KPMG (AN3) {KPMG}: a mail search for 'Audit Request' returns it first with FY23 and FY24 older; the whole thread reads in one call, so the follow-up {FOLLOW} comes with it.",
        f"- Sunset's ask {SUNSET}: the project description says 'what Sunset asked for'; a mail search for 'Sunset' or 'stockholder' returns it.",
        f"- Family amendment {FAM}: a reply under {LIST}, which H1 names twice ('where I left things today', 'reply under my list in #winddown') and which every run must write under. A channel read shows reply_count 4; `slack_read_thread` returns it.",
        f"- T1 ADV: claim met first, the owner list {OWNER} (86,470, 81,383, 31,536 twice). Overturning: the advisor table {ADVT} (61,038, 30,518, 6,104, 6,104) and the term sheet {TERM} (3,051,879). A run sees it when its sum is 103,764 too high, or from any Advisor Agreement hit.",
        f"- T4 and T5 LETTER: claim met first, {LETTERS} and {CARTA}. Overturning: the six letters (one search on their shared phrase, for example {BRIAN}) against the eight Feb 12 Carta entries such as {ES14}.",
        f"- T6 TOLD: claim met first, {LIST}. Overturning: {SEG}, a DM reached by the holder's name or by Leonard's DM list; thin link recorded under Platform follow-ups.",
        f"- T7 TOLD: same claim. Overturning: {ROBERT}, a reply on a 2023 wire thread, found by a mail search on the holder's address or on 'closing'.",
        f"- T10 and T11 BOARD: claim met first, the financing documents {SPA}. Overturning: {MATT} and {PHIL}; the vote is in the charter {CHARTER}.",
        f"- T12 ASOF: {KPMG} and {FOLLOW} against the effective dates in the 14 notices such as {ES14}.",
        f"- T13 FAM: the owner list shows no shared surname; {ENES} and {BROS} tie the three lines, and {FAM} gives the rule.",
        f"- T17 ASK: {CLAIRE}, a group DM; the reply beside it answers a different question.",
    ]:
        A(t)
    A("")
    A("## Self-validation")
    A("")
    table(["QC category", "Tool-enforced (result)", "Manual (evidence)"], [
        ["Missing Universe Data", "check-sql PASS (1.E)", f"every deciding fact is Leonard-readable: {N}, {KPMG}, {SUNSET}, {ROBERT}, {FAM}, {OWNER}, {ADVT}"],
        ["Temporal Field", "sql_lint 0 errors; base_check Check C PASS", f"card {C} 22:54Z, folder {F} 23:20Z, project {P} 23:24Z, notes {N} 01:05Z, KPMG {KPMG} 16:48Z, Sunset {SUNSET} 18:06Z; project updated after Sunset's mail; no Slack row after the export end"],
        ["Cross-service Referential", "base_check Check A PASS", f"every id the text names resolves; the notes name the list {LIST} and draft {DRAFT} in words, with no link (hazard R04)"],
        ["Quantitative / Reconciliation", f"list parent counters updated on {LIST}: reply_count 4, reply_users_count 2, latest_reply the seeded ts", f"truth ties: Series Seed {SUM['Series Seed total']:,}; live options {SUM['Options outstanding now']:,}; at Dec 31 {SUM['Options outstanding at Dec 31']:,}; none of the three appears in the SQL except where a base record has it ({TERM})"],
        ["State / Lifecycle", "26 issues in Backlog with no stamps; no activity on a closed record", f"Trello card {C} is open in To Do; base card 68c5a49e8491a9d7faf869d0 untouched"],
        ["Identifier / Format", "eval lint FAIL 0 CHECK 0", "ids follow base schemes (1.A); base tokens kept; Contacts rows use the bare token form as /contacts/84 does"],
        ["Semantic / Category", "fact_check PASS", f"titles match content ({N}, {C}, {P}); the project name and issue titles say nothing about the closing"],
        ["Other", "(none)", "voice per 1.C; no record states an owed label, a total or a told state"],
    ])
    A("")
    A("## Integrations and companions")
    A("")
    table(["Service", "INT entries", "Companion"], [
        ["slack", "INT-22 optional, never load-bearing", f"none needed; parent counters updated on {LIST}"],
        ["gmail", "none: no integration has Gmail as source", "own companions: thread rows, in_reply_to in the same mailbox, a Robert copy where the base keeps one (robert@harmonygames.co/1773963101279916523)"],
        ["gcal", "INT-11, recorded as no_notify in integration_exceptions", f"one copy, Leonard sole attendee, {E}"],
        ["linear", "INT-04 window ended 2026-01-28, INT-05 not required", "no mirror; issue updated_at equals its newest comment"],
        ["gdrive", "INT-13 mirror ended 2026-01-19, recorded in integration_exceptions", "nothing is shared at seed time"],
        ["contacts", "none: contacts has no integration", "two rows, token and email only"],
        ["trello", "INT-21: no integration exists", f"dateLastActivity, badges, createCard and commentCard actions on {C}; trello_boards activity updated"],
    ])
    A("")
    A("## Touched-data census and coherence hazards")
    A("")
    A(f"Touched data: #winddown C0ADGSZKR3R (Feb 12 evening, plus the thread under {LIST}, counters updated); Leonard's Drive root d_63fffeb4fab5233ed5bb73; the Harmony Games Trello board; base thread {MB}/1773963101399472184 and robert@harmonygames.co/1773963101279916523 (snippets updated); team_ENG's series from ENG-2438. Everything else is new records.")
    A("")
    A("Hazards from coherence_hazards.json (normal KB):")
    for t in [
        "- temporal: hazard T06, the card's dateLastActivity equals its newest action; hazard T07, no seeded #prototype message.",
        "- semantic: hazard S06, the Contacts rows set job 'Investor' and do not touch rows whose job differs from the roster; hazard S07 none in scope.",
        "- referential: hazard R04, the seeded text names docs in words and carries no Drive link; hazard R08, the hold has no invitation mail and is listed under integration_exceptions.",
        f"- quantitative: hazards Q01, Q02, Q03, the parent {LIST} carries reply_count 4, reply_users_count 2 and latest_reply; hazard Q10, Robert's reply is word for word the same in both mailboxes; hazard Q11, one calendar copy.",
        "- state/lifecycle: hazard L13 excluded and L08 excluded, as in hazard_acknowledgements; seeded issues are unassigned and carry no PR.",
        "- identifier/format: hazard I02, every seeded Slack id is sha256(channel|ts)[:32]; hazard I03, every seeded row uses leonard.hayes@harmonygames.co.",
    ]:
        A(t)
    A("")
    A("Known data issues (references/known_data_issues/normal.md; no load-bearing fact, trap or graded slot rests on a card's 'Don't grade' value):")
    for t in [
        "- NB-1: only Leonard and Arthur post the seeded lines, in #winddown; nothing grades channel access.",
        "- NB-3, NB-4: no cash figure and nothing on whether Sunset was paid.",
        "- NB-6: the last seeded Slack row is Feb 13 02:23Z; five later records sit in other services and imply no Slack message.",
        "- NB-12: rows are keyed by issue, and token name forms count.",
        "- NB-15: seeded text says 'service' and 'let the team go', never employee or contractor.",
        "- NB-22: 'as Carta shows it' sends ES-12's date to the notice, never the letter.",
        "- NB-24: base Linear has no comments, so all seeded comments are new; each is a dated, quoted fact.",
        "- NB-29: no seeded text gives a decision date.",
        "- NB-31: nothing argues who saw a DM from its member list.",
        "- NB-32: ES-5 is decided by Carta's dates; the end date is never graded.",
    ]:
        A(t)
    A("")
    A("## Intended disagreements")
    A("")
    DIS = [
        [f"owner list lines 86,470, 81,383, 31,536 ({OWNER})", f"advisor table {ADVT} and term sheet {TERM}", "a 2024 list merged what a holder bought with their advisor grant", "stock is the line less the grant; the sum then ties to 3,051,879"],
        [f"'All termination letters are sent' {LETTERS}", f"six letters such as {BRIAN} against eight Carta entries such as {ES14}", "a founder's done line said from memory the night before the Carta work", "ES-14 and ES-18 have no letter"],
        [f"'Carta terminations are done' {CARTA}", f"the letters only promise a Carta mail ({BRIAN})", "administrator notices go to Leonard alone", "every live holder is still owed a last day"],
        [f"'the angels are what's open' {N}, from {LIST}", f"{SEG} and {ROBERT}", "the list is Leonard's own; Robert acted without telling him in Slack", "two angels are already told"],
        [f"Tor's Nov 4 DM {TOR}", f"{N} 'about the closing'", "a runway warning is not the closing", "Tor is still owed the closing"],
        [f"board of four in {SPA}", f"{MATT} and {PHIL}", "resignations happened by mail", "directors in office are Leonard and Robert"],
        [f"earlier notes {O}", f"close-out notes {N}", "a rough plan was replaced", "the later notes govern"],
        [f"holder sheet draft {SH}", f"project {P} and Carta", "figures copied before the Feb 12 entries", "the draft is not the list"],
        [f"H1 'One row and at most one note per person' {N}", f"family reply {FAM}", "Leonard adds a rule after writing the doc", "one note covers the family's lines"],
    ]
    table(["Claim met first", "Overturning record", "Why realistic", "Resolution"], DIS)
    A("")
    A("## Constraints for the prompt brief")
    A("")
    table(["Anchor", "May be named (noun phrases only)", "Record"], [
        ["AN1", "the investor email draft in #winddown", DRAFT],
        ["AN2", "the holder project in Linear", P],
        ["AN3", "KPMG's audit request for Griffin", KPMG],
    ])
    A("")
    A("Never name in the prompt: Tuesday or any due date, the notes' rule sentences, the family rule, Arthur's sharing, Robert's reply, the advisor table, the side letter, any resignation, Claire's question, Sunset's list.")
    A("")
    A("The prompt must settle one thing: the KPMG reply and the Griffin heads-up go out as replies, because the personal notes alone stay drafts. rev1_run_sim.md section 4 shows a careful run may otherwise leave a draft, and 39 weight reads replies only. It settles this by saying what to send, with no rule text.")
    A("")
    A("## Fact sheet")
    A("")
    A("Facts declared in the manifest (checked by fact_check --no-leak):")
    table(["Key", "Value", "Kind", "Home records"], [[f["key"], f["value"], f["kind"], "; ".join(f.get("home_ids") or [])] for f in MAN["facts"]])
    A("")
    A("Truth totals (solver/truth.json; never in the SQL):")
    table(["Figure", "Value"], [[k, f"{v:,}" if isinstance(v, int) else v] for k, v in SUM.items()] + [["Owed classes", json.dumps(AGG["classes"])], ["Issue states", json.dumps(AGG["states"])], ["Notes", AGG["notes"]], ["Reason comments", AGG["reason_comments"]], ["Goes first", AGG["first_to_go"]]])
    A("")
    A("## Facts for the human")
    A("")
    rows = [
        [N, "seeded", "close-out notes: the asks and the closed rule", "owner", "authority H1"],
        [O, "seeded", "earlier notes: one mail to everyone", "owner", "decoy"],
        [f"{P} (team_ENG)", "seeded", "project description: scope, states, why on the issue", "unscoped", "hub AN2"],
        [KPMG, "seeded", "FY25 request, as of December 31, 2025", "Leonard's mail", "AN3, H4"],
        [FOLLOW, "seeded", "a termination effective on the as-of date counts as of that date", "Leonard's mail", "boundary"],
        [SUNSET, "seeded", "what the intake needs on stockholders", "Leonard's mail", "K8"],
        [ROBERT, "seeded", "Robert tells the holder the company is closing, Leonard copied", "Leonard's mail", "T7"],
        [FAM, "seeded", "family line, Covered label, sheet goes to Arthur too", "#winddown member", "T13, K14"],
        [ORI, "seeded", "the holders go in Linear", "#winddown member", "K15"],
        [SH, "seeded", "partial draft, figures marked as copied", "owner", "T20"],
        [D, "seeded", "update outline", "owner", "K12, T19"],
        [C, "seeded", "order of work", "unscoped", "K10"],
        [E, "seeded", "Tuesday hold, Feb 17", "owner", "K11"],
        [OWNER, "base", "Nov 2024 owner list", "Leonard's mail", "T1, T2"],
        [ADVT, "base", "advisor table, 103,764 in all", "Drive share", "T1"],
        [TERM, "base", "term sheet, 3,051,879 and 268,772", "Drive share", "T1, T3"],
        [ES14, "base", "ES-14: effective Nov 21, 2025, entered Feb 12, 2026, last day Feb 21", "Leonard's mail", "T3, T12"],
        [BRIAN, "base", "a Feb 11 letter; equity paragraph gives no date", "Leonard's mail", "T4, T5"],
        [VINC, "base", "ES-14's resignation", "Leonard's mail", "C2"],
        [SEG, "base", "Leonard's Feb 9 DM to Segerstrale", "DM member", "T6"],
        [LIST, "base", "Leonard's Feb 12 list", "#winddown member", "K4"],
        [TOR, "base", "Nov 4 runway DM", "DM member", "T8"],
        [MATT, "base", "Collins resigns, May 1, 2025", "Leonard's mail", "T10"],
        [PHIL, "base", "Griffin's director resigns, Feb 12, 2026", "Leonard's mail", "T10"],
        [CHARTER, "base", "protective provision: a vote of the preferred", "Drive share", "T11"],
        [ENES, "base", "Enes gives all three addresses", "Leonard's mail", "T13"],
        [BROS, "base", "all three brothers wired", "Leonard's mail", "T13"],
        [CLAIRE, "base", "Claire's open equity question", "group DM member", "T17"],
    ]
    table(["Locator", "Base/seeded", "Fact", "Reach", "Role"], rows)
    A("")
    A("## Platform follow-ups")
    A("")
    for t in [
        "- Prove `gmail_create_draft` in the pre-check: 18 slots rest on it, and it has never run in a stored baseline. Sends are the fallback.",
        f"- Test live Slack file-name search in the pre-check. {SEG}'s partner is named only by a 2023 file name, so a run with no such search has a longer route.",
        f"- Confirm `slack_read_channel` shows reply_count on {LIST}.",
        "- Linear comments are load-bearing carriers only for calls, never for a deciding fact.",
        "- The gate's Gmail base lookup takes a thread's first `files` match, which is an attachment on four cited threads; those version records use the file and pointer form.",
    ]:
        A(t)
    A("")
    A("## Self-review")
    A("")
    A("### Tool outputs (final SQL, verbatim)")
    A("")
    A("`sql_lint.py`:")
    fence(rd("sql_lint.txt"))
    A("sql_lint warning disposition (clock class, 2 warnings): the Tuesday hold starts and ends on Feb 17, after the clock: a not-yet-happened event, a deadline-type plan field, allowed.")
    A("")
    A("`hg.py lint` (the eval's hg_injection_lint, with base data):")
    hl = rd("hg_lint.json")
    hl = json.loads(hl[hl.index("{"):])
    fence(f"hg_injection_lint (base data): counts {hl.get('counts')}; flags: {len(hl.get('flags') or [])}; info: {len(hl.get('info') or [])}")
    A("LINT: counts FAIL 0, CHECK 0, INFO 0, so there is no CHECK to disposition.")
    A("")
    for name, f in (("base_check.py", "base_check.txt"), ("base_claims.py", "base_claims.txt"), ("fact_check.py --no-leak", "fact_check.txt"), ("hardness_gate.py (final manifest + SQL)", "hardness_gate.txt")):
        A(f"`{name}`:")
        fence(rd(f))
    A("fact_check warning disposition: the inactive_person_named lines are holders named in issue titles, who are the subject of a record and not its author; the ambiguous_name line is the Carta form of ES-13's name.")
    A("")
    A("### Preflight (S4b–S5e)")
    A("")
    A("`oracle_kit.py check`:")
    fence(rd("oracle_kit.txt"))
    A("`difficulty_mutation.py mutate` (tail) and `geometry`:")
    fence("\n".join(rd("mutation.txt").splitlines()[-44:]))
    fence(rd("geometry.txt"))
    A("`trap_liveness.py` (SQL):")
    fence(rd("trap_liveness_sql.txt"))
    A("`hardness_forecast.py forecast --preregister` (tail) and `preflight_report.py`:")
    fence("\n".join(rd("forecast.txt").splitlines()[-14:]).replace("[]", "(none)"))
    fence(rd("preflight.txt").replace("[]", "(none)"))
    fid = (re.search(r"'id': '(hev_[0-9a-f]+)'", rd("forecast.txt")) or [None, "(not recorded)"])[1]
    dfid = rd("forecast_id.txt").strip()
    A(f"Forecast (UNCALIBRATED, advisory), two views that disagree by construction:")
    A(f"- Solver-based, pre-registered as {fid} (01c_Forecast.json). It never fails a write-content slot, and those carry 144 of the 245 weight points, so it reads high (tail above).")
    A(f"- Design view, pre-registered as {dfid} (plan/forecast_output.txt), which fails write-content slots with their declared mechanisms: E[avg] about 73-74 %, P(all four gates) 0.44-0.54.")
    A("- Cold run simulation (research/sweeps/rev1_run_sim.md): 75.5 % on the first text, about 71 % after the three changes made here, judgement only.")
    A("")
    A("Every mutation result, channel degrade, intervention and liveness flag has a written disposition in `Working_Files/01c_Dispositions.json`. preflight {report, digest} is not written back into the final manifest, because the report binds the manifest by sha256.")
    A("")
    A("### Changes made at this stage (and why)")
    A("")
    for d in MAN.get("design_delta", []):
        A(f"- {d['id']}: {d['change']}. Reason: {d['reason']}")
    A("")
    A("### /injection Checks A–C walk")
    A("")
    A(f"- Inventory: {len(G['ins'])} INSERT, {len(G['upds'])} UPDATE (thread snippets, the list's counters, board activity), no DELETE; every statement is in the record ledger.")
    A(f"- Check A (references, uniqueness, identities, id contracts): PASS. base_check Check A; every parent resolves ({LIST}'s row e3e198cc6e3f866a032d34c5f69e39f9, Drive root d_63fffeb4fab5233ed5bb73, board 640643a3fd8f3ca308d9318e, list 640643a3fd8f3ca308d93195); 1.F shows 0 id collisions.")
    A("- Check B (structure, literal JSON, generated and NOT NULL columns): PASS. sql_lint 0 errors; no text_fts or body_text_fts; every *_json column holds literal JSON; Linear dates YYYY-MM-DDTHH:MM:SSZ.")
    A("- Check C (dates, parent and reply, statuses, counts, claimed updates, superseding records): PASS. base_check Check C; every seeded event is before the seed bound except the Tuesday hold; replies follow their roots; comments follow their issues; each issue's updated_at is its newest comment.")
    A("")
    A("### Touched-data census")
    A("")
    A("The census and hazard dispositions are in 'Touched-data census and coherence hazards' above (all six categories; ten NB cards dispositioned).")
    A("")
    A("### Counter-readings")
    A("")
    A("| Category | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |")
    A("|---|---|---|---|")
    CR = [
        ("Temporal", "Robert's reply says the team has gone while people still work on Feb 12", f"reworded to 'we've had to let the team go'; {ROBERT}; research/sweeps/rev1_coherence.md B1", "fixed"),
        ("Temporal", "the notes say Tuesday while #winddown says google is archived after Feb 15", f"the notes now say that waits; C0ADGSZKR3R/1770933903.645709 keeps accounts with data until it is extracted; {N}", "fixed"),
        ("Temporal", "project text refers to Sunset's ask before it exists", f"project updated_at is after {SUNSET}; the Slack line {ORI} says nothing about Sunset", "PASS"),
        ("Semantic / Category", "'founders aside' could leave out ENG-2462, whose holder the roster calls Co-founder", f"reworded to 'the three of us aside'; {P}; rev1_coherence.md M3", "fixed"),
        ("Semantic / Category", "'told' could mean heard about it from a channel post", f"H1 says 'sent to them directly and delivered'; {N}; C05KNDCHAAG/1770839984.194409 is not sent to them directly", "PASS"),
        ("Semantic / Category", "'what we still need from Griffin' could be nothing, since the director left", f"Sunset asks who holds the preferred vote ({SUNSET}) and the charter's provision {CHARTER} needs a vote of the preferred", "PASS"),
        ("Cross-service Referential", "the Wind Down folder could look barred to Leonard", f"reworded; {N} says what that folder holds; rev1_coherence.md B2", "fixed"),
        ("Cross-service Referential", "the Task List row might not exist", "gsheets f_31115ddb6ed866f2b10d60 row 'Send email to investors'; design K5", "PASS"),
        ("Quantitative / Reconciliation", "266,436 could be right if a Dec 31 termination counts in full", f"{FOLLOW} closes the boundary; {KPMG} says as Carta shows it", "PASS"),
        ("Quantitative / Reconciliation", "the Side Fund's issue quoting 2,746,693 reads false", "the comment labels it 'both funds on one line'; ENG-2439; research/g2_holder_facts.md section 4", "PASS"),
        ("State / Lifecycle", "Covered lines could be Todo while the family note waits", f"the project sentence says 'where its own note is waiting'; {P}", "PASS"),
        ("State / Lifecycle", "a lapsed line could be Done", f"the project sentence tests Canceled first; {P}", "PASS"),
        ("Identifier / Format", "a Contacts row could use the wrong token form", "first_name uses the bare token as base /contacts/84 does; rev1_coherence.md m6", "fixed"),
        ("Identifier / Format", "the Trello id could disagree with its time", f"{C}'s hex prefix is 2026-02-12T22:54:08Z, the time used; research/g1_grounding.md", "PASS"),
        ("Other (designed T1)", "best argument the owner list is simply right", f"{TERM} totals 3,051,879 and the list sums 103,764 above it; {ADVT}", "designed"),
        ("Other (designed T4)", "best argument Leonard's done line stands", f"six letters against eight entries; {BRIAN}; {ES14}", "designed"),
        ("Other (designed T6, T7)", "best argument the angels are all open", f"{SEG}; {ROBERT}", "designed"),
        ("Other (designed T8)", "best argument Tor was told", f"{TOR} never says the company is closing", "designed"),
        ("Other (designed T10)", "best argument the document board stands", f"{MATT}; {PHIL}", "designed"),
        ("Other (designed T13)", "best argument 'one note per person' forbids the family note", f"{FAM} comes after {N} and says the family's lines need no note of their own", "designed"),
        ("Other (designed T18)", "best argument the earlier notes still govern", f"{N} says it replaces them; {O}", "designed"),
        ("Other (designed T20)", "best argument the draft sheet is the list", f"its rows say they are copied from the Nov 2024 list; {SH}", "designed"),
        ("Other (pre-existing)", "the roster's Co-founder holds an option line that lapsed", f"Carta's notice for ES-17 and {MB}/<176175429549.10.8466995912642267217@notifications-email-sending-worker-6b65bf6cf7-gcpxf>", "PASS (pre-existing)"),
    ]
    for c in CR:
        A("| " + " | ".join(c) + " |")
    A("")
    A(rd("sweep_dispositions.md"))
    A("")
    A("Unresolved:")
    for t in [
        "- `gmail_create_draft` is unproven until the pre-check.",
        "- Opus 5.5 landing rates remain UNCALIBRATED priors, and under 70 % is not supported by the current estimates.",
        "- SD is the gate most at risk once the rubric multiplies rows.",
        "- Every Slack count in 1.D is a substring count from hg.py, not live tool behaviour.",
    ]:
        A(t)
    A("")
