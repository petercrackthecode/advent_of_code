# https://adventofcode.com/2023/day/5
# importing the sys module
# appending the directory of read_txt_from_file.py in the sys.path list
import re
import sys
import os
from typing import Dict, List, Set, Tuple

# Get the absolute path of the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, "../lib")

sys.path.append(lib_dir)
from utils import read_txt_from_file

FILE_PATH = "part_1_input.txt"
ABSOLUTE_FILE_PATH = os.path.abspath(FILE_PATH)
inp:List[str] = read_txt_from_file(ABSOLUTE_FILE_PATH)

'''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2 -> [50, 51] and [98, 99]
52 50 48 -> [52..99] and [50..97] 79 -> 77

soil-to-fertilizer map:
0 15 37 -> [0..36] and [15..51]
37 52 2 -> [37..38] and [52..53]
39 0 15 -> [39..53] and [0..14] 77 -> 77

fertilizer-to-water map:
49 53 8 -> [49..56] and [53..60]
0 11 42 -> [0..41] and [11..52]
42 0 7  -> [42..48] and [0..6]
57 7 4  -> [57..60] and [7..10] 77 -> 77

water-to-light map:
88 18 7 -> [88..94] and [18..24]
18 25 70 -> [18..87] and [25..94] 77 -> 84

light-to-temperature map:
45 77 23
81 45 19 -> [81..99] and [45..63] 84 -> 48
68 64 13

temperature-to-humidity map:
0 69 1 -> 
1 0 69 -> [1..69] and [0..68] 48 -> 47

humidity-to-location map:
60 56 37 
56 93 4
'''

''' ALGORITHM
- split the input by double newlines ('\n\n'). call that splitted_input: = ''.join(inp).split('\n\n')
- read all the seeds from the first element within splitted_input, read all the seeds & save them to the array seeds:
seeds:List[int] = get_seeds(splitted_input[0])
- have a list of maps called converters: converters:List[Dict[int, int]] = []
- loop from index i = 1 to 7:
  - populate_maps(converters[i-1], splitted_input[i])
- have a variable called lowest_loc:float = float('inf')
- loop for every seed within seeds:
  - curr_loc = get_location(seed)
  - lowest_loc = min(lowest_loc, curr_loc)

- return int(lowest_loc)
'''

''' CONTEXT
Any source numbers that aren't mapped correspond to the same destination number. 
So, seed number 10 corresponds to soil number 10.

7 maps in total.
- Given a list of seeds, return the lowest location number generated from one of those
seed.
'''
# seeds: 79 14 55 13
def min_location(inp: str) -> int:
  splitted_input:List[str] = ''.join(inp).split('\n\n')
  # print(f"''.join(inp) = {''.join(inp)}\n")
  # print(f'splitted_input = {splitted_input}\n')

  def get_seeds(seed_input: str) -> List[int]:
    # seeds: 79 14 55 13
    if not bool(seed_input.strip()):
      return []
    
    seeds_str:str = seed_input.split(':')[1].strip()

    return [int(seed_str) for seed_str in seeds_str.split(' ') if bool(seed_str.strip())]

  def populate_maps(converter:Dict[int, int], inp: str) -> None:
    '''
    seed-to-soil map:
    50 98 2
    52 50 48
    '''
    lines:List[str] = inp.split('\n')
    rules:List[str] = lines[1:]

    for rule in rules:
      stats:List[int] = [int(stat_str) for stat_str in rule.strip().split(' ') if bool(stat_str.strip())]
      dest, source, _range = stats
      for offset in range(_range):
        converter[source + offset] = dest + offset


  seeds:List[int] = get_seeds(splitted_input[0])

  converters:List[Dict[int, int]] = [dict() for _ in range(7)]
  for i in range(1, 8):
    populate_maps(converters[i-1], splitted_input[i])

  def get_location(seed:int) -> int:
    nonlocal converters
    
    for converter in converters:
      seed = converter.get(seed, seed)  

    return seed

  min_loc:float = float('inf')

  # for converter in converters:
  #   print(f'converter = {converter}\n')

  for seed in seeds:
    curr_loc:int = get_location(seed)
    # print(f'seed = {seed}, location = {curr_loc}\n')
    min_loc = min(min_loc, curr_loc)
    # break

  return int(min_loc)


if __name__ == "__main__":
  ans:int = min_location(inp)
  print(f'ans = {ans}')