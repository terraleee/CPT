#two player tic tac toe!
# i am creating a dictionary, with each key representing a box of the board, and the corresponding value being the move made by the player

gameboard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in gameboard:
    board_keys.append(key)

#this function will print a fresh board when needed throughout the game

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#this function will check the user input and monitor the general moves of the game

def tictactoe():
    print("Welcome to a two player tic tac toe! The gameboard is set up like your keyboard number pad. Good luck!")
    player = 'X'
    count = 0

    for i in range(10):
        printBoard(gameboard)
        print("Make your move player " + player + ". Choose a number from 1-9.")

        move = input()        

        if gameboard[move] == ' ':
            gameboard[move] = player
            count += 1
        else:
            print("That box is already taken. Choose a different number from 1-9.")
            continue

#in order to determine the winner, the next set of code checks 8 different conditions

        if count >= 5:
            if gameboard['7'] == gameboard['8'] == gameboard['9'] != ' ': 
                printBoard(gameboard)               
                print("Player " + player + " won!")                
                break
            elif gameboard['4'] == gameboard['5'] == gameboard['6'] != ' ': 
                printBoard(gameboard)               
                print("Player " + player + " won!")  
                break
            elif gameboard['1'] == gameboard['2'] == gameboard['3'] != ' ': 
                printBoard(gameboard)             
                print("Player " + player + " won!")  
                break
            elif gameboard['1'] == gameboard['4'] == gameboard['7'] != ' ': 
                printBoard(gameboard)              
                print("Player " + player + " won!")  
                break
            elif gameboard['2'] == gameboard['5'] == gameboard['8'] != ' ': 
                printBoard(gameboard)              
                print("Player " + player + " won!")  
                break
            elif gameboard['3'] == gameboard['6'] == gameboard['9'] != ' ': 
                printBoard(gameboard)              
                print("Player " + player + " won!")  
                break 
            elif gameboard['3'] == gameboard['5'] == gameboard['7'] != ' ': 
                printBoard(gameboard)             
                print("Player " + player + " won!")  
                break
            elif gameboard['1'] == gameboard['5'] == gameboard['9'] != ' ':
                printBoard(gameboard)               
                print("Player " + player + " won!")  
                break 

        if count == 9:               
            print("It's a Tie!!")
            break

#this is to make sure the players alternate after every move

        if player =='X':
            player = 'O'
        else:
            player = 'X'        

#at the end of the game, the players have the option to play again, or end there

    newgame = input("Do want to play a new game?")
    if newgame == "yes" or newgame == "Yes":  
        for key in board_keys:
            gameboard[key] = " "
        tictactoe()
    else: 
        print("Thanks for playing!")

if __name__ == "__main__":
    tictactoe()