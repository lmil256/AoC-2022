opponent_moves = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
move_beats = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
move_beaten_by = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
move_scores = {'rock': 1, 'paper': 2, 'scissors': 3}
draw_score = 3
win_score = 6
total = 0

with open('input.txt') as infile:
    for line in infile:
        opponent_move = opponent_moves[line[0]]
        if line[2] == 'X':
            player_move = move_beats[opponent_move]
        elif line[2] == 'Y':
            player_move = opponent_move
            total += draw_score
        else:
            player_move = move_beaten_by[opponent_move]
            total += win_score
        total += move_scores[player_move]


print(total)
