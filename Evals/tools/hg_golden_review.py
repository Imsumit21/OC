#!/usr/bin/env python3
"""Bind a golden audit to its inputs and evidence; never generate an answer.

Checks completeness, references, recorded judgments and file hashes. Source
interpretation and the truth of those judgments remain the evaluator's work.
"""

import argparse
import json
import os
from pathlib import Path
import re
import tempfile

from hg_review_evidence import EvidenceReader, authority, sources as evidence_sources
from hg_preflight import reject_constant, unique_object
from hg_rubric_loop import digest, fingerprint, load_json, local, review_context

POLICY = "golden-audit-v4"
FORMAT_VERSION = 3
DEFECT_CLASSES = ("wrong_value", "added_restriction", "missing_outcome", "loose_acceptance",
                  "contradiction", "infeasible_path", "upstream_artifact")
REPAIR_OWNERS = ("contributor", "platform", "prompt")
# Platform caps on the golden_answer field: 5,000 until 2026-09-22, 50,000 after. A body of
# exactly either length is a cut, not a coincidence.
TRUNCATION_LENGTHS = (5000, 50000)
SENTENCE_END = re.compile(r'[.!?)\]|`"\u201d*]$|```$')
ENTITY_PATTERNS = (
    re.compile(r"\b[A-Z]{2,6}-\d{1,5}\b"),                 # ticket ids: ENG-2438
    re.compile(r"(?<![\w#])#\d{1,6}\b"),                    # PR / issue numbers: #540
    re.compile(r"(?<![\w#])#[a-z][a-z0-9_-]{2,}\b"),         # channels: #engineering
    re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),                  # ISO dates
    re.compile(r"\b[A-Z][a-z]{2,} [A-Z][a-z]{2,}\b"),         # person names: Arthur Blake
)
VALUE_PATTERNS = (
    re.compile(r"\$\s?\d[\d,]*(?:\.\d+)?"),               # currency
    re.compile(r"\b\d+(?:\.\d+)?\s?%"),                     # percentages
    re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),                  # ISO dates
    re.compile(r"\b[A-Z]{2,6}-\d{2,5}\b"),                 # ticket ids
    re.compile(r"(?<![\w#])#\d{1,6}\b"),                    # PR / issue numbers
)
REPORT = Path("Evals/task_inputs/reports/2_golden.md")
CONTEXT = REPORT.parent / "drafts/golden_review_context.json"
RECORD = CONTEXT.with_name("golden_review_record.json")
HISTORY = CONTEXT.parent / "golden_history"
ANSWER = Path("Evals/task_inputs/08_Golden_Answer.md")
EXPLICIT_DRAFT = CONTEXT.parent / "08_Golden_Answer.md"
CHECKS = ("completeness", "accuracy", "authority", "valid_solutions",
          "wrong_solutions", "consistency_feasibility")
INPUT_KEYS = {"task-details", "universe", "prompt", "golden", "injection", "error-async", "dynamic-context"}
REFERENCES = (
    "Evals/2_Golden_Response_Eval.md", "claude/skills/golden/SKILL.md",
    "Evals/WORKFLOW.md", "Evals/INPUTS.md", "Evals/EXECUTION.md", "Evals/ENVIRONMENT.md",
    "Evals/SEARCH.md", "Evals/UNIVERSE_MAP.md", "Evals/Authoring_Workflow.md",
    "Evals/references/rules/golden_review_record.md", "Evals/references/rules/scoring_notes.md",
    "Evals/references/rules/scoring.json", "Evals/references/rules/long_horizon.md",
    "Evals/references/persona/roster.json", "Evals/references/persona/acl.md",
    "Evals/references/tools/catalog.json", "Evals/references/tools/manifest.json",
    "{universe}/universe_manifest.json", "{universe}/source_layout.json",
    "Evals/tools/hg_review_evidence.py",
    "Evals/tools/hg_golden_review.py", "Evals/tools/hg_report_contract.py",
    "Evals/tools/hg_write_output.py", "Evals/tools/hg_rubric_loop.py",
)
BINDING = ("review_policy", "review_mode", "review_iteration", "reviewed_golden_sha256",
           "review_context_sha256")


def _normalize(text):
    return re.sub(r"\s+", "", text).casefold()


def entities(text):
    found = set()
    for pattern in ENTITY_PATTERNS:
        found.update(m.group(0) for m in pattern.finditer(text))
    return found


