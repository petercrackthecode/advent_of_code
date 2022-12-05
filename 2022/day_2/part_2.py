import os

convert_score = {
    'A': 1,
    'B': 2,
    'C': 3
}

with open(os.path.join('.', 'input.txt'), 'r') as file:
    content = file.read(100)
    full_input = []
    while len(content) > 0:
        full_input.extend(content)
        content = file.read(100)
    matches = ''.join(full_input).split('\n')[:-1]
    final_score = 0
    all_moves = ['A', 'B', 'C']
    for match in matches:
        [opponent_move, result] = match.split(' ')
        opponent_move_index = all_moves.index(opponent_move)
        # draw by default
        my_move = opponent_move
        if result == 'X':
            # lose
            my_move = all_moves[(opponent_move_index-1) % 3]
        elif result == 'Z':
            # win
            my_move = all_moves[(opponent_move_index+1) % 3]
        base_score = convert_score[my_move]
        match_score = 0 if result == 'X' else (3 if result == 'Y' else 6)
        final_score += (base_score + match_score)

    print('final_score = ', final_score)
