# importing the sys module
import sys
import os
from typing import Deque, List, Set, DefaultDict
from collections import defaultdict, deque

# appending the directory of read_txt_from_file.py in the sys.path list
sys.path.append('../lib')

from utils import read_txt_from_file

"""
Edge case: different directories can share the same names, as long as they are in different paths.
=> We have to save the absolute path of the directory.
We have to memoize the size of files using absolute paths as well.

+ size_lookup = defaultdict()
  key: the absolute path to the directory/file.
  value: the directory/file's size

+ directory_children_lookup = defaultdict()
  key: the absolute path to the directory
  value: the absolute paths of the folders & files that are the direct children of the current directory- list of strings

+ directory_abs_path = set():
  contains all the strings that serve as the absolute path of all directories under our tree.

+ go through all the commands from the input to build our tree structure. Save all the files' sizes to size_lookup. Save the children of a certain
folder to directory_children_lookup. 
+ Starting from the main directory, go through all the children again:
  current_directory_size = 0
  - if the child is a file: current_directory_size += size_lookup(file_absolute_name)
  - if the child is a folder:
      if not folder_absolute_path in size_lookup:
        get_directory_size(folder_absolute_path)
      current_directory_size += size_lookup(folder_absolute_path)
+ Iterate through every folder path in directory_abs_path:
    current_folder_size = size_lookup(a_directory_abs_path)
    if current_folder_size < 100000:
      sum += current_folder_size
+ print out sum
"""

# parse the input
"""
+ Use the dollar sign ($) as a delimeter for each command.
+ For the path, have a deque acting as a stack call current_path_stack to keep track of the current directory we are at.
"""

def cd(current_path_stack: Deque[str], target_directory: str, directory_abs_path: Set[str]) -> None:
  if target_directory == '..' and len(current_path_stack) > 0:
    current_path_stack.pop()
  else:
    current_path_stack.append(target_directory)

  abs_path = '/'.join(current_path_stack)[1:] if len(current_path_stack) > 1 else '/'
  directory_abs_path.add(abs_path)

def ls(current_path_stack: Deque[str], directory_content: List[str], size_lookup: DefaultDict, directory_children_lookup: DefaultDict) -> None:
  abs_path = '/'.join(current_path_stack)[1:] if len(current_path_stack) > 1 else '/'
  for content in directory_content:
    name = content.split(' ')[1]
    new_abs_path = f'{abs_path}/{name}' if abs_path != '/' else f'/{name}'
    if content[:3] != 'dir':
      # a file => gotta calculate the size
      size = int(content.split(' ')[0])
      size_lookup[new_abs_path] = size
    directory_children_lookup[abs_path].append(new_abs_path)

def calculate_directory_size(abs_path: str, size_lookup: DefaultDict, directory_children_lookup: DefaultDict) -> None:
  current_directory_size = 0

  children = directory_children_lookup[abs_path]
  for child in children:
    if not child in size_lookup:
      # a folder that we haven't calculate the size yet
      calculate_directory_size(child, size_lookup, directory_children_lookup)
    current_directory_size += size_lookup[child]

  size_lookup[abs_path] = current_directory_size

FILE_PATH = './input.txt'
ABSOLUTE_FILE_PATH = os.path.abspath(FILE_PATH)

full_input = ''.join(read_txt_from_file(ABSOLUTE_FILE_PATH)).strip()
# print('full_input = ', full_input)

commands = [command.strip() for command in full_input.split('$')[1:]]
# print('commands = ', commands)

# set the default size of every file or directory to be 0
size_lookup = defaultdict(int)
# every directory has 0 children by default
directory_children_lookup = defaultdict(list)

directory_abs_path = set()

current_path_stack = deque()

for command in commands:
  if command[:2] == 'cd':
    target_directory = command.split(' ')[1]
    cd(current_path_stack, target_directory, directory_abs_path)
  else:
    # command[:2] == 'ls'
    directory_content = command.split('\n')[1:]
    ls(current_path_stack, directory_content, size_lookup, directory_children_lookup)

# print(directory_children_lookup)
main_directory = '/'
calculate_directory_size(main_directory, size_lookup, directory_children_lookup)

under_100000_size_directories_sum = 0
for path in directory_abs_path:
  size = size_lookup[path]
  if size < 100_000:
    under_100000_size_directories_sum += size

print('under_100000_size_directories_sum = ', under_100000_size_directories_sum)

  