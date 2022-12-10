

# https://adventofcode.com/2022/day/6
import os
from typing import List

INPUT_FILE_NAME = 'input.txt'


def has_repeated_character(char_list: List[str]) -> bool:
    unique_char = set()
    for char in char_list:
        if char in unique_char:
            return True
        unique_char.add(char)
    return False


with open(os.path.join('.', INPUT_FILE_NAME), 'r') as file:
    content = file.read(100)
    full_input = []
    while len(content) > 0:
        full_input.extend(content)
        content = file.read(100)
    for index in range(len(full_input) - 13):
        sub_str_char_list = full_input[index:index+14]
        if not has_repeated_character(sub_str_char_list):
            print('the number of character processed is ', index + 14)
            break
