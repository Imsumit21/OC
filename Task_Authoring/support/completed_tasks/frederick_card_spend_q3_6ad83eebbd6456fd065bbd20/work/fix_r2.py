import json,sys
p=sys.argv[1]; d=json.load(open(p))
R=lambda n: d[n-1]
THR="in its reply on the 'Card spend breakdown for Q3 Standard Metrics' thread"
C481="in its comment on Trello card #481 'Q4 cost cuts - card subscriptions'"
def T(n,t,w=None,j=None,e=None):
    r=R(n); r['title']=t
    if w: r['weight']=w
    if j: r['justification']=j
    if e: r['evidence']=e
T(2,"The Agent shows the Jan–Sep 2025 card statement cycle amounts on the Ledger tie-out tab summing to 97,968.21, the total of the eight 2025 'Unreconciled operating expenses' ledger lines")
T(3,"The Agent ties the June and July 2025 cycles on the Ledger tie-out tab to the July ledger line of 24,354.37 dated 2025-07-31, either as June 12,222.02 plus July 12,132.35 or as one combined July figure of 24,354.37",
  j="Close notes rule 4: there is no June ledger line and July carries both cycles; the tie-out puts the June cycle under the July line, either split out or combined.",
  e="FIN-000580 (snowflake.json /tables/38/rows/579); close notes rules 3–4 in f_2a1e1bf25cf49d5d974bfc (SQL L19)")
T(4,"The Agent ties the August 2025 ledger line of 22,090.21 on the Ledger tie-out tab as the August category amounts plus a separate 1,000.00 Unity Ads reclass",
  j="Close notes rule 7: an ad-network charge is a reclass in the tie-out, not a category. The August cycle's categorized amounts are 21,090.21; a tie-out that also leaves Unity Ads in an August category cannot tie to 22,090.21 with a separate reclass.",
  e="Feed sheet f_f7299de2df377944f21e7b (UNITY ADS 1,000.00, Aug 20); FIN-000600 22,090.21 (snowflake.json tables/38)")
T(5,"The Agent shows the September 2025 cycle at 10,438.20 on the Ledger tie-out tab, tying to the ledger line dated 2025-09-30",w=5)
T(6,"The Agent shows the January 2025 statement cycle at 7,759.99 on the Ledger tie-out tab, tying to the ledger line dated 2025-01-31",w=5,
  j="Close notes rule 3: the January cycle runs Dec 26, 2024 to Jan 25, 2025; calendar January does not tie.")
T(7,"The Agent lists 41 vendors on the By vendor tab besides its Unity Technologies and Unity Ads rows",
  j="Close notes rule 12 merges each brand into one vendor; the count is right only after reading every sheet and applying every merge. Counting outside the two Unity names keeps the row independent of whether Unity Ads appears on By vendor and of how Unity is split (R11 grades the Unity seats).",
  e="Feed folder d_e342e9e32a98e7cc2d5d57; close notes rule 12 in f_2a1e1bf25cf49d5d974bfc (SQL L19)")
T(8,"The Agent shows AppMagic amounts on the By vendor tab for 2025-01 to 2025-09 that sum to 1,293.46, including its foreign transaction fee rows")
T(9,"The Agent shows Sensor Tower amounts on the By vendor tab for 2025-01 to 2025-09 that sum to 1,043.33, net of the -106.67 credit of Sep 8, 2025")
T(10,"The Agent shows the OPENAI *CHATGPT SUBSCR and OPENAI CHATGPT TEAM charges under a single vendor name, of any label, on the By vendor tab with 2025-01 to 2025-09 amounts that sum to 1,050.00",
  j="Close notes rule 12: one vendor per brand, so both OpenAI descriptors merge.",
  e="Feed sheets f_4406ba0c8bd5212ecaf145 (OPENAI *CHATGPT SUBSCR 90.00, Dec 26, 2024) and f_ecda6fb95d068733de87d1 (OPENAI CHATGPT TEAM 150.00, Mar 26, 2025); close notes rule 12 in f_2a1e1bf25cf49d5d974bfc (SQL L19)")
