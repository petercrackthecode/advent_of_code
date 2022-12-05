import os

convert_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

translated_moves = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}


def get_match_score(opponent_move, my_translated_move):
    if opponent_move == my_translated_move:
        return 3

    if opponent_move == 'A':
        if my_translated_move == 'B':
            return 6
        else:
            return 0
    elif opponent_move == 'B':
        if my_translated_move == 'C':
            return 6
        else:
            return 0
    else:
        # opponent_move = 'C'
        if my_translated_move == 'A':
            return 6
        else:
            return 0


with open(os.path.join('.', 'input.txt'), 'r') as file:
    content = file.read(100)
    full_input = []
    while len(content) > 0:
        full_input.extend(content)
        content = file.read(100)
    matches = ''.join(full_input).split('\n')[:-1]
    final_score = 0
    for match in matches:
        [opponent_move, my_move] = match.split(' ')
        my_translated_move = translated_moves[my_move]
        base_score = convert_score[my_move]
        match_score = get_match_score(opponent_move, my_translated_move)
        final_score += (base_score + match_score)

    print('final_score = ', final_score)
