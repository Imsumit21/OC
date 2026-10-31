"""Bind factual checks to primary evidence in both rubric review routes."""
from hg_rubric_facts import validate_facts
from hg_source_checks import prepare_facts, guard_absence


def checked_facts(review, criterion, reader, known, root, context, **options):
    # options: literal_tokens=True for the rubric review only (other stages keep the default).
    result = validate_facts(prepare_facts(review, known, root, context), criterion, reader, known, **options)
    return guard_absence(result, review, reader, known, root, context)
