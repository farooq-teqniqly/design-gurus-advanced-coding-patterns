from collections import Counter
from typing import Callable, Dict, List


def count_letter_frequencies(
    input_str: str, counter_func: Callable[[str], Dict[str, int]]
) -> dict:
    return counter_func(input_str)


def counter_counter_func(input_str: str) -> Dict[str, int]:
    return Counter(input_str)


def dict_counter_func(input_str: str) -> Dict[str, int]:
    histogram = {}

    for ch in input_str:
        histogram[ch] = histogram.get(ch, 0) + 1

    return histogram


def get_total_max_frequencies(nums: List[int]) -> int:
    c = Counter(nums)
    frequencies = c.most_common()
    max_frequency = frequencies[0][1]
    total = max_frequency

    for num, frequency in frequencies[1:]:
        if frequency == max_frequency:
            total += frequency

    return total