def values(text):
    found = []
    for pattern in VALUE_PATTERNS:
        for match in pattern.finditer(text):
            token = match.group(0)
            if token not in found:
                found.append(token)
    return found


def golden_section(text):
    """The graded answer body: the `## golden_answer` section of a composite export, else the whole text."""
    match = re.search(r"(?ms)^## golden_answer\s*\n(.*?)(?=^## |\Z)", text)
    return match.group(1) if match else text


GENERIC_TOKENS = frozenset("""github linear slack gmail gdrive drive sheets docs confluence jira trello notion snowflake
calendar email ticket tickets issue issues channel thread message messages report reports harmonygames""".split())


def distinctive_tokens(text):
    """Proper-noun-like or numeric tokens that identify a task; generic tool names are excluded."""
    found = set()
    for match in re.finditer(r"[A-Za-z][A-Za-z0-9_'-]{3,}|\d{3,}", text):
        token = match.group(0)
        lowered = token.casefold()
        if lowered in GENERIC_TOKENS:
            continue
        if token[0].isupper() or any(c.isdigit() for c in token) or "_" in token or "-" in token:
            found.add(lowered)
    return found


def prompt_overlap(golden_text, prompt_text=None, dynamic_context=None):
    """Mechanical evidence for the reviewer's artifact_match judgment; never a verdict by itself."""
    answer = distinctive_tokens(golden_section(golden_text)) | entities(golden_section(golden_text))
    result = {}
    for label, other in (("prompt", prompt_text), ("dynamic_context", dynamic_context)):
        if not other:
            continue
        expected = distinctive_tokens(other) | {e.casefold() for e in entities(other)}
        shared = sorted(expected & {a.casefold() for a in answer})
        result[label] = {"expected": len(expected), "shared": len(shared), "examples": shared[:8]}
    return result


def integrity_findings(golden_text, prompt_text=None, dynamic_context=None, accept_ending=None):
    """Artifact-integrity checks (golden-audit-v4 G2) on the graded answer body. Returns blocking findings."""
    findings = []
    body = golden_section(golden_text)
    stripped = body.strip()
    cut = next((n for n in TRUNCATION_LENGTHS if len(body) == n or len(stripped) == n), None)
    if cut is not None:
        findings.append(f"artifact_truncated: the golden_answer is exactly {cut:,} characters, a known platform cap; restore the full text")
    if stripped and not SENTENCE_END.search(stripped[-3:]) and not accept_ending:
        findings.append("bad_ending: the golden_answer does not end on sentence-final punctuation, a table row or a code fence (last characters "
                        + repr(stripped[-20:]) + "); restore the ending or start with --accept-ending \"<reason>\"")
    return findings


def relevant_input(key):
    # Hashing a supplied lookup binds its version; it does not inspect its rubric.
    if key.startswith("source:"):
        from hg_store_input import SLOTS, BATCHES

        slot = key.removeprefix("source:")
        if slot in SLOTS or slot in BATCHES:
            return slot in INPUT_KEYS
    return key in INPUT_KEYS or key.startswith(("reference:", "source:", "extra:"))


def context(root, answer, mode):
    result = review_context(root, input_filter=relevant_input,
                            reference_paths=REFERENCES, policy=POLICY)
    result["manifest"]["review_artifact"] = dict(path=answer, mode=mode,
                                                   sha256=fingerprint(local(root, Path(answer))))
    result["sha256"] = digest(json.dumps(result["manifest"], sort_keys=True,
                                        ensure_ascii=False).encode("utf-8"))
    return result


def archive(root, relative):
    path = local(root, relative)
    if not path.is_file():
        return
    payload = path.read_bytes()
    target = local(root, HISTORY / f"{path.stem}-{digest(payload)}{path.suffix}")
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if target.read_bytes() != payload:
            raise ValueError("Golden history collision; preserve and investigate.")
        path.unlink()
    else:
        path.replace(target)


