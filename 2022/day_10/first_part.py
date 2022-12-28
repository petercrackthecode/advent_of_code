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
X_at_a_cycle = [0 for _ in range(total_number_of_cycles)]

