#!/usr/bin/env python3
"""Write selfreview.md (the plan's Self-review) from rows.json, the local baseline grade and the re-read sources."""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
TI = WF.parent
rows = json.loads((HERE / "rows.json").read_text())
TAG = {r["tag"]: f"P{i + 1}" for i, r in enumerate(rows)}
ev = json.loads((WF / "00_V3_Authoring_Evidence.json").read_text())

grade = subprocess.run([sys.executable, "-B", str(HERE / "grade_baselines.py")], capture_output=True, text=True).stdout.strip()
import re  # noqa: E402
_m = re.search(r"mean (\S+) · SD (\S+)", grade)
SDLINE = {"mean": _m.group(1), "sd": _m.group(2)} if _m else {}

CR = {  # (a) valid answer that could fail · (b) wrong answer that could pass — resolution with evidence
    "log_folder": "(a) a run that copies the template into the folder (gdrive_copy_file, all six rev4 baselines) has no create call; the "
                  "title accepts 'copied there' · (b) a sheet in My Drive fails on d_80a8c04753ba82ba4ba6a5",
    "log_header": "(a) a header in another letter case is accepted; columns appended after Next date stay legal · (b) a dropped 'Answered by' "
                  "fails against README f_846ddc38b2aab3d2ed3fcb",
    "log_rows": "(a) duplicate rows for one company count once (title: one row per company) · (b) 37 rows with Appodeal or NCsoft fail; "
                "the sweep OE 14 lists every look-alike with its reason (F65–F73)",
    "nin_decision": "(a) 'Nintendo Developer Portal' as the company name is accepted · (b) End or Answered from the 'Registration Completed' "
                    "notice fails against ZOM-567 comment cmt_c9a6660d81e067ad1de7",
    "fw_decision": "(a) none: Park is the only fair Decision once C07C2866011/1758920520.674991 is read (brief §4b D1) · (b) End from the "
                   "order form f_fba21c2d5d4bbb02983961 fails",
    "lf_decision": "(a) none: guardrails step 1 is first-fit (f_b98287f6f80fe431a71209) · (b) Sign from the 2-year exclusive deck fails; "
                   "Park fails (Leonard already answered, D05S58U4SAK/1759174260.052645)",
    "sp_decision": "(a) none: step 1 stops the order · (b) End from Rina's $750 ask fails; C07C2866011/1758134460.899858 is the answer",
    "lf_by": "(a) 'Leonard (Sep 27)' or 'Leonard Hayes, Sat Sep 27' accepted · (b) Frederick fails: his Sep 10 reply is a holding reply "
             "(thread frederick.stone@harmonygames.co/1842800807116855774)",
    "sp_by": "(a) 'Robert, Sep 17' accepted · (b) blank fails; Robert's post C07C2866011/1758134460.899858 names the answer",
    "bal_by": "(a) 'Leonard, Sep 11' (PT) or Sep 12 (UTC) both accepted — the date is not graded · (b) a missing Balancy row fails; the "
              "base thread frederick.stone@harmonygames.co/1840501641217286806 holds the answer",
    "mf_by": "(a) 'Arthur Blake' accepted · (b) blank fails; Arthur's Sep 19 reply is in thread frederick.stone@harmonygames.co/1843346276352084348",
    "nin_next": "(a) 'Oct 15, 2025' or '10/15/2025' accepted · (b) blank or Sep 4 (the notice date) fails; ZOM-567 comment gives Oct 15",
    "cf_next": "(a) any date form accepted · (b) Jan 15, 2026 from f_8d0e0e3ae076b2f745e7e2 fails; the notice frederick.stone@harmonygames.co/1843067564852153540 overrides it",
    "ph_next": "(a) any date form accepted · (b) Oct 20 or Oct 24 from f_614f88a28a2f0cf1b88408 fails (README: last day to say no)",
    "pw_next": "(a) any date form accepted · (b) Oct 31 (the downgrade cut-off, thread frederick.stone@harmonygames.co/1844157874176168845) fails; README Keep rule: when it next bills",
    "ph_told": "(a) 'released the booth hold' carries the decline and passes · (b) 'parked' fails; booth quote f_614f88a28a2f0cf1b88408 bills before January",
    "lf_told": "(a) wording with 'after the raise' with or without January passes · (b) 'with our lawyers first' fails; D05S58U4SAK/1759174260.052645",
    "sv_told": "(a) 'declined the licence' passes · (b) 'parked' fails; f_2686da1086bfcc2fba3f57 is paid on signature",
    "kin_told": "(a) 'ESG review first, then Leonard or Arthur' passes · (b) 'with Leonard or Arthur' alone fails; ESG note frederick.stone@harmonygames.co/1844177063117059830 lists exclusivity",
    "ww_told": "(a) 'declined, travel counts as cash' passes · (b) 'parked' (the doc's original travel rule) fails; C07C2866011/1759166100.370044",
    "ans_count": "(a) a reply plus a new mail to one company counts once; Clipforge's two mails count once · (b) 33 (Rina and Wen written to "
                 "again) fails; guardrails f_b98287f6f80fe431a71209 step 1",
    "cf_cancel": "(a) a new email or a forward to billing@paylane.io both pass · (b) a reply to the unmonitored notice fails "
                 "(frederick.stone@harmonygames.co/1843067564852153540)",
    "cf_priya": "(a) a reply on her thread or a new email to PERSON_9704_EMAIL passes · (b) only the billing cancellation fails; her Sep 22 ask "
                "(thread frederick.stone@harmonygames.co/1837102635418059486)",
    "ans_orbit": "(a) 'Leonard or Arthur will accept it in the portal' passes · (b) writing nothing because it is a portal fails; Mateo's "
                 "Sep 30 nudge (thread frederick.stone@harmonygames.co/1843708664218314020)",
    "esg_count": "(a) three separate emails in any order pass · (b) a fourth for Lanternfly Publishing fails (four of six rev4 baselines sent "
                 "one); ESG note frederick.stone@harmonygames.co/1844177063117059830 'one email per agreement'",
    "esg_lumen": "(a) '36 months' or 'three years' both state the term · (b) an email without the term fails; f_a227b14f03e12005fe8324",
    "esg_bundle": "(a) 'licence of Domino Delights' name and art' passes · (b) an email without the licence fails; f_9d1e0270574584de0eb92c",
    "card_count": "(a) any titles pass this count · (b) six cards (Nintendo missing) fail; list 640643a3fd8f3ca308d93195",
    "card_nin": "(a) 'Nintendo Developer Portal - accept ToS' passes · (b) no Nintendo card fails; ZOM-567 comment cmt_c9a6660d81e067ad1de7",
    "card_kin": "(a) any title naming Kinetic Arcade passes · (b) a card in Doing fails; Leonard's reply in thread frederick.stone@harmonygames.co/1844177063117059830 names To Do",
    "card_mark": "(a) any title naming Markward passes · (b) no card (Fred accepts it himself under the July note) fails; 'This replaces what I said in July'",
    "ct_count": "(a) contacts without an email still count · (b) re-adding Noor Haddad (a6ebc7683d450b0017b8acf3) overcounts",
    "ct_hoot": "(a) the email field is optional · (b) Gemma with no job fails; README f_846ddc38b2aab3d2ed3fcb job rule",
    "ct_rev": "(a) the email field is optional · (b) Hana with job 'Onboarding' fails; README job rule",
    "rem_count": "(a) all-day or timed events on Jan 5 both pass (Pacific and UTC day are both 2026-01-05) · (b) one listing event fails; "
                 "evt_fd469c29811879519c2c96",
    "rem_fw": "(a) the company named in the description passes · (b) no Framewell event fails; C07C2866011/1758920520.674991",
    "rem_lf": "(a) 'Lanternfly' alone passes · (b) no Lanternfly event fails; D05S58U4SAK/1759174260.052645 says January",
    "rem_hoot": "(a) the company named in the description passes · (b) an event on Jan 31 fails; evt_fd469c29811879519c2c96 gives Jan 5",
    "reply_thread": "(a) reply-all passes · (b) a new email outside the thread fails; frederick.stone@harmonygames.co/1844732913254784171",
    "reply_keep_count": "(a) any order and extra context pass · (b) two kept companies fail; keep card on board 640643a3fd8f3ca308d9318e",
    "reply_pingwise": "(a) 'Pingwise (the night pager)' passes · (b) Pingwise as ended fails; thread frederick.stone@harmonygames.co/1844157874176168845",
    "reply_sign_count": "(a) split into ESG-first and officer-only groups still counts seven · (b) seven with Lanternfly instead of Nintendo "
                        "passes this count, and fails P4 and P29 (F20)",
    "reply_markward": "(a) any wording placing Markward with the officers passes · (b) Markward reported as accepted by Fred fails; ESG note thread frederick.stone@harmonygames.co/1844177063117059830",
}
CR["reply_sign_count"] = ("(a) split into ESG-first and officer-only groups still counts seven · (b) seven with Lanternfly instead of "
                          f"Nintendo passes this count, and fails {TAG['nin_decision']} and {TAG['card_nin']} (F20)")