def start_review(root, answer=None, draft=False, accept_ending=None):
    """Create a receipt for an existing input (or an explicitly authored draft)."""
    from hg_store_input import SLOTS

    relative = Path(answer) if answer is not None else (EXPLICIT_DRAFT if draft else ANSWER)
    if relative.is_absolute():
        relative = relative.resolve().relative_to(root.resolve())
    path = local(root, relative)
    mode = "DRAFT" if draft else "AUDIT"
    ctx = context(root, relative.as_posix(), mode)
    states = ctx["manifest"]["inputs"]
    def supplied(key):
        return any(states.get(k, {}).get("state") == "saved" and states[k].get("files")
                   for k in (key, "source:" + key)) or (
                       key not in states and local(root, Path("Evals/task_inputs") / SLOTS[key]).is_file())
    for key in ("prompt", "task-details"):
        if not supplied(key):
            raise ValueError("Save the required " + key + " input before starting the golden audit.")
    if not (supplied("injection") or states.get("injection", {}).get("usage") == "not_used"):
        raise ValueError("Save injection SQL or an explicit no-injection decision first.")
    if draft:
        if relative != EXPLICIT_DRAFT:
            raise ValueError("Explicit draft reviews use reports/drafts/08_Golden_Answer.md.")
    else:
        allowed = {item["path"] for key in ("golden", "source:golden")
                   for item in states.get(key, {}).get("files", [])}
        if "golden" not in states:
            allowed.add(ANSWER.as_posix())  # Legacy canonical input.
        if relative.as_posix() not in allowed:
            raise ValueError("Audit target must be the saved golden input; save/match its input mapping first.")
    if not path.is_file() or not path.read_bytes().strip():
        raise ValueError("No nonempty golden answer to audit. Supply it; this helper never generates one.")
    golden_text = path.read_text(encoding="utf-8", errors="replace")
    def saved_text(key):
        files = states.get(key, {}).get("files") or states.get("source:" + key, {}).get("files")
        if files:
            candidate = local(root, Path(files[0]["path"]))
        else:
            candidate = local(root, Path("Evals/task_inputs") / SLOTS[key])
        return candidate.read_text(encoding="utf-8", errors="replace") if candidate.is_file() else None
    prompt_text, dynamic_text = saved_text("prompt"), saved_text("dynamic-context")
    findings = integrity_findings(golden_text, prompt_text, dynamic_text, accept_ending)
    overlap = prompt_overlap(golden_text, prompt_text, dynamic_text)
    if findings:
        raise ValueError("artifact_integrity: " + " | ".join(findings)
                         + " | Write a BLOCKED report (no six-check verdict); this is a platform/upstream defect, not an authoring finding.")
    previous = load_json(local(root, CONTEXT)) if local(root, CONTEXT).is_file() else {}
    iteration = previous.get("review_iteration", 0)
    if type(iteration) is not int or iteration < 0:
        raise ValueError("Invalid previous golden iteration.")
    receipt = dict(review_policy=POLICY, review_mode=mode, review_iteration=iteration + 1,
                   reviewed_golden_sha256=fingerprint(path), review_context_sha256=ctx["sha256"],
                   answer_path=relative.as_posix(), integrity_override=accept_ending or None,
                   golden_length=len(golden_text), golden_answer_length=len(golden_section(golden_text).strip()),
                   prompt_overlap=overlap, context=ctx["manifest"])
    for item in (REPORT, RECORD, CONTEXT):
        archive(root, item)
    destination = local(root, CONTEXT)
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=destination.parent, delete=False) as stream:
        pending = Path(stream.name)
        stream.write(payload)
    try:
        os.replace(pending, destination)
    finally:
        pending.unlink(missing_ok=True)
    return {k: v for k, v in receipt.items() if k != "context"}


