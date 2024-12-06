# https://adventofcode.com/2024/day/2
# importing the sys module
# appending the directory of read_txt_from_file.py in the sys.path list
from collections import defaultdict
import sys
import os
import re
from typing import DefaultDict, List, Optional, Set, Tuple

# Get the absolute path of the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, "../lib")

sys.path.append(lib_dir)
from utils import read_txt_from_file  # noqa


def print_lines(lines):
    print(f"[\n{lines}\n]")



def solve(first_page_lines: List[str], remaining_lines: List[str]) -> None:
    """
    - find the middle number of each correct page.
    - X|Y: page X must locate before page Y.

    # given a page, returns the pages staying after that page
    pages_after = {
      61: {13, 53, 29},
      75: {29, 53, 47, 61, 13},
      47: {53, 13, 61, 29},
      53: {29, 13},
      29: {13}
    }

    75 47 61 53 29
    i

    - nums[i] = 75
    - nums[i+1] = 47

    - nums[i] must not exist within pages_after[nums[i + 1]]

    """
    ans_1: int = 0
    ans_2: int = 0

    pages_after: DefaultDict[int, Set[int]] = defaultdict(set)

    def is_correct(nums: List[int]) -> bool:
        nonlocal pages_after
        
        for i in range(len(nums) - 2, -1, -1):
            curr_page, next_page = nums[i], nums[i+1]
            if curr_page in pages_after[next_page]:
                return False
        
        return True
    
    def reorder(nums: List[int]) -> None:
        nonlocal pages_after

        '''
        pages_after = {
          61: {13, 53, 29},
          75: {29, 53, 47, 61, 13},
          47: {53, 13, 61, 29},
          53: {29, 13},
          29: {13},
          97: {13, 61, 47, 29, 53, 75}
        }

        75 97 47 61 53
           i
        nums[i] = 97
        nums[i+1] = 47

        97 75 13 47 29
            i

        nums[i] = 29
        nums[i+1] = 47
        '''
        # every time we violate the rules within pages_after, swap nums[i] and nums[i+1]
        # bubble sort- after each inner loop, the page with the highest priority will rank first
        for until_page in range(len(nums) - 1): # until len(nums) - 2
            for i in range(len(nums) - 2, until_page - 1, -1):
                curr_page, next_page = nums[i], nums[i+1]
                if curr_page in pages_after[next_page]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
    
    # initialize pages_after
    for line in first_page_lines:
        before_page_str, after_page_str = line.split('|')
        before_page, after_page = int(before_page_str), int(after_page_str)

        pages_after[before_page].add(after_page)

    # loop thru each line within the remaining page & to find if each line is valid
    for line in remaining_lines:
        nums: List[int] = [int(num_str) for num_str in line.split(',') if num_str.strip() != '']
        if is_correct(nums):
            # 0, 1, 2, 3, 4
            mid_idx: int = len(nums) // 2
            ans_1 += nums[mid_idx]
        else: # reorder the pages so that it's in the correct order
            # print(f'nums before reorder = {nums}')
            reorder(nums)
            # print(f'nums after reorder = {nums}\n')
            # 0, 1, 2, 3, 4
            mid_idx: int = len(nums) // 2
            ans_2 += nums[mid_idx]

    print(f'ans_1 = {ans_1}')
    print(f"ans_2 = {ans_2}")


    


FILE_PATH = "input_p1.txt"
ABSOLUTE_FILE_PATH = os.path.abspath(FILE_PATH)
first_page, remaining_pages = "".join(read_txt_from_file(ABSOLUTE_FILE_PATH)).split('\n\n')

first_page_lines: List[str] = [line for line in first_page.split('\n') if line != '']
remaining_lines: List[str] = [line for line in remaining_pages.split('\n') if line != '']

lines = [
    s for s in "".join(read_txt_from_file(ABSOLUTE_FILE_PATH)).split("\n") if s != ""
]

# print('output = ', output)
# print_lines(lines)

# output = ""
# print('output = ', output)

if __name__ == "__main__":
    solve(first_page_lines, remaining_lines)
