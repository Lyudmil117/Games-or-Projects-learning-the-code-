from help_ttt import draw_board, check_turn, check_for_win
#make another file and import those functions from there
# def check_turn(turn):
#     if turn % 2 == 0:
#         return '0'
#     else:
#         return 'X'
#
#
# def check_for_win(spots):
#     # check horizontal cases
#     if (spots[1] == spots[2] == spots[3]) \
#             or (spots[4] == spots[5] == spots[6]) \
#             or (spots[7] == spots[8] == spots[9]):
#         return True
#     # Now handle Vertival cases
#     elif (spots[1] == spots[4] == spots[7]) \
#             or (spots[2] == spots[5] == spots[8]) \
#             or (spots[3] == spots[6] == spots[9]):
#         return True
#     # Now diagonal cases
#     elif (spots[1] == spots[5] == spots[9]) \
#             or (spots[7] == spots[5] == spots[3]):
#         return True
#     else:
#         return False


import os
#e tuka pravq promqna

spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


playing = True
turn = 0
prev_turn = -1
complete = False

while playing:
    #Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    #Now writhe a message if Player inputs invalid input
    if prev_turn == turn:
        print("Invalid spot selection, please press another !!!")
    prev_turn = turn
    print("Player" + str((turn % 2) + 1) + "'s turn: Pick your spot  or press q to quit")

    #Get input from the player
    choise = input()
    if choise == "q":
        playing = False

    #Check if the player gave a number from 1 ot 9
    elif str.isdigit(choise) and int(choise) in spots:
        #check if the spot has already been taken
        if not spots[int(choise)] in {"X", "O"}:
            #Valid number, so update the board
            turn += 1
            spots[int(choise)] = check_turn(turn)
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False

#Out of the loop, print the results
#Draw  board one last time

os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
#here if there was a winner, say who won
if complete:
    if check_turn(turn) == "X":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")
else:
    print("There is no Winner!")

print("Thanks for playing!!!")
