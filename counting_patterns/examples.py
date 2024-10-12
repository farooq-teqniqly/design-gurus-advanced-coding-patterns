from typing import Callable, Dict


def count_letter_frequencies(
    input_str: str, counter_func: Callable[[str], Dict[str, int]]
) -> dict:
    return counter_func(input_str)


def counter_counter_func(input_str: str) -> Dict[str, int]:
    from collections import Counter

    return Counter(input_str)


def dict_counter_func(input_str: str) -> Dict[str, int]:
    histogram = {}

    for ch in input_str:
        histogram[ch] = histogram.get(ch, 0) + 1

    return histogram
