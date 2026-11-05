"""Write plan/record_dump_rules.md: the seeded rule/context records as Frederick sees them (blind-sweep packet)."""
import sys,json,contextlib,io
sys.path.insert(0,'../../tools'); sys.path.insert(0,'plan')
from base_check import parse_sql
with contextlib.redirect_stdout(io.StringIO()):
    import build_scenario as B
st=parse_sql(open('../01_Universe_Inject.sql').read())
ids=json.load(open('plan/sql_ids.json'))['ids']
rows={}
for x in st:
    if x['op']!='insert': continue
    r=x['row']; rid=r.get('id') or r.get('event_id') or r.get('document_id') or r.get('contact_id') or r.get('spreadsheet_id')
    rows.setdefault(rid,[]).append((x['table'],r))
out=["# Rule and context records (seeded), as Frederick sees them\n"]
def show(rid,label,where):
    for t,r in rows.get(rid,[]):
        if t in ('gdrive.drive_files','gsheets.sheets_spreadsheets'): continue
        txt = r.get('body_text') or r.get('text') or r.get('body') or r.get('description') or r.get('desc') or r.get('name') or r.get('grid_json')
        hdr = ' | '.join(str(r.get(k)) for k in ('subject','title','summary','name','date','created_at','start_ts','end_ts') if r.get(k))
        out.append(f"## {label} ({where}) id {rid}\n{hdr}\n{str(txt).replace(chr(92)+'r','').replace(chr(92)+'n',chr(10))}\n")
I=B.IDS
show(ids['msg']['hub'],"Leonard's email to Frederick, Sep 30","Gmail, Frederick's inbox")
show(I['guardrails_doc'],'Runway guardrails doc','Google Docs, shared with Frederick'); show(I['readme_doc'],'README in the Q4 commitments folder','Google Docs')
show(I['template_sheet'],'Template sheet','Google Sheets')
show(ids['msg']['esg_note'],"ESG Law's signing note to Leonard (Frederick cc)",'Gmail'); show(ids['msg']['esg_ack'],"Leonard's reply in that thread",'Gmail'); show(I['esg_checklist_doc'],'ESG intake checklist','Google Docs')
show(I['ua_buckets_doc'],'UA spend buckets doc','Google Docs (Frederick owns)'); show(I['tracker_sheet'],"Frederick's July vendor tracker",'Google Sheets')
for k,v in ids['slack_mid'].items(): show(v,'Slack message','#executives or Leonard-Frederick DM')
show('ZOM-567','Linear issue (team ZOM)','Linear'); show(I['zom567_cmt'],'Comment on ZOM-567 by Arthur','Linear')
show(I['keep_card'],"Card on the Harmony Games Trello board (Doing list), by Arthur",'Trello')
out.append("Checklist 'Keep running' on that card:")
for it in ids['keep_items']:
    for t,r in rows.get(it,[]): out.append('  - '+r['name'])
show(ids['msg']['clipforge_notice'],'Notice from Paylane (no-reply)','Gmail')
for e,l in (('evt_fd469c29811879519c2c96','Calendar event (organizer Leonard; Frederick, Robert, Arthur invited)'),('evt_564a16d0f5f6598d0360d5','Calendar event (organizer Robert; Frederick invited)'),('evt_0a5e42c3aac62434ba2cfc','Calendar event (organizer Frederick; one external attendee)')):
    show(e,l,"Frederick's calendar")
out.append("## Contacts already present\n- ESG Law intake (job: Outside counsel - agreement intake), PERSON_2599_EMAIL\n- Noor Haddad (job Kinetic Arcade), Aiden Clarke (job Lumencloud), Leah Brennan (job Markward)\n")
open('plan/record_dump_rules.md','w').write('\n'.join(out))
print(len(out))
