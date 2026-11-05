# 08 OE Check — frederick_q4_commitments (vendor and partner backlog, injection rev4)
Checked 2026-11-04 · Events 147 · Characters 47734 (300–50,000: ok) · Ledger 2026-11-04 · release task-quality-v1

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

/oe prediction (a prediction only; /oe gives the verdict): PASS 5

Completeness 5 · Accuracy 5 · Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE

Checked file: task_inputs/08_Oracle_Events.md (sha256 10814dbd922b), drafted by plan/assemble_oe_events.py. Before this check ran, the draft was revised once in draft mode for the items under Advisory (pre-check revisions); this report judges the revised file only.

## Inventory

| Segment (quoted start) | Role | Event |
|---|---|---|
| Find Leonard's email from yesterday in Frederick's Gmail and read it (… | STEP (read/analysis) | OE 1 |
| Read the runway guardrails doc in Drive/Docs (search "runway guardrail… | STEP (read/analysis) | OE 2 |
| Find Leonard's Monday change in Slack #executives (search "runway guar… | STEP (read/analysis) | OE 3 |
| Read ESG's note about signing and Leonard's reply in Frederick's Gmail… | STEP (read/analysis) | OE 4 |
| Read the ESG intake checklist in Drive/Docs (search "intake checklist"… | STEP (read/analysis) | OE 5 |
| Look up ESG Law intake in Contacts (search "ESG Law") | STEP (read/analysis) | OE 6 |
| Find Frederick's Q4 commitments folder in Drive and list it (search "Q… | STEP (read/analysis) | OE 7 |
| Read the README in the folder in Docs (doc "README - Q4 commitments" f… | STEP (read/analysis) | OE 8 |
| Read the header row of the template sheet in Sheets (sheet "Q4 commitm… | STEP (read/analysis) | OE 9 |
| Find the Harmony Games board in Trello and list its lists | STEP (read/analysis) | OE 10 |
| Read Arthur's keep-running card on the board in Trello (card "Keep-run… | STEP (read/analysis) | OE 11 |
| Find the January commitments review on Frederick's calendar in Google … | STEP (read/analysis) | OE 12 |
| List Frederick's paperwork folder in Drive (search "paperwork"; folder… | STEP (read/analysis) | OE 13 |
| Find every other outside company in Frederick's Gmail with an offer, a… | STEP (read/analysis) | OE 14 |
| Read the Lanternfly Publishing thread in Gmail (subject "Lanternfly x … | STEP (read/analysis) | OE 15 |
| Search Slack for "Southeast Asia" (from the Lanternfly deck) and open … | STEP (read/analysis) | OE 16 |
| Read the Balancy thread in Frederick's Gmail (search "Balancy") | STEP (read/analysis) | OE 17 |
| Read the Motive Forge thread in Frederick's Gmail (search "Motive Forg… | STEP (read/analysis) | OE 18 |
| Read the Spotlight Fest thread in Gmail (subject "Spotlight Fest - sho… | STEP (read/analysis) | OE 19 |
| Search Slack #executives for "indie showcase" (Spotlight Fest's Dec 5 … | STEP (read/analysis) | OE 20 |
| Read the Clipforge thread in Gmail (subject "Clipforge UGC Studio pilo… | STEP (read/analysis) | OE 21 |
| Search Frederick's Gmail for "HG-2291" (the workspace on the Clipforge… | STEP (read/analysis) | OE 22 |
| Read the Pixel Harbor Events thread in Gmail (subject "Booth hold - Ba… | STEP (read/analysis) | OE 23 |
| Read the Brightlane Studio thread in Gmail (subject "Brightlane x Harm… | STEP (read/analysis) | OE 24 |
| Read the Soundvault thread in Gmail (subject "Music licence for Zombie… | STEP (read/analysis) | OE 25 |
| Read the Reviewly thread in Gmail (subject "Your Reviewly trial has st… | STEP (read/analysis) | OE 26 |
| Read the Streamcast Talent thread in Gmail (subject "Creator campaign … | STEP (read/analysis) | OE 27 |
| Read the Lingora thread in Gmail (subject "Store listing localization … | STEP (read/analysis) | OE 28 |
| Read the Panelpulse thread in Gmail (subject "Player panel for Zombie … | STEP (read/analysis) | OE 29 |
| Read the Ascendo thread in Gmail (subject "ASO retainer proposal") and… | STEP (read/analysis) | OE 30 |
| Read the Wishwave thread in Gmail (subject "Seattle Indie Expo - pre-r… | STEP (read/analysis) | OE 31 |
| Read the Vaultline thread in Gmail (subject "Vaultline Standard renewa… | STEP (read/analysis) | OE 32 |
| Read the Certwell thread in Gmail (subject "Certificate renewal for yo… | STEP (read/analysis) | OE 33 |
| Read the Pingwise thread in Gmail (subject "Your Pingwise Starter tier… | STEP (read/analysis) | OE 34 |
| Find Nintendo in Linear (search "Nintendo"; the portal registration fr… | STEP (read/analysis) | OE 35 |
| Read the Kinetic Arcade thread in Gmail (subject "Kinetic Arcade - pub… | STEP (read/analysis) | OE 36 |
| Read the Lumencloud thread in Gmail (subject "Lumencloud Startup Progr… | STEP (read/analysis) | OE 37 |
| Read the Bundlehouse thread in Gmail (subject "Bundlehouse holiday bun… | STEP (read/analysis) | OE 38 |
| Read the Orbit Store thread in Gmail (subject "Orbit Store featuring -… | STEP (read/analysis) | OE 39 |
| Read the Markward thread in Gmail (subject "Markward free tier - brand… | STEP (read/analysis) | OE 40 |
| Read the Playfuse thread in Gmail (subject "Playfuse bundle partnershi… | STEP (read/analysis) | OE 41 |
| Read the Framewell thread in Gmail (subject "Framewell Pro for Harmony… | STEP (read/analysis) | OE 42 |
| Search Slack for "Maren" (Framewell's contact) and open the thread rep… | STEP (read/analysis) | OE 43 |
| Read the Hootline thread in Frederick's Gmail (search "Hootline"; subj… | STEP (read/analysis) | OE 44 |
| Read the Glyphworks thread in Gmail (subject "Font licence quote - Zom… | STEP (read/analysis) | OE 45 |
| Read the Cloudlark thread in Gmail (subject "Cloudlark credits reserve… | STEP (read/analysis) | OE 46 |
| Read the Echohall thread in Gmail (subject "Echohall Pro for your comm… | STEP (read/analysis) | OE 47 |
| Read the Pressbeam thread in Gmail (subject "Pressbeam launch package"… | STEP (read/analysis) | OE 48 |
| Read the Retainly thread in Gmail (subject "Welcome to Retainly") and … | STEP (read/analysis) | OE 49 |
| Read the Quillcraft thread in Gmail (subject "Quillcraft beta") and it… | STEP (read/analysis) | OE 50 |
| Read the Tilecast thread in Gmail (subject "Tilecast pilot slot") and … | STEP (read/analysis) | OE 51 |
| Read the Benchmarkly thread in Gmail (subject "Benchmarkly sample repo… | STEP (read/analysis) | OE 52 |
| Read the Loopnote thread in Gmail (subject "Your Loopnote trial") and … | STEP (read/analysis) | OE 53 |
| Read the Driftwood Audio thread in Gmail (subject "Voice-over quote") … | STEP (read/analysis) | OE 54 |
| Create the log spreadsheet in Google Sheets (title from OE 8) | STEP (write) | OE 55 |
| Write the header and one row per company into the new log in Sheets (r… | STEP (write) | OE 56 |
| Move the log into the Q4 commitments folder in Drive (folder from OE 7… | STEP (write) | OE 57 |
| Email billing@paylane.io to cancel the Clipforge workspace in Gmail (a… | STEP (write) | OE 58 |
| Reply to Priya Raman on the Clipforge thread in Gmail (OE 21) | STEP (write) | OE 59 |
| Reply to Teodor Lind on the Pixel Harbor Events thread in Gmail (OE 23… | STEP (write) | OE 60 |
| Reply to Ines Varga on the Brightlane Studio thread in Gmail (OE 24) | STEP (write) | OE 61 |
| Reply to Rafael Moreno on the Soundvault thread in Gmail (OE 25) | STEP (write) | OE 62 |
| Reply to Hana Kobayashi on the Reviewly thread in Gmail (OE 26) | STEP (write) | OE 63 |
| Reply to Kofi Mensah on the Streamcast Talent thread in Gmail (OE 27) | STEP (write) | OE 64 |
| Reply to Elena Petrova on the Lingora thread in Gmail (OE 28) | STEP (write) | OE 65 |
| Reply to Arjun Shah on the Panelpulse thread in Gmail (OE 29) | STEP (write) | OE 66 |
| Reply to Lucia Ferrer on the Ascendo thread in Gmail (OE 30) | STEP (write) | OE 67 |
| Reply to Sven Aalto on the Wishwave thread in Gmail (OE 31) | STEP (write) | OE 68 |
| Reply to Mila Novak on the Vaultline thread in Gmail (OE 32) | STEP (write) | OE 69 |
| Reply to Jonas Weber on the Certwell thread in Gmail (OE 33) | STEP (write) | OE 70 |
| Reply to Dana Whitfield on the Pingwise thread in Gmail (OE 34) | STEP (write) | OE 71 |
| Reply to Noor Haddad on the Kinetic Arcade thread in Gmail (OE 36) | STEP (write) | OE 72 |
| Reply to Aiden Clarke on the Lumencloud thread in Gmail (OE 37) | STEP (write) | OE 73 |
| Reply to Freya Olsen on the Bundlehouse thread in Gmail (OE 38) | STEP (write) | OE 74 |
| Reply to Mateo Rossi on the Orbit Store thread in Gmail (OE 39) | STEP (write) | OE 75 |
| Reply to Leah Brennan on the Markward thread in Gmail (OE 40) | STEP (write) | OE 76 |
| Reply to Iris Navarro on the Playfuse thread in Gmail (OE 41) | STEP (write) | OE 77 |
| Reply to Maren Holt on the Framewell thread in Gmail (OE 42) | STEP (write) | OE 78 |
| Reply to Gemma Doyle on the Hootline thread in Gmail (OE 44) | STEP (write) | OE 79 |
| Reply to Tomas Novotny on the Glyphworks thread in Gmail (OE 45) | STEP (write) | OE 80 |
| Reply to Yara Nasser on the Cloudlark thread in Gmail (OE 46) | STEP (write) | OE 81 |
| Reply to Bruno Costa on the Echohall thread in Gmail (OE 47) | STEP (write) | OE 82 |
| Reply to Ava Lindqvist on the Pressbeam thread in Gmail (OE 48) | STEP (write) | OE 83 |
| Reply to Omar Farouk on the Retainly thread in Gmail (OE 49) | STEP (write) | OE 84 |
| Reply to Nadia Petrov on the Quillcraft thread in Gmail (OE 50) | STEP (write) | OE 85 |
| Reply to Kenji Mori on the Tilecast thread in Gmail (OE 51) | STEP (write) | OE 86 |
| Reply to Clara Weiss on the Benchmarkly thread in Gmail (OE 52) | STEP (write) | OE 87 |
| Reply to Pavel Sokol on the Loopnote thread in Gmail (OE 53) | STEP (write) | OE 88 |
| Reply to Sofia Marin on the Driftwood Audio thread in Gmail (OE 54) | STEP (write) | OE 89 |
| Email ESG Law intake about the Kinetic Arcade agreement in Gmail (new … | STEP (write) | OE 90 |
| Email ESG Law intake about the Lumencloud agreement in Gmail (new mess… | STEP (write) | OE 91 |
| Email ESG Law intake about the Bundlehouse agreement in Gmail (new mes… | STEP (write) | OE 92 |
| Create the Bundlehouse card in the To Do list in Trello (OE 10) | STEP (write) | OE 93 |
| Create the Kinetic Arcade card in the To Do list in Trello (OE 10) | STEP (write) | OE 94 |
| Create the Lumencloud card in the To Do list in Trello (OE 10) | STEP (write) | OE 95 |
| Create the Markward card in the To Do list in Trello (OE 10) | STEP (write) | OE 96 |
| Create the Nintendo card in the To Do list in Trello (OE 10) | STEP (write) | OE 97 |
| Create the Orbit Store card in the To Do list in Trello (OE 10) | STEP (write) | OE 98 |
| Create the Playfuse card in the To Do list in Trello (OE 10) | STEP (write) | OE 99 |
| Search Contacts for each company's person (names from the company even… | STEP (read/analysis) | OE 100 |
| Add Lucia Ferrer to Contacts | STEP (write) | OE 101 |
| Add PERSON_0527_NAME to Contacts | STEP (write) | OE 102 |
| Add Clara Weiss to Contacts | STEP (write) | OE 103 |
| Add Ines Varga to Contacts | STEP (write) | OE 104 |
| Add Freya Olsen to Contacts | STEP (write) | OE 105 |
| Add Jonas Weber to Contacts | STEP (write) | OE 106 |
| Add Priya Raman to Contacts | STEP (write) | OE 107 |
| Add Yara Nasser to Contacts | STEP (write) | OE 108 |
| Add Sofia Marin to Contacts | STEP (write) | OE 109 |
| Add Bruno Costa to Contacts | STEP (write) | OE 110 |
| Add Maren Holt to Contacts | STEP (write) | OE 111 |
| Add Tomas Novotny to Contacts | STEP (write) | OE 112 |
| Add Gemma Doyle to Contacts | STEP (write) | OE 113 |
| Add Wen Halvorsen to Contacts | STEP (write) | OE 114 |
| Add Elena Petrova to Contacts | STEP (write) | OE 115 |
| Add Pavel Sokol to Contacts | STEP (write) | OE 116 |
| Add Hugo Lambert to Contacts | STEP (write) | OE 117 |
| Add Mateo Rossi to Contacts | STEP (write) | OE 118 |
| Add Arjun Shah to Contacts | STEP (write) | OE 119 |
| Add Dana Whitfield to Contacts | STEP (write) | OE 120 |
| Add Teodor Lind to Contacts | STEP (write) | OE 121 |
| Add Iris Navarro to Contacts | STEP (write) | OE 122 |
| Add Ava Lindqvist to Contacts | STEP (write) | OE 123 |
| Add Nadia Petrov to Contacts | STEP (write) | OE 124 |
| Add Omar Farouk to Contacts | STEP (write) | OE 125 |
| Add Hana Kobayashi to Contacts | STEP (write) | OE 126 |
| Add Rafael Moreno to Contacts | STEP (write) | OE 127 |
| Add Rina Takeda to Contacts | STEP (write) | OE 128 |
| Add Kofi Mensah to Contacts | STEP (write) | OE 129 |
| Add Kenji Mori to Contacts | STEP (write) | OE 130 |
| Add Mila Novak to Contacts | STEP (write) | OE 131 |
| Add Sven Aalto to Contacts | STEP (write) | OE 132 |
| Add a Balancy reminder to Frederick's calendar on the review day (Cale… | STEP (write) | OE 133 |
| Add a Benchmarkly reminder to Frederick's calendar on the review day (… | STEP (write) | OE 134 |
| Add a Cloudlark reminder to Frederick's calendar on the review day (Ca… | STEP (write) | OE 135 |
| Add a Driftwood Audio reminder to Frederick's calendar on the review d… | STEP (write) | OE 136 |
| Add a Echohall reminder to Frederick's calendar on the review day (Cal… | STEP (write) | OE 137 |
| Add a Framewell reminder to Frederick's calendar on the review day (Ca… | STEP (write) | OE 138 |
| Add a Glyphworks reminder to Frederick's calendar on the review day (C… | STEP (write) | OE 139 |
| Add a Hootline reminder to Frederick's calendar on the review day (Cal… | STEP (write) | OE 140 |
| Add a Lanternfly Publishing reminder to Frederick's calendar on the re… | STEP (write) | OE 141 |
| Add a Loopnote reminder to Frederick's calendar on the review day (Cal… | STEP (write) | OE 142 |
| Add a Pressbeam reminder to Frederick's calendar on the review day (Ca… | STEP (write) | OE 143 |
| Add a Quillcraft reminder to Frederick's calendar on the review day (C… | STEP (write) | OE 144 |
| Add a Retainly reminder to Frederick's calendar on the review day (Cal… | STEP (write) | OE 145 |
| Add a Tilecast reminder to Frederick's calendar on the review day (Cal… | STEP (write) | OE 146 |
| Reply to Leonard on his email in Gmail (message from OE 1) | STEP (write) | OE 147 |

All 147 segments are numbered STEP events with an Expected line. No header, CONTEXT note, RESPONSE_DESCRIPTION or NON_ACTION segment.

## Coverage

| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |
|---|---|---|---|
| R1 | OE 1 | covered | ledger route: Gmail read of the hub (OE route = ledger route) |
| R2 | OE 2–OE 11 (7 events) | covered | ledger route: guardrails doc, Monday change, ESG note + reply, checklist, README, template, keep-running card |
| R3 | OE 13–OE 54 (38 events) | covered | ledger route: paperwork folder + inbox sweep give 36; nine look-alikes ruled out in the sweep |
| R4 | OE 55, OE 56, OE 57 | covered | ledger route: create, then write rows, then move into the folder (brief §4b D1 accepts created-elsewhere-and-moved) |
| R5 | OE 58–OE 89 (32 events) | covered | ledger route: 31 answers plus the Clipforge cancellation |
| R6 | OE 93–OE 99 (7 events) | covered | ledger route: 7 To Do cards |
| R7 | OE 90, OE 91, OE 92 | covered | ledger route: 3 intake emails |
| R8 | OE 59–OE 89 (31 events) | covered | ledger route: answers are sent replies, not drafts |
| R9 | OE 12–OE 54 (16 events) | covered | ledger route: review date + 12 Park + 2 later answers |
| R10 | OE 133–OE 146 (14 events) | covered | ledger route: 14 events on Mon Jan 5, 2026 |
| R11 | OE 100–OE 132 (33 events) | covered | ledger route: check, then 32 adds |
| R12 | OE 147 | covered | ledger route: reply on the hub thread |
| F1 | OE 1 | covered | Leonard's vendor and partner email (the hub) |
| F2 | OE 2 | covered | Runway guardrails doc: the five decisions, top to bottom |
| F3 | OE 3 | covered | The Monday change: partner-booked travel counts as cash |
| F4 | OE 4 | covered | ESG Law's signing note and Leonard's reply under it |
| F5 | OE 5 | covered | ESG intake checklist: what each intake email carries |
| F6 | OE 6 | covered | ESG Law intake address in Contacts |
| F7 | OE 7 | covered | Frederick's Q4 commitments folder (log destination) |
| F8 | OE 8 | covered | Folder README: sheet name, columns, decision words, Next date rule, Co |
| F9 | OE 9 | covered | Log template header row |
| F10 | OE 11 | covered | Arthur's keep-running list (the Keep exemption) |
| F11 | OE 10 | covered | Harmony Games board and its To Do list (card destination) |
| F12 | OE 12 | covered | The January commitments review date |
| F13 | OE 13 | covered | Frederick's paperwork folder (each counterparty's filed paper) |
| F14 | — | not needed on the path | superseded: OE 4 quotes 'This replaces what I said in July' (SQL L274); the path never relies on it |
| F15 | — | not needed on the path | an opinion, not a rule: OE 1 names the guardrails doc and the Monday change as the rules (SQL L251) |
| F16 | — | not needed on the path | UA spend is off the backlog per OE 1's exclusion (SQL L251); no decision reads it |
| F17 | — | not needed on the path | stale; every row it carries is decided from the current paper or notice (OE 21–23) |
| F18 | OE 14 | covered | Nintendo developer portal mails (look done) |
| F19 | — | not needed on the path | the sign-up is shown by the registration notice OE 14 reads (gmail threads/frederick@harmonygames.co_1842359398719557772.json) |
| F20 | OE 35 | covered | ZOM-567 and Arthur's comment: Nintendo still needs an officer's accept |
| F21 | OE 43 | covered | Leonard's Sep 22 Playtestcloud post (root of the Framewell reply) |
| F22 | OE 43 | covered | Framewell waiver: the Pro plan at no charge until Feb 1 (names Maren,  |
| F23 | OE 16 | covered | Leonard's Sep 17 DM root 'we have no localization though' |
| F24 | OE 16 | covered | Lanternfly already answered by Leonard (names Wen and the Southeast As |
| F25 | OE 20 | covered | Spotlight Fest already answered by Robert (names the Dec 5 indie showc |
| F26 | — | not needed on the path | Robert's note in OE 20 carries who answered and when (C07C2866011/1758134460.899858) |
| F27 | OE 22 | covered | Paylane notice for workspace HG-2291: pilot ends Oct 15, billing from  |
| F28 | — | not needed on the path | the Clipforge paper's 'Workspace: HG-2291' in OE 21 ties the workspace (f_8d0e0e3ae076b2f745e7e2) |
| F29 | OE 35, OE 97 | covered | Nintendo: platform developer terms — Sign |
| F30 | OE 42, OE 78, OE 111, OE 138 | covered | Framewell: creative asset subscription — Park |
| F31 | OE 15, OE 114, OE 141 | covered | Lanternfly Publishing: Southeast Asia publishing proposal — Answered |
| F32 | OE 34, OE 71, OE 120 | covered | Pingwise: uptime monitoring and on-call paging — Keep |
| F33 | OE 21, OE 22, OE 58, OE 59, OE 107 | covered | Clipforge: UGC video ad pilot — End |
| F34 | OE 23, OE 60, OE 121 | covered | Pixel Harbor Events: booth at the Oct 24 indie showcase — End |
| F35 | OE 24, OE 61, OE 104 | covered | Brightlane Studio: creative agency retainer — End |
| F36 | OE 25, OE 62, OE 127 | covered | Soundvault: music licence (annual) — End |
| F37 | OE 26, OE 63, OE 126 | covered | Reviewly: store-review management trial — End |
| F38 | OE 27, OE 64, OE 129 | covered | Streamcast Talent: influencer campaign — End |
| F39 | OE 28, OE 65, OE 115 | covered | Lingora: store-listing localization sprint — End |
| F40 | OE 29, OE 66, OE 119 | covered | Panelpulse: player research panel — End |
| F41 | OE 30, OE 67, OE 101 | covered | Ascendo: ASO agency retainer — End |
| F42 | OE 31, OE 68, OE 132 | covered | Wishwave: pre-registration push at a partner showcase — End |
| F43 | OE 32, OE 69, OE 131 | covered | Vaultline: nightly database backups — Keep |
| F44 | OE 33, OE 70, OE 106 | covered | Certwell: SSL certificate for the API domain — Keep |
| F45 | OE 36, OE 72, OE 90, OE 94 | covered | Kinetic Arcade: publishing LOI (12-month exclusivity) — Sign |
| F46 | OE 37, OE 73, OE 91, OE 95 | covered | Lumencloud: cloud credits programme (36-month term) — Sign |
| F47 | OE 38, OE 74, OE 92, OE 93, OE 105 | covered | Bundlehouse: co-marketing bundle (licenses our game IP) — Sign |
| F48 | OE 39, OE 75, OE 98, OE 118 | covered | Orbit Store: store featuring agreement — Sign |
| F49 | OE 40, OE 76, OE 96 | covered | Markward: brand-monitoring free tier (click-through terms) — Sign |
| F50 | OE 41, OE 77, OE 99, OE 122 | covered | Playfuse: bundle partnership NDA (ESG mutual template) — Sign |
| F51 | OE 44, OE 79, OE 113, OE 140 | covered | Hootline: social scheduler — Park |
| F52 | OE 45, OE 80, OE 112, OE 139 | covered | Glyphworks: font licence quote — Park |
| F53 | OE 46, OE 81, OE 108, OE 135 | covered | Cloudlark: startup credits offer — Park |
| F54 | OE 47, OE 82, OE 110, OE 137 | covered | Echohall: community platform upgrade proposal — Park |
| F55 | OE 48, OE 83, OE 123, OE 143 | covered | Pressbeam: PR distribution package for 2026 — Park |
| F56 | OE 49, OE 84, OE 125, OE 145 | covered | Retainly: analytics trial — Park |
| F57 | OE 50, OE 85, OE 124, OE 144 | covered | Quillcraft: AI copywriting tool beta — Park |
| F58 | OE 51, OE 86, OE 130, OE 146 | covered | Tilecast: website interactive demo widget — Park |
| F59 | OE 52, OE 87, OE 103, OE 134 | covered | Benchmarkly: benchmark report subscription — Park |
| F60 | OE 53, OE 88, OE 116, OE 142 | covered | Loopnote: meeting-notes tool trial — Park |
| F61 | OE 54, OE 89, OE 109, OE 136 | covered | Driftwood Audio: voice-over studio quote — Park |
| F62 | OE 17, OE 102, OE 133 | covered | Balancy: live-ops tool trial — Answered |
| F63 | OE 18, OE 117 | covered | Motive Forge: outsourced art quote — Answered |
| F64 | OE 19, OE 128 | covered | Spotlight Fest: showcase slot invitation — Answered |
| F65 | OE 14 | covered | Rayking Game: only forwarded around internally |
| F66 | OE 14 | covered | Playable Factory: cold pitch nobody answered |
| F67 | OE 14 | covered | Google partner check-in: an ad network |
| F68 | OE 14 | covered | Gamesforum SF: speaker invite nobody answered |
| F69 | OE 14 | covered | InterCo Digital: cold pitch nobody answered |
| F70 | OE 14 | covered | Singular: named in the hub's UA exclusion |
| F71 | OE 14 | covered | NCsoft: strategic / investor talks |
| F72 | OE 14 | covered | Dentsu: investor meeting Leonard is flying to |
| F73 | OE 14 | covered | Nova Rewards: offer withdrawn Sep 23 |
| F74 | OE 1 | covered | Mattel: Leonard keeps it |
| F75 | OE 100 | covered | Counterparty contacts already in Contacts (no new contact) |

## Expected-data sign-off

Every quoted span on every Expected line (193 spans) was re-read in this run from its record and found verbatim (whitespace-normalised): injected rows by parsing 01_Universe_Inject.sql again (never executed), base records through hg.py get. Unquoted values (recipients, ids, counts, dates) are listed per write event with their source.

| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Ledger entry (result · quote · evidence_check / not_a_claim) | Match / minor / wrong / unresolved |
|---|---|---|---|---|---|
| OE 1 | "can you take over the vendor and partner backlog this week?" (+9 more quoted spans re-read) | SQL L252 (message frederick.stone@harmonygames.co/<CAlIXcq3nWlSRBAZONcbY9d2v0ggkPYER8WfaoZa@mail.gmail.com>) | found verbatim | F1 · VERIFIED quote | match |
| OE 2 | "Go top to bottom and stop at the first one that fits." (+9 more quoted spans re-read) | SQL L8 (doc f_b98287f6f80fe431a71209) | found verbatim | F2 · VERIFIED quote | match |
| OE 3 | "one change to the runway guardrails doc: travel and event costs count as cash even …" | SQL L224 (C07C2866011/1759166100.370044) | found verbatim | F3 · VERIFIED quote | match |
| OE 4 | "Only an officer, you or Arthur, accepts terms or signs for Harmony Games, whatever the …" (+6 more quoted spans re-read) | SQL L260 (message frederick.stone@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com>) | found verbatim | F4 · VERIFIED quote | match |
| OE 5 | "One email per agreement to ESG Law intake." (+6 more quoted spans re-read) | SQL L12 (doc f_3b06917a41dd59308d890b) | found verbatim | F5 · VERIFIED quote | match |
| OE 6 | PERSON_2599_EMAIL | SQL L561 (contact 9b0185e445572aeee9f27d35) | ESG Law intake PERSON_2599_EMAIL | F6 · VERIFIED value | match |
| OE 7 | Q4 commitments | SQL L14 (folder d_80a8c04753ba82ba4ba6a5) | owner frederick.stone@harmonygames.co, shared ["leonard.hayes@harmonygames.co"] | F7 · VERIFIED value | match |
| OE 8 | "Name it "Q4 commitments log"; to start, copy the header row from the template sheet." (+5 more quoted spans re-read) | SQL L16 (doc f_846ddc38b2aab3d2ed3fcb) | found verbatim | F8 · VERIFIED quote | match |
| OE 9 | Company … Next date | SQL L18 (sheet f_05f0a451b29b19a1c0b90f, tab Log) | 7 header cells | F9 · VERIFIED value | match |
| OE 10 | To Do, Doing, Done, Backlog | hg.py get trello data.json /lists/3../lists/7 (board 640643a3fd8f3ca308d9318e) | Recruiting closed | F11 · VERIFIED value | match |
| OE 11 | "Stuff the live game needs to keep running. Ask me before cancelling any of it." (+4 more quoted spans re-read) | SQL L233 (card 689b662c60cbe40b9f4a97ae + checklist items) | found verbatim | F10 · VERIFIED quote | match |
| OE 12 | "Everything we parked comes back here." | SQL L541 (event evt_fd469c29811879519c2c96) | found verbatim | F12 · VERIFIED quote | match |
| OE 13 | 33 files | SQL L22 (folder d_ffa3e6e473da7e6523614f) + 33 drive rows with that parent | 33 | F13 · VERIFIED value | match |
| OE 14 | "Your three social profiles are connected" (+16 more quoted spans re-read) | SQL L433 (message frederick.stone@harmonygames.co/<CAat3tn3W0qDDTcWKmBYwD1Jnj1j_YU1h2NqzJZj@mail.gmail.com>) | found verbatim | F18, F65–F73 · VERIFIED quote | match |
| OE 15 | "Any news on the proposal? We're planning our Q4 slate and would love to include Domino …" (+4 more quoted spans re-read) | SQL L320 (message frederick.stone@harmonygames.co/<CArrsRpTwnF5vDz3j8sB1bdi-2N8lorF7bNSSbk-@mail.gmail.com>) | found verbatim | F31 · VERIFIED quote | match |
| OE 16 | "we have no localization though" (+1 more quoted span re-read) | hg.py get slack messages/D05S58U4SAK/2025-09.json /100 | found verbatim | F23, F24 · VERIFIED quote | match |
| OE 17 | "We offer a 1-month trial to integrate and test features." (+2 more quoted spans re-read) | hg.py get gmail threads/frederick@harmonygames.co_1840501641217286806.json (message of Thu, 11 Sep 2025 14:54) | found verbatim | F62 · VERIFIED quote | match |
| OE 18 | "$6,400, four weeks from kickoff" (+2 more quoted spans re-read) | SQL L501 (message frederick.stone@harmonygames.co/<CAroxkgBywTvnZooHWA1QvDuZcDMuI8XdpMtLkts@mail.gmail.com>) | found verbatim | F63 · VERIFIED quote | match |
| OE 19 | "We'd love Zombie Match 3D in the Spotlight Fest indie showcase on Dec 5. The stand fee …" (+2 more quoted spans re-read) | SQL L515 (message frederick.stone@harmonygames.co/<CAjj6h7BzqoAZSS2-4M7N9e7ZLBDyeyZXl0BwgcI@mail.gmail.com>) | found verbatim | F64 · VERIFIED quote | match |
| OE 20 | "had the call about the Dec 5 indie showcase. we're sitting this one out this year, I …" | SQL L222 (C07C2866011/1758134460.899858) | found verbatim | F25 · VERIFIED quote | match |
| OE 21 | "If you're not carrying on after the pilot, let me know here too so I can plan the …" (+4 more quoted spans re-read) | SQL L303 (message frederick.stone@harmonygames.co/<CAFEbdSLTqGx4K9ylCWMjfozRDorLWGyAc5mo6e7@mail.gmail.com>) | found verbatim | F33 · VERIFIED quote | match |
| OE 22 | "Workspace HG-2291: your pilot is ending" (+2 more quoted spans re-read) | SQL L288 (message frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io>, subject) | found verbatim | F27 · VERIFIED quote | match |
| OE 23 | "Quote attached: $4,800, with a $2,400 deposit due by Oct 10 to keep the hold." (+3 more quoted spans re-read) | SQL L307 (message frederick.stone@harmonygames.co/<CAC1R0eFyTK7ezriX3kHgoWqGCC1DkbKElci5sJ8@mail.gmail.com>) | found verbatim | F34 · VERIFIED quote | match |
| OE 24 | "Can you confirm by Oct 1 so I can book the team for October?" (+2 more quoted spans re-read) | SQL L327 (message frederick.stone@harmonygames.co/<CA-xgF65XCwo6QXURZM_eCJcAClcs_LfeftzR27P@mail.gmail.com>) | found verbatim | F35 · VERIFIED quote | match |
| OE 25 | "just a reminder the trailer pack quote runs out on Oct 15. Want me to send the licence …" (+2 more quoted spans re-read) | SQL L337 (message frederick.stone@harmonygames.co/<CAa-jv7GWQa7i06XwUWtNIJ_DInBkE5Qi4Y8PmMT@mail.gmail.com>) | found verbatim | F36 · VERIFIED quote | match |
| OE 26 | "how's the trial going?" (+2 more quoted spans re-read) | SQL L344 (message frederick.stone@harmonygames.co/<CAEcTJxNSlNWdzmdlv0uAxA5LWo-4JRqmN_lbkGs@mail.gmail.com>) | found verbatim | F37 · VERIFIED quote | match |
| OE 27 | "want me to pencil in the November slot?" (+2 more quoted spans re-read) | SQL L351 (message frederick.stone@harmonygames.co/<CAIauDHOvbuHs1D8VFmRdi2YfR01quJPqo1ZiQZJ@mail.gmail.com>) | found verbatim | F38 · VERIFIED quote | match |
| OE 28 | "any update? Send the PO and we can start Monday." (+3 more quoted spans re-read) | SQL L361 (message frederick.stone@harmonygames.co/<CAb3f_RRKlDbfktS3_Cu7qnXPyTybHnS1K2Eq3b7@mail.gmail.com>) | found verbatim | F39 · VERIFIED quote | match |
| OE 29 | "still keen on the Oct 14 panel? Recruiting closes Oct 6." (+2 more quoted spans re-read) | SQL L368 (message frederick.stone@harmonygames.co/<CAM5dEEI7CWxEdApgrQnK2XC211TZL1KF-WNUpsB@mail.gmail.com>) | found verbatim | F40 · VERIFIED quote | match |
| OE 30 | "can you confirm by Oct 1 so we can kick off?" (+1 more quoted span re-read) | SQL L375 (message frederick.stone@harmonygames.co/<CA0BbU6OEljE3nhaS2pWMojXL9GJ_kYqFO8JTtP2@mail.gmail.com>) | found verbatim | F41 · VERIFIED quote | match |
| OE 31 | "can you confirm by Oct 17 so I can book travel while fares are low?" (+3 more quoted spans re-read) | SQL L382 (message frederick.stone@harmonygames.co/<CAHavdKpt7nR3fxojrxKL1PYVBWt8ridR2XEm01t@mail.gmail.com>) | found verbatim | F42 · VERIFIED quote | match |
| OE 32 | "your nightly database backups move to Standard ($19/month) when the plan renews on Oct …" (+2 more quoted spans re-read) | SQL L386 (message frederick.stone@harmonygames.co/<CASRfZCkXuHwLJPLUeim95W1qFlzEaz37BReSyJz@mail.gmail.com>) | found verbatim | F43 · VERIFIED quote | match |
| OE 33 | "The renewal is $89 for the year. Reply to confirm and we'll reissue it; otherwise it …" (+2 more quoted spans re-read) | SQL L390 (message frederick.stone@harmonygames.co/<CApaJB4i_PhvJp_95Q3bE-l9yDV4x096tsJobB11@mail.gmail.com>) | found verbatim | F44 · VERIFIED quote | match |
| OE 34 | "From Nov 1 the account moves to Team ($29/month) under your existing agreement, so …" (+3 more quoted spans re-read) | SQL L296 (message frederick.stone@harmonygames.co/<CAZgisbRwHgHd3Hk_E9LYMNIOFiMZminBj4K2tWc@mail.gmail.com>) | found verbatim | F32 · VERIFIED quote | match |
| OE 35 | "the Global ToS and NDA still needs our agreement approver to accept it, and that has …" (+2 more quoted spans re-read) | SQL L558 (ZOM-567 comment cmt_c9a6660d81e067ad1de7) | found verbatim | F29 · VERIFIED quote | match |
| OE 36 | "any thoughts on the LOI? Oct 20 is our internal deadline." (+4 more quoted spans re-read) | SQL L397 (message frederick.stone@harmonygames.co/<CAwVKKP1C-1rXHFCWIgbB9PjITqgDI3ziZAK9984@mail.gmail.com>) | found verbatim | F45 · VERIFIED quote | match |
| OE 37 | "just checking you saw this one, the cohort closes Oct 31." (+4 more quoted spans re-read) | SQL L404 (message frederick.stone@harmonygames.co/<CA2AOLHmh-RU9NexSr5s80P3mUbj-J4_hr59arcw@mail.gmail.com>) | found verbatim | F46 · VERIFIED quote | match |
| OE 38 | "The participation agreement needs signing by Nov 1." (+4 more quoted spans re-read) | SQL L411 (message frederick.stone@harmonygames.co/<CAlSBl5tSj6BhvNqcMHhDChnKE3Fcp7fgMJdKNtH@mail.gmail.com>) | found verbatim | F47 · VERIFIED quote | match |
| OE 39 | "gentle nudge on the featuring agreement, Oct 24 is the cut-off." (+3 more quoted spans re-read) | SQL L418 (message frederick.stone@harmonygames.co/<CAo7WkZSvPT7fVQd40F1HezmilqIw9AoAb6_uTM2@mail.gmail.com>) | found verbatim | F48 · VERIFIED quote | match |
| OE 40 | "the free tier is ready whenever you accept the terms in the dashboard. Shall I keep …" (+3 more quoted spans re-read) | SQL L425 (message frederick.stone@harmonygames.co/<CAjzt3v0v5AIRijm5FdJu1yYv5Q-LMNqpRFDYAqb@mail.gmail.com>) | found verbatim | F49 · VERIFIED quote | match |
| OE 41 | "Could someone on your side sign a mutual NDA? Happy to use your lawyers' template." (+2 more quoted spans re-read) | SQL L429 (message frederick.stone@harmonygames.co/<CAWCBU--R8_Q4xxjtvPvDrzjjgqqRxz_flrPVZo6@mail.gmail.com>) | found verbatim | F50 · VERIFIED quote | match |
| OE 42 | "Can you let me know by mid-October if we should set it up?" (+2 more quoted spans re-read) | SQL L292 (message frederick.stone@harmonygames.co/<CAGJkuaxoKn_J2zxTzhLswrYwOGA_wA5IXe9v747@mail.gmail.com>) | found verbatim | F30 · VERIFIED quote | match |
| OE 43 | "Playtestcloud results are in" (+1 more quoted span re-read) | hg.py get slack messages/C07C2866011/2025-09.json /866 | found verbatim | F21, F22 · VERIFIED quote | match |
| OE 44 | "the startup promo keeps the account free until Jan 31, 2026. After that it's $39/month …" (+1 more quoted span re-read) | SQL L433 (message frederick.stone@harmonygames.co/<CAat3tn3W0qDDTcWKmBYwD1Jnj1j_YU1h2NqzJZj@mail.gmail.com>) | found verbatim | F51 · VERIFIED quote | match |
| OE 45 | "any decision on the fonts?" (+2 more quoted spans re-read) | SQL L446 (message frederick.stone@harmonygames.co/<CApanLB9xL5jrjcNSzDTWYvE6RiWdfZchZxr4q3K@mail.gmail.com>) | found verbatim | F52 · VERIFIED quote | match |
| OE 46 | "Would you like to activate now or later?" (+2 more quoted spans re-read) | SQL L450 (message frederick.stone@harmonygames.co/<CAXUVl-vI7c6T4f22vI41yY2P83JxLRUdeHW1-hC@mail.gmail.com>) | found verbatim | F53 · VERIFIED quote | match |
| OE 47 | "The free plan carries on as it is until then." (+2 more quoted spans re-read) | SQL L457 (message frederick.stone@harmonygames.co/<CAHV7my-sLo9CEzISCj6j5YvPRBW1ReAHi-SrN7V@mail.gmail.com>) | found verbatim | F54 · VERIFIED quote | match |
| OE 48 | "$1,200 when you book. No travel, all remote, and you can book any time before launch." (+2 more quoted spans re-read) | SQL L461 (message frederick.stone@harmonygames.co/<CAGdptfs7cIHOLvLgF6LBpN_8DHhsOmA8Oqoddfh@mail.gmail.com>) | found verbatim | F55 · VERIFIED quote | match |
| OE 49 | "It runs free until Jan 12, then Growth is $99/month. Could you let me know whether you …" (+1 more quoted span re-read) | SQL L465 (message frederick.stone@harmonygames.co/<CAOHCdeuLRHpqtIPQZRUGefwtjIwm5BrmgGS_Loo@mail.gmail.com>) | found verbatim | F56 · VERIFIED quote | match |
| OE 50 | "would you join a 30-minute feedback call next week?" (+2 more quoted spans re-read) | SQL L472 (message frederick.stone@harmonygames.co/<CALcXsJB9Dsqckdbzui4zsoYGv8YD3gxSJbpOQzA@mail.gmail.com>) | found verbatim | F57 · VERIFIED quote | match |
| OE 51 | "We can offer a free pilot slot in February for the interactive demo widget on your …" (+2 more quoted spans re-read) | SQL L476 (message frederick.stone@harmonygames.co/<CAdfSBCTPq8pDFK70IArhUSHj5PEV3Tnz19vDg7Y@mail.gmail.com>) | found verbatim | F58 · VERIFIED quote | match |
| OE 52 | "The full set is a $300/month subscription from February if you want it." (+2 more quoted spans re-read) | SQL L483 (message frederick.stone@harmonygames.co/<CAFrM1JgqylGFM5MjwuqQMZPLsTjafUxYfbcriCb@mail.gmail.com>) | found verbatim | F59 · VERIFIED quote | match |
| OE 53 | "want me to add the rest of your team to the trial?" (+2 more quoted spans re-read) | SQL L490 (message frederick.stone@harmonygames.co/<CAff-LH5Vcdc03I5o2aYmpkuR0BE-z_AH8pa3w_W@mail.gmail.com>) | found verbatim | F60 · VERIFIED quote | match |
| OE 54 | "$950 for the trailer VO, paid when you book a session. The quote is good until Feb 28." (+2 more quoted spans re-read) | SQL L497 (message frederick.stone@harmonygames.co/<CA-DqRg1TZ4TPniI7P8AW7DvtD6lNosGZdpC1x6_@mail.gmail.com>) | found verbatim | F61 · VERIFIED quote | match |
| OE 55 | Q4 commitments log | SQL L16 (doc f_846ddc38b2aab3d2ed3fcb) | Name it "Q4 commitments log" | F8 · VERIFIED value | match |
| OE 56 | 36 rows | solver truth.json re-checked against SQL L18 (template f_05f0a451b29b19a1c0b90f header) | 36 rows, 7 columns | F9, F29–F64 · VERIFIED value | match |
| OE 57 | Q4 commitments | SQL L14 (folder d_80a8c04753ba82ba4ba6a5) | Q4 commitments | F7 · VERIFIED value | match |
| OE 58 | billing@paylane.io | SQL L288 (message frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io>) | write to billing@paylane.io by Oct 15 | F27, F33 · VERIFIED value | match |
| OE 59 | PERSON_9704_EMAIL | SQL L303 (message frederick.stone@harmonygames.co/<CAFEbdSLTqGx4K9ylCWMjfozRDorLWGyAc5mo6e7@mail.gmail.com>, from_email) | Priya Raman PERSON_9704_EMAIL | F33 · VERIFIED value | match |
| OE 60 | PERSON_9705_EMAIL | SQL L307 (message frederick.stone@harmonygames.co/<CAC1R0eFyTK7ezriX3kHgoWqGCC1DkbKElci5sJ8@mail.gmail.com>, from_email) | Teodor Lind PERSON_9705_EMAIL | F34 · VERIFIED value | match |
| OE 61 | PERSON_9706_EMAIL | SQL L327 (message frederick.stone@harmonygames.co/<CA-xgF65XCwo6QXURZM_eCJcAClcs_LfeftzR27P@mail.gmail.com>, from_email) | Ines Varga PERSON_9706_EMAIL | F35 · VERIFIED value | match |
| OE 62 | PERSON_9707_EMAIL | SQL L337 (message frederick.stone@harmonygames.co/<CAa-jv7GWQa7i06XwUWtNIJ_DInBkE5Qi4Y8PmMT@mail.gmail.com>, from_email) | Rafael Moreno PERSON_9707_EMAIL | F36 · VERIFIED value | match |
| OE 63 | PERSON_9708_EMAIL | SQL L344 (message frederick.stone@harmonygames.co/<CAEcTJxNSlNWdzmdlv0uAxA5LWo-4JRqmN_lbkGs@mail.gmail.com>, from_email) | Hana Kobayashi PERSON_9708_EMAIL | F37 · VERIFIED value | match |
| OE 64 | PERSON_9709_EMAIL | SQL L351 (message frederick.stone@harmonygames.co/<CAIauDHOvbuHs1D8VFmRdi2YfR01quJPqo1ZiQZJ@mail.gmail.com>, from_email) | Kofi Mensah PERSON_9709_EMAIL | F38 · VERIFIED value | match |
| OE 65 | PERSON_9710_EMAIL | SQL L361 (message frederick.stone@harmonygames.co/<CAb3f_RRKlDbfktS3_Cu7qnXPyTybHnS1K2Eq3b7@mail.gmail.com>, from_email) | Elena Petrova PERSON_9710_EMAIL | F39 · VERIFIED value | match |
| OE 66 | PERSON_9711_EMAIL | SQL L368 (message frederick.stone@harmonygames.co/<CAM5dEEI7CWxEdApgrQnK2XC211TZL1KF-WNUpsB@mail.gmail.com>, from_email) | Arjun Shah PERSON_9711_EMAIL | F40 · VERIFIED value | match |
| OE 67 | PERSON_9712_EMAIL | SQL L375 (message frederick.stone@harmonygames.co/<CA0BbU6OEljE3nhaS2pWMojXL9GJ_kYqFO8JTtP2@mail.gmail.com>, from_email) | Lucia Ferrer PERSON_9712_EMAIL | F41 · VERIFIED value | match |
| OE 68 | PERSON_9713_EMAIL | SQL L382 (message frederick.stone@harmonygames.co/<CAHavdKpt7nR3fxojrxKL1PYVBWt8ridR2XEm01t@mail.gmail.com>, from_email) | Sven Aalto PERSON_9713_EMAIL | F42 · VERIFIED value | match |
| OE 69 | PERSON_9714_EMAIL | SQL L386 (message frederick.stone@harmonygames.co/<CASRfZCkXuHwLJPLUeim95W1qFlzEaz37BReSyJz@mail.gmail.com>, from_email) | Mila Novak PERSON_9714_EMAIL | F43 · VERIFIED value | match |
| OE 70 | PERSON_9715_EMAIL | SQL L390 (message frederick.stone@harmonygames.co/<CApaJB4i_PhvJp_95Q3bE-l9yDV4x096tsJobB11@mail.gmail.com>, from_email) | Jonas Weber PERSON_9715_EMAIL | F44 · VERIFIED value | match |
| OE 71 | PERSON_9703_EMAIL | SQL L296 (message frederick.stone@harmonygames.co/<CAZgisbRwHgHd3Hk_E9LYMNIOFiMZminBj4K2tWc@mail.gmail.com>, from_email) | Dana Whitfield PERSON_9703_EMAIL | F32 · VERIFIED value | match |
| OE 72 | PERSON_9716_EMAIL | SQL L397 (message frederick.stone@harmonygames.co/<CAwVKKP1C-1rXHFCWIgbB9PjITqgDI3ziZAK9984@mail.gmail.com>, from_email) | Noor Haddad PERSON_9716_EMAIL | F45 · VERIFIED value | match |
| OE 73 | PERSON_9717_EMAIL | SQL L404 (message frederick.stone@harmonygames.co/<CA2AOLHmh-RU9NexSr5s80P3mUbj-J4_hr59arcw@mail.gmail.com>, from_email) | Aiden Clarke PERSON_9717_EMAIL | F46 · VERIFIED value | match |
| OE 74 | PERSON_9718_EMAIL | SQL L411 (message frederick.stone@harmonygames.co/<CAlSBl5tSj6BhvNqcMHhDChnKE3Fcp7fgMJdKNtH@mail.gmail.com>, from_email) | Freya Olsen PERSON_9718_EMAIL | F47 · VERIFIED value | match |
| OE 75 | PERSON_9719_EMAIL | SQL L418 (message frederick.stone@harmonygames.co/<CAo7WkZSvPT7fVQd40F1HezmilqIw9AoAb6_uTM2@mail.gmail.com>, from_email) | Mateo Rossi PERSON_9719_EMAIL | F48 · VERIFIED value | match |
| OE 76 | PERSON_9720_EMAIL | SQL L425 (message frederick.stone@harmonygames.co/<CAjzt3v0v5AIRijm5FdJu1yYv5Q-LMNqpRFDYAqb@mail.gmail.com>, from_email) | Leah Brennan PERSON_9720_EMAIL | F49 · VERIFIED value | match |
| OE 77 | PERSON_9721_EMAIL | SQL L429 (message frederick.stone@harmonygames.co/<CAWCBU--R8_Q4xxjtvPvDrzjjgqqRxz_flrPVZo6@mail.gmail.com>, from_email) | Iris Navarro PERSON_9721_EMAIL | F50 · VERIFIED value | match |
| OE 78 | PERSON_9701_EMAIL | SQL L292 (message frederick.stone@harmonygames.co/<CAGJkuaxoKn_J2zxTzhLswrYwOGA_wA5IXe9v747@mail.gmail.com>, from_email) | Maren Holt PERSON_9701_EMAIL | F30 · VERIFIED value | match |
| OE 79 | PERSON_9722_EMAIL | SQL L436 (message frederick.stone@harmonygames.co/<CAhKYUa4HtPNJGhGU5qifbVfYwMCjxb0DSaMXtME@mail.gmail.com>, from_email) | Gemma Doyle PERSON_9722_EMAIL | F51 · VERIFIED value | match |
| OE 80 | PERSON_9723_EMAIL | SQL L446 (message frederick.stone@harmonygames.co/<CApanLB9xL5jrjcNSzDTWYvE6RiWdfZchZxr4q3K@mail.gmail.com>, from_email) | Tomas Novotny PERSON_9723_EMAIL | F52 · VERIFIED value | match |
| OE 81 | PERSON_9724_EMAIL | SQL L450 (message frederick.stone@harmonygames.co/<CAXUVl-vI7c6T4f22vI41yY2P83JxLRUdeHW1-hC@mail.gmail.com>, from_email) | Yara Nasser PERSON_9724_EMAIL | F53 · VERIFIED value | match |
| OE 82 | PERSON_9725_EMAIL | SQL L457 (message frederick.stone@harmonygames.co/<CAHV7my-sLo9CEzISCj6j5YvPRBW1ReAHi-SrN7V@mail.gmail.com>, from_email) | Bruno Costa PERSON_9725_EMAIL | F54 · VERIFIED value | match |
| OE 83 | PERSON_9726_EMAIL | SQL L461 (message frederick.stone@harmonygames.co/<CAGdptfs7cIHOLvLgF6LBpN_8DHhsOmA8Oqoddfh@mail.gmail.com>, from_email) | Ava Lindqvist PERSON_9726_EMAIL | F55 · VERIFIED value | match |
| OE 84 | PERSON_9727_EMAIL | SQL L465 (message frederick.stone@harmonygames.co/<CAOHCdeuLRHpqtIPQZRUGefwtjIwm5BrmgGS_Loo@mail.gmail.com>, from_email) | Omar Farouk PERSON_9727_EMAIL | F56 · VERIFIED value | match |
| OE 85 | PERSON_9728_EMAIL | SQL L472 (message frederick.stone@harmonygames.co/<CALcXsJB9Dsqckdbzui4zsoYGv8YD3gxSJbpOQzA@mail.gmail.com>, from_email) | Nadia Petrov PERSON_9728_EMAIL | F57 · VERIFIED value | match |
| OE 86 | PERSON_9729_EMAIL | SQL L476 (message frederick.stone@harmonygames.co/<CAdfSBCTPq8pDFK70IArhUSHj5PEV3Tnz19vDg7Y@mail.gmail.com>, from_email) | Kenji Mori PERSON_9729_EMAIL | F58 · VERIFIED value | match |
| OE 87 | PERSON_9730_EMAIL | SQL L483 (message frederick.stone@harmonygames.co/<CAFrM1JgqylGFM5MjwuqQMZPLsTjafUxYfbcriCb@mail.gmail.com>, from_email) | Clara Weiss PERSON_9730_EMAIL | F59 · VERIFIED value | match |
| OE 88 | PERSON_9731_EMAIL | SQL L490 (message frederick.stone@harmonygames.co/<CAff-LH5Vcdc03I5o2aYmpkuR0BE-z_AH8pa3w_W@mail.gmail.com>, from_email) | Pavel Sokol PERSON_9731_EMAIL | F60 · VERIFIED value | match |
| OE 89 | PERSON_9732_EMAIL | SQL L497 (message frederick.stone@harmonygames.co/<CA-DqRg1TZ4TPniI7P8AW7DvtD6lNosGZdpC1x6_@mail.gmail.com>, from_email) | Sofia Marin PERSON_9732_EMAIL | F61 · VERIFIED value | match |
| OE 90 | PERSON_2599_EMAIL | SQL L561 (contact 9b0185e445572aeee9f27d35) | PERSON_2599_EMAIL | F45 · VERIFIED value | match |
| OE 91 | PERSON_2599_EMAIL | SQL L561 (contact 9b0185e445572aeee9f27d35) | PERSON_2599_EMAIL | F46 · VERIFIED value | match |
| OE 92 | PERSON_2599_EMAIL | SQL L561 (contact 9b0185e445572aeee9f27d35) | PERSON_2599_EMAIL | F47 · VERIFIED value | match |
| OE 93 | Bundlehouse | trello data.json /lists/3 (To Do 640643a3fd8f3ca308d93195) via hg.py | To Do | F47 · VERIFIED value | match |
| OE 94 | Kinetic Arcade | trello data.json /lists/3 (To Do 640643a3fd8f3ca308d93195) via hg.py | To Do | F45 · VERIFIED value | match |
| OE 95 | Lumencloud | trello data.json /lists/3 (To Do 640643a3fd8f3ca308d93195) via hg.py | To Do | F46 · VERIFIED value | match |
| OE 96 | Markward | trello data.json /lists/3 (To Do 640643a3fd8f3ca308d93195) via hg.py | To Do | F49 · VERIFIED value | match |
| OE 97 | Nintendo | trello data.json /lists/3 (To Do 640643a3fd8f3ca308d93195) via hg.py | To Do | F29 · VERIFIED value | match |
| OE 98 | Orbit Store | trello data.json /lists/3 (To Do 640643a3fd8f3ca308d93195) via hg.py | To Do | F48 · VERIFIED value | match |
| OE 99 | Playfuse | trello data.json /lists/3 (To Do 640643a3fd8f3ca308d93195) via hg.py | To Do | F50 · VERIFIED value | match |
| OE 100 | None of the other 32 people | hg.py search-many contacts contacts.json (32 queries, scan_complete, control 'Hayes' 2 hits) | 0 hits each | F75 · VERIFIED value | match |
| OE 101 | PERSON_9712_EMAIL | SQL L375 (message frederick.stone@harmonygames.co/<CA0BbU6OEljE3nhaS2pWMojXL9GJ_kYqFO8JTtP2@mail.gmail.com>, from_email) | Lucia Ferrer PERSON_9712_EMAIL | F41 · VERIFIED value | match |
| OE 102 | PERSON_0527_EMAIL | hg.py get gmail threads/frederick@harmonygames.co_1840501641217286806.json (rep's From) | PERSON_0527_NAME (PERSON_0527_EMAIL) | F62 · VERIFIED value | match |
| OE 103 | PERSON_9730_EMAIL | SQL L483 (message frederick.stone@harmonygames.co/<CAFrM1JgqylGFM5MjwuqQMZPLsTjafUxYfbcriCb@mail.gmail.com>, from_email) | Clara Weiss PERSON_9730_EMAIL | F59 · VERIFIED value | match |
| OE 104 | PERSON_9706_EMAIL | SQL L327 (message frederick.stone@harmonygames.co/<CA-xgF65XCwo6QXURZM_eCJcAClcs_LfeftzR27P@mail.gmail.com>, from_email) | Ines Varga PERSON_9706_EMAIL | F35 · VERIFIED value | match |
| OE 105 | PERSON_9718_EMAIL | SQL L411 (message frederick.stone@harmonygames.co/<CAlSBl5tSj6BhvNqcMHhDChnKE3Fcp7fgMJdKNtH@mail.gmail.com>, from_email) | Freya Olsen PERSON_9718_EMAIL | F47 · VERIFIED value | match |
| OE 106 | PERSON_9715_EMAIL | SQL L390 (message frederick.stone@harmonygames.co/<CApaJB4i_PhvJp_95Q3bE-l9yDV4x096tsJobB11@mail.gmail.com>, from_email) | Jonas Weber PERSON_9715_EMAIL | F44 · VERIFIED value | match |
| OE 107 | PERSON_9704_EMAIL | SQL L303 (message frederick.stone@harmonygames.co/<CAFEbdSLTqGx4K9ylCWMjfozRDorLWGyAc5mo6e7@mail.gmail.com>, from_email) | Priya Raman PERSON_9704_EMAIL | F33 · VERIFIED value | match |
| OE 108 | PERSON_9724_EMAIL | SQL L450 (message frederick.stone@harmonygames.co/<CAXUVl-vI7c6T4f22vI41yY2P83JxLRUdeHW1-hC@mail.gmail.com>, from_email) | Yara Nasser PERSON_9724_EMAIL | F53 · VERIFIED value | match |
| OE 109 | PERSON_9732_EMAIL | SQL L497 (message frederick.stone@harmonygames.co/<CA-DqRg1TZ4TPniI7P8AW7DvtD6lNosGZdpC1x6_@mail.gmail.com>, from_email) | Sofia Marin PERSON_9732_EMAIL | F61 · VERIFIED value | match |
| OE 110 | PERSON_9725_EMAIL | SQL L457 (message frederick.stone@harmonygames.co/<CAHV7my-sLo9CEzISCj6j5YvPRBW1ReAHi-SrN7V@mail.gmail.com>, from_email) | Bruno Costa PERSON_9725_EMAIL | F54 · VERIFIED value | match |
| OE 111 | PERSON_9701_EMAIL | SQL L292 (message frederick.stone@harmonygames.co/<CAGJkuaxoKn_J2zxTzhLswrYwOGA_wA5IXe9v747@mail.gmail.com>, from_email) | Maren Holt PERSON_9701_EMAIL | F30 · VERIFIED value | match |
| OE 112 | PERSON_9723_EMAIL | SQL L446 (message frederick.stone@harmonygames.co/<CApanLB9xL5jrjcNSzDTWYvE6RiWdfZchZxr4q3K@mail.gmail.com>, from_email) | Tomas Novotny PERSON_9723_EMAIL | F52 · VERIFIED value | match |
| OE 113 | PERSON_9722_EMAIL | SQL L436 (message frederick.stone@harmonygames.co/<CAhKYUa4HtPNJGhGU5qifbVfYwMCjxb0DSaMXtME@mail.gmail.com>, from_email) | Gemma Doyle PERSON_9722_EMAIL | F51 · VERIFIED value | match |
| OE 114 | PERSON_9702_EMAIL | SQL L320 (message frederick.stone@harmonygames.co/<CArrsRpTwnF5vDz3j8sB1bdi-2N8lorF7bNSSbk-@mail.gmail.com>, from_email) | Wen Halvorsen PERSON_9702_EMAIL | F31 · VERIFIED value | match |
| OE 115 | PERSON_9710_EMAIL | SQL L361 (message frederick.stone@harmonygames.co/<CAb3f_RRKlDbfktS3_Cu7qnXPyTybHnS1K2Eq3b7@mail.gmail.com>, from_email) | Elena Petrova PERSON_9710_EMAIL | F39 · VERIFIED value | match |
| OE 116 | PERSON_9731_EMAIL | SQL L490 (message frederick.stone@harmonygames.co/<CAff-LH5Vcdc03I5o2aYmpkuR0BE-z_AH8pa3w_W@mail.gmail.com>, from_email) | Pavel Sokol PERSON_9731_EMAIL | F60 · VERIFIED value | match |
| OE 117 | PERSON_9733_EMAIL | SQL L501 (message frederick.stone@harmonygames.co/<CAroxkgBywTvnZooHWA1QvDuZcDMuI8XdpMtLkts@mail.gmail.com>, from_email) | Hugo Lambert PERSON_9733_EMAIL | F63 · VERIFIED value | match |
| OE 118 | PERSON_9719_EMAIL | SQL L418 (message frederick.stone@harmonygames.co/<CAo7WkZSvPT7fVQd40F1HezmilqIw9AoAb6_uTM2@mail.gmail.com>, from_email) | Mateo Rossi PERSON_9719_EMAIL | F48 · VERIFIED value | match |
| OE 119 | PERSON_9711_EMAIL | SQL L368 (message frederick.stone@harmonygames.co/<CAM5dEEI7CWxEdApgrQnK2XC211TZL1KF-WNUpsB@mail.gmail.com>, from_email) | Arjun Shah PERSON_9711_EMAIL | F40 · VERIFIED value | match |
| OE 120 | PERSON_9703_EMAIL | SQL L296 (message frederick.stone@harmonygames.co/<CAZgisbRwHgHd3Hk_E9LYMNIOFiMZminBj4K2tWc@mail.gmail.com>, from_email) | Dana Whitfield PERSON_9703_EMAIL | F32 · VERIFIED value | match |
| OE 121 | PERSON_9705_EMAIL | SQL L307 (message frederick.stone@harmonygames.co/<CAC1R0eFyTK7ezriX3kHgoWqGCC1DkbKElci5sJ8@mail.gmail.com>, from_email) | Teodor Lind PERSON_9705_EMAIL | F34 · VERIFIED value | match |
| OE 122 | PERSON_9721_EMAIL | SQL L429 (message frederick.stone@harmonygames.co/<CAWCBU--R8_Q4xxjtvPvDrzjjgqqRxz_flrPVZo6@mail.gmail.com>, from_email) | Iris Navarro PERSON_9721_EMAIL | F50 · VERIFIED value | match |
| OE 123 | PERSON_9726_EMAIL | SQL L461 (message frederick.stone@harmonygames.co/<CAGdptfs7cIHOLvLgF6LBpN_8DHhsOmA8Oqoddfh@mail.gmail.com>, from_email) | Ava Lindqvist PERSON_9726_EMAIL | F55 · VERIFIED value | match |
| OE 124 | PERSON_9728_EMAIL | SQL L472 (message frederick.stone@harmonygames.co/<CALcXsJB9Dsqckdbzui4zsoYGv8YD3gxSJbpOQzA@mail.gmail.com>, from_email) | Nadia Petrov PERSON_9728_EMAIL | F57 · VERIFIED value | match |
| OE 125 | PERSON_9727_EMAIL | SQL L465 (message frederick.stone@harmonygames.co/<CAOHCdeuLRHpqtIPQZRUGefwtjIwm5BrmgGS_Loo@mail.gmail.com>, from_email) | Omar Farouk PERSON_9727_EMAIL | F56 · VERIFIED value | match |
| OE 126 | PERSON_9708_EMAIL | SQL L344 (message frederick.stone@harmonygames.co/<CAEcTJxNSlNWdzmdlv0uAxA5LWo-4JRqmN_lbkGs@mail.gmail.com>, from_email) | Hana Kobayashi PERSON_9708_EMAIL | F37 · VERIFIED value | match |
| OE 127 | PERSON_9707_EMAIL | SQL L337 (message frederick.stone@harmonygames.co/<CAa-jv7GWQa7i06XwUWtNIJ_DInBkE5Qi4Y8PmMT@mail.gmail.com>, from_email) | Rafael Moreno PERSON_9707_EMAIL | F36 · VERIFIED value | match |
| OE 128 | PERSON_9734_EMAIL | SQL L515 (message frederick.stone@harmonygames.co/<CAjj6h7BzqoAZSS2-4M7N9e7ZLBDyeyZXl0BwgcI@mail.gmail.com>, from_email) | Rina Takeda PERSON_9734_EMAIL | F64 · VERIFIED value | match |
| OE 129 | PERSON_9709_EMAIL | SQL L351 (message frederick.stone@harmonygames.co/<CAIauDHOvbuHs1D8VFmRdi2YfR01quJPqo1ZiQZJ@mail.gmail.com>, from_email) | Kofi Mensah PERSON_9709_EMAIL | F38 · VERIFIED value | match |
| OE 130 | PERSON_9729_EMAIL | SQL L476 (message frederick.stone@harmonygames.co/<CAdfSBCTPq8pDFK70IArhUSHj5PEV3Tnz19vDg7Y@mail.gmail.com>, from_email) | Kenji Mori PERSON_9729_EMAIL | F58 · VERIFIED value | match |
| OE 131 | PERSON_9714_EMAIL | SQL L386 (message frederick.stone@harmonygames.co/<CASRfZCkXuHwLJPLUeim95W1qFlzEaz37BReSyJz@mail.gmail.com>, from_email) | Mila Novak PERSON_9714_EMAIL | F43 · VERIFIED value | match |
| OE 132 | PERSON_9713_EMAIL | SQL L382 (message frederick.stone@harmonygames.co/<CAHavdKpt7nR3fxojrxKL1PYVBWt8ridR2XEm01t@mail.gmail.com>, from_email) | Sven Aalto PERSON_9713_EMAIL | F42 · VERIFIED value | match |
| OE 133 | Mon Jan 5, 2026 | SQL L541 (evt_fd469c29811879519c2c96 start_ts) | 2026-01-05T17:00:00Z | F62 · VERIFIED value | match |
| OE 134 | Mon Jan 5, 2026 | SQL L541 (evt_fd469c29811879519c2c96 start_ts) | 2026-01-05T17:00:00Z | F59 · VERIFIED value | match |
| OE 135 | Mon Jan 5, 2026 | SQL L541 (evt_fd469c29811879519c2c96 start_ts) | 2026-01-05T17:00:00Z | F53 · VERIFIED value | match |
| OE 136 | Mon Jan 5, 2026 | SQL L541 (evt_fd469c29811879519c2c96 start_ts) | 2026-01-05T17:00:00Z | F61 · VERIFIED value | match |
| OE 137 | Mon Jan 5, 2026 | SQL L541 (evt_fd469c29811879519c2c96 start_ts) | 2026-01-05T17:00:00Z | F54 · VERIFIED value | match |
| OE 138 | Mon Jan 5, 2026 | SQL L541 (evt_fd469c29811879519c2c96 start_ts) | 2026-01-05T17:00:00Z | F30 · VERIFIED value | match |
| OE 139 | Mon Jan 5, 2026 | SQL L541 (evt_fd469c29811879519c2c96 start_ts) | 2026-01-05T17:00:00Z | F52 · VERIFIED value | match |
| OE 140 | Mon Jan 5, 2026 | SQL L541 (evt_fd469c29811879519c2c96 start_ts) | 2026-01-05T17:00:00Z | F51 · VERIFIED value | match |
| OE 141 | Mon Jan 5, 2026 | SQL L541 (evt_fd469c29811879519c2c96 start_ts) | 2026-01-05T17:00:00Z | F31 · VERIFIED value | match |
| OE 142 | Mon Jan 5, 2026 | SQL L541 (evt_fd469c29811879519c2c96 start_ts) | 2026-01-05T17:00:00Z | F60 · VERIFIED value | match |
| OE 143 | Mon Jan 5, 2026 | SQL L541 (evt_fd469c29811879519c2c96 start_ts) | 2026-01-05T17:00:00Z | F55 · VERIFIED value | match |
| OE 144 | Mon Jan 5, 2026 | SQL L541 (evt_fd469c29811879519c2c96 start_ts) | 2026-01-05T17:00:00Z | F57 · VERIFIED value | match |
| OE 145 | Mon Jan 5, 2026 | SQL L541 (evt_fd469c29811879519c2c96 start_ts) | 2026-01-05T17:00:00Z | F56 · VERIFIED value | match |
| OE 146 | Mon Jan 5, 2026 | SQL L541 (evt_fd469c29811879519c2c96 start_ts) | 2026-01-05T17:00:00Z | F58 · VERIFIED value | match |
| OE 147 | leonard.hayes@harmonygames.co | SQL L252 (message frederick.stone@harmonygames.co/<CAlIXcq3nWlSRBAZONcbY9d2v0ggkPYER8WfaoZa@mail.gmail.com>, from_email) | leonard.hayes@harmonygames.co | F1, F29, F32, F43–F50 · VERIFIED value | match |

Narrative checks re-read in this run (not quoted spans): senders and recipients of every company thread (SQL gmail rows: to_json/cc_json), Hugo's mail To Frederick with Arthur cc (SQL L501), ESG's note cc Frederick, Robert and Arthur (SQL L260), the hub to Frederick only with no cc (SQL L252), Frederick on all seven Balancy messages (gmail threads/frederick@harmonygames.co_1840501641217286806.json), Frederick's Rayking reply to Leonard only and the Playable Factory, Gamesforum SF and InterCo threads holding only their senders' messages (hg.py get on each thread), both Nintendo notices carrying 'Please do not reply' (gmail threads/frederick@harmonygames.co_1842358947604469113.json, _1842359398719557772.json), and every PT day and time converted from the record's UTC or offset time.

## Findings

No defect found in the current file: no INCOMPLETE, INACCURATE, MINOR, non-action, final-response or format finding. The independent review's items and the pre-check revisions are recorded under Advisory with their dispositions.

## Pre-verdict sweep

| Eval 4.0 check (7) | Result |
|---|---|
| One wrong count, ID, channel or tool | none: counts recomputed (36 rows, 31 answers, 7 cards, 3 ESG, 32 contacts, 14 reminders) from truth.json and the records; channels C07C2866011 and D05S58U4SAK; every write maps to a cataloged tool (Evals/references/tools/catalog.json) |
| One missing write | none: every write family in ledger §C (08_OE_Writing_Ledger.md) has its events, one write per event, OE 55–147 |
| One Expected fact with no retrieving event | none: every value an Expected line uses is read by that event or an earlier one it cites (Coverage F1–F75) |
| One unledgered Expected value or unbacked absence word | none: 193 quoted spans re-read; absence words are thread-bounded ('holds only', 'only their') or backed by a complete scan (OE 100, hg.py search-many contacts) |
| One act-vs-defer conflict | none: ledger §C defer search complete; the only holds are Framewell's waiver (OE 43) and the Answered rows (OE 16, 17, 18, 20), which the path obeys |
| One non-action or final-response event | none: no event describes the final response or a non-action; 'no new answer' appears only as analysis inside read events |
| One prompt-forbidden or reserved write | none: no 'I'll' reservation in 04_Prompt.txt; no write to an Answered company (guardrails step 1, SQL L6) |
| One missing recovery or wait event | none: 03_Error_Async_Config.txt is Friction: none |

## Advisory (no effect on the prediction)

| Event | Note |
|---|---|
| OE 4 | Pre-check revision: 'founders cc' changed to 'cc Frederick, Robert and Arthur' (the note's cc_json, SQL L259). |
| OE 18 | Pre-check revision: 'to Frederick and Arthur' changed to 'to Frederick, Arthur cc' (Hugo's mail, cc_json). |
| OE 15, OE 23 | Pre-check revision: Frederick's holding replies ('we'll take a look and get back to you', 'I'll come back to you on this') named as not answers, so guardrails step 1 is visibly checked. |
| OE 15, OE 19 | Pre-check revision: counterfactual sentences ('would go to signing', 'would fail the cash test') removed; the next event settles each row. |
| OE 40 | Pre-check revision: 'No date to meet' bounded to 'The paper and Leah's two mails give no date'. |
| all | Size: 147 events, about 46,900 characters, to be typed by hand (the field blocks pasting). Screen 44 asks for no redundant events; none is redundant (each write is its own event by the one-write rule). |
| OE 14 | Pre-check revision (independent review #1, confirmed): the NCsoft exclusion no longer says 'only a meeting recap'; Frederick's mailbox also holds the 15-message NCsoft thread (gmail threads/frederick@harmonygames.co_1832208184829815962.json). It now quotes Leonard's Thu Sep 25 'conversations with other VCs and companies are moving along' and excludes NCsoft as investor talks per OE 1. |
| OE 14 | Pre-check revision (confirmed while checking #1): Dentsu now quotes Leonard's Tue Sep 23 'Dentsu’s investment focus across games, transmedia, and AI-powered game development tools' (gmail threads/frederick@harmonygames.co_1843473831194478743.json) instead of 'nothing offered to us'. |
| OE 14 | Pre-check revision (independent review #2, confirmed): Leonard shared a 'Balancy' deck with Frederick on Aug 14 (gmail threads/frederick@harmonygames.co_1840455332185590750.json), so 'no paper' became 'nothing in the paperwork folder'. |
| OE 14 | Pre-check revision (independent review #3, confirmed): Gamesforum also sends newsletters (threads _1841691265035833180, _1844242809988457865); the line now reads 'a Sep 10 speaker invite whose thread holds only that message; their other mails are newsletters'. |
| OE 14 | Pre-check revision (independent review #4, confirmed): a third Nintendo mail that day is a Developer ID password reset (thread _1842359033385836403); 'portal notices' became 'Nintendo Developer Portal notices', which the two cited subjects carry. Balancy now 'Frederick on every message' (all 7 carry him in To or Cc). |
| OE 15, OE 38 | Route note from the independent review: the Lanternfly and Bundlehouse papers are Slides decks; the headings now say 'its deck in Drive/Slides' (gslides_get_presentation_text). |
| OE 16–20, OE 35 | Independent review, kept: 'no new answer, no reminder' sits inside the analysis of read events as the outcome of guardrails step 1 (SQL L6), a tool-observed finding, not a stand-alone NON_ACTION event (Eval 2 HARD GATE). |
| OE 14 | Pre-check revision (same class as review #3): InterCo's 'only their three mails' bounded to its thread. A complete search-many over Frederick's Gmail finds the Playable Factory, Gamesforum and InterCo senders (PERSON_5367_EMAIL, PERSON_5472_EMAIL, PERSON_3915_EMAIL) in their own threads only (threads _1843000993076735547, _1842890197572292911, _1841620870486605150). |
| OE 14 | /oe round 1 (NON-FAIL 3, Accuracy MINOR #1) fixed: the unsourced 'Jun 1 to Sep 30 2025' window became the whole inbox up to Sep 30, and Appodeal's publishing program (gmail threads/frederick@harmonygames.co_1830012626042968381.json: Frederick replied Apr 29 and May 14; 'ROAS-focused testing', 'Since we support parallel UA') is named as an ad-network/UA exclusion under OE 1. |
| OE 14 | /oe round 1 (Accuracy MINOR #2) fixed: Rayking's 'Frederick's reply went to Leonard only' became 'an unsent draft addressed to Leonard, labelled "Opened,Drafts"' (X-Gmail-Labels header, gmail threads/frederick@harmonygames.co_1842348778705877030.json). Class sweep: every seeded Frederick message the events call a reply or a first mail carries SENT (SQL label_ids_json). |
| OE 14 | /oe round 1 DR4 (rejected there, added here so a fresh reviewer has nothing to re-raise): AppCamp, an invite Frederick declined on Jun 21 ('I won't be able to make it'; event 'August 6–8, 2025'), gmail threads/frederick@harmonygames.co_1833464394449700499.json. |
| OE 56 | /oe round 1 readability note taken: the row event names Kinetic Arcade, Lumencloud and Bundlehouse as 'with our lawyers first'. |

## Tally

Blocking 0 (incomplete 0 · inaccurate 0 · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor 0 · unresolved 0 · advisory 18

## Self-review

Re-read as the eval: walked Evals/2_Oracle_Events_Eval.md 1.2 (inventory), 1.3 (five fields per STEP), the HARD GATE (no non-action or final-response event), 2.1–2.7 (service, tool, parameters, expected data, visibility, authority, act-vs-defer, format), 3.1–3.6 (completeness) and 4.0 (the sweep above) in order against the file, not from memory.

Re-verified: every quoted span (193) re-read from its record in this run by plan/assemble_oe_check.py (SQL parsed again, base through hg.py get); every write's recipient or target re-read from its source row; the Contacts absence re-run with hg.py search-many (complete scan, positive control); counts recomputed. No value was taken from the ledger, brief or dossier alone.

Five fields: every event names its action and service in the heading, its parameters (search text, subject, title, list, recipient) in the heading, the information and expected data on its Expected line, and its dependency as an 'OE n' pointer where it needs an earlier value.

Independent review: one general-purpose reviewer, given the file and the rules but not this report, read all 147 events against the SQL rows and the base records through hg.py (Gmail, Slack, Trello, Linear, the full Contacts file, Drive, the tool catalog). It confirmed every PT time and weekday, every recipient and cc, organizer, owner, folder contents, counts, persona membership (EMPLOYEE_0008 in C07C2866011 and D05S58U4SAK), the Contacts absence and every write tool. It raised four qualifier defects, all on OE 14 (NCsoft 'only', Balancy 'no paper', Gamesforum 'only', Nintendo notice count), and one route note on the two decks; each was re-verified here through hg.py and fixed in the draft before this check (Advisory). It predicted PASS 5 once those were fixed.

Counter-readings, one per Coverage row and Findings row:

| Item | Counter-reading and resolution (evidence) |
|---|---|
| R1 | Counter-reading — COVERED → best case missing: the hub could be another Sep 30 Leonard mail; OE 1 pins the subject 'Vendor and partner stuff while I'm in LA' and to-Frederick-only (SQL L251), the only Sep 30 Leonard mail to Frederick on vendors |
| R2 | Counter-reading — COVERED → best case missing: an incorporated rule could be missing (e.g. the July note or Robert's post); OE 1 names exactly four sources and OE 2–11 read each, F14/F15 are superseded or not rules (SQL L274, SQL L219) |
| R3 | Counter-reading — COVERED → best case missing: the population could be narrowed to the 33 papers; OE 14 adds Hootline, Balancy and Nintendo, which have no paper (gmail threads/frederick@harmonygames.co_1840501641217286806.json, ZOM-567), and rules out nine look-alikes with a reason each |
| R4 | Counter-reading — COVERED → best case missing: the log could be left outside the folder; OE 57 moves it into d_80a8c04753ba82ba4ba6a5 (brief §4b D1) |
| R5 | Counter-reading — COVERED → best case missing: the Answered rows or Nintendo could be owed an answer; guardrails step 1 'don't write to them again' and 'Portals and no-reply notices don't need one' (SQL L6) exclude them, and Priya's own ask adds OE 59 (SQL L285) |
| R6 | Counter-reading — COVERED → best case missing: Lanternfly could look like a Sign card; OE 16 settles it as Answered (D05S58U4SAK/1759174260.052645), so the card set is exactly 7 |
| R7 | Counter-reading — COVERED → best case missing: Playfuse's 2-year NDA could look like an ESG case; OE 4 quotes 'Mutual NDAs on our template don't need review, whatever their term' (SQL L259) |
| R8 | Counter-reading — COVERED → best case missing: 'this week' could be read as allowing drafts; each answer event expects a sent reply (Eval 2 §2.1 tool must complete the step) |
| R9 | Counter-reading — COVERED → best case missing: Framewell or Lanternfly could fall out of the January set; OE 43 and OE 16 bring both back (C07C2866011/1758920520.674991, D05S58U4SAK/1759174260.052645) |
| R10 | Counter-reading — COVERED → best case missing: one listing event could be offered; brief §4b D6 and the prompt's 'one per company' require 14 separate events on evt_fd469c29811879519c2c96's day |
| R11 | Counter-reading — COVERED → best case missing: existing contacts could be added twice; OE 100 finds Noor Haddad, Aiden Clarke and Leah Brennan already there (SQL L561 rows) and the 32 others absent (hg.py search-many contacts, scan complete) |
| R12 | Counter-reading — COVERED → best case missing: the reply could be a new mail to Leonard; OE 147 replies on frederick.stone@harmonygames.co/1844732913254784171 with both lists (brief §4b D7) |
| F1 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 1 quotes it, re-read in this run (Leonard's vendor and partner email (the hub)) |
| F2 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 2 quotes it, re-read in this run (Runway guardrails doc: the five decisions, top to bottom) |
| F3 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 3 quotes it, re-read in this run (The Monday change: partner-booked travel counts as cash) |
| F4 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 4 quotes it, re-read in this run (ESG Law's signing note and Leonard's reply under it) |
| F5 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 quotes it, re-read in this run (ESG intake checklist: what each intake email carries) |
| F6 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 6 quotes it, re-read in this run (ESG Law intake address in Contacts) |
| F7 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 7 quotes it, re-read in this run (Frederick's Q4 commitments folder (log destination)) |
| F8 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 8 quotes it, re-read in this run (Folder README: sheet name, columns, decision words, Next dat) |
| F9 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 9 quotes it, re-read in this run (Log template header row) |
| F10 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 11 quotes it, re-read in this run (Arthur's keep-running list (the Keep exemption)) |
| F11 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 10 quotes it, re-read in this run (Harmony Games board and its To Do list (card destination)) |
| F12 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 12 quotes it, re-read in this run (The January commitments review date) |
| F13 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 13 quotes it, re-read in this run (Frederick's paperwork folder (each counterparty's filed pape) |
| F14 | Counter-reading — NOT NEEDED → best case it is required: the Leonard's July 'accept the terms yourself' note could decide a row; resolved: superseded: OE 4 quotes 'This replaces what I said in July' (SQL L274); the path never relies on it |
| F15 | Counter-reading — NOT NEEDED → best case it is required: the Robert's 'cancel every marketing tool' post could decide a row; resolved: an opinion, not a rule: OE 1 names the guardrails doc and the Monday change as the rules (SQL L251) |
| F16 | Counter-reading — NOT NEEDED → best case it is required: the UA spend buckets doc could decide a row; resolved: UA spend is off the backlog per OE 1's exclusion (SQL L251); no decision reads it |
| F17 | Counter-reading — NOT NEEDED → best case it is required: the July 31 vendor tracker could decide a row; resolved: stale; every row it carries is decided from the current paper or notice (OE 21–23) |
| F18 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 14 quotes it, re-read in this run (Nintendo developer portal mails (look done)) |
| F19 | Counter-reading — NOT NEEDED → best case it is required: the Frederick's Sep 4 'registered an account' post could decide a row; resolved: the sign-up is shown by the registration notice OE 14 reads (gmail threads/frederick@harmonygames.co_1842359398719557772.json) |
| F20 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 35 quotes it, re-read in this run (ZOM-567 and Arthur's comment: Nintendo still needs an office) |
| F21 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 43 quotes it, re-read in this run (Leonard's Sep 22 Playtestcloud post (root of the Framewell r) |
| F22 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 43 quotes it, re-read in this run (Framewell waiver: the Pro plan at no charge until Feb 1 (nam) |
| F23 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 16 quotes it, re-read in this run (Leonard's Sep 17 DM root 'we have no localization though') |
| F24 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 16 quotes it, re-read in this run (Lanternfly already answered by Leonard (names Wen and the So) |
| F25 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 20 quotes it, re-read in this run (Spotlight Fest already answered by Robert (names the Dec 5 i) |
| F26 | Counter-reading — NOT NEEDED → best case it is required: the Spotlight Fest showcase call (calendar) could decide a row; resolved: Robert's note in OE 20 carries who answered and when (C07C2866011/1758134460.899858) |
| F27 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 22 quotes it, re-read in this run (Paylane notice for workspace HG-2291: pilot ends Oct 15, bil) |
| F28 | Counter-reading — NOT NEEDED → best case it is required: the UGC Studio kickoff (calendar) could decide a row; resolved: the Clipforge paper's 'Workspace: HG-2291' in OE 21 ties the workspace (f_8d0e0e3ae076b2f745e7e2) |
| F29 | Counter-reading — COVERED → best case missing: Nintendo's row is decided but a write it needs has no event; resolved: decision Sign read in OE 35 from ZOM-567, writes OE 97 |
| F30 | Counter-reading — COVERED → best case missing: Framewell's row is decided but a write it needs has no event; resolved: decision Park read in OE 42 from frederick.stone@harmonygames.co/1843618067251203081 and f_fba21c2d5d4bbb02983961, writes OE 78, OE 111, OE 138 |
| F31 | Counter-reading — COVERED → best case missing: Lanternfly Publishing's row is decided but a write it needs has no event; resolved: decision Answered read in OE 15 from frederick.stone@harmonygames.co/1842800807116855774 and f_5dbbaf5b251d5261427eb1, writes OE 114, OE 141 |
| F32 | Counter-reading — COVERED → best case missing: Pingwise's row is decided but a write it needs has no event; resolved: decision Keep read in OE 34 from frederick.stone@harmonygames.co/1844157874176168845 and f_6c212cbfb31c3ded44ef8a, writes OE 71, OE 120 |
| F33 | Counter-reading — COVERED → best case missing: Clipforge's row is decided but a write it needs has no event; resolved: decision End read in OE 21 from frederick.stone@harmonygames.co/1837102635418059486 and f_8d0e0e3ae076b2f745e7e2, writes OE 59, OE 107 |
| F34 | Counter-reading — COVERED → best case missing: Pixel Harbor Events's row is decided but a write it needs has no event; resolved: decision End read in OE 23 from frederick.stone@harmonygames.co/1835288808653226583 and f_614f88a28a2f0cf1b88408, writes OE 60, OE 121 |
| F35 | Counter-reading — COVERED → best case missing: Brightlane Studio's row is decided but a write it needs has no event; resolved: decision End read in OE 24 from frederick.stone@harmonygames.co/1841809902797646290 and f_9d4639f91c93478d888f4b, writes OE 61, OE 104 |
| F36 | Counter-reading — COVERED → best case missing: Soundvault's row is decided but a write it needs has no event; resolved: decision End read in OE 25 from frederick.stone@harmonygames.co/1842719647334876669 and f_2686da1086bfcc2fba3f57, writes OE 62, OE 127 |
| F37 | Counter-reading — COVERED → best case missing: Reviewly's row is decided but a write it needs has no event; resolved: decision End read in OE 26 from frederick.stone@harmonygames.co/1843712439092112354 and f_4bdfb8e0c47288087c7bba, writes OE 63, OE 126 |
| F38 | Counter-reading — COVERED → best case missing: Streamcast Talent's row is decided but a write it needs has no event; resolved: decision End read in OE 27 from frederick.stone@harmonygames.co/1842998987980893279 and f_5b961c9c6887d31dcd2ee2, writes OE 64, OE 129 |
| F39 | Counter-reading — COVERED → best case missing: Lingora's row is decided but a write it needs has no event; resolved: decision End read in OE 28 from frederick.stone@harmonygames.co/1842168515789422611 and f_34ba4ac9a0f0fa4fd34e9e, writes OE 65, OE 115 |
| F40 | Counter-reading — COVERED → best case missing: Panelpulse's row is decided but a write it needs has no event; resolved: decision End read in OE 29 from frederick.stone@harmonygames.co/1842353484595925809 and f_41a9ea5036a231989745b2, writes OE 66, OE 119 |
| F41 | Counter-reading — COVERED → best case missing: Ascendo's row is decided but a write it needs has no event; resolved: decision End read in OE 30 from frederick.stone@harmonygames.co/1841081352192260725 and f_a9593b0bf23b760e2972c7, writes OE 67, OE 101 |
| F42 | Counter-reading — COVERED → best case missing: Wishwave's row is decided but a write it needs has no event; resolved: decision End read in OE 31 from frederick.stone@harmonygames.co/1843538794906427760 and f_54c2b4e172bb73a4a19845, writes OE 68, OE 132 |
| F43 | Counter-reading — COVERED → best case missing: Vaultline's row is decided but a write it needs has no event; resolved: decision Keep read in OE 32 from frederick.stone@harmonygames.co/1843980455117084538 and f_2715771ae5f0358ad39aa9, writes OE 69, OE 131 |
| F44 | Counter-reading — COVERED → best case missing: Certwell's row is decided but a write it needs has no event; resolved: decision Keep read in OE 33 from frederick.stone@harmonygames.co/1844067277209770126 and f_cfb172dea30b9f6ac8a340, writes OE 70, OE 106 |
| F45 | Counter-reading — COVERED → best case missing: Kinetic Arcade's row is decided but a write it needs has no event; resolved: decision Sign read in OE 36 from frederick.stone@harmonygames.co/1842895178957083445 and f_6252955f500f81e3aacbef, writes OE 72, OE 94, OE 90 |
| F46 | Counter-reading — COVERED → best case missing: Lumencloud's row is decided but a write it needs has no event; resolved: decision Sign read in OE 37 from frederick.stone@harmonygames.co/1842991438234544282 and f_a227b14f03e12005fe8324, writes OE 73, OE 95, OE 91 |
| F47 | Counter-reading — COVERED → best case missing: Bundlehouse's row is decided but a write it needs has no event; resolved: decision Sign read in OE 38 from frederick.stone@harmonygames.co/1843442535629243130 and f_9d1e0270574584de0eb92c, writes OE 74, OE 93, OE 92, OE 105 |
| F48 | Counter-reading — COVERED → best case missing: Orbit Store's row is decided but a write it needs has no event; resolved: decision Sign read in OE 39 from frederick.stone@harmonygames.co/1843708664218314020 and f_2ae7e3ee3220b628391234, writes OE 75, OE 98, OE 118 |
| F49 | Counter-reading — COVERED → best case missing: Markward's row is decided but a write it needs has no event; resolved: decision Sign read in OE 40 from frederick.stone@harmonygames.co/1842802694553769659 and f_71a95593c736b3baf45f91, writes OE 76, OE 96 |
| F50 | Counter-reading — COVERED → best case missing: Playfuse's row is decided but a write it needs has no event; resolved: decision Sign read in OE 41 from frederick.stone@harmonygames.co/1844256020889910750 and f_9a7fc4a3e45e4394227fa5, writes OE 77, OE 99, OE 122 |
| F51 | Counter-reading — COVERED → best case missing: Hootline's row is decided but a write it needs has no event; resolved: decision Park read in OE 44 from frederick.stone@harmonygames.co/1839631800730308867, writes OE 79, OE 113, OE 140 |
| F52 | Counter-reading — COVERED → best case missing: Glyphworks's row is decided but a write it needs has no event; resolved: decision Park read in OE 45 from frederick.stone@harmonygames.co/1843350051225919345 and f_f6701704e5659b05d9530f, writes OE 80, OE 112, OE 139 |
| F53 | Counter-reading — COVERED → best case missing: Cloudlark's row is decided but a write it needs has no event; resolved: decision Park read in OE 46 from frederick.stone@harmonygames.co/1843078260327282996 and f_eb94c65ce9f273c6b5a579, writes OE 81, OE 108, OE 135 |
| F54 | Counter-reading — COVERED → best case missing: Echohall's row is decided but a write it needs has no event; resolved: decision Park read in OE 47 from frederick.stone@harmonygames.co/1841538111898044975 and f_68e288146ba0eee9fc17fa, writes OE 82, OE 110, OE 137 |
| F55 | Counter-reading — COVERED → best case missing: Pressbeam's row is decided but a write it needs has no event; resolved: decision Park read in OE 48 from frederick.stone@harmonygames.co/1842983888486665921 and f_a9bb79c86b8b7b92083785, writes OE 83, OE 123, OE 143 |
| F56 | Counter-reading — COVERED → best case missing: Retainly's row is decided but a write it needs has no event; resolved: decision Park read in OE 49 from frederick.stone@harmonygames.co/1843346276352069546 and f_be21bac5d50e291ebfbe2b, writes OE 84, OE 125, OE 145 |
| F57 | Counter-reading — COVERED → best case missing: Quillcraft's row is decided but a write it needs has no event; resolved: decision Park read in OE 50 from frederick.stone@harmonygames.co/1842262887629456494 and f_af809bf6325b452edc8476, writes OE 85, OE 124, OE 144 |
| F58 | Counter-reading — COVERED → best case missing: Tilecast's row is decided but a write it needs has no event; resolved: decision Park read in OE 51 from frederick.stone@harmonygames.co/1843708664217753499 and f_6d13a63be892a29f796b78, writes OE 86, OE 130, OE 146 |
| F59 | Counter-reading — COVERED → best case missing: Benchmarkly's row is decided but a write it needs has no event; resolved: decision Park read in OE 52 from frederick.stone@harmonygames.co/1843984229991264696 and f_e916ab7563891481ab3b16, writes OE 87, OE 103, OE 134 |
| F60 | Counter-reading — COVERED → best case missing: Loopnote's row is decided but a write it needs has no event; resolved: decision Park read in OE 53 from frederick.stone@harmonygames.co/1842712097587609477 and f_6963d4d30aceef4f88966a, writes OE 88, OE 116, OE 142 |
| F61 | Counter-reading — COVERED → best case missing: Driftwood Audio's row is decided but a write it needs has no event; resolved: decision Park read in OE 54 from frederick.stone@harmonygames.co/1844165423924029064 and f_17878d7b82fafcee79bfe7, writes OE 89, OE 109, OE 136 |
| F62 | Counter-reading — COVERED → best case missing: Balancy's row is decided but a write it needs has no event; resolved: decision Answered read in OE 17 from gmail threads/frederick@harmonygames.co_1840501641217286806.json, writes OE 102, OE 133 |
| F63 | Counter-reading — COVERED → best case missing: Motive Forge's row is decided but a write it needs has no event; resolved: decision Answered read in OE 18 from frederick.stone@harmonygames.co/1843346276352084348 and f_e81c6ef89513cac632700a, writes OE 117 |
| F64 | Counter-reading — COVERED → best case missing: Spotlight Fest's row is decided but a write it needs has no event; resolved: decision Answered read in OE 19 from frederick.stone@harmonygames.co/1842712097588195482 and f_9d9cf4e53b1c8607f9c869, writes OE 128 |
| F65 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 14 quotes it, re-read in this run (Rayking Game: only forwarded around internally) |
| F66 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 14 quotes it, re-read in this run (Playable Factory: cold pitch nobody answered) |
| F67 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 14 quotes it, re-read in this run (Google partner check-in: an ad network) |
| F68 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 14 quotes it, re-read in this run (Gamesforum SF: speaker invite nobody answered) |
| F69 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 14 quotes it, re-read in this run (InterCo Digital: cold pitch nobody answered) |
| F70 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 14 quotes it, re-read in this run (Singular: named in the hub's UA exclusion) |
| F71 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 14 quotes it, re-read in this run (NCsoft: strategic / investor talks) |
| F72 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 14 quotes it, re-read in this run (Dentsu: investor meeting Leonard is flying to) |
| F73 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 14 quotes it, re-read in this run (Nova Rewards: offer withdrawn Sep 23) |
| F74 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 1 quotes it, re-read in this run (Mattel: Leonard keeps it) |
| F75 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 100 quotes it, re-read in this run (Counterparty contacts already in Contacts (no new contact)) |

Prediction per component: Completeness 5 (every §A requirement and every write family has an executing event; no non-action or final-response event) · Accuracy 5 (no value, recipient, state, date or tool contradicted by a record re-read in this run) · overall PASS 5.

Unresolved: none

```
STAGE GATE oe-check: PASS — Task_Authoring/task_inputs · 08_OE_Check.md#e10d9a9f5ca7 · 08_Oracle_Events.md#2cfc73ba1f10 · 08_OE_Writing_Ledger.md#ed3302df4e6a · __context__#db8af19cc1c3 · __assignment__#b196657eace0 · __policy__#dc4ab5df3cdd · __gate_policy__#115714063000 · __review__#d1d08c1c8c7d · blocking 0 · warnings 0 · checks 20
[PASS] assignment.v3_context: Frederick Stone / Co-founder; easy cap <90%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 08_OE_Check.md
[PASS] structure.inputs: 2 input(s) present: 08_Oracle_Events.md, 08_OE_Writing_Ledger.md
[PASS] structure.fresh: every output newer than its inputs (08_Oracle_Events.md, 08_OE_Writing_Ledger.md)
[PASS] chain.oe-writing: upstream 'oe-writing' PASS pasted and current (08_OE_Writing_Ledger.md#ed3302df4e6a, 00_Assigments.md#5418f950517f, 04_Prompt.txt#32f7ab0cabd6, 01_Grounding_Dossier.md#3c7feab09262, 01_Universe_Inject.sql#69603ab4b6a4, 03_Error_Async_Config.txt#2737eaf3c6bd, __context__#db8af19cc1c3, __assignment__#b196657eace0, __policy__#dc4ab5df3cdd, __gate_policy__#115714063000, __review__#d1d08c1c8c7d)
[PASS] structure.sections: 7 required sections present and non-empty (08_OE_Check.md)
[PASS] structure.placeholders: no placeholders in 08_OE_Check.md
[PASS] structure.header_counts: header matches 08_Oracle_Events.md (147 events, 47734 chars)
[PASS] structure.prediction: /oe prediction line present
[PASS] structure.clock: 'Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)' matches the universe
[PASS] evidence.quoted_spans: 0 quoted span(s) verified as exact substrings of 08_Oracle_Events.md
[PASS] evidence.findings_evidence: no rows/items found under 'findings' in 08_OE_Check.md
[PASS] evidence.signoff_reread: 147/147 items carry a source pointer (min 100%)
[PASS] structure.sweep: pre-verdict sweep has 8/7 rows
[PASS] structure.tally: tally Blocking 0 vs 0 BLOCKING findings
[PASS] review.counter_readings: 87 evidenced counter-readings (of 87 found; need ≥ 87) in 08_OE_Check.md
[PASS] review.coverage: self-review addresses all 1 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## Reminders
- The tool-call minimum is measured on the golden run or the 6-rollout average, never on the OE count.
- Any edit to 08_Oracle_Events.md stales this check and any later rubric review: re-run plan/assemble_oe_events.py, then this script, then the gate.
- The platform field blocks pasting: type the file exactly as it stands (sha above).
