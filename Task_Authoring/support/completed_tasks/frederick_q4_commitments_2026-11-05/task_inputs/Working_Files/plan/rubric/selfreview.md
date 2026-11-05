## Self-review

Re-read as /rubric: walked Evals/3_Rubrics_Eval.md 1.4 and 3.1 against the plan in order. Every prompt requirement (ledger R1–R12), every write family (log, written answers, ESG intake, cards, contacts, reminders, reply), both told lists in the reply, every exclusion (the look-alikes, as exact counts on the required writes) and the ordering ask ('When it's all done') has a row on the correct artifact. No row grades the final response; the reply to Leonard is the deliverable the prompt names.

Re-verified: every source value in 00_V3_Authoring_Evidence.json was read in this run by plan/rubric/build_rubric.py — seeded rows by parsing 01_Universe_Inject.sql (never executed), base records through hg.py get-many (Balancy thread frederick.stone@harmonygames.co/1840501641217286806, Nintendo notice frederick.stone@harmonygames.co/1842359398719557772, Trello board 640643a3fd8f3ca308d9318e). The values each title names (dates, recipients, counts, company names) were re-read from the same records; the counts were recomputed from solver/truth.json and the records (36 rows, 31 answers, 3 ESG, 7 cards, 32 contacts, 14 reminders, 3 kept, 7 to sign). The eval's rubric lint (hg.py rubric-lint) reports 0 findings.

Predicted all-fail re-check: for every row the persona reaches the value through a cataloged tool (Gmail, Slack, Calendar and Drive records pasted YES under Visibility proof; Trello, Linear and Contacts unscoped), each write exists in the catalog (gsheets/gdrive, gmail_reply_to_message, gmail_send_message, trello_create_card, contacts_add_new_contact, gcal_create_event), no row needs a rate-1.0 retry, and no evidence sits outside Frederick's view. Count on the four bases: 0. The local grade below shows every row passed by at least one plausible run shape except the rows the six rev4 baselines all missed, and each of those is reachable (the misses are discovery failures, not impossible targets).

Local baseline grade (plan/rubric/grade_baselines.py over run_forensics/rev4/baseline/run-*/writes.json; a local estimate of the verifier, not its result):

```text
run-1: 0.706  rows 34 answered 33 esg 4 cards 7 contacts 31 jan5 11 | failed: log_rows nin_decision fw_decision lf_decision sp_decision lf_by sp_by bal_by nin_next lf_next lf_told ans_count ans_framewell esg_count card_nin ct_count rem_count rem_fw rem_lf reply_sign_count reply_nintendo
run-2: 0.720  rows 33 answered 32 esg 4 cards 7 contacts 30 jan5 11 | failed: log_rows nin_decision fw_decision lf_decision sp_decision lf_by sp_by bal_by nin_next lf_next lf_told ans_count ans_framewell esg_count card_nin ct_count rem_count rem_fw rem_lf reply_nintendo
run-3: 0.680  rows 34 answered 33 esg 3 cards 6 contacts 31 jan5 13 | failed: log_rows nin_decision fw_decision lf_decision sp_decision sv_waiting lf_by sp_by bal_by nin_next ph_next ph_told lf_told sv_told ww_told ans_count rev_cancel ans_framewell esg_bh_term card_count card_nin ct_count rem_count rem_fw reply_sign_count reply_nintendo
run-4: 0.720  rows 34 answered 33 esg 4 cards 7 contacts 31 jan5 11 | failed: log_rows nin_decision fw_decision lf_decision sp_decision lf_by sp_by bal_by nin_next lf_next lf_told ans_count ans_framewell esg_count card_nin ct_count rem_count rem_fw rem_lf reply_nintendo
run-5: 0.680  rows 34 answered 33 esg 3 cards 6 contacts 31 jan5 13 | failed: log_rows nin_decision fw_decision lf_decision sp_decision sv_waiting lf_by sp_by bal_by nin_next ph_next ph_told lf_told sv_told ww_told ans_count rev_cancel ans_framewell esg_bh_term card_count card_nin ct_count rem_count rem_fw reply_sign_count reply_nintendo
run-6: 0.680  rows 33 answered 32 esg 4 cards 7 contacts 30 jan5 10 | failed: log_rows nin_decision fw_decision lf_decision sp_decision lf_by sp_by bal_by nin_next lf_next lf_told ans_count ans_framewell ans_hootline esg_count card_nin ct_count ct_hoot rem_count rem_fw rem_lf rem_hoot reply_sign_count reply_nintendo
rows 102 weight 350 · mean 0.698 · SD 0.018 (sample 0.020)
failure patterns: 4 largest 2 of 6
failed by every run: ['ans_count', 'ans_framewell', 'bal_by', 'card_nin', 'ct_count', 'fw_decision', 'lf_by', 'lf_decision', 'lf_told', 'log_rows', 'nin_decision', 'nin_next', 'rem_count', 'rem_fw', 'reply_nintendo', 'sp_by', 'sp_decision']
```

Shortcut and diversity: the §F probe hits are dispositioned below the paste. The largest unit of discovery is the guardrails doc (F2), upstream of every decision row by construction — see Unresolved.

Surface dispositions: X9 (Clipforge Decision) and X14 (Framewell Next date) are the only dispositioned slots. Strongest case for a row: each is a log cell the README asks for, and the log's Decision and Next date columns are sampled. Resolution: the facts are graded on their own deliverables (P29/P19/P30; P7/P52/P87), the Decision and Next date samples are already at five each (gate 15), and /rubric round 1 raised no coverage gap for either cell.

Counter-readings, one per section A row:

| P | Counter-reading (a valid answer that could fail · a wrong answer that could pass) and resolution (evidence) |
|---|---|
| P1 | Counter-reading — (a) a copy of the template made inside the folder counts as created there; a sheet moved in passes · (b) a sheet left in My Drive fails on d_80a8c04753ba82ba4ba6a5 |
| P2 | Counter-reading — (a) a template copied as a Google Sheet passes · (b) an uploaded xlsx fails against README f_846ddc38b2aab3d2ed3fcb ('One sheet') |
| P3 | Counter-reading — (a) any letter case or spacing passes · (b) 'Vendor backlog' fails; README f_846ddc38b2aab3d2ed3fcb fixes the name (brief §4b's wider name class is superseded by the incorporated README line) |
| P4 | Counter-reading — (a) a header in another letter case is accepted; columns appended after Next date stay legal · (b) a dropped 'Answered by' fails against README f_846ddc38b2aab3d2ed3fcb |
| P5 | Counter-reading — (a) duplicate rows for one company count once (title: one row per company) · (b) 37 rows with Appodeal or NCsoft fail; the sweep OE 14 lists every look-alike with its reason (F65–F73) |
| P6 | Counter-reading — (a) 'Nintendo Developer Portal' as the company name is accepted · (b) End or Answered from the 'Registration Completed' notice fails against ZOM-567 comment cmt_c9a6660d81e067ad1de7 |
| P7 | Counter-reading — (a) none: Park is the only fair Decision once C07C2866011/1758920520.674991 is read (brief §4b D1) · (b) End from the order form f_fba21c2d5d4bbb02983961 fails |
| P8 | Counter-reading — (a) none: guardrails step 1 is first-fit (f_b98287f6f80fe431a71209) · (b) Sign from the 2-year exclusive deck fails; Park fails (Leonard already answered, D05S58U4SAK/1759174260.052645) |
| P9 | Counter-reading — (a) none: step 1 stops the order · (b) End from Rina's $750 ask fails; C07C2866011/1758134460.899858 is the answer |
| P10 | Counter-reading — (a) none: Keep is the only fair Decision once the keep-running card's 'night pager' is matched to Pingwise's paging · (b) End from the $29/month fails; thread frederick.stone@harmonygames.co/1844157874176168845 |
| P11 | Counter-reading — (a) 'Hana' alone, 'Hana Kobayashi' or PERSON_9708_EMAIL passes (title now names 'or Hana') · (b) a blank cell fails; Reviewly thread frederick.stone@harmonygames.co/1843712439092112354 |
| P12 | Counter-reading — (a) 'license' (US spelling) or 'trailer music pack licence' passes ('in any wording') · (b) a blank cell fails; paper f_2686da1086bfcc2fba3f57 |
| P13 | Counter-reading — (a) 'Leonard (Sep 27)' or 'Leonard Hayes, Sat Sep 27' accepted · (b) Frederick fails: his Sep 10 reply is a holding reply (thread frederick.stone@harmonygames.co/1842800807116855774) |
| P14 | Counter-reading — (a) 'Robert, Sep 17' accepted · (b) blank fails; Robert's post C07C2866011/1758134460.899858 names the answer |
| P15 | Counter-reading — (a) 'Leonard, Sep 11' (PT) or Sep 12 (UTC) both accepted — the date is not graded · (b) a missing Balancy row fails; the base thread frederick.stone@harmonygames.co/1840501641217286806 holds the answer |
| P16 | Counter-reading — (a) 'Arthur Blake' accepted · (b) blank fails; Arthur's Sep 19 reply is in thread frederick.stone@harmonygames.co/1843346276352084348 |
| P17 | Counter-reading — (a) the date in Answered by ('Arthur Blake, Sep 19, 2025') or in What we told them passes (any column) · (b) no date fails; Arthur's 2025-09-19T17:45Z reply is Sep 19 in both Pacific and UTC |
| P18 | Counter-reading — (a) 'Oct 15, 2025' or '10/15/2025' accepted · (b) blank or Sep 4 (the notice date) fails; ZOM-567 comment gives Oct 15 |
| P19 | Counter-reading — (a) any date form accepted · (b) Jan 15, 2026 from f_8d0e0e3ae076b2f745e7e2 fails; the notice frederick.stone@harmonygames.co/1843067564852153540 overrides it |
| P20 | Counter-reading — (a) any date form accepted · (b) Oct 20 or Oct 24 from f_614f88a28a2f0cf1b88408 fails (README: last day to say no) |
| P21 | Counter-reading — (a) any date form accepted · (b) Oct 31 (the downgrade cut-off, thread frederick.stone@harmonygames.co/1844157874176168845) fails; README Keep rule: when it next bills |
| P22 | Counter-reading — (a) 'Jan 5, 2026' or '2026-01-05' passes · (b) blank (Answered with no date) fails: the README gives 'later' answers the January review; D05S58U4SAK/1759174260.052645 says January |
| P23 | Counter-reading — (a) 'released the booth hold' carries the decline and passes · (b) 'parked' fails; booth quote f_614f88a28a2f0cf1b88408 bills before January |
| P24 | Counter-reading — (a) wording with 'after the raise' with or without January passes · (b) 'with our lawyers first' fails; D05S58U4SAK/1759174260.052645 |
| P25 | Counter-reading — (a) 'declined the licence' passes · (b) 'parked' fails; f_2686da1086bfcc2fba3f57 is paid on signature |
| P26 | Counter-reading — (a) 'ESG review first, then Leonard or Arthur' passes · (b) 'with Leonard or Arthur' alone fails; ESG note frederick.stone@harmonygames.co/1844177063117059830 lists exclusivity |
| P27 | Counter-reading — (a) 'declined, travel counts as cash' passes · (b) 'parked' (the doc's original travel rule) fails; C07C2866011/1759166100.370044 |
| P28 | Counter-reading — (a) a reply plus a new mail to one company counts once; Clipforge's two mails count once · (b) 33 (Rina and Wen written to again) fails; guardrails f_b98287f6f80fe431a71209 step 1 |
| P29 | Counter-reading — (a) a new email or a forward to billing@paylane.io both pass · (b) a reply to the unmonitored notice fails (frederick.stone@harmonygames.co/1843067564852153540) |
| P30 | Counter-reading — (a) 'we won't be carrying on after the pilot' passes · (b) an email that only says the pilot ends (a fact) fails; Priya's Sep 22 ask in thread frederick.stone@harmonygames.co/1837102635418059486 |
| P31 | Counter-reading — (a) 'we won't go ahead', 'we're passing' or 'please release the hold' carries the decline and passes · (b) parking Pixel Harbor Events for January fails: its offer costs cash before January (guardrails step 2) |
| P32 | Counter-reading — (a) 'we won't go ahead', 'we're passing' or 'please release the hold' carries the decline and passes · (b) parking Brightlane Studio for January fails: its offer costs cash before January (guardrails step 2) |
| P33 | Counter-reading — (a) 'we won't go ahead', 'we're passing' or 'please release the hold' carries the decline and passes · (b) parking Soundvault for January fails: its offer costs cash before January (guardrails step 2) |
| P34 | Counter-reading — (a) 'we won't go ahead', 'we're passing' or 'please release the hold' carries the decline and passes · (b) parking Streamcast Talent for January fails: its offer costs cash before January (guardrails step 2) |
| P35 | Counter-reading — (a) 'we won't go ahead', 'we're passing' or 'please release the hold' carries the decline and passes · (b) parking Lingora for January fails: its offer costs cash before January (guardrails step 2) |
| P36 | Counter-reading — (a) 'we won't go ahead', 'we're passing' or 'please release the hold' carries the decline and passes · (b) parking Panelpulse for January fails: its offer costs cash before January (guardrails step 2) |
| P37 | Counter-reading — (a) 'we won't go ahead', 'we're passing' or 'please release the hold' carries the decline and passes · (b) parking Ascendo for January fails: its offer costs cash before January (guardrails step 2) |
| P38 | Counter-reading — (a) 'we won't be doing the expo push' passes · (b) parking it under the doc's original travel rule fails; C07C2866011/1759166100.370044 |
| P39 | Counter-reading — (a) a reply or new email to Hana cancelling passes · (b) parking Reviewly (two rev4 baselines) fails; terms f_4bdfb8e0c47288087c7bba |
| P40 | Counter-reading — (a) 'please go ahead and reissue it' confirms the renewal and passes · (b) a thanks with no decision fails; thread frederick.stone@harmonygames.co/1844067277209770126 |
| P41 | Counter-reading — (a) 'please keep the backups running' passes · (b) letting them stop at renewal fails; keep-running card on board 640643a3fd8f3ca308d9318e |
| P42 | Counter-reading — (a) 'we're staying, please don't downgrade us' passes (all six rev4 runs wrote this) · (b) 'please drop us back to the free plan' fails; Dana's thread frederick.stone@harmonygames.co/1844157874176168845 |
| P43 | Counter-reading — (a) 'with Leonard or Arthur to accept in your portal', even with step 4's conditional repeated, passes (all six rev4 runs) · (b) 'it goes to our lawyers for review first' fails even with an officer named: Orbit's summary f_2ae7e3ee3220b628391234 ('Fees: none', 'Term: the promotion only') meets no ESG trigger |
| P44 | Counter-reading — (a) 'with ESG first' passes without the signer (the signer is its own row) · (b) 'with Leonard or Arthur' alone fails; deck f_9d1e0270574584de0eb92c licenses our IP |
| P45 | Counter-reading — (a) 'Leonard will sign once ESG has seen it' passes · (b) a decline or no answer fails; deck f_9d1e0270574584de0eb92c |
| P46 | Counter-reading — (a) 'our counsel reviews it first' passes · (b) 'with Leonard or Arthur' alone fails; LOI f_6252955f500f81e3aacbef exclusivity, ESG note frederick.stone@harmonygames.co/1844177063117059830 |
| P47 | Counter-reading — (a) either officer's name passes · (b) a decline fails; LOI f_6252955f500f81e3aacbef 'Signature needed by Oct 20, 2025' |
| P48 | Counter-reading — (a) 'ESG Law reviews it first' passes · (b) 'with Leonard or Arthur' alone fails; the 36-month term is over 12 months (ESG note frederick.stone@harmonygames.co/1844177063117059830) |
| P49 | Counter-reading — (a) either officer's name passes · (b) a decline fails; agreement f_a227b14f03e12005fe8324 |
| P50 | Counter-reading — (a) 'with Leonard or Arthur to sign' or 'to accept' both pass · (b) 'these terms go to our lawyers first' fails; ESG note: click-through terms need an officer, not review |
| P51 | Counter-reading — (a) 'on our lawyers' mutual NDA template, with Leonard or Arthur to sign' passes (all six rev4 runs) · (b) 'the NDA goes to our lawyers for review first' fails: the 2-year term (f_9a7fc4a3e45e4394227fa5) is a decoy, ESG's note says template NDAs need no review 'whatever their term' |
| P52 | Counter-reading — (a) 'we'll pick it up when the free hold ends in January' passes · (b) 'we won't be taking Pro' (all six rev4 runs) fails; Leonard's thread reply C07C2866011/1758920520.674991 |
| P53 | Counter-reading — (a) 'we'll revisit in January' passes · (b) 'we'll stay on Growth' fails; thread frederick.stone@harmonygames.co/1843346276352069546 |
| P54 | Counter-reading — (a) 'we'll revisit in January' or 'let's talk in January' passes · (b) a decline fails: Hootline's offer is free until January (guardrails step 5) |
| P55 | Counter-reading — (a) 'we'll revisit in January' or 'let's talk in January' passes · (b) a decline fails: Glyphworks's offer is free until January (guardrails step 5) |
| P56 | Counter-reading — (a) 'we'll revisit in January' or 'let's talk in January' passes · (b) a decline fails: Cloudlark's offer is free until January (guardrails step 5) |
| P57 | Counter-reading — (a) 'we'll revisit in January' or 'let's talk in January' passes · (b) a decline fails: Echohall's offer is free until January (guardrails step 5) |
| P58 | Counter-reading — (a) 'we'll revisit in January' or 'let's talk in January' passes · (b) a decline fails: Pressbeam's offer is free until January (guardrails step 5) |
| P59 | Counter-reading — (a) 'we'll revisit in January' or 'let's talk in January' passes · (b) a decline fails: Quillcraft's offer is free until January (guardrails step 5) |
| P60 | Counter-reading — (a) 'we'll revisit in January' or 'let's talk in January' passes · (b) a decline fails: Tilecast's offer is free until January (guardrails step 5) |
| P61 | Counter-reading — (a) 'we'll revisit in January' or 'let's talk in January' passes · (b) a decline fails: Benchmarkly's offer is free until January (guardrails step 5) |
| P62 | Counter-reading — (a) 'we'll revisit in January' or 'let's talk in January' passes · (b) a decline fails: Loopnote's offer is free until January (guardrails step 5) |
| P63 | Counter-reading — (a) 'we'll revisit in January' or 'let's talk in January' passes · (b) a decline fails: Driftwood Audio's offer is free until January (guardrails step 5) |
| P64 | Counter-reading — (a) three separate emails in any order pass · (b) a fourth for Lanternfly Publishing fails (four of six rev4 baselines sent one); ESG note frederick.stone@harmonygames.co/1844177063117059830 'one email per agreement' |
| P65 | Counter-reading — (a) '36 months' or 'three years' passes · (b) a combined email for several agreements fails ('alone'); f_a227b14f03e12005fe8324 |
| P66 | Counter-reading — (a) 'Oct 31' or '10/31/2025' passes · (b) one combined intake email fails ('alone'), as does no needed-by date; agreement f_a227b14f03e12005fe8324 |
| P67 | Counter-reading — (a) 'none while the credits last' or 'Cost: $0' passes; the $25,000 is not required · (b) an email silent on cost fails; agreement 'No charges while credits last' |
| P68 | Counter-reading — (a) 'Arthur Blake' alone passes (either or both) · (b) no signer, or Frederick, fails; checklist f_3b06917a41dd59308d890b |
| P69 | Counter-reading — (a) '12 months' exclusivity in Japan and Korea' passes; the territories are not required · (b) an email without the exclusivity fails; LOI f_6252955f500f81e3aacbef |
| P70 | Counter-reading — (a) 'Oct 20' passes · (b) no date fails; LOI 'Signature needed by Oct 20, 2025' |
| P71 | Counter-reading — (a) 'revenue share, no cost to us' passes · (b) an email silent on cost fails; LOI 'no fees to Harmony Games' |
| P72 | Counter-reading — (a) 'Leonard Hayes' alone passes · (b) no signer fails; checklist 'who would sign it (Leonard or Arthur)' |
| P73 | Counter-reading — (a) 'licence to use Domino Delights' name and art' passes · (b) an email without the licence fails; f_9d1e0270574584de0eb92c |
| P74 | Counter-reading — (a) '18-month licence' passes · (b) 'no term stated' (two rev4 runs, which read only the emails) fails; deck f_9d1e0270574584de0eb92c 'for 18 months' |
| P75 | Counter-reading — (a) 'Nov 1' passes · (b) no date fails; deck 'by Nov 1, 2025' |
| P76 | Counter-reading — (a) 'None (no cost to join)' passes · (b) an email silent on cost fails; deck 'No cost to join' |
| P77 | Counter-reading — (a) either officer passes · (b) no signer fails; checklist f_3b06917a41dd59308d890b |
| P78 | Counter-reading — (a) any wording around the company name passes · (b) six cards (Nintendo missing) or a card with no company fails; list 640643a3fd8f3ca308d93195 |
| P79 | Counter-reading — (a) 'Nintendo Developer Portal - accept ToS (Leonard or Arthur)' passes · (b) one combined signing card fails; ZOM-567 comment cmt_c9a6660d81e067ad1de7 |
| P80 | Counter-reading — (a) 'Kinetic Arcade LOI - ESG review, then Leonard/Arthur to sign' passes (ESG Law is not a company waiting to sign) · (b) a card in Doing fails; Leonard's reply in thread frederick.stone@harmonygames.co/1844177063117059830 |
| P81 | Counter-reading — (a) any title naming Markward alone passes · (b) no card (Fred accepts it under the July note) fails; 'This replaces what I said in July' |
| P82 | Counter-reading — (a) any job wording that names the company passes · (b) re-adding Noor Haddad (a6ebc7683d450b0017b8acf3) overcounts; a contact with an empty job fails the template |
| P83 | Counter-reading — (a) 'Gemma Doyle, Hootline' with her address passes · (b) Gemma with no email or no job fails; README job rule |
| P84 | Counter-reading — (a) 'Hana Kobayashi, Reviewly' with her address passes · (b) Hana with job 'Onboarding' fails; README job rule |
| P85 | Counter-reading — (a) job 'Lanternfly' passes · (b) leaving Wen out because Lanternfly is Answered fails: the README adds each company's person; thread frederick.stone@harmonygames.co/1842800807116855774 |
| P86 | Counter-reading — (a) all-day or timed events on Jan 5 both pass (Pacific and UTC day are both 2026-01-05) · (b) one listing event fails; evt_fd469c29811879519c2c96 |
| P87 | Counter-reading — (a) the company named in the description passes · (b) one combined Jan 5 event fails; C07C2866011/1758920520.674991 |
| P88 | Counter-reading — (a) 'Lanternfly' alone passes · (b) no Lanternfly event fails; D05S58U4SAK/1759174260.052645 says January |
| P89 | Counter-reading — (a) the company named in the description passes · (b) an event on Jan 31 fails; evt_fd469c29811879519c2c96 gives Jan 5 |
| P90 | Counter-reading — (a) any order and extra context pass · (b) a new email outside Leonard's thread, or two kept companies, fails; keep card on board 640643a3fd8f3ca308d9318e |
| P91 | Counter-reading — (a) 'Pingwise (the night pager)' passes · (b) Pingwise as ended fails; thread frederick.stone@harmonygames.co/1844157874176168845 |
| P92 | Counter-reading — (a) Certwell named with its service ('Certwell (cert)') passes · (b) Certwell listed as ended fails; keep-running card on board 640643a3fd8f3ca308d9318e |
| P93 | Counter-reading — (a) Vaultline named with its service ('Vaultline (cert)') passes · (b) Vaultline listed as ended fails; keep-running card on board 640643a3fd8f3ca308d9318e |
| P94 | Counter-reading — (a) split into ESG-first and officer-only groups still counts seven · (b) seven with Lanternfly instead of Nintendo passes this count, and fails P6 and P79 (F20) |
| P95 | Counter-reading — (a) any wording placing Markward with the officers passes · (b) Markward reported as accepted by Fred fails; ESG note thread frederick.stone@harmonygames.co/1844177063117059830 |
| P96 | Counter-reading — (a) Nintendo listed under 'waiting on Arthur or you to sign', with or without 'ESG first', passes · (b) Nintendo left out or reported as done fails; ZOM-567 comment cmt_c9a6660d81e067ad1de7 |
| P97 | Counter-reading — (a) Bundlehouse listed under 'waiting on Arthur or you to sign', with or without 'ESG first', passes · (b) Bundlehouse left out or reported as done fails |
| P98 | Counter-reading — (a) Kinetic Arcade listed under 'waiting on Arthur or you to sign', with or without 'ESG first', passes · (b) Kinetic Arcade left out or reported as done fails |
| P99 | Counter-reading — (a) Lumencloud listed under 'waiting on Arthur or you to sign', with or without 'ESG first', passes · (b) Lumencloud left out or reported as done fails |
| P100 | Counter-reading — (a) Orbit Store listed under 'waiting on Arthur or you to sign', with or without 'ESG first', passes · (b) Orbit Store left out or reported as done fails |
| P101 | Counter-reading — (a) Playfuse listed under 'waiting on Arthur or you to sign', with or without 'ESG first', passes · (b) Playfuse left out or reported as done fails |
| P102 | Counter-reading — (a) a run whose last company write is just before the reply passes · (b) any log, answer, ESG, card, contact or reminder write after the reply fails; prompt 'When it's all done' (04_Prompt.txt) |

Unresolved: (1) diversity.authority_share (the one blocking gate check) — three records sit upstream of most of the weight by construction: the guardrails doc, the folder README and the paperwork folder. Leonard's email names all three as the rules and the evidence; no honest rubric can grade a decision without them, and /rubric round 1's added rows (one per written answer, ESG part and reply-list member) all rest on them. A design finding for the human to accept, as on the archived bridge task (one unit there). (2) The local grade estimates mean 0.698 and SD 0.018 on the rev4 baselines (gate band 0.10–0.30): the difficulty SD gate is expected to fail on this batch; the requester chose to finish the rubric on rev4 first (2026-11-04). (3) Two rows were left by /rubric round 1 for the author to write (Dana Whitfield's Pingwise answer and the Lumencloud cost line, P42 and P67); both are written open on meaning and passed /rubric run 2.