CR.update({
    "log_type": "(a) a template copied as a Google Sheet passes · (b) an uploaded xlsx fails against README f_846ddc38b2aab3d2ed3fcb ('One sheet')",
    "log_name": "(a) any letter case or spacing passes · (b) 'Vendor backlog' fails; README f_846ddc38b2aab3d2ed3fcb fixes the name (brief §4b's wider "
                "name class is superseded by the incorporated README line)",
    "ans_certwell": "(a) 'confirm the renewal' or 'keep it running' passes · (b) a thanks with no decision fails; thread frederick.stone@harmonygames.co/1844067277209770126",
    "ans_retainly": "(a) 'we'll decide in January' passes · (b) 'we'll stay on Growth' fails; thread frederick.stone@harmonygames.co/1843346276352069546",
    "ans_bundle": "(a) 'with ESG first, then Leonard or Arthur' passes · (b) 'with Leonard or Arthur' alone fails; deck f_9d1e0270574584de0eb92c licenses our IP",
    "rev_cancel": "(a) a reply or new email to Hana cancelling passes · (b) parking Reviewly (two rev4 baselines) fails; terms f_4bdfb8e0c47288087c7bba",
    "esg_kinetic": "(a) '12 months' exclusivity' or 'one year' passes · (b) one email covering all three agreements fails; LOI f_6252955f500f81e3aacbef",
    "esg_lumen_date": "(a) 'Oct 31' or '10/31/2025' passes · (b) no needed-by date fails; agreement f_a227b14f03e12005fe8324",
})
# /rubric round 1 (2026-11-05): changed rows and the rows its Fix List added
CR.update({
    "log_folder": "(a) a copy of the template made inside the folder counts as created there; a sheet moved in passes · (b) a sheet left "
                  "in My Drive fails on d_80a8c04753ba82ba4ba6a5",
    "pw_decision": "(a) none: Keep is the only fair Decision once the keep-running card's 'night pager' is matched to Pingwise's paging · "
                   "(b) End from the $29/month fails; thread frederick.stone@harmonygames.co/1844157874176168845",
    "rev_contact": "(a) 'Hana' alone or her address PERSON_9708_EMAIL passes · (b) a blank cell fails; Reviewly thread "
                   "frederick.stone@harmonygames.co/1843712439092112354",
    "sv_waiting": "(a) 'license' (US spelling) or 'trailer music pack licence' passes ('in any wording') · (b) a blank cell fails; paper "
                  "f_2686da1086bfcc2fba3f57",
    "mf_when": "(a) the date in Answered by ('Arthur Blake, Sep 19, 2025') or in What we told them passes (any column) · (b) no date fails; "
               "Arthur's 2025-09-19T17:45Z reply is Sep 19 in both Pacific and UTC",
    "lf_next": "(a) 'Jan 5, 2026' or '2026-01-05' passes · (b) blank (Answered with no date) fails: the README gives 'later' answers the "
               "January review; D05S58U4SAK/1759174260.052645 says January",
    "cf_priya": "(a) 'we won't be carrying on after the pilot' passes · (b) an email that only says the pilot ends (a fact) fails; Priya's "
                "Sep 22 ask in thread frederick.stone@harmonygames.co/1837102635418059486",
    "ans_certwell": "(a) 'please go ahead and reissue it' confirms the renewal and passes · (b) a thanks with no decision fails; thread "
                    "frederick.stone@harmonygames.co/1844067277209770126",
    "ans_retainly": "(a) 'we'll revisit in January' passes · (b) 'we'll stay on Growth' fails; thread frederick.stone@harmonygames.co/1843346276352069546",
    "ans_bundle": "(a) 'with ESG first' passes without the signer (the signer is its own row) · (b) 'with Leonard or Arthur' alone fails; "
                  "deck f_9d1e0270574584de0eb92c licenses our IP",
    "ans_bundle_sign": "(a) 'Leonard will sign once ESG has seen it' passes · (b) a decline or no answer fails; deck f_9d1e0270574584de0eb92c",
    "ans_kin_lawyers": "(a) 'our counsel reviews it first' passes · (b) 'with Leonard or Arthur' alone fails; LOI f_6252955f500f81e3aacbef "
                       "exclusivity, ESG note frederick.stone@harmonygames.co/1844177063117059830",
    "ans_kin_sign": "(a) either officer's name passes · (b) a decline fails; LOI f_6252955f500f81e3aacbef 'Signature needed by Oct 20, 2025'",
    "ans_lumen_lawyers": "(a) 'ESG Law reviews it first' passes · (b) 'with Leonard or Arthur' alone fails; the 36-month term is over 12 "
                         "months (ESG note frederick.stone@harmonygames.co/1844177063117059830)",
    "ans_lumen_sign": "(a) either officer's name passes · (b) a decline fails; agreement f_a227b14f03e12005fe8324",
    "ans_markward": "(a) 'Leonard or Arthur will accept the terms in the dashboard' passes · (b) 'I've accepted them' (the July note) "
                    "fails; ESG note 'That includes click-through terms'",
    "ans_playfuse": "(a) 'Leonard will sign your mutual NDA before Oct 8' passes · (b) sending it to ESG only, with no signer, fails; ESG "
                    "note 'Mutual NDAs on our template don't need review'",
    "ans_vaultline": "(a) 'please keep the backups running' passes · (b) letting them stop at renewal fails; keep-running card on board "
                     "640643a3fd8f3ca308d9318e",
    "ans_pingwise": "(a) 'we're staying, please don't downgrade us' passes (all six rev4 runs wrote this) · (b) 'please drop us back to "
                    "the free plan' fails; Dana's thread frederick.stone@harmonygames.co/1844157874176168845",
    "ans_wishwave": "(a) 'we won't be doing the expo push' passes · (b) parking it under the doc's original travel rule fails; "
                    "C07C2866011/1759166100.370044",
    "ans_framewell": "(a) 'we'll pick it up when the free hold ends in January' passes · (b) 'we won't be taking Pro' (all six rev4 runs) "
                     "fails; Leonard's thread reply C07C2866011/1758920520.674991",
    "esg_count": "(a) three separate emails in any order pass · (b) a fourth for Lanternfly Publishing fails (four of six rev4 baselines "
                 "sent one); ESG note frederick.stone@harmonygames.co/1844177063117059830 'one email per agreement'",
    "esg_lumen": "(a) '36 months' or 'three years' passes · (b) a combined email for several agreements fails ('alone'); "
                 "f_a227b14f03e12005fe8324",
    "esg_bundle": "(a) 'licence to use Domino Delights' name and art' passes · (b) an email without the licence fails; f_9d1e0270574584de0eb92c",
    "esg_kinetic": "(a) '12 months' exclusivity in Japan and Korea' passes; the territories are not required · (b) an email without the "
                   "exclusivity fails; LOI f_6252955f500f81e3aacbef",
    "esg_lumen_date": "(a) 'Oct 31' or '10/31/2025' passes · (b) no needed-by date fails; agreement f_a227b14f03e12005fe8324",
    "esg_lumen_cost": "(a) 'none while the credits last' or 'Cost: $0' passes; the $25,000 is not required · (b) an email silent on cost "
                      "fails; agreement 'No charges while credits last'",
    "esg_lumen_signer": "(a) 'Arthur Blake' alone passes (either or both) · (b) no signer, or Frederick, fails; checklist f_3b06917a41dd59308d890b",
    "esg_kin_date": "(a) 'Oct 20' passes · (b) no date fails; LOI 'Signature needed by Oct 20, 2025'",
    "esg_kin_cost": "(a) 'revenue share, no cost to us' passes · (b) an email silent on cost fails; LOI 'no fees to Harmony Games'",
    "esg_kin_signer": "(a) 'Leonard Hayes' alone passes · (b) no signer fails; checklist 'who would sign it (Leonard or Arthur)'",
    "esg_bh_term": "(a) '18-month licence' passes · (b) 'no term stated' (two rev4 runs, which read only the emails) fails; deck "
                   "f_9d1e0270574584de0eb92c 'for 18 months'",
    "esg_bh_date": "(a) 'Nov 1' passes · (b) no date fails; deck 'by Nov 1, 2025'",
    "esg_bh_cost": "(a) 'None (no cost to join)' passes · (b) an email silent on cost fails; deck 'No cost to join'",
    "esg_bh_signer": "(a) either officer passes · (b) no signer fails; checklist f_3b06917a41dd59308d890b",
    "card_count": "(a) any wording around the company name passes · (b) six cards (Nintendo missing) or a card with no company fails; "
                  "list 640643a3fd8f3ca308d93195",
    "card_nin": "(a) 'Nintendo Developer Portal - accept ToS (Leonard or Arthur)' passes · (b) one combined signing card fails; ZOM-567 "
                "comment cmt_c9a6660d81e067ad1de7",
    "card_kin": "(a) 'Kinetic Arcade LOI - ESG review, then Leonard/Arthur to sign' passes (ESG Law is not a company waiting to sign) · "
                "(b) a card in Doing fails; Leonard's reply in thread frederick.stone@harmonygames.co/1844177063117059830",
    "card_mark": "(a) any title naming Markward alone passes · (b) no card (Fred accepts it under the July note) fails; 'This replaces "
                 "what I said in July'",
    "ct_count": "(a) any job wording that names the company passes · (b) re-adding Noor Haddad (a6ebc7683d450b0017b8acf3) overcounts; a "
                "contact with an empty job fails the template",
    "ct_hoot": "(a) 'Gemma Doyle, Hootline' with her address passes · (b) Gemma with no email or no job fails; README job rule",
    "ct_rev": "(a) 'Hana Kobayashi, Reviewly' with her address passes · (b) Hana with job 'Onboarding' fails; README job rule",
    "ct_wen": "(a) job 'Lanternfly' passes · (b) leaving Wen out because Lanternfly is Answered fails: the README adds each company's "
              "person; thread frederick.stone@harmonygames.co/1842800807116855774",
    "rem_fw": "(a) the company named in the description passes · (b) one combined Jan 5 event fails; C07C2866011/1758920520.674991",
    "rem_lf": "(a) 'Lanternfly' alone passes · (b) no Lanternfly event fails; D05S58U4SAK/1759174260.052645 says January",
    "rem_hoot": "(a) the company named in the description passes · (b) an event on Jan 31 fails; evt_fd469c29811879519c2c96 gives Jan 5",
    "reply_keep_count": "(a) any order and extra context pass · (b) a new email outside Leonard's thread, or two kept companies, fails; "
                        "keep card on board 640643a3fd8f3ca308d9318e",
    "reply_pingwise": "(a) 'Pingwise (the night pager)' passes · (b) Pingwise as ended fails; thread frederick.stone@harmonygames.co/1844157874176168845",
    "reply_markward": "(a) any wording placing Markward with the officers passes · (b) Markward reported as accepted by Fred fails; ESG "
                      "note thread frederick.stone@harmonygames.co/1844177063117059830",
    "order_reply": "(a) a run whose last company write is just before the reply passes · (b) any log, answer, ESG, card, contact or "
                   "reminder write after the reply fails; prompt 'When it's all done' (04_Prompt.txt)",
})
for co, w in [("Pixel Harbor Events", "pixel"), ("Brightlane Studio", "brightlane"), ("Soundvault", "soundvault"),
              ("Streamcast Talent", "streamcast"), ("Lingora", "lingora"), ("Panelpulse", "panelpulse"), ("Ascendo", "ascendo")]:
    CR[f"ans_{w}"] = (f"(a) 'we won't go ahead', 'we're passing' or 'please release the hold' carries the decline and passes · (b) parking "
                      f"{co} for January fails: its offer costs cash before January (guardrails step 2)")
