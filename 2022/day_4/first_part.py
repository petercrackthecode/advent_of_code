# https://adventofcode.com/2022/day/4
import os

INPUT_FILE_NAME = 'input.txt'


def does_one_range_fully_contain_the_other(range_1, range_2):
    (start_1, end_1) = range_1
    (start_2, end_2) = range_2
    return (start_1 <= start_2 and end_2 <= end_1) or (start_2 <= start_1 and end_1 <= end_2)


def get_tuple_from_number_range(range):
    range_array = range.split('-')
    return (int(range_array[0]), int(range_array[1]))


with open(os.path.join('.', INPUT_FILE_NAME), 'r') as file:
    content = file.read(100)
    full_input = []
    while len(content) > 0:
        full_input.extend(content)
        content = file.read(100)
    pairs = ''.join(full_input).split('\n')[:-1]
    fully_contained_ranges_count = 0
    for pair in pairs:
        [first_elf_range, second_elf_range] = pair.split(',')
        first_elf_range_tuple = get_tuple_from_number_range(first_elf_range)
        second_elf_range_tuple = get_tuple_from_number_range(second_elf_range)
        if does_one_range_fully_contain_the_other(first_elf_range_tuple, second_elf_range_tuple):
            fully_contained_ranges_count += 1

    print('fully_contained_ranges_count = ', fully_contained_ranges_count)
