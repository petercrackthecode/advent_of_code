# https://adventofcode.com/2024/day/2
# importing the sys module
# appending the directory of read_txt_from_file.py in the sys.path list
import sys
import os
from typing import List, Optional

# Get the absolute path of the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, "../lib")

sys.path.append(lib_dir)
from utils import read_txt_from_file  # noqa


def print_lines(lines):
    print(f"[\n{lines}\n]")


def is_safe_level(nums: List[int]) -> bool:
    is_asc: Optional[bool] = None

    # print(f"nums = {nums}")

    for i in range(1, len(nums)):
        curr_num, prev_num = nums[i], nums[i - 1]
        diff: int = abs(curr_num - prev_num)

        if diff < 1 or diff > 3:
            # print(f'curr_num = {curr_num}, prev_num = {prev_num}, is_asc = {is_asc}')
            # print("not safe")
            return False
        if is_asc == None:
            is_asc = curr_num > prev_num
        else:
            if (is_asc and curr_num < prev_num) or (not is_asc and curr_num > prev_num):
                # print(f'curr_num = {curr_num}, prev_num = {prev_num}, is_asc = {is_asc}')
                # print("not safe")
                return False

    # print("safe")

    return True

def is_safe_after_dampened(nums: List[int]) -> bool:
    for ignored_idx in range(len(nums)):
        new_nums: List[int] = nums[:ignored_idx] + nums[ignored_idx+1:]
        if is_safe_level(new_nums):
            return True
        
    return False


def solve(lines: List[str]) -> None:
    """
    - Count the number of safe levels.
    - safe condition for a level:
        - the numbers are strictly increasing or decreasing.
        - two adjacent number only differ by at most three.

            i
    7 6 4 2 1 | desc | 1

    1 2 7 8 9 | asc  | 0
    9 7 6 2 1 | desc | 0

            i
    1 3 2 4 5 | rand | 0
    is_asc: Optional[bool] = None

    8 6 4 4 1 | rand | 0
    1 3 6 7 9 | asc  | 1

    ans = 2

    - loop thru each number starting at index 1 & see the gap between arr[i] and arr[i-1]:
        - if the gap (abs) is < 1 or > 3: skip this level.
        - otherwise:
                        - if is_asc is None: set is_asc = arr[i] > arr[i-1]
            - otherwise:
                - if (is_asc and arr[i] < arr[i-1]) or (not is_asc and arr[i] > arr[i-1]): skip this level.
                - otherwise: increment ans by 1 (safe level)

    Time: O(N * len(lines)) | N = the longest length of any line
    Space: O(1)
    """
    ans_1: int = 0
    for line in lines:
        nums: List[int] = [int(num)
                           for num in line.split(" ") if num.strip() != ""]
        if is_safe_level(nums):
            ans_1 += 1

    print(f"problem 1: ans = {ans_1}")

    """
    - removing a single level from an unsafe report will make it safe.
    - bruteforce: if a list is unsafe, check if there exists a safe list yielded by omitting a number 0..len(N)-1
    """
    ans_2: int = 0
    for line in lines:
        nums: List[int] = [int(num)
                           for num in line.split(" ") if num.strip() != ""]
        if is_safe_level(nums) or is_safe_after_dampened(nums):
            ans_2 += 1

    print(f"problem 2: ans = {ans_2}")


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