for co, w in [("Retainly", "retainly"), ("Hootline", "hootline"), ("Glyphworks", "glyphworks"), ("Cloudlark", "cloudlark"),
              ("Echohall", "echohall"), ("Pressbeam", "pressbeam"), ("Quillcraft", "quillcraft"), ("Tilecast", "tilecast"),
              ("Benchmarkly", "benchmarkly"), ("Loopnote", "loopnote"), ("Driftwood Audio", "driftwood")]:
    CR.setdefault(f"ans_{w}", f"(a) 'we'll revisit in January' or 'let's talk in January' passes · (b) a decline fails: {co}'s offer is "
                              "free until January (guardrails step 5)")
for co in ("Certwell", "Vaultline"):
    CR[f"reply_{co.lower()}"] = (f"(a) {co} named with its service ('{co} (cert)') passes · (b) {co} listed as ended fails; keep-running "
                                 "card on board 640643a3fd8f3ca308d9318e")
for co in ("Nintendo", "Bundlehouse", "Kinetic Arcade", "Lumencloud", "Orbit Store", "Playfuse"):
    CR[f"reply_{co.split()[0].lower()}"] = (f"(a) {co} listed under 'waiting on Arthur or you to sign', with or without 'ESG first', "
                                            f"passes · (b) {co} left out or reported as done fails"
                                            + ("; ZOM-567 comment cmt_c9a6660d81e067ad1de7" if co == "Nintendo" else ""))
