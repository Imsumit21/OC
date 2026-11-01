import json,re,csv,io
w=json.load(open('writes.json'))
R={}
for k,v in w.items():
    rows=[]
    for r in v['reg']:
        m=re.search(r"cat > /tmp/reg.csv <<'EOF'\n(.*?)\nEOF",r,re.S)
        if m: rows=list(csv.reader(io.StringIO(m.group(1))))
        elif r.startswith('{'):
            j=json.loads(r)
            if 'values' in j: rows=j['values']
    hdr=rows[0]; body=rows[1:]
    reg={}
    for row in body:
        t=re.search(r"ZOM-\d+",row[0]) if row else None
        if not t: continue
        txt=' | '.join(row)
        st=[c for c in row if c.strip() in('Y','N')]
        reg[t.group(0)]=dict(change=row[hdr.index([h for h in hdr if 'erver' in h][0])], status=st[0] if st else '?', raw=txt)
    dm=' '.join(d.get('text') or d.get('message','') for d in v['dm'])
    mv={}
    for m_ in v['mv']:
        mv[m_.get('id') or m_.get('issueId')]=m_.get('state') or m_.get('stateId')
    cm={}
    for c in v['cm']:
        cm[c.get('issueId')]=c.get('body')
    R[k]=dict(reg=reg,dm=dm,mv=mv,cm=cm,share=v['share'],other=v['other'],hdr=hdr)
json.dump(R,open('parsed.json','w'),indent=1)
for k,x in R.items():
    print(k,'hdr',x['hdr'],'rows',len(x['reg']),sorted(x['reg']))
    print('  mv',x['mv']); print('  dm',x['dm'][:150].replace('\n',' '))