T(11,"The Agent shows Unity Technologies seat amounts on the By vendor tab for 2025-01 to 2025-09 that sum to 17,970.00",
  j="Close notes rule 12: Unity seats (UNITY TECHNOLOGIES) and Unity Ads are separate vendors, so the 1,000.00 Unity Ads charge is not part of this total.")
T(12,"The Agent shows Software & subscriptions at 1,107.91 for 2025-08 on the Category by month tab",
  j="Griffin's 2025 categories replace the 2024 list; Unity seats go under Hosting & infrastructure per Griffin's answer in Leonard's Sep 30 DM, so August Software holds none of the 10,200.00 Unity prepay.",
  e="Forwarded note frederick.stone@harmonygames.co/1844639871009298010; Slack DM D05S58U4SAK/1759248472.204417; feed sheet f_e5bd3c66de846ccd52eb65 (Aug 8)")
T(13,"The Agent shows Travel & events at 3,265.46 for 2025-06 on the Category by month tab")
T(14,"The Agent shows Hosting & infrastructure at 1,025.84 for 2025-09 on the Category by month tab")
T(15,"The Agent shows Professional & admin at 3,552.00 for 2025-03 on the Category by month tab")
T(16,"The Agent lists Q4 monthly run-rate amounts on the Q4 run-rate tab that total 2,869.80 (±0.01)")
T(17,"The Agent shows Edgegap at 420.00 per month on the Q4 run-rate tab",
  j="Rule 8 counts a downgrade once the vendor confirms it by email to the account owner. Edgegap's Sep 29 email to Arthur (cc Frederick) confirms the 420.00 plan from the Oct 10 invoice, though ENG-2370 and the Edgegap card show no change and the #481 item is still unticked.")
T(18,"The Agent shows Unity Pro at 850.00 per month on the Q4 run-rate tab",
  j="Close notes rule 9: annual plans at 1/12 of the last annual charge, here the 10,200.00 prepay of Aug 8, 2025.")
T(19,"The Agent shows Sensor Tower at 250.00 per month on the Q4 run-rate tab")
T(20,"The Agent shows Envato Elements at 27.04 per month (±0.01) on the Q4 run-rate tab",
  j="Close notes rule 9: annual plans at 1/12, fee rows count with the plan. (314.97 annual charge + 9.45 FX fee) / 12 = 27.035.")
T(21,"The Agent shows Cogency Global at 25.00 per month on the Q4 run-rate tab",
  j="Close notes rule 9 names COGENCY GLOBAL INC registered-agent renewals as annual plans: 1/12 of the 300.00 renewal.")
T(23,"The Agent addresses its reply in the 'Card spend breakdown for Q3 Standard Metrics' thread to exactly leonard.hayes@harmonygames.co, arthur.blake@harmonygames.co and robert@harmonygames.co (each as To or Cc)",
  e="Slack DM D05S58U4SAK/1759248331.512089; contacts.json /contacts/107")
T(24,f"The Agent gives Travel & events at 23,043.63 for Jan–Sep 2025 {THR}",w=5,
  j="Leonard asks the reply to carry 'the totals by category' under Griffin's 2025 categories.",
  e="Forwarded note frederick.stone@harmonygames.co/1844639871009298010; feed folder d_e342e9e32a98e7cc2d5d57")
T(25,f"The Agent gives Software & subscriptions at 8,361.12 for Jan–Sep 2025 {THR}")
T(26,f"The Agent gives Hosting & infrastructure at 27,305.36 for Jan–Sep 2025 {THR}")
T(27,f"The Agent gives Professional & admin at 7,473.00 for Jan–Sep 2025 {THR}")
T(28,f"The Agent gives a Q4 monthly run-rate of 2,869.80 (±0.01) {THR}, stated as a total or as per-vendor amounts that sum to it",
  j="Leonard asks the reply to carry 'the monthly run-rate'.")
T(29,f"The Agent names the 60.00 Midjourney charge posted Sep 2, 2025 as a disputed charge {THR}",
  j="Midjourney was cancelled Jul 3 (Trello card comment). Its Aug 2 charge was refunded on Aug 25, so the Sep 2 charge is Midjourney's one unrefunded charge after its confirmed cancellation (close notes rule 8).",
  e="Feed sheets f_1830257bf9ea6d5269d440, f_64e214d78ad44085744dad, f_8eeb88266f2fd9e9f26737")