for t in ("reply_thread", "order_log", "order_answers", "order_esg", "order_cards", "order_contacts", "order_reminders"):
    CR.pop(t, None)
# /rubric round 2 (2026-11-05): the five checked fixes
CR.update({
    "rev_contact": "(a) 'Hana' alone, 'Hana Kobayashi' or PERSON_9708_EMAIL passes (title now names 'or Hana') · (b) a blank cell fails; "
                   "Reviewly thread frederick.stone@harmonygames.co/1843712439092112354",
    "ans_orbit": "(a) 'with Leonard or Arthur to accept in your portal', even with step 4's conditional repeated, passes (all six rev4 "
                 "runs) · (b) 'it goes to our lawyers for review first' fails even with an officer named: Orbit's summary f_2ae7e3ee3220b628391234 "
                 "('Fees: none', 'Term: the promotion only') meets no ESG trigger",
    "ans_markward": "(a) 'with Leonard or Arthur to sign' or 'to accept' both pass · (b) 'these terms go to our lawyers first' fails; ESG "
                    "note: click-through terms need an officer, not review",
    "ans_playfuse": "(a) 'on our lawyers' mutual NDA template, with Leonard or Arthur to sign' passes (all six rev4 runs) · (b) 'the NDA goes "
                    "to our lawyers for review first' fails: the 2-year term (f_9a7fc4a3e45e4394227fa5) is a decoy, ESG's note says "
                    "template NDAs need no review 'whatever their term'",
    "esg_lumen_date": "(a) 'Oct 31' or '10/31/2025' passes · (b) one combined intake email fails ('alone'), as does no needed-by date; "
                      "agreement f_a227b14f03e12005fe8324",
})
assert set(CR) == {r["tag"] for r in rows}, set(r["tag"] for r in rows) ^ set(CR)

