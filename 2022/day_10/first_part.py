# importing the sys module
import sys
import os
from typing import Deque, List, Set, DefaultDict, Tuple

# appending the directory of read_txt_from_file.py in the sys.path list
sys.path.append("../lib")

from utils import read_txt_from_file

FILE_PATH = "./input.txt"
ABSOLUTE_FILE_PATH = os.path.abspath(FILE_PATH)

operations = "".join(read_txt_from_file(ABSOLUTE_FILE_PATH)).strip().split("\n")
# print('operations = ', operations)
"""
+ Calculate the total number of cycles through noop and addx: number_of_cycles
 - if operation == noop: number_of_cycles += 1
 - elif operation == addx: number_of_cycles += 2

"""
total_number_of_cycles = 0
for operation in operations:
  if operation[:4] == 'noop':
    total_number_of_cycles += 1
  elif operation[:4] == 'addx':
    total_number_of_cycles += 2
X_at_the_start_of_a_cycle = [1]

for operation in operations:
  last_X = X_at_the_start_of_a_cycle[-1]
  if operation[:4] == 'noop':
    X_at_the_start_of_a_cycle.append(last_X)
  elif operation[:4] == 'addx':
    addx_value = int(operation.split(' ')[1])
    X_at_the_start_of_a_cycle.append(last_X)
    X_at_the_start_of_a_cycle.append(last_X + addx_value)
print('X_at_the_start_of_a_cycle = ', X_at_the_start_of_a_cycle)

signal_strength_sum = 0

# offset the indices in the X_at_the_start_of_a_cycle list by 1 since we start counting from 0
to_be_calculated_signal_strength_points = [20, 60, 100, 140, 180, 220]
for point in to_be_calculated_signal_strength_points:
  signal_strength_sum += (X_at_the_start_of_a_cycle[point-1] * point)
  print(f"X_at_the_start_of_a_cycle[{point-1}] = ", X_at_the_start_of_a_cycle[point-1])
print('signal_strength_sum = ', signal_strength_sum)


