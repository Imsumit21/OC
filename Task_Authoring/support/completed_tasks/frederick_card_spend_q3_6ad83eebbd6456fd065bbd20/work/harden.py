import re,json,uuid,random
from datetime import datetime,timezone,timedelta
P='/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/01_Universe_Inject.sql'
L=open(P).read().split('\n')
random.seed(20251022)
FS='frederick.stone@harmonygames.co'
def q(s): return s.replace("'","''")
PT=timedelta(hours=-7)
COLS="INSERT INTO gmail.gmail_messages (id, thread_id, user_email, label_ids_json, snippet, internal_date, date, size_estimate, subject, from_email, from_name, to_json, cc_json, bcc_json, reply_to_json, body_text, body_html, headers_json, in_reply_to, \"references\", mbox_from, attachments_meta_json)"
TCOLS="INSERT INTO gmail.gmail_threads (id, user_email, snippet, history_id)"
NEW=[]; facts=[]
def msg(utc,subject,body,reply_to='["SVC_0177_NAME <SVC_0177_EMAIL>"]',labels='["INBOX", "CATEGORY_UPDATES"]',dom='support.facebook.com'):
    ms=int(utc.timestamp()*1000); tid=str((ms<<20)+random.randint(1000,900000))
    mid=f"<{uuid.UUID(int=random.getrandbits(128),version=4)}@{dom}>"
    pt=utc+PT
    snip=re.sub(r'\s+',' ',body.replace('\r\n',' '))[:140]
    hdr=[{"name":"X-GM-THRID","value":tid},{"name":"X-Gmail-Labels","value":"INBOX,CATEGORY_UPDATES"},{"name":"Delivered-To","value":FS},
         {"name":"Date","value":pt.strftime('%a, %d %b %Y %H:%M:%S -0700')},{"name":"To","value":f"frederick stone <{FS}>"},
         {"name":"Subject","value":subject},{"name":"From","value":"SVC_0521_NAME <SVC_0521_EMAIL>"},{"name":"Reply-To","value":"SVC_0177_NAME <SVC_0177_EMAIL>"},{"name":"Message-ID","value":mid}]
    NEW.append(TCOLS); NEW.append(f"VALUES ('{FS}/{tid}', '{FS}', '{q(snip[:90])}', NULL);")
    NEW.append(COLS)
    NEW.append(f"VALUES ('{FS}/{mid}', '{FS}/{tid}', '{FS}', '{labels}', '{q(snip)}', {ms}, '{utc.strftime('%Y-%m-%dT%H:%M:%SZ')}', {len(body)+900}, '{q(subject)}', 'SVC_0521_EMAIL', 'SVC_0521_NAME', '[\"frederick stone <{FS}>\"]', '[]', '[]', '{reply_to}', E'{q(body).replace(chr(13),'\\r').replace(chr(10),'\\n')}', NULL, '{q(json.dumps(hdr,ensure_ascii=False))}', '', '', NULL, '[]');")
    return f"{FS}/{tid}", f"{FS}/{mid}"
ACC='4417730962158804'
# 1) ad-account notification
body=("You can access the ad account for Leonard Hayes (ID: %s)Facebook for Business\r\n\r\nYou can access the ad account for Leonard Hayes (ID: %s)Facebook "
      "Leonard Hayes has added you to an ad account.  Ad Account Name: Leonard Hayes (ID: %s) Business: none (personal ad account) "
      "Your role: Finance analyst (view billing and receipts)\r\n\r\nSee ad account[https://www.facebook.com/ads/manager/account_settings/information/?act=%s]\r\n\r\n"
      "========================================\r\nThis message was sent to %s.\r\nmeta Platforms, Inc., Attention: Community Support, 1 Meta Way, Menlo Park, CA 94025")%(ACC,ACC,ACC,ACC,FS)
t,m=msg(datetime(2025,7,2,17,14,tzinfo=timezone.utc),f"You’ve been added to the ad account for Leonard Hayes (ID: {ACC})",body,dom='facebookmail.com')
facts.append(('notice',t,'2025-07-02 10:14 PT','Leonard Hayes personal ad account %s added Frederick (billing view)'%ACC))
R=[(datetime(2025,7,18,16,12),'Jul 14, 2025','Jul 17, 2025',[('ZM_UK_Hooks_A',102.55),('ZM_UK_Hooks_B',84.85)]),
   (datetime(2025,8,15,1,40),'Aug 8, 2025','Aug 14, 2025',[('ZM_UK_Statics_D',243.15)]),
   (datetime(2025,9,15,14,5),'Sep 12, 2025','Sep 14, 2025',[('ZM_UK_CopyAds_Alt',96.20)]),
   (datetime(2025,9,19,18,48),'Sep 15, 2025','Sep 18, 2025',[('ZM_UK_Retention_iOS_Alt',158.65)]),
   (datetime(2025,9,26,23,22),'Sep 22, 2025','Sep 25, 2025',[('ZM_UK_CPE_CopyAds_Alt',171.30)])]
