def count_letter_frequencies(input_str: str, counter_func) -> dict:
    return counter_func(input_str)


def counter_counter_func(input_str: str) -> dict:
    from collections import Counter

    return Counter(input_str)


def dict_counter_func(input_str: str) -> dict:
    histogram = {}

    for ch in input_str:
        histogram[ch] = histogram.get(ch, 0) + 1

    return histogram
