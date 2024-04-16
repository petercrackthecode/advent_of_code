# https://adventofcode.com/2023/day/4
# importing the sys module
# appending the directory of read_txt_from_file.py in the sys.path list
from collections import defaultdict
import sys
import os
from typing import DefaultDict, List, Set

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

'''
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53 -> matched = 48, 83, 86, 17 (4 cards) 
                                                 -> win 1 copy of cards 2, 3 (4, 5), 4, 5
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19 -> matched = 61, 32 (2 cards)
                                                 -> win 1 copy of cards 3 (4, 5), 4
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1 -> matched = 21, 1 (2 cards)
                                                 -> 4 cards 3
                                                 -> win 4 copies of card 4, 5
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83 -> 10 cards 4
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11


Card             1
          /          \      \  \
       2,              3,     4, 5
     /   \            / \    /
    3     4          4   5  5
   / \   /          /
  4  5  5          5
 /
5

Card              2
                /    \
               3      4
              / \    /
             4   5  5
            /
           5

Card             3
                / \
               4   5
              /
             5

Card             4 | extra_cards[4] = 2
                /
                5

Card             5

Card             6

- The parent cards are the original
- The children cards are the copies.

Card      |  1      |  2  |  3  | 4 | 5  | 6  | 
Matched   |  4      |  2  |  2  | 1 | 0  | 0  |
Count     |  1      |  2  |  4  | 8 | 14 | 1  |
Children  |2,3,4,5  | 3,4 | 4,5 | 5 |    |    |

* ALGO:
- have a variable called count:int = 0 to keep track of the final result
- have a dictionary called extra_cards:DefaultDict[int, int] where given a card, returns the total cards added by that card (inclusively).
- card = len(inp)
- loop thru the list reversely to count the graph: while card > 0:
  - line = inp[card-1]
  - initialize the curr_count by 1
  - calculate the number of matches: matches = get_match(line)
  - loop: for i from 1 -> matches (inclusively):
      - incremeent curr_count by extra_cards[card+i]
  - extra_cards[card] = curr_count
  - increment count by extra_cards[card]
  - decrement card by 1

- return count


4: 4+2+1+1=8
5: 1+ 4 + 8 + 1 = 13
(Cards will never make you copy a card past the end of the table.)
Total card: 30

Card      |  1      |  2  |  3  | 4 | 5  | 6  | 
Matched   |  4      |  2  |  2  | 1 | 0  | 0  |
Count     |  1      |  2  |  4  | 8 | 14 | 1  |
Children  |2,3,4,5  | 3,4 | 4,5 | 5 |    |    |

* ALGO:
- have a variable called count:int = 0 to keep track of the final result
- have a dictionary called extra_cards:DefaultDict[int, int] where given a card, returns the total cards added by that card (inclusively).
- card = len(inp)
- loop thru the list reversely to count the graph: while card > 0:
  - line = inp[card-1]
  - initialize the curr_count by 1
  - calculate the number of matches: matches = get_matches(line)
  - loop: for i from 1 -> matches (inclusively):
      - incremeent curr_count by extra_cards[card+i]
  - extra_cards[card] = curr_count
  - increment count by extra_cards[card]
  - decrement card by 1

- return count
'''

'''
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53 -> matched = 48, 83, 86, 17 (4 cards) 
                                                 -> win 1 copy of cards 2, 3 (4, 5), 4, 5
'''
def get_matches(line: str) -> int:
    cards_str:str = line.split(':')[1].strip()
    winning_cards_str, our_cards_str = cards_str.split('|')

    winning_cards:Set[int] = set([int(card) for card in winning_cards_str.strip().split(' ') if bool(card)])
    our_cards:Set[int] = set([int(card) for card in our_cards_str.strip().split(' ') if bool(card)])

    return len(winning_cards.intersection(our_cards))

def get_total_scratchcards(inp: List[str]) -> int:
    count:int = 0
    extra_cards:DefaultDict[int, int] = defaultdict(int)
    card = len(inp)

    while card > 0:
        line:str = inp[card-1]
        curr_count:int = 1
        matches = get_matches(line)
        for i in range(1, matches+1):
            curr_count += extra_cards[card+i]

        extra_cards[card] = curr_count
        count += extra_cards[card]
        card -= 1

    return count


if __name__ == "__main__":
    ans: int = get_total_scratchcards(inp)
    print(f"ans = {ans}")
