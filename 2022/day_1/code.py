import os
import heapq


def get_total_weight_from_weight_str(weight_str: str) -> int:
    weights = weight_str.split('\n')[:-1]
    ans = 0
    for weight in weights:
        ans += int(weight)
    return ans


with open(os.path.join('.', 'input.txt'), 'r') as file:
    content = file.read(100)
    full_input = []
    while len(content) > 0:
        full_input.extend(content)
        content = file.read(100)
    cleaned_up_input = []
    for index, char in enumerate(full_input):
        if char == '\n' and (index == 0 or full_input[index-1] == '\n'):
            cleaned_up_input.append('|')
        else:
            cleaned_up_input.append(char)
    elves_carried_weights_str = ''.join(cleaned_up_input).split('|')
    elves_total_carried_weight = []

    for weight_str in elves_carried_weights_str:
        elves_total_carried_weight.append(
            get_total_weight_from_weight_str(weight_str))

    heapq.heapify(elves_total_carried_weight)
    print(sum(heapq.nlargest(3, elves_total_carried_weight)))
