# Prompt Brief — leonard_stockholder_closeout · prep
> Built 2026-11-08 from 00_Assigments.md, Working_Files/00_Task_Context.json, Working_Files/01_Grounding_Dossier.md (injection rev1, SQL sha256 6f3b18994e1a; the platform /injection PASS plateform_reports/6aed9d01a1cb8067d8ac7dee_0_injection.md reviewed the earlier sha256 bc72db9c31e9, so /injection re-runs with /prompt), 01_Universe_Inject.sql, 01_Scenario_Design.md, 01_Hardness_Manifest.json, solver/truth.json · no 03_Error_Async_Config.txt (Friction: none by default), no 02_Reference_Files_Manifest.md (no attachment) · Persona view verified: all (check-sql PASS on every seeded load-bearing record; base records by persona_view search, §5a) · Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) · Leonard's today: Saturday Feb 14, 2026.
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Executive | Founders / Exec / Strategy in `Evals/references/rules/task_categories.md`: a founder closes out the company's stockholders, the board and the auditor after the Feb 11, 2026 shutdown (C0ADGSZKR3R/1770934638.035469). |
| Persona | Leonard Hayes · leonard.hayes@harmonygames.co · Co-founder & Creative Director (roster.json persona_key leonard_hayes, Executive) | Voice: plain and direct to his assistant, short sentences (C0ADGSZKR3R/1770934638.035469 'next things for me are'). Remit: he promised to reach every angel himself (D04UC0UEN2V/1770665186.368229), runs the Carta terminations (C0ADGSZKR3R/1770935621.095649) and answers KPMG every year (leonard.hayes@harmonygames.co/1817557789846606177). Read scope: his mailbox and calendar, his Drive, #winddown C0ADGSZKR3R, his DMs (D04UC0UEN2V, D09R59580EM, D04UGG61DUM) and group DM C51ECE5102ED; Linear and Trello unscoped. |
| Competency | Finance | Cap table and equity reconciliation: stock by line apart from advisor options, options outstanding at the clock and at KPMG's date, holders' last days, the auditor's confirmation (leonard.hayes@harmonygames.co/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com>). Expected outputs: a holder schedule, a confirmation reply, investor communications. |
| Task skill | Authoring | Authored artifacts: the holder sheet, 14 personal messages, the investor letter (from C0ADGSZKR3R/1770664700.848759), the KPMG reply and the Griffin heads-up. |
| Task type | long-horizon (Long Horizon; difficulty mode medium, V3 cap < 85 %; requester target < 70 %, 130+ counted calls) | Services carrying weight: Linear (26 issues, 52 notes, 26 state moves, 12 reason comments; ec2ea957-fc8e-4958-b809-0fb735b1e916 (team_ENG)), Gmail (14 Carta notices, six letters, owner list, KPMG, Sunset, side letter chain, resignations, 14 drafts, 2 replies), Slack (#winddown, three DMs, a group DM), Drive/Docs/Sheets/Slides (notes, advisor table, term sheet, charter, side letter, the sheet and letter), Trello, GCal, Contacts. hardness_gate (extreme): PASS in the dossier. |

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
|---|---|---|---|
| Leonard promised to reach out to each investor himself, and his Feb 12 list in #winddown still shows the angels as open. | Leonard | D04UC0UEN2V/1770665186.368229; C0ADGSZKR3R/1770934638.035469 | none needed |
| He has set up one Linear issue per holder on Carta and written close-out notes on how each holder gets handled. | Leonard | ec2ea957-fc8e-4958-b809-0fb735b1e916 (team_ENG); f_a37b403d5200d4f0a31d31 | — |
| KPMG asked on Feb 13 for Griffin's FY25 confirmation, and Sunset's legal asked for a stockholder sheet for the intake. | Leonard | leonard.hayes@harmonygames.co/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com>; leonard.hayes@harmonygames.co/<mlkq74xd.3f9e2c1a-6b48-4d07-a1e5-8c2f0d7b6a94@we.are.superhuman.com> | — |
| The investor email he drafted on Feb 9 predates the signing, the resignations and the Carta entries. | Leonard | C0ADGSZKR3R/1770664700.848759 | — |

## 3 · Investigation → action

Questions to resolve (no answers here):
- Who holds what today, line by line, and how much of each merged owner-list line is stock?
- Which option lines are live at the clock, and what is each one's last day?
- Who has already had a written message about the closing, sent to them directly and delivered?
- What is each holder owed under the notes, and whose last day comes first?
- Which lines does one family member speak for?
- Who is on the board now, and who holds the preferred vote?
- What did the company have outstanding at KPMG's date, using effective dates?
- Did any holder ask something about their holding that was never answered?

Writes those answers feed: the holder sheet, the personal messages as drafts, the Linear states and reason comments, the letter, the KPMG reply, the Griffin heads-up and the #winddown reply. Every write depends on the investigation.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |
|---|---|---|---|---|---|
| Holder sheet (Google Sheet) | one row per project issue (ENG-2438 to ENG-2463) with holder, stock, options, last day, told, label; totals of shares and options; count by label; directors and the preferred vote | close-out folder d_601064334a0b493022fe83 | shared with robert@harmonygames.co and arthur.blake@harmonygames.co | gsheets create + values update; gdrive move + share | every §3 question |
| Personal messages (14 Gmail drafts) | the closing where not told, the last day where there is one, what they hold, an answer to an open question | Leonard's drafts (leonard.hayes@harmonygames.co) | the 14 holders owed one; one to Enes for the family's three lines | gmail create draft | told, owed, family, ask |
| Linear issues | state per the project description; a reason comment on every issue with no note of its own | project ec2ea957-fc8e-4958-b809-0fb735b1e916 (team_ENG) | — | linear update issue ×26; linear create comment ×12 | owed |
| Investor letter (Google Doc) | the #winddown draft C0ADGSZKR3R/1770664700.848759 brought up to date | close-out folder d_601064334a0b493022fe83 | shared with robert@harmonygames.co | gdocs create; gdrive move + share | board, Sunset, options |
| KPMG reply | shares by class with each fund's holding; each option line and the total at Dec 31, 2025; shares plus those options; later events | reply to all on leonard.hayes@harmonygames.co/1857029474983245439 | PERSON_3088_EMAIL, cc PERSON_4416_EMAIL, PERSON_2322_EMAIL, PERSON_2847_EMAIL | gmail reply to message | as-of figures |
| Griffin heads-up | a request for Griffin's vote as preferred holders on the dissolution | reply to all on the partner's own Feb 12 mail in leonard.hayes@harmonygames.co/1856958794180374704 | PERSON_4337_EMAIL, cc PERSON_2847_EMAIL | gmail reply to message | board, vote |
| #winddown reply | who goes first | thread under C0ADGSZKR3R/1770934638.035469 | the founders in #winddown | slack send message (thread) | last days |

Alternatives a careful run could defend, and how each is settled: editing the draft sheet in the folder instead of a new sheet (accepted: same folder, contents and sharing); the KPMG reply or the Griffin heads-up left as drafts (settled: the project says 'Send KPMG's confirmation as a reply to all', the notes say the heads-up 'can go out once the sheet is done'); three messages for the family (settled by the reply under the list, C0ADGSZKR3R/1770949310.220519); the letter sent by mail (settled: H1 'a letter I can send', in the folder); a new top-level #winddown post instead of a thread reply (settled: 'reply under my list').

### 4b · Canonical outcome (all fair outcomes)

| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by (quoted span, or —) | Allowed equivalence class | Material / representational |
|---|---|---|---|---|---|
| Holder sheet | rows | 26 rows keyed by ENG-2438 to ENG-2463; the founders only in the totals; counts by rows | 'One row per issue on the sheet, and the counts go by rows' (f_a37b403d5200d4f0a31d31) | extra summary rows; any column order | material |
| Holder sheet | label per row | Nothing 6, Already told 4, Closing 6, Covered 2, Last day 6, Closing and last day 2 (solver/truth.json) | 'Labels for the sheet' (f_a37b403d5200d4f0a31d31); 'Mark those lines Covered' (C0ADGSZKR3R/1770949310.220519) | First note = Closing; Date note = Last day; Full note = Closing and last day | material |
| Holder sheet | stock lines | Griffin II 2,662,255; Side Fund 84,438; Segerstrale and TOR 50,865; eight lines 25,432 | Sunset's list (leonard.hayes@harmonygames.co/<mlkq74xd.3f9e2c1a-6b48-4d07-a1e5-8c2f0d7b6a94@we.are.superhuman.com>) | with or without separators | material |
| Holder sheet | options | advisor grants 61,038, 30,518, 6,104, 6,104; live vested lines per Carta | '(for options, what's vested)' (leonard.hayes@harmonygames.co/<mlkq74xd.3f9e2c1a-6b48-4d07-a1e5-8c2f0d7b6a94@we.are.superhuman.com>) | in an options column or beside the stock | material |
| Holder sheet | totals | Series Seed 3,051,879; common 6,000,000; options now 164,114 | 'Total shares and options outstanding' (leonard.hayes@harmonygames.co/<mlkq74xd.3f9e2c1a-6b48-4d07-a1e5-8c2f0d7b6a94@we.are.superhuman.com>) | shares issued 9,051,879 may also appear | material |
| Holder sheet | board | directors in office Leonard Hayes and Robert; preferred vote Griffin, 90.0 % | 'Directors in office, and who holds the preferred vote' (leonard.hayes@harmonygames.co/<mlkq74xd.3f9e2c1a-6b48-4d07-a1e5-8c2f0d7b6a94@we.are.superhuman.com>); 'That leaves Leonard and me on the board' (leonard.hayes@harmonygames.co/<CAGkro_Tn7wQ2xLp9VbR4mYc8KsHd3EjUf6ZaNi1oGqX5tBe0Rw@mail.gmail.com>) | Griffin's two funds named together | material |
| Holder sheet | destination and sharing | in d_601064334a0b493022fe83; shared with robert@harmonygames.co and arthur.blake@harmonygames.co | 'everything goes in the close-out folder' and 'Share it ... with Robert' (f_a37b403d5200d4f0a31d31); 'the sheet goes to you as well as Robert' (C0ADGSZKR3R/1770949310.220519) | reader or writer role | representational (role) |
| Messages | set | 14 drafts: Closing to Schaeppi, Bergmann, Enes (for three lines), TOR, Deepak; Last day to ES-1, ES-4, ES-7, ES-13, ES-15; Closing and last day to ES-3, ES-12, ES-14 and ES-18 (Collins was told on Feb 12 as Akin) | 'as Gmail drafts' and the handling rules (f_a37b403d5200d4f0a31d31) | any order | material |
| Messages | content | each states what they hold; Claire's answers her open equity question; Enes's covers the three lines and says what each holds | 'Each note says what they hold'; 'Anything they asked ... gets answered' (f_a37b403d5200d4f0a31d31); C0ADGSZKR3R/1770949310.220519 | any wording | material |
| Messages | address | the email on the holder's issue description (ENG-2438 to ENG-2463) | 'Messages go to the email on each holder's issue' (f_a37b403d5200d4f0a31d31) | — | material |
| Linear | states | Canceled 5, Todo 14, Done 7 | project description (ec2ea957-fc8e-4958-b809-0fb735b1e916 (team_ENG)) | — | material |
| Linear | reason comments | 12, one on each issue with no note of its own, Canceled included | 'On every issue with no note of its own, Canceled included, say why' (ec2ea957-fc8e-4958-b809-0fb735b1e916 (team_ENG)) | any wording | material |
| Letter | contents | the draft brought up to date: the closing, Sunset running it, no distribution expected, tax papers, IP and code, the board, options | 'take my draft from #winddown and bring it up to date' (f_a37b403d5200d4f0a31d31) | any wording; the outline's sections in any order | material |
| KPMG reply | figures | options at Dec 31, 2025 243,757; shares plus options 9,295,636; Griffin II 2,662,255 and Side Fund 84,438; the closing as a later event | items 1-4 (leonard.hayes@harmonygames.co/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com>) and the follow-up (leonard.hayes@harmonygames.co/<LV3PR19MB85246D2E9B14C7A03F5E8D12BC4A7@LV3PR19MB8524.namprd19.prod.outlook.com>) | per-line table in any order | material |
| KPMG reply | delivery | sent, reply to all on leonard.hayes@harmonygames.co/1857029474983245439 | 'Send KPMG's confirmation as a reply to all' (ec2ea957-fc8e-4958-b809-0fb735b1e916 (team_ENG)) | — | material |
| Griffin heads-up | delivery | sent, reply on leonard.hayes@harmonygames.co/1856958794180374704 | 'That one can go out once the sheet is done' (f_a37b403d5200d4f0a31d31) | — | material |
| #winddown reply | who goes first | ES-3 (Calvin Price), last day Feb 20, 2026 by Carta's Jan 23 update; then ES-14 (Vincent Parker), Feb 21 | 'reply under my list in #winddown and say who goes first' (f_a37b403d5200d4f0a31d31) | name, token or issue key | material |
| All | dates | Pacific or UTC (clock line in leonard.hayes@harmonygames.co's view) | — | Feb 21 or 2026-02-21 | representational |

## 5 · Discovery map

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 holder project | 26 issues, description with states and asks | ec2ea957-fc8e-4958-b809-0fb735b1e916 (team_ENG) | YES (unscoped) | — | low | Yes: anchor AN2 |
| F2 investor email draft | Leonard's Feb 9 draft | C0ADGSZKR3R/1770664700.848759 | YES | — | low | Yes: anchor AN1 |
| F3 KPMG request | as of Dec 31, 2025, effective dates as Carta shows them | leonard.hayes@harmonygames.co/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com> | YES | FY24 request (as of Sep 30, 2024) | medium | Yes: anchor AN3 |
| F4 close-out notes | the closed rule and the asks | f_a37b403d5200d4f0a31d31 | YES (owner) | earlier notes f_762c60832854d3e7a7f7df | low | Yes: the persona's own doc |
| F5 earlier notes | one mail to everyone | f_762c60832854d3e7a7f7df | YES (owner) | replaced by f_a37b403d5200d4f0a31d31 | low | No |
| F6 Sunset's ask | what the intake needs | leonard.hayes@harmonygames.co/<mlkq74xd.3f9e2c1a-6b48-4d07-a1e5-8c2f0d7b6a94@we.are.superhuman.com> | YES | — | low | No |
| F7 family rule | one note covers the family's lines | C0ADGSZKR3R/1770949310.220519 | YES (#winddown member) | H1 'at most one note per person' (f_a37b403d5200d4f0a31d31) | high (thread reply) | No: never in the prompt |
| F8 Robert's reply | Nebojsa told on Feb 12 | leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com> | YES (cc) | the Feb 12 list C0ADGSZKR3R/1770934638.035469 | high | No: never in the prompt |
| F9 Carta notices | 14 lines, effective dates and last days | leonard.hayes@harmonygames.co/1856960478782792748 | YES | term sheet 268,772 | medium | No |
| F10 Feb 11 letters | six letters, no last day | leonard.hayes@harmonygames.co/1856861400116562076 | YES | 'All termination letters are sent' C0ADGSZKR3R/1770841239.761999 | high | No: never in the prompt |
| F11 letters done claim | a founder's done line | C0ADGSZKR3R/1770841239.761999 | YES | the six letters | medium | No |
| F12 Carta done claim | terminations entered | C0ADGSZKR3R/1770935621.095649 | YES | no last day sent | medium | No |
| F13 Feb 12 list | angels open | C0ADGSZKR3R/1770934638.035469 | YES | D04UC0UEN2V/1770664988.379119; leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com> | low | No |
| F14 Segerstrale told | Feb 9 DM | D04UC0UEN2V/1770664988.379119 | YES (DM) | C0ADGSZKR3R/1770934638.035469 | high | No: never in the prompt |
| F15 Tor DM | runway warning, not the closing | D09R59580EM/1762285888.654689 | YES (DM) | — | medium | No |
| F16 owner list | merged lines | leonard.hayes@harmonygames.co/1816809274978043917 | YES | advisor table f_6a37227593d0977fdbdd7a | medium | No |
| F17 advisor table | 103,764 in four grants | f_6a37227593d0977fdbdd7a | YES (share) | — | high | No: never in the prompt |
| F18 term sheet | 3,051,879 and 268,772 | f_11040fe5d66821bd6951aa | YES (share) | Carta notices | medium | No |
| F19 signed side letter chain | Segerstrale added as a party | leonard.hayes@harmonygames.co/1777052222643175480 | YES | Drive copy f_6201c7027d02997bfb2c84 | high | No: never in the prompt |
| F20 side letter Drive copy | Tor only | f_6201c7027d02997bfb2c84 | YES (share) | leonard.hayes@harmonygames.co/1777052222643175480 | medium | No |
| F21 Collins resigns | May 1, 2025 | leonard.hayes@harmonygames.co/1830959847543474636 | YES | financing documents f_966445655f653d26dc8537 | medium | No: never in the prompt |
| F22 Griffin's director resigns | Feb 12, 2026 | leonard.hayes@harmonygames.co/1856958794180374704 | YES | f_966445655f653d26dc8537 | low | No |
| F23 charter | protective provision: a vote of the preferred | f_90c029015fc474199cf736 | YES (share) | — | medium | No |
| F24 Claire's question | equity question unanswered | C51ECE5102ED/1770903714.600249 | YES (group DM member) | Leonard's replies answer another question | high | No: never in the prompt |
| F25 family addresses | Enes gives all three | leonard.hayes@harmonygames.co/1770141224265557526 | YES | the owner list shows no shared surname | high | No |
| F26 ES-14 resignation | left Nov 21, 2025 | leonard.hayes@harmonygames.co/1849344928983425627 | YES | #company-internal membership | medium | No |
| F27 Trello card | order of work | 698e5a10c3f24b7e9d16a0e4 | YES (unscoped) | — | low | No |
| F28 Tuesday hold | Feb 17 | evt_6f1a2c9e4b7d3a58c0e1d2 | YES (owner) | — | low | No: never in the prompt |
| F29 Task List row | send email to investors | f_31115ddb6ed866f2b10d60 | YES (share) | — | low | No |
| F30 draft sheet | copied Nov 2024 figures | f_5ecaa967db3adcfa440b09 | YES (owner) | Carta and the project | low | No |
| F31 outline deck | letter sections | f_75dddccabb26eeea4842c8 | YES (owner) | — | low | No |
| F32 close-out folder | destination | d_601064334a0b493022fe83 | YES (owner) | the Wind Down folder | low | No |
| F33 Bergmann contact | PERSON_0693_EMAIL | contacts d3c6e5b57e0ee6656a1bdd2c | YES (unscoped) | patrick@ mail | low | No |
| F34 ES-17 letter | 34,409 and Jan 22, deferring to Carta | leonard.hayes@harmonygames.co/1847335165884050330 | YES | Carta 34,439 and Jan 28 | medium | No |
| F35 advisor agreement | Nebojsa's grant | f_3ee38465decc57e61df6e5 | YES (share) | — | medium | No |
| F36 board after Feb 12 | Leonard and Robert | leonard.hayes@harmonygames.co/<CAGkro_Tn7wQ2xLp9VbR4mYc8KsHd3EjUf6ZaNi1oGqX5tBe0Rw@mail.gmail.com> | YES (cc) | financing documents f_966445655f653d26dc8537; the Feb 11 notes | low | No |
| F37 seed figure correction | the Jan 14 modelling runs 2 high | C07C2866011/1768418331.402719 | YES (#executives member) | C07C2866011/1768416262.426129 | medium | No |
| F38 SSP-10 holder | Husnu Matthew Collins | leonard.hayes@harmonygames.co/1777100628672295991 | YES | owner-list token | low | No |

## 5a · Search-as-persona proof

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| F1 | linear | Holder records | 0 base + 1 seeded | 0 | ec2ea957-fc8e-4958-b809-0fb735b1e916 | YES (seeded; unscoped) |
| F2 | slack | periodic updates | 1 base + 0 seeded | n/a (--no-hidden) | C0ADGSZKR3R/1770664700.848759 | YES (base hit) |
| F3 | gmail | Audit Request | 2 base + 1 seeded | n/a (--no-hidden) | leonard.hayes@harmonygames.co/1857029474983245439 | YES (seeded; check-sql YES) |
| F4 | gdocs | close-out notes | 0 base + 1 seeded | 0 | f_a37b403d5200d4f0a31d31 | YES (seeded; check-sql YES) |
| F5 | gdocs | outreach notes | 0 base + 2 seeded | 0 | f_762c60832854d3e7a7f7df | YES (seeded; check-sql YES) |
| F6 | gmail | stockholder | 7 base + 1 seeded | n/a (--no-hidden) | leonard.hayes@harmonygames.co/1857034369525983506 | YES (seeded; check-sql YES) |
| F7 | slack | family | 697 base + 1 seeded | n/a (--no-hidden) | C0ADGSZKR3R/1770949310.220519 | YES (seeded; check-sql YES) |
| F8 | gmail | closing the company | 0 base + 1 seeded | n/a (--no-hidden) | leonard.hayes@harmonygames.co/1773963101399472184 | YES (seeded; check-sql YES) |
| F9 | gmail | Termination details | 14 base + 0 seeded | n/a (--no-hidden) | 1856960478782792748 | YES (base hit) |
| F10 | gmail | independent contractor | 6 base + 0 seeded | n/a (--no-hidden) | 1856861400116562076 | YES (base hit) |
| F11 | slack | termination letters | 3 base + 0 seeded | n/a (--no-hidden) | C0ADGSZKR3R/1770841239.761999 | YES (base hit) |
| F12 | slack | Carta terminations | 2 base + 0 seeded | n/a (--no-hidden) | C0ADGSZKR3R/1770935621.095649 | YES (base hit) |
| F13 | slack | Reaching out to our angels | 1 base + 0 seeded | n/a (--no-hidden) | C0ADGSZKR3R/1770934638.035469 | YES (base hit) |
| F14 | slack | shut down the company | 8 base + 0 seeded | n/a (--no-hidden) | D04UC0UEN2V/1770664988.379119 | YES (base hit) |
| F15 | slack | investor updates | 4 base + 0 seeded | n/a (--no-hidden) | D09R59580EM/1762285888.654689 | YES (base hit) |
| F16 | gmail | diluted ownership | 8 base + 0 seeded | n/a (--no-hidden) | 1816809274978043917 | YES (base hit) |
| F17 | gdocs | Due Diligence | 6 base + 0 seeded | 4 | f_6a37227593d0977fdbdd7a | YES (base hit) |
| F18 | gdocs | term sheet | 4 base + 0 seeded | 1 | f_11040fe5d66821bd6951aa | YES (base hit) |
| F19 | gmail | Tor Capital | 22 base + 0 seeded | n/a (--no-hidden) | 1777052222643175480 | YES (base hit) |
| F20 | gdocs | side letter | 3 base + 1 seeded | 1 | f_6201c7027d02997bfb2c84 | YES (base hit) |
| F21 | gmail | board position | 3 base + 1 seeded | n/a (--no-hidden) | 1830959847543474636 | YES (base hit) |
| F22 | gmail | Board position | 3 base + 1 seeded | n/a (--no-hidden) | 1856958794180374704 | YES (base hit) |
| F23 | gdocs | Certificate of Incorporation | 26 base + 0 seeded | 36 | f_90c029015fc474199cf736 | YES (base hit) |
| F24 | slack | equity lerimiz | 1 base + 0 seeded | n/a (--no-hidden) | C51ECE5102ED/1770903714.600249 | YES (base hit) |
| F25 | gmail | 25.000 usd | 1 base + 0 seeded | n/a (--no-hidden) | 1770141224265557526 | YES (base hit) |
| F26 | gmail | Resignation | 6 base + 1 seeded | n/a (--no-hidden) | 1849344928983425627 | YES (base hit) |
| F27 | trello | close-out | 0 base + 1 seeded | 0 | 698e5a10c3f24b7e9d16a0e4 | YES (seeded; unscoped) |
| F28 | gcal | holder notes | 0 base + 1 seeded | 0 | evt_6f1a2c9e4b7d3a58c0e1d2 | YES (seeded; check-sql YES) |
| F29 | gsheets | Task List | 1 base + 0 seeded | 1 | f_31115ddb6ed866f2b10d60 | YES (base hit) |
| F30 | gsheets | Holder list | 0 base + 1 seeded | 0 | f_5ecaa967db3adcfa440b09 | YES (seeded; check-sql YES) |
| F31 | gslides | Update | 57 base + 1 seeded | 32 | f_75dddccabb26eeea4842c8 | YES (seeded; check-sql YES) |
| F32 | gdrive | close-out | 0 base + 2 seeded | 0 | d_601064334a0b493022fe83 | YES (seeded; check-sql YES) |
| F33 | contacts | PERSON_0693 | 0 base + 1 seeded | 0 | contact_bergmann | YES (seeded; unscoped) |
| F34 | gmail | Notice of Involuntary Termination | 2 base + 0 seeded | n/a (--no-hidden) | 1847335165884050330 | YES (base hit) |
| F35 | gdocs | Advisor Agreement | 1 base + 0 seeded | 4 | f_3ee38465decc57e61df6e5 | YES (base hit) |
| F36 | gmail | Leonard and me on the board | 0 base + 1 seeded | n/a (--no-hidden) | leonard.hayes@harmonygames.co/1856958794180374704 | YES (seeded; check-sql YES) |
| F37 | slack | seed figures | 0 base + 1 seeded | n/a (--no-hidden) | C07C2866011/1768418331.402719 | YES (seeded; check-sql YES) |
| F38 | gmail | Husnu Matthew Collins | 1 base + 0 seeded | n/a (--no-hidden) | 1777100628672295991 | YES (base hit) |

Outputs (persona_view.py search, verbatim):

```
SEARCH linear 'Holder records' as leonard_hayes  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH slack 'periodic updates' as leonard_hayes  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0ADGSZKR3R/1770664700.848759", "channel": "winddown", "kind": "private", "date": "2026-02-09", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "including key dates for operational shutdown. • I will send periodic updates as we complete the major steps and once we have clarity o
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Audit Request' as leonard_hayes  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=2 (showing 2)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "leonard.hayes@harmonygames.co/1788910618703813283", "last": "2024-02-02T04:42:53Z", "subject": "Re: [ORG_NAME_0153] 2023 Audit Request - [SOURCE_ORG_0001], Inc.", "snippet": "Re: [ORG_NAME_0153] 2023 Audit Request - [SOURCE_ORG_0001], Inc."}
  {"id": "leonard.hayes@harmonygames.co/1817557789846606177", "last": "2024-12-19T00:28:43Z", "subject": "Re: GRIFFIN GAMING PARTNERS 2024 Audit Request [SOURCE_ORG_0001], Inc.", "snippet": "Re: GRIFFIN GAMING PARTNERS 2024 Audit Request [SOURCE_ORG_0001], Inc."}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gdocs 'close-out notes' as leonard_hayes  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gdocs 'outreach notes' as leonard_hayes  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gmail 'stockholder' as leonard_hayes  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=7 (showing 7)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "leonard.hayes@harmonygames.co/1774892093376420723", "last": "2023-08-22T01:50:03Z", "subject": "Leonard Hayes accepted CS-01", "snippet": "s, Carta is an SEC-registered Transfer Agent  and maintains stockholder ownership records for issuers on Carta's  platform. No action is needed on your"}
  {"id": "leonard.hayes@harmonygames.co/1777066945091428455", "last": "2023-09-15T01:58:23Z", "subject": "You have a certificate to sign", "snippet": "  certificate needs your signature so it can be sent to the stockholder.         Review and sign <https://mandrillapp.com/track/click/30051246/app.Cart
  {"id": "leonard.hayes@harmonygames.co/1778137298011543323", "last": "2023-09-26T21:31:11Z", "subject": "You have a certificate to sign", "snippet": "  certificate needs your signature so it can be sent to the stockholder.         Review and sign <https://mandrillapp.com/track/click/30051246/app.Cart
  {"id": "leonard.hayes@harmonygames.co/1780231452834504508", "last": "2023-10-20T00:16:53Z", "subject": "You have a certificate to sign", "snippet": "  certificate needs your signature so it can be sent to the stockholder.         Review and sign <https://mandrillapp.com/track/click/30051246/app.Cart
  {"id": "leonard.hayes@harmonygames.co/1799137174148645468", "last": "2024-05-15T16:34:55Z", "subject": "GRIFFIN GAMING PARTNERS: This Week in Gaming 🎮", "snippet": "s Updates + During FY 2024, the Company returned $1,505M to stockholders through stock repurchases and dividends. The board also author
  {"id": "leonard.hayes@harmonygames.co/1844728765710241566", "last": "2025-09-30T22:14:02Z", "subject": "GRIFFIN GAMING PARTNERS: Last Week in Gaming 🎮", "snippet": "PIF rolling over its existing 9.9% stake in the Company. EA stockholders will receive $210 per share in cash, representing a 25% premiu
  {"id": "leonard.hayes@harmonygames.co/1856675475513544349", "last": "2026-02-12T22:56:54Z", "subject": "Combo Fighter Data and [SOURCE_ORG_0001] Shut-Down", "snippet": "old for     taxes, payroll, and chargebacks     -       Any stockholder approvals or creditor notice steps we should consider     -
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'family' as leonard_hayes  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=697 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04RSEB8K0W/1677782769.228729", "channel": "pitch-deck", "kind": "private", "date": "2023-03-02", "user": "PERSON_6046_SLACK_ID", "reply": false, "snippet": "I did 2 pitches today basically with family/friends :slightly_smiling_face:"}
  {"id": "C04RYU8TJ8K/1680743222.080049", "channel": "random", "kind": "public", "date": "2023-04-06", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Playing dominoes with family. Anticipating what opponents will do is more fun than I thought. "}
  {"id": "C04RYU8TJ8K/1682732733.435169", "channel": "random", "kind": "public", "date": "2023-04-29", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "and we love to splash as a family"}
  {"id": "C04RYU8TJ8K/1685590351.637719", "channel": "random", "kind": "public", "date": "2023-06-01", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "e want to build? We're gonna strong arm you and kidnap your family until you succumb."}
  {"id": "C04RYU8TJ8K/1685741231.620699", "channel": "random", "kind": "public", "date": "2023-06-02", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I don’t know how a family of 4 in Turkey can really survive without getting help/support from somewhere i"}
  {"id": "C04RYU8TJ8K/1686186648.236219", "channel": "random", "kind": "public", "date": "2023-06-08", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ebit card and spent $64,000 on mobile games, wiping out her family's life savings"}
  {"id": "C04RYU8TJ8K/1686244971.576339", "channel": "random", "kind": "public", "date": "2023-06-08", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Me: PS5 is in the family room and I’m worried my wife will yell at me for playing Diablo all day long wh"}
  {"id": "C04RYU8TJ8K/1693439531.838409", "channel": "random", "kind": "public", "date": "2023-08-30", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Bay Area. I’m taking a break to enjoy nice weather with the family. "}
  {"id": "C04RYU8TJ8K/1696900565.608179", "channel": "random", "kind": "public", "date": "2023-10-10", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Hocus Pocus (1993) :star: 6.9 | Comedy, Family, Fantasy"}
  {"id": "C04RYU8TJ8K/1698373178.710369", "channel": "random", "kind": "public", "date": "2023-10-27", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": " my [NATIONALITY_1601] girlfriend wanted to intro me to her family. We did some gingerbread house decoration lol. We do decorate Christmas
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'closing the company' as leonard_hayes  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Termination details' as leonard_hayes  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=14 (showing 14)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "leonard.hayes@harmonygames.co/1808666480668498098", "last": "2024-08-28T20:59:28Z", "subject": "Termination details for [PERSON_NAME_0100]", "snippet": "Termination details for [PERSON_NAME_0100]"}
  {"id": "leonard.hayes@harmonygames.co/1830952527208439510", "last": "2025-05-01T20:46:38Z", "subject": "Termination details for Victor [PERSON_NAME_2770] [PERSON_NAME_0086]", "snippet": "Termination details for Victor [PERSON_NAME_2770] [PERSON_NAME_0086]"}
  {"id": "leonard.hayes@harmonygames.co/1847333272519888206", "last": "2025-10-29T16:11:35Z", "subject": "Termination details for [PERSON_NAME_0038]", "snippet": "Termination details for [PERSON_NAME_0038]"}
  {"id": "leonard.hayes@harmonygames.co/1847333318158821452", "last": "2025-10-29T16:12:19Z", "subject": "Termination details for [PERSON_NAME_2768] [PERSON_NAME_0011]", "snippet": "Termination details for [PERSON_NAME_2768] [PERSON_NAME_0011]"}
  {"id": "leonard.hayes@harmonygames.co/1847333347700620793", "last": "2025-10-29T16:12:47Z", "subject": "Termination details for Calvin Price", "snippet": "Termination details for Calvin Price"}
  {"id": "leonard.hayes@harmonygames.co/1847333395311994879", "last": "2025-10-29T16:13:32Z", "subject": "Termination details for [PERSON_NAME_0612]", "snippet": "Termination details for [PERSON_NAME_0612]"}
  {"id": "leonard.hayes@harmonygames.co/1856960351896429942", "last": "2026-02-12T22:29:53Z", "subject": "Termination details for Marcus Bennett", "snippet": "Termination details for Marcus Bennett"}
  {"id": "leonard.hayes@harmonygames.co/1856960382677662910", "last": "2026-02-12T22:30:23Z", "subject": "Termination details for [PERSON_NAME_0022] [PERSON_NAME_2767] [PERSON_NAME_2763]", "snippet": "Termination details for [PERSON_NAME_0022] [PERSON_NAME_2767] [PERSON_NAME_2763]"}
  {"id": "leonard.hayes@harmonygames.co/1856960410709778333", "last": "2026-02-12T22:30:50Z", "subject": "Termination details for Claire Morgan", "snippet": "Termination details for Claire Morgan"}
  {"id": "leonard.hayes@harmonygames.co/1856960433624350836", "last": "2026-02-12T22:31:12Z", "subject": "Termination details for [PERSON_NAME_0043]", "snippet": "Termination details for [PERSON_NAME_0043]"}
  {"id": "leonard.hayes@harmonygames.co/1856960478782792748", "last": "2026-02-12T22:31:54Z", "subject": "Termination details for [PERSON_NAME_0051]", "snippet": "Termination details for [PERSON_NAME_0051]"}
  {"id": "leonard.hayes@harmonygames.co/1856960504234892536", "last": "2026-02-12T22:32:19Z", "subject": "Termination details for [PERSON_NAME_0068]", "snippet": "Termination details for [PERSON_NAME_0068]"}
  {"id": "leonard.hayes@harmonygames.co/1856960532806250145", "last": "2026-02-12T22:32:46Z", "subject": "Termination details for [PERSON_NAME_2769] [PERSON_NAME_0093]", "snippet": "Termination details for [PERSON_NAME_2769] [PERSON_NAME_0093]"}
  {"id": "leonard.hayes@harmonygames.co/1856960563574318616", "last": "2026-02-12T22:33:16Z", "subject": "Termination details for Martin [PERSON_NAME_7250] Walsh", "snippet": "Termination details for Martin [PERSON_NAME_7250] Walsh"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'independent contractor' as leonard_hayes  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=6 (showing 6)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "leonard.hayes@harmonygames.co/1761203751780760643", "last": "2023-05-05T03:11:16Z", "subject": "RE: Intros: Leonard ([SOURCE_ORG_0001]) <> PERSON_5593_NAME", "snippet": "s – 1 way and 2 way    >    > ·         US Standard Form of Independent Contractor Agreement (CA, De)    >    > ·         
  {"id": "leonard.hayes@harmonygames.co/1856860994291529096", "last": "2026-02-11T20:13:48Z", "subject": "Termination of Independent Contractor Agreement", "snippet": "Termination of Independent Contractor Agreement"}
  {"id": "leonard.hayes@harmonygames.co/1856861229984402233", "last": "2026-02-11T20:15:32Z", "subject": "Termination of Independent Contractor Agreement", "snippet": "Termination of Independent Contractor Agreement"}
  {"id": "leonard.hayes@harmonygames.co/1856861323365646598", "last": "2026-02-11T20:16:46Z", "subject": "Termination of Independent Contractor Agreement", "snippet": "Termination of Independent Contractor Agreement"}
  {"id": "leonard.hayes@harmonygames.co/1856861400116562076", "last": "2026-02-11T20:17:49Z", "subject": "Termination of Independent Contractor Agreement", "snippet": "Termination of Independent Contractor Agreement"}
  {"id": "leonard.hayes@harmonygames.co/1856861462411533365", "last": "2026-02-11T20:18:37Z", "subject": "Termination of Independent Contractor Agreement", "snippet": "Termination of Independent Contractor Agreement"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'termination letters' as leonard_hayes  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=3 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0ADGSZKR3R/1770837803.405649", "channel": "winddown", "kind": "private", "date": "2026-02-11", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "gonna write official termination letters now"}
  {"id": "C0ADGSZKR3R/1770841239.761999", "channel": "winddown", "kind": "private", "date": "2026-02-11", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "All termination letters are sent"}
  {"id": "D05Q3QAH2QZ/1770824780.548099", "channel": "D05Q3QAH2QZ", "kind": "im", "date": "2026-02-11", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "e in February. In fact my plan is to send Everyone official termination letters as early as today. I will address all questions today at
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'Carta terminations' as leonard_hayes  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=2 (showing 2)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0ADGSZKR3R/1770934638.035469", "channel": "winddown", "kind": "private", "date": "2026-02-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "next things for me are • Carta terminations • Reaching out to our angels properly and let them know about the situation • o"}
  {"id": "C0ADGSZKR3R/1770935621.095649", "channel": "winddown", "kind": "private", "date": "2026-02-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Carta terminations are done"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'Reaching out to our angels' as leonard_hayes  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0ADGSZKR3R/1770934638.035469", "channel": "winddown", "kind": "private", "date": "2026-02-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "next things for me are • Carta terminations • Reaching out to our angels properly and let them know about the situation • onboarding w
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'shut down the company' as leonard_hayes  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=8 (showing 8)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C07C2866011/1764793149.178559", "channel": "executives", "kind": "private", "date": "2025-12-03", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "chatgpt says we need $30K-$50K to shut down the company - see the thread"}
  {"id": "C07C2866011/1769106885.265059", "channel": "executives", "kind": "private", "date": "2026-01-22", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "but we have no money left to shut down the company and do other stuff if needed"}
  {"id": "C07C2866011/1769207123.847009", "channel": "executives", "kind": "private", "date": "2026-01-23", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I think they will tell us to shut down the company"}
  {"id": "C07C2866011/1770765443.359489", "channel": "executives", "kind": "private", "date": "2026-02-10", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "This $25K is great if we can get it - we can use it to shut down the company properly and reduce the potential out-of-pocket expense
  {"id": "D04UC0UEN2V/1758328261.697169", "channel": "D04UC0UEN2V", "kind": "im", "date": "2025-09-20", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " happened to Sanlo? Did they get get acquihired or did they shut down the company? Looks like [PERSON_NAME_51553] left "}
  {"id": "D04UC0UEN2V/1770664988.379119", "channel": "D04UC0UEN2V", "kind": "im", "date": "2026-02-09", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "’t improve. The most reasonable thing to do right now is to shut down the company we decided."}
  {"id": "D04UGG61DUM/1762036295.609199", "channel": "D04UGG61DUM", "kind": "im", "date": "2025-11-01", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "what happens if we shut down the company? lol"}
  {"id": "D04UP2L3E3S/1759195769.911469", "channel": "D04UP2L3E3S", "kind": "im", "date": "2025-09-30", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Maybe it’s better to shut down the company "}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'investor updates' as leonard_hayes  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=4 (showing 4)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UM32UWKD/1684344688.073959", "channel": "investors", "kind": "private", "date": "2023-05-17", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I’m done with investor updates this morning."}
  {"id": "C04UM32UWKD/1684528793.524279", "channel": "investors", "kind": "private", "date": "2023-05-19", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "save this for investor updates - my bad"}
  {"id": "D09R59580EM/1762283800.142359", "channel": "D09R59580EM", "kind": "im", "date": "2025-11-04", "user": "PERSON_5275_SLACK_ID", "reply": false, "snippet": "onygames. Just two quick questions:  1. Do you send out any investor updates? If you do, I don’t think I am on the mail list. It would be 
  {"id": "D09R59580EM/1762285888.654689", "channel": "D09R59580EM", "kind": "im", "date": "2025-11-04", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "0128] - it’s great to hear from you.  1- I haven’t sent any investor updates recently. Let me send you the latest board deck from 2.5 we
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'diluted ownership' as leonard_hayes  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=8 (showing 8)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "leonard.hayes@harmonygames.co/1773160052067710033", "last": "2023-08-18T19:22:53Z", "subject": "RE: [SOURCE_ORG_0001] Second Close- Tor Capital", "snippet": "sk for a cap table for the purpose of calculating its fully diluted ownership percentage from time to time. We appreciate the shares m
  {"id": "leonard.hayes@harmonygames.co/1774541878774535160", "last": "2023-08-29T22:33:01Z", "subject": "Re: Ping - [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0128]", "snippet": "the purpose of calculating its fully >>>>>>>>>>>>>>>>>>>    diluted ownership percentage from time to time
  {"id": "leonard.hayes@harmonygames.co/1775512614090714832", "last": "2023-09-13T16:44:56Z", "subject": "RE: [SOURCE_ORG_0001] Second Close- Tor Capital - side letter", "snippet": "sk for a cap table for the purpose of calculating its fully diluted ownership percentage from time to time. We appreciat
  {"id": "leonard.hayes@harmonygames.co/1775602109531090463", "last": "2023-09-15T01:06:01Z", "subject": "Fwd: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132]- side letter", "snippet": "   for a cap table for the purpose of calculating its fully diluted ownership     percentage from t
  {"id": "leonard.hayes@harmonygames.co/1777052222643175480", "last": "2023-09-22T16:56:16Z", "subject": "RE: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132]- signing and closing", "snippet": "sk for a cap table for the purpose of calculating its fully diluted ownership percentage fro
  {"id": "leonard.hayes@harmonygames.co/1777757908648367779", "last": "2023-10-12T19:34:34Z", "subject": "Re: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132] - closing", "snippet": "sk for a cap table for the purpose of calculating its fully diluted ownership percentage from time to t
  {"id": "leonard.hayes@harmonygames.co/1778196793707902941", "last": "2023-09-27T19:37:11Z", "subject": "Re: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132] - closing set", "snippet": "sk for a cap table for the purpose of calculating its fully diluted ownership percentage from time 
  {"id": "leonard.hayes@harmonygames.co/1816809274978043917", "last": "2024-11-26T18:47:40Z", "subject": "Re: ACTION NEEDED: Response Required by (11/27) for UBI: (605 624 997)", "snippet": "      -           Arthur Blake – 2,000,000 shares – 19.863% diluted ownership          -           [PERSON_NAME
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gdocs 'Due Diligence' as leonard_hayes  scope: GDocs title + body_text
visible hits=6 (showing 6)  hidden by ACL=4 in 4 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_5e80ba8a32129193f119bc", "name": "Term Sheet Analysis.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "n connection with management, market research and technical due diligence and the negotiation, preparation
  {"id": "f_6a37227593d0977fdbdd7a", "name": "Due Diligence Disclosures.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "Due Diligence Disclosures"}
  {"id": "f_6e5e980d9827e16128c8b5", "name": "Harmony Games Inc. - Investors_ Rights Agreeme(3).docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "n in such registration statement and to conduct appropriate due diligence in connection therewith; notify e
  {"id": "f_b4a31e52cb00aad21acb65", "name": "Harmony Games Inc. - Investors_ Rights Agreeme(2).docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "n in such registration statement and to conduct appropriate due diligence in connection therewith; notify e
  {"id": "f_d373f14848cf5977b5fe99", "name": "Harmony Games Inc. - Investors_ Rights Agreeme.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "n in such registration statement and to conduct appropriate due diligence in connection therewith; notify each
  {"id": "f_eea48de956d91794d58280", "name": "Harmony Games Inc. - Investors_ Rights Agreeme(1).docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "n in such registration statement and to conduct appropriate due diligence in connection therewith; notify e

SEARCH gdocs 'term sheet' as leonard_hayes  scope: GDocs title + body_text
visible hits=4 (showing 4)  hidden by ACL=1 in 1 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_11040fe5d66821bd6951aa", "name": "Reset Financing Term Sheet (Washout Recap + Pay-to.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "Reset Financing Term Sheet (Washout Recap + Pay-to"}
  {"id": "f_5e80ba8a32129193f119bc", "name": "Term Sheet Analysis.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Term Sheet Analysis"}
  {"id": "f_86664a90c389754b60fd14", "name": "VC strategy.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "duce some of the above. Go for smaller pockets first, get a term sheet, then start the formal process with bigger 
  {"id": "f_af27742bf4dfc38c924fdb", "name": "Apple Arcade & Netflix Notes.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "d to Push for more than we got for TMNT -They got an offer (term sheet) from Netflix for their next game and used terms to Push

SEARCH gmail 'Tor Capital' as leonard_hayes  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=22 (showing 22)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "leonard.hayes@harmonygames.co/1768520517901907516", "last": "2023-08-01T23:09:52Z", "subject": "Re: Latest [SOURCE_ORG_0001] Material and the Term Sheet", "snippet": "the opportunity and look forward to working together!  ---  TOR Capital Limited  Whiteley Chambers  [LOCATION_38954]  St Heli
  {"id": "leonard.hayes@harmonygames.co/1773127341469801602", "last": "2023-08-10T17:18:03Z", "subject": "Re: [SOURCE_ORG_0001] Second Close", "snippet": "ng in PERSON_5593_NAME who is acting as > legal counsel for TOR Capital. PERSON_5593_NAME will be in touch shortly. > > > > Best, > > [PERSON_NAME_
  {"id": "leonard.hayes@harmonygames.co/1773160052067710033", "last": "2023-08-18T19:22:53Z", "subject": "RE: [SOURCE_ORG_0001] Second Close- Tor Capital", "snippet": "RE: [SOURCE_ORG_0001] Second Close- Tor Capital"}
  {"id": "leonard.hayes@harmonygames.co/1774250421965722936", "last": "2023-08-25T22:44:08Z", "subject": "Re: Follow Up", "snippet": "my updates in blue >> below. I think we need your help with Tor Capital and loan repayments. >> >> Pending items we need to take care of: >> >> Loan re"}
  {"id": "leonard.hayes@harmonygames.co/1774541878774535160", "last": "2023-08-29T22:33:01Z", "subject": "Re: Ping - [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0128]", "snippet": "Re: Ping - [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0128]"}
  {"id": "leonard.hayes@harmonygames.co/1774603492218434534", "last": "2023-08-22T19:25:54Z", "subject": "Re: Side letter request from [PERSON_NAME_0129] (Tor Capital)", "snippet": "Re: Side letter request from [PERSON_NAME_0129] (Tor Capital)"}
  {"id": "leonard.hayes@harmonygames.co/1775512614090714832", "last": "2023-09-13T16:44:56Z", "subject": "Re: [SOURCE_ORG_0001] Second Close- Tor Capital - side letter", "snippet": "Re: [SOURCE_ORG_0001] Second Close- Tor Capital - side letter"}
  {"id": "leonard.hayes@harmonygames.co/1775512792182982416", "last": "2023-08-28T22:15:44Z", "subject": "Automatic reply: [SOURCE_ORG_0001] Second Close- Tor Capital - side letter", "snippet": "Automatic reply: [SOURCE_ORG_0001] Second Close- Tor Capital - side letter"}
  {"id": "leonard.hayes@harmonygames.co/1775602109531090463", "last": "2023-09-15T01:06:01Z", "subject": "Fwd: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132]- side letter", "snippet": "Fwd: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132]- side letter"}
  {"id": "leonard.hayes@harmonygames.co/1775636449493308689", "last": "2023-09-24T20:47:54Z", "subject": "Re: [SOURCE_ORG_0001] pro-rata / Leonard-[PERSON_NAME_0128]-PERSON_5593_NAME", "snippet": " >>>>>>>>>>>>> investors! Please note cap table should have TOR Capital Ltd vs my name, if >>>>>>>>>>>>> 
  {"id": "leonard.hayes@harmonygames.co/1776432843811839680", "last": "2023-09-09T11:10:17Z", "subject": "Re: [SOURCE_ORG_0001]: A few pending board approvals", "snippet": " over the phone a > couple weeks ago. Note that he is using TOR capital as his investment > vehicle. Attached, you can find a WIP
  {"id": "leonard.hayes@harmonygames.co/1777052222643175480", "last": "2023-09-22T16:56:16Z", "subject": "Re: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132]- signing and closing", "snippet": "Re: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132]- signing and closing"}
  {"id": "leonard.hayes@harmonygames.co/1777757908648367779", "last": "2023-10-12T19:34:34Z", "subject": "Re: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132] - closing", "snippet": "Re: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132] - closing"}
  {"id": "leonard.hayes@harmonygames.co/1778021424406449623", "last": "2023-09-25T14:49:22Z", "subject": "Automatic reply: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132] - closing", "snippet": "Automatic reply: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132] - closin
  {"id": "leonard.hayes@harmonygames.co/1778188119485709093", "last": "2023-09-27T10:58:58Z", "subject": "Carta activity for Sept. 26, 2023", "snippet": "pp.Carta.com/certificates/list/3048065/?open=17696370> for  TOR Capital Limited     Arthur Blake signed  certificate SSP-11  <https://app.Carta.com/
  {"id": "leonard.hayes@harmonygames.co/1778196793707902941", "last": "2023-09-27T19:37:11Z", "subject": "Re: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132] - closing set", "snippet": "Re: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132] - closing set"}
  {"id": "leonard.hayes@harmonygames.co/1780678901649061677", "last": "2023-10-24T23:24:20Z", "subject": "Re: Announcement prep + question", "snippet": "al, [PERSON_NAME_6550]' ex CTO at Playfish, he invested via Tor Capital Matthew Collins: https://www.linkedin.com/in/redacted-profile/ COO at Tripled
  {"id": "leonard.hayes@harmonygames.co/1797136850952953680", "last": "2024-04-23T14:40:56Z", "subject": "📈 CKC.Fund –  average 100% + p.a.", "snippet": "m of risks. Comprehensive insurance cover ensures that investor capital is safeguarded, enhancing trust and stability.    **Mission-Driven Investmen
  {"id": "leonard.hayes@harmonygames.co/1816809274978043917", "last": "2024-11-26T18:47:40Z", "subject": "Re: ACTION NEEDED: Response Required by (11/27) for UBI: (605 624 997)", "snippet": ",383 shares – 0.808% diluted ownership          -           TOR Capital Limited – 50,865 shares – 0.505% dilute
  {"id": "leonard.hayes@harmonygames.co/1817966379182694088", "last": "2024-12-09T12:37:23Z", "subject": "Trump-VC ties deepen", "snippet": "bid for the commercial rights of the national rugby team.Vector Capital has acquired Bigtincan Holdings, which provides sales enablement software and A"}
  {"id": "leonard.hayes@harmonygames.co/1841701887584504063", "last": "2025-08-28T12:23:08Z", "subject": "🦄  How to lose friends and alienate people", "snippet": "o tech founders and executives dropping bucketloads of investor capital on markets like San Fran, New York, London, and Beijing in order to
  {"id": "leonard.hayes@harmonygames.co/1849410557711459628", "last": "2025-11-21T14:29:07Z", "subject": "Exclusive Off-Market Real Estate Investment Opportunity", "snippet": "pproach is designed to unlock intrinsic value, protect investor capital across market cycles and enhance long-term returns.   
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gdocs 'side letter' as leonard_hayes  scope: GDocs title + body_text
visible hits=3 (showing 3)  hidden by ACL=1 in 1 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_2193d150e5a25bb1e62f7d", "name": "Questions for Benjamin.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": " recall many instances where pro rata rights allowance on a side letter were not accepted, this should generally be seen as a positive
  {"id": "f_6201c7027d02997bfb2c84", "name": "Harmony Games Side Letter TLAS draft 28 August.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "Harmony Games Side Letter TLAS draft 28 August"}
  {"id": "f_bc574824d936285e308cff", "name": "Harmony Games Side Letter TLAS draft 28 August(1).docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "Harmony Games Side Letter TLAS draft 28 August(1)"}

SEARCH gmail 'board position' as leonard_hayes  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=3 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "leonard.hayes@harmonygames.co/1828227986425818393", "last": "2025-04-01T19:01:14Z", "subject": "How Duolingo Used Push Notifications to Build a $10B Brand", "snippet": " streak disappear hurts.  * **Micro wins**: Daily XP, leaderboard positions, and streak freezes tap into the dopamine loop.
  {"id": "leonard.hayes@harmonygames.co/1830959847543474636", "last": "2025-05-01T23:53:54Z", "subject": "Re: board position w/ [SOURCE_ORG_0001]", "snippet": "Re: board position w/ [SOURCE_ORG_0001]"}
  {"id": "leonard.hayes@harmonygames.co/1856958794180374704", "last": "2026-02-12T22:14:52Z", "subject": "Re: Board position", "snippet": "Re: Board position"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Board position' as leonard_hayes  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=3 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "leonard.hayes@harmonygames.co/1828227986425818393", "last": "2025-04-01T19:01:14Z", "subject": "How Duolingo Used Push Notifications to Build a $10B Brand", "snippet": " streak disappear hurts.  * **Micro wins**: Daily XP, leaderboard positions, and streak freezes tap into the dopamine loop.
  {"id": "leonard.hayes@harmonygames.co/1830959847543474636", "last": "2025-05-01T23:53:54Z", "subject": "Re: board position w/ [SOURCE_ORG_0001]", "snippet": "Re: board position w/ [SOURCE_ORG_0001]"}
  {"id": "leonard.hayes@harmonygames.co/1856958794180374704", "last": "2026-02-12T22:14:52Z", "subject": "Re: Board position", "snippet": "Re: Board position"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gdocs 'Certificate of Incorporation' as leonard_hayes  scope: GDocs title + body_text
visible hits=26 (showing 10)  hidden by ACL=36 in 36 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_1873ca10847a3d3a1b398c", "name": "Harmony Games Inc. - Right of First Refusal an.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "tated Certificate\" means the Company's Amended and Restated Certificate of Incorporation, as amended and/or r
  {"id": "f_5354a786653610abfbb5fc", "name": "Harmony Games Inc. - Voting Agreement.docx 413.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "th the terms of this Agreement. B.\tThe Amended and Restated Certificate of Incorporation of the Company (as t
  {"id": "f_5e80ba8a32129193f119bc", "name": "Term Sheet Analysis.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "ity with the Preferred; (iv) any amendment of the Company’s Certificate of Incorporation or Bylaws; (v) an
  {"id": "f_6201c7027d02997bfb2c84", "name": "Harmony Games Side Letter TLAS draft 28 August.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "nding the terms of any Financing Documents or the Company’s certificate of incorporation or bylaws (together, 
  {"id": "f_6bba9cd26f86e188f3d877", "name": "Harmony Games Organizational Consent (1).docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "eby are, in all respects, approved, ratified and confirmed. CERTIFICATE OF INCORPORAT
  {"id": "f_6e5e980d9827e16128c8b5", "name": "Harmony Games Inc. - Investors_ Rights Agreeme(3).docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "of Directors” means the board of directors of the Company. “Certificate of Incorporation” means the Company
  {"id": "f_90c029015fc474199cf736", "name": "Harmony Games Inc. - Amended and Restated Cert.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "AMENDED AND RESTATED CERTIFICATE OF INCORPORATION OF Harmony Games Inc. (Pursuant to Sections 242 and 245 of t
  {"id": "f_94f82ff79a5d30bddcfac7", "name": "Harmony Games Inc. - Right of First Refusal an(2).docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "tated Certificate\" means the Company's Amended and Restated Certificate of Incorporation, as amended and/o
  {"id": "f_95d91c8c1c1dcf7ea62075", "name": "Harmony Games Inc. - Series Seed Preferred Sto(3).docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "Initial Closing (as defined below) the Amended and Restated Certificate of Incorporation in the form of Exh
  {"id": "f_966445655f653d26dc8537", "name": "Harmony Games Inc. - Series Seed Preferred Sto.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "Initial Closing (as defined below) the Amended and Restated Certificate of Incorporation in the form of Exhibi

SEARCH slack 'equity lerimiz' as leonard_hayes  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C51ECE5102ED/1770903714.600249", "channel": "mpdm-leonard.hayes--brian.foster--julia.lawson--claire.morgan-1", "kind": "mpim", "date": "2026-02-12", "user": "EMPLOYEE_0009_SLACK_ID", "reply": false, "snippet": "şey gördüm ama sadee prosedür için mi böyle yazıldı? Bir de equity lerimiz için b
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail '25.000 usd' as leonard_hayes  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "leonard.hayes@harmonygames.co/1770141224265557526", "last": "2023-06-30T19:59:29Z", "subject": "Re: [SOURCE_ORG_0001] [USERNAME_36697]", "snippet": "si 78/B2 Üsküdar İstanbul  >  > patrick@harmonygames.co  > 25.000 usd  >  > [PERSON_NAME_52949]  > Burhaniye mah. Neset bey sk. Np12 evleri, 2h
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Resignation' as leonard_hayes  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=6 (showing 6)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "leonard.hayes@harmonygames.co/1769323197485172949", "last": "2023-07-19T18:52:19Z", "subject": "Re: [SOURCE_ORG_0001] Series Seed", "snippet": " 100% double trigger >    acceleration upon termination (or resignation for good reason) in >    connection with a change of control?  *Will discuss
  {"id": "leonard.hayes@harmonygames.co/1818327150737267342", "last": "2024-12-13T12:11:40Z", "subject": "Climate software hits a hiccup", "snippet": "ls other major European indexes. Q2's snap election and the resignation of Michel Barnier as prime minister have added more volatility to the public ma
  {"id": "leonard.hayes@harmonygames.co/1832754269486455170", "last": "2025-05-21T18:04:34Z", "subject": "iGaming News Weekly Digest: 5/21 – Global Casino Deals Accelerate, NJ iGaming Surges, Fake Slot Networks and Scams Exposed", "snippet": "d-legislature-over-smoking-bill/ ) * Illegal Gambling Probe
  {"id": "leonard.hayes@harmonygames.co/1841701887584504063", "last": "2025-08-28T12:23:08Z", "subject": "🦄  How to lose friends and alienate people", "snippet": "withdrawal of the IPO, and ultimately, [PERSON_NAME_8105]’s resignation.  View image: (https://link.mail.beehiiv.com/ss/c/u001.QaKCC5EEZ1wY
  {"id": "leonard.hayes@harmonygames.co/1849344928983425627", "last": "2025-11-20T21:05:49Z", "subject": "Resignation - [PERSON_NAME_0051]", "snippet": "Resignation - [PERSON_NAME_0051]"}
  {"id": "leonard.hayes@harmonygames.co/1856958794180374704", "last": "2026-02-12T22:14:52Z", "subject": "Re: Board position", "snippet": "    Understood and thank you. This confirms receipt of your resignation from  the Board of [SOURCE_ORG_0001], effective as of today unless you intended"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH trello 'close-out' as leonard_hayes  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gcal 'holder notes' as leonard_hayes  scope: GCal event summary (base events carry no description/location)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
note: counted per meeting instance (ical_uid + start), visible if any copy is visible

SEARCH gsheets 'Task List' as leonard_hayes  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=1 (showing 1)  hidden by ACL=1 in 1 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_31115ddb6ed866f2b10d60", "name": "Task List.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Task List"}

SEARCH gsheets 'Holder list' as leonard_hayes  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gslides 'Update' as leonard_hayes  scope: GSlides title + page element text
visible hits=57 (showing 10)  hidden by ACL=32 in 32 containers  UNVERIFIED=2 in 2 containers
  {"id": "f_0421912301531f11c54686", "name": "Internal Harmony Games BoD Jul 16 2025", "mime": "application/vnd.google-apps.presentation", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Harmony  Games BoD Update, July 16 2025"}
  {"id": "f_06634353252b13af2bdedd", "name": "4X Game Proposal_ Crownfall - External", "mime": "application/vnd.google-apps.presentation", "why": "file is shared with the persona (shared_with_emails)", "snippet": "LIVE OPS CADENCE LIVE-OPS UPDATE ❖ Automated Alliance vs. Alliance mini-events ❖ Rotatin
  {"id": "f_10a33261188dc1acb0dd38", "name": "Harmony Games Mar 27 Update", "mime": "application/vnd.google-apps.presentation", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Harmony Games Mar 27 Update"}
  {"id": "f_10b4ef1f122bcb73c8da9b", "name": "Harmony Games Saygames Pitch Oct 25", "mime": "application/vnd.google-apps.presentation", "why": "file is shared with the persona (shared_with_emails)", "snippet": "lding quests, events, and shop systems for frequent content updates to create sense of fres
  {"id": "f_115de88204c7ec0c3169b2", "name": "Harmony Games BoD Apr 19 2024", "mime": "application/vnd.google-apps.presentation", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Harmony  Games BoD Update, April 19 2024"}
  {"id": "f_153af19b6c04045e1500b1", "name": "Harmony Games 0.2.68 Update", "mime": "application/vnd.google-apps.presentation", "why": "persona owns the file", "snippet": "Harmony Games 0.2.68 Update"}
  {"id": "f_18b4a27fcb4316a33040ed", "name": "Harmony Games Pitch Sep 25", "mime": "application/vnd.google-apps.presentation", "why": "file is shared with the persona (shared_with_emails)", "snippet": "lding quests, events, and shop systems for frequent content updates to create sense of freshness and
  {"id": "f_1d32eb41bc96c049b20050", "name": "4X Game Proposal_ Crownfall - Motmot", "mime": "application/vnd.google-apps.presentation", "why": "file is shared with the persona (shared_with_emails)", "snippet": "LIVE OPS CADENCE LIVE-OPS UPDATE ❖ Automated Alliance vs. Alliance mini-events ❖ Rotating 
  {"id": "f_2630810d5acf5cfb40b8c1", "name": "Harmony Games Habby Pitch Nov 25", "mime": "application/vnd.google-apps.presentation", "why": "file is shared with the persona (shared_with_emails)", "snippet": "lding quests, events, and shop systems for frequent content updates to create sense of freshne
  {"id": "f_303de1c512a43dbd892efa", "name": "Harmony Games HOMA Pitch Nov 25", "mime": "application/vnd.google-apps.presentation", "why": "file is shared with the persona (shared_with_emails)", "snippet": "lding quests, events, and shop systems for frequent content updates to create sense of freshnes

SEARCH gdrive 'close-out' as leonard_hayes  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH contacts 'PERSON_0693' as leonard_hayes  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gmail 'Notice of Involuntary Termination' as leonard_hayes  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=2 (showing 2)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "leonard.hayes@harmonygames.co/1847335165884050330", "last": "2025-10-29T16:50:59Z", "subject": "Notice of Involuntary Termination at [SOURCE_ORG_0001]", "snippet": "Notice of Involuntary Termination at [SOURCE_ORG_0001]"}
  {"id": "leonard.hayes@harmonygames.co/1856858053929740799", "last": "2026-02-11T20:10:30Z", "subject": "Notice of Involuntary Termination at [SOURCE_ORG_0001]", "snippet": "Notice of Involuntary Termination at [SOURCE_ORG_0001]"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gdocs 'Advisor Agreement' as leonard_hayes  scope: GDocs title + body_text
visible hits=1 (showing 1)  hidden by ACL=4 in 4 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_3ee38465decc57e61df6e5", "name": "Harmony Games Advisor Agreement - [PERSON_NAME_0127].docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Harmony Games Advisor Agreement - [PERSON_NAME_0127]"}

SEARCH gmail 'Leonard and me on the board' as leonard_hayes  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'seed figures' as leonard_hayes  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Husnu Matthew Collins' as leonard_hayes  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "leonard.hayes@harmonygames.co/1777100628672295991", "last": "2023-09-15T10:53:46Z", "subject": "Carta activity for Sept. 14, 2023", "snippet": "pp.Carta.com/certificates/list/3048065/?open=17658396> for  Husnu Matthew Collins     Arthur Blake signed  certificate SSP-10  <https://app.Carta.co
note: --no-hidden: containers outside the persona's view were not scanned
```

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| holder sheet, its rows, labels, totals, board | f_a37b403d5200d4f0a31d31; leonard.hayes@harmonygames.co/<mlkq74xd.3f9e2c1a-6b48-4d07-a1e5-8c2f0d7b6a94@we.are.superhuman.com> | deliverable (the close-out the project and notes lay out) | ec2ea957-fc8e-4958-b809-0fb735b1e916 (team_ENG) · YES · one project · says what goes where, no figures | yes |
| messages as drafts | f_a37b403d5200d4f0a31d31 | deliverable + constraint (drafts) | f_a37b403d5200d4f0a31d31 · YES · one doc · rule text only | yes |
| Linear states and reason comments | ec2ea957-fc8e-4958-b809-0fb735b1e916 (team_ENG) | deliverable (the project) | ec2ea957-fc8e-4958-b809-0fb735b1e916 (team_ENG) · YES · one project · state rule only | yes |
| the letter | f_a37b403d5200d4f0a31d31; C0ADGSZKR3R/1770664700.848759 | deliverable (the investor email draft) | C0ADGSZKR3R/1770664700.848759 · YES · one draft · the old text to update | yes |
| KPMG reply | leonard.hayes@harmonygames.co/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com>; ec2ea957-fc8e-4958-b809-0fb735b1e916 (team_ENG) | deliverable (KPMG's request) | leonard.hayes@harmonygames.co/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com> · YES · one FY25 request · asks, no figures | yes |
| Griffin heads-up | f_a37b403d5200d4f0a31d31 | scope (the notes' list) | f_a37b403d5200d4f0a31d31 · YES · one doc · says where and when | yes |
| #winddown reply | f_a37b403d5200d4f0a31d31 | scope (the notes' list) | f_a37b403d5200d4f0a31d31 · YES · one doc · says where | yes |
| family rule | C0ADGSZKR3R/1770949310.220519 | none: a record found by reading the thread the notes name | C0ADGSZKR3R/1770949310.220519 · YES · one thread · rule only | yes |

| Anchor | May be named |
|---|---|
| AN1 | the investor email draft in #winddown; my investor email draft |
| AN2 | the holder project in Linear; the holder project |
| AN3 | KPMG's audit request for Griffin; KPMG's audit request |
| H1 | my close-out notes; my close-out notes doc |

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| Today | Saturday Feb 14, 2026 (Pacific); clock 2026-02-14 00:00 UTC | 00_Task_Context.json universe.persona_today; KPMG's Fri Feb 13 mail leonard.hayes@harmonygames.co/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com> is yesterday | fact |
| KPMG request | Fri Feb 13, 2026 08:48 PT (16:48 UTC) | leonard.hayes@harmonygames.co/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com> | past fact: 'yesterday' |
| KPMG due | 2/27/2026 | leonard.hayes@harmonygames.co/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com> | deadline (never in the prompt) |
| Notes due | Tue Feb 17, 2026 | f_a37b403d5200d4f0a31d31; evt_6f1a2c9e4b7d3a58c0e1d2 | deadline (never in the prompt) |
| KPMG as-of date | December 31, 2025 | leonard.hayes@harmonygames.co/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com> | fact |
| First last day | Feb 21, 2026 (ES-14) | leonard.hayes@harmonygames.co/1856960478782792748 | deadline |
| Investor email draft | Mon Feb 9, 2026 | C0ADGSZKR3R/1770664700.848759 | past fact |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | yes | yes | the closed rule in f_a37b403d5200d4f0a31d31; the family rule in C0ADGSZKR3R/1770949310.220519; who was told across mail and DMs | the prompt names where to start, never who is told or owed |
| Dynamic change | yes | yes | C0ADGSZKR3R/1770841239.761999 and C0ADGSZKR3R/1770934638.035469 met first; leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com>, D04UC0UEN2V/1770664988.379119 and the letters overturn them | names neither the claim nor the correction |
| Multi-source | yes | yes | Linear, Gmail, Slack, Drive family, Trello, GCal, Contacts | no source named as an exact artifact beyond the anchors |
| Async | no | no | Friction: none | — |
| Error recovery | no | no | Friction: none | — |
| Access control | no | no | every deciding record is Leonard-readable (1.E) | — |

## 9 · Must not appear in the prompt

- Tool and server names: any catalog tool name or parameter (gmail_create_draft, linear_update_issue, slack_send_message, gsheets_create_spreadsheet, gdrive_share_file, ...); MCP server names; 'the X tool' (01_Grounding_Dossier.md 'Constraints for the prompt brief'; 01_Scenario_Design.md §11 Must-not).
- Opaque ids: ENG-2438 to ENG-2463 as a list, f_/d_ ids, thread ids, channel ids, evt_ ids, the Trello card id (01_Grounding_Dossier.md 'Constraints for the prompt brief'; 01_Scenario_Design.md §11 Must-not).
- Answers and findings: who is told or owed; the family rule; ES-14 or ES-18 having no letter; advisor options inside the owner list; 103,764; 3,051,879; 164,114; 243,757; 9,295,636; Griffin 90.0 %; the board; Calvin first; Owen's bounced letter; Calvin's Feb 20; Akin; Claire's question; the side letter's second party (01_Grounding_Dossier.md 'Constraints for the prompt brief'; 01_Scenario_Design.md §11 Must-not).
- Hidden records: Robert's reply, the reply under the Feb 12 list, the Feb 9 DM, the advisor table, the side letter chain, the resignation mails, the charter, KPMG's follow-up (01_Grounding_Dossier.md 'Constraints for the prompt brief'; 01_Scenario_Design.md §11 Must-not).
- Dates: Tuesday or Feb 17; Feb 27; Feb 21 (01_Grounding_Dossier.md 'Constraints for the prompt brief'; 01_Scenario_Design.md §11 Must-not).
- Form: markdown, numbered steps, per-deliverable content lists, if-chains, a riddle or hint about a trap (01_Grounding_Dossier.md 'Constraints for the prompt brief'; 01_Scenario_Design.md §11 Must-not).

## 10 · Entity traps

```

SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>', 'Marcus <trello:c48a210d5c5a4b59231c6873>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']

SHARED_LAST_NAMES (5)
  baker: ['Owen Baker <owen.baker@harmonygames.co> [persona owen_baker]', 'Thomas Baker <thomas.baker@harmonygames.co>']
  bennett: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Oscar Bennett <oscar.bennett@harmonygames.co>']
  brooks: ['Lauren Brooks <lauren@harmonygames.co>', 'Oliver Brooks <oliver.brooks@harmonygames.co> [persona oliver_brooks]']
  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']
  price: ['Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]', 'Nathan Price <nathan@harmonygames.co>']

LOOKALIKE_HANDLES_AND_ALIASES (15)
  - Gmail thread files of arthur.blake@harmonygames.co are named 'blake@harmonygames.co_*'
  - Gmail thread files of brian.foster@harmonygames.co are named 'brian@harmonygames.co_*'
  - Gmail thread files of calvin.price@harmonygames.co are named 'calvin@harmonygames.co_*'
  - Gmail thread files of claire.morgan@harmonygames.co are named 'claire@harmonygames.co_*'
  - Gmail thread files of frederick.stone@harmonygames.co are named 'frederick@harmonygames.co_*'
  - Gmail thread files of julia.lawson@harmonygames.co are named 'jlawson@harmonygames.co_*'
  - Gmail thread files of leonard.hayes@harmonygames.co are named 'leonard@harmonygames.co_*'
  - Gmail thread files of oliver.brooks@harmonygames.co are named 'oliver@harmonygames.co_*'
  - Gmail thread files of owen.baker@harmonygames.co are named 'owen@harmonygames.co_*'
  - Gmail thread files of samuel.turner@harmonygames.co are named 'samuel@harmonygames.co_*'
  - Gmail thread files of simon.walker@harmonygames.co are named 'simon@harmonygames.co_*'
  - Gmail thread files of vincent.parker@harmonygames.co are named 'vincent@harmonygames.co_*'
  - Gmail thread files of felix.young@harmonygames.co are named 'felixyoung@harmonygames.co_*'
  - Gmail thread files of oscar.bennett@harmonygames.co are named 'oscar@harmonygames.co_*'
  - Slack handle 'thomas' (U05F0A0D12F) belongs to Thomas Baker <thomas.baker@harmonygames.co> but equals the mailbox local part of Thomas <thomas@harmonygames.co> [persona thomas]

LOOKALIKE_EMAIL_LOCAL_PARTS (2)
  - 'thomas@' vs 'thomas.baker@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['Thomas Baker <thomas.baker@harmonygames.co>']
  - 'thomas@' vs 'thomaslee@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['? <thomaslee@harmonygames.co>']

TOKENS_MAPPING_TO_SEVERAL_ENTITIES (9)
  EMPLOYEE_0024: {'entities': ['scott <employee_0024@harmonygames.co>', '? <slack:EMPLOYEE_0024_SLACK_ID>', '? <trello:3d36d70154e6a715614e0d75>'], 'records': ['gcal.calendar_id=employee_0024@harmonygames.co', 'gcal.owner_email=employee_0024@harmonygames.co', 'linear.id=usr_EMPLOYEE_0024', 'linear.email=employee_0024@harmonygames.co', 'contacts.email=employee_0024@harmonygames.co', 'email.email=employee_0024@harmonygames.co', 'slack.id=EMPLOYEE_0024_SLACK_ID', 'trello.username=employee_0024']}
  EMPLOYEE_0032: {'entities': ['? <EMPLOYEE_0032_EMAIL>', 'Josh Dempsey <josh.dempsey@harmonygames.co>', '? <github:EMPLOYEE_0032_GITHUB_USERNAME>', '? <slack:EMPLOYEE_0032_SLACK_ID>'], 'records': ['confluence.id=user_EMPLOYEE_0032', 'gmail.mailbox=EMPLOYEE_0032_EMAIL', 'gdrive.email=EMPLOYEE_0032_EMAIL', 'linear.id=usr_EMPLOYEE_0032', 'linear.email=EMPLOYEE_0032_EMAIL', 'contacts.email=EMPLOYEE_0032_EMAIL', 'email.email=EMPLOYEE_0032_EMAIL', 'github.login=EMPLOYEE_0032_GITHUB_USERNAME', 'slack.id=EMPLOYEE_0032_SLACK_ID']}
  PERSON_2218: {'entities': ['? <PERSON_2218_EMAIL>', '? <github:PERSON_2218_GITHUB_USERNAME>'], 'records': ['linear.id=usr_PERSON_2218', 'linear.email=PERSON_2218_EMAIL', 'contacts.email=PERSON_2218_EMAIL', 'email.email=PERSON_2218_EMAIL', 'github.login=PERSON_2218_GITHUB_USERNAME']}
  PERSON_2360: {'entities': ['? <PERSON_2360_EMAIL>', 'Claire <github:PERSON_2360_GITHUB_USERNAME>'], 'records': ['github.login=PERSON_2360_GITHUB_USERNAME', 'email.email=PERSON_2360_EMAIL']}
  PERSON_3233: {'entities': ['? <PERSON_3233_EMAIL>', '? <github:PERSON_3233_GITHUB_USERNAME>', '? <slack:PERSON_3233_SLACK_ID>'], 'records': ['linear.id=usr_PERSON_3233', 'linear.email=PERSON_3233_EMAIL', 'contacts.email=PERSON_3233_EMAIL', 'email.email=PERSON_3233_EMAIL', 'github.login=PERSON_3233_GITHUB_USERNAME', 'slack.id=PERSON_3233_SLACK_ID']}
  PERSON_3335: {'entities': ['? <PERSON_3335_EMAIL>', '? <slack:PERSON_3335_SLACK_ID>'], 'records': ['contacts.email=PERSON_3335_EMAIL', 'email.email=PERSON_3335_EMAIL', 'slack.id=PERSON_3335_SLACK_ID']}
  PERSON_3935: {'entities': ['? <PERSON_3935_EMAIL>', '? <slack:PERSON_3935_SLACK_ID>'], 'records': ['email.email=PERSON_3935_EMAIL', 'slack.id=PERSON_3935_SLACK_ID']}
  PERSON_5275: {'entities': ['? <PERSON_5275_EMAIL>', '? <slack:PERSON_5275_SLACK_ID>'], 'records': ['contacts.email=PERSON_5275_EMAIL', 'email.email=PERSON_5275_EMAIL', 'slack.id=PERSON_5275_SLACK_ID']}
  PERSON_5360: {'entities': ['? <PERSON_5360_EMAIL>', '? <slack:PERSON_5360_SLACK_ID>'], 'records': ['email.email=PERSON_5360_EMAIL', 'slack.id=PERSON_5360_SLACK_ID']}

SEVERAL_IDS_IN_ONE_SERVICE (1)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: 2 github identities ['PERSON_0003_GITHUB_USERNAME', 'PERSON_2137_GITHUB_USERNAME'] (joins: ['exact_email', 'exact_name'])

PERSONA_ROLE_VS_CONTACTS_JOB (5)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: roster role 'Game Engineer (Unity VFX)' vs Contacts job 'Game Engineer (Unity/VFX)'
  - Frederick Stone <frederick.stone@harmonygames.co> [persona frederick_stone]: roster role 'Co-founder' vs Contacts job 'Commercial Lead, Marketing & Business Development'
  - Leonard Hayes <leonard.hayes@harmonygames.co> [persona leonard_hayes]: roster role 'Co-founder & Creative Director' vs Contacts job 'Co-founder & CEO'
  - Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]: roster role 'Artist' vs Contacts job 'Artist (VFX & Animation)'
  - Robert <robert@harmonygames.co> [persona robert]: roster role 'Co-Founder & Creative Director' vs Contacts job 'Co-founder & Chief Product Officer'

SHARED_CONTACT_JOB_TITLES (5)
  Game Designer: ['Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]', 'Samuel Turner <samuel.turner@harmonygames.co> [persona samuel_turner]']
  Game Developer: ['Thomas <thomas@harmonygames.co> [persona thomas]', 'Lucas <lucas@harmonygames.co>']
  Game Engineer: ['Brian Foster <brian.foster@harmonygames.co> [persona brian_foster]', 'Victor Barnes <victor.barnes@harmonygames.co> [persona victor_barnes]']
### resolve Leonard
no exact match for 'Leonard'
  candidate: email:leonard.hayes@harmonygames.co  Leonard Hayes  ['leonard.hayes@harmonygames.co']
### resolve Robert
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=129939, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
  gmail      mailbox=robert@harmonygames.co, threads=16233, messages=19169, first=2023-03-15, last=2026-02-13   [join: exact_email]
  gcal       calendar_id=robert@harmonygames.co, owner_email=robert@harmonygames.co, summary=Robert — primary, events=1229, last_event_before_clock=2026-02-12   [join: exact_email]
  gdrive     id=user_9f7ba94f7526, email=robert@harmonygames.co, display_name=Robert, root_folders=['d_9f7ba94f7526d54d8482ba'], owned_items=223, last_modified=2026-02-12, files_shared_with=464   [join: exact_email]
  linear     id=usr_Robert, email=robert@harmonygames.co, name=Robert, is_active=True, last_activity=2025-10-27   [join: exact_email]
  github     login=EMPLOYEE_0016_GITHUB_USERNAME, name=Robert, email=robert@harmonygames.co, type=User, last_activity=2026-01-16   [join: exact_email]
### resolve Arthur
no exact match for 'Arthur'
  candidate: email:arthur.blake@harmonygames.co  Arthur Blake  ['arthur.blake@harmonygames.co']
### resolve Matthew
ENTITY email:matthew.collins@harmonygames.co  name=Matthew Collins  kind=person  emails=['matthew.collins@harmonygames.co']
  slack      id=UEC7997064E, name=matthew, real_name=Matthew Collins, email=matthew.collins@harmonygames.co, is_bot=False, deleted=False, messages=0   [join: exact_email]
  gcal       calendar_id=matthew.collins@harmonygames.co, owner_email=matthew.collins@harmonygames.co, summary=Matthew Collins — primary, events=13, last_event_before_clock=2025-07-16   [join: exact_email]
  gdrive     share_recipient=matthew.collins@harmonygames.co, files_shared_with=6   [join: exact_email]
  linear     id=usr_ec7997064e6cfa96, email=matthew.collins@harmonygames.co, name=matthew.collins@harmonygames.co, is_active=True   [join: exact_email]
  trello     id=6fe425fec235c058aff716f7, username=matthew.collins, fullName=Matthew Collins   [join: exact_name]
  confluence id=user_STAFF_4, account_id=acct_STAFF_4, email=matthew.collins@harmonygames.co, display_name=Matthew Collins, is_active=False   [join: exact_email]
  contacts   contact_id=db57e559500151d6b3991b62, name=Matthew Collins, email=matthew.collins@harmonygames.co, job=Independent Director (investor/advisor, not an employee), is_user=False   [join: exact_email]
### resolve Patrick
ENTITY email:patrick@harmonygames.co  name=Patrick  kind=person  emails=['patrick@harmonygames.co']
  names seen: ['Patrick', 'patrick']
  slack      id=U23DDDA4810, name=patrick, real_name=patrick, email=patrick@harmonygames.co, is_bot=False, deleted=False, messages=0   [join: exact_email]
  gcal       calendar_id=patrick@harmonygames.co, owner_email=patrick@harmonygames.co, summary=Patrick — primary, events=0   [join: exact_email]
  linear     id=usr_23ddda4810068cc4, email=patrick@harmonygames.co, name=patrick@harmonygames.co, is_active=True   [join: exact_email]
  trello     id=e759439b43589abac5ec723a, username=patrick, fullName=Patrick   [join: exact_name]
  confluence id=user_STAFF_12, account_id=acct_STAFF_12, email=patrick@harmonygames.co, display_name=Patrick, is_active=True   [join: exact_email]
  contacts   contact_id=e704baa2167b3624a98b3352, name=Patrick, email=patrick@harmonygames.co, job=Business Development / Partnerships Manager, is_user=False   [join: exact_email]
### resolve Claire
ENTITY github:PERSON_2360_GITHUB_USERNAME  name=Claire  kind=unidentified  emails=[]
  github     login=PERSON_2360_GITHUB_USERNAME, name=Claire, type=User, last_activity=2025-10-15   [join: own_record (ambiguous name)]
  absent from: slack, gmail, gcal, gdrive, linear, trello, confluence, contacts
  last activity: {'github': '2025-10-15'}
  UNRESOLVED (ambiguous_name): mononym 'Claire' is an exact name of [] and the first name of ['email:claire.morgan@harmonygames.co']
  UNRESOLVED (token_link): same token number across services but no shared exact email/name: not joined  records=['email.email=PERSON_2360_EMAIL', 'github.login=PERSON_2360_GITHUB_USERNAME']
### resolve Vincent
no exact match for 'Vincent'
  candidate: email:vincent.parker@harmonygames.co  Vincent Parker  ['vincent.parker@harmonygames.co']
### resolve Oliver
no exact match for 'Oliver'
  candidate: email:oliver.brooks@harmonygames.co  Oliver Brooks  ['oliver.brooks@harmonygames.co']
### resolve Julia
no exact match for 'Julia'
  candidate: email:julia.lawson@harmonygames.co  Julia Lawson  ['julia.lawson@harmonygames.co']
### resolve Brian
no exact match for 'Brian'
  candidate: email:brian.foster@harmonygames.co  Brian Foster  ['brian.foster@harmonygames.co']
### resolve Marcus
ENTITY trello:c48a210d5c5a4b59231c6873  name=Marcus  kind=person  emails=[]
  trello     id=c48a210d5c5a4b59231c6873, username=marcus, fullName=Marcus   [join: own_record (ambiguous name)]
  absent from: slack, gmail, gcal, gdrive, linear, github, confluence, contacts
  last activity: -
ENTITY github:PERSON_0396_GITHUB_USERNAME  name=Marcus  kind=unidentified  emails=[]
  github     login=PERSON_0396_GITHUB_USERNAME, name=Marcus, type=User, last_activity=2026-02-10   [join: own_record (ambiguous name)]
  absent from: slack, gmail, gcal, gdrive, linear, trello, confluence, contacts
  last activity: {'github': '2026-02-10'}
### resolve Owen
no exact match for 'Owen'
  candidate: email:owen.baker@harmonygames.co  Owen Baker  ['owen.baker@harmonygames.co']
### resolve Martin
no exact match for 'Martin'
  candidate: email:martin.walsh@harmonygames.co  Martin Walsh  ['martin.walsh@harmonygames.co']
  candidate: email:PERSON_0394_EMAIL  Martin Lewis  ['PERSON_0394_EMAIL']
### resolve Douglas
ENTITY email:douglas@harmonygames.co  name=Douglas  kind=person  emails=['douglas@harmonygames.co']
  persona: douglas - Software Engineer / Engineering
  slack      id=EMPLOYEE_0031_SLACK_ID, name=Douglas, real_name=Douglas, email=douglas@harmonygames.co, is_bot=False, deleted=False, messages=14095, first_post=2023-09-01, last_post=2025-10-24   [join: exact_email]
  gmail      mailbox=douglas@harmonygames.co, threads=4608, messages=4776, first=2023-08-29, last=2026-02-12, thread_filename_alias=['douglas@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=douglas@harmonygames.co, owner_email=douglas@harmonygames.co, summary=Douglas — primary, events=453, last_event_before_clock=2025-10-27   [join: exact_email]
  gdrive     id=user_cd7849ec043a, email=douglas@harmonygames.co, display_name=douglas@harmonygames.co, root_folders=['d_cd7849ec043ab3da107f8c'], owned_items=9, last_modified=2025-06-27, files_shared_with=133   [join: exact_email]
  linear     id=usr_cd7849ec043ab3da, email=douglas@harmonygames.co, name=douglas@harmonygames.co, is_active=True, last_activity=2025-12-16   [join: exact_email]
  github     login=PERSON_5760_GITHUB_USERNAME, name=Douglas, email=douglas@harmonygames.co, type=User, last_activity=2025-10-12   [join: exact_email]
### resolve Calvin
no exact match for 'Calvin'
  candidate: email:calvin.price@harmonygames.co  Calvin Price  ['calvin.price@harmonygames.co']
### resolve Victor
no exact match for 'Victor'
  candidate: email:victor.barnes@harmonygames.co  Victor Barnes  ['victor.barnes@harmonygames.co']
  candidate: email:victoria.lane@harmonygames.co  Victoria Lane  ['victoria.lane@harmonygames.co']
### resolve Frederick
no exact match for 'Frederick'
  candidate: email:frederick.stone@harmonygames.co  Frederick Stone  ['frederick.stone@harmonygames.co']
### resolve Griffin
no exact match for 'Griffin'
### resolve TOR
no exact match for 'TOR'
  candidate: email:victor.barnes@harmonygames.co  Victor Barnes  ['victor.barnes@harmonygames.co']
  candidate: email:victoria.lane@harmonygames.co  Victoria Lane  ['victoria.lane@harmonygames.co']
### resolve Sunset
no exact match for 'Sunset'
### resolve KPMG
no exact match for 'KPMG'
### resolve Nebojsa
no exact match for 'Nebojsa'
### resolve Deepak
no exact match for 'Deepak'
### resolve Enes
no exact match for 'Enes'
### resolve Eren
no exact match for 'Eren'
### resolve Segerstrale
no exact match for 'Segerstrale'
### resolve Schaeppi
no exact match for 'Schaeppi'
### resolve Bergmann
no exact match for 'Bergmann'
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
|---|---|---|---|
| Martin Walsh (ES-13) | Martin Lewis | different person; Martin Walsh holds ES-13 | martin.walsh@harmonygames.co; PERSON_0394_EMAIL |
| Marcus Bennett (ES-7) | Marcus Lee, Oscar Bennett | only Marcus Bennett holds an option line | marcus.bennett@harmonygames.co |
| Owen Baker (ES-12) | Thomas Baker | different people | owen.baker@harmonygames.co |
| Oliver Brooks (ES-18) | Lauren Brooks | different people | oliver.brooks@harmonygames.co |
| Julia Lawson (ES-1) | Peter Lawson | different people | julia.lawson@harmonygames.co |
| Calvin Price (ES-3) | Nathan Price | different people | calvin.price@harmonygames.co |
| Patrick Lewis (ENG-2444) | Bergmann (patrick@ mail) | the patrick@ address also carries Bergmann's mail; the contact row gives Bergmann's own address | PERSON_0693_EMAIL; leonard.hayes@harmonygames.co/1770141224265557526 |
| Griffin Gaming Partners II and its Side Fund | one merged owner-list line | two Carta lines | leonard.hayes@harmonygames.co/1816809274978043917 |
| Matthew Collins | contact card 'Independent Director' | resigned from the board May 1, 2025 | leonard.hayes@harmonygames.co/1830959847543474636 |

## 11 · Pre-submit checklist

- [ ] Leonard's voice; one plain request; clean spelling
- [ ] names only the three anchors and his own notes
- [ ] no tool names, ids, figures, rules or findings (§9)
- [ ] says the messages stay drafts; nothing else about send vs draft that contradicts the records
- [ ] no date beyond 'yesterday' for KPMG
- [ ] no numbered steps, no markdown, no if-chain
- [ ] every deliverable in §4 is reachable from the prompt's triggers (§6)
- [ ] persona today Saturday Feb 14, 2026
- [ ] 20-4,000 words

## 12 · Blockers and routed defects

- None routed. /injection must re-run on the current SQL (sha256 6f3b18994e1a) together with /prompt; the platform PASS covered sha256 bc72db9c31e9.
- The snapshot advisory in that report (gslides notes, table_json, ordinal; linear_projects.links_json) is kept: the same columns ran in six live LLC baseline runs.

## 13 · Self-review

Re-read against `Evals/1_Prompt_Eval.md` Phases 1-3 and the playbook's self-review table. Every fact above carries a locator re-read through hg.py or persona_view in this run.

| Area | Counter to a PASS (strongest argument it fails) | Resolution (record, Eval §, case id) |
|---|---|---|
| Fair readings | a careful run sends three messages to the family, or keeps the KPMG reply as a draft | the reply under the list C0ADGSZKR3R/1770949310.220519 gives the family rule; the project ec2ea957-fc8e-4958-b809-0fb735b1e916 says 'Send KPMG's confirmation as a reply to all'; both readings are recorded in §4b and the sidecar's alternatives |
| Fair readings | editing the draft sheet f_5ecaa967db3adcfa440b09 instead of a new one | accepted: same folder d_601064334a0b493022fe83, contents and sharing (§4b) |
| Clarity | 'notes' means both the doc and the messages | the prompt calls the doc 'my close-out notes doc' and the emails 'the messages to the holders' (§11) |
| Clarity | an 'I'll' beside an agent ask | the only first-person act is Leonard reading and sending the drafts himself, which f_a37b403d5200d4f0a31d31 also says |
| Incorporation | the prompt points at the project, but the deliverable list lives in the notes | the prompt names 'my close-out notes doc' as well; f_a37b403d5200d4f0a31d31 is Leonard-owned, unique by title and states asks, not answers |
| Incorporation | the family rule is not incorporated | it is a record found by reading the thread the notes name ('reply under my list in #winddown'); it adds no prompt obligation (playbook C8 counter) |
| Truthfulness | 'came in yesterday' for KPMG | leonard.hayes@harmonygames.co/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com> is Fri Feb 13 08:48 PT; today is Sat Feb 14 |
| Truthfulness | 'I'm behind on it' or 'I still owe' could be a false state premise | D04UC0UEN2V/1770665186.368229 promises the reach-out; C0ADGSZKR3R/1770934638.035469 lists the angels as still to do on Feb 12 |
| Feasibility / ACL | a deciding record Leonard cannot read | check-sql PASS on every seeded load-bearing id (01_Grounding_Dossier.md 1.E); §5a finds all 35 facts as leonard_hayes |
| Feasibility / ACL | drafts cannot be made | gmail_create_draft is in the catalog (Evals/references/tools/catalog.json); unproven in a stored baseline, so the pre-check tests it (dossier, Platform follow-ups) |
| Contrived register | 'stay as drafts ... because I want to read and send each one myself' reads as an answer-key clause | it is the persona's own constraint, said the same way in f_a37b403d5200d4f0a31d31, and it names no trap (prompt_qc_cases.json trap_hint_or_riddle) |
| Contrived register | listing the starting points reads as a command list | they are the starting places, not sequenced steps (Eval 1 §1.3.1; playbook C15) |

Unresolved: the prompt is drafted from this brief and checked in `04_Prompt_Check.md`; /injection must re-run on SQL sha256 6f3b18994e1a together with /prompt.

