# https://adventofcode.com/2022/day/3
import os

INPUT_FILE_NAME = 'first_part_input.txt'


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
    for items in rucksacks_items:
        [first_compartment, second_compartment] = get_two_parts_of_a_rucksack(
            items)
        first_compartment_items = set(first_compartment)
        second_compartment_items = set(second_compartment)
        for item in second_compartment_items:
            if item in first_compartment_items:
                priorities_sum += get_item_priority(item)
    print('priorities_sum = ', priorities_sum)