L = ["## Self-review", ""]
A = L.append
A("Re-read as /rubric: walked Evals/3_Rubrics_Eval.md 1.4 and 3.1 against the plan in order. Every prompt requirement (ledger R1–R12), "
  "every write family (log, written answers, ESG intake, cards, contacts, reminders, reply), both told lists in the reply, every "
  "exclusion (the look-alikes, as exact counts on the required writes) and the ordering ask ('When it's all done') has a row on "
  "the correct artifact. No row grades the final response; the reply to Leonard is the deliverable the prompt names.")
A("")
A("Re-verified: every source value in 00_V3_Authoring_Evidence.json was read in this run by plan/rubric/build_rubric.py — seeded "
  "rows by parsing 01_Universe_Inject.sql (never executed), base records through hg.py get-many (Balancy thread "
  "frederick.stone@harmonygames.co/1840501641217286806, Nintendo notice frederick.stone@harmonygames.co/1842359398719557772, Trello "
  "board 640643a3fd8f3ca308d9318e). The values each title names (dates, recipients, counts, company names) were re-read from the "
  "same records; the counts were recomputed from solver/truth.json and the records (36 rows, 31 answers, 3 ESG, 7 cards, 32 "
  "contacts, 14 reminders, 3 kept, 7 to sign). The eval's rubric lint (hg.py rubric-lint) reports 0 findings.")
