import re,sys
S=sys.argv[1]
P='/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/Working_Files/01_Grounding_Dossier.md'
t=open(P).read()
def repl_block(t,cmd_sub,newtext):
    i=t.index(cmd_sub); a=t.index('```',i); b=t.index('```',a+3)
    nl=t.index('\n',a)
    return t[:nl+1]+newtext.rstrip('\n')+'\n'+t[b:]
t=repl_block(t,'tools/sql_lint.py Task_Authoring/task_inputs/01_Universe_Inject.sql`',open(S+'/o_lint.txt').read())
t=repl_block(t,'tools/base_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql`',open(S+'/o_base.txt').read())
t=repl_block(t,'tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json Task_Authoring/task_inputs/01_Universe_Inject.sql`',open(S+'/o_hg.txt').read())
t=repl_block(t,'tools/fact_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql --manifest',open(S+'/o_fc.txt').read())
t=t.replace('--load-bearing <138 ids>`','--load-bearing <175 ids>`')
t=repl_block(t,'--load-bearing <175 ids>`',open(S+'/checksql.txt').read())
# entity rows
old=[l for l in t.split('\n') if l.startswith('| Meta ad account | Account ID [IDENTIFIER_3125]')][0]
new=("| Meta company ad account | 907669287942378 (the export's top-level subject shows the token [IDENTIFIER_3125]; the runtime Gmail tool returns the raw Subject header, 907669287942378 — pre-check run event 391) | gmail frederick.stone@harmonygames.co/1843428112007517388; seeded receipts now carry 907669287942378; seeded f_4591ef30be4f920ba1ed14 names it 'the company ad account Node runs for us' | receipts in Frederick's, Leonard's and Robert's mailboxes | AGREE (hardening D1) |\n"
     "| Leonard Hayes personal Meta ad account | 4417730962158804, bills Visa 7731 | seeded notice frederick.stone@harmonygames.co/1836556159549956945; receipts frederick.stone@harmonygames.co/1838001810309861113 … frederick.stone@harmonygames.co/1844370651218486865 | Leonard's own ZM_UK creative tests Jul – Sep 2025 | AGREE; the rules doc's 'My own Meta test account stays out' (T23) |")
t=t.replace(old,new)
t=t.replace('| f_0cd1e1402e8052d3d4e903 | gsheets | shared with the persona | LB |','| f_0cd1e1402e8052d3d4e903 | gsheets | owned by the persona (hardening D2: writer needed for W1) | LB |')
t=t.replace('| ● grid | shared with persona | write target |','| ● grid | owned by persona (D2) | write target |')
t=t.replace('viewer on the data room folder and Q4 pack | AGREE |','viewer on the data room folder; shared on the Q4 pack (owner Frederick) | AGREE |')
t=t.replace('| Meta ad account | 3125 | id | f_4591ef30be4f920ba1ed14 |','| Meta company ad account | 907669287942378 | id | frederick.stone@harmonygames.co/1844734171545827192 |\n| Leonard Hayes personal ad account | 4417730962158804 | id | frederick.stone@harmonygames.co/1836556159549956945 (home: the notice and its five receipts) |')
t=t.replace('Meta receipts (account ending 3125)','Meta receipts (company account 907669287942378)')
# 9.1 rows: insert after the page_ua_spend_buckets row
anchor=[l for l in t.split('\n') if l.startswith('| page_ua_spend_buckets | seeded |')][0]
rows=["| frederick.stone@harmonygames.co/1836556159549956945 | seeded | Meta notice, 2025-07-02T17:14:00Z (10:14 AM PT): Leonard Hayes added Frederick to the ad account 'Leonard Hayes' (ID 4417730962158804), personal ad account, billing view | own INBOX | decoy identity (T23) | no |",
 "| frederick.stone@harmonygames.co/1838001810309861113 | seeded | Meta receipt, account 4417730962158804, 2025-07-18T16:12:00Z: $187.40 (ZM_UK_Hooks_A 102.55, ZM_UK_Hooks_B 84.85), Visa 7731, ref J3MFHZGFY2 | own INBOX | decoy (T23): excluded | no |",
 "| frederick.stone@harmonygames.co/1840483663872198178 | seeded | Meta receipt, account 4417730962158804, 2025-08-15T01:40:00Z (Aug 14 6:40 PM PT): $243.15 (ZM_UK_Statics_D), Visa 7731, ref KS59EUKFY2 | own INBOX | decoy (T23): excluded | no |",
 "| frederick.stone@harmonygames.co/1843339041178378696 | seeded | Meta receipt, account 4417730962158804, 2025-09-15T14:05:00Z: $96.20 (ZM_UK_CopyAds_Alt, Sep 12 – 14), Visa 7731, ref J5MHXJCFY2 | own INBOX | decoy (T23): not Fundraising | no |",
 "| frederick.stone@harmonygames.co/1843719233863958066 | seeded | Meta receipt, account 4417730962158804, 2025-09-19T18:48:00Z: $158.65 (ZM_UK_Retention_iOS_Alt, Sep 15 – 18), Visa 7731, ref TNVV4LBFY2 | own INBOX | decoy (T23): not Fundraising | no |",
 "| frederick.stone@harmonygames.co/1844370651218486865 | seeded | Meta receipt, account 4417730962158804, 2025-09-26T23:22:00Z: $171.30 (ZM_UK_CPE_CopyAds_Alt, Sep 22 – 25), Visa 7731, ref LZDDFGXFY2 | own INBOX | decoy (T23): not Fundraising | no |",
 "| f_0cd1e1402e8052d3d4e903 | seeded | Q4 Board Pack - Oct 14, owner Frederick (D2), shared with Leonard, Arthur and PERSON_6098_EMAIL; Summary tab: Paid UA section owner Frederick, tab Marketing | owned | write target (W1) | no |",
 "| f_4591ef30be4f920ba1ed14 (Meta clause) | seeded | rules doc now reads 'Meta (the company ad account Node runs for us)' (D1; was 'ending 3125'); 'My own Meta test account stays out of this' unchanged | shared | authority (H2) | no |"]
t=t.replace(anchor,anchor+'\n'+'\n'.join(rows),1)
# follow-ups note
t=t.replace('## 12 Platform follow-ups\n','## 12 Platform follow-ups\n\n- Hardening revision 2026-10-22 (01a_Hardening_Report.md): D1 account id, D2 board-pack owner, T23 personal-account decoy. Ground truth unchanged: Real UA $111,387.92, Fundraising $3,485.20 (the T23 receipts are excluded).\n',1)
open(P,'w').write(t); print('ok')
