# https://adventofcode.com/2024/day/2
# importing the sys module
# appending the directory of read_txt_from_file.py in the sys.path list
import sys
import os
import re
from typing import List, Optional, Set, Tuple

# Get the absolute path of the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, "../lib")

sys.path.append(lib_dir)
from utils import read_txt_from_file  # noqa


def print_lines(lines):
    print(f"[\n{lines}\n]")



def solve(lines: List[str]) -> None:
    """
    - words can be:
        - horizontal
        - vertical
        - diagonal
        - written backward
        - overlapping with other words

    ..X...
    .SAMX.
    .A..A.
    XMAS.S
    .X....

    ....XXMAS.
    .SAMXMS...
    ...S..A...
    ..A.A.MS.X
    XMASAMX.MM
    X.....XA.A
    S.S.S.S.SS
    .A.A.A.A.A
    ..M.M.M.MM
    .X.X.XMASX

    - loop thru each letter in our lines: for each character of 'X', check if we can form a word 'XMAS' by:
        - looking upward.
        - looking downward.
        - looking to the left on the same row.
        - looking to the right on the same row.

    - In either of the case above: if we can form the word, increment ans_1 by 1
    """
    ans_1: int = 0
    
    max_row: int = len(lines)
    max_col: int = len(lines[0])

    def is_inbound(row: int, col: int) -> bool:
        nonlocal max_row, max_col

        return 0 <= row < max_row and 0 <= col < max_col

    def can_form(row: int, col: int, row_transform: int, col_transform: int):
        nonlocal lines
        search_word: List[str] = ['X', 'M', 'A', 'S']

        for letter in search_word:
            if not is_inbound(row, col) or lines[row][col] != letter:
                return False
            # move upward on the same col
            row += row_transform
            col += col_transform
        
        return True

    transform_coords = [
        [-1, 0], # upward
        [1, 0], # downward
        [0, -1], # left
        [0, 1], # right
        [-1, -1], # top left
        [-1, 1], # top right
        [1, -1], # bottom left
        [1, 1] # bottom right
    ]

    for row in range(max_row):
        for col in range(max_col):
            if lines[row][col] == 'X':
                for row_transform, col_transform in transform_coords:
                    if can_form(row, col, row_transform, col_transform):
                        ans_1 += 1

    print(f'ans_1 = {ans_1}')

    ans_2: int = 0
    '''
    - find two MAS in the shape of an X
    - within the X, each MAS can be written forwards or backwards.

    M.S
    .A.
    M.S

    . M . S . . . . . .
    . . A . . M S M S .
    . M . S . M A A . .
    . . A . A S M S M .
    . M . S . M . . . .
    . . . . . . . . . .
    S . S . S . S . S .
    . A . A . A . A . .
    M . M . M . M . M .
    . . . . . . . . . .

    - loop: for row = 0..max_row - 3:
        - for col = 0..max_col - 3:
            - check if we can form the word "MAS" or "SAM" from top left to bottom right:
                - if yes: check if we can form the word "MAS" or "SAM" at (row + 2, col):
                    - if yes: increment ans_2 by 1
    '''
    for row in range(max_row - 2):
        for col in range(max_col - 2):
            topleft_bottomright_word: str = f'{lines[row][col]}{lines[row+1][col+1]}{lines[row+2][col+2]}'
            if topleft_bottomright_word in ("MAS", "SAM"):
                bottomleft_topright_word: str = f'{lines[row + 2][col]}{lines[row + 1][col+1]}{lines[row][col+2]}'
                if bottomleft_topright_word in ("MAS", "SAM"):
                    ans_2 += 1

    print(f"ans_2 = {ans_2}")


    


FILE_PATH = "input_p1.txt"
ABSOLUTE_FILE_PATH = os.path.abspath(FILE_PATH)
lines = [
    s for s in "".join(read_txt_from_file(ABSOLUTE_FILE_PATH)).split("\n") if s != ""
]

# print('output = ', output)
# print_lines(lines)

# output = ""
# print('output = ', output)

if __name__ == "__main__":
    solve(lines)
