def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f" |{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f" |{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)


#this file is used to import funkctions for the game tik tac toe. Name if the file of the game tic_tac_toe.py
def check_turn(turn):
    if turn % 2 == 0:
        return '0'
    else:
        return 'X'


def check_for_win(spots):
    # check horizontal cases
    if (spots[1] == spots[2] == spots[3]) \
            or (spots[4] == spots[5] == spots[6]) \
            or (spots[7] == spots[8] == spots[9]):
        return True
    # Now handle Vertival cases
    elif (spots[1] == spots[4] == spots[7]) \
            or (spots[2] == spots[5] == spots[8]) \
            or (spots[3] == spots[6] == spots[9]):
        return True
    # Now diagonal cases
    elif (spots[1] == spots[5] == spots[9]) \
            or (spots[7] == spots[5] == spots[3]):
        return True
    else:
        return False
