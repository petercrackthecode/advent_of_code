# https://adventofcode.com/2023/day/3
# importing the sys module
from collections import deque
import sys
import os
from typing import Deque, List, Set, Tuple
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
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

46714114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592..*..
......755.  755 * 58
...$.*....
.664.598..  755 * 598?
"""


def calc_gear_ratios(inp: List[str]) -> int:
    """
    - loop thru each row r and each column c in inp to see if inp[r][c] is equal to '*':
      - yes:
        - call the function get_nearby_parts(r, c) -> List[int] to get list of all numbers representing nearby parts.
        nearby_parts = get_nearby_parts(r, c)
        - if the length of nearby_parts is exactly 2. add the power of two numbers within nearby_parts to ans:
          - ans += (nearby_parts[0] & nearby_parts[1])
    """
    ans: int = 0

    def get_nearby_parts(row: int, col: int) -> List[int]:
        nonlocal inp
        ans: List[int] = []

        # save the positions of the digits surrounding our '*' gear
        digits_pos: Set[Tuple[int, int]] = set()
        # get digits from top:
        if row - 1 >= 0:
            for c in range(col - 1, col + 2):
                if 0 <= c < len(inp[row - 1]):
                    if inp[row - 1][c].isdigit():
                        digits_pos.add((row - 1, c))
        # get the digit on the left:
        if col - 1 >= 0 and inp[row][col - 1].isdigit():
            digits_pos.add((row, col - 1))
        # get the digit on the right:
        if col + 1 < len(inp[row]) and inp[row][col + 1].isdigit():
            digits_pos.add((row, col + 1))
        # get the digits at the bottom
        if row + 1 < len(inp):
            for c in range(col - 1, col + 2):
                if 0 <= c < len(inp[row + 1]):
                    if inp[row + 1][c].isdigit():
                        digits_pos.add((row + 1, c))

        # have a set to saved the checked positions of the digits
        checked_pos: Set[Tuple[int, int]] = set()

        def get_part_num(row: int, col: int) -> int:
            nonlocal checked_pos, inp
            checked_pos.add((row, col))
            digits: Deque[str] = deque([inp[row][col]])
            # 617*......
            left_c = col - 1
            right_c = col + 1

            while (
                left_c >= 0
                and inp[row][left_c].isdigit()
                and (row, left_c) not in checked_pos
            ):
                checked_pos.add((row, left_c))
                digits.appendleft(inp[row][left_c])
                left_c -= 1

            while (
                right_c < len(inp[row])
                and inp[row][right_c].isdigit()
                and (row, right_c) not in checked_pos
            ):
                checked_pos.add((row, right_c))
                digits.append(inp[row][right_c])
                right_c += 1

            return int("".join(digits))

        for r, c in digits_pos:
            if not (r, c) in checked_pos:
                part_num = get_part_num(r, c)
                ans.append(part_num)

        return ans

    for r in range(len(inp)):
        for c in range(len(inp[0])):
            if inp[r][c] == "*":
                nearby_parts = get_nearby_parts(r, c)
                if len(nearby_parts) == 2:
                    ans += nearby_parts[0] * nearby_parts[1]

    return ans


if __name__ == "__main__":
    gear_ratios: int = calc_gear_ratios(inp)

    print(f"gear_ratios = {gear_ratios}")