A("")
A("Predicted all-fail re-check: for every row the persona reaches the value through a cataloged tool (Gmail, Slack, Calendar and "
  "Drive records pasted YES under Visibility proof; Trello, Linear and Contacts unscoped), each write exists in the catalog "
  "(gsheets/gdrive, gmail_reply_to_message, gmail_send_message, trello_create_card, contacts_add_new_contact, gcal_create_event), "
  "no row needs a rate-1.0 retry, and no evidence sits outside Frederick's view. Count on the four bases: 0. The local grade below "
  "shows every row passed by at least one plausible run shape except the rows the six rev4 baselines all missed, and each of "
  "those is reachable (the misses are discovery failures, not impossible targets).")
A("")
A("Local baseline grade (plan/rubric/grade_baselines.py over run_forensics/rev4/baseline/run-*/writes.json; a local estimate of the "
  "verifier, not its result):")
A("")
A("```text")
A(grade)
A("```")
A("")
A("Shortcut and diversity: the §F probe hits are dispositioned below the paste. The largest unit of discovery is the guardrails "
  "doc (F2), upstream of every decision row by construction — see Unresolved.")
A("")
A("Surface dispositions: X9 (Clipforge Decision) and X14 (Framewell Next date) are the only dispositioned slots. Strongest case for "
  "a row: each is a log cell the README asks for, and the log's Decision and Next date columns are sampled. Resolution: the "
  f"facts are graded on their own deliverables ({TAG['cf_cancel']}/{TAG['cf_next']}/{TAG['cf_priya']}; {TAG['fw_decision']}/"
  f"{TAG['ans_framewell']}/{TAG['rem_fw']}), the Decision and Next date samples are already at five each (gate 15), and /rubric "
  "round 1 raised no coverage gap for either cell.")