T(30,"The Agent makes Trello changes on exactly one card",
  j="Leonard: 'put what you find in a comment on that one ... don't start a new card.' The one card is #481 'Q4 cost cuts - card subscriptions'; a new card, or a change on the near-match #480 'Cut list - art tools (Claire Morgan's invoices)', makes two cards. A run with no Trello change fails.",
  e="Trello card 68d2dafdbfcc777cc630fad0 (#481); decoy card #480 (SQL L3319)")
T(31,f"The Agent records that Sensor Tower is kept rather than cancelled {C481}")
T(32,f"The Agent records that AppMagic is cancelled {C481}")
T(33,f"The Agent records the 99.99 LinkedIn Sales Navigator charge of Sep 3, 2025 as a charge to dispute {C481}")
T(34,f"The Agent records the 60.00 Midjourney charge of Sep 2, 2025 as a charge to dispute {C481}")
T(36,"The Agent lists Unity Pro as still being charged in its ENG-2370 comment",
  e="Feed sheet f_e5bd3c66de846ccd52eb65; ENG-2370 Sep 3 comment; #481 comment 68d55da0fc9579f06920f651 (seat drop at the Aug 2026 renewal)")
T(37,"The Agent lists Edgegap as still being charged in its ENG-2370 comment")
T(38,"The Agent lists Google Cloud as still being charged in its ENG-2370 comment")
T(39,"The Agent lists 1Password as still being charged in its ENG-2370 comment",
  e="Trello card 678167bdc481ee214e69886d comment 68dac5f2a1b3c4d5e6f70812; feed sheet f_8eeb88266f2fd9e9f26737 (Sep 2)")
T(40,"The Agent shows 1Password at 23.97 per month on the Q4 run-rate tab",
  j="Rule 8 counts a comment on the vendor's card; Leonard's Sep 29 comment on the 1Password card sets 3 seats (3 × 7.99) from the Oct bill, later than Arthur's Sep 25 note of 4 seats on card #481.")
T(41,f"The Agent gives Marketing (non-UA) at 3,019.00 for Jan–Sep 2025 {THR}")
T(42,"The Agent shows Marketing (non-UA) at 2,398.00 for 2025-02 on the Category by month tab")
T(43,f"The Agent names the 99.99 LinkedIn Sales Navigator charge posted Sep 3, 2025 as a disputed charge {THR}")
T(44,"The Agent shows Webflow at 18.00 per month on the Q4 run-rate tab")
T(45,"The Agent values WeWork at 0.00 per month in its Q4 run-rate on the Q4 run-rate tab, as a 0.00 row or by leaving it out of the listed plans",
  j="Leonard forwarded WeWork's email to him as account owner: the membership ends Sep 30 and the Sep 1 charge was the last one. Rule 8 counts a vendor-confirmed change even before it is on the board, so the Sep charge of 299.00 is not the Q4 rate.")
T(46,"The Agent shows Murf at 11.00 per month on the Q4 run-rate tab")
T(47,f"The Agent names the 16.00 SavvyCal charge posted Sep 11, 2025 as a disputed charge {THR}")
T(48,f"The Agent names the 20.00 Buttondown charge posted Sep 21, 2025 as a disputed charge {THR}")
T(49,f"The Agent records the 16.00 SavvyCal charge of Sep 11, 2025 as a charge to dispute {C481}")
T(50,f"The Agent records the 20.00 Buttondown charge of Sep 21, 2025 as a charge to dispute {C481}")
T(51,f"The Agent lists exactly four disputed charges {THR}",w=3,
  j="Leonard asks the reply to carry 'the disputed charges'. Close notes rule 8: Midjourney 60.00 (Sep 2), LinkedIn 99.99 (Sep 3), SavvyCal 16.00 (Sep 11) and Buttondown 20.00 (Sep 21). The Aug 2 Midjourney charge (refunded Aug 25) and the Jul 9 Loom charge (refunded Jul 15) are decoys; WeWork has no charge after Sep 1.")