def validate_record(root, content, passing=False):
    def require(ok, message):
        if not ok:
            raise ValueError("Golden review record: " + message)
    def obj(value, label):
        require(isinstance(value, dict), label + " must be an object")
        return value
    def text(value, label):
        require(isinstance(value, str) and bool(value.strip()), label + " needs evidence/explanation")
    def enum(value, choices, label):
        require(isinstance(value, str) and value in choices, label + " has an invalid result")
    def array(value, label, nonempty=False):
        require(isinstance(value, list) and (not nonempty or bool(value)), label + " must be an array" + (" with entries" if nonempty else ""))
        return value
    def refs(value, known, label, nonempty=False):
        ids = array(value, label, nonempty)
        require(all(isinstance(x, str) and x in known for x in ids), label + " references unknown evidence/claims")
        require(len(set(ids)) == len(ids), label + " contains duplicate references")
        return set(ids)

    receipt_path = local(root, CONTEXT)
    require(receipt_path.is_file(), "start an audit with hg_golden_review.py start first")
    receipt = obj(load_json(receipt_path), "review context")
    require(receipt.get("review_policy") == POLICY, "retired review context")
    text(receipt.get("answer_path"), "review context.answer_path")
    enum(receipt.get("review_mode"), {"AUDIT", "DRAFT"}, "review context.mode")
    require(type(receipt.get("review_iteration")) is int and receipt["review_iteration"] > 0,
            "invalid review iteration")
    ctx = context(root, receipt["answer_path"], receipt["review_mode"])
    require(ctx["sha256"] == receipt.get("review_context_sha256"), "inputs, answer or rules changed; start a new review")
    require(receipt.get("reviewed_golden_sha256") == ctx["manifest"]["review_artifact"]["sha256"],
            "review context does not match the actual golden fingerprint")
    record = json.loads(content, object_pairs_hook=unique_object, parse_constant=reject_constant)
    obj(record, "record")
    require(type(record.get("format_version")) is int and record["format_version"] == FORMAT_VERSION,
            "unsupported format_version; golden-audit-v4 uses record format 3 with defect_class and repair_owner")
    require(type(record.get("review_iteration")) is int and all(record.get(k) == receipt.get(k) for k in BINDING),
            "record binding differs from the current audit")
    open_items, sources, claims, requirements = [], {}, {}, {}
    defect_classes, repair_owners = {}, {}
    def classify(item, label, failing):
        if not failing:
            return
        require(item.get("defect_class") in DEFECT_CLASSES, label + " needs defect_class: " + ", ".join(DEFECT_CLASSES))
        require(item.get("repair_owner") in REPAIR_OWNERS, label + " needs repair_owner: " + ", ".join(REPAIR_OWNERS))
        defect_classes[item["defect_class"]] = defect_classes.get(item["defect_class"], 0) + 1
        repair_owners[item["repair_owner"]] = repair_owners.get(item["repair_owner"], 0) + 1
    reader = EvidenceReader(root)
    sources = evidence_sources(reader, record.get("sources"))
    answer_anchor = dict(path=receipt["answer_path"], sha256=receipt["reviewed_golden_sha256"])
    def golden_quote(item):
        anchor = {**answer_anchor, "quote": item.get("golden_quote")}
        if "golden_pointer" in item:
            anchor["pointer"] = item["golden_pointer"]
        reader.quote(anchor)

    for claim in array(record.get("claims"), "claims"):
        obj(claim, "claim")
        for key in ("id", "statement", "golden_location", "reason"):
            text(claim.get(key), "claim." + key)
        require(claim["id"] not in claims, "duplicate claim ID")
        golden_quote(claim)
        enum(claim.get("result"), {"VERIFIED", "INCORRECT", "UNRESOLVED"}, "claim")
        classify(claim, "claim " + claim["id"], claim["result"] == "INCORRECT")
        refs(claim.get("source_ids"), sources, "claim.source_ids", claim["result"] != "UNRESOLVED")
        support = refs(claim.get("supporting_source_ids"), sources, "claim.supporting_source_ids", claim["result"] == "VERIFIED")
        require(support <= set(claim["source_ids"]), "supporting sources must be included in source_ids")
        if claim["result"] == "VERIFIED" and any(sources[x]["visibility"] != "VISIBLE" for x in support):
            open_items.append(claim["id"] + ": verified claim depends on inaccessible/unresolved evidence")
        if claim["result"] != "VERIFIED":
            open_items.append(claim["id"] + ": " + claim["result"])
        claims[claim["id"]] = claim
    for req in array(record.get("requirements"), "requirements", True):
        obj(req, "requirement")
        for key in ("id", "authority", "scope", "expected_result", "golden_resolution", "reason"):
            text(req.get(key), "requirement." + key)
        require(req["id"] not in requirements, "duplicate requirement ID")
        if not authority(req.get("authority_chain"), sources, root, receipt["context"]):
            open_items.append(req["id"] + ": unresolved/inaccessible requirement authority")
        enum(req.get("result"), {"PASS", "FAIL", "UNRESOLVED"}, "requirement")
        classify(req, "requirement " + req["id"], req["result"] == "FAIL")
        refs(req.get("source_ids"), sources, "requirement.source_ids", req["result"] != "UNRESOLVED")
        linked = refs(req.get("claim_ids"), claims, "requirement.claim_ids", req["result"] == "PASS")
        if req["result"] == "PASS":
            require(all(claims[x]["result"] == "VERIFIED" for x in linked), "PASS requirement depends on an unverified claim")
        verification = obj(req.get("verification"), "requirement.verification")
        enum(verification.get("kind"), {"direct", "calculation", "absence", "cohort", "decision"}, "verification.kind")
        text(verification.get("details"), "verification.details")
        require(type(verification.get("complete")) is bool, "verification.complete must be Boolean")
        if req["result"] != "PASS" or not verification["complete"]:
            open_items.append(req["id"] + ": incomplete/failed verification")
        for name, expected in (("valid_case", "ACCEPT"), ("wrong_case", "REJECT")):
            case = obj(req.get(name), req["id"] + "." + name)
            for key in ("example", "reason"):
                text(case.get(key), name + "." + key)
            enum(case.get("result"), {"ACCEPT", "REJECT", "UNRESOLVED"}, name)
            if case["result"] != expected:
                open_items.append(req["id"] + "." + name + ": expected " + expected)
        requirements[req["id"]] = req
    chronology = obj(record.get("chronology"), "chronology")
    require(type(chronology.get("complete")) is bool, "chronology.complete must be Boolean")
    text(chronology.get("reason"), "chronology.reason")
    if not chronology["complete"]:
        open_items.append("incomplete source chronology check")
    for comparison in array(chronology.get("comparisons"), "chronology.comparisons"):
        refs(comparison.get("source_ids"), sources, "chronology.source_ids", True)
        refs(comparison.get("claim_ids"), claims, "chronology.claim_ids", True)
        enum(comparison.get("result"), {"PASS", "FAIL", "UNRESOLVED"}, "chronology comparison")
        text(comparison.get("reason"), "chronology comparison.reason")
        classify(comparison, "chronology comparison", comparison["result"] == "FAIL")
        if comparison["result"] != "PASS":
            open_items.append("chronology: " + comparison["result"])
    alternatives = obj(record.get("alternative_review"), "alternative_review")
    require(type(alternatives.get("complete")) is bool, "alternative_review.complete must be Boolean")
    text(alternatives.get("reason"), "alternative_review.reason")
    if not alternatives["complete"]:
        open_items.append("incomplete main-answer/alternative consistency review")
    for branch in array(alternatives.get("branches"), "alternative_review.branches"):
        golden_quote(branch)
        enum(branch.get("result"), {"PASS", "FAIL", "UNRESOLVED"}, "alternative")
        for key in ("example", "reason"):
            text(branch.get(key), "alternative." + key)
        classify(branch, "alternative branch", branch["result"] == "FAIL")
        if not authority(branch.get("authority_chain"), sources, root, receipt["context"]):
            open_items.append("unresolved/inaccessible alternative authority")
        if branch["result"] != "PASS":
            open_items.append("alternative: " + branch["result"])
    for repair in array(record.get("repairs"), "repairs"):
        text(repair.get("old_quote"), "repair.old_quote")
        text(repair.get("reason"), "repair.reason")
        # A claimed fix must actually be in the saved answer. Old wording may
        # legitimately remain as an explicitly labelled historical quotation.
        golden_quote(repair)
        affected = refs(repair.get("claim_ids"), claims, "repair.claim_ids", True)
        if any(claims[x]["result"] != "VERIFIED" for x in affected):
            open_items.append("claimed repair still has unverified/incorrect claims")
    match = obj(record.get("artifact_match"), "artifact_match")
    enum(match.get("result"), {"MATCH", "MISMATCH"}, "artifact_match")
    text(match.get("reason"), "artifact_match.reason")
    mismatch = match["result"] == "MISMATCH"
    if mismatch:
        classify({"defect_class": match.get("defect_class", "upstream_artifact"),
                  "repair_owner": match.get("repair_owner", "platform")}, "artifact_match", True)
    checks = obj(record.get("checks"), "checks")
    require(set(checks) == set(CHECKS), "all six golden checks are required")
    for name, check in checks.items():
        obj(check, name)
        enum(check.get("result"), {"PASS", "FAIL", "UNRESOLVED"}, name)
        text(check.get("reason"), name + ".reason")
        classify(check, "check " + name, check["result"] == "FAIL")
        if check["result"] != "PASS":
            open_items.append(name + ": " + check["result"])
    # G3: every value-bearing token in the saved golden must be a ledgered claim.
    answer_path = local(root, Path(receipt["answer_path"]))
    golden_text = answer_path.read_text(encoding="utf-8", errors="replace") if answer_path.is_file() else ""
    ledger = _normalize(" ".join(c.get("golden_quote", "") + " " + c.get("statement", "") for c in claims.values()))
    unledgered = [token for token in values(golden_text) if _normalize(token) not in ledger]
    for token in unledgered:
        open_items.append("unledgered value: " + token + " appears in the golden but in no claim")
    demonstrated = any(c["result"] == "INCORRECT" for c in claims.values())
    demonstrated |= any(r["result"] == "FAIL" for r in requirements.values())
    demonstrated |= any(c["result"] == "FAIL" for c in checks.values())
    demonstrated |= any(c["result"] == "FAIL" for c in chronology["comparisons"])
    demonstrated |= any(c["result"] == "FAIL" for c in alternatives["branches"])
    for req in requirements.values():
        demonstrated |= req["valid_case"]["result"] == "REJECT" or req["wrong_case"]["result"] == "ACCEPT"
    unresolved = any(c["result"] == "UNRESOLVED" for c in claims.values())
    unresolved |= any(r["result"] == "UNRESOLVED" or not r["verification"]["complete"] for r in requirements.values())
    unresolved |= any(c["result"] == "UNRESOLVED" for c in checks.values())
    unresolved |= not chronology["complete"] or not alternatives["complete"]
    unresolved |= any(c["result"] == "UNRESOLVED" for c in chronology["comparisons"] + alternatives["branches"])
    unresolved |= any(req[name]["result"] == "UNRESOLVED" for req in requirements.values() for name in ("valid_case", "wrong_case"))
    unresolved |= any("inaccessible" in item or "unresolved" in item or "unledgered" in item for item in open_items)
    verdict = "FAIL" if demonstrated else "NON-FAIL" if open_items else "PASS"
    calculated = dict(verdict=verdict, verdict_score=5 if verdict == "PASS" else None,
                      execution_status="PARTIAL" if unresolved else "COMPLETE")
    if mismatch:
        # A wrong-task artifact is not graded: BLOCKED, routed upstream, never PASS.
        open_items.append("artifact_match: MISMATCH - the golden does not answer this prompt")
        calculated = dict(verdict="NON-FAIL", verdict_score=None, execution_status="BLOCKED")
    if passing:
        require(not open_items, "failed/unresolved evidence prevents PASS: " + "; ".join(open_items))
    return {**calculated, **{k: receipt[k] for k in BINDING}, "review_record_sha256": digest(content.encode("utf-8")),
            "review_requirements": len(requirements), "review_claims": len(claims),
            "review_open_items": open_items, "defect_classes": defect_classes, "repair_owners": repair_owners,
            "unledgered_values": unledgered, "integrity_override": receipt.get("integrity_override"),
            "artifact_match": match["result"], "prompt_overlap": receipt.get("prompt_overlap")}


