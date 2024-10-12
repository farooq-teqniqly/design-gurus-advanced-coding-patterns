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


def get_max_population_year(
    logs: List[List[int]], start_year: int, end_year: int
) -> int:
    population = [0] * (end_year - start_year + 1)

    for birth_year, death_year in logs:
        population[birth_year - start_year] += 1
        population[death_year - start_year] -= 1

    current_pop = 0
    max_pop = 0
    max_index = 0

    for i, p in enumerate(population):
        if p == 0:
            continue
        current_pop += p

        if current_pop > max_pop:
            max_pop = current_pop
            max_index = i

    return start_year + max_index
