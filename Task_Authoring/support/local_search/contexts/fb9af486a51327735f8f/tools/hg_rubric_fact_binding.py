"""Bind factual checks to primary evidence in both rubric review routes."""
from hg_rubric_facts import validate_facts
from hg_source_checks import prepare_facts, guard_absence


def checked_facts(review, criterion, reader, known, root, context):
    result = validate_facts(prepare_facts(review, known, root, context), criterion, reader, known)
    return guard_absence(result, review, reader, known, root, context)
