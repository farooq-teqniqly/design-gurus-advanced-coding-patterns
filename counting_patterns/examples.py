from typing import Dict, List


def count_letter_frequencies(input_str: str) -> Dict[str, int]:
    histogram = {}

    for ch in input_str:
        histogram[ch] = histogram.get(ch, 0) + 1

    return histogram


def get_total_max_frequencies(nums: List[int]) -> int:
    frequencies = {}

    for n in nums:
        frequencies[n] = frequencies.get(n, 0) + 1

    max_frequency = 0
    sum_of_max_frequency = 0

    for _, frequency in frequencies.items():
        if frequency > max_frequency:
            max_frequency = frequency
            sum_of_max_frequency += frequency
        elif frequency == max_frequency:
            sum_of_max_frequency += frequency

    return sum_of_max_frequency


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


def min_steps_to_make_array_unique(nums: List[int]) -> int:
    max_value = -1

    for n in nums:
        if n > max_value:
            max_value = n

    frequencies = [0] * (len(nums) + max_value)

    for n in nums:
        frequencies[n] += 1

    min_moves = 0

    for i, n in enumerate(frequencies):
        if n <= 1:
            continue

        excess = frequencies[i] - 1
        frequencies[i + 1] += excess
        min_moves += excess

    return min_moves