def approve_report(root, parsed):
    if parsed.get("review_policy") != POLICY:
        raise ValueError("Golden PASS requires the current evidence record; historical PASS text is not a new audit.")
    path = local(root, RECORD)
    if not path.is_file():
        raise ValueError("Golden PASS requires a saved golden-review evidence record.")
    record = validate_record(root, path.read_text(encoding="utf-8"), passing=parsed["verdict"] == "PASS")
    if any(parsed.get(k) != record[k] for k in BINDING + ("review_record_sha256",)):
        raise ValueError("Golden report does not match the reviewed answer/context/record; recheck the current audit.")
    for key in ("verdict", "verdict_score", "execution_status"):
        if parsed.get(key) != record[key]:
            raise ValueError("Golden report contradicts recorded findings: " + key)
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["start"])
    parser.add_argument("--answer", help="Saved golden input mapping; default is 08_Golden_Answer.md")
    parser.add_argument("--draft", action="store_true", help="Audit an already existing explicitly requested draft; never create it")
    parser.add_argument("--accept-ending", metavar="REASON",
                        help="Override only the sentence-ending integrity check for a golden that legitimately ends on a list item; recorded in the receipt")
    args = parser.parse_args()
    try:
        result = start_review(Path(__file__).resolve().parents[2], args.answer, args.draft, args.accept_ending)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
