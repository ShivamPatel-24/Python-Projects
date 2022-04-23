from func import *

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = [' ']*10
    display_board(board)
    player1, player2 = player_input()

    game_on = True
    # pass

    while game_on:
        # Player 1 Turn
        choice = player_choice(board)
        place_marker(board, player1, choice)
        if win_check(board, player1):
            display_board(board)
            print("\n" + "*~"*10)
            print("\nWohoo! Player 2 won!!\n\n")
            break
        display_board(board)
        
        # Player2's turn.
        choice = player_choice(board)
        place_marker(board, player2, choice)
        if win_check(board, player2):
            display_board(board)
            print("\n" + "*~"*10)
            print("\nWohoo! Player 2 won!!\n\n")
            break
        display_board(board)
            

    if replay() == 'n':
        break