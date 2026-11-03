# Human Time Worksheet — frederick_bridge_pipeline

Pass: first        Tier: Long-Horizon
Universe: synth-cut · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Hours: 19.25

Prompt: 04_Prompt.txt (sha256 cecfad824fd8) · SQL: 01_Universe_Inject.sql (sha256 3ba2b413458f, rev5; platform /injection and /prompt PASS) · persona: frederick_stone · persona "today" Wed Oct 1, 2025; status window Sep 3 to Sep 30, 2025 PT
Friction: none (03_Error_Async_Config.txt), so there are no workaround lines. No reference files are attached.

## Sub-tasks

Manual effort only: Frederick opens the records himself, one by one, with no search tool and no AI, and classifies each firm by hand against Leonard's template. Volumes are what Frederick can see. For the scoped services that means his mailbox, his own calendar, the two channels he belongs to and the Drive files shared with him. Linear, Trello and Contacts are unscoped.

| # | Sub-task | Kind | Volume (measured, persona view) | Rate | Minutes |
|---|---|---|---|---|---|
| 1 | Read Leonard's Sep 30 ask, and Robert's Sep 29 "email the pipeline to the board" mail that the ask overrules (D5) | read | 2 threads, 1 message each (frederick.stone@harmonygames.co/1844724419788800011, frederick.stone@harmonygames.co/1844623441920000059) | decisive thread read past its first answer ≈ 20 min (LH §4) | 20 |
| 2 | Read the Oct 14 template's rules and the folder README; find the Board - Oct 14 2025 folder | read | template f_3b9e61c04d7a52e8f1a6c2 (3,018-character body, 4 sections: who goes in, status buckets, money, build access) + README f_c61a0e93b7d24f58a2e917 (285 characters) + folder d_5e8a1c3f9b07d2e64a1b93 | decisive document ≈ 20 min (LH §4) + 5 min for the README and folder | 25 |
| 3 | Rule out the July template (committed = verbal yes, trap T9) and the internal investor list (D1) | dead end | 1 doc f_8d2c47a91e05b3f6d7c418 (432 characters) + 1 sheet f_0b29566cd7932a205d54d2 (Frederick can see 2 investor lists, persona_view gsheets "Investor List") | 5 min each: open it, check the date and title against the ask, set it aside | 10 |
| 4 | Read the two Trello cards Leonard names: Board Deck - Oct 14 (comment + Sections checklist) and Existing Investor Update (the Keep warm comment, trap T8) | read | 2 cards (68d8193cf451863621c88a2a, 68c5a49e8491a9d7faf869d0), 2 comments (68d81f30a6c94e2b7d05e1f4, 68c64270d660c977c4696986), 4 check items | 15 min: two short comments, below the 20 min decisive-thread anchor because each is 2–3 sentences | 15 |
| 5 | Rule out the April "Investor Update" card (D6) | dead end | 1 card 663ea0fc3f231e879cefd5e8 (4 actions) | 5 min | 5 |
| 6 | Open the draft deck to see what the fundraising slide needs | read | 12 slides (f_a47d0e2c95b18f63e2c0d5), 1 fundraising slide with 3 blanks | 10 min: 12 short slides | 10 |
| 7 | Go through the 2025 investor list: merge repeated names and read the 09/11 Latest Status notes | read | 80 rows, 77 distinct firms, 23 Latest Status notes, 17 used columns (gsheets data.json /sheets_spreadsheets/96, f_48247af79428823c3cac92) | triage a listing ≈ 450 rows/h (V1) = 11 min + classify one note ≈ 2 min (V1) × 23 = 46 | 57 |
| 8 | Read #bridge-pitch from Sep 3 to Sep 30 in full, with its replied threads | read | 406 messages (399 base + 7 seeded; 8,370 words in the base messages) + 7 replied threads with 19 replies (C096HFA5Z8W) | slower than the 3,000/h skim anchor because any line can decide a firm: ≈ 600 messages/h (≈ 200 words/min) = 41 min + 7 threads × 2 min | 55 |
| 9 | Skim #executives from Sep 3 to Sep 30 and open its replied threads | read | 1,089 messages (1,087 base + 2 seeded) + 19 replied threads with 83 replies (C07C2866011) | skim ≈ 3,000 messages/h (LH §4) = 22 min + 19 threads × 1 min | 41 |
| 10 | List Frederick's calendar from Sep 3 to Sep 30 and open each call titled with a person's name for its attendees and description (traps T6, T7) | read | 22 events (20 base + 2 seeded, 3 cancelled); 8 titled only with a person's name (evt_89381fe5a15b802c5652a9, evt_7934d6c78f843013d5d676, evt_be57cd7ca86d925fb5900c, evt_b7af120af94383d8f0781b, evt_38bdf82a0d337c4d82695e, evt_2204ffea306847eea6e5b0, evt_7d3e19b04a6c25f8e1b9a0, evt_2f86b0d4c9e17a35b64e0d) | triage ≈ 450/h (V1) = 3 min + 5 min per person-titled event | 43 |
| 11 | Look up the people behind those calls and behind partner-only mail in Contacts (traps T5, T6, T11) | read | 10 lookups in 174 contacts (170 base + 4 seeded: e3a91c07d5b48f26a0c7e314, b72f0d6e19c3a84e5d21f9a0, 5d0e8b31f7a29c64e1b0d3a8, a4c2e9f07b31d85e6c0f1b29) | 3 min per lookup | 30 |
| 12 | Firm-by-firm check for firms with bridge activity since Sep 3: mail by firm and partner name, the latest thread, the calendar and the channel notes; set the status | read | 31 firms (8 Passed, 9 In talks, 14 Awaiting reply per Working_Files/solver/truth.json), drawn from 168 base threads last active Sep 3–30 in Frederick's mailbox (112 after dropping build, calendar and notification mail) + 11 seeded threads | check one cohort record across 2–3 surfaces ≈ 8–15 min (V1); 12 min each | 372 |
| 13 | Firm-by-firm check for the rest of the list: two mail searches and a channel search per firm to confirm nothing has come from us since Sep 3 | read | 48 list firms with no bridge outreach since Sep 3 (Working_Files/solver/truth.json) | 4 min each: below the 8 min V1 floor because the searches come back empty or before Sep 3, so there is nothing to read | 192 |
| 14 | Money: Leonard's angel post, the Bridge angels sheet, Anton's Sep 24 mail, the DocuSign Completed notice and Leonard's Sep 29 nudge to Paul (traps T1, T4) | read | 5 records (C07C2866011/1758303600.418207; f_6e1d93a0c4b72f85d39a0e, 2 rows; frederick.stone@harmonygames.co/1844162278195200023; frederick.stone@harmonygames.co/1844354293432320031; frederick.stone@harmonygames.co/1844610859008000037) | decisive thread ≈ 20 min (LH §4) + 2 min for each of the 4 other short records | 28 |
| 15 | Build access: find the tester ticket in Linear and read its 2 comments; compare them with the Dentsu thread (trap T2) | read | 13 Linear issues mention TestFlight (the ZOM team has 570 issues); ZOM-567 + 2 comments (lc_94eb35d962cfbdd31e1bd496, lc_b549f3057640a5eb08f7581e); Dentsu thread frederick.stone@harmonygames.co/1844294398771200045 (2 messages) | triage 13 hits = 5 min + decisive thread ≈ 20 min (LH §4) | 25 |
| 16 | Rule out talks that aren't the bridge: the SVB catch-ups (bank), Mattel (RFP only), Rollic and Playable Factory (D3), and Arthur's "just list who Leonard emailed" aside (D2) | dead end | 3 SVB events on Sep 5 (evt_19bb017fa3fb8514bdf6f7, evt_434c1d2e33c42863b1836c, evt_d78356b83bb0c94f28a25b), 1 Mattel post (C096HFA5Z8W/1758927000.205874), 2 Rollic / Playable Factory items (C096HFA5Z8W/1758130464.175719, frederick.stone@harmonygames.co/1843000993076735547), 1 post (C07C2866011/1759168800.117903) | 5 min per item; the 3 SVB events count as one item, so 6 items | 30 |
| 17 | Rule out a16z's Sep 30 speedrun rejection as a bridge answer (template accelerator rule) and the advisor's read on Sony | dead end | 1 forwarded thread (frederick.stone@harmonygames.co/1844748127814183717) + its Sep 3 bridge thread (frederick.stone@harmonygames.co/1842277213140775733) + 1 list note | decisive thread ≈ 20 min (LH §4) + 5 min for Sony | 25 |
| 18 | Rule out Leonard's Sep 8 tracker post and the list's stale 09/11 notes for Hiro and T-Accelerate (D4, T5, T10) | dead end | 1 tracker post (C096HFA5Z8W/1757345124.546449) + 2 list notes (/sheets_spreadsheets/96) | 5 min each | 15 |
| 19 | Sort out name traps: Homa, whose call is titled with a person (T7); PXLite, named in T-Accelerate's call notes (T11); two Dentsu events, one of them on Oct 1 (D7); 1AM Gaming = March Gaming Fund | dead end | 1 note (C096HFA5Z8W/1758210489.170809), 1 thread (frederick.stone@harmonygames.co/1843978997950200606), 2 events (evt_3671b9a924ccba550e51fa, evt_eeca6fc7670fe1acd94440), 1 post (C096HFA5Z8W/1757365500.384216) | 5 min each, 4 items | 20 |
| 20 | Re-check firms that a later record overturns: SciPlay (Robert's Sep 29 phone note in a reply, T3), Play Ventures (Sep 25 correction), Dentsu (ZOM-567 after "invites are out", T2), Anton (the later, smaller amount, T4), Hiro (Sep 26 pass), T-Accelerate (Sep 22 call) | re-read | 6 firms re-opened (C096HFA5Z8W/1759184040.552871, C096HFA5Z8W/1758817200.730591, ZOM-567, frederick.stone@harmonygames.co/1844162278195200023, frederick.stone@harmonygames.co/1844318935449600041, frederick.stone@harmonygames.co/1842283406259093714) | 5 min each | 30 |
| 21 | Create the sheet "Fundraising - Oct 14 board" in the Board - Oct 14 2025 folder, type the rows and the totals | write | 1 Google Sheet, 79 rows × 5 columns (firm, status, build access, committed, soft-circled) + 2 totals, in folder d_5e8a1c3f9b07d2e64a1b93 | ≈ 1 min per short row (most rows are firm + status only; the 1 h 45 "write the record" anchor scaled to the rows) + 10 min to create, name, move and total it | 89 |
| 22 | Add the Keep warm checklist on the Existing Investor Update card | write | 1 checklist + 3 one-line items on card 68c5a49e8491a9d7faf869d0 | one tailored write ≈ 5 min (V1) + 1 min per one-line item | 8 |
| 23 | Reply to Leonard on his thread with the three numbers for the slide | write | 1 email reply on frederick.stone@harmonygames.co/1844724419788800011 (firm count, committed total, soft-circled total) | one tailored write ≈ 10 min (V1) | 10 |
| Total | | | | | 1155 = 19.25 h |

Tier check: in band. V3 puts Long-Horizon at about 12–24 hours (references/Docs/11_V3_Changes.md, tier table), and 19.25 h sits inside it. It is also near the V1 Long examples (10.5 h worksheet; 24 h at about 338 calls) and well under 37 h, the V1 Normal over-scope case.
Baseline count basis (post-baseline only): not yet available. This is the first pass; 07_Baseline_Trajectories/ is not in task_inputs yet.
Condensed breakdown length: 875 characters (field accepts 50–2,000)
Sources measured: `hg.py search get slack --file messages/C096HFA5Z8W/2025-09.json` and `messages/C07C2866011/2025-09.json` (with the 2025-08 files), counted by ts in the Sep 3–30 PT window, with roots, replied roots and replies counted separately; `persona_view.py search frederick_stone gmail "@" --no-hidden` (4,594 visible threads; 168 last active Sep 3–30 PT; 112 after dropping TestFlight builds, notes, invitations and RSVPs); `persona_view.py reach frederick_stone` (gcal 316 events visible; Slack channels visible); `hg.py search search gcal "frederick.stone@harmonygames.co" --key calendar_id` + `get-many` on the 316 events, counted by start in the PT window (20); `hg.py search get gsheets --file data.json --pointer /sheets_spreadsheets/96` (80 rows, 77 distinct firms, 23 Latest Status notes); `persona_view.py search frederick_stone gsheets "Investor List"` (2 visible lists); `hg.py search search trello "640643a3fd8f3ca308d9318e" --key idBoard` plus the two card ids; `hg.py search search linear "TestFlight"` (13 issues) and `--key team_id team_ZOM` (570); `hg.py search get contacts --pointer /contacts` (170); seeded rows counted from the 01_Universe_Inject.sql INSERTs (13 messages in 11 threads in Frederick's mailbox, 3 events on his calendar, 7 #bridge-pitch and 2 #executives posts, 4 contacts, 3 docs with 432 / 3,018 / 285-character bodies, 12 slides, 2 Linear comments); the 79-firm status split from Working_Files/solver/truth.json (sha256 33d88dacdb04ab89), which matches the platform /prompt derivation.

## Condensed breakdown (facts for the human's own wording; not for retyping)

The human writes the field in their own words, one short line per group. The facts and minutes for each group are listed below, and the groups add up to the total. The 875-character count is the length of the "Facts" column as written here, as a guide to the field size.

| Group | Facts | Time (min) |
|---|---|---|
| G1 | Leonard's ask + Robert's board mail, the Oct 14 template and README; the July template and the internal list ruled out | 55 |
| G2 | 2 Trello cards and the April lookalike card, 12-slide draft deck | 30 |
| G3 | 2025 investor list: 80 rows, 77 firms, 23 Latest Status notes | 57 |
| G4 | #bridge-pitch 406 msgs + 7 threads read in full; #executives 1,089 msgs + 19 threads skimmed | 96 |
| G5 | 22 calendar events Sep 3–30, 8 titled only with a person; 10 Contacts lookups | 73 |
| G6 | 31 firms with bridge activity: mail, calendar and Slack per firm, ~12 min each | 372 |
| G7 | 48 list firms confirmed untouched since Sep 3, ~4 min each | 192 |
| G8 | Angel money (post, sheet, 3 mails incl. signing notice); tester ticket + Dentsu thread | 53 |
| G9 | Dead ends: SVB, Mattel RFP, Rollic, Playable Factory, a16z speedrun no, stale trackers, name traps | 90 |
| G10 | Re-checking 6 firms a later record overturns | 30 |
| G11 | Writes: 79-row sheet + totals in the folder, Keep warm checklist with 3 items, reply with 3 numbers | 107 |

G1 = rows 1–3; G2 = 4–6; G3 = 7; G4 = 8–9; G5 = 10–11; G6 = 12; G7 = 13; G8 = 14–15; G9 = 16–19; G10 = 20; G11 = 21–23. Sum 55+30+57+96+73+372+192+53+90+30+107 = 1155 min = 19.25 h.

## Self-review

Checks walked in order: `references/Docs/10_Long Horizon Guidelines - V2.md` §5 (dead ends, workaround, re-reading, no learning time) and §10 (justified sub-task by sub-task, arithmetic adds up); `references/Docs/9_Common Errors & Pre-QC - V2.md` "Difficulty and submission" (the estimate is justified and adds up); `references/Docs/11_V3_Changes.md` (human effort fits the tier: Long-Horizon about 12–24 hours); and the field text (hours on a 0.25 step, 50–2,000 characters, pasting and copying blocked).

| Check | Result |
|---|---|
| Manual effort, same work | Every row feeds one of the prompt's three writes: the sheet (rows 1–21), the Keep warm checklist (rows 4, 12, 20, 22) or the reply (rows 4, 6, 14, 23). No row counts learning the universe. The channels are read only for the status window |
| Volumes persona-filtered | Gmail counts come from Frederick's mailbox only (`persona_view.py ... --no-hidden`). Calendar counts are events whose calendar_id is frederick.stone@harmonygames.co. Frederick posts in both channels in the window (EMPLOYEE_0008_SLACK_ID: 9 #bridge-pitch and 69 #executives messages, so he is a member). The seeded docs, deck and folder list him in shared_with or as owner (SQL L7–L18). Linear, Trello and Contacts are unscoped |
| Rates anchored | Each row names the LH §4 anchor or a V1 rate. Rows 4, 6, 8, 13 and 21 state their own rate and why (short comments; a fundraising channel read line by line; empty searches; short rows) |
| Dead ends explicit | Rows 3, 5, 16, 17, 18 and 19 cover T5, T6, T7, T9, T10, T11 and D1–D7. Traps met in the main reads are named on their rows: T1 and T4 (row 14), T2 (rows 15 and 20), T3 (row 20), T8 (row 4) |
| Workaround | Friction: none (03_Error_Async_Config.txt), so there is no workaround line |
| Writes per write | Rows 21–23: 1 sheet (79 rows + 2 totals, moved into the folder), 1 checklist with 3 items, 1 email reply |
| Arithmetic | 23 rows sum to 1155 min = 19.25 h, on the 0.25 step; groups G1–G11 sum to the same 1155 |
| Field length | condensed facts are 875 characters, inside 50–2,000 |

| Counter-reading | Resolution (evidence) |
|---|---|
| Counter (inflated): 19 h is a lot for "one sheet and a reply" | Each row has a measured volume and a rate. The two largest rows are per-firm checks: 31 active firms at 12 min and 48 untouched firms at 4 min (Working_Files/solver/truth.json; 79 = 77 list names in /sheets_spreadsheets/96 + Homa evt_89381fe5a15b802c5652a9 + Brightwater evt_2f86b0d4c9e17a35b64e0d). At the V1 floor (8 min and 3 min) those two rows fall from 564 to 392 min, and the total is still 983 min ≈ 16.4 h, inside the band |
| Counter (solution-path estimate): written as if Frederick knew which firms were active | Rows 12–13 split the firms by what the searches return, not by known answers. Every firm gets at least the 4-minute check. Every manifest trap (01_Hardness_Manifest.json traps T1–T11, D1–D7) has a dead-end line or is named on the row where it bites. Row 20 adds the re-reads after later records: C096HFA5Z8W/1759184040.552871 (SciPlay), C096HFA5Z8W/1758817200.730591 (Play Ventures), lc_b549f3057640a5eb08f7581e (Dentsu) |
| Counter (evaluator-wide volume): counts include mail and channels Frederick can't see | The mailbox count is from `persona_view.py search frederick_stone gmail "@" --no-hidden` (4,594 threads visible; Robert's and Leonard's copies such as leonard.hayes@harmonygames.co/1844724419788800013 are not counted). The calendar is filtered to calendar_id frederick.stone@harmonygames.co (316 events, matching persona_view reach). The channel counts are for C096HFA5Z8W and C07C2866011, where EMPLOYEE_0008_SLACK_ID posts. The internal list f_0b29566cd7932a205d54d2 is one of the 2 lists persona_view shows him |
| Counter (tier mismatch): wrong size for Long-Horizon | 19.25 h is inside the V3 Long-Horizon band of about 12–24 h (11_V3_Changes.md tier table). The design budget is 502 calls (01_Hardness_Manifest.json call_budget), well over the 100-call Long-Horizon minimum, so tier and scope agree; no change |
| Counter (linter reading): from the prompt and SQL alone, is 19.25 h within 3× of a defensible figure? | The prompt asks for a whole pipeline sheet. The SQL shows the template's four rule sections (SQL L23), the 80-row list it points to, 13 seeded mails and 9 seeded posts across 7 services. A reader who sees about 80 firms, each checked in mail, Slack and the calendar, lands between about 8 h and 25 h, so 19.25 h is within 3×. The reasoning must name the volumes (80 rows / 77 firms, 406 + 1,089 channel messages, 22 calendar events, 79-row sheet) so the linter can see the scope |
| Counter (could fail): row 8 at 600 messages/h understates a careful read of #bridge-pitch | The base messages average 21 words each (8,370 words / 399 messages, C096HFA5Z8W 2025-09). At 200 words/min that is 42 min, so 41 min plus 14 for the 7 threads holds. A slower 150 words/min adds 14 min, still within the band |

Unresolved: none. Refresh this worksheet after 08_Oracle_Events.md exists and again after the baseline (count basis).

```
STAGE GATE humantime: PASS — Task_Authoring/task_inputs · 05_Human_Time_Worksheet.md#d892f87c1f74 · 04_Prompt.txt#cecfad824fd8 · 00_Assigments.md#8ae66b700bc2 · 08_Oracle_Events.md#e3b0c44298fc · 07_Baseline_Trajectories#ad7848c1ad99 · __context__#f1f763cb8cb4 · __assignment__#827e8afa884d · __policy__#dc4ab5df3cdd · __gate_policy__#0fc4bb90877f · __review__#724c5240bc3b · blocking 0 · warnings 0 · checks 17
[PASS] assignment.v3_context: Frederick Stone / Co-founder; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 05_Human_Time_Worksheet.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 00_Assigments.md, 08_Oracle_Events.md, 07_Baseline_Trajectories)
[PASS] chain.prompt-check: upstream 'prompt-check' PASS pasted and current (04_Prompt_Check.md#a1b3a4551872, 04_Prompt.txt#cecfad824fd8, 04_Prompt_Writing_Brief.md#c53118f3dba1, __context__#f1f763cb8cb4, __assignment__#827e8afa884d, __policy__#dc4ab5df3cdd, __gate_policy__#0fc4bb90877f, __review__#1c447503f025)
[PASS] structure.placeholders: no placeholders in 05_Human_Time_Worksheet.md
[PASS] structure.arithmetic: 23 sub-tasks sum to 1155 min = 19.25 h
[PASS] evidence.volumes: every sub-task has a measured volume
[PASS] structure.kinds: dead-end / workaround / write lines present
[PASS] structure.field_length: condensed breakdown 875 characters
[PASS] evidence.sources: volume sources name the hg.py / persona_view queries
[PASS] structure.tier_check: tier check line present
[PASS] review.counter_readings: 6 evidenced counter-readings (of 6 found; need ≥ 5) in 05_Human_Time_Worksheet.md
[PASS] review.coverage: self-review addresses all 5 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```