A("")
A("Counter-readings, one per section A row:")
A("")
A("| P | Counter-reading (a valid answer that could fail · a wrong answer that could pass) and resolution (evidence) |")
A("|---|---|")
for i, r in enumerate(rows):
    A(f"| P{i + 1} | Counter-reading — {CR[r['tag']]} |")
A("")
DIV = json.loads((HERE / "diversity.json").read_text()) if (HERE / "diversity.json").exists() else {}
A(f"Unresolved: (1) diversity.authority_share (the one blocking gate check) — three records sit upstream of most of the weight by "
  f"construction: {DIV.get('units', 'the guardrails doc, the folder README and the paperwork folder')}. Leonard's email names all three "
  "as the rules and the evidence; no honest rubric can grade a decision without them, and /rubric round 1's added rows (one per "
  "written answer, ESG part and reply-list member) all rest on them. A design finding for the human to accept, as on the archived "
  "bridge task (one unit there). "
  f"(2) The local grade estimates mean {SDLINE.get('mean', '?')} and SD {SDLINE.get('sd', '?')} on the rev4 baselines (gate band "
  "0.10–0.30): the difficulty SD gate is expected to fail on this batch; the requester chose to finish the rubric on rev4 first "
  "(2026-11-04). (3) Two rows were left by /rubric round 1 for the author to write (Dana Whitfield's Pingwise answer and the "
  f"Lumencloud cost line, {TAG['ans_pingwise']} and {TAG['esg_lumen_cost']}); both are written open on meaning and passed /rubric run 2.")
(HERE / "selfreview.md").write_text("\n".join(L) + "\n")
print("selfreview written:", len(rows), "counter-readings")
