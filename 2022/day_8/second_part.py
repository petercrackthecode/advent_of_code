# importing the sys module
import sys
import os
from typing import Deque, List, Set, DefaultDict, Tuple
from collections import defaultdict, deque

# appending the directory of read_txt_from_file.py in the sys.path list
sys.path.append('../lib')

from utils import read_txt_from_file

FILE_PATH = './input.txt'
ABSOLUTE_FILE_PATH = os.path.abspath(FILE_PATH)

def get_tree_scenic_score(coord: Tuple[int], matrix: List[List[int]]) -> int:
  [row, col] = [len(matrix), len(matrix[0])]
  (r, c) = coord

  current_tree_height = matrix[r][c]
  # scenic scores from 4 positions
  [top, bottom, left, right] = [0 for _ in range(4)]

  # check above:
  [y, x] = [r-1, c]
  while y >= 0:
    if matrix[y][x] >= current_tree_height:
      if matrix[y][x] == current_tree_height:
        top += 1
      break
    y -= 1
    top += 1

  # check below:
  [y, x] = [r+1, c]
  while y < row:
    if matrix[y][x] >= current_tree_height:
      if matrix[y][x] == current_tree_height:
        bottom += 1
      break
    y += 1
    bottom += 1

  # check left:
  [y, x] = [r, c-1]
  while x >= 0:
    if matrix[y][x] >= current_tree_height:
      if matrix[y][x] == current_tree_height:
        left += 1
      break
    x -= 1
    left += 1
  
  # check right:
  [y, x] = [r, c+1]
  while x < col:
    if matrix[y][x] >= current_tree_height:
      if matrix[y][x] == current_tree_height:
        right += 1
      break
    x += 1
    right += 1

  return top * bottom * left * right

full_input = ''.join(read_txt_from_file(ABSOLUTE_FILE_PATH)).strip().split('\n')
# print('full_input = ', full_input)

tree_height_matrix = []
for row_str in full_input:
  char_list = [ch for ch in row_str]
  row_numbers = [int(num_char) for num_char in char_list]
  tree_height_matrix.append(row_numbers)

[MAX_ROW, MAX_COL] = [len(tree_height_matrix), len(tree_height_matrix[0])]

highest_scenic_score = 0

# starting from 1 and ending 1 index early since we ignore the trees on the edges.
for r in range(1, MAX_ROW-1):
  for c in range(1, MAX_COL-1):
    current_tree_scenic_score = get_tree_scenic_score((r, c), tree_height_matrix)
    highest_scenic_score = max(highest_scenic_score, current_tree_scenic_score)

print("highest_scenic_score = ", highest_scenic_score)
