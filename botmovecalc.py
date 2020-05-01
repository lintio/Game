import random
import time


def make_dict(score, game):
    board = ''
    board_moves = []
    move_score = {}
    default_score = 5

    def pick_move(score):
        aval_moves = dict.keys(score[board])
        aval_moves = list(aval_moves)
        aval_score = dict.values(score[board])
        maxIndexList = [i for i,j in enumerate(aval_score) if j==max(aval_score)] #here,i=index and j = value of that index
        try:
            next_index = random.choice(maxIndexList)
            next_move = aval_moves[next_index]
        except:
            print('No Moves Left plese enter 0 to reset game')
            next_move = ''
        return(next_move, score)

    for row in range(len(game)):
        for col in range(len(game)):
            board += str(game[row][col])

    if board in score:
        next_move, score = pick_move(score)
        return(next_move, score)
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
        return(next_move, score)
    
        

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    board = ''
    try:
        if game_map[row][column] != 0:
            for row in range(len(game)):
                for col in range(len(game)):
                    board += str(game[row][col])
            print(board, "This space has been taken, Please choode another!")
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



def init_game():
    moves = []
    game_size = 3 #int(input("What size game of tic tac toe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    for c in range(game_size):
        for r in range(game_size):
            moves.append(str(r) + ':' + str(c))
    game_won = False
    game, _ = game_board(game, just_display=True)
    return(moves, game_size, game, game_won)

moves, game_size, game, game_won = init_game()
score = {}
next_move = ''
#make_dict(score, game, game_size)

for x in range(20):
    current_player = 2
    if next_move == '':
        current_player = 1
        space_choice = int(input(f'Player {current_player} pick a space: '))
        if space_choice == 0:
            moves, game_size, game, game_won = init_game()
        else:
            move = moves[space_choice - 1].split(':')
            game, played = game_board(game, current_player, int(move[1]), int(move[0]))
            time.sleep(1)
            next_move, score = make_dict(score, game)
    else:
        print(f'Player 2 made move {next_move}')
        move = str(next_move).split(':')
        next_move = ''
        game, played = game_board(game, current_player, int(move[1]), int(move[0]))
        make_dict(score, game)
        #time.sleep(0.5)
