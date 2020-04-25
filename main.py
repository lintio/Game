current_game = [[1, 2, 3],
                [4, 0, 6],
                [7, 8, 9]]

# Tie
tie_check = []
for row in range(len(current_game)):
    for col in range(len(current_game)):
        tie_check.append(current_game[row][col])
if 0 not in tie_check:
    print("The game is a tie nobody won")
    