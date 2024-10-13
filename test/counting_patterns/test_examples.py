import pytest

import counting_patterns.examples as cp
from counting_patterns.examples import min_increment_to_make_array_unique


@pytest.mark.parametrize(
    ("input_str", "want"),
    [
        ("hello", dict(h=1, e=1, l=2, o=1)),
        ("apple", dict(a=1, p=2, l=1, e=1)),
        ("mississippi", dict(m=1, i=4, s=4, p=2)),
    ],
)
def test_count_letter_frequencies_using_dict_returns_correct_histogram(input_str, want):
    got = cp.count_letter_frequencies(input_str)
    assert got == want


@pytest.mark.parametrize(
    ("nums", "want"),
    [
        ([3, 2, 2, 3, 1, 4], 4),
        ([5, 5, 5, 2, 2, 3], 3),
        ([7, 8, 8, 7, 9, 9], 6),
    ],
)
def test_get_total_max_frequencies(nums, want):
    got = cp.get_total_max_frequencies(nums)
    assert got == want


@pytest.mark.parametrize(
    ("logs", "want"),
    [
        (
            [
                [1980, 1990],
                [1975, 1985],
                [1985, 1995],
                [1990, 2000],
                [1999, 2020],
                [1994, 2032],
            ],
            1994,
        ),
        ([[1970, 1990], [1980, 2009], [1960, 1970], [1959, 1982]], 1980),
        ([[2000, 2010], [2005, 2015], [2010, 2020], [2015, 2025]], 2005),
    ],
)
def test_get_max_population_year(logs, want):
    got = cp.get_max_population_year(logs, 1950, 2050)
    assert want == got


@pytest.mark.parametrize(
    ("nums", "want"),
    [
        ([4, 3, 2, 2, 1, 4], 5),
        ([5, 5, 5, 5, 5], 10),
        ([1, 1, 1, 1, 2], 9),
    ],
)
def test_min_increment_to_make_array_unique(nums, want):
    got = min_increment_to_make_array_unique(nums)
    assert got == want