T(52,f"The Agent records the Edgegap downgrade to 420.00 per month as confirmed {C481}",w=5,
  j="The #481 item 'Edgegap - downgrade plan (Arthur, ENG-2370)' is still unticked, but Edgegap's Sep 29 email to Arthur (cc Frederick) confirms the 420.00 plan from the Oct 10 invoice; Leonard asks for what Frederick finds to go in a comment on #481.",
  e="Email frederick.stone@harmonygames.co/1844619081941308353 (Edgegap, Sep 29); #481 checklist item (SQL L3359)")
T(53,"The Agent lists exactly four of Arthur's subscriptions as still being charged in its ENG-2370 comment")
T(54,"The Agent shows Informa (GDC) at -399.00 for 2025-03 on the By vendor tab")
def A(t,w,j,e): d.append(dict(title=t,category="Outcome",weight=w,justification=j,evidence=e))
A("The Agent shows category cells on the Category by month tab whose 2025-01 to 2025-09 values for the eight categories sum to 96,968.21",5,
  "Volume control for the tab: the cells need every feed sheet, the cycle rules and the bank-rule exclusions; the 1,000.00 Unity Ads reclass sits outside opex (close notes rule 7).",
  "Feed folder d_e342e9e32a98e7cc2d5d57; close notes rules 7 and 11 in f_2a1e1bf25cf49d5d974bfc (SQL L19)")
A("The Agent shows the March 2025 cycle at 12,214.05 on the Ledger tie-out tab, tying to the ledger line dated 2025-03-31",5,
  "Close notes rule 5 nets a refund in the cycle it posts (the -399.00 GDC refund of Mar 4), unlike the 2024 Confluence rule that netted refunds against the month of the original charge.",
  "FIN-000474 (snowflake.json tables/38, 2025-03-31, 12,214.05); feed sheet card_0417_2025-03-04 adjustments tab (SQL L441)")
for cat,amt in [("Hardware & equipment","19,203.87"),("Other G&A","6,475.77"),("Research & user testing","2,086.46")]:
    A(f"The Agent gives {cat} at {amt} for Jan–Sep 2025 {THR}",3,
      "Leonard asks the reply to carry 'the totals by category' under Griffin's 2025 categories.",
      "Forwarded note frederick.stone@harmonygames.co/1844639871009298010; feed folder d_e342e9e32a98e7cc2d5d57")
A("The Agent sends exactly one email",1,
  "Prompt: 'the summary goes out as a reply on his email thread'. Leonard's same-day 'Fwd: Q2 metrics - opex categories' thread is a near-match; a second send (or a send on that thread as well) makes two emails. A run that sends nothing fails.",
  "Thread frederick.stone@harmonygames.co/1844640253739158706; decoy thread (SQL L3042)")
A("The Agent makes exactly one change to Trello card #481 'Q4 cost cuts - card subscriptions'",1,
  "Leonard: 'put what you find in a comment on that one (I'll keep the checklist myself)'. The one expected change is the findings comment; ticking a checklist item, renaming or moving the card, or a second comment makes more than one change. A run with no change on #481 fails. The checklist stays at Notion, ChatGPT and 1Password complete.",
  "Trello card 68d2dafdbfcc777cc630fad0 checklist (SQL L3341–L3361)")
A(f"The Agent records exactly four charges to dispute {C481}",3,
  "Close notes rule 8: Midjourney 60.00 (Sep 2), LinkedIn 99.99 (Sep 3), SavvyCal 16.00 (Sep 11) and Buttondown 20.00 (Sep 21). The refunded Midjourney Aug 2 and Loom Jul 9 charges are decoys.",
  "Feed sheets f_8eeb88266f2fd9e9f26737, f_9c2cecbd35b55e83151f42; adjustments tabs SQL L1245 and L1493")
json.dump(d,open(p,'w'),indent=2,ensure_ascii=False)
print(len(d), sum(r['weight'] for r in d))
import re
for i,r in enumerate(d,1):
    if r['title'].startswith("The Agent's"): print("POSSESSIVE",i)
