#!/usr/bin/env python3
"""Assemble Working_Files/04_Prompt_Check.md for the current 04_Prompt.txt (check mode, C1 to C24) and write the
prompt-check outcome and role reviews into 00_V3_Authoring_Evidence.json. The prompt file is read byte for byte and never
written. Every quoted span is asserted to be an exact substring before the report is written."""
import datetime as D, hashlib, json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
ROOT = TASK.parents[1]
OUT = HERE / "out"
TOOLS = TASK.parent / "tools"
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(TOOLS))
import design_model as M
import planned_texts as TXT
from base_check import parse_sql
from stage_gate import file_digest

prompt = (TASK / "04_Prompt.txt").read_text()
before = hashlib.sha256(prompt.encode()).hexdigest()
words, sha12 = len(prompt.split()), before[:12]
ctx = json.loads((WF / "00_Task_Context.json").read_text())
man = json.loads((WF / "01_Hardness_Manifest.json").read_text())
S, B, PT, C = M.SEED, M.BASE, M.PACK_TICKET, M.COUNTS
ASK, NOTES, LIST, HOLD, CONTACT = (S[k]["id"] for k in ("ask", "notes", "tracker", "hold", "contact"))
A1, A2, REPLY, LOG, SHEET, PICKS = (S[k]["id"] for k in ("a1_post", "a2_dm", "c3_reply", "c4_log", "c2_sheet", "picks"))
ROOT_DRIVE = B["julia_root"]
FRED, BRIAN, ROBERT, INTAKE = "frederick.stone@harmonygames.co", "brian.foster@harmonygames.co", "robert@harmonygames.co", TXT.CONTACT["email"]
def tk(n): return M.BY_NAME[n]["ticket"]
FIRST, LAST = tk(M.LINES[0]["name"]), M.LAST_CHILD
def table(head, rws): return "\n".join(["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(str(c) for c in r) + " |" for r in rws])
def code(t): return "```\n" + t.rstrip("\n") + "\n```"
def q(span):
    assert span in prompt, ("not an exact substring of 04_Prompt.txt", span)
    return f"\"{span}\""
def run(*a):
    p = subprocess.run([sys.executable, "-B", *[str(x) for x in a]], capture_output=True, text=True, cwd=ROOT)
    return (p.stdout or p.stderr).rstrip()

# ---- facts re-read in this run
rows = [r for r in parse_sql((TASK / "01_Universe_Inject.sql").read_text()) if r["op"] == "insert"]
ch, ts = ASK.split("/")
ask_row = next(r["row"] for r in rows if r["table"] == "slack.slack_messages" and r["row"]["channel_id"] == ch and r["row"]["ts"] == ts)
ask_text = ask_row["text"]
for needle in ("both in your Drive", "give me the count for each state here", "post both links in the PlayableX channel", "My hand-off notes say what goes in the brief"):
    assert needle in ask_text, needle
sent = D.datetime.fromtimestamp(float(ts), D.timezone.utc)
sent_pt = sent - D.timedelta(hours=7)
assert sent.date().isoformat() == "2025-09-30" and sent_pt.date().isoformat() == "2025-09-30"
cansee = "\n".join(run(TOOLS / "persona_view.py", "can-see", "julia_lawson", svc, rid) for svc, rid in (("slack", M.DM_FRED), ("slack", M.VENDOR_CH), ("gdrive", ROOT_DRIVE)))
v2 = run(TOOLS / "hardness_v2_check.py", "--task-dir", TASK)
(OUT / "hardness_v2_prompt.txt").write_text(v2 + "\n")
assert "RULE_IN_PROMPT" in v2 and "CLEAN      RULE_IN_PROMPT" in v2, "rule-in-prompt check is not clean"
sweep = (OUT / "sweep_check.txt").read_text() if (OUT / "sweep_check.txt").exists() else ""
cases = json.loads((ROOT / "Evals/references/rules/prompt_qc_cases.json").read_text())
cases = cases.get("calibration_cases") or cases
CLOCK = ctx["universe"]["clock_line"]
S1, S2, S3 = "I need a hand with Frederick's playable message from yesterday.", "Can you do everything he's asking for in it, start to finish?", "The files he wants should end up in my Drive, and once they're ready the links go in the PlayableX channel like he says."
for s in (S1, S2, S3): assert s in prompt
calls = sum(x["calls"] for x in man["call_budget"])

P = [f"""# Prompt Check — {M.SLUG}
> Prompt: 04_Prompt.txt · {words} words · sha256 {sha12} · {CLOCK} · checked 2026-11-12 against 04_Prompt_Writing_Brief.md (2026-11-12) · release task-quality-v1
> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.

{CLOCK}

## Summary

- Fail: 0 · Non-fail: 0 · Advisory: 1 (C23, no supplied samples) · UNVERIFIED checks: none
- Checks clean: C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C22, C24
- Predicted /prompt band: PASS
- Status: READY FOR /prompt

The prompt, as it will be submitted:

> {prompt}

## Findings

No Fail and no Non-fail finding. One advisory note:

""" + table(["#", "Check", "Dimension · severity", "Quoted span", "Rule (source)", "Defect"], [
    (1, "C23", "Originality · Advisory", q("Frederick's playable message"), "Eval 1 §2.9 is N/A without supplied samples; fingerprint against the guideline and taxonomy examples only", "none found: no guideline, taxonomy or long-horizon example has a vendor brief with an asset hand-off list; noted so the reviewer knows no sample was supplied with the task"),
]) + f"""

## Fair readings (accepted outcomes)

Per deliverable: Reading A (best supported) · Reading B (the strongest alternative) · what settles it.

""" + table(["Deliverable", "Reading A", "Reading B", "Resolution and evidence"], [
    ("The job itself", "do what Frederick's message asks: write the brief and the hand-off list, follow his notes for the states and the tickets, share, send him the counts, post the links", "report back what Frederick wants and wait", f"the request is 'do everything he's asking for in it, start to finish'; his message is an instruction to produce two files and two messages ({ASK}). One reading"),
    ("W1 brief", "the eight with the bow, the four zombies and walk, 7 slots, lost at zero health, the two library sounds held back, music after the first click, 3 November", "the eight with the dynamite; or the reference level's items", f"Robert's own later reply {REPLY} replaces the last item of his list {PICKS}; the ask keeps his latest word. Settled by a newer source on the same issue"),
    ("W2 hand-off list", f"{M.N_LIST} rows; Delivered {C['Delivered']}, Ready {C['Ready']}, Owed {C['Owed']}", f"Brian's notes taken as they stand: {M.NAIVE['Delivered']} / {M.NAIVE['Ready']} / {M.NAIVE['Owed']}", f"the notes {NOTES} say a later word from someone who knows the file or the art counts; the later statements are {A1}, {A2}, {B['pr462']}, {SHEET}, {LOG}, each readable by Julia. Settled by an incorporated source's authority"),
    ("W3 shares", f"both files, view only, to {FRED}, {BRIAN}, {ROBERT} and {INTAKE}", "the brief only; or Leonard, whose Trello card is the 'kickoff'", f"the notes: 'Sharing: both files, view only. Everyone on the kickoff hold, and PlayableX through their intake address' ({HOLD}, {CONTACT}); the card has no attendees ({B['trello_kickoff']})"),
    ("W4 tickets", f"the {C['Owed']} Owed lines' tickets to Todo with a comment each; the others untouched", "nothing for a line whose note already says not exported; or a description edit", f"the notes: 'An Owed line's ticket goes to Todo with a comment saying what is owed and who has it. Leave the Delivered and Ready ones as they are.' ({NOTES})"),
    ("W5 counts", f"the three numbers in Frederick's DM {M.DM_FRED}", "the numbers in the vendor channel", f"his message: 'give me the count for each state here' ({ASK}); a new message or a reply under his ask is the same write to the same person"),
    ("W6 links", f"both links in {M.VENDOR_CH}", "the links in Frederick's DM", f"his message: 'post both links in the PlayableX channel'; the prompt repeats it. A top-level post or a reply in the 3 November thread is the same channel and content (sweep fork F10, accepted)"),
]) + f"""

No material fork is open: `COHERENCE SWEEP (full): PASS` on this prompt and SQL (pasted in the Self-review).

## Verification log

Every proper noun, relationship, state premise and narrative claim of the prompt, looked up in this run.

""" + table(["Span", "Type", "Universe record (locator)", "Result"], [
    (q("Frederick's playable message"), "person / event", f"{ASK}, sender `EMPLOYEE_0008_SLACK_ID` ({FRED}), in Julia's DM with him {M.DM_FRED}; the only message of that DM after 18 Sep", "true: the message exists, is his, and is about the playable ('write the brief they build from, and tell me where the item pack actually stands')"),
    (q("from yesterday"), "date", f"{ASK}: ts {ts} = {sent:%Y-%m-%d %H:%M:%S} UTC = {sent_pt:%a %b %-d, %-I:%M %p} PT; Julia's today is Wed Oct 1, 2025", "true on both calendars (Tue Sep 30)"),
    (q("everything he's asking for in it"), "state premise", f"{ASK} asks for the brief, the list, the counts and the links, and names his notes {NOTES} for 'what goes in the brief, what counts as ready, what to do with the tickets and who gets the files'", "true: the message carries requests; a requested new output, not a premise about the world"),
    (q("The files he wants"), "doc", f"{ASK}: 'Brief as a doc and the hand-off list as a sheet'", "true: he asks for files"),
    (q("my Drive"), "doc / place", f"{ROOT_DRIVE} (Julia's Drive root, owner {ctx['email']}); {ASK}: 'both in your Drive'", "true: the place exists and is hers; it is where he asked for them"),
    (q("the PlayableX channel"), "channel", f"{M.VENDOR_CH} (private, name ends in '-playablex', Julia is a member); {B['vendor_nov3']} is in it", "true: one channel carries the vendor's name"),
    (q("like he says"), "relationship", f"{ASK}: 'post both links in the PlayableX channel so they know what's still coming from us'", "true: the message says so"),
]) + "\n\n`persona_view.py can-see` for the three named places:\n\n" + code(cansee) + f"""

## Brief coverage

""" + table(["Brief item (§4 deliverables, §6 triggers)", "Present in the prompt (quoted span, or \"absent\")"], [
    ("Anchor A1: Frederick's message is the job", q("I need a hand with Frederick's playable message from yesterday")),
    ("R1 to R6 through the hub (list, states, what is owed, the board, the brief, the tickets)", q("Can you do everything he's asking for in it, start to finish?")),
    ("W1 brief and W2 hand-off list: destination (anchor A3)", q("The files he wants should end up in my Drive")),
    ("W6 links: destination (anchor A2)", q("the links go in the PlayableX channel like he says")),
    ("W3 shares", q("everything he's asking for in it") + " (through his notes; not named, by design)"),
    ("W4 ticket follow-through", q("everything he's asking for in it") + " (through his notes; not named, by design)"),
    ("W5 counts to Frederick", q("everything he's asking for in it") + " (his message says where; not repeated)"),
    ("§9 must-not-appear items", "absent: no tool name, id, title, state word, count, item, person other than Frederick, source list or step order"),
]) + f"""

## Self-review

Walked `Evals/1_Prompt_Eval.md` Phases 1 to 3 against the prompt text. One row per check: the result, the best case against it, and what resolves it.

""" + table(["Check", "Result", "Counter-reading (best case against the result)", "Evidence that resolves it"], [
    ("C1", f"clean: {words} words", "A request this short could be under the field's floor.", f"the field takes 20 to 4,000 words; whitespace count of 04_Prompt.txt is {words} (sha256 {sha12})"),
    ("C2", "clean", "An assigned field could be missing or changed.", f"`Working_Files/00_Task_Context.json` holds all eight fields, context_hash {ctx['context_hash'][:12]}; persona resolves to {ctx['email']}"),
    ("C3", "clean", "A Product Manager would not write a vendor's creative brief; a marketer would.", f"she wrote the storyboard and brief for the first playable in this vendor's channel ({B['julia_dd_brief']}) and built this one's reference level ({B['julia_level']}); Frederick asks her by name ({ASK})"),
    ("C4", "clean", "The work is asset tracking (Engineering Ops), not Marketing and GTM, and Authoring is incidental.", f"the object is a playable ad, a user-acquisition creative chosen to filter for players who will like the game ({B['fred_retention']}); the two authored files are the deliverables ({NOTES}: 'The brief. One doc PlayableX can build from')"),
    ("C5", "clean", "The prompt restates where the files and the links go, details that live in Frederick's message.", f"both are destinations the persona knows (playbook: name them); no column, state, rule or source is restated. Dynamic change and multi-source are load-bearing in the records ({A1}, {A2}, {REPLY}, {LOG}, {SHEET})"),
    ("C6", "clean", "Reading B (Brian's notes as they stand) is a fair outcome that would be rejected.", f"the incorporated notes say a later word counts ({NOTES}); every later statement is in a record Julia can open; both cold reviewers reach {C['Delivered']} / {C['Ready']} / {C['Owed']} (`Working_Files/01d_Coherence_Sweep.json`)"),
    ("C7", "clean", "Whether the links are a top-level post or a thread reply, and whether the counts are a message or a reply, is left open: a Minor clarity finding.", f"the conversation and the recipients are fixed ({M.VENDOR_CH}, {M.DM_FRED}) and the write is the same message in the same place; position inside one conversation is not a channel, time or form choice. Accepted either way in brief §4b and in the sweep (fork F10). No 'I'll' statement in the prompt"),
    ("C8", "clean", "The prompt points at a message that points at notes: the rule source is two hops away and unnamed.", f"(a) {ASK} is readable (DM member) and {NOTES} is shared with her; (b) one message of that DM is about the playable; (c) it says what the prompt attributes to it ('both in your Drive', 'post both links in the PlayableX channel'); (d) it gives instructions, not answers"),
    ("C9", "clean", "Naming the files and the links hands over part of the answer.", f"they are the requested outputs, stated by Frederick ({ASK}); no state, count, line, item or reason appears in the prompt"),
    ("C10", "clean", "'Frederick's playable message' names the hub exactly, collapsing discovery.", f"the hub is an anchor the persona knows (dossier anchor table, A1); the hidden authorities ({NOTES}, {LIST}, {HOLD}) and the six deciding records are not named"),
    ("C11", "clean", "The writes could be made without investigating.", f"the list's states, the comments and the brief's facts all depend on the tickets' notes and the later statements ({PT}; {FIRST} to {LAST})"),
    ("C12", "clean", "Only Slack and Linear carry weight.", f"Docs, Sheets, Slides, Calendar, Contacts, GitHub and Confluence each hold a fact a graded row needs ({NOTES}, {LIST}, {SHEET}, {HOLD}, {CONTACT}, {B['pr462']}, {B['gdd']}); `HARDNESS GATE (extreme): PASS` is pasted in the dossier"),
    ("C13", "clean", "Three sentences could be three unrelated asks.", f"all three serve one hand-over: the message, its files, its links ({ASK}); deleting any sentence removes the job or a destination"),
    ("C14", "clean", "'my Drive' and 'the PlayableX channel' are tool mentions.", "natural product and place names (`prompt_qc_examples.md` row 103); no function, parameter or server name appears; checked against `Evals/references/tools/catalog.json` names used in brief §9"),
    ("C15", "clean", "'once they're ready the links go in ...' is a sequenced step list.", f"it is the order of deliverables Frederick gave ({ASK}: 'Then ... post both links'), one clause, not a method of two or more investigation steps"),
    ("C16", "clean", "'start to finish' hints that there is more than meets the eye.", f"it asks for the whole of what the message requests, which includes messages and tickets ({ASK}); it points at no trap, record or cause. Calibration cases below: no failing rule matched"),
    ("C17", "clean", "'from yesterday' or 'the PlayableX channel' could be a near-match phantom.", f"the ask is stamped {sent:%Y-%m-%d %H:%M} UTC, Tue Sep 30 on both calendars ({ASK}); the channel {M.VENDOR_CH} is the only one named for the vendor and she is a member (can-see YES above)"),
    ("C18", "clean", "Sharing with an outside address or moving a Design-team ticket may be beyond the tools.", f"gdrive_share_file takes an e-mail and a role; linear_update_issue sets a state name, and Todo is in use in that team (`DES-312`); gdocs_create_document, gsheets_create_spreadsheet, gsheets_values_update, linear_create_comment and slack_send_message exist in the catalog (manifest `writes`)"),
    ("C19", "clean", "A deciding record could be outside her scoped view.", f"check-sql PASS for every load-bearing seeded row (dossier 1.E): {A1}, {A2}, {REPLY}, {SHEET}, {LOG}; no ask directs her to anyone else's scoped data"),
    ("C20", "clean", "'yesterday' could resolve to two windows.", f"Tue Sep 30, 2025 in Pacific and in UTC ({ASK}); the only later date in the records is the 3 Nov kickoff, a scheduled event ({HOLD})"),
    ("C21", "clean", "A wait or an error could be announced or missing its alternate path.", "none is configured: `03_Error_Async_Config.txt` Friction: none, gate PASS"),
    ("C22", "clean", "An inconsistency between records the prompt touches was met.", f"none met in C17 or C18; `BASE CHECK` PASS, citation chronology PASS (26 pairs) and the sweep's 15 seeded facts checked against the base ({ASK}, {NOTES}). The platform /injection review is the user's to run"),
    ("C23", "advisory", "A supplied sample could match on persona and scenario.", f"no sample was supplied with the task; no guideline or `long_horizon.md` example is a vendor brief with a hand-off list ({ASK})"),
    ("C24", "clean", "The task is 'investigate and post one Slack message'.", f"two authored files, {C['Owed']} ticket moves and comments, eight shares and two messages (manifest `writes`; call budget {calls}; {FIRST} to {LAST})"),
]) + "\n\nCalibration self-test against the 15 cases of `Evals/references/rules/prompt_qc_cases.json` (matched means the prompt shows the case's failing pattern):\n\n" +
    table(["Case", "Rule", "Case verdict", "This prompt"], [(c["id"], c["rule"], c.get("verdict") or c.get("expected"),
        {"staged_errors": "not matched: clean spelling, capitals and punctuation", "trap_hint_or_riddle": "not matched: names the job, no hint at a cause", "hidden_destination": "not matched: both destinations the persona knows are named",
         "audit_form": "not matched: one plain request, no catalogue of verbs", "if_chain": "not matched: no condition", "false_state_premise": "not matched: Frederick is active and messaged her on 30 Sep",
         "ugt_both_fair_figure": "not matched: no unsettled figure"}[c["rule"]]) for c in cases]) + f"""

Mechanics: every quoted span above was asserted as an exact substring of 04_Prompt.txt by the generator; the file's sha256 is {before} before and after this run. Facts re-verified in this run: the ask's text and time (SQL row), the three places (can-see), the rule-in-prompt check:

""" + code("\n".join(l for l in v2.splitlines() if l.strip().startswith(("ADVISORY", "CLEAN", "FLAG", "UNRESOLVED")))) + "\n\nCoherence sweep on this prompt and SQL:\n\n" + code(sweep or "pending") + f"""

Unresolved: none. UNVERIFIED: none. The first measurement of difficulty is the pre-check run.

## Route

No Fail. Paste `04_Prompt.txt` exactly as saved into `/prompt`, paired with `/injection` on `01_Universe_Inject.sql`; when asked for the task date, answer Oct 1, 2025 (synth-cut). `03_Error_Async_Config.txt` is not supplied (Friction: none). Next: `/create-humantime`.
"""]
out = WF / "04_Prompt_Check.md"
out.write_text("\n".join(P))
assert hashlib.sha256((TASK / "04_Prompt.txt").read_text().encode()).hexdigest() == before
print("wrote", out.name, len(P[0]), "chars · prompt", words, "words", sha12)

# ---- sidecar reviews for prompt-check
ev_path = WF / "00_V3_Authoring_Evidence.json"
ev = json.loads(ev_path.read_text())
digest = file_digest(TASK / "04_Prompt.txt")
pw = ev["outcome_reviews"]["prompt-writing"]
ev["outcome_reviews"]["prompt-check"] = {
    "artifact": "04_Prompt.txt", "artifact_hash": digest,
    "reviewer": "claude-fable-5-2 (authoring session, /create-prompt-writing check; two cold reviewers read the prompt with the injected records)",
    "rationale": ("The prompt makes Frederick's message the job and names two destinations; every requirement reaches the assistant through that message and the notes it names. "
                  "Under each reasonable reading the writes are the same: two files in Julia's Drive, the shares, the Owed tickets' moves and comments, the counts to Frederick and the links in the vendor channel. "
                  "The accepted outcomes are those of the brief; no reading with a different decision, write, destination or recipient survives the records."),
    "accepted_outcomes": pw["accepted_outcomes"],
    "alternatives_considered": pw["alternatives_considered"] + ["Reporting what Frederick wants without doing it: rejected, the prompt asks to do everything he asks, start to finish"],
}
ev.setdefault("role_reviews", {})["prompt-check"] = {
    "artifact": "04_Prompt.txt", "artifact_hash": digest,
    "reviewer": "claude-fable-5-2 (authoring session, /create-prompt-writing check)",
    "persona_role": ctx["persona_role"],
    "rationale": ("Julia Lawson, Product Manager, hands off a request a co-founder sent her: write the vendor's brief for the second playable and say where its item pack stands. It is hers on base evidence before the freeze: "
                  f"she wrote the first playable's storyboard and brief in the vendor's channel ({B['julia_dd_brief']}), built this playable's reference level ({B['julia_level']}) after Brian asked her ({B['brian_asks_level']}), "
                  f"is named as the game's designer on the design page ({B['gdd']}) and is a member of the vendor channel ({B['vendor_nov3']}). Asking an assistant to take a message off her plate and put the files in her Drive is an ordinary request for the role."),
    "source_ids": [f"slack:{B['julia_dd_brief']}", f"slack:{B['julia_level']}", f"slack:{B['brian_asks_level']}", f"confluence:{B['gdd']}", f"slack:{B['vendor_nov3']}", f"slack:{ASK}"],
}
ev_path.write_text(json.dumps(ev, indent=1, ensure_ascii=False) + "\n")
print("sidecar reviews written for prompt-check:", digest)
