# Tic-Tac-Toe Project
# Author: Manisha Kasam
# UnitId: mkasam

# printing board status
def board(board_dict):
    items = list(board_dict.items())
    print('**********Board status**********')
    for i in range(0,9,3):
        for j in range (i, i + 3, 1):
            key, value = items[j]
            print(key +'-' + value, end =' ')
        print(end = '\n')

#X player turn
def X_turn(board_dict):
    X_pos = input('\n Player X-enter a position: ')
    if X_pos in board_dict.keys():
        if board_dict[X_pos] == 'Empty':
            board_dict[X_pos] = 'X'
        else:
            print('enetered position is not available')
            X_turn(board_dict)
    else:
        print('enetered position is not valid')
        X_turn(board_dict)
#Y player turn
def Y_turn(board_dict):
    Y_pos = input('\n Player O - enter a position: ')
    if Y_pos in board_dict.keys():
        if board_dict[Y_pos] == 'Empty':
            board_dict[Y_pos] = 'O'
        else:
            print('enetered position is not available')
            Y_turn(board_dict)
    else:
        print('enetered position is not valid')
        Y_turn(board_dict)

#check win
def check_win(board_dict):
    wins = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[3,4,5],[2,4,6],[2,5,8],[6,7,8]]
    my_list = list(board_dict.values())
    for i in range(len(wins)):
        if my_list[wins[i][0]]==my_list[wins[i][1]]==my_list[wins[i][2]]!= 'Empty':
            winner = my_list[wins[i][0]]
            print('\n')
            print(winner + ' is the winner')
            return('Win')


#check tie
def check_tie(board_dict):
    tie_list = list(board_dict.values())
    Tie = 1
    for i in range(len(tie_list)):
        if tie_list[i]!= 'Empty':
            Tie = Tie + 1
    if Tie == 10:
        print('\n')
        print("All positions are filled, it's a Tie")
        return('Tie')

# main game
# using dictionary, with keys as positions and empty values
board_dict = {'A1':'Empty','B1':'Empty','C1':'Empty','A2':'Empty','B2':'Empty','C2':'Empty','A3':'Empty','B3':'Empty','C3':'Empty'}

#print empty board
board(board_dict)
# X turn
for i in range(9):
    X_turn(board_dict)
    board(board_dict)
    status = check_win(board_dict)
    if status == 'Win':
        break;
    status_2 = check_tie(board_dict)
    if status_2 == 'Tie':
        break;
    Y_turn(board_dict)
    board(board_dict)
    status = check_win(board_dict)
    if status == 'Win':
        break;
    status_2 = check_tie(board_dict)
    if status_2 == 'Tie':
        break;
