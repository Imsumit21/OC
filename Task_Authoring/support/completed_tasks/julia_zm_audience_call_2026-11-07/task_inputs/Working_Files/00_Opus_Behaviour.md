# Opus 5.5 behaviour on HarmonyGames tasks (from stored runs)

Evidence only. Companion to `00_Carrier_Calibration.md`; rates there are not repeated here.

## Corpus and limits
- 30 baseline runs, 5 tasks: D Douglas, H Frederick handover, C Frederick card spend, J Julia, B Robert. Citation `J r6#892` = run 6, event 892 (0-based export index). `J-hard r6` = `eval_reports/1a_hardness_NONFAIL_r6.md`.
- Weighted pass (12_difficulty_input.json): D 52/71/45/52/74/45; H 72/60/64/93/100/96; C 75/79/79/79/70/88; J 68/77/100/83/88/87; B 86/85/87/82/92/83.
- All 1,251 thinking blocks are empty. Every "why" below is read from narration, tool inputs and briefs, so reasons are inferred.
- Five tasks only, and they all went through hardening. Anything from one task is marked; "one-off" means seen once.

## Q1 Opening moves
- Slack-asked tasks open the same way. D, H, J: `slack_read_user_profile`, `slack_search_users(name)`, `slack_read_channel(user id)` in 17/18 runs (J r3 puts a Slack search first). B: `slack_search_channels` and the profile in one turn, 5/6 (B r6#2 passes `#winddown` directly).
- Mail-asked task: C opens with `gmail_search_messages from:leonard after:...` using the prompt's date, 6/6, then a batch fetch, then Bash base64 decode (C r1#10, C r2#7).
- The ask is read by call 3 (call 2 in C). No run starts by browsing folders or writing a plan. Narration is one line ("Now the Trello card.", J r3#15).
- Route is ask, then the rule carrier the ask names, then what the rule names. First main-thread call by service, min-max over 6 runs:
  - D: trello 6, confluence 8-10, gdrive 10-15, github 20-23, linear 20-24
  - H: trello 5-7, gdrive 8-13, gmail 30-54, snowflake 30-58
  - J: trello 6-11, gcal 11-20, gmail 12-21, gdrive 13-18, linear 29-34, github 34-52
  - B: linear 8-9, gdrive 8-10, gmail 21-48
  - C: gdrive 4-10, snowflake 14-38, trello 35-542, linear 37-543, slack 52-552
- Named sources are reached within about 25 calls. Unnamed services come late or never: B gcal, github and snowflake 1/6 each; C trello and slack come as late as call 540+.
- Bulk starts once the list is known: H reads 14 sheets back to back from about call 14 (H r1#26); B reads 28 issues' comments from about call 17 (B r2#48).
- The Leonard mail in D's prompt: 4 runs read it early, 2 just before writing (D r2#329, D r5#573). See Q8.

## Q2 Delegation
- When: spawned in D 5/6, H 1/6, C 5/6, J 6/6, B 0/6, 140 spawns in all. It fires after the list is enumerated and looks large: 70-odd D tickets, 496 C sheets, about 500 J tickets. It did not fire for 28 B issues, nor for 14 H sheets except H r6#93. D r2 did 74 comment reads inline and scored 71.
- Brief shape: 120-2,600 chars, "Read-only" first, exact tool name, explicit id list or range, a reply format, "be exhaustive". C r6#346 is 121 chars pointing at a prompt file (one-off).
- Briefs omit the task goal and the rule text. J scans reduce the rule to literal words: `tiers`, `replac`, `supersed` (J r2#159, J r4#1084); J r5#176 has the widest filter. Only "matches" come back, so a differently worded fact never returns.
- Briefs also fix the endpoints. D r1#76 names issue comments, reviews and timeline. Only D r3#84 of the D GitHub briefs names inline comments. J r2#2241 asks for reviews on 477 PRs and not inline comments.
- Failure, by `model` parameter: none set 72 spawns = 55 failed, 16 stopped by parent, 1 completed. `sonnet`/`haiku` set 68 spawns = 68 completed. All 55 failures are one error, "Autocompact is thrashing".
- This looks like a harness effect, not task difficulty. Subagents start at about 220k tokens (J r2, J r4, J r5, C r4, C r5, D r4) and modelUsage lists a 200,000 window for plain opus. Explicit-model subagents log model `claude-opus-5-5` and peak at 603,863 (J r2) and 659,994 (C r4), so they appear to get the 1M window whatever was requested. Inferred from usage fields, not proven.
- Smaller batches did not save unset-model agents: J r3#1035 (10 calls) and J r5#1094 (15-20 calls) still failed. J r3#1307 concluded "the agents' overhead is the problem".
- Loss: no main thread read a failed agent's `.output` file (0/30). Text findings die with the agent. Agents that wrote files kept their work (C r1#640 "70 files are saved").
- Reactions: redo it myself, priority slice first, then widen (J r1#966 to #1159, J r2#676, J r4#860); redo in batches (D r3#254, D r4#223, D r6#290); respawn with explicit model and tight brief (J r2#907, J r4#1084, C r1#646, the fix that worked); narrow and stop (J r6#892).
- What was lost, by case:
  - J r6#892 limited the direct sweep to Blake-assigned tickets; ZOM-281 was never read, by anyone.
  - J-hard r6 F1: batch E had the ZOM-281 note; the parent stopped it (#2666) and never collected it.
  - J-hard r7 F1: a subagent read #271 "not tiers" (#2380) and failed; the parent went on without the one repeat call.
  - D r3: inline comments read in the agent (#152, #191), agent failed (#248); the main redo made 34 GitHub reads, none inline.
  - Recovered: J r3 and J r5 failed agents read ZOM-281 (#1230, #855) and the main sweep re-read it (#1935, #2283).
- Hand-back trust: completed findings are taken as given. J r2 and J r4 never re-read ZOM-281 in main (#1763, #1410 subagent only); "Batch A came back clean" (J r2#1679). C checks by file counts and ledger tie-out.
- One-off: H r6#255 wrote a `<task-notification>` with a full invented receipts result as its own text while the agent was still running. It then spot-checked (#259), redid the work itself (#297), and the real agent failed at #361.

## Q3 Overflow and parsing
- Spills by tool: gdrive_list_folder 29, github_list_pull_requests 23, slack_read_channel 22, linear_list_issues 12, gdrive_search 12, PR reviews 8. A default 100-message Slack read is 77-82k chars and spills at call 3 (D r1#6, J r1#6, B r1#6).
- The notice says read the file in sequential chunks. No run did; 1 Read of a spill file in 30 runs (C r4). 26/30 try `jq` first (not installed, D r1#8), then a python one-liner printing chosen fields (D r1#10).
- Fields printed from the 22 Slack spills: ts, user, text always; `reply_count` 19/22 (dropped J r1, r2, r4); `thread_ts` 3/22; `latest_reply` 0/22; `has_more` value 4/22 at first parse (J r2, B r1, B r4, B r5), later B r3#288, B r6#196. `print(d.keys())` shows the key without the value (D r1#10).
- Dropping `reply_count` tracked the J outcome exactly. Kept or seen raw: r5, r6, and r3 (limit=30, no spill, #8) opened both DM threads. Dropped: r2 and r4 reached only the ask thread through a Slack search (J r2#65-67, J r4#40-44); r1 reached neither. J-hard r5 F1 is the same mechanism. One task, n=6.
- Whether the field is kept is an unprompted choice in a throwaway script; the same script shape varies run to run with no visible cause.
- For unfamiliar shapes it prints one item first to learn the schema (J r5#98). Truncation in scripts (`[:3000]` J r1#10, `[:400]` D r3#57) cut nothing that mattered that I saw.
- Paging, non-spilled results flagged more / followed by a same-tool page call within 60 calls: gmail_search 58/0; slack_search 13/2; slack_read_channel 12/6; linear_list_issues 5/4; github_list_pull_requests 4/1; gdrive_search 3/1.
- So enumerations get paged (C r2#46-52 folder offsets, linear cursors). Search results are never paged in Gmail: it writes another query instead.
- Channel history: #winddown paged in 5/6 B runs, mostly mid-run; B r2 never. D 0/6. J r2 printed `has_more` true and did not page.

## Q4 Search habits
- Key is the entity: vendor, account id, ticket or topic words. Person only for the sender of the ask or a rule owner: `from:leonard` D 6/6, `from:arthur.blake...` J 6/6. Date is usually a filter added to entity terms (`after:2025/08/20 (waive OR ...)`, H r1#94); bare date listing is rare (B r6#56).
- Volume follows the task: Gmail queries per run D 1, J 2-3, C 4-9, H 8-14, B 11-25. Slack search 0-8.
- Shape: `OR` bundles of 4-10 vendors first, then single-vendor queries for what stays open (B r1 list: `Pond5 OR ElevenLabs` then `from:elevenlabs`, `from:pond5`). Aliases come only after a hit shows them (`bizxpress`, B r5#248).
- Listed vs opened: Gmail search gives ids only. Touched D 1 of 10-100, H 19-61 of 115-362, C 12-30 of 99-284, B 48-77 of 306-522. About 10-33%, and "touched" includes snippet-only fetches.
- Triage: `get_messages_batch format=minimal` is common (B r2 61 ids, B r5 56, H r2 28). Minimal returns id, labels, snippet, date, size, with no Subject or From (H r2#174). A notice whose snippet is a URL looks like nothing.
- Selection also seems to use the sender domain visible in the message id (H r6#220 lists ids by domain). Inferred.
- Zero-hit searches, main thread, zero of total: confluence 11/18, github PR 21/49, gmail 18/203, gdrive 13/84, slack 10/85. A retry sharing a word follows about half (confluence 6, github 17, gmail 12, gdrive 5, slack 2).
- Normally one retry, then it changes service or moves on: D retries a zero-hit `title ~ "ZM Beta"` with a text or bare query in 6/6; H confluence `money moving` got no retry (H r3#128, H r5#136).
- Channels: it reads the ask's channel and almost nothing else. Distinct channels read per run: D 1, C 1, H 1-2, J 2-3, B 1 except B r5 (3).

## Q5 Stop rules
- Explicit moments: "I have everything I need" H r1#191, B r1#368, B r4#299, B r5#392, J r5#2902; "All inputs gathered" J r1#1701.
- Three triggers:
  - List exhausted: D r6#462 "All 67 tickets checked", J r3#2231, J r4#2384.
  - Numeric tie-out: C r3#1497, C r5#1925 "ties to the ledger to the cent ... so the extracted data is complete".
  - Last named check done: J r2#3814, H r2#225, H r3#247.
- Coverage audits count items, not surfaces. Bash set-difference audits appear only in C and J (0-2 per run), none in D, H or B.
- J r2#3846 declares "No 'not tiers' review exists on any PR" after 477 review reads and 0 inline reads. The sweep was complete on the wrong endpoint. A tie-out equally says nothing about what the ledger cannot see (C run-rate prices).
- Pre-write rechecks are narrow and name items it already doubted: J r3#2307 ZOM-263, J r5#2852 four statuses, H r2#225 ledger, C r4#2124 found its own sort bug. I saw no run reopen a settled row.
- It proceeds past a known failed check (J-hard r7 F1). Final replies carry a caveat in about 21/30 (crude regex), for example D r3 "One judgement call" on ZOM-461.

## Q6 Authority handling
- Usual case: a later message from the rule owner is applied at once and narrated. H r2#183 "Arthur emailed an override"; C r6#481 "Leonard changed the cut list"; J r2#3919 Blake's reply beats build and write-ups; D r6#512 tells the user two earlier statements were wrong.
- The 6 surfaced-but-unapplied cases in the calibration file split three ways; only 2 are true read-and-not-applied:

case | what happened | why
--- | --- | ---
D r3 x2 (inline #38, #39) | Text only inside a failed subagent (#152, #191); 0 main inline calls | Never reached main. Lost at hand-back, not an authority decision
H r2, H r6 (AdMob mail) | Fetched `minimal` (H r2#174, H r6#317); snippet is a URL, no subject | Never readable. Triage miss. H r3 listed it only, H r4 never. H r1, H r5 used default format and applied it (H r1#216, H r5#288)
B r1, B r5 (Slack Feb 11) | Read on page 2 (B r1#199, B r5#164) and Sunset's request also read | Reasoned down: "Not a clash, just worth checking" (B r1#481); "Worth a check ... We're still paid, so history is fine" (B r5#513)

- The B pattern: it tests whether harm has already happened rather than decision against request, and picks a softer label. B r3, B r4, B r6 with the same evidence named the clash. B r2 never saw it. One task, 2 runs.
- Related (D r4#542, D r5#656, D r1#517): dev-only imports with no linked ticket are reported as unattributed instead of chased. Evidence that fits no row goes into a note.

## Q7 Writes
- Read everything, then write everything. First write falls at 73-78% of events in B, 82-92% D, 87-94% H, 95-98% C and J.
- Order: create sheet, fill, move, share, ticket states, ticket comments, reply. The reply or mail is the last write in 30/30. Variants are minor (B r6 comments before states; D r2 interleaves).
- Reads after the first write: 0-2 per run, 0 in 13/30. Most are lookups (`linear_list_issue_statuses`, `trello_search` for the card id). True sheet read-backs in about 10 runs, one call each (B r2#384, C r1, D r1).
- So no run went back to investigate after writing started, and new evidence had no chance to arrive.
- Write errors: only one kind in 30 runs, `gdrive_move_file` 404 on the Wind Down folder, B 6/6 (B r1#388). No retry, no folder lookup; it leaves the file in My Drive and says so (B r1#395, B r5#426). Friction was configured "none", so this is an environment quirk.
- Late corrections go out as new messages, not edits: D r4#534-535 corrects a name in a follow-up DM; C r1#2725 mails a subtotal correction after noticing a $1 slip. Two cases.
- Fix-ups before moving on: B r2#382 repairs a total formula and reads it back; B r5#414-419 creates ENG-2467 for an uncovered account and back-fills the cell (one-off).

## Q8 Variation
- Fixed across runs: opening, route to named sources, read-then-write, order of writes, reply last. Variable: effort and a few small choices.
- Effort does not track score. J r3 895 calls 100; J r2 1,266 calls 77; J r6 386 calls 87. C cost about $10 (r2) to $41 (r1) for 79 and 75.

choice point | split | effect
--- | --- | ---
Parse script keeps `reply_count` (J) | r3, r5, r6 vs r1, r2, r4 | Second DM reply; runs 3, 5, 6 got it
Leonard mail read as thread or message (D) | r2, r5 thread vs r1, r3, r4, r6 message | Reply-all; 71, 74 vs 45-52. The 4 early readers all used get_message; the 2 late readers both used get_thread
Gmail fetch format (H) | r1, r5 default vs r2, r3, r4, r6 minimal | AdMob row. r5 scored 100; r1 72 lost marks elsewhere (no tab listing)
Comment sweep after agent failure (J) | r6 narrowed vs others widened | ZOM-281; register sizes r1 33, r2 29, r3 23, r4 27, r6 22 tickets narrated
PR endpoint (J) | inline calls r2 0, r1 1, r5 1 vs r3 4, r4 5, r6 9 | "not tiers" exclusions
Open threads vs read listings (C) | r6 opened the listed threads (6 thread calls); others 0-4 | Forwards; r6 88 vs 70-79
Page the named channel (B) | r2 no vs the rest | Feb 11 decision reachable
Clash label (B) | r1, r5 soften vs r3, r4, r6 | Judgement on identical evidence
Enter an unnamed channel (B) | r5 only | Unity note; r5 92

- Subagent luck is real but runtime-driven: explicit `model` on the respawn decided whether the scan finished by agents or by hand. C r4 and C r5 set a model from the start and had no failures.

## Q9 Fair design implications
Each needs a working path for a careful person. "Works with" is what the stored runs suggest, not a tested guarantee.

1. **Own-script parse of a spilled read.** A correction as a thread reply under a parent the ask did not name, in the ask's own channel; the marker sits in the saved JSON. Unfair: no marker, or depending on `jq` missing.
2. **Mail triage on snippets.** A notice from a vendor the task covers, ordinary automated format, subject carrying the fact and a boilerplate snippet. Unfair: a mail no sensible vendor query returns, or a sole path past Gmail page 1 (58/0 paged).
3. **Endpoint fixed early.** Facts in inline review comments where the rule says "his review notes". Rely on the direct read; GitHub search does not index them (J-hard r7). Unfair: requiring the search to find them, or a rule that never implies review text.
4. **Literal keyword scans.** State the fact in plain language the rule still covers, so a `tiers|replac` filter misses a variant. Unfair: a rule that requires a word that appears nowhere, or a meaning a reader could dispute.
5. **Priority slices.** The rule says "whoever the assignee is"; place one qualifying record on a ticket outside the obvious owner's set. It must hold when agents succeed: J r2 and J r4 caught ZOM-281 with working agents.
6. **Stop at a clean tie-out or full count.** Make the wrong answer tie out: a forward price, a status or a change the ledger cannot show, with the rule asking for it. Unfair: totals that cannot be reconciled at all.
7. **Soft labels on a judgement.** Ask for a binary label with a stated test ("a decision that goes against a request is a clash"). Grades B r1 and B r5 type softening. Unfair: a test open to two readings; then the hedge is right.
8. **Reads only the channels it is pointed at.** A decisive note in a second channel that a named person or ticket points to indirectly. Pointer must exist. 1/6 reached #executives with no pointer, which is close to unreachable.
9. **Depth of a named channel.** A decision on page 2 of the channel the ask names; 5/6 paged it, a good partial splitter. Only for named channels. Page 3+ of an unnamed channel is unfair.
10. **Read-then-write with one late look.** One hidden fact that must move register, ticket and reply together, so outputs compound. Do not build on a late-arriving correction or on re-reading after a write: no run does that, and it would measure nothing.

Never count on, because they are tool or harness failures: subagent autocompact failure, `jq` absence, the B move 404, overflow notice wording. A design that scores only because agents die will change with the harness: explicit-model agents completed 68/68. The parent's choices after a failure are fair to grade, as the J-hard reports do. Volume is not a lever (Q8).
