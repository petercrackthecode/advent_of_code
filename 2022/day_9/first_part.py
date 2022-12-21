# importing the sys module
import sys
import os
from typing import Deque, List, Set, DefaultDict, Tuple

# appending the directory of read_txt_from_file.py in the sys.path list
sys.path.append("../lib")

from utils import read_txt_from_file

FILE_PATH = "./input.txt"
ABSOLUTE_FILE_PATH = os.path.abspath(FILE_PATH)

moves = "".join(read_txt_from_file(ABSOLUTE_FILE_PATH)).strip().split("\n")
