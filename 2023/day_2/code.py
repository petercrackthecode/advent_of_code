# https://adventofcode.com/2023/day/2
# importing the sys module
import sys
import os
from typing import List
import re

# Get the absolute path of the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, "../lib")

sys.path.append(lib_dir)

# appending the directory of read_txt_from_file.py in the sys.path list
from utils import read_txt_from_file

FILE_PATH = "part_1_input.txt"
ABSOLUTE_FILE_PATH = os.path.abspath(FILE_PATH)
inp = [s for s in "".join(read_txt_from_file(ABSOLUTE_FILE_PATH)).split("\n") if s != ""]


"""
THe bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes.

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green | T
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue | T
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red | F
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red | F
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green | T

what makes a game possible?

each game has a few turns. At each turn, each subset of cubes has to be smaller than or equal to 12 red, 13 green, and 14 blue. 

return the sum of the IDs of the possible games: int
"""


def get_cubes(s: str) -> List[int]:
    red = green = blue = 0
    cubes_info_idx = s.find(":")
    cubes_info = s[cubes_info_idx + 1 :].strip()
    # print(f'cubes_info = |{cubes_info}|')
    bags = [s for s in cubes_info.split(";") if s != ""]
    for bag in bags:
        cubes = [x.strip() for x in bag.split(",") if x.strip() != ""]
        for cube in cubes:
            stats = cube.split(" ")
            # print('stats = ', stats)
            [count, cube_type] = [int(stats[0]), stats[1]]
            if cube_type == "blue":
                blue += count
            elif cube_type == "red":
                red += count
            else:  # cube_type == 'green'
                green += count

    return [red, green, blue]


def cube_conundrum_p1(inp: str = inp):
    """
    - have a variable called ans:int = 0
    - Read the input line by line:
        - get the game Id & convert it to an integer & save it to a variable called gameId
        - get the cubes subsets.
        - check if all the cube combos in the subset is valid: have a helper function called is_subset_valid(subset: str) -> bool to do so:
            - Yes: Add the game Id to ans
    - return ans
    """
    RED_CUBES, GREEN_CUBES, BLUE_CUBES = 12, 13, 14
    ans = 0
    # need a better method in getting the game Id
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    pattern = r"Game (?P<game_id>\d+): (?P<cube_subsets>.+)"

    def is_game_valid(cube_subsets: str) -> bool:
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green | T
        subsets = [
            subset.strip() for subset in cube_subsets.strip().split(";") if subset.strip() != ""
        ]

        for subset in subsets:
            red, blue, green = 0, 0, 0
            cube_types = [
                cube_type.strip() for cube_type in subset.split(",") if bool(cube_type.strip())
            ]
            for cube_type in cube_types:
                count_str, _type = cube_type.split(" ")
                count: int = int(count_str)
                if _type.lower() == "blue":
                    blue = count
                elif _type.lower() == "green":
                    green = count
                elif _type.lower() == "red":
                    red = count

            if red > RED_CUBES or green > GREEN_CUBES or blue > BLUE_CUBES:
                return False

        return True

    for line in inp:
        match_obj = re.match(pattern, line)

        if not match_obj:
            return None

        game_id, cube_subsets = (
            int(match_obj.groupdict()["game_id"]),
            match_obj.groupdict()["cube_subsets"],
        )
        if is_game_valid(cube_subsets):
            ans += game_id

    return ans


def cube_conundrum_p2(inp: str) -> None:
    """
    - for each game, get the minimum number of red, blue, green cubes to make the game possible:
        - iterate thru each turn:
            - get the maximum value of red, green, blue and assign them to the current game's min_red, min_green, min_blue
    - multiply those min red, green, blue numbers
    - add those multipies together. return the total sum.

    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green | 4 red, 2 green, 6 blue => 48
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue | 1 red, 3 green, 4 blue => 12
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red | 20 red, 13 green, 6 blue => 1560
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red | 14 red, 3 green, 15 blue => 630
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green | 6 red, 3 green, 2 blue => 36
    """
    ans: int = 0
    pattern = r"Game \d+: (?P<cube_subsets>.+)"

    def get_multiply(cube_subsets: str) -> int:
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green | T
        subsets = [
            subset.strip() for subset in cube_subsets.strip().split(";") if subset.strip() != ""
        ]

        min_red = 0
        min_green = 0
        min_blue = 0

        for subset in subsets:
            cube_types = [s.strip() for s in subset.split(",") if s.strip() != ""]
            for cube_type in cube_types:
                # 3 blue, 4 red
                count_str, color = cube_type.split(" ")
                count: int = int(count_str)

                if color.lower() == "red":
                    min_red = max(min_red, count)
                elif color.lower() == "blue":
                    min_blue = max(min_blue, count)
                elif color.lower() == "green":
                    min_green = max(min_green, count)

        return (
            (min_red if min_red > 0 else 1)
            * (min_green if min_green > 0 else 1)
            * (min_blue if min_blue > 0 else 1)
        )

    for line in inp:
        match_obj = re.match(pattern, line)

        if not match_obj:
            return None

        cube_subsets = match_obj.groupdict()["cube_subsets"]

        ans += get_multiply(cube_subsets)

    return ans


output = cube_conundrum_p2(inp)
print("output = ", output)
