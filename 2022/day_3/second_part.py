# https://adventofcode.com/2022/day/3
import os

INPUT_FILE_NAME = 'input.txt'


def get_item_priority(item):
    is_upper_case = item.isupper()
    item = item.lower()
    return (ord(item) - ord('a') + 1) + (26 if is_upper_case else 0)


def get_two_parts_of_a_rucksack(items):
    half_length = len(items) // 2
    first_compartment = items[:half_length]
    second_compartment = items[half_length:]

    return [first_compartment, second_compartment]


with open(os.path.join('.', INPUT_FILE_NAME), 'r') as file:
    content = file.read(100)
    full_input = []
    while len(content) > 0:
        full_input.extend(content)
        content = file.read(100)
    rucksacks_items = ''.join(full_input).split('\n')[:-1]
    priorities_sum = 0
    number_of_items = len(rucksacks_items)
    for index in range(0, number_of_items, 3):
        [first_elf, second_elf, third_elf] = [rucksacks_items[index],
                                              rucksacks_items[index+1], rucksacks_items[index+2]]
        first_elf_distinct_items = set(first_elf)
        second_elf_distinct_items = set(second_elf)
        third_elf_distinct_items = set(third_elf)
        dinstict_item = first_elf[0]
        for item in first_elf_distinct_items:
            if item in second_elf_distinct_items and item in third_elf_distinct_items:
                distinct_item = item

        priorities_sum += get_item_priority(distinct_item)

    print('priorities_sum = ', priorities_sum)
