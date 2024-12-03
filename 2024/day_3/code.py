# https://adventofcode.com/2024/day/2
# importing the sys module
# appending the directory of read_txt_from_file.py in the sys.path list
import sys
import os
import re
from typing import List, Optional, Tuple

# Get the absolute path of the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, "../lib")

sys.path.append(lib_dir)
from utils import read_txt_from_file  # noqa


def print_lines(lines):
    print(f"[\n{lines}\n]")



def solve(lines: List[str]) -> None:
    """
    - use regular expression to fetch the valid mul(x,y) statements:
    - we should join the line

    pattern = r"mul\((\d+),(\d+)\)"
    text = ''.join(lines)
    
    - use re.findall(pattern, text) to get all the matches [('123', '456'), etc.]
    - loop thru each numbers (x,y) within groups (converted them from strings to int firts), then add
    the multiplication of x & y to ans
    """
    ans_1: int = 0

    pattern = r"mul\((\d+),(\d+)\)"
    text = ''.join(lines)

    groups: List[Tuple[str, str]] = re.findall(pattern, text)

    for x_str, y_str in groups:
        x, y = int(x_str), int(y_str)

        ans_1 += (x * y)

    print(f'ans_1 = {ans_1}')

    '''
    012345678910111213141516171819202122232425262728
    xmul(2,4)& m u l [ 3 , 7 ] ! ^ d o n ' t ( ) _ m u l ( 5 , 5 ) + m u l (32,64](mul(11,8)undo()?mul(8,5))

    - save the matches & their start indices
    - loop thru finditer to find the group and the start idx:
        - get the full str: match.group(). Then, fetch x & y from that str using match:
        - save the tuple (x, y, start_idx) to mult_list
    - use regex to find the `do()` and `don't()` strings and their start indices (in the format of (do()/don't(), start_idx)). Save them to another list called flags
                    0           1
    mult_list = [(2, 4, 1), (3, 7, 10)]
                                            i
                                            j
    flags = [("do()", -1), ("don't()", 4), ("do()", 8)]

    is_doing: bool = True

    ans = 0 + (2 * 4) = 8 

    - loop: i = 0 -> len(mult_list) - 1:
        - keep moving j while in_bound and flags's start_idx is greater than mult_list's start idx:
            - is_doing = flags[j][0] == "do()"
        - if doing, do the multiplication & add to ans.
    '''
    #                    (x, y, start_idx)
    mult_list: List[Tuple[int, int, int]] = []
    #           ("do()"/"don't()", start_idx)
    flags: List[Tuple[str, int]] = []
    flag_pattern: str = r"do(?:n't)?\(\)"
    ans_2: int = 0

    for match in re.finditer(pattern, text):
        x_str, y_str = match.groups()
        x, y = int(x_str), int(y_str)
        start_idx: int = match.start()

        mult_list.append((x, y, start_idx))

    for match in re.finditer(flag_pattern, text):
        flag_str: str=  match.group()
        start_idx: int = match.start()

        flags.append((flag_str, start_idx))

    j: int = 0
    is_doing: bool = True

    for (x, y, start_idx) in mult_list:
        while j < len(flags) and flags[j][1] < start_idx:
            is_doing = flags[j][0] == 'do()'
            j += 1

        if is_doing:
            ans_2 += (x * y)

    print(f'ans_2 = {ans_2}')



    


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
