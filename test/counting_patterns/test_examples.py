import pytest

import counting_patterns.examples as cp


@pytest.mark.parametrize(
    ("input_str", "want"),
    [
        ("hello", dict(h=1, e=1, l=2, o=1)),
        ("apple", dict(a=1, p=2, l=1, e=1)),
        ("mississippi", dict(m=1, i=4, s=4, p=2)),
    ],
)
def test_count_letter_frequencies_using_dict_returns_correct_histogram(input_str, want):
    got = cp.count_letter_frequencies(input_str, cp.dict_counter_func)
    assert got == want


@pytest.mark.parametrize(
    ("input_str", "want"),
    [
        ("hello", dict(h=1, e=1, l=2, o=1)),
        ("apple", dict(a=1, p=2, l=1, e=1)),
        ("mississippi", dict(m=1, i=4, s=4, p=2)),
    ],
)
def test_count_letter_frequencies_using_counter_returns_correct_histogram(
    input_str, want
):
    got = cp.count_letter_frequencies(input_str, cp.counter_counter_func)
    assert got == want
