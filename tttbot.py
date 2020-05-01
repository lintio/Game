import itertools, random, time, json


def make_dict(score, game):
    board = ''
    board_moves = []
    move_score = {}
    default_score = 5
    #moves = []

    def pick_move(score):
        moves = []
        aval_moves = dict.keys(score[board])
        aval_moves = list(aval_moves)
        aval_score = dict.values(score[board])
        aval_score = list(aval_score)
        for m in range(len(aval_moves)):
            for count in range(aval_score[m]):
                moves.append(aval_moves[m])
        random.shuffle(moves)
        try:
            next_move = random.choice(moves)
        except:
            next_move = ''
        return(next_move, score)

    for row in range(len(game)):
        for col in range(len(game)):
            board += str(game[row][col])

    if board in score:
        next_move, score = pick_move(score)
        return(next_move, score, board)
    elif board not in score:
        #find moves
        for r in range(len(game)):
            for c in range(len(game)):
                if game[r][c] == 0:
                    board_moves.append(str(c) + ':' + str(r))
        #add default score 5
        for move in board_moves:
            move_score[move] = default_score
        #build Dict
        score[board] = move_score
        next_move, score = pick_move(score)
        return(next_move, score, board)


def modify_score(score, game_won, Player_1_mm, Player_2_mm):
    if game_won == 1:
        board = dict.keys(Player_1_mm)
        board = list(board)
        for b in board:
            score[b][Player_1_mm[b]] +=1
        board = dict.keys(Player_2_mm)
        board = list(board)
        for b in board:
            if score[b][Player_2_mm[b]] > 1:
                score[b][Player_2_mm[b]] -=1
    elif game_won == 2:
        board = dict.keys(Player_2_mm)
        board = list(board)
        for b in board:
            score[b][Player_2_mm[b]] +=1
        board = dict.keys(Player_1_mm)
        board = list(board)
        for b in board:
            if score[b][Player_1_mm[b]] > 1:
                score[b][Player_1_mm[b]] -=1
    return(score)


def win(current_game):

    def all_same(l, win_type):
        if l.count(l[0]) == len(l) and l[0] != 0:
            player = l[0]
            print(f"Player {player} is the winner {win_type}!")
            return(player)
        else:
            player = 0
            return(player)


    # Horizontal
    for row in current_game:
        player = all_same(row, "horizontally (-)")
        if player != 0:
            return(player)
    # Diagonal /
    diags = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        diags.append(current_game[row][col])
    player = all_same(diags, "diagonally (/)")
    if player != 0:
        return(player)
    # Diagonal \
    diags = []
    for ix in range(len(current_game)):
        diags.append(current_game[ix][ix])
    player = all_same(diags, "diagonally (\\)")
    if player != 0:
        return(player)
    # Vertically
    for col in range(len(current_game)):
        check = []
        for row in current_game:
            check.append(row[col])
        player = all_same(check, "Vertically (|)")
        if player != 0:
            return(player)
    # Tie
    tie_check = []
    for row in range(len(current_game)):
        for col in range(len(current_game)):
            tie_check.append(current_game[row][col])
    if 0 not in tie_check:
        print("The game is a tie nobody won")
        return(3)

    return(0)


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
#score = {}
try:
    with open('data.json') as json_file: 
        score = json.load(json_file)
    json_file.close()
    #print(score)
except:
    score = {}
while play:
    #print(score)
    player = 0
    print('Key for moves in 3x3 \n[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]')
    print('Please select a game mode \n1) Human vs PC \n2) PC vs Human \n3) Human vs Human \n4) PC vs PC \n0) Exit ')
    game_mode = int(input('-> '))
    if game_mode == 0:
        with open('data.json', 'w') as fp:
            json.dump(score, fp,  indent=4)
        fp.close()
        print("Saved 'Score' Goodbye!")
        play = False
        continue
    moves = []
    game_size = int(input("What size game of tic tac toe (e.g. 3 = 3x3, 4 = 4x4)? "))
    if game_mode == 4:
        loop = int(input('how meny games? '))
    else:
        loop = 1
    for g in range(loop):
        game = [[0 for i in range(game_size)] for i in range(game_size)]
        for c in range(game_size):
            for r in range(game_size):
                moves.append(str(r) + ':' + str(c))
        game_won = 0
        game, _ = game_board(game, just_display=True)
        player_choice = itertools.cycle([1, 2])
        make_dict(score, game)
        Player_1_mm = {}
        Player_2_mm = {}
        while game_won == 0:
            current_player = next(player_choice)
            if game_mode == 1 and current_player == 2: # Human vs PC
                time.sleep(0.5)
                next_move, score, board = make_dict(score, game)
                print(f'Player {current_player} made move {next_move}')
                Player_2_mm[board] = next_move
                move = next_move.split(':')
                game, played = game_board(game, current_player, int(move[1]), int(move[0]))
            elif game_mode == 2 and current_player == 1: # PC vs Human
                time.sleep(0.5)
                next_move, score, board = make_dict(score, game)
                print(f'Player {current_player}2 made move {next_move}')
                Player_1_mm[board] = next_move
                move = next_move.split(':')
                game, played = game_board(game, current_player, int(move[1]), int(move[0]))
            elif game_mode == 4: # PC vs PC
                #time.sleep(0.001)
                next_move, score, board = make_dict(score, game)
                print(f'Player {current_player} made move {next_move}')
                if current_player == 1:
                    Player_1_mm[board] = next_move
                elif current_player == 2:
                    Player_2_mm[board] = next_move
                move = next_move.split(':')
                print(move)
                game, played = game_board(game, current_player, int(move[1]), int(move[0]))
            else:
                print(f"Current player: {current_player}")
                played = False
                next_move = ''
                next_move, _, board = make_dict(score, game)
                while not played:
                    space_choice = int(input(f'Player {current_player} pick a space: '))
                    next_move = moves[space_choice - 1].split(':')
                    if current_player == 1:
                        Player_1_mm[board] = moves[space_choice - 1]
                    elif current_player == 2:
                        Player_2_mm[board] = moves[space_choice - 1]
                    game, played = game_board(game, current_player, int(next_move[1]), int(next_move[0]))
                    make_dict(score, game)

            game_won = win(game)
            if game_won != 0:
                make_dict(score, game)
                score = modify_score(score, game_won, Player_1_mm, Player_2_mm)
                if g == loop -1:
                    again = input("The game is over, would you like to play again (y/n) ")
                else:
                    again = 'y'
                if again.lower() == "y":
                    print("Restarting...")
                elif again.lower() == "n":
                    with open('data.json', 'w') as fp:
                        json.dump(score, fp,  indent=4)
                    fp.close()
                    print("Saved 'Score' Goodbye!")
                    play = False
                else:
                    print("Not a valid answer, Saved 'Score' and exiting")
                    with open('data.json', 'w') as fp:
                        json.dump(score, fp,  indent=4)
                    fp.close()
                    play = False