for utc,a,b,camps in R:
    utc=utc.replace(tzinfo=timezone.utc); tot=round(sum(x for _,x in camps),2)
    ref=''.join(random.choice('ABCDEFGHJKLMNPQRSTUVWXYZ23456789') for _ in range(7))+'FY2'
    tx=f"{random.randint(10**15,10**16-1)}-{random.randint(10**15,10**16-1)}"
    lines=''.join(f"Campaign: {c}Results: {random.randint(4000,26000)} (Impressions) Amount: ${v:,.2f}" for c,v in camps)
    body=(f"Hi [PERSON_NAME_0036],\r\n\r\nPayment summaryAmount billed: ${tot:,.2f} USD Date range: {a}, 12:00 AM - {b}, 11:59 PM Product type: meta ads "
          f"Billing reason: Ads spend since {a}. Payment method: Visa · 7731 Reference number: {ref} \r\n\r\n{lines}\r\n\r\nTAX: TOTAL: ${tot:,.2f} USD\r\n\r\n"
          f"Transaction ID: {tx}\r\n\r\nSee full receipt[https://www.facebook.com/ads/billing_email/email_actions/?act={ACC}&txid={tx}&tx_type=3&email_action=view_transaction_detail] \r\n\r\n"
          f"Manage your ads[https://www.facebook.com/ads/billing_email/email_actions/?act={ACC}&txid={tx}&tx_type=3&email_action=manage_ads] \r\n\r\n"
          "You’re now being billed by meta Platforms Inc., formerly Facebook, Inc.\r\n\r\nThanks,\r\nThe Facebook team\r\n\r\n\r\n\r\n========================================\r\n"
          f"This message was sent to {FS}. If you don't want to receive these emails from meta in the future, please follow the link below to unsubscribe.\r\n"
          "meta Platforms, Inc., Attention: Community Support, 1 Meta Way, Menlo Park, CA 94025")
    t,m=msg(utc,f"Your meta ads receipt (Account ID: {ACC})",body)
    facts.append(('receipt',t,(utc+PT).strftime('%Y-%m-%d %H:%M PT'),f"${tot:,.2f} {ref} {camps}"))
# 2) token -> real company account id
s='\n'.join(L)
n3125=s.count('[IDENTIFIER_3125]'); s=s.replace('[IDENTIFIER_3125]','907669287942378')
# 3) doc wording
old='Meta (our ad account ending 3125)'; new='Meta (the company ad account Node runs for us)'
assert s.count(old)==1; s=s.replace(old,new)
d=len(new)-len(old)
s=s.replace('{"start": 32, "end": 1583, "named_style": "NORMAL_TEXT"','{"start": 32, "end": %d, "named_style": "NORMAL_TEXT"'%(1583+d),1)
# 4) board pack ownership
oldd="'f_0cd1e1402e8052d3d4e903', 'Q4 Board Pack - Oct 14', 'application/vnd.google-apps.spreadsheet', '[\"d_b563e7f1e1608c4d36f3b0\"]', 'leonard.hayes@harmonygames.co', '[\"frederick.stone@harmonygames.co\", \"arthur.blake@harmonygames.co\", \"PERSON_6098_EMAIL\"]', 'private', '[\"leonard.hayes@harmonygames.co\"]'"
newd="'f_0cd1e1402e8052d3d4e903', 'Q4 Board Pack - Oct 14', 'application/vnd.google-apps.spreadsheet', '[\"d_b563e7f1e1608c4d36f3b0\"]', 'frederick.stone@harmonygames.co', '[\"leonard.hayes@harmonygames.co\", \"arthur.blake@harmonygames.co\", \"PERSON_6098_EMAIL\"]', 'private', '[\"frederick.stone@harmonygames.co\"]'"
assert s.count(oldd)==1; s=s.replace(oldd,newd)
olds="'f_0cd1e1402e8052d3d4e903', 'Q4 Board Pack - Oct 14', 'leonard.hayes@harmonygames.co', '[\"frederick.stone@harmonygames.co\", \"arthur.blake@harmonygames.co\", \"PERSON_6098_EMAIL\"]'"
news="'f_0cd1e1402e8052d3d4e903', 'Q4 Board Pack - Oct 14', 'frederick.stone@harmonygames.co', '[\"leonard.hayes@harmonygames.co\", \"arthur.blake@harmonygames.co\", \"PERSON_6098_EMAIL\"]'"
assert s.count(olds)==1; s=s.replace(olds,news)
L=s.split('\n')
# insert new gmail rows after line 106 (end of receipt block)
idx=106
assert L[idx-1].startswith("VALUES ('frederick.stone@harmonygames.co/<9a17576b")
L=L[:idx]+NEW+L[idx:]
open(P,'w').write('\n'.join(L))
print('3125 tokens replaced',n3125,'doc delta',d,'new lines',len(NEW))
for f in facts: print(f)
