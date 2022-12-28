# importing the sys module
import sys
import os
from typing import Deque, List, Set, DefaultDict, Tuple

# appending the directory of read_txt_from_file.py in the sys.path list
sys.path.append("../lib")

from utils import read_txt_from_file

FILE_PATH = "./input.txt"
ABSOLUTE_FILE_PATH = os.path.abspath(FILE_PATH)

moves = "".join(read_txt_from_file(ABSOLUTE_FILE_PATH)).strip().split("\n")
# print('moves = ', moves)

# knots is a list of 10 elements, whose each represents the position (row, column) of a knot in the rope
# from head to tail
knots = [[0, 0] for _ in range(10)]

"""
.....
.....
..T..
.....
.....
"""
def are_two_points_adjacent(first_point: List[int], second_point: List[int]) -> bool:
  [first_point_row, first_point_col] = first_point
  [second_point_row, second_point_col] = second_point
  return (
    # right above or right below
    (abs(first_point_row - second_point_row) == 1 and first_point_col == second_point_col) or
    # next-to on the left or next-to on the right
    (abs(first_point_col - second_point_col) == 1 and first_point_row == second_point_row) or
    # diagonal by 1 unit
    (abs(first_point_col - second_point_col) == 1 and abs(first_point_row - second_point_row) == 1)
  )

def up_by_2_units(first_point: List[int], second_point: List[int]) -> bool:
  [first_point_row, first_point_col] = first_point
  [second_point_row, second_point_col] = second_point
  return (first_point_col == second_point_col and first_point_row == second_point_row - 2) 

def down_by_2_units(first_point: List[int], second_point: List[int]) -> bool:
  [first_point_row, first_point_col] = first_point
  [second_point_row, second_point_col] = second_point
  return (first_point_col == second_point_col and first_point_row == second_point_row + 2) 

def left_by_2_units(first_point: List[int], second_point: List[int]) -> bool:
  [first_point_row, first_point_col] = first_point
  [second_point_row, second_point_col] = second_point
  return (first_point_row == second_point_row and first_point_col == second_point_col - 2)

def right_by_2_units(first_point: List[int], second_point: List[int]) -> bool:
  [first_point_row, first_point_col] = first_point
  [second_point_row, second_point_col] = second_point
  return (first_point_row == second_point_row and first_point_col == second_point_col + 2)

def in_top_left_quarter(first_point: List[int], second_point: List[int]) -> bool:
  [first_point_row, first_point_col] = first_point
  [second_point_row, second_point_col] = second_point
  return (
    (first_point_row == second_point_row - 1 and first_point_col == second_point_col - 2) or
    (first_point_row == second_point_row - 2 and first_point_col == second_point_col - 2) or
    (first_point_row == second_point_row - 2 and first_point_col == second_point_col - 1)
  )

def in_top_right_quarter(first_point: List[int], second_point: List[int]) -> bool:
  [first_point_row, first_point_col] = first_point
  [second_point_row, second_point_col] = second_point
  return (
    (first_point_col == second_point_col + 2 and first_point_row == second_point_row - 1) or 
    (first_point_col == second_point_col + 2 and first_point_row == second_point_row - 2) or 
    (first_point_col == second_point_col + 1 and first_point_row == second_point_row - 2)
  )

def in_bottom_left_quarter(first_point: List[int], second_point: List[int]) -> bool:
  [first_point_row, first_point_col] = first_point
  [second_point_row, second_point_col] = second_point
  return (
    (first_point_col == second_point_col - 2 and first_point_row == second_point_row + 1) or 
    (first_point_col == second_point_col - 1 and first_point_row == second_point_row + 2) or 
    (first_point_col == second_point_col - 2 and first_point_row == second_point_row + 2)
  )

def in_bottom_right_quarter(first_point: List[int], second_point: List[int]) -> bool:
  [first_point_row, first_point_col] = first_point
  [second_point_row, second_point_col] = second_point
  return (
    (first_point_col == second_point_col + 2 and first_point_row == second_point_row + 1) or 
    (first_point_col == second_point_col + 2 and first_point_row == second_point_row + 2) or 
    (first_point_col == second_point_col + 1 and first_point_row == second_point_row + 2)
  )

def move_dependent_knot(lead_knot: List[int], dependent_knot: List[int]) -> None:
  if up_by_2_units(lead_knot, dependent_knot):
    dependent_knot[0] -= 1
  elif down_by_2_units(lead_knot, dependent_knot):
    dependent_knot[0] += 1
  elif left_by_2_units(lead_knot, dependent_knot):
    dependent_knot[1] -= 1
  elif right_by_2_units(lead_knot, dependent_knot):
    dependent_knot[1] += 1
  elif in_top_left_quarter(lead_knot, dependent_knot):
    dependent_knot[0] -= 1
    dependent_knot[1] -= 1
  elif in_top_right_quarter(lead_knot, dependent_knot):
    dependent_knot[0] -= 1
    dependent_knot[1] += 1
  elif in_bottom_left_quarter(lead_knot, dependent_knot):
    dependent_knot[0] += 1
    dependent_knot[1] -= 1
  elif in_bottom_right_quarter(lead_knot, dependent_knot):
    dependent_knot[0] += 1
    dependent_knot[1] += 1

def execute_move(direction: str, steps_count: int, knots: List[List[int]], all_tail_positions: Set[Tuple[int]]) -> None:
  head_knot = knots[0]
  after_head_knot = knots[1]
  while steps_count > 0:
    if direction == 'U':
      # move up 1 step => row -= 1
      head_knot[0] -= 1
    elif direction == "D":
      # move down 1 step => row += 1
      head_knot[0] += 1
    elif direction == "L":
      # move left 1 step => column -= 1
      head_knot[1] -= 1
    elif direction == "R":
      # move right 1 step => column += 1
      head_knot[1] += 1

    if not head_knot == after_head_knot and not are_two_points_adjacent(head_knot, after_head_knot):
      move_dependent_knot(head_knot, after_head_knot)
      # check and possibly move the knots after the first 2 knots
      for index in range(1, len(knots) - 1):
        current_knot = knots[index]
        next_knot = knots[index+1]
        move_dependent_knot(current_knot, next_knot)
      tail_knot = knots[-1]
      all_tail_positions.add((tail_knot[0], tail_knot[1]))


    steps_count -= 1

# initialize with the start position of (0, 0)
all_tail_positions = set([(0, 0)])


for move in moves:
  [direction, step] = move.split(' ')
  steps_count = int(step)
  execute_move(direction, steps_count, knots, all_tail_positions)
# print('len(all_tail_positions) = ', len(all_tail_positions))
print('knots = ', knots)


