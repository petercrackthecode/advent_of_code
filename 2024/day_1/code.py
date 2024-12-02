# https://adventofcode.com/2023/day/1
# importing the sys module
# appending the directory of read_txt_from_file.py in the sys.path list
import sys
import os
from collections import Counter

# Get the absolute path of the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, '../lib')

sys.path.append(lib_dir)
from utils import read_txt_from_file

def print_lines(lines):
	print(f'[\n{lines}\n]')


def solve(lines: str) -> None:
	# Part 1
	'''
	- Format each line to get the left and right numbers. Then, save the numbers respectively into each list.
	- Sort both the lists ascendingly.
	- Go thru each list index by index, then find the absolute gap between 2 numbers.
	'''
	left_list: List[int]  = []
	right_list: List[int] = []

	ans_1: int = 0

	for line in lines:
		left, right = [int(num_str) for num_str in line.split(' ') if bool(num_str)]
		left_list.append(left)
		right_list.append(right)
	
	left_list.sort()
	right_list.sort()

	for i in range(min(len(left_list), len(right_list))):
		dist: int = abs(right_list[i] - left_list[i])
		ans_1 += dist		

	print(f'part 1\' ans_1 = {ans_1}')
	
	# Part 2
	'''
	- Get the number frequencies within the right list.
	- Loop thru each number on the left list:
		- Count the number of times this number appears on the right list via the dictionary.
		- Multiply the frequency with this current number, then add to ans.
	- Return ans. 
	'''
	ans_2: int = 0

	right_freq: Counter[int] = Counter(right_list)
	
	for num in left_list:
		num_freq: int = right_freq[num]
		ans_2 += (num * num_freq)

	print(f'part 2\'s ans_2 = {ans_2}')		
	
FILE_PATH = 'input_p1.txt'
ABSOLUTE_FILE_PATH = os.path.abspath(FILE_PATH)
lines = [s for s in ''.join(read_txt_from_file(ABSOLUTE_FILE_PATH)).split('\n') if s != '']

# print('output = ', output)
# print_lines(lines) 

# output = ""
# print('output = ', output)

if __name__ == "__main__":
	solve(lines)
