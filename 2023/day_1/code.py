# https://adventofcode.com/2023/day/1
# importing the sys module
# appending the directory of read_txt_from_file.py in the sys.path list
import sys
import os

# Get the absolute path of the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, '../lib')

sys.path.append(lib_dir)
from utils import read_txt_from_file




FILE_PATH = 'input_1.txt'
ABSOLUTE_FILE_PATH = os.path.abspath(FILE_PATH)
inp = [s for s in ''.join(read_txt_from_file(ABSOLUTE_FILE_PATH)).split('\n') if s != '']

def trebuchet_p1(inp=inp):
    ans = 0

    for s in inp:
        [first_digit, last_digit] = [None, None]
        for ch in s:
            if ch.isnumeric():
                digit = int(ch)
                if first_digit == None:
                    first_digit = digit
                last_digit = digit
        ans += (first_digit * 10) + last_digit

    return ans

def find_first_digit(s: str) -> int:
    first_digit = None
    first_digit_index = -1

    for i, ch in enumerate(s):
        if ch.isnumeric():
            digit = int(ch)
            first_digit = digit
            first_digit_index = i
            break
    digits_in_letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    letters_to_digit = {
       'one': 1, 
       'two': 2, 
       'three': 3, 
       'four': 4, 
       'five': 5, 
       'six': 6, 
       'seven': 7, 
       'eight': 8, 
       'nine': 9
    }
    for digit_letter in digits_in_letters:
        found_idx = s.find(digit_letter)
        if found_idx == -1:
            continue
        if found_idx < first_digit_index:
            first_digit_index = found_idx
            first_digit = letters_to_digit[digit_letter]
            

    return first_digit

def find_last_digit(s: str) -> int:
    last_digit = None
    last_digit_idx = len(s)
    for i, ch in reversed(list(enumerate(s))):
        if ch.isnumeric():
            digit = int(ch)
            last_digit = digit
            last_digit_idx = i
            break
        
    digits_in_letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    letters_to_digit = {
       'one': 1, 
       'two': 2, 
       'three': 3, 
       'four': 4, 
       'five': 5, 
       'six': 6, 
       'seven': 7, 
       'eight': 8, 
       'nine': 9
    }

    for digit_letter in digits_in_letters:
        found_idx = s.rfind(digit_letter)
        if found_idx == -1:
            continue
        if found_idx > last_digit_idx:
            last_digit_idx = found_idx
            last_digit = letters_to_digit[digit_letter]

    return last_digit
    

def trebuchet_p2(inp: str=inp):
    ans:int = 0
    for s in inp:
        first_digit = find_first_digit(s)
        last_digit = find_last_digit(s)
        ans += (first_digit * 10) + last_digit
    return ans

# output = trebuchet_p1(inp)
# print('output = ', output)
output = trebuchet_p2(inp)
print('output = ', output)
