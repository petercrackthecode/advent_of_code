# importing the sys module
import sys
import os
from typing import List, Tuple

# appending the directory of read_txt_from_file.py in the sys.path list
sys.path.append('../lib')

from utils import read_txt_from_file

FILE_PATH = './input.txt'
ABSOLUTE_FILE_PATH = os.path.abspath(FILE_PATH)

def is_tree_visible(coord: Tuple[int], matrix: List[List[int]]) -> bool:
  [row, col] = [len(matrix), len(matrix[0])]
  (r, c) = coord

  current_tree_height = matrix[r][c]
  # check above:
  [y, x] = [r-1, c]
  while y >= 0:
    if matrix[y][x] >= current_tree_height:
      break
    y -= 1
  if y < 0:
    return True

  # check below:
  [y, x] = [r+1, c]
  while y < row:
    if matrix[y][x] >= current_tree_height:
      break
    y += 1
  if y >= row:
    return True

  # check left:
  [y, x] = [r, c-1]
  while x >= 0:
    if matrix[y][x] >= current_tree_height:
      break
    x -= 1
  if x < 0:
    return True
  
  # check right:
  [y, x] = [r, c+1]
  while x < col:
    if matrix[y][x] >= current_tree_height:
      break
    x += 1
  if x >= row:
    return True

  return False

full_input = ''.join(read_txt_from_file(ABSOLUTE_FILE_PATH)).strip().split('\n')
# print('full_input = ', full_input)

tree_height_matrix = []
for row_str in full_input:
  char_list = [ch for ch in row_str]
  row_numbers = [int(num_char) for num_char in char_list]
  tree_height_matrix.append(row_numbers)

[MAX_ROW, MAX_COL] = [len(tree_height_matrix), len(tree_height_matrix[0])]

# since all trees on the edges are visible, we initialize our count with those trees' number.
visible_trees_count = MAX_ROW*2 + (MAX_COL-2)*2

# starting from 1 and ending 1 index early since we ignore the trees on the edges.
for r in range(1, MAX_ROW-1):
  for c in range(1, MAX_COL-1):
    if is_tree_visible((r, c), tree_height_matrix):
      visible_trees_count += 1

print("visible_trees_count = ", visible_trees_count)


