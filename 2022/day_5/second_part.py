

# https://adventofcode.com/2022/day/5
import os
import re
from collections import deque

INPUT_FILE_NAME = 'input.txt'


def put_crates_to_stacks(crate_line, crates_stacks):
    index = 0
    stack_index = 0
    while index < len(crate_line):
        char = crate_line[index]
        if char == '[':
            crate = crate_line[index+1]
            crates_stacks[stack_index].appendleft(crate)
        index += 4
        stack_index += 1


def move_crates(crates_stacks, number_of_crates, from_stack_index, to_stack_index):
    from_stack = crates_stacks[from_stack_index-1]
    to_stack = crates_stacks[to_stack_index-1]
    temp_stack = deque()
    while number_of_crates > 0 and len(from_stack) > 0:
        crate = from_stack.pop()
        temp_stack.appendleft(crate)
        number_of_crates -= 1
    to_stack.extend(temp_stack)


with open(os.path.join('.', INPUT_FILE_NAME), 'r') as file:
    content = file.read(100)
    full_input = []
    while len(content) > 0:
        full_input.extend(content)
        content = file.read(100)
    [diagram, moves] = ''.join(full_input).split('\n\n')
    crates_indices = diagram.split('\n')[-1].strip()
    crates_line_length = len(diagram.split('\n')[-1])
    stacks_count = int(re.split('\s+', crates_indices)[-1])
    moves = moves.strip().split('\n')
    crates_stacks = [deque() for _ in range(stacks_count)]
    for crate_line in diagram.split('\n')[:-1]:
        put_crates_to_stacks(crate_line, crates_stacks)

    for move in moves:
        moves_components = move.split(' ')
        [number_of_crates, from_stack_index, to_stack_index] = [
            int(moves_components[1]), int(moves_components[3]), int(moves_components[-1])]
        move_crates(crates_stacks, number_of_crates,
                    from_stack_index, to_stack_index)
    final_top_crate_combo = []
    for stack in crates_stacks:
        if len(stack) > 0:
            top = stack.pop()
            final_top_crate_combo.append(top)
    print("final_top_crate_combo = ", ''.join(final_top_crate_combo))
