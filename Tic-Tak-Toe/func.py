from IPython.display import clear_output
import random


''' 
    A function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
'''
def display_board(board):
    clear_output()
    for i in range(0, 9, 3):
        # print(i+1, i+2, i+3)
        print(f"  {board[i+1]}  |  {board[i+2]}  |  {board[i+3]}  ")
        if (i < 6): print(f"_____|_____|_____")           
        else: print(f"     |     |     ")


''' 
    A function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.
'''
def player_input():
    
    choice = ""
    while choice not in ['X', 'O']:
        player1 = input("Please pick a marker 'X' or 'O': ")
        choice = player1

    if player1 == 'X': return ('X', 'O')
    else: return ('O', 'X')



''' 
    A function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board
'''
def place_marker(board, marker, position):
    board[position] = marker


''' 
    A function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
'''
def win_check(board, mark):
    
    for i in range(0, 9, 3):
        # print(i+1, i+2, i+3)
        if board[i+1] == board[i+2] == board[i+3] == mark:
            # print(f"1. {i}, ({board[i]}, {board[i+1]}, {board[i+2]}")
            return True

    for i in range(1, 4, 1): 
        # print(i, i+3, i+6)     
        if board[i] == board[i+3] == board[i+6] == mark:
            # print(f"2. {i}, ({board[i]}, {board[i+3]}, {board[i+6]}")
            return True
    if board[1] == board[5] == board[9] == mark:
        # print(f"3. 1, ({board[1]}, {board[5]}, {board[9]}")
        return True
    if board[3] == board[5] == board[7] == mark:
        # print(f"4. 2, ({board[3]}, {board[5]}, {board[7]}")
        return True   

    return False


''' 
    A function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.
'''
def choose_first():
    print(random.randint(1,2))


''' 
    A function that returns a boolean indicating whether a space on the board is freely available.
'''
def space_check(board, position):
    return board[position] == ' '


''' 
    A function that checks if the board is full and returns a boolean value. True if full, False otherwise.
'''
def full_board_check(board):
    return ' ' in board


''' 
    A function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
'''
def player_choice(board):
    choice = 0
    while not choice in range(1, 10) or not space_check(board, choice):
        choice = input("Choose a number from (1-9): ")
        if (choice.isdigit()): choice = int(choice)
    return choice


''' 
    A function that asks the player if they want to play again and returns a boolean True if they do want to play again
'''
def replay():
    choice = ''
    while not choice in ['y', 'n']:
        choice = input("Would you like to play again? (y/n): ") 
    return choice