#Creating a function to display a pattern for the game.

def display_board(board):
      
    print(" "+board[1]+"  |  "+board[2]+"  |  "+board[3])
    print("----|"+"-----|"+"----")
    print(" "+board[4]+"  |  "+board[5]+"  |  "+board[6])
    print("----|"+"-----|"+"----")
    print(" "+board[7]+"  |  "+board[8]+"  |  "+board[9])

#Creating a function to get the player's input.

def player_input():
    marker=''
    while marker not in ['X','O']:
        marker = input("P1 :- Choose X or O: ").upper()
        if marker not in ['X','O']:
            print("Pick either X or O")
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
        print('Player1 is "X" and Player2 is "O"') 
    else:
        player2 = 'X'
        print('Player1 is "O" and Player2 is "X"') 
    return (player1,player2)

#Creating a function to take in the marker to the board. 

def place_marker(board, marker, position):
    board[position] = marker

#Creating a function for the game win/lose logic. 

def win_check(board, mark):
    return ((board[1]==board[2]==board[3]==mark) or
            (board[4]==board[5]==board[6]==mark) or
            (board[7]==board[8]==board[9]==mark) or
            (board[1]==board[4]==board[7]==mark) or
            (board[2]==board[5]==board[8]==mark) or
            (board[3]==board[6]==board[9]==mark) or
            (board[1]==board[5]==board[9]==mark) or
            (board[7]==board[5]==board[3]==mark))

#Importing Random module to randomly pick the starting player. 

import random

def choose_first():
    starting_player = random.randint(0,1)
    if starting_player == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
#Creating a function to see if the board has a space available. 

def space_check(board, position):
    
    return board[position] == ' '

#Creating a function to see if the board is full. 

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i): #calling space_check function to check the board is full or not. (i is each position of the board)
            return False         
    return True  #if board is full, True   

#Creating a function to ask the player where should the marker be placed on the board. 

def player_choice(board):
    
    position = 0 #index 0 will not be considered as board starts from index 1. 
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position): #calling space_check to see if the position is available. 
        position = int(input('Choose a position (1-9): '))
    return position

#Creating a function to ask the player if they want to replay the game. 

def replay():
    
    choice = ''
    while choice not in ['Y','N']:
        choice = input('Play again? enter Y or N: ').upper()
        if choice not in ['Y','N']:
            print("Type 'Y' for yes, 'N' for no")
    if choice == 'N':
        print("The Game has ended.")
    else:
        pass
    return choice == 'Y'

#Building the game with all the created functions. 

print('Welcome to Tic Tac Toe!')

while True:
    the_board = [' ']*10      #creating a board with empty spaces.
    p1_marker, p2_marker = player_input()    #assigning marker for each player based on input. 
    player_turn = choose_first()    
    print(f'{player_turn} will go first')
    play_game= input('Wre you ready? Y or N?').upper()
    if play_game == 'Y':
        game_on = True  #assigning a variable to keep the running. 
    else:
        print("whenever you are ready! ")
        break
    while game_on:
        if player_turn == 'Player 1': #logic for player1
            display_board(the_board)
            position = player_choice(the_board) #assigning the player choice to a variable. 
            place_marker(the_board,p1_marker,position)
            if win_check(the_board,p1_marker):
                display_board(the_board)
                print('Player 1 has won the game!')
                game_on = False  #ends the loop. 
            else:
                if full_board_check(the_board):   #logic behind Tie game
                    display_board(the_board)
                    print('Tie!')
                    game_on = False
                else:
                    player_turn = 'Player 2'
        else:   
            if player_turn == 'Player 2': #logic for player2 
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board,p2_marker,position)
                if win_check(the_board,p2_marker):
                    display_board(the_board)
                    print('Player 2 has won the game!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                       display_board(the_board)
                       print('Tie!')
                       game_on = False
                    else:
                        player_turn = 'Player 1'
    if not replay():
        break