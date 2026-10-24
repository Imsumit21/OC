"""Validate recorded authority, alternatives and outcome ownership for rubric v6."""

from hg_review_evidence import EvidenceReader, authority, links, sources


def validate_acceptance(record, proposal, root, context, *, reader=None, known=None, check_facts=True):
    reader = reader or EvidenceReader(root)
    known = known if known is not None else sources(reader, record.get("sources"))
    pending = []

    def text(value, label):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(label + " needs an explanation")

    for req in record["requirements"]:
        if not authority(req.get("authority_chain"), known, root, context):
            pending.append(req["id"] + ": unresolved/inaccessible requirement authority")

    owners = {}
    units = {}
    for req in record["requirements"]:
        for outcome in req["outcomes"]:
            identity = tuple(outcome[k].strip().casefold() for k in ("entity", "property", "output"))
            if identity in units:
                pending.append("duplicate semantic outcome IDs: " + units[identity] + ", " + outcome["id"])
            units[identity] = outcome["id"]
    for row in record["rows"]:
        number = row["row"]
        if check_facts:
            from hg_rubric_fact_binding import checked_facts
            result = checked_facts(row.get('fact_review'), proposal[number-1], reader, known, root, context)
            pending.extend(f"R{number}: source-derived fact mismatch: " + str(item.get('quote'))
                           for item in result['mismatches'])
            pending.extend(f"R{number}: " + item['reason'] for item in result['unresolved'])
        from hg_coherent_record import verify_record_source
        verify_record_source(row["atomicity"], reader, known)
        for oid in row["atomicity"]["outcome_ids"]:
            owners.setdefault(oid, []).append(number)
        review = row.get("restriction_review")
        if not isinstance(review, dict) or not isinstance(review.get("restrictions"), list):
            raise ValueError(f"R{number} needs restriction_review and its explicit restriction list")
        text(review.get("reason"), f"R{number}.restriction_review.reason")
        for restriction in review["restrictions"]:
            field = restriction.get("field")
            quote = restriction.get("quote")
            text(quote, "restriction.quote")
            if field not in {"title", "justification", "evidence"} or quote not in proposal[number-1][field]:
                raise ValueError("Restriction quote is absent from the saved rubric field")
            status = restriction.get("status")
            if status not in {"AUTHORIZED", "UNSUPPORTED", "UNRESOLVED"}:
                raise ValueError("Restriction needs AUTHORIZED, UNSUPPORTED or UNRESOLVED")
            text(restriction.get("reason"), "restriction.reason")
            if status == "AUTHORIZED":
                if not authority(restriction.get("authority_chain"), known, root, context):
                    pending.append(f"R{number}: unresolved/inaccessible restriction authority")
            else:
                text(restriction.get("counterexample"), "restriction.counterexample")
                pending.append(f"R{number}: {status} restriction: {quote}")
    for oid, rows in owners.items():
        if len(rows) > 1:
            pending.append(f"duplicate grading of outcome {oid}: rows {rows}")

    overlap = record.get("overlap_review")
    if not isinstance(overlap, dict) or type(overlap.get("complete")) is not bool:
        raise ValueError("overlap_review needs Boolean complete and reason")
    text(overlap.get("reason"), "overlap_review.reason")
    if not overlap["complete"]:
        pending.append("incomplete set-wide overlap review")

    alternatives = record.get("alternative_review")
    if not isinstance(alternatives, dict) or type(alternatives.get("complete")) is not bool:
        raise ValueError("alternative_review needs Boolean complete")
    links(alternatives.get("source_ids"), known, "alternative_review.source_ids")
    text(alternatives.get("reason"), "alternative_review.reason")
    if not alternatives["complete"]:
        pending.append("incomplete alternative inventory")
    branches = alternatives.get("branches")
    if not isinstance(branches, list):
        raise ValueError("alternative_review.branches must be an array (empty needs a reason)")
    seen = set()
    for branch in branches:
        text(branch.get("id"), "alternative.id")
        if branch["id"] in seen:
            raise ValueError("Duplicate alternative ID")
        seen.add(branch["id"])
        for key in ("quote", "example", "reason"):
            text(branch.get(key), "alternative." + key)
        src = links([branch.get("source_id")], known, "alternative.source_id")[0]
        reader.quote({**src, "quote": branch["quote"]})
        validity = branch.get("validity")
        if validity not in {"SUPPORTED", "UNSUPPORTED", "UNRESOLVED"}:
            raise ValueError("Alternative validity must be SUPPORTED, UNSUPPORTED or UNRESOLVED")
        if validity == "SUPPORTED":
            if not authority(branch.get("authority_chain"), known, root, context):
                pending.append(branch["id"] + ": unresolved alternative authority")
        elif validity == "UNRESOLVED":
            pending.append(branch["id"] + ": unresolved alternative validity")
        tested, rejected = branch.get("tested_rows"), branch.get("rejecting_rows")
        if (not isinstance(tested, list) or any(type(i) is not int for i in tested) or
                sorted(tested) != list(range(1, len(proposal)+1))):
            raise ValueError("Every alternative needs a whole-rubric test, including all rows")
        if (not isinstance(rejected, list) or any(type(i) is not int or i not in tested for i in rejected) or
                len(rejected) != len(set(rejected))):
            raise ValueError("Alternative rejecting_rows must be unique current rows")
        if branch.get("result") not in {"ACCEPT", "REJECT", "UNRESOLVED"}:
            raise ValueError("Alternative test needs ACCEPT, REJECT or UNRESOLVED")
        if (branch["result"] == "ACCEPT" and rejected) or (branch["result"] == "REJECT" and not rejected):
            raise ValueError("Alternative result disagrees with rejecting_rows")
        if validity == "SUPPORTED" and branch["result"] != "ACCEPT":
            pending.append(branch["id"] + ": valid alternative rejected/unresolved")
    return pending
