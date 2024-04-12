# https://adventofcode.com/2023/day/4
# importing the sys module
# appending the directory of read_txt_from_file.py in the sys.path list
import re
import sys
import os
from typing import List, Set, Tuple

# Get the absolute path of the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, "../lib")

sys.path.append(lib_dir)
from utils import read_txt_from_file

FILE_PATH = "input.txt"
ABSOLUTE_FILE_PATH = os.path.abspath(FILE_PATH)
inp = [
    s for s in "".join(read_txt_from_file(ABSOLUTE_FILE_PATH)).split("\n") if s != ""
]


def get_numbers(line: str) -> Tuple[Set[int], Set[int]]:
    pattern = (
        r"Card\s+\d+:\s+(?P<winning_nums>(?:\d+\s+)+)\|\s+(?P<our_nums>(?:\d+\s*)+)"
    )

    winning_nums, our_nums = (
        re.match(pattern, line).groupdict()["winning_nums"],
        re.match(pattern, line).groupdict()["our_nums"],
    )
    # print(f"winning_nums = {winning_nums}")
    # print(f"our_nums = {our_nums}")
    winning_nums = set([int(x) for x in winning_nums.split(" ") if x.strip() != ""])
    our_nums = set([int(x) for x in our_nums.split(" ") if x.strip() != ""])

    return winning_nums, our_nums


def get_total_points_on_cards(inp: List[str]) -> int:
    """
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53  -> 4 matched cards (83, 86, 17, 48) -> 2^(4-1) = 8
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19  -> 2 matched cards (61, 32) -> 2^(2-1) = 2
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1  -> 2 matched cards (1, 21) -> 2^(2-1) = 2
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83  -> 1 matched card (84) -> 2^(1-1) = 1
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36  -> 0 matched cards
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11  -> 0 matched cards

    - ans:int = 0
    - loop through each line of input:
        - via a helper function called get_numbers(line: str) -> Tuple[Set[int], Set[int]] to get the 2 sets of winning
        numbers and our numbers: winning_nums, our_nums = get_numbers(line)
        - count the intersections between two sets: matched_cards = len(winning_nums.intersection(our_nums))
        - if match_cards > 0:
            - add 2**(matched_cards - 1) to ans
    - return ans
    """
    ans: int = 0

    for line in inp:
        winning_nums, our_nums = get_numbers(line)
        matched_cards: int = len(winning_nums.intersection(our_nums))
        if matched_cards > 0:
            ans += 2 ** (matched_cards - 1)

    return ans


if __name__ == "__main__":
    ans: int = get_total_points_on_cards(inp)
    print(f"ans = {ans}")
