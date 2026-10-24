"""Coherent-record atomicity exception (rubric-revision-v8); binding checks only, not a semantic grader."""
import json

FIELDS={'pull_request':{'number','merged_at'},'relocation':{'person','company','city'}}


def allowed_group(assertions, atomicity):
    ex=atomicity.get('exception') or {}
    if not isinstance(assertions,list) or not all(isinstance(a,dict) for a in assertions):
        return False
    if ex.get('kind') in {'same_tool_output', 'shared_email_content'}:
        req=[a for a in assertions if a.get('role')=='REQUIRED_RESULT']
        common=(bool(req) and len(set(atomicity['outcome_ids']))==1 and
                isinstance(ex.get('source_id'),str) and bool(ex['source_id']) and
                all(a.get('field')=='title' and a.get('source_id')==ex['source_id'] and
                    a.get('behavior')=='CONTENT' and a.get('outcome_id')==atomicity['outcome_ids'][0]
                    for a in req))
        if not common:
            return False
        if ex['kind']=='same_tool_output':
            return isinstance(ex.get('fields'),list) and bool(ex['fields']) and {a.get('property') for a in req}==set(ex['fields'])
        recipients=ex.get('recipients')
        return (isinstance(recipients,list) and len(recipients)>=2 and len(set(recipients))==len(recipients)
                and isinstance(ex.get('shared_predicate'),str) and bool(ex['shared_predicate'])
                and all(a.get('quote')==ex['shared_predicate'] for a in req))
    if ex.get('kind')!='coherent_record':
        return False
    kind=ex.get('record_kind')
    fields=ex.get('fields')
    if kind not in FIELDS or not isinstance(fields,list) or len(fields)<2:
        return False
    if any(not isinstance(f,str) for f in fields) or len(fields)!=len(set(fields)) or not set(fields)<=FIELDS[kind]:
        return False
    if not all(isinstance(ex.get(k),str) and ex[k].strip() for k in ('source_id','entity')):
        return False
    req=[a for a in assertions if a.get('role')=='REQUIRED_RESULT']
    return (len(req)==len(fields) and len(set(atomicity['outcome_ids']))==1 and
            {a.get('property') for a in req}==set(fields) and
            all(a.get('field')=='title' and a.get('kind')=='ENTITY_PROPERTY' and
                a.get('entities')==[ex['entity']] and a.get('source_id')==ex['source_id'] and
                a.get('outcome_id')==atomicity['outcome_ids'][0] for a in req))


def verify_record_source(atomicity, reader, sources):
    ex=atomicity.get('exception') or {}
    if ex.get('kind') in {'same_tool_output', 'shared_email_content'}:
        source=sources.get(ex.get('source_id'))
        if not source or source.get('visibility')!='VISIBLE':
            raise ValueError('QC grouping exception needs a visible source')
        text=reader.quote(source)
        if ex['kind']=='same_tool_output':
            if source.get('origin')!='tool_output' or not source.get('output_id') or 'pointer' not in source:
                raise ValueError('same_tool_output needs identified output evidence, not a whole export')
            selected=json.loads(text)
            if not isinstance(selected,dict) or not ex.get('fields') or any(f not in selected for f in ex['fields']):
                raise ValueError('shared output fields must exist in one selected output')
        elif ex.get('shared_predicate','') not in text or not ex.get('shared_predicate'):
            raise ValueError('shared content predicate must be supported by its source')
        return
    if ex.get('kind')!='coherent_record':
        return
    source=sources.get(ex.get('source_id'))
    if not source or source.get('visibility')!='VISIBLE' or 'pointer' not in source:
        raise ValueError('coherent_record needs one visible, exactly selected JSON source record')
    selected=json.loads(reader.quote(source))
    if not isinstance(selected,dict) or any(field not in selected for field in ex.get('fields',[])):
        raise ValueError('coherent_record fields must exist in the selected record')
    if not ex.get('fields'):
        raise ValueError('coherent_record needs explicit fields')
