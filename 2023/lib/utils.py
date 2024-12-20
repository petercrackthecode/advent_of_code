import os
from typing import List


def read_txt_from_file(input_path):
    full_input:List[str] = []
    with open(os.path.join('.', input_path), 'r') as file:
        content = file.read(100)
        while len(content) > 0:
            full_input.extend(content)
            content = file.read(100)
    return full_input
    
