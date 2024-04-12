# https://adventofcode.com/2023/day/3
# importing the sys module
import sys
import os
from typing import List
import re

# Get the absolute path of the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, "../lib")

# appending the directory of read_txt_from_file.py in the sys.path list
sys.path.append(lib_dir)

from utils import read_txt_from_file


FILE_PATH = "day_3/part_1_input.txt"
ABSOLUTE_FILE_PATH = os.path.abspath(FILE_PATH)
inp = [
    s for s in "".join(read_txt_from_file(ABSOLUTE_FILE_PATH)).split("\n") if s != ""
]

"""
     0123456789
     __________
0    467..114..
1    ...*......
2    ..35..633.
3    ......#...
4    617*......
5    .....+.58.
6    ..592.....
7    ......755.
8    ...$.*....
9    .664.598..

what if a number overflows? would a digit of that number be spanning onto the next row? 

we have to check the circumference area of a number to see if there is any character that is not period exists.

- for each number at row r spanning from columns c..(c+n):
  - if each of these coordinates exist, check coordinates from [r-1][c-1] to [r-1][c+n+1]: check top of the number
  - check the left side of the number (if exists): check coordinates [r][c-1]
  - check the right side of the number (if exists): check coordinates [r][c+n+1]
  - if each of these coordinates exist, check coordinates from [r+1][c-1] to [r+1][c+n+1]: check bottom of the number

  
- loop from each row in input:
    - set i = 0.
    - set the current row's length row_length = len(row)
    - set the current number = 0
    - have a variable to save the start column of the current number: start_col:int = -1
    - have a variable to save the end column of the current number: end_col:int = -1
    - loop while i < row_length:
        - if row[i] is not a digit:
            - call the helper function: if is_part_number(start_col, end_col, row) is True:
                - add current_number to our final answer.
            - reset start_col = -1, end_col = -1
            - reset current_number to be 0
        - otherwise, if row[i] is a digit:
            - if start_col is -1: assign start_col = i
            - end_col = i
            - assign: curr_num = (curr_num * 10) + int(row[i])
            - if i is the last index of the row:
                - call the helper function: if is_part_number(start_col, end_col, row) is True:
                    - add current_number to our final answer.
"""


def is_special_char(s: str) -> bool:
    return len(s) == 1 and s != "." and not s.isdigit()


def main():
    ans: int = 0

    def is_part_number(start_col: int, end_col: int, row: int) -> bool:
        if start_col == -1 or end_col == -1:
            return False

        # print(f"num = {inp[row][start_col:end_col+1]}")

        # check top
        if row - 1 >= 0:
            # check diagonally top-left:
            if start_col - 1 >= 0 and is_special_char(inp[row - 1][start_col - 1]):
                return True
            # check top
            for c in range(start_col, end_col + 1):
                if is_special_char(inp[row - 1][c]):
                    return True
            # check diagonally top-right:
            if end_col + 1 < len(inp[row]) and is_special_char(
                inp[row - 1][end_col + 1]
            ):
                return True

        # check left
        if start_col - 1 >= 0 and is_special_char(inp[row][start_col - 1]):
            return True
        # check right
        if end_col + 1 < len(inp[row]) and is_special_char(inp[row][end_col + 1]):
            return True

        # check bottom
        if row + 1 < len(inp):
            # check diagonally bottom-left:
            if start_col - 1 >= 0 and is_special_char(inp[row + 1][start_col - 1]):
                return True
            # check bottom
            for c in range(start_col, end_col + 1):
                if is_special_char(inp[row + 1][c]):
                    return True
            # check diagonally bottom-right:
            if end_col + 1 < len(inp[row]) and is_special_char(
                inp[row + 1][end_col + 1]
            ):
                return True

        return False

    for row, line in enumerate(inp):
        # print(f"line = {line}")
        curr_num: int = 0
        start_col: int = -1
        end_col: int = -1
        i: int = 0

        while i < len(line):
            # print(f"start_col = {start_col}")
            # print(f"end_col = {end_col}")
            if not line[i].isdigit():
                if curr_num > 0 and is_part_number(start_col, end_col, row):
                    # print(f"curr_num = {curr_num}")
                    ans += curr_num
                start_col = end_col = -1
                curr_num = 0
            else:  # line[i] is a digit
                start_col = i if start_col == -1 else start_col
                end_col = i
                curr_num = curr_num * 10 + int(line[i])
                if i == len(line) - 1:
                    if curr_num > 0 and is_part_number(start_col, end_col, row):
                        # print(f"curr_num = {curr_num}")
                        ans += curr_num

            i += 1
        # print()

    return ans


if __name__ == "__main__":
    ans: int = main()
    print(f"ans = {ans}")
