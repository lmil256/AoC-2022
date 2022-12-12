opponent_moves = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
player_moves = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
move_beats = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
move_scores = {'rock': 1, 'paper': 2, 'scissors': 3}
draw_score = 3
win_score = 6
total = 0

with open('input.txt') as infile:
    for line in infile:
        opponent_move = opponent_moves[line[0]]
        player_move = player_moves[line[2]]
        if opponent_move == player_move:
            total += draw_score
        elif move_beats[player_move] == opponent_move:
            total += win_score
        total += move_scores[player_move]

print(total)
