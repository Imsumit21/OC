"""Validate an explicit assertion inventory, not the semantics of English prose.

The reviewer must identify every acceptance-bearing assertion. This catches
declared bundles hidden under one outcome ID and distinguishes evidence from
requirements; it cannot discover an omitted or falsely classified assertion.
"""

ROLES = {"REQUIRED_RESULT", "QUALIFIER", "SUPPORTING_EVIDENCE",
         "UNREQUESTED_REQUIREMENT", "UNRESOLVED"}
KINDS = {"ENTITY_PROPERTY", "RELATIONSHIP", "IDENTITY_SET", "AGGREGATE",
         "DESTINATION", "ATOMIC_CELL"}


def validate_assertions(inventory, criterion, atomicity):
    def require(ok, message):
        if not ok:
            raise ValueError("Rubric assertion inventory: " + message)

    def text(value, label):
        require(isinstance(value, str) and bool(value.strip()), label + " needs substantive text")

    require(isinstance(inventory, dict), "each row needs assertion_inventory")
    require(type(inventory.get("complete")) is bool, "complete must be Boolean")
    text(inventory.get("reason"), "reason")
    assertions = inventory.get("assertions")
    require(isinstance(assertions, list) and bool(assertions), "assertions must be a nonempty array")
    allowed = set(atomicity["outcome_ids"])
    pending = [] if inventory["complete"] else ["incomplete assertion inventory"]
    required, seen = [], set()
    for assertion in assertions:
        require(isinstance(assertion, dict), "each assertion must be an object")
        for key in ("id", "quote", "reason"):
            text(assertion.get(key), key)
        aid = assertion["id"]
        require(aid not in seen, "duplicate assertion ID " + aid)
        seen.add(aid)
        field = assertion.get("field")
        require(isinstance(field, str) and field in {"title", "justification", "evidence"},
                aid + " needs a title/justification/evidence field")
        require(assertion["quote"] in criterion[field], aid + " quote is absent from the saved criterion field")
        role = assertion.get("role")
        require(isinstance(role, str) and role in ROLES, aid + " has an invalid role")
        oid = assertion.get("outcome_id")
        if role in {"UNREQUESTED_REQUIREMENT", "UNRESOLVED"}:
            require(oid is None, aid + " must not invent an outcome for an unsupported/unresolved requirement")
            text(assertion.get("repair"), aid + ".repair")
            pending.append(aid + ": " + role)
            continue
        require(isinstance(oid, str) and oid in allowed, aid + " must link to this row's declared outcome")
        if role == "REQUIRED_RESULT":
            required.append(oid)
            if field != "title":
                pending.append(aid + ": required result hidden in a supporting field")
            kind = assertion.get("kind")
            require(isinstance(kind, str) and kind in KINDS, aid + " needs a recognized result kind")
            entities = assertion.get("entities")
            require(isinstance(entities, list) and bool(entities) and
                    all(isinstance(x, str) and x.strip() for x in entities), aid + ".entities must name actual subjects")
            require(len(entities) == len({x.strip().casefold() for x in entities}), aid + " repeats an entity")
            text(assertion.get("property"), aid + ".property")
            exception = atomicity.get("exception") or {}
            from hg_coherent_record import allowed_group
            if kind == "ENTITY_PROPERTY" and len(entities) != 1 and not allowed_group(assertions, atomicity):
                pending.append(aid + ": per-entity properties need one result per entity")
            elif kind == "IDENTITY_SET":
                if assertion["property"] != "membership" or exception.get("kind") != "identity_only_set":
                    pending.append(aid + ": identity-only membership cannot hide per-entity properties")
            elif kind == "RELATIONSHIP":
                text(assertion.get("conclusion"), aid + ".conclusion")
            elif kind in {"AGGREGATE", "DESTINATION", "ATOMIC_CELL"}:
                eligible = {"AGGREGATE": {"aggregate_invariant", "large_audit"},
                            "DESTINATION": {"destination_identity"}, "ATOMIC_CELL": {"atomic_cell"}}[kind]
                if exception.get("kind") not in eligible:
                    pending.append(aid + ": justify the applicable narrow atomic exception")
        elif role == "SUPPORTING_EVIDENCE":
            omission = assertion.get("omission_test")
            require(isinstance(omission, dict), aid + " needs an omission_test")
            for key in ("example", "reason"):
                text(omission.get(key), aid + ".omission_test." + key)
            require(omission.get("result") in ("ACCEPT", "REJECT", "UNRESOLVED"), aid + " needs an actual omission-test result")
            if omission["result"] != "ACCEPT":
                pending.append(aid + ": supporting evidence acts as an extra acceptance requirement")
    if not required:
        pending.append("no independently required result identified")
    if len(required) > 1:
        from hg_coherent_record import allowed_group
        if not allowed_group(assertions, atomicity):
            pending.append("multiple required assertions need separate criteria, even under one outcome ID")
    if set(required) != allowed:
        pending.append("required assertions do not cover this row's declared outcomes")
    return pending
