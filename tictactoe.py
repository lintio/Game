import itertools

def win(current_game):

    def all_same(l, win_type):
        if l.count(l[0]) == len(l) and l[0] != 0:
            print(f"Player {l[0]} is the winner {win_type}!")
            return True
        else:
            return False


    # Horizontal
    for row in current_game:
        if all_same(row, "horizontally (-)"):
            return True
    # Diagonal /
    diags = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        diags.append(current_game[row][col])
    if all_same(diags, "diagonally (/)"):
        return True
    # Diagonal \
    diags = []
    for ix in range(len(current_game)):
        diags.append(current_game[ix][ix])
    if all_same(diags, "diagonally (\\)"):
        return True
    # Vertically
    for col in range(len(current_game)):
        check = []
        for row in current_game:
            check.append(row[col])
        if all_same(check, "Vertically (|)"):
            return True
    

    # Tie
    tie_check = []
    for row in range(len(current_game)):
        for col in range(len(current_game)):
            tie_check.append(current_game[row][col])
    if 0 not in tie_check:
        print("The game is a tie nobody won")
        return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This space has been taken, Please choode another!")
            return game_map, False
        print("   "+"  ".join(str(i) for i in range(len(game_map))))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e: 
        print("Error: did you input row/column as 0 1 or 2 ect?", e)
        return game_map, False


play = True
players = [1, 2]
while play:
    game_size = int(input("What size game of tic tac toe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    turns = game_size * game_size
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")
        played = False

        while not played:
            column_choice = int(input(f"What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again (y/n) ")
            if again.lower() == "y":
                print("Restarting...")
            elif again.lower() == "n":
                print("Goodbye!")
                play = False
            else:
                print("Not a valid answer, so exiting")
                play = False